# Lua API catalogs

> ADR document set: **v0.1.80**. Research revisions and source/build versions below describe their original scope.

Current canonical locations:

- [UI catalog and October 11 follow-ups](ui/README.md).
- [A-Life/Warfare C++ and Lua catalog](alife/README.md).
- [Focused faction and relation contracts](factions/relations-api.md).
- [Community mutation and live team contracts](factions/community-mutation-api.md).
- [Rank/reputation and action-flag contracts](factions/action-values-api.md).
- [Native persistence extension contracts](persistence/native-extension-contracts.md).
- [Supplied Lua codec/storage caller contracts](persistence/lua-storage-api.md).
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

For cross-layer selection, see the [faction development reference](../04-game-systems/factions/development-reference.md).

- [Inventory ownership APIs](inventory/ownership-api.md).

[Inventory placement APIs](inventory/placement-api.md).

[Consumption/destruction APIs](inventory/consumption-api.md).

Inventory contracts are consolidated in the [development reference](../04-game-systems/inventory/development-reference.md); [effective-source completion](../04-game-systems/inventory/source-completion-status.md) remains partial.

[Money and base-cost Lua contracts](economy/money-cost-api.md): native balances/deltas and virtual item Cost, distinct from partner trade price.

[Trader policy and supplies Lua contracts](economy/trader-policy-api.md): owner/global factors, show filters, scalar setters and destructive supply requests.

[Live condition properties and changes](gameplay/condition-api.md): current fields versus pending deltas and base/actor limits.

[Actor booster and modifier contracts](gameplay/actor-effects-api.md): selected class exports, replacement semantics and map accessor build limit.

[Native task/info contracts](tasks/native-task-info-api.md): actor task-manager forwarding/adoption and owner info query/transfer return boundaries.

- [Selected world spatial/restriction/patrol contracts](world/spatial-api.md): WORLD-02; source-confirmed within scope, effective/runtime limits retained.

- [Selected world use/zone/changer/marker APIs](world/interaction-api.md): WORLD-03; effective/runtime gaps retained.

- [WORLD-04 selected dynamic restriction consumer extensions](world/consumer-extension-api.md); [world consolidation](../04-game-systems/world/development-reference.md).

## Configuration contracts

[Selected Lua INI construction/read/write/lifetime and DLTX diagnostics](configuration/ini-api.md), CONFIG-02/ENGINE1011. Exact registered arities, ownership and converter limits; runtime deferred.

[Selected script lookup/prefetch and shared callback contracts](configuration/script-callback-api.md), CONFIG-03/ENGINE1011: native-only versus Lua exports, exact listener identity, ordering/removal/dispatch, debug-global route and effective-wrapper limits.

[Supplied option/patch helper contracts](configuration/options-patch-api.md), CONFIG-04: direct get/set versus pending/current/default/preset/apply/change, class/instance and original-capture limits; effective integration partial.

## Selected debugging exports

[Diagnostic API](debugging/diagnostic-api.md) records exact source-qualified log/error_log/print_stack/flush signatures, converter/build guards, void returns and failure/output limits. [Debugging reference](../06-debugging/README.md), [evidence](../evidence/debugging/README.md). DEBUG-01 selected scope complete; runtime deferred.
