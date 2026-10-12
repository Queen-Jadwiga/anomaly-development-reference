# Use touch actor transitions and map-marker lifecycle

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

- ID: WORLD-03
- Subsystem: world interaction/navigation
- Research revision: v0.1.72
- Source status: source-confirmed selected native exports/implementations/callers; effective integration partial
- Runtime status: untested; deferred
- Last reviewed: 2026-10-12

ENGINE1011 is the uploaded October 11 archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Upstream commit/executable/profile correspondence remains unknown. [Ledger U01–U16, T01–T13, M01–M19](../../evidence/world/interaction-transition-markers-2026-10-12.csv) pins raw hashes, source paths, counts, symbols and ranges. IDs are ledger-local. [API contracts](../../02-lua-api/world/interaction-api.md), [investigation](../../08-research/investigations/2026-10-12-WORLD-03-interaction-transitions-markers.md).

## Selected use routing and return limits

Level input can stop during precache or through a truthy `level_input.on_key_press` result; subsequent selected routing invokes the current entity's input receiver. Actor key handling separately rejects remote/talking/unauthorized/dead contexts and can let inventory handling consume the action before kUSE reaches ActorUse. This is a selected input chain, not an exhaustive UI/input routing audit. U01/U02: `Level_input.cpp:160–206,551–562`; `ActorInput.cpp:43–95,211–214`.

Actor scheduled update derives its current target pointers from the visible HUD-ray object within 2 m and without an external input handler; the alternate branch clears them. ActorUse consumes those fields, not a durable identified contact. It first handles holder detachment, pickup mode and existing physics capture, then invokes non-item usable-object use. Inventory-box handling and optional standard holder/physics/talk/corpse routes follow their own gates. The usable return is ignored here; nonscript_usable controls standard continuation. The selected corpse branch requires not closed, AlreadyDie and more than 3,000 real-time milliseconds after its level death time. U02/U03: `ActorInput.cpp:525–628`; `Actor.cpp:2010–2086`. [Inventory](../inventory/development-reference.md) and [task/dialogue](../tasks/development-reference.md) remain authoritative for their deeper consumers.

CUsableScriptObject defaults nonscript_usable to true. Its use method verifies the user/owner, rejects the selected blocked-door states before firing `callback.use_object`, and otherwise invokes the **used object's** void callback with used-object and user wrappers, then returns true. That return establishes neither listener success nor a completed door/loot/talk action. The ordinary GameObject use forwards to this method; derived overrides remain type-specific. U04/U05: `UsableScriptObject.cpp:12–68`; `GameObject.h:97–101`.

The Lua `object:use(user)` wrapper is a separate path: first call the target's native virtual use, then if the user is an actor and singleplayer UI is available, route inventory boxes/owners to StartCarBody. Those branches return true after requesting UI; a generic target can finish with false despite its earlier callback effects. No distance/alive/closed preconditions equivalent to ActorUse are added by this wrapper itself. The UI helper can still return early for an existing input receiver or a truthy script veto; it has a void return. Thus forced-use bool is not an authoritative menu-open or paid-action receipt. U06/U07: `script_game_object.cpp:1286–1321`; `UIGameSP.cpp:219–261`.

Selected item pickup follows an independent before-pickup veto, then usable use, then the pickup event; it does not consume the use bool. Tip text and nonscript_usable setters require the usable type; callback install/clear overloads target an object's native callback slot. They do not themselves establish effective listener chains or persistence. U08–U12: `Actor_Feel.cpp:124–156`, `script_game_object_use.cpp:24–48,213–227`, selected registrars.

## Contact lists differ from geometry and movement restrictions

CSpaceRestrictor builds shape geometry and conditionally registers a movement restrictor with the level manager. It has no generic script-zone enter/exit loop in the selected class. CScriptZone derives from that shape plus Feel::Touch and explicitly schedules overlap sampling. CLevelChanger independently derives from GameObject plus Feel::Touch; it is not interchangeable with a script-zone wrapper. U13/U14 and T01: `space_restrictor.cpp:42–141`; `script_zone.cpp:35–96,132–140`; `level_changer.h:16–51`. [WORLD-02 restriction state](spatial-queries-relocation.md) stays separate.

