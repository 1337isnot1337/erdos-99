> Generated reading edition · [exact source](../../../docs/reports/global_planarity_and_radius_barriers_2026-10-12.md) · source SHA-256 `02ba72cab64b73b6611a77c6d04af24c51ee3b345b58636e9d4b1acf61491593`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4193B848EBB4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Global replacement mechanisms: planarity and enclosing-radius barriers

**Date:** 2026-10-12
**Repository commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`
**State version:** `2026-10-10.audit.234`
**Run type:** whole-problem closing exploration and regression
**Target:** Level I, independent full-source mechanisms
**Classification:** unreviewed candidate; exact regressions
**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`
**Level I:** STILL OPEN

## 1. Exact goal and dependencies

The intended implication remains

```text
every sufficiently large triangle-free global source admits a planar replacement
of the same cardinality with all distances >= 1 and all distances < D
 -> contradiction to globality -> Level I.
```

This report uses only the problem definition, elementary linear algebra, and
elementary Euclidean geometry. It assumes no Target A/B/C source reductions.
All claims apply to actual source coordinates or explicitly distinguished
higher-dimensional distance matrices. The finite regressions are not global
minimizers for an unbounded cardinality sequence.

## 2. Convex contraction of all squared distances really is feasible in higher dimension

Let `P` be any unit-separated planar `n`-point source, centered at its centroid.
Let `B_0=P P^T` be its centered Gram matrix, with `P` the `n` by `2` coordinate
matrix, and let `J=I-11^T/n`. For `0<t<=1` put

$$
B_t=(1-t)B_0+\frac t2 J.
\tag{1}
$$

This is positive semidefinite, centered, and gives squared distances

$$
d_{ij}(t)^2=(1-t)|p_i-p_j|^2+t.
\tag{2}
$$

Thus all lower distances remain at least one, every old unit distance stays
exactly one, and if the old diameter `D>1`,

$$
\max d_{ij}(t)^2=(1-t)D^2+t<D^2.
\tag{3}
$$

So there is a genuine higher-dimensional strict competitor. This does not require
triangle-freeness.

### Exact obstruction to planar realization

For every nonzero `v` perpendicular to `1`,

$$
v^TB_t v=(1-t)|P^Tv|^2+\frac t2|v|^2>0.
$$

Consequently `rank B_t=n-1` for every `t>0`. Since a planar Euclidean distance
matrix has centered Gram rank at most two, the exact distance data (2) are
not realizable in the plane whenever `n>=4`. This statement covers collinear
sources as well.

The tempting chain

```text
convex feasibility of all lower/upper distance constraints
 -> planar strict competitor
```

therefore fails for every `n>=4`, not only at a special contact graph.

### Why closest rank-two truncation does not fix the argument

Suppose `P` is noncollinear and has two positive Gram eigenvalues `lambda_1`
and `lambda_2`. For `0<t<1`, the two largest eigenvalues of `B_t` are

$$
(1-t)\lambda_k+t/2\quad(k=1,2),
$$

and every remaining eigenvalue on `1^perp` is `t/2`. Keeping the two largest
eigenvalues therefore keeps the original coordinate column space. The resulting
planar placement is an affine image of `P`, up to a rigid motion. It is not an
independent general nonlinear replacement. In particular, a global source cannot
be improved by that truncation after unit normalization, by the definition of
global optimality. The canonical affine tensor obstruction is consistent with
this conclusion but is not needed to prove it here. At `t=1` every positive
eigenvalue ties; the column-space assertion is not claimed at that endpoint.

## 3. Contraction plus bounded corrections secretly decreases enclosing radius

Let `R(P)` be the minimum enclosing-circle radius of a planar source with diameter
`D`, and let `r(n)` be the minimum possible enclosing-circle radius of any
unit-separated `n`-point source. Suppose an endpoint has the form

$$
q_i=\alpha p_i+w_i,\qquad 0\le\alpha<1,
\qquad |w_i|\le\tau,
\tag{4}
$$

after choosing the origin at a minimum enclosing-circle center. Then

$$
R(Q)\le\alpha R(P)+\tau,
\qquad
\operatorname{diam}Q\le\alpha D+2\tau.
\tag{5}
$$

A frequently suggested sufficient condition for strict diameter improvement is

$$
2\tau<(1-\alpha)D.
\tag{6}
$$

But `D<=2R(P)`, so (6) also gives

$$
R(Q)<\alpha R(P)+(1-\alpha)D/2\le R(P).
\tag{7}
$$

