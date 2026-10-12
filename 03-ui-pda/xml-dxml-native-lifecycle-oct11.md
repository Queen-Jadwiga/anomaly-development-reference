# UI-04 — Native XML interception and DXML lifecycle (2026.10.11)

> ADR document set: **v0.1.67**. Research revisions and source/build versions below describe their original scope.

**Baseline:** User-supplied `xray-monolith-2026.10.11.zip`. **Status:** source research complete for the traced `CXml::Load` → DXML path; integration and runtime validation pending. This analysis does **not** establish that every XML load in the game invokes `CXml::Load`.

## Source-confirmed execution sequence

1. `CXml::Load(path, xml_filename)` stores `m_xml_file_name` from its supplied filename, reads via `FS.r_open`, expands file includes through `ParseFile`, and parses the assembled data with `m_Doc.Parse`. Parse errors assert. Only **after this initial parse succeeds**, `CXml::Load` calls `XMLLuaCallback(*this, W.pointer())`. [src/xrXMLParser/xrXMLParser.cpp:111–158](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrXMLParser/xrXMLParser.cpp#L111-L158)
2. `XMLLuaCallback` rejects null/empty strings, strips UTF-8 BOM, attempts to resolve `_G.COnXmlRead` through the script engine, and, **only if the functor exists**, invokes it with `(m_xml_file_name, xml_string)`. The returned string is passed to `CXml::LoadFromString`, which clears and reparses the native XML document, asserting if the result is invalid. The code shown has no exception-recovery wrapper around that call. [src/xrGame/ScriptXMLInit.cpp:53–65](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ScriptXMLInit.cpp#L53-L65).
3. `dxml_core.script` registers the `on_xml_read` script callback. It finds nonempty root-level `modxml_*.script` files using the game script filesystem, sorts their derived module names, and calls each module's `on_xml_read()` hook to register callbacks. It also force-loads the specified `ui_options_modded_exes` hook. **This sorting proves hook registration order for discovered modules, not an unconditional runtime order for every callback from other mods.** [gamedata/scripts/dxml_core.script:116–160](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L116-L160).
4. When `_G.COnXmlRead` is available, the DXML function filters unsupported text-language paths and bypasses `gameplay\character_desc_general.xml`. It checks a filename-keyed in-memory string cache, parses the provided XML into a Lua DOM, sends `SendScriptCallback('on_xml_read', xml_file_name, xml_obj, flags)`, serializes the DOM, and caches the result only if a callback sets `flags.cache=true`. **Caching is opt-in**, not universal. Parse/DOM creation failures return the original XML string, rather than guaranteeing that malformed native XML is safe. [gamedata/scripts/dxml_core.script:961–1012](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L961-L1012).
5. `openXMLFile` is a separate script helper that reads `$game_config$`, parses with the Lua XML library, fires `on_xml_read` with a fresh `{}` flags table, and returns a Lua XML object. It is **not evidence** that the engine's native XML load cycle has been invoked or that its cache policy applies. [gamedata/scripts/dxml_core.script:1016–1049](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L1016-L1049).

## Consequences for CtZ

- Prefer narrowly targeted, idempotent `modxml_ctz_*.script` callbacks for shared XML changes. Guard by exact resource path and check for already-inserted nodes.
- Do not assume the callback sees raw unprocessed XML: the native loader first expands includes and parses the assembled document, then hands the combined text to the hook.
- Do not treat the hook as a safe error boundary: malformed replacement output leads to native reparse assertions. Validate CtZ XML before shipping.
- Keep tab creation independent from shared XML rewriting when native dynamic PDA tabs suffice; content layout XML can still be patched.
- Cache behavior is per filename in `dxml_core.script`, is set by callback flags, and can prevent subsequent callbacks on cache hits; if CtZ changes an XML patch at runtime, no cache invalidation mechanism has been verified here.

## Open questions — do not infer

- **UI-04a (source):** Enumerate other XML readers and paths that may bypass `CXml::Load` and identify `correct_file_name` normalization/case consequences. This record confirms the `CXml` path only, not *every* native or script XML reader.
- **UI-04b (source):** Full callback-error handling and Lua module registration ordering across GAMMA wrappers outside the bundled source. The native call site shows no recovery wrapper, but Luabind/script-engine error behavior was not audited here.
- **UI-05 (runtime pending):** Validate patch ordering, conflicts with other GAMMA addons, path variants, caching and missing-hook startup on the October 11 runtime.

## Exact primary-source references

- xrXMLParser: [src/xrXMLParser/xrXMLParser.cpp:111–158](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrXMLParser/xrXMLParser.cpp#L111-L158)
- Native hook: [src/xrGame/ScriptXMLInit.cpp:53–65](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ScriptXMLInit.cpp#L53-L65)
- DXML registration: [gamedata/scripts/dxml_core.script:11–16](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L11-L16)
- Discovery: [gamedata/scripts/dxml_core.script:116–160](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L116-L160)
- Modification/cache: [gamedata/scripts/dxml_core.script:961–1012](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L961-L1012)
- Separate helper: [gamedata/scripts/dxml_core.script:1016–1049](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L1016-L1049)

## External probe observation — 2026-10-12

[Issue #4](https://github.com/Queen-Jadwiga/anomaly-development-reference/issues/4) reports DXML editing text files during startup/font setup: a unique control retained the edited text, while a duplicate ID in a later distinct file replaced the earlier edited value. Separately, MO exposed only the winning copy of each same-named file. These are separate layers—virtual-filesystem shadowing, per-file editing, then cross-file duplicate replacement—not a general claim that DXML overrides every later resource.

This supports the selected source trace on the reported September-era installation; it does not close all UI-05 cache, localization, reader or competing-hook scenarios. [R05/R06 and provenance](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md#corroborating-observations).
