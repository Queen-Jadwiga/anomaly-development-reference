# Actor survival boosters and equipment mitigation

> ADR document set: **v0.1.69**. Research revisions and source/build versions below describe their original scope.

- ID: GAME-02
- Subsystem: actor/NPC gameplay state
- Research revision: v0.1.64
- Source status: source-confirmed selected actor/effect/equipment paths; scoped-source-audit for missing medicine updater
- Runtime status: untested; deferred
- Baseline/provenance: ENGINE1011; [source record](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-12

[Evidence A01–A21](../../evidence/gameplay/actor-effects-2026-10-12.csv), [investigation](../../08-research/investigations/2026-10-12-GAME-02-actor-effects.md), [focused Lua contracts](../../02-lua-api/gameplay/actor-effects-api.md). This extends [GAME-01 base condition](native-condition.md), not a universal NPC survival model. Active GAMMA configs/scripts and executable correspondence are unknown. Full derived death, condition reconstruction and effective consumers remain next work.

## Actor update order and survival

LoadCondition extends the base condition_sect, loads awake/sleep rates and movement costs, and requires ordered begin/end thresholds. SatietyCritical is clamped to [0,1]; that does not establish safe division for both endpoints. Sleep means the actor has info actor_is_sleeping, not every pause or time jump. Actor change_v selects sleeping versus awake rates. A01/A04.

UpdateCondition has distinct god-mode branches: AF_GODMODE_RT updates food/boosters/alcohol before the GodMode return; the other GodMode branch updates boosters then returns. Ordinary updates require alive and local or current-view actor. Movement costs and maximum-power leak apply outside a holder; holding sets maximum power to 1. Then alcohol/psy presentation, satiety and booster updates precede inherited condition commit. Tutorial thresholds, low-health death effector and environmental hit production follow. GodMode is the selected single-player flag test, not the same gate as base CanBeHarmed. A02/A03; GAME-01.

| System | Selected actor behavior | Boundary |
| --- | --- | --- |
| Food | Apply queued satiety, clamp, decay by awake/sleep rate; normalize around critical food level | Critical 0 or 1 can meet zero denominator at corresponding endpoint; no guaranteed finite output for arbitrary config |
| Food effects | Add health delta and satiety-dependent power only if CanBeHarmed and not RT god mode | Multiplayer branch adds power and returns before actor food bookkeeping |
| Movement | Jump consumes a discrete weight-dependent amount; walk uses elapsed time, acceleration/sprint and optional progressive cost; stand uses elapsed time | Direct power write/clamp here, distinct from queued base ChangePower |
| Exhaustion | Single-player max-power leak depends on weight; setter bounds max power separately | Not a strategic squad readiness counter |
| Walk/sprint/limp | Begin/end hysteresis; equality retains prior boolean state | Weight gate and health gate are different tests |
| Low-health effector | Optional configured effect below health 0.05; retains starting health while active, sets -1 when released | Presentation can write health; threshold crossing is not completed death |

A01–A04/A21. Power loss through gear averages outfit, helmet and backpack power_loss inputs (missing slots use EPS), multiplies by 0.5 and adds 0.25, clamps to [0,1]. It is a stamina-loss factor, not armor penetration. A13.

The actor periodically produces radiation/psy/burn GE_HIT requests from material and live monsters within PDA feel-touch. It uses Device time in 0.1-second steps and bounds catch-up by clamping its prior time to now−0.3. These requests run after this selected update's base commit and do not return completed damage. It is not an exhaustive anomaly/zone influence model. A20.

## Medicine and boosters have different lifecycles

Base ApplyInfluence calls pending health/power/satiety/radiation changes, immediate wound incarnation, max-power adjustment and alcohol change, then returns true. Base ApplyBooster is a true-return no-op. Actor ApplyInfluence refuses while its medicine record InProcess (>0 remaining time); negative apply_time_sec delegates to base, otherwise copies the record and sets current time to total. Item use already applies these calls before depletion/removal, as documented in [consumption](../inventory/consumption-destruction.md). A06/A11/A12.

**Timed medicine limit:** a scoped search of all ENGINE1011 src/xrGame C++ files and bundled gamedata scripts finds the medicine record stored/checked/serialized, but no decrement or application update for its current time in that scope. Do not infer effective timed healing from the record or true return. A zero duration is not InProcess and does not enter the instantaneous-negative branch. Installed scripts/build revisions may supply different behavior. This is a missing source edge, not an observed broken medkit. A06/A08/A11/A12.

Actor ApplyBooster ignores nonpositive value but still returns true. Positive effects are keyed by type. With an existing type, a new value×duration strictly smaller than the existing value×remaining-time is ignored with true return; otherwise old parameters are subtracted, the new record replaces the old one and its parameters are applied. It is replacement by that product test, not additive stacking of multiple same-type records. Positive value does not validate type, finite input or positive duration. A06.

UpdateBoosters subtracts delta_time / game_time_factor in single-player (factor 1 otherwise). When remaining time <=0, it reverses parameters and erases the map entry; current-view UI indicators follow. No zero-time-factor guard is in this body, and actor update gates still determine whether it runs. Parameter add/subtract dispatch occurs on server. Restoration modifiers update awake and sleep rates, weight modifies carry boost, and immunity/protection modify separate accumulator fields used by GAME-01. Raw Boost* exports add values without creating a timed map record. A05/A07.

The actor serializer retains alcohol, flags, satiety, all medicine fields, then booster type/value/time; load restores and reapplies each boost. The inspected load body does not first clear/reverse an existing map. Consequently the body alone does not establish idempotent repeated load; whole initialization/binder/restoration must be traced next. Saved maps are not proof that raw manual modifiers or every runtime field is reconstructed. A08.

## Lua helper source/build mismatch

SBooster exports constructor and writable type/value/time, but its constructor initializes only time to -1. A caller must initialize meaningful type/value/time; no safe default effect follows. Actor ApplyBooster returns a bool without a guarantee of replacement, as above. A10/A12.

BoosterForEach and ClearAllBoosters bind a non-const BOOSTER_MAP reference to GetCurBoosterInfluences, while the inspected ActorCondition.h returns BOOSTER_MAP by value. Standard C++ rejects that temporary binding; permissive compiler behavior, a corrected header or executable/source mismatch require verification. Even if accepted as an extension, mutating the copy cannot be assumed to clear the authoritative map. ClearAllBoosters also subtracts effects, so it is especially unsuitable as a verified cancellation recipe under this mismatch. Do not silently alter source or promise these helpers work. A09/A10.

WoundForEach directly iterates the wound vector with true stopping iteration; mutation/lifetime safety is not promised. Other condition exports expose raw additive modifiers and movement thresholds. [Exact API subset](../../02-lua-api/gameplay/actor-effects-api.md).

## Actor hit stages and artefacts

Selected single-player CActor::Hit sets incoming aim_bullet false and validates hit type. God mode writes zero hit power and delegates to inherited Hit. For an alive ordinary actor it constructs a temporary script hit, calls optional _G.CActor__BeforeHitCallback (false returns before the remaining hit path), copies edits, reduces belt artefact damage, sets add_wound=true and invokes the object eHit callback, then delegates to inherited Hit. This eHit observation precedes GAME-01 outfit/helmet/condition processing; it is not post-damage settlement. The callback source cast/dereference has no local null guard in that call. A18; [base hit/callback boundaries](native-condition.md).

HitArtefactsOnBelt accepts an optional script table override; when override=true it returns supplied hit_power directly, without the fallback clamp. Native fallback subtracts each belt artefact's immunity coefficient and clamps [0,flt_max], without multiplying by condition. GetProtection_ArtefactsOnBelt separately sums coefficients×condition. Thus a displayed protection query is not necessarily the selected damage formula. A19.

Periodic artefact restoration does scale by artefact condition, whereas selected outfit/helmet passive restoration sums configured rates without a condition multiplier in that body. Its static accumulated update interval batches the previous elapsed time; these queued changes remain distinct from final health state. Positive artefact radiation uses a boost subtraction and the literal clamp(val,0,val); that is not a proven nonnegative guard when the calculated upper bound is negative. No full installed artefact/armor stat formula is inferred. A19.

## Outfit and helmet armor formulas

GAME-01 applies outfit then helmet. Each piece receives the previous piece's remaining hit power; its own durability loss uses its input hit power times item immunity. If a fire-wound hit meets raw bone armor <=0, the function returns before durability loss. Positive armor is scaled by equipment condition. Current item protection and item durability immunity are separate from character hit immunity. A13–A17.

For the standard fire-wound branch, write BA=raw bone armor×condition and F=hit_fraction_actor. If AP<=BA, output=input×F; otherwise multiplier=(AP−BA)/(AP×APScale), clamped between F and 1. The commented add_wound=false line is inactive, so stopped penetration does not automatically clear the wound flag. A14/A15.

When both fire_wound_param_1 and fire_wound_param_2 exist, an alternate branch is selected. Let v1/v2 be those configured values. AP<=BA/v2 uses F, with F×v1 when AP<=BA×v2. Otherwise use (AP−BA×v2)/(AP×(1.1−BA×v1)); divide that by v1 if AP/2>BA/v2; clamp this penetrating multiplier to [F,1]. The first branch's F×v1 is not similarly clamped. These formulas expose divisors and configuration dependencies; arbitrary zero/negative inputs are not validated by the optional-field presence test. A14–A17.

For non-fire-wound types, protection=hit-type protection×condition; subtract protection×1 for strike/wound/wound_2/explosion and ×0.1 for the other selected types, then floor at zero. Finally apply wear to the piece using input damage, not the mitigated output. Outfit and helmet have selected parallel formulas, but bone tables, owner skeleton mapping, upgrades and winning configs still determine actual values. A14/A15.

## Practical limits and next work

Actor food/stamina, timed boosters, belt effects and current-view bone mapping cannot be assumed to run for NPC squad members or offline server creatures. A displayed equipment stat, item use return, booster return or hit callback is not a delivery/healing/death receipt. For CtZ troop equipment or medical logistics, effective NPC/derived paths must be traced before selecting adapters. No CtZ, Arsenal or ZoneMart code changes are included.

GAME-02 selected actor survival/booster/equipment source pass is complete within scope. Next derived death and server/client condition reconstruction, including medicine/build/helper gaps and supplied effective-script consumers; then gameplay-state consolidation/audit. Runtime remains deferred. [Roadmap](../../ROADMAP.md).
