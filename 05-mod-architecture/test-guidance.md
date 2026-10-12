# Test guidance for qualified mod patterns

> ADR document set: **v0.1.82**. Research revisions and source/build versions below describe their original scope.

- ID: ARCH-03-TESTS
- Subsystem: practical architecture / verification
- Research revision: v0.1.82 maintenance; original pattern guidance v0.1.81
- Record status: complete-within-scope for selected test guidance and implemented ADR test inventory
- Source status: pinned reference/test-source synthesis; proposed mod fixture/runtime plans distinguished
- Runtime status: game/profile tests untested; deferred
- Baseline: ADR v0.1.80 `a9248aea46442c3cd520b7e33974827dbd810a95`; Q01–Q16 in [reference ledger](../evidence/architecture/qualified-patterns-2026-10-12.csv)
- Last reviewed: 2026-10-12

Choose a check that can answer the claim being made. This page records **existing ADR checks** and **proposed implementation tests** separately. It introduces no engine harness, runnable mod or mocked result presented as native verification. [Qualified patterns](../07-code-library/qualified-patterns.md), [verification policy](../08-research/evidence-policy.md).

## Evidence levels and implemented checks

| Check | What it can establish | What it cannot establish | Current status |
| --- | --- | --- | --- |
| Repository validator | Local target/anchor, banner, containment, forwarding/empty-file, required navigation and CSV-width integrity within tool scope | Correct interpretation, complete source coverage or game behavior | Implemented; run for each increment |
| Validator regression fixtures | Nine tests check valid current tree and deliberate missing target/anchor, root escape, stale revision, forwarding page, malformed CSV and explicit verification-label agreement | Native error recovery or installed addon compatibility | Implemented in tests/test_repository_checks.py |
| Binding-pattern fixtures | Three tests cover property recognition/origin and preservation of earlier binding categories | Every overload/converter, actual export availability or setter safety | Implemented in tests/test_binding_patterns.py |
| Source/document pin checks | Declared raw hashes, ranges/counts/markers and baseline identity | Interpretation or unknown executable/profile equivalence | Per-increment integrity checks; recorded in verification |
| Generator reproduction | Same outputs from declared inputs/projection/tool | Engine compilation, universal ABI/API completeness or runtime | Use when generator/input/output scope changes; unchanged catalogs preserved here |
| Proposed pure model/adapter fixtures | Implemented mod's bookkeeping, schema/result policy, identity/forwarding contract using explicit fake dependencies | Actual producer, native mutation completion, crash termination, pointer lifetime or encoding phase | Not implemented or executed by ARCH-03 |
| Engine/build checks | Identified build can compile/link a selected implementation | Installed profile behavior or all build combinations | Not performed here |
| Game/profile reproduction | Recorded behavior for exact executable/winning files/settings/save/trigger | Universal compatibility or another setup's result | Deferred |

Q12–Q14/Q16; [tests entry](../tests/README.md), [tools](../tools/README.md). ADR-01 adds two focused report-label regressions; the current suite is nine repository tests plus three binding-pattern tests. ARCH-03’s original seven-plus-three inventory remains pinned at its research revision. Actual counts/results for this revision belong in the [current audit verification](../08-research/verification-2026-10-12-v0.1.82.md), not in a proposed protocol's runtime status.

From the repository root, the implemented ADR checks are:

```bash
python tools/check_repository.py
python -m unittest discover -s tests -p 'test_*.py'
```

For a source change, separately check definitions/registrations/converters/callers, compile conditions, return/error meaning, effects and ownership against the declared pin. For a changed generator, reproduce its scoped outputs into an isolated output location and compare; retain the tool/input/projection/line-ending details. Do not rerun an unrelated catalog merely to imply broader verification when it and its inputs are unchanged. Q16; [workflow](../08-research/workflow.md), [A-Life generator scope](../02-lua-api/alife/README.md).

## Define an oracle before adding a fixture

