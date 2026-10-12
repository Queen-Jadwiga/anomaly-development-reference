# Focused faction and relation Lua contracts

> ADR document set: **v0.1.60**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-01-API
- Subsystem: factions / relations
- C++ owners: `CScriptGameObject`, `RELATION_REGISTRY`, `CHARACTER_COMMUNITY`, native helper functions
- Lua owners: `game_object` methods and `relation_registry` module
- Interface kind: selected Lua exports; `relation` continues through native virtual dispatch
- Source baseline: ENGINE1011; [provenance](../../00-environment/source-baseline-2026-10-11.md)
- Source status: source-confirmed within selected declarations/definitions/registrations
- Runtime status: untested; deferred until explicitly resumed by the user
- Build/conditional scope: inspected registration bodies; no all-build/configuration projection
- Native versus registered Lua inheritance: scoped receiver casts below; no exhaustive inheritance/converter inventory
- Example status: none
- Last reviewed: 2026-10-11

Evidence F01–F18 refers to the [FAC-01 ledger](../../evidence/factions/native-relations-2026-10-11.csv), pinned to the uploaded source archive hash in the [native reference](../../04-game-systems/factions/native-relations.md). This is a focused contract table, not an exhaustive faction API catalog or a promise of optional Lua arguments.

## Queries: receiver and direction matter

Method signatures below show Lua argument order after the receiver; native argument/result types come from the selected declarations and bodies. Pointers to another `CScriptGameObject` are exposed as object arguments, with conversion policy and nil behavior not exhaustively audited.

| Lua interface | Selected native signature / return | Meaning and preconditions | Evidence |
| --- | --- | --- | --- |
| `obj:character_community()` | `LPCSTR CharacterCommunity()` | Receiver must be `CInventoryOwner`; returns its configured community ID, not a numeric index or owner state. Unsupported receiver logs and returns null; Lua null conversion is not certified here | F10 `1045–1055`; F11/F18 |
| `obj:goodwill(other)` | `int GetGoodwill(CScriptGameObject*)` | Personal `obj → other` contribution. Receiver inventory-owner cast checked; unsupported receiver logs and returns 0. Target is dereferenced for ID | F10 `750–761`; F11/F18 |
| `obj:community_goodwill(community)` | `int GetCommunityGoodwill_obj(LPCSTR)` | Community's goodwill **toward obj**. Inventory-owner receiver check; community ID resolves through native lookup | F10 `852–866`; F11/F18 |
| `obj:general_goodwill(other)` | `int GetAttitude(CScriptGameObject*)` | Full five-term character attitude `obj → other`; both inventory-owner casts are asserted, with no local graceful fallback | F05 `69–93`; F10 `886–894`; F11/F18 |
| `obj:relation(other)` | `ALife::ERelationType GetRelationType(CScriptGameObject*)` | Validates `CEntityAlive` types, then virtual dispatch. Stalker/trader selected human path is directed registry classification; base path uses monster matrix | F12–F16/F18 |
| `relation_registry.community_goodwill(community, entity_id)` | `int g_community_goodwill(LPCSTR,int)` | Community → character, by registry ID; helper casts integer to `u16`, without local range validation or client lookup | F09 `1170–1176,2935–2945` |
| `relation_registry.community_relation(from,to)` | `int g_get_community_relation(LPCSTR,LPCSTR)` | Directed community matrix cell; strings resolve configured indexes, not arbitrary faction labels | F01/F03; F09 `1192–1200,2935–2945` |
| `relation_registry.get_general_goodwill_between(from_id,to_id)` | `int g_get_general_goodwill_between(u16,u16)` | Personal + community-to-character + community-to-community terms only; server objects must cast to `CSE_ALifeTraderAbstract`. Failed cast logs and returns 0; registry lookup/assertion behavior still applies | F09 `1212–1231,2935–2945` |

**The two “general goodwill” interfaces are not equivalent.** The game-object method adds rank and reputation relations; the module helper omits them. A returned zero can be neutral contribution or an error fallback depending on the path; it is not a standalone success indicator. F05/F09/F10.

