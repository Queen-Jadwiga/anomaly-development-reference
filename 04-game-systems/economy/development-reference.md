# Trade and economy development reference

> ADR document set: **v0.1.64**. Research revisions and source/build versions below describe their original scope.

- ID: ECO-03
- Subsystem: trade/economy
- Research revision: v0.1.62
- Source status: source-confirmed selected contracts; scoped-source-audit consolidation
- Runtime status: untested; deferred
- Baselines/provenance: ENGINE1011/BETA150/ZIP142; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

The selected available-source economy foundation is consolidated and audited. Full installed integration remains partial under the [completion rule](source-completion-status.md). This reference explains which layer a mod can reason about; it does not provide a runtime-tested transaction or faction requisition recipe. Archive pins and unknown executable/profile correspondence remain in the [environment record](../../00-environment/source-baseline-2026-10-11.md) and manifest.

Evidence IDs are ledger-local: [ECO-01 E01–E23](../../evidence/economy/native-trade-2026-10-11.csv) and [ECO-02 T01–T21](../../evidence/economy/trader-configuration-2026-10-12.csv). Each ledger retains original paths, symbols, ranges and full-file hashes. [Consolidation record](../../08-research/investigations/2026-10-12-ECO-03-economy-consolidation.md), [bounded audit](../../08-research/verification-2026-10-12-v0.1.62.md).

## Choose the accounting layer

| Requirement | Relevant state or operation | Limit |
| --- | --- | --- |
| Read a live character balance | game_object:money / owner m_money | Not server m_dwMoney or CtZ faction funds |
| Adjust that balance | give_money signed delta, saturating helper | Infinite-money policy can prevent deductions; zero delta sends no event |
| Move character money | transfer_money wrapper | Source-delta sign/conversion hazard; no certified conservation or receipt |
| Determine base item value | virtual Cost / Lua cost | Not the partner quote or a refund record |
| Price an actor-menu trade | Selected partner CTrade GetItemPrice plus scripts | Profile discounts required; no installed formula/table inferred |
| Move an item | Inventory transfer/event chain | GE_TRADE names do not establish payment or completion |
| Refresh native supplies | buy_supplies purchase list | Selective destruction plus random spawn requests; no stock reservation/payment |
| Maintain a faction economy | Mod-owned accounts, stock and orders | Separate schema, persistence and reconciliation required |

E01–E14/E19; T05–T13; [inventory lifecycle](../inventory/development-reference.md) and [CtZ campaign safety](../persistence/ctz-campaign-safety.md). The final row is design guidance inferred from these distinct state owners, not an implemented engine service.

Live set_money can send GE_MONEY; the selected server consumer writes trader m_dwMoney. Owner custom save/load and server STATE store different representations. A supplied script's resupply timestamp is another layer, and a strategic faction account is another. Neither money events nor serialization names establish an atomic common ledger. Selected CAI_Trader spawn applies server money after its inherited chain; do not extend that restoration order to every owner. E01–E05/E23; [persistence](../persistence/development-reference.md).

## Follow price direction and policy scope

The actor-menu uses the partner's CTrade. For that selected path, buying=true quotes actor items being bought by the partner; false quotes partner items sold to the actor. Native TransferItem uses buying relative to its pThis owner. A Lua inventory transfer is a different wrapper. Non-actor factor selection retains its internal buying=true even while exponent and discount follow b_buying; the actor-menu recipe is not a general NPC pricing rule. E13/E14/E17–E19/E22; [price flow](native-trade.md).

The quote combines virtual base Cost, condition exponent, directed pThis→partner attitude, action factors, a native deficit factor fixed at 1, required script discount and selected remaining-use scaling. Disabled action/zero action factor return zero before the final 1–1,000,000 clamp. The clamp does not validate previous numeric conversion, unsigned arithmetic, script input or basket sums. A zero quote is not a safe eligibility verdict for a direct native TransferItem call: it still proceeds with hooks, item requests and zero-price accounting. E13/E14.

Local and global disabled entries veto enabled policy; factors resolve local explicit → global explicit → local default. An omitted INI row falls back rather than denies. INI buy/sell setters replace explicit entries but retain defaults; numeric overloads alter defaults without clearing explicit entries. Owner settings are recreated at net spawn; global singleton lifetime ends at selected level teardown. Those are not proof of persisted script-profile policy. T01/T03/T05/T08–T11/T15; [policy APIs](../../02-lua-api/economy/trader-policy-api.md).

CTradeFactors and action rows use friend then enemy. The constructor passes hostile-named settings first and friendly-named settings second, assigning them to the opposite named members. Keep that literal source discrepancy and possible masking by script overrides visible. The minimum buy-condition setter is separate from price exponent setters. The selected sell-list gate rejects condition strictly below the threshold, so equality passes that test; multi-use eatables bypass it. Show policy has a selected dead-stalker consumer, while live stalkers use can_sell. T01/T02/T08/T14; E17. None of these qualifiers certifies installed behavior.

