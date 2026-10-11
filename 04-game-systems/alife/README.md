# A-Life reference

**Current revision: v0.1.39.** First source pass established server identity, native squad membership, selected online/offline paths, and the boundary with Lua smart assignment. Installed GAMMA behavior and runtime tests remain deferred.

- [ALIFE-01 — Identity, squad membership and lifecycle](identity-lifecycle-oct11.md)
- [October 11 source evidence ledger](source-evidence-oct11.csv)
- [Warfare/CtZ integration boundary](../warfare/ctz-integration-boundary-oct11.md)

- [ALIFE-02 — Creation, registration, release and callback ordering](creation-registration-release-oct11.md)
- [ALIFE-02 evidence ledger](creation-release-evidence-oct11.csv)

Native lifecycle source follow-up complete within its stated scope. Next: effective smart-terrain, simulation-board, global callback wrappers and Warfare scripts.

## Effective-script follow-up

- [Supplied Warfare package provenance and missing effective sources](../warfare/source-packages-effective-profile-oct11.md).
- [Assignment/arrival, ownership and offline-death boundaries](../warfare/warfare-policy-offline-combat-oct11.md).

ALIFE-03 remains partial: board/smart implementations and installed creature/safe-release overrides are still needed.

## v0.1.34 — Native persistence and CtZ reconstruction

- [ALIFE-04: save/load, late member repair and campaign identity](save-load-identity-oct11.md).
- [15-file source evidence ledger](save-load-evidence-oct11.csv).

Native/CtZ pass complete within scope; effective persistence wrappers and runtime verification deferred. Next independent source work: native offline scheduler and squad/monster brains.

## v0.1.35 — Native scheduling and brains

- [ALIFE-05: scheduler, individual/group brains and offline movement](offline-scheduling-brains-oct11.md).
- [21-file source evidence ledger](offline-scheduling-evidence-oct11.csv).

Bounded native pass complete; effective settings/overrides and runtime deferred. Next: graph location changes and online spawn realization.

## v0.1.36 — Graph location and online realization

- [ALIFE-06: graph changes, client spawn positions and callback ordering](graph-online-realization-oct11.md).
- [27-file source evidence ledger](graph-online-realization-evidence-oct11.csv).

Bounded source pass complete; installed overrides/runtime deferred. Next: client-to-server position synchronization and offline teardown.

## v0.1.37 — Position synchronization and offline teardown

- [ALIFE-07: client updates, save packets, retained state and destruction callback phases](client-server-offline-teardown-oct11.md).
- [25-file source evidence ledger](client-server-offline-evidence-oct11.csv).

Bounded source pass complete; effective profile/runtime deferred. Next: native switching eligibility, distance hysteresis and forced-state overrides.

## v0.1.38 — Switching eligibility and forced states

- [ALIFE-08: permission truth table, distance hysteresis, group/member gates and Lua policy](switching-eligibility-oct11.md).
- [19-file source evidence ledger](switching-eligibility-evidence-oct11.csv).

Bounded native switching pass complete. Remaining effective smart/board, death/release and persistence chains require winning scripts. Consolidation and audit can continue from available sources; runtime deferred. See [current remaining scope](../../ROADMAP.md#current-a-lifewarfare-remaining-scope--v0138).

## v0.1.39 — C++ and Lua interface catalog

- [ALIFE-09 catalog and searchable inventories](api/README.md).
- [Class and ownership map](api/class-map.md).
- [Simulator API](api/simulator-api.md) and [server/squad/task/movement API](api/server-squad-api.md).
- [Script interfaces and unresolved effective modules](api/script-interfaces.md).

Scoped source mapping complete. Native-only machinery, Lua exports, virtual callbacks and script helpers are distinguished; runtime/effective profile and exhaustive signature/converter coverage remain qualified. Next: consolidate lifecycle/state and callback-phase maps from these references.
