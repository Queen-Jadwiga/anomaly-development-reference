# Money and base-cost Lua contracts

> ADR document set: **v0.1.76**. Research revisions and source/build versions below describe their original scope.

- ID: ECO-01-API
- Subsystem: trade/economy
- C++/Lua owner: CScriptGameObject / game_object
- Interface kind: registered native wrappers
- Baseline IDs/provenance: ENGINE1011; [manifest](../../evidence/manifest.md)
- Source status: source-confirmed selected declarations/registrations/bodies
- Runtime status: untested; deferred
- Build scope: inspected snapshot bindings; executable/profile correspondence unknown
- Native/Lua inheritance: dynamic inventory-owner/item casts constrain receiver; no exhaustive hierarchy audit
- Converter policy: existing int/u32/live-wrapper conversions; nil/dangling/out-of-range behavior not certified
- Example status: none; source arithmetic illustration in reference is not a runtime-tested example
- Last reviewed: 2026-10-11

Evidence E06–E12 in [ledger](../../evidence/economy/native-trade-2026-10-11.csv); [behavior reference](../../04-game-systems/economy/native-trade.md).

| Lua export | Exact native signature excluding receiver | Return / guard / mutation |
| --- | --- | --- |
| money() | u32 Money() | VERIFY inventory-owner receiver, return live get_money; not server balance getter |
| give_money(delta) | void GiveMoney(int money) | VERIFY inventory-owner; helper saturates signed delta, then infinite-money setter policy applies; nonzero delta invokes setter with event=true; zero delta invokes no setter/event; no success return |
| transfer_money(amount, target) | void TransferMoney(int money, CScriptGameObject* pForWho) | Explicit target-null log/return; VERIFY both inventory owners; source-balance gate then signed-delta algorithm described below; no success return |
| cost() | u32 Cost() const | Dynamic inventory-item cast; failed cast logs/returns numeric zero; calls virtual native Cost, not CTrade GetItemPrice |

All four inspected bindings use SAFE_WRAP. Its receiver forwarding/debug limit is documented in [inventory APIs](../inventory/ownership-api.md); the name does not establish transaction safety, nil conversion behavior or memory ownership transfer. Dependencies/lifetime: valid live wrappers/types, money event/server receiver, profile infinite-money flag and derived item Cost.

TransferMoney uses new-source minus old-source as destination delta, mixed signed/unsigned balance comparison and int conversion; positive small transfers can deduct from both under ordinary target conversion. Unary negation of INT_MIN occurs before widened handling. See E06 and the qualified [source arithmetic analysis](../../04-game-systems/economy/native-trade.md#lua-money-wrappers-literal-hazards). This remains an unverified runtime hazard; do not infer conservation or reliable negative transfer from method/comment names.

Native versus Lua signatures: CTrade::TransferItem(item,bool buying,bool free=false) and GetItemPrice(item,bool buying,bool free=false) are native methods in the inspected declaration (E22), distinct from Lua game_object:transfer_item(item,target), which requests containment transfer and does not call this priced native method. No Lua CTrade method export or optional argument contract is claimed in this pass.

State/persistence/callbacks: live set_money may emit GE_MONEY, selected server consumer writes server trader balance; owner custom save and server STATE are separate. trade_perform_operation is selected trader aggregate callback before UI transfers; trade_sell_buy_item follows per-item request/accounting, not confirmed inventory settlement. E01–E05/E14/E15/E18/E21; [reference](../../04-game-systems/economy/native-trade.md).

Checks: declaration/registration/body and numeric/phase comparison, source hashes/ranges/symbols and repository checks. Installed dispatch/discounts, converter limits, effective overrides and runtime remain open. [Verification](../../08-research/verification-2026-10-11-v0.1.59.md).
