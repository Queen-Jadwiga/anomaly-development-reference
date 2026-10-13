# Qualified mod patterns

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

- ID: ARCH-03-PATTERNS
- Subsystem: practical architecture / examples
- Research revision: v0.1.81
- Record status: complete-within-scope for four selected design patterns and linked UI sketch qualification
- Source status: pinned reference synthesis; inherited implemented contracts retain their original source/build scope
- Runtime status: untested; deferred
- Baseline: ADR v0.1.80 `a9248aea46442c3cd520b7e33974827dbd810a95`; original native/script/package/external evidence retained
- Last reviewed: 2026-10-12

These are **experimental design patterns, unimplemented and non-runnable**, rather than a drop-in framework. They make a few recurring integration decisions concrete without inventing missing engine services. No new Lua module or third-party code is supplied. Each implementation still needs its effective dependencies, lifecycle and tests. [16-row reference ledger](../evidence/architecture/qualified-patterns-2026-10-12.csv) Q01–Q16 pins the supporting sections/test sources; IDs below are local to that ledger. [Test guidance](../05-mod-architecture/test-guidance.md), [central guide](../05-mod-architecture/development-reference.md).

## P01 — Own subscriptions by exact identity

**Use:** a feature subscribes during an established installation phase and later releases its subscriptions. **Dependencies:** actual winning Register/Send/Unregister chain, supported event/arguments, exact function or userdata identity, dispatcher version/order and object lifecycle. **Preconditions:** caller has an established phase and listener lifetime; optional unavailable dependencies have a declared unsupported outcome. Source motivation: Q01–Q03/Q05; [CONFIG-03 registry/removal](../04-game-systems/configuration/script-loading-startup-callbacks.md#shared-registry-identity-registration-and-removal).

| Proposed step | Owned record/effect | Required qualification |
| --- | --- | --- |
| Declare | Keep event name, exact listener token, dependency constraints and feature/module generation | A new closure with identical code is a different token; do not persist a native listener handle as campaign data |
| Request registration | Use the retained identity and record the attempt/phase | Selected callback_set has no boolean receipt; a returned call alone does not certify acceptance or later invocation |
| Repeat installation | Compare the owned installation record and effective route before deciding no-op/update | Re-registering one identity may change ordering rules; hot reload can leave older identities installed |
| Observe | Accept only observations belonging to the intended feature generation and valid argument lifetimes | A generation check is proposed stale-work policy; it does not make invalid native userdata safe to dereference |
| Remove | Unregister using the same event/token and record the attempted disposition | Do not remove unrelated listeners or claim every external reference/dependency rule was revoked |

**Failure/reentry:** define whether one listener mutates shared arguments, what later listeners receive, and how nested invocation is handled. Registration/order rejection and gameplay effects are different rollback domains. An effective error handler may terminate before cleanup; do not promise a finalizer always runs. **Cleanup/lifetime:** discard owned transient records only under the actual route's lifetime contract; retained function targets elsewhere can keep closures alive. **Persistence:** save domain facts through their real serializer, not subscription objects.

**Discriminating review cases:** repeated installation with the same token, a fresh closure after reload, unsupported event, rejected dependency order, mutation/reentry and removal while another rule retains the token. A fixture can check the proposed owner's bookkeeping; only the effective dispatcher/source and eventual runtime observations establish actual registration/removal behavior. No such fixture or game test is supplied here.

## P02 — Install a wrapper with a restoration record

**Use:** a narrowly scoped adapter intentionally wraps one function slot. **Dependencies:** winning function and later installers, call signature/returns, capture phase, reentry/error policy and installation owner. **Preconditions:** supported target is callable and the original's lifetime is known; no assumption that filename order controls final replacement. Source motivation: Q02/Q03/Q05/Q07; [CONFIG-04 captures](../04-game-systems/configuration/supplied-options-patches.md#captured-originals-and-startup-wrappers).

| Proposed step | Owned record/effect | Required qualification |
| --- | --- | --- |
| Capture | Store original, exact wrapper identity and the installation generation together | Capture once for that installation; avoid a mutable shared original slot that repeated installation can point back at itself |
| Install | Replace only the declared slot under the chosen repeat policy | A once-only body guard does not prevent recursive original capture before the guard |
| Invoke | Forward documented arguments and original results, then apply intended adapter behavior in the declared order | Preserve multiple returns/trailing nil where the interface requires them; define before/after effects and partial failure |
| Restore | Restore original only if the public slot still contains this owner's exact wrapper | Otherwise record superseded/unresolved; do not overwrite a later addon's replacement |
| Release record | Follow the actual module/VM lifetime and external reference policy | Another wrapper can have captured this wrapper; public-slot restoration cannot remove that embedded reference |

**Failure/reentry:** decide whether the adapter may call itself, what happens after the original mutates then fails, and whether any cleanup route can actually be reached. A protected Lua call does not roll back native side effects or catch every assertion/termination. Q09. **Cleanup/persistence:** the capture/restore record is transient installation state; removal does not reverse prior gameplay effects, revoke all aliases or certify hot reload.

**Discriminating review cases:** same-install repeat, fresh-module install over an old wrapper, another addon replacing the slot, another addon capturing this wrapper, return tuples containing nil, original failure after an effect, and reentry. A mock slot can test the proposed identity/forwarding rules; it cannot certify the native target's lifetime, final patch order or termination behavior.

## P03 — Stage restoration and reconcile owned operations

**Use:** a mod restores durable records and later binds them to world representations or resumes pending work. **Dependencies:** actual serializer/encoder/root/reset, supported schema migrations, campaign/object identity producer, selected restore phase, request adapter and completion/accounting authority. **Preconditions:** supported input shape and identity can be validated; unknown prerequisites produce an explicit pending/unsupported outcome. Source motivation: Q01/Q02/Q04/Q06; [persistence phases](../04-game-systems/persistence/development-reference.md#save-and-load-phase-contracts).

| Proposed stage | Decision/output | Effect boundary |
| --- | --- | --- |
| Decode/classify | Current accepted shape, known older migration candidate, malformed or unsupported/newer input | Keep original unknown input intact; codec availability does not establish schema acceptance |
| Validate candidate | Check owned fields, schema, campaign pairing and internal references | Construct a separate candidate under the actual schema; do not stamp an unsupported record current or assume a generic deep-copy policy |
| Publish owned model | Replace/commit according to the real storage and alias policy | Domain-model publication is distinct from durable disk commit; old table holders need explicit refresh |
| Bind representations | Reacquire identity in the intended native/server/client phase | Successful numeric lookup does not prove campaign/generation identity; client absence is not death |
| Reconcile operation | Compare intended effect, target identity and last established outcome before a replay | Owned operation ID alone does not deduplicate native delivery or payment |
| Resolve outcome | Requested, observed complete, reconciled, failed or unresolved under declared evidence rules | These are proposed mod states, not an engine transaction API or atomic receipt |

**Failure/reentry:** decoding, migration, publication, world request and accounting can fail at different points. Leave an operation unresolved when an effect may have occurred; a retry/refund needs evidence for safety. Define repeated load, partial migration, game-clock rewind, missing target and duplicate observation behavior. Avoid world mutation during early decoding merely because a callback is named load.

**Cleanup/persistence:** ephemeral clients/windows do not belong in the durable record. Define campaign reset and permanent removal separately from level/client teardown. Persist operation state only through a traced snapshot/encode/write route; references attached to shared tables can be mutated later. No crash-safe transaction, save repair or CtZ migration implementation is provided.

**Discriminating review cases:** accepted current/known older/newer/malformed records, campaign mismatch, reused target ID, old consumer alias, repeated load, duplicate completion observation and request failure after a possible effect. Model fixtures can check a proposed state machine with fake identities/receipts; they cannot make the actual engine provide those identities/receipts.

## P04 — Use a bounded probe to discriminate one hypothesis

**Use:** a source-qualified investigation needs a small observation of one operation/phase. **Dependencies:** actual log alias/export and build/command gates, value lifetimes, chosen clock/unit, privacy policy and ability to remove the probe. **Preconditions:** one written hypothesis and different expected observations for its alternatives. Source motivation: Q08–Q10; [diagnostic exports](../02-lua-api/debugging/diagnostic-api.md).

| Proposed step | Probe record/effect | Required qualification |
| --- | --- | --- |
| Scope | Record hypothesis, producer/phase, baseline/winner and run/operation ID | Feature name or last log line alone cannot identify cause |
| Bound | Choose a message-length and sample-count policy for this probe | No safe rate/throughput threshold is certified by source; reserve is not a buffer cap |
| Sample | Emit a short preformatted record of validated scalars and missing/false/empty distinctions | Do not access stale objects merely to print them; log buffering/filtering/compression can change visible output |
| Interpret | Compare expected discriminating outcomes with complete captured context | Returned log/flush calls are not disk receipts; absence can involve gates, suppression or I/O |
| Remove | Disable/remove the owned probe and retain the private incident record | Do not clear the log as cleanup; retained evidence is distinct from probe code |

**Failure/reentry:** routine instrumentation uses the selected ordinary logging route; `error_log` deliberately adds assertion behavior. Stack/flush-per-item/full-table logging can alter execution and memory/I/O; overhead is unmeasured. **Persistence:** diagnostic output is separate from campaign serialization. Label timestamps as wall time, engine milliseconds or simulation time; repeated/load-rewound clocks require explicit interpretation. **Cleanup:** preserve private raw hashes and redact shared copies.

**Discriminating review cases:** disabled gate, duplicate-message compression, budget exhaustion, missing versus false, no_log/invalid writer, truncated record and failure before a post-operation message. A fake sink tests the proposed budget/schema only; it does not reproduce native formatting, buffering, stack or fatal behavior. Runtime work remains deferred.

## Reuse the two UI sketches with their lifetime limits

The existing [progress-bar and scroll-view sketches](../03-ui-pda/examples/minimal-static-ui-patterns.md) stay non-runnable and untested. They assume valid initialized widgets; Q11/Q15 do not establish constructor safety, ownership transfer, display registration or PDA-ready timing. Their original source/build qualifications remain in the linked UI catalogs and ownership references.

| Required qualification | Existing sketch boundary |
| --- | --- |
| Dependencies/preconditions | Correct widget/API/build plus known initialization, parent and native registration route |
| State ownership | Content/model owner separate from transient widget; holding a Lua reference is insufficient proof of lifetime |
| Failure/reentry | Calls require a valid current object; a pcall is not generic stale-pointer protection |
| Cleanup | Match the real creation/attachment/registration owner; no generic delete/HideDialog rule |
| Checks/status | Review source/export and actual ownership path; no standalone constructor, mock-engine result or game test added |

UI XML factories, manual allocation and native/PDA ownership retain separate contracts. See [UI guide](../03-ui-pda/development-reference.md), [construction/ownership](../03-ui-pda/ui-construction-ownership.md) and [test guidance](../05-mod-architecture/test-guidance.md).

## Promotion record

Before an implementation is promoted, record its source/dependency pins, exact interface, preconditions, state/lifetime owner, failure/reentry/repeat/cleanup policy, schema/config/package support, actual checks and runtime status. A mock fixture may strengthen a pure model claim; it does not change the native guarantee or installed compatibility label. Q02/Q05/Q07/Q12–Q16. The four protocols above remain experimental design; the two linked UI examples remain call sketches. [ARCH-03 investigation](../08-research/investigations/2026-10-12-ARCH-03-patterns-consolidation-audit.md), [verification](../08-research/verification-2026-10-12-v0.1.81.md).
