# A-Life reference

> ADR document set: **v0.1.53**. Research revisions and source/build versions below describe their original scope.

Available-source consolidation is complete within scope; the full effective section remains partial. See [completion status](../alife/source-completion-status.md), [native controls](../alife/configuration-controls.md), [Warfare controls](../warfare/policy-controls.md) and the [final audit](../../08-research/verification-2026-10-11-v0.1.43.md). Runtime verification remains deferred.

## Current practical references

- [Lifecycle/state map](lifecycle-state-reference.md): representations, transitions, position and persistence boundaries.
- [Callback phases](callback-phase-reference.md): observation/readiness contracts and API implications.
- [ALIFE-10 synthesis and scope](../../08-research/investigations/2026-10-11-ALIFE-10-lifecycle-callback-consolidation.md).

**Current revision: v0.1.53.** First source pass established server identity, native squad membership, selected online/offline paths, and the boundary with Lua smart assignment. Installed GAMMA behavior and runtime tests remain deferred.

- [ALIFE-01 — Identity, squad membership and lifecycle](../../08-research/investigations/2026-10-11-ALIFE-01-identity-lifecycle.md)
- [October 11 source evidence ledger](../../evidence/alife/source-evidence-oct11.csv)
- [Warfare/CtZ integration boundary](../../08-research/investigations/2026-10-11-WAR-001-ctz-integration-boundary.md)

- [ALIFE-02 — Creation, registration, release and callback ordering](../../08-research/investigations/2026-10-11-ALIFE-02-creation-registration-release.md)
- [ALIFE-02 evidence ledger](../../evidence/alife/creation-release-evidence-oct11.csv)

Native lifecycle source follow-up complete within its stated scope. Next: effective smart-terrain, simulation-board, global callback wrappers and Warfare scripts.

## Effective-script follow-up

- [Supplied Warfare package provenance and missing effective sources](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).
- [Assignment/arrival, ownership and offline-death boundaries](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md).

ALIFE-03 remains partial: board/smart implementations and installed creature/safe-release overrides are still needed.

## v0.1.34 — Native persistence and CtZ reconstruction

- [ALIFE-04: save/load, late member repair and campaign identity](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md).
- [15-file source evidence ledger](../../evidence/alife/save-load-evidence-oct11.csv).

Native/CtZ pass complete within scope; effective persistence wrappers and runtime verification deferred. Next independent source work: native offline scheduler and squad/monster brains.

## v0.1.35 — Native scheduling and brains

- [ALIFE-05: scheduler, individual/group brains and offline movement](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md).
- [21-file source evidence ledger](../../evidence/alife/offline-scheduling-evidence-oct11.csv).

Bounded native pass complete; effective settings/overrides and runtime deferred. Next: graph location changes and online spawn realization.

## v0.1.36 — Graph location and online realization

- [ALIFE-06: graph changes, client spawn positions and callback ordering](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md).
- [27-file source evidence ledger](../../evidence/alife/graph-online-realization-evidence-oct11.csv).

Bounded source pass complete; installed overrides/runtime deferred. Next: client-to-server position synchronization and offline teardown.

## v0.1.37 — Position synchronization and offline teardown

- [ALIFE-07: client updates, save packets, retained state and destruction callback phases](../../08-research/investigations/2026-10-11-ALIFE-07-client-server-offline-teardown.md).
- [25-file source evidence ledger](../../evidence/alife/client-server-offline-evidence-oct11.csv).

Bounded source pass complete; effective profile/runtime deferred. Next: native switching eligibility, distance hysteresis and forced-state overrides.

## v0.1.38 — Switching eligibility and forced states

- [ALIFE-08: permission truth table, distance hysteresis, group/member gates and Lua policy](../../08-research/investigations/2026-10-11-ALIFE-08-switching-eligibility.md).
- [19-file source evidence ledger](../../evidence/alife/switching-eligibility-evidence-oct11.csv).

Bounded native switching pass complete. Remaining effective smart/board, death/release and persistence chains require winning scripts. Consolidation and audit can continue from available sources; runtime deferred. See [current remaining scope](../../ROADMAP.md#current-a-lifewarfare-remaining-scope--v0138).

## v0.1.39 — C++ and Lua interface catalog

- [ALIFE-09 catalog and searchable inventories](../../02-lua-api/alife/README.md).
- [Class and ownership map](../../02-lua-api/alife/class-map.md).
- [Simulator API](../../02-lua-api/alife/simulator-api.md) and [server/squad/task/movement API](../../02-lua-api/alife/server-squad-api.md).
- [Script interfaces and unresolved effective modules](../../02-lua-api/alife/script-interfaces.md).

Scoped source mapping complete. Native-only machinery, Lua exports, virtual callbacks and script helpers are distinguished; runtime/effective profile and exhaustive signature/converter coverage remain qualified. Next: consolidate lifecycle/state and callback-phase maps from these references.

## v0.1.40 — Standard repository structure

Current API catalogs live in [the central API section](../../02-lua-api/api-index.md); dated investigations and ledgers have separate homes. Follow the [workflow](../../08-research/workflow.md) and [layout conventions](../../08-research/repository-layout.md). Historical findings and effective-profile/runtime limits are preserved.
