> Generated reading edition · [exact source](../../../docs/audits/target_c_one_pin_restoration_gap_capacity_plateau_independent_audit_2026-10-10.md) · source SHA-256 `ce709b3988db6bae2b1deb5aacc0d5ed755e86bf7781e77e167e6203b0702f7c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-996A15A014C9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C Audit.253 — restored-pin gap and near-triangular capacity plateau

> **Publication lifecycle:** this is an unreviewed proposal from source PR #947.
> Its historical PASS/promote language requests a change; the current publication
> manifest does not grant the proposed promotion or stronger scope. Use the exact
> current manifest entry for any inherited canonical premise.


Date: 2026-10-10\
Audit base: origin/main ab6dd3336f9f8d440f2bada76edb32153391cddc, state 2026-10-10.audit.234\
Frozen source: origin/research/level-i-fused-review-20261009 at 6132201c1d3056ca68a222217094acb819f5b4d7\
Candidate: Sections 16 and 16.2 of docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md, SHA-256 2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd\
Status before audit: Section 16 labels the displacement statement a regression awaiting independent audit; Section 16.2 is an unpromoted finite capacity claim.

## Verdict

**PASS — promote two distinct finite results at their exact scopes.**

1. **Regression valid:** with the deleted boundary pin restored as a movable label, every feasible placement in the old closed parallelogram is either the reference placement or at maximum displacement at least $`a/(2(m+n+1))\ge\sqrt3/(4(m+n+1))`$. This differs from the canonical triangular one-pin regression, where that pin is deleted and only interior labels move.
2. **Capacity plateau valid:** for each fixed $`m,n\ge3`$, there is an $`\epsilon_{m,n}>0`$ such that for $`\pi/3<\phi<\pi/3+\epsilon_{m,n}`$, deleting boundary label $`p_{1,0}`$ leaves exactly $`K=(m-1)(n-1)`$ available sites in the open reference parallelogram, both for weak separation and for strict separation from each other and all retained boundary pins. The radius $`\epsilon_{m,n}`$ is not uniform in growing $`m,n`$.

Neither result extracts an oblique wall from a canonical source, counts points outside the fixed wall, or supplies a full-source move or C-II closure.

## Exact statements

Let $`m,n\ge3`$, $`L=m+n`$, $`u=(1,0)`$, $`v=(c,a)=(\cos\phi,\sin\phi)`$, with $`\pi/3\le\phi\le\pi/2`$. Let
```math
P_{m,n}(\phi)=\{s u+t v:0\le s\le m,\ 0\le t\le n\},\qquad p_{ij}=iu+jv.
```

**C-TRIANGULAR-ONE-PIN-RESTORATION-DISPLACEMENT-GAP-REGRESSION.** Keep every boundary label except $`p_{1,0}`$ fixed. Allow $`p_{1,0}`$ and all interior labels to move, require all movable labels to stay in the closed set $`P_{m,n}(\phi)`$, and require every pair of labels to remain at distance at least one. If $`\rho`$ is the maximum displacement among the movable labels, then
```math
\rho=0\quad\hbox{or}\quad \rho\ge\frac{a}{2(L+1)}\ge\frac{\sqrt3}{4(L+1)}.
```
Consequently every continuous feasible path from the full reference grid is constant. Distant feasible alternatives are not excluded.

**C-NEAR-TRIANGULAR-ONE-PIN-CAPACITY-PLATEAU.** Delete $`p_{1,0}`$, keep all other boundary labels fixed, and count additional points in the open parallelogram $`P_{m,n}(\phi)`$. Weak capacity requires mutual and boundary distances at least one; strict capacity requires them all greater than one. For each fixed $`m,n`$, there is some $`\epsilon_{m,n}>0`$ such that both capacities equal $`K=(m-1)(n-1)`$ whenever $`\pi/3<\phi<\pi/3+\epsilon_{m,n}`$. The boundary-pin model is artificial and finite; no global-minimizer assumption is part of this claim.

## Independent proof of the restored-pin displacement gap

For any original unit edge directed along a unit vector $`e`$, feasibility gives
```math
1\le|e+\xi_b-\xi_a|,\qquad
e\cdot(\xi_b-\xi_a)\ge-\tfrac12|\xi_b-\xi_a|^2\ge-2\rho^2.
```
Every horizontal interior row has two fixed endpoints. Summing along the row from each end gives $`|u\cdot\xi_{ij}|\le2m\rho^2`$. The restored pin has two fixed horizontal neighbors, so the two incident inequalities give the stronger $`|u\cdot\xi_{1,0}|\le\rho^2/2`$.

Because the restored pin remains in the closed parallelogram, its vertical displacement is nonnegative. Since $`0\le c\le1/2`$,
```math
v\cdot\xi_{1,0}=c(u\cdot\xi_{1,0})+a(\xi_{1,0})_y\ge-\rho^2/4.
```
Summing the vertical edge inequalities up column one from this pin and down from its fixed top endpoint gives
```math
-(2n+1)\rho^2\le v\cdot\xi_{1,j}\le2n\rho^2.
```
Every other interior column has fixed top and bottom endpoints and satisfies the same weaker absolute bound $`2n\rho^2`$.

The dual vectors to $`u,v`$ both have norm $`1/a`$. Hence each movable displacement satisfies
```math
|\xi_{ij}|\le\frac{|u\cdot\xi_{ij}|+|v\cdot\xi_{ij}|}{a}
\le\frac{2m+2n+1}{a}\rho^2
\le\frac{2(L+1)}{a}\rho^2.
```
Taking the maximum and dividing when $`\rho>0`$ proves the gap. The continuous-path statement follows because the maximum displacement is continuous and cannot take any value strictly between zero and this gap.

## Independent proof of the capacity plateau

Let $`K=(m-1)(n-1)`$, and suppose the weak capacity exceeded $`K`$ arbitrarily close to $`\phi=\pi/3`$. Choose $`\phi_j\downarrow\pi/3`$ and $`K+1`$ feasible additional points in the open parallelogram for each $`j`$. Together with the retained boundary pins they form
```math
N=2(m+n)-1+(K+1)=(m+1)(n+1)
```
unit-separated points in the closed reference parallelogram.

The four retained corners fix the convex hull as the full parallelogram. As $`j\to\infty`$, the parallelograms are uniformly bounded; compactness gives a limiting unit-separated $`N`$-point set in the triangular parallelogram. Its area is $`mn\sqrt3/2`$ and its perimeter is $`2(m+n)`$, so the normalized Thue–Groemer/Oler expression is exactly
```math
\frac{mn\sqrt3/2}{\sqrt3/2}+\frac{2(m+n)}2+1=(m+1)(n+1)=N.
```
Thus equality holds in the finite packing inequality.

The equality classification in Böröczky and Ruzsa, “Note on an inequality of Wegner,” page 2, says that in the two-dimensional case the convex hull of the centers is triangulated by regular triangles using all centers as vertices; their unit-disc normalization has center separation two, so scaling coordinates by one half gives unit equilateral triangles here. The limiting points therefore lie on one unit triangular lattice. The fixed corner and the hull side directions fix its phase and orientation. The lattice sites in this parallelogram are exactly the original $`(m+1)(n+1)`$ grid sites, so the $`K+1`$ targets converge, after a fixed finite relabeling subsequence, to the $`K`$ interior grid sites together with the missing boundary site $`p_{1,0}`$.

Assign the target converging to $`p_{1,0}`$ to the restored pin and the others to the interior labels. This is a feasible placement covered by the displacement-gap regression: all targets are in the open parallelogram, hence in its closure, and all pairwise distances are at least one. Its maximum displacement tends to zero. For large $`j`$, the gap forces displacement zero, putting the restored pin target at $`p_{1,0}`$ on the boundary, a contradiction. This proves weak capacity at most $`K`$.

The original $`K`$ interior grid sites give weak capacity at least $`K`$. For strict capacity, the canonical C-OBLIQUE-ONE-PIN-STRICT-REFILL gives $`K`$ targets strictly separated from every retained boundary label. Check target-target pairs as well. Put $`\delta=1-2\cos\phi>0`$. Every nonbasis difference of two grid sites has squared length at least $`1+\delta`$; the construction moves each target by less than $`\delta/(50L)`$, so each such pair remains at distance at least

```math
\sqrt{1+\delta}-\frac{\delta}{25L}
\ge 1+\delta\left(\frac13-\frac1{25L}\right)>1.
```

The only unit differences at these strict angles are $`\pm u,\pm v`$. Among target-target horizontal contacts, the stage-two contacts in columns at least two lengthen; the column-one/column-two interface starts stage two with squared excess at least $`s^2`$ and loses less than $`s^2/2`$. Among target-target vertical contacts, column one lengthens in stage one, while columns at least two gain the positive squared excess $`h^2(m-i)^2(f_j-f_{j-1})^2/a^2`$, with $`f_j-f_{j-1}\ne0`$. Thus every target pair is strictly separated. Strict capacity is at most weak capacity, so both capacities equal $`K`$ on a sufficiently small fixed-$`(m,n)`$ interval above $`\pi/3`$.

## Hostile scope and dependency checks

- The existing C-TRIANGULAR-ONE-PIN-DISPLACEMENT-GAP-REGRESSION deletes $`p_{1,0}`$; this new gap restores it as a movable label and includes its displacement in $`\rho`$. The two statements are not duplicates.
- The capacity theorem concerns only inserted sites inside a fixed open wall after one pin is deleted. It does not constrain sites outside the wall, changed walls, or positions of other source points.
- The strict lower bound uses C-OBLIQUE-ONE-PIN-STRICT-REFILL. Its upper bound uses the new restored-pin regression and the finite equality case; no global optimality premise is used.
- The literature statement was checked in the original 2007 manuscript. In its unit-disc normalization equality is characterized by a triangulation with all centers as vertices (or a segment); the four corners ensure this application is two-dimensional. No equality-uniqueness claim beyond that source is used.
- No finite verifier encodes the displacement or compactness/equality argument. The underlying exact verifier for Audit.187 does not test these universal claims.

**Canonical disposition:** register the displacement statement as a regression and the fixed-frame plateau as a finite canonical theorem. The displacement bound is proved in this same audit and used inside the compactness argument; the theorem manifest records the external C-OBLIQUE-ONE-PIN-STRICT-REFILL dependency. This narrows the restored one-pin local refill route only for fixed $`m,n`$ and sufficiently near-triangular angles. No arbitrary-wall extraction or C-II frontier closure follows.
