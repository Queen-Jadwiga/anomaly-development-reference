# ALIFE-10 verification — 11 October 2026 — ADR v0.1.42

> ADR document set: **v0.1.43**. Research revisions and source/build versions below describe their original scope.

- Target ADR starting commit: `c52f86ff59f2eaea64a71482cc82bb1b90cfcb40` (v0.1.41)
- Changed scope: lifecycle/state and callback reference, synthesis record/ledger, current navigation and document-set version
- Source baseline IDs: ENGINE1011
- Last reviewed: 2026-10-11

## Checks performed

The source review is bounded to ALIFE-10's cited native/bundled-script phases and their original investigations; it is not an engine-wide semantic audit.

- Re-read registration/unregistration, group switching and load callback repair, GameObject spawn/destroy, level outer spawn, spawn-manager immediate lookup, bundled squad/monster callbacks and generic server bridges.
- Verify 47 synthesis ledger entries over 39 distinct source files: paths, SHA-256, line counts, cited range bounds and named symbol presence against the uploaded snapshot. Origin ledger/ID is retained in each subject.
- Check all Markdown links/anchors, canonical C-03/C-04/CtZ navigation, current version banners, absence of forwarding pages/empty files and CSV row widths with `python tools/check_repository.py`.
- Run the seven documentation-validator regression tests using `python -m unittest discover -s tests -p 'test_*.py'`.
- Compare pre-existing CSVs and A-Life catalog statistics against the starting Git tree. Existing research record bodies must match after removing only the document-set banner; historic snapshots are untouched.

## Results and corrections

The new pages retain different readiness contracts for direct versus bulk registration, queued versus immediate spawn-manager callbacks, base versus derived spawn completion, generic versus binder destruction, and network representation removal versus persistent release. Statements about effective wrappers/build guards and client-state freshness remain qualified.

No generator or source-input scope changes are made in this increment, so catalog rebuilding is not required; the v0.1.41 reproducibility result and unchanged blob comparison apply. No research conclusion is rewritten and no gameplay/configuration/license change is introduced.

Validation outcome: 124 Markdown files, 608 local navigation targets and nine anchors checked with zero errors; all seven validator tests passed. All 20 prior CSV blobs, catalog statistics, 33 prior investigation bodies (excluding only the synchronized version banner) and three historical snapshots are unchanged. The 47 new ledger entries verify 73 source-range groups over 39 files; all cited L-identifiers resolve within that ledger.

## Publication verification

Publish from the inspected starting tree with a branch-head lease. Verify the complete resulting path/blob map and published head, then read back the new reference pages and evidence/verification records. The final commit SHA is checked after publication rather than fabricated in this document.

## Remaining limitations

The exact upstream commit and installed executable/profile correspondence remain unknown. The phase tables do not establish effective startup/listener order, complete export/converter coverage, all subclasses or exact timing. Effective board/smart, death/safe-release and strategic persistence chains remain open. Engine/game runtime verification stays deferred until the user explicitly resumes it.
