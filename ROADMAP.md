# ADR roadmap

> ADR document set: **v0.1.70**. Research revisions and source/build versions below describe their original scope.

## Current source status

UI/PDA is development-reference ready within the documented source scope. A-Life/Warfare native foundations and the scoped interface catalog are complete; lifecycle/callback references are consolidated within their source scope. Native configuration and supplied-package policy controls are consolidated, and the bounded final consistency audit is complete. Effective script chains remain open. Independent in-game verification remains deferred; [selected external observations](08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md) are recorded separately.

## Runtime feedback priorities — 2026-10-12

- [ ] Issue #1: isolate shown-dialog/HUD/PDA teardown, native aliases and quickload; obtain exact executable/profile and raw logs/probe.
- [ ] Issue #2: isolate registration during loading with/without MAC/full strip; establish an actual post-load readiness phase, not a fixed-delay guarantee.
- [x] Issue #3: fix `.property` extraction and regenerate condition property while preserving existing catalog rows.
- [x] Issue #4: record scoped external string/clock/header observations, source LuaJIT 2.0.4 and September/October callback differences.

Documentation intake does not close the two crash investigations or independently certify the user’s install. [Confidence/disposition](08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md). CtZ UI timing/lifetime review belongs in its separate project; no mod change is included here.

## Next source work

The planned consolidation and bounded audits from available snapshots are complete for A-Life/Warfare and factions. Both retain effective installed-source requirements; see [A-Life/Warfare completion](04-game-systems/alife/source-completion-status.md) and [faction completion](04-game-systems/factions/source-completion-status.md). Persistence available-source work is complete within selected scope: PER-01 selected native save/load pipeline and Lua extension boundaries are complete within scope. PER-02 supplied codec/caller/gap pass is complete within scope; effective core manager/dispatch/storage remains partial. PER-03 selected CtZ campaign identity/schema/restoration/reconciliation is complete; PER-04 practical consolidation and final bounded audit are complete. Full effective installed persistence remains partial under its [completion rule](04-game-systems/persistence/source-completion-status.md). Inventory ITEM-01–04 selected foundations and ITEM-05 practical consolidation/bounded audit are complete within available-source scope. [Effective inventory integration](04-game-systems/inventory/source-completion-status.md) remains partial. Trade/economy and gameplay state available-source work are now consolidated and audited within scope; effective installed inputs and runtime remain open. Tasks/dialogue/info state TASK-01–03 are also consolidated and audited within selected available-source scope; effective installed integration remains partial under the [task completion rule](04-game-systems/tasks/source-completion-status.md). World interaction/navigation WORLD-01 [coverage inventory](04-game-systems/world/coverage-inventory.md) is complete within scope; the subsystem remains partial. Next WORLD-02 spatial queries/relocation and selected restriction/patrol contracts. Runtime verification remains deferred.

<a id="current-a-lifewarfare-remaining-scope--v0138"></a>

## Current A-Life/Warfare remaining scope


This is the current consolidated checklist for the earlier **CtZ-focused development reference**, now incorporated into the broader general-modding foundation. Older plans are preserved in the [historical roadmap](08-research/history/roadmap-through-v0.1.40.md). Source readiness and runtime verification remain separate.

