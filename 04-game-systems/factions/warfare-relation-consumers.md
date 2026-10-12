# Supplied Warfare faction and relation consumers

> ADR document set: **v0.1.57**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-05
- Source status: source-confirmed within selected BETA150 main-package paths
- Runtime status: untested; deferred until explicitly resumed by the user
- Last reviewed: 2026-10-11

Baseline BETA150 archive SHA-256 `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d`. This pass uses the **main package** script paths, not an assumed installation combining optional GAMMA patches, ZIP142 or public sources. R01–R20 refer to the [consumer ledger](../../evidence/factions/warfare-consumers-2026-10-11.csv). Installed winners, settings, helpers and callback order remain unknown; [package provenance](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).

This page retains the FAC-05 consumer investigation scope. The later [FAC-06 consolidation and final available-source audit](development-reference.md) now complete those separate tasks; installed integration remains open.

## Identity inputs are separate

`sim_squad_scripted:get_squad_community()` maps `player_id` through `squad_community_by_behaviour`; it is not a query of every member's native character community. Main Warfare adds a trader mapping and caches `actor_faction` from `get_actor_true_community()` with server-community `sub(7)` fallback at the selected update phases. The PDA tab obtains the true-community helper independently. These producer calls do not prove installed disguise/true-community semantics or instantaneous agreement between caches. R07–R09/R18.

`warfare_factions.factions` is the selected participating list, while `all_factions` also includes monster. Those script lists are not the native configured community-index order. `game_relations` has its own faction lists, including actor-prefixed identities. Do not turn these list positions into native faction IDs. R01/R19; [FAC-01 identity](native-relations.md).

## Helper names and actual contracts

The supplied `game_relations.script` declares FRIENDS=1000 and ENEMIES=-1000. Its friend/enemy predicates compare a **directed native community-matrix cell** inclusively against those thresholds; neutral is strictly between them. These are this script's thresholds, not proof of equality with native full-attitude thresholds. R01/R02; [native relation resolution](native-relations.md).

| Supplied helper | Selected effect | Boundary |
| --- | --- | --- |
| `get_factions_community(from,to)` | Read native directed matrix cell | Omits personal/community-to-character, rank and reputation contributions |
| `is_factions_friends/enemies/neutrals(from,to)` | Classify that directed cell | Reverse direction is not automatically queried |
| `set_factions_community(from,to,value)` | Numeric conversion, named enemy/friend mapping (-5000/+5000), otherwise 0, then directed setter | Does not itself save both directions or mutate characters |
| `set_factions_community_num(from,to,value)` | Directed native matrix write | No demonstrated saved-state write in this helper |
| `change_factions_community_num(faction,obj_id,delta)` | Change community goodwill **toward a character ID** | Despite name, not a faction-to-faction delta |
| `save_relation(a,b,value)` | Write both directions and call actor `save_var` for both named keys | Script supplies symmetry/storage intent; native setter itself does neither |
| `load_relation(a,b)` | Read each stored direction independently and apply non-nil values | Depends on effective load_var/storage and dispatch order |

R02/R03. Guards reject selected nil/`"none"` inputs but do not fully validate configured identities: the second faction nil case is not consistently rejected by these guards. They are not safe arbitrary-input contracts. The native lookup/converter requirements remain those in [FAC-01 APIs](../../02-lua-api/factions/relations-api.md).

## Selected consumer map

| Consumer | Value and direction | Decision / distinction |
| --- | --- | --- |
| Squad arrival | Smart owner → squad community enemy predicate | Non-hostile gate before smart reach test/after-reach action; not proof of arrival or ownership |
| Squad fog/PDA visibility | Some branches actor faction → squad; info/hide branches squad → actor | Opposite query directions appear in one module; symmetry must come from actual policy |
| Squad relation tooltip | Average loaded members' `general_goodwill(actor)`; fallback below | Full character attitude label differs from faction-only visibility/target gates |
| Warfare PDA dominance style | Faction → true actor faction matrix | Selects friend/enemy/neutral UI style; no personal goodwill or full attitude |
| Faction enemy boosts | Faction → cached actor faction | Adds configured base/resource boosts in selected statistics path |
| Resurgence candidates | Smart owner → spawning faction | Includes unowned or hostile bases; not live NPC attitude |
| Smart ownership/influence | Selected faction/owner/actor matrix tests | Nested transfer and influence bookkeeping; not a universal strongest-faction rule |
| Offline enemy validation | First squad community → second squad community | Combined with offline, occupancy, ignore/mutant and distance gates |

R11/R12/R15/R16/R18/R19. Ownership/target/reach context remains [WAR-002b](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md), rather than being redefined by this table.

