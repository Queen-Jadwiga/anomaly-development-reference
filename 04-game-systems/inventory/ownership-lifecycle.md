# Inventory ownership, containment and pickup/drop

> ADR document set: **v0.1.74**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-01
- Research revision: v0.1.54
- Source status: source-confirmed selected native/server/actor/box paths
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline: ENGINE1011, archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`
- Last reviewed: 2026-10-11

I01–I20 refer to the [ownership ledger](../../evidence/inventory/ownership-lifecycle-2026-10-11.csv). Unknown upstream commit, executable correspondence and effective installed scripts remain unknown. [Investigation](../../08-research/investigations/2026-10-11-ITEM-01-ownership-lifecycle.md), [Lua contracts](../../02-lua-api/inventory/ownership-api.md).

## Three related representations

| Representation | Owner/fields | Meaning and limit |
| --- | --- | --- |
| Server containment | CSE_Abstract ID_Parent and parent's children IDs | Server attachment relation; no client inventory pointer implied by this field alone |
| Live-object parenting | CObject Parent via H_SetParent | Runtime parent/hooks/spatial membership; does not itself insert into CInventory m_all |
| Owner inventory | CInventory m_all, ruck/belt/slot containers; item m_pInventory and current place | Selected inventory membership and placement, maintained separately from server IDs |
| Inventory box | CInventoryBox m_items IDs and child parenting | Separate box path; not a CInventory owner membership insertion in this handler |

I01/I02/I07–I13. Here ownership describes gameplay containment, not Lua garbage-collection adoption or transfer of C++ memory ownership. A parent pointer/ID alone is insufficient evidence that every representation has completed its update.

## Server attach and detach

Server Process_event first invokes the destination server entity's OnEvent when present, then routes trade-buy/ownership-take to Process_event_ownership and trade-sell/ownership-reject to Process_event_reject. I07.

Take resolves parent/item and requires server-client object validity, an independent item (ID_Parent 0xffff), and a trusted sender (server client or new owner's client). A dead-creature restriction in this body excludes single-player. Accepted game OnTouch is followed by owner-client migration if needed, ID_Parent assignment, child ID insertion and broadcast. Single-player OnTouch conditionally calls the A-Life graph attach helper when relevant objects/registry conditions hold, but returns TRUE even without that call. Do not infer full graph helper effects from the caller alone. I08/I10.

Reject requires both entities, child membership and a non-independent item. A mismatching ID_Parent logs an error but does not return at that branch. It calls game OnDetach before setting ID_Parent to 0xffff and erasing the child; optional broadcast follows. The selected single-player OnDetach conditionally calls graph detach. A missing child causes false return, not an idempotent successful detach. No equivalent sender-authorization gate is present in this selected reject body; broader transport/security policy is outside scope. I09/I10.

## Actor take: parenting before inventory insertion

The selected actor event handler resolves the live item, checks CanTakeItem, sets the live parent to the actor, calls inventory.Take with strict placement, then SelectBestWeapon. Failed take in single-player sends a reject event. This consumer is actor-specific; NPC overrides remain a later source pass. I05.

CanTakeItem rejects destroying items and items whose CanTake is false, verifies absence of a duplicate ID, and applies excess-weight rejection to non-actor owners. The actor bypass in this method is not proof of unrestricted pickup across every UI/script/gameplay path. I03.

Take asserts the item is valid, not already assigned an inventory and eligible; then assigns m_pInventory, clears manual-drop state, allows trade, removes correction-prediction tracking and inserts into m_all. It tries retained placement or chooses slot/belt/ruck, calls owner OnItemTake, then recalculates total weight, invalidates inventory state, deactivates item processing and notifies selected UI views. Detailed placement/activation guards are deferred to ITEM-02. I01.

Base OnItemTake emits the native on_item_take callback with the item, then performs owner attachment and possible remembered-slot activation. Actor override invokes the base first. Thus in this actor path the callback observes assigned live parent and inventory membership/placement, but occurs before the Take function's weight recomputation and later UI work. It is not a universal completed-operation notification for every derived owner. I01/I04/I05/I06/I20.

## Actor drop: callback before live detachment

Actor reject/sell reads the optional pre-destroy byte, suppresses shell creation for sale/pre-destroy, verifies parent ownership and calls DropItem for a non-destroying object. Successful drop adds a temporary pickup denial; a remaining position payload can move the item. I05.

DropItem asserts valid membership/place, updates processing/active slot handling, removes the placement entry and m_all entry, and clears m_pInventory. It then calls owner OnItemDrop, recalculates weight, invalidates state, marks a later drop update and performs selected UI/weapon launch handling. Only near the end does it call H_SetParent(nullptr, dont_create_shell) and return true. Base OnItemDrop invokes the item callback before owner attachment detach; actor override then performs selected outfit/weapon/grenade handling. I02/I04/I06.

**Callback phase:** in this path on_item_drop runs after inventory membership removal but before live parent detachment; the old placement can still be visible, while the cached total weight has not yet been recomputed. Do not treat it as proof the item is already an independent world object or safe to re-transfer synchronously. Reentrant mutation safety is not established by this pass. I02/I04/I06/I11/I12.

H_SetParent rejects direct non-null parent replacement through VERIFY, calls before-child/independent hook, updates spatial registration, assigns Parent and calls the after hook. Independent item hooks reset placement to undefined; the after-independent hook also records server time. net_Destroy checks that an inventory-associated item is already absent from m_all; its pointer-clear line is commented, not a general cleanup sweep. Full destruction/release/owner teardown will be investigated separately. I11/I12.

## Boxes and transfers

Box take adds an ID, parents the object, hides/disables it and conditionally notifies the search UI. Box reject removes the ID and clears parent with sale/pre-destroy shell policy; when the box is in use it emits Actor's take_item_from_box callback with box and item. That callback is tied to the box removal branch and in-use flag, not proof that a destination inventory has received the item. I13/I20.

Lua transfer_item sends sell from the receiver then buy to the target; take_item transfers via sell/buy for recognized live inventory-owner/box parents, otherwise sends a pickup request for an independent item. Drop sends rejection; drop_item_and_teleport additionally sends a separate position-change event. These are request sequences, not an atomic transaction or completion-return API. Event names GE_TRADE_* here do not by themselves establish pricing/payment. I14/I15/I16; [focused contracts](../../02-lua-api/inventory/ownership-api.md).

inventory_for_each builds an AddAvailableItems list and invokes the callback with item/owner until true. It is not a raw m_all enumeration: usefulness flags and persistent-slot exclusions affect the available list even without trade filtering. Copying the list snapshots membership pointers, not item lifetime or safe mutation during enumeration. I18/I19.

## Scope and next steps

ITEM-01 closes selected server/actor/box ownership and focused request/observer contracts. It does not close NPC consumers, placement/activation details, item use/consumption/destruction, item serialization/reconstruction, price/payment, effective GAMMA scripts, full graph attach/detach internals or runtime. Existing [A-Life lifecycle](../alife/lifecycle-state-reference.md) and [persistence pipeline](../persistence/native-save-load-pipeline.md) provide surrounding context without proving every item-specific edge.

Next ITEM-02: slot/belt/ruck movement, eligibility, active-item transitions and callback ordering; then consumption/destruction and persistence, followed by bounded consolidation. [Roadmap](../../ROADMAP.md).

Current completion: the selected ITEM-01–04 foundations and [ITEM-05 consolidation/audit](development-reference.md) are complete within available-source scope. Earlier next-step text above records the individual increment; use [completion status](source-completion-status.md) and the [current roadmap](../../ROADMAP.md) for the active backlog.
