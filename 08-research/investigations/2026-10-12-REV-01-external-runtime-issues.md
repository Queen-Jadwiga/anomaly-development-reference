# REV-01 — External runtime issue review and catalog correction

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

- ID: REV-01
- Subsystem: UI/PDA, native API catalog, callbacks and persistence
- ADR revision: v0.1.60
- Record status: complete-within-scope (review and documentation); UI runtime investigations remain open
- Source status: source-confirmed / scoped-source-audit for specified corrections/comparisons
- Runtime status: observed (external reports); independent ADR reproduction untested
- Baseline IDs: ENGINE1011 uploaded archive; UPSTREAM0912 immutable source; ENV-RT01 reported executable/profile
- Last reviewed: 2026-10-12

## Question and scope

Which claims in GitHub issues #1–#4 can correct the reference now, which are externally observed support for earlier traces, and which require unresolved runtime investigation? Fix the scoped `.property` catalog omission, clarify feature/build boundaries, add actionable qualified lifecycle guidance and preserve provenance. No CtZ implementation, engine code, or independent game tests are included.

## Evidence and method

Read all four issues and their reported setups; no comments/attachments were present at intake. Compare the current catalog/tool and uploaded native source. Independently inspect the September upstream registry/dispatcher/native bindings and official feature history. [Environment/provenance](../../00-environment/reported-gamma-runtime-2026-10-12.md), [six-entry source ledger](../../evidence/runtime/issue-review-source-2026-10-12.csv), and [ten reported observations](../../evidence/runtime/reported-observations-2026-10-12.csv). The observations carry issue-body hashes and review timestamps; they paraphrase the report and do not pretend raw logs were supplied.

## Findings and confidence

