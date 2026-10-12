# World interaction/navigation coverage inventory

> ADR document set: **v0.1.73**. Research revisions and source/build versions below describe their original scope.

- ID: WORLD-01
- Subsystem: world interaction/navigation
- Research revision: v0.1.70
- Record status: complete-within-scope for the inventory; subsystem partial
- Source status: scoped documentation audit of existing source-qualified records
- Runtime status: untested; deferred
- Baseline: ADR main `6ab1f93634f54ccc40dfe3fe33b716114a62157e` (v0.1.69), retaining each linked record's ENGINE1011/supplied-package provenance
- Last reviewed: 2026-10-12

This pass inventories established ADR coverage before extending it. It does not revalidate every native claim, certify new exports or establish installed behavior. [Coverage ledger](../../evidence/world/coverage-inventory-2026-10-12.csv), [investigation](../../08-research/investigations/2026-10-12-WORLD-01-existing-coverage.md), [verification](../../08-research/verification-2026-10-12-v0.1.70.md).

## Existing coverage and remaining work

| Area | Existing coverage level | Canonical reference | Increment needed |
| --- | --- | --- | --- |
| W01 — Server lookup and namespaces | selected-contract | [simulator-api](../../02-lua-api/alife/simulator-api.md) | Live lookup overloads, failed lookup and returned pointer lifetime. |
| W02 — Client lookup and readiness | boundary-only | [class-map](../../02-lua-api/alife/class-map.md) | Trace level.object_by_id definitions and exports; absence, type and readiness limits. |
| W03 — Identity across relocation and load | selected-lifecycle | [lifecycle-state-reference](../../04-game-systems/alife/lifecycle-state-reference.md) | Connect new spatial helpers to existing identity/persistence rules without recertifying them. |
| W04 — Offline graph movement | selected-behavior | [2026-10-11-ALIFE-05-offline-scheduling-brains](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md) | Extend only missing live level-graph and movement-request contracts; no exhaustive pathfinder audit. |
| W05 — Graph changes and group propagation | selected-behavior | [2026-10-11-ALIFE-06-graph-online-realization](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md) | Keep graph crossing distinct from actor level transition and installed smart arrival. |
| W06 — Arrival and task completion | selected-behavior | [lifecycle-state-reference](../../04-game-systems/alife/lifecycle-state-reference.md) | Effective reach/jobs require winning board/smart implementations; do not duplicate ALIFE-03 backlog. |
| W07 — Stored client and display position | selected-behavior | [lifecycle-state-reference](../../04-game-systems/alife/lifecycle-state-reference.md) | Trace live coordinate/vertex helper preconditions and mutation effects. |
| W08 — Relocation APIs and side effects | mixed-contract-behavior | [2026-10-11-ALIFE-06-graph-online-realization](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md) | Trace simulator teleport_object and actor relocation separately; catalog signature alone is insufficient. |
| W09 — Restriction interfaces | catalog-only | [simulator-api](../../02-lua-api/alife/simulator-api.md) | Trace add/remove ownership, accessibility, invalid inputs and refresh versus completed movement. |
| W10 — Patrol and task targets | catalog-plus-selected-movement | [server-squad-api](../../02-lua-api/alife/server-squad-api.md) | Trace live patrol lookup/parameters and caller failures; retain optional exhaustive patrol algorithms. |
| W11 — Smart assignment and jobs | effective-gap | [source-completion-status](../../04-game-systems/alife/source-completion-status.md) | Trace supplied callers only where available; keep missing effective job/restriction handoff open. |
| W12 — Map position authority | selected-behavior | [2026-10-11-ALIFE-06-graph-online-realization](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md) | Trace marker add/remove/query, identity, lifetime and serialization; position calculation is not marker lifecycle. |
| W13 — Actor level transitions | outside-reviewed-closure | [2026-10-11-ALIFE-06-graph-online-realization](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md) | Trace actor transition trigger, request, gates, destination and restoration; avoid equating squad graph changes with travel. |
| W14 — Live use and touch routing | adjacent-only | [development-reference](../../04-game-systems/inventory/development-reference.md) | Trace actor selection/use and restrictor touch entry, callbacks and object-type branches; reference item/task consumers. |

Coverage labels classify these selected ADR records. `outside-reviewed-closure` means the reviewed records do not establish that chain, not that no relevant source or mod exists. `catalog-only` records declarations/export mapping; `selected-behavior` records an already traced bounded implementation. Mixed and adjacent labels preserve the weaker edge. All rows retain effective-profile and runtime limits.

## Reuse boundary

Keep graph registry changes, offline movement and group propagation, switching/spawn/client readiness, coordinate authority and the selected map calculation in A-Life. Link their canonical investigations and original ledgers. Existing [ALIFE-05](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md), [ALIFE-06](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md), [ALIFE-07](../../08-research/investigations/2026-10-11-ALIFE-07-client-server-offline-teardown.md) and [ALIFE-08](../../08-research/investigations/2026-10-11-ALIFE-08-switching-eligibility.md) retain their scoped conclusions. Do not duplicate or normalize their evidence ledgers.

`teleport_object` is cataloged but its name/return does not establish full live/server/group relocation semantics. Restrictions and patrol exports likewise need implementation and caller tracing. A map's calculated position does not establish marker creation, removal, visibility or save restoration. A squad crossing a graph edge or reporting a changed level does not establish the actor's transition request lifecycle.

## Bounded follow-on plan

1. **WORLD-02 — spatial queries and movement requests:** live/server lookup distinction; position/level/game vertex conversions and validity; relocation helpers; selected live accessibility/restriction and patrol interfaces. Trace registrations, definitions and callers with failure/lifetime/state-update limits. Reuse existing offline pathfinding findings.
2. **WORLD-03 — interaction, actor transitions and marker lifecycle:** selected use/touch routing and callbacks; level-changer trigger/request/destination/gates; map marker add/query/remove/visibility/persistence. Link inventory, task and persistence consumers instead of retracing their completed scopes.
3. **WORLD-04 — supplied consumers, consolidation and bounded audit:** trace available Lua/configuration callers and source variants; record missing installed smart/job/transition/marker dependencies; consolidate APIs and practical guidance and verify evidence/navigation. Split this step further if independent tracing volume warrants it.

Native candidate locations found in ENGINE1011 include `src/xrGame/level_script.cpp`, `script_game_object2.cpp`, `script_game_object_script2.cpp`, `script_game_object_script3.cpp`, `space_restriction_manager.cpp`, `patrol_path_params.cpp`, `level_changer.cpp`, `Level_input.cpp`, `script_game_object_use.cpp`, `map_manager.cpp` and `map_location.cpp`. These are inspected path-presence/search targets, not newly certified APIs or completed behavior audits. Follow dependencies outside these files where the chosen chain requires them.

No new API page or runnable recipe is introduced until its contract is traced. Renderer internals, exhaustive pathfinding/AI/physics, every interactable, vehicle travel and unrelated multiplayer remain optional depth unless a concrete question requires them. [Completion status](source-completion-status.md), [roadmap](../../ROADMAP.md).
