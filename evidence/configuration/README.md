# Configuration/script integration evidence

> ADR document set: **v0.1.81**. Research revisions and source/build versions below describe their original scope.

[Coverage inventory](coverage-inventory-2026-10-12.csv) has 18 rows K01–K18 pinned to ADR v0.1.73 main `6327645f473774753964454c79beabe4f4c2c716`. It hashes full raw documentation bytes, records inclusive selected section ranges/markers, classifies coverage and allocates follow-on work. It is a documentation-inventory schema, not a native source-evidence ledger. Repeated files represent distinct reviewed boundaries; original underlying ledgers and their source/runtime qualifications remain authoritative.

Reproduce hashes/ranges against that immutable ADR commit, not later banner-updated pages. Marker text must occur in its cited range. `outside-reviewed-closure` and `plan-only` do not assert absent engine functionality. Candidate local source paths are presence checks only; no new source artifact or upstream commit pin is introduced. [Investigation](../../08-research/investigations/2026-10-12-CONFIG-01-existing-coverage.md), [inventory](../../04-game-systems/configuration/coverage-inventory.md), [manifest](../manifest.md).

## CONFIG-02 source contracts

[ltx-ini-dltx-2026-10-12.csv](ltx-ini-dltx-2026-10-12.csv): 50 ENGINE1011 rows N01–N28/A01–A20/S01–S02, 21 raw file hashes and 72 inclusive range groups. Standard source-evidence schema; semicolon-separated symbols/ranges. Parser, Lua registration/definitions, ownership/converters and selected bundled defaults are separate evidence layers. [Behavior](../../04-game-systems/configuration/ltx-ini-dltx.md), [API](../../02-lua-api/configuration/ini-api.md), [investigation](../../08-research/investigations/2026-10-12-CONFIG-02-ltx-ini-dltx.md), [verification](../../08-research/verification-2026-10-12-v0.1.75.md). No installed winner or runtime certification.

## CONFIG-03 loading and callbacks

[script-loading-callbacks-2026-10-12.csv](script-loading-callbacks-2026-10-12.csv): 35 ENGINE1011 rows N01–N22/S01–S13, 14 raw file hashes/47 inclusive range groups, standard source-evidence schema. [Scope JSON](script-source-scope-2026-10-12.json) covers requested filenames in 161 engine gamedata files and records five standalone dispatcher events. CONFIG-01 K08 and WORLD-04 C12 six-name subjects remain historical bytes and are explicitly corrected by the [new investigation](../../08-research/investigations/2026-10-12-CONFIG-03-script-loading-startup-callbacks.md). Conditional debug-global loading is distinct from installed winner/alias proof. [Behavior](../../04-game-systems/configuration/script-loading-startup-callbacks.md), [API](../../02-lua-api/configuration/script-callback-api.md), [verification](../../08-research/verification-2026-10-12-v0.1.76.md).

## CONFIG-04 consumers and consolidated audit

[supplied-options-patches-2026-10-12.csv](supplied-options-patches-2026-10-12.csv): 29 rows B01–B14/P01–P02/E01–E12/N01, ENGINE1011/BETA150 main/explicit optional paths, 15 files/37 ranges; standard source-evidence schema. [Comparisons](package-comparison-2026-10-12.csv) record five equal results across seven raw-file/normalized-method-slice checks. Slice normalization is cp1251 decode and CRLF→LF only, bounded by GetValue and OnKeyboard markers; it is not full-file/profile equivalence. [Scope](supplied-source-scope-2026-10-12.json) records ENGINE1011 gamedata 161 files/full BETA150 62/ZIP142 gamedata 29 and 13 main preset includes, four present there. No installed absence/winner follows.

[CONFIG-04 investigation](../../08-research/investigations/2026-10-12-CONFIG-04-consumers-consolidation-audit.md), [consumer reference](../../04-game-systems/configuration/supplied-options-patches.md), [guide](../../04-game-systems/configuration/development-reference.md), [bounded audit](../../08-research/verification-2026-10-12-v0.1.77.md). CONFIG-02–04 audit covers 114 source rows/156 ranges and the original 18 CONFIG-01 documentation pins. Prior raw ledgers and five-event correction remain authoritative.
