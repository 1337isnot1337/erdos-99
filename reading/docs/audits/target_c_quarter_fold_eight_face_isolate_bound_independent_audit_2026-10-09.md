> Generated reading edition · [exact source](../../../docs/audits/target_c_quarter_fold_eight_face_isolate_bound_independent_audit_2026-10-09.md) · source SHA-256 `e2c585702621d87d15276f36536df494922af288acb3ea506fffb7f88ebdec4a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-778BC219F537","canonical":true,"claim_ids":["C-PARALLELOGRAM-UNIT-GUARD-CENTER-BOUND","C-QUARTER-FOLD-EIGHT-FACE-ISOLATE-BOUND"],"claim_statuses":{"C-PARALLELOGRAM-UNIT-GUARD-CENTER-BOUND":"canonical","C-QUARTER-FOLD-EIGHT-FACE-ISOLATE-BOUND":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: guarded parallelograms and eight-face isolate count

**Date:** 2026-10-09. **Audit:** 225.
**Audit base:** `origin/main=31c71068c57ea39e83f378ed7a417fc707e97ba5`, state `2026-10-09.audit.217`.
**Frozen source:** `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`.
**Source report:** `docs/reports/target_c_small_convex_contact_face_quarter_fold_exclusion_2026-10-09.md`, SHA-256 `ec4bb6ac4e7c6096d7921074d1326c6ec55494d422d67cbff976637c55802f23`, Sections 5.6.1–5.6.2.

## Verdict

**PASS — promote `C-PARALLELOGRAM-UNIT-GUARD-CENTER-BOUND` and `C-QUARTER-FOLD-EIGHT-FACE-ISOLATE-BOUND`.** The first is a standalone finite packing lemma. The second says an actual bounded convex eight-sided contact face carrying an endpoint-feasible nonconstant quarter-fold has at most one contact-isolated source point in its interior. No global source-population payment follows.

## Claim 1: guarded parallelogram center bound

Let `P` be a nondegenerate parallelogram with side vectors of lengths at most `sqrt(3)`, and let `K` be the set of points of `P` at distance at least one from all four vertices. Then `K` is contained in the closed disk of radius `1/2` about the center of `P`. The strict-clearance set, where all four distances are greater than one, is contained in the open radius-`1/2` disk. Consequently `diam(K)<=1`, and the strict-clearance set has diameter `<1`.

### Proof

Write the side-vector Gram matrix as `G`. Replace it by

$$
G'=\begin{pmatrix}3&a\cdot b\\a\cdot b&3\end{pmatrix}.
$$

Because `P` is nondegenerate and `|a|,|b|<=sqrt(3)`, `G'` is positive definite. The difference `G'-G` is diagonal positive semidefinite. The linear map taking the original side vectors to vectors with Gram matrix `G'` therefore expands every distance. It maps `P` to a rhombus of side `sqrt(3)`, preserves the center and convex coefficients, and sends weak or strict unit-clear points to weak or strict unit-clear points. A center-radius bound in the rhombus pulls back to at least as strong a bound in `P`.

Use this covering identity: if vertices `v_i` lie in a radius-`r` disk centered at `o`, and `p=sum(lambda_i v_i)` is a convex combination, then

$$
\sum_i\lambda_i|p-v_i|^2
=\sum_i\lambda_i|v_i-o|^2-|p-o|^2\le r^2.
$$

At least one vertex is therefore within distance `r` of `p`; if `r<1`, the cover is strict. Represent the rhombus vertices as `(+-A,0),(0,+-B)`, with `A,B>0` and `A^2+B^2=3`. If `A>3/2`, triangulate along the `B` diagonal. Each triangle has circumradius `3/(2A)<1`; the identity covers both triangles strictly by unit disks about their vertices. Thus `K` is empty. The case `B>3/2` is symmetric.

Otherwise `A^2,B^2` lie in `[3/4,9/4]`, so `A^2B^2>=27/16`. Reflect a weak-clear point to `p=(x,y)` with `x,y>=0`, and put `chi=x/A`, `psi=y/B`. Since `p` lies in the rhombus, `chi+psi<=1`. If `chi>=1/2`, then

$$
|p-(A,0)|^2
=A^2(1-\chi)^2+B^2\psi^2
\le 3(1-\chi)^2\le3/4<1,
$$

contrary to weak clearance. Likewise `psi<1/2`.

Give the vertices `(A,0),(-A,0)` weights `1/4+chi/2,1/4-chi/2`, and `(0,B),(0,-B)` weights `1/4+psi/2,1/4-psi/2`. These weights are nonnegative, sum to one, and have barycenter `p`. The variance identity gives

$$
1\le\sum_i\lambda_i|p-v_i|^2
=\sum_i\lambda_i|v_i|^2-|p|^2
=3/2-t,
\qquad t=x^2+y^2,
$$

so `t<=1/2`.

Clearance from `(A,0)` and `(0,B)` also gives

$$
x\le\frac{t+A^2-1}{2A},
\qquad
y\le\frac{t+B^2-1}{2B}.
$$

The right sides are nonnegative for a feasible point. Squaring and adding, then using `A^2+B^2=3`, yields

$$
4t\le4t-1+\frac{3(t-1)^2}{A^2B^2}.
$$

Since `t<=1/2` and `A^2B^2>=27/16`, this implies

$$
t\le1-\sqrt{A^2B^2/3}\le1/4.
$$

