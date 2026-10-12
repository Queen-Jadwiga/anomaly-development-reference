# Repository file and folder conventions

> ADR document set: **v0.1.60**. Research revisions and source/build versions below describe their original scope.

**Effective from v0.1.40.** Every new record has one canonical home. Entry pages may link it; obsolete forwarding pages are removed after internal navigation is repaired (v0.1.41). Earlier URLs remain in Git history.

| Location | Responsibility |
| --- | --- |
| `README.md`, `INDEX.md`, `ROADMAP.md`, `CHANGELOG.md` | Landing page, full navigation, current work and dated increments |
| `00-environment/` | Source/executable/profile baselines and provenance |
| `01-engine/` | Cross-system native architecture and ownership |
| `02-lua-api/<subsystem>/` | API catalogs, class/method contracts and generated export datasets |
| `02-lua-api/templates/` | Shared API template |
| `03-ui-pda/` | UI/PDA behavior and integration reference |
| `04-game-systems/<subsystem>/` | A-Life, Warfare, factions and persistence references/entry pages |
| `05-mod-architecture/`, `06-debugging/`, `07-code-library/` | Mod design, diagnostics and qualified examples |
| `08-research/investigations/` | Dated question/evidence/findings/disposition records |
| `08-research/templates/` | Shared investigation and verification templates |
| `08-research/` | Workflow/policy, verification reports and historical question registers |
| `09-projects/` | Project-specific links and integration context; CtZ code remains in its separate repository |
| `evidence/<subsystem>/` | Source evidence ledgers and package comparisons |
| `tools/` | Extraction, auditing and documentation validators |
| `tests/` | Test scope/status and links to recorded checks |

## Names and metadata

Use lowercase hyphenated descriptive filenames. New investigation names use `YYYY-MM-DD-ID-topic.md`; API/reference filenames use `topic.md`; new evidence datasets use `topic-YYYY-MM-DD.csv`. Keep native symbols case-exact inside the content. Existing dated names such as `*-oct11.csv` retain their identity during migration.

New investigation/API records carry the template's explicit ID, subsystem, baseline, source status, runtime status, scope and review date. Source IDs identify artifacts/packages; evidence IDs are local to a ledger unless qualified with its path. Do not assume E01 is globally unique. Keep a canonical record per question and link it rather than maintaining parallel edited copies.

## Historical records and this migration

v0.1.40 moves the recent A-Life/Warfare question records to `08-research/investigations/`, current UI/A-Life API pages/data to `02-lua-api/ui/` and `02-lua-api/alife/`, their evidence ledgers to `evidence/alife/` and `evidence/warfare/`, and the A-Life extractor to `tools/`. v0.1.40 added Markdown forwarding pages; v0.1.41 removes them to keep the current tree canonical. CSV/tool paths are updated in current links; their canonical locations are listed in the catalogs.

Older UI investigations already under `08-research/investigations/` stay there. Earlier UI behavioral reference pages under `03-ui-pda/` and historical audits at the API root remain valid historical exceptions. Their findings/baselines and original evidence schemas are not retrospectively rewritten. The current API index and evidence manifest identify where to start; older templates/starter descriptions are superseded by this convention.

## Link and tooling rules

Use relative repository links internally; use immutable upstream links when available and explain snapshot-only line checks. Never traverse above the repository root. Do not put generated output back into a historical forwarding directory. Generators accept explicit source/output roots and document prerequisites. Source archives, compiled executables, private profile paths and gameplay assets are not repository artifacts.
