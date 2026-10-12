# Spatial queries relocation and selected restriction/patrol contracts

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

- ID: WORLD-02
- Subsystem: world interaction/navigation
- Research revision: v0.1.71
- Source status: source-confirmed selected definitions/registrations/callers; effective integration partial
- Runtime status: untested; deferred
- Last reviewed: 2026-10-12

Baseline ENGINE1011 is the uploaded October 11 source archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Upstream commit and installed executable/profile correspondence remain unknown. [Ledger P01–P40](../../evidence/world/spatial-contracts-2026-10-12.csv) records archive-relative paths, raw hashes, line counts, symbols and ranges. IDs below are local to this ledger. [Focused API contracts](../../02-lua-api/world/spatial-api.md), [investigation](../../08-research/investigations/2026-10-12-WORLD-02-spatial-contracts.md).

## Lookup and location namespaces

`level.object_by_id` resolves the current client object registry, casts to CGameObject and returns its existing Lua wrapper or null. Its no-argument/nil paths log and print a stack; its general Lua-object overload casts to u16, without an additional conversion catch in the helper. This is not the persistent A-Life lookup. Live `position()` reads the client transform, while `level_vertex_id()`/`game_vertex_id()` read its AI location. Successful lookup alone does not certify completed spawn or synchronized server coordinates. ENGINE1011 `level_script.cpp:133–160,2690–2692` (P01), `script_game_object.cpp:107,163–171` and registrars (P07–P09); reuse [A-Life readiness/authority](../alife/lifecycle-state-reference.md).

Level vertices index the loaded level graph; game vertices index the game graph; patrol point indices identify vertices inside one patrol path. These inputs are not interchangeable. `level.vertex_id(position)` searches the compressed current-level X/Z column and selects its vertical candidate, rather than searching all graph points for an arbitrary nearest vertex. Invalid position/no matching column can yield u32(-1); a VERIFY precedes the explicit invalid-position return. `level.vertex_position` gives Fvector{} for an invalid ID. `vertex_link` rejects invalid source IDs but does not add an index-range guard; `vertex_in_direction` rejects an invalid start, normalizes/scales its direction and falls back to the start if its result is invalid. None is a path-success receipt. P02–P04: `level_script.cpp:344–352,412–434,1291–1308`; `level_graph.cpp:259–324`; `level_graph_inline.h:26–36`.

`get_nearby_vertices` builds a `{[level_vertex_id]=true}` table from the underlying spatial query. This wrapper does not certify the receiver's restriction eligibility. Its radius/search algorithm is not exhaustively audited here. P02.

`game_graph()` and vertex helpers refer to engine-owned graph data. `valid_vertex_id` is a count-range check. The exported raw `vertex(id)` body does pointer arithmetic without its own bounds check, so a successful conversion to a numeric argument is insufficient validation. Graph `accessible(id[,bool])` reads/writes the shared enabled mask; it is not the per-creature level restriction query. `nearest_vertex(level_name,position)` scans that level's representative level points by geometric distance and returns an ID or nil. It does not test enabled masks or route reachability. `level_neighbours(level_id)` collects other level IDs across graph edges, without an accessibility filter. P05/P06: `game_graph_script.cpp:16–121`, `game_graph_inline.h:96–132,253–270`. The bundled `dynamic_items_by_level` caller handles nil and updates item configuration fields; it is not runtime proof of reachability (P40).

## Relocation routes update different authorities

| Route | Selected source sequence | Boundary |
| --- | --- | --- |
| Simulator `teleport_object` | Lookup server object; log/return if missing; call virtual offline switch when online; change graph registration; write requested node and position; set monster next graph ID | No explicit final vertex/position consistency or accessibility validation and no online realization step in this body. Virtual/group/attachment dependencies retain A-Life limits. |
| Actor `set_actor_position` with collision skip | Write live XFORM; update existing character position; reset velocity unless keep_speed | keep_speed matters in this branch; character presence controls physics writes. No server graph transaction is shown. |
| Actor normal branch | Forward through actor ForceTransform to character physics support | Support returns for dead entities, validates transform, corrects collision position and clears velocity. Final live position can differ from the request. |
| NPC `set_npc_position` | Require CCustomMonster; invalidate detail path; destroy active animation movement control; forward ForceTransform | Support's dead gate still applies. No paired A-Life graph/member/bookmark transaction in this wrapper. |

