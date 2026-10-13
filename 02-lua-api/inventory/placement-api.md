# Placement and active-item Lua contracts

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-02-API
- Subsystem: inventory
- C++ owner / Lua owner: CScriptGameObject / game_object
- Interface kind: registered native event-request helpers
- Baseline: ENGINE1011; [manifest](../../evidence/manifest.md)
- Source status: source-confirmed selected signatures/registrations/bodies
- Runtime status: untested; deferred
- Build scope: selected registrations; placement enums conditional on EXTENDED_ITEM_CALLBACKS
- Native/Lua inheritance: dynamic inventory-owner/item casts impose receiver requirements; no exhaustive hierarchy/converter certification
- Converter policy: CScriptGameObject pointer, u16 and bool through existing bindings; nil/dangling/overflow behavior not certified
- Example status: none
- Last reviewed: 2026-10-11

P-IDs refer to [ITEM-02 ledger](../../evidence/inventory/placement-activation-2026-10-11.csv); read with [phase reference](../../04-game-systems/inventory/placement-activation.md).

| Lua method | Exact native signature excluding receiver | Behavior/limits |
| --- | --- | --- |
| make_item_active(item) | void MakeItemActive(CScriptGameObject* pItem) | Casts/dereferences owner and item without explicit null/type failure branch in this body; derives BaseSlot; requests occupant ruck, target slot, activation. SAFE_WRAP registration does not establish transaction/success |
| move_to_ruck(item) | void MoveItemToRuck(CScriptGameObject* pItem) | Dereferences pItem then casts; failed owner logs/returns; predicate check then request. No explicit item-null/type guard before later use |
| move_to_slot(item, slot_id, doNotActivate) | void MoveItemToSlot(CScriptGameObject* pItem, u16 slot_id, bool doNotActivate) | Owner failure logs; slot preflight commented; occupant ruck then slot request, byte 1 suppresses auto activation. Third argument has no default in declaration/binding |
| move_to_belt(item) | void MoveItemToBelt(CScriptGameObject* pItem) | Failed owner logs; predicate check then request. Item/receiver/lifetime must satisfy native assumptions |

P07/P10/P11. These operations target already owned live inventory items; helpers do not certify that condition or complete NPC event delivery. Return is void, not a success boolean. SafeWrap behavior remains documented in [ownership APIs](ownership-api.md); do not infer memory ownership transfer, nil safety or atomicity from its name.

| Native operation | Return/defaults | Distinction |
| --- | --- | --- |
| Slot(u16 slot_id, PIItem item, bool bNotActivate=false, bool strict_placement=false) | bool | Normal eligibility versus strict path; placement before/after callback distinction |
| Belt(PIItem item, bool strict_placement=false) | bool | Belt type set before owner callback |
| Ruck(PIItem item, bool strict_placement=false) | bool | Owner callback before ruck type assignment |
| ActiveItem() const | PIItem | Current-slot lookup; not next/requested slot or readiness |

P01–P05/P14. These native defaults are not optional argument promises for the separate Lua wrappers.

Native enum callbacks item_to_slot/belt/ruck pass item only from selected base owner, despite native owner methods having previous_place. Enum/producer guard is EXTENDED_ITEM_CALLBACKS; snapshot enables it. Their different metadata/attachment phases are in the reference. P06/P12/P13.

Optional named _G.CActor_OnChangedSlot(new_slot, new_item_or_null, previous_slot, previous_item_or_null) is a looked-up functor in selected Update, not the same enum callback or guaranteed shared dispatcher. It follows current-slot assignment; direct forced Activate assignment can bypass this site. Null object arguments and installed function contract require effective sources. P04/P05.

Dependencies/lifetime: live wrappers and valid owner/item/slot, established containment, event transport/actor or effective NPC consumer, HUD/state/activation gates. No persistence or C++ memory ownership transfer is established here. Checks: declarations/registrations/payload-consumer comparison and evidence/hash/range validation; [verification](../../08-research/verification-2026-10-11-v0.1.55.md). Weapon AI/readiness, exhaustive converters/reentrancy, effective callback overrides and runtime remain open.
