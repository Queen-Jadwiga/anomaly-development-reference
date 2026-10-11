# Evidence and verification policy

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
