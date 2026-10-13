# Compatibility, dependencies and package contracts

> ADR document set: **v0.1.84**. Research revisions and source/build versions below describe their original scope.

- ID: ARCH-02-COMPATIBILITY
- Subsystem: practical mod architecture
- Research revision: v0.1.79
- Record status: complete-within-scope for selected synthesis; installed compatibility partial
- Source status: pinned documentation synthesis with proposed mod-owned contracts
- Runtime status: untested; deferred
- Baseline: ADR v0.1.78 `b187f8707ae4276c442284a25359baa8b3cf538f`; original source/build/external confidence retained
- Last reviewed: 2026-10-12

Compatibility is a claim about a specified combination of interfaces, files, build and state. Start with [module/state ownership](module-state-contracts.md). Evidence IDs belong to the [26-row ARCH-02 ledger](../evidence/architecture/module-state-contracts-2026-10-12.csv); proposed support records and package rules below are **design guidance**, not a compatibility result for GAMMA, Warfare or CtZ.

## Record each dependency edge

| Dependency kind | What to pin/trace | What is insufficient |
| --- | --- | --- |
| Native/Lua export | Implementation, registered arity/converters, build conditions, executable identity when known | Feature name, source date or another build's catalog |
| Script service/class | Winning file hash, public member/version, construction and later replacements | Namespace existence or a file in one addon archive |
| Shared event | Effective Register/Send/Unregister, event producer, listener identity/order and arguments | Same event spelling across distinct dispatchers |
| Configuration | Effective roots/includes/mod files, parse rules, writer/helper chain and consumer refresh | DLTX final filename metadata or a menu's displayed value alone |
| Storage | Actual manager/root, serializer/encoder, emit timing, schema and reset behavior | Codec availability, attaching a table or naming a callback save |
| UI/resource | Winning script/XML/registry, assets/font/config dependencies and ownership route | Pointer presence, generic hide/delete or another page's workaround |
| Patch/unlocalizer | Directive and target line form, installer caller/phase, capture and later replacements | Filename order or definition of an uncalled installer |

M02/M04/M07/S01–S07/S10–S12/U01–U02/C01–C04. Mark each dependency required or optional **for the proposed feature**, with an explicit unavailable/unsupported outcome. Missing optional capability should disable the dependent behavior rather than silently select an unrelated owner; that is a recommended policy, not a source-provided fallback. Presence checks cannot certify signatures or readiness. Missing effective source keeps the relevant edge unresolved.

## Collect effective files before claiming integration

