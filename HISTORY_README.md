# Anomaly Development Reference (ADR)

> **Current verified-source baseline (v0.1.30, 2026-10-11):** uploaded `xray-monolith-2026.10.11.zip`. The October 11 compiled runtime is a candidate target, **not** yet verified in GAMMA. UI source research is development-reference ready, with documented source exclusions and deferred runtime tests. See [verification report](08-research/verification-2026-10-11-v0.1.30.md). Earlier revision headers and May 15 notes below are retained as historical context.


**Documentation revision:** 0.1.1 (research baseline, 2026-10-09)

**Installed engine target:** X-Ray Monolith v1.5.3; MT-TEST 2026.05.15; xrCore 9959 (observed in user-supplied game logs).

## Mission

Create an evidence-driven, version-aware technical reference for Anomaly/GAMMA Lua, X-Ray native code, UI/PDA, Warfare, and mod debugging. Keep technical claims tied to a source location or runtime observation. *Never* assume that latest upstream features exist in the installed build.

## Read first

- `INDEX.md` — topical entry points
- `00-environment/engine-version.md` — installed baseline
- `00-environment/source-repositories.md` — upstream pointers and provenance rules
- `08-research/evidence-policy.md` — evidence standards
- `ROADMAP.md` — planned work

## Current limitations

Exact May 15 source commit unknown; no source-level exported API has yet been verified against it. No game runtime testing performed in this revision. The investigative tables are explicit research targets, not verified API promises.


**Current revision:** v0.1.3, containing an initial source-derived UI Lua export catalog. See `02-lua-api/api-index.md`.


**v0.1.7 note:** XML native initialization does not automatically imply Lua exposure; see the new boundary audit and font getter guide.

**v0.1.9 research note:** partial historical source audit added. The complete checkout was not accessible in this run; see `01-engine/source-tree-audit-v0.1.9.md`. Earlier README version notes are historical and should not supersede the latest changelog.

## Current milestone: v0.1.10 Part D

[Integrated UI architecture](01-engine/ui-lua-native-integration.md) and [consolidated open questions](08-research/open-questions-v0.1.10.md). Runtime verification remains deferred.

## Current authoritative revision: v0.1.13 (2026-10-11)
- October 11 user-provided source is the source-research baseline; October 11 runtime is a candidate pending in-game checks.
- A-01 and A-02: source research complete; runtime checks pending as applicable. See INDEX.md. Earlier version/status paragraphs above are historical.

**Latest focused research:** v0.1.14 B-01, October 11 manager ownership; see `08-research/investigations/2026-10-11-B01-font-manager-ownership.md`. B-02 next; runtime deferred.

**Current research state (v0.1.15):** October 11 source baseline; A-01, A-02, B-01 and B-02 source-researched. All runtime validation postponed. See [B-02](08-research/investigations/2026-10-11-B02-font-manager-lifecycle.md).

**v0.1.16 research amendment:** C-01 source trace completed; [`CScriptXmlInit` native child creation and `CUIWindow` attachment/deletion](08-research/investigations/2026-10-11-C01-ui-ownership.md). No runtime verification.

**v0.1.17 research amendment:** C-02 scroll-view pad, add/remove/clear ownership and Lua binding evidence: [C-02](08-research/investigations/2026-10-11-C02-scrollview-ownership.md). No runtime validation.

**v0.1.18 research amendment:** C-03 established the distinct semantics of Luabind `adopt<2>()` and native UI `AutoDelete`; see [C-03](08-research/investigations/2026-10-11-C03-luabind-adoption-autodelete.md). Tests deferred.

**v0.1.19 research amendment:** XML-created native controls normally return non-owning Lua pointer wrappers. Parented controls have native AutoDelete, but parentless controls need a separate lifetime plan. [C-04 findings](08-research/investigations/2026-10-11-C04-xml-factory-return-ownership.md).

**October 11 UI survey (v0.1.20):** Dynamic tab registry, DXML, UI input, and selected Lua UI exports now have source-linked notes in `03-ui-pda/`. The UI subsystem is still **source-incomplete**; unresolved topics are explicitly tracked.

**v0.1.22 UI lifecycle update:** [Native PDA selection and dynamic registry behavior](03-ui-pda/pda-subdialog-lifecycle-oct11.md) now source-traced. The UI audit is ongoing.


UI research update v0.1.22: tab-control selection/reset/message routing inspected against October 11 source; see UI-01a.

**v0.1.23 UI audit update:** October 11 XML/DXML native interception and Lua cache/patch lifecycle verified for `CXml::Load`; scope and exceptions recorded in [UI-04](03-ui-pda/xml-dxml-native-lifecycle-oct11.md). Runtime tests deferred.

**v0.1.24 source update:** UI-04a XML load routes and resolved-filename handling documented in [UI-04a](03-ui-pda/xml-loading-paths-ui04a-oct11.md). This does not prove universal XML interception; UI-04b and runtime checks remain open.

**v0.1.25:** UI-04b XML/DXML callback error and registration ordering audit added. The October 11 source is the research baseline; no installed GAMMA runtime claims.

**v0.1.26 UI inventory:** Source-indexed Lua UI widget names, with event/binding-context validation still open. See `03-ui-pda/ui-widget-event-inventory-oct11.md`.

**Latest source update:** v0.1.27 documents UI-06a–d (registrations, callback dispatch, build conditionality, edit focus); see `03-ui-pda/ui06a-d-registrations-events-focus-oct11.md`. It does not claim exhaustive event or build coverage.

**v0.1.28:** supplementary UI-06 source record added; see INDEX. Remaining exhaustive questions are source-open; no runtime tests conducted.

**Current research milestone: v0.1.29 (2026-10-11).** CtZ-focused UI source pass consolidated: rendering/scaling/fonts/textures [here](03-ui-pda/ui-rendering-scaling-fonts-textures-oct11.md). UI remains runtime-unverified; global UI exhaustiveness is intentionally deferred. Next major subsystem: A-Life and Warfare. Earlier version notes above are historical.
