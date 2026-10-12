# XML initializer Lua registration audit — v0.1.9

> ADR document set: **v0.1.68**. Research revisions and source/build versions below describe their original scope.

## Current result

**Open.** The pinned header and implementation establish native methods, not Lua exports. Since a complete local source tree was not available, absence of `CUIXmlInit` registration **cannot** be asserted.

## Exact reproducible source search (requires checkout)

```bash
git clone https://github.com/themrdemonized/xray-monolith.git
cd xray-monolith
git checkout 2026.5.15
git rev-parse HEAD
# ripgrep is optional; git grep is included with Git.
git grep -n -E 'CUIXmlInit|class_<.*UIXml|module\(|script_register' -- src
git grep -n -E 'GetFontSmall|GetFontMedium|GetFontDI|GetFontLetterica' -- src
```

Log each hit with exact filename, function name, Luabind registration expression, and commit permalink. Determine whether an exported `CUIXml` or XML helper wrapper is distinct from native `CUIXmlInit` before making API claims. Preserve negative results only after a complete repo-wide search.

## Confirmed native declaration

[Historical `CUIXmlInit.h`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.h#L31-L66) declares methods such as `InitWindow`, `InitTextWnd`, `InitFont`, and `InitScrollView` as static C++ members. Binding status is not proven by the declaration.


> **Update (v0.1.10 Part A):** A script-facing bridge `CScriptXmlInit` was found and documented at [registration-architecture-part-A.md](registration-architecture-part-A.md). The unresolved question here is **direct** `CUIXmlInit` registration, not the existence of any Lua XML initializer.
