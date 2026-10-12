# Selected world spatial restriction and patrol APIs

> ADR document set: **v0.1.75**. Research revisions and source/build versions below describe their original scope.

- ID: WORLD-02-API
- Subsystem: world interaction/navigation
- Research revision: v0.1.71
- C++ / Lua owners: CLevel → level; CGameGraph → game_graph()/CGameGraph; CScriptGameObject → game_object; CPatrolPathParams → patrol; CALifeSimulator → alife()
- Interface kind: selected native Lua exports and native/script callers
- Source baseline: ENGINE1011, [manifest](../../evidence/manifest.md); archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`
- Source status: source-confirmed selected registration/definition/consumer paths
- Runtime status: untested; deferred
- Build scope: inspected game registrars; DEBUG assertions/duplicate guards explicitly qualified; executable macro/compiler/settings correspondence unknown
- Evidence: [P01–P40 ledger](../../evidence/world/spatial-contracts-2026-10-12.csv), [behavior and exact source references](../../04-game-systems/world/spatial-queries-relocation.md)
- Example status: none; call shapes below are contract notation, not tested recipes
- Last reviewed: 2026-10-12

## Lookup and query call shapes

Signatures omit the receiver where bound. Native integer widths/namespaces still apply; numeric Lua values do not guarantee a valid object or vertex.

| Lua call shape | Selected return/error contract | Evidence |
| --- | --- | --- |
| level.object_by_id(u16), no arguments, or general Lua object | Existing CScriptGameObject pointer/null; missing/nil forms diagnose; general form casts to u16 | P01 |
| object:position(); object:level_vertex_id(); object:game_vertex_id() | Fvector client position; u32 AI-location IDs | P07/P08 |
| level.vertex_id(Fvector) | u32 current-level column lookup; u32(-1) possible with prior VERIFY on invalid position | P02–P04 |
| level.vertex_position(u32) | Fvector; invalid ID returns Fvector{} | P02 |
| level.vertex_link(u32,int) | u32; invalid source ID returns u32(-1), no helper index-range guard | P02 |
| level.vertex_in_direction(u32,Fvector,float) | u32; invalid source sentinel; invalid result falls back to start | P02 |
| level.get_nearby_vertices(Fvector,float) | Table of level IDs mapped to true; no wrapper-level receiver accessibility certification | P02 |
| game_graph() | const CGameGraph pointer to engine-owned graph | P05 |
| graph:valid_vertex_id(u32); graph:vertex(u32) | bool count range test; borrowed vertex pointer with raw unchecked pointer arithmetic in its body | P05/P06 |
| vertex:level_point(); vertex:game_point(); vertex:level_id(); vertex:level_vertex_id() | Copied Fvector coordinates; graph level ID; level vertex ID | P05 |
| graph:accessible(u32); graph:accessible(u32,bool) | bool getter / void setter of shared enabled mask; VERIFY bounds precondition | P05/P06 |
| graph:nearest_vertex(string,Fvector) | Game vertex ID or nil; geometric nearest on that level, no route/mask filtering | P05/P06 |
| graph:level_neighbours(u32) | Other-level ID → true table across edges; no accessibility filtering | P05 |

## Relocation and live movement requests

| Lua shape after receiver | Return and mutation limits | Evidence |
| --- | --- | --- |
| alife():teleport_object(object_id,game_vertex_id,u32,Fvector) | void; virtual offline switch if online, graph registry change, explicit final node/position and monster next graph; not a live actor travel guarantee | P11–P14 |
| actor:set_actor_position(Fvector,bool skip_collision,bool keep_speed) | void; one three-argument native method registration. C++ default bool values are not registered Lua arity overloads. Skip branch controls speed preservation; normal branch uses alive-gated/collision-corrected physics and resets speed | P08/P10/P15–P17 |
| monster:set_npc_position(Fvector) | void; CCustomMonster only; detail/animation invalidation and alive-gated transform forwarding | P08/P15/P16/P18 |
| stalker:set_dest_level_vertex_id(u32); stalker:set_dest_game_vertex_id(graph_id) | void; type/validity gates; level destination also checks restrictions; setter return is not completed motion | P08/P19/P20 |
| stalker:set_patrol_path(string,start_enum,route_enum,bool) | void; updates selected patrol manager, without setting path type or planner in helper | P08/P19/P34/P36 |
| stalker:inactualize_patrol_path() | void; selected patrol actuality/completion reset | P08/P19/P36 |

## Live restriction calls

| Shape on a CCustomMonster wrapper | Native / converter contract | Evidence |
| --- | --- | --- |
| add_restrictions(string out,string in); remove_restrictions(string out,string in); remove_all_restrictions() | void; client restriction updates and refresh; defaults and server event routes are separate | P18/P20–P25/P28/P29 |
| in_restrictions(); out_restrictions(); base_in_restrictions(); base_out_restrictions() | LPCSTR selected lists; wrong-type wrapper yields empty string; current merged lists versus base lists | P21/P24 |
| accessible(Fvector); accessible(u32 level_vertex) | bool; wrong type/invalid vertex false, but absent effective restriction or failed initialization can be permissive | P21/P24/P25 |
| accessible_nearest(Fvector position,Fvector result_input) | Native u32 with Fvector&; SAFE_WRAP creates receiver argument 1, position 2, result 3. out_value<3> consumes the supplied vector and emits converted output after call; not pure_out_value. Early u32(-1)/assertions are not a destination | P10/P21/P22/P25/P26/P38 |

The output converter uses temporary storage copied from its Lua argument. Do not depend on mutation of the input vector itself. Native return and postcall output are distinct; no executable-tested multi-return recipe is asserted. P38.

Simulator add/remove in/out wrappers instead take a CSE_ALifeMonsterAbstract pointer plus restrictor object ID; remove_all_restrictions takes creature object ID and ERestrictorTypes. Selected implementations mutate server dynamic ID lists; those are serialized fields, with live projection handled separately. P11/P23/P27–P30. See existing [simulator catalog](../alife/simulator-api.md) for the wider interface set.

## Patrol query contracts

Registered patrol constructors: `(string)`, `(string,start_enum)`, `(string,start_enum,route_enum)`, `(string,start_enum,route_enum,bool)`, `(string,start_enum,route_enum,bool,u32 previous_index)`. Explicit registrations supply these arities. The native class retains an engine path pointer; its constructor requires the named path under THROW. `level.patrol_path_exists(string)` is the nonasserting existence query. P02/P31–P34.

| patrol object method | Meaning / failure limit | Evidence |
| --- | --- | --- |
| count() | u32; VERIFY path, fallback 0 if null branch reached | P31 |
| point(u32) | Copied Fvector export; invalid point can fall back to first stored vertex after logging; VERIFY nonempty; native m_dummy fallback is not a certified safe destination | P31–P33 |
| level_vertex_id(u32); game_vertex_id(u32) | Respective vertex namespace; VERIFY point; invalid sentinel when fallback branch reached | P31 |
| index(string); get_nearest(Fvector) | Named/geometric nearest patrol vertex index or u32(-1); nearest query does not filter accessibility | P31/P32/P35 |
| name(u32); flag(u32,u8); flags(u32); terminal(u32) | Name/bit flags; terminal means no outgoing edges; assertions and per-helper fallbacks differ, not a universal bounds-safe contract | P31/P32 |

## Ownership, inheritance and validation

The game_object registrar composes its helper registrations; exact type checks occur in the implementations, so a shared wrapper method name does not make every actor/stalker/monster operation applicable to every object. Graph vertices and patrol paths remain owner-held; changing levels or destroying a receiver can invalidate retained references. No ownership transfer/adoption is introduced. P05/P09/P10/P33/P34.

SAFE_WRAP is diagnostic forwarding, not a safe-lifetime/converter exception guarantee. These selected registrations do not certify all build variants, effective addon overrides or arbitrary Lua argument coercions. Source/hash/range/symbol and focused policy checks are recorded in [verification](../../08-research/verification-2026-10-12-v0.1.71.md). Runtime, installed source closure and full planner/pathfinding algorithms remain open. [World guide](../../04-game-systems/world/development-reference.md), [completion status](../../04-game-systems/world/source-completion-status.md).
