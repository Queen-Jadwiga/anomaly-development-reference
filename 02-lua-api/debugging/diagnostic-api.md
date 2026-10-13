# Selected Lua diagnostic exports

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

- ID: DEBUG-01-API
- Subsystem: debugging
- C++ owner and Lua owner/name: CScriptEngine::script_register global exports, implemented by free wrappers in script_engine_script.cpp
- Interface kind: Lua export; native helpers/installed script aliases distinguished
- Exact signatures: log(text), error_log(text), print_stack(), flush(); no receiver or registered variadic/optional overload in selected registration
- Return/null/error/converter policy: void wrappers, no success result; selected LPCSTR matcher accepts a Lua string; error_log can terminate through assertion
- Native versus registered Lua inheritance: not applicable to these global functions
- Source baseline/provenance: ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit/executable equivalence unknown
- Source status: source-confirmed selected definitions/registration/default converter
- Runtime status: untested; deferred
- Build/conditional scope: MASTER_GOLD, DEBUG, USE_DEBUGGER/USE_LUA_STUDIO, LUA_DEBUG_PRINT, game script-log guards and selected assertion projection
- Evidence: A01–A04/S01–S04/B01–B06/N03 in [source ledger](../../evidence/debugging/diagnostic-routes-2026-10-12.csv)
- Dependencies/ownership/lifetime: initialized script engine/VM/logger/filesystem; effective Lua names may be replaced; text consumed synchronously, no ownership transfer
- State mutation/persistence/phase: logging buffer and optional secondary stream; flush output distinct from campaign save; error_log invokes diagnostic/assertion effects
- Known caveats: effective printf/printe/callstack globals, exact binary flags, crash-save callback body and installed replacements remain unverified
- Example status: none; no runnable probe or runtime-tested safety recipe
- Reproduction/check steps: compare pinned wrapper/registration/converter and conditional source hashes/ranges; no engine execution
- Last reviewed: 2026-10-12

## Exact selected contracts

| Lua export | Definition and registration | Result/effect | Important boundary |
| --- | --- | --- | --- |
| `log(text)` | LuaLog1(LPCSTR), script_engine_script.cpp:21–35,229–237 | Void; non-MASTER_GOLD uses script_log message with `%s`; MASTER_GOLD calls Log | Can be filtered/truncated; buffered output is not disk receipt; no native printf varargs export |
| `error_log(text)` | ErrorLog(LPCSTR), same file:37–57,229–237 | Void; direct error_log prefix, print_stack, then R_ASSERT2 | DEBUG skips assertion when debugger pointer exists; other selected branch enters assertion backend; not routine nonfatal logging |
| `print_stack()` | PrintStack(), same file:59–63,229–237 | Void; calls script engine print_stack | Current engine Lua state, build readiness/filter gates; does not promise every coroutine/native frame |
| `flush()` | FlushLogs(), same file:67–74,229–237 | Void; native FlushLog then conditional LUA_DEBUG_PRINT secondary flush_log | No acknowledged write/durability result; -nolog gates native file stage; does not serialize addon state |

A01–A03. The default const-char converter in `src/3rd party/luabind/detail/policy.hpp:553–556` matches Lua strings and applies lua_tostring; do not infer nil/default arguments, numeric overloads or a format/vararg list. Embedded NUL in a Lua string can terminate the native C-string traversal early; native Log uses xr_strlen and scans to zero. A04/L03. Registered signatures do not establish final installed name resolution after Lua patches.

## Native helpers and aliases remain separate

Native Msg(format,...) and CScriptStorage::script_log/error_log return/format signatures do not become extra overloads of global log/error_log. Native error_log's formatting body returns a character count and does not itself assert; the exported ErrorLog wrapper discards that result and adds stack/assertion behavior. S01/S04/A02.

`SetLogCB`, `LogStackTrace`, `Debug.fatal` and Windows dump/filter functions are native routes in this selected trace, not additional Lua exports certified here. Global `printf`, `printe`, `callstack` and effective `_G` aliases remain dependent on their actual winning definitions. The supplied printf_xrscript helper emits debug.traceback through log then calls printf; the supplied try helper uses ordinary pcall and returns only its captured first result/status fields. Their presence does not prove installed invocation or equivalence to print_stack/error_log. P01/P02, [loading/callback guide](../../04-game-systems/configuration/script-loading-startup-callbacks.md).

The console command named `flush` is another entry: it calls native FlushLog then unconditionally emits a success message. It does not call the Lua FlushLogs wrapper's optional secondary path or inspect write success. Console `clear_log` removes buffered evidence before flushing. L07. Scope-qualified controls and output paths are in [diagnostic routes](../../06-debugging/diagnostic-routes.md); [triage](../../06-debugging/triage.md) explains what to collect before proposing changes.

## Failure and use qualification

Keep messages short and bounded: even `%s` forwarding reaches fixed buffers with unbounded intermediate vsprintf in selected script/error helpers, followed by bounded native Msg. No general oversized-string safety or measured logger cost is established. S01/S04/L03/B05.

Lua pcall, loader lua_pcall, Luabind's installed error-handler call and an outer native binder catch are distinct boundaries. In the selected no-exceptions/NO_BUG_TRAP chain a handler can enter process termination before a caller sees an error result. This page does not certify pcall around error_log, native assertions or stale pointers as safe. [Route table](../../06-debugging/diagnostic-routes.md#error-handling-is-not-one-recovery-protocol), S06–S11/B03/N03.

DEBUG-01 certifies these selected source/export/converter contracts only. API availability and behavior in another executable/profile require its own evidence. Runtime remains deferred. [Evidence](../../evidence/debugging/README.md), [verification](../../08-research/verification-2026-10-12-v0.1.80.md).
