# Actor booster and modifier Lua contracts

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

- ID: GAME-02-API
- Subsystem: actor/NPC gameplay state
- C++/Lua owner: CActorCondition derived from CEntityCondition; SBooster
- Interface kind: selected class exports and helper functions
- Baseline/provenance: ENGINE1011; [manifest](../../evidence/manifest.md)
- Source status: source-confirmed selected registrations/bodies with accessor build mismatch
- Runtime status: untested; deferred
- Converter/lifetime scope: borrowed live condition/wound objects; no exhaustive nil/enum/float/compiler audit
- Example status: none; receiver acquisition and safe mutation recipe not established here
- Last reviewed: 2026-10-12

A05–A12 in [ledger](../../evidence/gameplay/actor-effects-2026-10-12.csv); [reference](../../04-game-systems/gameplay/actor-effects-equipment.md).

| Export | Native interface | Limit |
| --- | --- | --- |
| SBooster() | Struct constructor | Initializes time=-1 only; set type/value/time explicitly |
| ApplyBooster(B, section) | bool helper → actor ApplyBooster | true can mean ignored nonpositive value or weaker product; no replacement receipt |
| BoosterForEach(functor) | void; callback(type,time,value), true stops | Header returns map by value, helper binds non-const reference; build/authoritative iteration unresolved |
| ClearAllBoosters() | void; subtract parameters, clear accessed map | Same accessor mismatch; not a verified cancellation helper |
| WoundForEach(functor) | void; callback(wound), true stops | Direct vector iteration, borrowed wound lifetime; no mutation-safety guarantee |
| BoostHpRestore / BoostPowerRestore / BoostRadiationRestore / BoostBleedingRestore | void(float) | Raw additive rates; awake/sleep counterparts changed, no timed record |
| BoostMaxWeight | void(float) | Add to carry-weight boost, not instantaneous inventory transfer |
| Boost*Immunity / Boost*Protection | void(float) | Raw accumulators; no automatic cap/timer/accounting |

Selected registrations expose these on CActorCondition with its CEntityCondition base; they do not provide an NPC consumable policy. The GetCurBoosterInfluences declaration/helper mismatch is preserved as source/build uncertainty rather than fixed in research. GetBoosterValue's native implementation looks up known section name and returns time when bool=true, otherwise value, or zero when absent; no Lua registration for that method is claimed by this subset. Full converter/overload/class acquisition coverage remains later depth.

Actor food change accumulates before UpdateSatiety; base NPC satiety no-op is still described in [GAME-01 APIs](condition-api.md). Persistence reapplies saved booster records through server parameter dispatch; idempotent full reconstruction and effective timed medicine remain unresolved. No safe save-edit, cancellation or healing example is supplied.
