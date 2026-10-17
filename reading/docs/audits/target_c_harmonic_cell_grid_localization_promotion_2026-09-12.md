> Generated reading edition · [exact source](../../../docs/audits/target_c_harmonic_cell_grid_localization_promotion_2026-09-12.md) · source SHA-256 `37c348d5326df36df16a16d5e17e857977e23fd291c7f13d8f122bb8ebf7cf39`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-CDAF5A7D06C8","canonical":true,"claim_ids":["C-HARMONIC-GRID-LOCAL"],"claim_statuses":{"C-HARMONIC-GRID-LOCAL":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Section 78 promotion audit

**Date:** 2026-09-12

This note records the independent hostile audit of `78-harmonic-cell-grid-localization-audit.md` before theorem-state promotion.

## Certified chain

1. A loaded force-hull vertex is incident to at most three positive unit contacts. All positive-contact neighbors lie in the inward half-plane of the force hull; triangle-freeness makes consecutive unit-contact directions differ by more than `pi/3`, so four such directions cannot fit in a semicircle. Therefore at most `3q<=3*pi*D` rhombi of the Section-69 grain touch the loaded set.
2. Deleting those rhombi removes only `O(D)` cells and creates at most four new boundary-edge occurrences per deletion. The surviving rhombi still have quadratic total mass and `O(D)` total physical perimeter.
3. Isoperimetry is valid for each edge-connected surviving rhombic component even with holes or pinch vertices: the counted physical perimeter dominates its geometric perimeter. Hence one surviving component `G_*` has `Omega(D^2)` rhombi.
4. Every remaining rhombus has all four vertices in `V\B` and its boundary contacts are positive-contact edges. Thus every edge-connected component lies in one unloaded positive-contact component `I_*`.
5. Harmonic trapping is the discrete maximum principle for the positive equilibrium weights at unloaded vertices. It gives `I_* subset conv(A_*)=:P_*`; convexity then contains every rhombus of `G_*`. Hence `G_* subset P_*`.
6. Since `area(P_*)>=a0 R_*` and `area(P_*)<=pi d_*^2/4`, the local attachment-cell diameter `d_*=diam(P_*)` is `Omega(D)` and at most `D`.
7. Theorem 10.6 applies to `G_*` with arbitrary holes. Its local trains are subsegments of trains of the parent coherent grain, so they inherit the same phase labels and reduced phase potential. Canonical Section 73 therefore gives an `Omega(D) x Omega(D)` phase-pure complete grid inside `P_*`.
8. The localization of Section 76 is exact. In its proof, the only use of the global source diameter before the two-leg estimate is `|p_11-p_00|<=D` for the two selected crossing centers. Here both centers lie in `G_* subset P_*`, so the same projection proof has `|p_11-p_00|<=d_*` and yields
   `d_* >= (sqrt(3)/2)(a+b) - S_AB/min(a,b) - 2`.
9. Canonical Section 68 still gives the global `S_AB=O(D)` defect bound. Since both shores are `Omega(D)`, the quotient is `O(1)`, so
   `a+b <= (2/sqrt(3))d_*+O(1)` and `ab<=d_*^2/3+O(d_*)`.

## Scope and non-conclusions

The theorem is only for the quadratic positive-core branch. It does not claim that shrinking one harmonic cell shrinks the global source diameter, does not prove the extracted complete grid covers a sufficiently large fraction of the cell, does not control contact-isolated source points, and does not assign KKT weight to physical contacts. Section 77 is a complementary branch theorem and is not a proof dependency.

## Disposition

Section 78 is valid and should be promoted as the canonical harmonic-cell localization of the quadratic coherent-grain branch. Dependencies should be explicit: `C-COHERENT-GRAINS`, `C-ATTACH-CURRENCY` for the harmonic-cell framework, `C-PSEUDO-GRID`, `C-HOLE-GRID-DIAMETER`, and `C-PUNCTURED-PHASE` for the global angular-defect budget. C-II remains open.
