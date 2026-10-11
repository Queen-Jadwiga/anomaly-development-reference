# ALIFE-04 — Native persistence and CtZ identity reconstruction

> ADR document set: **v0.1.41**. Research revisions and source/build versions below describe their original scope.

**ADR v0.1.34 · 11 October 2026 · bounded source investigation.** Native save/load ordering and the supplied CtZ persistence/reconciliation code are traced below. Effective GAMMA serialization wrappers, installed overrides and all engine runtime verification remain deferred.

## Baselines and evidence

Native references use archive-relative paths in the supplied `xray-monolith-2026.10.11` archive (SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`). Its exact upstream commit and equivalence to the installed executable remain unverified. The [evidence ledger](../../evidence/alife/save-load-evidence-oct11.csv) gives complete-file hashes and line ranges, labeled P01–P15.

CtZ references use `gamedata/scripts/ctz_campaign.script` at repository commit [eba6660db09353dcc42a195ae6e7e706f4762277](https://github.com/Queen-Jadwiga/capture-the-zone/tree/eba6660db09353dcc42a195ae6e7e706f4762277), the published Alpha 0.0.5j package. Its internal `VERSION = "0.0.3b"` and `SAVE_VERSION = 9` are separate code/schema labels; they do not change the package identity (P12). No mod code was changed.

## Native save contract

`src/xrGame/alife_storage_manager.cpp` has two distinct save entry points (P01):

- The packet entry calls `prepare_objects_for_save`, which calls `Level().ClientSend()` then `Level().ClientSave()`, before forwarding the save name and flag (235–250).
- The filename entry calls the optional Lua **before-save** hook, writes header, time manager, spawns, objects and registry container in that order, compresses the payload, writes its file header/data, closes the writer, then calls the optional Lua **save** hook (46–124).

The hooks are guarded by `ENGINE_LUA_ALIFE_STORAGE_MANAGER_CALLBACKS`. Their named functors are `alife_storage_manager.CALifeStorageManager_before_save` and `alife_storage_manager.CALifeStorageManager_save`. The latter runs after the native writer closes. This locates native hooks; it does not prove when the installed `save_state` dispatcher serializes CtZ's table.

`alife_object_registry.cpp` saves each eligible root with `Spawn_Write` followed by `UPDATE_Write`, then recursively saves eligible attached children (29–95, P02). Roots are skipped if `can_save()` is false, `redundant()` is true, or `ID_Parent != 0xffff`. The child recursion checks existence and `can_save`; it does not repeat the root's redundancy test. Thus being present in the registry is not, by itself, a guarantee of inclusion.

`src/xrServerEntities/xrServer_Object_Base.cpp` writes/reads the server ID, parent ID and client-data payload, and calls virtual `STATE_Write`/`STATE_Read` inside the spawn representation (P03). Saved numeric identity and serialized object state can survive; a C++ address or arbitrary Lua field does not survive merely because it existed before saving.

`alife_registry_container.cpp` persists info portions, character relations, news, specific characters, map locations, tasks and actor statistics (14–38, P04). This inspected container is not a generic serializer for every addon table.

## Native load phases and callback readiness

The filename loader validates the save, calls `unload()` and `reload(m_section)`, decompresses the payload, invokes the buffer loader, and only afterward calls `groups().on_after_game_load()` (170–232, P01).

| Phase | Source action | What is ready / still pending |
| --- | --- | --- |
| Early hook | Optional `CALifeStorageManager_load(file_name)` before reading the buffer | Native object reconstruction has not happened in this call yet. |
| Object construction | Header/time/spawns load; graph reset; object registry load; legacy spawn remap | `F_entity_Create`, `Spawn_Read`, `UPDATE_Read` make new objects and add them to the object map (P02). |
| Registry reconstruction | Disable `can_register_objects`; reserve each saved ID; verify it is unchanged; `register_object(object, false)` | Graph/schedule/story/smart/group registries and attached-item relationships are rebuilt (P05). `on_before_register` still runs; only the final `on_register` is gated. |
| Deferred registration callbacks | Load registry container; enable callbacks; loop over `on_register()` | Objects and registry-container data are present. Native group member pointers are still pending the later pass. |
| Late group repair | Return from buffer load; iterate group registry's `on_after_game_load` | Saved member IDs are resolved into live native member pointers (P06–P07). |

The buffer loader also calls the autosave manager's `on_game_loaded()` when a game level exists, before returning to the late group pass. Do not equate that native method with a particular Lua `on_game_load` dispatch without its wrapper evidence.

Native group `STATE_Write` saves member IDs; `STATE_Read` inserts those IDs with null pointer values (2269–2297, P08). Late repair copies the IDs, clears the member map, and calls `register_member` for each. That method resolves a monster, verifies it is alive, handles graph/schedule or online membership, sets its group ID and inserts its pointer (102–145, P07).

**Consequence:** an `on_register` listener may find a squad object and its saved member IDs without having fully reconstructed native member pointers. Registration completion is a phase boundary, not proof that every downstream squad operation is ready. This is a source-order conclusion, not a reproduced runtime failure.

## Identity across load, switching and release

| Operation | Identity consequence in inspected source |
| --- | --- |
| Load an included object | A newly constructed object receives its saved numeric ID; the loader requests that ID and verifies equality. Old native pointers are not durable handles. |
| Remove online representation | `remove_online` destroys the network representation, requests the object's previous ID again, then calls `add_offline` (74–103, P09). This is not permanent entity loss. |
| Permanent release | Native `release` recursively handles children, unregisters the object, clears ALife control and may destroy it; `entity_Destroy` removes network lookup and frees its ID (P10, P15). |
| Later allocation | The generator accepts a requested available ID, rejects an already-used request, and returns freed IDs to its pool (59–125, P11). A numeric ID is not a lifetime-unique generation token. |

See [ALIFE-01](2026-10-11-ALIFE-01-identity-lifecycle.md) and [ALIFE-02](2026-10-11-ALIFE-02-creation-registration-release.md) for the wider online/offline and destroy-route distinctions. Neither a temporary lookup failure nor preservation of an ID proves death or lifetime continuity respectively.

The level-change path in `alife_update_manager.cpp` is also explicitly a persistence boundary (159–240, P13): send client updates, retain the actor's old location, set the destination location, save client data, update holder location if applicable, save an autosave, then restore the actor/holder's old location. This explains which actor location is captured in that save; the complete destination startup and installed Lua callback sequence are outside this pass.

## CtZ campaign state versus squad state

CtZ `save_state(m_data)` assigns `m_data.ctz_state = state` and a schema label. `load_state` restores that table or creates an initial state, fills selected missing fields, preserves older siege origins as `native`, normalizes fort anchors and movement fields, recounts forts and stamps the current labels (3209–3261, P12). The inspected loader does not branch on the saved version label to reject incompatible future schemas. Assignment into `m_data` establishes a callback contract; the missing installed storage wrapper still determines actual encoding and dispatch timing.

The bundled engine `sim_squad_scripted.script` uses active packet `STATE_Write`/`STATE_Read` to persist five Lua values: current target ID, respawn point ID, respawn property section, smart ID and scripted target (925–999, P14). Numeric fields are converted back with `tonumber`; scripted target remains a string unless it is `"nil"`. The older `save_state`/`load_state` functions immediately above are inside a block comment (899–923). They must not be cited as active persistence. This packet serializer does not list CtZ ownership markers or its membership signature; it does not establish a generic arbitrary-field save contract.

CtZ instead reapplies `ctz_campaign_owned`, faction, detachment and role markers with `mark_owned` (349–355, P12). `restore_loaded_squads` looks up each `det.squad_id` through `alife():object(id)`, marks the result, fills missing expected/requested counts, and calls member setup only when its member-ID signature changes (649–652; 1418–1436). The signature is a repair trigger, not an identity generation check.

`on_game_load` resets readiness/transition timers and quarantines target fields. It does not call `setup_members` there. Later first/update handlers apply readiness and transition-grace gates before restoration/validation (3277–3288; 3430–3490). These are observable code safeguards; their comments about destination realization are not independent proof of installed callback ordering.

## Reconciliation limits and source-derived risks

`get_squad` is a numeric lookup without a class, faction, detachment or generation validation. Restoration reapplies markers to a non-nil lookup result. `reclaim_core_members` similarly resolves saved `spawn_member_ids`, checks available alive/group information, and can unregister a member from another group before attempting registration into the campaign squad (1542–1586, P12).

**Source-derived risk, not a confirmed bug:** if an ID outlives permanent release in campaign data and is later reused, these lookup paths can reconnect a saved strategic record to a different entity. The inspected paths contain no generation comparison. The native generator proves reuse is possible, not that this occurs in a particular session or that every persisted detachment suffers it.

Loss accounting deliberately ignores a `MISSING` snapshot and otherwise subtracts drops from `accounted_alive` (1588–1609). The missing-squad branch normally waits for a game-time confirmation window for garrison/movement detachments, but has an earlier field-engagement loss exception when a live opposing movement detachment remains (2602–2647). The death callback logs observation instead of decrementing strength again (3264–3275). Therefore the confirmation delay is not an unconditional rule.

CtZ fort ownership in its campaign table and Warfare ownership are separate persistence authorities. Restoring the CtZ table/recounting forts is not proof of successful synchronization to effective smart-terrain/Warfare state. See [WAR-002b](2026-10-11-WAR-002b-policy-offline-combat.md).

## Disposition and next source work

ALIFE-04's native ordering and supplied CtZ identity/reconciliation pass is complete within this scope. Full effective-profile persistence remains open: installed `alife_storage_manager` serializer/dispatch, global callbacks, squad/creature overrides, safe release and board/smart policy. No PC access is needed to retain these findings; that reconciliation and all runtime tests remain deferred.

Next independent source task: native offline scheduling and squad/monster brain updates—eligibility, update order, movement/task ownership, and what native simulation does versus the supplied Lua offline-combat coordinator. Potential generation guards or schema migrations are design questions for later mod work, not changes made here.
