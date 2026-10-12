# World interaction/navigation completion status

> ADR document set: **v0.1.81**. Research revisions and source/build versions below describe their original scope.

**As of 12 October 2026:** WORLD-01–04 planned available-source inventory/traces/consumers/consolidation and bounded audit are **complete within selected scope**. Effective installed integration remains **partial**; independent runtime is **untested/deferred**. [Central guide](development-reference.md), [audit](../../08-research/verification-2026-10-12-v0.1.73.md).

## Completed selected source work

- [WORLD-01 inventory](coverage-inventory.md): 14 pinned document coverage rows; canonical A-Life graph/offline/realization reuse.
- [WORLD-02 spatial contracts](spatial-queries-relocation.md): lookup/coordinates/relocation, selected requests/restrictions/patrols and focused APIs.
- [WORLD-03 interaction/travel/markers](interaction-transitions-markers.md): selected use/touch ordering, actor travel/save/restart and ordinary-marker lifecycle/serialization.
- [WORLD-04 consumers](supplied-consumers.md): available binder/squad/zone-condition/marker/configuration/polling consumers, qualified package comparison, practical synthesis and audit. Focused additional live restriction exports are documented separately.

## Effective-source closure still required

Winning _G/global aliases and callback/module/startup replacements; actor/stalker/restrictor/teleport binders and helper definitions including utils_obj/db/TeleportSquad/knife/looted storage; actual map_spots/message-box/destination/patrol/dynamic-item/option include roots and current applied values; smart/board/jobs and target predicates; active serializers/storage/reset/rebind phases; source/executable/compiler/build correspondence. File-name absence is scoped to the three selected gamedata roots, not the installation. ui_options and axr_main are available in their qualified package scopes; availability does not close their effective dependencies or aliases.

Reconcile accepted requests with completed motion/use/travel, native contacts versus Lua zone tables, old/new bookmarks and member locations, restriction default/client/server state, marker manager versus script bookkeeping, duplicate/remove/recreate behavior and active save/load/level-change order. Inspect cross-method icon and option-path source discrepancies under actual winning callers before treating them as installed defects. Existing [A-Life](../alife/source-completion-status.md), [persistence](../persistence/source-completion-status.md) and [tasks](../tasks/source-completion-status.md) requirements remain authoritative.

## Deferred runtime and optional depth

Lookup/relocation/path/accessibility/use/touch/travel/marker callbacks, duplicate operations, save/load/restoration and level changes need an identified executable/profile with logs/observations. Runtime remains deferred. Exhaustive pathfinder/AI/physics, every interactable/patrol/level/marker/relation policy, renderer/vehicles/multiplayer and every build/converter branch remain optional unless a concrete question requires them.

The source stopping rule is satisfied for this planned available-source pass; full installed closure is not declared complete. Another ADR subsystem can proceed independently. No CtZ gameplay changes or third-party source/assets are included. [Roadmap](../../ROADMAP.md).
