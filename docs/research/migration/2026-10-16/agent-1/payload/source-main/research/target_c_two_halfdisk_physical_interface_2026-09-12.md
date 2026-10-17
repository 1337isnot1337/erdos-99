# Target C — two-half-disk global physical-boundary floor

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only candidate; theorem-state authority unchanged.  
**Dependencies:** audited-working all-regime two-half-disk dichotomy, groupwise
strict-rhombus area localization, and physical-boundary two-arc transport.

The two-half-disk branch contains two quadratic strict-rhombus systems, each filling
one limiting half-disk. Applying the physical-boundary transport theorem to the two
systems separately produces a global physical-boundary floor. The Type-II cell-label
localization is strong enough to remove the provisional interface loss: strict rhombi
from different harmonic-cell groups cannot share a full contact edge.

The candidate implication chain is:

```text
two complementary half-disk groups
  -> two separate physical-boundary lower bounds
  -> no cross-cell rhombus-edge overlap
  -> a source-level global boundary/defect inequality.
```

This does not yet close the half-disk branch. It identifies the extra global boundary
payment after the groupwise atomic-train floor.

## 1. Group physical boundaries

Work along the finite diagonal supplied by the audited two-half-disk alternative. Let
`K_{1,D}` and `K_{2,D}` be the two closed half-disks of radius `D/2`, and let
`R_{i,D}` be the strict-rhombus subcomplex assigned to group `i`. Write `A_{i,D}` for
its rhombus area, `P_{i,D}` for its physical boundary-edge occurrence count, and
`rho_{i,j,D}` for the diameter of its `j`th edge-connected component.

The groupwise area theorem gives

\[
A_{i,D}=\left({\pi\over8}-o(1)\right)D^2,
\qquad i=1,2.
\tag{1.1}
\]

Each `R_{i,D}` lies in `K_{i,D}`, and the complement of `R_{i,D}` in `K_{i,D}` has
area `o(D^2)`. The projection-coverage lemma in the audited physical-boundary
transport theorem therefore gives

\[
\sum_j\rho_{i,j,D}\ge D-o(D).
\tag{1.2}
\]

Its finite component inequality, with ambient diameter `D`, is

\[
D\left(P_{i,D}-2\sum_j\rho_{i,j,D}\right)
>
(4-2\sqrt3)A_{i,D}.
\tag{1.3}
\]

Consequently

\[
\boxed{
P_{i,D}\ge
\left(2+{\pi\over8}(4-2\sqrt3)-o(1)\right)D.
}
\tag{1.4}
\]

Put

\[
\gamma:={\pi\over8}(4-2\sqrt3)
=0.210446803619233\ldots .
\tag{1.5}
\]

Then

\[
P_{1,D}+P_{2,D}\ge(4+2\gamma-o(1))D.
\tag{1.6}
\]

This is a separate application of physical-boundary transport; the two group
boundaries have not been identified with one global boundary.

## 2. Cross-cell rhombus edges are absent

The all-regime half-disk proof supplies the needed finite edge-label fact. If two
strict rhombi share an edge with an unloaded endpoint, their unloaded components are
connected through that endpoint, so the two rhombi have the same harmonic-cell label.
If both endpoints are loaded, the audited Type-II `c_B=0` localization makes the edge
a force-hull side; a force-hull side cannot have bounded strict-rhombus faces on both
sides. Therefore strict rhombi belonging to different harmonic-cell groups cannot
share an edge.

It follows that every boundary occurrence of either dominant group is a physical
boundary occurrence of the full strict-rhombus complex `R_D`. If `P_{R,D}` is its
physical boundary occurrence count, then

\[
\boxed{P_{1,D}+P_{2,D}\le P_{R,D}.}
\tag{2.1}
\]

The full physical boundary is contained in the occurrence-counted global outer walk
and bounded nonquadrilateral-face boundaries, so

\[
P_{R,D}\le b_D+4f_D+Q_D.
\tag{2.3}
\]

Canonical Type-II loaded-hull accounting gives

\[
b_D+Q_D=2(q_D-k_D).
\tag{2.4}
\]

Therefore the new source-level global boundary inequality is

\[
\boxed{
2{q_D-k_D\over D}+4{f_D\over D}
\ge4+2\gamma-o(1).
}
\tag{2.5}
\]

Equivalently, with `t_D=(q_D-k_D)/D`,

\[
\boxed{
t_D+2{f_D\over D}
\ge2+\gamma-o(1).
}
\tag{2.6}
\]

There is no residual interface term in (2.6): a residual strict-rhombus complex may
touch a dominant group only at vertices or through non-rhombus contact faces. The
remaining loss is in the upper estimate `P_R<=b+4f+Q`, where defect-face boundaries
need not all border strict rhombi.

## 4. Interaction with the current half-disk floor

The groupwise atomic theorem already gives

\[
\liminf {T-q/2\over D}
\ge2\sqrt{2\Delta_2},
\qquad
\Delta_2={\pi\over2\sqrt3}.
\tag{4.1}
\]

The boundary inequality is independent of that train-phase argument. It retains the
physical boundary occurrences that the atomic argument discards and supplies an
additional constraint whenever `2(q-k)+4f` falls below `(4+2\gamma)D`.

It is not a contradiction by itself. The current scalar system can pay (2.6) through
`q-k` and `f`; no contradiction follows from the boundary floor alone. The reduction
leaves the defect-face payment and the common limiting diameter to control.

## 5. Scope and classification

- The two group area limits, projection coverage, and physical-boundary transport are
  used at their audited-working proof-only scopes.
- Boundary edges and repeated vertices are counted as occurrences.
- Contact-isolated source points remain in the full source and never enter the core
  affine-kernel statement.
- No equality uniqueness for disk packing and no near-equality-to-quadrangulation
  inference is used.
- The theorem-state manifest is unchanged.

**Classification:** proved candidate awaiting promotion; proof-only. C-II remains open.
