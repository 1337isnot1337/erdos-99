> Generated reading edition · [exact source](../../../docs/audits/target_c_complete_grid_phase_collapse_promotion_2026-09-12.md) · source SHA-256 `f32577f70b45b056551c0cf87063a4ee7db218a8f09e7f84c7c10d9d91e2e83f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E1EA857D86EE","canonical":true,"claim_ids":["C-GRID-PHASE-COLLAPSE"],"claim_statuses":{"C-GRID-PHASE-COLLAPSE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — Section 74 complete-grid phase-collapse promotion audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## Scope audited

This audit covers the proof-only `74-complete-grid-phase-collapse-audit.md` against canonical audit.26. The theorem is restricted to the quadratic positive-core branch after Section 73 supplies a linear-by-linear phase-pure complete train grid. It does not assert common crossing order, simple-connectedness, an additive Cartesian array, or a final diameter contradiction.

## Exact proof audit

Let `A,B` be the Section-73 phase-pure complete shores, with fixed labels `ell_A,ell_B in Z/3`, and let `x_v` be the exact real phase potential from Sections 68–69.

1. Section 68 orients every retained rhombus crossing `u->v` so that
   $$
   \phi_v-\phi_u\equiv\pi/3+\delta_{uv}\pmod\pi,
   \qquad x_v-x_u=\delta_{uv}>0.
   $$
   Section 69 writes `phi_v congruent x_v+(pi/3)ell_v (mod pi)` on the retained grain.
2. Substitution cancels the real increment and gives `ell_v-ell_u=1 (mod 3)` for every oriented retained crossing.
3. The shores `A,B` have two fixed distinct labels. Therefore the same label order occurs at every `A x B` crossing. After swapping shore names if needed, every crossing is oriented `A->B`, so
   $$
   \delta_{ab}=x_b-x_a>0
   \quad(a\in A,b\in B).
   $$
   In particular `max_A x < min_B x`.
4. Every `A x B` pair is a distinct retained rhombus. Hence
   $$
   S_{AB}:=\sum_{a,b}\delta_{ab}
   $$
   is a sub-sum of the global Section-68 angular defect `Delta_train`.
5. Canonical (68.14) gives
   $$
   \Delta_{train}<C_{phase}D,
   \qquad
   C_{phase}={\pi^2\sqrt3(2+\sqrt3)\over12}.
   $$
   Thus if `|A|,|B|>=gamma D`, the product mean
   $$
   \lambda=S_{AB}/(|A||B|)
   $$
   is at most `C_phase/(gamma^2 D)`.
6. Put `x_A^+=max_A x` and `x_B^-=min_B x`. Since every product term is at least `x_B^- - x_A^+`, that gap is at most `lambda`.
7. The exact product identity also gives
   $$
   {1\over|A|}\sum_A(x_A^+-x_a)\le\lambda,
   \qquad
   {1\over|B|}\sum_B(x_b-x_B^-)\le\lambda.
   $$
   Markov therefore retains subfamilies `A_0,B_0` of at least half the original shore sizes with each tail at most `2lambda`.
8. For every retained pair,
   $$
   \delta_{ab}
   =(x_b-x_B^-)+(x_B^--x_A^+)+(x_A^+-x_a)
   \le5\lambda.
   $$
   Hence every crossing in the still-complete `A_0 x B_0` grid has angular defect `O(1/D)`.

No topology enters steps 2–8. Holes remain allowed. The argument is stronger than an average-defect statement because the product sign/order turns one global average into a uniform bound on half-sized shores.

## Promotable conclusion

There is a fixed `gamma>0` along every quadratic-core subsequence such that the actual source contains a complete internally noncrossing train grid `A_0 x B_0` with

$$
|A_0|,|B_0|\ge(\gamma/2)D
$$

and every grid rhombus satisfies

$$
0<\theta_{ab}-\pi/3\le {5C_{phase}\over\gamma^2D}.
$$

Equivalently, both train phase families have `O(1/D)` potential width on a linear-size complete grid.

The next obligation is unchanged in type but much sharper in scale: use the inverse-diameter phase-collapsed complete grid plus the `O(D)` physical boundary/interface budget to prove common-order/penetration or a direct strict diameter contradiction.
