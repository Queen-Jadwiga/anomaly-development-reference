# ITEM-01 increment verification — v0.1.54

> ADR document set: **v0.1.70**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Scope: selected native inventory/server/actor/box ownership and Lua request contracts
- Runtime: untested; deferred until explicitly resumed by the user
- Publication base: v0.1.53, commit `95eef88b6b46a9a59109b2314555a042245f7193`

## Source review

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; unknown upstream commit/installed executable correspondence. [New ledger](../evidence/inventory/ownership-lifecycle-2026-10-11.csv): 20 entries across 16 files, 25 range groups. Read selected native Take/DropItem/CanTakeItem, owner and actor overrides, actor and box events, server take/reject/routing and single-player graph-helper callers, live parent/item hooks, Lua methods/registration/declarations/SAFE_WRAP and available-item enumeration/filtering.

Semantic comparison separates server ID containment, live parenting and inventory membership/place; server graph calls versus their deeper effects; event requests versus completion/atomicity; callback point versus subsequent weight/attachment/UI updates; active code versus commented cleanup; available-item list versus raw all-item membership. Native callback exports are not conflated with effective shared-script callbacks. Broader NPC consumers, converter/reentrancy/lifetime certification, equipment internals, consumption/destruction and item reconstruction are outside this pass.

## Preservation and checks

- Compared original local base blobs with inspected published v0.1.53 tree; no base files deleted.
- Preserved 31 prior CSV datasets byte for byte, 45 prior dated investigation bodies except current document-set banners, and all three historical snapshots byte for byte. Source/CtZ files were read only.
- Verified 475 hash-bearing evidence rows against retained sources: full-file SHA-256, recorded counts, 634 range groups and symbols where present. New ledger symbols also occur within cited ranges. Existing datasets without compatible path/hash fields remain outside this hash pass.
- Six unchanged A-Life catalog outputs match earlier reproduced files; no generator/input change.
- Repository checker and seven existing validator tests pass. Checks include local Markdown targets/anchors, C-03/C-04/CtZ routes, VERSION/banners, nonempty files, CSV widths and absence of forwarding pages.
- Publish with expected-head lease; compare full remote path/blob map, read back increment/VERSION and verify main head.

## Disposition

ITEM-01 selected foundation complete within scope; inventory/item lifecycle remains partial. Broader first-edition ADR scope reflects the user's general-modding objective rather than only CtZ. Next ITEM-02 slot/belt/ruck eligibility, movement and active-item/callback transitions; later consumption/destruction/cleanup, persistence and consolidation. Runtime stays deferred. No gameplay/save edits, engine build, redistributed source/assets or license. [Reference](../04-game-systems/inventory/ownership-lifecycle.md), [roadmap](../ROADMAP.md).
