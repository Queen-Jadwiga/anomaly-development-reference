# ADR roadmap

## v0.1.1 — Research baseline (this revision)
- [x] Record runtime engine version from existing logs
- [x] Document authoritative upstream repository and MT branch context
- [x] Define UI/PDA and Warfare investigation targets
- [x] Create provenance and evidence records
- [ ] Identify exact May 15, 2026 source commit
- [ ] Extract font crash trace, root cause and tested solution
- [ ] Build source-backed Lua export inventory
- [ ] Inspect actual GAMMA Warfare scripts

## v0.2 — Source-backed interface catalog
- Pin commit and add path/line citations
- Document C++ -> Lua binding patterns and verified widget APIs
- Trace PDA construction and font registration
- Prototype static validators

## v0.3 — Runtime checks
- Run minimal Lua/UI tests on installed GAMMA
- Mark applicable APIs runtime-verified
- Document relevant mod conflicts and regression tests

## After v0.1.4
- Next: CUIStatic/CUITextWnd/CUILines declaration audit; XML initialization chain; font lifetimes.
- Later: runtime smoke tests on GAMMA MT-TEST 2026.05.15.

## After v0.1.5
- Trace CUIXmlInit and font getter registrations; resolve exact XML widget initialization.
- Audit events/callbacks followed by Warfare/A-Life APIs.
- Verify source findings against the installed May 2026 executable when available.

## After v0.1.6
- Trace script registration for XML initialization interfaces and the native font manager.
- Build conservative static XML validation (no unverified Lua UI examples).
- Compare CtZ crash traces and exact effective UI XML once provided. Runtime tests deferred at user request.


### Following v0.1.7
- Find complete pinned-source Lua registration sites for `CUIXmlInit` / `CUIXml` and game-side XML wrappers.
- Trace font manager initialization lifecycle and explicit global-getter binding sites.
- After these, move to callbacks and Warfare/A-Life interfaces. Runtime tests remain deferred.

### v0.1.8 follow-up
- [ ] Obtain full pinned source checkout, verify historical Lua XML registration across repository.
- [ ] Trace global font getter bindings and UI manager font creation/destruction to startup/shutdown.
- [ ] Only then expand callback/A-Life/Warfare catalog.

## v0.1.9 outstanding
- Obtain full pinned checkout; enumerate all source files and Lua registration sites.
- Establish font manager allocation and teardown from complete native call graph.
- Only after closing these items begin callback/A-Life extraction; runtime testing deferred.

## v0.1.10 audit status
- Part A — Lua registration: targeted source findings recorded; registration aggregator and whole-repository absence checks remain open.
- Part B — Native font lifecycle: pending.
- Part C — XML/UI construction and ownership: pending.
- Part D — Integration/cross-reference synthesis: pending.

## v0.1.10 remaining
- Part C: XML/UI construction and ownership.
- Part D: Integrate A–C.
- Font manager startup/shutdown and Lua getter ownership remain open until verified from further source.


### v0.1.10 Part C completed
- Native XML factory and parent-child deletion traced from pinned source.
- Part D next: synthesize A–C.
- **After Part D: review and prioritize all unresolved questions from Parts A, B and C.**

### v0.1.10 Part D completed — consolidated review checkpoint
- [x] Merge Parts A–C in one source-grounded integration diagram and cross-linked narrative.
- [x] Create prioritized, deduplicated open-question register.
- [ ] Source audit: A-01/A-02, B-01/B-02, C-01/C-02; see `08-research/open-questions-v0.1.10.md`.
- [ ] Runtime checks (user postponed): R-01 through R-05.
- Next planned technical subject after source gaps: callbacks, then A-Life and Warfare.

### v0.1.11 — Registration bootstrap follow-up
A-01 and A-02 remain open. Run `tools/audit_xml_lua_registrations.py` on pinned full Git source, trace startup callers and inspect aliases/indirect registration. Runtime checks remain deferred.

## v0.1.13 — A-02 research status
- [x] Inspect entire October 11 extracted source for separate `CUIXmlInit` Lua registration and aliases.
- [x] Document Lua wrapper exports and limitations.
- [ ] Optional in-game global-presence smoke test on October 11 binary.
- Next focused item: B-01, font manager ownership; source research first.

## v0.1.14 — B-01
- [x] Source-verify `ui_core` → `CFontManager` → named `CGameFont` ownership.
- [ ] B-02: full manager startup/shutdown call chronology and device-reset interactions.
- [ ] Runtime validation deferred by request.

## v0.1.15 — B-02
- [x] Source trace of client UI font construction, app teardown, and device-reset behavior.
- [ ] Runtime validation deferred. Next research question to select separately; do not equate B-02 source completion with diagnosis of the historical CtZ font crash.

## v0.1.16 — C-01
- [x] Narrow source-level UI creation, parent-child ownership, and Lua `adopt<2>()` contract.
- [ ] Runtime validation deferred. Inspect scroll-view-specific ownership and userdata lifetime as independent follow-up questions.

## v0.1.17 — C-02
- [x] Identify internal scroll pad, AddWindow/RemoveWindow/Clear native deletion rules and Lua exports from October 11 source.
- [ ] Lua userdata lifetime / adoption semantics remain separate; runtime testing deferred.

