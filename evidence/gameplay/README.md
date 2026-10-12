# Gameplay state evidence

> ADR document set: **v0.1.75**. Research revisions and source/build versions below describe their original scope.

[Native condition ledger](native-condition-2026-10-12.csv): G01–G21, ENGINE1011 archive-relative paths, full-file hashes and line/symbol ranges. IDs are ledger-local. [Reference](../../04-game-systems/gameplay/native-condition.md), [investigation](../../08-research/investigations/2026-10-12-GAME-01-native-condition.md), [manifest](../manifest.md). Source checks are not installed/runtime verification.

- [Actor effects/equipment ledger](actor-effects-2026-10-12.csv), A01–A21; [GAME-02](../../08-research/investigations/2026-10-12-GAME-02-actor-effects.md).

- [Death/condition restoration](death-restoration-2026-10-12.csv), R01–R19; [GAME-03](../../08-research/investigations/2026-10-12-GAME-03-death-restoration.md).

[GAME-04 consolidation/audit](../../08-research/investigations/2026-10-12-GAME-04-gameplay-consolidation.md) reuses all 61 ledger entries without altering bytes/schema; [verification](../../08-research/verification-2026-10-12-v0.1.66.md).
