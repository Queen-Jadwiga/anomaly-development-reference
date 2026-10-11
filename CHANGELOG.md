## v0.1.22 — 2026-10-11 — UI-01a native tab state transitions
- Added source-backed `CUITabControl` selection/reset/event routing and `CUIPdaWnd` rebuild consequences, with explicit limits and runtime deferral.
- Only the tab-state research record and navigation/status files updated; other subjects unchanged.

## v0.1.10 — Part D (2026-10-09)
- Integrated Lua/XML/native UI construction, font lifecycle, and ownership evidence in `01-engine/ui-lua-native-integration.md`.
- Added source-backed architecture flowchart and cross-references.
- Consolidated open questions by priority, evidence requirements and runtime deferral in `08-research/open-questions-v0.1.10.md`.
- Added Part D research record; no claims of completed full-repository search or runtime verification.

## v0.1.7 — 2026-10-09 — XML/Lua interface boundary and font getter audit
- Separated native XML initializer signatures from verified Lua registrations.
- Added explicit unresolved Lua XML-wrapper inventory and research procedure.
- Cross-referenced 10 previously catalogued native font getters with XML tokens; flagged `arial_14` Lua getter as unverified.
- Added INV-007 and deferred runtime-check list. Examples remain minimal.

# Changelog

## v0.1.4 — 2026-10-09
- Resolved documented UI method parameters and return types from pinned C++ headers for CUIWindow, CUIScrollView, and CUIProgressBar.
- Documented output-reference and ownership hazards, scroll view initialization gap, and independently confirmed progress-bar color-binding mismatch.
- Added two tiny, explicitly non-standalone code sketches.
- Left remaining UI classes and runtime tests pending.

## v0.1.3 — 2026-10-09
- Extracted six source-confirmed Lua UI classes and machine-readable exported method inventory from pinned May 15 source.
- Recorded 10 engine font getter globals.
- Documented Luabind child ownership transfer and two suspicious ProgressBar color bindings.
- Separated symbol registration from unverified parameters and runtime behavior.

## v0.1.2 — 2026-10-09
- Identified official May 15, 2026 X-Ray Monolith release tag and short commit hash.
- Added explicit source-versus-installed-binary confidence assessment and reproducible pinning commands.
- Opened CUIProgressBar Lua export research entry based on May 15 release notes.
- Added post-May cutoff examples and investigation INV-003; no unverified Lua signatures asserted.



## v0.1.1 — 2026-10-09
- Populated environment/version and upstream repository references.
- Added architecture outline, preliminary Lua API index, PDA/font/widget research plans, and Warfare scope.
- Added evidence manifest and two open investigations.
- Explicitly separated engine-source research from runtime verification; no exact source commit claimed.

## v0.1 — Starter
- Initial directory skeleton and templates.

## v0.1.5 — Text and UI declaration audit
Expanded CUIStatic, CUITextWnd and CUILines native signatures; documented CGameFont pointer requirement and XML/font investigation boundaries. No runtime testing or new runnable examples.

## v0.1.6 — 2026-10-09 — Native XML and font resolver
- Documented 11 accepted XML font tokens and their native pointers with pinned source line links.
- Confirmed unknown-font and missing-font assertion paths in native UI text initialization.
- Mapped `InitWindow`, `InitStatic`, `InitTextWnd`, `InitText`, and `InitScrollView` with native XML attributes and defaults.
- Preserved source/runtime separation; no in-game test or standalone code examples.

## v0.1.8 — 2026-10-09 — XML export search / font lifecycle boundary
- Audited pinned `UIXmlInit.h` declaration against `UIXmlInit.cpp` call sites.
- Logged unsuccessful external registration lookup without converting non-findings into claims of absence.
- Traced source-confirmed XML text → font pointer resolution; explicitly flagged missing font-manager allocation and teardown trace.
- Added INV-008 and full-tree source search commands for next phase; no Lua examples added; runtime still deferred.

