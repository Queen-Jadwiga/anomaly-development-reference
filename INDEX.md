# ADR index

- [Environment: engine version](00-environment/engine-version.md)
- [Environment: source repositories](00-environment/source-repositories.md)
- [Engine architecture](01-engine/architecture.md)
- [Engine source map](01-engine/source-map.md)
- [Lua API index](02-lua-api/api-index.md)
- [PDA architecture](03-ui-pda/pda-architecture.md)
- [UI widgets](03-ui-pda/widgets.md)
- [UI fonts](03-ui-pda/fonts.md)
- [Warfare](04-game-systems/warfare/README.md)
- [Evidence manifest](evidence/manifest.md)
- [INV-001: source baseline](08-research/investigations/2026-10-09-source-baseline.md)
- [INV-002: font crash](08-research/investigations/2026-10-09-ui-fonts.md)
- [Roadmap](ROADMAP.md)

- [May 15 official source baseline](00-environment/source-baseline-2026-05-15.md)
- [CUIProgressBar research candidate](02-lua-api/classes/CUIProgressBar.md)
- [Source tag investigation](08-research/investigations/2026-10-09-tag-reconstruction.md)

## Source-extracted API subset (v0.1.3)
- [UI Lua API index](02-lua-api/api-index.md)
- [Font getter exports](03-ui-pda/fonts.md)
- [UI binding research log](08-research/investigations/2026-10-09-lua-ui-binding-extraction.md)

- [v0.1.4 UI signature audit](02-lua-api/signature-audit-v0.1.4.md)

- [v0.1.5 UI/text signature audit](02-lua-api/signature-audit-v0.1.5.md)

## v0.1.6 — XML initialization
- [Font aliases and failure paths](03-ui-pda/fonts.md)
- [Native XML initializer and scrollview attributes](03-ui-pda/xml-layouts.md)
- [INV-006 XML/font initialization](08-research/investigations/2026-10-09-xml-font-init.md)

## ADR v0.1.7 investigations
- [Lua-facing XML initialization boundary](02-lua-api/xml-initialization-exposure.md)
- [Font manager / Lua getters](03-ui-pda/font-manager-and-lua-getters.md)
- [INV-007 XML-Lua bridge](08-research/investigations/2026-10-09-xml-lua-bridge.md)

## ADR v0.1.8 — XML registration and font lifecycle
- [XML initializer Lua registration search](02-lua-api/xml-registration-search-v0.1.8.md)
- [Font initialization: confirmed path and open lifecycle](03-ui-pda/font-initialization-lifecycle-v0.1.8.md)
- [INV-008 research log](08-research/investigations/2026-10-09-xml-lua-search-and-font-lifecycle.md)

## v0.1.9 source audit
- [Historical source audit](01-engine/source-tree-audit-v0.1.9.md)
- [UI initialization call flow](01-engine/ui-initialization-callflow.md)
- [Lua XML registration search](02-lua-api/xml-registration-audit-v0.1.9.md)
- [Font lifecycle audit](03-ui-pda/font-lifecycle-audit-v0.1.9.md)
- [Reproducible checkout commands](tools/source-audit-commands.md)
- [INV-009 audit log](08-research/investigations/2026-10-09-source-tree-audit-v0.1.9.md)

## ADR v0.1.10 Part A — Lua registration
- [Luabind and XML bridge audit](02-lua-api/registration-architecture-part-A.md)
- [CScriptXmlInit class](02-lua-api/classes/CScriptXmlInit.md)
- [XML creation call flow](01-engine/lua-xml-bridge-callflow.md)
- [INV-010: findings and unresolved searches](08-research/investigations/2026-10-09-part-A-registration-audit.md)

## ADR v0.1.10 — Part B

- [Native CGameFont lifecycle](01-engine/native-font-object-lifecycle.md)
- [Part B font manager investigation](08-research/investigations/2026-10-09-part-B-native-font-manager.md)


