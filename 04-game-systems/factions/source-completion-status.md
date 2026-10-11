# Faction source completion and remaining work

> ADR document set: **v0.1.49**. Research revisions and source/build versions below describe their original scope.

**As of 11 October 2026:** planned native and selected supplied-package faction research, practical consolidation and bounded final available-source audit are complete within scope. The reference is ready for development use **within those documented source boundaries**. Full effective GAMMA/CtZ faction integration remains **partial**. Runtime is **untested** and deferred until the user explicitly resumes it.

## Completed available-source work

| Area | Record / reference | Disposition |
| --- | --- | --- |
| Native configured identity, goodwill and relation resolution | [FAC-01](../../08-research/investigations/2026-10-11-FAC-01-native-relations.md), [reference](native-relations.md) | Selected query foundations and focused Lua contracts complete |
| Native persistence/reset/ID cleanup | [FAC-02](../../08-research/investigations/2026-10-11-FAC-02-relation-persistence.md), [reference](relation-persistence.md) | Storage/lifetime boundaries traced; installed diplomacy persistence still open |
| Native community mutation and team/group effects | [FAC-03](../../08-research/investigations/2026-10-11-FAC-03-community-mutation.md), [reference](community-mutation.md) | Selected bridge/hierarchy/packet chain complete; strategic conversion still open |
| Native action, rank/reputation and flag contracts | [FAC-04](../../08-research/investigations/2026-10-11-FAC-04-action-goodwill.md), [reference](action-goodwill.md) | Selected outcomes/contributions complete; not every installed award |
| Supplied Warfare faction/relation consumers | [FAC-05](../../08-research/investigations/2026-10-11-FAC-05-warfare-consumers.md), [reference](warfare-relation-consumers.md) | Main-package helpers/consumers traced; variants/winners remain qualified |
| Practical consolidation and bounded consistency review | [FAC-06](../../08-research/investigations/2026-10-11-FAC-06-faction-consolidation.md), [development reference](development-reference.md), [audit](../../08-research/verification-2026-10-11-v0.1.49.md) | Planned available-source final step complete |

## Required for effective-source closure

| Remaining contract | Needed sources/provenance | Closure evidence |
| --- | --- | --- |
| Identity and diplomacy | Winning globals/true-community/disguise helpers, game-relations scripts, configured community/team order and relevant native/script tables | Resolve all identity mappings, relation direction/thresholds and active setter/predicate replacements |
| Startup and persistence | Effective dispatcher/listeners, storage/save_var/load_var implementations, marshal settings and load/reset/restore producers | Trace execution order, matrix reapplication, campaign/ID cleanup and durability boundaries |
| Awards and death | Winning creature/squad death handlers, rank/reward helpers, offline combat and later addons | Identify native versus script awards, callback phase, online/offline convergence and deduplication authority |
| Strategic reassignment and CtZ integration | Effective board/smart/squad ownership and faction-switch helpers, CtZ reconciliation | Establish membership, assignment, owner synchronization and UI update contracts after identity changes |

These overlap the [A-Life/Warfare effective-source backlog](../alife/source-completion-status.md). A supplied file is evidence of that package's implementation, not proof it wins in the installed profile. Use the [package source requirements](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md) when collecting actual winners/dependencies. No installation values are inferred from comments, declaration defaults or archive labels.

## Runtime and stopping rule

After explicit user authorization, identify executable/build/profile/configuration and record repeatable relation-query, faction-change, online/offline award, save/load/reset, cleanup and strategic/display observations. Documentation checks do not promote runtime confidence.

Close the effective contracts above and reconcile results into the reference before marking the complete installed integration **development-reference ready at source level / runtime pending**. Exhaustive unrelated AI types, every binding/converter/build combination and all quest/dialog consumers remain optional expansions. The planned work possible from current snapshots is finished; another ADR subsystem can proceed independently.

Research conclusions, dated records, baseline pins and existing evidence remain preserved. Later corrections must identify their source basis and affected claims. [Roadmap](../../ROADMAP.md).
