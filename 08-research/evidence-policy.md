# Evidence and verification policy

> ADR document set: **v0.1.47**. Research revisions and source/build versions below describe their original scope.

**Current policy from ADR v0.1.40.** Use the [workflow](workflow.md) and [layout conventions](repository-layout.md).

Record source and runtime status independently:

| Axis | Values and meaning |
| --- | --- |
| Source | `unverified`; `source-confirmed` for a specific implementation/registration with pinned evidence; `scoped-source-audit` for a bounded inventory/search conclusion |
| Runtime | `untested`; `observed` for recorded behavior/logs; `verified` for a repeatable successful test; `rejected` for a repeatable failure under documented conditions |

Existing labels such as source-verified/source-supported map to their stated source scope; they are never runtime proof. Investigation completion (open/partial/complete-within-scope) is a separate axis.

## Acceptable pins and citations

Use an immutable repository commit plus file/line/symbol when known. An uploaded archive SHA-256 plus archive-relative path, full-file SHA-256 and line/symbol evidence is also a valid **snapshot pin**. Record unknown upstream commit and executable correspondence explicitly. Do not fabricate a Git commit or infer binary/profile equivalence from a date/tag/archive label.

Cite claims near their statements, naming the baseline, path, symbol and relevant line ranges. Identify inferences, negative-search scope, build guards, missing files and installed overrides. Version-sensitive claims cannot silently inherit another record's baseline. Evidence IDs are scoped to their ledger, not globally unique.

## Source ledger convention

New claim-oriented ledgers use [the CSV template](../evidence/templates/source-evidence.csv): `evidence_id,source_id,source_path,symbol,line_ranges,file_sha256,line_count,subject`. Leave unavailable values blank and explain why; never invent a symbol or hash. File-only generated ledgers may use `source_id,archive_relative_path,sha256,line_count`, with line/symbol citations in the associated catalog. API inventories have purpose-specific columns documented beside their generator.

Existing ledgers retain their original schemas and bytes. The [manifest](../evidence/manifest.md) and adjacent records explain source IDs and locations; do not silently normalize away fields, IDs or provenance. A future conversion requires an explicit lossless mapping and validation.

## Verification limits

Link/range/hash checks establish reference integrity. Reproducibility establishes extraction stability. Neither alone proves interpretation, complete export/converter coverage, module execution or installed behavior. Runtime work requires executable/profile identity, reproduction steps, observations and outcome recorded separately. It remains deferred in the current source phase.

## Historical starter policy — superseded

The following is retained as a record of the original May 15-era convention. Its Git-commit-only requirement and default target are superseded by the current policy above.

### Original text

Record two independent axes:

**Source status:** `unverified`, `source-confirmed` (requires immutable repository commit + file/line/symbol).

**Runtime status:** `untested`, `observed` (log/behavior), `verified` (repeatable successful test), `rejected` (repeatable failure under documented conditions).

A function in current HEAD is NOT assumed present in MT-TEST 2026.05.15.
Every claim needs ID, version target, date, source evidence, confidence, and outstanding questions.

Suggested claim form:

```yaml
id: ADR-CLAIM-0001
statement: "..."
engine_target: MT-TEST 2026.05.15
source_status: unverified
runtime_status: untested
source_commit: null
source_path: null
evidence: []
last_checked: 2026-10-09
```
