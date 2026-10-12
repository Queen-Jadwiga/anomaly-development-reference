# Reusable code library

> ADR document set: **v0.1.79**. Research revisions and source/build versions below describe their original scope.

Only promote code after specifying dependency/version and test status. Early examples should be called **experimental**, not drop-in verified.

[ARCH-01 inventory](../05-mod-architecture/coverage-inventory.md) identifies existing coverage and gaps. Current [minimal UI patterns](../03-ui-pda/examples/minimal-static-ui-patterns.md) are two non-runnable call sketches assuming initialized owned widgets. ARCH-03 will consolidate selected qualified patterns/test guidance after architecture and diagnostic contracts; no new runtime-tested example is introduced by the inventory. [Roadmap](../ROADMAP.md).

[ARCH-02 interface/ownership contracts](../05-mod-architecture/module-state-contracts.md) and [package support fields](../05-mod-architecture/compatibility-package-contracts.md) provide design review guidance. They introduce no runnable or runtime-tested example. DEBUG-01 precedes ARCH-03 patterns/test guidance and bounded consolidation.
