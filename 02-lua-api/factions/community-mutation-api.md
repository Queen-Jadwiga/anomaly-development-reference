# Community mutation and live team APIs

> ADR document set: **v0.1.73**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-03-API
- Subsystem: factions / relations
- C++ owners: `CScriptGameObject`, `CInventoryOwner`, `CCharacterInfo`, `CEntity` and selected overrides
- Lua owner: `game_object`; guarded server getter on `cse_alife_trader_abstract`
- Interface kind: selected Lua exports forwarding to native/virtual mutation
- Baseline: ENGINE1011; [provenance](../../00-environment/source-baseline-2026-10-11.md)
- Source status: source-confirmed within selected declarations, registrations and bodies
- Runtime status: untested; deferred until explicitly resumed by the user
- Build/conditional scope: inspected bodies; server getter guarded by `XRGAME_EXPORTS`; no exhaustive configuration projection
- Native versus registered Lua inheritance: receiver casts below, not an exhaustive inheritance inventory
- Example status: none
- Last reviewed: 2026-10-11

M-labels refer to the [FAC-03 ledger](../../evidence/factions/community-mutation-2026-10-11.csv). [The native mutation reference](../../04-game-systems/factions/community-mutation.md) traces phase order, packets and integration limits.

| Lua interface | Exact selected native signature / result | Contract and caveats | Evidence |
| --- | --- | --- | --- |
| `obj:set_character_community(comm,squad,group)` | `void CScriptGameObject::SetCharacterCommunity(LPCSTR,int,int)` | Requires inventory-owner and entity receiver casts; resolves configured ID, calls community bridge, then virtual tuple change with supplied squad/group. No success result or rollback; no optional arguments inferred | M01/M09/M16 |
| `obj:character_community()` | `LPCSTR CScriptGameObject::CharacterCommunity()` | Reads current client character-info community; unsupported inventory-owner receiver logs/returns null. Lua null conversion not certified | M01/M09/M16 |
| `obj:change_team(team,squad,group)` | `void CScriptGameObject::ChangeTeam(u8,u8,u8)` | Receiver cast must be `CCustomMonster`; failure logs/returns. Calls virtual team migration, not community setter. Binding names this exact three-byte-argument overload through `SAFE_WRAP`; arbitrary-number conversion/nil safety not audited | M08/M10/M16 |
| `server:community()` | `LPCSTR CSE_ALifeTraderAbstract::CommunityName() const` | Returns server community ID, or literal `"unknown"` for invalid sentinel; getter registration guarded by `XRGAME_EXPORTS`. Does not mutate/hydrate a client | M11 `554–564`; M12 |

All table entries are borrowed-object/scalar/string interfaces, with no documented ownership transfer. Live receiver methods require a valid current representation; an A-Life registry object is a separate native type, not a replacement `game_object`. Selected string conversion/return lifetimes and every Luabind failure case remain outside this pass.

## Native-only contracts behind the exports

| Native method | State and phase | Boundary |
| --- | --- | --- |
| `CCharacterInfo::SetCommunity(CHARACTER_COMMUNITY_INDEX)` | Changes current index and recomputes sympathy | Does not itself migrate hierarchy or update a server object. M03 |
| `CInventoryOwner::SetCommunity(CHARACTER_COMMUNITY_INDEX)` | Server lookup → client community → alive-only team change retaining old squad/group → trader cast/write → actor display hook | Can return before all phases; no atomic success return. M02 |
| `CEntity::ChangeTeam(int,int,int)` | Same-tuple no-op; otherwise alive/registration assertions → before hook → old unregister → field writes → new register → after hook | Live seniority membership, not native A-Life squad membership. M04/M05/M18 |

A same-tuple call returns before the non-no-op assertions. This does not make arbitrary corpse mutation safe: the outer community setter can change identity before requesting a different tuple. The inner alive-only guard does not guard the outer wrapper's subsequent call. M01/M02/M04.

The setter accepts integer squad/group arguments without local clamping; the separate team API takes `u8` arguments, and selected packet export writes tuple bytes. Do not infer that all integers or all byte values are valid hierarchy identifiers, or that serialization preserves arbitrary out-of-range values. Native fields are integers; table/configuration and hierarchy preconditions still apply. M01/M04/M06/M10/M16/M18/M19.

## Observation, persistence and callbacks

Community server field write is in the inventory-owner call; creature tuple synchronization is a later inspected update-packet path. No setter emits a demonstrated shared Lua “faction switch complete” callback here. Native before/after team hooks surround local migration; stalker hooks preserve combat registration, and base-monster override migrates its monster-squad registration. These are selected virtual paths, not a global strategic completion phase. M04–M07/M11/M17/M19.

Selected server state serialization preserves community and tuple through their separate fields, under the documented build/version scope. Exact update receipt versus save timing and effective script restoration remain unverified. Use [FAC-02](../../04-game-systems/factions/relation-persistence.md) and [A-Life callbacks](../../04-game-systems/alife/callback-phase-reference.md) for existing storage/lifetime boundaries.

Installed actor true-community/disguise producers, Warfare faction-switch helpers, smart/board reassignment and CtZ ownership synchronization require separate source traces. The actor `RPC_UpdateFaction` body here is a Discord display update, not proof of any of those changes. M13.

## Checks

Compared signatures, argument order, registrations, native phases, receiver/assertion paths, hierarchy helpers and selected serialization/receipt bodies. Verified hash/count/range/symbol integrity against the pinned snapshot. No engine build, runtime verification or gameplay change. [Investigation](../../08-research/investigations/2026-10-11-FAC-03-community-mutation.md), [verification](../../08-research/verification-2026-10-11-v0.1.46.md).
