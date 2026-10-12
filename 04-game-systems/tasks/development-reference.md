# Tasks dialogue and info state development reference

> ADR document set: **v0.1.78**. Research revisions and source/build versions below describe their original scope.

**Research revision: v0.1.69.** TASK-01 native foundation, TASK-02 supplied consumers and TASK-03 consolidation/audit finish the planned available-source pass within scope. Effective installed integration remains **partial**; runtime is **untested/deferred**. [Completion rule](source-completion-status.md), [audit](../../08-research/verification-2026-10-12-v0.1.69.md).

## Choose the state owner first

| Concern | Established distinction | Detailed source |
| --- | --- | --- |
| Player task grant | Actor native manager adopts a task; in-progress duplicate guard; Lua wrapper void | [Native foundation](native-task-dialogue-info.md), [Lua contracts](../../02-lua-api/tasks/native-task-info-api.md), T01–T08 |
| Mission progress | Supplied tsk.stage=1 is separate from native completed and dialogue turn-in | [Supplied consumers](supplied-task-dialogue-consumers.md), L02/L06/L07/L12 |
| Dialogue eligibility | Native actor-global info plus speaker-aware predicates; Lua condlist may use other owners | Native T12–T14; supplied L08/L09 |
| Offer description | A selected text helper runs setup effects before grant | Supplied L01/L06/L12 |
| Reward | Script effects, item delivery, money mutation and task terminal state are distinct | Supplied L03–L05/L12; [economy](../economy/development-reference.md), [inventory](../inventory/development-reference.md) |
| Restoration | Native explicit saved fields versus actor stored tables, transient caches and manager mission state | Native T03/T15/T18; supplied L06/L07/L10/L11; [persistence](../persistence/development-reference.md) |

Evidence IDs are ledger-local: [TASK-01 T-ledger](../../evidence/tasks/native-task-dialogue-info-2026-10-12.csv), [TASK-02 L-ledger](../../evidence/tasks/supplied-consumers-2026-10-12.csv). ENGINE1011, BETA150 and ZIP142 are pinned source artifacts, not verified winning installed components.

## Ordering and failure rules

Native fail deadline/info/function groups precede completion groups; each nonempty list is conjunctive, groups are alternatives. Native terminal task effects precede the actor task callback; direct task setter versus manager setter have different repeat guards. Missing functors, task adoption and unsigned timer arithmetic have documented limits. T01–T08/T18.

Selected native spoken phrases transfer info before two-speaker actions, then rebuild next choices. One-speaker actions have different ordering. Caught action exceptions do not roll back earlier info/actions. Lua info give/disable true means forwarding, not a new mutation or paid reward. T06/T09–T14.

Supplied offers, description/setup, acceptance, objective stage and turn-in are separate phases. Winning managers must connect them before any repeat or payment guarantee can be stated. BETA150's condlist can invoke a truthy-returning effect twice; ZIP142's corresponding branch invokes once. Determine the active dispatcher and handler before relying on callback/effect counts. L01/L02/L06/L08/L09/L12.

## Development review questions

1. Identify the authoritative task ID/giver, native task state, scripted stage, actor info owner and reward receipt separately. A numeric object ID or task name does not independently certify campaign/generation identity.
2. Identify the actual caller and arguments: native one/two-speaker phrase variants versus xr_logic dispatch. Keep description/eligibility functions free of unintended side effects when designing new logic; the supplied text consumer demonstrates why their names alone do not guarantee purity.
3. Trace reward validation, consumption, money/item mutation, info unlock and final marking in execution order. Require explicit retry/deduplication evidence. Native callbacks, ignored action returns and news messages are insufficient receipts.
4. Locate the serializer for each field, then the restore caller and readiness gate. Native info vectors/read state are omitted from the selected serializer; save_var tables and tsk fields need their own proven owner. Current-script functors and current-config caches can change restored behavior.
5. Check active use before changing code. Smart-control discrepancies are source candidates, but this task file has no active smart_control reference. Native dynamic text support does not justify restoring unused CtZ dialogue code.

These are source-derived design/diagnosis questions, not tested runtime recipes. Full conversation sessions, every mission variant and installed reward/restore logic remain beyond the available-source closure.

## Next boundary

Collect the [effective inputs](source-completion-status.md), then reconcile task grant/stage/turn-in/reward/save/load/cancellation and repeated calls. Runtime resumes separately only under an identified executable/profile, with logs and observed state/delivery outcomes. Other ADR subsystems can proceed without promoting these gaps to verified behavior. [Roadmap](../../ROADMAP.md).
