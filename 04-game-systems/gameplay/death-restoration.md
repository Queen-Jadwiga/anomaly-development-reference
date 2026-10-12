# Derived death and condition restoration

> ADR document set: **v0.1.72**. Research revisions and source/build versions below describe their original scope.

- ID: GAME-03
- Subsystem: actor/NPC gameplay state
- Research revision: v0.1.65
- Source status: source-confirmed selected derived/native/server/supplied paths
- Runtime status: untested; deferred
- Baselines/provenance: ENGINE1011/BETA150; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

[Ledger R01–R19](../../evidence/gameplay/death-restoration-2026-10-12.csv), [investigation](../../08-research/investigations/2026-10-12-GAME-03-death-restoration.md). IDs are local to this ledger. [GAME-01](native-condition.md) owns base hit/death requests; [GAME-02](actor-effects-equipment.md) owns actor effects. This pass extends selected actor/stalker/base-monster death and server/live/custom-data restoration. Every species override, whole installed callback profile and safe revival remain outside scope.

## Death callbacks sit inside derived cleanup

GAME-01 traces KillEntity→GE_DIE→virtual Die and the compile-guarded actor-before-death interception. CEntityAlive performs faction KILL action, inherited CEntity death/membership change, then eDeath, followed by killer assignment/sound/physics work. That callback is inside a larger derived call chain, not its final barrier.

| Selected owner | Before inherited death | After inherited death and therefore after inherited eDeath |
| --- | --- | --- |
| CAI_Stalker | Movement death, wounded/killed notification, animation, sound and hammer state | Optional holder detach, slots marked not useful; conditional active-weapon ammo destroy requests |
| CCustomMonster | None in this small override | Actor visibility changed |
| CBaseMonster | State-manager critical finalization, aura shutdown and anti-aim notification | Death sound, monster-squad removal, grouping reset and controlled-monster notification |
| CActor | Optional holder detach | Server inventory slot/ruck processing, active item drop/grenade handling and belt evacuation |

R04–R07. Stalker notification/animation occurs before its inherited call, while slots/ammo processing follows it. The ammo branch requires an active slot, item and weapon; it sends GE_DESTROY for inventory sections in that weapon's ammo-class list. No demonstrated all-items drop, universal loot rule or immediate successful removal follows. Actor processing preserves the non-active outfit in the selected slot loop and requests/drop-marks or rucks other entries according to branches. [Inventory removal phases](../inventory/consumption-destruction.md) still apply.

Neither eDeath nor a health <=0 test certifies completion of derived squad removal, ammo cleanup, item-event delivery, server release or addon ID-keyed bookkeeping. A mod listener that performs those actions again risks duplication unless it owns a separate, explicit lifecycle. This is design guidance from the call order, not tested callback-safe mutation policy.

## Server health has its own persistence channel

CSE_ALifeCreatureAbstract owns fHealth. STATE_Write retains team/squad/group, health, restrictions, killer ID and death time. STATE_Read has version gates: health only above 18, old values divided by 100 below 115, killer above 94, death time above 115. UPDATE_Write/Read also retain health and movement/team data. The object registry restores spawn STATE then the saved M_UPDATE through virtual UPDATE_Read; there can therefore be a later saved-update health write after spawn-state reading. Full inherited/derived packet layout matters. R13/R14.

The server set_health helper verifies against positive health with a known killer, then writes fHealth. on_death under XRGAME_EXPORTS sets game death time and fHealth=-1. CSE_ALifeMonsterAbstract::kill instead unregisters an A-Life group member when present and calls set_health(0); that body does not call live Die or the server on_death body. These are distinct operations and do not themselves demonstrate object release, live callback execution or a safe revival. R13.

The selected server Lua health() and alive() are getter methods; health() is not the live game_object health property and no setter overload is registered in that block. Server monster kill() is registered separately. Lua wrapper/derived on_death dispatch and actual installed scripts remain required; do not assume every script on_death call invokes only the native base. R17/R18; [existing A-Life API coverage](../../02-lua-api/alife/README.md).

## Live spawn and binder order

