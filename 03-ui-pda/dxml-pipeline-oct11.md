# October 11 UI survey — DXML pipeline and patch scoping

> ADR document set: **v0.1.75**. Research revisions and source/build versions below describe their original scope.

**Baseline:** `2026.10.11`, bundled gamedata. This is a script-side system, not a general guarantee that every loaded XML goes through it.

## Verified

- `dxml_core.script` registers `on_xml_read` and loads candidate `modxml_*.script` hooks from the scripts directory. [gamedata/scripts/dxml_core.script:11-15](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L11-L15); [gamedata/scripts/dxml_core.script:116-158](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L116-L158).
- After parsing an XML document, it invokes `SendScriptCallback('on_xml_read', xml_file_name, xml_obj, flags)`, then serializes the modified document. `flags.cache` controls whether the transformed XML is cached. [gamedata/scripts/dxml_core.script:986-1010](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/scripts/dxml_core.script#L986-L1010).
- `gamedata/configs/mod_script_dxml.ltx` includes `dxml_core` in script loading. [gamedata/configs/mod_script_dxml.ltx:1-2](https://github.com/themrdemonized/xray-monolith/blob/2026.10.11/gamedata/configs/mod_script_dxml.ltx#L1-L2).

## CtZ design implication

Apply path-targeted, minimal `modxml_*.script` patches; preserve idempotence and check for existing nodes before adding. Do not claim DXML reaches every native XML load site without a complete native interception audit. A native dynamic War tab may obviate changing shared `pda_16.xml` for tab registration; content XML may still be appropriate.

## Open

- UI-04 (SOURCE): trace exact native XML-read interception feeding DXML, determine exclusions, filename normalization, and cache edge cases.
- UI-05 (RUNTIME): test multiple mods patching same XML, patch ordering and GAMMA load integration.
