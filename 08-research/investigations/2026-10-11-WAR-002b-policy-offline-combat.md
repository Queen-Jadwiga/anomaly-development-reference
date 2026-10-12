# WAR-002b — Targeting, ownership and offline combat in the supplied Warfare source

> ADR document set: **v0.1.60**. Research revisions and source/build versions below describe their original scope.

**ADR v0.1.33 · 11 October 2026 · scoped package-source findings; runtime deferred.**

## Scope

This traces BETA150 main files and its separately supplied GAMMA squad variant, as defined in [WAR-002a provenance](2026-10-11-WAR-002a-source-packages-effective-profile.md). ZIP142 shares several exact files, but is not substituted silently for BETA150 where they differ. Evidence IDs W01–W16 refer to the [source ledger](../../evidence/warfare/source-evidence-war002-oct11.csv).

The effective MO2 winner and later script patches are unverified. In particular, base smart-terrain and board implementations are missing, so calls into their methods are evidence boundaries rather than fully verified internal behavior.

## Four states that CtZ must distinguish

| State | Examined representation | Evidence |
| --- | --- | --- |
| A-Life membership | Native group/member records | [ALIFE-01](2026-10-11-ALIFE-01-identity-lifecycle.md) |
| Warfare eligibility/registration | `registered_with_warfare`, checked flag and faction-indexed `warfare.registered_squads` | W06:70–166 |
| Routing and arrival | Target IDs, `smart_id`, `current_action`, `combat_target_id`, arrival time | W06:198–238,913–965; W10:516–540 |
| Strategic terrain ownership | `smart.owning_faction`, owner history/cache and policy checks | W07:4387–4424,4474–4630 |

CtZ's own campaign-fort owner is a separate model. No synchronizer between that model and Warfare's owner state is established by this pass.

## Targeting does not itself prove arrival

`sim_squad_warfare.set_target` returns early for missing/companion squads, task squads with `stay_time`, and ignored sections. For a resolvable target, it sets action 0, clears the scripted target, writes current/assigned target IDs, marks/registers the squad with Warfare, invokes a smart target's `on_reach_target`, and calls board setup for members. Despite the method name, this hook is invoked during targeting; it is not independent evidence of completed physical arrival. Its smart-terrain implementation is unavailable here. [W06:913–965]

In `squad_warfare_update`, a smart target whose ID differs from `smart_id` is assigned through `squad:assign_smart` before the arrival check. For action 0 without a combat target, the smart branch checks faction hostility and `am_i_reached`, invokes `on_after_reach`, and then sets action 1 and arrival/wait times. The non-smart branch lacks that smart-owner hostility test. This traces script state changes, not the missing reach-test internals. [W06:198–238]

The supplied squad `assign_smart` resolves the old smart, sets `smart_id` when a new smart exists, and iterates members to unregister from the old smart and register with the new one. With a nil new smart, this body does not explicitly clear `smart_id`. The board's nil-assignment contract must therefore be inspected separately; do not infer that every nil assignment clears every squad/member/job field. [W10:516–540]

## Update and override order

The supplied squad update calls `check_online_status`, sends `squad_on_update`, then computes the current actor distance, checks invulnerability and invokes specific/generic targeting. A callback listener thus cannot assume the distance has already been refreshed for this update. [W10:219–243]

Warfare's squad listener checks game mode and registration, uses a checked flag to avoid repeated registration checks, and, for non-companions that reach that part of the function, sets `__lock`, clears scripted targeting, updates rush state and invokes the Warfare-specific update. Do not generalize this to every unregistered or early-returning squad. [W06:70–166]

`warfare_options.script` assigns an override of `check_online_status` at module level. It computes `forced_online_status` using survival/force-online/companion/level checks and selected monster/exclusion conditions. It also **defines** `override_functions` to replace generic/specific update methods, but a search of the supplied BETA150 package found only the function definition, not a caller. Defining it is not proof that those replacements are installed. External callers or other overrides remain open. [W09:224–229,255–304]

Warfare startup registers smart update, squad update, actor update, save/load, member-death and server-entity-unregister listeners, initially sets the global Warfare flag, and schedules a resetter on game load. The resetter removes its listeners when the game is not in Warfare mode. Offline-combat startup separately schedules its coordinator, which subscribes to squad or smart updates depending on the offline-combat option. These callbacks can share a bus; their effective relative listener order is not established from the missing global wrappers/profile patches. [W05:917–940,1084–1098; W08:243–367,766–778] See also [ALIFE-02](2026-10-11-ALIFE-02-creation-registration-release.md).

## Ownership is a policy result

The examined smart update runs `check_owner` before the initialized-Warfare gate and before subsequent autocapture/spawn/strategic processing. Ownership recalculation is therefore a phase within the update, not a dedicated capture callback documented here. [W07:368–456]

`squad_count_defending_all` iterates the board's smart squad table. A counted squad must have the group class, recognized Warfare faction, an entry in that faction's registered-squad table, action 1, no companion/ignored classification, positive power/member count, and current target matching the smart. It counts qualifying squads and sums their power by faction. Board assignment alone is insufficient. [W07:4387–4424]

