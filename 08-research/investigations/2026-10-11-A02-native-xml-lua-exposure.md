# A-02 — Separate native CUIXmlInit Lua exposure (2026-10-11)

> ADR document set: **v0.1.47**. Research revisions and source/build versions below describe their original scope.

**Status:** SOURCE RESEARCH COMPLETE — runtime validation optional/pending.  **Revision:** ADR v0.1.13. **Source:** user-supplied `xray-monolith-2026.10.11.zip`; extracted project root `xray-monolith-2026.10.11/`. This result applies only to that snapshot, not automatically to previous releases, custom DLLs, or runtime-injected registrations.

## Answer

The October 11 shipped source defines native `CUIXmlInit` but **does not register it as an independently named Luabind class**. Instead it registers `CScriptXmlInit`, a dedicated Lua-facing wrapper whose functions call `CUIXmlInit` internally. The native initializer's public C++ methods are **not** automatically exposed to Lua. A different dynamically loaded module or post-startup script could theoretically create an alias; the source-wide result does not establish an absence of every possible runtime alias.

## Reproducible full-tree audit

- All extracted regular files enumerated: **6352**; UTF-8-decodable files inspected: **6236**. This includes `src/`, project data and tooling; search was not limited to registration files.
- Files containing literal `CUIXmlInit`: **103**. All such files were inspected for registration context; non-source mentions are not treated as exports.
- Targeted expression checks for `class_<CUIXmlInit>`, `CUIXmlInit::script_register`, `add_to_type_list(CUIXmlInit)`, and literal `"CUIXmlInit"`: **0 matches**.
- This is a reproducible negative source finding, **not** a proof concerning external binary modules or arbitrary runtime additions.

Run `rg -n 'CUIXmlInit' src`, `rg -n 'class_<\s*CUIXmlInit|CUIXmlInit::script_register|add_to_type_list\(CUIXmlInit\)|"CUIXmlInit"' src` and review wrapper registrations.

## Positive evidence (October 11 source-relative line locations)

| File | Lines | Evidence |
| --- | --- | --- |
| `src/xrGame/ui/UIXmlInit.h` | 35–99 | Native class and static XML/widget initialization methods; no `script_register` declaration |
| `src/xrGame/ScriptXMLInit.h` | 34–82 | Separate `CScriptXmlInit` wrapper with `DECLARE_SCRIPT_REGISTER_FUNCTION` |
| `src/xrGame/ScriptXMLInit.cpp` | 145–147; 180–183; 212–215 | Wrapper methods delegate to `CUIXmlInit::InitWindow`, `InitStatic`, `InitScrollView` |
| `src/xrGame/ScriptXMLInit.cpp` | 361–406 | Luabind registration names `CScriptXmlInit`, constructs it and exports named wrapper methods |
| `src/xrGame/ui_export_script.cpp` | 29–45 | UIRegistrator invokes `CScriptXmlInit::script_register(L)`; no native CUIXmlInit registration |

## Interpretation for CtZ

Use `CScriptXmlInit()` and its exported `ParseFile`, `InitStatic`, `InitWindow`, `InitScrollView`, etc. **Do not** call `CUIXmlInit()` or `CUIXmlInit.Init*` directly from Lua based on this source. If CtZ requires a native method omitted from the wrapper, first investigate an existing alternative export or supported UI API; only then consider extending native bindings.

## Remaining runtime-only validation

When the October 11 runtime is installed, run an isolated safe Lua smoke test for the presence of the `CScriptXmlInit` global and absence of a global `CUIXmlInit`. Record the actual Lua environment, loading stage and whether any addons inject globals. A runtime alias would not invalidate the source conclusion but must be catalogued separately. No in-game test was run.

## Source file references

Github browser reference (tag): https://github.com/themrdemonized/xray-monolith/tree/2026.10.11/src/xrGame ; the authoritative evidence for this audit is the exact user-uploaded archive, not a newly fetched website. GitHub path/line anchors should be validated before citing the remote tag as interchangeable with the uploaded snapshot.
