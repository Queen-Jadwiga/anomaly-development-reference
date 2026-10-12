# Consumption and destruction Lua contracts

> ADR document set: **v0.1.67**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-03-API
- Subsystem: inventory
- C++/Lua owner: CScriptGameObject/game_object; separate CEatableItem class exports
- Interface kind: native wrappers and registered class accessors
- Baseline: ENGINE1011; [manifest](../../evidence/manifest.md)
- Source status: source-confirmed selected bodies/registrations
- Runtime status: untested; deferred
- Build scope: inspected exports; actual binary/profile unknown
- Native/Lua inheritance: CEatableItem native derives inventory item; its inspected class registration does not declare a Lua base or constructor
- Converter/lifetime policy: existing live wrapper, u8 and BOOL conversions; exhaustive nil/dangling/range conversion audit not performed
- Example status: none
- Last reviewed: 2026-10-11

[D-ledger](../../evidence/inventory/consumption-destruction-2026-10-11.csv); [phase reference](../../04-game-systems/inventory/consumption-destruction.md).

| Export | Native signature/return | Contract |
| --- | --- | --- |
| game_object:eat(item) | void eat(CScriptGameObject* item) | Null/non-item/non-inventory-owner log and return; calls native Eat directly and discards bool. Effects can precede false internally; not actor ClientEat gate |
| game_object:destroy_object() | void DestroyObject() | Forwards native request; no immediate-removal success result |
| CEatableItem Empty() | bool Empty() const | Remaining uses exactly zero |
| CanDelete() | bool CanDelete() const | Removal flag equals 1 |
| GetMaxUses()/GetRemainingUses() | u8 accessors const | Native counters; not schema/durability or safe reuse guarantees |
| SetRemainingUses(value) | void SetRemainingUses(u8 value) | Assigns only when value <= max; no success result, no max setter in selected registration |

D03/D13–D17. Both game-object methods register through SAFE_WRAP; earlier [ownership APIs](ownership-api.md) describe its forwarding/debug limit. CEatableItem also exposes removal/full/empty weight fields read-write and Weight/Cost methods; that capability does not establish a use transaction. No ownership-adoption/persistence policy follows from accessors.

Native Eat returns bool and ClientEat returns bool with different semantics: effects versus request, and possible post-effect false versus send success. use_object is a native callback enum exported at D18 and invoked for selected actor consumption after UseBy but before empty/drop policy. It is not universal NPC/shared dispatcher or removal completion. D01/D05.

Dependencies: matching native inventory/parent, live wrappers and entity conditions, event authority/transport, delayed drop/destroy processing and effective gate/policy. Full converter, derived item/owner, repeat safety and installed scripts remain open. Verification: signature/body/registration and phase review plus [hash/navigation checks](../../08-research/verification-2026-10-11-v0.1.56.md).
