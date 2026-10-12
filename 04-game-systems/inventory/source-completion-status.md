# Inventory source completion and remaining work

> ADR document set: **v0.1.66**. Research revisions and source/build versions below describe their original scope.

**As of 11 October 2026:** selected ITEM-01–04 native/server/actor/box/eatable foundations, focused Lua contracts, practical consolidation and bounded final available-source audit are complete within scope. The [development reference](development-reference.md) is usable within those boundaries. Full effective installed inventory integration is **partial**; runtime is **untested** and deferred until explicitly resumed.

## Completed available-source work

| Area | Record/reference | Disposition |
| --- | --- | --- |
| Ownership/containment and pickup/drop | [ITEM-01](../../08-research/investigations/2026-10-11-ITEM-01-ownership-lifecycle.md), [reference](ownership-lifecycle.md), [APIs](../../02-lua-api/inventory/ownership-api.md) | Selected server/actor/box paths and request/callback limits mapped |
| Placement and requested/current activation | [ITEM-02](../../08-research/investigations/2026-10-11-ITEM-02-placement-activation.md), [reference](placement-activation.md), [APIs](../../02-lua-api/inventory/placement-api.md) | Eligibility/strict paths, unequal callback phases, actor requests and readiness limits mapped |
| Consumption/destruction and owner cleanup | [ITEM-03](../../08-research/investigations/2026-10-11-ITEM-03-consumption-destruction.md), [reference](consumption-destruction.md), [APIs](../../02-lua-api/inventory/consumption-api.md) | Effects/return versus delayed removal, server/client teardown and Clear distinctions mapped |
| Item save/load and reconstruction | [ITEM-04](../../08-research/investigations/2026-10-11-ITEM-04-persistence-reconstruction.md), [reference](persistence-reconstruction.md) | Selected saved fields, later derived initialization, strict take and pending active-slot restoration mapped |
| Consolidation and bounded audit | [ITEM-05](../../08-research/investigations/2026-10-11-ITEM-05-inventory-consolidation.md), [audit](../../08-research/verification-2026-10-11-v0.1.58.md) | Available-source final step complete; qualifiers retained |

## Effective contracts still open

| Contract | Required evidence |
| --- | --- |
| Installed inventory/loadout policy | Winning pickup/transfer/equipment/loot/consumable helpers and configuration; startup/replacement order and caller/consumer chains |
| NPC authority and readiness | Derived owner event consumers, AI selection, actual ownership/membership/placement/selection convergence and weapon usability |
| Callback delivery and state | Effective named gates/slot/belt hooks, enum-to-shared dispatch/listener order, compile configuration and reentrant/deferred mutation policy |
| Death, removal and cleanup | Derived death/owner teardown, server release and client cleanup convergence, addon ID-keyed metadata removal and casualty/loot duplication policy |
| Item persistence and migration | Effective binders/storage/schema, offline/live state synchronization, applicable derived serializers and restoration ordering under active sections/upgrades |
| Native/profile correspondence | Actual executable/build/configuration and effective winning data/scripts; snapshot date alone is insufficient |

The existing [A-Life/Warfare](../alife/source-completion-status.md) and [persistence](../persistence/source-completion-status.md) source requirements overlap these gaps. Collection uses the existing [effective-profile provenance requirements](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).

## Stopping rule

Mark full installed inventory integration development-reference ready at source level only after relevant effective chains are traced and reconciled with the selected native findings. Runtime remains a separate, explicitly resumed phase with identified build/profile, repeatable acquisition/transfer/placement/activation/use/removal/save-load/level-change observations and recorded outcomes.

Full weapon/animation/physics internals, every item/owner subclass, exhaustive converter/binding/build coverage and malformed-save/relationship robustness are optional later depth unless a concrete modding question requires them. Trade pricing/payment/configuration is the next subsystem, not implicitly completed by inventory GE_TRADE names. [Roadmap](../../ROADMAP.md).
