# Item placement and active-slot transitions

> ADR document set: **v0.1.72**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-02
- Research revision: v0.1.55
- Source status: source-confirmed selected native and actor event paths
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline: ENGINE1011, archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`
- Last reviewed: 2026-10-11

P01–P19 refer to the [placement ledger](../../evidence/inventory/placement-activation-2026-10-11.csv). Unknown upstream commit/executable/profile correspondence remains unknown. [Investigation](../../08-research/investigations/2026-10-11-ITEM-02-placement-activation.md), [Lua contracts](../../02-lua-api/inventory/placement-api.md), [ownership foundation](ownership-lifecycle.md).

## CtZ relevance and boundary

Ownership, placement and activation are distinct. A soldier possessing an item does not by itself establish that the item is selected, shown, usable or selected by NPC combat policy. This pass maps native placement/activation and selected actor event consumers; it does not certify the player-event Lua helpers as a working NPC loadout API. NPC AI selection, effective GAMMA loadout scripts and weapon readiness remain separate dependencies. P01–P05/P07–P09/P16–P18.

## Eligibility is not ownership transfer

| Predicate | Selected checks | Limit |
| --- | --- | --- |
| CanPutInSlot | Slots useful; owner predicate; outfit helmet/backpack availability; non-sentinel empty slot | No universal item BaseSlot equality test in this method; caller must supply valid slot/item |
| Owner predicate | Base owner returns true; stalker rejects outfit/PDA slots | Derived/configured policy can differ; not every NPC owner traced |
| CanPutInBelt | Not already on belt; belt useful; item belt flag; count below BeltWidth | Rectangle free-room check is commented; width can call Lua actor-menu hook |
| CanPutInRuck | Not already in ruck | Not a weight/capacity/ownership verification by itself |

P03/P15/P16. Native Slot/Belt/Ruck declarations default strict_placement to false. Their strict paths bypass the respective CanPut predicate; they do not constitute a general safe bypass API. Selected Slot/Ruck parent checks are additionally conditional on non-single-player. Neither these predicates nor successful local movement establishes server containment transfer. P01/P02/P14.

## Movement and callback ordering

| Operation | Container mutation before owner callback | Placement field at callback | Following work |
| --- | --- | --- | --- |
| Slot | Populate new slot; remove ruck/belt; clear old slot; possibly request activation | Old type/slot | Set slot type/ID, item OnMoveToSlot, processing activation |
| Belt | Clear old slot/request deactivate; insert belt; remove ruck as applicable; recalc/invalidate | New belt type; previous placement passed separately to owner | Item OnMoveToBelt, processing changes |
| Ruck | Clear old slot/request deactivate or remove belt; insert ruck; recalc/invalidate | Old type/slot | Set ruck type, item OnMoveToRuck, processing changes |

P01/P02. These move existing inventory placement rather than inserting a new m_all ownership record. Slot rejects NO_ACTIVE_SLOT/same-item target; normal eligibility prevents occupied destination. Its automatic activation condition depends on current/next slot state, not merely successful placement; bNotActivate suppresses this request and PDA is excluded from that automatic branch. No transaction rollback/reentrant safety contract is established.

Base OnItemSlot/Belt/Ruck emits item-only native callbacks under EXTENDED_ITEM_CALLBACKS. Slot callback runs before owner attachment; ruck callback runs before owner detach; the previous-placement argument is not forwarded to Lua here. Enum names item_to_slot, item_to_belt and item_to_ruck use the same compile guard. The supplied define enables it, but actual binary and effective callback delivery remain unverified. P06/P12/P13.

Consequently an item_to_slot callback can see the destination slot pointer while the item's placement metadata still describes its old location; item_to_ruck has an analogous temporary distinction. Belt metadata is updated earlier. Consumers must use the documented phase, not treat all placement callbacks as equivalent settled snapshots. P01/P02/P06.

## Requested slot versus current slot

ActiveItem resolves the current active slot's item; a requested next slot is separate state. Activate returns immediately off server. It checks blocking unless forced, handles same-current/next requests, checks slot bounds/activation eligibility, and either queues next slot or initiates old HUD item deactivation. A forced/no-current-item branch can activate the target and directly assign current slot. The ordinary no-active-slot path queues a present target; an empty grenade slot has a selected fallback. P04/P14/P19.

Update advances differing current/next state on server. The current-view owner has an additional player-HUD activation gate. An existing non-hidden HUD item postpones the transition; an idle item can receive another deactivate request. After hidden-state and block checks, it invokes next-item ActivateItem, captures previous item/slot, assigns current slot and calls optional _G.CActor_OnChangedSlot(new_slot, new_item, old_slot, old_item). Although actor-named, this call is not explicitly actor-only inside the selected inventory Update branch. The forced direct-current assignment in Activate is not shown emitting that same hook. P04/P05.

The changed-slot hook establishes selected inventory slot assignment, not finished draw animation, ammunition availability or AI readiness. Base item ActivateItem returns false; HUD override calls OnActiveItem and returns true. HUD deactivation sends a hiding state event; moving a HUD item to ruck switches to hidden. Inventory code does not turn these into an observed ready-to-fire completion guarantee. P05/P17/P18.

## Lua requests and actor consumers

make_item_active can send three requests: occupied base-slot item to ruck, target into base slot with do-activate byte, then activate-slot. move_to_slot can evict a current occupant to ruck then send target/slot/doNotActivate; its producer-side CanPutInSlot preflight is commented. Ruck/belt helpers test their predicate before sending one request. No void helper returns success or rolls back earlier requests on later rejection. P07/P10/P11.

Server routes placement events through broadcast, while activate-slot goes to SV_Client. Selected actor consumer validates item presence/non-destruction, applies its mode-dependent alive guard and invokes native placement methods with default non-strict behavior; their bool results are not propagated to the Lua producer. Slot's byte equals 1 to suppress auto-activation. Actor activate-slot calls Activate. P08/P09/P14.

These files establish the selected actor chain. They do not establish effective NPC consumers, universal synchronous event completion, or a weapon-selection guarantee for CtZ soldiers. Existing wrappers' null/type/lifetime assumptions are detailed in [API contracts](../../02-lua-api/inventory/placement-api.md). Ownership must already be established independently. [ITEM-01](ownership-lifecycle.md).

## Scope and next work

ITEM-02 closes this focused placement/requested-current/callback pass. Detailed animations, weapon mechanics, every derived item/AI selection path, blocking/load/recovery policies, installed script overrides and runtime remain outside scope. Next: item consumption/destruction and inventory-owner cleanup, then item persistence/reconstruction and consolidation. [Roadmap](../../ROADMAP.md).

Current completion: the selected ITEM-01–04 foundations and [ITEM-05 consolidation/audit](development-reference.md) are complete within available-source scope. Earlier next-step text above records the individual increment; use [completion status](source-completion-status.md) and the [current roadmap](../../ROADMAP.md) for the active backlog.
