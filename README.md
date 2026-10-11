# Anomaly Development Reference (ADR)

**Source-backed modding research for S.T.A.L.K.E.R. Anomaly / X-Ray Monolith / Modded Exes**

> **Work in progress — independent research, not official engine documentation.**
> Current ADR revision: **v0.1.30** (11 October 2026). Primary research source: the
> **2026.10.11** X-Ray Monolith source archive. Runtime behavior in GAMMA is **not yet validated**.

## What is this?

A version-aware development reference produced while researching the **Capture the Zone (CtZ)**
mod. Its purpose is to make native engine and Lua behavior traceable to source code,
document ownership and lifecycle rules, and keep unknowns visible rather than guessing.

It is **not** the game mod itself, nor a replacement for the X-Ray source or official documentation.

## Capture the Zone mod

The [Capture the Zone (CtZ) repository](https://github.com/Queen-Jadwiga/capture-the-zone)
contains the mod files for **Alpha 0.0.5j — Revised Fixed Bars / Advantage Marker**,
with its original build documentation and assets.

## Recommended quick review

If you only have a few minutes, start here:

| Topic | Why read it? |
| --- | --- |
| [C-03 — Luabind and native UI ownership](08-research/investigations/2026-10-11-C03-luabind-adoption-autodelete.md) | `adopt<2>()` versus native `AutoDelete` — see research index for the exact C-03 record |
| [C-04 — XML factory return ownership](08-research/investigations/2026-10-11-C04-xml-factory-return-ownership.md) | How XML-created control pointers are owned and returned |
| [UI construction & ownership](03-ui-pda/ui-construction-ownership.md) | Practical consequences for XML-created controls and native parent ownership |
| [Dynamic PDA tabs](03-ui-pda/dynamic-pda-tabs-oct11.md) | New native-backed PDA tab registration and Lua integration |
| [PDA subdialog lifecycle](03-ui-pda/pda-subdialog-lifecycle-oct11.md) | Rebuild, selection, and content synchronization |
| [Verification report](08-research/verification-2026-10-11-v0.1.30.md) | What was checked and what was not |
| [Full research index](INDEX.md) | Every investigated area and historic records |

## Research status

- **UI/PDA:** development-reference ready at source level; native ownership, XML/DXML,
  widget exports, input, fonts, scaling, rendering, and dynamic tabs investigated.
- **A-Life / Warfare:** still being researched.
- **October 11 executable in GAMMA:** candidate target; runtime compatibility and behavior
  are unverified.
- **Source-level limits:** some exhaustive export, indirect event, configuration, and
  cross-addon questions remain open; see [ROADMAP.md](ROADMAP.md).

## Evidence conventions

- **Source-verified:** supported by a specified source path and implementation.
- **Scoped source audit:** supported within an explicitly bounded search; not an engine-wide proof.
- **Hypothesis / open:** further evidence required.
- **Runtime pending:** source research sufficient for now; actual in-game behavior not yet tested.

Claims should not be promoted to runtime-verified without testing.

## Repository navigation

- [Full index](INDEX.md)
- [Research roadmap and open work](ROADMAP.md)
- [Environment and source baselines](00-environment/)
- [Engine architecture](01-engine/)
- [Lua API reference](02-lua-api/)
- [UI / PDA reference](03-ui-pda/)
- [Game systems](04-game-systems/)
- [Research and verification](08-research/)
- [Changelog](CHANGELOG.md)
- [Original evolving README / version history](HISTORY_README.md)

## Publishing

See [publishing instructions](PUBLISHING.md) for GitHub Desktop or Git CLI.

## Feedback welcome

For an engine developer reviewing this guide, the most helpful feedback would be:

1. Are the Luabind/UI ownership conclusions correct, particularly the distinctions between
   Lua userdata ownership and native `AutoDelete`?
2. Have we overlooked supported engine interfaces or intended usage patterns, especially for
   dynamic PDA tabs?
3. Are there sections likely to mislead modders despite being source-referenced?

Please reference the specific Markdown file and line or open a GitHub Issue.

## Attribution and scope

X-Ray Monolith / Modded Exes and Anomaly are third-party projects. This repository contains
independent research and source references; it does **not** redistribute the engine sources
or the compiled executables. No upstream endorsement is implied.
