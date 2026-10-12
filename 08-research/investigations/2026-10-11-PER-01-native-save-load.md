# PER-01 — Native save/load pipeline and Lua extension boundaries

> ADR document set: **v0.1.55**. Research revisions and source/build versions below describe their original scope.

- ID: PER-01
- Subsystem: persistence
- ADR revision: v0.1.50
- Record status: complete-within-scope
- Source status: source-confirmed within selected single-player A-Life paths
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline/provenance: ENGINE1011; [October 11 source](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

## Question and scope

How does the selected native A-Life save/load pipeline frame and restore data, and where do native-to-Lua storage hooks and binder serialization occur?

Include selected server request/delegation and client quick-load boundary, live state preparation/custom save packets, `.scop` envelope/chunk order, object/auxiliary serializers, filename/buffer load phases and late group repair, named hooks and selected binder forwarding/relevance. Exclude every save/UI/reconnect/constructor route, complete binary schema/compatibility/integrity certification, full spawn-pack remapping, installed Lua storage implementation, every entity serializer and runtime tests. Completion is a pinned native architecture/extension reference; persistence subsystem remains partial.

## Evidence and method

ENGINE1011 archive hash `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; exact upstream commit/executable/build/effective script correspondence unknown. [Ledger S01–S24](../../evidence/persistence/native-pipeline-2026-10-11.csv) records selected paths, symbols, ranges, whole-file hashes and counts.

Read native request/storage/packet/serializer/registration bodies. Distinguish message request from reconstruction, server state from custom client bytes, filename storage from binder load, native emission from installed listener. Reuse ALIFE-04/06/07 and FAC-02 identity/persistence boundaries rather than rewriting their conclusions.

## Findings

[Pipeline reference](../../04-game-systems/persistence/native-save-load-pipeline.md) and [extension contracts](../../02-lua-api/persistence/native-extension-contracts.md) provide nearby S-citations.

- Packet save prepares client updates/save data; direct filename save differs. Load request edits server options; selected client quick-load later replaces simulator. S01/S05–S08/S22–S24.
- Compressed `.scop` framing and serializer order are explicit; version predicate checks sentinel/minimum/version, not full payload integrity or installed compatibility. External spawn/configuration dependencies remain. S01–S04/S09–S12.
- Objects serialize selected server spawn/update packets and retained custom bytes; auxiliary registry order is explicit. Unavailable factory section can skip an object in the selected loader. Arbitrary Lua state is not automatically included. S09/S10/S21.
- Named load hook precedes native reconstruction. Final native registration follows auxiliary load, while filename-level group repair is later. No universal installed Lua/client readiness callback follows. S01/S13/S14.
- Binder methods are explicit virtual serialization, relevance-gated in selected enumeration; save/load defaults empty and errors can clear the binder. They occur in a separate custom-data/spawn phase. S07/S15–S19.
- Supplied define file enables the native named-hook macro; actual binary/listeners and script storage/atomicity remain unknown. S01/S20.

## Missing edges and alternatives

Other entry/transport modes or installed serializers can add stages/files and change dispatch. A native writer closing does not certify script companion data, every client packet, crash-safe atomicity or all addon schema completion. A passed version predicate does not prove whole-save correctness. Current runtime observations and effective wrappers are unavailable.

## Checks and disposition

Review signatures/phase order, message consumers, constants/chunks, source filters, pointer/relevance/exception boundaries and validation scope. Verify hashes/counts/ranges/symbols and repository preservation/navigation/version tests; [increment report](../verification-2026-10-11-v0.1.50.md). No engine build, gameplay/save edits, license addition or source redistribution.

PER-01 completes the selected native pipeline/extension pass. Next PER-02: supplied Lua storage helper contracts and effective-profile gaps; then CtZ campaign identity/reconciliation and eventual consolidation/audit. Runtime stays deferred. [Roadmap](../../ROADMAP.md).
