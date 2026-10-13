# Provenance-aware diagnostic triage

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

- ID: DEBUG-01-TRIAGE
- Subsystem: practical debugging
- Research revision: v0.1.80
- Record status: complete-within-scope for selected guidance; incident-specific diagnosis remains open
- Source status: selected source-confirmed routes plus pinned documentation synthesis; investigation/probe recommendations are design guidance
- Runtime status: untested; deferred; no incident reproduced here
- Baselines: ENGINE1011 [diagnostic source ledger](../evidence/debugging/diagnostic-routes-2026-10-12.csv); six prior-reference pins at ADR v0.1.79 `2db0cc343662140d3670eec16ea247e75b00279b`
- Last reviewed: 2026-10-12

Use [diagnostic routes](diagnostic-routes.md) to interpret what emitted a message, and [ownership contracts](../05-mod-architecture/module-state-contracts.md) to identify the affected state. The workflow below is recommended investigation practice, not a tested fix or permission to resume game execution. Runtime verification remains deferred.

## Preserve an incident before changing its inputs

Keep the original full log and any dump privately, with capture time and raw hashes. Preserve `.bkp` separately if present; creation of a later run's log can replace the previous log/backup. Work from redacted copies when sharing; maintain the private mapping to unredacted paths. Do not clear the logger during intake. Application/user names, source paths and dump contents can contain private machine information. L04/L07/N04 from the source ledger; [evidence policy](../08-research/evidence-policy.md).

| Intake field | Concrete evidence to record | Limitation to retain |
| --- | --- | --- |
| Executable/environment | Actual executable hash if available, startup build/version banner, command line, renderer/debug configuration | Banner/version label alone does not prove exact source equivalence |
| Profile/package | Active profile identity, mod revision, virtual winning bytes/hash/origin and differently named patches | Enabled-mod list is not final installed function order |
| Save/campaign | New game versus load versus level transition, save/campaign identity and schema labels | Numeric object ID or filename alone does not certify campaign pairing |
| Trigger/phase | Last completed action, expected versus observed result, load/spawn/UI/dispatch phase | “On load” is too broad to locate an emitter/prerequisite |
| Error artifacts | Full preceding context, first relevant symptom, assertion fields, Lua trace, native frames/address and dump if actually present | Final line, clipboard/dialog and disk log can differ |
| Frequency/comparison | Repeated or single report, prior working revision, changes made and controls used | Correlation with a recent addon is not isolation of its effect |
| Evidence status | Reporter, raw artifact availability, source pin, observed outcome and inferred mechanism | External observation is not independent ADR reproduction |

I01/L01–L07/N01–N05; triage-reference D03/D05/D06 in the [documentation ledger](../evidence/debugging/triage-references-2026-10-12.csv). These fields are an intake record, not required engine APIs. Do not publish original user paths/profile exports by default.

## Identify the emitter and failure boundary

1. Separate the first relevant symptom from the terminal failure. A warning/rejected registration can precede a different assertion or access violation. Keep the sequence and surrounding messages rather than extracting only the final line.
2. Match script/native file and line to the **winning bytes and qualified baseline**. Startup, unlocalizer preprocessing, generated namespace headers and wrappers can affect the effective implementation. Do not silently translate a reported line to a different archive's same filename.
3. Follow the reporting route: ordinary log, script category, ErrorLog assertion, local loader false, Luabind handler, binder catch or Windows filter. Record arguments/return meaning, build guards and whether the route can terminate before an outer handler.
4. Locate the owned resource/state and its lifecycle. Ask what was initialized, replaced, invalidated, serialized or still pending before this observation.
5. Write competing explanations and one discriminating source check or eventual observation for each. Mark unknown edges rather than converting them into a suggested fix.

