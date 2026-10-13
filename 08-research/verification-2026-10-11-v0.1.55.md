# ITEM-02 increment verification — v0.1.55

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Scope: focused placement/active-slot transitions, Lua producers and selected actor consumers
- Runtime: untested; deferred until explicitly resumed by the user
- Publication base: v0.1.54, commit `1e6da02f3b88a92c1a4882c9b23c956328360760`

## Source review

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit/executable/profile correspondence unknown. [New ledger](../evidence/inventory/placement-activation-2026-10-11.csv): 19 entries across 14 files, 24 range groups. Read native placement predicates/mutators/defaults, base/stalker owner predicate boundary, callbacks/compile guard, requested/current Activate/Update, minimal HUD activation/hidden producers, Lua declaration/registration/request payload, server routing and actor consumers.

Compared placement pointers and metadata at callback time, activation request versus current slot, ordinary Update versus forced direct assignment, native defaults versus Lua arguments, active versus commented preflight and named hooks versus native enum callbacks. Selected actor consumer is not promoted to effective NPC loadout/readiness evidence. This is not exhaustive NPC event/AI, converter/reentrancy, animation/weapon, blocking restoration or runtime certification.

## Preservation and checks

- Compared every original local base blob to inspected published v0.1.54 tree; no base files deleted.
- Preserved 32 prior CSV datasets byte for byte, 46 prior dated investigation bodies except current document-set banners, and all three historical snapshots byte for byte. Source/CtZ files were read only.
- Verified 494 hash-bearing evidence rows: full-file SHA-256, recorded line counts, 658 range groups and symbols where present. New symbols also occur in cited ranges. Original datasets without compatible path/hash columns remain outside this pass.
- Six unchanged A-Life catalog outputs match earlier reproduced files; no generator/input-scope change.
- Repository checker and seven existing validator tests pass. Checks cover local Markdown targets/anchors, C-03/C-04/CtZ routes, VERSION/banners, CSV widths, nonempty files and forwarding-page absence.
- Publication uses expected-head lease; compare full remote path/blob map, read back new increment/VERSION and verify main head.

## Disposition

ITEM-02 complete within focused source scope; inventory partial. Relevant CtZ equipment boundaries are documented without a verified NPC API recipe. Next consumption/destruction and owner cleanup, then item persistence and consolidation. Runtime remains deferred; no gameplay/save/source edits, engine build, source/assets redistribution or license. [Reference](../04-game-systems/inventory/placement-activation.md), [roadmap](../ROADMAP.md).
