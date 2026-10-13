# UI-07 — Button/checkbox Lua contracts and over-permissive fixtures

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

- ID: UI-07
- Subsystem: UI/PDA and implementation verification
- ADR revision: v0.1.85
- Record status: complete-within-scope for the identified contract error and guidance
- Source status: source-confirmed for the pinned factories/bindings; scoped-source-audit for XML initialization
- Runtime status: observed (user-supplied failure); corrected game path untested
- Baseline IDs and provenance record: UPSTREAM-UI07, commit `c57fe5b9fab4fe0506659db03137c52d2500eb2f` (public 2026.10.11 tag); RT-UI07 private observation, unknown binary/profile equivalence
- Last reviewed: 2026-10-13

## Question and scope

Why did entering CtZ Experimental 0.1.9's Command tab fail with `attempt to call method 'SetCheck' (a nil value)` despite passing Lua fixture checks? Trace the exact factory result, export owner and selected-state implementation. This is not an exhaustive widget/API audit or a native-runtime certification of the proposed correction.

## Evidence and method

Read the supplied screenshot and fatal trace privately, inspect the changed caller and its fixture, and compare four public source files at the immutable commit above. [Source ledger](../../evidence/runtime/button-checkbox-contract-2026-10-13.csv) pins full-file hashes, symbols and ranges. Raw logs, installation paths, session metadata and private-package fingerprints are withheld under the [public-content policy](../../00-environment/public-content-policy.md). RT-UI07 is not independently reproducible from the public repository alone.

## Findings

1. `CScriptXmlInit::Init3tButton` allocates and returns `CUI3tButton*`; `InitCheck` allocates and returns `CUICheckButton*`. The parent's ownership does not change that class contract. S02, `ScriptXMLInit.cpp:228–234,268–274`.
2. `CUIButton::script_register` binds `CUI3tButton` as a subclass of `CUIButton`, and `CUICheckButton` as a subclass of `CUI3tButton`. `GetCheck`/`SetCheck` are exported on the checkbox subclass, not either button class. A base-class object does not acquire a subclass-only export. `CUITrackBar` separately exports methods with those names; matching names do not make them common CUIWindow methods. S01, `UIButton_script.cpp:17–30,44–48`.
3. The inspected `CUIXmlInit::Init3tButton` initializes an existing button, text, textures, sounds, accelerators and hints. No `check_mode` read occurs in the scoped function. XML attributes cannot substitute for selecting the correct constructor/export contract. This is bounded to S03, `UIXmlInit.cpp:362–428`, not a claim about every XML handler or future engine.
4. The inherited `CUIStatic::TextControl` returns the text control whose `CUILines` interface exports `SetText` and `SetTextColor`. Those provide a source-supported way to reflect Lua-owned selection without checkbox calls. S04, `UIStatic_script.cpp:13–29`; inheritance at S01.
5. RT-UI07: clicking Command after successful game startup reached `WarPDA:refresh_overall` and failed at its direct officer-button `SetCheck` call. That narrows this failure to method lookup, rather than early native PDA creation. No inference of overall build stability follows.
6. The initial fixture shared one method-rich window table across all constructors, including `SetCheck`. It therefore accepted an invalid button call. Passing that fixture established execution against the fake interface, not actual binding availability. This is an implementation-test defect; the existing ADR export catalog already assigns `SetCheck` to the correct classes and needs no invented new binding.

## Practical correction and test contract

Keep officer/tab selection in Lua. Remove button `SetCheck` calls and unused `check_mode` attributes; render the selected officer through supported text color plus the existing expanded/collapsed label marker. Use `InitCheck` only when an actual checkbox is intended, with its native XML/control semantics. Do not replace a required native operation with a silent protected no-op and call that verification.

For fixtures, define class-specific capability surfaces from a separately checked binding/factory contract. Include a negative capability assertion: an `Init3tButton` result has no `SetCheck`, while an `InitCheck` result has it. Execute tab entry, repeated officer open/close, target-submenu close, officer switching, periodic refresh and tab switching with that restriction. This is a scoped regression guard, not a complete engine emulator; unsupported methods must not be added merely to make a test pass.

## Competing explanations and missing edges

The factory/binding mismatch and observed error agree. An installed wrapper could change a return contract in another setup, but none is required to explain this report. Binary equivalence to the public source is unknown. Native drawing, input behavior, text-state refresh and reload lifetime remain game-test questions. The correction's local Lua 5.4 fixtures do not reproduce LuaJIT/X-Ray termination or prove native success.

## Checks and outcomes

Public source files were fetched at the immutable commit and full-file hashes/ranges/symbols checked. The corrected local CtZ implementation passes 48 behavior assertions, including the new negative-capability guard, and all 22 scripts syntax-compile in Lua 5.4; XML parsing/layout checks pass. These are external implementation checks, not the ADR test suite or a successful game retest. Repository/privacy/test checks for this documentation increment are recorded in [verification](../verification-2026-10-13-v0.1.85.md).

## Disposition and next work

The contract error and permissive-fixture lesson close within this scope. CtZ Experimental 0.1.10 is a local retest candidate; its gameplay source is not committed or published with ADR. Retest Command entry and repeated submenu toggles in the actual game before promoting the correction to observed success. See the [widget inventory](../../03-ui-pda/ui-widget-event-inventory-oct11.md) and [test guidance](../../05-mod-architecture/test-guidance.md).
