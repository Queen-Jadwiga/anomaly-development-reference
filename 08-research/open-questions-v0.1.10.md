# Open questions — consolidated review after Parts A–D

> ADR document set: **v0.1.72**. Research revisions and source/build versions below describe their original scope.

**Snapshot:** ADR v0.1.10 Part D, 2026-10-09. **Historical snapshot; see October 11 amendments for current statuses.** Runtime work postponed by user. Prior individual investigation files remain authoritative for context.

## Highest priority: address with source inspection

| ID | Priority | Question | Proposed method | Completion evidence |
|---|---|---|---|---|
| A-01 | P1 | Which engine startup registration aggregator invokes `CScriptXmlInit::script_register`? | Full pinned source `git grep` + callers | Committed source path, line, call graph to Lua VM initialization |
| A-02 | P1 | Is `CUIXmlInit` *separately* exposed to Lua? | Repository-wide search of all registration definitions; inventory search coverage | Whole-tree inspected set, results, any registration paths; no false absence claim |
| B-01 | P1 | Which UI manager owns the named `CGameFont` pointers? | Trace `UI().Font()` getters and class members | Manager type, file/line references, pointer ownership |
| B-02 | P1 | When are fonts created/configured and destroyed? | Trace calls from engine initialization/shutdown, manager ctor/dtor | Start-to-end call graph with source citations |
| C-01 | P1 | What Luabind return-ownership policy applies to `CScriptXmlInit` widget factories, including parentless widgets? | Audit registration return policies and Luabind converters | Source-backed table of return policy and destruction owner |
| C-02 | P1 | What does each XML factory do when a required node is absent/malformed? | Trace native initializer per widget and assertion branches | Per-widget source-backed error/return table |

## Secondary source questions

| ID | Priority | Question | Method |
|---|---|---|---|
| A-03 | P2 | Exactly which parser entry paths invoke `_G.COnXmlRead`, and what happens on callback error? | Exhaustive call-site and exception-flow tracing |
| B-03 | P2 | How do fonts behave during renderer reset, resolution change, or localization change? | Follow recreation/reload signals and manager functions |
| B-04 | P2 | What lifetime guarantees apply to Lua font-getter pointers? | Getter registration plus manager reset and owner trace |
| C-03 | P2 | `CUIScrollView::RemoveWindow` vs `Clear`: when is a child deleted? | Native source trace incl. internal pad and auto-delete flags |
| C-04 | P2 | Are reparented children safe and under what contracts? | Full native / Luabind lifetime analysis; cautious until runtime checks |
| I-01 | P2 | Are all current ADR source links and Lua method signatures consistent? | Mechanically validate cross-links and reconcile against pinned source |

## Deferred to user's PC / binary inspection

| ID | Priority | Question | Evidence required |
|---|---|---|---|
| R-01 | Deferred | Does installed MT-TEST 2026.05.15 exactly match the official released code? | Binary hashes/build provenance or controlled comparison |
| R-02 | Deferred | Does any GAMMA-specific binary/script patch change these paths? | Effective load order, patches, scripts, in-game log |
| R-03 | Deferred | Which actual font failure caused Capture the Zone's crash? | Original crash trace + exact active Lua/XML + minimal reproduction |
| R-04 | Deferred | Are the documented UI calls and object lifetime behavior safe in-game? | Minimal reproducible script tests, logs and version info |
| R-05 | Deferred | Is source-observed `CUIProgressBar` color registration mismatch present in the installed executable? | Runtime controlled test or exact binary correspondence |

## Important resolved question

