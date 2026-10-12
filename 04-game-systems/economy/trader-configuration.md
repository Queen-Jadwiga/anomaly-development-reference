# Trader configuration and supply consumers

> ADR document set: **v0.1.61**. Research revisions and source/build versions below describe their original scope.

- ID: ECO-02
- Subsystem: trade/economy
- Research revision: v0.1.61
- Source status: source-confirmed selected native and supplied Lua paths; scoped-source-audit for missing definitions
- Runtime status: untested; deferred
- Baselines: ENGINE1011 and BETA150; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

[Evidence ledger](../../evidence/economy/trader-configuration-2026-10-12.csv), T01–T21; [investigation](../../08-research/investigations/2026-10-12-ECO-02-trader-configuration.md). These uploaded snapshots do not identify installed winners or executable correspondence. [ECO-01](native-trade.md) owns the price and accounting flow.

## Policy ownership and action parsing

The owner's `net_Spawn` recreates CTradeParameters using its configured `trade_section`, falling back to `trade`. The constructor reads four price-factor fields from pSettings and sets buy-condition threshold 1.0 and buy/sell exponents 0.75. Global defaults are a separate lazily allocated singleton, deleted at selected level teardown. Do not treat changed live factors as a saved trader profile or shared faction account. T01/T05/T15.

| Entry or operation | Selected native behavior | Boundary |
| --- | --- | --- |
| buy/sell INI section | Assert section exists; clear that action's explicit enable/disable entries; skip names absent from pSettings | It does not load a full trader profile, choose a conditional section or schedule restock |
| Empty buy/sell value | Disable known item section | An omitted item remains eligible for fallback factors, not implicitly forbidden |
| Nonempty buy/sell value | atof first token as friend factor, second as enemy; one token repeats first | Extra tokens unused; no strict two-token validation or nonnegative bound here |
| Numeric buy/sell overload | Change local default factors only | Existing explicit item factors/disabled entries remain |
| Global buy/sell overloads | Same operations on global singleton | Shared policy can veto an owner's locally enabled entry |
| show INI section | Clear show disables; empty values disable names; nonempty values do nothing | No pSettings item-existence filter in this body; not an ordinary sell-price table |

T01–T04/T08–T11. Both local and global disabled entries veto `enabled`. Factor resolution is local explicit → global explicit → local default. Action `clear` leaves its default factors unchanged; CTradeParameters::clear clears buy/sell only. T01/T03. The selected show consumer is the dead-stalker AllowItemToTrade branch; the living branch uses can_sell instead. This does not establish one universal trader/deadbody visibility policy. T14.

**Literal factor-order caveat:** CTradeFactors takes `(friend, enemy)`. INI action rows and numeric wrappers use that order. The constructor nevertheless passes `*_price_factor_hostile` first and `*_price_factor_friendly` second. Thus those configured names are assigned to the opposite named members in this inspected body. Keep this source-level discrepancy explicit; actual values and script overrides may mask it. It is not a verified installed pricing fault. T01/T02/T08.

`buy_item_condition_factor` sets the minimum condition field; `buy_item_exponent` and `sell_item_exponent` set pricing exponents. They are separate void setters with no normalization here. ECO-01 records the selected UI threshold exemption for multi-use eatables and positive-exponent/fallback pricing behavior. T08/T11; [money and pricing flow](native-trade.md).

## Native supplies replace eligible stock through spawn requests

`buy_supplies(ini, section)` lazily creates an owner CPurchaseList and invokes process. The routine first calls sell_useless_items, clears deficits, then reads the supply section. There is no affordability check, money debit, trader reputation check, timer or transactional rollback in these bodies. Destruction precedes section parsing/validation, so malformed input is not safely preflighted. T05/T06.

The cleanup iterates all inventory items. It retains bolts, weapons for which CurrSlot() is nonzero, and a PDA whose original owner matches this owner; other items have drop-manual cleared and DestroyObject requested. This is the literal weapon-slot predicate, not a claim that every equipped item survives. No sale payment is made despite the helper name. T05.

Supply rows with empty values or absent pSettings item sections are skipped. First token is atoi count, converted to u32; optional second token is atof probability, default 1.0. Count must be nonzero and probability not approximately zero under VERIFY, but this body supplies no general range clamp: negative counts, negative probabilities, values above one and malformed input must not be treated as validated data. Each of count trials spawns when `Random.randF(0,1) <= probability`. T06.

Spawn calls use owner position, level vertex and parent ID, with return_item=false. That path builds and sends a spawn packet, destroys its temporary server entity and returns null. PurchaseList increments j before calling it; j counts selected spawn requests, not confirmed live inventory arrivals. No completion receipt or finite faction-stock consumption follows. Repeating this routine requests a new destructive reroll rather than an idempotent stock reconciliation. T06/T12; [inventory event acceptance](../inventory/ownership-lifecycle.md).

The deficit cache stores `(count * probability) / max(j, 0.3)` and returns 1 for absent names. However ECO-01's inspected GetItemPrice compiles out the deficit lookup and uses 1. Native supply scarcity therefore does not automatically change these native quotes. Script price policy may still apply, but requires its own definition. T06/T07/T13.

