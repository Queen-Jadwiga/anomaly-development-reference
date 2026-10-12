# Warfare development reference

> ADR document set: **v0.1.81**. Research revisions and source/build versions below describe their original scope.

- ID: STRUCT-01-WARFARE
- Subsystem: Warfare
- Reference revision: v0.1.67 navigation synthesis
- Source status: synthesis of linked selected supplied-package and native boundary findings
- Runtime status: untested; deferred
- Baseline/provenance: qualified ENGINE1011/BETA150/ZIP142 and comparison inputs; [manifest](../../evidence/manifest.md)
- Last reviewed: 2026-10-12

Start here for the strategic script layer. Warfare policy consumes A-Life facilities but is not the native simulation itself. This central guide links the existing package, policy and integration references; it does not move or duplicate their source claims. Available-source selected work is complete within scope; [effective-source status](source-completion-status.md) remains partial.

## Separate strategic policy from native behavior

Target selection, assigned smart, arrival, capture ownership, offline casualty bookkeeping and CtZ campaign state are distinct. A native squad or graph location alone is not proof of strategic ownership. Inspect the selected consumer and package variant before treating a declared option or callback name as actual installed behavior.

| Question | Canonical reference or investigation | Boundary |
| --- | --- | --- |
| Which supplied script variant was inspected? | [WAR-002a provenance/effective requirements](../../08-research/investigations/2026-10-11-WAR-002a-source-packages-effective-profile.md) | Supplied bytes/public comparison do not identify MO2 winners |
| Targeting, arrival, ownership and offline combat | [WAR-002b](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md) | Effective board/smart/helper chains still missing |
| Options, caches, clocks and forced-status producers | [Policy controls](policy-controls.md) | Declared/default values and module snapshots are not installed values |
| Native permissions, scheduling and representation | [A-Life central guide](../alife/development-reference.md) | Native switching differs from strategic routing |
| Faction/diplomacy consumers | [FAC-05 supplied consumers](../factions/warfare-relation-consumers.md) | Effective faction helpers/startup remain open |
| CtZ source integration boundary | [WAR-001](../../08-research/investigations/2026-10-11-WAR-001-ctz-integration-boundary.md) | Project-specific earlier snapshot, not a new mod build |

[Script declarations/interfaces](../../02-lua-api/alife/script-interfaces.md), [evidence](../../evidence/warfare/README.md), [WAR-003 controls investigation](../../08-research/investigations/2026-10-11-WAR-003-configuration-policy-controls.md), [available-source bounded audit](../../08-research/verification-2026-10-11-v0.1.43.md).

For a strategic mod, reconcile persistent member/owner identity across script and native representations rather than using one assignment or callback as a completion receipt. Offline combat abstractions do not establish traversal through live weapon/armor/death behavior; [gameplay state](../gameplay/development-reference.md) and [persistence](../persistence/development-reference.md) keep those contracts separate. This is navigation/synthesis of existing findings, not additional verified integration.