The selected enum registration names friend, neutral, enemy and dummy. The base monster path can return native worst enemy even though that name is absent from this particular enum list. Do not invent a Lua named constant from that native value or extrapolate to every registration body. F12 `39–49`; F16.

## Mutations: selected contracts, not tested recipes

| Lua interface | Native signature / result | Mutation and validation boundary | Evidence |
| --- | --- | --- | --- |
| `obj:set_goodwill(value,other)` | `void SetGoodwill(int,CScriptGameObject*)` | Personal receiver → target contribution, clamped by configured personal limits. Unsupported receiver logs/returns; target dereference assumes a valid object | F06 `154–162`; F10 `763–774`; F11/F18 |
| `obj:change_goodwill(delta,other)` | `void ChangeGoodwill(int,CScriptGameObject*)` | Read personal value + delta → same clamped setter | F06 `182–186`; F10 `789–800`; F11/F18 |
| `obj:force_set_goodwill(value,other)` | `void ForceSetGoodwill(int,CScriptGameObject*)` | Native server trader casts required; subtracts two community terms, writes personal value directly, omitting rank/reputation and the selected personal clamp | F06 `164–179`; F10 `776–787`; F11/F18 |
| `obj:set_relation(enum,other)` | `void SetRelation(ALife::ERelationType,CScriptGameObject*)` | Both objects must be inventory owners; target cast has an assertion before fallback. Writes configured personal preset for enemy/neutral/friend; does not lock final category | F05 `25–46`; F10 `804–824`; F11/F18 |
| `obj:set_community_goodwill(community,value)` | `void SetCommunityGoodwill_obj(LPCSTR,int)` | Community → receiver contribution, clamped by configured community limits | F06 `208–217`; F10 `868–882`; F11/F18 |
| `relation_registry.set_community_goodwill(community,id,value)` | `void g_set_community_goodwill(LPCSTR,int,int)` | Same contribution via target `u16` ID; not an online-object requirement | F09 `1178–1183,2935–2945`; F06 |
| `relation_registry.change_community_goodwill(community,id,delta)` | `void g_change_community_goodwill(LPCSTR,int,int)` | Same ID cast; read + delta → clamped community setter | F09 `1185–1190,2935–2945`; F06 |
| `relation_registry.set_community_relation(from,to,value)` | `void g_set_community_relation(LPCSTR,LPCSTR,int)` | Directed matrix cell only; reverse cell not automatically written; valid configured identities required | F09 `1202–1210,2935–2945`; F01 |

These scalar/value interfaces do not transfer ownership or create entities. Live object arguments require valid current representations; pointers are not durable campaign identities. Module ID calls avoid client-object arguments but do not validate campaign identity or guarantee safe out-of-range conversion. Apply the [A-Life identity/lifetime boundary](../../04-game-systems/alife/lifecycle-state-reference.md).

No inspected setter establishes completed AI reevaluation, a UI refresh, strategic ownership, a shared script callback or save durability. Native [persistence](../../04-game-systems/factions/relation-persistence.md), [community mutation](community-mutation-api.md) and [action-driven changes](action-values-api.md) now have scoped follow-ups; effective integration remains open. `set_character_community` is outside this FAC-01 table; its downstream identity/team/AI chain is now traced in [FAC-03 contracts](community-mutation-api.md). No gameplay change is proposed.

## Checks and limitations

Signatures, argument order, helper bodies, receiver checks, virtual path and literal names were compared with F09–F18 and the registry definitions. Full-file hashes, line counts, cited range bounds and symbol presence were checked against the snapshot. Runtime, installed tables/scripts, all native derived overrides, converter/error behavior and exhaustive conditional export coverage remain unverified. See [FAC-01](../../08-research/investigations/2026-10-11-FAC-01-native-relations.md) and [verification](../../08-research/verification-2026-10-11-v0.1.44.md).

Native persistence/reset and ID-cleanup boundaries are now traced in [FAC-02](../../04-game-systems/factions/relation-persistence.md). These findings do not certify installed diplomacy save/reapply or UI/AI refresh.
