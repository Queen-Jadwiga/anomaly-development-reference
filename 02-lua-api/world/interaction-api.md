# Selected use zone level-changer and marker APIs

> ADR document set: **v0.1.81**. Research revisions and source/build versions below describe their original scope.

- ID: WORLD-03-API
- Subsystem: world interaction/navigation
- Research revision: v0.1.72
- C++/Lua owners: CScriptGameObject → game_object; CLevel → level; native use/zone/changer/map managers are distinct owners
- Interface kind: selected Lua exports, native callbacks and native/bundled callers
- Baseline/provenance: ENGINE1011 [manifest](../../evidence/manifest.md); archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`
- Source status: source-confirmed selected definitions/registrations/callers
- Runtime status: untested; deferred
- Build scope: inspected game registrars; INPUT_CALLBACKS/ENGINE_LUA_ALIFE_UPDAGE_MANAGER_CALLBACKS and singleplayer branches qualified; executable/compiler/profile correspondence unknown
- Evidence: [U/T/M source ledger](../../evidence/world/interaction-transition-markers-2026-10-12.csv), [behavior and file/line citations](../../04-game-systems/world/interaction-transitions-markers.md)
- Example status: none; call shapes are source contract notation
- Last reviewed: 2026-10-12

## Use and zone contracts

| Lua shape / callback | Selected return, owner and failure boundary | Evidence |
| --- | --- | --- |
| target:use(user_game_object) | bool; target virtual use runs first, actor-user box/owner paths request void UI then return true; generic actor-target path can return false after effects; user pointer must be valid | U04–U07/U10 |
| target:set_tip_text(string); set_tip_text_default(); set_nonscript_usable(bool) | void, usable-type checked; tip/control setter is not an action receipt or automatic persistence | U04/U09/U11 |
| object:set_callback(callback_enum,functor); (...,functor,object); (callback_enum) | void, install bound/unbound callback or clear slot; not independent multi-listener registration | U09/U10 |
| callback.use_object(used_object,user) | Void callback on used object after selected door-block gate; ActorUse ignores native use bool; no generic bool veto from listener | U02/U04/U12 |
| zone:active_zone_contact(u16) | bool sampled contact-list membership; wrong type false; CScriptZone requirement | U14/U16/U11 |
| restrictor:inside(Fvector); inside(Fvector,float epsilon) | bool sphere/shape intersection; one-vector form uses EPS_L; wrong type diagnoses/false | U06/U11/U13 |
| callback.zone_enter(zone,object); callback.zone_exit(zone,object) | Owned by zone; sampled membership timing and ordinary-delete/release paths differ; not exactly-once guarantee | U12/U14/U15 |

These game_object registrations share a wrapper class but their native receiver casts differ. CLevelChanger is an independent GameObject/Touch class, not a CScriptZone/CSpaceRestrictor merely because its server description inherits the restrictor schema. Physical key, actor-use and Lua forced-use routes are not equivalent. Read [behavior](../../04-game-systems/world/interaction-transitions-markers.md) before choosing them.

## Level-changer controls

| Lua shape | Return / mutation limit | Evidence |
| --- | --- | --- |
| changer:enable_level_changer(bool) | void; wrong type no-op; writes client enable flag used by dialog presentation, not silent-contact packet gate | U11/T01–T03/T05/T06 |
| changer:is_level_changer_enabled() | bool; wrong type false; not a universal travel-permission query | U11/T05 |
| changer:set_level_changer_invitation(string) | void; wrong type no-op; changes invitation text, locally serialized with enable flag | U11/T04/T05 |

No destination-change Lua method or direct travel recipe is inferred from these controls. Native travel sends M_CHANGE_LEVEL to server acceptance/autosave/reconnect; the selected optional before-change hook receives a NET_Packet pointer before changing=true and may affect the request. It is not an arrival callback. Packet/actor/current-world lifetime, save failures and winning installed wrappers remain qualified. T08–T13; [persistence](../../04-game-systems/persistence/development-reference.md).

## Marker call shapes

| level export | Exact selected input and return | Key limit | Evidence |
| --- | --- | --- | --- |
| map_add_object_spot | (u16 id,string type,string text) → void | Append permits duplicates; XML can set serialization; callbacks precede explicit hint | M01/M02/M07 |
| map_add_object_spot_ser | Same → void | Forces Serializable after Add callbacks and hint | M01/M02 |
| map_change_spot_hint | (u16,string,string) → void | First match; absent marker no-op | M01/M04 |
| map_remove_object_spot | (u16,string) → void | First match, task/UI release then deferred deletion/notification | M01/M03/M16/M17 |
| map_remove_all_object_spots | (u16) → void | All types for this numeric ID; not campaign/generation identity | M01/M03 |
| map_has_object_spot | (u16,string) → u16 0/1 | Numeric return, not bool; zero is truthy in Lua; no visibility guarantee | M01/M04 |
| map_get_object_spot_static / map_get_object_minimap_spot_static | (u16,string) → borrowed UI pointer/null | Existing first marker's widget can itself be null; deletion/unload invalidates retention | M01/M11 |
| map_get_object_spots_by_id | (u16) → array of {spot_type,text} | One row per registered marker; no forced fresh update | M01/M04 |
| map_get_all_object_spots | () → array of copied metadata/last-position rows | Empty table if no game level; cached location/pose, not a fresh map query | M01/M11 |

Pointers are marker-owned; copied enumeration tables do not transfer native ownership. Added actor/global callbacks are synchronous within manager Add; removals are queued and later delivered through the global hook. Missing sinks/reset can discard notices. Serializable, actual, enabled pointer/spot, XML visibility and drawn state are independent. Stored fields and current XML reconstruction do not preserve an original TTL deadline. M02–M15.

## Lifetime, persistence and reproduction limits

No ownership adoption is added by these registrations. Receiver/object IDs and wrapper pointers follow existing [A-Life lifetime](../../04-game-systems/alife/lifecycle-state-reference.md) rules; SAFE_WRAP retains its [WORLD-02 forwarding qualification](spatial-api.md). Dynamic object release, map destruction and registry rebinding invalidate pointers even when an ID is later reused. Effective callback dispatcher, UI/map XML, binder/state helpers, destination definitions and addon replacements remain open. Full inheritance/export/build coverage and every interactable/relation marker policy are outside this selected pass.

Source/hash/range/symbol, native order and documentation checks are recorded in [verification](../../08-research/verification-2026-10-12-v0.1.72.md). No runtime-tested usage examples, game build or installed transaction guarantees. [World guide](../../04-game-systems/world/development-reference.md), [status](../../04-game-systems/world/source-completion-status.md).
