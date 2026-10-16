<!-- theorem-state: {"artifact_id":"ART-3417BDBCDECF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Audit — Target C §148 outer-geodesic endpoint exclusion

**Date:** 2026-09-12
**Reviewed:** docs/reports/target_c_section148_outer_geodesic_endpoint_2026-09-12.md
**Disposition:** PASS at proof-only/audited-working scope; theorem state unchanged.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

The load-bearing checks are:

1. The hypothesis \(b-P_F=o(D)\) is explicit. No general outer-detour theorem is
   imported.
2. The occurrence-counted outer walk may backtrack. Projection total variation is
   still at least twice the force-hull width, so the cosine-transform argument
   yields uniform projective direction measure only under that hypothesis.
3. §142 supplies atomic train mass \(x\sigma\ge2\sqrt{\Delta_2}\). Every train has
   two face-side endpoint occurrences, and the exact handshake identity is
   \(2T=b+Q+4f\). Hence atomic endpoints not on the outer walk pay \(Q+4f\).
4. The degree-five bound \(f\le Q\) gives \(Q+4f\le5Q\), so
   \(Q/D\ge(4/5)\sqrt{\Delta_2}\) and then
   \((q-k)/D\ge\pi/2+(2/5)\sqrt{\Delta_2}\).
5. At the §146 endpoint, \(t-\kappa/9\ge C_{146}\) and \(t\to C_{146}\) force
   \(\kappa=k/D\to0\). The face lower and outer-walk upper bounds squeeze
   \(f/D,Q/D\) to \(2C_{146}-\pi\), which forces \(b/D\to\pi\), hence the
   explicit zero-detour hypothesis.
6. The conclusion is only qualitative separation above \(C_{146}\). No numerical
   uniform gap is claimed, and the linear-detour and inactive-container branches
   remain open.

No canonical theorem-state promotion is proposed.
