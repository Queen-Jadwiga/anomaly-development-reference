# SRC-001 — Official May 15, 2026 source baseline

> ADR document set: **v0.1.77**. Research revisions and source/build versions below describe their original scope.

**Finding:** Official GitHub release [`2026.5.15`](https://github.com/themrdemonized/xray-monolith/releases/tag/2026.5.15) exists. Its displayed target commit is [`6a08e09`](https://github.com/themrdemonized/xray-monolith/commit/6a08e09). Release published May 15, 2026, 05:37 (GitHub displayed timestamp; timezone not confirmed).

**Installed log baseline:** `Modded Exes MT-TEST version 2026.05.15`, `xrCore build 9959, May 15 2026`, `X-Ray Monolith v1.5.3` (see engine-version.md).

**Evidence assessment:** *Release/tag confirmed; binary-to-source identity NOT verified.* The matching calendar date and MT distribution make the official release the preferred initial source baseline. Confirmation requires installed binary checksum comparison or reproducible build/symbol evidence. Do not equate matching banner strings with byte-identical executables.

**Git pinning commands (when network access available):**

```bash
git clone https://github.com/themrdemonized/xray-monolith.git
cd xray-monolith
git fetch --tags
git checkout --detach 2026.5.15
git rev-parse HEAD
```

Expected short prefix from official release page: `6a08e09`. Capture the *full* SHA locally rather than inventing it.

**Useful pinned browsing links:**
- [Release](https://github.com/themrdemonized/xray-monolith/releases/tag/2026.5.15)
- [Commit](https://github.com/themrdemonized/xray-monolith/commit/6a08e09)
- [Repository at tag](https://github.com/themrdemonized/xray-monolith/tree/2026.5.15)
- [Compare prior release](https://github.com/themrdemonized/xray-monolith/compare/2026.5.12...2026.5.15)

**Release-specific change:** The May 15 release credits PR #532 with exported functions for `physics_shell` and `CUIProgressBar`, as well as a change to `xr_combat_ignore.script`. This establishes release-note evidence, **not** the actual Lua signatures or in-game compatibility. [Release notes](https://github.com/themrdemonized/xray-monolith/releases/tag/2026.5.15) and [PR #532](https://github.com/themrdemonized/xray-monolith/pull/532).

**Post-baseline exclusion examples:** The project's changelog dates PDA context menu additions to July 6, 2026 and script/shader messaging to September 12, 2026. These must NOT enter our May 15-compatible catalog without separate verification. [Maintainer README](https://github.com/themrdemonized/xray-monolith).

**Known research limitation:** The GitHub release and commit pages were reviewed; a full checkout and line-level inspection of the historical tree were not possible in this research environment. C++ binding signatures remain pending.
