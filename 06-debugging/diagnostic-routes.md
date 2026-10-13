# Selected native and Lua diagnostic routes

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

- ID: DEBUG-01-ROUTES
- Subsystem: debugging / native-Lua integration
- Research revision: v0.1.80
- Record status: complete-within-scope for selected diagnostic chains; effective executable/profile partial
- Source status: source-confirmed selected ENGINE1011 paths; scoped build projection
- Runtime status: untested; deferred
- Baseline: ENGINE1011 archive SHA-256 `withheld-upload-fingerprint`; upstream commit/executable equivalence unknown
- Last reviewed: 2026-10-12

Read this before interpreting a crash log or adding a diagnostic call. [Lua API contracts](../02-lua-api/debugging/diagnostic-api.md), [triage guidance](triage.md), [investigation](../08-research/investigations/2026-10-12-DEBUG-01-diagnostic-routes-triage.md). Evidence IDs below belong to the [41-row source ledger](../evidence/debugging/diagnostic-routes-2026-10-12.csv), pinning 67 range groups across 21 files. Source paths/ranges and conditions remain authoritative; no compiled engine or game was run.

## Message, memory buffer and disk are different stages

| Stage | Selected source contract | Diagnostic implication |
| --- | --- | --- |
| Native `Msg(format, ...)` | Formats through `_vsnprintf` into 2048 bytes, forces final NUL and calls Log when result is nonzero | Long output can be truncated; zero-length output can be omitted; no success result |
| Native `Log(text)` | Allocates a split buffer on the stack, splits on newline and always sends the final fragment | Multiple lines are separate entries; trailing newline adds a final empty fragment |
| `AddOne` | Under log lock: optional timestamp, adjacent identical-entry compression, then synchronous callback with original split text | Buffer and callback text can differ; callback receives each emission even when buffer compresses it |
| `LogFile` | Vector reserves 10,000 entries at initialization; no bound/eviction policy in selected logger | Reserve is capacity preparation, not a log-size cap |
| `FlushLog` | If logging enabled, opens writer and writes every buffered entry; closes writer under the lock; returns void | Emission is not disk completion; flush does not return a persistence receipt |
| File writer | `w_open` constructs nonexclusive CFileWriter; opens `wb`, closes via fclose | Flush rewrites/truncates rather than appending; no atomic replacement or filesystem-durability guarantee |

L01–L06 (`src/xrCore/log.cpp`, `LocatorAPI.cpp`, `FS_internal.h`). The ordinary game `w_open` only deletes an invalid writer under `_EDITOR`; a failed fopen can leave a non-null writer whose writes do nothing. Valid writes assert on failed fwrite. The logger's `if (f)` is therefore not a universal successful-open/write check. No safe behavior is certified for recursive failure during logging or every I/O error. L05/L06.

`AddOne` timestamps use local wall-clock `system_clock` time formatted as hours/minutes/seconds/milliseconds, preserve a recognized leading console mark, and compare the **timestamped** text for compression. Identical consecutive entries replace the preceding buffered row with a count suffix. Timestamp changes can prevent compression; different entries break the run. Callback text remains the original split, without the timestamp/count decoration. `SetLogCB` replaces a single native slot and returns the previous callback; it is not a Lua listener registry. The split pointer is transient: copying needed data during the call is a design obligation for a retaining native consumer. L02/L04.

`CreateLog` sets no_log, derives an application/user filename, resolves `$logs$` if available, renames the existing log to `.bkp`, and opens/closes a new writer when enabled. The path buffer initially names engine.log; installed path resolution is not inferred. `CLocatorAPI` calls CreateLog with the `-nolog` substring test and CloseLog during destruction. CloseLog flushes then clears the memory buffer. `-nolog` gates file creation/flush here; it does not prevent AddOne buffering or callback execution. L01/L04/L05.

Console `flush` calls void FlushLog **before** logging its success message. That message does not inspect a result and is not itself written by the just-finished flush. `clear_log` clears the buffer, flushes, then logs its own message; it destroys preceding buffered evidence. The selected clear operation does not reset AddOne's static duplicate-history fields. Do not infer a fully reset logger from its name. L02/L07. No clear command is recommended as a crash-intake step.

## Qualify logging and debugging flags separately

