# Mod architecture and GAMMA compatibility

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

Start with [module/state ownership contracts](module-state-contracts.md) and [compatibility/dependency/package contracts](compatibility-package-contracts.md). **ARCH-02 is complete within selected synthesis scope**; effective integration and the remaining practical foundation are partial. Runtime verification remains deferred.

- [ARCH-02 investigation](../08-research/investigations/2026-10-12-ARCH-02-module-state-compatibility.md), [26 pinned documentation boundaries](../evidence/architecture/README.md), [verification](../08-research/verification-2026-10-12-v0.1.79.md).
- [ARCH-01 coverage inventory](coverage-inventory.md) preserves the original gaps and allocation. Existing source guides remain authoritative: [configuration/script integration](../04-game-systems/configuration/development-reference.md), [UI lifetime](../03-ui-pda/development-reference.md), [A-Life identity](../04-game-systems/alife/development-reference.md), [persistence](../04-game-systems/persistence/development-reference.md) and [effective-profile provenance](../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md).
- [Debugging entry](../06-debugging/README.md), [example qualification](../07-code-library/README.md), [source-tool tests](../tests/README.md).

Next DEBUG-01 traces selected logging/crash routes; ARCH-03 adds qualified patterns/test guidance and consolidates/audits. Proposed mod contracts are design guidance, not an implemented framework or installed compatibility result. No tested drop-in architecture is certified. [Roadmap](../ROADMAP.md).
