# Target C — harmonic attachment-cell disjointness and tiling audit

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module rebuilds the valid geometric core of the old unreviewed report
`docs/reports/target_c_attachment_cell_disjointness_2026-08-31.md` against the current
post-ZF stack. The old report cited stale C36/C37 labels. The proof below uses only the
current canonical Section-62 harmonic trapping and planar attachment-incidence theorem.

For distinct unloaded positive-contact components `I_r,I_s`, let

\[
A_r,A_s\subset B,
\qquad
P_r:=\operatorname{conv}(A_r),
\qquad
P_s:=\operatorname{conv}(A_s).
\]

The main theorem is

\[
\boxed{
\operatorname{int}P_r\cap\operatorname{int}P_s=\varnothing
\qquad(r\ne s).
}
\]

Thus harmonic attachment cells are actual pairwise interior-disjoint convex cells, not
merely abstract response containers. In the rhombic-saturation branch of Section 79,
this becomes much stronger: the cells asymptotically tile the force hull in area, and
the sum of their local non-rhombic area deficits is `o(D^2)`.

No contact-isolated source point is reclassified or deleted.

---

# 83. Harmonic attachment cells are interior-disjoint

Retain canonical Section-62 notation. The loaded set `B` is the vertex set of the
convex force hull `F`. For every unloaded component `I_r`, its distinct loaded
attachment set `A_r` has at least three vertices and harmonic trapping gives

\[
I_r\subset P_r:=\operatorname{conv}(A_r)\subset F.
\tag{83.1}
\]

Every member of `A_r` is an extreme vertex of `F` and remains an extreme vertex of
`P_r`.

## 83.1 Alternating attachment pairs are impossible

### Lemma 83.1 — no proper crossing of cell boundaries

For distinct `r,s`, the polygon boundaries `partial P_r` and `partial P_s` do not
cross properly.

### Proof

Suppose an edge `ac` of `P_r` and an edge `bd` of `P_s` cross in their relative
interiors. All four endpoints are distinct vertices of the same convex polygon `F`,
so they occur in alternating cyclic order on `partial F`.

Because `a,c in A_r`, choose a simple contact path from `a` to `c` whose internal
vertices lie entirely in the connected unloaded component `I_r`: use one attachment
edge at each end and a path inside `I_r`. Likewise choose a simple path from `b` to
`d` with all internal vertices in `I_s`.

The two paths are vertex-disjoint. Their endpoints are four distinct loaded vertices,
and `I_r cap I_s=empty`. Every contact segment lies in the convex disk `F`. But two
disjoint arcs in a disk joining alternating boundary pairs must intersect. Such an
intersection is impossible in the straight-line planar contact graph unless the paths
share a vertex, which they do not. Contradiction. `square`

This is the current-stack replacement for the stale noncrossing-attachment citation in
the old report.

## 83.2 Nested cells are impossible

We use one elementary convex fact: if two convex polygons have intersecting interiors
and neither contains the other, then their boundaries cross properly, except for a
possible common boundary segment. Here all polygon vertices come from the strictly
convex-position set `B=Vert(F)`. Distinct cell edges therefore cannot have a partially
overlapping collinear segment; a common segment is the same chord with the same two
endpoints. If two polygons lie on opposite sides of such a shared chord their interiors
are disjoint near the chord, while if they overlap elsewhere without containment some
other pair of boundary edges crosses properly. Consequently, in the absence of a
proper crossing, intersecting interiors force containment.

### Lemma 83.2 — no containment

For distinct `r,s`, neither `P_r subseteq P_s` nor `P_s subseteq P_r` is possible.

### Proof

Assume `P_s subseteq P_r`. Let `b in A_s`. If `b notin A_r`, then

\[
A_r\subset B\setminus\{b\}.
\]

Since `b` is an extreme vertex of `F=conv(B)`,

\[
b\notin\operatorname{conv}(B\setminus\{b\}),
\]

and therefore `b notin conv(A_r)=P_r`, contradicting `P_s subseteq P_r`. Hence

