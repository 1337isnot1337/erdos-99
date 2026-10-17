> Generated reading edition · [exact source](../../../docs/audits/target_c_local_quarter_fold_hull_cover_independent_audit_2026-10-09.md) · source SHA-256 `f9cd28d4b5a5f6f600e0ddfb7428ed60ede44d11382184ee1fd70fcfef2d8b5a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E8A1FC1E0477","canonical":true,"claim_ids":["C-QUARTER-FOLD-TRANSFORMED-EIGHT-FACE-HULL-COVER"],"claim_statuses":{"C-QUARTER-FOLD-TRANSFORMED-EIGHT-FACE-HULL-COVER":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: local hull cover for an integrated eight-face fold

**Date:** 2026-10-09. **Audit:** 228.
**Audit base:** `origin/main=a6823f7de5b1f5fbd257f591ac2f025193e53e06`, state `2026-10-09.audit.221`.
**Frozen source:** `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`.
**Source report:** `docs/reports/target_c_small_convex_contact_face_quarter_fold_exclusion_2026-10-09.md`, SHA-256 `ec4bb6ac4e7c6096d7921074d1326c6ec55494d422d67cbff976637c55802f23`, Sections 5.5 and 7.3.

## Verdict

**PASS — broaden the canonical `C-QUARTER-FOLD-TRANSFORMED-EIGHT-FACE-HULL-COVER` scope to boundary-local endpoint feasibility.** The previous audit's conclusion is correct, but its stated hypothesis that all other source labels stay fixed is stronger than the geometry needs. In Section 7.3 the rest of the contact core moves, so that older scope cannot be invoked directly. The proof below uses only the old convex face and the transformed positions of its eight boundary labels.

## Exact broadened statement

Let a finite unit-separated source contain a simple convex actual eight-sided unit-contact face `F` with cyclic labels `p_i` and unit edge vectors `q_i=p_{i+1}-p_i`. Give its boundary a nonconstant face-closed quarter-fold sign pattern `s_i∈{−1,+1}` with four two-edge arcs and four transition corners, so `sum_i s_iq_i=0`; the folded labels `U_i` satisfy `U_{i+1}-U_i=s_iJq_i` for `J(x,y)=(-y,x)`. Let `alpha,beta>=0` be the outward deflection angles of the two pairs of arcs. Assume only that the eight folded boundary labels are unit-separated and triangle-free; the other source labels may move and are not constrained by this local statement. Let `H` be their convex hull.

Every point of `H` is within distance at most one of a transformed boundary label. If the two arc-deflection angles are `alpha,beta` and `alpha+beta>0`, every point of `H` is within distance strictly less than one of a transformed boundary label. Thus `H` contains no strict unit-clear slot for a contact isolate; in the bowed case it contains no unit-separated insertion at all.

## Independent reconstruction

### Turn interval from local boundary feasibility

Let `tau` be the old exterior turn at a transition corner. The two old unit edges incident to it have nonconsecutive endpoints on the actual convex face, so their chord is strictly longer than one: a unit chord would be an actual contact drawn inside and splitting that face. Since the chord length is `2cos(tau/2)`, this gives `tau<2pi/3`.

At a sign transition the folded exterior turn is the supplementary angle `pi-tau`. Its two incident transformed edges are still unit. Unit separation requires their opposite chord to be at least one; equality would make the two edges and chord an equilateral triangle, forbidden by the local triangle-free hypothesis. Thus `2cos((pi-tau)/2)>1`, or `tau>pi/3`.

By `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION`, the four transition vertices form the inscribed parallelogram. Write `alpha,beta>=0` for the outward deflections of its two-edge unit arcs, so their chords have lengths `2cos(alpha)` and `2cos(beta)`. Let `gamma` be the angle between the two adjacent chord directions. At a transition, the incident face-edge directions differ from the corresponding chord directions by the adjacent arc deflections; subtracting those deflections from the alternating parallelogram turns gives old transition turns `gamma-(alpha+beta)` and `pi-gamma-(alpha+beta)`. With `s=alpha+beta`, the two strict turn bounds therefore imply

```math
s<\pi/6,\qquad \pi/3+s<\gamma<2\pi/3-s.
\tag{1}
```

Only old-face and transformed-boundary pairs were used here; no position of an outside source label was held fixed.

### Transformed hull and disk cover

Undo the common quarter-turn and put `c_alpha=cos(alpha)`, `s_alpha=sin(alpha)`, with the corresponding notation for `beta`. For unit chord directions `u,v` at angle `gamma`, the four transformed transition corners are

```math
\pm c_\alpha u\;\pm c_\beta v.
```

The other four transformed labels are `+x,-x,+y,-y`, with

```math
x=c_\alpha u+s_\beta Jv,
\qquad y=c_\beta v-s_\alpha Ju.
```

In the basis `u,v`,

```math
x=(c_\alpha-s_\beta\csc\gamma)u+(s_\beta\cot\gamma)v,
\quad
y=(s_\alpha\cot\gamma)u+(c_\beta-s_\alpha\csc\gamma)v.
```

By (1), `alpha,beta<pi/6`, `sin(gamma)>sqrt(3)/2`, and `|cot(gamma)|<1/sqrt(3)`. Hence

```math
0<c_\alpha-s_\beta\csc\gamma<c_\alpha,
\qquad |s_\beta\cot\gamma|<c_\beta,
```

and symmetrically for `y`. Thus all four middle labels lie strictly inside the corner parallelogram `P=conv{+/-c_alpha u +/-c_beta v}`, so `H=P`.

The cells used below are in the claimed cyclic order, not just contained in `P`. Write `C_{++}=c_alpha u+c_beta v`, `C_{-+}=-c_alpha u+c_beta v`, and `C_{+-}=c_alpha u-c_beta v`. Direct cross-product expansion gives

```math
x\times C_{++}=c_\alpha\sin(\gamma-\beta)-c_\beta\sin\beta,\qquad
C_{++}\times y=c_\beta\sin(\gamma-\alpha)-c_\alpha\sin\alpha,
```
```math
y\times C_{-+}=c_\beta\sin(\gamma+\alpha)-c_\alpha\sin\alpha,\qquad
C_{+-}\times x=c_\alpha\sin(\gamma+\beta)-c_\beta\sin\beta.
```

Each is positive: all four angles `gamma±alpha` and `gamma±beta` lie strictly in `(pi/3,2pi/3)`, so the first product in each expression exceeds `3/4`, while the subtracted term is below `1/2`. Together with central symmetry these signs place the rays in the order `x,C_{++},y,C_{-+},-x,C_{--},-y,C_{+-}`. Hence the central diamond, the four transition-corner triangles, and the four side pockets form a noncrossing triangulation of `P`.

The middle labels form a nondegenerate central diamond because

```math
x\mathbin\times y=\cos(\alpha-\beta)\{\sin\gamma-\sin(\alpha+\beta)\}>0.
```

Their squared radii are

```math
|x|^2=c_\alpha^2+s_\beta^2-2c_\alpha s_\beta\sin\gamma,
\qquad
|y|^2=c_\beta^2+s_\alpha^2-2c_\beta s_\alpha\sin\gamma.
```

Both are at most one. For example, if `beta>0`, then `s_beta<2c_alpha sin(gamma)`, so the beta terms in `|x|^2` have negative sum; if `beta=0`, `|x|^2=c_alpha^2`. The symmetric argument handles `y`. If `alpha+beta>0`, both radii are strictly below one.

For any convex combination `p=sum lambda_i v_i` of points `v_i` in a radius-`r` disk centered at zero,

```math
\sum_i\lambda_i|p-v_i|^2=\sum_i\lambda_i|v_i|^2-|p|^2\le r^2.
```

Therefore the central diamond is covered by the radius-`r` disks centered at its four middle labels, with `r<=1` and `r<1` when bowed.

The parallelogram partitions into this central diamond, four corner triangles, and four side pockets. Each corner triangle has two unit sides and included angle equal to an old transition turn `tau in (pi/3,2pi/3)`. Its circumradius is `1/(2cos(tau/2))<1`; the same variance identity covers it strictly by disks centered at its three boundary labels. A side pocket with positive deflection `alpha` lies in the disk of radius `cos(alpha)<1` about its chord midpoint, since its corner vertices are at radius `cos(alpha)` and its middle vertex at radius `sin(alpha)`. At zero deflection the pocket degenerates to a segment of length two divided at its retained middle label, so every point is within `1/2` of a boundary label. The four pieces prove the claimed weak cover, and the cover is strict everywhere when `alpha+beta>0`.

## Hostile scope and limits

- **Moving outside core:** the earlier full-endpoint theorem fixed all other labels. Its hypothesis is not supplied by a simultaneous integrated core move; the local boundary derivation above removes that mismatch.
- **Triangle equality:** a transformed two-step chord of length exactly one creates a unit triangle, so the strict turn bound uses triangle-freeness as well as lower feasibility.
- **Actual face:** old nonconsecutive face vertices cannot have a unit chord through a simple convex actual face. A generic convex octagon with extra unit chords is outside scope.
- **No source-wide capacity:** the theorem gives no placement for an isolate outside `H`, no full endpoint, no diameter upper bound, and no global-minimality or C-II conclusion.

## Dependencies and application boundary

The only canonical theorem dependency is `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION`, which supplies the transition parallelogram from the local boundary fold. The old Audit.224 dependency on `C-QUARTER-FOLD-EIGHT-FACE-AREA-LOWER-BOUND` is not needed: the turn window is derived here from old actual-face chords and transformed boundary feasibility. No finite verifier encodes the angle and cover proof. All steps are finite exact geometry; no numerical tolerance or continuity claim is used.

This audit proves the cover for four arcs with two edges apiece. It does not broaden `C-QUARTER-FOLD-MINIMUM-FACE-SIZE` from its full-endpoint scope to a boundary-local endpoint, so applying this cover to every nonconstant face of a simultaneous integrated core fold still requires the two-edge-arc pattern to be established under that local scope.
