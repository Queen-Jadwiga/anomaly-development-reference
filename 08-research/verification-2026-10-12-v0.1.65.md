# Verification — 2026-10-12 — ADR v0.1.65

> ADR document set: **v0.1.77**. Research revisions and source/build versions below describe their original scope.

- Target revision: v0.1.65, based on main f45d4d00454bece799ae3bcde0bc3d417a4d2f05
- Scope: GAME-03 selected death/condition reconstruction
- Baselines: ENGINE1011/BETA150
- Last reviewed: 2026-10-12

## Checks and results

Repository checker passes: **220 Markdown files, 1,637 local targets, 25 anchors, zero errors**. All **10 existing regression tests** pass. All **19 new source rows and 24 cited range groups** pass hash/count/range/cited-symbol checks. Local base files match the published v0.1.64 path/blob map, and preservation checks pass. No independent game runtime ran.

Semantic review matches derived death call order, virtual actor condition serialization, Entity-before-binder versus CustomMonster-after-binder health writes, server STATE then UPDATE restoration and supplied offline bookkeeping. Prior CSV/history/generated inventories and tool/test implementations remain byte-identical; dated investigation bodies change only current banners. No generator input/implementation changed. No independent runtime or engine compilation ran.

## Publication verification

Use expected main head and compare complete staged/published path/blob map. No CtZ, licenses or third-party source/assets changes.

## Remaining limits

Whole effective profile, all species/loot/casualty handlers, membership/health reconciliation, medicine advance, booster accessor/compiler/reset questions and malformed restoration remain open. Runtime deferred. Next consolidation/audit.
