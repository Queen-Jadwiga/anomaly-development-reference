# Native faction identity, goodwill and relation resolution

> ADR document set: **v0.1.68**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-01
- Source status: source-confirmed within selected native definitions and Lua registrations
- Runtime status: untested; deferred until explicitly resumed by the user
- Last reviewed: 2026-10-11

Baseline ENGINE1011 is the uploaded October 11 source archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Upstream commit, installed executable, configuration tables and GAMMA overrides remain unknown. F01–F18 below are local to the [native relation ledger](../../evidence/factions/native-relations-2026-10-11.csv), which records paths, symbols, ranges and hashes. Read with the [focused Lua contracts](../../02-lua-api/factions/relations-api.md) and [investigation](../../08-research/investigations/2026-10-11-FAC-01-native-relations.md).

## Identity is not attitude or ownership

`CHARACTER_COMMUNITY` holds a configured string ID and integer index, with a separately loaded team value. Its loader reads `game_relations/communities`; indexes follow insertion order in the configured ID/team pairs. The relation matrix uses `communities_relations`, and sympathy uses `communities_sympathy`. Rows resolve by community ID; columns follow configured indexes. The table is loaded lazily and cached. These are native configuration contracts, not a verified list of installed factions, team numbers or relations. F01–F04.

The ID lookup uses `xr_strcmp`. Although loading creates a lowercase temporary, the selected insertion uses the original ID string. Do not assume case-insensitive lookup, invent numeric faction IDs or use indexes as portable save identifiers across different configuration orders. Unknown IDs and out-of-range indexes reach assertion/fatal paths; this is not a validated arbitrary-string API. F03 `55–69,83–93,124–151`; F08.

| State | Direction / storage | Meaning |
| --- | --- | --- |
| Character community | One character's configured identity | Membership identity; distinct from rank/reputation and squad assignment |
| Personal goodwill | `from → to`; source-character record's `personal[to]` | Explicit individual contribution; absent entry returns neutral zero |
| Community goodwill | `community → character`; target-character record's `communities[community]` | How that community regards the character, not the reverse |
| Community relation | Matrix `[from][to]` | Directed faction-to-faction contribution; setter writes one cell |
| Final attitude / relation type | Computed for the selected observer and target | Derived value/category using multiple contributions |
| Warfare smart owner / CtZ owner model | Separate strategic state | Not proved or changed by a native goodwill query |

F01/F05–F08. The final row is the integration boundary from [WAR-002b](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md). No automatic synchronizer between these models is established.

## Native attitude and thresholds

For inventory-owner arguments, `RELATION_REGISTRY::GetAttitude(from,to)` adds five terms:

```text
personal goodwill(from ID, to ID)
+ reputation relation(from reputation, to reputation)
+ rank relation(from rank, to rank)
+ community goodwill(from community, to ID)
+ community relation(from community, to community)
```

F05 `69–93`; F06 `236–248`. This pass establishes the selected aggregation and delegated rank/reputation calls, not all rank/reputation table initialization or action-based updates.

`GetRelationType` reads the literal keys `game_relations/attitude_neutal_threshold` and `attitude_friend_threshold` into function-local statics. The misspelling `neutal` is part of the inspected key. Below the neutral threshold is enemy; from that threshold up to but excluding the friend threshold is neutral; at or above the friend threshold is friend. The `NO_GOODWILL` sentinel maps to neutral in this function. Active threshold values remain unknown; normal missing personal/community entries return zero, not this sentinel. F05 `49–66`; F06 `131–151,190–205`; F07/F08.

Directed resolution does not assume reciprocity. The separate native `GetRelationBetween` checks both directions, choosing enemy if either is enemy, otherwise neutral if either is neutral, otherwise friend. This is a different helper, not the implementation invoked by the selected stalker/trader Lua `relation` path. F05 `10–22`; F13–F15.

## Which relation does a live object resolve?

`game_object:relation(other)` validates `CEntityAlive` types and invokes virtual `tfGetRelationType`. The selected stalker and trader overrides use directed character-registry resolution for inventory-owner targets that are not base monsters, then fall back to their inherited path otherwise. F12–F15.

Base `CEntityAlive` uses the separate `MONSTER_COMMUNITY` matrix, whose configuration comes from `monster_communities/communities` and `monster_relations`. Values 1, 0, -1 and -2 map to friend, neutral, enemy and worst enemy respectively; other values map to dummy. That integer matrix is not the character goodwill threshold table. This pass does not trace every derived monster or actor override. F16/F17.

**Practical implication:** identify the receiver's native type and lookup path before interpreting a displayed relation. Being castable to `CEntityAlive` does not certify current health is positive; the wrapper does not call `g_Alive()` here. An unsupported native type logs and returns dummy; a nil/dangling argument is not shown to be safe. F13.

## Selected mutations and limits

| Native operation | Inspected effect | Qualification |
| --- | --- | --- |
| `SetGoodwill` / `ChangeGoodwill` | Write personal contribution; clamp to `action_points/personal_goodwill_limits` | Not a direct final-attitude setter; limits cached in a local static |
| `SetCommunityGoodwill` / `ChangeCommunityGoodwill` | Write community-to-target contribution; clamp to `community_goodwill_limits` in `action_points` | Different storage direction and limit from personal goodwill |
| `SetCommunityRelation` | Write directed community matrix cell through `CHARACTER_COMMUNITY` | No mirrored reverse-cell write or clamp in the selected setter |
| `SetRelationType` | Select `goodwill_enemy`, literal `goodwill_neutal`, or `goodwill_friend`, then call personal `SetGoodwill` | Does not subtract the other attitude terms; requested enum alone does not guarantee final category |
| `ForceSetGoodwill` | Subtract community-to-character and community-to-community terms before directly writing personal goodwill | Omits rank/reputation compensation and bypasses the selected `SetGoodwill` clamp; not a permanent diplomacy lock |

F05 `25–46`; F06 `154–186,208–227,252–255`; F01 `80–96`. “Force” compensates only the two selected community terms. Later state changes can affect the derived result; this is a source implication, not a tested tuning instruction.

Configuration loading/caching and relation writes do not prove installed script refresh order, serialization, AI target reevaluation, UI updates or callbacks. `RELATION_DATA` has native save/load methods, but their outer integration and the mutable community matrix's persistence are deliberately left for the next pass. No callback or save durability guarantee is added here.

## CtZ use and remaining work

For a display, label what is being queried: community matrix, faction goodwill toward a character, three-term server aggregate, full character attitude or virtual live-object relation. A faction icon, smart owner or hostile squad is not independent proof of all those values. Use the [API table](../../02-lua-api/factions/relations-api.md) to avoid interchanging similarly named getters.

FAC-01 completes the native identity/query foundation within scope. Those native and selected supplied-package follow-ups are now complete within scope; [FAC-06](development-reference.md) consolidates them. Effective diplomacy integration remains open under the [completion rule](source-completion-status.md). Installed relation values and runtime verification remain open.

Follow-up: [FAC-02 persistence, reset and ID cleanup](relation-persistence.md) closes the bounded native storage question; effective diplomacy persistence remains open.
