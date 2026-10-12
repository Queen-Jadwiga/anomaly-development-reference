# World interaction/navigation development reference

> ADR document set: **v0.1.70**. Research revisions and source/build versions below describe their original scope.

- ID: WORLD-01-GUIDE
- Subsystem: world interaction/navigation
- Reference revision: v0.1.70 coverage synthesis; native extension pending
- Source status: linked selected source findings plus scoped documentation inventory
- Runtime status: untested; deferred
- Baseline: ADR v0.1.69 inventory; original ENGINE1011/supplied-package limits retained
- Last reviewed: 2026-10-12

The [coverage inventory](coverage-inventory.md) is the starting point. WORLD-01 is complete within its inventory scope; the world subsystem is **partial**. This guide organizes existing knowledge and the next source questions, with no newly certified API recipes.

## Choose the authority and operation

| Development question | Existing guidance | Remaining distinction |
| --- | --- | --- |
| Which object and position should I query? | [A-Life lifecycle/state](../alife/lifecycle-state-reference.md), [lookup catalog](../../02-lua-api/alife/simulator-api.md) | Server identity, live client availability, sampled coordinates and display interpolation differ; live query implementation remains to trace. |
| Has a squad arrived? | [Offline brains/movement](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md) | Movement/detail completion, smart reach and strategic capture differ. Effective board/jobs remain missing. |
| What does relocation update? | [Selected position helpers](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md), [server/squad catalog](../../02-lua-api/alife/server-squad-api.md) | Requested point, representative graph point, member propagation and live transform are separate; actor/simulator routes still need tracing. |
| Is a route usable? | [Task/movement controls](../../02-lua-api/alife/server-squad-api.md) | Cataloged restriction/patrol controls do not establish active accessibility or successful movement. |
| Does a marker show the authoritative position? | [Map position authority](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md) | Position source and marker creation/lifetime/visibility/restoration need separate evidence. |
| Can use/touch or a level changer change state? | [Inventory](../inventory/development-reference.md), [tasks](../tasks/development-reference.md), [persistence](../persistence/development-reference.md) | These consumer references do not replace a general actor-use/touch/transition dispatch trace. |

For new logic, identify the representation, location namespace and phase before choosing a helper. Reacquire live references across spawn/load/teardown under existing lifetime rules. Treat a movement request, eligible vertex, registered marker and completed action as separate observations until their connecting callers are traced. These are source-derived review questions, not runtime guarantees.

## Continue research

WORLD-02 next traces spatial lookup/conversion/relocation and selected restriction/patrol contracts. WORLD-03 covers use/touch, actor level transitions and map marker lifecycle; WORLD-04 covers supplied consumers, consolidation and audit. [Scope and gaps](source-completion-status.md), [inventory](coverage-inventory.md), [roadmap](../../ROADMAP.md).
