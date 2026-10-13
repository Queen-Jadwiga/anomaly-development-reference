# UI widgets — source-backed starting index

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

Refer to [`02-lua-api/api-index.md`](../02-lua-api/api-index.md). Source-confirmed at pinned May 15 commit: `CUIWindow`, `CUIStatic`, `CUITextWnd`, `CUIScrollView`, `CUIProgressBar`, `CUILines`.

## CtZ implications
- `CUIScrollView` exports scroll-position queries and `SetScrollPos`, potentially relevant for longer PDA lists; implementation and ownership tests pending.
- `CUIProgressBar` exports progress and snapping methods, potentially relevant to faction power displays.
- `CUITextWnd` exports font getters/setters, relevant to the reported UI font crash.

**No existing Capture the Zone UI fix is claimed or installed in this research revision.**
