# Factions and relations

> ADR document set: **v0.1.80**. Research revisions and source/build versions below describe their original scope.

**Current revision: v0.1.80.** Planned native and selected supplied-package research, consolidation and bounded source audit are complete within scope. Full effective GAMMA/CtZ integration remains partial; runtime verification remains deferred until the user explicitly resumes it.

Start with the [practical development reference](development-reference.md) and [completion status](source-completion-status.md).

| Topic | Detailed source reference | Focused API |
| --- | --- | --- |
| Identity, goodwill and relation resolution | [FAC-01](native-relations.md) | [Relation queries/setters](../../02-lua-api/factions/relations-api.md) |
| Save/load, matrix reset and ID cleanup | [FAC-02](relation-persistence.md) | Native storage boundaries in reference |
| Community mutation and team/group effects | [FAC-03](community-mutation.md) | [Community/team contracts](../../02-lua-api/factions/community-mutation-api.md) |
| Action-driven goodwill, rank and reputation | [FAC-04](action-goodwill.md) | [Values and flags](../../02-lua-api/factions/action-values-api.md) |
| Supplied Warfare faction/relation consumers | [FAC-05](warfare-relation-consumers.md) | Script helper/consumer map in reference |

[Source ledgers](../../evidence/factions/README.md), [FAC-06 synthesis](../../08-research/investigations/2026-10-11-FAC-06-faction-consolidation.md), [final available-source audit](../../08-research/verification-2026-10-11-v0.1.49.md), [full index](../../INDEX.md).

Configured community identity, directed contributions, derived character attitude, virtual live-object relation, Warfare ownership and CtZ owner state remain distinct. No installed relation matrix, universal hostility rule or automatic owner synchronizer is inferred.

Effective identity/diplomacy, storage/dispatch, rewards/death and strategic reassignment remain open in the [completion status](source-completion-status.md) and [roadmap](../../ROADMAP.md). The planned work from current snapshots is finished; later corrections require an explicit source basis.
