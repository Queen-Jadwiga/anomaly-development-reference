# ALIFE-06 — Graph location, online realization and spawn callbacks

> ADR document set: **v0.1.46**. Research revisions and source/build versions below describe their original scope.

**ADR v0.1.36 · 11 October 2026 · bounded source investigation.** This follows game-graph location changes into online member spawns, distinguishes stored/client/map positions, and establishes the inspected callback phases. Effective GAMMA overrides and all runtime verification remain deferred.

## Evidence baseline

References use archive-relative paths in the supplied `xray-monolith-2026.10.11` archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Exact upstream commit and installed executable equivalence remain unverified. The [27-file evidence ledger](../../evidence/alife/graph-online-realization-evidence-oct11.csv) records full-file hashes and exact ranges G01–G27. Game-build, DEBUG and feature-macro branches are distinguished below; no installed build settings are inferred.

Previous context: [ALIFE-05 scheduling and brains](2026-10-11-ALIFE-05-offline-scheduling-brains.md), [ALIFE-04 load reconstruction](2026-10-11-ALIFE-04-save-load-identity.md), and [ALIFE-02 creation/release](2026-10-11-ALIFE-02-creation-registration-release.md). This pass does not audit every creature class, physics transform, transport path or map marker override.

## Graph change is a discrete location change

`src/xrGame/alife_graph_registry_inline.h:22–32` removes the entity from the old graph point, adds it to the new point, sets the game vertex ID, then replaces its stored position and level vertex with that game vertex's representative `level_point` and `level_vertex_id` (G01). Registry add/remove also maintains the current-level registry when requested (G02). A game-graph change is therefore more than changing an ID, and is not a continuous geometric movement operation.

The offline detail path accumulates distance between game vertices. At an edge crossing it calls `graph().change`, then `object().on_location_change`; at a final one-node path it sets the exact destination position/level vertex (228–287, G03). Its draw helper can interpolate along a same-level graph edge; across levels it returns stored position instead (299–320). Stored position and interpolated display position can differ during travel.

Native group update advances the group brain, then copies the group's position, game/level vertices and distance to each non-null member (55–94, G04). The edge callback occurs inside movement **before** that subsequent member-copy loop. Group `on_location_change` calls its brain hook; the inspected group/monster brain location hooks are empty (G06–G07). Do not treat this hook as a verified Lua faction-capture notification.

The supplied Lua squad update calls the native base first, then later compares its final game vertex/level to cached values and emits `squad_on_after_game_vertex_change` followed, if needed, by `squad_on_after_level_change` (144–146; 239–247, G25). The caches are updated after each callback. These are sampled old-to-final changes: multiple native graph edges in one movement update need not produce one Lua event per edge. Earlier disabled/error paths can also prevent reaching this code.

## Position helpers do not all preserve the requested coordinates

| Path | Inspected behavior |
| --- | --- |
| Group `force_change_position` | Sets requested position and nearest level vertex; if the cross-table game vertex differs, calls graph change, which overwrites them with the representative graph point (399–411, G04). No explicit restoration follows. |
| Individual `synchronize_location` | Derives a level/game vertex from position. Offline graph change may restore the saved position, but the inspected code assigns the reset node ID into a local variable rather than restoring the original node into the object (93–130, G05). |
| Online group synchronization | Copies the first member's stored server position, vertices and distance when its pointer is non-null (183–198, G04). This is not a direct read of a client object's transform. |
| Lua `set_npc_position` | Calls `SetNpcPosition`, invalidates online detail movement and forces a `CCustomMonster` transform (392–408, G24). This function is not a native ALife graph-change transaction. |

The first two rows are literal source observations, not reproduced bugs. Do not silently rewrite their assignments in the reference or assume all related fields stay synchronized. The bundled squad `set_squad_position` separately records per-member bookmark vertices and handles client/server member positions (824–845, G25), illustrating that moving a container and moving its members are distinct operations.

## Online switching realizes members, not the squad container

Native group `switch_online` sets its online flag, iterates members and calls `alife().add_online(member, false)` for members still offline, then removes the group from scheduled/offline graph processing (270–285, G04). It does not call `Process_spawn` for the group container in this function. The false flag suppresses ordinary per-member registry updates, keeping the group-managed representation distinction.

`CALifeSwitchManager::add_online` (47–71, G08) verifies the current level, sets the member online, removes its old server network entry with `entity_Destroy`, sets `M_SPAWN_UPDATE`, passes the existing ALife entity to `Process_spawn`, clears the flag, then calls `object->add_online(update_registries)`. The server entity remains under ALife control; this is realization of an existing entity, not the full fresh-creation lifecycle.

`xrServer_process_spawn.cpp` reserves/inserts its network ID, calls `PerformRP`, writes spawn/update packets and sends them (G09). Its `OnPreCreate`, `OnCreate`, parent-touch and `OnPostCreate` actions are guarded by the **new entity** path and do not run for this existing-entity switch. `PerformRP`'s old respawn-point selection body is commented out; its inspected active body returns true without changing coordinates (G10).

The packet writes `o_Position` and angles, and the receiver reads them into a temporary server-description object (G11). **No inspected switch path substitutes `draw_level_position()` for `o_Position` when building that packet.** An interpolated offline map marker is therefore not proof of the eventual online spawn coordinate. Other code can change position before or after this chain.

## Server online is not proof of client readiness

