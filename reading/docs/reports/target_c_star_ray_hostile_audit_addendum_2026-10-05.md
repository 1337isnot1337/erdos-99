> Generated reading edition · [exact source](../../../docs/reports/target_c_star_ray_hostile_audit_addendum_2026-10-05.md) · source SHA-256 `a12cc4589ae410cf99efe71183549ae83f871aad0437be4df4c9e3c29f6fef0b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-7BBC77E150C9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: exact endpoint regressions for the star-ray hostile audit

**Date:** 2026-10-05  
**Source branch:** `swarm/audit/star-ray-20261001`  
**Source HEAD:** `542c8b93aca2fccf14f5c5973c89b7e44f8ba0be`  
**Source verifier SHA-256:** `4b462cb5086c892ae2c5e006bbdef09dd5bfd133b58c9eb0e60c88c7ec5353c7`  
**Classification:** unreviewed finite regressions; noncanonical.

## Recovered checks

The recovered exact verifier extends the existing star-ray hostile audit with three finite checks. It tests full-span exterior-train moves with multiple row spans and exact inactive blockers; it tests two quadratic-field sources that distinguish empty and singleton far-arc endpoints; and it tests whether aggregate contact-cut balance implies the edgewise contact-vector rule. The script also retains its earlier finite directed-cycle ordering enumeration.

The verifier passed. Its encoded examples include a nine-vertex full-span move with four full-span rows, two proper rows, two inactive unit blockers, preserved old contacts, and feasible old diameters. The exact five-vertex endpoint checks find an empty far arc at parameter `1/100` where the aggregate balance holds but the edgewise rule fails, and a singleton endpoint at parameter zero with a feasible encoded move reducing the diameter count from four to two.

These are finite regressions only. The examples do not encode the full source KKT/contact-cut law, actual global train cuts, or global optimality. They do not settle C-II or Level I.
