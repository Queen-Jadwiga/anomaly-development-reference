# DEBUG-01 — Diagnostic routes and triage

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

- ID: DEBUG-01
- Subsystem: debugging / practical architecture
- ADR revision: v0.1.80
- Record status: complete-within-scope for selected routes/triage; effective integration partial
- Source status: source-confirmed selected definitions/registration/converter/callers; scoped build inspection and documentation synthesis
- Runtime status: untested; deferred
- Baseline IDs and provenance record: ENGINE1011 archive SHA-256 `withheld-upload-fingerprint`; six ADR v0.1.79 documentation pins at `2db0cc343662140d3670eec16ea247e75b00279b`; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

What do selected native/Lua diagnostics establish about message emission, stack/error handling and file output, and how should a mod developer investigate failure without assuming recovery or installed correspondence?

Included: native logger/writer/creation/close and console controls; Lua log/error_log/print_stack/flush exports and default string converter; build/command guards; soft/fatal assertion, current-stack filtering, Windows unhandled filter and conditional dump attempt; loader report versus Luabind handler versus binder catch versus panic; selected supplied helper/rejection boundaries; provenance-aware triage, clock and bounded probe guidance.

Completion requires traced selected definition/export/caller/conditional paths with hashes/ranges, explicit failure/output/format/lifetime limits and usable intake/hypothesis plans. Excluded: every native crash, full debugger/StackWalker/symbol/profiler implementation, alternate older xrDebug.cpp behavior, exhaustive security/error propagation, all addon profiles, actual gameplay reproduction, measured overhead and runnable examples. ARCH-03 and the later whole-ADR audit remain separate.

## Evidence and method

[41-row source ledger](../../evidence/debugging/diagnostic-routes-2026-10-12.csv) pins **67 range groups in 21 files**. [Scope record](../../evidence/debugging/diagnostic-scope-2026-10-12.json) records selected inputs and exclusions; [six documentation pins](../../evidence/debugging/triage-references-2026-10-12.csv) preserve original XML/config/REV-01/clock/environment/ownership qualifications. Evidence IDs are ledger-local.

Read definitions, registration, default converter, file writer, Luabind pcall/functor and relevant guards/callers. Match common header flags with selected project definitions and excluded older debug implementation. Read LuaJIT panic exit edges rather than interpreting a callback return as resumed success. Reuse local XML and script contracts instead of claiming exhaustive outer-chain closure. Do not identify a user binary or winning profile from the uploaded archive/date.

## Findings

1. **Emission is not disk completion.** LogFile buffers; adjacent timestamped duplicates compress; native callback receives original split under lock. Flush rewrites via wb and has no success/durability result; -nolog does not disable buffering. Invalid writer handling and unconditional console success text retain their limits. L01–L07; [routes](../../06-debugging/diagnostic-routes.md#message-memory-buffer-and-disk-are-different-stages).
2. **Flags describe different mechanisms.** R_ASSERT/FATAL, DEBUG/release VERIFY, ignore_verify, -dbg, debug/Panda startup and secondary output are distinct. Source/header/project projection does not prove installed build flags. B01–B06/S01/S12–S15/A01–A03.
3. **Stacks are filtered current observations.** Lua print_stack has readiness/filter gates; native StackWalker drops selected module/symbol lines and the selected unhandled route does not walk the saved exception context. Assertion fields locate reporting code; GetLastError text differs from ExceptionRecord address. N01/N02/N05/S02.
4. **Error boundaries differ.** Lua ErrorLog adds assertion behavior. Local loader false/stack restoration does not roll back effects. Luabind installs its own protected-call handler; no-exceptions fatal termination can precede outer catch. Binder catch clears its object with specific continuation results; panic returning zero does not undo LuaJIT exit. A02/S03/S05–S11/B03/N03.
5. **Crash artifacts are conditional.** Selected backend optionally invokes crash-save callback before diagnostics and terminates; selected Windows filter separately flushes, attempts a conditional dump and continues search. Dump availability and emitted status are not guaranteed. No crash-save success/atomicity or generic minidump-for-every-fatal guarantee. N03–N06.
6. **Triage separates symptom, emitter and cause.** Missing-event branches and unresolved effective helpers do not by themselves establish fatal behavior. Existing UI/clock external reports retain observation/inference/source axes. Recommended intake/competing hypotheses/minimal probes are design guidance; independent runtime work remains deferred. P01/P02/I01 and documentation D01–D06; [triage](../../06-debugging/triage.md).

## Competing explanations and missing edges

Absent output may be filtering, stack-ready suppression, failed/nonexistent flush, invalid writer, -nolog, truncation or a different alias. A last logged warning can precede another fatal route; filtered stacks can omit involved modules. A loader partial failure, repeat installer or missing dependency can cause later symptoms without the same recovery boundary.

Exact binary/compiler flags, installed logger/global printf/printe/callstack definitions, dispatcher/producer/emitter chains, symbols/raw dumps, crash-save callback body, filter replacement and active settings/resources remain profile-specific gaps. No blanket pcall/catch recovery, safe logger rate, measured overhead, memory corruption cause or all-version compatibility is inferred.

## Checks and outcomes

[Verification](../verification-2026-10-12-v0.1.80.md) records source/hash/range/scope reproduction, six documentation pins, retained prior evidence and dated bodies, repository validation, existing regression tests and publication blob checks. Semantic review separates logging from serialization, returned status from recovery, soft checks from fatal assertion, current from saved fault stack, and recommendations from runtime results. No engine compiled, game ran, save altered or third-party source/assets redistributed.

## Disposition and next work

DEBUG-01 selected routes and triage are complete within scope. [Debugging entry](../../06-debugging/README.md) now leads to the routes and triage; the [API](../../02-lua-api/debugging/diagnostic-api.md) certifies only four selected exports with original conditions. Existing local XML scope gains an additive link to the selected shared handlers; historical investigations/evidence stay preserved.

Next **ARCH-03 — qualified patterns/test guidance, practical architecture/debugging consolidation and bounded audit**. Effective-source collection and runtime resumption remain separate open work. The later cross-system final ADR audit is still separate. [Roadmap](../../ROADMAP.md).
