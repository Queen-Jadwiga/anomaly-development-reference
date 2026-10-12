# Tasks dialogue and info state development reference

> ADR document set: **v0.1.68**. Research revisions and source/build versions below describe their original scope.

This subsystem is in progress. Start with the [native foundation](native-task-dialogue-info.md), [Lua contracts](../../02-lua-api/tasks/native-task-info-api.md) and [completion status](source-completion-status.md). This central guide follows the common subsystem structure without implying a completed final consolidation.

| Requirement | Use this distinction | Detailed source |
| --- | --- | --- |
| Grant/update a player task | Native task state/deadline versus script-managed mission state | Native foundation task sections |
| Gate a dialogue choice | Actor info flags versus passed speaker and script predicate | Native foundation dialogue sections |
| Give a reward | Script side effect versus task completion callback/info return | Native foundation callback/action ordering; economy/inventory references |
| Restore a mission | Saved native fields versus reconstructed info lists/current functors | Native foundation task persistence; general persistence reference |

Do not equate “completed”, a true info/booster-style helper return, or a callback with atomic money/item delivery. Dialogue state, actor knowledge flags and campaign-owned records have separate authority/lifetime. Effective consumers and runtime remain open. Final practical consolidation follows the supplied-script/gap pass. [Roadmap](../../ROADMAP.md).
