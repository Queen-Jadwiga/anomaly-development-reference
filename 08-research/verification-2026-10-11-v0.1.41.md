# ADR verification — v0.1.41

> ADR document set: **v0.1.47**. Research revisions and source/build versions below describe their original scope.

**Date:** 11 October 2026. **Starting commit:** `5d069de0957ba1000bb7637043476dc52503c031` (v0.1.40). **Scope:** canonical-tree cleanup, version semantics, documentation integrity and reproducibility. All engine/game runtime testing remains deferred.

## Cleanup and version rules

- Deleted all 22 Markdown forwarding pages, including the former `04-game-systems/warfare/ctz-integration-boundary-oct11.md`. WAR-001 now has one canonical [investigation](investigations/2026-10-11-WAR-001-ctz-integration-boundary.md). Old URLs remain recoverable from Git history; they no longer resolve on current `main`.
- Replaced append-only root index/roadmap with current navigation and scope. Their former content and the evolving README are retained as visibly marked historical snapshots under `08-research/history/`; the old root `HISTORY_README.md` is removed.
- `VERSION` declares the current ADR document set. Every current Markdown page carries the same banner. Research revisions (for example ALIFE-09's v0.1.39), policy adoption dates, historical changelog versions, engine tags and CtZ Alpha 0.0.5j retain their distinct meaning. They are not replaced with the ADR version.
- Changelog entries now appear in descending revision order; original entry text is retained.
- Research findings were not rewritten. After removing only the new version banner, 106 original Markdown bodies were initially identical; further changes are confined to maintenance guidance, navigation and test documentation.

## Checks performed

| Check | Result |
| --- | --- |
| Markdown paths and anchors | All current/historical pages checked, including C-03/C-04 and canonical WAR-001; zero errors |
| Forwarding pages, versions, empty files, CSV row width | Zero errors; enforced by the updated checker |
| CSV preservation | All 20 pre-existing CSV blobs retain their original Git blob SHA, schemas and bytes |
| A-Life/Warfare source ledgers | 227 path/hash/line-count entries verified against locally available declared snapshots; 252 cited ranges within file bounds |
| A-Life catalog rebuild | Five CSVs and statistics JSON match published output byte for byte after fixing generator line endings to LF |
| Catalog scope | 21 registrar files; 84 class rows; 1,150 binding rows; 174 helper declarations; 1,372 named script declarations; 73 input files |
| Validator regression tests | Seven tests pass: valid repository, missing file, missing anchor, root escape, stale version, obsolete forwarding page, malformed CSV |
| CtZ repository | Public repository and branch head checked: `eba6660db09353dcc42a195ae6e7e706f4762277`; no CtZ modifications |

The catalog row counts remain occurrences/declarations within their documented extraction scope, not an exhaustive count of runtime APIs. Range/hash checks do not prove claim interpretation or installed execution. The uploaded engine snapshot's exact upstream commit and correspondence with the executable remain unknown.

## Repeatable checks

```bash
python tools/check_repository.py
python -m unittest discover -s tests -p 'test_*.py'
python tools/build_alife_catalog.py --source-root PATH_TO_ENGINE_SNAPSHOT --warfare-root PATH_TO_BETA150 --repo-root PATH_TO_TEMP_OUTPUT
```

Compare the resulting `02-lua-api/alife/` CSVs/statistics and `evidence/alife/interface-evidence-oct11.csv` byte for byte with the repository. This generator needs the source snapshots and C preprocessor described in its catalog; it does not compile the engine.

## Publication and limits

Publication uses the inspected base tree and a branch-head lease. Verify the resulting tree's complete path/blob map, all deleted paths and the published branch head. No license, source archive, game asset or compiled executable is added.

This pass verifies documentation integrity, recorded source references and catalog stability. It does not establish every historical external URL's availability, complete API/converter coverage, effective GAMMA module order or runtime behavior. Those qualifications and the current effective-source gaps remain explicit in the [roadmap](../ROADMAP.md).
