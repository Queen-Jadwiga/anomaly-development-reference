# ECO-02 — Trader configuration and supplied economy consumers

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

- ID: ECO-02
- Subsystem: trade/economy
- ADR revision: v0.1.61
- Record status: complete-within-scope
- Source status: source-confirmed selected paths; scoped-source-audit missing-definition inventory
- Runtime status: untested; deferred
- Baseline IDs and provenance record: ENGINE1011/BETA150/ZIP142; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

## Question and scope

Trace native action parsing, default policy, supply requests, selected Lua bindings and supplied refresh/profile/NPC consumers. Close the available-source contract map and identify the exact missing effective inputs. Exclude full mechanic upgrades, every native NPC trade variant, unavailable stock tables, unrelated external mod source and runtime/CtZ changes.

## Evidence and method

[Ledger](../../evidence/economy/trader-configuration-2026-10-12.csv): T01–T21, file hashes, archive-relative paths and line/symbol ranges. [Supplied source scope](../../evidence/economy/supplied-source-scope-2026-10-12.json) records package inventory counts, manifest digest and absent core inputs. Archive pins: ENGINE1011 14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee; BETA150 9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d; ZIP142 566739c68b4597ab417e98ee9e3ce11858f3d42ed29a39d7e3c39ed2d76443a8. Upstream/installed winners and binary correspondence unknown. Read definitions, declarations, registrations and callers; compare comments to literal predicates and loop bounds.

## Findings

[Reference](../../04-game-systems/economy/trader-configuration.md) maps policy parsing/precedence and constructor factor-order discrepancy (T01–T05), destructive randomized supplies/spawn receipt limits and inactive native deficit pricing (T05–T07/T12/T13), exact void bindings (T08–T11), selected show/lifetime consumers (T14/T15), nearby restock timestamp wrapper/update requests (T16), supplied NPC inventory/money hazards (T17/T18) and Warfare profile/UI state consumers (T19–T21). [API page](../../02-lua-api/economy/trader-policy-api.md) distinguishes global and owner mutation.

## Competing explanations and missing edges

Installed scripts may override or bypass these helpers; supplied monkeypatch capture/registration does not identify effective execution order. Native request counts are not live delivered stock. Constructor field-name inversion and NPC inclusive loops/comment disagreement are source findings, not reproduced faults. Core trade/discount/gate/replenishment policy is absent. A UI stored option does not prove its consumer, scaling or persistence implementation. Preserve ECO-01's transfer_money concern without altering upstream source.

## Checks and outcomes

Check new ledger hashes, line ranges and symbols against declared roots; regenerate scoped missing-file inventory; preserve earlier CSV/history bytes and dated record bodies apart from revision banners. Run repository checker and its existing regression suite. [Verification](../verification-2026-10-12-v0.1.61.md) records results. No engine/game runtime execution.

## Disposition and next work

Available-source ECO-02 complete within scope; economy effective integration remains partial. Next practical consolidation and bounded consistency audit. Required winning managers, trade/item/economy configs, helper/binder startup order and runtime remain open in the [roadmap](../../ROADMAP.md).
