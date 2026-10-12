# Supplied task dialogue reward and restoration consumers

> ADR document set: **v0.1.82**. Research revisions and source/build versions below describe their original scope.

- ID: TASK-02
- Research revision: v0.1.69
- Source status: selected supplied consumers confirmed; effective installation partial
- Runtime status: untested; deferred
- Last reviewed: 2026-10-12

[Ledger L01–L16](../../evidence/tasks/supplied-consumers-2026-10-12.csv), [investigation](../../08-research/investigations/2026-10-12-TASK-02-supplied-task-dialogue-consumers.md), [native foundation](native-task-dialogue-info.md). Source IDs and pinned archive provenance are in the [manifest](../../evidence/manifest.md). BETA150 main and ZIP142 are alternative supplied snapshots, not one installed profile. No third-party code/assets are redistributed.

## Scope and source availability

The selected archives contain dialogs, xr_logic, assault/smart-control extensions, task configuration and offline-combat listeners. Expected standalone task_manager, axr_task_manager, task_functor, task_status_functor, xr_effects, xr_conditions, itms_manager, bind_actor, _g and axr_main implementations are absent from the selected main package. Extensions assign into some of these namespaces; their presence does not supply the base implementation or prove startup order. This pass traces the available callers to those explicit boundaries rather than inventing the missing callees.

The full dialogs, tasks_assault, tasks_smart_control and tm_warfare files are byte-identical between these two snapshots. xr_logic differs at the effect-dispatch branch below. L01–L16. File identity does not establish winning XML, task include chains, core managers or executable correspondence.

## Offers, descriptions and acceptance are different operations

Dialogue callers resolve the NPC using AC_ID and the two speakers, then use per-NPC lists in axr_task_manager. generate_available_tasks builds offers; npc_has_task reads the first entry; npc_give_task passes that ID and giver ID to task_manager:get_task_manager():give_task. Skipping removes the first offer entry. Neither the supplied wrapper nor this list mutation is proof of a successful native task grant. L01/L04.

text_npc_has_task is not a pure text read: it parses the configured on_job_descr and evaluates it with db.actor as both arguments before returning text. Fetch descriptions trigger another external setup helper. In tm_warfare an assault on_job_descr names setup_assault_task. That extension reads cached selection, modifies squad stay_time, marks sim_offline_combat.task_squads, stores an actor task-keyed table and schedules a next-frame talk message. Therefore selected description generation can perform world/state setup before acceptance. Repeated text requests and abandoned offers are not certified harmless; callback registration, dispatcher behavior and installed UI/XML decide actual invocation. L01/L06/L12.

The assault validator writes an offer cache; setup requires a cached squad and smart still available. Status later reads load_var(actor,task_id), checks the smart/board and rebuilds faction parameter caches from current task_ini. Missing data/smart returns fail, but availability nil defers while false fails. An uninitialized same-level squad returns a wait result; otherwise scans may reselect a squad and force it online. Checks are throttled by time_global()+3000 stored on tsk. No relevant qualifying squads ultimately sets tsk.stage=1 and may assign controllable smart faction. L06. That assignment is not the native completed enum or a paid reward.

## Stage, turn-in and reward boundaries

Assault/smart-control target functors redirect to task_giver_id at stage 1, and their status functions stop at stage 1. Supplied tm_warfare sections specify stage_complete=1. Dialogue generates finished-task lists and delegates turn-in to axr_task_manager.set_finished_task_complete(npc); cancellation delegates to task_manager:set_task_cancelled(task_id). The missing managers must establish how stage, terminal native state, callbacks, on_complete and history/repeat timing are related. L02/L06/L07/L12.

The task file contains 89 section headers; no active smart_control reference occurs in this file. The smart-control extension is source-present, but its configured consumer remains unproven in this supplied task definition. Do not label it an implemented installed mission or delete external code from this absence.

| Selected configured path | What the supplied file names | Unresolved callee behavior |
| --- | --- | --- |
| Loner assault | Stage increment, random money, stash and community goodwill effects; repeat_timeout=86400 | Manager timing, deduplication, random payout implementation and repeat units/enforcement |
| Loner artefact fetch | fetch_reward_and_remove then stage/goodwill; reward_item=vodka | Consumption validation, item grant, payout and partial-failure handling |
| Mechanic tool tiers | Info unlock plus goodwill, fetch removal/reward and stage effects; earlier-tier info preconditions | Effective definitions, execution ordering across the manager, rollback and repeated turn-in |

