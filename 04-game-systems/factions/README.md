# Factions and relations

> ADR document set: **v0.1.46**. Research revisions and source/build versions below describe their original scope.

**Current revision: v0.1.46.** Subsystem status: partial. Native query foundations are complete within the selected source scope; installed faction/diplomacy behavior remains unverified. Runtime verification is deferred until the user explicitly resumes it.

- [Native identity, goodwill and relation resolution](native-relations.md).
- [Focused Lua contracts](../../02-lua-api/factions/relations-api.md).
- [FAC-01 investigation](../../08-research/investigations/2026-10-11-FAC-01-native-relations.md).
- [Source evidence](../../evidence/factions/README.md).

The foundation distinguishes configured community identity, directed contributions, final character attitude, virtual object relation, Warfare smart ownership and CtZ owner state. No installed relation matrix or universal hostility rule is inferred.

[Native relation persistence/reset/ID cleanup](relation-persistence.md) and [FAC-02](../../08-research/investigations/2026-10-11-FAC-02-relation-persistence.md) are complete within scope.

[Native community mutation and team/group effects](community-mutation.md), [focused APIs](../../02-lua-api/factions/community-mutation-api.md) and [FAC-03](../../08-research/investigations/2026-10-11-FAC-03-community-mutation.md) are complete within scope.

Next source work: action-driven goodwill updates; then supplied Warfare consumers and effective diplomacy configuration/overrides. See [current roadmap](../../ROADMAP.md).