P10–P18: signatures `script_game_object.h:294–301`; simulator wrapper `alife_simulator_script.cpp:426–430,693`; implementation `alife_update_manager.cpp:400–432`; offline virtual dispatch `alife_switch_manager.cpp:117–126`; graph change `alife_graph_registry_inline.h:22–32`; live helpers `script_game_object2.cpp:363–408`; physics support `CharacterPhysicsSupport.cpp:744–810`; actor/monster ForceTransform forwarding (P17/P18). Graph change temporarily assigns a representative point/node, then teleport overwrites them with the supplied values. It assumes `used_ai_locations()` under VERIFY. Do not infer a universal teleport recipe for actors, attached items, all groups or inactive levels from the helper name.

The bundled monster binder's dead-body branch attempts `accessible_nearest` and `set_npc_position` correction (P39). Deeper ForceTransform support declines dead entities (P16). That source request does not prove successful corpse relocation; its effective wrapper/physics behavior remains an installed/runtime question. No correction to third-party code is made here.

## Destination and patrol requests are not motion completion

Live stalker `set_dest_level_vertex_id` requires CAI_Stalker, a valid current-level vertex and restriction accessibility before updating its level destination. The game destination setter validates the game vertex but does not add the same per-level accessibility test. Wrong receiver types log; invalid/unavailable destinations return without a success bool. Manager setters store path destinations and update actuality; subsequent `update_path` can defer for disabled movement/distributed computation. P19/P20: `script_game_object3.cpp:1100–1171`, `movement_manager.cpp:131–194`.

`set_patrol_path` updates a live stalker's patrol manager parameters. The path setter can leave an identical path pointer in place; a changed pointer resets actuality/completion and manager state. Start/route changes have their own actuality rules; changing randomness alone is a different setter. This does not set movement path type or override the active planner in the inspected helper. Patrol lookup uses the storage's asserting mode here. P19/P34/P36: `patrol_path_storage_inline.h:20–29`, `patrol_path_manager_inline.h:61–108`. Existing [A-Life movement/task completion distinctions](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md) remain authoritative for offline movement.

## Restriction ownership and refresh

Live add/remove/query APIs require CCustomMonster and forward through CRestrictedObject into the level's per-client manager. Wrong-type mutations log/return; wrong-type accessibility yields false or u32(-1). Live level-vertex accessibility first rejects invalid IDs. Vector accessibility does not add that vertex-ID check. Empty add/remove string pairs return early; other changes invalidate restrictions and notify monster memory/movement. Movement invalidates path actuality, removes pending path builders and refreshes level-path restrictions. P18/P20–P24: `script_game_object_inventory_owner.cpp:1203–1337`; `restricted_object.cpp:382–444`; `space_restriction_manager.cpp:124–141,242–283`.

The manager retains base lists separately from merged defaults. `restrict` merges default in/out lists with the opposing-list exclusions and has an applied-border assertion. Clearing base lists does not prove all defaults disappear. Access requires an existing per-client entry under VERIFY; a null restriction entry returns true. A restriction that cannot finish initialization also returns true. Therefore `accessible` is a selected restriction predicate, not collision/path/arrival proof. P24/P25: `space_restriction_manager.cpp:91–104,154–199`; `space_restriction.cpp:56–108`.

