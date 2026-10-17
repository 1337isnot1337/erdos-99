> Generated reading edition · [exact source](../../../docs/audits/target_c_inactive_chamber_hull_stability_promotion_2026-09-12.md) · source SHA-256 `b778de2e52ea370a110a26d32a31266ad95cfed31744a6c15ed84cd907a3a059`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-24F6D7DE2CD3","canonical":true,"claim_ids":["C-INACTIVE-HULL-STABILITY"],"claim_statuses":{"C-INACTIVE-HULL-STABILITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C convex-hull stability promotion audit

**Date:** 2026-09-12

This note records the independent hostile audit of
docs/reports/target_c_subquadratic_chamber_hull_saturation_2026-09-11.md.
The audit concerns only the convex-hull stability corollary; it does not promote
the unresolved protected inactive-hull release.

## Certified chain

1. Canonical C-INACTIVE-CHAMBER supplies, in the m=o(D^2) branch, one actual
   convex inactive chamber C_* with
   A_*>=(a_ch)D^2, P_*<=P_ch D, and
   a_0 z_*>=A_*-L_ch D. Every point in the selected set S_* is a retained
   contact-isolated source point, and C_* is contained in F and F is contained
   in conv(A); hence diam(C_*)<=D.
2. For any convex body C, the inner-parallel-body coarea formula and perimeter
   monotonicity give area(C)<=r(C) per(C). The maximal inner parallel body has
   zero area, so r(C)>=area(C)/per(C). Applying this to C_* gives
   r(C_*)>=(a_ch/P_ch)D.
3. For K=conv(S_*) contained in C_*, Oler gives
   a_0 z_*<=area(K)+c_0 per(K)+a_0, while convex perimeter monotonicity gives
   per(K)<=P_*. Combining with the Section-77 lower population bound gives
   area(C_*)-area(K)<=M_ch D, with
   M_ch=L_ch+c_0P_ch+a_0.
4. Fix a support direction u, an inball center o, a support point v, and
   s_0=h_C(u)-u dot o. The inball gives r(C)<=s_0, and
   s_0<=|v-o|<=D. The triangle with vertices
   v,o+r(C)w,o-r(C)w has a cap of depth s and area
   r(C)s^2/s_0 for every 0<=s<=r(C). If
   s<=h_C(u)-h_K(u), that cap lies in C\K, so
   area(C\K)>=(r(C)/D)s^2.
5. If a support gap t=h_C(u)-h_K(u) exceeds r(C), use the same cap estimate
   at depth s=r(C). It yields
   area(C\K)>=r(C)^3/D>=(a_ch/P_ch)^3D^2, contradicting the
   O(D) area deficit for large D. Otherwise use s=t and obtain
   t^2<=(D/r(C))M_chD<=(M_ch/kappa_ch)D.
6. Taking the supremum over support directions gives
   d_H(C_*,K_*)<=C_ch sqrt(D), with
   C_ch=sqrt(M_ch/kappa_ch). Since the support function of
   B(o,r) is u dot o+r, the same inequalities give
   B(o_*,kappa_chD-C_ch sqrt(D)) contained in K_*.
7. The argument uses no KKT variable for an isolated point, no full-source
   affine-kernel extension, and no claim that the inner disk contains a diameter
   pair. The strict near-equilateral rhombic regression remains compatible with
   the conclusion.

## Scope and non-conclusions

The audited statement is a source-specific geometric stability theorem for the
actual isolated points supplied by C-INACTIVE-CHAMBER. It is not an Oler equality
classification, a lattice-stability theorem, or a finite motion theorem. In
particular, it does not produce a unit contact, a unit equilateral triangle, or a
same-cardinality diameter-decreasing competitor. The protected inactive-hull
release remains the exact unresolved C-II obligation.

## Disposition

The convex-hull stability corollary is valid at the stated subquadratic-chamber
scope and should be promoted as C-INACTIVE-HULL-STABILITY, depending only on
C-INACTIVE-CHAMBER and standard convex/Oler inequalities. Target C-II remains open.