If the original source already has `R(P)=r(n)`, no unit-separated endpoint (4)
can satisfy (6). This is a full-source cardinality obstruction, allowing arbitrary
independent corrective vectors. A finite candidate cloud consisting of multiple
translations of `alpha P`, with all translations of norm at most `tau`, is subject
to the same radius bound even if labels are selected or reassigned: every candidate
site lies in that one smaller disk.

This rejects (6) as a universal certificate for all nonglobal diameter sources.
It does not reject every endpoint of the form (4): an actual diameter test can
pass even when its crude bound (6) fails. It also does not establish that large
triangle-free diameter minimizers are enclosing-radius minimizers.

## 4. Actual six-point replacement: the radius stays fixed while diameter falls

Take the regular unit hexagon, with axial triangular-lattice coordinates

$$
(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1),
$$

where the physical basis is `(1,0),(1/2,sqrt(3)/2)`. The source is triangle-free,
has six unit contacts, diameter two, and minimum enclosing radius one.

No six unit-separated points can fit in a disk of radius `r<1`. Indeed, unless a
point is its center (which already puts that point at distance less than one from
all others), order the six polar angles. One consecutive angle is at most `pi/3`.
If the two radii are `a,b<=r`, their squared distance is at most

$$
a^2+b^2-ab\le r^2<1.
$$

The middle inequality follows by maximizing the separately convex function
`a^2+b^2-ab` on `[0,r]^2`: its four corner values are `0,r^2,r^2,r^2`.
This proves `r(6)=1` without a literature import.

Now replace the entire source by the center together with the vertices of a
regular pentagon of circumradius one. This is the existing six-point fixture in
`docs/problem/literature_baseline.md`, not a newly discovered packing. Its role
here is to distinguish a genuine planar replacement from the obstructed global
mechanisms. All five center-to-rim distances are one.
The squared rim distances are

$$
\frac{5-\sqrt5}{2}>1,
\qquad
\frac{5+\sqrt5}{2}<4.
$$

Thus the complete six-point endpoint is unit-separated and has

$$
\operatorname{diam}Q=\sqrt{\frac{5+\sqrt5}{2}}<2.
\tag{8}
$$

Its contact graph is `K_{1,5}`, so this strict competitor is itself triangle-free.
The pentagon surrounds the center; no smaller disk contains it, since its vertices
sum to zero and their average squared distance from any center `c` is `1+|c|^2`.
Hence `R(Q)=1`.

The old hexagon has the balanced-incidence certificate from
`global_factorized_distance_barrier_2026-10-12.md`, so no factorized-distance map
can obtain (8). It also has the enclosing-radius obstruction above, so no endpoint
certified through (6) can obtain (8). Nevertheless an actual planar replacement
shortens its diameter. The obstruction is a property of the proposed mechanisms,
not evidence of global diameter optimality.

## 5. Exact checks and limitations

Run `python3 research/verify_global_planarity_and_radius_barriers.py`.
The checker verifies centered Gram rank and every virtual lower and upper pair
for the unit square and the unit hexagon at three positive rational interpolation
parameters. It checks every old hexagon pair in rational axial arithmetic and every
pentagon-plus-center pair in `Q(sqrt(5))`. It verifies that both finite contact
graphs are triangle-free and that the endpoint diameter is strictly smaller.

The all-`t`, all-`n` rank theorem and enclosing-radius theorem are proved analytically.
The finite checker does not prove a planar realization of (2), global diameter
optimality of either fixture, or Level I.

## 6. Frontier effect

**Promotion recommendation:** unreviewed research checkpoint; no canonical state
change.

The whole-source search now has two explicit requirements for a viable new bridge:

1. it must produce actual planar coordinates, rather than stop at convex distance
   data or an affine spectral projection;
2. it must control the actual maximum distance, allowing boundary rearrangement
   that retains enclosing radius when necessary.

Neither requirement narrows to a special Target C chart or contact component.
The open obligation remains a same-cardinality strict diameter competitor for
every sufficiently large triangle-free global source, or an exact unit triangle.

## Autonomous audit (2026-10-15)

The [PR #960 AI proof audit](../audits/pr960_autonomous_proof_audit_2026-10-15.md)
records the full argument, dependencies and computational repairs. The checkers
require assertions and refuse optimized Python. This remains noncanonical;
the destination independent exact-head AI-agent mathematical audit required for consequential promotion is not completed.