\[
A_s\subseteq A_r.
\tag{83.2}
\]

Canonical harmonic trapping gives `|A_s|>=3`. Choose three distinct shared attachment
vertices. Contract `I_r` and `I_s` to two interior incidence nodes and retain one edge
from each node to each of those three loaded vertices. This is a connected bipartite
plane incidence subgraph with

\[
q_j=3,
\qquad
c_j=2,
\qquad
e_j=6,
\]

and all three loaded-side vertices lie on the outer face. The canonical Section-62
planar incidence bound gives

\[
e_j\le q_j+2c_j-2=5,
\]

contradicting `e_j=6`. `square`

### Theorem 83.3 — attachment-cell disjointness

For all distinct harmonic components,

\[
\boxed{
\operatorname{int}P_r\cap\operatorname{int}P_s=\varnothing.
}
\tag{83.3}
\]

### Proof

If the interiors intersect, Lemma 83.1 and the convex observation preceding Lemma 83.2
force one cell to contain the other. Lemma 83.2 forbids containment. `square`

Cells may share one or two loaded vertices or a common boundary chord. Only their
interiors are disjoint.

Since every `P_r subset F`, finite additivity gives

\[
\boxed{
\sum_r\operatorname{area}(P_r)
\le\operatorname{area}(F).
}
\tag{83.4}
\]

This conclusion holds in every post-ZF C-II branch.

## 83.3 Global area and square-root budgets for the cells

Canonical Section 62 already gives

\[
\sum_r\operatorname{per}(P_r)
\le
\pi\bigl(2+2q-e_{BB}-k\bigr)
=O(D),
\qquad k=d_H+s_Z.
\tag{83.5}
\]

By the planar isoperimetric inequality,

\[
2\sqrt{\pi\operatorname{area}(P_r)}
\le\operatorname{per}(P_r).
\]

Therefore

\[
\boxed{
\sum_r\sqrt{\operatorname{area}(P_r)}=O(D).
}
\tag{83.6}
\]

This has the standard macroscopic-tail consequence. For fixed `eta>0`, let

\[
\mathcal S_\eta:=
\{r:\operatorname{area}(P_r)<\eta D^2\}.
\]

Then

\[
\sum_{r\in\mathcal S_\eta}\operatorname{area}(P_r)
\le
\sqrt\eta D
\sum_r\sqrt{\operatorname{area}(P_r)}
=O(\sqrt\eta\,D^2).
\tag{83.7}
\]

Thus whenever the total cell area is quadratic, after first choosing `eta` small only
boundedly many macroscopic cells carry all but an arbitrarily small fraction of it.

## 83.4 Rhombic saturation forces the cells to tile the force hull in area

Now assume the rhombic-saturation branch of canonical Section 79 (equivalently the
full-core branch of canonical Section 80):

\[
A_4=\operatorname{area}(F)-o(D^2),
\tag{83.8}
\]

where `A_4` is the total area of all bounded strict unit-rhombus contact faces.

Let `A_4^0` be the total area of those strict rhombi that are incident to no loaded
vertex. A loaded vertex has positive-contact degree at most three. The number of
quadrilateral faces incident to the loaded set is therefore at most

\[
\sum_{b\in B}\deg_C(b)
\le3q
\le3\pi D.
\tag{83.9}
\]

Every unit rhombus has area at most one, so

\[
\boxed{A_4-A_4^0=O(D).}
\tag{83.10}
\]

Every rhombus counted by `A_4^0` has all four vertices unloaded. Its four contact
edges form a connected cycle, so all four vertices lie in one unloaded component
`I_r`. By harmonic trapping and convexity, the whole rhombus lies in `P_r`.

Because the cell interiors are pairwise disjoint, these rhombi are assigned to cells
without area overlap. Consequently

\[
\sum_r\operatorname{area}(P_r)
\ge A_4^0.
\tag{83.11}
\]

Combine (83.4), (83.8), (83.10), and (83.11):

