# A-Life callback phases and observation contracts

> ADR document set: **v0.1.45**. Research revisions and source/build versions below describe their original scope.

- ID: ALIFE-10 — callback reference
- Subsystem: A-Life / Warfare integration
- Source status: source-confirmed within the inspected native/bundled-script paths
- Runtime status: untested; verification deferred until the user resumes it
- Baseline: ENGINE1011, uploaded October 11 source snapshot
- Last reviewed: 2026-10-11

Read alongside the [lifecycle/state reference](lifecycle-state-reference.md). All L-labels below refer to the [lifecycle/callback evidence ledger](../../evidence/alife/lifecycle-callbacks-2026-10-11.csv). Its source paths, symbols, ranges and hashes pin the uploaded archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Upstream commit, installed executable, winning Lua files and wrapper population remain unverified.

**There is no single global “entity ready” callback in this reference.** Native virtual hooks, optional global functors, shared script dispatch and object-bound callbacks have distinct conditions. A source-defined emission is not proof that a listener is installed or that an effective override reaches it.

## Native registration and squad notifications

| Observation | Source order and available state | Still pending / conditional | Evidence |
| --- | --- | --- | --- |
| `on_before_register()` | First call in `register_object` | Subsequent registry work/setup/attachment has not run; base hook is empty; override can differ | L02/L03 |
| Native `on_register()` | After the inspected registry helpers, simulator setup and attached-item branch | Gated by `can_register_objects`; direct creation may still need supplies/on_spawn; Lua board initialization may still be pending | L01/L02 |
| Generic `server_object_on_register` | Native optional `_G.CSE_ALifeDynamicObject_on_register(id)` → supplied bridge resolves server object and dispatches | Requires the base hook/bridge/global route; callback order inside shared dispatch does not advance later board insertion | L03/L08 |
| Bundled squad `server_entity_on_register(self,"sim_squad_scripted")` | Base registration (possible generic notification) first, type-specific dispatch second | Board `squads[self.id]=true` comes afterward; commented `squad_on_register` is not an active emission | L07 |
| Native `on_unregister()` | First call in native `unregister_object`, before subsequent registry removal | Lookups can still succeed in this pre-removal window; future object lifetime is not guaranteed | L01/L02 |
| Bundled squad `server_entity_on_unregister` | Type-specific dispatch → board removal/unassignment → respawn bookkeeping → base unregister/generic phase | Missing respawn-smart lookup can return before base/generic notification; native removal continues after override returns | L07 |
| Generic `server_object_on_unregister` | Optional native functor → supplied bridge while native unregister has not finished removing the object | Different phase from type-specific squad unregister; not unconditional on the bundled early-return path | L02/L03/L07/L08 |

**Practical use:** inspect the callback's provided server object and checked native fields, with context appropriate to its phase. Before invoking strategic board/assignment helpers, separately establish their required state and effective contract. Observe generic/type-specific notifications as potentially two phases of one event; do not count both as new entities. See [creation/register/release API](../../02-lua-api/alife/simulator-api.md#creation-and-release) and [ALIFE-02](../../08-research/investigations/2026-10-11-ALIFE-02-creation-registration-release.md).

## Registration during save reconstruction

1. Construct objects and load saved IDs/state.
2. Disable final `on_register` callbacks and rebuild native registries; `on_before_register` still runs.
3. Load the auxiliary registry container, enable callbacks, then run the `on_register` loop.
4. After the buffer loader returns, run the group after-load pass resolving saved member IDs into native pointers.

L10–L13. Thus registration observers can resolve objects before complete native member-pointer repair. Neither a generic registration callback nor native autosave-manager `on_game_loaded()` proves the timing of an installed Lua `on_game_load` or CtZ storage dispatch. Defer operations requiring repaired members to a separately established phase rather than inventing an ordering guarantee. [Persistence investigation](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md).

## Native storage hooks and strategic persistence

The following optional functors are all guarded by `ENGINE_LUA_ALIFE_STORAGE_MANAGER_CALLBACKS` and resolved by name in `alife_storage_manager.cpp`. Their existence in source does not prove that the installed build enables them or that a particular addon dispatcher is connected. L10, `46–250`.

