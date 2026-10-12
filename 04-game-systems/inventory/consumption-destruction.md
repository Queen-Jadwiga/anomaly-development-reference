# Item consumption, destruction and owner cleanup

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-03
- Research revision: v0.1.56
- Source status: source-confirmed selected native/actor/eatable paths
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline: ENGINE1011, archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`
- Last reviewed: 2026-10-11

D01–D18 refer to the [ledger](../../evidence/inventory/consumption-destruction-2026-10-11.csv). Unknown upstream commit, executable/profile and winning scripts remain unknown. [Investigation](../../08-research/investigations/2026-10-11-ITEM-03-consumption-destruction.md), [Lua contracts](../../02-lua-api/inventory/consumption-api.md). Read with [ownership](ownership-lifecycle.md) and [placement](placement-activation.md).

## Consume effects and remove objects are separate

ClientEat validates eatable type, living-entity/inventory-owner receiver, matching inventory and live parent ID, then sends an eat event and returns true. That is request success, not completed consumption. Selected actor event processing validates live item/non-destruction and mode-specific alive state, and calls Eat only when the named _G.CInventory__eat functor exists and returns true for the item. There is no unconditional fallback Eat in that selected branch. D01/D05.

Native Eat independently checks eatable/entity/owner/inventory consistency and compares the parent ID, then calls UseBy. Eat and ClientEat dereference H_Parent for that ID comparison without an explicit null guard; a valid live parent is a required invariant, not a null-safe rejection contract. The selected UseBy applies medicine influence and configured boosters, sends the mode-dependent booster event, adjusts uses and condition, then returns true. It has no early Empty rejection in this body. Full condition/booster internals and effective script use policy are outside scope. D01–D03.

For the actor's inventory in single-player, Eat then emits native use_object(item). UI selection/refresh follows. Only afterward does it test Empty: an empty non-deletable item returns false; an empty deletable item gets manual-drop marked. Thus **false can follow applied effects and the callback**, and true does not mean object destruction has completed. Retrying merely because Eat returned false is not established safe behavior. The native in-Eat named gate block is commented; the active actor event gate is a separate path. D01/D05/D18.

## Uses, configuration and exhausted-item removal

Load reads max_uses as u8 (default 1), remove_after_use (default true) and empty_weight. Empty means exactly remaining uses == 0; CanDelete tests the removal flag == 1. UseBy clamps zero rather than returning before effects. The comment intends 255 infinite uses, but the literal test is a u8 field compared with integer -1; under ordinary C++ integer promotion 255 differs from -1 and the positive count is decremented. This source interpretation is not a runtime diagnosis or a tested infinite-use contract. D02/D03.

UpdateDropTasks visits slot, belt and ruck entries. For manual-drop items it clears the flag and denies trade; on server it sends ownership rejection addressed to the live parent. It does not immediately erase inventory membership. A later drop-update notification is separately gated by m_drop_last_frame. D04.

During eatable detachment, a non-useful item is hidden/disabled and its physical item marked ready to destroy before inherited independent handling. After becoming independent, a non-useful item requests DestroyObject only when local and on server. Useful rejects exhausted removable items but also delegates to base Useful. This is the selected exhausted-eatable removal path; it is not every item subclass's destruction policy. D02; ITEM-01 documents actual DropItem/parent hook phases.

## Destruction request, server removal and client teardown

| Stage | Selected source action | Limit |
| --- | --- | --- |
| DestroyObject request | Sets m_bObjectRemoved once; returns if already destroy-marked; only Local sends GE_DESTROY | No immediate memory free or universal remote send |
| Server destroy | Resolves entity, asserts sender owns it, recursively processes children | Not a rollback-safe transaction under malformed relationships |
| Attached entity | Server reject updates containment; pack appends pre-destroy reject before destroy | Successful rejection is required for this selected cleanup branch |
| Server final removal | Optional A-Life release(false), game OnDestroyObject, entity_Destroy | Separate from client inventory/drop callback completion |
| Live GE_DESTROY consumer | Parented object logs and breaks; independent object setDestroy(true) | Parent cleanup is a prerequisite in this selected consumer |
| Live destruction queue | Reference-release notifications, then net_Destroy and Destroy | Not synchronous completion at request time |

D06–D09. Server child recursion uses a shared event pack; this preserves selected reject/destroy ordering, not a multi-object atomicity promise. Read with [native release lifecycle](../alife/lifecycle-state-reference.md) for broader registry boundaries.

CGameObject net_Destroy calls optional _G.CGameObject_NetDestroy early, then tears down selected native resources, unregisters the live object, updates current-entity state and removes correction-prediction tracking. Binder net_Destroy follows; the Lua game-object wrapper is deleted afterward. Early native hook, binder hook and memory release are different observation phases. Derived teardown ordering and effective Lua cleanup remain qualified. D06/D09.

## Owner cleanup is not one universal sweep

InventoryOwner net_Destroy invokes attachment-owner teardown, Clear, then resets active slot. Clear empties m_all/ruck/belt and slot pointers, clears inventory owner and recalculates/invalidates. This body does not call per-item DropItem, send destroy requests, clear each item's m_pInventory or emit each item drop callback. Item net_Destroy separately verifies it is absent from m_all when its inventory pointer exists; the pointer-clear line is commented. These are invariants at different stages, not proof every derived owner/drop script is safe. D10–D12.

sell_useless_items is a selective helper: it skips bolts, weapons with nonzero CurrSlot and original-owner PDA; other entries have manual-drop disabled and DestroyObject requested. Its name is not proof of a priced sale/payment transaction. Broader death loot and NPC policy remain effective-source dependencies. D11.

## Lua and CtZ boundaries

game_object:eat(item) calls native inventory Eat directly after explicit argument/item/owner checks and discards its bool result. It does not call ClientEat or the actor event gate. destroy_object() forwards the destruction request, returning no completion result. Eatable class use/removal getters/setters expose state, not a safe consumption transaction. [API contracts](../../02-lua-api/inventory/consumption-api.md). D13–D17.

For CtZ logistics or soldier equipment, distinguish abstract campaign balances from actual item effects/counts/removal; establish the effective NPC policy before assuming actor consumption/UI behavior applies. This pass supplies source boundaries rather than a working NPC consumable recipe. Full weapon/ammunition/artefact use, death-drop strategy, decoder/schema and runtime remain outside scope.

Next: item persistence and reconstruction, followed by inventory consolidation and bounded audit. [Roadmap](../../ROADMAP.md).

Current completion: the selected ITEM-01–04 foundations and [ITEM-05 consolidation/audit](development-reference.md) are complete within available-source scope. Earlier next-step text above records the individual increment; use [completion status](source-completion-status.md) and the [current roadmap](../../ROADMAP.md) for the active backlog.
