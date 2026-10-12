# ALIFE-02 — Native creation, registration, release and callback ordering

> ADR document set: **v0.1.61**. Research revisions and source/build versions below describe their original scope.

**ADR v0.1.32 · 11 October 2026 · targeted source research complete; engine runtime verification deferred.**

## Scope and provenance

This follows [ALIFE-01](2026-10-11-ALIFE-01-identity-lifecycle.md) through the inspected native creation/release entry points and bundled squad callbacks. It is not an exhaustive audit of every entity subclass, creation producer, shutdown path or installed GAMMA override.

Source: user-supplied `xray-monolith-2026.10.11.zip`, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Exact upstream commit and binary equivalence remain unverified. The [ALIFE-02 evidence ledger](../../evidence/alife/creation-release-evidence-oct11.csv) records archive-relative paths, line ranges and file hashes. References R01–R16 below refer to that ledger, not remote source permalinks.

## What “registered” means here

Native A-Life registration, server network-entity insertion, and Lua simulation-board insertion are separate operations. A callback can observe one completed operation while another is still pending. Registration also occurs during save reconstruction, so it is not inherently a newly created squad event.

### Native registration sequence

`CALifeSimulatorBase::register_object(object, add_object)` executes the following sequence. Calls are listed in source order; registry helper calls may internally have their own conditions. [R02:23–56]

| Step | Operation | Observation boundary |
| --- | --- | --- |
| 1 | `on_before_register()` | Before the subsequent registry work |
| 2 | `objects().add(object)` if `add_object` | Save restoration can use an already populated object registry |
| 3 | Graph update; schedule, story, smart-terrain and group registry helpers | Native registry work precedes `on_register` |
| 4 | `setup_simulator(object)` | Simulator setup precedes `on_register` |
| 5 | For an attached inventory item, append to parent children and attach | Applies to this registration path's attached-item branch |
| 6 | `on_register()` if `can_register_objects()` | May be suppressed and called later by bulk initialization |

This establishes ordering, not a guarantee that every registry contains every object or that arbitrary Lua gameplay policy has completed. `on_before_register` is empty in the inspected dynamic-object base; derived behavior must be checked separately. [R03:46–48]

## Creation entry points and their different readiness states

### Direct section creation

`spawn_item` allocates the server entity through `F_entity_Create`, assigns an ID and parent/location/spawn fields, optionally calls `register_object`, then calls `spawn_supplies()` and `on_spawn()` before returning. With immediate callbacks enabled, registration therefore precedes supplies and `on_spawn`. Passing native `registration=false` suppresses registration, but does not suppress those two later calls. [R01:98–145]

Spawn-template creation clones spawn/update data, assigns its ID, registers, sets `m_bALifeControl=true`, performs monster graph assignment, creates legacy `CSE_ALifeGroupAbstract` members or supplies, then calls `on_spawn`. That legacy member-creation branch is not itself a specification of `sim_squad_scripted` membership. The post-registration control assignment and graph/member work must not be treated as already complete at an immediate callback. [R01:187–234]

### Lua overloads and online parents

The simulator exports several `create` overloads, `register` through `reprocess_spawn`, and `release` through its wrapper. [R04:645–700]

| Examined Lua route | Native behavior | Consequence |
| --- | --- | --- |
| Section creation without a parent, or with an offline parent | Direct `spawn_item` registration | Callback may run before the call returns and before supplies/on_spawn finish |
| Section creation with an online parent | Create an unregistered temporary object, serialize it, free its ID, destroy it, then `Process_spawn` | Temporary pointer lifetime differs from returned server object lifetime |
| Six-argument creation with `reg=false` | Only the valid online-parent branch returns an unregistered temporary object | For no parent or offline parent, this wrapper still takes the ordinary registered path |
| `alife():register(object)` | Serialize, free ID, `F_entity_Destroy(object)`, then return `Process_spawn` result | The supplied object is consumed; use and validate the returned object rather than retaining the old pointer |

These are source findings, not a recommendation to packet-edit live registered objects. The manual-registration route is documented in the source as supporting delayed registration for online-parent spawning. Its body does not make it a general idempotent registry-insertion API. `Process_spawn` can return null on configuration/pre-create or parent validation failures. No Lua alias invalidation or runtime error behavior is claimed here. [R04:172–234,444–462; R05:9–65]

For fresh server spawns, `Process_spawn` inserts the entity into the network entity map before `game->OnCreate`. In single-player, `OnCreate` checks A-Life control/type, marks the entity online, and either adopts it into A-Life or disables control; the parent branch accepts the examined trader/inventory-box parent types. `CALifeSimulatorBase::create(CSE_ALifeObject*)` checks `can_save`, copies parent location and temporarily clears `ID_Parent` around registration, then restores it. Thus this path's immediate registration callback can see the temporary parent sentinel. Parent touch/child linkage occurs later in `Process_spawn`. Existing-entity spawns used by online switching skip `OnCreate` and `OnPostCreate`. [R05:76–179; R06:52–90; R01:236–267]

## Bulk initialization changes callback timing

Save loading populates objects, disables registration callbacks, reserves saved IDs and calls `register_object(object,false)` for each object. It then loads the auxiliary registry, re-enables callbacks and calls each object's `on_register`. New-game initialization similarly disables callbacks around `spawn_new_objects`, then runs a separate `on_register` loop. [R07:136–168; R08:249–274]

Consequently, the immediate-spawn statement “callback before supplies/on_spawn” must not be generalized to bulk initialization. Native records can already be present while another object's Lua `on_register` has not run. The loops do not establish dependency-aware ordering of squad and smart-terrain script initialization. Full save/load lifecycle and post-load membership reconstruction remain ALIFE-04.

