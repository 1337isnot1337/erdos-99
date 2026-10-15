# Target C — parallel trains cannot repeat a bounded stopping-face pair

**Date:** 2026-09-12  
**Status:** proof-only structural candidate; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The global stopped-train endpoint multigraph has no loops at bounded stopping faces.
This note removes one further multiplicity: two distinct, disjoint trains with the
same projective direction cannot join the same pair of bounded stopping faces.

The implication chain is

```text
two parallel trains with the same bounded endpoints
  -> Jordan cut through the two trains and the two stopping faces
  -> piecewise transverse contact shear with no active diameter crossing
  -> non-Euclidean mixed flex on the positive-contact core
  -> contradiction to the canonical Section-57 rank theorem.
```

The conclusion is only for the stated parallel/disjoint case. Trains joining the same
two faces with different directions remain unclassified.

## 1. Statement

Work in the canonical contact-minimal, then diameter-pair-minimal C-II representative.
Let `F` and `G` be two distinct bounded nonquadrilateral faces of the full positive
contact graph. Let `tau_1,tau_2` be distinct complete stopped train midpoint paths
such that

1. both paths have the same projective contact-edge direction `[u]`;
2. the paths are disjoint, including their terminal edge occurrences; and
3. each path has one terminal occurrence on `F` and one on `G`.

Then this configuration is impossible.

The disjointness in (2) is automatic for distinct complete trains of the same
projective direction in the canonical pseudosegment train geometry; it is listed
explicitly so the cut construction does not rely on an unstated crossing convention.

## 2. Build the two-train cut

The bounded faces `F` and `G` are strict convex polygons with empty open interiors.
Choose an arc in the open interior of `F` joining the two terminal edge midpoints of
`tau_1` and `tau_2`, and likewise choose such an arc in `G`. The arcs can be chosen
to meet the contact graph only at their endpoints. Since the train paths are disjoint
and connect the same two faces, their endpoint order on `F` and `G` is the noncrossing
order. Pairing the two paths accordingly gives a simple Jordan curve `Gamma`.

Every train midpoint path lies in the union of its strict rhombi, and every bounded
contact face lies in the convex hull `K` of the full source. Hence

\[
\Gamma\subset K,
\qquad
\operatorname{Int}(\Gamma)\subset K.
\tag{2.1}
\]

The curve meets the contact graph only at the midpoints of contact edges belonging to
`tau_1` or `tau_2`. All such edges are parallel to `u`.

Let `S` be the set of nonisolated positive-contact-core vertices in
`Int(Gamma)`. Both `S` and its complement in the core are nonempty: a crossed train
edge has its two endpoints on opposite sides of the Jordan curve.

## 3. No active diameter edge crosses the cut

Every endpoint of an active diameter edge is an extreme point of `K`. An extreme point
of a convex set cannot lie in the interior of a Jordan domain contained in that convex
set. Therefore no active diameter endpoint lies in `Int(Gamma)`, and every active
diameter edge has both endpoints outside `S`.

Contact-isolated source points may lie inside the curve, but they are not vertices of
the mixed core matrix and are assigned zero velocity below.

## 4. Contradictory mixed flex

Let `J` denote a quarter-turn and define a core velocity field

\[
w(p)=
\begin{cases}
Ju,&p\in S,\\
0,&p\in V\setminus S,
\end{cases}
\tag{4.1}
\]

where `V` is the nonisolated positive-contact core. For a contact edge with both
endpoints on one side of `Gamma`, the relative velocity is zero. For a contact edge
crossing `Gamma`, the edge belongs to one of the two selected trains and is parallel
to `u`; its first length variation is

\[
u\cdot(\pm Ju)=0.
\]

Thus every active contact row vanishes. Every active diameter row also vanishes,
because both endpoints lie outside `S`. The field `w` is therefore an infinitesimal
flex of the mixed active framework on `V`.

It is not Euclidean. The canonical Section-57 endpoint count supplies at least three
active diameter edges in distinct projective directions for sufficiently large `D`,
and hence at least two distinct active core vertices outside `S`. A Euclidean
infinitesimal motion that vanishes at two distinct points is identically zero, while
`w` is nonzero on `S`. This contradicts

\[
\operatorname{rank}R_{C\cup H}[V]=2|V|-3.
\]

Therefore the two parallel trains cannot exist. `square`

## 5. Endpoint-graph consequence and scope

In the global stopped-train endpoint multigraph, there is no pair of parallel edges
between two bounded stopping-face vertices when the corresponding trains have the
same projective direction. The theorem does not forbid different-direction parallel
edges, outer-face repetitions, or local harmonic-cell train segments whose stopping
face has not been globalized.

The proof uses the mixed-rigidity theorem only on `V`; contact-isolated source points
remain in the full configuration. It uses no affine-kernel statement for isolated
coordinates and no finite global optimality assertion beyond the canonical rank
theorem.

**Classification:** proved candidate awaiting promotion; proof-only. C-II remains
open. A remaining endpoint-multigraph closure would need to handle different
directions between the same two faces or convert the resulting face graph into a
source-preserving diameter descent.
