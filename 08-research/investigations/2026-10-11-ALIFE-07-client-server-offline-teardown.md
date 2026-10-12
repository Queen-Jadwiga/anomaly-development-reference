# ALIFE-07 — Client-to-server position synchronization and offline teardown

> ADR document set: **v0.1.71**. Research revisions and source/build versions below describe their original scope.

**ADR v0.1.37 · 11 October 2026 · bounded source investigation; runtime verification deferred.**

Online creature position returns to the server through `M_UPDATE`. Offline switching consumes the server entity's stored state; the inspected ordinary transition does not explicitly request a final client update or save packet. Destroying an online representation is distinct from releasing its persistent A-Life entity.

## Baseline and evidence

This report uses the supplied `xray-monolith-2026.10.11` archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Its exact upstream commit and equivalence to the installed executable are unverified. Paths and one-based lines below refer to the extracted archive, not an inferred upstream revision. [The evidence ledger](../../evidence/alife/client-server-offline-evidence-oct11.csv) records full-file hashes and inspected ranges. Evidence labels S01–S25 refer to that ledger.

This extends [ALIFE-06](2026-10-11-ALIFE-06-graph-online-realization.md), [ALIFE-05](2026-10-11-ALIFE-05-offline-scheduling-brains.md), and [ALIFE-04](2026-10-11-ALIFE-04-save-load-identity.md). Effective GAMMA scripts, startup wrappers and build settings remain unverified.

## 1. How the position reaches the server

`CLevel::net_Update` calls `ClientSend` when the game is configured. The host path builds `M_UPDATE` packets through `Objects.net_Export`; the separate `OnClient` branch exports its control entity through `M_CL_UPDATE` and returns. `CLevel::Send` can dispatch directly to the local server, use synchronized server dispatch, or use the network transport. These branches do not justify assigning a fixed export interval or frame order. **S01:** `src/xrGame/Level_network.cpp:179–238,294–330`.

`CObjectList::net_Export` visits active and sleeping objects, selecting `net_Relevant()` objects that are not marked for destruction. It writes an object ID and byte-sized update chunk and invokes the virtual exporter. **S02:** `src/xrEngine/xr_object_list.cpp:344–384`.

| Layer | Position/state used | Source |
| --- | --- | --- |
| `CCustomMonster::net_Export` | `NET.back().p_pos`, plus sampled timestamp/orientation; not a fresh `Position()` read for that position field | S03, `CustomMonster.cpp:271–289` |
| Local monster sample production | Scheduled update pushes `Position()` into `NET`; the `dt > 3` early return is before this sampling branch | S03, `CustomMonster.cpp:324–418` |
| Stalker and base-monster exporters | Sampled `NET.back()` position, with current AI game vertex and distances computed from current `Position()` | S04, `ai/stalker/ai_stalker.cpp:870–917`; S05, `ai/monsters/basemonster/base_monster_net.cpp:22–59` |
| Server creature update reader | Reads packet position into `o_Position`, alongside health/timestamp/orientation/team fields | S08, `xrServer_Objects_ALife_Monsters.cpp:1119–1154` |
| Server monster extra fields | Reads exported graph fields into next/previous graph IDs and distance fields; these are not direct updates to `m_tGraphID` or `m_tNodeID` | S08, same file:1365–1383 |

The payload can therefore combine a sampled position with more current AI vertex/distance values. The source establishes that distinction; it does not establish a visible error or the magnitude of any runtime lag.

`xrServer::OnMessage` dispatches `M_UPDATE` to `Process_update`. The reader looks up the ID in the server's online entity registry, sets `net_Ready`, and calls the virtual `UPDATE_Read`; an unknown ID's chunk is skipped. Its local-client assertion bounds this path. **S06:** `xrServer_process_update.cpp:7–58`; **S07:** `xrServer.cpp:457–485`.

## 2. Stored position versus graph location

`CSE_ALifeDynamicObject::synchronize_location` separately validates the stored node and position, resolves the level vertex, converts it through the cross table and updates graph/distance state. Its online branch updates `m_tGraphID` directly; its offline branch uses graph-registry change machinery. Invalid-node and position/inside checks can return before recomputation. See ALIFE-06 for the literal offline restoration logic. **S16:** `src/xrGame/alife_dynamic_object.cpp:93–130`.

During group `switch_offline`, the group first becomes offline. If it has members, it synchronizes the first member and copies that member's **server-side** position, node, graph ID and distance into the group. It then clears eligible member client data and removes each online member with `update_registries=false`, before adding the group to the schedule and graph. The first member is still online when that explicit synchronization runs. This is not an average of client positions. **S15:** `alife_online_offline_group.cpp:287–317`.

## 3. Update packets and saved client data are separate channels

`ClientSave` emits `M_SAVE_PACKET` through `Objects_net_Save`, selecting non-destroyed game objects whose virtual `net_SaveRelevant` returns true. `CGameObject::net_Save` serializes its save data and binder data inside the client-data chunk. Stalker/base-monster overrides also serialize physics state; their relevance includes physics-shell state. **S01:** `Level_network.cpp:240–289`; **S10:** `GameObject.cpp:483–510,1095–1097`; **S04:** `ai_stalker.cpp:859–868`; **S05:** `base_monster_net.cpp:11–20`; **S21:** `script_binder.cpp:216–260`.

Server `Process_save` invokes virtual `load`, independently of `UPDATE_Read`. `CSE_Abstract::load` reads the version-dependent client-data size and replaces or clears `client_data`; derived monster/stalker loaders consume their inherited components. Thus ordinary position updates do not themselves serialize arbitrary binder state. **S06:** `xrServer_process_update.cpp:60–95`; **S09:** `xrServer_Object_Base.cpp:375–395`; **S08:** `xrServer_Objects_ALife_Monsters.cpp:2026–2030,2189–2207`; **S07:** `xrServer.cpp:614–620`.

