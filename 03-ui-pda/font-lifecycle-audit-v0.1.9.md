# Font lifecycle — source audit v0.1.9

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

## What is confirmed

1. The native `CUIXmlInit` constructor invokes `InitColorDefs`, not a demonstrated font allocation routine.
2. `InitText` resolves a pointer via `InitFont`, asserts that it is not null, then assigns it via `SetFont`.
3. An absent `:text` XML node returns early and **does not** by itself assert. It is a **present** text node with an unresolved/null font that encounters the assertion.

[Source: pinned `UIXmlInit.cpp` lines 47–50, 277–296](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L277-L296).

## Not yet confirmed

- Construction and destruction of font objects.
- UI font manager startup relative to Lua VM and PDA/UI initialization.
- Font pointer lifetimes during UI reload, game transitions, or shutdown.
- Any modified-executable-only font replacement hooks.

### Checkout search plan

```bash
git grep -n -E 'class CGameFont|CGameFont::|GetFontSmall|GetFontMedium|FontManager|DeleteFonts|DestroyFont' -- src
git grep -n -E 'InitFont\(|DeleteColorDefs\(|UI\(\)\.Font\(' -- src
```

For every candidate, distinguish definitions, calls, declarations and registered Lua bindings. Runtime verification deferred.
