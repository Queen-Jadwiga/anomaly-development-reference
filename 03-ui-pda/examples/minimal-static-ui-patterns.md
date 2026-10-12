# Minimal UI patterns — reference only

> ADR document set: **v0.1.72**. Research revisions and source/build versions below describe their original scope.

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
