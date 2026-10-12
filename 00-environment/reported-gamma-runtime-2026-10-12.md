# ENV-RT01 — External GAMMA runtime report

> ADR document set: **v0.1.68**. Research revisions and source/build versions below describe their original scope.

- Report received/reviewed: 2026-10-12
- Reporter: GitHub `devinhorowitz`; [issues 1–4](https://github.com/Queen-Jadwiga/anomaly-development-reference/issues)
- Evidence status: external runtime observations; no independent ADR game reproduction

Issues #1 and #4 identify a Modded Exes build compiled **2026-09-20**, described as **SSS24 RC2**, with exports reportedly matching tag **2026.9.12**, LuaJIT **2.0.4**, and September 12 Modded Exes gamedata. Issue #2 separately identifies a build from the September source with GAMMA and MAC’s full eight-tab `pda_16.xml`; do not infer a fully identical executable/profile from that wording.

The exact executable SHA-256, complete GAMMA/MO2 profile, winning addon/script hashes, raw crash logs, probe source and `.scop` bytes were not attached to these issue reports at review. Offsets are reported addresses, not symbols independently resolved by the ADR. Preserve this as a **reported build**, not a new pin for the user’s installation or the uploaded October archive.

For independent source comparison, upstream tag `2026.9.12` resolves to commit `9b491ffbfe5d529e817ceffed70214d0f03f62c5`. Retrieved September registry/dispatcher/native-export files are hashed in the [source ledger](../evidence/runtime/issue-review-source-2026-10-12.csv); this commit does not identify the reported compiled executable. ENGINE1011 remains the separately pinned uploaded October archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`.

[Review and issue disposition](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md) · [reported observations](../evidence/runtime/reported-observations-2026-10-12.csv).