| Native functor name in `alife_storage_manager` | Source boundary | Not established by this hook |
| --- | --- | --- |
| `CALifeStorageManager_before_save` | Filename save path, before native header/time/spawns/objects/registry serialization | Actual encoding or dispatch order of CtZ's Lua campaign table |
| `CALifeStorageManager_save` | After native compression/write and writer closure | That arbitrary addon fields were persisted or synchronized to Warfare ownership |
| `CALifeStorageManager_load` | Buffer-load entry, before header/object reconstruction in that call | Restored native objects, repaired members or effective Lua load-completion readiness |

The packet save entry first calls `ClientSend` then `ClientSave`; the filename save hook is a later boundary in that entry's route. Ordinary offline teardown does not invoke that preparation in its inspected chain. L10/L29/L32/L46.

CtZ's supplied `save_state`, `load_state` and `on_game_load` handlers have separate table/restoration contracts. Their effective storage wrapper and listener order remain missing evidence; they cannot be inserted into this native sequence by matching names. The [ALIFE-04 record](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md) pins the CtZ source commit, schema labels, restoration gates and ID-reconciliation limits.

## Online spawn observations

The server online flag/network insertion occurs before completion of client realization. `M_SPAWN` processing can be queued/postponed, rejected or skipped under documented branches. No fixed frame delay, cross-member spawn order or eventual-success guarantee is established. L05/L21/L24/L39.

| Phase | What has happened | What can follow | Evidence |
| --- | --- | --- | --- |
| Client ID registration inside base `CGameObject::net_Spawn` | Packet ID/transform assigned and client lookup begins succeeding | Binder reload/load, AI validation and further base/derived initialization | L22 |
| `game_object_on_net_spawn` via `_G.CGameObject_NetSpawn` | Later base spawn phase, after transform/AI validation and supplies | Binder `net_spawn`, then derived native work. Functor invocation is absent in this function's DEBUG branch | L22; supplied bridge in [ALIFE-06](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md) |
| Binder `net_spawn` / bundled `monster_on_net_spawn(client,server)` | Binder path reached; monster implementation resolves the server object before dispatch | `db.add_obj`, living-monster enemy/logic setup and cached-position correction. Dead-body path differs | L26 |
| Full virtual `net_Spawn` returns success | Base/binder and inspected derived native spawn work have returned | Outer level spawn-manager delivery, player entity setup and parent ownership handling | L24/L37/L38 |
| Already-queued client-spawn-manager callbacks | Outer level invokes manager after full virtual success, when not dedicated | Remaining outer player/parent work and optional after-spawn callback | L24/L25 |
| Spawn-manager callback added for an already-found object | `CClientSpawnManager::add` invokes it immediately | Lookup may have become available during partial base spawn; this route is not the same readiness contract as queued delivery | L22/L25 |
| Object callback `callback.net_spawn_after` | Outer spawn function has completed manager, player and parent-handling steps | Only present under `NET_SPAWN_AFTER_CALLBACKS`; requires an object-bound listener | L24 |

The supplied `callbacks_gameobject.script` after-spawn listener example is commented out. Its presence does not install the listener. Likewise, a true binder return can arise with no binder or caught exceptions and does not certify every addon initialized. See [ALIFE-06](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md), including `script_binder.cpp:134–164` in its ledger.

**Practical use:** choose a phase that establishes the specific prerequisite. Early client lookup supports identifying a currently registered representation, not arbitrary post-initialization work. A queued post-full-spawn callback has a stronger native completion boundary, but still does not prove installed board policy, all members realized, or later script stability. Treat the immediate add-time callback as a separate case. Position-sensitive work must account for later binder correction and derived setup; parent-dependent work also needs the outer ownership phase. These are design implications of the cited ordering, not runtime-tested recipes.

## Location and update notifications

| Hook / notification | Observation boundary | Constraint | Evidence |
| --- | --- | --- | --- |
| Native `on_location_change` | Detail path has changed graph registration/location at an edge | Group member-copy loop can be later; inspected group/monster brain location hooks are empty, not verified faction-capture callbacks | L16/L19/L20; [ALIFE-06](../../08-research/investigations/2026-10-11-ALIFE-06-graph-online-realization.md) |
| Bundled `squad_on_update` | After native base update, first-update/refresh work and online-status policy on paths reaching the notification | Later distance/target selection and location comparison remain; disabled/error paths can bypass it | L18 |
| `squad_on_after_game_vertex_change` | Later Lua comparison sees cached old game vertex versus final native-updated vertex | Cache assignment follows the callback; not one notification per traversed edge | L47 |
| `squad_on_after_level_change` | Subsequent Lua old-to-final level comparison | Follows the game-vertex notification when both occur; its own cache is updated afterward | L47 |

