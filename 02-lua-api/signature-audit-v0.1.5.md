# ADR v0.1.5 — text/UI declaration audit

> ADR document set: **v0.1.62**. Research revisions and source/build versions below describe their original scope.

Pinned version: May 15 2026 / `6a08e0905ce34748ee2904a5e0809f8afd141137`.

Expanded `CUIStatic`, `CUITextWnd`, `CUILines`, with minimal examples (no new runnable snippets). Native C++ headers and existing Luabind registration inventory were cross-referenced to avoid treating non-exported C++ functions as Lua API.

**Resolved high-priority signatures:** `CUITextWnd::SetFont(CGameFont*)`; `CUILines::SetFont(CGameFont*)`; `SetText(LPCSTR)`; `SetTextColor(u32)`; `CUIStatic::InitTexture(LPCSTR)`; `CUIStatic::SetTextureColor(u32)`.

**Unresolved:** Lua-wrapper overloads for certain `CUIStatic` animation helpers; concrete Lua enum values; XML initialization, font getter initialization timing, runtime equivalence of GAMMA executable and official source.

**Standing known issue:** `CUIProgressBar` binding anomaly described in v0.1.4 remains source-confirmed but GAMMA runtime untested.
