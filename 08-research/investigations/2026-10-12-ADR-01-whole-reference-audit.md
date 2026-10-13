# ADR-01 — Whole-reference consolidation, provenance, navigation and consistency audit

> ADR document set: **v0.1.83**. Research revisions and source/build versions below describe their original scope.

- ID: ADR-01
- Subsystem: whole-reference maintenance / cross-system consolidation
- ADR revision: v0.1.82
- Record status: complete-within-scope for repository-wide audit and substantiated corrections; effective integration partial
- Source status: scoped-source-audit of files/ledgers/current entry contracts; prior source findings remain qualified
- Runtime status: independent game/profile testing deferred; external observations not reclassified
- Baseline IDs and provenance record: ADR v0.1.81 `dc826c78041971cac96710b329b6ce85905e8e13`; original archive/commit/report pins in [provenance register](../../00-environment/provenance-register.md)
- Last reviewed: 2026-10-12

## Question and scope

Are current ADR entry points, source/artifact identities, completion claims and evidence/navigation roles coherent across the entire repository, and what corrections can be supported without exhaustive native revalidation or game execution?

Included: all 378 baseline files/304 Markdown pages, 59 CSV schemas/seven JSON datasets; eleven behavior README/guide/status triples and their scoped audit links; current API/evidence/index/roadmap/provenance/project categories; source/reference integrity where original inputs are available; preservation; targeted validator improvement and tests.

Completion requires a complete inventory, coherent current status/provenance/navigation, explicit unchecked categories and corrections with evidence. Excluded: every sentence/native symbol/export/converter/build semantic re-trace, full unchanged catalog regeneration, every package comparison re-execution, historical May/September source checkout, raw report/dump review, all addons, actual migrations and engine/game runtime. The audit is whole-reference in coverage, with bounded semantic/provenance checks rather than a universal correctness guarantee.

## Evidence and method

[Audit evidence](../../evidence/reference/README.md) contains raw base-file inventory, ledger classification/integrity, eleven entry contracts/33 original hashes, 19 correction boundaries and summary. Original ledger schemas and datasets are retained byte-for-byte. Map explicit source IDs/legacy archive labels to their declared source roots; recheck hashes/counts/ranges and reference markers at original revisions. Do not substitute October source for historical May/September claims.

Checks cover **938 source/file rows/1,322 ranges/334 available source paths** and **102 earlier ADR reference rows**. Four UPSTREAM0912 rows retain remote pins without a local rehash. Generated APIs, comparisons, external observations, migration and templates retain their original purpose; a schema inventory does not reproduce a generator or game observation.

Read current category/index/baseline/manifest/API and eleven entry/status contracts; compare scoped audits and independently named source/effective/runtime axes. Review public guides for lifecycle/authority/alias, request/completion, schema/campaign and diagnostic/error qualifications. Rebuild current index from actual Markdown paths/titles, preserve detailed canonical homes and separate current versus historical groupings. Add a focused structural check only where the actual label drift demonstrated a gap.

## Findings and corrections

- **Current grouping drift:** later APIs/ledgers were appended under historical sections, the game-system hub omitted configuration, and the full index mixed later additions into unrelated blocks. Current API/evidence categories now lead, original May/starter bodies are retained as historical, and the index lists all actual Markdown pages by category. N01/N09/N10 and correction V01.
- **Verification labels were misleading despite valid links:** INDEX v0.1.56/v0.1.60 labels pointed to v0.1.69. The full report listing now derives labels from each report title/path. A narrow local report-label validator with two positive/negative regression cases prevents the same explicit revision mismatch without conflating source-version labels. V01/V02.
- **Next-step drift:** some current hubs/status pages still called completed gameplay/tasks/ARCH-02 work next. Those allocations are labeled original or replaced with current scoped status; all central guides link consolidated closure while retaining source findings and per-subsystem audit authority. N02–N08/N11/N12.
- **Provenance roles required consolidation:** archive source pins, binary candidate, historical user logs, external reports, full May UI pin, September comparison and CtZ research snapshot now have a central register. The CtZ link no longer asserts an unseen current release; early short-pin limitations are explicitly historical. P01/P02.
- **Preservation counts distinguish document roles:** v0.1.81’s reported 74 dated bodies included the directory README (73 dated records plus one entry). That historical report remains preserved; the current baseline has 74 dated investigations plus the entry README. C01.
- **Completion remains qualified:** selected foundations and this documentation audit close within scope. Effective installed winners/aliases/serializer/identity/lifetime chains remain partial; external UI/clock reports remain separately observed; runtime remains deferred. No design protocol is promoted to implemented or tested engine behavior.

Correction IDs are local to [corrections ledger](../../evidence/reference/corrections-2026-10-12.csv). They describe maintenance, not newly diagnosed native bugs.

## Competing explanations and missing edges

A correct local link can carry a wrong revision label; a current document banner can obscure an older source scope; an available package can be mistaken for a winning profile; a passing fixture can be mistaken for integration success. Separate roles/axes address these ambiguities without inferring runtime behavior.

Historical May extraction and four September remote source rows were not re-traced locally. Unchanged generated inventories/comparisons and external report bodies are preserved, not newly reproduced. Exact executable/compiler/profile, winning globals/binders/dispatch/installers/resources, storage/root/snapshot and campaign pairing remain named gaps in the [status matrix](../reference-status.md). No exhaustive claim-level proof follows from hashes and structural tests.

## Checks and outcomes

[Verification](../verification-2026-10-12-v0.1.82.md) records integrity/reproduction, all eleven entry roles, full Markdown index coverage, preservation, repository checks, the twelve-test suite and full published-tree verification. Two implemented validator tests are added; earlier ten tests continue to pass. Tool/test changes are explicitly excluded from the otherwise byte-preserved artifact set. No engine compiled, game ran, save altered or third-party source/assets redistributed.

## Disposition and next work

ADR-01 is complete within declared whole-reference audit scope. [Current status](../reference-status.md), [provenance](../../00-environment/provenance-register.md), [full index](../../INDEX.md) and [roadmap](../../ROADMAP.md) are the central entry points. Prior dated investigations/history and source/evidence pins remain intact.

The planned selected source/design foundation and whole-reference documentation pass are complete. Remaining work is relevant effective-profile source closure, a concrete targeted question or separately resumed runtime verification. Exhaustive unrelated engine/addon/build depth remains optional. CtZ gameplay remains in its separate project.
