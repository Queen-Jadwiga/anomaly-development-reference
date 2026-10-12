# Inventory and item lifecycle

> ADR document set: **v0.1.55**. Research revisions and source/build versions below describe their original scope.

**Current revision: v0.1.55.** Subsystem partial. Runtime untested and deferred until explicitly resumed.

- [Native ownership, containment and pickup/drop](ownership-lifecycle.md).
- [Focused ownership Lua APIs](../../02-lua-api/inventory/ownership-api.md).
- [ITEM-01 investigation](../../08-research/investigations/2026-10-11-ITEM-01-ownership-lifecycle.md).
- [Evidence](../../evidence/inventory/README.md).


[Placement and active-slot transitions](placement-activation.md), [Lua APIs](../../02-lua-api/inventory/placement-api.md) and [ITEM-02](../../08-research/investigations/2026-10-11-ITEM-02-placement-activation.md) complete the focused placement pass. Next consumption/destruction and owner cleanup, then item persistence/consolidation.
