# Native XML UI initialization (ADR v0.1.6)

> ADR document set: **v0.1.56**. Research revisions and source/build versions below describe their original scope.

**Evidence:** historical [`CUIXmlInit.cpp`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp) and [`CUIXmlInit.h`](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.h). These describe native initialization; **do not infer all methods are callable from Lua.**

## Initialization pathways

| Function | Observed behavior | Evidence |
| --- | --- | --- |
| `InitWindow` | Requires target XML node, reads `x`,`y`,`width`,`height`, sets window position/size, processes child auto statics | [lines 70–92](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L70-L92) |
| `InitStatic` | Calls `InitWindow`, processes `:text`, texture, texture offset, heading and animations | [lines 138–184](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L138-L184) |
| `InitTextWnd` | Calls `InitWindow`, initializes `:text` through native `CUILines` and checks children/texture invariants | [lines 186–212](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L186-L212) |
| `InitText` | Checks existence of text node, sets color/font/alignment/offset, translates the text | [lines 277–325](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L277-L325) |
| `InitScrollView` | Sets indents, interval, orientation flags, scroll profile, initializes native scroll view and optional text children | [lines 1097–1141](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L1097-L1141) |

## Scroll-view XML attributes

| Attribute | Native behavior / default |
| --- | --- |
| `right_ident`, `left_ident` | right/left indent; default `0.0` |
| `top_indent`, `bottom_indent` | top/bottom indent; default `0.0` |
| `vert_interval` | inter-item vertical spacing; default `0.0` |
| `inverse_dir` | inverse direction flag; default `0` |
| `scroll_profile` | profile name; default `default` |
| `flip_vert` | vertical flipping; default `0` |
| `always_show_scroll` | fixed scrollbar flag; default `1` |
| `can_select` | item selection flag; default `0` |

The initializer then calls `pWnd->InitScrollView()`. It can also create `CUITextWnd` children from `<text>` nodes, adjust their heights, and `AddWindow(newText, true)`. [Source lines 1097–1141](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L1097-L1141).

## XML text attributes

The `<text>` node provides `font` (see `fonts.md`), `align` (`l`,`c`,`r`), `vert_align` (`t`,`c`,`b`), `complex_mode` (default `0`), and optional `x`/`y` text offsets (default `0`). Source also passes its content through localization (`CStringTable().translate`). [Source lines 286–325](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L286-L325).

## Lifetime and failure observations

`InitAutoStaticGroup` creates statics on the native heap, calls `SetAutoDelete(true)` and attaches them as children. This is evidence of **native-owned** children for that path; it should not be conflated with every possible Lua creation/attachment lifecycle. [Source lines 619–646](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIXmlInit.cpp#L619-L646).

A missing required XML node triggers `R_ASSERT4` in several initializers. An unknown XML font triggers an assertion, and a present text node without a valid font triggers another assertion. UI mod validation should check these before startup.

**Pending:** precise Lua-exported `CUIXmlInit` surface; XML overlays/DXML runtime behavior; effective GAMMA UI files, profile definitions; in-game verification. No stand-alone code examples in this revision.