## Eligibility and callbacks are not settlement

| Phase in selected actor-menu flow | Established | Still unproved at that point |
| --- | --- | --- |
| CanMoveToPartner | Item CanTrade, enabled partner buy policy, condition and projected capacity checks | Successful later transfer; this is not TransferItem's own universal preflight |
| Buy/Sell button preflight | Selected basket quote and signed balance projections | Fixed quote, reserved stock, safe arbitrary-large arithmetic |
| trade_perform_operation | TT_TRADER aggregate callback before item transfer | Paid/delivered completion |
| Native per-item TransferItem | Requote; before hooks; sell request; seller credit; buy request; buyer debit | Transfer acceptance, rollback or conserved result under every profile |
| trade_sell_buy_item | Selected actor callback after requests and balance changes | Final live inventory membership or restoration convergence |
| UI batch completion | Both final live balances passed to setters with money events | Atomic whole-batch persistence or item-delivery receipt |

E14/E15/E17–E21. Native TransferItem lacks its own affordability, condition, CanTrade and completion checks. Base before hooks are void no-ops; derived and reentrant effects remain outside that guarantee. UI quotes items again during execution, so the earlier total is not reserved. Donation is an optional script gate followed by zero-price native transfer; it retains the item-event boundary. [Inventory callback phases](../inventory/development-reference.md#callback-observation-boundaries).

The saturating give_money helper bounds a single signed adjustment; it does not make a multi-owner operation atomic. Infinite-money policy and saturation can change the actual delta. TransferMoney computes new-source minus old-source as destination delta; the qualified positive-transfer sign/conversion illustration remains an unresolved executable/effective-path concern. No rewritten payment implementation is supplied. E01/E02/E06–E08; [money API](../../02-lua-api/economy/money-cost-api.md).

## Stock refresh and supplied Lua economy

Native buy_supplies calls sell_useless_items before reading the supply section. Cleanup requests destruction except for bolts, weapons with a nonzero CurrSlot and owner-matching PDA. Rows use atoi count→u32 and atof probability, not a general validated data schema. Selected trials increment a request count and spawn with owner parent ID; the non-returning spawn path sends a packet and returns null. Repetition rerolls stock without payment, reservation or idempotence. Deficit data is retained but the inspected price branch does not use it. T05–T07/T12/T13. Calling this on a squad member can destroy equipment or generate unaccounted items; it is not an established loadout helper.

The supplied engine-script patch captures an earlier trade_init, preserves an existing resupply_time around that call, and registers a nearby-trader update requester. Within distance_squared < 900, with profile/config present, it requests update when a timestamp is absent or the configured interval has elapsed; its fallback is 24 hours with a 12-hour minimum. Core update/timer writes, remote traders and installed patch order are absent. BETA150 selects faction trade paths only inside the explicit logic trade branch, exposes UI economy factors and stores a condition override whose effective consumer remains missing. T16/T19–T21.

The supplied NPC patch is not the native actor-menu economy: sales credit NPC money without debiting seller; purchases create NPC items without consuming seller inventory and use the unresolved transfer_money wrapper. The ammo OR predicate is broader than its comment, and the existing-count loop is inclusive. Keep these literal boundaries when evaluating the patch; neither comments nor supplied presence establish installed execution or a finite market. T17/T18; [supplied consumer details](trader-configuration.md).

Core trade_manager, axr_trade_manager, game_difficulties and referenced trader profiles are missing from the scoped packages. Therefore actual discounts, goodwill/reputation/progression gates, stock tables, restock schedules and reconstruction remain open. [Inventory of missing inputs](../../evidence/economy/supplied-source-scope-2026-10-12.json), [effective completion requirements](source-completion-status.md).

## Applying the contracts to a mod

Design guidance inferred from the audit: choose one authoritative owner for each account and stock pool; record the price and intended resource change for an order; distinguish requested, delivered, cancelled and unresolved work; reconcile stable identities and persisted order IDs before retries. Live wrappers must not become persistent order identity. A callback or local balance estimate alone must not authorize a second delivery or a refund. The engine exposes separate mutation/request mechanisms rather than a proven common transaction receipt. Concrete adapters and failure recovery need effective-source review and runtime verification.

For CtZ, keep abstract faction supplies separate from physical inventory until an explicit conversion rule is applied. Equipment catalogs, markets and requisition screens can present those rules, but do not supply transaction integrity by themselves. No CtZ, Arsenal or ZoneMart code is changed or reviewed in this audit. Available-source stopping point is complete; next general ADR foundation is actor/NPC gameplay state. Effective-source collection and runtime resumption remain separate work. [Roadmap](../../ROADMAP.md).
