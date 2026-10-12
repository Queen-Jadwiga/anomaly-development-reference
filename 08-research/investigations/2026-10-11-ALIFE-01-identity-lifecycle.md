# ALIFE-01 — Server identity, squad membership and online/offline lifecycle

> ADR document set: **v0.1.69**. Research revisions and source/build versions below describe their original scope.

**ADR v0.1.31 · 11 October 2026 · source research complete within this first-pass scope; runtime deferred.**

## Question and scope

What persists when NPCs and squads switch online/offline, what identifies their membership and smart assignment, and which parts require the gameplay scripts rather than the native engine?

This is a targeted inspection of the user-supplied October 11 source snapshot and its bundled `sim_squad_scripted.script`. It does not establish the effective behavior of the installed GAMMA profile or close the entire A-Life/Warfare subsystem.

**Source archive SHA-256:** `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee` — verified before extraction; matches [SRC-002](../../00-environment/source-baseline-2026-10-11.md). The archive's exact upstream commit and binary equivalence remain unverified. Evidence IDs below refer to the [source-location and file-hash ledger](../../evidence/alife/source-evidence-oct11.csv); line numbers belong to the extracted archive, not a claimed remote permalink.

## Plain-language model

An NPC can have a server-side A-Life record while having no active object in the current level. A squad has its own server object and a native membership container referencing NPC records. Bringing a squad online creates online member representations; taking it offline removes those representations and restores offline scheduling of the group. This is a representation/simulation transition, not itself proof that anyone died or that territory changed hands. [E07–E09, E13]

Four kinds of state must remain distinct:

| State | What this source establishes | What it does not establish |
| --- | --- | --- |
| Server identity | `CSE_Abstract::ID`, exposed as read-only `id`; `parent_id` is separate. [E01] | A globally unique, never-reused campaign/history identifier |
| Native squad membership | Member `m_group_id` references the group's ID; the group maps member IDs to server pointers. [E03, E09] | CtZ officer role or strategic detachment identity |
| NPC smart assignment | `m_smart_terrain_id`, exposed through `smart_terrain_id()` and a read/write field. [E03–E04] | Which faction owns or has captured that terrain |
| Lua squad routing | Bundled script separately tracks `smart_id`, `assigned_target_id`, `current_target_id`, `current_action`, and section-derived `player_id`. [E15] | Identical installed GAMMA policy, or equivalence between assignment, destination and physical arrival |

`65535` / `0xffff` is used as an invalid/unassigned sentinel in the examined native paths. Lua also uses `nil` in its squad state; they are not interchangeable without following the relevant code path. [E04, E06, E09, E15]

## Native lifecycle findings

### 1. Membership is an explicit operation

`register_member(member_id)` looks up the server record, verifies a live monster-derived member, reconciles its online/group state, sets `m_group_id = ID`, and inserts the member into `m_members`. Registration of the first member also copies location and speed to the group. `unregister_member` clears the member's group ID, updates graph/schedule state, and erases the entry. [E09:102–168]

The membership map is not the same thing as an attached-child list (`ID_Parent` / `children`). The examined registration code checks that relevant members have no parent and stores membership separately. [E01, E09]

The Lua registrations name `cse_alife_online_offline_group`, expose `MEMBERS__value_type.id` / `.object`, and list `register_member`, `unregister_member`, `commander_id`, `squad_members` (iterator), and `npc_count`. Those group methods are inside `#ifdef XRGAME_EXPORTS`; this documents the registration source and guard, not a new exhaustive build/link audit or runtime availability test. [E05]

### 2. Online/offline switching has several gates

For a generic dynamic object, `try_switch_online` checks the switch flags and, on its ordinary distance path, the actor-to-object distance against `online_distance()`. `try_switch_offline` uses `offline_distance()` and the flags. The manager also skips independent switching of attached objects, synchronizes location, and releases objects classified as redundant before/after its switch attempt. [E07:133–184; E08:160–247]

Group logic adds member checks. On the ordinary online path, a member within online distance leads to the inherited online attempt; that inherited attempt still applies its own checks. On the ordinary offline path, any member within offline distance prevents switching. Empty-group and forced-flag branches differ. Therefore “one NPC is near the actor” is not a complete sufficient-condition specification. This pass does not establish numeric distances or every scheduler/level eligibility path. [E09:201–267; E07]

`switch_online` on the group marks the group online, calls `add_online(member, false)` for offline members, and removes the group from offline scheduling/graph tracking. It does not call the generic group-container `add_online(this)` path. `switch_offline` copies location from a member, removes online members through `remove_online(member, false)`, and adds the group to offline scheduling/graph tracking. [E09:270–317]

### 3. Removing the level representation is not necessarily deleting the A-Life record

`CALifeSwitchManager::add_online` removes the server registration and spawns an online representation with `M_SPAWN_UPDATE`. `remove_online` preserves eligible child IDs, invokes `Perform_destroy`, reclaims the requested object ID through `PerformIDgen`, and calls the object's offline handler. Client-only children are explicitly filtered out of the saved list. [E08:47–103]

The inspected `xrServer::entity_Destroy` erases the server entity registration and frees its ID, but calls `F_entity_Destroy` only when no A-Life simulator is present or the object is not A-Life-controlled. This is why the function name alone cannot be treated as evidence of permanent A-Life deletion. The full `Perform_destroy` event chain remains a follow-up. [E13]