The normal `M_SPAWN` receive branch inserts the packet into `game_events`; it may invoke processing immediately in the debug-events mode (88–105, G12). `ProcessGameEvents` later invokes `cl_Process_Spawn`, or can divert eligible spawns through prefetch when the `SPAWN_ANTIFREEZE` build/runtime/boot gates apply (G13).

The postponed route checks whether a previously present ALife entity still exists and is online, and checks parent presence/online status before realization; a bolt exception bypasses these checks (636–706, G13). This is source evidence for delayed or skipped realization, not a guarantee about the active GAMMA configuration or cross-object ordering.

`cl_Process_Spawn` creates a temporary entity description, reads spawn/update state, checks configuration, calls `g_sv_Spawn`, and destroys the description afterward (13–51, G14). `g_sv_Spawn` creates a client `CObject` and calls its full virtual `net_Spawn(E)`. Server flag, network-map presence and client `level.object_by_id` availability are separate phases. A callback on one member does not establish that every member has completed spawning.

## Client spawn and callback phases

`CGameObject::net_Spawn` sets ID and transform from the packet, marks/registers the client object, reloads/reinitializes the binder, loads client data, establishes/validates AI locations, may adjust Y to the AI plane, calls inherited spawn and creates supplies, then reaches the script spawn phase (267–481, G15).

| Phase | Inspected ordering / readiness limit |
| --- | --- |
| Generic `game_object_on_net_spawn` | The non-DEBUG branch calls `_G.CGameObject_NetSpawn` **before** `CScriptBinder::net_Spawn`. The supplied wrapper dispatches the named callback (G17). The DEBUG branch omits this functor call in this function. |
| Binder `net_spawn` | `CScriptBinder` invokes its bound object's method for an ALife description; absent binder or caught exception falls through to true (134–164, G16). Success alone does not prove all addon initialization ran. |
| Monster `monster_on_net_spawn` | Supplied `bind_monster` emits this before `db.add_obj`, enemy/logic setup and cached-position correction (295–350, G18). It is an early binder notification. |
| Derived native completion | Work can continue after base GameObject/binder spawn. `CCustomMonster` establishes movement destinations and other resources; stalker spawn performs animation/rank/sight setup after its inherited call (G26–G27). |
| Queued client-spawn-manager callbacks | `g_sv_Spawn` invokes these only after the full virtual spawn returns success, when not dedicated (G14, G20). This is separate from generic/binder callbacks. |
| `callback.net_spawn_after` | Under `NET_SPAWN_AFTER_CALLBACKS`, the outer level function emits it after spawn-manager callbacks, player-entity setup and parent ownership event handling (162–187, G14). It requires a listener bound to that object's callback. |

The `net_spawn_after` binder code in `callbacks_gameobject.script:60–80` is a **commented example**, not an automatically installed listener. Its phase is supported by native emission, not by the example's execution. Likewise, callback names do not establish listener priority; installed dispatch and registrations remain separate evidence.

The spawn manager also calls a newly added callback **immediately** if its target client object is already found (46–73, G20). Client registration occurs partway through base spawn, so this add-time path does not promise the same readiness as an already queued callback delivered by the outer spawn function. The map of queued callbacks is iterated and cleared afterward; this pass does not establish safety for listeners that mutate that registry while it is iterated.

## Cached positions can override native progress

For a living monster, the supplied binder first sets up smart/logic state, then prefers `db.offline_objects[id].level_vertex_id` over `db.spawned_vertex_by_id[id]`, clears the chosen cache and calls `set_npc_position` (334–347, G18). Its dead-body branch has different corrections and returns earlier. On destruction it emits `monster_on_net_destroy` before writing the last client level vertex/active section into an existing offline record (353–378).

Bundled `aaaa_script_fixes_mp.script` defines and calls a startup fix that wraps both motivator and monster `net_destroy` methods, calls the original, then clears the bookmark for recognized squad members (1283–1306; 1606–1649, G19). The monster wrapper uses the server group ID; the stalker wrapper uses `self.squad`. The supplied archive does not include `xr_motivator.script`, so that original stalker implementation is not reconstructed here.

**Scoped conclusion:** the unpatched monster binder can reapply an older online bookmark after native offline movement; the supplied patch explicitly clears that bookmark for recognized squad members. This is not proof of an installed defect or of installed protection. Startup execution, prerequisites, wrapper replacement order and winning binder files remain unverified. The fix does not clear every independent spawn-position cache.

## Map/PDA position authority

`CMapLocation::CalcPosition` uses the current actor for actor-relative markers; otherwise it uses a matching client object's `Position()` if present, or the server object's `draw_level_position()` if no client is found (276–299, G21). Base ALife draw position returns stored position (G23). A monster with a brain delegates to detail-path interpolation; without a brain it returns stored position (G22–G03).

Thus the map can change its position source as the client object becomes registered, even before full spawn completion. The group container's stored position and individual member interpolation also must not be conflated. This establishes the inspected native map calculation; CtZ/custom map overrides and visual discontinuities remain untested.

## Disposition and next source work

ALIFE-06's graph-to-client realization and position/callback ordering pass is complete within this scope. No gameplay code, configuration, research conclusions from earlier files or license were changed. Effective profile reconciliation and runtime checks remain deferred.

Next independent native source topic: online client-to-server synchronization and offline teardown—when a moving NPC's transform reaches its ALife entity, which state is retained on switching offline, and how destruction callbacks, client-data snapshots and bookmark writes are ordered. That closes the return path of the position-authority chain without requiring PC access.
