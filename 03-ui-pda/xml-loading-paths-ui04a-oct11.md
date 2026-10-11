# UI-04a — XML loading routes, naming and DXML interception boundaries

> ADR document set: **v0.1.42**. Research revisions and source/build versions below describe their original scope.

**Baseline:** user-supplied X-Ray Monolith source tag `2026.10.11`. **Status:** source research completed for enumerated native `CXml` entry points, UI filename remapping, and bundled Lua XML helper. Runtime confirmation and exhaustive third-party addon coverage deferred.

## Verified call paths

1. `CXml::Load(path_alias, path, _xml_filename)` calls the virtual `correct_file_name(path, _xml_filename)`, assembles `path\corrected_name`, and calls the two-argument `Load`. That two-argument loader records the resulting string as `m_xml_file_name`, loads through `FS.r_open`, expands includes, parses XML, then calls `XMLLuaCallback`. **Thus both overloads reach the hook on successful load.** [src/xrXMLParser/xrXMLParser.cpp:111–144](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrXMLParser/xrXMLParser.cpp#L111-L144).
2. `CXml::LoadFromString` parses supplied XML but **does not call `XMLLuaCallback`**. It is called by `XMLLuaCallback` after the Lua result is returned, avoiding direct reentrant interception. It is a public API that can be invoked independently in native code. [src/xrXMLParser/xrXMLParser.cpp:146–158](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrXMLParser/xrXMLParser.cpp#L146-L158); [src/xrGame/ScriptXMLInit.cpp:55–65](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ScriptXMLInit.cpp#L55-L65).
3. The base `CXml::correct_file_name` is an identity function. `CUIXml` overrides it: when the path compares equal to `UI_PATH` (`ui`) or `UI`, under `XRGAME_EXPORTS`, it delegates to `UI().get_xml_name`; other paths return the original filename. The non-XRGAME build branch also returns the original. [src/xrXMLParser/xrXMLParser.h:89–99](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrXMLParser/xrXMLParser.h#L89-L99); [src/xrGame/ui/xrUIXmlParser.cpp:8–20](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui/xrUIXmlParser.cpp#L8-L20).
4. `ui_core::get_xml_name` selects default (`.xml`) or screen-mode variant (`_16.xml` / `_21.xml`), checks variant presence with `FS.exist`, and includes a fallback to `_16` (in wide mode) or the original name. **This is UI resource selection, not generic case folding or path normalization.** Its exact fallback behavior depends on extension and screenmode branches; no universal separator/case normalization is proved. [src/xrGame/ui_base.cpp:298–339](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ui_base.cpp#L298-L339).
5. Include processing is performed **before** DXML interception. The `ParseFile` helper recognizes `#include`, handles wildcard includes via `FS.file_list`, resolves certain `ui\` includes using `correct_file_name`, and concatenates their content. The hook is invoked once on the assembled text of the outer `Load`, not separately for every include (unless an include is also loaded independently elsewhere). [src/xrXMLParser/xrXMLParser.cpp:24–109](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrXMLParser/xrXMLParser.cpp#L24-L109); [src/xrXMLParser/xrXMLParser.cpp:121–144](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrXMLParser/xrXMLParser.cpp#L121-L144).
6. `XMLLuaCallback` passes `m_xml_file_name` to `_G.COnXmlRead`. Therefore, for the three-argument UI load, DXML normally receives **the resolved `ui\...` path**, not necessarily the caller's original filename. For direct two-argument loads, it receives the caller-supplied filename unmodified by the three-argument remapper. This has consequences for literal path comparisons and cache keys. [src/xrGame/ScriptXMLInit.cpp:55–65](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrGame/ScriptXMLInit.cpp#L55-L65); [src/xrXMLParser/xrXMLParser.cpp:111–143](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/src/xrXMLParser/xrXMLParser.cpp#L111-L143).
7. The bundled `dxml_core.openXMLFile` loads a file directly with `getFS():r_open('$game_config$', path)`, parses through the Lua XML library, calls `on_xml_read`, and returns a Lua XML object. It **does not itself invoke** native `CXml::Load` or `_G.COnXmlRead`; it supplies a different path and flags table, so native include expansion and filename remapping cannot be assumed. [gamedata/scripts/dxml_core.script:1014–1049](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L1014-L1049).

## Carefully bounded conclusions

- The documented native hook covers successfully parsed loads through either `CXml::Load` overload **when `_G.COnXmlRead` is available**. It is not a claim about every XML parser or direct filesystem reader in the engine and installed mods.
- Direct `LoadFromString` skips the hook; the bundled `openXMLFile` Lua path is separate. Other raw file readers or third-party parsers cannot be covered by the CXml claim without their own call-site audit.
- UI naming is resolution-mode-dependent. To patch known resources, compare the *observed/resolved* DXML filename variants, rather than assuming a single unsuffixed XML basename.
- Literal DXML path checks and filename-keyed caching can distinguish different naming forms; this research does not establish filesystem-level case insensitivity, separator canonicalization, or callback-path normalization.
- Failures in file opening or first native parse can prevent callback entry; callback errors belong to **UI-04b**, not this investigation.

## CtZ implementation guidance (design, not tested behavior)

- Use version-specific path guards for `ui\` resources; handle `_16.xml`/`_21.xml` variants where applicable.
- Prefer the dynamic PDA tab registry for registering CtZ's War tab; reserve DXML for surgical layout changes.
- Avoid relying on patching an XML file that is included only as a fragment; inspect the outer document receiving the DXML callback.
- In source diagnostics, log the resolved `xml_file_name` supplied to callbacks instead of guessing it from the original request.

## Remaining open questions

- **UI-04b (source):** trace native/Luabind functor exception behavior and bundled callback failure handling. Audit third-party wrapping only if actual GAMMA addon sources are available; don't assume bundled script load order describes an arbitrary installed stack.
- **UI-05 (runtime):** test actual resolved file names, language/variant paths, DXML registration conflicts, cache behavior, and callback timing in installed GAMMA.
- **Separate optional deeper source audit:** an exhaustive inventory of unrelated XML parsers/direct readers across all modules, including third-party code, is not proven by this scoped investigation. Reopen only with a concrete CtZ-facing reader or interoperability need.
