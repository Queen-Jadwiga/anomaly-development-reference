# ALIFE-05 — Native scheduling, brains and offline movement

> ADR document set: **v0.1.51**. Research revisions and source/build versions below describe their original scope.

**ADR v0.1.35 · 11 October 2026 · bounded source investigation.** This traces the native scheduled-update path, individual and group brains, and their supplied Lua task boundary. All runtime verification and installed GAMMA profile reconciliation remain deferred.

## Evidence and scope

References are archive-relative paths in the supplied `xray-monolith-2026.10.11` source archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Exact upstream commit and installed executable equivalence remain unverified. The [source evidence ledger](../../evidence/alife/offline-scheduling-evidence-oct11.csv) gives full-file hashes and exact ranges S01–S21. The group and monster implementations discussed below are the `XRGAME_EXPORTS` game branches where applicable.

This is not an exhaustive online AI/combat, scheduler-threading, patrol-navigation or graph-search audit. Missing effective board/smart/creature wrappers remain the same boundary as [WAR-002](2026-10-11-WAR-002b-policy-offline-combat.md).

## Two update stages, different limits

`src/xrGame/alife_update_manager.cpp` reads `schedule_min`, `schedule_max`, `process_time`, `update_monster_factor` and `objects_per_update` from configuration (59–74, S01). `shedule_Update` returns until initialized. Its first working update runs directly; later updates can enqueue `update` in `Device.seqParallel` when `mtALife` is enabled (119–142). This identifies an execution branch, not a proof of installed threading settings or synchronization safety.

Each `update()` calls **switching first, scheduled updates second** (92–117). Switching iterates the current-level registry with a cycle counter; scheduled updates iterate the separate schedule registry. Native `switch_object` checks redundancy, synchronizes location, attempts online/offline switching, then checks redundancy again (229–247, S16). Switching may therefore change registry membership before the scheduled stage.

The schedule registry specializes `CSafeMapIterator` with `use_time_limit = false` (S02). Its update predicate allows at most `objects_per_update` entries, marking each with the current schedule cycle before invoking its virtual `update`. It does **not** call `need_update` afresh for each entry in this loop.

`safe_map_iterator_inline.h` maintains a next-entry cursor, advances it before invoking an update, wraps at the end, and stops when the predicate rejects further work (38–140, S05). Removal adjusts the saved cursor when removing that entry. Entries use an ID-ordered map; the cursor persists across calls. This is a rolling traversal, not “start from the lowest ID every tick.” The cycle guard prevents revisiting the same marked entity within one call, including when the configured count exceeds a stable population.

The registry initially defaults to one object per update, but `reload` applies the manager's configured value through its setter (S01, S04). The inspected `set_process_time` forwards a budget to the graph registry; the scheduled specialization does not use its inherited time cutoff. **Do not treat `process_time` as a wall-clock cap on every brain update.** No effective `alife.ltx` values are claimed here.

For a stable population N and positive batch size K, visiting every entry takes approximately `ceil(N/K)` scheduled calls. This is an inference from the traversal, not a guaranteed latency: additions/removals, work inside virtual Lua updates, manager cadence and parallel execution affect timing. A zero batch permits no scheduled entry updates in this predicate.

## Eligibility is not the same as membership or activity

`alife_schedule_registry.cpp` adds an entity only if it casts to `CSE_ALifeSchedulable` and its virtual `need_update(object)` accepts it (16–35, S03). Removal uses the same eligibility check to relax a missing-entry assertion. Other lifecycle paths add/remove entries explicitly.

| Entity/path | Inspected rule | Consequence |
| --- | --- | --- |
| Base schedulable | Direct control, AI locations and offline status when given a non-null object (S06) | `interactive()` is commented out in this eligibility expression. |
| Monster / inherited human eligibility | Base rule plus health greater than `EPS_L` (S07) | Dead individuals fail this admission check. |
| Online/offline group eligibility | `need_update` returns true (S08) | Eligibility does not mean it stays in the schedule while online. |
| Individual active update | `bfActive()` gates the brain (S09–S10) | Activity requires interactivity and health, or positive count for the older aggregate-group representation. |
| Group active update | Offline and nonempty members (S08) | An online group update takes a position-mirroring branch, then returns before its brain. |

Ordinary `add_online` removes schedule/graph entries and `add_offline` adds them when `update_registries` is true. The individual `try_switch_online` also repairs schedule membership according to `need_update` (S15). These are distinct from the schedule loop's predicate.

Native group `switch_online` explicitly removes the group from the schedule; `switch_offline` adds it again (270–317, S08). Therefore the always-true group eligibility must **not** be described as continuous online scheduling. The online branch exists when a group update is invoked—for example by a caller or during a transitional membership state—but this pass does not prove it runs every online frame.

When an offline member is registered into an offline native group, it is removed from individual graph/schedule processing. Unregistration resets its group ID and attempts to add it back, subject to eligibility (102–168, S08). The group is thus the normal offline movement unit for its members, rather than independently moving each member through its own scheduled brain.

## Individual monster and human brains

The active `CSE_ALifeMonsterAbstract::update` and human counterpart test activity, then call `brain().update()` (S09–S10). The monster file's old population/movement/interaction loop is inside a block comment; it is not the active update implementation.

`CALifeMonsterBrain::update` runs task selection, then either an assigned smart-terrain task or default behavior, then movement (110–193, S11):

