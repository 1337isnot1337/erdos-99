<!-- theorem-state: {"artifact_id":"ART-C574AE181173","canonical":false,"claim_ids":["C-TRIANGULAR-TWO-BOUNDARY-HOLE-CAPACITY-REGRESSION"],"claim_statuses":{"C-TRIANGULAR-TWO-BOUNDARY-HOLE-CAPACITY-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit: strict capacity after two triangular boundary holes

**Date:** 2026-10-09  
**Audit base:** `origin/main=7fb7a7d1256f0e6b17bf2fb5fe01cfc6cfb664a1`, state `2026-10-09.audit.187`  
**Source branch:** `origin/research/sol/target-c-level1-gpt61-2026-10-04` at `9875cd6a77939bb6347353fc798ab8f9ab03ec3e`  
**Classification:** independent reconstruction; **REGRESSION VALID — promote the exact finite-frame capacity statement**.  
**Dependency:** the lower capacity bound uses `C-TRIANGULAR-TWO-BOUNDARY-HOLE-STRICT-REFILL`, promoted by PR #892 at main commit `7fb7a7d1256f0e6b17bf2fb5fe01cfc6cfb664a1`.  
**Target effect:** no C-II route is eliminated; this blocks a `K+1` strict-site argument in the stated frames only.

## Frozen candidate and verifier

The source candidate is [`target_c_triangular_two_pin_strict_capacity_2026-10-05.md`](https://github.com/1337isnot1337/e-99/blob/9875cd6a77939bb6347353fc798ab8f9ab03ec3e/docs/reports/target_c_triangular_two_pin_strict_capacity_2026-10-05.md), SHA-256 `ac83868db308eefa21e107a2fb733c0803aa0c8dd849ae302e6a3d26d1642085`. The checker is [`verify_target_c_triangular_two_pin_capacity_2026_10_05.py`](https://github.com/1337isnot1337/e-99/blob/9875cd6a77939bb6347353fc798ab8f9ab03ec3e/research/verify_target_c_triangular_two_pin_capacity_2026_10_05.py), SHA-256 `a9797a7b9e0c95bb56fef8d3111ec75737692f6bbf976ac007f079a690a76749`. I inspected and reran it: 716 elementary unit triangles and 228 admissible triangles across `(3,3)`, `(3,4)`, `(3,7)`, `(3,20)`, `(3,80)`, and `(4,4)`; all checks pass using exact rational / `Q(sqrt(3))` coordinates.

The script verifies the finite triangulation counts and center-star incidence for those listed cases. It does not prove the all-`n` count, the continuous packing upper bound, or the lower construction. The all-`n` upper bound and the disk-packing argument below are analytic; the lower bound is the separately audited Audit.192 refill theorem.

## Exact surviving statement

Let `C_(m,n)` be the closed triangular-lattice parallelogram with vertices `0`, `m u`, `n v`, `m u+n v`, where `u=(1,0)` and `v=(1/2,sqrt(3)/2)`. Let `B_(m,n)` be all boundary lattice labels `(i,j)` with `i=0,m` or `j=0,n`, except the two adjacent bottom labels `(1,0),(2,0)`. Define strict capacity as the maximum size of a finite set `X subset int(C_(m,n))` satisfying

- `|x-y|>1` for all distinct `x,y` in `X`; and
- `|x-b|>1` for every `x in X` and retained pin `b in B_(m,n)`.

**`C-TRIANGULAR-TWO-BOUNDARY-HOLE-CAPACITY-REGRESSION`.** The strict capacity is exactly `K=(m-1)(n-1)` when either (i) `m=3` and `n>=3`, or (ii) `m=n=4` (where `K=9`). Thus two adjacent deleted pins do not universally create a `K+1` strict site.

## Independent upper-bound proof

Triangulate `C_(m,n)` into the closed elementary equilateral triangles

`((i,j),(i+1,j),(i,j+1))` and `((i+1,j),(i,j+1),(i+1,j+1))`.

Every triangle has diameter one. If `x` belongs to a closed unit triangle containing a retained pin `b`, then `|x-b|<=1`: write `x` as a convex combination of the triangle's vertices and apply the triangle inequality to the three distances from those vertices to `b`, each at most one. This contradicts the strict pin clearance. Therefore every feasible target lies in at least one triangle containing no retained pin. Call those triangles admissible. A unit triangle has diameter one, so it contains at most one point of a mutually strictly separated set. Assigning each target to any admissible triangle containing it gives `|X|<=N_adm`, with closed triangles covering edge and vertex cases.

For `m=3`, any triangle using a column `i=0` or `i=3` contains a retained wall pin. Any triangle using the top row `j=n` also contains a retained pin. The only admissible triangles are the two per cell in the one-column strip `i=1`, `j=0,...,n-2`; all their vertices are either interior labels or the two deleted bottom pins. Hence

`N_adm = 2(n-1) = (m-1)(n-1) = K`.

For `m=n=4`, only cells `i=1,2` and `j=0,1,2` can contribute. The bottom cell at `i=2,j=0` contains retained pin `(3,0)` in both triangles. The other contributing cells are `(1,0)` with two triangles, `(1,1),(1,2)` with four, and `(2,1),(2,2)` with four, for ten admissible triangles. Six of them contain the lattice vertex `c=(2,2)`; each is contained in the closed unit disk `B(c,1)`, since all its vertices are either `c` or unit neighbors of `c` and the disk is convex.

Six points with mutual distances strictly greater than one cannot lie in a closed unit disk. If one is the disk center, it is within one of each other point. Otherwise order their polar angles; some consecutive angular gap is at most `pi/3`. If the corresponding radii are `r,s in [0,1]`, then

`|x-y|^2 <= r^2+s^2-rs <= 1`.

The last inequality follows because the expression is convex in each variable and its four corner values on `[0,1]^2` are `0,1,1,1`. If ten targets existed, the ten admissible triangles would each be assigned one target, placing six strictly separated targets in that disk, a contradiction. Thus `|X|<=9=K`.

For both frame families, Audit.192 supplies `K` strict interior sites by releasing all `K` interior lattice labels after omitting the two pins. The upper and lower bounds match, proving exact capacity.

## What the regression does not show

This is a continuous arbitrary-point capacity result for the stated pinned containers, not a sampled packing bound. The 4-by-4 frame contains many unit triangles, and neither frame is asserted to occur in a triangle-free global minimizer. In particular, the regression does **not** exhibit a canonical source with interior population `K-1` and does not refute `C-TRIANGULAR-TWO-BOUNDARY-HOLE-POPULATION`. It shows only that the two-hole replacement cannot improve that population bound to `K` by counting strict interior sites alone in these frames. No statement is made for `m,n` both tending to infinity or for a different interface/capacity mechanism.
