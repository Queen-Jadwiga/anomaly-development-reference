# Server entity, squad and movement API

> ADR document set: **v0.1.74**. Research revisions and source/build versions below describe their original scope.

[Catalog conventions](README.md). These are selected checked contracts. The complete scoped occurrence inventory, with overload expressions and evaluated guards, is in [the bindings CSV](native-lua-bindings-oct11.csv).

## Server fields and identity

| Lua owner / export | Access | Native source / meaning |
| --- | --- | --- |
| `cse_abstract.id`, `parent_id` | Readonly | `ID`, `ID_Parent`; object and attachment identity |
| `cse_abstract.position`, `angle` | Read/write | `Fvector o_Position`, `o_Angle`; stored server transform |
| `cse_abstract.script_version` | Readonly | Script version field, not campaign generation |
| `section_name()`, `name()` | String-returning helpers | Section name versus replacement/display object name |
| `clsid()` | Native script CLSID method | Script class identifier used by filtered iteration |
| `spawn_ini()` | `CScriptIniFile*` helper return | Cast address of native spawn INI; no fresh INI allocation in helper |
| `cse_alife_object.online` | Readonly | `m_bOnline`; not client spawn completion |
| `m_level_vertex_id`, `m_game_vertex_id`, `m_story_id` | Readonly | Server node, graph and story fields |
| `cse_alife_creature_abstract.team`, `squad`, `group` | Read/write | Native numeric `u8` fields; **not** the online/offline-group member registry |
| `cse_alife_monster_abstract.group_id` | Readonly | Native `m_group_id`, the online/offline group ID |
| `m_smart_terrain_id` | Read/write | Native assignment field; writing it alone does not execute board/job bookkeeping |

Source: `xrServer_Objects_script.cpp:16–32,119–140`, `xrServer_Objects_ALife_script.cpp:41–64`, `xrserver_objects_alife_monsters_script3.cpp:66–83`, `xrServer_Objects_ALife_Monsters_script4.cpp:93–126`; type declarations in `xrServer_Object_Base.h` and `xrServer_Objects_ALife_Monsters.h`. Exact registration origin lines are also available in the CSV; names preserve source capitalization.

Base A-Life exports overload `move_offline` and `visible_for_map` as bool getters and bool-taking setters. `can_switch_online/offline` combines shared virtual bool getters with explicit void(bool) setters. The native field `online` remains readonly. Permission changes and offline movement eligibility are separate controls; see [ALIFE-08](../../08-research/investigations/2026-10-11-ALIFE-08-switching-eligibility.md).

Creature `health()` returns float and `alive()` returns bool. `o_torso()` returns an address of the native torso rotation. Trader exports include community, profile/name/icon, rank/set_rank and reputation under `XRGAME_EXPORTS`. Human and monster `rank` registrations differ; inheritance and local registrations must be considered rather than assigning one universal implementation from the name.

## Native → Lua virtual calls

| Shared registration family | Methods / hooks | Boundary |
| --- | --- | --- |
| Abstract | `STATE_Write`, `STATE_Read`, `init`; `FillProps` in non-game branch | Packet/state hooks; not arbitrary field autosaving |
| A-Life | `can_switch_online`, `can_switch_offline`, `interactive`, `used_ai_locations`, `can_save` | Virtual decisions native callers can consume |
| Dynamic A-Life, game branch | `on_spawn`, `on_before_register`, `on_register`, `on_unregister`, `keep_saved_data_anyway`, `switch_online`, `switch_offline` | Lifecycle policy; base calls and callback phases matter |
| Creature | `g_team`, `g_squad`, `g_group`; `on_death` in game branch | Native/script death entry is separate from completed release |
| Online/offline group | `update`; `get_current_task` in game branch | Group brain/task handoff |
| Monster | `update` | Individual update virtual, distinct from group update |
| Custom zone | `update`, `smart_touch`, `detect_probability`; additional game-branch task/registration methods | Native smart interface; effective Lua smart implementation still missing |

Sources: `xrServer_script_macroses.h:260–375`, `script_export_macroses.h`, and macro invocation rows in the CSV. Wrapper implementations call Lua members and expose static inherited fallbacks; catch behavior varies with wrapper macro and return type. The bool wrapper's catch-all returns zero, as traced in ALIFE-08. This catalog does not generalize that behavior to every hook.

`CSE_Abstract` also directly registers `UPDATE_Read`/`UPDATE_Write` and its packet methods with the special base wrapper. Do not assume every abstract fallback performs serialization: its examined pure-method fallback bodies log an attempted pure virtual call. Packet overload/declaration details require the recorded binding expression, not just the function name.

