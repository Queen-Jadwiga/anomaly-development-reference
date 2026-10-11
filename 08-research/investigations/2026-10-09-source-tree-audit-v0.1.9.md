# INV-009 — Source-tree audit and XML/font lifecycle

> ADR document set: **v0.1.49**. Research revisions and source/build versions below describe their original scope.

Status: **Partial / blocked on full checkout**. Source revision: `2026.5.15` / recorded SHA `6a08e0905ce34748ee2904a5e0809f8afd141137`.

- Checked historical native `UIXmlInit.cpp` and `UIXmlInit.h` directly.
- Confirmed text initializer call path, including early return for missing text node and assertion on null font for a present text node.
- Produced explicit native flow diagram and reproducible Git commands.
- Attempted full remote ZIP/clone access, but full archive could not be retrieved in current environment.
- Did **not** complete repository-wide Lua registration inventory or font manager allocation/destruction trace.
- Runtime verification deferred at user's request.

**Next blocking prerequisite:** historical full source checkout. Then systematically search Luabind registration units and native font lifecycle, attach line-specific permalinks, and revise findings.