## v0.1.9 — 2026-10-09
- Added historically pinned XML initializer source map and a Mermaid call-flow diagram.
- Clarified the assertion is associated with a present text node whose font cannot be resolved, not an absent text node.
- Added reproducible commands for complete repository-wide Lua binding and font lifecycle audits.
- Full checkout unavailable; research remains partial. No claims of fully resolved registrations or lifecycle.

## v0.1.10 — Part A (2026-10-09)
- Identified source-confirmed `CScriptXmlInit::script_register` and the XML-to-native-UI bridge.
- Added registered-name inventory, selected header signatures, parent/child attachment behavior, and a call-flow diagram.
- Retained unresolved whole-repository negative search and startup registration path as explicit investigation questions.
- No runtime verification and no speculative examples.

## v0.1.10 — Part B (2026-10-09)
- Documented source-confirmed CGameFont constructors, glyph metrics loading, renderer initialization, OnRender, and destruction.
- Added object-level lifecycle diagram, source URLs, and separately tracked higher-level font manager unknowns.
- Preserved Part A findings and unresolved questions. No new Lua examples; runtime verification deferred.

- **v0.1.10 Part C:** Documented XML/UI widget creation, attachment, `AutoDelete` deletion, scroll-view initialization hazards, and unresolved Lua pointer ownership. Runtime verification deferred.

## v0.1.11 — A-01/A-02 research increment (2026-10-09)
- Added INV-014 with explicit registration bootstrap/negative-proof closure criteria.
- Added read-only repository audit tool `tools/audit_xml_lua_registrations.py`.
- Both A-01 and A-02 remain open pending full pinned source scan; no runtime verification.


## v0.1.12 — 2026-10-11 (focused update, no new A-02 claims)
- Adopted user-supplied October 11 C++ source ZIP as preferred source-research baseline; logged archive and compiled release hashes, with unverified runtime equivalence clearly distinguished.
- Resolved A-01 source-level call chain using full local repository (`CScriptEngine::init` → `export_classes` → `UIRegistrator` → `CScriptXmlInit::script_register`).
- Promoted A-01 to **source research complete / runtime validation pending**; left A-02 and other findings unchanged.
- Superseded earlier A-01 source-access blocked status without deleting historical reports. Added code locations and cautious remote-link provenance.

## v0.1.13 — 2026-10-11 — A-02 source research complete
- Exhaustively searched extracted October 11 source for independent `CUIXmlInit` registration; no matching native Luabind registration found.
- Confirmed separately exposed `CScriptXmlInit` wrapper and delegated native operations with exact code line references.
- Left runtime alias/global test pending; updated question register and index.

## v0.1.14 — 2026-10-11 — B-01 surgical insertion
- Added one source-verified investigation: `ui_core` owns `CFontManager`, which owns its named `CGameFont` pointers.
- Explicitly excluded other font owners and full UI startup/shutdown chronology (B-02). No runtime claims.

## v0.1.15 — B-02 (October 11 source)
- Source-verified application-start/UI-core/font-manager construction, teardown, and reset registration/reinitialization. Added `08-research/investigations/2026-10-11-B02-font-manager-lifecycle.md`. No runtime testing; no unrelated source conclusions changed.

## v0.1.16 — C-01 (October 11 source)
- Established focused source evidence for `CScriptXmlInit` child creation/attachment, native `CUIWindow` delete-on-detach contracts, and Lua `AttachChild` adoption policy. See `08-research/investigations/2026-10-11-C01-ui-ownership.md`. Runtime tests deferred.

## v0.1.17 — C-02 (October 11 source)
- Traced `CUIScrollView` pad, AddWindow/RemoveWindow/Clear deletion paths, layout recalculation, XML auto-delete setup, and Lua bindings. See `08-research/investigations/2026-10-11-C02-scrollview-ownership.md`; runtime deferred.

