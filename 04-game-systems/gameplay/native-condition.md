# Native health and condition hit processing

> ADR document set: **v0.1.63**. Research revisions and source/build versions below describe their original scope.

- ID: GAME-01
- Subsystem: actor/NPC gameplay state
- Research revision: v0.1.63
- Source status: source-confirmed selected base/live/native and supplied callback paths
- Runtime status: untested; deferred
- Baseline/provenance: ENGINE1011; [environment record](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-12

The first pass covers live condition fields, queued changes, selected hit mitigation and death-request phases. Actor-specific survival/boosters/equipment, all derived creature death paths and full server/client persistence remain later work. [Ledger G01–G21](../../evidence/gameplay/native-condition-2026-10-12.csv), [investigation](../../08-research/investigations/2026-10-12-GAME-01-native-condition.md), [Lua contracts](../../02-lua-api/gameplay/condition-api.md). The uploaded archive pins source, not executable/profile correspondence or installed scripts.

## Existing coverage and distinct state owners

[Faction attack/kill actions](../factions/action-goodwill.md) already documents relation/reward attempts and selected death callback order. [A-Life callbacks](../alife/callback-phase-reference.md) and Warfare offline combat describe casualty phases; offline server death is not evidence of traversing this live hit path. [Inventory consumption](../inventory/consumption-destruction.md) already traces UseBy effects before item depletion/removal. This pass extends condition processing without replacing those findings.

CEntityConditionSimple owns health and maximum health. SetHealth directly assigns the field without a clamp, harm gate, hit attribution or Die call. CEntity g_Alive is `GetfHealth() > 0`, not proof of completed death bookkeeping. CEntityCondition owns pending deltas, power, radiation, psy health, morale, wounds and hit attribution; its CanBeHarmed requires OnServer and m_bCanBeHarmed. Actor-derived condition behavior is separate. G01/G13/G21.

| Operation | Selected base behavior | Boundary |
| --- | --- | --- |
| SetHealth / Lua health assignment | Direct health write | Not damage processing, health-event receipt, resurrection or immediate death callback |
| ChangeHealth / change_health | Validate float; accumulate delta only if CanBeHarmed or delta > 0 | Getter does not immediately include pending delta; negative change can be suppressed |
| SetPower / radiation / psy health / morale | Direct field writes | Base setter does not normalize or invoke item/medicine effects |
| Corresponding Change methods | Accumulate pending deltas | Commit depends on update/derived gates |
| Base satiety getter/setter/change | Getter 1, setters/change no-op | Actor survival cannot be inferred from generic NPC satiety |
| ChangeBleeding | Incarnate each wound; mark zero-size wounds for destruction | Not an assignment to a bleeding-rate field; cleanup follows separately |

G01/G02/G07/G16/G17; [API page](../../02-lua-api/gameplay/condition-api.md). Direct writes and queued changes are different tools and neither is a general safe kill/heal/revive recipe.

## Time update and commit

Base UpdateConditionTime uses game time in single-player and server time otherwise. Positive elapsed milliseconds become seconds; non-forward time gives zero delta. On first invalid-time update it sets zero time and clears pending health/power/radiation/circumspection/morale, but not psy delta in that body. Therefore a pending change around initialization/load is not universally retained. G03.

UpdateCondition returns immediately when current health <= 0. Otherwise it observes lethal pending hit damage through OnCriticalHitHealthLoss or noncritical negative pending damage through OnHitHealthLoss; adds bleeding/restoration, checks critical wound loss; updates power/radiation, checks critical radiation loss; then psy health/morale. These are pre-final-write hooks, not a completed-death notification. G03/G07.

If Device.fTimeGlobal exceeds m_fInvulnerableTime, health commits. When current health > killing_hit_treshold and current+delta < 0 (strictly negative), it assigns last_chance_health and advances the invulnerability time; otherwise writes current+delta. At exact zero that last-chance predicate is false. During the timer's non-expired interval the health write is skipped, but all pending deltas are still reset after other fields are applied. Final health clamp is [-0.01, max_health]; power/radiation/morale/psy fields get their own bounds. This mixed game/server elapsed-time versus Device timer behavior is literal source, not a guaranteed survival feature under installed values. G02/G03.

Passive base health includes summed wounds (bleeding speed clamped 0–10), elapsed bleeding loss gated by CanBeHarmed, and configured restoration plus boost. Radiation decay and radiation-health loss operate on existing radiation; psy health and morale have separate restoration. Base UpdatePower is empty. Actor override can return for god mode, dead actors or nonlocal/non-current-view actors and performs additional survival behavior; full actor effects remain GAME-02 work. G07/G21.

## Selected live hit path

1. CEntityAlive copies SHit, normalizes Wound_2 to Wound, and computes damage/wound bone scales.
2. ConditionHit records original hit source pointer/ID, applies outfit then helmet HitThroughArmor if present, and dispatches by the original switch hit type.
3. Selected branches apply hit-type immunity minus boost; telepathic/chemical/radiation protection is first subtracted and clamped at zero. An optional _G.CBeforeHitAfterCalcs mutates a temporary script hit before pending changes are recorded.
4. Branches update pending condition damage; permitted wounds can be accumulated while current GetHealth > 0.
5. CEntityAlive sets condition delta time to zero and calls inherited Hit. CEntity::Hit dispatches virtual CalcCondition; the alive override commits UpdateCondition and returns GetHealthLost. Hit signals and the local lethal gate follow.
6. Only after inherited hit processing does the selected alive single-player victim/attacker gate register the faction fight/action already covered by FAC-04.

G04–G11; [faction actions](../factions/action-goodwill.md). Derived actor/stalker/monster Hit and equipment internals can add earlier/later policy; this chain is not every final damage formula.

## Hit-type and mutation boundaries

| Hit type | Selected base condition result | Qualification |
| --- | --- | --- |
| Telepathic | Psy loss, health share, power loss; no wound | Health harm gate does not block every other field |
| Burn / light burn | Health share with bone scale, power loss; no wound | Burn immunity branch used |
| Chemical / shock / strike | Health share, power loss; no wound | Protection subtraction is present for chemical, not every branch |
| Radiation | Pending radiation, no wound; returns early | Does not update m_fHealthLost in this branch |
| Explosion | Health share, power loss; wound flag may survive | No bone health scale in this selected branch |
| Fire wound / wound | Health share with bone scale, power loss; wound flag may survive | Wound uses separate bone scale and random 0.5–1.5 multiplier |

G04/G06. No universal clamp of `immunity - boost` to nonnegative is present, so nonnegative damage cannot be promised for arbitrary configs/boosts/scripts. GetHitImmunity is a raw coefficient lookup; default coefficients are 1, loaded from named immunity fields, and light-burn mirrors burn. Higher coefficient multiplies damage rather than inherently granting more protection. AddImmunities adds supplied coefficients with zero fallback. G14/G15.

The optional callback constructs CScriptHit, multiplies power by a positive branch hit_part, calls Lua with hit/target/bone ID, divides by that original positive factor, then ApplyScriptHit copies power/impulse/direction/type/draftsman/weapon back. It does not re-enter the switch or recompute original attribution, outfit mitigation or local bAddWound. Changing type/source is therefore not equivalent to starting a new hit of that type/source. ApplyScriptHit dereferences draftsman without a local null guard; valid live references are required. The temporary hit is stack-lifetime data, not a persistent handle. G04/G19.

The supplied callbacks_gameobject registers on_before_hit_after_calcs and relays the same mutable hit to SendScriptCallback; it has no ret_value veto convention in this body. Listener order/winning relay and installed overrides remain unproved. The native functor is optional; absent functor skips it. The phrase after calculations refers to this branch stage, not all future wound, condition, health and death processing. G20/G04.

## Death request versus completed cleanup

The base hit local lethal gate requires !g_Alive, !AlreadyDie and unknown killer ID before KillEntity(whoID). The scheduled alive update separately updates condition/time/wounds and requests KillEntity when local, nonalive and not AlreadyDie, using stored last hit source when available, otherwise self. G10/G11.

KillEntity has a compile-guarded ACTOR_BEFORE_DEATH_CALLBACK interception in single-player for the actor unless bypassed: leave holder, invoke eActorBeforeDeath and return. The normal path records killer/death time and, if not destroying, sends GE_DIE only on server. The event consumer resolves the killer object and calls virtual Die. CEntity::Die writes -1 health and unregisters live team/squad/group membership; CEntityAlive's override performs faction KILL action before inherited Die, then eDeath, then killer assignment and sound/physics work. This is not permanent server release or completed addon casualty cleanup. G09/G12; [existing faction/death boundaries](../factions/action-goodwill.md).

Selected CEntityAlive::Die accepts a missing killer for the Lua callback argument, but later its non-destroyed single-player killer-event path dereferences who->ID without a local null guard. The event lookup may return null; caller/derived invariants and effective handling must be established before calling this a null-safe kill recipe. Actor-before-death build activation/dispatcher and every derived override remain later work. G09/G12.

## Persistence boundary and next pass

The base condition serializer writes an alive marker and, only when alive, power/radiation/morale/psy health plus a u8 wound count and wound records. Its paired loader invalidates time and reconstructs those fields/wounds only under that marker. Health itself, pending deltas, full attribution, active invulnerability and all boosters are not serialized by these selected bodies; other entity/derived/server storage must be traced separately. Do not infer loss from omission in this one serializer or claim that health assignment is already persisted everywhere. G07; [general persistence](../persistence/development-reference.md).

GAME-01 is complete within its selected base-condition/hit boundary. Next GAME-02 actor-specific survival/boosters and equipment mitigation; then derived death and server/client condition restoration plus effective-script consumers, followed by consolidation/audit. For CtZ, a live health reading is distinct from strategic readiness, resource stock, server creature health and confirmed casualty identity. No CtZ behavior is changed and no runtime-tested healing/loadout/kill recipe is supplied.
