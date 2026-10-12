# Live condition property and change contracts

> ADR document set: **v0.1.73**. Research revisions and source/build versions below describe their original scope.

- ID: GAME-01-API
- Subsystem: actor/NPC gameplay state
- C++/Lua owner: CScriptGameObject / game_object → CEntityAlive condition
- Interface kind: registered native properties and methods
- Baseline/provenance: ENGINE1011; [manifest](../../evidence/manifest.md)
- Source status: source-confirmed selected wrapper/body/registration paths
- Runtime status: untested; deferred
- Converter policy: float/property conversion and live wrapper lifetime not exhaustively audited
- Build scope: selected snapshot; installed correspondence unknown
- Native inheritance: base condition semantics differ from actor overrides
- Example status: no runtime-tested invocation recipe
- Last reviewed: 2026-10-12

[Ledger G01–G03/G07/G16–G18](../../evidence/gameplay/native-condition-2026-10-12.csv), [behavior](../../04-game-systems/gameplay/native-condition.md).

| Lua interface | Native getter/setter or method | Selected contract |
| --- | --- | --- |
| health | float GetHealth / void SetHealth(float) | Read/direct write current condition health; setter does not clamp or invoke Die |
| change_health(delta) | void ChangeHealth(float) | Accumulate pending delta; negative values subject to server harm gate |
| power / radiation / psy_health / morale | float getters / void setters(float) | Direct base fields; deferred change methods are distinct |
| change_power / change_radiation / change_psy_health / change_morale | void changes(float) | Pending accumulators committed by condition updates |
| satiety / change_satiety | float getter / void setter/change(float) | Base getter 1 and setter/change no-op; derived actor behavior separate |
| bleeding | float GetBleeding / void ChangeBleeding(float) | Setter changes wound incarnation, not an assigned bleeding-speed field |

The forwarding macros dynamic-cast the underlying object; failed getters log/return configured fallback -1 and failed void setters log/return. These selected bindings use direct property/member registration, not a claimed universal SAFE_WRAP policy. None returns a damage/heal/death completion receipt. Pending changes can be discarded at the first invalid-time update, while health <= 0 causes base UpdateCondition to return. Direct field writes do not reverse AlreadyDie, membership or corpse cleanup. G01–G03/G16–G18.

Optional before-hit callback _G.CBeforeHitAfterCalcs receives a temporary mutable script hit, target wrapper and bone ID; supplied relay exposes on_before_hit_after_calcs. It is not a bool veto and is not after final health/death settlement. Do not retain the temporary hit or nil its required draftsman. Detailed copied fields, branch scaling and attribution limits are in the [reference](../../04-game-systems/gameplay/native-condition.md#hit-type-and-mutation-boundaries), G04/G19/G20.

Persistence and live/server authority are separate. Whole-profile scripts, callback order, actor/derived conditions, converter failures and runtime remain unresolved. No safe resurrection, direct kill or NPC medicine recipe follows from these property names.
