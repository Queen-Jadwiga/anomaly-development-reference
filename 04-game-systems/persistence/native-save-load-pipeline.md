# Native save/load pipeline and Lua extension boundaries

> ADR document set: **v0.1.59**. Research revisions and source/build versions below describe their original scope.

- ID: PER-01
- Source status: source-confirmed within selected single-player A-Life paths
- Runtime status: untested; deferred until explicitly resumed by the user
- Last reviewed: 2026-10-11

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee` pins this source. Exact upstream commit, installed executable/build and effective scripts remain unknown. S01–S24 refer only to the [PER-01 ledger](../../evidence/persistence/native-pipeline-2026-10-11.csv). This maps the selected A-Life `.scop` path, not every engine save function or a binary compatibility specification.

Read with [ALIFE-04 identity/reconstruction](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md), [A-Life callback phases](../alife/callback-phase-reference.md), [faction persistence](../factions/relation-persistence.md) and [extension contracts](../../02-lua-api/persistence/native-extension-contracts.md).

## Requests are not completed persistence

Server `M_SAVE_GAME` routes to the game-state handler; single-player delegates to A-Life `save(NET_Packet&)` when a simulator exists. That packet entry prepares live state with `ClientSend()` then `ClientSave()`, reads the requested name/update-name flag and calls the filename save implementation. A direct filename save call does not contain that preparation step. S01/S05/S06.

Server `M_LOAD_GAME` routes to `game_sv_Single::load_game`, which reads the name and calls `CALifeUpdateManager::load_game`. That latter function checks file existence and edits server command options, returning success for that request stage; it does not read/decompress/reconstruct the saved objects. Server then broadcasts the message. S05/S06/S24.

In the selected client route, same-level metadata can defer `Game:QuickLoad`; other cases reconnect. The quick-load event removes client objects and calls `restart_simulator`, which deletes the old simulator, clears server IDs, sets load parameters and constructs a replacement. This is distinct from the storage-manager reconstruction below. Full reconnect/constructor routing and every entry source are outside this pass. S06/S22/S23.

## Three representations in a save

| Layer | Producer → consumer | What is retained |
| --- | --- | --- |
| Live update packet | Client export → server `UPDATE_Read` | Selected current native server fields; not arbitrary script tables |
| Live custom-save packet | Relevant client `net_Save` → server `load(NET_Packet&)` | Object-framed native/binder bytes held as server `client_data` in the selected base path |
| Native A-Life file | Server object packets + auxiliary serializers → compressed `.scop` | Selected persistent server fields, retained custom bytes and explicitly serialized registries |

S01/S07–S10/S15/S21. The custom packet's server method named `load` is a packet-import operation, not the same API as loading a saved campaign from disk.

`ClientSave` includes valid, non-destroying game objects whose `net_SaveRelevant()` allows it. It frames ID and length, writes native object save data followed by binder save data, and sends `M_SAVE_PACKET` batches. Update and save readers use different packet-size widths. Server `Process_save` skips missing IDs and logs/seeks to the advertised boundary on a consumption mismatch. This does not certify a valid addon schema or undo partially consumed/mutated state. S07/S08/S15/S16.

`CLevel::Send` has an inspected direct-connect branch calling server `OnMessage` immediately. Other transport modes are separate; invoking preparation does not establish a universal network acknowledgement, fresh-every-object or multi-file atomic-save guarantee. No observed timing is asserted. S07; [ALIFE-07 synchronization limits](../../08-research/investigations/2026-10-11-ALIFE-07-client-server-offline-teardown.md).

## Native file framing and payload

The selected writer resolves `$game_saves$` plus `.scop`, writes three `u32` fields—sentinel `0xffffffff`, `ALIFE_VERSION`, uncompressed byte count—then the compressed memory payload. This snapshot defines `ALIFE_VERSION=0x0006`. These are format constants, not ADR revision or proof that a particular executable matches the archive. S01/S03.

| Payload write order | Chunk ID / selected contents | Evidence |
| --- | --- | --- |
| Header | `0x0000`: inner A-Life version | S02/S03 |
| Time | `0x0005`: game time, time factor, normal time factor | S03/S11 |
| Spawn registry | `0x0001`: saved spawn name/GUID, optional current level metadata, spawn updates | S03/S12 |
| Objects | `0x0002`: object count, framed spawn/update packets | S03/S09 |
| Auxiliary registries | `0x0009`: info portions, relations, news, specific characters, map locations, tasks, actor statistics | S03/S10 |

Write order is not numeric chunk order. The file does not embed every external spawn/configuration dependency. Spawn load opens the named external `.spawn` and passes the saved GUID into its loader; deeper pack/legacy remapping is retained in ALIFE-04 rather than treated as an unrestricted migration promise. S12.

Object save selects saveable, non-redundant root entries and recursively visits qualifying children. It writes `Spawn_Write(...,TRUE)` and `UPDATE_Write`, not a dump of every C++/Lua object in memory. Loading instantiates the recorded section, reads spawn/update packets and inserts reconstructed server objects; an unavailable factory section can be skipped in the selected function. This is not proof that a changed mod set preserves every object/reference. S09.

## Validation and disk-load phases

`valid_saved_game(IReader&)` checks minimum length 8, the sentinel and an outer version **at least** `ALIFE_VERSION`. It consumes those first two words. It does not inspect the decompressed payload or establish a checksum/whole-save validation in this predicate. Inner header loading also requires a version at least the constant. Passing those comparisons does not certify forward compatibility, matching addons or safe malformed-file handling. S02/S04.

The storage filename loader returns false when the file cannot open, validates through that predicate, unloads/reloads simulator storage, reads the advertised uncompressed size and decompresses the remaining bytes. It then invokes buffer reconstruction. Assertions and deeper failures are not converted into a universal graceful false result. The selected write body writes directly to its resolved path; no temp-file rename transaction or native Lua companion-file commit is established by that body. S01.

Buffer reconstruction runs in this order:

1. Optional named Lua load functor, before reading native chunks.
2. Header/time/spawn, graph load hook, object load and legacy remap.
3. Native object ID reservation and registry insertion with final registration callbacks disabled.
4. Auxiliary registry restoration, then enabled final `on_register` loop.
5. Native autosave-manager notification when a level exists.

After the buffer function returns, the filename loader calls group `on_after_game_load`, repairs member pointers through member registration and verifies actor graph presence before returning true. Thus the final native registration callbacks can precede late native group repair. No phase here proves order of installed Lua load/save dispatch or completion of every client spawn. S01/S13/S14; ALIFE-04/callback reference.

## Lua extension points have different contracts

| Extension | Selected phase | Important limit |
| --- | --- | --- |
| `CALifeStorageManager_before_save(name)` | Before native memory serialization | Packet entry has prepared live state earlier; direct filename entry differs |
| `CALifeStorageManager_save(name)` | After native writer closes | Does not establish atomicity/durability of script companion storage |
| `CALifeStorageManager_load(file_name)` | Before native buffer reads, after file validation/decompression in filename path | Reconstructed objects and registries are not ready in this function yet |
| Binder `save(NET_Packet*)` | After native client object save in custom-data packet | Requires a bound object and save relevance; explicit serialization only |
| Binder `load(IReader*)` | During selected live object's spawn from retained custom bytes | Not whole-world readiness or the native disk-load hook |

S01/S15–S20. Named storage hooks are conditional on `ENGINE_LUA_ALIFE_STORAGE_MANAGER_CALLBACKS`; the supplied define file enables it, but actual binary/build and installed functors remain unverified. Binder virtual Lua methods are registered as `object_binder` extensions. Default native binder methods save/load nothing and return false for relevance. The selected binder dispatcher catches exceptions and clears the binder; a native save continuing is not proof that every addon serialized successfully. S16–S20.

Live reconstruction reloads/reinitializes the binder before passing nonempty server `client_data` into `net_Load`; native then binder load occurs during base spawn, before later derived/outer completion. Cross-object work must use an independently established observation phase. S15; [ALIFE-06](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md).

## Development boundaries and next work

For persistent CtZ data, identify which explicit serializer owns each field, its identity/schema and the phase at which dependencies are restored. Neither arbitrary Lua tables nor runtime callbacks automatically enter the native file. Save names are path inputs, not a demonstrated campaign fingerprint. Native auxiliary relation storage and dynamic script matrix reapplication remain different domains. [Faction reference](../factions/development-reference.md).

PER-01 completes this selected native pipeline/extension map. Next: supplied Lua storage helper contracts and active-profile gaps, then CtZ campaign identity/reconciliation, practical consolidation and final available-source audit. Runtime remains deferred; no gameplay or save files are modified.
