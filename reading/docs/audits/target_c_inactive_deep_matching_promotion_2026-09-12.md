> Generated reading edition · [exact source](../../../docs/audits/target_c_inactive_deep_matching_promotion_2026-09-12.md) · source SHA-256 `ba4808e8ecb871dc5604188340c7b3c7c661c96307a5e4f61dba412191db4f98`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-B49974A38923","canonical":true,"claim_ids":["C-INACTIVE-DEEP-MATCHING"],"claim_statuses":{"C-INACTIVE-DEEP-MATCHING":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C deep near-unit isolate matching promotion audit

**Date:** 2026-09-12

This note records the independent hostile audit of
docs/targets/target-c/87-deep-near-unit-isolate-matching-audit.md.

## Certified chain

1. In a convex chamber with perimeter P<=P_0D, the radius-1/2 disks centered at
   isolates in the width-w boundary strip lie in
   (C+B_{1/2})\setminus C_{-(w+1/2)}. Steiner's outer-parallel formula and
   inner-parallel coarea bound this annulus by (w+1)P+pi/4. Disjoint disk
   areas therefore give |Z cap U_w|<=4(w+1)P/pi+1=O_w(D).
2. The canonical near-unit matching inequality gives, at epsilon=K/D,
   nu_{K/D}>=(3alpha K/(8a_0)-S_0/2)D for a chamber with
   A>=alpha D^2 and isolate slack sigma<=S_0D.
3. Choose K=K_w so the matching coefficient exceeds the boundary-strip
   coefficient. Since a matching is vertex-disjoint, at most |Z cap U_w| of
   its edges touch the strip. At least c_wD matching edges therefore have both
   endpoints at depth at least w and lengths in (1,1+K_w/D].
4. For w>1, both endpoints and their joining segment lie in the convex inner
   parallel body C_{-w}. Moving one endpoint toward its mate by at most K_w/D
   stays in C_{-w}. Every source point outside C is at distance at least w from
   every point of C_{-w}; the global source hull has diameter D. Thus neither
   an outside source point nor the diameter constraint can be the first
   obstruction. Any first blocker is another source point inside the same
   chamber.

## Scope and non-conclusions

The conclusion is a linear family of deep almost-contacts and a localization of
possible first blockers. It does not make the pair-closing motions simultaneous,
does not force an exact unit contact in the original minimizer, and does not imply
an equilateral triangle. The remaining isolate-only collective deformation problem
is still open.

## Disposition

The theorem is valid and should be promoted as C-INACTIVE-DEEP-MATCHING, depending
on C-INACTIVE-CHAMBER, C-INACTIVE-NEAR-MATCHING, and standard convex geometry.
Target C-II remains open.