A useful proposed test record names the implementation under test, preconditions, exact input/trigger, observable result, side effects, failure phase, cleanup/reset and allowed repeat behavior. Its oracle must be independent enough to detect a violated contract: asserting that a field equals the same expression used to assign it adds little confidence.

For example, a wrapper fixture can test that a later foreign replacement remains intact when the owner attempts removal. It can also test a result tuple containing nil, original failure after a recorded fake side effect, and repeated installation without unintended self-capture. Those distinguish behavior; they do not merely restate a setter. The wrapper implementation and fixtures do **not** exist in this increment. Q02/Q03/Q09 and [P02](../07-code-library/qualified-patterns.md#p02--install-a-wrapper-with-a-restoration-record).

Use fake dependencies that honestly expose their limitations. A fake callback registry may return a success boolean; the selected callback_set returns none. A fake transfer may complete synchronously; native requests may remain pending. A fake log sink may preserve every line; the native buffer can gate/compress/truncate and flush without a receipt. Model those differences explicitly rather than passing mocks off as integration evidence. Q04/Q08/Q09 and [source contracts](../06-debugging/diagnostic-routes.md).

## Proposed cases for later implementations

| Pattern | Independent contract cases | Native/effective evidence still needed |
| --- | --- | --- |
| P01 subscriptions | Same/fresh listener identity, rejected event/order, nested dispatch, shared-argument mutation, removal with retained target | Actual Register/Send/Unregister, emitter/phase, ordering version and listener lifetime |
| P02 wrapper | Same-install repetition, foreign replacement/capture, nil/multiple returns, original partial failure and reentry | Final slot/winner, capture/installer order, callable signature, native side effects/termination |
| P03 restore/reconcile | Known older/current/newer/malformed schema, campaign mismatch, reused target, repeated load, duplicate observation and unresolved effect | Real serializer/root/snapshot, identity producer, restore phase and request/result/accounting authority |
| P04 probe | Count/length budget, missing versus false, gate off, duplicate emission, truncated/absent output and no post-event record | Actual alias/build/logger/file/clock route; measured cost only after runtime resumption |
| Linked UI sketches | Valid supplied widget versus unavailable/invalidated representation; content update independent of window replacement | Exact creation/XML/parent/display registration/teardown and PDA phase |

These are **test plans**, not results. Q01–Q11/Q15. A fixture can cover owned pure data/state transitions; it cannot safely simulate away a missing engine prerequisite. No native failure is deliberately induced here and no game save is altered.

## Eventual profile test record

When runtime verification is resumed, record executable hash/build, active profile/winning file hashes, package/schema/campaign identity, configuration/debug/clock state, preserved reproduction, expected/observed outcomes and private logs/dumps. Keep normal install/start, repeated start/load, relevant transition, partial failure/retry, cleanup/disable/upgrade and interaction with a known replacement separate where they affect the claim. Select cases for the changed behavior; this is not a demand to test every addon or engine path. Q05–Q10/Q16.

A repeated successful run strengthens only the specified case. A reproducible failure rejects the tested claim for that setup; an external observation retains its reporter/provenance. An untested alternative stays a hypothesis. A caught error or surviving native caller does not prove the addon completed, rolled back or saved. [Triage](../06-debugging/triage.md), [source/runtime axes](../08-research/evidence-policy.md).

Runtime remains deferred under the user's standing instruction. Document-only checks and source collection can proceed without executing a game. Proposed fixtures, probes and package migrations require an actual implementation before their results can be reviewed.

## Promotion and stopping rule

A promotion record states exactly which checks passed, which dependencies remain unknown, what failures/cleanup/repeats were covered, and the runtime status. Pure model tests can justify a model-level claim while integration remains partial. Keep the label experimental until its stated integration contract is supported; reserve runtime-tested for recorded executable/profile outcomes. Q02/Q05/Q07/Q12–Q16.

ARCH-03 completes this selected guidance and the [bounded practical audit](../08-research/verification-2026-10-12-v0.1.81.md). No new test implementation, runnable pattern or runtime result is added. The later whole-ADR audit remains separate. [Central reference](development-reference.md), [roadmap](../ROADMAP.md).