`accessible_nearest` rejects an already accessible position with a diagnostic and u32(-1). Its deeper path requires restriction/border candidates, searches boundary-adjacent vertices and samples a point; assertions and explicit invalid-ID returns differ by stage. This is not a globally nearest collision-safe point search. `out_value<3>()` consumes a supplied result vector through a temporary conversion and emits a postcall vector; omission is not established. Failure before writing output is not a valid destination. P21/P22/P25/P26/P38: `space_restriction_bridge_inline.h:23–138`, `src/3rd party/luabind/out_value_policy.hpp:55–112,191–224`.

Server simulator restriction wrappers operate on creature dynamic ID lists, with object/restrictor/type checks and separate in/out cases. Add duplicate checks are DEBUG-only in the inspected implementation; remove erases a found entry and reports absence. These bodies do not directly rebuild the already-live per-client string restriction state. Live projection at spawn reads static lists plus same-level dynamic IDs; destroy removes the client entry. Selected live remove-all also sends two server events and calls the local manager's `restrict(id,"","")`, still subject to defaults. Events route through server dispatch to singleplayer A-Life-gated consumers. P11/P23/P27–P29: `alife_update_manager.cpp:434–628`, `restricted_object.cpp:27–128,262–280,412–444`, `xrServer_process_event.cpp:352–373`, `game_sv_single.cpp:271–327`.

The server creature serializer explicitly saves dynamic in/out ID lists and reads them when m_wVersion > 87. That is evidence for those fields, not automatic persistence of arbitrary live strings, default configurations or all restriction-manager caches. P30: `xrServer_Objects_ALife_Monsters.cpp:1073–1109`; [persistence](../persistence/development-reference.md).

## Patrol query failure behavior is not uniform

`level.patrol_path_exists` performs a nonasserting storage lookup. Constructing `patrol(name,...)` then requires the named path under THROW; the five registered constructor arities are real exports, unlike inferred optional arguments. CPatrolPathParams retains a borrowed path pointer. Its `point(index)` can log and fall back to the first stored patrol vertex, while level/game vertex, flag/name/terminal helpers have their own VERIFY and sentinel/fallback behavior. A nonempty path is a precondition of that point fallback; no universal safe-zero-vector fallback is certified. P02/P31–P34: `patrol_path_params.cpp:14–110`, `patrol_path_params_script.cpp:15–60`, `patrol_path_params.h:19–46`.

`index(name)` returns the named point's vertex index or u32(-1); `get_nearest(position)` searches geometric squared distance with an always-true evaluator. It is not an accessibility-filtered route selection. In contrast, the live patrol manager's selected nearest-start branch uses an accessibility evaluator. `flag(index,flag_index)` shifts a u32 bit by the supplied u8 without an added bit-index guard in this body. `terminal(index)` tests zero outgoing edges; it is not observed physical arrival. P31/P35/P37: `patrol_path_inline.h:11–45`, `patrol_path_manager.cpp:105–138`.

## Lifetime and completion boundary

Graph vertices, live wrappers and patrol paths are owner-held references, not new persistent entities. Retention across level unload/spawn/teardown needs existing lifecycle rules. SAFE_WRAP is diagnostic forwarding: the selected definition optionally logs/calls the error path, then forwards the member call; its name does not certify stale-pointer recovery, rollback or optional arguments. P09/P10: `script_game_object.h:1323–1412`.

WORLD-02 selected native/contracts pass is complete within this scope. Graph mutation masks, relocation and restriction changes still require the winning callers/configuration/planner/binder and identified executable to establish installed effects. Engine compilation and runtime remain deferred. WORLD-03 next covers use/touch, actor level transitions and marker lifecycle; broader supplied-consumer reconciliation and consolidation remain WORLD-04. [Status](source-completion-status.md), [audit](../../08-research/verification-2026-10-12-v0.1.71.md).

## Current navigation after WORLD-04

The original research scope and findings above are retained. [Supplied consumers](supplied-consumers.md), [central guide](development-reference.md), [completion status](source-completion-status.md) and [v0.1.73 bounded audit](../../08-research/verification-2026-10-12-v0.1.73.md) record the completed available-source pass and remaining effective/runtime requirements.
