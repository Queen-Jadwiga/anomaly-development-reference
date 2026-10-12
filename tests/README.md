# Verification and tests

> ADR document set: **v0.1.61**. Research revisions and source/build versions below describe their original scope.

ADR has documentation/source checks; engine/game runtime testing remains deferred.

- Run [the repository checker](../tools/check_repository.py) for local link/anchor and entry-page integrity.
- For source increments, verify the declared baseline hashes, relevant paths/ranges/symbols and scoped interpretation.
- For generator changes, rebuild from the declared inputs and compare outputs; consult [the A-Life catalog](../02-lua-api/alife/README.md).
- Record results and limits with [the verification template](../08-research/templates/verification.md). Published reports are indexed in [INDEX.md](../INDEX.md).

Do not describe documentation checks, preprocessing or CSV reproducibility as engine compilation or in-game verification. Eventual runtime checks require executable/profile identity, reproducible steps and observations/logs.

## Documentation validator regression checks

Run `python -m unittest discover -s tests -p "test_*.py"`. Checks cover the valid current tree and rejection of missing links/anchors, root escapes, stale document-set versions, obsolete forwarding pages and malformed CSV rows. These are documentation tests; engine/game runtime verification remains deferred.

## Property extractor regression checks

`test_binding_patterns.py` checks that accessor-backed properties are recognized alongside methods/fields, that property-only source origins pass validation, and that prior binding categories remain distinct. Full generator reproduction additionally checks the actual condition property and preserves all earlier rows. These are source-tool tests, not game tests. Selected externally reported runtime observations are tracked separately in [REV-01](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md).
