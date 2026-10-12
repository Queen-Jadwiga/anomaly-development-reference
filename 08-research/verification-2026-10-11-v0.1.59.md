# ECO-01 increment verification — v0.1.59

> ADR document set: **v0.1.67**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-11
- Scope: selected native money/pricing/actor-menu trade and Lua money/cost
- Runtime: untested; deferred
- Publication base: v0.1.58, commit `d6f17f91228664241b1feac2fcb9335eb6aa6c76`

## Source review

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream/binary/profile unknown. [Ledger](../evidence/economy/native-trade-2026-10-11.csv): 23 entries. Read money field/setter/event consumer and selected saved state; wrapper signatures/registrations/saturation and mixed signed arithmetic; virtual cost and GetItemPrice; local/default factors; selected UI preflight/batch/per-item payment/callback order. Prior inventory/faction/persistence coverage linked rather than retraced as newly closed work.

Price directions, required discounts, commented eligibility/deficit branches, unsigned payment arithmetic and callback phase limits reviewed. TransferMoney hazard is literal qualified source arithmetic, not runtime reproduction or a source fix. Effective scripts/NPC variants/configuration/supplies and comprehensive numeric robustness remain outside this increment.

## Checks and preservation

Base local blobs compared with published v0.1.58 tree before editing. Preserve every prior path, prior CSV/history bytes and dated investigation bodies except current banners. Check all hash-bearing source ledger paths/hashes/counts/ranges/symbols against retained inputs; new symbols also checked inside cited ranges. Compare unchanged generated catalog files with retained reproduced outputs. Repository checker and seven existing validator tests pass; Actual checks: 550 hash-bearing evidence rows and 737 range groups validated; all new ledger symbols occur within cited ranges. Repository checker inspected 196 Markdown files, 1,419 local targets and 16 anchors; seven validator tests passed. Prior CSVs, history and dated investigation bodies passed preservation checks.

Publish using expected-head lease; compare complete remote path/blob map and read back VERSION/reference/head. Structural/source integrity checks do not prove runtime or effective integration. [Reference](../04-game-systems/economy/native-trade.md), [roadmap](../ROADMAP.md).

## Disposition

ECO-01 selected foundation complete within scope; economy partial. Next ECO-02 native configuration/supplies and supplied Lua consumer/effective gaps, then consolidation/audit. Runtime deferred. No game/save/source changes, engine build, source/assets redistribution or license addition.