Explicit native save preparation calls both `ClientSend()` and `ClientSave()`. The inspected `remove_online`/`Perform_destroy` route contains neither call. **S25:** `alife_storage_manager.cpp:235–250`; **S14:** `alife_switch_manager.cpp:74–103`; **S13:** `xrServer_sls_clear.cpp:9–59`.

**Bounded conclusion:** this offline route provides no explicit final-snapshot barrier. Its inputs can be previously imported state. This does not prove packet loss, prescribe an exact last-update age, or exclude calls elsewhere or installed wrappers.

## 4. What offline teardown retains and clears

`remove_online` marks the entity offline, filters saved children, performs server destruction, reserves its existing ID, then calls `add_offline`. `xrServer::entity_Destroy` removes the online registry entry and frees its network ID, but only destroys the actual entity when no A-Life exists or the entity is not A-Life-controlled. The ID reservation follows that removal. Persistent A-Life identity can therefore survive destruction of the online representation. This path is not inherently an A-Life unregistration or death notification. **S14:** `alife_switch_manager.cpp:74–103`; **S07:** `xrServer.cpp:865–883`; compare [ALIFE-02](2026-10-11-ALIFE-02-creation-registration-release.md).

| State | Inspected offline behavior |
| --- | --- |
| Structured server position/graph/member state | Reused by the persistent A-Life object and group transition; no blanket reset shown in this route |
| Opaque `client_data` | Ordinary dynamic-object `switch_offline` clears it after `remove_online`; group switch clears online members before removal |
| Retention exception | `clear_client_data` respects virtual `keep_saved_data_anyway`; base A-Life object returns false, anomalous zone returns true |
| Native brain transition | Monster/human `add_offline` calls inherited registry work and its brain's offline hook |
| Lua `db.offline_objects` | Separate script memory, written and potentially cleared by binder/wrapper logic below |

Evidence: **S16:** `alife_dynamic_object.cpp:58–91,294–307`; **S15:** `alife_online_offline_group.cpp:287–317`; **S17:** `alife_object.cpp:205–208`; **S18:** `alife_anomalous_zone.cpp:136–139`; **S19:** `alife_monster_abstract.cpp:25–36`; **S20:** `alife_human_abstract.cpp:85–96`. These statements do not generalize the anomalous-zone exception to every subclass or installed override.

## 5. Destruction event and callback ordering

`Perform_destroy` recursively handles children, removes the server entity, then broadcasts `GE_DESTROY`. Client event processing invokes `Game().OnDestroy` before object event dispatch. The base `CGameObject::OnEvent` handles an unattached object's `GE_DESTROY` by setting the destroy flag; `CObject::setDestroy` queues destruction. **S13:** `xrServer_sls_clear.cpp:9–59`; **S11:** `Level.cpp:433–459`; **S10:** `GameObject.cpp:241–261`; **S12:** `xr_object.cpp:482–502`.

The object-list destruction pass calls object/sound/registered release notifications, then processes queued objects in reverse order through virtual `net_Destroy` followed by `Destroy`. Hence receiving the event and running final teardown are distinct phases. No exact delay in frames is asserted. **S02:** `xr_object_list.cpp:272–313`.

Within `CGameObject::net_Destroy`, the relevant ordering is:

1. `_G.CGameObject_NetDestroy` runs while the object is still registered in the client ID map. Unlike the spawn hook discussed in ALIFE-06, this call has no adjacent `#ifndef DEBUG` guard.
2. Inherited destruction/readiness cleanup and client `net_Unregister` occur.
3. `CScriptBinder::net_Destroy` calls the bound object's destroy method, then deletes the binder object.
4. The Lua game-object wrapper is deleted and the spawned flag cleared. Derived monster cleanup continues after its inherited destroy call.

**S10:** `GameObject.cpp:114–167`; **S02:** `xr_object_list.cpp:316–340`; **S21:** `script_binder.cpp:166–183`; **S03:** `CustomMonster.cpp:860–882`. Generic callback listeners and binder callbacks therefore run at different client lookup phases; retained pointers must not be treated as proof of continued lifetime.

The supplied global wrapper forwards to `game_object_on_net_destroy`. The supplied monster binder clears selected object callbacks and sound, emits `monster_on_net_destroy`, handles scheme/offline-condition logic, then writes a bookmark only if a record already exists; it subsequently removes script database entries. **S24:** `gamedata/scripts/callbacks_gameobject.script:16–34`; **S22:** `gamedata/scripts/bind_monster.script:353–394`.

The supplied `aaaa_script_fixes_mp.script` startup patch wraps binder teardown: original teardown runs first, then the wrapper clears the bookmark for group members. That Lua bookmark policy is separate from native `client_data` clearing. Its presence in the archive does not establish that the installed profile executes it; the referenced effective stalker binder is not supplied. **S23:** same script:1283–1306,1606–1649; see ALIFE-06.

## Practical scope and remaining work

For CtZ/Warfare research, use persistent server/group state for offline tracking and treat a client object as a temporary online representation. Generic destroy callbacks, binder callbacks, packet state and Lua bookmarks are different observation points. This report identifies their native/source ordering; it does not introduce a CtZ code change or diagnose a runtime defect.

Source research complete within this boundary. Still deferred: installed winning exporters/binders/wrappers, actual update cadence and frame ordering, executable correspondence, and in-game tests of transition positions/bookmark restoration. Next independent source task: native online/offline switching eligibility, distance hysteresis and forced-state overrides.
