# Minimal UI patterns — reference only

> ADR document set: **v0.1.81**. Research revisions and source/build versions below describe their original scope.

Examples intentionally restricted to **two non-runnable call sketches** pending runtime testing. They assume valid initialized widgets and are not standalone mods.

```lua
-- Existing initialized progress bar, acquired through a supported path:
bar:SetRange(0, 100)
bar:SetProgressPos(35)
bar:SnapProgressPos()
```

```lua
-- Existing initialized and properly owned scroll view:
scroll:ScrollToBegin()
local position = scroll:GetCurrentScrollPos()
```

Neither sketch establishes that bare Lua constructors produce safely initialized PDA elements. Avoid copying these into CtZ without verifying the initialization and lifetime route.

[ARCH-03 qualification](../../07-code-library/qualified-patterns.md#reuse-the-two-ui-sketches-with-their-lifetime-limits) adds dependency/ownership/failure/cleanup review fields for these same two sketches; [test guidance](../../05-mod-architecture/test-guidance.md) keeps source/fixture and game evidence separate. No constructor, teardown recipe or runtime-tested example is added.
