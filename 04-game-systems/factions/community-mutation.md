# Character-community mutation and team/group effects

> ADR document set: **v0.1.53**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-03
- Source status: source-confirmed within selected native setters, registrations and packet consumers
- Runtime status: untested; deferred until explicitly resumed by the user
- Last reviewed: 2026-10-11

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee` pins this source. Upstream commit, executable/build and installed script/configuration correspondence remain unknown. M01–M19 refer to the [community-mutation ledger](../../evidence/factions/community-mutation-2026-10-11.csv), with file/line/symbol/hash pins. Read with [identity and relation queries](native-relations.md), [persistence/reset](relation-persistence.md), and [focused setter contracts](../../02-lua-api/factions/community-mutation-api.md).

## Distinct identities and memberships

| State | Native owner | Selected mutation/transfer path |
| --- | --- | --- |
| Live character community | Inventory owner's `CCharacterInfo::m_CurrentCommunity` | `SetCommunity` changes index and resets sympathy from the configured table |
| Server character community | `CSE_ALifeTraderAbstract::m_community_index` | Inventory-owner bridge writes the server field directly after live mutation |
| Live team/squad/group tuple | `CEntity::id_Team/id_Squad/id_Group` | `ChangeTeam` migrates membership through the level seniority hierarchy |
| Server creature tuple | `s_team/s_squad/s_group` | Selected update-packet consumer imports the live tuple; state/update serializers retain it |
| A-Life squad membership | Native online/offline group membership and script squad/board state | Separate mechanism; changing the live tuple does not establish strategic reassignment |

M02–M06/M11/M18/M19; the last row uses the [A-Life lifecycle reference](../alife/lifecycle-state-reference.md) and its squad evidence. A live hierarchy `group` number is not `CSE_ALifeMonsterAbstract::m_group_id`, a smart assignment ID or a faction name. No CtZ/Warfare owner transfer follows from these setters alone.

## The Lua community setter has two stages

`game_object:set_character_community(comm,squad,group)` validates inventory-owner and entity receiver casts, resolves the configured community ID, calls `CInventoryOwner::SetCommunity(index)`, then calls `entity->ChangeTeam(community.team(),squad,group)`. It returns void. M01/M09/M16.

Inside the inventory-owner stage, source order is:

1. Cast to `CEntityAlive` and assert it; obtain the matching server object through A-Life lookup. If no object is returned, return.
2. Change live character community; `CCharacterInfo::SetCommunity` also recomputes sympathy from that community's table.
3. If alive, call virtual `ChangeTeam(new team,current squad,current group)`.
4. Cast server object to trader; if unavailable, return after the earlier live changes.
5. Write server `m_community_index`; for the actor, invoke `RPC_UpdateFaction`.

M02 `432–453`; M03 `190–194`; M14. The outer Lua wrapper then requests the caller-supplied squad/group tuple even if the inner void bridge returned early. This is not an atomic transaction or a boolean success contract.

**Two-stage consequence:** when both the configured team and supplied squad/group differ, the selected live path can migrate first to the new team with old squad/group, then migrate again to the requested tuple. Each actual tuple change runs the native hooks; either call can be a no-op when all three values already match. This follows source order, not a runtime observation. M01/M02/M04.

A missing/non-trader server object, invalid community, an unsupported receiver or unmet live-membership conditions does not produce a reliable rollback guarantee. Community lookup has assertion paths before the wrapper's negative-index fallback; arbitrary community strings are not proven safe. M01/M02/M15. The live hierarchy's non-no-op `ChangeTeam` asserts alive status and, in single-player, existing registered membership. Do not use this as a general corpse/offline-entity mutation recipe. M04.

## What the hierarchy migration does

For a changed tuple, `CEntity::ChangeTeam` calls the before hook, unregisters from the old level `team → squad → group`, writes the three fields, registers in the new group, then calls the after hook. Base hooks are empty. M04 `378–407`.

The group helper removes/adds the member vector, processes leader bookkeeping under its compile guard, removes/adds agent-manager membership, and detaches/reattaches shared visual/sound/hit memory pointers for custom monsters. Empty groups release shared memory collections; an empty agent-member registry releases its agent manager. New stalker groups can create a manager and bind the shared collections. These are concrete local AI effects, not a promise that all enemy selection or strategic behavior has completed. M05.

Stalker before/after hooks preserve whether it was registered in combat: before records that flag; after re-registers in combat when needed. Base monsters have an additional `monster_squad` removal/registration around inherited team migration and rebind grouping behavior when present. Different native types therefore have different virtual side effects. M06 `1506–1517`; M07.

`game_object:change_team(team,squad,group)` is a separate custom-monster wrapper. Its selected body does not call character-community mutation or write trader community identity. Treating team number as faction identity would conflate these interfaces. M08/M10; [API contracts](../../02-lua-api/factions/community-mutation-api.md).

## Client/server synchronization and later reconstruction

The inventory-owner community bridge writes server trader identity synchronously in this inspected call chain. It does not directly write server creature `s_team/s_squad/s_group`. The selected stalker/custom-monster export writes current live tuple bytes; server `Process_update` dispatches `UPDATE_Read`, which imports the creature tuple. This is a separate packet-receipt boundary, not an atomic part of the community setter. M02/M06/M11/M17/M19.

Server trader state writes the community index under `XRGAME_EXPORTS`; reader has legacy-version gates. Creature state and update packets carry their own tuple. The native object-save path preserves server spawn/update data as traced in ALIFE-04; no claim is made that a save immediately after a Lua setter has already received the final tuple packet. M11; [ALIFE-04](../../08-research/investigations/2026-10-11-ALIFE-04-save-load-identity.md), [ALIFE-07](../../08-research/investigations/2026-10-11-ALIFE-07-client-server-offline-teardown.md).

At live reconstruction, inventory-owner spawn initializes character info from server trader data; `CCharacterInfo::Init` applies server community before profile/specific-character initialization. Specific-character community fallback applies only when the current community is invalid. Entity spawn separately takes server creature tuple, with a selected monster-species team override when the configured monster team is not 255. Those reconstruction mechanisms are distinct; no universal automatic repair of mismatched community/team fields is established. M02 `124–135`; M03 `79–82,153–161`; M04 `199–224`.

Remote tuple import in the selected client bodies assigns fields directly, rather than invoking the same migration hooks shown above. This comparison is scoped to those packet bodies, not a multiplayer correctness diagnosis or all replicated state. M06/M19.

## Actor display and strategic boundaries

The actor's `RPC_UpdateFaction` here updates `discord_gameinfo` using `_g.get_actor_true_community` and translated faction display text. Despite its name, this selected body is not a community network mutation or proof that the PDA/CtZ ownership UI has refreshed. The effective script producer can report a different actor identity model; its installed implementation remains open. M13.

The inspected setter chain does not clear personal/community goodwill, change the faction matrix, transfer A-Life squad membership, assign a smart, rewrite Warfare squad faction policy or move CtZ campaign ownership. It changes inputs to later relation calculations and local hierarchy/agent state. These are bounded call-chain findings; installed wrappers may add policy. M01–M08 and FAC-01/02; [Warfare integration boundary](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md).

## Development use and disposition

When designing a later faction-changing feature, specify whether it changes character community, a live hierarchy tuple, server identity, strategic squad membership or campaign ownership. Identify effective policy for each additional layer and its observation phase. Reacquire objects across online/offline lifetime boundaries; do not treat these client methods as offline server APIs. No gameplay implementation or runtime-tested conversion recipe is provided.

FAC-03 closes this selected native mutation chain. Full effective faction switching, disguise/true-community policy, strategic reassignment and update/save timing remain open. Later [action-driven goodwill/rank/reputation](action-goodwill.md) and [FAC-06 consolidation](development-reference.md) are complete within scope; [effective integration](source-completion-status.md) remains open.
