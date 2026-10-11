# FAC-01 source and repository verification — v0.1.44

> ADR document set: **v0.1.45**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Scope: native faction identity/query foundations and selected Lua contracts
- Source status: source-confirmed within selected definitions/registrations; not exhaustive
- Runtime status: untested; deferred until explicitly resumed by the user
- Publication base: v0.1.43, commit `ea0f10ca84213544a64720953c48a0b867d0e273`

## Inputs and claim review

ENGINE1011 is pinned by archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit, installed executable/configuration and effective GAMMA overrides remain unknown. No third-party source/configuration assets are published.

FAC-01's [18-file ledger](../evidence/factions/native-relations-2026-10-11.csv) covers community/INI loaders, relation registry, selected client declarations/wrappers/registrations, module helpers and stalker/trader/base virtual paths. Reviewed direction, storage, fallback, threshold boundaries, aggregation terms, selected mutation/limit paths, type requirements and argument order. The [reference](../04-game-systems/factions/native-relations.md) and [API](../02-lua-api/factions/relations-api.md) distinguish character identity, directed contributions, derived attitude, monster fallback and strategic owner state.

Key semantic checks: matrix setter writes one cell; community goodwill storage is target-owned; object general-goodwill adds five terms while module ID aggregate adds three; relation preset writes personal goodwill without compensation; force-set subtracts two community terms while bypassing the selected clamp. Live-object relation dispatch is not universally the mutual `GetRelationBetween` helper. Installed thresholds/values and all derived overrides are not asserted.

## Integrity and preservation

- Compared the complete local v0.1.43 base snapshot's blob hashes with its published Git tree before evaluating the increment. No files deleted.
- Preserved all 23 prior CSV blobs byte for byte, all 35 prior investigation bodies except current document-set banners, and all three history snapshots byte for byte. A-Life/Warfare practical-reference bodies retain their findings and completion limitations.
- Verified 328 hash-bearing ledger rows against retained snapshots: full-file SHA-256, recorded line counts, 417 range groups and symbols where recorded. Datasets without compatible path/hash fields are outside this check; preserved comparison datasets remain available.
- New FAC-01 ledger: 18 entries across 18 files, 32 range groups. Reviewed selected signatures, registrations and consumers; hash/range validity alone is not semantic proof.
- Six ALIFE-09 catalog files remain unchanged and match the outputs reproduced during v0.1.43. No extractor/input scope changed in this increment.
- Repository checker passed with 135 Markdown files, 738 local targets, 14 anchors and zero errors. It validates Markdown targets/anchors, required C-03/C-04/CtZ routes, document-set version/banner consistency, CSV widths, nonempty files and absence of forwarding pages. All seven existing negative/positive validator tests pass.
- Publish from the inspected tree with an expected-head lease; compare the full remote path/blob map, read back the new reference/API/investigation/ledger and verify published main head.

## Limits and disposition

FAC-01 is complete within its native query-foundation scope. Factions/relations remains partial: persistence/reset/ID cleanup is next, with community mutation, action-driven goodwill, Warfare consumers and installed diplomacy subsequently open. No arbitrary-input/nil converter safety, AI refresh timing, callbacks, save durability or installed faction values are certified. No engine build, gameplay edit, license addition or runtime test occurred. The [roadmap](../ROADMAP.md) records this scope alongside the unchanged A-Life/Warfare effective-source backlog.
