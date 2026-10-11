# Native class and Lua name map

> ADR document set: **v0.1.48**. Research revisions and source/build versions below describe their original scope.

[Catalog and evidence conventions](README.md).

## Principal server types

The bases in this table are registered Lua bases, not every native C++ base. Exact registration arguments and source lines are in [the class CSV](native-lua-classes-oct11.csv).

| C++ type | Lua class | Registered bases | Role |
| --- | --- | --- | --- |
| `CALifeSimulator` | `alife_simulator` | None listed in its Lua registration | Persistent simulator service returned by global `alife()` |
| `CSE_Abstract` | `cse_abstract` | `CPureServerObject` | Server ID, parent, transform, section/name and packets |
| `CSE_ALifeObject` | `cse_alife_object` | `CSE_Abstract` | Online flag, graph/node/story IDs and switching permissions |
| `CSE_ALifeDynamicObject` | `cse_alife_dynamic_object` | `CSE_ALifeObject` | Lifecycle and online/offline virtual hooks |
| `CSE_ALifeDynamicObjectVisual` | `cse_alife_dynamic_object_visual` | Dynamic object + `CSE_Visual` | Server visual capability |
| `CSE_ALifeCreatureAbstract` | `cse_alife_creature_abstract` | Dynamic visual | Health, team/squad/group numeric fields and death virtual |
| `CSE_ALifeMonsterAbstract` | `cse_alife_monster_abstract` | Creature + `CSE_ALifeSchedulable` | Native membership, smart task state and brain |
| `CSE_ALifeHumanAbstract` | `cse_alife_human_abstract` | Trader abstract + monster abstract | Human brain and character capabilities |
| `CSE_ALifeHumanStalker` | `cse_alife_human_stalker` | Human abstract + `CSE_PHSkeleton` | Stalker server representation |
| `CSE_ALifeOnlineOfflineGroup` | `cse_alife_online_offline_group` | Dynamic object + schedulable | Native squad container and member registry |
| `CSE_ALifeCustomZone` | `cse_custom_zone` | Dynamic object + `CSE_Shape` | Native zone/smart-task virtual interface |
| `CSE_ALifeTraderAbstract` | `cse_alife_trader_abstract` | None listed | Character profile/name, community, rank and reputation exports |

Source: server registrar files `xrServer_Objects_script.cpp`, `xrServer_Objects_ALife_script.cpp`, `xrServer_Objects_ALife_Monsters_script.cpp`, `..._script2.cpp`, `xrserver_objects_alife_monsters_script3.cpp`, `..._script4.cpp`; exact row origins and hashes are in the inventories.

Native-only bases include `CRandom` for the A-Life object and `CMovementManagerHolder` for monster/group types, declared in `xrServer_Objects_ALife.h` and `xrServer_Objects_ALife_Monsters.h`. Their presence in C++ does not make all their methods callable through Lua.

## Brains, movement and graph values

| Native/Lua class name | Obtained through | Relationship |
| --- | --- | --- |
| `CALifeMonsterBrain` | Monster `brain()` | Entity-owned brain; exported `movement`, `update`, task-choice setter |
| `CALifeHumanBrain` | Human `brain()` | Registered as a descendant of `CALifeMonsterBrain` |
| `CALifeMonsterMovementManager` | Brain `movement()` | Provides detail/patrol managers and path state |
| `CALifeMonsterDetailPathManager` | Movement `detail()` | Graph/task target and speed; actual/completed/failed |
| `CALifeMonsterPatrolPathManager` | Movement `patrol()` | Patrol name, start/route types, randomness and target queries |
| `CALifeSmartTerrainTask` | Constructor or task virtual return | Game vertex, level vertex and position |
| `CGameGraph` | Global `game_graph()` | Graph lookup, accessibility, levels and nearest/neighbour helpers |
| `GameGraph__CVertex` | Graph `vertex()` | Read methods for level/game points and IDs |

Source: corresponding `alife_*_script.cpp`, `game_graph_script.cpp`, server monster script4, and native declarations listed in the evidence ledger. The native group owns `CALifeOnlineOfflineGroupBrain`; no registration for that brain class was found in these scoped units. Do not substitute the exported individual monster brain for it.

`CALifeSimulator` inherits native `CALifeUpdateManager` and `CALifeInteractionManager` (`alife_simulator.h:18–20`). Registry/switch/storage/schedule machinery is reached through its native manager hierarchy; it is not separately listed as a Lua base in `alife_simulator`. Consult [ALIFE-05](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md) for update ownership.

## Server versus client object lifetime

`alife():object(id)` returns a persistent **server** object. `level.object_by_id(id)` used by the scripts returns the online **client** representation; it is a separate interface and is outside this registration inventory. A server entity can remain while its client object is destroyed. Group IDs and member pointers likewise differ from client readiness.

Brain/movement helper implementations return addresses of objects owned by their native owner; they do not allocate a new brain for each call. Task constructors allocate through the registered constructor path, whereas task pointers returned by native/Lua virtual hooks need separate lifetime treatment. This pass does not redo a general Luabind converter/GC audit. Do not infer ownership transfer or safe retention from a raw pointer return.

The underlying lifecycle evidence is [ALIFE-02](../../08-research/investigations/2026-10-11-ALIFE-02-creation-registration-release.md), [ALIFE-04](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md), and [ALIFE-07](../../08-research/investigations/2026-10-11-ALIFE-07-client-server-offline-teardown.md). Release/unregistration and load reconstruction can invalidate references even when a numeric ID is later reused.
