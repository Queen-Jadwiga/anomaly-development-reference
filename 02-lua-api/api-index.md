# Lua API catalogs

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

Choose a current catalog below. Each page retains its own source/build/registration/converter scope; none is a complete ABI or runtime certification. [Provenance register](../00-environment/provenance-register.md), [whole-reference status](../08-research/reference-status.md).

| Area | Current canonical contracts |
| --- | --- |
| UI/PDA | [UI catalog and qualified historical/October entries](ui/README.md) |
| A-Life/Warfare | [Class/binding/script catalogs and focused server/simulator interfaces](alife/README.md) |
| Factions | [Relations](factions/relations-api.md), [community mutation](factions/community-mutation-api.md), [rank/reputation](factions/action-values-api.md) |
| Persistence | [Native extension contracts](persistence/native-extension-contracts.md), [Lua codec/storage callers](persistence/lua-storage-api.md) |
| Inventory | [Ownership](inventory/ownership-api.md), [placement](inventory/placement-api.md), [consumption/destruction](inventory/consumption-api.md) |
| Economy | [Money/base cost](economy/money-cost-api.md), [trader policy/supplies](economy/trader-policy-api.md) |
| Gameplay state | [Condition](gameplay/condition-api.md), [actor effects](gameplay/actor-effects-api.md) |
| Tasks/dialogue/info | [Native task/info contracts](tasks/native-task-info-api.md) |
| World/navigation | [Spatial](world/spatial-api.md), [interaction/transition/markers](world/interaction-api.md), [consumer restriction extensions](world/consumer-extension-api.md) |
| Configuration/script | [INI/DLTX](configuration/ini-api.md), [loading/callbacks](configuration/script-callback-api.md), [options/patch helpers](configuration/options-patch-api.md) |
| Diagnostics | [Four selected Lua exports](debugging/diagnostic-api.md) |

[Practical guide](../05-mod-architecture/development-reference.md), [qualified patterns](../07-code-library/qualified-patterns.md) and [test guidance](../05-mod-architecture/test-guidance.md) organize use of these contracts without implementing new native services. [API template](templates/api-entry.md), [workflow](../08-research/workflow.md), [layout](../08-research/repository-layout.md), [full file index](../INDEX.md).

The sections below retain the original May-era extraction/declaration research and its revision-specific caveats. They are history, not the status of every current catalog or an October availability claim.

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


Current cross-layer UI navigation: [UI guide](../03-ui-pda/development-reference.md), [native/Lua architecture](../01-engine/ui-lua-native-integration.md).
