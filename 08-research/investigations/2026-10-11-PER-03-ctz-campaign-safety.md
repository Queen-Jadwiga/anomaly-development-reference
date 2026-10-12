# PER-03 — CtZ campaign identity, schema and restoration

> ADR document set: **v0.1.75**. Research revisions and source/build versions below describe their original scope.

- ID: PER-03
- Subsystem: persistence
- ADR revision: v0.1.52
- Record status: complete-within-scope
- Source status: source-confirmed selected paths; scoped identity/schema audit
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline: CTZ005J; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-11

## Question and scope

How does pinned CtZ save/restore strategic state, resolve native identity and reconcile realization/casualties? Include campaign version labels, targeted backfills, economy clock, transition/readiness gates, initial retry reuse, ownership/member repair and missing/lost accounting. Exclude exhaustive battle/strategy/UI behavior, effective core manager/file/dispatcher implementation, gameplay fixes and runtime.

## Evidence and method

CTZ005J Alpha 0.0.5j commit `eba6660db09353dcc42a195ae6e7e706f4762277`. Retrieved committed tree contains `gamedata/scripts/ctz_campaign.script` blob `25638cc5ae5ed81ceddacf6c16f39f53a5f4d791`; retained original bytes match. [C01–C13 ledger](../../evidence/persistence/ctz-campaign-safety-2026-10-11.csv): 13 entries, one file, 22 range groups. Read selected handlers/helper bodies and searched the whole campaign file for version/scenario/fingerprint uses. Absence claims are bounded to the load and numeric rebind chains, not all installed addons. Profile/engine correspondence remains unknown.

## Findings

[Practical reference](../../04-game-systems/persistence/ctz-campaign-safety.md) carries nearby claim IDs and phase/identity tables.

- Package Alpha 0.0.5j differs from literal campaign VERSION 0.0.3b; SAVE_VERSION 9 is stamped, not used for rejection/dispatch by load_state. C01/C02.
- Load assigns shared state directly, repairs selected missing fields and transient route state, and recounts forts. Economy migration deliberately anchors on a later authoritative tick. No general shape/schema certification follows. C02/C03/C10.
- Load quarantine, readiness and elapsed grace separate target sanitization from actor restore/validation. Marker/task operations have distinct gates; callback registration attempt is not effective emitter evidence. C06/C07/C13.
- Numeric lookup/retry reuse and member reclamation lack independent identity comparison in selected paths. ID collision consequences are a conditional inference, not an observed runtime bug. C04/C05/C08/C09.
- Validation has world effects. Missing timers, field-loss exception, snapshot-based casualty baseline and death-observation-only callback define accounting; no blanket load success/idempotence guarantee. C10–C13.

## Competing explanations and missing edges

Winning storage can supply reset/pairing/version checks or change dispatch ordering; retained consumer source cannot establish that. Native ID behavior may prevent some collision scenarios, but campaign-source lookup alone cannot certify it. Delays may mask registration churn without proving completion. Protected setup/transfer calls can hide errors and partial state. Existing ALIFE-04/PER-01/PER-02 remain preserved; this extends their CtZ boundary without revising their conclusions.

## Checks and outcomes

Compare pin/blob, ledger hashes/counts/ranges/symbols and semantic branch order. Preserve prior evidence/history/investigation bodies, align current version/navigation and run repository validator/tests. [Increment verification](../verification-2026-10-11-v0.1.52.md) records results. No runtime, CtZ edits, save edits, engine build, assets/source redistribution or license addition.

## Disposition and next work

PER-03 closes this selected campaign identity/schema/reconciliation source pass. Effective persistence remains partial. Next practical consolidation/final available-source audit; runtime deferred. [Roadmap](../../ROADMAP.md).
