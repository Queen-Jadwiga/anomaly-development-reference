# Faction and relation development reference

> ADR document set: **v0.1.71**. Research revisions and source/build versions below describe their original scope.

- ID: FAC-06
- Source status: consolidated source-confirmed findings within FAC-01–05 scope
- Runtime status: untested; deferred until explicitly resumed by the user
- Last reviewed: 2026-10-11

This guide joins the completed native and supplied-package investigations for CtZ development. It does not specify installed GAMMA relations, tuning values or tested gameplay recipes. Available-source consolidation and bounded consistency audit are complete; full effective integration remains partial. [Completion status](source-completion-status.md).

## Source and citation scope

| Baseline | Pin and scope | Ledger-local labels |
| --- | --- | --- |
| ENGINE1011 | Uploaded archive SHA-256 `14d82b26f0e2579898e912c87224ee87a4c9daafc0c5950d5a322406d15e6aee`; upstream commit/executable match unknown | [F: identity/queries](../../evidence/factions/native-relations-2026-10-11.csv), [P: persistence](../../evidence/factions/relation-persistence-2026-10-11.csv), [M: mutation](../../evidence/factions/community-mutation-2026-10-11.csv), [A: actions](../../evidence/factions/action-goodwill-2026-10-11.csv) |
| BETA150 main | Supplied archive SHA-256 `9f71999bb44cb6d3e41c431feaf5be4714159522df1fa8d71599ac039946315d`; main scripts only, installation unknown | [R: Warfare consumers](../../evidence/factions/warfare-consumers-2026-10-11.csv) |

Labels below always refer to those respective ledgers. Each pins paths, symbols, ranges and whole-file hashes. No optional patch, historical package or installed configuration is silently substituted. Detailed source-order findings stay in the linked references and dated records.

## First identify the state you need

| Development question | Relevant representation/interface | What it establishes | Detailed reference / evidence |
| --- | --- | --- | --- |
| Which faction does this live character identify as? | `character_community()`; configured ID/index | Client character-info community, not strategic ownership | [Identity](native-relations.md); F01–F04/F10/F11 |
| Which faction does the server character identify as? | Guarded trader `community()` | Server trader field; distinct from live tuple or script true-community | [Mutation](community-mutation.md); M02/M11/M12 |
| How does faction A regard faction B? | `relation_registry.community_relation(A,B)` | Directed matrix cell | [Query contracts](../../02-lua-api/factions/relations-api.md); F01/F09 |
| How does faction A regard this character? | Community goodwill getter | Community → character contribution, stored with target character | [Queries](native-relations.md); F06/F09/F10 |
| How does this character regard another? | Personal `goodwill`, full `general_goodwill`, or virtual `relation` | Different contribution/aggregation/category contracts | [Queries](native-relations.md); F05/F06/F09–F16 |
| What relation should a Warfare display label show? | Selected matrix or loaded-member average | Display-specific approximation and direction, not universal AI hostility | [Consumers](warfare-relation-consumers.md); R11/R12/R18 |
| Who owns the terrain or CtZ campaign point? | Smart `owning_faction` / separate CtZ model | Strategic state requiring its own policy | [WAR-002b](../../08-research/investigations/2026-10-11-WAR-002b-policy-offline-combat.md); R15 |

Numeric community indexes follow native configuration order. A script faction list, team number, `player_id`, native A-Life group ID and smart ID are not interchangeable identities. Use configured strings and documented mapping producers where their contract requires them; do not invent portable numeric faction IDs. F01–F04; M04/M18; R01/R07–R09/R19.

## Choose the query before interpreting its result

Native full character attitude adds personal goodwill, reputation relation, rank relation, community-to-character goodwill and community-to-community relation. The object method `general_goodwill` uses that five-term path; the ID-based module `get_general_goodwill_between` uses only personal plus the two community terms. Substituting one for the other can omit contributions. F05/F09/F10; [focused APIs](../../02-lua-api/factions/relations-api.md).

Native character classification uses configured threshold keys; the selected live `relation` call goes through virtual native-type behavior, including monster-table fallback. BETA150 faction predicates instead classify directed matrix cells using script ±1000 boundaries. Its squad tooltip can average loaded members' full attitude and use a different fallback when none are available. Do not infer symmetry or agreement across these labels. F05/F13–F17; R01/R02/R11/R12/R18.

A zero or neutral-looking result is not a general success indicator: some paths have neutral missing-entry defaults, other wrappers log and return zero/null/dummy on unsupported receiver types, and deeper paths assert. Valid configured identities/current object representations remain preconditions. F03/F06/F09/F10/F13; API contracts above.

