# CONFIG-04 — Supplied consumers, consolidation and bounded audit

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

- ID: CONFIG-04
- Subsystem: configuration/script integration
- ADR revision: v0.1.77
- Record status: complete-within-scope; effective integration partial
- Source status: selected native/supplied consumers confirmed; scoped package comparison/audit
- Runtime status: untested; deferred
- Baseline IDs and provenance: ENGINE1011, BETA150 main/explicit optional patches, ZIP142 via [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

How do selected supplied option definitions, reads/defaults, pending/backup, preset/apply/save/change, Warfare refresh, builders, unlocalizers and original captures use CONFIG-02/03 contracts? Trace available consumers, preserve caller/variant gaps, consolidate guidance and perform a bounded final audit. Close only this selected available-source pass; no installed winner selection, runtime/compilation, MCM/all-option/exhaustive VM audit or CtZ implementation.

## Evidence and method

[29-row ledger](../../evidence/configuration/supplied-options-patches-2026-10-12.csv) B01–B14/P01–P02/E01–E12/N01 pins 15 files/37 ranges. Read selected BETA150 option/preset/default/current/cache/apply and startup/refresh/assignment bodies; engine extension/builders/helper patch/original capture phases; native unlocalizer preprocessing. Optional declaration files are identified rather than merged. Source archive pins and unknown executable/upstream equivalence remain qualified.

[Seven comparisons](../../evidence/configuration/package-comparison-2026-10-12.csv) distinguish raw full-file hashes from cp1251-decoded CRLF-normalized GetValue-through-before-OnKeyboard slices. [Scope JSON](../../evidence/configuration/supplied-source-scope-2026-10-12.json) records requested filenames in ENGINE1011 gamedata/full BETA150/ZIP142 gamedata, plus declared main-preset includes. Original CONFIG-01 pins and CONFIG-02/03 ledgers/five-event correction remain authoritative.

## Findings

[Consumers](../../04-game-systems/configuration/supplied-options-patches.md) distinguish direct get/set from UI current/default/pending; preset conversion from native defaults; read-time writes from staged edits and sequential accept; config/console/keybind saves from gated dispatch; cancel from discard; copied Warfare fields from persistence. Higher-level new-row/default writes do not bypass native-derived existing-key checks without a proven effective class/instance/writer chain. B01–B14/E05–E07.

The option extension and dynamic-item installer hold originals in mutable shared slots; same-instance reinstallation can self-reference. These conditional source deductions are not observed crashes. Binder originals are captured per installation and trade original at evaluation. Builder table/metatable mutation and unlocalizer precompile exposure retain their own dependencies. E01–E12/N01; [helper API](../../02-lua-api/configuration/options-patch-api.md).

Five comparisons are equal. Optional ui_options files differ overall, while the selected normalized value/edit/accept/cancel methods match; declaration/default differences remain material. Main preset includes declares 13 files, four present there; base/other resources remain needed, not a proven installed failure. Scope counts are ENGINE1011 161, BETA150 62, ZIP142 29. Existing domain policy/lifecycle and confidence are retained.

## Competing explanations and missing edges

A getter can persist defaults, a displayed clamp is weaker than stored validation, and direct set is not option-change dispatch. Sequential accept is not a transaction. Retained faction/function references need not follow replacement. Identical methods and installer definitions cannot certify execution or profile compatibility. Winning global/class/exec/configuration/dispatcher/binder/storage inputs, optional selection, later patches and native/cache/debug/profile identity remain missing effective edges. No third-party fix or installed bug claim is introduced.

## Checks and outcomes

Audit all **114 CONFIG-02–04 source rows/156 ranges**, 18 original CONFIG-01 documentation pins, seven raw/slice comparisons and both CONFIG-03/04 availability scopes. Preserve prior evidence/history/generated/tool/test bytes and dated bodies except banners. Review parser/cache/ownership, initialization/handler/emission, identity/order/error/lifetime, option-state/apply and variant boundaries. Run repository validation/10 existing regressions; compare complete remote base/staged/published blob maps with expected-head update. [Verification](../verification-2026-10-12-v0.1.77.md). No runtime or engine compilation.

## Disposition and next work

CONFIG-01–04 planned available-source inventory/contracts/consumers/consolidation/audit are complete within selected scope; effective integration remains partial under the [completion rule](../../04-game-systems/configuration/source-completion-status.md). Next practical architecture/debugging existing-coverage inventory. [Guide](../../04-game-systems/configuration/development-reference.md), [roadmap](../../ROADMAP.md). Runtime deferred; no CtZ gameplay or third-party source/assets changes.
