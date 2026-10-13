# FAC-04 source and repository verification — v0.1.47

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Scope: selected native action-driven goodwill, rank/reputation contributions and Lua value/flag contracts
- Source status: source-confirmed within selected paths; not universal award coverage
- Runtime status: untested; deferred until explicitly resumed by the user
- Publication base: v0.1.46, commit `cba152b994a34209d6e0a5283272f547c10ca0d0`

## Source and semantic review

ENGINE1011 archive SHA-256 `withheld-upload-fingerprint` pins the snapshot; upstream commit/executable/build and effective settings/scripts remain unknown.

[New ledger](../evidence/factions/action-goodwill-2026-10-11.csv): 20 entries across 19 files and 24 range groups. Read Hit/Die callers, fight memory/first-match/expiry, action settings and eligibility, attack/kill/help outcomes, numerical bands/tables/setters, Lua declarations/registrations/receiver checks, relation flags and mask implementation, actor display side effects and device clock.

Reviewed source order and gate nesting, not just identifier occurrence:

- Hit's surviving-victim/live-attacker gate differs from Die's KILL attempt and later object-bound death callback.
- Inventory-owner eligibility differs from actor-only commentary; flags precede branch suppression.
- Attack and kill goodwill exclusions differ; community delta is nested inside nonzero personal delta; reputation and kill rank have separate gates.
- Kill uses current relation despite historical variable/comment wording; rank award uses victim stalker band.
- Actor help is inferred from first-match fight memory; configured deltas/signs and exact elapsed behavior are not installed findings.
- Rank/reputation numerical setters differ from goodwill clamps and contribute through directed tables.
- Literal zero kill action plus mask implementation does not set an independent kill bit; flags are not award receipts or counted histories.
- Offline server death/script bookkeeping does not prove native live Hit/Die traversal.

See the [reference](../04-game-systems/factions/action-goodwill.md), [API contracts](../02-lua-api/factions/action-values-api.md) and [FAC-04](investigations/2026-10-11-FAC-04-action-goodwill.md). No reproduced bug or tuning recommendation is claimed.

## Integrity and preservation

- Compared every local base blob with published v0.1.46 tree. No files deleted.
- Preserved all 26 prior CSV datasets byte for byte, all 38 dated investigation bodies except current document-set banners, and all three history snapshots byte for byte.
- Verified 385 hash-bearing evidence rows against retained snapshots: full-file SHA-256, recorded line counts, 501 range groups and symbols where present. Datasets without compatible path/hash fields remain outside this hash pass; existing comparisons remain preserved.
- New ledger symbols occur inside their cited ranges. Valid ranges/hashes are supplemented by the semantic review above.
- Six unchanged ALIFE-09 catalog outputs match the earlier reproduced files; extractor/input scope is unchanged.
- Repository checker passed: 146 Markdown files, 849 local targets, 14 anchors and zero errors. Checks cover Markdown targets/anchors, required C-03/C-04/CtZ navigation, VERSION/banners, nonempty files, CSV widths and absence of forwarding pages. Seven existing validator tests pass.
- Publish with inspected base tree and expected-head lease; compare full remote path/blob identities, read back the increment/VERSION and verify main points to the intended commit.

## Limits and disposition

FAC-04 completes this bounded native pass; factions remains partial. Next is supplied Warfare relation consumers and effective-script boundaries, then consolidation/audit. Installed diplomacy, rank/reputation/reward configuration, additional action paths, converter behavior, online/offline convergence and runtime timing remain open. No engine build, gameplay edits, third-party source/assets distribution, license addition or in-game verification. [Roadmap](../ROADMAP.md).
