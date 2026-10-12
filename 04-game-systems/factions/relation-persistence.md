# Native relation persistence, reset and ID cleanup

> ADR document set: **v0.1.59**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-02
- Source status: source-confirmed within the selected native paths; cleanup/serializer negative findings are scoped
- Runtime status: untested; deferred until explicitly resumed by the user
- Last reviewed: 2026-10-11

ENGINE1011 is the uploaded October 11 archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Upstream commit and executable/effective profile correspondence remain unknown. P01–P18 refer to the [FAC-02 ledger](../../evidence/factions/relation-persistence-2026-10-11.csv), independently of earlier F-labels. Read with [native relation queries](native-relations.md), [Lua contracts](../../02-lua-api/factions/relations-api.md) and [ALIFE-04](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md).

## Two storage domains

| State | Owner / selected serializer | Reset or lifetime boundary |
| --- | --- | --- |
| Personal goodwill and community-to-character goodwill | `CALifeRegistryContainer::m_character_relations`: `u16 → RELATION_DATA`; each record serializes `personal` then `communities` | Saved/restored by the native A-Life registry path; individual clear empties a record's maps |
| Community-to-community relation matrix and sympathy table | Static `CHARACTER_COMMUNITY` table caches | Level's selected before-load hook clears caches; subsequent access reloads configured tables |
| Wrapper-local relation map without A-Life | `CALifeRegistryWrapper` local fallback | Owned by wrapper; not the active A-Life registry serializer |
| Fight bookkeeping and map-spot cache | Separate static registry pointers | Deleted by `clear_relation_registry`; not the per-character goodwill map |

P01–P07/P12–P16. The native goodwill record includes target IDs in `personal` and community indexes in `communities`, not faction names or campaign fingerprints. Loading those numeric keys does not establish portability across a changed faction-index configuration or prevent ID reuse. P01/P17; [identity reference](../alife/lifecycle-state-reference.md).

## Save/load order and observation phases

The selected native save path writes header, time, spawn data and objects, then `registry().save`. Its registry chunk serializes info portions before character relations, followed by the other auxiliary registries. `RELATION_DATA::save` writes both contribution maps; the abstract registry saves its outer map. P02/P04/P05/P08.

On load, objects and native registry insertion are reconstructed with final `on_register` callbacks disabled. The auxiliary registry, including character relations, loads next; only then is final `on_register` enabled and the loop invoked. The generic map loader's default predicate clears existing containers and accepts serialized entries; it is not a live-object referential-validity filter. P04/P05/P08/P17.

Thus the selected final native registration loop occurs after relation-record restoration. `on_before_register` still occurs during the earlier native insertion path; the guarded `CALifeStorageManager_load` functor occurs before the native reads in this function. Neither is a post-restoration guarantee. This does not establish the order of installed Lua `on_game_load`, diplomacy restoration, CtZ storage or the later group-member repair described in ALIFE-04. P08/P10 and [callback reference](../alife/callback-phase-reference.md).

The save callback's selected before-save hook is guarded by `ENGINE_LUA_ALIFE_STORAGE_MANAGER_CALLBACKS`. Source presence does not prove build flags, a bound listener or successful installed save behavior. P08.

## Matrix changes have a different durability contract

`set_community_relation` reaches the static character matrix setter, which changes one cached cell. `CHARACTER_COMMUNITY::Reset` clears relation and sympathy table caches. The selected `CLevel::Load_GameSpecific_Before` invokes this reset, alongside rank, reputation and monster-table resets. Subsequent table access reloads from `pSettings`; the reset itself does not delete the community ID/index vector. Full `DeleteIdToIndexData` is a separate disposal operation. P13–P15/P18; FAC-01 F03/F09.

The inspected A-Life relation serializer contains the per-character maps, not this static matrix. **A matrix write is therefore not given native save durability by that serializer.** A script/addon may explicitly save and reapply diplomacy after reset; its implementation and effective ordering must be traced before promising persistence. This is a bounded storage/reset conclusion, not an engine-wide assertion that no diplomacy addon persists relations. P01–P05/P13–P15/P18.

## What individual cleanup actually removes

`CSE_ALifeMonsterAbstract::on_unregister` runs its inherited hook, calls `ClearRelations(ID)`, then its brain hook and group member unregister when applicable. Native `unregister_object` invokes that virtual hook before removing the server object from subsequent registries. Overrides must actually reach this native path; effective creature overrides remain unresolved. P09/P10.

`ClearRelations(id)` looks up **that one outer record** and calls `RELATION_DATA::clear`. It empties both maps but does not erase the outer record. It has no loop over other characters and no removal of their `personal[id]` entries. P02 `32–36,123–130`; P05.

| Example state before `ClearRelations(A)` | Selected result |
| --- | --- |
| `A.personal[B]` | Removed with A's personal map |
| `A.communities[faction]` (faction → A goodwill) | Removed with A's community map |
| `B.personal[A]` | Not touched by this function |
| Outer record keyed by A | Retained with empty maps if previously present |
| Community matrix cell | Not touched |

This is a source-state example, not an in-game experiment. The remaining incoming ID-keyed entry could address a later object if the numeric ID is reused and no additional cleanup runs. That is a conditional implication, **not an observed contamination bug** or proof about installed scripts. The selected serializer also does not reconcile those entries against the live object set. P01/P02/P17; A-Life identity/release evidence.

Ordinary online/offline client teardown is not native server unregistration, and death is not automatically permanent release. Do not clear goodwill merely because a client disappeared or a death notification fired; use the established server lifecycle and effective policy. [ALIFE-07](../../08-research/investigations/2026-10-11-ALIFE-07-client-server-offline-teardown.md), [WAR-002b](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md).

## Full lifetime and wrapper cleanup

With A-Life present, wrapper calls route to the current simulator relation registry. Reads can return no record; writes create one when absent. Without A-Life, its separate local map is used, and even `objects_ptr` creates an absent local record. Deleting a wrapper is not equivalent to clearing the simulator-owned relation map. P06/P07.

A-Life unload deletes the object registry first, whose destructor invokes every object's virtual unregister hook before deleting them; the auxiliary registry container is deleted later. Reload constructs a new container. That owner lifetime is broader than an individual record clear. P11/P12.

`RELATION_REGISTRY::clear_relation_registry` deletes wrapper, fight-registry and map-spot pointers. The inspected call-site search in `src/` finds the module-detach call; it does not make this function a documented per-level goodwill reset API. P02/P16. No Lua cleanup export, universal inbound-reference purge or runtime cache-reset recipe is introduced here.

## Development implications and next work

Track separately which state must persist: personal/community goodwill records, dynamic faction matrix, strategic owners or CtZ records. Record who saves/restores it and the phase relative to native restoration/table reset. Reacquire ID-backed state with campaign/lifetime context rather than treating a stored number as permanent identity. These are source-derived design implications, not gameplay changes.

FAC-02 completes this bounded native persistence/cleanup pass. Effective diplomacy serializers, overrides and runtime behavior remain open. Later [community mutation](community-mutation.md), [action updates](action-goodwill.md) and [FAC-06 consolidation](development-reference.md) are complete within scope. [Effective integration](source-completion-status.md) remains open.