`check_owner` starts with a candidate of none and uses that count table. It can retain the present owner when represented, select a candidate on an unowned smart by count, and transfer loner/ecologist/zombified ownership to another non-hostile faction under special base/count rules. Manual-capture state can suppress a candidate that is not the actor's faction. It then applies cached-owner restoration within an initial 300 game-second window and a keep-last-base branch. Counts and powers are stored for the candidate before those later retention branches. This is not a universal “strongest squad wins” rule. [W07:4474–4630]

The loop uses `pairs`; tied/competing candidates are not given a stable total order. The source also references `owner` before its local declaration and compares faction against unquoted `monster`. Those references must not be paraphrased as a proven literal monster-exclusion rule. No source correction or runtime diagnosis is made.

The keep-last-base branch deserves literal treatment: entering its outer branch does not guarantee a new assignment on every inner outcome. A previous owner state can persist. Owner transitions also trigger targeting/patrol/invasion and respawn-timer bookkeeping. A single UI icon, destination field or board row does not establish the complete ownership result.

### Autocapture routes differ

The newer BETA150 route checks settings/faction/base availability, surge and initiation-night conditions, active powered PDA, eligible unowned base/territory proximity, existing allied targets and nearby bases. It records a staged request; after its waits, a base branch creates a squad at that base and targets the destination. The old-method branch instead creates a squad at the smart after its wait and population check. Both are squad-spawn/target operations, not direct owner assignment within these functions. Their restrictions and properties differ; the fallback occurs before some newer-route checks. [W07:502–799]

Numeric distances, active presets, exact reach criteria and effective option values remain unverified.

## Offline combat and death ordering

The offline coordinator selects the smart-only or full simulation mode and rebuilds a per-level candidate registry. The examined update paths reject online attacker squads; enemy validation rejects online targets, checks opponent availability, faction hostility and squared X/Z distance, and applies mode/ignore/story policy. Several task-exclusion lines are commented out. Warfare-specific distance and faction power come from its options; no active values are inferred. [W08:28–49,105–469]

Power is an abstraction: stalker rank or randomized monster class/rank values with faction multipliers, summed/cached per squad. A battle subtracts a rounded randomized fraction of attacker power from the victim's cached power. A depleted victim squad follows a full-defeat branch; another threshold can kill a selected member. This is not a native weapon/armor/ballistics simulation. [W08:471–558,622–670]

| Examined path | Operations in source order |
| --- | --- |
| Full defeat | Outcome bookkeeping → remove squad combat/Warfare cache info → iterate victims and call `victim:on_death(attacker)` |
| Selected-member loss | Outcome bookkeeping → remove cache info if the squad has at most one member → selected victim `on_death` |
| Special-story exclusion branch | Remove losing squad info → call member `on_death`; no normal battle-outcome call in that branch |

`remove_squad_info` and `sim_squad_warfare.remove_squad` clear combat/registration bookkeeping; the latter's actual squad-removal calls are commented out. The function name is not proof of native deletion. Full-defeat outcome bookkeeping refers to a selected victim and attacker; its rank/kill-stat increments are not a per-member death ledger for every victim in the subsequent loop. [W08:374–619; W06:316–333]

### Why online/offline cleanup equivalence remains open

In ENGINE1011, native creature `on_death` sets the game death time and health to -1. The simulator death method calls creature death and then notifies the native group about its dead member; the single-player server death entry calls that simulator method. Calling the creature method directly is not the same call chain. Creature virtual wrappers expose `on_death` under the examined game-export guard, permitting script-specific behavior. [W12–W15; W13:84–100]

Offline combat calls the victim method directly. The installed `se_stalker` / `se_monster` implementations are missing, so the step from that call to squad `on_npc_death` cannot be closed. If reached, the supplied squad method sends `squad_on_npc_death` **before** `remove_npc`; that removal unregisters membership and can invoke safe release for offline members or empty groups. The safe-release implementation/timing is also missing. [W08:471–558; W10:445–540]

CtZ should not infer native removal, completed membership cleanup or one casualty per kill-stat increment from these calls alone. The existing [ALIFE-02 release-chain findings](2026-10-11-ALIFE-02-creation-registration-release.md) remain valid within their native scope.

## Persistence and next source work

Warfare's save handler explicitly stores squad IDs/targets, smart owners, timers and strategic tables; the newer file adds maximum resource-count state. Its load handler restores selected tables. This proves an intentional persistence mechanism, not a complete save-order contract or automatic serialization of arbitrary CtZ fields. [W05:123–222; comparison ledger]

**Completed:** supplied package comparison, targeted squad assignment/arrival boundaries, owner-selection policy, offline combat call sites and callback phases.

**Still open:** active winning files and runtime function replacements; board/smart register/reach internals; server-creature death overrides; safe-release queue; full save/load ordering and CtZ campaign identity. ALIFE-03 / WAR-002 remain partial and ALIFE-04 remains open. No in-game tests, gameplay changes or license additions were made.
