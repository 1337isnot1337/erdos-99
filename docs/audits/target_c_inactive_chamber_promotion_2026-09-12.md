<!-- theorem-state: {"artifact_id":"ART-28C6B2C29CAD","canonical":true,"claim_ids":["C-INACTIVE-CHAMBER"],"claim_statuses":{"C-INACTIVE-CHAMBER":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Section 77 promotion audit

**Date:** 2026-09-12

This note records the hostile promotion audit of `77-inactive-chamber-saturation-audit.md`.

## Certified finite chain

1. Every actual diameter endpoint is an extreme source-hull vertex. The proof by strict convexity of squared distance is valid.
2. Consecutive force-hull extreme vertices cut the source hull into disjoint convex exterior caps. Oler applied to each cap's external source points plus the two closing-chord endpoints gives
   `Z_ext <= (area(K)-area(F))/a0 + (per(K)+per(F))/2 - P_com - r`.
   Points on a closing chord already lie in `F`, so they are not external and create no omission or double count.
3. Combining the cap inequality with the strict translated-lattice comparison, isodiametry, and Cauchy's perimeter bound gives `a0 N_F=area(F)+O(D)`. Oler on the full source hull gives `a0 n=pi D^2/4+O(D)`, hence `a0 Z_ext=pi D^2/4-area(F)+O(D)`.
4. Canonical `C-FS-STABILITY` therefore gives `liminf N_F/D^2 >= A_SC/a0`, where `A_SC=(2rho+sin(2rho))/4` and `rho=cos rho`.
5. The Section-67 chamber assignment is literal. An isolated source point cannot lie in the interior of an old unit contact edge. A point on an added force-hull side is assigned to the unique convex pocket on the interior side. Exceptional bounded faces and outer pockets therefore partition the inactive population in `F` without double counting.
6. The exact identity `m=R_4+f+q-k+1` and `A_4=a0 R_4+E_4`, with canonical Section-68 `E_4=O(D)`, imply `a0 Z_ch=A_ch+O(D)`.
7. Exceptional-face perimeter is `4f+Q<=10 pi D`. The exact outer-pocket perimeter identity gives total outer-pocket perimeter at most `3 pi D`. Hence total chamber perimeter is at most `13 pi D`; the chamber count is `O(D)`.
8. For isolate-only Oler slacks `sigma_j=A_j/a0+P_j/2+1-z_j>=0`, the summed slack is `O(D)`.
9. In the branch `m=o(D^2)`, rhombus area is `o(D^2)` while chamber area has liminf at least `A_SC D^2`. Isoperimetry gives one chamber with
   `liminf area(C_*)/D^2 >= 4 A_SC^2/(169 pi)>0`.
   Its individual Oler slack and perimeter are `O(D)`, so it contains `Omega(D^2)` actual contact-isolated source points.

## Scope and non-conclusions

The theorem keeps every source point. It does not infer that contact-isolated points are KKT-positive, does not use the historical annular Voronoi theorem, and does not claim that boundary-order Oler slack alone forces an exact unit contact or equilateral triangle. The macroscopic chamber may be either one exceptional bounded contact face or one convex outer pocket.

## Disposition

Section 77 is valid and should be promoted as the canonical subquadratic-core reduction. Dependencies are exactly `C-FS-STABILITY`, `C-RHOMBUS-POP`, and `C-PUNCTURED-PHASE` plus standard finite Oler/convex inequalities already used in the canonical stack. C-II remains open.
