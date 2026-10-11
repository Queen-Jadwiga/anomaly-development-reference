# FAC-03 source and repository verification — v0.1.46

> ADR document set: **v0.1.54**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Scope: character-community mutation, live team/group effects and selected server transfer/reconstruction
- Source status: source-confirmed within selected definitions/registrations; not all entity types or installed policies
- Runtime status: untested; deferred until explicitly resumed by the user
- Publication base: v0.1.45, commit `da1b1557e56b53849ff7a6a84db7c367017a52ac`

## Source and semantic review

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee` pins the retained snapshot; upstream commit, actual executable/build and effective script/configuration correspondence remain unknown.

The [FAC-03 ledger](../evidence/factions/community-mutation-2026-10-11.csv) covers 19 files and 34 range groups. Read signatures/registrations, configured community lookup, Lua setter and inventory-owner bridge, character-info mutation/hydration, entity migration, hierarchy member/shared memory/agent helpers, selected stalker/base-monster overrides, tuple exports/imports and server receipt, guarded trader community state/getter, actor display side effect.

Compared source order and these boundaries:

- Inner alive-only team migration retains current squad/group; outer wrapper separately requests supplied values. Same-tuple no-op and possible two migrations are distinct.
- Live community/sympathy change precedes trader write; early returns and assertions do not create atomic success/rollback.
- Hierarchy and agent/shared-senses membership differ from A-Life group/strategic squad assignment.
- Team-only wrapper differs from community mutation; integer native fields differ from byte binding/packet representation.
- Direct trader community write differs from later creature tuple update receipt; serialization does not certify immediate save synchronization.
- Spawn hydration and monster species team handling are separate; remote tuple assignment does not invoke the same shown migration hooks.
- Actor faction RPC body updates Discord display through a script producer; no universal strategic/UI completion follows.

These are bounded source contracts in the [reference](../04-game-systems/factions/community-mutation.md) and [API](../02-lua-api/factions/community-mutation-api.md), not reproduced defects, tuning instructions or runtime tests.

## Integrity, preservation and publication

- Compared every base snapshot blob with the published v0.1.45 tree. No repository files deleted.
- Preserved all 25 prior CSV datasets byte for byte, all 37 dated investigation bodies except current document-set banners, and all three historical snapshots byte for byte. Current FAC-01 API now links the completed separate FAC-03 contracts rather than leaving its earlier untraced status current.
- Verified 365 hash-bearing evidence rows against retained source snapshots: full-file SHA-256, recorded line counts, 477 range groups and recorded symbols. Datasets without compatible path/hash fields are outside this hash pass; preserved comparison datasets remain available.
- New ledger symbols also occur within cited range groups. Structural validity is supplemented by the semantic source-order review above.
- Six ALIFE-09 catalog outputs remain unchanged and match the earlier reproduced outputs; extractor/input scope is unchanged.
- Repository checker passed: 142 Markdown files, 810 local targets, 14 anchors and zero errors. Checks cover local Markdown targets/anchors, required C-03/C-04/CtZ routes, current VERSION/banners, nonempty files, CSV widths and absence of forwarding pages. All seven existing validator tests pass.
- Publish using the inspected base tree and expected-head lease; compare the full remote path/blob map, read back the increment and VERSION, and verify the main head.

## Disposition and limits

FAC-03 is complete within its selected native chain. Factions remains partial: action-driven goodwill/rank/reputation is next; effective disguise/true-community policy, Warfare strategic reassignment and diplomacy overrides remain open. Runtime stays deferred. No gameplay edits, engine build, third-party source/assets distribution or license addition. [Roadmap](../ROADMAP.md).
