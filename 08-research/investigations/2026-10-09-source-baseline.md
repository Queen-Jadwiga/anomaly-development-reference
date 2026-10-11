# INV-001: Establish upstream source baseline

> ADR document set: **v0.1.54**. Research revisions and source/build versions below describe their original scope.

- Date: 2026-10-09
- Question: Which source represents the user's installed `MT-TEST 2026.05.15` engine?
- Runtime observations: `xrCore` 9959; X-Ray Monolith 1.5.3; Modded Exes MT-TEST 2026.05.15.
- Upstream evidence: https://github.com/themrdemonized/xray-monolith ; https://github.com/themrdemonized/xray-monolith/releases
- Finding: Repository describes MT-TEST builds of Anomaly 1.5.3 and provides dated changelog, supporting branch-family match.
- **Unresolved:** Exact commit/release artifact match, executable hash and any GAMMA-distributed patches.
- Status: OBSERVED + UPSTREAM-DOCUMENTED; NOT YET SOURCE-PINNED.
- Next step: Identify release tag/commit and compare with packaged executable details.
