# Gameplay state development reference

> ADR document set: **v0.1.77**. Research revisions and source/build versions below describe their original scope.

- ID: GAME-04
- Subsystem: actor/NPC gameplay state
- Research revision: v0.1.66
- Source status: scoped-source-audit consolidation of selected source-confirmed contracts
- Runtime status: untested; deferred
- Baselines/provenance: ENGINE1011/BETA150; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

The selected available-source gameplay-state foundation is consolidated and audited. Full installed integration remains partial under the [completion rule](source-completion-status.md). This is a practical map of the inspected contracts, not a runtime-tested healing, loadout, revival or casualty recipe. Exact source/build/profile correspondence remains unknown.

Evidence IDs are ledger-local: [GAME-01 G01–G21](../../evidence/gameplay/native-condition-2026-10-12.csv), [GAME-02 A01–A21](../../evidence/gameplay/actor-effects-2026-10-12.csv), [GAME-03 R01–R19](../../evidence/gameplay/death-restoration-2026-10-12.csv). Original hashes/ranges/symbols and archive pins remain intact. [Consolidation record](../../08-research/investigations/2026-10-12-GAME-04-gameplay-consolidation.md), [bounded audit](../../08-research/verification-2026-10-12-v0.1.66.md).

## Choose the state and phase you need

| Mod requirement | Relevant representation | What it does not prove |
| --- | --- | --- |
| Read current live health | game_object health / CEntity condition field | Pending health changes, offline/server health or completed death bookkeeping |
| Set live health | Direct field assignment | Clamped input, hit attribution, group repair, resurrection or persisted common state |
| Apply a health delta | change_health pending accumulator | Immediate getter change or guaranteed retention through first invalid-time update |
| Assess server creature health | CSE fHealth / health() getter method | Live wrapper state, actor survival mechanics or effect restoration |
| Use a medicine item | Influence/effect application plus inventory use path | Final healing, accepted timed medicine, inventory deletion or a safe retry |
| Apply a timed booster | Type-keyed actor record plus server parameter dispatch | Additive same-type stacking or replacement when return is true |
| Interpret a hit callback | Its specific producer stage | Final health, wounds, death, loot or strategic casualties |
| Record a strategic casualty | Reconciled persistent identity and owned ledger | Universal online/offline evidence from one health read/callback |

G01–G04/G16–G20; A05–A12; R13/R17/R19. The last row is design guidance inferred from separate native/script phases; it is not an implemented CtZ feature. [Inventory use](../inventory/consumption-destruction.md), [faction actions](../factions/action-goodwill.md) and [campaign identity](../persistence/ctz-campaign-safety.md) remain distinct linked contracts.

## Health changes and update gates

Direct SetHealth assigns without the queued-change harm gate or immediate Die. Base ChangeHealth validates its float and accumulates only when CanBeHarmed or positive; CanBeHarmed requires server authority and its harm flag. Generic base satiety getter is 1 and setters/change no-op; actor food is a derived implementation. Property bindings and delta methods must not be interchanged merely because their names sound similar. G01/G02/G16–G18; [condition APIs](../../02-lua-api/gameplay/condition-api.md).

Base UpdateCondition returns at current health <=0. First invalid-time update zeros elapsed time and clears selected pending deltas, so a requested change around load can disappear before commit. During ordinary commit, critical-hit/wound/radiation hooks precede the final write; last-chance logic uses strict negative projected health and a Device-time timer, whereas condition elapsed time uses game/server time. An active timer can skip the health write while resetting the pending delta. Final clamps occur in the commit body, not in direct property assignment. G03/G07. Raising health alone does not restore AlreadyDie, membership or all derived corpse state.

Actor update separately gates god mode, living state and local/current-view ownership. Sleep chooses rates through actor_is_sleeping info. Food, movement stamina and boosters precede inherited condition commit, with later tutorial/death-effector/environmental work. Food and movement costs therefore cannot be transferred wholesale to NPC squads. Food thresholds and formula divisors depend on configuration; walk/sprint/limp use begin/end hysteresis, with equality preserving existing booleans. A01–A04/A20/A21; [actor behavior](actor-effects-equipment.md).

## Follow the selected hit chain

For an ordinary alive single-player actor, optional CActor__BeforeHitCallback can veto before further actor hit work. Script edits then feed belt artefact reduction; actor eHit observes that intermediate result before inherited outfit/helmet/base condition processing. Native fallback belt damage reduction and condition-weighted protection query are different formulas; a script override can bypass the fallback clamp. A18/A19.

GAME-01's selected live chain computes bone scales, applies outfit then helmet, applies branch-specific character immunity/protection and the optional CBeforeHitAfterCalcs, records pending damage/wounds, then commits condition through inherited hit/virtual CalcCondition. The before-hit-after-calcs relay is a mutable stage, not a bool veto or final damage receipt. It copies selected hit fields but does not restart branch selection or recompute original attribution/local wound eligibility. Its temporary hit must not be retained as persistent state, and draftsman must remain a valid live reference. G04–G11/G19/G20.

