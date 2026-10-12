# FAC-01 — Native faction identity and relation queries

> ADR document set: **v0.1.63**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-01
- Subsystem: factions / relations
- ADR revision: v0.1.44
- Record status: complete-within-scope
- Source status: source-confirmed within selected native definitions/registrations
- Runtime status: untested; deferred until explicitly resumed by the user
- Baseline IDs and provenance: ENGINE1011; [October 11 archive](../../00-environment/source-baseline-2026-10-11.md)
- Last reviewed: 2026-10-11

## Question and scope

What are native character-community identity, personal/community goodwill and final relation categories, and how do the selected Lua interfaces differ?

Include configured ID/index/team mapping and matrix loading, registry storage direction/fallback/limits, five-term attitude and threshold classification, directed versus mutual helper, selected stalker/trader/base virtual resolution, two different general-goodwill queries, and direct setters needed to explain those query contracts. Exclude installed faction values, complete action/fight updates, faction-change propagation, serialization/reset/ID cleanup closure, all actor/monster overrides, AI enemy reevaluation, diplomacy addons and runtime tests. Completion requires a source-pinned foundation reference and focused API contracts; it does not complete the faction subsystem.

## Evidence and method

ENGINE1011 archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit and installed executable/configuration correspondence unknown. [Ledger F01–F18](../../evidence/factions/native-relations-2026-10-11.csv) records 18 files, selected symbols/ranges, full-file hashes and line counts.

Read character-community and generic loader definitions; registry declarations/bodies/templates; game-object declarations/registrations/wrappers; registry module helpers; stalker/trader overrides and base monster path. Compare receiver/argument direction, aggregation, validation and selected writes. No public configuration substituted for the user's installed profile.

## Findings

The [native reference](../../04-game-systems/factions/native-relations.md) and [Lua contract table](../../02-lua-api/factions/relations-api.md) carry nearby evidence citations.

- Configured character IDs, indexes and team values differ. Matrix rows resolve by ID, columns by index; numeric indexes are configuration-order dependent. Lookup is not shown to normalize arbitrary input case. F01–F04/F08.
- Personal goodwill is source-to-target; community goodwill is community-to-character and stored with the target. Missing entries return neutral zero. Matrix writes affect one directed cell. F01/F06/F07.
- Final character attitude includes personal, reputation, rank, community-to-character and community-to-community terms. Threshold comparison uses literal configured keys, including `attitude_neutal_threshold`. No active threshold values are established. F05/F06.
- `GetRelationBetween` combines both directions, while the selected stalker/trader `relation` paths use directed `GetRelationType`. Base monster matrix resolution is a separate path. F05/F13–F17.
- `game_object:general_goodwill` uses five terms; module `relation_registry.get_general_goodwill_between` uses three and requires server trader casts. Similar naming does not make them interchangeable. F05/F09–F11/F18.
- Relation enum setter selects a personal preset without compensating other attitude terms. Force-set subtracts the two community contributions, omits rank/reputation compensation and writes directly rather than using the selected clamp. F05/F06/F10/F11.
- Type/error, ID-cast and object-lifetime requirements differ between client methods and module helpers. Valid community names and object representations are required; no nil-safe/general success return contract is inferred. F03/F09–F13/F18.

## Competing explanations and missing edges

Observed hostility can depend on a different receiver virtual path, changed personal/community terms, rank/reputation or installed scripts; strategic ownership is separate. Missing effective configuration and addon consumers prevent an installed diagnosis. Native setter inspection does not establish timing of AI reevaluation, callback dispatch, save durability or display refresh. Those chains remain explicit subsequent work.

## Checks and outcomes

Compared selected definitions, signatures, registrations and callers; verified ledger hashes, line counts, range bounds and symbols. Repository navigation/version and preservation checks are recorded in [v0.1.44 verification](../verification-2026-10-11-v0.1.44.md). No engine compilation, runtime tests, source redistribution, gameplay edits or license addition.

## Disposition and next work

FAC-01 is complete within its query-foundation scope; the subsystem remains partial. Next FAC-02: relation persistence/reset/ID cleanup, followed by faction identity mutation and action-driven goodwill paths. Then connect supplied Warfare relation consumers and installed diplomacy overrides where evidence exists. Runtime verification remains deferred; see [roadmap](../../ROADMAP.md).
