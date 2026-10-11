# ADR maintenance

> ADR document set: **v0.1.52**. Research revisions and source/build versions below describe their original scope.

- Read `08-research/workflow.md`, `08-research/repository-layout.md` and `08-research/evidence-policy.md` before research or structural edits.
- Use `02-lua-api/<subsystem>/` for current API catalogs, `04-game-systems/<subsystem>/` for subsystem references, `08-research/investigations/` for research records, `evidence/<subsystem>/` for ledgers and `tools/` for generators/checkers.
- Preserve dated findings and source baselines. Do not invent an upstream commit for an uploaded archive or equate source findings with runtime validation.
- New investigations/API pages use the templates. Existing historical formats remain explicitly grandfathered; do not bulk rewrite conclusions or evidence schemas merely to satisfy formatting.
- Update current entry pages, `INDEX.md`, `ROADMAP.md` and `CHANGELOG.md` when relevant. Use canonical paths only; repair internal links after moves and remove obsolete forwarding pages. Earlier URLs remain recoverable in Git history.
- `VERSION` is the current document-set revision. Synchronize current Markdown banners when it changes; preserve research/source/build revisions and explicitly marked history.
- Run `python tools/check_repository.py` and relevant source/hash/reproducibility checks. Verify the committed files/tree after publication; a passing link check is not a semantic audit.
- Engine/game runtime tests remain deferred by the user. Keep ADR and CtZ gameplay changes separate; do not add a license or publish third-party source/assets.
- Respect the user's existing authorization to commit ADR research directly. No extra permission is needed for routine reversible documentation maintenance within that scope.