- [x] ALIFE-01/02: identity, membership, native creation/registration/release and callback boundaries.
- [x] ALIFE-04: bounded native save/load and supplied CtZ identity reconstruction.
- [x] ALIFE-05/06/07: scheduling/brains, graph movement, online realization, client state return and offline teardown.
- [x] ALIFE-08: native switching permissions, distance hysteresis, attachment/group/member gates and supplied forced-status boundary. See [report](08-research/investigations/2026-10-11-ALIFE-08-switching-eligibility.md).
- [x] WAR-002 package pass: supplied variants, targeting/arrival boundaries, ownership/autocapture and offline combat call sites.
- [ ] ALIFE-03 effective smart/board layer: assignment/unassignment, reach tests, member registration, jobs and native task/restriction handoff. Requires missing core/winning scripts.
- [ ] Effective Warfare closure: active files, module/startup replacements and callback order; relevant spawning/strategy/configuration contracts for targeting, capture and combat. Selected supplied-package controls are documented; installed closure requires effective sources.
- [ ] Death/safe-release closure: creature overrides, casualty notification, membership cleanup and queued release; establish online/offline convergence from effective scripts.
- [ ] Persistence integration: effective save/load order and storage wrappers, restoration of strategic state, CtZ reconciliation and campaign/ID safety. The native/CtZ source pass is complete within its documented boundary.
- [x] ALIFE-09: scoped C++/Lua class map, binding inventory, focused API contracts and script declaration catalog.
- [x] Workflow, canonical folder structure and current navigation audit.
- [x] ALIFE-10: [lifecycle/state map](04-game-systems/alife/lifecycle-state-reference.md) and [callback observation contracts](04-game-systems/alife/callback-phase-reference.md), with linked APIs and scoped evidence.
- [x] ALIFE-11 / WAR-003: [native controls](04-game-systems/alife/configuration-controls.md), [Warfare controls](04-game-systems/warfare/policy-controls.md) and bounded final source-consistency audit; unresolved effective-script edges retained.
- [ ] Runtime checks, deferred: switching positions and callbacks, assignment versus arrival, ownership changes, online/offline deaths and cleanup, save/load/CtZ restoration and level changes. Confirm target executable/profile correspondence.

Effective source requirements are listed in [WAR-002a](08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md). Selected optional entity/AI internals and exhaustive unrelated API coverage are not prerequisites. Source-level stopping point: close the effective script chains, consolidate and audit, then mark this portion development-reference ready with runtime pending. No runtime test is required during the current source phase.

## Factions / relations current scope

- [x] FAC-01: [native identity/goodwill/attitude foundations](04-game-systems/factions/native-relations.md) and [focused Lua contracts](02-lua-api/factions/relations-api.md).
- [x] FAC-02: [native relation serialization, reset/reload and object-ID cleanup boundaries](04-game-systems/factions/relation-persistence.md).
- [x] FAC-03: [native community mutation, client/server identity and local team/group effects](04-game-systems/factions/community-mutation.md); effective strategic reassignment remains open.
- [x] FAC-04: [selected native attack/kill/help pathways, rank/reputation contributions and callback boundaries](04-game-systems/factions/action-goodwill.md). Effective reward scripts remain open.
- [x] FAC-05: [selected supplied-main-package Warfare faction/relation consumers](04-game-systems/factions/warfare-relation-consumers.md).
- [ ] Effective GAMMA diplomacy/configuration/helpers and startup/override order.
- [x] FAC-06: [practical faction consolidation](04-game-systems/factions/development-reference.md).
- [x] FAC-06: [final bounded available-source consistency audit](08-research/verification-2026-10-11-v0.1.49.md).
- [ ] Runtime verification, deferred until explicitly resumed.

Planned available-source work is complete within scope. Full effective integration remains partial under the [faction completion rule](04-game-systems/factions/source-completion-status.md); configured faction indexes, active numeric values and installed relations are not inferred.

## Persistence current scope

- [x] PER-01: [selected native save/load architecture and Lua extension phases](04-game-systems/persistence/native-save-load-pipeline.md).
- [x] PER-02: [supplied codec/caller contracts, formats/limits and effective-profile gaps](04-game-systems/persistence/lua-storage-contracts.md). Core installed implementations remain required.
- [x] PER-03: [CtZ identity/schema/restoration/reconciliation](04-game-systems/persistence/ctz-campaign-safety.md). Effective identity/schema safeguards remain unverified.
- [x] PER-04: [practical persistence reference](04-game-systems/persistence/development-reference.md) and [bounded final audit](08-research/verification-2026-10-11-v0.1.53.md).
- [ ] Effective installed dispatcher/storage/binders/configuration and executable correspondence.
- [ ] Runtime verification, deferred until explicitly resumed.

Native phase/source findings do not certify arbitrary Lua table serialization, whole-save integrity or companion-file atomicity.

## UI/PDA remaining work

- [ ] Optional exhaustive binding/overload, converter, inherited emitter and build/configuration coverage beyond the scoped inventories.
- [ ] Effective addon interaction and conflict analysis when the installed profile becomes available.
- [ ] Deferred runtime checks: ownership/GC, tabs, font initialization, assets, scaling and input behavior under the identified executable/profile.

