# Action-driven goodwill, rank and reputation

> ADR document set: **v0.1.72**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-04
- Source status: source-confirmed within selected native action/caller paths
- Runtime status: untested; deferred until explicitly resumed by the user
- Last reviewed: 2026-10-11

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee` pins the source; upstream commit/executable and effective GAMMA policy/configuration remain unknown. A01–A20 refer to the [FAC-04 ledger](../../evidence/factions/action-goodwill-2026-10-11.csv), separate from earlier F/P/M labels. Read with [native relation queries](native-relations.md), [community mutation](community-mutation.md), [persistence](relation-persistence.md) and [rank/reputation Lua contracts](../../02-lua-api/factions/action-values-api.md).

## Selected online entry paths

After the selected `CEntityAlive::Hit` has applied condition/inherited hit processing, it registers a fight and invokes `Action(ATTACK)` only in single-player when the victim is still alive and the attacker casts to a living, different `CEntityAlive`. This gate does not establish that every hit, lethal hit or offline casualty awards an attack change. A01 `276–313`.

In `CEntityAlive::Die`, the single-player path calls `Action(KILL)` before inherited death processing and before the object-bound `eDeath` callback. The latter therefore follows this particular native action attempt, but not necessarily completed effective script bookkeeping or permanent release. Derived death paths and installed handlers remain separate. A01 `321–339`; [A-Life callback boundaries](../alife/callback-phase-reference.md).

`Action` requires the source to be an inventory owner and excludes a base-monster source. Although a comment says actor-only, the actual common gate is broader. For a stalker target it attempts to set the target's relation flags and resolves the target's directed relation **toward the source** before choosing the action branch. This flag operation precedes attack throttling; it is not proof that a goodwill/reputation award occurred. A03 `97–123`.

## Fight memory, throttling and inferred help

`FightRegister` expires stale fights, updates an existing attacker/defender pair or inserts a new pair with time, accumulated damage and initial defender relation. `FindFight(id,true)` returns the first matching attacker entry, not a demonstrated most-recent pair. Expiry compares millisecond `Device.dwTimeGlobal` against `fight_remember_time × 1000`; `UpdateFightRegister` is called by this selected registration path, not established as a periodic scheduler here. A02/A19.

For an actor source, `ATTACK` looks up the source's first fight record and suppresses the remaining branch when elapsed time since its `attack_time` is below `min_attack_delta_time × 1000`; otherwise it updates that timestamp. The inspected code relies on a fight record and has no local null check before dereference. The shown Hit route registers first, but this is not a safe arbitrary external `Action` API. The throttle is not a universal per-victim rate guarantee. A02/A03.

The actor branch can infer help if the attacked target itself has an attacker record and that record's defender resolves to a stalker. It recursively applies human- or monster-help according to whether the recorded attacker resolves to a stalker. This is a fight-memory inference, not proof of the actor's intent or every ally assist. Both help enums use the same outcome branch; `SOS_HELP` is declared but has no implemented case in this inspected action switch. A03 `127–140`; A04 `297–356`; A18.

## Outcome gates and directions

All configured deltas below come from the selected `action_points` readers. Their installed magnitudes/signs are unknown; “help” does not itself prove a positive reward.

| Action, with selected stalker target | Personal/community goodwill gate and direction | Reputation / rank |
| --- | --- | --- |
| Attack | Nonzero selected personal delta, and source is **not another stalker**. Apply each member of target's live hierarchy group → source; community of target → source uses target sympathy × configured community attack delta | Reputation delta applied separately when nonzero. No rank award in this branch |
| Kill | Nonzero selected personal delta, and source/target are not same-community stalkers. Apply group-entry loop except victim ID → source; community of victim → source uses sympathy × community kill delta | Reputation delta applied separately; rank delta independently comes from victim stalker's rank band |
| Human/monster fight help | Helped stalker must still be alive; nonzero selected personal delta. Apply each member of helped stalker's live hierarchy group → source; community of helped stalker → source uses sympathy × community help delta | Reputation delta applied separately. No rank award in this branch |

A04 `187–214,258–293,297–351`. The kill loop excludes the victim ID; it does not itself check every other group member's health. The group is the live team/squad/group hierarchy, not the A-Life strategic squad object traced in FAC-03.

Community goodwill is **nested inside the nonzero personal-goodwill branch**, so a nonzero community delta alone does not guarantee application. The float sympathy product is cast to integer goodwill, then applied only if nonzero. Personal/community changes use their existing clamped registry setters. Reputation and kill rank are outside that goodwill gate; same-community suppression does not automatically suppress them. A04/A12.

Attack selection uses `danger_` or `free_` settings. The danger branch requires an actor source, a selected human enemy of the victim, and that selected enemy's relation toward the actor to be enemy. It is not simply “victim is in combat,” “source is hostile” or a guaranteed danger classification. A03 `143–164`.

The kill branch's `relation_before_attack` name/comment does not establish historical relation use: the fight-record lookup/assignment is commented out, and active code assigns the just-computed current relation. Rank points use the **victim's** band, not the killer's band or a universal constant. Native monster victims do not reach this stalker-target reward branch; other script systems may award separately. A04 `218–293`.

## Rank/reputation as values and attitude inputs

Rank configuration uses `game_relations/rating`, `rank_relations` and one-column `rank_kill_points`. Reputation uses `game_relations/reputation` and `reputation_relations`. Value-to-index picks the first configured threshold strictly greater than the value; if none, it returns the last index. Equality advances past that threshold. Order and installed values remain configuration-dependent. A05/A06.

These numerical values feed two directed attitude-table contributions in the five-term calculation from FAC-01. A rank change can alter its band/attitude contribution independently of explicit personal goodwill, but exact hostility impact depends on installed tables and the other terms. A05/A06/A11/A12.

`CInventoryOwner::SetRank` and `SetReputation` require a matching server object/trader before writing live and server values. Change methods add a delta then call setters; these selected bodies do not clamp numeric rank/reputation. This differs from personal/community goodwill limits. Lookup/assertion and effective overrides still apply; arbitrary values are not recommended. A07.

Actor rank/reputation side effects invoke RPC-named functions which read script producers and update Discord display fields. They are not a demonstrated shared Lua reward-completion callback or proof that PDA/CtZ state refreshed. A13. Server serialization/hydration of rank/reputation was pinned in FAC-03 M03/M11; that does not close effective storage or save timing.

Rank/reputation relation caches and rank kill-point cache have native Reset operations; the level-before-load hook from FAC-02 invokes them. This does not establish dynamic rereading of already initialized action deltas. Attack `danger_/free_` storage loads when the relation wrapper is first created; most action readers and timer values are function-local statics. Active addon settings/reload policy remain open. A03/A16/A17; FAC-02 P02/P13.

## Flags and callback limits

Selected Lua interfaces can copy/write stalker relation flags; they do not run the action function. Construction zeroes flags. Registered action names are attack, kill and human/monster fight help; the native KILL value is literal zero, so it must not be treated as an independently set nonzero event bit. No counted event history, deduplication, campaign persistence or reliable award receipt follows from a flag query. A09/A14/A15/A18/A20.

The selected native death callback follows Action and inherited Die, whereas an attack flag attempt occurs before throttle/outcome gates. Do not equate these observation points or assume a notification means all strategic cleanup has run. A01/A03.

## Warfare/CtZ integration and next work

Supplied offline combat calls server creature death methods and separate script bookkeeping, as documented in [WAR-002b](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md). Those calls do not establish traversal through live `CEntityAlive::Hit/Die` or automatic native rewards. Effective `game_relations`, creature overrides and global dispatch are required before unifying online/offline awards or deduplicating CtZ casualty history. No gameplay changes are proposed.

FAC-04 closes this bounded native action/rank/reputation pass. Later [supplied Warfare consumers](warfare-relation-consumers.md) and [FAC-06 consolidation/audit](development-reference.md) are complete within scope. Effective diplomacy/true-community policy, installed settings and runtime remain open.