Feel::Touch samples nearby objects, excludes destroyed/noncontact candidates and denied newcomers, inserts an object before its enter callback, and erases it before ordinary delete notification. This is sampled contact membership, not continuous geometry monitoring. Script-zone enter fires on the zone with zone/object wrappers. Ordinary zone delete suppresses its callback when the object is already marked destroyed; net_Relcase has a separate exit path when the object remains in the contact list. The generic Feel release handler also erases and invokes delete. No universal one-enter/one-exit delivery or listener-mutation safety is certified. U14/U15: `script_zone.cpp:60–96`; `xrEngine/Feel_Touch.cpp:28–108`.

`active_zone_contact(id)` requires CScriptZone and queries its sampled list. `inside(position[,epsilon])` requires CSpaceRestrictor and tests a sphere against prepared shape geometry; the one-position overload uses EPS_L. These can differ without contradicting one another. U06/U11/U16: `script_game_object.cpp:1105–1123`, `script_game_object2.cpp:67–80`, registrars.

## Actor travel: trigger, dialog, packet, save, restart

At level-changer spawn, destination graph/node/position/angles and silent mode come from server fields; the client resets enabled=true, default invitation and entrance time, with local restoration later available. Shape contact accepts a living actor. Selected native flow:

1. **Silent contact:** sends M_CHANGE_LEVEL with destination IDs/pose and returns. This branch does not consult m_b_enabled.
2. **Dialog contact:** computes an optional reject pose from patrol points 0 and 1, calls singleplayer ChangeLevel with enabled/invitation values, then timestamps the entrance. A living actor remaining inside can be invited again after the strict five-second test; an already-topmost change-level dialog is not replaced.
3. **Choice:** Show picks enabled/disabled message-box XML and pauses the device. OnOk hides and sends the packet; OnCancel hides and optionally calls MoveActor at the reject pose. OnOk itself has no second enabled check. XML/message handling and installed callers decide whether that path is offered.
4. **Server acceptance:** xrServer invokes game change_level and broadcasts only a true result. Singleplayer delegates to A-Life when present, otherwise returns true. A-Life rejects when m_changing_level is already true; its optional before-change hook sees the packet before ClientSend and before the flag becomes true.
5. **Destination save:** after ClientSend, set changing=true; retain the actor's old server fields; read requested destination into server fields; ClientSave; set torso from angles; temporarily move a holder's server fields if present; update server options to autosave, save, then restore old actor/holder fields and return true.
6. **Client restart:** the received change/reload/load branch clears selected LuaGC tracking and requests MakeReconnect, which defers disconnect/start if no disconnect is pending. This is not destination client readiness or a successful arrival observation.

T01–T12: `level_changer.cpp:39–232`; `UIGameSP.cpp:265–369`; `Actor_Events.cpp:362–378`; `alife_update_manager.cpp:159–246`; `game_sv_single.cpp:234–240`; `xrServer.cpp:578–589`; `Level_network_messages.cpp:306–334`; `Level.cpp:949–975`. The selected A-Life body lacks a universal final destination-validation/transaction rollback result; assertions, hooks, save and restart dependencies retain their own limits. [Persistence](../persistence/development-reference.md), [A-Life spawn readiness](../alife/callback-phase-reference.md) and [WORLD-02 relocation](spatial-queries-relocation.md) supply the linked boundaries. Actor travel is not simulator teleport or squad graph-level notification.

Level-changer local save stores invitation and enabled flag; net_SaveRelevant becomes true for nondefault controls. Server STATE writes destination IDs/pose/name fields and silent flag; reads retain version branches, including silent only above version 116. Lua enable/query/invitation controls silently no-op/return false on wrong type. Disabling this client flag does not prove blocking every travel path, particularly silent packets or other direct callers. T04/T05/T13: `level_changer.cpp:212–232`, `script_game_object4.cpp:385–406`, `xrServer_Objects_ALife.cpp:907–973`.

## Marker creation, queries and callback phases

CMapManager AddMapLocation constructs and appends a new marker without a duplicate guard. Identity for matching is spot_type plus u16 object ID. Added notifications occur after append but **before** Lua add wrappers apply their explicit hint or serializable flag: first actor map_location_added callback, then the optional global hook in singleplayer with g_actor. Callback observers therefore cannot assume final wrapper customization or a reentrancy-safe creation transaction. M01/M02: `level_script.cpp:436–469`; `map_manager.cpp:125–169`.

Ordinary add can already be serializable when spot XML has a store attribute; `_ser` forces that flag true afterward. Spot XML also controls no_offline, pos_to_actor and positive TTL; a missing spot XML node asserts. A new marker resolves/caches its server owner pointer at construction. SP Update considers that owner pointer, then expiration; successful add does not independently certify actual/visible state. M07/M08: `map_location.cpp:34–69,128–163,351–410`.

