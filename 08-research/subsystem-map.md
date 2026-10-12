# Subsystem entry point map

> ADR document set: **v0.1.71**. Research revisions and source/build versions below describe their original scope.

This map identifies the ten currently researched behavior subsystems. Each has a README for browsing, a development reference for practical synthesis and links, and a source-completion status for readiness, missing effective inputs and runtime limits. These are different roles; adding a guide does not mark research complete.

| Subsystem | Folder entry | Central guide | Status and gaps | Research/audit scope |
| --- | --- | --- | --- | --- |
| UI/PDA | [README](../03-ui-pda/README.md) | [Development reference](../03-ui-pda/development-reference.md) | [Completion status](../03-ui-pda/source-completion-status.md) | UI API and per-page scoped audits |
| A-Life | [README](../04-game-systems/alife/README.md) | [Development reference](../04-game-systems/alife/development-reference.md) | [Completion status](../04-game-systems/alife/source-completion-status.md) | ALIFE-10/11 and v0.1.43 audit |
| Warfare | [README](../04-game-systems/warfare/README.md) | [Development reference](../04-game-systems/warfare/development-reference.md) | [Completion status](../04-game-systems/warfare/source-completion-status.md) | WAR-002/003 and shared v0.1.43 audit |
| Factions/relations | [README](../04-game-systems/factions/README.md) | [Development reference](../04-game-systems/factions/development-reference.md) | [Completion status](../04-game-systems/factions/source-completion-status.md) | FAC-06 and v0.1.49 audit |
| Persistence | [README](../04-game-systems/persistence/README.md) | [Development reference](../04-game-systems/persistence/development-reference.md) | [Completion status](../04-game-systems/persistence/source-completion-status.md) | PER-04 and v0.1.53 audit |
| Inventory | [README](../04-game-systems/inventory/README.md) | [Development reference](../04-game-systems/inventory/development-reference.md) | [Completion status](../04-game-systems/inventory/source-completion-status.md) | ITEM-05 and v0.1.58 audit |
| Trade/economy | [README](../04-game-systems/economy/README.md) | [Development reference](../04-game-systems/economy/development-reference.md) | [Completion status](../04-game-systems/economy/source-completion-status.md) | ECO-03 and v0.1.62 audit |
| Tasks/dialogue/info | [README](../04-game-systems/tasks/README.md) | [Development reference](../04-game-systems/tasks/development-reference.md) | [Completion status](../04-game-systems/tasks/source-completion-status.md) | TASK-01–03 consolidation and v0.1.69 audit; effective integration partial |
| World interaction/navigation | [README](../04-game-systems/world/README.md) | [Development reference](../04-game-systems/world/development-reference.md) | [Completion status](../04-game-systems/world/source-completion-status.md) | WORLD-01 inventory and WORLD-02 selected spatial contracts; WORLD-03/04 pending; v0.1.71 verification |
| Gameplay state | [README](../04-game-systems/gameplay/README.md) | [Development reference](../04-game-systems/gameplay/development-reference.md) | [Completion status](../04-game-systems/gameplay/source-completion-status.md) | GAME-04 and v0.1.66 audit |

UI/PDA retains its established 03-ui-pda location; A-Life and Warfare retain distinct guides while their combined closure requirements remain authoritative in A-Life completion status. Detailed pages, API catalogs, dated investigations, evidence and historical snapshots stay in their canonical homes.

Environment, cross-system engine architecture, mod architecture, debugging, examples and project records are other document categories. They do not require artificial subsystem completion pages merely to match filenames. World interaction/navigation uses that pattern for its inventory and selected spatial contracts; it remains partial.

Use [layout rules](repository-layout.md), [workflow](workflow.md), [full index](../INDEX.md) and [current roadmap](../ROADMAP.md). This map is navigation, not an exhaustive engine subsystem inventory.
