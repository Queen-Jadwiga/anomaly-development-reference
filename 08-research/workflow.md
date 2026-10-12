# Standard ADR research workflow

> ADR document set: **v0.1.81**. Research revisions and source/build versions below describe their original scope.

**Effective from ADR v0.1.40 · 11 October 2026.** Applies to every subsystem. Existing dated records remain historical evidence; this workflow governs new work and current navigation.

## 1. Define the investigation

Assign a stable question ID (for example ALIFE-10 or WAR-003), name the subsystem, state the question, enumerate included paths/mechanisms and exclusions, and state a concrete completion boundary. Use the [investigation template](templates/investigation.md). Separate optional exhaustive work from requirements for the CtZ-focused reference.

## 2. Establish source provenance

Select a baseline from [environment records](../00-environment/) and the [evidence manifest](../evidence/manifest.md). Prefer an immutable upstream commit where known. For an uploaded archive, record its SHA-256, archive-relative paths and full-file hashes; leave unknown upstream commit/executable correspondence explicitly unknown. Identify script package variants and active-profile uncertainty. A filename/version label alone is not a pin.

## 3. Trace behavior and interfaces

Read definitions, declarations, registrations and relevant callers. Distinguish C++ implementation, Lua export, virtual override, script helper and effective installed policy. Trace state ownership, return/error behavior, mutation, serialization, callback order and lifetime where relevant. Identify missing edges rather than filling them from names/comments. Use competing hypotheses when evidence is incomplete.

## 4. Write the research record and reference

Put the dated question/evidence/findings/disposition record in `08-research/investigations/`. Put usable subsystem guidance in its reference section and APIs in `02-lua-api/<subsystem>/`. A small investigation may serve as the linked reference without duplicating its conclusions. Mark source status and runtime status separately. Cite each substantive claim at a file/line/symbol boundary and link its evidence ledger.

## 5. Generate inventories when appropriate

Keep repeatable extractors in `tools/`; generated API datasets go beside their catalog, and source ledgers go in `evidence/<subsystem>/`. Record input baselines, extraction scope, tool requirements, build/conditional projections, parsing limits and output row meanings. Preserve overloads/variants; do not equate occurrence counts with unique runtime APIs. Use the [evidence conventions](evidence-policy.md). Rebuild and compare generated results where the increment changes a generator or its input scope.

## 6. Verify the increment

Run `python tools/check_repository.py`. Check cited source paths/ranges/symbols and recorded hashes against the declared source inputs. Apply focused declaration/converter/lifetime checks where needed. Review changed claims and missing dependencies. State what was actually checked and what remains untested. A valid line number or reproducible CSV does not prove the interpretation.

Document-only work does not require unrelated engine compilation or gameplay tests. Runtime checks, when resumed, need the executable/profile, reproduction steps, observations/logs and outcome recorded separately. Do not promote source-confirmed findings to runtime-verified through documentation checks.

## 7. Update navigation and publish

Update root/subsystem entry pages, API index, current roadmap and changelog as relevant. Change `VERSION` once per published increment and synchronize the document-set banner in every current Markdown page; marked `08-research/history/` snapshots retain their historical labels. Preserve research revision/source/build version text. Ensure C-03/C-04, CtZ and canonical research navigation resolve. Remove obsolete forwarding files when moving records; Git history retains prior paths. Commit with a concrete scoped message, reject unexpected branch-head changes rather than overwriting them, and verify published contents/blob identities and branch head.

GitHub renders the Markdown directly. The documentation build is extraction plus validation; it is not an engine build. [Publishing guidance](../PUBLISHING.md) describes initial import versus ongoing maintenance.

## Completion states

Use `open`, `partial`, or `complete-within-scope` for an investigation, independently of source confidence and runtime status. A missing effective script or deferred runtime test can remain open even after a native source question closes. Next steps belong in the current roadmap; superseded historical plans are not silently erased.
