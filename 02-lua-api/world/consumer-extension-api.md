# Selected dynamic restriction consumer extensions

> ADR document set: **v0.1.80**. Research revisions and source/build versions below describe their original scope.

- ID: WORLD-04-API
- Subsystem: world interaction/navigation
- Research revision: v0.1.73
- C++/Lua owner: CScriptGameObject → game_object, with CSpaceRestrictor/CCustomMonster receiver casts
- Interface kind: native Lua exports reached by supplied consumer
- Baseline/provenance: ENGINE1011; [manifest](../../evidence/manifest.md)
- Source status: source-confirmed selected exports/implementation/default-manager callers
- Runtime status: untested; deferred
- Build scope: inspected registrar/native bodies; executable/compiler/profile correspondence unknown
- Evidence: [C06–C10 ledger](../../evidence/world/supplied-consumers-2026-10-12.csv), [consumer reference](../../04-game-systems/world/supplied-consumers.md)
- Example status: none; source call shapes only
- Last reviewed: 2026-10-12

| Lua shape after receiver | Native contract | Boundary |
| --- | --- | --- |
| force_set_restrictor_type(u8) | void; CSpaceRestrictor required, wrong type no-op; enum validation and same-type return, then old unregister/new register | Live restriction/default-manager state; no server-field synchronization or universal receiver/manager readiness guarantee |
| invalidate_restrictions() | void; CCustomMonster required; wrong type diagnoses/returns; sets movement restriction actual(false) | Path refresh notification, not completed rebuild or observed route success |

ENGINE1011 `script_game_object3.cpp:2678–2724`, `script_game_object_script3.cpp:389–393`, `xrServerEntities/restriction_space.h:27–36`, `space_restriction_holder.cpp:115–150,183–205` (C07–C10). Selected supplied anomaly consumer uses 2 = eDefaultRestrictorTypeIn and 3 = eRestrictorTypeNone. The native setter's enum whitelist is not proof that every value's downstream manager preconditions hold; broader type combinations remain optional depth. No ownership adoption is introduced. Lifetimes follow [WORLD-02](spatial-api.md); default versus base/client/server state remains distinct.

The supplied poller and post-loading registration are C06, not independent runtime observations. Persistence, callback aliases, actor/zone readiness, invalid references and winning wrappers remain effective gaps. Reproduction/source checks are in [verification](../../08-research/verification-2026-10-12-v0.1.73.md); no engine/game test ran.
