# ADR roadmap

> ADR document set: **v0.1.46**. Research revisions and source/build versions below describe their original scope.

## Current source status

UI/PDA is development-reference ready within the documented source scope. A-Life/Warfare native foundations and the scoped interface catalog are complete; lifecycle/callback references are consolidated within their source scope. Native configuration and supplied-package policy controls are consolidated, and the bounded final consistency audit is complete. Effective script chains remain open. All in-game runtime verification is deferred.

## Next source work

The planned consolidation from available snapshots is complete. Continue effective A-Life/Warfare closure when the winning scripts and relevant configuration producers become available; see the [completion status and stopping rule](04-game-systems/alife/source-completion-status.md). Factions/relations is now the active independent subsystem. FAC-01 native query foundations are complete within scope; FAC-02 native persistence/reset/ID cleanup is complete within scope; FAC-03 character-community mutation is complete within scope; next trace action-driven updates and rank/reputation contributions. Supplied Warfare consumers and installed diplomacy remain later integration work. Runtime verification remains deferred.

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
- [ ] Action-driven goodwill: attack/kill/help pathways, rank/reputation contributions and callbacks.
- [ ] Supplied Warfare consumers and effective GAMMA diplomacy/configuration/override order.
- [ ] Practical consolidation and final bounded source audit after those investigations.
- [ ] Runtime verification, deferred until explicitly resumed.

Subsystem remains partial; configured faction indexes, numeric values and installed relations are not inferred from the native source.

## UI/PDA remaining work

- [ ] Optional exhaustive binding/overload, converter, inherited emitter and build/configuration coverage beyond the scoped inventories.
- [ ] Effective addon interaction and conflict analysis when the installed profile becomes available.
- [ ] Deferred runtime checks: ownership/GC, tabs, font initialization, assets, scaling and input behavior under the identified executable/profile.

## Maintenance

Use the [standard workflow](08-research/workflow.md), [layout conventions](08-research/repository-layout.md) and [current verification report](08-research/verification-2026-10-11-v0.1.46.md). Historical unchecked boxes are not the current backlog.
