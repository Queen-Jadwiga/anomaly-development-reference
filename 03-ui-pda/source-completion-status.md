# UI and PDA source completion and remaining work

> ADR document set: **v0.1.71**. Research revisions and source/build versions below describe their original scope.

The documented UI/PDA source foundation is development-reference ready within its recorded selected scope. Detailed pages retain their own source baselines and inventory limits; this navigation change does not imply exhaustive binding/converter/build coverage or installed compatibility.

Independent runtime verification remains deferred. [REV-01 external observations](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md) are separately attributed and do not certify the user's installation. Quickload/lifetime and live-tab load-readiness investigations remain open.

| Remaining contract | Required evidence |
| --- | --- |
| Effective PDA/addon integration | Winning registry/pda/XML, MAC and other wrappers, assets/fonts and startup/replacement order |
| Lifetime and readiness | Owned display-registration teardown, applicable parent/GC/holder paths, deliberate verified post-load registration phase |
| Callback/input behavior | Installed dispatch/listener order, focus/key routing, event producer and propagation paths |
| Runtime presentation/compatibility | Identified build/profile and repeatable tab, ownership, fonts, scaling, input, quickload and level-change observations |

Optional exhaustive binding/overload/converter/inherited emitter and renderer/build coverage remains later depth. Use [central development reference](development-reference.md) and [API catalog](../02-lua-api/ui/README.md) for completed source paths; [roadmap](../ROADMAP.md#uipda-remaining-work) for ongoing work.