`spawn_supplies` is a distinct owner initialization routine (selected body spawns bolts); its name is not evidence of invoking trader stock lists. ECO-01 already traces the selected trader override. [Native trade](native-trade.md), ENGINE1011 InventoryOwner.cpp:372–398 and ai/trader/ai_trader.cpp:327–331.

## Supplied Lua refresh and profile selection

ENGINE1011's aaaa_script_fixes_mp captures the current trade_manager.trade_init during module evaluation. Its replacement returns without initialization if db.actor is absent; otherwise it saves the existing profile resupply_time, calls the captured function, then restores that timestamp if both old time and resulting profile exist. It does not wrap every later replacement or prove persistence through reload. T16.

The same file registers npc_on_update_force_trader_update for npc_on_update in on_game_start. Within strictly less than 30 metres squared-distance comparison, it requires a profile, cfg_ltx and get_trade_cfg result. It reads `max(get_eco_factor("restock") or 24, 12)` hours; with a timestamp and elapsed seconds below that interval it returns, otherwise calls trade_manager.update(npc). Timestamp reconstruction uses Y/M/D/h/m/s/ms through game.CTime. This is a nearby update request, not a proved whole-world schedule, successful refresh, or timer write. There is no db.actor nil guard inside this callback body. Actual callback phase, core update behavior and other patches remain required. T16.

BETA150 main xr_logic selects a trade path for live trader/stalker scheme initialization. If an explicit `trade` string exists and WARFARE plus check_npc_trader succeed, it substitutes the community's trade_names entry. Without explicit trade it uses items\trade\trade_generic.ltx; the faction substitution is inside the explicit-trade branch. An unmapped community has no fallback at the assignment. Then it calls trade_manager.trade_init and spawn_items. The table names faction-specific profiles but does not supply their stock or unlock rules. T19.

The BETA150 options expose restock 12–168 and a condition-buy override 0–100. Restock writes through game_difficulties.set_eco_factor; reads use get_eco_factor. New-game selection saves diff_eco with a configured restock or fallback 24. trader_cond writes trader_buy_condition_override into alife_storage_manager state, but no supplied consumer proves how it is scaled or applied to the native threshold. UI bounds do not validate all stored or scripted values. T20/T21.

## Supplied NPC trade consumer is a separate economy

The selected axr_trade_manager.npc_trade_buy_sell patch requires db.storage trade_items/has_items_to_sell and a server NPC. It protects the best weapon and slots 1–12 from its sell loop. A configured eligible item is transferred to a live seller, or released if none exists; it credits only the NPC using configured base cost (fallback 30) times parameter 4 (fallback 1), then records items_sold. It does not debit seller money or wait for transfer acceptance. The keep-count check runs after the sale; do not assume it prevents all sales at the stated reserve boundary. T17.

The buy phase requires positive local money, smart/job and live seller. It collects buy_sell sections, counts owned matching items, and uses cost times parameter 5. Its condition is `IsItem("ammo", sec) or (bw_ammos and bw_ammos[sec])`: the literal OR is broader than the comment claiming only best-weapon ammo. For an existing count c it loops from c through target inclusive, yielding target−c+1 attempts when c <= target; absent count starts at 1. It creates items for the NPC and calls transfer_money, updating a local balance estimate, without consuming seller inventory. Parameter 3, utilities, trade-item production and caller cadence remain unresolved. T17.

This supplied call site makes ECO-01's transfer_money sign/conversion concern relevant to actual candidate code, but does not prove that an installed executable runs this patch or exhibits the illustrated defect. Do not reuse it as a conserved requisition recipe. Mechanic upgrades and other NPC transaction paths are outside this focused pass. [Money wrapper limits](../../02-lua-api/economy/money-cost-api.md).

## Effective source requirements and CtZ boundary

Scoped inventory/search of ENGINE1011 gamedata and the full BETA150/ZIP142 extracted packages finds no core trade_manager.script, axr_trade_manager.script or game_difficulties.script, and no referenced items/trade profile files. The unlocalizer exposes axr_trade_manager ini/upgrade helpers for patching, not their definitions. T18; [scope inventory](../../evidence/economy/supplied-source-scope-2026-10-12.json).

Collect the winning trade managers, trader LTX/include/inheritance chains, game_difficulties and economy configs, logic/binders/condition helpers, item cost/section configs, unlocalizers and startup/monkeypatch order. Needed questions: conditional profile selection, goodwill/reputation/progression unlocks, exact buy/sell discounts, refresh inventory cleanup and timer writes, save/load reconstruction, and which NPC patch actually runs. A default 24-hour fallback is not the installed cycle; trade profiles named by a caller are not available stock evidence.

For CtZ, keep faction accounts, reserved stock, orders and successful delivery separate from character money and spawn requests. Native buy_supplies can destroy troop inventory and create unaccounted supplies; it is unsuitable as a general troop loadout/requisition helper without a deliberate adapter and runtime checks. No CtZ, Arsenal or ZoneMart implementation is included. ECO-02 is complete within this available-source boundary; effective integration remains partial. Next practical economy consolidation and bounded audit; runtime stays deferred.