| Issue | Source-confirmed correction/comparison | External runtime finding | Disposition |
| --- | --- | --- | --- |
| [#1](https://github.com/Queen-Jadwiga/anomaly-development-reference/issues/1) | Earlier C-03/C-04 already distinguish ownership from alias safety; no automatic alias revocation was established | Dialog/HUD registrations surviving quickload crashed; matched cleanup reportedly produced three clean reloads | Keep open: practical guidance added, exact teardown mechanism and wider applicability unresolved |
| [#2](https://github.com/Queen-Jadwiga/anomaly-development-reference/issues/2) | Dynamic tabs shipped July 31; September source exposes registry dependencies; apply immediately rebuilds a live strip | Startup/load registration crashed with MAC’s full strip; later keypress registration worked | Keep open: version wording corrected, loading/full-strip interaction still unresolved |
| [#3](https://github.com/Queen-Jadwiga/anomaly-development-reference/issues/3) | Extractor omitted `.property`; source registers condition getter/setter at S01 | No runtime proof needed for this source-catalog defect | Resolved by corrected extractor, regression checks and regenerated catalog |
| [#4](https://github.com/Queen-Jadwiga/anomaly-development-reference/issues/4) | Source declares LuaJIT 2.0.4; September registration-index dispatcher differs from October tiered model; earlier save/XML traces remain scoped | Probe order, MO shadowing, early load clock, save framing and installed wrapper observations support or qualify those traces | Resolved as documentation/evidence intake; not a certification of all engine/profile behavior |

### UI lifetime and registration safety

R01/R02 support the practical requirement to remove native display registrations before Lua teardown, using the operation matching how the window was registered. `HideDialog` corresponds to a shown dialog; `RemoveDialogToRender` corresponds to the HUD render registration. Merely clearing a Lua singleton or relying on finalization does not establish removal of native aliases. This is not a blanket instruction to delete XML-owned children, change AutoDelete, or call HideDialog on every PDA-attached page. The precise stale-pointer mechanism is **inferred**, not proven from unsymbolized offsets.

R03/R04 disprove the registry comment’s unrestricted timing claim in the reported configuration. S03 shows why `level.present()` and a non-null PDA pointer are weaker than completed load/readiness. Do not substitute an arbitrary fixed delay as a proved gate. Test a deliberately selected post-load phase with the actual PDA/addon stack. The full eight-tab strip is not demonstrated to be inherently unsupported: later registration succeeded in that setup. Keep loading-only, strip-only and combined-interaction explanations open.

### Feature history and build scope

Upstream [commit f137afe292e879128adcbf39c42563cc60846156](https://github.com/themrdemonized/xray-monolith/commit/f137afe292e879128adcbf39c42563cc60846156), dated 2026-07-19, introduces dynamic PDA support; the [2026.7.31 release](https://github.com/themrdemonized/xray-monolith/releases/tag/2026.7.31) lists it. The [August PDA improvements PR](https://github.com/themrdemonized/xray-monolith/pull/633), merged 2026-08-16 and shipped in [2026.8.16](https://github.com/themrdemonized/xray-monolith/releases/tag/2026.8.16), adds/improves reskin/icon support; S05 independently confirms SetTabIcon in September. October labels identify the inspected snapshot, not the feature’s introduction or universal minimum version.

September S04 assigns increasing registration indices and dispatches by them. The inspected October implementation has PRE/NORMAL/POST and dependency ordering. Neither can be silently generalized to every earlier/later effective script. The reporter’s two-argument global RegisterScriptCallback wrapper is an installed observation; S04 separately verifies the two-argument callback_set implementation, not an unavailable global wrapper file.

### Catalog correction

Add `.property` recognition and accept property registration lines in the source-origin checker. Preserve getter/setter expressions and classify accessor bindings as `property`; do not infer method-call arity or general setter policy from the row alone. S01 condition reads m_fCondition; its setter logs/rejects ordinary values outside zero to one and otherwise writes the field. The source comparisons do not establish a finite-number/NaN rejection contract.

Regeneration adds exactly one row: cse_alife_inventory_item.condition, both evaluated XRGAME_EXPORTS branches, with get_condition_script/set_condition_script, line 51. All 1,150 previous rows and the other class/helper/script inventories and input ledger remain byte/content-preserved. New total: **1,151 binding rows**, 84 class rows, 174 helpers, 1,372 script declarations and 73 input files. A missing inventory row is never proof that an API is absent outside the declared extraction scope.

### Corroborating observations

R05/R06 separate per-file DXML interception, duplicate-ID replacement across distinct filenames, and MO’s same-filename winner. Font-startup timing is observed in the reporter’s setup, not every initialization path. R08 supports early load-hook timing before saved native time is restored; it does not identify the winning storage dispatcher or completion callback for every install. R09 supports the outer header constants, not whole-save integrity or binary compatibility. R07 matches the source LuaJIT version and warns against treating table iteration in another Lua implementation/version as a portable order contract. Independent source checks and external observations remain separate axes.

## Competing explanations and missing edges

Open #1: obtain the probe/log, executable hash and symbols or exact native stack; compare dialog-holder versus HUD-render-list versus PDA attachment teardown. Open #2: isolate loading with/without MAC/full strip, compare post-load gates and effective XML/native code; capture crash logs and exact profile. General missing data: winning scripts/wrappers, complete profile and raw artifacts. No test here establishes the user’s installed build.

## Checks and outcomes

Catalog extractor/output/source-origin checks, isolated reproducibility, focused regression tests, source ranges/hashes and repository navigation are recorded in [verification](../verification-2026-10-12-v0.1.60.md). No game ran for this increment. Externally reported observations are retained now; independent runtime work remains deferred.

## Disposition and next work

Close #3 and #4 after publication for the completed catalog/documentation scope. Leave #1 and #2 open despite improved guidance. Continue ECO-02 source work independently; treat the UI hazards as priority runtime/CtZ review items before claiming startup or quickload safety. This revision changes ADR only and neither replies to the reporter nor closes unresolved crash investigations.
