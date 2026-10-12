# ITEM-04 — Item persistence and reconstruction

> ADR document set: **v0.1.71**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-04
- Subsystem: inventory/item lifecycle
- ADR revision: v0.1.57
- Record status: complete-within-scope
- Source status: source-confirmed selected native/server/actor/eatable paths
- Runtime status: untested; deferred
- Baseline IDs and provenance record: ENGINE1011; [baseline](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

## Question and scope

How do selected items retain server/client fields, reconstruct ownership/placement and request saved active-slot restoration? Include registry packets, base inventory serializers, one concrete live item chain, eatable uses and selected actor/owner consumers. Completion requires separating saved fields from live membership/readiness, with explicit derived/effective gaps. Exclude exhaustive weapons/physics, all owner variants, effective GAMMA policy and runtime tests.

## Evidence and method

[Ledger](../../evidence/inventory/persistence-reconstruction-2026-10-11.csv): R01–R15, full-file hashes and line/symbol ranges against ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`. Read paired writers/readers, inheritance/callers and active versus commented code. Upstream commit and installed executable/script correspondence unknown.

## Findings

The [canonical reference](../../04-game-systems/inventory/persistence-reconstruction.md) records the claim/evidence mapping: R01/R02 server reconstruction and parent/custom bytes; R03–R06 base state/update/custom-save differences; R07–R10 virtual native/binder load and subsequent derived initialization; R11–R14 live take/placement/pending active selection; R15 selected derived server fields. In particular, binder load and client spawn callbacks are earlier phases than completed live inventory restoration, and the take callback precedes the owner's matching-slot activation request.

## Competing explanations and missing edges

Neither a generic update packet nor an earlier custom load establishes final derived condition. Actual installed binders, offline state return and NPC policies may add or replace behavior; they require effective source evidence. Saved placement can fall back under current eligibility. No observation establishes a bug in condition restoration, inventory duplication or active selection.

## Checks and outcomes

Verified new cited hashes, ranges and symbols; reviewed writer/reader and spawn/take order. Repository checker and existing validator tests recorded in [verification](../verification-2026-10-11-v0.1.57.md). No engine build/gameplay/save changes or runtime checks.

## Disposition and next work

Selected pass complete-within-scope; subsystem remains partial pending practical consolidation and bounded audit. Effective-source and runtime gaps remain open. [Roadmap](../../ROADMAP.md).
