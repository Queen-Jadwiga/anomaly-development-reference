# ADR roadmap

> ADR document set: **v0.1.53**. Research revisions and source/build versions below describe their original scope.

## Current source status

UI/PDA is development-reference ready within the documented source scope. A-Life/Warfare native foundations and the scoped interface catalog are complete; lifecycle/callback references are consolidated within their source scope. Native configuration and supplied-package policy controls are consolidated, and the bounded final consistency audit is complete. Effective script chains remain open. All in-game runtime verification is deferred.

## Next source work

The planned consolidation and bounded audits from available snapshots are complete for A-Life/Warfare and factions. Both retain effective installed-source requirements; see [A-Life/Warfare completion](04-game-systems/alife/source-completion-status.md) and [faction completion](04-game-systems/factions/source-completion-status.md). Persistence available-source work is complete within selected scope: PER-01 selected native save/load pipeline and Lua extension boundaries are complete within scope. PER-02 supplied codec/caller/gap pass is complete within scope; effective core manager/dispatch/storage remains partial. PER-03 selected CtZ campaign identity/schema/restoration/reconciliation is complete; PER-04 practical consolidation and final bounded audit are complete. Full effective installed persistence remains partial under its [completion rule](04-game-systems/persistence/source-completion-status.md). Next independent subsystem: inventory/item lifecycle and trade foundations, beginning with native ownership, containment, pickup/drop and Lua interfaces. Runtime verification remains deferred.

<a id="current-a-lifewarfare-remaining-scope--v0138"></a>

## Current A-Life/Warfare remaining scope


This is the current consolidated checklist for the agreed **CtZ-focused development reference**. Older plans are preserved in the [historical roadmap](08-research/history/roadmap-through-v0.1.40.md). Source readiness and runtime verification remain separate.

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

## Maintenance

Use the [standard workflow](08-research/workflow.md), [layout conventions](08-research/repository-layout.md) and [current verification report](08-research/verification-2026-10-11-v0.1.53.md). Historical unchecked boxes are not the current backlog.
