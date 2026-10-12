# Native money, pricing and trade flow

> ADR document set: **v0.1.63**. Research revisions and source/build versions below describe their original scope.

- ID: ECO-01
- Subsystem: trade/economy
- Research revision: v0.1.59
- Source status: source-confirmed selected native/Lua/UI paths
- Runtime status: untested; deferred until explicitly resumed
- Baseline: ENGINE1011; [source record](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

Archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit, binary/profile and winning script correspondence unknown. E01–E23 are local to the [ledger](../../evidence/economy/native-trade-2026-10-11.csv). [Investigation](../../08-research/investigations/2026-10-11-ECO-01-native-trade.md), [Lua money/cost contracts](../../02-lua-api/economy/money-cost-api.md).

## Existing coverage and first-pass boundary

[Inventory](../inventory/development-reference.md) already traces containment/events and distinguishes Lua transfer_item from payment. [Faction attitude](../factions/native-relations.md) supplies directed relation semantics, and [persistence](../persistence/development-reference.md) supplies server/client-save phases. CtZ has [separate strategic economy repair/ticking](../persistence/ctz-campaign-safety.md); those account tables are not native character money.

This pass adds selected native balance, price and actor-menu accounting contracts. Full trader LTX/action parsing, supplies/restock, effective discount/economy scripts, all NPC transaction variants and runtime are later work. No installed GAMMA price table or working NPC purchase recipe is inferred.

## Money has live and server representations

| Layer | State/change | Limit |
| --- | --- | --- |
| Live inventory owner | u32 m_money, get_money and set_money(amount, send_event) | Infinite-money profile flag makes setter keep max(old, amount), preventing a requested decrease |
| Money event | Optional GE_MONEY carries current live balance | Request/transport stage; not a payment receipt |
| Selected server consumer | Cast receiver to CSE_ALifeTraderAbstract and write m_dwMoney | No explicit null-cast guard in this branch; valid trader receiver is an invariant |
| Save state | Owner custom save/load retains m_money; server STATE retains m_dwMoney with legacy reader gate | Distinct persistence channels; do not assume they are always synchronized |

E01–E05. Setter itself has no general saturating arithmetic: its input is already u32. Calling with send_event=false changes live money without emitting this event. Selected UI TransferItems synchronizes both resulting balances at its end; direct native per-item TransferItem uses false for its updates. E02/E14/E19.

CAI_Trader's selected spawn applies server m_dwMoney after its inherited spawn chain; it also has native owner custom save/load calls. This is a specific trader chain, not a universal actor/stalker restore-order guarantee. E23; [inventory reconstruction](../inventory/persistence-reconstruction.md).

## Cost is not a trade quote

Base inventory item Load reads u32 cost and virtual Cost returns it. Lua cost forwards the virtual method, so derived cost may differ; it does not compute the partner's quote. The selected CAI_Trader::ArtefactPrice currently returns artefact Cost. E10–E12/E23.

Selected GetItemPrice computes:

1. Return zero immediately for b_free.
2. Choose virtual Cost, or ArtefactPrice when the item is an artefact, pThis is TT_ACTOR and pPartner is TT_TRADER.
3. Apply pow(condition * 0.9 + 0.1, exponent): exponent from pThis buy/sell parameters according to b_buying, positive value or fallback 0.75.
4. Compute directed attitude from pThis to pPartner, map (attitude + 1000)/2000 into [0,1], with NO_GOODWILL mapped to zero.
5. Choose enabled buy/sell action factors, interpolate enemy→friend by relation and clamp to their endpoints. Disabled action or zero action factor returns zero early.
6. Multiply by the condition/action factors and the active deficit factor 1, then floor. The dynamic deficit branch is compiled out here.
7. Require trade_manager.get_buy_discount or get_sell_discount by b_buying, passing pThis owner ID; multiply/floor the returned script factor.
8. For an eatable with nonzero max uses, scale by remaining/max uses using integer arithmetic and enforce at least 1. Finally clamp the non-early-return result to [1, 1000000].

E13/E14. A disabled action or zero factor produces a zero quote; direct native TransferItem still proceeds with item requests and zero-price accounting. The selected UI eligibility layer and the quote result have different contracts.

E13. The required discount lookup is asserted; no identity-discount fallback is present in this body. Conversion/overflow/nonfinite script inputs and exhaustive derived Cost are not validated by this function's name or the final clamp.

Buy/sell directions are from the CTrade instance's pThis owner. Selected actor-menu pricing uses m_partner_trade: true prices actor items being bought by the partner, false prices partner items sold to the actor. The inspected factor lookup uses pThis trade parameters. In its non-actor branch the internal buying selector stays true even though exponent/discount selection still follows b_buying; do not generalize an NPC↔NPC pricing recipe from the actor path. E13/E17/E18.

Local or global-default disabled entries reject enabled(); factors prefer local explicit, then global explicit, then local default factors. Constructors initialize buy-condition threshold 1.0 and buy/sell exponents 0.75. Full action/configuration parsing and actual overrides remain next-pass work. E20.

## UI preflight and native per-item accounting

Selected CanMoveToPartner requires CanTrade, partner buy-action enabled, and condition at or above the buy threshold except for eatables with nonzero max uses. It computes resulting partner weight from current inventory and selected baskets. This is the selected actor-sell-list gate, not a universal native TransferItem guard. E17.

The native CanTrade scan uses nearby objects, can return false on a dead entity encountered, then checks selected partner distance [0.5,4.5] and opposite facing. StartTradeEx instead calls SetPartner then StartTrade without invoking CanTrade in that body or checking SetPartner's bool. Thus session-start and that optional proximity predicate have different contracts. E15/E16.

Actor-menu Buy prices only the partner basket; Sell prices only the actor basket. Both cast balances/totals to int for projected affordability; Buy's partner-nonnegative check is commented, while Sell checks both. These signed projections/unsigned basket sums are not an arbitrary-large-balance safety guarantee. CalcItemsPrice sums each cell and its children in u32. E17/E18.

When accepted, UI invokes partner OnPerformTrade before item transfers. That native callback emits trade_perform_operation(money_get,money_put) only for TT_TRADER. It is a pre-transfer aggregate observation, not settlement confirmation. E15/E18/E21.

Per-item native TransferItem then:

1. Recompute GetItemPrice and call seller on_before_sell, buyer on_before_buy. Base hooks are void no-ops; derived effects remain separate.
2. Send GE_TRADE_SELL from seller.
3. Credit seller using unsigned balance + price and set_money(..., false).
4. Send GE_TRADE_BUY to buyer.
5. Debit buyer using unsigned balance - price and set_money(..., false).
6. Perform selected artefact bookkeeping and, when actor participates, emit trade_sell_buy_item(item, direction, price).

E01/E14/E21. Here bBuying=true means pThis buys from partner; false reverses it. Actor callback direction is literal (pThis.type != TT_ACTOR) && bBuying. TransferItem has no affordability/CanTrade/condition preflight, completion acknowledgement, saturation or rollback in this body. Item events retain [inventory acceptance/phase limits](../inventory/ownership-lifecycle.md); accounting can proceed without a returned successful transfer.

UI TransferItems removes each cell, calls that native method, updates lists, then emits money events for both final balances. The batch preflight price is not reserved: each item is quoted again, and script/derived changes are not a documented fixed-price transaction. Donation has an optional actor-menu hook, then calls TransferItem(..., true, true) at zero price; the split item events remain. E19.

## Lua money wrappers: literal hazards

[Exact API contracts](../../02-lua-api/economy/money-cost-api.md). GiveMoneySafe saturates positive additions to u32 max and negative deductions to zero using widened magnitude, then calls set_money for nonzero deltas; a zero delta skips both setter and event. Infinite-money policy can prevent a requested deduction. Money/give_money require inventory-owner receiver by VERIFY. E01/E02/E06–E08.

TransferMoney's wrapper is not an established conservative transfer algorithm. It checks source u32 balance against signed int money, changes source by -money, computes **new source minus old source** as unsigned arithmetic assigned to int, and passes that signed result to GiveMoneySafe on destination. For a positive small transfer on ordinary 32-bit two's-complement conversion, a source deduction yields a negative destination delta: e.g. 1000→900 yields -100, so a destination 1000 can also become 900. This is a qualified source arithmetic illustration, not an observed runtime test or cross-platform conversion guarantee. E06.

Negative money meets mixed signed/unsigned comparison; source deduction delta conversion depends on target C++ behavior for out-of-range unsigned-to-int values. INT_MIN also encounters unary -money before the helper's widened-magnitude protection. Infinite-money source can produce zero actual delta. No reliable conserved payment, safe negative/edge input, success return or rollback follows. Keep this wrapper unresolved pending executable/effective-path verification rather than silently correcting ADR source or endorsing it as a payment recipe. E01/E02/E06/E07.

## Scope and next work

ECO-01 selected native money/pricing/UI accounting foundation complete within scope. Effective get_buy_discount/get_sell_discount, trader configuration/action/supply refresh, NPC economy, restoration convergence and numeric/reentrant failure behavior remain open. Next ECO-02: native trader configuration/supply contracts plus supplied Lua consumers and missing effective definitions, then practical consolidation/audit. Runtime remains deferred. [Roadmap](../../ROADMAP.md).

## ECO-02 follow-up — 2026-10-12

[Trader configuration and supply consumers](trader-configuration.md) closes the selected parsing/binding/supply and supplied-script pass. Effective price discounts, stock tables, unlock rules, NPC paths beyond the selected patch and runtime remain open. The original ECO-01 scope and dated disposition above are preserved.
