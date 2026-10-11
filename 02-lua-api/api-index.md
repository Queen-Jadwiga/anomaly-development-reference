# Lua API catalogs

> ADR document set: **v0.1.42**. Research revisions and source/build versions below describe their original scope.

Current canonical locations:

- [UI catalog and October 11 follow-ups](ui/README.md).
- [A-Life/Warfare C++ and Lua catalog](alife/README.md).
- [Shared API entry template](templates/api-entry.md).
- [Research workflow](../08-research/workflow.md) and [repository layout](../08-research/repository-layout.md).

Each record declares its own baseline and scope. An inventory is not an exhaustive ABI or runtime certification. Earlier class-entry content remains historically scoped even after relocation.

## Historical May 15 index — preserved

### Lua API index — pinned source extraction

**Target:** `6a08e0905ce34748ee2904a5e0809f8afd141137` (tag `2026.5.15`). **Scope:** UI binding subset only, *not a complete Lua API*.

- [**CUIWindow**](ui/classes/CUIWindow.md) — 22 registered entries
- [**CUIScrollView**](ui/classes/CUIScrollView.md) — 11 registered entries
- [**CUIProgressBar**](ui/classes/CUIProgressBar.md) — 16 registered entries
- [**CUIStatic**](ui/classes/CUIStatic.md) — 20 registered entries
- [**CUITextWnd**](ui/classes/CUITextWnd.md) — 15 registered entries
- [**CUILines**](ui/classes/CUILines.md) — 6 registered entries

See [machine-readable export index](ui/exports-ui-2026-05-15.csv).

## Important caveats
- Registration proves Lua-visible names in this source revision, not successful operation in GAMMA.
- `SetMiddleColor` and `SetMaxColor` both point to `SetMinColor` in the inspected `CUIProgressBar` source. This may be a binding error; do not assume they work as named.
- Method argument types, ownership, object states, and overloaded semantics need declaration-level verification.

## v0.1.4 declaration audit
- [CUIWindow](ui/classes/CUIWindow.md): selected parameter/result signatures and child ownership.
- [CUIScrollView](ui/classes/CUIScrollView.md): `AddWindow` parameters and initialization warning.
- [CUIProgressBar](ui/classes/CUIProgressBar.md): complete listed parameter signatures and confirmed Lua binding mismatch.
- [Audit and remaining gaps](signature-audit-v0.1.4.md).

## ADR v0.1.7
- [XML initialization exposure audit](xml-initialization-exposure.md) — native initializer documented; direct Lua registration not yet proven.
- [Font globals vs. XML tokens](../03-ui-pda/font-manager-and-lua-getters.md).

## Architecture cross-reference

[End-to-end UI/Lua-native integration](../01-engine/ui-lua-native-integration.md).
