# Source repositories — SRC-001

> ADR document set: **v0.1.85**. Research revisions and source/build versions below describe their original scope.

**Historical intake/orientation:** original May research limitations below are retained. Later scoped UI extraction records the full May commit in the [API catalog](../02-lua-api/api-index.md); the [provenance register](provenance-register.md) distinguishes that source pin, the preferred October archive and unverified binary correspondence.

**Research date:** 2026-10-09. **Evidence level:** Public upstream documentation, not local executable verification.

## Primary reference

- X-Ray Monolith Modded Exes: https://github.com/themrdemonized/xray-monolith
- Releases and dated changelog: https://github.com/themrdemonized/xray-monolith/releases
- Git commit history: https://github.com/themrdemonized/xray-monolith/commits

Upstream README calls out Anomaly 1.5.3 and says the MT build is labeled `MT-TEST` in the main menu and logs. It describes MT changes including multi-threaded subsystems and a reworked render graph. This agrees with our runtime log identification but does **not** uniquely identify the source commit.

## Secondary references

- Anomaly-focused fork: https://github.com/bergemon/xray-monolith-anomaly (may differ from user's executable)
- OpenXRay: https://github.com/OpenXRay/xray-16 (architectural comparison only; not an authoritative source for GAMMA's exact API)

## Source discipline

1. Capture full URL, revision SHA, path, symbol, and preferably line permalink for every engine-level finding.
2. Prefer the commit corresponding to the installed build once established.
3. Record `introduced_by` and `last_verified` separately.
4. Treat current HEAD docs as **upstream-current**, not automatically May-2026-compatible.
5. Don't copy repository code into the ADR unless licensing and attribution are reviewed; link to source instead.

### Follow-up investigation

Locate the May 15, 2026 MT-TEST release and trace its tag or archival commit. Existing changelog entries around 2026-05-05 and 2026-05-08 are useful chronological anchors but are not exact commit proof.
