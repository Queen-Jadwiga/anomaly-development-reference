# WORLD-02 — Spatial queries relocation and selected restriction/patrol contracts

> ADR document set: **v0.1.73**. Research revisions and source/build versions below describe their original scope.

- ID: WORLD-02
- Subsystem: world interaction/navigation
- ADR revision: v0.1.71
- Record status: complete-within-scope
- Source status: source-confirmed selected registrations/implementations/native and bundled callers
- Runtime status: untested; deferred
- Baseline IDs and provenance: ENGINE1011 uploaded archive, SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

Extend the [WORLD-01 inventory](../../04-game-systems/world/coverage-inventory.md) with selected live/server lookup, level/game vertex queries, actor/NPC/simulator relocation, live destination requests, restriction mutation/accessibility and patrol queries/request handoff. Trace exports, definitions, owning managers, failure branches and relevant persistence/callers. Reuse A-Life offline movement, graph/realization, coordinate/readiness and identity findings. Exclude WORLD-03 use/touch/actor level travel/map marker lifecycle; exhaustive pathfinding/planner/physics and all installed Lua consumers remain later scope.

## Evidence and method

[Ledger P01–P40](../../evidence/world/spatial-contracts-2026-10-12.csv) pins raw archive-relative file hashes, counts, ranges and cited symbols. Read exact definitions/declarations and registrations, follow movement/restriction/physics/patrol manager forwarding and selected server event consumers, and compare return/guard/converter branches. No uploaded archive is assigned an invented upstream commit. Build/compiler/executable/profile correspondence remains unknown.

## Findings

[Behavior reference](../../04-game-systems/world/spatial-queries-relocation.md) documents the findings and source boundaries. P01–P10 cover client lookup, namespaces, query failure and registration/wrapping limits. P11–P20 follow relocation and accepted destinations into their owners. P21–P30 distinguish live restriction checks/refresh/defaults and server ID-list/event/serialization state. P31–P38 cover borrowed patrol paths, differing fallback behavior, geometric versus accessibility-filtered queries and input-output conversion. P39/P40 are two selected bundled callers, not a complete effective-consumer audit.

Important distinctions: registry-valid versus client-ready; geometric nearest versus accessible/reachable; live transform versus server graph relocation; request versus completed travel; merged/default versus base/server restrictions; invalid patrol point fallback versus a successful requested point; diagnostic SAFE_WRAP versus safe stale-pointer recovery. Dead-body corrective caller requests are not proof of actual transformation because the traced physics support has an alive gate. No source or mod patch is made.

## Competing explanations and missing edges

C++ defaults could appear to imply omitted Lua arguments; only explicit constructor/method registrations establish those call shapes. Restriction accessibility can appear to certify path/collision safety, but permissive empty/uninitialized branches and separate movement updates prevent that inference. Simulator dynamic lists and live restriction strings are distinct owners. Geometric graph/patrol nearest functions do not certify installed routing. Effective planners, static/default restrictor definitions, binder/startup replacements and active call forms remain to reconcile. Assertions and converter failures are not certified recoverable in the executable.

## Checks and outcomes

Check every ledger hash/count/range/symbol; review selected branch/policy semantics and registration composition; preserve old evidence/history/tools; run repository checks and ten existing regressions; verify remote base and published path/blob map. [Verification](../verification-2026-10-12-v0.1.71.md). No engine build, runtime, third-party redistribution or CtZ gameplay change.

## Disposition and next work

WORLD-02 is complete within this selected native/contracts scope. World interaction/navigation remains partial under the [completion rule](../../04-game-systems/world/source-completion-status.md). **Next WORLD-03: use/touch, actor level transitions and marker lifecycle.** Effective supplied-consumer reconciliation and final consolidation/audit remain WORLD-04. [Guide](../../04-game-systems/world/development-reference.md), [roadmap](../../ROADMAP.md).
