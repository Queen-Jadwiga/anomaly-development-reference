# Configuration/script integration evidence

> ADR document set: **v0.1.75**. Research revisions and source/build versions below describe their original scope.

[Coverage inventory](coverage-inventory-2026-10-12.csv) has 18 rows K01–K18 pinned to ADR v0.1.73 main `6327645f473774753964454c79beabe4f4c2c716`. It hashes full raw documentation bytes, records inclusive selected section ranges/markers, classifies coverage and allocates follow-on work. It is a documentation-inventory schema, not a native source-evidence ledger. Repeated files represent distinct reviewed boundaries; original underlying ledgers and their source/runtime qualifications remain authoritative.

Reproduce hashes/ranges against that immutable ADR commit, not later banner-updated pages. Marker text must occur in its cited range. `outside-reviewed-closure` and `plan-only` do not assert absent engine functionality. Candidate local source paths are presence checks only; no new source artifact or upstream commit pin is introduced. [Investigation](../../08-research/investigations/2026-10-12-CONFIG-01-existing-coverage.md), [inventory](../../04-game-systems/configuration/coverage-inventory.md), [manifest](../manifest.md).

## CONFIG-02 source contracts

[ltx-ini-dltx-2026-10-12.csv](ltx-ini-dltx-2026-10-12.csv): 50 ENGINE1011 rows N01–N28/A01–A20/S01–S02, 21 raw file hashes and 72 inclusive range groups. Standard source-evidence schema; semicolon-separated symbols/ranges. Parser, Lua registration/definitions, ownership/converters and selected bundled defaults are separate evidence layers. [Behavior](../../04-game-systems/configuration/ltx-ini-dltx.md), [API](../../02-lua-api/configuration/ini-api.md), [investigation](../../08-research/investigations/2026-10-12-CONFIG-02-ltx-ini-dltx.md), [verification](../../08-research/verification-2026-10-12-v0.1.75.md). No installed winner or runtime certification.
