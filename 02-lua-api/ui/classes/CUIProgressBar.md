# CUIProgressBar — declaration-backed signatures

> ADR document set: **v0.1.42**. Research revisions and source/build versions below describe their original scope.

**Source-confirmed, runtime-untested:** [registration](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIProgressBar_script.cpp#L5-L29); [declarations](https://github.com/themrdemonized/xray-monolith/blob/6a08e0905ce34748ee2904a5e0809f8afd141137/src/xrGame/ui/UIProgressBar.h#L44-L74).

| Lua method | Signature in C++ | Interpretation |
|---|---|---|
| `SetRange(min,max)` | `void(float, float)` | Assigns minimum / maximum and updates bar |
| `GetRange_min()` | `float()` | Minimum |
| `GetRange_max()` | `float()` | Maximum |
| `SetProgressPos(pos)` | `void(float)` | Sets target progress |
| `GetProgressPos()` | `float()` | Returns target progress (`m_ProgressPos.y`) |
| `SnapProgressPos()` | `void()` | Sets current progress equal to target |
| `GetSnapNoDelay()` | `bool()` | Reads snapping setting |
| `SetSnapNoDelay(status)` | `void(bool)` | Changes snapping setting |
| `GetProgressStatic()` | `CUIStatic&()` | Reference to **internal** child; do not destroy independently |
| `ShowBackground(status)` | `void(bool)` | Controls background visibility |
| `SetColor(color)` | `void(u32)` | ARGB packed color |
| `UseColor(status)` | `void(bool)` | Enables/disables color |
| `SetMinColor(color)` | `void(u32)` | Native minimum color setter |
| `SetMiddleColor(color)` | `void(u32)` expected | **Misbound** to `SetMinColor` in Lua registration |
| `SetMaxColor(color)` | `void(u32)` expected | **Misbound** to `SetMinColor` in Lua registration |

**Verified source defect:** Both `SetMiddleColor` and `SetMaxColor` names point at `CUIProgressBar::SetMinColor` in this pinned source, despite separate native functions being defined. Their Lua-visible behavior should not be trusted as named until fixed and runtime-tested.

**Initialization gap:** Native `InitProgressBar(Fvector2,Fvector2,EOrientMode)` exists in the header but is **not exported here**. Normal XML initialization or another supported path needs separate documentation.
