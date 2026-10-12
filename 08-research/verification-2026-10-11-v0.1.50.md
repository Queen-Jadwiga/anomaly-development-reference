# PER-01 increment verification — v0.1.50

> ADR document set: **v0.1.69**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Scope: selected native single-player A-Life save/load architecture and Lua extension phases
- Source status: source-confirmed within selected bodies; not exhaustive format/compatibility coverage
- Runtime status: untested; deferred until explicitly resumed by the user
- Publication base: v0.1.49, commit `86d71ea7fddef3ca1b9e88583c72d59084b09aca`

## Source review

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee` pins the snapshot. Exact upstream commit/executable/build and effective script correspondence remain unknown.

[PER-01 ledger](../evidence/persistence/native-pipeline-2026-10-11.csv): 24 entries across 24 files, 33 range groups. Read request/delegation, live packet preparation/receipt, compressed writer/validator/reconstruction, selected chunk serializers, group repair, named storage functors, binder default/registration/virtual/error/relevance path, opaque custom data, client quick-load decision and simulator replacement.

Compared these boundaries against active code:

- Save packet entry prepares live state while direct filename save differs; update/save packet consumers are separate.
- Load request checks/options differ from native reconstruction and selected quick-load simulator replacement.
- `.scop` framing, version constant and chunk/field order are documented without treating version predicates as full validation or compatibility proof.
- Native serializer filters and external spawn dependencies remain qualified; no arbitrary Lua-state dump is inferred.
- Native load functor runs early; auxiliary restoration/final registration precede late group repair.
- Binder serialization occurs in custom client data/live spawn, not as a universal world-ready hook; base defaults and exception clearing can matter.
- Supplied hook macro definition does not certify installed binary/functor behavior, script companion-file durability or global dispatch.

[Reference](../04-game-systems/persistence/native-save-load-pipeline.md) and [contracts](../02-lua-api/persistence/native-extension-contracts.md) retain ALIFE-04/06/07 and FAC-02 detailed boundaries. No previous research conclusion is rewritten.

## Repository integrity and preservation

- Compared every local base blob with published v0.1.49 tree; no files deleted.
- Preserved all 28 prior CSV datasets byte for byte, all 41 prior dated investigation bodies except current document-set banners, and all three history snapshots byte for byte.
- Verified 429 hash-bearing evidence rows against retained snapshots: full-file SHA-256, recorded line counts, 566 range groups and recorded symbols. Datasets without compatible path/hash fields remain outside this hash pass; preserved comparisons remain available.
- New ledger symbols also occur within cited ranges. Hash/range validity supplements, rather than proves, semantic interpretation.
- Six unchanged ALIFE-09 catalog outputs match earlier reproduced files; extractor/input scope unchanged.
- Repository checker passed: 158 Markdown files, 1,017 local targets, 14 anchors and zero errors. Checks cover local Markdown targets/anchors, required C-03/C-04/CtZ routes, VERSION/banners, nonempty files, CSV widths and absence of forwarding pages. All seven existing validator tests pass.
- Publish from inspected base tree with expected-head lease; verify full remote path/blob identities, read back increment/VERSION and confirm main head.

## Disposition and limits

PER-01 closes this bounded native pipeline/extension investigation; persistence remains partial. Next PER-02 is supplied Lua storage helper contracts and effective gaps, followed by CtZ campaign identity/reconciliation, consolidation and final available-source audit. All runtime remains deferred. No engine build, gameplay/save edits, source/assets redistribution or license addition. [Roadmap](../ROADMAP.md).