L12/L16. These are declarative policy requests, not proven completed economic transactions. inc_task_stage, reward_random_money, reward_stash, fetch_reward_and_remove and relevant base helpers are absent as implementations in the selected main package. Native task callbacks and info-add booleans retain their [TASK-01 limits](native-task-dialogue-info.md).

Available dialogue money wrappers directly give_money or transfer_money then send news; item wrappers delegate to missing itms_manager. trade_important_documents_reward sequentially asks to remove each cached document, releases any remaining matching actor object, awards cached money and two random item selections. This body has no explicit transaction, rollback or paid-once record. Its eligibility/cache producers and winning dialogue definitions must be traced before treating it as an installed reward protocol. L03–L05; [economy](../economy/development-reference.md), [inventory](../inventory/development-reference.md).

## Condition-list dispatch differs between supplied snapshots

BETA150 xr_logic checks ordered condlist entries and applies the first matching entry's effects before returning its result. Info conditions/effects can route to NPC, actor, or A-Life owner 0 depending on flags and availability. This is separate from native phrase helpers' actor-global info policy. Missing predicate lookup logs without setting the failure flag in that branch; missing effect lookup logs but can still reach a nil call when obj/npc are present. No transactional protection is shown. L08.

Most consequentially, BETA150 tests the effect's return by invoking it in the condition. With both obj and npc present, a truthy return causes a second invocation in the else body. A false/nil return executes once and logs the diagnostic; missing obj/npc short-circuits invocation. ZIP142 has one unconditional effect invocation at the corresponding point. These source branches do not establish whether the installed dispatcher double-applies any particular reward: that requires the winning file, handler return and actual call. L08/L09. setup_assault_task has no explicit success return, so the selected function does not qualify for that truthy double-call branch merely by existing.

## Restoration callers and source anomalies

The task extensions store tables through save_var and read load_var; base helper implementation, namespace ownership/defaults and durable encoding remain absent. Local caches have no explicit serializer/listener in these two extensions. Assault rebuilds its status faction cache from current configuration; task selection is recovered through the external actor store. The separate tsk.stage and __check_smart_time ownership/restoration depend on the missing manager. Do not claim these are preserved by native CGameTask serialization. L06/L07; [Lua storage contracts](../persistence/lua-storage-contracts.md).

xr_logic.save_obj/load_obj call pstor_save_all/pstor_load_all. Under USE_MARSHAL those helpers forward to named callbacks and return; the alternative scalar/CTime path is already covered by PER-02. That path alone does not establish task tables are encoded. Offline combat load_state adopts offline_task_squads or {}, while save_state attaches the live task_squads table to shared input. on_game_start registers load_state and an on_game_load listener; that listener schedules the coordinator and registers save_state. Emitter/encoder timing, reset, repeat registration and active binder remain unresolved. L10/L11; [persistence reference](../persistence/development-reference.md).

Smart-control has two concrete source discrepancies: the target function reads cache_info.smart_id/squad_id, while status stores cache_info[task_id]; and the squad-readiness helper can return boolean true, which status treats as a squad_id in its cache. Setup stores only is_enemy/scripted and derives smart lists from current configuration. These are source-level candidates for inspection if an effective consumer exists, not runtime-confirmed crashes or requested fixes. L07/L15. No source or CtZ gameplay code is modified.

## Effective inputs needed to close these chains

Obtain winning task_manager/axr_task_manager and functor implementations; xr_effects/xr_conditions and fetch/reward helpers; itms_manager; global save_var/load_var/storage definitions; actor/generic binders and dispatcher; task include roots, character dialogue XML, info definitions and active addon replacements; USE_MARSHAL producer and executable build correspondence. Trace startup namespace availability, stage-to-terminal transition, reward/payment/removal order, cancellation/retry guards, repeat history, omitted native info-list reconstruction, cache reset/rebuild and save/load/level-change phases.

The available-source pass is complete within this scope; installed closure remains partial. [Completion status](source-completion-status.md), [central guide](development-reference.md), [audit](../../08-research/verification-2026-10-12-v0.1.69.md). Runtime remains deferred.
