# CONFIG-02 — LTX/INI and selected DLTX contracts

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-02
- Subsystem: configuration/script integration
- ADR revision: v0.1.75
- Record status: complete-within-scope; effective installed integration partial
- Source status: source-confirmed selected ENGINE1011 implementation/registration/converter/caller paths
- Runtime status: untested; deferred
- Baseline IDs and provenance: ENGINE1011 archive SHA-256 `withheld-upload-fingerprint`; [baseline](../../00-environment/source-baseline-2026-10-11.md), [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

How do selected settings roots, file/reader construction, includes, section inheritance, DLTX discovery/scalar/list/deletion resolution, typed reads, writes/save, Lua signatures and ownership behave? Trace CInifile, CScriptIniFile registrations/wrappers, native settings construction/teardown, indexed filename ordering, selected converter/finalizer paths and bundled defaults. Completion requires implementation/export/caller and lifetime/failure limits plus evidence/navigation checks. Preserve domain controls and XML/DXML coverage; no game tests, all-option tuning, installed MO2 winner audit or exhaustive VM/parser/security analysis.

## Evidence and method

[50-row source ledger](../../evidence/configuration/ltx-ini-dltx-2026-10-12.csv) N01–N28/A01–A20/S01–S02 pins 21 files and 72 inclusive range groups. Read the full active parser/evaluator and wrapper/registration bodies; trace settings entry/exit, FS_FileSet ordered container/comparator, cache keys/invalidation, string/integer/pointer/adoption/in-out conversion, constructor ownership and finalization. Search and inspect the selected bundled helper definitions and feature/cache-command guards. Raw hashes/count/range/symbol checks establish reference integrity, not runtime semantics.

The uploaded snapshot has no proven exact upstream commit or installed binary correspondence. Native filesystem indexed enumeration is not MO2 supplying-mod precedence. Prior [CONFIG-01](2026-10-12-CONFIG-01-existing-coverage.md) retains the v0.1.73 documentation pin and original source confidence; no earlier evidence is migrated or silently reclassified.

## Findings

The [behavior reference](../../04-game-systems/configuration/ltx-ini-dltx.md) records the active order: settings-root construction; cache or reader parse; depth-increasing includes; named-root mod discovery at EOF; separate base/override key filtering; recursive parent/local/override resolution; ordered list edits; post-evaluation section deletion; final sorted DATA/cache insertion. Distinguish scalar depth precedence from list insertion order, ordinary section duplicates from overrides, conditional creation from unresolved overrides, empty values from deletion, inherited copies from final section removal, and filename metadata from complete provenance. N01–N28.

The [API page](../../02-lua-api/configuration/ini-api.md) preserves exact constructor arities, BOOL integer flags, fifth filename-constructor path selection, receiver/in-out positions, read prechecks and vector4 fallback, typed-conversion limits, existing-key writer requirements, one-input save, borrowed versus owning pointer results and diagnostic tables. A01–A20. C++ null/default branches do not create optional Lua arities or general nil-string acceptance. Native read assertions are not silently described as safe defaults.

Named caching ignores mode/include predicate/input changes in its key; a hit skips parsing. Runtime mutation does not invalidate the cache or consumer copies. Saving writes resolved plain data rather than original include/inheritance/DLTX structure, and an open failure can follow stored-filename mutation. Reload destroys the old system object and clears named cache without proving all aliases or dependent caches are repaired. Explicit close deletes this without clearing owned userdata; finalizer/alias hazards follow from the traced bodies, not an independent observed crash. N01–N04/N20/N22, A05/A07/A10/A12–A15.

Bundled default helpers use Lua tonumber/exact boolean strings and differ from native conversion. Replacement ini_file_ex's bool-null rule differs from inherited r_bool_ex. Advanced mode changes writable/override/autosave flags but does not remove native wrapper existing-key checks. Definition-level assignment is established; effective startup/global installation and later replacement order are CONFIG-03/04 work. S01/S02.

## Competing explanations and missing edges

A single “last mod wins” rule loses include depth, separate scalar/list stages and inheritance. An override marker is not identical to the mod_-filename diagnostic heuristic. Missing native root open, missing parent, missing read key, empty value and Lua helper default are distinct outcomes. Cache invalidation is not object reload, consumer refresh or restored startup, and save output is not a source-preserving patch.

Installed winning scripts/configs/packed resources, actual cache setting, executable flags and callback order remain unknown. The cache/include-predicate observation is a key-composition limit, not an installed authentication/security conclusion. Malformed parser input, all outer assertion/exception handlers, reader lifetime/exposure, full unlocalizer/namespace installation, large numeric/vector/color conversions and arbitrary addon stacks remain outside selected closure. Existing XML/UI and domain consumer records retain their limits.

## Checks and outcomes

All 50 raw hashes/counts, 72 cited range groups and symbol occurrences are checked against ENGINE1011. Review source branches and registration/policy mappings, rerun repository validation and the 10 existing regressions, and preserve prior evidence/history/generated/tool/test bytes plus dated bodies except synchronized document-set banners. [Verification](../verification-2026-10-12-v0.1.75.md). Compare complete remote base/staged/published blob maps with expected-head update. No independent runtime or engine compilation.

## Disposition and next work

CONFIG-02 closes this selected available-source contract pass. Configuration/script integration remains partial under its [completion rule](../../04-game-systems/configuration/source-completion-status.md). **Next CONFIG-03 — native script loading, startup and shared callbacks**, then selected supplied option/patch consumers and consolidation/audit. No CtZ gameplay changes or third-party source/assets redistribution. [Guide](../../04-game-systems/configuration/development-reference.md), [roadmap](../../ROADMAP.md).