The existing [WAR-002a collection record](../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md#missing-pieces-required-for-effective-profile-closure) requests a copy from the active MO2 virtual view, including scripts, relevant configs and supplying-mod/conflict information. Packed base inputs may need separately identified extraction. This can be source collection without running the game. A physical gamedata folder or enabled-mod list does not establish all winning bytes. C03.

Record the effective file hash and origin for overwritten paths, then trace **differently named** modules that evaluate or install later replacements. Distinguish filesystem winner, DLTX composition, module evaluation, startup handler, DXML installer and final function slot. An ordinal filename can participate in one enumeration without controlling dependency autoload or later patching. For callbacks, distinguish the conditional five-event debug-global route from axr_main; resolve the effective aliases as a chain. M04/M07, [startup contracts](../04-game-systems/configuration/script-loading-startup-callbacks.md).

CONFIG-04's equal optional menu method slice is narrower than full-file equality; equal files in two uploaded packages are narrower than installed execution. Missing preset includes in a partial package do not establish their absence from the profile. Keep alternative package inputs separate until a real winning chain is demonstrated. C04/S05, [qualified comparisons](../04-game-systems/configuration/supplied-options-patches.md#package-comparisons-and-effective-inputs).

## Keep version and identity axes separate

| Axis | What it identifies | Proposed support decision |
| --- | --- | --- |
| ADR revision | Documentation increment | Cite research; do not use it as a game compatibility version |
| Engine source archive/commit | Inspected implementation | Pin source; state unknown binary equivalence/build guards |
| Executable/build | Runtime candidate or observed binary | Record actual identity when available; source findings stay source-qualified meanwhile |
| Addon package/interface | Distributed bytes and public contract | Declare exact supported interface/features; leave unreviewed variants unknown |
| Native save format | Selected engine's outer version/predicate | Do not treat the native validity predicate as addon schema certification |
| Mod schema | Owned encoded record shape/meaning | Explicit accepted versions, validation, migrations and unsupported-version policy |
| Campaign/object identity | Which campaign/generation a record describes | Pair/reset owned state and validate rebinding beyond numeric lookup |

C01–C02/S09–S12. October research labels are not minimum supported engine versions. The source baseline and REV-01 distinguish September/October dispatchers and earlier dynamic-tab availability. No new minimum engine release is derived here. The source LuaJIT header also does not identify every binary or make another Lua version's table iteration order portable. Use [environment qualification](../00-environment/source-baseline-2026-10-11.md).

Selected CtZ load repairs/stamps version fields without saved-version dispatch or an independent campaign/generation comparison. That is a bounded source finding, not a demonstrated defect in every campaign. A proposed mod schema policy should explicitly classify accepted current records, known older records requiring migration, malformed records and unsupported/newer records. Preserve the original record or refuse the operation according to a documented recovery policy; avoid overwriting unknown state merely to relabel it current. Migration completion must include shape validation and a defined result. This recommendation does not imply CtZ already implements it. S09/S12, [campaign safety](../04-game-systems/persistence/ctz-campaign-safety.md).

Decode/validate before phase-specific identity rebinding; reconcile world effects only when their prerequisites are established. Define what a repeated load/migration does and what happens after partial failure. Do not assume migration, configuration output, native save and companion storage commit together. A mod-owned campaign key/generation may help, but its producer, persistence and pairing/reset protocol must exist; the key's name is not identity evidence. S10–S12.

## Publish a bounded package contract

These are recommended deliverable fields for a mod package, rather than a new prescribed addon layout or MO2 implementation:

| Field | Concrete record |
| --- | --- |
| Files and names | Relative installation paths, project namespace, owned config/save keys and intentional overwritten paths |
| Dependencies | Required/optional interface versions, source-qualified features and resource origins |
| Integration | Evaluation/startup/installation route, intended wrapped slots/listeners, repeat behavior and known competing patches |
| Configuration | Defaults/types, missing/empty policy, validation and restart/refresh requirements |
| State | Schema support, actual serializer, campaign pairing, reset and upgrade/disable limits |
| Support scope | Source/build/package pins, effective-profile coverage, runtime status and known unknowns |
| Recovery | Partial installation/application/migration outcome, retained state and allowed retry/restoration |

Where an addon uses gamedata, record exact paths under `gamedata/scripts`, `gamedata/configs` and any owned UI/resources. Do not infer that every package needs every directory or distribute borrowed engine/addon files simply to make it self-contained. Declare and minimize intentional shared-file edits; separately named patch modules still require capture/order evidence. This ADR increment distributes documentation only, with no third-party source/assets. C03–C04/S06–S07/U01.

For upgrade, inventory removed/renamed files as well as added ones: stale differently named installers can remain active in a merged installation. State whether the supported route requires a clean package replacement, restart, migration or new campaign; do not certify one without the relevant source/runtime evidence. Module reload and cache clearing are not a generic upgrade protocol. For disable/uninstall, declare whether saved namespaces and gameplay effects remain, and how subsequent loads behave without the code. Removing files is not proof of reversing prior native mutations. M03/S01/S10–S13.

## Review support claims by evidence level

| Claim | Minimum evidence for that claim | Current ARCH-02 result |
| --- | --- | --- |
| Selected implementation contract | Original pinned source/export/caller record | Reused with its existing source/build limits |
| Proposed module/package design | Named owner, dependencies, lifetime and failure policy | Documented as design guidance; implementation absent |
| Effective source integration | Winning files/configs plus emitter, installation and later replacement chain | Partial; missing edges retained |
| Runtime compatibility | Identified executable/profile, reproduction and recorded outcomes | Untested; deferred |
| Safe upgrade/uninstall/retry | Actual schema/lifecycle/side-effect path plus appropriately scoped verification | No general recipe certified |

Complete-within-scope means ARCH-02's selected synthesis is done. It does not close every effective dependency or promote external UI/clock observations to independent ADR verification. Logging/assertion/stack/error routes remain DEBUG-01; qualified examples and test guidance remain ARCH-03. No CtZ gameplay changes or universal load-order/save-repair guidance. [Investigation](../08-research/investigations/2026-10-12-ARCH-02-module-state-compatibility.md), [verification](../08-research/verification-2026-10-12-v0.1.79.md), [roadmap](../ROADMAP.md).

Current practical completion: ARCH-03 [central guide](development-reference.md), [patterns](../07-code-library/qualified-patterns.md), [test guidance](test-guidance.md) and [bounded audit](../08-research/verification-2026-10-12-v0.1.81.md) complete the selected foundation. The ARCH-02 research allocation above remains dated; effective installed compatibility and runtime are not certified. Next separate whole-ADR audit.
