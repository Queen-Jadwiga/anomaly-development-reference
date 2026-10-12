# Verification — 2026-10-12 — ADR v0.1.64

> ADR document set: **v0.1.70**. Research revisions and source/build versions below describe their original scope.

- Target revision: v0.1.64, based on main a6adb209565a9ad1b3207b4f187987f2b7926c20
- Scope: GAME-02 selected actor survival/boosters/equipment
- Baseline: ENGINE1011
- Last reviewed: 2026-10-12

## Checks and results

Repository checker passes: **217 Markdown files, 1,610 local targets, 25 anchors, zero errors**. All **10 existing regression tests** pass. All **21 new source rows and 26 cited range groups** pass hash/count/range/cited-symbol checks. Local base files match the published v0.1.63 path/blob map, and preservation checks pass. No independent game runtime ran.

Semantic review separates update gates, raw versus timed modifiers, success versus effect replacement, query versus damage formulas, mitigation versus wear, serialization versus safe repeated load, and source/compiler mismatch versus runtime reports. Scoped medicine search covers all src/xrGame .cpp/.h and bundled gamedata .script files; The 2,770 searched files yield 25 matching lines in ActorCondition.cpp, ActorCondition.h and EntityCondition.h, with no timer decrement/application consumer. Matched readers/writes do not establish one. No engine compilation/runtime ran. Old CSV/history/generated inventories and tool/test implementations remain byte-identical; dated investigation bodies change only current banners.

## Publication verification

Expected-head branch update and complete staged/published blob map required. No CtZ changes or third-party source/assets/license publication.

## Remaining limits

Timed medicine updater, booster accessor/compiler correspondence, effective callbacks/configs/equipment upgrades, derived NPC behavior and full restoration remain open. Runtime deferred; next derived death/condition persistence and consumers.
