# Verification — 2026-10-12 — ADR v0.1.80

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

- Target ADR revision: v0.1.80, based on main `2db0cc343662140d3670eec16ea247e75b00279b`
- Changed scope: DEBUG-01 selected native/Lua diagnostic routes and triage
- Source baseline IDs: ENGINE1011 uploaded archive; six ADR v0.1.79 documentation pins; original evidence confidence retained
- Last reviewed: 2026-10-12

## Checks performed

Check all 41 source rows/67 inclusive range groups/21 files for raw full-file SHA-256, line count/range integrity and agreement with the diagnostic scope record. Rebuild the two CSV ledgers and scope JSON from the selected inputs and compare exact bytes. Check six documentation pins at immutable v0.1.79; preserve earlier evidence/history/generated/tool/test artifacts and dated investigation bodies under the banner rule.

Focused review covers registered four-export arity/default string matcher, logger buffer versus disk/invalid writer, script gates and buffer sizes, project/header/exception projection, installed Luabind pcall handler versus ordinary pcall, binder fallback/clear and LuaJIT panic exit, current/filtered stack versus saved context, assertion/soft failure and unhandled/dump output limits. Existing XML local findings gain a selected shared-handler link without exhaustive closure. Triage recommendations and external reports retain their separate evidence labels.

## Results and corrections

All **41 source rows/67 ranges/21 files** and **six documentation pins** pass; the two CSV ledgers and scope JSON rebuild byte-identically. **70 prior evidence/history/generated/tool/test artifacts** remain byte-identical; **73 dated investigation bodies** change only revision banners. Repository validation passes: **299 Markdown files, 2,629 local targets, 37 anchors, zero errors**. All **10 existing regression tests** pass. No extractor behavior or source-tool test implementation is changed. No native compilation, game/profile execution, save migration or measured diagnostic/profiler overhead occurs.

## Publication verification

Verify the complete remote base/staged/published path/blob maps, expected-head fast-forward update and final main commit. The resulting commit is supplied by Git history; no self-referential hash is fabricated.

## Remaining limitations

Selected source/build projection only. Actual executable/compiler flags, installed printf/printe/callstack/global/dispatcher/binder/winner routes, symbols/dumps and crash-save callback body remain qualified/missing. No every-crash minidump, universal pcall/catch recovery, safe logger throughput, diagnosed incident or tested fix. Runtime deferred; next ARCH-03, later whole-ADR audit separate. No CtZ gameplay or third-party source/assets changes.