If `A^2B^2>27/16`, this gives a uniform radius bound strictly below `1/2`, so the weak-clearance set has diameter strictly below one. In the equality case `A^2B^2=27/16`, the conditions `A^2+B^2=3` imply `{A^2,B^2}={3/4,9/4}`. The weak-clearance inequality from the shorter-axis vertices forces `t-2A|x|>=1/4`; combined with `t<=1/4`, this gives `x=0`, `t=1/4`, and `y=+/-1/2` (or the swapped case). These weak-clearance points are exactly distance one from a long-axis vertex, so no point is strictly clear of all four vertices. Therefore the strict-clearance set is empty in the equality case. For nonempty strict-clearance sets, the preceding estimate gives a uniform radius below `1/2`; their diameter is strictly below one. In the original parallelogram, distance contraction under the inverse linear map preserves both pairwise bounds.

This equality-case argument is necessary: mere containment in an open disk of radius `1/2` would give pairwise distances `<1` but would not by itself imply that the supremum diameter is `<1`.

## Claim 2: at most one isolate in an active eight-face

Let a finite unit-separated source have a simple bounded convex actual eight-sided unit-contact face `F`. Suppose a nonconstant face-closed quarter-fold of its boundary labels, retaining every other source label, has a full unit-separated triangle-free endpoint. Then the interior of `F` contains at most one contact-isolated source point.

### Proof

By `C-QUARTER-FOLD-MINIMUM-FACE-SIZE`, the four transition arcs each have two unit edges. The four transition corners form the inscribed parallelogram of `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION`. Write its adjacent unit chord directions as `u,v`, with the deflections `alpha,beta` from `C-QUARTER-FOLD-EIGHT-FACE-AREA-LOWER-BOUND`. That theorem gives `alpha+beta<pi/6` and `pi/3+alpha+beta<gamma<2pi/3-alpha-beta`.

Opposite two-edge arcs have equal chord lengths, hence equal midpoint heights; convexity places their midpoint offsets on opposite sides of the transition parallelogram. Their four middle vertices therefore occur in opposite pairs about its center. To check the resulting central parallelogram is nondegenerate, its two representative half-diagonals may be written, up to the cyclic orientation, as

$$
m_u=\cos\beta\,v+\sin\alpha\,Ju,
\qquad
m_v=\cos\alpha\,u-\sin\beta\,Jv.
$$

Their cross product is

$$
m_v\mathbin\times m_u
=\cos(\alpha-\beta)\sin\gamma
+\sin\alpha\cos\alpha+\sin\beta\cos\beta>0.
$$

At each transition corner let `theta` be the old exterior turn. Endpoint unit separation and triangle-freeness force `theta>pi/3`; the old two-step chord between nonconsecutive actual face vertices has length `2cos(theta/2)>1`, so `theta<2pi/3`. The side of the middle parallelogram across that corner is exactly this chord, and hence has length `2cos(theta/2)<sqrt(3)`. All four sides meet the hypotheses of Claim 1.

The old face partitions into the middle parallelogram and four corner triangles. Each corner triangle has two unit sides and included angle `pi-theta`, which is also in `(pi/3,2pi/3)`. Its circumradius is `1/(2cos((pi-theta)/2))<1`, so the convex-hull covering identity places every point of that triangle strictly within one of its three boundary vertices. A contact-isolated source point has strict distance greater than one from every source vertex and therefore lies in none of the four corner triangles.

Any such isolate must lie in the middle parallelogram, strictly clear of its four middle-vertex guards. Claim 1 puts all such points in one open disk of radius `1/2`. Two points in that disk would be less than one apart, contradicting source unit separation. Thus there is at most one.

## Adversarial scope and frontier effect

- The parallelogram lemma handles equality cases `A=3/2` or `B=3/2` in its algebraic branch; the strict branch is used only when all four guards are strictly clear. At `A^2=3/4`, `B^2=9/4`, the exact points `(0,+/-1/2)` are weak-clear and are one unit apart, while each has distance exactly one to a long-axis vertex. Thus the weak diameter bound is sharp and the strict-clear set is empty at the equality parameter.
- The face theorem counts only contact-isolated labels in the interior of the stated actual bounded face. It does not count isolates assigned elsewhere or give a bound on the number of active eight-faces.
- The corner-triangle exclusion uses strict clearance of a contact isolate from every face boundary label; equality at distance one would make it a contact and violate isolation.
- The rational eight-cycle plus the isolate `(40/41,40/41)` from source Section 5.5 gives a finite `z=1` example: exact scaled squared distances are `2401` to each middle vertex and `3200` to each corner, all greater than `41^2`. The eight-cycle's complete contact ledger was independently checked in Audit.222. This nonglobal example shows the one-isolate cap cannot be lowered to zero in this finite face scope.
- There is no finite verifier for the analytic parallelogram optimization. No script output is used as proof.
- Neither claim implies a source-wide isolate payment, any outside replacement slot, a finite move, a global-minimizer consequence, or C-II/Level-I closure.

Dependencies for Claim 1 are none. Claim 2 depends on canonical `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION`, `C-QUARTER-FOLD-MINIMUM-FACE-SIZE`, and `C-QUARTER-FOLD-EIGHT-FACE-AREA-LOWER-BOUND`, in addition to Claim 1 above. The C-II endpoint is unchanged.
