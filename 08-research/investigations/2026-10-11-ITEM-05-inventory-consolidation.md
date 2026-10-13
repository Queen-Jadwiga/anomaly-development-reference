# ITEM-05 — Inventory consolidation and bounded audit

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

- ID: ITEM-05
- Subsystem: inventory/item lifecycle
- ADR revision: v0.1.58
- Record status: complete-within-scope
- Source status: scoped-source-audit; selected underlying contracts source-confirmed
- Runtime status: untested; deferred
- Baseline IDs and provenance record: ENGINE1011; [source record](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

## Question and scope

Can ITEM-01–04 be used as a coherent general-modding inventory reference without collapsing ownership, placement, activation, effects, removal and reconstruction phases? Include current references/APIs, ledger integrity and selected native producer/consumer order. Completion requires practical consolidation, bounded semantic review, navigation/provenance checks and explicit stopping/gap rules. Exclude new gameplay code, effective-profile closure, exhaustive derived classes and runtime verification.

## Evidence and method

Reuse four immutable inventory ledgers: [I01–I20](../../evidence/inventory/ownership-lifecycle-2026-10-11.csv), [P01–P19](../../evidence/inventory/placement-activation-2026-10-11.csv), [D01–D18](../../evidence/inventory/consumption-destruction-2026-10-11.csv), [R01–R15](../../evidence/inventory/persistence-reconstruction-2026-10-11.csv). Archive SHA-256 `withheld-upload-fingerprint`; unknown upstream commit and executable/profile correspondence remain unknown. No copied/renumbered evidence ledger is introduced.

Compare reference/API claims with declarations, registrations, wrappers, selected server/actor/base-owner consumers and persistence inheritance order. Reread risk-bearing source bodies; separate scoped semantic review from mechanical verification of all ledger rows. Detailed matrix and outcomes are in [verification](../verification-2026-10-11-v0.1.58.md).

## Findings

[Practical reference](../../04-game-systems/inventory/development-reference.md) consolidates state owners, request/return limits, callback phases, consumption/removal and saved-state reconstruction. No new contradiction requiring reversal of the four passes was found within this bounded review. Clarify ITEM-04 current reference: actor strict Take bypasses ordinary placement predicates, so fallback wording must not imply normal eligibility revalidation. Clarify native Eat/ClientEat: the H_Parent ID comparison dereferences a required valid parent; it is not a null-safe rejection predicate. These qualifications use existing R12/R13/P01–P03 and D01 ranges; dated investigations and ledger bytes are preserved.

## Competing explanations and missing edges

Names such as trade, safe wrapper, changed slot and net load do not establish payment, safe rollback, weapon readiness or settled restored membership. Later derived/effective code can alter final state or callback delivery. No runtime bug, NPC equipment recipe, universal completion barrier or malformed-state recovery guarantee is inferred. [Completion rule](../../04-game-systems/inventory/source-completion-status.md) lists remaining evidence.

## Checks and outcomes

Local base blobs checked against published v0.1.57 tree. Prior ledger/history bytes and dated investigation bodies preserved apart from current banners. Source hashes/counts/ranges/symbols, unchanged catalog reproduction, repository navigation/version/CSV checks and existing validator tests recorded in verification. No engine build, game/save modification or runtime test.

## Disposition and next work

Available-source first-edition inventory pass complete-within-scope; effective integration partial and runtime deferred. Next general subsystem: trade/economy, beginning with inventory of existing coverage and selected money/pricing/transaction/configuration ownership. [Roadmap](../../ROADMAP.md).