## v0.1.18 — C-03 (October 11 source)
- Traced bundled Luabind `adopt<2>()` ownership-flag transfer, userdata destructor/GC behavior, and its separation from UI `AutoDelete`. Documented scroll-view `AddWindow` binding risk and limits. Runtime validation deferred.

## v0.1.19 — C-04 (October 11 source)
- Verified ordinary `CScriptXmlInit` raw-pointer factory returns use Luabind non-owning pointer conversion; parented factories attach with native AutoDelete; parentless creation and InitHint require independent lifetime treatment. Tests deferred.

## v0.1.20 — October 11 UI source survey
Added four narrowly evidenced UI system records (dynamic PDA tabs, DXML hooks, input dispatch, native UI/font bindings). Nine explicitly open UI verification questions. No runtime claims; rest of ADR retained.

## v0.1.21 — 2026-10-11 — PDA subdialog lifecycle
- Source-traced native PDA tab rebuild, TAB_CHANGED dispatch, `SetActiveSubdialog`, and bundled dynamic-tab Lua wrapper.
- Open source questions retained for native tab-control state transitions and installed-addon conflicts; runtime tests deferred. See `03-ui-pda/pda-subdialog-lifecycle-oct11.md`.

## v0.1.23 — 2026-10-11 — UI-04 XML/DXML interception
- Traced `CXml::Load` native parse and `XMLLuaCallback` to `_G.COnXmlRead`, Lua `on_xml_read` dispatch, cache, filters and fallback paths.
- Added precise citations and explicit UI-04a/UI-04b source boundaries. No runtime claims; prior files preserved.

## v0.1.24 — 2026-10-11 — UI-04a
- Scoped source verification of CXml load overloads, LoadFromString bypass, CUIXml resolution-dependent file selection, include expansion, DXML filename identity, and distinct Lua openXMLFile path. See `03-ui-pda/xml-loading-paths-ui04a-oct11.md`. UI-04b remains open; runtime validation deferred.

## v0.1.25 — 2026-10-11 — UI-04b callback errors and ordering
- Added source-traced native XML callback failure boundaries, Lua protected parsing scope, module registration and callback ordering semantics. Runtime tests deferred.

## v0.1.26 — Oct 11 UI binding inventory
- Added scope-limited source extraction of 425 `.def` method-name occurrences across 16 files (CSV with exact locations); published UI class inventory and explicit unresolved event/context questions.
- No changes to prior research; no runtime claims.
- Added targeted native `CUIDialogWndEx` Register / AddCallback / SendMessage trace; event emission coverage remains open.

## v0.1.27 — 2026-10-11 — UI-06a/b/c/d source pass
- Added targeted audit of UI registrator contexts, selected exact Luabind signatures, event matching and overrides, build reachability limits, and keyboard/edit/dialog focus. See `03-ui-pda/ui06a-d-registrations-events-focus-oct11.md`. Exhaustiveness/build/modal questions remain open; no runtime claims.

## v0.1.28 — October 11 UI-06 supplementary pass
- Added one bounded source-evidence report and two reproducible source-derived CSVs; did not alter earlier conclusions.
- Confirmed direct event emitters, the specified project-file inputs, and dialog-holder input routing; preserved explicit global-completeness caveats.

## v0.1.29 — October 11 UI rendering/scaling/font/texture consolidation
- Added one scoped, source-backed reference for XML font validation, font-manager reinitialization, aspect-based XML resource resolution, and texture owner initialization.
- UI is development-reference ready for CtZ; deferred runtime tests and optional renderer/atlas deep dives remain explicit. Next subsystem: A-Life/Warfare. No unrelated source claims modified.

## v0.1.30 — October 11 source verification pass
- Checked local Markdown links and sampled source citations against uploaded October 11 source. Repaired three out-of-range line links; added clear current-baseline header to README; added [verification report](08-research/verification-2026-10-11-v0.1.30.md). Historical findings retained; no runtime promotion.
