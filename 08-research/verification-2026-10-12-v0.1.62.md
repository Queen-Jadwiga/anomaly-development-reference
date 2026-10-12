# Verification — 2026-10-12 — ADR v0.1.62

> ADR document set: **v0.1.80**. Research revisions and source/build versions below describe their original scope.

- Target ADR revision: v0.1.62, based on main 7145b9d7107fa38005d8dd66c30a1fda1a8e70a0
- Changed scope: ECO-03 consolidation and bounded available-source economy audit
- Source baseline IDs: ENGINE1011/BETA150/ZIP142
- Last reviewed: 2026-10-12

## Semantic audit

| Audit group | Reconciled contracts | Evidence / outcome |
| --- | --- | --- |
| Account owner and persistence | Live m_money, GE_MONEY server m_dwMoney, custom/STATE serialization and specific trader spawn | E01–E08/E23; retained distinct layers; zero-delta event wording clarified |
| Quote and direction | Virtual cost, pThis buy/sell, directed attitude, script discounts and disabled/zero early returns | E10–E14/E20/E22; no complete NPC quote or numeric-safety promise; zero quote is not direct native refusal |
| UI and event phases | Eligibility, signed projections, aggregate/per-item callbacks, end money sync and donation | E14–E19/E21; threshold equality clarified; no settlement receipt or atomic batch inferred |
| Policy and native supplies | Local/global/default factors, constructor names/order, void overloads, selective destruction and random spawn requests | T01–T15; destructive reroll, inactive deficit branch and initialization/lifetime limits retained |
| Supplied Lua and missing inputs | Captured timestamp wrapper, nearby update requester, NPC stock/money loops, Warfare profiles/UI values | T16–T21 and scoped inventory; core managers/configs and installed order still missing |
| Cross-system mod design | Inventory acceptance, faction attitude and save reconstruction versus strategic accounts | Existing references linked; inferred order/reconciliation guidance labelled as design, no tested code supplied |

The audit is bounded to the cited selected contracts; it is not every engine economy path. Source caveats remain source findings rather than reported runtime faults.

## Integrity and checks

Repository checker passes: **207 Markdown files, 1,538 local targets, 24 anchors, zero errors**. All **10 existing regression tests** pass. All **44 economy source rows and 63 cited range groups** pass full-file hash, line-count, range and cited-symbol checks. The three scoped package inventories reproduce counts/digests and absent manager/profile results. Base local files match the published v0.1.61 path/blob map; preservation checks pass. No generator inputs or implementation changed, so unchanged generated inventories were compared byte-for-byte rather than regenerated.

Earlier economy/evidence CSVs, scope JSON, generated inventories, tool/test implementations and history snapshots remain byte-identical. Dated investigation bodies change only current revision banners. Corrections to current ECO-01/API phrasing are identified in ECO-03 and this report. No new generator/data schema, source baseline, third-party source/assets, licenses or CtZ files are introduced.

## Publication verification

Use expected-head branch update; compare the complete staged and published path/blob map and final main head. The publication commit identifies this verification report; no future SHA is invented.

## Remaining limitations

Missing installed managers/configuration/gates/discounts/timer reconstruction and effective patch order keep full integration partial. Numeric/reentrant recovery, transfer/destroy/spawn convergence, executable correspondence and runtime observations remain open. Independent engine/game runtime is untested and deferred. Available-source economy work is complete within scope; next actor/NPC gameplay state.
