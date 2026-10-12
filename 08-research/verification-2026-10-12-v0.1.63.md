# Verification — 2026-10-12 — ADR v0.1.63

> ADR document set: **v0.1.65**. Research revisions and source/build versions below describe their original scope.

- Target ADR revision: v0.1.63, based on main 8fb8b70890311609c402435bcbfe4f46677db2f8
- Changed scope: GAME-01 base condition/live hit and focused Lua contracts
- Source baseline: ENGINE1011
- Last reviewed: 2026-10-12

## Checks and results

Repository checker passes: **213 Markdown files, 1,578 local targets, 25 anchors, zero errors**. All **10 existing regression tests** pass. All **21 new source rows and 25 cited range groups** pass hash/count/range/cited-symbol checks. Local base files match the published v0.1.62 path/blob map, and preservation checks pass. No independent game runtime ran.

Semantic comparison covers direct assignment/queued deltas, first invalid-time reset, branch immunity/callback order, actor override limits and death request/event versus cleanup. Existing faction/consumption/offline-casualty findings are linked without broadening their scope. Previous CSVs/history/generated outputs and tool/test implementations stay byte-identical; dated investigation bodies change only current banners. No generator/input change requires catalog regeneration.

## Publication verification

Use expected main head and verify complete staged/published path/blob map. No third-party source/assets, licenses or CtZ changes.

## Limits

Actor/equipment/booster internals, derived death and complete condition persistence, installed scripts/config/build correspondence and runtime remain open. This is the first gameplay-state source pass, not a tested damage/kill/healing recipe.
