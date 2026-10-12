# ECO-01 — Native money, pricing and trade flow

> ADR document set: **v0.1.69**. Research revisions and source/build versions below describe their original scope.

- ID: ECO-01
- Subsystem: trade/economy
- ADR revision: v0.1.59
- Record status: complete-within-scope
- Source status: source-confirmed selected native/Lua/UI paths
- Runtime status: untested; deferred
- Baseline IDs and provenance record: ENGINE1011; [baseline](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

## Question and scope

Which native state owns money, how is a selected trade price computed, and where do UI eligibility/accounting/callbacks differ from item transfer? Include live/server money, selected serialization, Lua wrappers, CTrade prices/per-item flow and actor-menu preflight/batching. Completion is a source-backed boundary map with exact direction/return/numeric/script qualifications. Exclude full configuration/supply parsing, effective GAMMA scripts, all NPC/derived transactions, runtime and gameplay changes.

## Evidence and method

[Ledger](../../evidence/economy/native-trade-2026-10-11.csv): E01–E23; original paths, full-file hashes and line/symbol ranges. ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream/binary/profile correspondence unknown. Inventory existing inventory/faction/persistence coverage first; read declarations, bindings, money sender/consumer, serializers and selected UI/native trade callers. Distinguish literal source arithmetic from runtime observations.

## Findings

[Reference](../../04-game-systems/economy/native-trade.md) maps E01–E05 live/server/save money; E06–E12 exact wrapper/base-cost contracts; E13 price direction/factors/mandatory discounts; E14/E15/E17–E19 accounting/eligibility/callback order; E20 parameter defaults/precedence; E21/E22 callback/signature boundaries; E23 selected trader restore/base-artefact route. [API page](../../02-lua-api/economy/money-cost-api.md) preserves void returns, receiver assumptions and transfer-delta sign/conversion hazards.

## Competing explanations and missing edges

Trade event names do not establish priced payment; native accounting does not acknowledge transfer acceptance. UI projections do not certify arbitrary balances/rollback. Required script discounts/configuration can change quotes; actual definitions and winners remain to be collected/traced. Literal TransferMoney sign/conversion concerns are not an observed installed fault and are not fixed by altering research source. Full derived owners/Cost/condition, supplies, offline economy and money reconstruction convergence remain open.

## Checks and outcomes

Reviewed bodies/callers in source order and matched focused signatures/registrations. Hash/range/symbol/preservation/navigation and existing validator outcomes in [verification](../verification-2026-10-11-v0.1.59.md). No engine/game execution, source/save/gameplay edits or runtime arithmetic experiment.

## Disposition and next work

Selected ECO-01 foundation complete within scope; subsystem partial. Next ECO-02 native trader configuration/supply and supplied Lua consumer/missing-effective-definition pass, then bounded consolidation/audit. [Roadmap](../../ROADMAP.md).
