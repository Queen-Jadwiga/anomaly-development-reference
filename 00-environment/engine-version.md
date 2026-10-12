# Installed engine baseline — ENV-001

> ADR document set: **v0.1.55**. Research revisions and source/build versions below describe their original scope.

**Status:** Runtime-observed from user's X-Ray startup logs. **Baseline:** 2026-10-09.

| Field | Value |
|---|---|
| Game engine | X-Ray Monolith v1.5.3 |
| Engine core | `xrCore` build `9959` |
| Build date | May 15, 2026 |
| Executable flavor | `Modded Exes MT-TEST version 2026.05.15` |
| Distribution context | Anomaly / GAMMA |

### Raw evidence

Three supplied log headers: `xray_erik(20261008-031926).log`, `xray_erik(20261009-005123).log`, `xray_erik(20261009-100733).log` all contain:

```text
'xrCore' build 9959, May 15 2026
Modded Exes MT-TEST version 2026.05.15
X-Ray Monolith v1.5.3
```

These strings are runtime-observed, not proof that the installed binary precisely matches a particular public Git commit. No executable hashes were supplied.

### Compatibility rule

Use the 2026-05-15 build as the conservative cutoff. Changes published after that date must be treated as **not established for this installation** even if they appear on the current GitHub main branch. A later release might contain a previously merged feature, so do not infer availability from release date alone.

### Pending local verification

- Record executable filenames and SHA-256 checksums (no files needed yet).
- Record renderer variant (DX11/DX10 and AVX), installed game/GAMMA version, MO2 profile and Modded Exes package identifier.
- Identify Git source commit matching packaged binaries using historical tags/commits and, if necessary, symbols/PDBs.

### Historical source pin (research update v0.1.2)

Official [2026.5.15 release](https://github.com/themrdemonized/xray-monolith/releases/tag/2026.5.15) points to commit [`6a08e09`](https://github.com/themrdemonized/xray-monolith/commit/6a08e09). This is our **provisional matching source**; exact binary equivalence is still unverified. See [SRC-001](source-baseline-2026-05-15.md).

## 2026-10-11 update — candidate runtime, not yet installed verification

The October 11 compiled release archive and matching-named source ZIP are now supplied. The **preferred source research baseline changes to October 11**, but the last **log-observed installed runtime remains May 15** until a new game session confirms the change. See [SRC-002](source-baseline-2026-10-11.md). Do not mistake this historical ENV-001 record for proof of an October 11 installation.
