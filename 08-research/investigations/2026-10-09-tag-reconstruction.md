# INV-003 — Map installed executable to historical source tag

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

**Status:** Source release located; binary equivalence unresolved.

## Observations
- User's three log headers identify X-Ray Monolith 1.5.3 / xrCore 9959 / MT-TEST 2026.05.15.
- Official repository has a [2026.5.15 release](https://github.com/themrdemonized/xray-monolith/releases/tag/2026.5.15) displaying commit `6a08e09`.
- [Commit page](https://github.com/themrdemonized/xray-monolith/commit/6a08e09) independently resolves and shows a README-only final commit.

## Conclusion
Use tag `2026.5.15` as **provisional authoritative historical source for research**, not a verified exact match of installed binaries. Full SHA, executable hashes and direct source inspection remain outstanding.

## Follow-up
- Fetch source at tag and index `src` C++ Lua UI bindings.
- Compare build metadata/PDB/release package with actual installed executables when available.
- Track public upstream features introduced after May 15 separately.
