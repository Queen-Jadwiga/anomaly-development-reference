# Mod architecture and GAMMA compatibility

> ADR document set: **v0.1.78**. Research revisions and source/build versions below describe their original scope.

Start with the [practical architecture/debugging coverage inventory](coverage-inventory.md). ARCH-01 inventory is **complete within scope**; the practical foundation remains **partial**, and runtime verification is deferred.

- [ARCH-01 investigation](../08-research/investigations/2026-10-12-ARCH-01-existing-coverage.md), [pinned evidence](../evidence/architecture/README.md), [inventory verification](../08-research/verification-2026-10-12-v0.1.78.md).
- Reuse [configuration/script integration](../04-game-systems/configuration/development-reference.md), [UI lifetime](../03-ui-pda/development-reference.md), [A-Life identity](../04-game-systems/alife/development-reference.md), [persistence](../04-game-systems/persistence/development-reference.md) and [effective-profile provenance](../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).
- [Debugging entry](../06-debugging/README.md), [example qualification](../07-code-library/README.md), [source-tool tests](../tests/README.md).

Next ARCH-02: module/state ownership and compatibility contracts. DEBUG-01 then traces selected logging/crash routes; ARCH-03 adds qualified examples/test guidance and consolidates/audits. File layout, dependencies, patching, packaging and migration still require those bounded practical passes; no generic installed compatibility or tested drop-in architecture is certified. [Roadmap](../ROADMAP.md).
