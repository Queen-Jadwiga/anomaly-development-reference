# ALIFE-10 — Lifecycle and callback reference consolidation

> ADR document set: **v0.1.65**. Research revisions and source/build versions below describe their original scope.

- ID: ALIFE-10
- Subsystem: A-Life / Warfare integration
- ADR revision: v0.1.42
- Record status: complete-within-scope
- Source status: source-confirmed for the selected native/bundled-script ordering; bounded synthesis
- Runtime status: untested; deferred until the user explicitly resumes verification
- Baseline IDs and provenance record: ENGINE1011; [October 11 source baseline](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

## Question and scope

How can the completed identity, creation/release, persistence, scheduling, graph/spawn, synchronization, switching and API investigations be combined into a practical reference without flattening their distinct readiness and ownership boundaries?

Included: the selected persistent server, online network, client and group representations; native/bundled-script callback phases; source-derived CtZ implications; API and evidence navigation. Completion requires a lifecycle/state page and callback-phase page with scoped evidence and explicit missing edges.

Excluded: new effective GAMMA file discovery, all entity subclasses/AI, every callback/export/converter, installed startup order, gameplay changes and any engine/game runtime test. This does not close ALIFE-03 or effective Warfare/death/persistence integration.

## Evidence and method

Source snapshot: `xray-monolith-2026.10.11.zip`, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Exact upstream commit and installed executable equivalence are unknown.

The [new synthesis ledger](../../evidence/alife/lifecycle-callbacks-2026-10-11.csv) follows the current eight-column evidence schema. Its 47 entries over 39 unique source files retain the original source hashes and selected ranges, name relevant symbols, and identify the originating investigation ledger/ID in `subject`. Labels L01–L47 are local to this ledger. The existing ledgers remain unchanged.

Read ALIFE-02/04/05/06/07/08 and selected ALIFE-09 API contracts. Re-read native register/unregister, group switching/load repair, GameObject spawn/destroy, outer level spawn-manager/after-spawn ordering, immediate add-time callback, bundled squad notifications, monster binder and generic server bridges. Verify ledger paths, full-file hashes, line counts, range bounds and symbol presence against the extracted snapshot. This is targeted consolidation, not a fresh engine-wide search.

## Findings

The deliverables are [lifecycle/state reference](../../04-game-systems/alife/lifecycle-state-reference.md) and [callback observation contracts](../../04-game-systems/alife/callback-phase-reference.md). Their nearby L-labels trace each selected mechanism to the new ledger and preceding investigation.

- Native registration, network insertion, Lua board membership and client spawn completion are separate boundaries. Generic/type-specific squad notifications can precede board insertion. L02/L05/L07/L22/L24.
- Save replay runs final registration callbacks before late native group pointer repair; numeric identity can survive while instances are reconstructed. L10–L14.
- Offline movement, task selection, sampled location notifications and strategic arrival/capture are distinct contracts. Native group movement consumes the Lua task and later propagates member locations. L15–L20/L47 and ALIFE-05's completion analysis.
- Client lookup may begin during partial base spawn. Queued manager delivery follows full virtual success, whereas add-time immediate delivery only requires lookup success. Optional after-spawn callbacks have a later outer boundary and a build/listener guard. L22/L24/L25/L37/L38.
- Ordinary switching retains the persistent A-Life object; client teardown, server unregister, death and permanent release are distinct. Generic destroy is before ordinary client unregistration; binder destroy is after it. L01/L02/L23/L26/L28/L34/L40–L46.
- Listener priority orders one dispatch and cannot reorder later native/script operations. Installed global routes/listeners remain unknown. L09 and ALIFE-02.

The practical CtZ guidance is explicitly an inference for later mod development: identify the required representation/phase, reacquire handles, avoid duplicate lifecycle accounting, and validate identity beyond a reusable numeric ID where strategic data outlives release. No CtZ implementation is changed.

## Competing explanations and missing edges

A same-named callback may come from another dispatcher or effective override. An absent notification may reflect a base call bypass, early return, missing listener/bridge, DEBUG/feature branch or failed realization rather than entity nonexistence. A successful lookup may reflect partial spawn or pre-removal registration rather than complete readiness/lifetime continuity. These alternatives remain explicit rather than converted into runtime diagnoses.

Missing effective board/smart/job and reach paths, `se_stalker`/`se_monster` death overrides, safe release, global wrappers, storage dispatch, stalker binder and startup replacement order retain their previous qualifications. Per-object success does not prove all squad members are ready. Active configuration/build flags and timing remain unknown.

## Checks and outcomes

See [v0.1.42 verification](../verification-2026-10-11-v0.1.42.md): native/bundled phase review, ledger hash/range/symbol checks, unchanged prior datasets and findings, navigation/version checks, documentation-validator regression checks and published tree verification. No runtime observations or engine/game tests were performed.

## Disposition and next work

ALIFE-10 closes the lifecycle/state and callback-reference portion of consolidation within the declared source scope. It does not declare the entire A-Life/Warfare section development-reference ready. The [roadmap](../../ROADMAP.md) retains effective script-chain closure, configuration-reference/final claim audit and deferred runtime work. Preserve this record's scope if later installed evidence refines these phases.