Listener priority cannot make these events atomic with another update, switch pass, member spawn or strategic assignment. Native movement completion and Lua arrival/capture remain distinct contracts. [Scheduling/brain investigation](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md).

## Client destruction and permanent removal

| Phase | Lookup and lifetime boundary | Pending work / restriction | Evidence |
| --- | --- | --- | --- |
| Client receives `GE_DESTROY` | Base unattached-object handling sets destroy flag; object enters destruction queue | Object-list teardown occurs separately; event receipt is not completion | L40; [ALIFE-07](../../08-research/investigations/2026-10-11-ALIFE-07-client-server-offline-teardown.md) |
| Object-list release notifications | Object/sound/registered release notifications precede reverse-order queued virtual `net_Destroy`/`Destroy` | Notification is a teardown phase, not a durable-lifetime grant | L28 |
| `game_object_on_net_destroy` via `_G.CGameObject_NetDestroy` | Generic functor runs before client ID unregistration; supplied wrapper dispatches the name | Inherited cleanup, unregister and binder teardown follow; this functor lacks the adjacent DEBUG exclusion of spawn | L23; ALIFE-07 bridge evidence |
| Binder `net_destroy` / bundled `monster_on_net_destroy(client)` | Ordinary client ID unregistration has already occurred; binder still has its object reference | Scheme/offline logic, conditional bookmark write and script-database removal follow in the bundled binder | L23/L26/L34 |
| Bundled bookmark-clearing wrapper | Calls original binder teardown first, then clears bookmark for recognized squad members | Winning files/startup/replacement order and effective stalker binder remain unknown | L27 |
| Final client lifetime work | Binder deleted, Lua wrapper deleted/spawn flag cleared; derived cleanup and object-list destruction proceed | Never retain the client wrapper as a persistent offline handle | L23/L28/L34 |
| Server A-Life unregister/release | Separate native or validated online event route | A client destroy notification can result from ordinary switching, without A-Life unregister or death | L01/L02/L41/L42/L46 |

**Practical use:** record the phase and relevant ID/context while the callback is executing; reacquire any later representation rather than retaining a destroyed pointer. Generic client destroy can still have client lookup; binder notification normally cannot. Do not classify all client destruction as casualties, or treat server unregister as a post-removal lookup test. Native opaque client-data retention and Lua bookmark writes are independent policies. [Lifecycle teardown](lifecycle-state-reference.md#offline-teardown-death-and-permanent-release).

## Listener order versus lifecycle order

The inspected `axr_main` implementation computes PRE → NORMAL → POST tiers and before/after constraints using stable topological ordering. Registration index provides fallback order; cycles/self-dependencies/conflicting cross-tier rules reject reordering. `make_callback` calls the resulting listeners directly, without local protected-call isolation or a listener snapshot. L09, `axr_main.script:235–665`; [dispatcher investigation](../../08-research/investigations/2026-10-11-ALIFE-02-creation-registration-release.md#ordering-listeners-within-a-callback).

This orders listeners **inside one dispatch**. It cannot move a registration observer past a later board insertion or turn an early binder callback into full virtual spawn completion. The archive's separate `dynamic_callbacks.lua` uses another callback set; the missing installed global wrappers determine the actual shared route. Error isolation, mutation during dispatch and installed listener ordering must not be assumed from the algorithm alone.

## Deferred boundaries

Effective board/smart readiness, Lua load/save dispatch, creature casualty/safe-release chains, startup monkey-patch order, active build flags and actual update/event timing remain open. Death and capture callbacks require those effective paths before receiving a unified completion contract. No gameplay edits or runtime tests are part of this reference. The [ALIFE-10 synthesis record](../../08-research/investigations/2026-10-11-ALIFE-10-lifecycle-callback-consolidation.md) records scope and verification; the [roadmap](../../ROADMAP.md) tracks remaining work.