## Squad container methods

All following explicit group methods are guarded by `XRGAME_EXPORTS` in `xrserver_objects_alife_monsters_script3.cpp`. Native declarations: `xrServer_Objects_ALife_Monsters.h:530–580`.

| Method | Checked native signature after receiver | Purpose / constraint |
| --- | --- | --- |
| `register_member(id)` | `void(_OBJECT_ID)` | Adds live native member; registry/online alignment side effects |
| `unregister_member(id)` | `void(_OBJECT_ID)` | Clears group relationship and restores independent processing |
| `commander_id()` | `_OBJECT_ID()` | Source-selected member ID; not an independent durable leader identity |
| `squad_members()` | `MEMBERS const&()`, iterator policy | Entries expose readonly `id` and `object` |
| `npc_count()` | `u32() const` | Native member count |
| `add_location_type(mask)` | `void(LPCSTR)` | Adds native location mask |
| `clear_location_types()` | `void()` | Clears masks |
| `force_change_position(position)` | `void(Fvector)` | Group/member location change; different graph node can overwrite requested point |
| `get_current_task()` | `CALifeSmartTerrainTask*()` virtual | Called through group brain/task path; not an immediate movement command |

Member iterator values refer to native members; the receiver `MEMBERS__value_type` is a separate registered support type. Mutation/release during iteration and retention across load/teardown need lifecycle care. See ALIFE-01/02/04/06. Native `try_switch_*`, `add_online/offline` and `synchronize_location` are traced mechanisms; their names are not direct exports in this group registration merely because they exist in C++.

Monster helper exports `clear_smart_terrain`, `smart_terrain_task_activate` and `..._deactivate` directly set `m_smart_terrain_id` / `m_task_reached`. They do not implement the missing simulation-board assignment/job chain. `travel_speed` and `current_level_travel_speed` have float getter/setter helper overloads in the game branch. `brain()` returns the entity-owned monster/human brain. Source: monster script4.

## Task and movement controls

| Lua class / methods | Checked contract |
| --- | --- |
| `CALifeSmartTerrainTask` constructors | Patrol name; patrol name + `u32` index; graph ID + `u32` level vertex |
| Task `game_vertex_id`, `level_vertex_id`, `position` | Returns graph ID, `u32`, and `Fvector` respectively |
| Brain `can_choose_alife_tasks(bool)` | Setter only in this brain registration; native getter exists but is not explicitly bound here |
| Brain `movement()` / movement `detail()`, `patrol()` | Returns addresses of owner-held managers |
| Movement `path_type` | Getter returns `const EPathType&`; setter takes `const EPathType&` |
| Detail `target` | Three overloads: graph + level vertex + position; graph ID; `const CALifeSmartTerrainTask*` |
| Detail `speed` | Getter returns `const float&`; setter takes `const float&` |
| Patrol controls | `path(LPCSTR)`, start/route enum getters/setters, randomness bool getter/setter; target position/vertex queries |

Sources: the corresponding `alife_*_script.cpp` registrars and native headers in the ledger. `actual` and `completed` are exported on movement/detail/patrol managers; detail also exports `failed`. Their meanings differ: movement-manager completion alone does not prove physical arrival or Warfare ownership. [ALIFE-05](../../08-research/investigations/2026-10-11-ALIFE-05-offline-scheduling-brains.md) explains the source implementations and task handoff.

Do not infer writable graph/node fields from task accessors or complete board assignment from a movement target. The catalog maps mechanisms; effective strategic policy and in-game verification remain separate.

## Lifecycle context

Read the [lifecycle/state reference](../../04-game-systems/alife/lifecycle-state-reference.md) and [callback phases](../../04-game-systems/alife/callback-phase-reference.md) before applying these contracts across spawn, switching, load or teardown. Runtime verification remains deferred.

## Server inventory item accessor property

The scoped catalog now includes `cse_alife_inventory_item.condition`, registered with `get_condition_script` and `set_condition_script` at ENGINE1011 `src/xrServerEntities/xrServer_Objects_ALife_Items_script.cpp:22–39,43–52`. This is property access (`server_item.condition`), not a `condition()` method. Apply only to a correctly typed exported server item; the registered class/base map governs inherited exposure.

The getter reads `m_fCondition`. The setter logs and returns for ordinary values below 0 or above 1, otherwise writes the field. Do not infer finite-number rejection, quantization guarantees or effective runtime synchronization from this guard. [S01 and catalog correction](../../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md#catalog-correction).
