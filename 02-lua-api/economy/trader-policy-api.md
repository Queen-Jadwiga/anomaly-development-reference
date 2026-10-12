# Trader policy and supplies Lua contracts

> ADR document set: **v0.1.77**. Research revisions and source/build versions below describe their original scope.

- ID: ECO-02-API
- Subsystem: trade/economy
- C++/Lua owner: CScriptGameObject / game_object; selected global functions
- Interface kind: registered native wrappers
- Baseline IDs/provenance: ENGINE1011; [manifest](../../evidence/manifest.md)
- Source status: source-confirmed selected declarations, registrations and bodies
- Runtime status: untested; deferred
- Build scope: inspected snapshot; installed correspondence unknown
- Native/Lua inheritance: dynamic CInventoryOwner cast required for object methods
- Converter policy: float and CScriptIniFile pointer conversions not exhaustively audited; nil/dangling values not certified
- Example status: none; no runtime-tested invocation recipe
- Last reviewed: 2026-10-12

T08–T11 in [ledger](../../evidence/economy/trader-configuration-2026-10-12.csv); [behavior and hazards](../../04-game-systems/economy/trader-configuration.md).

| Lua method | Native signature excluding receiver | Mutation / return |
| --- | --- | --- |
| buy_condition / sell_condition | void (CScriptIniFile*, LPCSTR) | Replace the selected action's explicit entries; assert section exists; preserve its default factors |
| buy_condition / sell_condition | void (float friend_factor, float enemy_factor) | Set default factors only; does not clear explicit entries |
| show_condition | void (CScriptIniFile*, LPCSTR) | Replace empty-value show disables |
| buy_supplies | void (CScriptIniFile*, LPCSTR) | Destroy eligible existing inventory and request randomized stock; no debit or success receipt |
| buy_item_condition_factor | void (float factor) | Write minimum buy condition, not an exponent |
| buy_item_exponent / sell_item_exponent | void (float factor) | Write corresponding price exponent |

Object methods log and return on a failed inventory-owner cast. Successful INI paths dereference the pointer without a local null guard. All return void; registration uses SAFE_WRAP, whose forwarding limits are described in [inventory APIs](../inventory/ownership-api.md). Do not interpret void return or lack of exception as completed stock delivery. Parameters require valid owner initialization and referenced INI/item sections.

Global buy_condition/sell_condition share both overloads; global show_condition shares the INI overload. These mutate the global singleton, with no object cast. No global buy_supplies or scalar setters are registered in the inspected block. Local and global disables veto availability; local explicit, global explicit, then local defaults select factors. Global changes affect shared fallback/veto policy and end at the selected level teardown. Object net spawn recreates local parameters; a full persisted script profile needs separate proof. T01/T05/T08/T10/T15.

Friend/enemy order is literal and differs from the constructor's hostile/friendly field placement. INI parser omission does not mean deny, scalar overload does not replace explicit rows, and supplies do not implement a priced purchase. See the [reference](../../04-game-systems/economy/trader-configuration.md) before integration.