## v0.1.18 — C-03
- [x] Trace adoption policy, Luabind GC owner flag, native AutoDelete, and explicit `AddWindow` registration.
- [ ] XML factory return conversions and Lua alias lifetime remain a separate source audit; runtime testing deferred.

## v0.1.19 — C-04
- [x] Trace ordinary XML-created controls from native allocation through return conversion and parent deletion.
- [ ] Complete remaining UI topics in a broader UI-system audit (event handling, PDA tabs, DXML, typography, rendering and UI version deltas), then move to other game systems. Runtime validation deferred.

## UI subsystem review — v0.1.20
- [x] Survey native dynamic PDA tab registry, Lua exports, DXML hooks and selected input paths.
- [ ] Finish UI-01/03/04/06/08 source questions (see open questions).
- [ ] Defer UI-02/05/07/09 runtime tests until user can test.
- [ ] Only after completing remaining source questions, move to next game system.

## v0.1.21 UI-01
- [x] Trace PDA dynamic-tab rebuild, show/selection and Lua subdialog forwarding.
- [ ] UI-01a source: native tab-control removal/reset event emission.
- [ ] UI-01b source: GAMMA PDA addon wrapper interplay, requires installed addon files.
- [ ] Remaining UI-03/04/06/08 source investigations; runtime deferred.

## v0.1.22 — UI-01a
- [x] Establish `ResetTab`, `SetActiveTab`, `OnTabChange` and accelerator-mode event behavior from October 11 source.
- [x] Cross-reference `RemoveDynamicTabs` and `CUIPdaWnd::RebuildExtraTabs` with tab/subdialog synchronization.
- [ ] Next source pass: DXML interception / XML patch lifecycle; later full Lua widget/event inventory and rendering contracts.
- [ ] Runtime PDA wrapper and selection checks deferred.

## v0.1.23 — UI-04 XML/DXML
- [x] Trace `CXml::Load` → `XMLLuaCallback` → `_G.COnXmlRead` → `on_xml_read` → optional cache.
- [ ] UI-04a: enumerate bypass readers and filename normalization. UI-04b: callback exception paths / external wrapper order.
- [ ] Next main UI topics: full Lua widget/event inventory, then rendering and scaling. Runtime tests deferred.

## v0.1.24 — UI-04a
- [x] Source-trace `CXml::Load` overloads, `LoadFromString`, UI filename variant remapping, include assembly, DXML hook filename, and separate `openXMLFile` path.
- [ ] UI-04b: native callback error/functor propagation and Lua hook registration/wrapper behavior.
- [ ] UI-05: GAMMA runtime patch-path, cache, and multi-addon checks (deferred).

## v0.1.25 — UI-04b
- [x] Inspect native XML callback error boundaries, DXML protected parser stages, `modxml_` registration, and callback priority/constraint behavior.
- [ ] UI-05 runtime interaction/conflict tests remain deferred. Next UI source topic: comprehensive Lua widget/event exports.

## v0.1.26 UI-06 inventory
- [x] Build source-location index of named `.def` bindings across scoped UI registrators.
- [ ] UI-06a/b/c/d: event delivery and exact contexts/signatures and supplementary registrations.
- [ ] Native typography/rendering/scaling study; runtime validation remains deferred.

## v0.1.27 — UI-06a through UI-06d
- [x] Source-trace selected registration contexts/signatures, event comparer, Lua virtual forwarding, keyboard capture, edit focus, and dialog gating.
- [ ] UI-06a-EXH: exhaustive registration/overload inventory beyond scoped 425-name CSV.
- [ ] UI-06b-EMIT: comprehensive per-widget event emission map.
- [ ] UI-06c-BUILD: build/link/conditional reachability audit.
- [ ] UI-06d-MODAL: modal dialog-stack/global-hotkey interplay.
- [ ] Rendering/scaling/texture/font pass; runtime verification deferred.

## v0.1.28 — UI-06 supplementary pass
- [x] Source audit of scoped binding occurrences, five event-emitting controls, two Visual Studio project files, and dialog holder input routing.
- [ ] Source-open: global exhaustive exports/overloads, all widgets and inherited emitters, all configuration/build paths, non-holder/global addon input.
- [ ] Next UI focus: fonts, rendering, scaling, textures, then subsystem consolidation. Runtime tests deferred.

## v0.1.29 — UI subsystem handoff
- [x] Document CtZ-relevant rendering, XML font, texture and aspect-ratio paths from October 11 source.
- [x] Move UI to **development-reference ready / runtime pending**; retain low-priority exhaustive source gaps.
- [ ] Next source investigation: A-Life/Warfare — start with smart-terrain/squad identity, spawning, assignment, and offline-to-online ownership boundaries.
- [ ] Test UI behavior, assets and compatibility in the target GAMMA runtime when available.

## v0.1.30 verification checkpoint
- UI source documentation checked against October 11 snapshot for citation integrity and key mechanisms; see `08-research/verification-2026-10-11-v0.1.30.md`. Runtime tests deferred. Next source focus remains A-Life/Warfare.
