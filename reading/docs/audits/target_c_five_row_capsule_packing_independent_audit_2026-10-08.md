> Generated reading edition · [exact source](../../../docs/audits/target_c_five_row_capsule_packing_independent_audit_2026-10-08.md) · source SHA-256 `6101e51dfc34b273483ff7a54414696b3b9ed37d89601d61f4cc9a87e76cbead`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C2525DCBD5F6","canonical":true,"claim_ids":["C-OO-SHORT-PAIR-PATH-BANDWIDTH-5","C-UNIT-CAPSULE-PACKING-5"],"claim_statuses":{"C-OO-SHORT-PAIR-PATH-BANDWIDTH-5":"canonical","C-UNIT-CAPSULE-PACKING-5":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit of the five-row capsule packing theorem

**Date:** 2026-10-08  
**Audit base:** `origin/main=4774ba12f82456aa178918789888d71d1cd0b6fe`, state `2026-10-08.audit.146`  
**Source branch:** `research/sol/target-c-owner-order-closure-20261006`  
**Frozen source tip:** `bf288c82e8a62466d5580025c94e750a177e63e2` (open PR #737)  
**Source report:** `research/target_c_high_t_tb1_five_row_capsule_packing_t18687_2026-09-17.md`, SHA-256 `f7f6b6d6db9838b88fbc46bb9b3e79f767fa7708dc8f2eddc015f4ab1e24395a`; Sections 1--2 only.  
**Source verifier:** `research/verify_target_c_high_t_tb1_five_row_capsule_packing_t18687.py`, SHA-256 `2c064f61abf5a4e3d5712126c5679ec9bccda40968e73b4485b844c2b07ace37`.

**Verdict:** **PASS — promote `C-UNIT-CAPSULE-PACKING-5` and `C-OO-SHORT-PAIR-PATH-BANDWIDTH-5`.** The exact finite theorem gives the supplied-path five-row consequence when `L<=21/20`, while the prior Oler path theorem remains canonical at its broader scope. The exact-swap density, Horn, poison-forest, and ladder claims in source Sections 3--5 are not included in this audit.

## Exact finite theorem

For `L>=0`, define the stadium

```math
S_L=([0,L]\times\{0\})+B(0,1/2).
```

If `L<=21/20` and `X` is a finite subset of `S_L` whose distinct points have mutual distance at least `sqrt(3)/2`, then

```math
\boxed{|X|\le5.}
```

The bound is sharp at `L=1`. One exact five-point set is

```math
(-1/2,0),\quad(1/4,1/2),\quad(1/4,-1/2),\quad
(6/5,9/20),\quad(6/5,-9/20).
```

All five points lie in `S_1`, and every squared pair distance is at least `3/4`. No claim is made that `21/20` is the largest segment length for which the packing number is at most five.

## Independent proof of the upper bound

The capsules are nested: `S_L` is contained in `S_{21/20}` whenever `L<=21/20`. Cover `S_{21/20}` by the closed squares of the grid `Q_ij=[i/24,(i+1)/24] x [j/24,(j+1)/24]` whose closures meet the stadium. A point on a grid boundary may be assigned to either incident retained square.

The exact distance from a square to the segment `[0,21/20] x {0}` is the Euclidean norm of its horizontal and vertical interval gaps. Scaling coordinates by `480` turns the test that this distance is at most `1/2` into an integer squared-distance comparison. The frozen certificate enumerates exactly `1096` retained squares. Each square has squared diameter `2/24^2=1/288<3/4`, so no square can contain two points of a `sqrt(3)/2`-separated set.

For two distinct squares `Q,Q'`, let `dx` and `dy` be the maximum possible absolute coordinate differences between points in the respective rectangles. Their maximum squared separation is `dx^2+dy^2`. Put an edge between the two square labels if and only if

```math
4(dx^2+dy^2)\ge3\cdot24^2.
```

This is an exact integer test. If six separated points existed, they would occupy six distinct retained squares. Each pair of those squares would have maximum separation at least `sqrt(3)/2`, so their six labels would form a `K_6` in this compatibility graph.

The verifier finds no `K_6`. I audited its bitset search: at each recursive state, it intersects the remaining candidates with a chosen vertex's neighborhood, then removes that vertex before trying the next branch, so every clique is considered. Its greedy coloring partitions the candidate graph into independent sets; the number of colors bounds every clique in the current candidate prefix. Pruning when the current clique plus that prefix bound is below six is therefore safe. All graph construction, branch decisions, and bounds use integer arithmetic. The small-graph brute-force comparisons are implementation checks; the proof of the finite statement is the covering and exhaustive no-`K_6` certificate together with the algorithm argument above.

## Path consequence and relation to the six-row theorem

By canonical `C-OO-SHORT-PAIR-PATH-BANDWIDTH`, the centers of the distinct actual strict unit rhombi crossed by a supplied ordered crosscut path lie in the radius-`1/2` capsule around the source segment and are pairwise separated by at least `sqrt(3)/2`. The finite theorem therefore gives row span `N<=5` whenever that segment length satisfies `L<=21/20`.

For fixed `K>0`, if `D>=20K` and `L<=1+K/D`, then `L<=21/20`, so the span is at most five. This strengthens the earlier Oler six-row consequence for `D>10K` on the narrower regime `D>=20K`; the general Oler inequality and its six-row consequence remain valid outside the five-row range.

This does not extract an ordered crosscut path for every source pair or from every owner system. It proves no exact-swap system exists, no blocker ownership or density estimate, no Horn implication, and no feasible source motion or strict-diameter competitor. Contact-isolated points are not deleted: the conclusion applies to the actual center set and path geometry supplied by the hypotheses.

## Verifier boundary

The frozen source verifier was inspected and rerun as `research/verify_target_c_unit_capsule_five_row_packing_2026_10_08.py`. It passes, enumerating `1096` cells and reporting `320050` branch-and-bound nodes before proving no `K_6`; its rational sharpness check confirms the five-point example. The code does not itself establish the continuous cover reduction or prove the clique-search pruning rule; those are supplied in this audit. Its `check_propagated_constants` routine asserts the exact `gamma6` value, `gamma6/gamma7=7/6`, and the threaded-lower coefficient. It assigns the proposed upper-localization coefficient as a `Fraction` and returns it without asserting its equality with `gamma6/(48 A_*)`; it also does not verify the source-level premises or the poison-forest alternatives. The verifier uses floating-point only for printed diagnostics after exact assertions pass.

## Withheld source claims

Source Sections 3--5 use additional population, simultaneous exact-swap decoupling, genuine-upper exception, Horn poison-forest, and path-capacity statements. Their hypotheses and dependency graph are outside this audit. In particular, the `7/6` density improvement and the stated permanent LOWER/UPPER, ladder, and localized-upper coefficients remain unreviewed and are not canonical premises here.

## Frontier effect

The source geometry's conditional short-pair bandwidth drops from six to five when `L<=21/20` (equivalently, for `L<=1+K/D` once `D>=20K`). This is a local geometric improvement only. The C-II finite-move/payment obligation and Level I status do not change.
