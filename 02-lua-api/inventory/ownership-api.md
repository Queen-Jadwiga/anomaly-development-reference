# Inventory ownership Lua contracts

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-01-API
- Subsystem: inventory
- C++ owner: CScriptGameObject; Lua owner: game_object
- Interface kind: Lua exports over native helpers/events
- Baseline: ENGINE1011; [manifest](../../evidence/manifest.md)
- Source status: source-confirmed selected registrations/bodies
- Runtime status: untested; deferred
- Build scope: inspected registrations; no installed binary equivalence asserted
- Native versus Lua inheritance: wrappers accept game-object instances; dynamic casts in individual methods impose narrower receiver/item requirements; this is not an exhaustive class hierarchy catalog
- Converter policy: existing CScriptGameObject pointer and Fvector/functor conversions; exhaustive nil/dangling-pointer conversion audit not performed
- Example status: none
- Last reviewed: 2026-10-11

Evidence I14–I20 in [ledger](../../evidence/inventory/ownership-lifecycle-2026-10-11.csv). See [phase reference](../../04-game-systems/inventory/ownership-lifecycle.md) for callback observation limits.

| Lua method | Exact native signature excluding receiver | Return / guard / mutation |
| --- | --- | --- |
| drop_item(item) | void DropItem(CScriptGameObject* pItem) | Casts receiver to inventory owner and item to inventory item; logs/returns on failed casts. Dereferences pItem before an explicit null check; do not infer nil safety. Sends ownership rejection; no completion result |
| drop_item_and_teleport(item, position) | void DropItemAndTeleport(CScriptGameObject* pItem, Fvector position) | Calls DropItem then independently sends change-position. A logged failed drop does not gate the second event; no atomic drop/move guarantee |
| transfer_item(item, target) | void TransferItem(CScriptGameObject* pItem, CScriptGameObject* pForWho) | Explicit null arguments and non-item check log/return; emits sell then buy. No explicit source ownership/destination inventory cast in this body; event consumers determine acceptance |
| take_item(item) | void TakeItem(CScriptGameObject* pItem) | Null/non-item log/return. Recognized inventory-owner/box parent: sell/buy; unknown parent: log/return; no parent: SendPickUpEvent |
| inventory_for_each(fn) | void ForEachInventoryItems(const luabind::functor<bool>& functor) | Requires inventory-owner receiver; builds available-item list; calls fn(item, owner); true stops iteration, false continues |

I14–I18. No optional arguments or success booleans are established for these void methods. Registration uses SAFE_WRAP for take/transfer, direct methods for drop/drop-and-teleport/enumeration. The inspected SAFE_WRAP execute path conditionally logs/calls a debug warning for receiver validity then still forwards to the method; it is not a rejection/rollback/success contract. Detailed luabind errors/argument converter lifetime remain outside this selected pass. I16/I17.

| Exported native callback enum | Selected producer | Phase |
| --- | --- | --- |
| on_item_take | Base CInventoryOwner::OnItemTake(item) | Callback before attachment/remembered-slot work; Take recalculates weight afterward |
| on_item_drop | Base CInventoryOwner::OnItemDrop(item, flag) | Callback receives item, not flag; after inventory removal but before parent detach in selected actor DropItem chain |
| take_item_from_box | Box removal branch -> Actor callback(box, item) | Only while box in use; after box parent detach, before any separately requested destination completion is proven |

I01/I02/I04–I06/I13/I20. These are native object callback enums, not automatically equivalent to shared axr_main callback names or effective addon delivery. Parent/item/owner wrappers remain lifetime-bound live objects; these methods do not transfer C++ memory ownership or certify persistence. Enumeration list filtering is documented at I19; not every m_all entry is returned.

Checks: registration/declaration/body alignment, ledger hashes/ranges/symbols and selected caller/consumer ordering; [verification](../../08-research/verification-2026-10-11-v0.1.54.md). Dependencies: valid live entities, event transport/server/client processing and effective receiver types. Installed dispatcher, NPC variants, transactional/reentrant behavior and runtime remain unverified.