`map_has_object_spot` has native u16 return populated from a bool, so its registered result is numeric 0/1; Lua numeric zero is truthy. It checks a matching registered marker, not visibility or drawn state. Hint changes and borrowed widget getters address the first match. By-ID enumeration returns one row per marker with spot_type/text; all-marker enumeration copies IDs/types/hints, cached level and last position, without forcing fresh position or filtering actual/drawn state. Widget pointers remain owned by the marker and may be null even while the marker exists. M01/M04/M11: `level_script.cpp:454–537,570–574`; `map_manager.cpp:240–291`; `map_location.h:94–123`. Reuse [A-Life map position authority](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md); enumeration timestamps/readiness are not new position guarantees.

## Removal and visibility are separate

Remove-by-type/ID removes the first matching entry. All-ID and object-destroy paths remove matching entries across types. Before unlinking, singleplayer calls task/UI MapLocationRelcase; notify-mode task cleanup clears links without recursively removing the same marker. These operations do not themselves complete/fail the associated task. Manager Destroy queues deletion; Update deletes the previous queue, updates/sorts markers and queues markers whose actuality expired. M03/M04/M16/M17: `map_manager.cpp:171–320`, `GametaskManager.cpp:265–274`, `GameTask.cpp:116–124`.

Removal notification uses a separate queue. Main-thread Flush occurs before scheduling/running that frame's map update, which may run in the parallel queue. Missing actor or missing global callback discards pending removal notices. A fixed initial count is delivered; notices appended by callbacks remain for a later flush. Exact wall-clock/frame latency, thread safety for arbitrary caller mutations and callbacks after unload are not certified. ResetStorage clears cached registry access and pending notices. M05/M06/M12: `map_manager.cpp:340–396`; `Level.cpp:1032–1044,1773–1785`; `map_manager.h:23–54`. The bundled callback relay forwards added/removed names to SendScriptCallback, without establishing installed dispatcher/listener order (M19).

Native server object unregistration invokes its script hook before notifying the map manager to remove markers. Do not equate transient client absence with permanent entity destruction or require that every release route has already delivered the queued removal notice. M18 plus [A-Life lifecycle](../alife/lifecycle-state-reference.md).

Selected drawing gates include matching level map, no_offline against server online state and the server visible-for-map flag, followed by UI visibility handling. Existence, actuality, spot/pointer flags and rendered visibility remain distinct. Relation-marker creation has its own type and duplicate assertion; exhaustive faction/helmet/minimap visibility policy is outside this ordinary-marker pass. M02/M08; [factions](../factions/development-reference.md).

## Marker persistence and restoration

The map manager wrapper selects holder registry 1 from A-Life, or local storage when no simulator exists. Registry save counts/writes only Serializable markers. Each key writes object ID/spot_type and a format byte; load constructs a base CMapLocation, then reads hint/flags/task-owner ID. Cached pose/level and original TTL deadline are not written by this selected marker serializer. Construction reads current XML and computes a new TTL before saved flags load, so exact remaining TTL and current-config compatibility are not guaranteed. No dynamic subclass restoration is encoded in the selected key loader. M09/M10/M13: `map_location.cpp:590–607`; `map_manager.cpp:60–123`; `alife_registry_wrapper.h:15–100`.

The registry container persists map locations; selected A-Life load restores objects/registrations, then registries, then replayed on_register callbacks. Loaded/unloaded notifications reset manager registry pointers and pending removal notices. Therefore restoration is not a fresh AddMapLocation callback sequence, and current source/custom wrappers can still recreate or alter markers. Full effective restore/script ordering remains WORLD-04/persistence work. M06/M14/M15: `alife_registry_container.cpp:15–40`, `alife_storage_manager.cpp:82–94,151–163`.

WORLD-03 selected use/touch, actor transition and ordinary-marker lifecycle pass is complete within scope. Effective installed integration and runtime remain partial/untested. Next WORLD-04 supplied consumers, cross-system consolidation and bounded audit. No engine/gameplay code or third-party assets changed. [Completion status](source-completion-status.md), [verification](../../08-research/verification-2026-10-12-v0.1.72.md).

## Current navigation after WORLD-04

The original research scope and findings above are retained. [Supplied consumers](supplied-consumers.md), [central guide](development-reference.md), [completion status](source-completion-status.md) and [v0.1.73 bounded audit](../../08-research/verification-2026-10-12-v0.1.73.md) record the completed available-source pass and remaining effective/runtime requirements.
