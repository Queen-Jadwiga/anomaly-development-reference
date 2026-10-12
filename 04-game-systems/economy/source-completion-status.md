# Economy source completion and remaining work

> ADR document set: **v0.1.66**. Research revisions and source/build versions below describe their original scope.

**As of 12 October 2026:** ECO-01 native money/pricing/selected UI trade, ECO-02 trader policy/supplies/selected supplied consumers, and ECO-03 practical consolidation/bounded audit are complete within their available-source scope. The [development reference](development-reference.md) is usable within those boundaries. Full effective installed integration is **partial**; runtime is **untested** and deferred.

| Completed area | Canonical record | Boundary |
| --- | --- | --- |
| Money, virtual cost, quotes and selected accounting | [ECO-01](../../08-research/investigations/2026-10-11-ECO-01-native-trade.md), [reference](native-trade.md), [APIs](../../02-lua-api/economy/money-cost-api.md) | Source-delta hazard, UI/direct-native and callback/request distinction retained |
| Policy, stock requests and supplied consumers | [ECO-02](../../08-research/investigations/2026-10-12-ECO-02-trader-configuration.md), [reference](trader-configuration.md), [APIs](../../02-lua-api/economy/trader-policy-api.md) | Missing core definitions, profile selection and installed order not inferred |
| Practical synthesis and consistency audit | [ECO-03](../../08-research/investigations/2026-10-12-ECO-03-economy-consolidation.md), [verification](../../08-research/verification-2026-10-12-v0.1.62.md) | Selected available-source first-edition stopping point |

## Effective contracts still open

| Contract | Required evidence |
| --- | --- |
| Actual stock, conditions and unlocks | Winning trader LTX/includes/inheritance, conditional-selection helpers, logic/binders, reputation/goodwill/progression and item section/cost configurations |
| Pricing and discounts | Winning trade_manager get_buy_discount/get_sell_discount, game_difficulties/economy configs and overrides; caller direction and numeric policy |
| Supply refresh and persistence | Core trade_init/update, cleanup, replenishment and timestamp writes; save/load reconstruction and late/nearby/offline scheduling |
| NPC markets and equipment | axr_trade_manager, helper/producer/caller cadence, native/derived paths actually used; stock consumption, funds and inventory acceptance |
| Transaction observation and recovery | Effective callbacks, before/donation hooks, reentrant behavior, pending item events, refunds/retries and lifetime/ID cleanup |
| Build/profile correspondence | Executable/configuration identity, winning files and monkeypatch/module order; uploaded snapshots are not installed winners |

Collection uses the existing [effective-profile provenance requirements](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md). [Inventory](../inventory/source-completion-status.md), [factions](../factions/source-completion-status.md) and [persistence](../persistence/source-completion-status.md) overlap these requirements.

## Stopping rule

Mark full installed economy integration development-reference ready at source level after relevant winning manager/configuration/consumer chains are traced and reconciled with the selected native source. Runtime remains a separate phase, resumed explicitly with identified build/profile, representative prices/gates/restock, money/item acceptance, edge inputs and save/load/level-change observations recorded.

Every derived item Cost, every native NPC/artefact/task variant, mechanic upgrades, multiplayer, exhaustive converters/build combinations and malformed-input robustness are optional later depth unless a concrete question needs them. A conserved faction market or safe loadout recipe is not established by completing this bounded source pass. Next general foundation: actor/NPC health, damage, death, condition/immunity/effects and callback boundaries. [Roadmap](../../ROADMAP.md).