| Observation | Position in selected producer chain | Later or separate work |
| --- | --- | --- |
| Actor pre-hit functor | Before belt reduction/inherited hit | May return false; accepted edits still need downstream processing |
| Actor eHit | After selected belt calculation, before inherited hit | Armor, character condition, wound/delta commit and death request |
| CBeforeHitAfterCalcs | After branch mitigation, before recording its effects | Wounds, final health commit and inherited hit processing |
| Critical health-loss hook | Before final base health assignment | Last-chance/timer policy and death-event path |
| eDeath | Inside CEntityAlive inherited chain | Derived actor/stalker/monster inventory/squad/sound cleanup and release |
| Supplied offline death bookkeeping | Server/script battle disposition | No proved traversal through the live callback chain |

G03/G04/G09; A18; R04–R07/R19. Actual installed dispatcher/listener order, build guards and reentrant mutation remain unverified. A callback listener cannot assume all later native cleanup has already occurred.

## Equipment mitigation and effect records

Character immunity is a damage coefficient; larger coefficient is not inherently more protection. Outfit/helmet protection, armor penetration, item durability immunity and stamina power_loss are separate inputs. Native sequential gear mitigation uses each piece's input for its wear; fire-wound raw armor <=0 can return before wear. Standard and optional fire_wound_param_1/2 formulas differ, and optional presence is not safe numeric validation. Blocking penetration does not activate the commented wound-suppression line. G14/G15; A13–A17. UI statistics or base section names do not establish a universal installed damage formula.

Passive artefacts scale restoration by condition in the inspected body; selected outfit/helmet passive rates are summed without that multiplier. Their batched queued updates are not final current health. Positive artefact radiation's literal clamp(val,0,val) is retained as a source caveat when boost subtraction makes the bound negative. A19. Full bone tables, upgrades, script overrides and NPC ownership remain effective inputs.

Actor boosters are keyed by type. ApplyBooster true can mean nonpositive value ignored or weaker value×duration ignored; accepted replacement subtracts the old effect and installs a new record. Expiration is checked when actor UpdateBoosters runs, using delta_time/game_time_factor in single-player. Raw Boost* exports add modifiers without a timed record. SBooster's constructor initializes time only; callers require meaningful type/value/time. A05–A07/A10/A12; [effect APIs](../../02-lua-api/gameplay/actor-effects-api.md).

Keep two source questions open: timed medicine is stored/serialized but no advance/application consumer was found in the documented native/bundled-script scope; and BoosterForEach/ClearAllBoosters bind a non-const reference to a by-value accessor. These are source/build gaps, not reproduced installed bugs. Neither true return, helper name nor save presence resolves them. A06/A08–A12; [GAME-02 limits](actor-effects-equipment.md).

## Death and restoration use several authorities

KillEntity requests GE_DIE under its gates; guarded actor-before-death handling can intercept. Live CEntityAlive death updates faction/inherited membership before eDeath, but derived stalker/base-monster/actor cleanup surrounds that call. Server on_death writes death time and -1 health; server monster kill unregisters its A-Life group and sets zero. Neither is a universal release or live-death equivalent. G09–G12; R04–R07/R13. Supplied offline Warfare has separate relation/news/on_death ordering and does not close online/offline casualty deduplication. R19.

Server health persists in STATE and UPDATE; registry load reads STATE then saved UPDATE. Client custom condition data retains alive marker and selected other fields/wounds, with actor medicine/boosters via virtual subclass serialization. Those are separate representations, not a single atomic snapshot. R02/R09–R14; [general persistence](../persistence/development-reference.md).

Live spawn first resets conditions, then Entity copies server health before base native/binder loading. CustomMonster copies server health again after inherited spawn, overwriting a binder's earlier direct health write in that selected chain. The inspected actor section establishes no analogous post-binder health overwrite. Membership was registered earlier and is not universally recomputed by later setters. R01–R04/R08–R10. Binder load is therefore not a final-health barrier across all owners.

Actor load inserts saved boosters and reapplies parameters without locally clearing/reversing prior records; actor reinit does not reset every booster modifier/map. Fresh construction and repeated reuse differ, and idempotent complete restoration remains unproved. A dead custom marker does not itself set health or clear every field. Saved data and final restored state require caller/initialization/effective-policy evidence. R11/R12; no safe arbitrary repeated load or revival recipe follows.

## Mod integration guidance and stopping point

Design guidance inferred from the audit: retain stable server/campaign identity instead of live handles, observe the producer phase relevant to the operation, and reconcile authoritative restored objects before treating temporary unavailability as death. Record strategic casualties through a mod-owned lifecycle that accounts for online/offline source and duplicate notifications. Separate requested healing/item use from observed state; do not retry solely on a generic return value, or use health assignment as a shortcut for membership/corpse reconstruction.

No CtZ, Arsenal or ZoneMart behavior is changed. Selected available-source gameplay-state work is complete within scope; full effective integration is partial and runtime remains deferred. [Completion requirements](source-completion-status.md). Next general ADR foundation: tasks, dialogue and info state, starting with an inventory of existing UI/XML/CtZ task/dialogue research to avoid duplication. [Roadmap](../../ROADMAP.md).
