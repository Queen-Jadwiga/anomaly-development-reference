# Native task dialogue and info state

> ADR document set: **v0.1.70**. Research revisions and source/build versions below describe their original scope.

- ID: TASK-01
- Subsystem: tasks/dialogue/info state
- Research revision: v0.1.68
- Source status: source-confirmed selected native/Lua/persistence paths
- Runtime status: untested; deferred
- Baseline/provenance: ENGINE1011; [source record](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-12

[Ledger T01–T18](../../evidence/tasks/native-task-dialogue-info-2026-10-12.csv), [investigation](../../08-research/investigations/2026-10-12-TASK-01-native-task-dialogue-info.md), [Lua contracts](../../02-lua-api/tasks/native-task-info-api.md). This first native pass does not establish effective GAMMA task rewards, repeatability, NPC dialogue packages or whole restoration. The subsequent [supplied-consumer pass](supplied-task-dialogue-consumers.md) and [practical consolidation](development-reference.md) retain these native limits.

## Prior coverage and state owners

[Persistence](../persistence/native-save-load-pipeline.md) already locates task/info registries in auxiliary save data; [UI/PDA](../../03-ui-pda/development-reference.md) owns window/registry readiness; prior CtZ task/dialogue work is project-specific. GAME-02 sleep reads an info flag but does not define task lifecycle. Keep the actor's CGameTaskManager, per-owner known-info registry, active dialogue graph/session and mod-owned mission state distinct.

Task states are fail=0, in_progress=1, completed=2 and dummy=u16(-1); types include storyline/additional. The manager holds task keys/pointers through a registry initialized with key 0 in the inspected constructor; active task ID is separate global state saved by the task registry. Known-info wrappers are initialized with the owner's server ID, use A-Life registry when present and a local fallback otherwise. These native keys are not a universal campaign fingerprint. T02/T04/T16/T17.

## Granting and updating tasks

GiveGameTaskToActor commits helper function names, then rejects an already-in-progress matching task ID. The bCheckExisting condition is commented in that guard: passing false does not bypass it. It pushes the task key/pointer, records game-time receive/deadline/display timer using supplied seconds×1000, stable-sorts descending priority, calls OnArrived (in_progress/unread/map setup), makes the task active/read, refreshes PDA if present and emits the state callback. The pointer is stored before callback. No duplicate terminal-history rule or safe failure ownership recipe follows. T01/T02.

UpdateTasks skips while Device.Paused, disables map pointers, copies task keys into a temporary stack buffer and processes in-progress tasks. The copy stabilizes the container iteration shape, not pointed-object lifetime under arbitrary callbacks. Terminal outcomes go through manager SetTaskState; active-pointer display and active-task reselection follow. Deadline failure tests game time strictly greater than deadline and is disabled when deadline equals receive time. Timer TTL is separately retained for map display; it is not this failure test. Unsigned seconds×1000 arithmetic is not an arbitrary-large-duration safety guarantee. T01/T02.

UpdateState checks in order: expired deadline → all fail-info entries → all fail-functions → all complete-info entries → all complete-functions → existing state. Within a nonempty list checks are conjunctive, but info and function groups are alternative triggers in this order; empty groups return false. A missing/invalid cached functor can affect CheckFunctions because its previous result is reused when the entry is invalid. Init logs missing functions rather than asserting every name resolved. Do not equate function registration with guaranteed eligibility/reward execution. T01/T03.

Terminal CGameTask::SetTaskState writes the state, removes map locations, records finish game time, sends fail/complete info, calls the corresponding functions, then emits actor eTaskStateChange. Its own body has no same-state guard; repeated direct calls can repeat side effects. The manager's ID setter only finds an in-progress task, which provides a different repeated-call boundary. Native task action functors share the bool(task_id) type with predicates, but CallAllFuncs discards their returns. A false action return is not rollback. Manager active-ID clearing/PDA refresh happens after the task callback. T01/T02/T18.

No native monetary/item reward transaction is present in these selected state bodies. Named scripts may perform rewards; [economy](../economy/development-reference.md) and [inventory](../inventory/development-reference.md) retain payment/delivery limits. Task completion callback is not a conserved reward receipt.

## Task reconstruction is narrower than the live object

save_task retains state/type, receive/finish/deadline/timer times, title/description, helper function-name lists, icon/map hint/map type/object ID and priority. The key serializer separately stores task ID; load constructs a fresh CGameTask, restores key ID, loads fields, resolves function names and reconnects an existing serialized map location by owner-task ID. The missing expected map link meets VERIFY rather than unconditional recreation; disabled/no-map fields return early. T03/T04.

The four live info vectors (complete/fail conditions and on-complete/on-fail additions) and m_read are not written by these selected task save/load bodies. This is a scoped omission, not a claim that an installed script cannot rebuild them. It makes effective task-manager restoration important. Saved function names resolve against current scripts rather than preserving prior Lua closures/code. Registry load places map locations before tasks; loaded info flags come earlier, but UI/actor/binder readiness remains separate. T03/T15/T18; [general persistence](../persistence/development-reference.md).

## Info transfers mutate locally and emit an event

TransferInfo verifies nonempty ID, emits GE_INFO_TRANSFER to the owner, constructs/loads a CInfoPortion, then directly invokes virtual receive or disable locally. Event handling invokes the same virtual hooks. Receive inserts a new ID or returns false for duplicate; disable erases if present. Therefore this inspected operation is not merely a deferred request. It also is not a general exactly-once callback contract for every derived override. T09.

Actor receive first performs base insertion; duplicates stop before eInventoryInfo. For a new ID it calls that actor callback, then may request talk-question refresh; lack of UI can yield false after insertion/callback. Actor disable removes via base and refreshes shown talk UI, with no corresponding eInventoryInfo callback in this body. Lua give/disable_info_portion returns true after forwarding for an inventory-owner receiver regardless of duplicate/no-op; has_info returns false on invalid owner, dont_has_info true. A boolean from a give operation is not proof of newly changed state. T06/T10.

The active CInfoPortion class only stores its loaded ID. The earlier XML/article/disable-list/script behavior is commented out in this snapshot; it must not be promoted to active native implementation from old code/comments. Per-owner known-info string state and installed scripts can supply other policy; XML existence/reward execution is not certified by this tiny Load method. T11.

## Dialogue conditions and actions

The helper loads precondition/action/has_info/dont_has_info/give_info/disable_info sequences from XML. Its info checks and transfers use Actor(), despite accepting and verifying a speaker inventory-owner argument. Required IDs all present and forbidden IDs all absent pass CheckInfo; with no constraints it returns true. A caller's NPC speaker does not redirect those native info checks to NPC knowledge. T12.

| Selected overload/stage | Script invocation | Info ordering |
| --- | --- | --- |
| One-speaker precondition | bool(speaker); required functor lookup | Info checks first; ordered predicates stop at false |
| One-speaker action | void(speaker, dialog_id) | Script actions before actor info transfers |
| Two-speaker precondition | bool(speaker1,speaker2,dialog_id,phrase_id,next_phrase_id), plus parameter table under DIALOG_UPGRADE | Info checks first; guarded prefix can invert predicate |
| Two-speaker action | void(speaker1,speaker2,dialog_id,phrase_id), plus empty next-id/parameter table under DIALOG_UPGRADE | Actor info transfers before scripts; action invocation surrounded by catch-all |

T12/T13. Missing functor resolution is asserted outside the action catch block; a caught invocation exception is not rollback of already transferred info or earlier actions. Build-guarded colon-parameter and !/= prefix handling must not be assumed active without executable flags. The string parser is not a general safe arbitrary-script expression evaluator.

The selected spoken-phrase caller uses the two-speaker Action, with the current speaker first. It then clears/rebuilds available next phrases, testing their Preconditions with speakers reversed for the next turn; no remaining available choices on an edged graph meets an assertion. Thus selected phrase actions/info can affect the next offered choices, but action success/return is not a conversation transaction. Dialog-level precondition also uses the two-speaker form. T14.

GetScriptText falls back to the supplied text key only when no text function is named. A configured missing function asserts; called arguments differ under DIALOG_UPGRADE. Dynamic text is therefore a native-supported mechanism in this scope, not proof that any CtZ dialogue actually configures or calls it. Existing unused project text code must not be resurrected on this finding alone. T13; [project boundary](../../09-projects/capture-the-zone/README.md).

## Limits and next pass

Task/map state, actor info flags, dialogue eligibility and scripted reward delivery are different layers. Persist mission identity and reconcile effective state before retries; neither task state callbacks nor info-add returns are atomic reward receipts. This is inferred design guidance, not a tested task/requisition recipe.

TASK-01 completes this selected native foundation. The subsequent supplied-consumer pass and practical consolidation/audit are complete within selected available-source scope; missing effective XML/configuration/binder/startup, manager/reward and restoration implementations remain open. Runtime remains deferred, and no CtZ code is changed. [Completion status](source-completion-status.md), [roadmap](../../ROADMAP.md).

## Subsequent source pass

TASK-02 available supplied caller tracing and TASK-03 practical consolidation/audit are now complete within selected scope. See [supplied consumers](supplied-task-dialogue-consumers.md), [central guide](development-reference.md) and [current status](source-completion-status.md). The TASK-01 findings above retain their original native scope; effective installation/runtime gaps remain open.
