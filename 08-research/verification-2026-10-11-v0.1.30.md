# ADR source verification — v0.1.30 (11 October 2026)

> ADR document set: **v0.1.80**. Research revisions and source/build versions below describe their original scope.

## Scope and method

Compared **ADR v0.1.29** with the user-supplied `xray-monolith-2026.10.11.zip` extracted source. This is a **source-reference integrity and targeted claim audit**, *not* a proof that every sentence in 95 ADR files is correct, that upstream URLs resolve externally, or that any behavior has been validated in GAMMA. No runtime tests were performed. Preserve all historical research.

## Checks and results

- Audited **89 Markdown documents** and **139 local Markdown link targets**: all local targets exist.
- Parsed **184 source-repository citations** matched by the audit scanner; checked referenced source paths and line ranges against extracted source files. Three anchors extended beyond file length (repaired below). Four initially flagged paths were false positives caused by Markdown backticks embedded in link paths; actual source paths exist and were not edited.
- Inspected key native mechanisms already referenced in the ADR: `CScriptXmlInit` registration chain; native font manager ownership and reset; `CUIWindow` child `AutoDelete`; scroll-view internal pad; Luabind ownership distinction; dynamic PDA Lua registry; `CXml::Load`/DXML interception; tab state; native UI callback dispatch; XML font and texture initialization. Existing bounded conclusions remain plausible and are not promoted to runtime-verified.
- Source URL anchors were checked against **the uploaded snapshot**, not against live GitHub. The archive tag name alone is not independent proof of an immutable remote commit. A complete semantic audit of 450 binding occurrences and all engine-side variants has not been performed.

## Corrections applied

| ADR document | Original link range | Corrected link range | Classification |
|---|---|---|---|
| `03-ui-pda/pda-subdialog-lifecycle-oct11.md` | `pda_dynamic_tabs.script#L46-L104` | `#L46-L99` | Citation range exceeded 99-line source file |
| `03-ui-pda/xml-dxml-callback-errors-ui04b-oct11.md` | `dxml_core.script#L1033-L1052` | `#L1033-L1050` | Citation range exceeded 1050-line source file |
| `03-ui-pda/ui06a-d-registrations-events-focus-oct11.md` | `UICustomEdit.cpp#L300-L343` | `#L300-L342` | Citation range exceeded 342-line source file |

Added a prominent current-baseline banner to `README.md`. Historical version paragraphs intentionally remain unchanged and should **not** be read as current status.

## Source-verification disposition

| Area | Result |
|---|---|
| A-01 class registration | Source-confirmed for October 11 chain: `CScriptEngine::init` → `export_classes` → `UIRegistrator` → `CScriptXmlInit::script_register` |
| A-02 `CUIXmlInit` Lua exposure | Source-supported *negative finding for scanned Luabind registration paths*; no claim about arbitrary external extensions |
| B-01/B-02 font ownership, lifecycle | Source-supported for native named-font manager; installed font resources and crash avoidance still runtime-dependent |
| C-01–C-04 UI controls, scroll and userdata | Source-supported conditional ownership rules; do not interpret returned pointer as guaranteed lifetime |
| Native PDA tabs and DXML | Source-supported bundled implementation; addon coexistence and installed gamedata remain runtime-dependent |
| UI API and events | Scoped inventory, **not an exhaustive exported ABI contract** |
| Rendering/scaling/assets | Selected native paths inspected; correctness at resolutions and actual assets untested |

## Remaining limitations and next gates

1. **Runtime pending:** confirm October 11 executable/bundled Lua match the user's eventual GAMMA installation; test dynamic PDA tab creation, XML patch conflicts, font presence, list teardown and keyboard capture.
2. **Source questions retained, not hidden:** exhaustive exported overload coverage; indirect widget event emission; all binary build configurations; input hooks bypassing dialog focus; renderer-specific behavior. Prioritize only when relevant to a CtZ implementation decision.
3. **Citation provenance:** match uploaded ZIP to a specific upstream commit/hash if immutable upstream provenance becomes important; local line checks are currently against the uploaded source archive.
4. **Engineering consequence:** no observed blocking source inconsistency in the sampled high-priority UI paths; this is **not** a blanket certification of the ADR or engine.

## Audit integrity

Scripted checks: read local Markdown paths, parse GitHub `blob/2026.10.11` references, validate line bounds against uploaded files, and verify final ZIP CRC. Absence of a match is not proof a native feature does not exist.
