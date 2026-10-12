# Supplied Lua codec and storage caller contracts

> ADR document set: **v0.1.80**. Research revisions and source/build versions below describe their original scope.

- ID: PER-02-API
- Subsystem: persistence
- Owners: supplied native `marshal` module; selected script callbacks and missing manager/global helpers
- Interface kind: native module functions, supplied script callbacks, caller-only dependency contracts
- Baselines: ENGINE1011, BETA150 main, CTZ005J pinned in the [reference](../../04-game-systems/persistence/lua-storage-contracts.md)
- Source status: source-confirmed for inspected implementations; scoped-source-audit for absent definitions
- Runtime status: untested; deferred until explicitly resumed by the user
- Build/conditional scope: inspected extension initialization and package modes; installed executable/winners unknown
- Native versus registered Lua inheritance: codec has no mapped game-object ownership API; script receiver contracts are caller-specific
- Example status: none
- Last reviewed: 2026-10-11

Evidence labels L01–L13 are local to the [PER-02 ledger](../../evidence/persistence/lua-storage-2026-10-11.csv).

## Implemented codec functions

| Lua interface | Selected input/output behavior | Scope / error |
| --- | --- | --- |
| `marshal.encode(value[,permanents])` | Returns binary string; omitted value becomes nil; absent/nil second argument uses empty table | Non-table second argument errors; unsupported encode types/custom persist failures error |
| `marshal.decode(bytes[,permanents])` | Reads binary string via luaL_checklstring; returns decoded value | Empty/bad-magic/error paths exist; second argument must be table or absent/nil; complete malformed-data behavior unaudited |
| `marshal.clone(value[,permanents])` | Selected body encodes then decodes with the supplied argument context | Not a universal game-object clone or certified cross-build deep-copy operation |

L01–L05. Preseeded permanent references must correspond between encoding and decoding. Ordinary tables use recursive key/value serialization and reference IDs; `lua_next` ordering is not a stable sorted format. Numbers and bytecode are native representation-dependent; no application schema/campaign pin is embedded by these functions. L01–L03.

Lua functions serialize dumped bytecode/upvalues; unlisted C functions error. Table/userdata `__persist` must return a function, and decoder calls reconstruction functions. Userdata without a hook errors in the selected encoder. Persisting supported userdata does not establish validity of a live game object after teardown/load. No ownership transfer or durable native pointer is promised. Full custom metatable/cycle, CTime, converter and portability policy remains open.

The codec operates on values/strings; file names, companion storage and save/load listener orchestration belong to missing effective wrappers. [Storage reference](../../04-game-systems/persistence/lua-storage-contracts.md).

## Supplied callback consumers

| Interface | Observed argument/state operation | Lifetime and missing guarantee |
| --- | --- | --- |
| Engine generic binder `save_state(m_data)` / `load_state()` | Manager object-state fields and transferred pstor tables | Manager ownership/defaults/creation and emitter order missing; mode differs from packet serialization |
| BETA150 Warfare `save_state(m_data)` / `load_state(m_data)` | Namespace/table attachments and selected ID maps; load clears m_data.warfare | Shared referenced tables can alias; no immutable snapshot/encoded-file promise |
| CtZ `save_state(m_data)` / `load_state(m_data)` | Attach/read ctz_state and save-version fields | Direct table attachment, not proved deep copy or campaign fingerprint |
| BETA150 `pstor_save_all(obj,packet)` / `pstor_load_all(obj,reader)` | Non-Marshal tagged scalar sequence plus separate CTime sequence; Marshal delegates callbacks | Requires appropriate db.storage/packet order and effective helper implementation; unsupported type branch is not a safe round-trip contract |

L07/L09/L10/L13. Shared callback invocation forwards table arguments; its inspected body has no listener-isolating local pcall/table snapshot. Later listeners can observe mutations by earlier ones. Exact effective ordering/emitter and encode timing remain unknown. L06.

## Dependencies whose implementations are absent

`get_state()`, `get_game_object_state(obj[,true])`, `get_se_obj_state(se_obj,true)` and global `save_var(actor,key,value)` / `load_var(actor,key,default)` are **observed call shapes**, not complete implemented API contracts in these snapshots. Return ownership, allocation, default/type/schema rules and storage paths must be read from winning definitions. The scoped search and required source set are recorded in [PER-02](../../08-research/investigations/2026-10-11-PER-02-lua-storage.md).

Neither a registered save callback nor successful encoding certifies native/companion-file atomicity, actual durable persistence, all objects restored or campaign/ID reconciliation. Use [PER-01 phases](native-extension-contracts.md) and defer runtime checks.

## Checks

Read codec registration/input/type/reference/error paths and selected consumer call/alias/consume behavior. Verify snapshot hashes/counts/ranges/symbols and CtZ committed blob identity. No engine build, execution tests, gameplay/save edits or source redistribution. [Verification](../../08-research/verification-2026-10-11-v0.1.51.md).