| Control/build condition | Selected role | Keep separate |
| --- | --- | --- |
| `MASTER_GOLD` | Lua log uses direct native Log instead of script_log | Other error/stack routes do not all bypass their guards |
| `-dbg` substring | Non-DEBUG game script_log gate; loader compile/runtime report gate | Can also match `-dbgdev`; not an exact-token parser or a universal error-recovery switch |
| DEBUG / aiLua / LUA_DEBUG_PRINT | Message filtering, stack-ready suppression and optional secondary output stream | Exact project flags and effective console state; not every build emits `_lua.log` |
| `-dbgdev` substring | Startup sets ignore_verify false when found | Affects soft verification output; does not convert soft_fail into fatal handling |
| `USE_VERIFY_IN_RELEASE` | Release VERIFY executes soft checks when defined; otherwise expressions are omitted | Commented in common header but enabled by selected Verified project configurations |
| `NON_FATAL_VERIFY` | DEBUG VERIFY takes soft_fail in this header | R_ASSERT and FATAL retain different routes |
| `-no_call_stack_assert` / native debugger | Gate stack gathering inside gather_info | Selected NO_BUG_TRAP UnhandledFilter does not use that same guard |
| DEBUG `-break_on_assert` | print_output's guard may assert on an error | Non-DEBUG branch fixes this setting false locally |
| `lua_debug` | Read during VM reconstruction; initializes selected globals/socket/Panda route | Not the script_log `-dbg` gate or instantaneous general verbose logging |
| `lua_busy_hands_debug` | Conditional diagnostic hook from a separate error-not-crash callback | No global guarantee of nonfatal errors or rollback |

A01–A03/B01–B06/S01–S07/S12–S15. Header `NO_BUG_TRAP`/`USE_OWN_MINI_DUMP` and the project source selection motivate the selected native projection. `xrCore.vcxproj` excludes the older xrDebug.cpp in five listed x64 configurations and includes xrDebugNew.cpp. The older file's mere presence is not a second active implementation. Exact final compiler definitions and binary correspondence remain unknown. B01/B02.

Script logging prefixes info/message/error separately. `vscript_log` formats with unbounded vsprintf into a fixed 4096-byte array, then uses native Msg; error_log has a similar fixed buffer, and fatal uses unbounded vsprintf into 1024 bytes. Passing a Lua string through `%s` avoids treating its percent signs as format directives at that wrapper boundary, but does not remove those size limits or certify arbitrary oversized inputs. Recommended probes are short, bounded summaries; no safe throughput/overhead threshold was measured. A01/A02/S01/S04/B05.

## Stack output is a scoped observation

`print_stack` inspects the script engine's current `lua()` state, obtains frame name/source/line metadata and emits through script_log_no_stack. In DEBUG it returns if m_stack_is_ready is false, then clears that flag before printing; init/hook paths can set it again. Error script_log has a local reentry guard to avoid its own repeated stack recursion. Log filtering still applies. This is not a dump of every coroutine, all native frames or a retained historical trace. S02/S12.

`LogStackTrace` requires initialized shared strings, invokes the Lua stack bridge, then uses StackWalker ShowCallstack for the current native call chain. The custom output filter discards lines containing dll/drv names, selected CRT startup text, missing symbol/filename/function messages and selected symbol lookup failures. A missing module/frame is therefore not proof it was uninvolved. This is distinct from passing a saved exception CONTEXT to a walker; the selected UnhandledFilter's old context-walk code is commented out. N01/N05.

`gather_info` formats expression/function/file/line/description/arguments into a bounded assertion buffer. It emits a log form, rewrites a dialog/clipboard form, and conditionally gathers stacks when no debugger and no `-no_call_stack_assert` substring are present. Native source file/line usually identifies the reporting assertion, not necessarily the earlier cause. Logs and clipboard/dialog text are different artifacts, and truncation/filtering/guards can affect them differently. N02, B04. Anonymous-build macros can suppress file/function/expression text.

## Error handling is not one recovery protocol

| Route | Selected outcome/boundary | What must not be inferred |
| --- | --- | --- |
| `soft_fail` | Only logs VERIFY_FAILED when ignore_verify=false; no explicit throw/termination in body | Failed invariant was repaired, or silent execution passed every check |
| R_ASSERT / FATAL, selected NO_BUG_TRAP backend | Conditional crash-save callback runs first; diagnostics/handler/flush/dialog then TerminateProcess | Lua pcall or an outer C++ catch can recover from process termination |
| Lua `error_log(text)` | Direct error prefix and stack, then R_ASSERT2 except selected DEBUG debugger-presence condition | Ordinary nonfatal severity logging |
| Loader compile/main-chunk failure | Conditional print_output/on_error, false locally; relevant stack restoration | Earlier assignments/native effects were rolled back or caller received success/failure |
| Luabind C++ protected call | Inserts configured pcall handler; selected no-exceptions handler reports then enters Debug.fatal | Every “protected call” shares plain Lua pcall's outcome |
| Exception-enabled Luabind path | Selected error path throws; binder methods can catch/clear | Clearing a binder reverses gameplay effects or every earlier handler returns |
| Lua panic | Callback prints/returns 0; LuaJIT no-frame/failed-unwind routes call panic then exit | Panic callback returning zero resumes successful execution |
| Unhandled Windows exception | Selected filter logs current stack/last-error/address, flushes, conditionally attempts dump and returns CONTINUE_SEARCH | It repairs/resumes the fault or every crash produces a usable dump |

