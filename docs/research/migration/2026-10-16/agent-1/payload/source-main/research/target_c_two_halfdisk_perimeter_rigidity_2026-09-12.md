# Target C — two-half-disk perimeter rigidity

**Date:** 2026-09-12  
**Status:** proof-only Type-II strengthening; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

The two-half-disk alternative gives more than the transport floor used in the
preceding global-boundary reduction. Each dominant strict-rhombus union is contained
in a Euclidean half-disk and misses only `o(D^2)` area. Finite-perimeter lower
semicontinuity therefore forces its physical boundary to have at least the perimeter
of that half-disk.

The candidate implication chain is

```text
half-disk containment + area saturation
  -> L1 convergence of each rhombus union to a half-disk
  -> lower semicontinuity of perimeter
  -> two-group physical boundary >= (2+pi)D
  -> global source ledger: (q-k)+2f >= (1+pi/2)D.
```

This is a source-level boundary strengthening, not a C-II closure.

## 1. Perimeter rigidity for one group

Let `K_{i,D}` be one of the two closed half-disks of radius `D/2` in the audited
two-half-disk alternative, and let `E_{i,D}` be the union of all closed strict
rhombi assigned to that group. The audited group decomposition supplies

\[
E_{i,D}\subseteq K_{i,D},
\qquad
\operatorname{area}(E_{i,D})
=\left(\frac{\pi}{8}-o(1)\right)D^2.
\tag{1.1}
\]

Since `area(K_{i,D})=pi D^2/8`, containment gives

\[
|K_{i,D}\mathbin{\triangle}E_{i,D}|=o(D^2).
\tag{1.2}
\]

Apply an isometry and scale by `D`. The normalized sets converge in `L^1` to the
unit-radius-`1/2` half-disk. Each `E_{i,D}` is a finite union of unit-edge rhombi,
hence a bounded finite-perimeter set. Lower semicontinuity of perimeter under `L^1`
convergence gives

\[
\liminf_{D\to\infty}\frac{\operatorname{Per}(E_{i,D})}{D}
\ge
\operatorname{Per}(K_{i,D}/D)
=1+\frac{\pi}{2}.
\tag{1.3}
\]

Let `P_{i,D}` be the occurrence-counted physical boundary-edge number used by the
two-half-disk transport theorem. Internal shared rhombus edges are removed from the
boundary, while every remaining unit edge has length one. At vertex pinches or
coincident boundary occurrences, the occurrence count is no smaller than the reduced
topological perimeter. Consequently

\[
P_{i,D}\ge\operatorname{Per}(E_{i,D}),
\tag{1.4}
\]

and therefore

\[
\boxed{
P_{i,D}\ge\left(1+\frac\pi2-o(1)\right)D.
}
\tag{1.5}
\]

No smoothness, connectedness, or disk-equality uniqueness is used. Holes and
edge-connected components only increase finite perimeter.

## 2. Two groups and the cross-cell edge audit

Adding (1.5) for the two complementary half-disks gives

\[
P_{1,D}+P_{2,D}\ge(2+\pi-o(1))D.
\tag{2.1}
\]

The independently audited cross-cell lemma says that strict rhombi with different
harmonic-cell labels cannot share a full edge: an unloaded endpoint would identify the
unloaded components, and a loaded-loaded endpoint pair is a force-hull side under
Type-II `c_B=0`, so it cannot border two bounded faces. Thus every selected-group
boundary occurrence is a physical boundary occurrence of the complete strict-rhombus
complex. With `P_{R,D}` denoting that full physical boundary,

\[
P_{1,D}+P_{2,D}\le P_{R,D}.
\tag{2.2}
\]

The full boundary is charged by the global outer walk and bounded nonquadrilateral
faces:

\[
P_{R,D}\le b_D+4f_D+Q_D.
\tag{2.3}
\]

Type-II loaded-hull accounting gives `b_D+Q_D=2(q_D-k_D)`. Hence

\[
\boxed{
2(q_D-k_D)+4f_D\ge(2+\pi-o(1))D,
}
\tag{2.4}
\]

or, equivalently,

\[
\boxed{
\frac{q_D-k_D}{D}+2\frac fD
\ge1+\frac\pi2-o(1).
}
\tag{2.5}
\]

Since `T_D=q_D+2f_D-k_D`, this is also

\[
\boxed{T_D/D\ge1+\frac\pi2-o(1).}
\tag{2.6}
\]

## 3. Why this does not yet close C-II

The new floor is strictly stronger than `2+gamma=2.2104468...` from the previous
transport estimate. It is still weaker than the current two-half-disk stopped-train
floor after the available loaded-density lower bounds are inserted. In particular,
the result does not upper-bound `f`, the aggregate detour, the exceptional-face
payment, or the source replacement cost. It also does not address the Type-I
macroscopic-container branch.

The remaining closure target is unchanged: a geometric correlation must turn this
boundary demand into a contradiction, an exact unit triangle, or a source-preserving
strict diameter decrease.

## 4. Scope and classification

- The half-disk area saturation and cross-cell edge localization are used only at
  their audited-working proof-only scopes.
- The perimeter step is an elementary finite-perimeter argument; it does not invoke
  equality uniqueness for disk packing.
- Every physical boundary edge is counted by occurrence, and contact-isolated source
  points are irrelevant to the rhombus-union perimeter calculation and remain in the
  full source.
- No theorem-state file is changed.

**Classification:** proved candidate awaiting promotion; proof-only.
