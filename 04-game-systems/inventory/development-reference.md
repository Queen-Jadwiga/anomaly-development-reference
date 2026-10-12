# Inventory and item lifecycle development reference

> ADR document set: **v0.1.78**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-05
- Subsystem: inventory/item lifecycle
- Research revision: v0.1.58
- Source status: source-confirmed selected contracts; scoped-source-audit consolidation
- Runtime status: untested; deferred until explicitly resumed
- Baseline: ENGINE1011; [source record](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

Available-source first-edition work is complete within the selected ITEM-01–04 boundaries. Effective installed inventory integration remains partial under the [completion rule](source-completion-status.md). This is practical guidance for those contracts, not a certified NPC loadout recipe. Archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit, executable/build/profile correspondence and winning scripts remain unknown.

Evidence IDs below are ledger-local: [ownership I01–I20](../../evidence/inventory/ownership-lifecycle-2026-10-11.csv), [placement P01–P19](../../evidence/inventory/placement-activation-2026-10-11.csv), [consumption D01–D18](../../evidence/inventory/consumption-destruction-2026-10-11.csv), [persistence R01–R15](../../evidence/inventory/persistence-reconstruction-2026-10-11.csv). Each ledger pins paths, symbols, ranges and full-file hashes. [Audit/investigation](../../08-research/investigations/2026-10-11-ITEM-05-inventory-consolidation.md).

## Choose the state you actually need

| Question | Relevant state or operation | What the result does not establish |
| --- | --- | --- |
| Is the item contained by this server entity? | ID_Parent and parent children IDs | Live parent, inventory membership or equipped state |
| Does this live owner possess the item? | H_Parent plus CInventory membership/item pointer | Saved identity, price/payment or active readiness |
| Where is an owned item placed? | Slot/belt/ruck containers and placement metadata | Requested/current active slot or settled callback snapshot |
| Which item is selected? | Current ActiveItem/active slot; next slot tracked separately | Finished animation, AI selection or ability to fire |
| Has consumption occurred? | UseBy/Eat effects and use count in the traced chain | Completed drop/destroy or a safe retry on false |
| Has removal completed? | Server containment/removal and live destruction stages | Synchronous completion at destroy_object request |
| What survives save/load? | Explicit server fields, retained client bytes and addon storage | Arbitrary Lua tables or final live equipment after binder load |

I01–I13/P01–P05/D01–D12/R01–R14. Inference for mod design: track these phases separately rather than treating one parent ID, request return or callback as a universal completion signal. Live wrappers remain lifetime-bound; containment is distinct from C++/Lua memory ownership.

## Transfer and inventory observation

For selected actor acquisition, eligibility precedes live parenting and Take. Take assigns inventory pointer and m_all membership, establishes placement, invokes owner OnItemTake, then recomputes weight/state and performs later UI work. For drop, membership/pointer are removed before OnItemDrop, while parent detachment follows later. Server attach/detach are separate event consumers with their own guards and graph caller boundaries. Box containment uses its own ID vector and parent handling. I01–I13; [ownership reference](ownership-lifecycle.md).

Lua take_item/transfer_item/drop_item/drop_item_and_teleport are requests, not completion-return transactions. Transfer emits sell then buy; teleport follows a separately requested drop. Failed earlier work does not imply rollback or cancellation of subsequent requests. GE_TRADE event names do not prove payment. Follow the [exact wrapper contracts](../../02-lua-api/inventory/ownership-api.md) for receiver/null/type assumptions. I14–I17.

inventory_for_each snapshots AddAvailableItems, whose belt/slot usefulness flags and persistent-slot filtering make it different from m_all enumeration. The callback receives item/owner and true stops it. Copying pointer membership does not retain object lifetime or establish mutation-safe iteration. I18/I19.

## Placement and selection

Ordinary Slot/Belt/Ruck paths use their respective eligibility predicates; strict paths bypass those predicates. The selected actor Take uses strict placement, retaining loaded placement metadata when possible. Do not describe that restoration as ordinary eligibility validation or use strict mode as a general safe bypass. Slot rejects the sentinel/same-item target before its ordinary predicate, and current configuration/derived assumptions remain important. P01–P03/P14/R12/R13.

Lua move_to_slot/make_item_active can send occupant-to-ruck, target-to-slot and activation requests. No void return certifies success; producer-side slot preflight is commented. The selected actor consumer uses native defaults for placement; NPC event delivery/selection is still open. P07–P11; [placement APIs](../../02-lua-api/inventory/placement-api.md).

Activate operates on server and may request next slot or directly change current slot in selected forced/no-current-item paths. Update has hidden-item, blocking and current-view HUD gates before current-slot assignment. The named changed-slot hook follows that assignment in Update; direct assignment in Activate is a distinct path. No path here proves readiness to fire. P04/P05/P17–P19; [placement reference](placement-activation.md).

## Callback observation boundaries

| Observation point | Established in selected producer chain | Still pending or qualified | Evidence |
| --- | --- | --- | --- |
| on_item_take | Live parent, m_all membership and placement in actor Take | Owner attachment/remembered activation, final weight/state/UI work | I01/I04–I06; R14 |
| on_item_drop | Membership removed and m_pInventory cleared | Parent detach, placement reset, final weight/UI work | I02/I04/I06/I11/I12 |
| item_to_slot | Destination slot pointer/container changes | Placement metadata assignment and owner attachment | P01/P06 |
| item_to_belt | Belt container and belt metadata | Later item hook/processing work | P02/P06 |
| item_to_ruck | Ruck container and weight/state recomputation | Ruck metadata assignment and owner detach | P02/P06 |
| take_item_from_box | Selected in-use box removal and parent detach | Destination acquisition | I13/I20 |
| use_object | Selected actor UseBy effects occurred | Empty/removal policy and deferred drop/destroy | D01/D05/D18 |
| CActor_OnChangedSlot | Current slot assigned in selected Update path | Derived animation/weapon readiness; not every activation path emits it | P04/P05 |
| Client spawn-manager callback | Selected live net_Spawn succeeded | Subsequent parent ownership-take event | R11 |
| Binder load | Native virtual load precedes binder load | Later derived spawn writes and live ownership restoration | R07–R10 |

These native enums/named functors are not automatically the installed shared callback dispatcher. Placement enums/producers use EXTENDED_ITEM_CALLBACKS. No universal callback-complete barrier or safe synchronous reentrant transfer is established. I20/P06/P12/P13; [source completion](source-completion-status.md).

## Consumption, removal and cleanup

ClientEat validates selected type/inventory/parent assumptions, sends an eat event and returns request success. Selected actor event processing requires the named CInventory__eat gate to exist and approve. game_object:eat calls native Eat directly, discards its bool and bypasses that event gate. Native Eat/ClientEat dereference H_Parent for the ID check without an explicit null guard; inventory consistency is an invariant required by these bodies. D01/D05/D13–D15; [consumption APIs](../../02-lua-api/inventory/consumption-api.md).

UseBy applies effects before Eat's empty test. Empty non-removable items can produce false after effects/callback; automatic retry based on false is not established safe. u8 uses, the literal comparison with -1 versus the infinite-use comment, and condition initialization remain documented source caveats rather than runtime findings. D01–D03; [consumption reference](consumption-destruction.md).

Manual-drop marking is processed later. The selected exhausted-eatable detach path can hide/disable and request destruction. DestroyObject requests differ from server recursive child removal, reject-before-destroy packing, the live GE_DESTROY consumer and queued reference release/teardown. Parent cleanup is required by the selected live destroy consumer; malformed relationships or failed reject do not have a demonstrated robust recovery contract. D04/D06–D09.

Owner Clear resets containers/pointers/owner state; it does not perform a per-item DropItem/destroy/callback sweep. Item net_Destroy separately asserts absence from m_all if its inventory pointer still exists. Teardown convergence for all derived owners/effective scripts remains open. sell_useless_items is selective destruction, with no demonstrated priced sale in that body. D10–D12.

## Persistence and reconstruction

Server spawn packets retain IDs/parent/custom bytes and class STATE; object registry save recursively visits qualifying children. Base item STATE includes condition/upgrades; selected derived weapon/ammo state differs. Base client net_Export returns a zero physical marker in single-player or when parented, so it is not proof of fresh generic server state. R01–R04/R06/R15; [persistence reference](persistence-reconstruction.md).

Client native save/load retains placement/condition and conditional independent physics; eatable appends remaining uses; owner retains a pending active slot. Native virtual load precedes binder load inside base spawn. Later inventory-item spawn copies server condition/installs upgrades, and eatable spawn can initialize condition again. Saved fields are not a complete final-state snapshot. R05–R10/R14.

Selected live spawn dispatches parent take after its spawn-manager callback. Actor take establishes membership/strict placement; owner OnItemTake emits the callback before matching saved-slot Activate. Further actor/derived selection policy and readiness gates remain separate. R11–R14. Use the [general persistence reference](../persistence/development-reference.md) and [campaign/ID safety](../persistence/ctz-campaign-safety.md) for addon-owned schema/reconciliation; item native storage does not close those effective contracts.

## Applying this to CtZ

Design guidance inferred from the traced phases: distinguish strategic resource balances from real item membership/counts, and persistent server identity from live handles. Reconcile against authoritative restored objects before treating temporarily unavailable clients as missing equipment. Observe the specific ownership/placement/selection/use/removal phase required by an operation; avoid treating event names or callbacks as transaction receipts. A tested soldier loadout/consumable implementation still requires the effective NPC chain. No gameplay changes or executable example are supplied.

Available-source stopping point: main selected ownership, placement/activation, consumption/removal and persistence paths plus focused Lua contracts are consolidated and audited. Continue general foundations with trade/economy. Effective-source collection and runtime resumption remain separate work; [status and requirements](source-completion-status.md), [roadmap](../../ROADMAP.md).