The tooltip averages only member objects available in `db.storage` when an actor exists. Its hardcoded ±1000 classification applies to that average. If none are counted, it falls back to actor `community_goodwill(squad.player_id)` plus `get_factions_community(squad.player_id, server actor community)`; recognized monster player IDs return an enemy label earlier. A missing squad returns neutral. This is a display approximation, not a universal squad AI relation. R12.

Several modules bind helper functions to local aliases at module initialization (`is_enemy`, `is_factions_enemies/friends`). Replacing the exported helper later does not by itself replace those already captured references. This is a Lua/source implication; installed module order/reloads remain unknown. R15/R16.

## Strategic relation mutation and persistence intent

`change_faction_relations` reads both directions and uses the larger absolute magnitude as its base. A force argument uses the supplied delta as the new value; otherwise it adds delta. Beyond configured friend/enemy limits it randomly chooses zero or the limit. It then calls `save_relation` for ordinary factions and two actor-prefixed pairs, writing six directed cells and named actor variables. Selected threshold crossings send news; hostility can call goodwill reset. R04.

That save/reapply mechanism is the supplied script layer FAC-02 explicitly left open, not evidence that the native matrix serializer changed. Its `on_game_load` runs restoration/reset only under `USE_MARSHAL`, uses `alife_storage_manager.get_state().new_game_relations`, and its startup registers `npc_on_death_callback` and `on_game_load`. Effective storage wrapper implementation, listener installation/order and placement relative to native table reset remain unresolved. R03/R06; [FAC-02](relation-persistence.md).

Keep literal code caveats visible: `reset_goodwill` uses an `or ("actor_" .. faction)` string operand, so that expression is truthy rather than the implied second equality check. The selected relation calculator repeats the neutral interval in its following friend-count `elseif`; it does not establish the comment's intended friend counting. These source observations are not fixes or reproduced runtime defects. R04.

Warfare all-out-war has separate paths: selected first update writes -5000 between distinct participating factions; `apply_all_out_war` writes -4000, selected actor-prefixed cells and, when its dynamic-relations flag is set, actor stored relation keys. Initialization/options govern these calls. Neither literal value is asserted as the user's active diplomacy. R08/R09.

## Contested targets, deaths and awards

The smart diplomatic-penalty function requires dynamic relations and the territory-penalty option, permits only eligible distinct faction pairs, and excludes stalker/ecolog involvement. It computes a negative configured death-value × contested smart capacity and calls `change_faction_relations`. Selected target invalidation loops invoke it after removing non-hostile, nonempty targets, subject to ceasefire-owner checks. This is a strategic diplomacy input, not a native personal attitude setter. R14.

Dynamic death adapters are distinct. Online adapter requires stalker victim/killer and loaded objects, normalizes actor-prefix character communities and checks unaffected factions. Offline adapter takes server objects, excludes monster/zombied communities and uses server rank/reputation helpers; its early unaffected-faction return is commented out. Both call the same stochastic relation calculator, which has further pair gates. No total equivalence or one-change-per-casualty guarantee follows. R05/R04.

Offline combat outcome calls the offline adapter, then has separate script rank/bookkeeping: selected attacker rank scales with damage, commander gets a random bonus, and server storage kill statistics update. Those are not FAC-04's native victim-rank-band reward. Outcome is not necessarily per victim in full-defeat processing; retain [WAR-002b casualty ordering](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md). R17.

The supplied squad member-death listener separately rewards actor support only for registered Warfare squads, actor-ID killer and victim faction → actor faction hostility. It grants configured money, actor-faction goodwill via `xr_effects`, and influence, with a loner special case. Missing/effective reward helper and dispatch prevent promising exact stacking/deduplication with native/dynamic awards. Option producers are UI reads, not installed numeric values. R13/R20.

Finally, ignored-squad identity handling contains a commented trader conversion block. Active code uses a story-community mapping and native `set_character_community(mapped,0,0)` only for available living members and participating mapped factions; it marks its one-shot flag before the loop. It does not actively perform the commented `squad.player_id="trader"` rewrite here or guarantee unloaded members convert later. R10; [FAC-03 mutation contract](community-mutation.md).

## Disposition and missing effective edges

FAC-05 completes selected BETA150 main-package helper/consumer traces. It does not exhaust every quest/dialog/menu predicate or optional package variant. Winning `game_relations`, globals/true-community mappings, storage, reward helpers, board/smart/creature overrides, applied configuration and startup/replacement order are still needed for installed closure.

The later [FAC-06 completion status](source-completion-status.md) records the completed consolidation/audit and remaining effective-source requirements. No gameplay changes, script fixes or runtime tests occurred.
