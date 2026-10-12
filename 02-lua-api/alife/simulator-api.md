# Simulator Lua API contracts

> ADR document set: **v0.1.66**. Research revisions and source/build versions below describe their original scope.

[Catalog conventions](README.md). Source: `src/xrGame/alife_simulator_script.cpp`, plus native update/combat declarations in the evidence ledger. The following signatures omit the bound C++ `self` receiver and retain native ID types. `LPCSTR` denotes string input; `Fvector` denotes a vector. Colon-call notation is descriptive, not a runnable sample.

## Lookup and identity

| Lua method | Checked source contract | Meaning / constraint |
| --- | --- | --- |
| Global `alife()` | `CALifeSimulator*` | Returns `ai().get_alife()` through const cast; do not assume available in every game context |
| `valid_object_id(id)` | `bool`, `_OBJECT_ID` | Tests only `id != 0xffff`; **does not test registry existence** |
| `object(id)` | `CSE_ALifeDynamicObject*` | Invalid sentinel logs and returns null; otherwise nonasserting registry lookup |
| `object(id, no_assert)` | Same pointer, ID + bool | Explicit registry assertion policy |
| `story_object(story_id)` | Same pointer, `_STORY_ID` | Nonasserting story-registry lookup; story ID is a different namespace |
| `actor()` | `CSE_ALifeCreatureActor*` | Server actor, not `db.actor` client object |
| `spawn_id(spawn_story_id)` | `_SPAWN_ID` | Spawn-story lookup, distinct from live object ID |
| `level_id()` / `level_name(level_id)` | `u32` / `LPCSTR`, integer argument | Current-level ID versus graph level-name lookup |

Definitions: simulator script lines 38–85,153–170,330–333,360–376; exact export expressions are in [the bindings CSV](native-lua-bindings-oct11.csv). Native numeric ID reuse and save reconstruction are described in ALIFE-01/04.

## Creation and release

| Method | Arguments after receiver | Native return |
| --- | --- | --- |
| `create` | `_SPAWN_ID` | `CSE_ALifeDynamicObject*` |
| `create` | section, position, `u32 level_vertex`, `_GRAPH_ID game_vertex` | `CSE_Abstract*` |
| `create` | Same + `_OBJECT_ID parent` | `CSE_Abstract*` |
| `create` | Same + parent + `bool reg` | `CSE_Abstract*` |
| `create_ammo` | section, position, level vertex, game vertex, parent, `int count` | `CSE_Abstract*` |
| `create_on_level` | section, level name, position | `CSE_Abstract*` |
| `create_on_level` | Same + level vertex | `CSE_Abstract*` |
| `register` | `CSE_Abstract*` | `CSE_Abstract*` replacement |
| `release` | `CSE_Abstract*`, bool | `void`; this helper does not use the bool |

Definitions: simulator script lines 158–358,444–461. Source default `reg=true` is not evidence that Lua can omit the seventh argument. The explicit registered overloads determine the call forms.

`register` serializes the supplied entity, frees its ID and destroys the input pointer, then returns the result of `Process_spawn`. **Use the returned entity; the original is consumed.** `create(..., parent, reg=false)` is conditional on the parent path: it is not a universal promise of delayed registration for every parent/state. `release` uses immediate native release for offline objects and a destroy-event route for online ones. See [ALIFE-02](../../08-research/investigations/2026-10-11-ALIFE-02-creation-registration-release.md) for exact branches and callback timing. Neither a method return nor a new server entity proves that a client object has finished spawning.

## State controls and iteration

| Method family | Contract | Boundary |
| --- | --- | --- |
| `set_switch_online/offline(id, bool)` | `void` | Changes permission bits; not an immediate transition command |
| `set_interactive(id, bool)` | `void` | Changes interactive flag; separate from switching permissions |
| `switch_distance()` / `set_switch_distance(float)` | `float` / `void` | Recomputes native online/offline thresholds; active settings unverified |
| `teleport_object(id, game_vertex, level_vertex, position)` | `void` | Native relocation entry; group propagation must follow its own contract |
| `set_objects_per_update(u32)` | `void` | Scheduled-update batch setting |
| `set_process_time(int)` | `void` | Integer input named `microseconds`; actual budget units require the [forwarding/comparison qualification](../../04-game-systems/alife/configuration-controls.md#time-and-count-limits-are-different) |
| `force_update()` | `void` | Calls `update_scheduled(true)`; does **not** call the full switch pass in its body |
| `get_children(object)` | Native `xr_vector<u16>&`, iterator policy | Child IDs, not ownership of new child objects |
| `object_count()` / `max_id()` | `_OBJECT_ID` | Source-defined count/highest-ID helpers; not generation identifiers |
| `object_ids(keytable, withActor)` | Lua table | Either indexed IDs or `{[id]=true}`; actor exclusion specifically tests ID 0 |
| `objects(keytable, withActor)` | Lua table | Values are server objects; key choice controlled by bool |
| `iterate_objects(functor<bool>)` | `void` | Calls callback with server objects; true stops iteration |
| `iterate_level_objects_of_clsid(int, functor<bool>)` | `void` | Current-level registry filtered by **script** CLSID; true stops iteration |

Definitions: simulator script lines 426–442,492–641; switch implementation in `alife_update_manager.cpp` is documented in ALIFE-08. C++ defaults on the table helpers do not establish Lua optional arguments. The level iterator source explicitly warns against releasing the iterated object; other live-registry iteration likewise requires care with mutation.

Restriction exports include monster-pointer + restrictor-ID add/remove helpers, and `remove_all_restrictions(id, ERestrictorTypes)`. `kill_entity` has the native monster + graph vertex + schedulable form and two helper overloads omitting schedulable/graph vertex respectively. Information exports include `has_info`, `dont_has_info`, `give_info`, `disable_info` and `iterate_info`; the helper signatures are recorded in [the declaration CSV](binding-helper-declarations-oct11.csv). These are mapped interfaces, not a completed restriction/death/info policy audit.

Commented iterator-object exports remain absent from this projected registration; the active functor iteration/table methods are not interchangeable with those commented names. The source also binds the without-actor iterator's `next`/`__call` to the base iterator member pointer literally. The inventory preserves that expression without diagnosing or repairing it.

## Lifecycle context

Read the [lifecycle/state reference](../../04-game-systems/alife/lifecycle-state-reference.md) and [callback phases](../../04-game-systems/alife/callback-phase-reference.md) before applying these contracts across spawn, switching, load or teardown. Runtime verification remains deferred.