## Match a mutation to its actual layer

| Intended layer | Selected mutation | Limits that matter |
| --- | --- | --- |
| Personal goodwill | Set/change personal contribution | Clamped configured goodwill; enum relation preset does not compensate other attitude terms |
| Community → character | Set/change community goodwill | Different target-owned map and configured clamp |
| Faction matrix | Directed native setter, or supplied dynamic helper | Native setter writes one cell; supplied save helper supplies symmetry/storage intent |
| Character community | Live `set_character_community(comm,squad,group)` | Client/server bridge plus potentially two live hierarchy migrations; partial returns, no atomic success contract |
| Live team/squad/group | `change_team` | Local hierarchy/AI membership, not character community or strategic squad reassignment |
| Rank/reputation | Absolute/delta numerical setters | Separate client/server value writes; different limits from goodwill |

F05/F06; M01–M11; A07–A10; R02–R04. [Mutation APIs](../../02-lua-api/factions/community-mutation-api.md) and [value APIs](../../02-lua-api/factions/action-values-api.md) specify receiver/signature requirements.

`force_set_goodwill` compensates only the two community contributions and writes personal state directly; it omits rank/reputation compensation and is not a permanent diplomacy lock. The community setter can migrate with old squad/group before the wrapper requests supplied values. Its direct server community write is separate from later server creature tuple update receipt. These are phase boundaries, not reproduced defects or recommended workarounds. F06; M01/M02/M04/M06/M11/M17/M19.

No selected setter establishes completed strategic reassignment, CtZ owner synchronization, UI refresh, all AI target reevaluation or a universal faction-change callback. Effective scripts can add those operations and must be traced separately. [Native mutation](community-mutation.md), [consumer boundary](warfare-relation-consumers.md).

## Keep persistence and cleanup domains distinct

Personal/community-to-character records are saved by native A-Life auxiliary registry serialization. The static community matrix and sympathy caches reset in the selected level-before-load hook and reload configuration lazily. BETA150's dynamic diplomacy deliberately saves actor variables and reapplies matrix values in a marshal-gated script load path. That script intent does not establish installed wrapper durability or ordering relative to native reset. P01–P08/P13–P18; R03/R06; [persistence reference](relation-persistence.md).

The selected final native registration loop follows relation-record restoration; before-register and guarded native storage load hooks are earlier. Neither that loop nor a named Lua load callback alone certifies all effective diplomacy/CtZ state is restored. P08/P10; [A-Life callback phases](../alife/callback-phase-reference.md).

Native monster unregister clears its own relation maps, retaining the outer record and leaving other characters' incoming personal references untouched by that function. Numeric ID reuse therefore needs campaign/lifetime context and effective cleanup review. This conditional implication is not an observed contamination bug. Client teardown or creature death is not automatically server unregister. P02/P09/P10/P17; [A-Life lifecycle](../alife/lifecycle-state-reference.md).

## Treat awards and notifications as separate contracts

Native online Hit/Die action attempts, dynamic faction diplomacy adapters, offline battle outcome and actor support rewards have different eligibility and gates. Native goodwill, reputation and rank can change independently; script rank bookkeeping is not the same formula as native victim-band kill points. No universal one-award-per-death or online/offline equivalence has been established. A01–A07; R04/R05/R13/R17/R20.

The native object death callback follows the selected action attempt and inherited death; a relation-flag attempt can precede attack throttling. The kill action has a zero mask, and flags are not counted history or reliable award receipts. Actor RPC-named hooks inspected here update Discord display through script producers. Their names do not establish strategic/UI completion. A01/A03/A09/A13–A15/A18/A20; M13.

For a later CtZ event feature, define which source event is being recorded, the identity/lifetime it refers to, its observation phase and deduplication authority before attaching callbacks. This is a design implication of the investigated boundaries, not a tested implementation recipe.

## Working sequence for later changes

1. State the required value or mutation layer using the tables above; record direction and native versus script identity.
2. Select the exact source variant and interface; establish valid receiver, object lifetime, configured identity and required dispatch phase.
3. Trace effective consumers and persistence/reconciliation for every additional layer, including ownership and rewards.
4. Keep a source claim separate from installed behavior. Resume runtime checks only when the user authorizes them, using identified executable/profile and repeatable observations.

FAC-06 completes the available-source consolidation and bounded audit. The [completion status](source-completion-status.md) gives the remaining evidence and stopping rule. Further unrelated AI/API expansion is optional; installed integration remains the required unresolved layer.