`PerformIDgen` delegates to `tfGetID`; for a specified valid ID, the examined generator reserves and returns that same requested value. The offline code's reassignment statement is therefore not evidence that an NPC necessarily receives a different ID on each ordinary transition. IDs can nevertheless be returned to the free pool and reused after object removal. [E08:94–95; E11–E12]

**CtZ inference:** use server IDs for current-object lookup, but pair historical records with a campaign identity and lifecycle/generation evidence if permanent identity matters. Do not count a missing online NPC as dead. This is a design implication, not an implementation change or tested persistence guarantee.

### 4. Group leadership and serialized membership have narrow meanings

`commander_id()` returns the first member-container entry's ID, or `0xffff` if empty; `npc_count()` returns container size. This does not establish an officer rank-selection algorithm, a named commander appointment, or a count of currently visible NPCs. [E09:359–374]

Native `STATE_Write` serializes member count and member IDs. `STATE_Read` restores IDs with null member pointers; `on_after_game_load` clears the temporary map and re-registers the saved IDs. This establishes a reconstruction mechanism, not uninterrupted validity of previously held Lua/native pointers across loading. [E10; E09:335–356]

`notify_on_member_death` unregisters the member. An empty group reports `redundant() = true`, which the switch manager can release. Death notification, membership removal, empty-group redundancy, and actual object release are separate steps. [E09:319–327; E08:229–247]

## Smart terrain and bundled Lua boundaries

The native smart-terrain registry examined here stores `CSE_ALifeSmartZone` pointers keyed by object ID, rejecting non-zone objects. Its add/remove routines do not contain faction-capture rules. NPC group and smart IDs are independent fields. [E14; E03]

The bundled squad script's `assign_smart(smart, old_smart_id)` updates `self.smart_id` only when a new smart exists, iterates members, unregisters them from the supplied old smart when available, and registers them at the new smart when available. The smaller member-assignment helper has additional checks. Directly changing the numeric smart field is not demonstrably equivalent to these registration operations. [E15:497–540]

`add_squad_member` calls the external helper `alife_create`, then native `register_member`, and emits `squad_on_add_npc`. The examined native simulator registers multiple `create` overloads and `release`, but the `alife_create` helper implementation is not resolved by this pass. Do not silently equate the helper with one overload. Other bundled creation branches call smart registration and `SIMBOARD:setup_squad_and_group`. [E15:588–627, 677–750; E06]

The active Lua `STATE_Write` / `STATE_Read` paths serialize `current_target_id`, respawn fields, `smart_id`, and `scripted_target`, and invoke `init_squad_on_load`, which calls the external simulation board and resets `current_action`. The nearby marshal `save_state` / `load_state` functions are inside a commented block and are not evidence of an active save callback. This pass does not audit the whole save format or prove persistence of arbitrary added fields. [E15:925–998, 89–95]

## WAR-001 — First Warfare boundary

The bundled script includes a `_G.WARFARE` branch that consults faction options for random squad size. Its `check_online_status` also carries a source comment stating that a version in `warfare_options.script` is used regardless of Warfare mode. The branch is executable source evidence; the override comment is a lead, not proof of the actual replacement path. [E15:709–718, 1034 onward]

A path inventory of this archive did not find `sim_board.script`, `smart_terrain.script`, `simulation_objects.script`, or `warfare_options.script`. Hence this archive alone cannot close simulation-board assignment, faction capture, Warfare replacement order, or active-profile behavior. This is a bounded archive inventory, not a claim that these scripts do not exist in Anomaly/GAMMA.

The current CtZ build calls squad smart assignment and simulation-board assignment separately, and keeps strategic detachment fields separate from the native group ID. See [CtZ integration boundary](2026-10-11-WAR-001-ctz-integration-boundary.md). Its comments about GAMMA patches remain hypotheses/previous implementation notes until the effective patched files are inspected.

## Callback leads, not an approved event contract

In this bundled file, active emitters include `squad_on_add_npc`, `squad_on_npc_death`, and `server_entity_on_register` / `server_entity_on_unregister`. The direct `squad_on_register` / `squad_on_unregister` calls visible nearby are commented out. Native dynamic-object registration also calls optional `_G` functors in `alife_dynamic_object.cpp:29–55`. Dispatch registration, effective overrides, duplicate notifications and event timing require their own audit. No guaranteed universal death/capture callback is established here. [E15:480–495, 600–626, 1006–1031; native path as stated]

## Next source work and deferred tests

1. **ALIFE-02:** trace object creation/registration/release and `Perform_destroy` end to end; identify server/client lookup lifetimes and actual callback ordering.
2. **ALIFE-03:** inspect effective `sim_board`, smart-terrain, simulation-object and squad scripts; distinguish stationed, travelling, arriving and job registration states.
3. **WAR-002:** inspect Warfare option patches, faction ownership/capture and offline combat policy; then map state changes to CtZ. Requires effective profile scripts, not generic web substitutes.
4. **ALIFE-04:** inspect save/load reconstruction and ID reuse across CtZ-owned data; define campaign/generation tracking before claiming permanent identities.

All in-game tests remain deferred by user request: online/offline transitions, member death/empty-group cleanup, assignment/arrival, save/reload, map transitions and Warfare ownership changes. No game or compiled engine was run for this update.
