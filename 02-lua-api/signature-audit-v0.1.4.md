# Signature audit — v0.1.4

> ADR document set: **v0.1.66**. Research revisions and source/build versions below describe their original scope.

**Coverage:** Three classes at the pinned May 15 source revision: CUIWindow, CUIScrollView and CUIProgressBar. The remaining three classes from v0.1.3 remain registration-only until their headers are examined.

## Material corrections from v0.1.3

1. `CUIWindow:GetAbsoluteRect(rect)` has an `Frect&` output argument; do not call it without one.
2. `CUIScrollView:AddWindow(window, auto_delete)` requires a boolean second parameter.
3. `CUIProgressBar:SnapProgressPos()` takes no arguments; `SetSnapNoDelay(bool)` controls the snapping setting.
4. `CUIProgressBar:GetProgressStatic()` yields a reference to a native child, not a newly owned Lua widget.
5. Lua binding symbols `SetMiddleColor` and `SetMaxColor` reference the minimum-color setter in the pinned code.

## Outstanding

- Confirm Lua marshaling details for Frect/Fvector2 and pointer/reference returns.
- Inspect how XML creation configures scroll views and progress bars.
- Extract signatures of CUIStatic, CUITextWnd, CUILines.
- Verify object ownership and teardown in actual GAMMA.
- Do not issue runtime-safe sample claims on the basis of static signatures alone.
