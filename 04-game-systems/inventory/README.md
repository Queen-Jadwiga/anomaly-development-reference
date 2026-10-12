# Inventory and item lifecycle

> ADR document set: **v0.1.66**. Research revisions and source/build versions below describe their original scope.

**Current revision: v0.1.66.** Selected available-source first-edition work is complete within scope. Full effective installed integration remains partial; runtime untested and deferred.

Start with the [practical development reference](development-reference.md) and [completion status/remaining evidence](source-completion-status.md).

| Topic | Reference | Focused Lua contracts | Research record |
| --- | --- | --- | --- |
| Ownership/containment, pickup/drop | [Ownership](ownership-lifecycle.md) | [Ownership APIs](../../02-lua-api/inventory/ownership-api.md) | [ITEM-01](../../08-research/investigations/2026-10-11-ITEM-01-ownership-lifecycle.md) |
| Placement and activation | [Placement](placement-activation.md) | [Placement APIs](../../02-lua-api/inventory/placement-api.md) | [ITEM-02](../../08-research/investigations/2026-10-11-ITEM-02-placement-activation.md) |
| Consumption/destruction and cleanup | [Consumption](consumption-destruction.md) | [Consumption APIs](../../02-lua-api/inventory/consumption-api.md) | [ITEM-03](../../08-research/investigations/2026-10-11-ITEM-03-consumption-destruction.md) |
| Persistence/reconstruction | [Persistence](persistence-reconstruction.md) | [General persistence contracts](../../02-lua-api/persistence/native-extension-contracts.md) | [ITEM-04](../../08-research/investigations/2026-10-11-ITEM-04-persistence-reconstruction.md) |
| Consolidation/bounded audit | [Development reference](development-reference.md) | Existing contracts above | [ITEM-05](../../08-research/investigations/2026-10-11-ITEM-05-inventory-consolidation.md) |

[Evidence ledgers](../../evidence/inventory/README.md); [current audit](../../08-research/verification-2026-10-12-v0.1.66.md). Snapshot findings do not establish installed NPC behavior or runtime compatibility. Next general subsystem: trade/economy. [Roadmap](../../ROADMAP.md).