B04/B05/N03/N05/S03/S05–S11/A02. Ordinary Lua pcall used by a supplied helper is a distinct route from `luabind::detail::pcall`, which installs the engine callback as lua_pcall's error handler. The selected functor failure path then throws with exceptions or invokes the configured error callback without exceptions. Catch blocks after a terminating handler are not a recoverability guarantee. S06–S09/P01. Protected execution also cannot reverse external side effects.

In the exception-enabled projection, lua_pcall_failed removes a string error object when present and returns the literal LUA_ERRRUN from its handler body. That is not a successful operation receipt for the outer caller; this pass does not certify the complete error-handler stack/payload contract across every VM/build branch. S06/S08.

Binder save/load catches clear the binder; net_Spawn falls through to TRUE after its catch, while net_SaveRelevant falls through to FALSE. These are specific native continuation results, not addon save/spawn success receipts. Actual compiler exception mode still qualifies which path can be reached. S11/B03.

Selected UnhandledFilter's textual Windows error uses GetLastError, while ExceptionRecord separately supplies an address. They are not the same datum; the formatted last error is not a decoded ExceptionCode/cause. Its StackWalker uses the current handler stack. The filter is installed by the selected initialization route, but another filter or failure before initialization can change coverage. N05/N06/B06.

The conditional dump code locates DBGHELP/MiniDumpWriteDump, constructs an application/user/timestamp `.mdmp` name, attempts logs/fallback paths, and requests MiniDumpNormal/FilterMemory/ScanMemory. Missing DLL/function/file or write failure remains possible. The local szResult strings are not emitted/returned by this body. The filter flushes **before** attempting the dump. Assertions entering the selected terminating backend do not themselves call this filter/dump function. Thus neither “crash occurred” nor “minidumps enabled in source” proves a dump exists or that a later dump status reached the log. N03–N05. Dumps/raw paths remain private diagnostic artifacts by default.

## Reuse local subsystem findings without widening them

[CONFIG-03](../04-game-systems/configuration/script-loading-startup-callbacks.md) retains partial-execution/module-table/startup/dispatch contracts. Its missing effective globals mean supplied `printf`, `printe`, `callstack` and their aliases cannot be equated to the four native exports solely from names. The selected axr_main rejection branches print/callstack and return; this does not by itself establish fatal termination in an installed profile. P01/P02 and [triage reference D02](../evidence/debugging/triage-references-2026-10-12.csv).

[XML/DXML local error findings](../03-ui-pda/xml-dxml-callback-errors-ui04b-oct11.md) remain local: protected parse/construction differs from unprotected callback/serialization and native XML assertions. DEBUG-01 now qualifies the selected shared Luabind/assertion handlers; it does not close every effective XML caller/addon chain. D01/S06–S09/B04/N03. [External UI/clock reports](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md) retain reported build/provenance and inferred-mechanism labels; no new independent reproduction occurs. D03.

Completion: selected logging/export/stack/assertion/loader/Luabind/binder/panic/unhandled/dump boundaries close within this scope. Every native crash, symbol implementation, debugger/renderer/profiler internals and installed aliases remain outside the pass. [Triage](triage.md), [verification](../08-research/verification-2026-10-12-v0.1.80.md), [roadmap](../ROADMAP.md). Next ARCH-03; runtime deferred.

## Subsequent practical consolidation

ARCH-03 [central reference](../05-mod-architecture/development-reference.md), [patterns](../07-code-library/qualified-patterns.md), [test guidance](../05-mod-architecture/test-guidance.md) and [bounded audit](../08-research/verification-2026-10-12-v0.1.81.md) now complete the selected practical foundation. DEBUG-01's original scope/next allocation above remains research history; effective aliases/build/profile and runtime limits remain unchanged. Next separate whole-ADR audit.
