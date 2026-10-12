# Item persistence and reconstruction

> ADR document set: **v0.1.78**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-04
- Research revision: v0.1.57
- Source status: source-confirmed within selected native/server/actor/eatable paths
- Runtime status: untested; deferred until explicitly resumed
- Baseline: ENGINE1011; [provenance](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

Archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; unknown upstream commit, binary/profile correspondence and installed script winners. R01–R15 are local to the [evidence ledger](../../evidence/inventory/persistence-reconstruction-2026-10-11.csv), which supplies exact paths, symbols, ranges and hashes. [Investigation](../../08-research/investigations/2026-10-11-ITEM-04-persistence-reconstruction.md). Read alongside [native save/load](../persistence/native-save-load-pipeline.md), [ownership](ownership-lifecycle.md) and [placement/activation](placement-activation.md).

## Saved representations

| Representation | Selected saved fields | Restoration boundary |
| --- | --- | --- |
| Server spawn packet | Section, object/parent IDs, retained client bytes and class STATE fields | Recreates a server entity; does not create live inventory membership |
| Server inventory STATE | Float condition and upgrade list; readers gate these by spawn version >52 and >123 | Base item mixin; derived fields differ |
| Server UPDATE | Conditional physical sync payload; derived weapon/ammo fields | Not interchangeable with client custom save bytes |
| Client inventory-item save | u16 placement value, float condition, u8 physical count marker; physical state for independent items | Native load restores fields, not the inventory container |
| Client eatable save | Inherited bytes followed by u8 remaining uses | Derived load consumes the same sequence |
| Client inventory-owner save | u8 active slot, character info, game-name string and money | Active slot becomes pending restoration state |

R01–R05/R10/R14/R15. This table is a selected field map, not a binary format specification for every derived item or an addon migration guarantee.

The object registry writes qualifying root objects, then recursively qualifying children, using Spawn_Write and UPDATE_Write. Spawn_Write includes ID_Parent and retained client_data, framed with a u16 length in this writer; historical comments about 256 bytes are not the actual width. Disk reconstruction creates by section, reads spawn/update packets and registers server objects. A missing section factory skips that selected entity; it does not prove dependent references remain valid. R01/R02; PER-01 covers the wider registry/registration sequence.

Base server item STATE stores condition/upgrades, whereas its UPDATE is primarily conditional physical data. Client CInventoryItem::net_Export writes zero and returns when parented **or in single-player**. Therefore the generic client update path is not evidence that every base item's condition or upgrades has been freshly copied to the server. Derived weapon UPDATE explicitly reads/writes quantized condition, ammo count/type, addon flags, state and zoom; ammo has its own count fields. Full client producers and every weapon variant remain outside this pass. R03/R04/R06/R15.

## Client bytes and spawn order

CGameObject::net_Save writes native virtual save before binder save. During base net_Spawn, reload/reinit precede net_Load of nonempty retained client_data; net_Load invokes native virtual load before binder load. Empty client_data skips this restoration. Binder load here cannot establish final derived spawn state or completed ownership. R07.

In the selected CInventoryItemObject chain, CPhysicItem::net_Spawn (which first calls its inherited spawn) precedes CInventoryItem::net_Spawn. The latter copies server condition and installs server upgrades in single-player, then resets spawn/activation flags. Thus an earlier loaded condition is not universally the final live condition. CEatableItem::net_Spawn subsequently initializes condition to 1 or 0 when IsUsingCondition, according to max uses. Its custom byte stores remaining uses; the net_Spawn body does not derive that final condition from the restored count. These are literal ordering findings, not a reported runtime bug. R06–R10.

Client item save writes zero as the physical marker when parented; independent items write sync count and PHSaveState. Load restores placement/condition first, returns for zero, otherwise creates/disables a missing shell and loads/disables physical state. This does not establish final physical readiness after every derived hook. Upgrade save/load lines in these client item bodies are commented; server upgrade storage/install is the active selected path. R05/R06.

## Membership, placement and active selection

After successful live net_Spawn, the selected Level spawn function invokes the client spawn manager callback, then dispatches GE_OWNERSHIP_TAKE to a non-sentinel parent. The active code uses immediate cl_Process_Event; the queued packet alternative in this block is commented. A spawn callback can therefore precede the item's live inventory take in this path. R11.

Selected actor ownership handling checks CanTakeItem, sets the live parent, calls Take(..., false, true), then SelectBestWeapon. Take attempts the restored belt/ruck/slot placement; a failed attempt makes placement undefined and triggers its normal fallback. Strict placement bypasses the ordinary Slot/Belt/Ruck eligibility predicates; this fallback is not proof that restoration revalidates normal eligibility or safely migrates an incompatible slot/configuration. See ITEM-02 P01–P03. OnItemTake follows placement, before final weight/state/UI work. Other owner variants remain explicit dependencies. R12/R13; ITEM-01/02 establish their earlier scoped contracts.

InventoryOwner save records the current active slot. Load reads it, directly sets NO_ACTIVE_SLOT only for that sentinel, and records m_tmp_active_slot_num; the immediate deferred-activation line is commented. OnItemTake emits eOnItemTake, attaches the item, then requests Activate when its slot matches the pending slot and ItemFromSlot exists, and clears the pending value. The callback precedes this restoration request; Activate still has ITEM-02 eligibility/readiness boundaries. Actor SelectBestWeapon and derived owner policy can further affect selection. R12–R14.

## Practical restoration rules and remaining scope

Inference from the traced phases: reconcile persistent IDs against restored server entities, and resolve live handles only after their actual availability; do not recreate an item merely because no client handle exists yet. A parent ID, loaded placement value, spawn callback or take callback alone is not proof of final equipped/readiness state. Keep addon-owned metadata in its explicitly traced storage/binder contract, with schema and campaign identity checks; native item fields do not serialize arbitrary Lua tables. See [CtZ campaign safety](../persistence/ctz-campaign-safety.md).

Missing installed binders/helpers, offline item-state synchronization, NPC-specific restoration, all derived item serializers, binary/profile equivalence and malformed-packet recovery remain open. No universal migration recipe, callback-complete barrier or tested save compatibility is asserted. ITEM-04 is complete within selected scope; next inventory consolidation and bounded audit. Runtime remains deferred.

Current completion: the selected ITEM-01–04 foundations and [ITEM-05 consolidation/audit](development-reference.md) are complete within available-source scope. Earlier next-step text above records the individual increment; use [completion status](source-completion-status.md) and the [current roadmap](../../ROADMAP.md) for the active backlog.