| Spawn stage | Selected behavior | Observation limit |
| --- | --- | --- |
| CEntityAlive::net_Spawn entry | Reinitialize condition before inherited spawn | Pending deltas/wounds and base fields reset according to GAME-01 |
| CEntity::net_Spawn | Copy server health/killer before inherited base spawn; register living membership; clear inconsistent live killer on positive health | Does not rewrite server killer; values can still be changed by later load/scripts |
| CGameObject base spawn | Load retained client_data when present | Native virtual load precedes script binder load |
| CEntityAlive condition load | Dispatch virtual condition serializer/load | Actor condition subclass adds actor-specific fields |
| CCustomMonster after inherited spawn | Copy server get_health again and set death time when nonalive | Binder's direct live health assignment is overwritten in this selected monster/stalker chain |
| Actor spawn chain | Inventory owner then inherited alive/entity spawn | No analogous post-binder actor health overwrite is established in the inspected section |

R01–R04/R08–R10. Crucially, Entity copies server health **before** CGameObject/binder processing, while CustomMonster copies it again **after** that processing. A single universal “binder load sees final health” rule would be wrong. Live membership registered earlier is not recomputed by every later health setter; divergence and effective reconciliation remain open. The actor row is a scoped finding, not proof that no later actor script can write health.

Selected stalker net_Export writes current live health and remote net_Import sets it. Actor import applies received health only under OnClient. These are update paths with full inherited framing and locality constraints; they are not the condition custom serializer or evidence that direct health assignment synchronously updates all server/live representations. [A-Life state return and persistence](../alife/lifecycle-state-reference.md) and [native save pipeline](../persistence/native-save-load-pipeline.md) supply the wider transport context. R15/R16.

## What client condition data retains

Base condition custom data stores an alive marker, then power/radiation/morale/psy health and wound count/records only when the marker is alive. Health is omitted from this body; the selected server spawn/update channel supplies it separately. Omission from this one serializer is not evidence that whole-save health is lost. Its loader invalidates time and reconstructs fields/wounds in the alive branch. A dead marker does not itself overwrite health or clear every prior field. R11/R13/R14.

CEntityAlive save/load forwards to inherited state then conditions(), dispatching the actual derived condition object. CActor's save/load likewise forwards its inherited chain before inventory/actor custom fields, while its condition factory constructs CActorCondition. Thus actor medicine and booster data are reachable through virtual condition serialization rather than requiring a direct CActor::save call to ActorCondition::save. R02/R09/R10/R12.

Actor condition adds alcohol/flags/satiety, all medicine fields and typed booster value/time records. On load it inserts each record and calls BoostParameters; there is no local subtract/clear of old boosts first. Actor reinit only calls base reinit, resets limping and satiety in that body; it does not clear the booster map or reverse all modified coefficients. On a fresh object the constructor/init path can differ from repeated reuse. Whole actor reload/configuration/reset order is not proved idempotent by these serializers. Saved duplicate types or repeated calls must not be treated as harmless. R12; [GAME-02 source/helper limits](actor-effects-equipment.md).

The first invalid-time update clears selected pending deltas under GAME-01. Saving current values, pending effects and later derived initialization are separate phases. Wound count is u8 in the base body; arbitrary malformed counts/data or universal full-condition reconstruction are not certified by normal save format.

## Supplied offline death and effective integration

The BETA150 selected defeat path calls set_battle_outcome, which invokes game_relations.offline_npc_on_death and news, then invokes server victim:on_death. A separate nearby squad-removal block is commented in that inspected path. Earlier WAR-002 already documents the wider offline fight/disposition branches; do not generalize this one path to all offline deaths. R19; [Warfare research](../warfare/README.md).

Those server/script actions do not establish traversal through live actor/stalker/base-monster Die, native eDeath or their post-callback cleanup. Online/offline casualty ledger convergence needs effective server script classes, squad storage/callback producers and release handling. Native health and callbacks alone cannot deduplicate CtZ strategic casualties.

## Carried questions and completion boundary

GAME-02's timed-medicine record is confirmed in the actor restoration chain, but serialization still does not supply its missing advance/application consumer. Its booster map accessor/reference mismatch remains a compiler/executable question; restoration does not fix it. No source changes or runtime fault claims are made.

Collect winning actor/NPC binders, condition/medicine scripts and item/creature configs, server script class overrides, death/wounded/loot handlers, dispatcher/startup order, squad registry/release consumers and storage/migration logic. Identify actual executable/build flags and restoration profile. Restore authoritative objects and their membership before interpreting unavailable clients or transient health as permanent casualty/revival.

GAME-03 is complete within this selected native/server/supplied boundary. Effective gameplay-state integration remains partial; broader species-specific behavior and runtime remain open. Next practical gameplay-state consolidation and bounded audit, preserving medicine/helper/restoration questions. No CtZ implementation or tested resurrection/death recipe is supplied. [Roadmap](../../ROADMAP.md).
