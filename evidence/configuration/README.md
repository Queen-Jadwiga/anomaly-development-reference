# Configuration/script integration evidence

> ADR document set: **v0.1.74**. Research revisions and source/build versions below describe their original scope.

[Coverage inventory](coverage-inventory-2026-10-12.csv) has 18 rows K01–K18 pinned to ADR v0.1.73 main `6327645f473774753964454c79beabe4f4c2c716`. It hashes full raw documentation bytes, records inclusive selected section ranges/markers, classifies coverage and allocates follow-on work. It is a documentation-inventory schema, not a native source-evidence ledger. Repeated files represent distinct reviewed boundaries; original underlying ledgers and their source/runtime qualifications remain authoritative.

Reproduce hashes/ranges against that immutable ADR commit, not later banner-updated pages. Marker text must occur in its cited range. `outside-reviewed-closure` and `plan-only` do not assert absent engine functionality. Candidate local source paths are presence checks only; no new source artifact or upstream commit pin is introduced. [Investigation](../../08-research/investigations/2026-10-12-CONFIG-01-existing-coverage.md), [inventory](../../04-game-systems/configuration/coverage-inventory.md), [manifest](../manifest.md).