## General modding foundations

The first broadly useful ADR extends beyond CtZ while remaining bounded. CtZ supplies practical examples/questions; it does not define the only completion criterion. Existing detailed scope/status qualifications remain in force.

- [x] Substantial UI/PDA, A-Life/Warfare, faction and persistence available-source foundations; effective/runtime gaps remain open.
- [x] Selected inventory/item lifecycle available-source foundation: [ownership](04-game-systems/inventory/ownership-lifecycle.md), [placement/activation](04-game-systems/inventory/placement-activation.md), [consumption/removal](04-game-systems/inventory/consumption-destruction.md), [persistence/reconstruction](04-game-systems/inventory/persistence-reconstruction.md) and [consolidation/audit](04-game-systems/inventory/development-reference.md) complete within scope; [effective integration](04-game-systems/inventory/source-completion-status.md) remains partial.
- [x] Trade/economy selected available-source foundation: ECO-01/ECO-02 plus [ECO-03 consolidation and bounded audit](04-game-systems/economy/development-reference.md). [Effective integration](04-game-systems/economy/source-completion-status.md) remains partial; winning managers/stock/gate/discount configs and runtime remain open.
- [x] Actor/NPC gameplay state selected available-source foundation: GAME-01–03 plus [GAME-04 consolidation/audit](04-game-systems/gameplay/development-reference.md). [Effective integration](04-game-systems/gameplay/source-completion-status.md) remains partial; medicine/helper/restore, installed-profile and runtime gaps retained.
- [x] Tasks/dialogue/info state: TASK-01 native foundation, TASK-02 supplied consumers and TASK-03 [consolidation/audit](04-game-systems/tasks/development-reference.md) complete within selected available-source scope. [Effective integration](04-game-systems/tasks/source-completion-status.md) remains partial; runtime deferred.
- [x] WORLD-01: [existing world/navigation coverage inventory](04-game-systems/world/coverage-inventory.md), canonical A-Life reuse boundary and bounded follow-on plan. Inventory closure only.
- [ ] WORLD-02: live spatial lookup/vertex/position/relocation and selected accessibility/restriction/patrol contracts.
- [ ] WORLD-03: selected use/touch, actor level transitions and marker lifecycle.
- [ ] WORLD-04: supplied consumers, practical consolidation and bounded audit; [world subsystem status](04-game-systems/world/source-completion-status.md) remains partial.
- [ ] Configuration/script integration: LTX sections/inheritance, Lua startup/loading, callback registration, patching and effective file precedence.
- [ ] Practical architecture/debugging: compatibility/state ownership, logging/crash diagnosis, qualified examples and evidence-based test guidance.
- [ ] Cross-system consolidation: C++/Lua maps, practical references, qualified examples and final provenance/navigation/consistency audit.

Each subsystem's first-edition boundary is its main lifecycle, state owner, relevant configuration/Lua contracts, callbacks, persistence, failure behavior and cross-system dependencies, with explicit gaps. Inventory existing coverage before each new investigation. Full renderer internals, every weapon/AI variant, animation/physics internals, multiplayer and exhaustive binding/build combinations are optional later depth unless a concrete question requires them. Effective-source collection and runtime resumption remain separate; all runtime remains deferred.

## Maintenance

Use the [standard workflow](08-research/workflow.md), [layout conventions](08-research/repository-layout.md) and [current verification report](08-research/verification-2026-10-12-v0.1.70.md). Historical unchecked boxes are not the current backlog.

## Tasks/dialogue/info effective backlog

- [ ] Winning task/turn-in/functor/reward helpers, startup order and active task/dialogue/info definitions.
- [ ] Actor stored tables, task-manager stage/history/repeat serialization, omitted native info-list reconstruction and effective binders/dispatcher/encoder restore phases.
- [ ] Confirm active consumers and handler returns before treating supplied smart-control/dispatcher discrepancies as installed bugs.
- [ ] Runtime task/turn-in/reward/info/save-load/level-change observations, deferred.

See [completion requirements](04-game-systems/tasks/source-completion-status.md); historical next-step descriptions in dated records retain their original scope.