## Generic callbacks versus squad callbacks

The dynamic-object native base resolves optional `_G.CSE_ALifeDynamicObject_on_register` / `_on_unregister` functors and calls them with the ID. The bundled `callbacks_gameobject.script` installs bridges that look up the object and send `server_object_on_register` / `server_object_on_unregister`. It also defines handlers maintaining `server_objects_registry`. These generic names differ from `server_entity_on_*`. Bridge presence, loading and listeners in an installed profile must be checked separately. [R03:29–55; R09:881–899]

The bundled `sim_squad_scripted` implementation has the following textual order. “Generic” here requires reaching the native base call and having its bridge installed. [R10:1006–1031]

| Squad operation | Order in this bundled implementation |
| --- | --- |
| Register | Base `on_register` → possible generic `server_object_on_register` → `server_entity_on_register(self,"sim_squad_scripted")` → board `squads[self.id]=true` |
| Unregister | `server_entity_on_unregister` → remove board entry → unassign smart → respawn bookkeeping → base `on_unregister` → possible generic callback |

Both direct `squad_on_register` and `squad_on_unregister` sends are commented out. In unregister, a non-nil respawn-point ID whose lookup fails causes an early return before the base call; a generic unregister notification is therefore not unconditional on this script path. Native removal resumes after the override returns. A listener subscribed to both generic and type-specific notifications can observe two phases of one lifecycle event; it should not count them as two creations/removals.

### Ordering listeners within a callback

The supplied `axr_main.script` implements PRE → NORMAL → POST tiers, before/after constraints, and a stable topological sort within each tier. Available unconstrained listeners are selected by registration index. Re-registering the same identity updates rules while retaining its fallback position. Active self-dependencies, cycles and contradictory cross-tier rules reject the proposed ordering; callback registration rolls back on reorder failure. Missing function targets act as forward references. [R11:235–609]

`make_callback` iterates ascending computed priorities and calls functions/userdata methods directly; it has no local protected-call or snapshot mechanism. Do not infer that an error isolates later listeners or that changing subscriptions mid-dispatch is safe. `on_game_start` discovers eligible scripts and then invokes their startup functions, but this source does not prove an installed addon's registration order. [R11:609–665]

The separate `dynamic_callbacks.lua` has a local callback set and uses `pairs`; its same-named functions must not be conflated with the axr dispatcher. The base global `SendScriptCallback` / `RegisterScriptCallback` wrappers are not supplied in this archive. Therefore the axr algorithm is verified as an implementation in the snapshot, while the installed global-wrapper route and listener population remain open. Priority rules order listeners within one dispatch; they cannot move a native callback past a later board insertion. [R12:1–37; R10]

## Release, destroy and offline switching

`CALifeSimulatorBase::release` looks up the A-Life object, snapshots and recursively releases its attached children, unregisters the parent, sets `m_bALifeControl=false`, and, for `alife_query=true`, calls `server.entity_Destroy`. This recursion follows `children`, not native squad membership. [R01:269–307]

`unregister_object` calls `on_unregister` first, then detaches an attached inventory item, removes object/story/smart/group registry entries and removes the applicable offline schedule/graph or online root-level graph entry. The unregister callback sees a pre-removal window; successful lookup at that moment does not establish future pointer validity. [R02:58–82]

| Route | Source chain | Interpretation |
| --- | --- | --- |
| Lua release of offline object | Wrapper → native `release(object,true)` → unregister → control false → `entity_Destroy` | Direct release path |
| Lua release of online object | Wrapper constructs/sends `GE_DESTROY`; server event dispatcher → `Process_event_destroy` → conditional `release(object,false)` → `OnDestroyObject` → `entity_Destroy` | Event-mediated path; wrapper return is not an explicit deletion acknowledgement |
| Ordinary offline switch | Switch manager → `Perform_destroy` → `entity_Destroy` → reserve requested ID → offline handler | Removes network representation while retaining the A-Life-controlled record on this path |

The Lua release wrapper ignores its boolean parameter; it chooses by `m_bOnline`. Do not equate that public argument with native `alife_query`. `Process_event_destroy` validates entity/client ownership, recursively processes attached children, and handles reject/broadcast packets before the final release/destroy section. This pass establishes the event route, not its frame timing or acknowledgement semantics. [R04:335–357; R13; R14]

`Perform_destroy` recursively rejects/destroys attached children and broadcasts a destroy packet, but does not call A-Life release/unregister. `entity_Destroy` erases the network entity entry and frees its ID, deleting through `F_entity_Destroy` only if there is no simulator or A-Life control is false. This completes the examined ALIFE-01 transition chain without turning online disappearance into death or permanent removal. [R15; R16; ALIFE-01 E08]

## CtZ implications and remaining work

These are design implications, not changes to CtZ gameplay:

- Treat registration as an observation phase, and distinguish initial creation from load reconstruction before creating historical records.
- Retain IDs for lookup; validate returned replacement objects and avoid holding consumed or released pointers.
- Make lifecycle bookkeeping tolerate duplicate observations and the bundled squad's missing generic-unregister branch.
- Require the relevant board/assignment state explicitly before strategic operations; listener priority alone does not establish readiness.
- Keep online representation loss, death, squad membership removal and permanent release separate.

**ALIFE-02 disposition:** inspected native creation/registration/release chains and bundled callback ordering are source-complete within the stated scope. Effective GAMMA global wrappers, smart-terrain/board/simulation-object implementations and Warfare overrides remain open under ALIFE-03 / WAR-002. Full persistence and campaign identity remain ALIFE-04. No engine runtime tests were performed.