- [Part C — UI construction/ownership](03-ui-pda/ui-construction-ownership.md)
- [INV-012 source audit](08-research/investigations/2026-10-09-part-C-ui-construction.md)

## v0.1.10 Part D
- [Integrated Lua/XML/native UI architecture](01-engine/ui-lua-native-integration.md)
- [Post-A–D open-question review](08-research/open-questions-v0.1.10.md)
- [Part D investigation and audit limitations](08-research/investigations/2026-10-09-part-D-integration.md)

- [A-01/A-02 bootstrap follow-up — INV-014](08-research/investigations/2026-10-09-A01-A02-registration-bootstrap.md)
- [Read-only source audit tool](tools/audit_xml_lua_registrations.py)


## ADR v0.1.12 — October 11 source-baseline adoption
- [October 11 source and candidate runtime baseline](00-environment/source-baseline-2026-10-11.md)
- [A-01 exact source registration chain, source-research closure](08-research/investigations/2026-10-11-A01-source-registration-closure.md)
- [Current open-question amendments](08-research/open-questions-v0.1.10.md#2026-10-11-superseding-status-amendment-adr-v0112)

**Next investigation:** A-02, separate `CUIXmlInit` Lua exposure. Previous May 15 findings remain historical until reconciled individually against the October 11 source.

## ADR v0.1.13 — A-02 source audit
- [A-02 native CUIXmlInit vs Lua-facing CScriptXmlInit](08-research/investigations/2026-10-11-A02-native-xml-lua-exposure.md)

## v0.1.14 — B-01 font ownership
- [Verified font manager and named-font ownership](08-research/investigations/2026-10-11-B01-font-manager-ownership.md)

- [B-02: UI font manager lifecycle (October 11 source)](08-research/investigations/2026-10-11-B02-font-manager-lifecycle.md) — source complete; runtime deferred.

- [C-01 — Native UI creation, attachment and ownership](08-research/investigations/2026-10-11-C01-ui-ownership.md) — October 11 source verified; runtime deferred.

- [C-02 — Scroll-view pad and native child lifetime](08-research/investigations/2026-10-11-C02-scrollview-ownership.md) — source verified; Lua userdata lifetime and runtime testing remain separate.

- [C-03 — Luabind adoption versus native AutoDelete](08-research/investigations/2026-10-11-C03-luabind-adoption-autodelete.md) — source verified within scope; userdata alias and runtime behavior not generalized.

- [C-04 — XML factory return ownership](08-research/investigations/2026-10-11-C04-xml-factory-return-ownership.md) — parented versus parentless factory controls; Lua return-converter ownership and exceptions.

### October 11 UI subsystem survey
- [Dynamic PDA tabs](03-ui-pda/dynamic-pda-tabs-oct11.md)
- [DXML pipeline](03-ui-pda/dxml-pipeline-oct11.md)
- [Input and events](03-ui-pda/ui-input-events-oct11.md)
- [UI controls and typography](03-ui-pda/ui-controls-typography-survey-oct11.md)

- **UI-01 focused lifecycle (v0.1.21):** [PDA tab rebuild and subdialog routing](03-ui-pda/pda-subdialog-lifecycle-oct11.md) — source boundaries and open cases.

- UI-01a native tab state transitions: `08-research/investigations/2026-10-11-UI-01a-tab-state-transitions.md` (source-complete, runtime deferred).

## ADR v0.1.23 — XML/DXML native lifecycle
- [UI-04: XML loading, Lua interception, DXML caching and limitations](03-ui-pda/xml-dxml-native-lifecycle-oct11.md)

- [UI-04a: XML reader boundaries and filename selection](03-ui-pda/xml-loading-paths-ui04a-oct11.md) — Oct 11 source; UI-04b remains open.

- [UI-04b: XML callback errors and registration order](03-ui-pda/xml-dxml-callback-errors-ui04b-oct11.md) — October 11 source verified; external GAMMA runtime behavior pending.

## v0.1.26 UI widget/event export inventory
- [UI binding survey and pending event questions](03-ui-pda/ui-widget-event-inventory-oct11.md)
- [Machine-readable binding occurrences](02-lua-api/ui-binding-inventory-oct11.csv)

- [UI-06a–d source audit: bindings, events, build reachability, focus](03-ui-pda/ui06a-d-registrations-events-focus-oct11.md) — October 11 source; bounded conclusions and open subquestions.

## v0.1.28 — UI-06 source follow-ups
- [Registration, emitters, build inclusion, dialog input](03-ui-pda/ui06-supplementary-registration-emission-build-modal-oct11.md)
- [Scoped binding-occurrence CSV](02-lua-api/ui06-followup-scoped-def-occurrences.csv)
- [Direct message emitter CSV](02-lua-api/ui06-followup-message-emitters.csv)

## v0.1.29 — UI rendering and source-pass disposition
- [UI fonts, textures, aspect scaling — source reference](03-ui-pda/ui-rendering-scaling-fonts-textures-oct11.md)
- CtZ-relevant UI reference ready for development planning; runtime validation and optional exhaustive internals remain open. Next: A-Life/Warfare.

## v0.1.30 — Verification
- [October 11 source-reference verification report](08-research/verification-2026-10-11-v0.1.30.md) — bounded audit, corrected citations, remaining qualifications.

## v0.1.31 — A-Life/Warfare source foundation

- [ALIFE-01: server identity, squad membership, online/offline lifecycle](04-game-systems/alife/identity-lifecycle-oct11.md).
- [Source evidence locations and hashes](04-game-systems/alife/source-evidence-oct11.csv).
- [WAR-001: CtZ integration boundary and effective-profile prerequisites](04-game-systems/warfare/ctz-integration-boundary-oct11.md).

Runtime remains deferred. Next source work: creation/release and callback ordering; effective board/smart/Warfare implementations remain separately open.

## v0.1.32 — Native A-Life creation/release and callback phases

- [ALIFE-02: creation, registration, release and callback ordering](04-game-systems/alife/creation-registration-release-oct11.md).
- [ALIFE-02 source evidence ledger](04-game-systems/alife/creation-release-evidence-oct11.csv).

Scoped source pass complete; runtime deferred. Next: effective smart-terrain/board assignment and Warfare policy.

## v0.1.33 — Supplied Warfare packages and policy trace

- [WAR-002a: source-package comparison and effective-profile boundary](04-game-systems/warfare/source-packages-effective-profile-oct11.md).
- [WAR-002b: assignment, ownership, callbacks and offline combat](04-game-systems/warfare/warfare-policy-offline-combat-oct11.md).
- [16-file source evidence ledger](04-game-systems/warfare/source-evidence-war002-oct11.csv).
- [17-script archive byte comparison](04-game-systems/warfare/archive-script-comparison-oct11.csv).

ALIFE-03 / WAR-002 partially investigated; installed winners and creature/board/smart internals remain open. Runtime deferred.

## v0.1.34 — Native persistence and CtZ reconstruction

- [ALIFE-04: save/load phases, member reconstruction and CtZ identity](04-game-systems/alife/save-load-identity-oct11.md).
- [15-file evidence ledger](04-game-systems/alife/save-load-evidence-oct11.csv).

Bounded source pass complete. Effective serializer/profile reconciliation and runtime tests deferred. Next independent source work: native offline scheduler and squad/monster brains.

## v0.1.35 — Native offline scheduling and brains

- [ALIFE-05: schedule eligibility, task ownership and graph movement](04-game-systems/alife/offline-scheduling-brains-oct11.md).
- [21-file source evidence ledger](04-game-systems/alife/offline-scheduling-evidence-oct11.csv).

Bounded source pass complete; installed overrides/configuration and runtime remain deferred. Next native source work: graph location changes and online spawn realization.