\[
\boxed{
\sum_r\operatorname{area}(P_r)
=\operatorname{area}(F)-o(D^2).
}
\tag{83.12}
\]

Hence the harmonic attachment cells asymptotically tile the force hull in area.

There is an additive local form. Let `A_{4,r}` be the total area of the unloaded-only
strict-rhombus faces belonging to `I_r`. Then

\[
\sum_rA_{4,r}=A_4^0
\]

and each `A_{4,r}<=area(P_r)`. Therefore

\[
\boxed{
\sum_r
\left(\operatorname{area}(P_r)-A_{4,r}\right)
=o(D^2).
}
\tag{83.13}
\]

Every summand is nonnegative. Thus for every fixed `tau>0`, the total area of cells
whose local rhombic filling fraction is at most `1-tau` is subquadratic:

\[
\boxed{
\sum_{\substack{r:\ A_{4,r}\le(1-\tau)\operatorname{area}(P_r)}}
\operatorname{area}(P_r)
=o(D^2).
}
\tag{83.14}
\]

So asymptotically almost all attachment-cell area lies in cells that are themselves
locally rhombus-saturated.

## 83.5 Finite macroscopic-cell reduction in the near-disk branch

Canonical Section 80 strengthens the no-macroscopic-inactive-container side to

\[
{\operatorname{area}(F)\over D^2}\to{\pi\over4}
\]

and, after translation and scaling by `D`, the force hull converges to the diameter-one
disk. In that branch, (83.12) and (83.7) say:

> for every fixed accuracy `xi>0`, one can choose a fixed `eta>0` so that, for all
> sufficiently large survivors, a bounded number of pairwise interior-disjoint convex
> harmonic cells of area at least `eta D^2` cover all but `xi D^2` of the force-hull
> area; and by (83.14), all but `o(D^2)` of that macroscopic cell area is locally
> filled by strict rhombi.

This is a genuine finite-cell geometric reduction. The remaining full-core problem is
not an arbitrary polycrystal with a sublinear number of overlapping response cells:
up to arbitrarily small area loss, it is a bounded collection of disjoint macroscopic
convex harmonic cells inscribed in an asymptotically round force hull.

Canonical Section 78 then localizes the complete-grid diameter mechanism inside at
least one such macroscopic cell, while canonical Section 82 strengthens its induced
contact graph to a boundary-order near-quadrangulation.

## 83.6 What this does not prove

The theorem does **not** show that

- one cell occupies asymptotically all of `F`;
- distinct cells have disjoint boundaries;
- every macroscopic cell has the same phase frame;
- local complete grids cover a fixed fraction large enough to violate Section 76;
- shrinking one cell decreases the global source diameter;
- contact-isolated source points vanish.

The inactive-container branch remains separate.

## 83.7 Dependency audit

- **Canonical Section 62 / `C-ATTACH-CURRENCY`:** harmonic trapping, at least three
  attachments per unloaded component, and the planar incidence bound
  `e_j<=q_j+2c_j-2`; also the total attachment-cell perimeter bound.
- **Loaded extremality:** `B=Vert(F)` from the canonical post-ZF harmonic framework.
- **Planarity:** the straight-line positive-contact graph is planar; paths through two
  distinct unloaded components are internally disjoint.
- **Canonical Section 79 / `C-INACTIVE-DICHOTOMY`:** used only for the rhombic-
  saturation consequence (83.8)--(83.14), not for cell disjointness.
- **Canonical Section 80 / `C-FULLCORE-NEAR-DISK`:** used only for the near-disk
  interpretation in Section 83.5.
- **Canonical Sections 78 and 82 / `C-HARMONIC-GRID-LOCAL`, `C-HARMONIC-CARRIER-QUAD`:**
  handoff only; not proof dependencies of Theorem 83.3.
- **Contact isolates:** untouched.

**Status:** canonical as `C-HARMONIC-CELL-TILING`; see `docs/state/theorem-state.yaml` for lifecycle authority. C-II remains open.
