> Generated reading edition · [exact source](../../../docs/audits/target_c_quarter_fold_transformed_hull_cover_independent_audit_2026-10-09.md) · source SHA-256 `a648f9fd8dad383c3e8407387993bacf0b3a9c3f93bfc05dbf11618da1397507`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8AEA59D1F9F7","canonical":true,"claim_ids":["C-QUARTER-FOLD-TRANSFORMED-EIGHT-FACE-HULL-COVER"],"claim_statuses":{"C-QUARTER-FOLD-TRANSFORMED-EIGHT-FACE-HULL-COVER":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: transformed hull of an endpoint-feasible eight-face fold

**Date:** 2026-10-09. **Audit:** 224.
**Audit base:** `origin/main=31c71068c57ea39e83f378ed7a417fc707e97ba5`, state `2026-10-09.audit.217`.
**Frozen source:** `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`.
**Source report:** `docs/reports/target_c_small_convex_contact_face_quarter_fold_exclusion_2026-10-09.md`, SHA-256 `ec4bb6ac4e7c6096d7921074d1326c6ec55494d422d67cbff976637c55802f23`, Section 5.5.

## Verdict

**PASS — promote `C-QUARTER-FOLD-TRANSFORMED-EIGHT-FACE-HULL-COVER`.** The transformed boundary hull has no strict unit-clear slot. If either pair of two-edge arcs bows, every point in the hull is strictly within distance one of a boundary vertex, so it contains no unit-separated insertion at all. This does not bound capacity outside the hull or force a full-source endpoint.

## Exact audited statement

Let a finite unit-separated source have a simple convex actual eight-sided unit-contact face. Take a nonconstant face-closed quarter-fold of its boundary labels, retain every other source label, and assume the full endpoint is unit-separated and triangle-free. Let `H` be the convex hull of the eight transformed boundary labels. For the parameters from `C-QUARTER-FOLD-EIGHT-FACE-AREA-LOWER-BOUND`, `alpha,beta >= 0`, `alpha+beta < pi/6`, and `pi/3+alpha+beta < gamma < 2pi/3-alpha-beta`.

Every point of `H` is at distance at most one from at least one of the eight boundary labels. If `alpha+beta>0`, every point is at distance strictly less than one from at least one boundary label. Hence no point in `H` can hold a contact-isolated label while preserving the old contact graph: such a label requires strict distance greater than one from each boundary label. In the bowed case, no new label can be inserted anywhere in `H` while preserving unit separation, even if a new contact were allowed.

## Independent reconstruction

Undo the common quarter-turn and let `u,v` be unit chord directions with angle `gamma`. Write `c_alpha=cos(alpha)`, `s_alpha=sin(alpha)`, and similarly for `beta`. The four transformed transition corners are

```math
\pm c_\alpha u\;\pm c_\beta v.
```

The other four transformed vertices are `+x,-x,+y,-y`, where

```math
x=c_\alpha u+s_\beta Jv,\qquad
y=c_\beta v-s_\alpha Ju.
```

In the basis `u,v` these become

```math
x=(c_\alpha-s_\beta\csc\gamma)u+(s_\beta\cot\gamma)v,
\qquad
y=(s_\alpha\cot\gamma)u+(c_\beta-s_\alpha\csc\gamma)v.
```

The parameter interval gives `alpha,beta < pi/6` and `pi/3 < gamma < 2pi/3`, hence `sin(gamma)>sqrt(3)/2`, `|cot(gamma)|<1/sqrt(3)`, and `c_alpha,c_beta>sqrt(3)/2`. It follows that

```math
0<c_\alpha-s_\beta\csc\gamma<c_\alpha,
\qquad |s_\beta\cot\gamma|<c_\beta,
```

and symmetrically `0<c_beta-s_alpha csc(gamma)<c_beta` and `|s_alpha cot(gamma)|<c_alpha`. Thus all four middle vertices lie strictly inside the parallelogram `P=conv{+/- c_alpha u +/- c_beta v}`. The transformed hull `H` is exactly `P`.

The four middle vertices form a nondegenerate central diamond because

```math
x\mathbin\times y
=\cos(\alpha-\beta)\{\sin\gamma-\sin(\alpha+\beta)\}>0.
```

This diamond, the four corner triangles, and the four side pockets between a chord side of `P` and its middle vertex partition `P`.

Use the following covering fact. If points `v_i` lie in a disk of radius `r` about `o`, then their convex hull is covered by their radius-`r` disks. For `p=sum(lambda_i v_i)` with nonnegative coefficients summing to one,

```math
\sum_i\lambda_i|p-v_i|^2
=\sum_i\lambda_i|v_i-o|^2-|p-o|^2\le r^2,
```

so at least one `v_i` is within distance `r` of `p`. If `r<1`, the cover is strict.

For the central diamond, direct expansion gives

```math
|x|^2=c_\alpha^2+s_\beta^2-2c_\alpha s_\beta\sin\gamma,
\qquad
|y|^2=c_\beta^2+s_\alpha^2-2c_\beta s_\alpha\sin\gamma.
```

Both are at most one. If `alpha+beta>0`, both are strictly below one: for `beta>0`, `sin(beta)<2c_alpha sin(gamma)` because the right side is greater than `3/2` while `sin(beta)<1/2`; the expression for `|x|^2-1` is then `-s_alpha^2+s_beta(s_beta-2c_alpha sin(gamma))<0`. If `beta=0<alpha`, `|x|^2=c_alpha^2<1`. The argument for `y` is symmetric. The covering fact therefore gives a weak unit cover of the diamond, and a strict cover whenever it bows.

Each corner triangle has two unit sides. Its included angle and its supplement lie in `(pi/3,2pi/3)`, since both the old and folded transition turns lie in that interval. Its circumradius is `1/(2 cos(theta/2))<1`; the covering fact gives a strict unit cover of the whole triangle.

For a side pocket with parameter `alpha`, its chord endpoints are at distance `c_alpha` from the chord midpoint, and its bowed middle vertex is at distance `s_alpha` from that midpoint. Since `alpha<pi/6`, the pocket is inside the radius-`c_alpha` disk. If `alpha>0`, this radius is less than one. If `alpha=0`, the pocket is a length-two segment with its retained midpoint, so every point is within `1/2` of a boundary vertex. The beta pockets obey the same argument.

Combining these nine pieces proves weak coverage everywhere, with strict coverage on all pieces except possibly the central diamond when both deflections vanish. In that remaining case, weak coverage still forbids a strict source slot.

## Regression and scope checks

- The report's rational eight-cycle plus isolate is a valid finite unit-separated source at the stated coordinates: after scaling by `41`, the isolate `(40,40)` has squared distances `2401` to each of the four middle vertices and `3200` to each corner, all greater than `41^2`. This verifies only the example's isolate status.
- No finite script encodes the analytic hull-cover argument. The exact arithmetic above does not prove the covering theorem.
- The result concerns the prescribed transformed boundary hull. A contact-isolated source label must be relocated outside this hull if the old contact graph is retained, but the audit proves no capacity or feasibility statement for other faces, exterior pockets, or simultaneous relocations.
- No global-minimality, KKT, stress, upper-diameter, or C-II closure claim is made.

## Dependencies and frontier effect

Dependencies are canonical `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION`, `C-QUARTER-FOLD-MINIMUM-FACE-SIZE`, and `C-QUARTER-FOLD-EIGHT-FACE-AREA-LOWER-BOUND`. The theorem adds a local no-slot obstruction for an already endpoint-feasible eight-face fold. It creates no fold, does not control relocation outside `H`, and changes no C-II route obligation.
