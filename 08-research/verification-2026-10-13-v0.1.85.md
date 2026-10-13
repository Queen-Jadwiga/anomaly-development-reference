# Verification — 2026-10-13 — v0.1.85

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

- Target ADR revision: v0.1.85; parent v0.1.84
- Changed scope: UI-07 button/checkbox factory/export contract, runtime failure intake and negative fixture-capability guidance
- Source baseline: public commit `c57fe5b9fab4fe0506659db03137c52d2500eb2f`; private RT-UI07 observation
- Last reviewed: 2026-10-13

## Checks performed

Verify four public source-file SHA-256 values and line ranges against the [ledger](../evidence/runtime/button-checkbox-contract-2026-10-13.csv). Inspect factory allocation/return classes, button hierarchy and SetCheck export owner, scoped XML initialization, and inherited text-control exports. Retain existing generated catalogs unchanged because their class attribution was already correct.

Run `python tools/check_repository.py`, `python tools/check_public_content.py` and `python -m unittest discover -s tests -p 'test_*.py'`. Synchronize current banners and navigation while preserving historical research revisions. Review new public prose for private intake details. No raw attachments, private paths or gameplay/source assets are included.

## Results and corrections

Repository and public-content checks pass; all 15 existing ADR regression tests pass. Four source hashes/ranges pass. The newly documented negative-capability guard belongs to the separate local CtZ fixture suite; it is not counted as an ADR test. No engine build or successful corrected game test was executed.

## Publication verification

Publish documentation only against the exact parent with branch lease protection. Verify the published head and prepared versus published tree identity; report the resulting commit after publication rather than inventing its SHA here.

## Remaining limitations

The supplied failure is observed privately, with unknown public-source/binary equivalence. The correction's native behavior and broader compatibility remain pending. Source/fixture checks are not runtime success. Prior startup/reload hazards retain their separate status.
