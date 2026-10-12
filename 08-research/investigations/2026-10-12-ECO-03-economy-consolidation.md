# ECO-03 — Economy consolidation and bounded audit

> ADR document set: **v0.1.81**. Research revisions and source/build versions below describe their original scope.

- ID: ECO-03
- Subsystem: trade/economy
- ADR revision: v0.1.62
- Record status: complete-within-scope
- Source status: scoped-source-audit synthesis of source-confirmed selected contracts
- Runtime status: untested; deferred
- Baseline IDs and provenance record: ENGINE1011/BETA150/ZIP142; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

Consolidate ECO-01/ECO-02 into practical modding guidance and a source-completion rule. Audit state owners, direction, policy, money arithmetic, stock mutation, callbacks/request phases and persistence/effective gaps against their cited native/supplied paths. Complete the selected available-source economy first edition without claiming effective installed closure. Exclude new runtime tests, exhaustive unrelated variants and gameplay changes.

## Evidence and method

Retain [ECO-01 ledger E01–E23](../../evidence/economy/native-trade-2026-10-11.csv), [ECO-02 ledger T01–T21](../../evidence/economy/trader-configuration-2026-10-12.csv) and [scoped input inventory](../../evidence/economy/supplied-source-scope-2026-10-12.json). Re-read selected native price/TransferItem/UI eligibility/money helpers and policy/supply/script consumers, match wrappers to registration, and check all 44 ledger entries against declared roots. No new source baseline or altered historical evidence schema is introduced.

## Findings

[Development reference](../../04-game-systems/economy/development-reference.md) separates live/server/mod-owned accounts, base cost/quote, eligibility/direct mutation and requests/delivery. [Completion status](../../04-game-systems/economy/source-completion-status.md) marks available-source work complete while retaining missing effective managers/configs/hooks and runtime.

Three current-reference clarifications are explicit: the selected condition test permits equality (E17); zero GiveMoneySafe delta skips set_money and therefore GE_MONEY (E06); disabled action/zero action factor return zero quote, but direct native TransferItem proceeds with requests/accounting (E13/E14). Add these without rewriting dated ECO-01/ECO-02 investigation bodies. Previously documented constructor factor order, transfer-delta conversion, destructive supply reroll, inactive deficit pricing and supplied NPC-loop/stock caveats remain qualified source findings.

## Competing explanations and missing edges

Effective scripts can replace, mask or bypass selected native/supplied behavior; installed manager definitions, stock/gates/discounts and executable correspondence are missing. Structural source checks do not prove comment interpretation, conservation, safe retry or runtime delivery. Parent containment/payment/state persistence must converge through their separate consumers. Optional exhaustive variants remain separate from first-edition completion.

## Checks and outcomes

[Verification](../verification-2026-10-12-v0.1.62.md) records semantic audit groups, all ledger hash/range/symbol checks, scoped inventory reproduction, preservation, navigation and existing regression outcomes. No engine/game execution or tested transaction recipe.

## Disposition and next work

ECO-03 complete within scope; full effective economy integration remains partial. Continue general foundations with actor/NPC gameplay state, inventorying existing death/casualty/eatable effects first. Missing-source collection and runtime remain open. [Roadmap](../../ROADMAP.md).
