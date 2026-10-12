# Configuration and script integration

> ADR document set: **v0.1.76**. Research revisions and source/build versions below describe their original scope.

Start with the [development reference](development-reference.md). CONFIG-01 inventory, CONFIG-02 LTX/INI/DLTX and CONFIG-03 loading/startup/shared callback contracts are **complete within scope**; configuration/script integration remains **partial**, and runtime verification is deferred.

- [Script loading/startup/callback behavior](script-loading-startup-callbacks.md), [lookup/callback APIs](../../02-lua-api/configuration/script-callback-api.md), [CONFIG-03 investigation](../../08-research/investigations/2026-10-12-CONFIG-03-script-loading-startup-callbacks.md), [contract verification](../../08-research/verification-2026-10-12-v0.1.76.md).
- [LTX/INI/DLTX behavior](ltx-ini-dltx.md), [Lua INI contracts](../../02-lua-api/configuration/ini-api.md), [CONFIG-02 investigation](../../08-research/investigations/2026-10-12-CONFIG-02-ltx-ini-dltx.md) and [contract verification](../../08-research/verification-2026-10-12-v0.1.75.md).
- [Coverage inventory](coverage-inventory.md) and [completion status](source-completion-status.md).
- [CONFIG-01 investigation](../../08-research/investigations/2026-10-12-CONFIG-01-existing-coverage.md), [evidence](../../evidence/configuration/README.md), [inventory verification](../../08-research/verification-2026-10-12-v0.1.74.md).
- Established domain controls and UI/DXML/callback/storage records remain canonical through the inventory's links.

Next: CONFIG-04 — supplied options/patch consumers, consolidation and bounded audit. [Roadmap](../../ROADMAP.md).
