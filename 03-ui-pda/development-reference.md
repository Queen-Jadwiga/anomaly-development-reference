# UI and PDA development reference

> ADR document set: **v0.1.75**. Research revisions and source/build versions below describe their original scope.

- ID: STRUCT-01-UI
- Subsystem: UI/PDA
- Reference revision: v0.1.67 navigation synthesis
- Source status: synthesis of linked source-confirmed selected paths and scoped catalogs
- Runtime status: independent verification deferred; selected external observations retained with their build limits
- Baselines/provenance: each linked record retains May/October or pinned September scope; [environment](../00-environment/source-baseline-2026-10-11.md), [manifest](../evidence/manifest.md)
- Last reviewed: 2026-10-12

Start here for UI/PDA development. Detailed research already exists across engine architecture, UI behavior, API catalogs and investigations. This guide organizes it under the same central entry pattern as newer subsystems. The documented source foundation is usable within scope; [installed-source/runtime closure](source-completion-status.md) remains separate. Moving or linking an older page does not revalidate its baseline.

## Construction and lifetime first

Widget allocation, XML initialization, parent attachment, AutoDelete, Luabind ownership and native display registration are separate. Trace the matching creation/registration and teardown path before relying on a Lua reference or generic finalizer. The [construction/ownership reference](ui-construction-ownership.md) and [native/Lua architecture](../01-engine/ui-lua-native-integration.md) retain exact source and ownership distinctions.

| Development question | Detailed guide | Supporting catalog/research |
| --- | --- | --- |
| Native widget construction and XML bridge | [Construction/ownership](ui-construction-ownership.md), [bridge](../01-engine/lua-xml-bridge-callflow.md) | [Part C investigation](../08-research/investigations/2026-10-09-part-C-ui-construction.md) |
| XML loading, callbacks and errors | [Loading paths](xml-loading-paths-ui04a-oct11.md), [DXML lifecycle](xml-dxml-native-lifecycle-oct11.md), [errors](xml-dxml-callback-errors-ui04b-oct11.md) | [DXML pipeline](dxml-pipeline-oct11.md) |
| Dynamic PDA tabs and subdialogs | [Tab survey](dynamic-pda-tabs-oct11.md), [subdialog lifecycle](pda-subdialog-lifecycle-oct11.md) | Native menu/registry versions and active section differ |
| Input, focus and event dispatch | [Input/events](ui-input-events-oct11.md), [registration/focus](ui06a-d-registrations-events-focus-oct11.md) | [Supplementary audit](ui06-supplementary-registration-emission-build-modal-oct11.md) |
| Rendering, scaling, typography and assets | [Rendering survey](ui-rendering-scaling-fonts-textures-oct11.md), [controls/typography](ui-controls-typography-survey-oct11.md), [font manager](font-manager-and-lua-getters.md) | Historical font lifecycle findings retain May-era scope |
| Available bindings and scoped emitters | [UI API catalog](../02-lua-api/ui/README.md), [widget/event inventory](ui-widget-event-inventory-oct11.md) | Lexical occurrence counts are not exhaustive ABI guarantees |

## Runtime reports and readiness

[REV-01](../08-research/investigations/2026-10-12-REV-01-external-runtime-issues.md) records externally reported quickload/display-registration and dynamic-tab rebuild hazards. Their observed build/setup and inferred mechanisms remain distinct. `level.present()` or a menu pointer is not a universal readiness gate; a fixed delay and a full tab strip do not prove safe registration. Match removal to owned display registration, while respecting different parent/PDA ownership paths. Detailed guidance remains in the construction and dynamic-tab pages.

Before integrating a PDA feature, identify the installed registry, pda script/XML, MAC/other addon wrappers, assets/fonts and callback startup/teardown. Keep content state separate from native window lifetime. No independently tested UI construction/teardown or cross-addon compatibility recipe is added by this guide.

## Older starter pages

[PDA architecture starter](pda-architecture.md), [widgets](widgets.md), [fonts](fonts.md) and [XML layouts](xml-layouts.md) retain early questions/patterns and their stated scope. They are not current completeness checklists. Use this guide and [completion status](source-completion-status.md) for current navigation; use individual dated research for exact evidence. [Full index](../INDEX.md), [roadmap](../ROADMAP.md).