1. Selection returns immediately if already assigned or `can_choose_alife_tasks` is false. Otherwise it is throttled by a configured smart-choice interval measured against game time.
2. It scans the smart registry, asks each smart's virtual `enabled` and `suitable`, and keeps a strictly better suitability value. A selected smart ID is stored and `register_npc` called. Actual eligibility/job policy belongs to those smart implementations.
3. An assigned smart's `task(&object)` must return a task; the brain selects game-path movement and passes that task to its detail manager. With no smart assignment, default behavior selects **NoPath**, not autonomous random roaming.

`CALifeHumanBrain` inherits this monster brain and declares no separate `update` override in its inspected header (S12). It adds an object handler and state/equipment data, but the scheduled human update here still uses the inherited task/movement flow. Do not infer a separate tactical combat loop merely from the class name.

The inspected brain's `perform_attack` returns false and `action_type` returns Ignore (76–85, S11). Together with the commented legacy interaction loop, this supports a narrow conclusion: **these active scheduled brain methods are task/movement code, not the supplied Warfare offline casualty resolver.** It does not prove all native engine combat paths are absent.

Lua exports expose monster-brain `movement`, `update` and the `can_choose_alife_tasks(bool)` setter (S20). That setter prevents new task selection; it does not, by itself, clear an existing smart assignment or stop processing its task.

## Group brain and Lua task ownership

Group native update first actualizes members. If online and nonempty, it mirrors the first member's position and vertex IDs when that member pointer is non-null. If offline and nonempty, it runs its group brain, then copies position, level/game vertices and distance into each non-null member (40–94, S08). It does not call every member's individual brain from this loop. Exceptions reaching its `catch (...)` block are swallowed; this is not a guarantee that assertions or all Lua errors are recoverable.

The group brain calls virtual `object().get_current_task()`, requires a non-null result, sets GamePath, supplies the task and updates movement (78–95, S13). Unlike the individual brain, it does not perform the smart suitability scan here.

The group's Luabind registration and wrapper macros expose virtual `update` and `get_current_task` (S18–S19). In bundled `gamedata/scripts/sim_squad_scripted.script`, the task provider resolves `assigned_target_id` through `simulation_objects`, consults the commander's job task when present, otherwise asks the target for its task; without a resolved target it returns a task at the squad's current vertices (1349–1386, S17). In the branch where a target exists but has no job, a nil target task is returned directly; there is no universal self-task fallback in that branch.

That is the source-backed division of responsibility: **Lua supplies the current task; native code advances the group along its game path.** `smart_id`, `assigned_target_id` and native individual smart ID remain separate authorities. The missing effective board/smart files still determine which task is offered in the actual GAMMA profile.

The supplied Lua `update` calls the native base first (144–146), then first-update work/refresh, a disabled gate, online-status policy and `squad_on_update`, followed by distance refresh and specific/generic target selection (209–243, S17). Thus a target change at the end of that Lua update generally feeds a later native movement invocation. This is local ordering, not a global one-frame timing guarantee; other scripts can call updates or change fields.

## Movement timing, progress and arrival

`CALifeMonsterMovementManager::update` dispatches GamePath to detail movement, PatrolPath to patrol navigation then detail movement, and NoPath to no movement (41–80, S14).

Detail movement uses elapsed **game time**, skips the first large delta when its previous timestamp is zero, and refreshes its timestamp after processing (104–117; 200–218, S21). An invalid/failed path triggers game-graph search using the entity's terrain masks. Failed search stops movement for that call; it does not itself prove permanent route failure.

`follow_path` selects current-level versus other-level speed, converts elapsed time using `normal_time_factor`, accumulates walked distance and can consume multiple graph edges in one update (220–287, S21). Crossing an edge changes graph registration and emits `on_location_change`. When processing a remaining single-node path it applies the destination level vertex and position. Switching online/offline clears the detail path; the inspected hooks do not reset its timestamp.

The detail manager's `completed()` compares game and level vertex IDs, not exact position (77–85). The higher movement manager's `actual()` and `completed()` simply return true (32–39, S14). Neither should be substituted for Lua smart-terrain `am_i_reached`, Warfare `current_action`, or a geometric arrival check. Those are different completion contracts.

The scheduler affects when accumulated movement is processed; these formulas do not make speed directly proportional to `objects_per_update`. Larger gaps can produce larger movement steps. Runtime catch-up and visual behavior remain untested.

## Warfare/CtZ implications and disposition

The supplied Lua offline-combat coordinator independently uses its own real-time cadence, eligibility, range/power abstraction and death calls, as documented in [WAR-002b](2026-10-11-WAR-002b-policy-offline-combat.md). Native scheduling/movement must not be equated with that combat calculation. Similarly, CtZ strategic destinations reach native movement through the Lua task/assignment chain; a CtZ label such as “Native/GAMMA” is not proof that native code chooses faction strategy.

This closes ALIFE-05's bounded native scheduler/brain/movement pass. No gameplay edits, configuration changes, license or runtime tests were added. Effective wrappers, installed batch/cadence values and addon overrides remain deferred.

Next independent source investigation: game-graph location changes and online spawn realization—how group/member locations turn into client spawn positions, which callbacks observe each phase, and where map/PDA position can differ from authoritative or interpolated movement state.
