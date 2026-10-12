# Workflow and structure verification — ADR v0.1.40

> ADR document set: **v0.1.57**. Research revisions and source/build versions below describe their original scope.

**11 October 2026 · documentation/source integrity checks; engine/game runtime deferred.**

## Scope

The migration starts from ADR commit `39f32e8f55d012a23fe35b850ea3b5f7b8d7b748`. It standardizes workflow/layout/templates and current navigation, relocates 41 paths, and retains 22 Markdown forwarding pages. [The migration manifest](migrations-2026-10-11-v0.1.40.csv) records every old/canonical path.

Canonical locations: APIs in `02-lua-api/<subsystem>/`, question records in `08-research/investigations/`, ledgers in `evidence/<subsystem>/`, extractors/checkers in `tools/`. Historical formats/baselines are preserved and explicitly grandfathered by [the layout conventions](repository-layout.md).

## Checks

- Compared all 10 relocated A-Life/Warfare investigation bodies and seven relocated UI class entries against the starting snapshot after mechanically rebasing relative links. No research statement was rewritten.
- The 18 relocated CSV datasets use their existing Git blob identities; original schemas, IDs and bytes are retained. Five catalog CSVs rebuilt through the relocated extractor match their previously published blob identities exactly.
- Rebuilt the catalog using explicit source/output roots, preserving 84 class rows, 1,150 binding rows, 174 helper declarations, 1,372 script declarations and 73 source input files. Repeated generation and input-hash checks establish stability within the documented extraction scope.
- Ran the new repository checker over the reorganized tree, checking local targets, Markdown anchors, repository-root containment and required entry/navigation files. Its totals are recorded below after the final run.
- Exercised the checker against valid/duplicate-heading links and missing-file, missing-anchor and root-escape cases, and checked both maintained Python tools for syntax.
- Reviewed forwarding pages and rewrote current internal links to canonical records. C-03/C-04 and the CtZ landing link remain present.

## Final structural check

Checked **139 Markdown files**, **433 local targets** and **4 anchors**; zero errors. This includes historical forwarding pages.

## Publication and limits

Publication checks compare the resulting tree's moved dataset identities and changed text/tool blobs, then confirm the branch head. The final commit is reported after publication; this file does not invent its own commit SHA in advance.

This is a structural/process verification, not a semantic audit of every historical claim, live upstream URL verification, an exhaustive signature/converter/build audit or engine compilation. Historical UI baselines and differing CSV schemas remain stated exceptions. Active GAMMA winning scripts/executable correspondence and all engine/game runtime checks remain pending. No gameplay change, third-party source redistribution or license is included.
