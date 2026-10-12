# Gameplay state source completion and remaining work

> ADR document set: **v0.1.66**. Research revisions and source/build versions below describe their original scope.

**As of 12 October 2026:** GAME-01 base condition/live hits, GAME-02 actor effects/equipment, GAME-03 selected derived death/restoration, and GAME-04 practical consolidation/bounded audit are complete within their available-source boundaries. [Development reference](development-reference.md). Full effective installed integration remains **partial**; runtime **untested** and deferred.

| Completed scope | Record | Limits retained |
| --- | --- | --- |
| Base condition and hit phases | [GAME-01](../../08-research/investigations/2026-10-12-GAME-01-native-condition.md), [reference](native-condition.md), [APIs](../../02-lua-api/gameplay/condition-api.md) | Current versus pending state, harm/time/branch/callback gates |
| Actor survival/boosters/equipment | [GAME-02](../../08-research/investigations/2026-10-12-GAME-02-actor-effects.md), [reference](actor-effects-equipment.md), [APIs](../../02-lua-api/gameplay/actor-effects-api.md) | Actor/NPC difference, medicine gap, helper/compiler mismatch, configuration formulas |
| Derived death and reconstruction | [GAME-03](../../08-research/investigations/2026-10-12-GAME-03-death-restoration.md), [reference](death-restoration.md) | Selected owners, server/live/custom-data split and callback/cleanup order |
| Synthesis and consistency audit | [GAME-04](../../08-research/investigations/2026-10-12-GAME-04-gameplay-consolidation.md), [audit](../../08-research/verification-2026-10-12-v0.1.66.md) | Selected first-edition available-source stopping point |

## Effective contracts still open

| Contract | Required evidence |
| --- | --- |
| Actual damage, survival and healing | Winning actor/creature/item configs, immunity/condition/medicine helpers, armor bone tables/upgrades and script effects |
| Medicine and booster behavior | Effective timed medicine consumer; accessor/header/compiler/executable correspondence; authoritative cancellation and restore reset/reapply chain |
| Callback observation and mutation | Winning pre-hit/after-calcs/death relays/listeners, startup order, actor-before-death build flag and reentrant/lifetime handling |
| Derived casualty and loot policy | Applicable creature overrides, wounded/loot/drop handlers, server script classes, squad/casualty consumers and final release/ID cleanup |
| Complete condition restoration | Winning binders/storage/migrations, fresh versus reused objects, field/membership convergence and online/offline synchronization |
| Build/profile identity | Actual executable/configuration and effective files; supplied archive date is not installed correspondence |

Use existing [effective-profile provenance requirements](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md). [Inventory](../inventory/source-completion-status.md), [A-Life](../alife/source-completion-status.md), [factions](../factions/source-completion-status.md) and [persistence](../persistence/source-completion-status.md) overlap these gaps.

## Stopping rule

Full installed gameplay-state integration becomes development-reference ready at source level when relevant winning condition/hit/death/restore chains are collected, traced and reconciled with selected native findings. Runtime remains a separate explicitly resumed phase: pin executable/profile, record repeatable state-change/effect/mitigation/callback/casualty/save-load/level-change observations, then classify actual outcomes.

Every monster species attack/death override, animation/physics/effect internals, multiplayer variants, exhaustive converters and malformed-save/input robustness are optional later depth unless a concrete modding question requires them. Safe NPC medicine, resurrection or casualty bookkeeping is not automatically proved by this scoped completion. Next general foundation: tasks/dialogue/info state. [Roadmap](../../ROADMAP.md).