- **A-00 CLOSED (source level):** There is a Lua-facing XML initializer defined as `CScriptXmlInit` which delegates to native `CUIXmlInit`. [ScriptXMLInit.cpp registration](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ScriptXMLInit.cpp#L337-L384). **This does not close A-01 or A-02.**

## Next recommended sequence

1. Obtain a complete checkout of pinned May 15 source (or exhaustive registration-source inventory), close **A-01 / A-02**.
2. Trace font ownership **B-01 / B-02**, before making lifecycle guarantees.
3. Review factory pointer policies and XML errors **C-01 / C-02**.
4. Then begin callbacks and A-Life/Warfare source audit; runtime remains a separate phase.

Do not substitute absence in a single inspected file for a repository-wide negative conclusion.

## Follow-up: v0.1.11 A-01/A-02 audit

Both questions remain **OPEN** after targeted source inspection. See [INV-014](investigations/2026-10-09-A01-A02-registration-bootstrap.md). A reproducible read-only scanner is available at `tools/audit_xml_lua_registrations.py`. No whole-repository absence claim or invocation trace has been asserted.


## 2026-10-11 superseding status amendment (ADR v0.1.12)

- **A-01 — SOURCE RESEARCH COMPLETE / RUNTIME VALIDATION PENDING.** The October 11 local source has the full dispatcher-to-class chain. See [A-01 closure](investigations/2026-10-11-A01-source-registration-closure.md). Earlier A-01 OPEN text and the v0.1.11 source-access blocker are historical, not the current status.
- **A-02 — OPEN.** No exhaustive source conclusion about separate `CUIXmlInit` Lua exposure is recorded. Next focused investigation.
- **May 15-specific A-01 — not separately closed against May source.** The October 11 chain should not be automatically ascribed to it.
- Other open issues retain prior statuses until separately investigated.

## 2026-10-11 A-02 amendment (ADR v0.1.13)

- **A-02 — SOURCE RESEARCH COMPLETE; runtime smoke test pending.** Complete October 11 extracted-source audit finds no independent `CUIXmlInit` Luabind registration, but confirms `CScriptXmlInit` as Lua-facing wrapper. See [A-02 audit](investigations/2026-10-11-A02-native-xml-lua-exposure.md). Earlier OPEN entries retained as history. No runtime test was performed.

## 2026-10-11 — B-01 status amendment (ADR v0.1.14)
- **B-01: Source research complete**, strictly for client UI core/manager/named-font pointer ownership. Evidence: [B-01 record](investigations/2026-10-11-B01-font-manager-ownership.md).
- **B-02 remains open** for broader initialization chronology and reset handling; runtime tests all deferred. Historical open-question entries above are preserved as history.

## 2026-10-11 — B-02 status amendment (ADR v0.1.15)
- **B-02 SOURCE RESEARCH COMPLETE:** client `CGamePersistent::OnAppStart` → `ui_core` → `CFontManager` → named `CGameFont` creation; `OnAppEnd` reverse teardown; manager registered at `REG_PRIORITY_HIGH` for device reset and reinitializes existing fonts. See [B-02 research](investigations/2026-10-11-B02-font-manager-lifecycle.md). Runtime checks deferred. Earlier OPEN entries are historical.

## 2026-10-11 — C-01 status amendment (v0.1.16)
- **C-01 SOURCE RESEARCH COMPLETE:** XML factory parent attachment and auto-delete behavior, `CUIWindow` destructor/DetachChild, and Lua `AttachChild` `adopt<2>()` documented. See [C-01](investigations/2026-10-11-C01-ui-ownership.md). Runtime checks deferred; do not infer generic Lua userdata lifetime safety. Older OPEN records are historical.

## 2026-10-11 — C-02 status amendment (v0.1.17)
- **C-02 SOURCE RESEARCH COMPLETE:** native scroll-view child container, auto-delete behavior, explicit Lua bindings recorded in [C-02](investigations/2026-10-11-C02-scrollview-ownership.md). Uninitialized pad and Lua GC behavior not generalized; runtime checks deferred. Earlier open records are historical.

## 2026-10-11 — C-03 status amendment (v0.1.18)
- **C-03 SOURCE RESEARCH COMPLETE (bounded):** `adopt<2>()` removes Luabind ownership for eligible Lua-owned child userdata; native `AutoDelete` is independent. `CUIScrollView::AddWindow` binds without explicit adoption. [C-03 record](investigations/2026-10-11-C03-luabind-adoption-autodelete.md). Return converter and alias handling remain unverified; tests deferred.

## 2026-10-11 — C-04 status amendment (v0.1.19)
- **C-04 SOURCE RESEARCH COMPLETE (bounded):** Ordinary `CScriptXmlInit` return pointers default to non-owning Luabind userdata, and parent attachment enables native AutoDelete. Parentless factories, special-case InitHint, and alias invalidation are not inferred safe. [C-04 evidence](investigations/2026-10-11-C04-xml-factory-return-ownership.md). Tests deferred.

## October 11 — UI subsystem broad source survey (v0.1.20)
The new records document proven dynamic PDA registration, DXML patch flow, native input routing and select UI exports. **UI subsection remains open**, and no runtime verification was performed.
- UI-01 SOURCE: subdialog/tab restore and competing wrappers.
- UI-02 RUNTIME: tab add/remove, caption, icon, scroll and addon compatibility.
- UI-03 SOURCE: static XML tabs / PDA reskin interplay.
- UI-04 SOURCE: native XML-read interception boundaries.
- UI-05 RUNTIME: concurrent DXML patch order/caching and GAMMA load.
- UI-06 SOURCE: precise Lua widget event/edit/focus APIs.
- UI-07 RUNTIME: keyboard focus, search, reopen and scroll behavior.
- UI-08 SOURCE: full UI export inventory, rendering, texture/font scaling.
- UI-09 RUNTIME: fonts, resolution, resets and lifetime stress.
See linked records in `03-ui-pda/`. Do not mark UI source research complete yet.

## UI-01 amendment — v0.1.21
- Native PDA rebuild + selected subdialog path verified in October 11 source; see `03-ui-pda/pda-subdialog-lifecycle-oct11.md`.
- Open UI-01a (tab control event transitions) and UI-01b (external addon wrapper conflicts). UI-02 remains runtime pending.

## v0.1.23 — UI-04 amendment
- **UI-04 SOURCE-RESEARCH COMPLETE for `CXml::Load` path:** The native-to-Lua callback and bundled DXML transformation/cache chain are traced in `03-ui-pda/xml-dxml-native-lifecycle-oct11.md`.
- **UI-04a / UI-04b remain OPEN SOURCE:** other XML entry points, filename normalization and exceptions, and callback errors / external mod registration order. No universal interception claim.
- **UI-05 RUNTIME pending** as before.

## v0.1.25 — UI-04b current amendment
- **UI-04b SOURCE COMPLETE** for October 11 examined native and bundled Lua code. See [`xml-dxml-callback-errors-ui04b-oct11.md`](../03-ui-pda/xml-dxml-callback-errors-ui04b-oct11.md). No global error recovery promise: DXML parse/construct is locally protected; callback dispatch and transformed native reparse have distinct risks.
- **UI-05 RUNTIME PENDING:** actual GAMMA wrapper/patch order, exception handling and caching compatibility.

## v0.1.26 current UI-06 source questions (superseding historical status where applicable)
- UI-06a: module contexts, signatures, and additional registration files.
- UI-06b: exact `CUIScriptWnd` callback/event dispatch and Lua message routing.
- UI-06c: registration coverage/conditional compilation.
- UI-06d: keyboard focus and edit box input paths. Runtime tests deferred.

## 2026-10-11 — v0.1.27 UI-06 amendment
- Targeted UI-06a/b/c/d source paths documented in [`ui06a-d-registrations-events-focus-oct11.md`](../03-ui-pda/ui06a-d-registrations-events-focus-oct11.md).
- OPEN SOURCE: UI-06a-EXH registration/overload exhaustiveness, UI-06b-EMIT widget event-emission matrix, UI-06c-BUILD build/conditional reachability, UI-06d-MODAL modal-stack and global input interactions.
- Prior runtime checks remain deferred.
