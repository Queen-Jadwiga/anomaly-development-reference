# ADR maintenance

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

- Read `08-research/workflow.md`, `08-research/repository-layout.md` and `08-research/evidence-policy.md` before research or structural edits.
- Use `02-lua-api/<subsystem>/` for current API catalogs, `04-game-systems/<subsystem>/` for subsystem references, `08-research/investigations/` for research records, `evidence/<subsystem>/` for ledgers and `tools/` for generators/checkers.
- Preserve dated findings and source baselines. Do not invent an upstream commit for an uploaded archive or equate source findings with runtime validation.
- New investigations/API pages use the templates. Existing historical formats remain explicitly grandfathered; do not bulk rewrite conclusions or evidence schemas merely to satisfy formatting.
- Update current entry pages, `INDEX.md`, `ROADMAP.md` and `CHANGELOG.md` when relevant. Use canonical paths only; repair internal links after moves and remove obsolete forwarding pages. Earlier URLs remain recoverable in Git history.
- `VERSION` is the current document-set revision. Synchronize current Markdown banners when it changes; preserve research/source/build revisions and explicitly marked history.
- Run `python tools/check_repository.py` and relevant source/hash/reproducibility checks. Verify the committed files/tree after publication; a passing link check is not a semantic audit.
- Runtime authorization resumed on 2026-10-12: the user now permits runtime verification. Authorization is not a test result; preserve historical deferral and label new tests/observations accurately. Keep ADR and CtZ gameplay changes separate; do not add a license or publish third-party source/assets. Raw uploaded profile/log/source data remain private.
- Respect the user's existing authorization to commit ADR research directly. No extra permission is needed for routine reversible documentation maintenance within that scope.
- Publishing authorization (2026-10-12): the user explicitly authorized all future ADR publishing to `Queen-Jadwiga/anomaly-development-reference`, including synchronized revision banners across existing pages. Carry this authorization forward for subsequent ADR increments; do not request renewed publication approval for that scope.

- Public content: follow `00-environment/public-content-policy.md`; keep personal intake metadata/private upload fingerprints out of public files. Run `python tools/check_public_content.py` before publication. Privacy redaction may amend historical identifiers without changing technical findings.