Mere function naming is insufficient: [Lua diagnostics API](../02-lua-api/debugging/diagnostic-api.md), [route boundaries](diagnostic-routes.md#error-handling-is-not-one-recovery-protocol). This sequence is triage guidance inferred from the selected routes and ARCH-02, not an implemented automatic diagnosis algorithm.

## Use bounded, discriminating cases

| Symptom | Keep these explanations distinct | Source check now / observation if runtime resumes |
| --- | --- | --- |
| Expected log text absent | Gated script_log, DEBUG stack suppression, buffer not flushed, -nolog, invalid writer, message truncation or wrong effective alias | Match export/helper and command/build guards; compare private full log/path. A later bounded probe would compare known emission and disk snapshot |
| Missing callback name | Wrong dispatcher/event registry, missing installer/producer, version mismatch or later alias replacement | Trace effective Register/Send/Unregister together. Selected axr_main diagnostic calls unresolved printf/callstack then returns; find the actual terminal route separately |
| Syntax/compile error | Malformed source, wrong winning file or preprocessing mismatch | Check exact bytes and syntax location. Compilation did not run that main chunk, but dependencies/previous modules may already have effects |
| Runtime error during module load | Partial evaluation, failed external call or stale dependency | Trace statements before failure; ordinary namespace presence can suppress retry. Record which effects precede failure rather than assuming reload repairs them |
| XML/DXML error | Protected parse/construction failure, unprotected callback/serialization or malformed transformed XML at native assertion | Match the local stage, callback/output and selected outer Luabind/assertion projection; protected parse fallback does not certify every stage |
| Quickload/UI fault | Display registration alias, parent/PDA ownership, rebuild timing or addon interaction | Compare creation/registration/teardown route and exact phase. REV-01 mechanisms retain inference labels; no arbitrary delay or generic delete is certified |
| Object/binder disappears after an error | Selected catch clears binder, client teardown, permanent server release or reused identity | Match representation and handler; binder continuation TRUE/FALSE is not restored addon success. Reacquire/validate at the actual phase |
| Repeated delivery/update or stale setting | Repeated installer/listener identity, unresolved retry, old table alias, separate caches or unapplied menu stage | Trace capture and owners plus native/request completion. A callback or successful stored write is not reconciliation |
| Timing/hitch discrepancy | Wall time, engine milliseconds, game-clock restore/rewind, native budget expression, workload or instrumentation | Record clock/unit/phase and inspected formula. Compare bounded measurements later; do not infer microsecond correctness from a parameter name |
| Native stack/dump incomplete | Filtering, symbols unavailable, handler stack instead of fault context, initialization/filter coverage or dump-write failure | Preserve address/build/raw artifact; inspect source guards. Missing frames/dump do not exclude native or addon involvement |

Source ledger L01–L07/B03–B06/N01–N06/A01–A03/S01–S15/P01–P02; documentation D01–D06. Each row is a set of alternatives with a discriminating plan. It does not diagnose a particular installed crash, modify saves or prescribe addon removal/load-order changes.

The callback case illustrates a useful boundary: ENGINE1011 axr_main's absent-event branch logs/callstack/returns locally; the effective helper could still behave differently, and a later call can fail elsewhere. Preserve a reported missing-event message without automatically calling that message the fatal cause. This also avoids mapping another build's dispatcher behavior onto October source. P02/D02/D03.

## Design minimal probes around a question

Recommended probe record: hypothesis, exact producer/phase, baseline/winner, value owner, expected discriminating outcomes, bounded message schema, removal plan and runtime status. Use a run/operation identifier plus phase and short validated scalar summaries where helpful. Document missing versus false/empty, copied versus aliased values, and pre/post boundaries. Do not dereference a potentially stale native handle solely to print its name. D06 and [ARCH-02 lifecycle](../05-mod-architecture/module-state-contracts.md#make-lifetime-transitions-explicit).

Choose the least invasive source check first: resolve an export/arity, compare winning-file hashes, inspect a callback emitter or follow a serializer. A passing repository/catalog test does not answer a gameplay hypothesis. When actual runtime work resumes, use a preserved reproduction copy and change one discriminating input at a time; record outcomes and regressions separately. Source/tool checks and eventual profile tests remain different evidence axes. [Workflow](../08-research/workflow.md), [tests](../tests/README.md).

Bound logging by feature/phase and sample count or rate under a defined clock; enable it deliberately and retain enough fields to distinguish outcomes. Use short preformatted strings for the native log wrapper; do not use error_log as routine instrumentation. Avoid full table dumps, per-frame stack traces and flush-per-item as defaults. These are recommendations motivated by fixed formatting buffers, vector growth, synchronous callbacks and whole-buffer disk rewrite, **not measured safe rates**. L01–L04/S01/S04/A02.

Log timestamps are local wall time. Scheduler Device.dwTimeGlobal milliseconds, simulation game-time delta and the inspected process-budget forwarding expression have separate units/semantics. State which clock a probe uses, whether it survives/rewinds on load, and whether a duration spans deserialization or later reconciliation. D04/D03; [clock guidance](../04-game-systems/alife/configuration-controls.md#time-and-count-limits-are-different). Profiler controls/results, logger cost and safe throughput remain unmeasured/deferred.

## Keep disposition separate from confidence

A useful incident disposition states the observed failure, qualified source route, supported mechanism or remaining alternatives, missing effective inputs, proposed next observation and any actual result. A source-confirmed route can coexist with an untested diagnosis; an external repeated observation can coexist with unknown executable correspondence. Do not close an incident because links/hashes match, a pcall returned false, or the native caller continued.

DEBUG-01 closes these selected diagnostic/triage contracts. Effective aliases/build/profile chains and independent runtime reproduction remain partial; no generic crash recovery or tested fix is certified. Next ARCH-03 qualifies selected patterns/test guidance and consolidates/audits the practical foundation. [Verification](../08-research/verification-2026-10-12-v0.1.80.md), [roadmap](../ROADMAP.md).

Current completion: ARCH-03 [central guide](../05-mod-architecture/development-reference.md), [patterns](../07-code-library/qualified-patterns.md), [test guidance](../05-mod-architecture/test-guidance.md) and [bounded audit](../08-research/verification-2026-10-12-v0.1.81.md) complete the selected practical foundation. Earlier DEBUG-01 allocation remains dated; proposed probes/fixtures remain unimplemented and runtime deferred. Next separate whole-ADR audit.
