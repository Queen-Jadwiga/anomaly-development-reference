# A-Life / Warfare source completion and remaining work

> ADR document set: **v0.1.71**. Research revisions and source/build versions below describe their original scope.

**As of 11 October 2026:** the planned consolidation using currently available sources is complete within scope. The complete CtZ-focused A-Life/Warfare section remains **partial**, because effective installed script chains are missing. Runtime status is **untested** and remains deferred until the user resumes verification.

## Completed source reference

| Area | Disposition | Entry |
| --- | --- | --- |
| Native identity, creation/registration/release | Complete within inspected paths | [Lifecycle/state reference](lifecycle-state-reference.md), ALIFE-01/02 evidence |
| Native save/load and supplied CtZ reconstruction | Complete within documented native/CtZ scope | [ALIFE-04](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md) |
| Scheduling, brains, movement and representation changes | Complete within selected native/bundled paths | [Lifecycle reference](lifecycle-state-reference.md), ALIFE-05–08 evidence |
| Scoped C++/Lua interfaces and focused contracts | Complete within recorded extraction scope | [ALIFE-09 API catalog](../../02-lua-api/alife/README.md) |
| Callback observation/readiness boundaries | Consolidated; effective dispatch still unknown | [ALIFE-10 callback reference](callback-phase-reference.md) |
| Native controls and supplied Warfare policy controls | Consolidated; active values/winners unknown | [Native controls](configuration-controls.md), [Warfare controls](../warfare/policy-controls.md) |
| Supplied package comparison and selected strategy/capture/combat | Complete package pass; effective integration partial | [WAR-002a](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md), [WAR-002b](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md) |
| Final available-source consistency audit | Bounded audit complete; not every sentence/export/configuration | [v0.1.43 verification](../../08-research/verification-2026-10-11-v0.1.43.md) |

## Required for effective-source closure

| Remaining chain | Required source/evidence | Closure boundary |
| --- | --- | --- |
| Assignment and arrival | Winning `sim_board`, `smart_terrain`, `simulation_objects`, squad overrides and dependencies | Trace assignment/unassignment, member registration, jobs, reach tests and native task/restriction handoff |
| Warfare startup and policy | Winning scripts, later replacements/listeners, applied preset and relevant option/configuration producers | Identify execution order and consumers for spawning/targeting/ownership/combat; resolve supplied-variant uncertainty |
| Death and cleanup | Winning `se_stalker`, `se_monster`, squad casualty handlers and `safe_release_manager` | Trace creature death → casualty notification → member/group cleanup → queued release; distinguish online/offline routes |
| Persistence integration | Effective global/storage wrappers and campaign/strategic serializer/restoration handlers | Establish save/load dispatch order, restored strategic state and CtZ identity reconciliation across load/level changes |

The exact export file set and priority details are in [WAR-002a's source requirements](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md). An old mod list, archive label or public default configuration does not establish the effective installation. Resolve missing chains from actual winning source and dependencies rather than substituting another version silently.

## Deferred runtime verification

After the user explicitly resumes it, identify executable/profile/build/configuration provenance, then record repeatable tests of switching positions and callback phases, assignment versus arrival, ownership, online/offline casualty cleanup, save/load/CtZ restoration and level changes. Source completion does not require performing those tests now, and documentation checks do not promote runtime status.

## Stopping rule

Close the four effective chains and reconcile their results into these references before marking the agreed section **development-reference ready at source level / runtime pending**. Exhaustive unrelated AI classes, every export/converter/build combination and a full engine manual remain optional expansions. Further work with the present snapshots can refine details, but the planned available-source consolidation is finished; it cannot replace the missing effective evidence.

Research records, previous source baselines and evidence datasets remain preserved. Later corrections should identify the changed claim and source basis explicitly. The [current roadmap](../../ROADMAP.md) tracks these requirements without presenting historical checklists as current tasks.
