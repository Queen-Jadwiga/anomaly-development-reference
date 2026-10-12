# SRC-002 — October 11, 2026 Modded Exes source and runtime candidate

> ADR document set: **v0.1.72**. Research revisions and source/build versions below describe their original scope.

**New preferred source baseline (from 2026-10-11 onward):** user-supplied `xray-monolith-2026.10.11.zip`.

- Source archive SHA-256: `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`
- Compiled release archive: `STALKER-Anomaly-MEXE-oct11.zip`
- Binary package SHA-256: `262ed3892626b3f79d459529288a070e1b10b2577082172de096d3562ccc5e56`
- Source tree root in archive: `xray-monolith-2026.10.11/`
- Repository: https://github.com/themrdemonized/xray-monolith
- Tag-format candidate: `2026.10.11` (local snapshot verified; remote tag/commit not independently verified in this entry).

## Baseline distinction
- **Source-research target:** October 11 source snapshot — confirmed available locally, used for A-01.
- **Runtime adoption candidate:** October 11 compiled archive — uploaded and available, *not* confirmed installed/tested in GAMMA.
- **Previously installed runtime:** MT-TEST 2026.05.15 / xrCore 9959 (log-observed); retain as historical baseline.
- Do not equate the uploaded source snapshot with the exact build of every executable without build provenance or runtime comparison.
- Never backport October 11 Lua exports to May 15 just because they appear in current source.

## Research version policy
For each API result, state the evidence version, source path and line range, registration path where applicable, and whether runtime behavior has been tested. Previous May 15 findings remain historical and may need reconciliation; they are not silently revalidated by changing the source baseline.

## Runtime and feature-version qualification — 2026-10-12

ENGINE1011’s bundled `src/3rd party/luajit-2/src/luajit.h:33–35` declares LuaJIT **2.0.4**, not 2.1. This source header does not identify every user binary; the [external runtime report](reported-gamma-runtime-2026-10-12.md) separately reports the same executable version. Do not use `pairs` iteration order from Lua 5.4/another LuaJIT version as a portable order contract; sort explicitly where order is part of a mod’s design.

October-labeled ADR pages identify their inspected source scope, not feature introduction. Dynamic tabs shipped July 31 and exist in September; the September callback dispatcher differs from October. [REV-01 source/runtime comparison](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md).
