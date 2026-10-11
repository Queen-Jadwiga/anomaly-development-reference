# Warfare subsystem

> ADR document set: **v0.1.45**. Research revisions and source/build versions below describe their original scope.

**Current revision: v0.1.45.**

Use the [A-Life lifecycle/state map](../alife/lifecycle-state-reference.md) and [callback-phase reference](../alife/callback-phase-reference.md) for native/bundled representation and readiness boundaries. Effective Warfare policy and installed callback order remain separate open work.

**Current evidence:** Capture the Zone is intended to extend Anomaly/GAMMA Warfare, including PDA strategy display and tracking faction control.

Available-source consolidation is complete within scope; the full effective section remains partial. See [completion status](../alife/source-completion-status.md), [native controls](../alife/configuration-controls.md), [Warfare controls](../warfare/policy-controls.md) and the [final audit](../../08-research/verification-2026-10-11-v0.1.43.md). Runtime verification remains deferred.

## Topics and questions

- Faction identifiers, faction relation state, ownership of smart terrains.
- Squad lifecycle and offline/online transitions.
- Territory capture events and their available callbacks.
- Whether current state and history are serialized; save and load boundaries.
- Interaction with other Warfare/CtZ mods and MO2 override priority.

## Needed source material

Exact GAMMA Warfare scripts from the active profile, any Warfare-overriding mods, and relevant save/log examples. Do **not** treat generic Anomaly scripts on the web as authoritative for a heavily modded GAMMA profile.

## Initial deliverable

A call graph connecting faction state -> squad/smart-terrain logic -> event source -> CtZ UI update, each edge labeled with evidence and version.

## v0.1.31 — First source boundary established

- [Native A-Life identity and lifecycle](../../08-research/investigations/2026-10-11-ALIFE-01-identity-lifecycle.md).
- [WAR-001: CtZ call sites and missing effective-profile dependencies](../../08-research/investigations/2026-10-11-WAR-001-ctz-integration-boundary.md).

The October 11 archive includes `sim_squad_scripted.script` and selected native bindings, but does not provide the referenced board/smart/Warfare policy implementations. Faction capture and effective GAMMA override behavior remain open. In-game verification is deferred by user request.

## v0.1.33 — Supplied package policy traced

- [WAR-002a: two Warfare packages, pinned public GAMMA comparison and effective-profile source requirements](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).
- [WAR-002b: target/arrival distinction, ownership policy, callbacks and offline combat](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md).
- [Source locations and hashes](../../evidence/warfare/source-evidence-war002-oct11.csv).
- [Archive script byte comparison](../../evidence/warfare/archive-script-comparison-oct11.csv).

Supplied package implementations are now inspected. Current MO2 winning files and runtime function overrides remain unverified; this supersedes the earlier missing-package status without changing its historical findings. Runtime tests remain deferred.

## v0.1.34 — Persistence boundary

[Native save/load and CtZ campaign reconstruction](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md) distinguishes saved campaign records, squad packet fields and late member-pointer repair. Effective storage wrappers and ownership synchronization remain open; runtime deferred.

## v0.1.35 — Movement versus combat update authority

[ALIFE-05](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md) traces the native scheduled task/movement flow and Lua squad task handoff. Native scheduling, Lua arrival policy and the supplied offline-combat coordinator are separate mechanisms; installed overrides and runtime remain deferred.

## v0.1.36 — Online realization and position authority

[ALIFE-06](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md) traces member realization, early versus completed-spawn callbacks, cached position corrections and native map position sources. Installed bookmark patches/binders and runtime behavior remain unverified.

## v0.1.37 — Offline state and callback boundaries

[ALIFE-07](../../08-research/investigations/2026-10-11-ALIFE-07-client-server-offline-teardown.md) separates imported position, graph state, saved client data and Lua bookmarks, and traces destruction callback phases while preserving A-Life identity. The ordinary inspected offline route has no explicit final client snapshot barrier. Installed overrides and runtime remain unverified.

## v0.1.38 — Forced-state policy and native switching

[ALIFE-08](../../08-research/investigations/2026-10-11-ALIFE-08-switching-eligibility.md) connects supplied squad forced-status policy to native permissions, threshold hysteresis and member/group gates. The bundled and Warfare status producers differ; active replacement order and option values remain unverified. See [remaining scope](../../ROADMAP.md#current-a-lifewarfare-remaining-scope--v0138).

## v0.1.39 — Interface catalog

[ALIFE-09](../../02-lua-api/alife/README.md) maps native/server/squad interfaces and [supplied Warfare script declarations](../../02-lua-api/alife/script-interfaces.md). Package/patch variants remain separate. Missing effective smart/board/creature/safe-release implementations are explicitly tracked; runtime deferred.

## v0.1.40 — Standard repository structure

Current API catalogs live in [the central API section](../../02-lua-api/api-index.md); dated investigations and ledgers have separate homes. Follow the [workflow](../../08-research/workflow.md) and [layout conventions](../../08-research/repository-layout.md). Historical findings and effective-profile/runtime limits are preserved.
