# Capture the Zone integration

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

[Capture the Zone](https://github.com/Queen-Jadwiga/capture-the-zone) contains the gameplay project separately. ADR contains source-qualified engine/interfaces/persistence/architecture findings and reproducible notes.

Selected CtZ research uses CTZ005J: Alpha 0.0.5j at commit `eba6660db09353dcc42a195ae6e7e706f4762277`. That pin is not a statement about current mod HEAD or the installed copy. [Campaign safety reference](../../04-game-systems/persistence/ctz-campaign-safety.md), [provenance](../../00-environment/provenance-register.md).

The initial War PDA, native font/widget, faction-state and strategic-statistics aims remain project context, not a crash-safe runtime guarantee. [Practical guide](../../05-mod-architecture/development-reference.md), [whole-reference status](../../08-research/reference-status.md). No CtZ gameplay changes are part of ADR-01; runtime verification stays deferred.
