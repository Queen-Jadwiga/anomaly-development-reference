# Actor and NPC gameplay state

> ADR document set: **v0.1.64**. Research revisions and source/build versions below describe their original scope.

**Current revision: v0.1.64.** Subsystem partial; runtime untested and deferred.

- [Native health and condition hit processing](native-condition.md).
- [Live condition Lua contracts](../../02-lua-api/gameplay/condition-api.md).
- [GAME-01 investigation](../../08-research/investigations/2026-10-12-GAME-01-native-condition.md).
- [Evidence](../../evidence/gameplay/README.md).

Existing faction attack/kill actions, A-Life/Warfare casualty phases and inventory consumption remain separate linked contracts. Actor-specific survival/boosters/equipment is complete within GAME-02 scope. Next derived death/condition persistence/effective consumers; consolidation follows. [Roadmap](../../ROADMAP.md).

[GAME-02 actor effects and equipment](actor-effects-equipment.md) and [Lua subset](../../02-lua-api/gameplay/actor-effects-api.md) complete within selected scope. Next derived death/server-client condition restoration and effective consumers, then consolidation/audit.
