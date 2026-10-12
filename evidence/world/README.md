# World coverage evidence

> ADR document set: **v0.1.82**. Research revisions and source/build versions below describe their original scope.

- [WORLD-01 coverage inventory](coverage-inventory-2026-10-12.csv): 14 rows indexing existing ADR documents at v0.1.69 main `6ab1f93634f54ccc40dfe3fe33b716114a62157e`.

Schema: `coverage_id,area,coverage_status,reference_path,reference_sha256,line_ranges,marker,retained_boundary,next_trace,planned_step`. Paths are repository-relative; SHA-256 values pin complete original document bytes at that immutable ADR commit, and line ranges/markers locate the reviewed section. They intentionally differ from current document hashes after banner updates. `planned_step` is a research allocation, not proof of source implementation. Labels are explained in the [inventory](../../04-game-systems/world/coverage-inventory.md).

This is a documentation-coverage ledger, not the claim-oriented native source-ledger schema. Original linked engine/package ledgers remain authoritative and unchanged. New raw source claims will need their own source evidence once traced. [WORLD-01 research](../../08-research/investigations/2026-10-12-WORLD-01-existing-coverage.md), [manifest](../manifest.md), [policy](../../08-research/evidence-policy.md).

[WORLD-02 spatial/contracts ledger](spatial-contracts-2026-10-12.csv): P01–P40, ENGINE1011, standard eight-column claim schema; selected queries, relocation, restrictions, patrols, converter and callers. [Behavior](../../04-game-systems/world/spatial-queries-relocation.md), [investigation](../../08-research/investigations/2026-10-12-WORLD-02-spatial-contracts.md). Original coverage inventory bytes remain preserved.

[WORLD-03 interaction/transition/marker ledger](interaction-transition-markers-2026-10-12.csv): U01–U16, T01–T13, M01–M19, ENGINE1011 standard claim schema; selected native and bundled relay evidence. [Behavior](../../04-game-systems/world/interaction-transitions-markers.md), [research](../../08-research/investigations/2026-10-12-WORLD-03-interaction-transitions-markers.md).

[WORLD-04 consumer ledger](supplied-consumers-2026-10-12.csv): C01–C13/S01–S13/Z01; standard claim schema across ENGINE1011/BETA150/ZIP142. [Scope/file hashes](supplied-scope-2026-10-12.json) inventory the selected gamedata roots and requested filename presence, excluding installation and other patch folders. [Comparison table](package-comparison-2026-10-12.csv) has left/right source/path/SHA-256, comparison_scope, equal and qualification columns: full raw bytes versus normalized selected slices are explicitly distinct. [Research](../../08-research/investigations/2026-10-12-WORLD-04-consumers-consolidation-audit.md), [audit](../../08-research/verification-2026-10-12-v0.1.73.md). Prior coverage/source ledgers retain their original bytes and IDs.
