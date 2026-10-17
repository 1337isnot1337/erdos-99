# Target C — two-phase boundary occurrence charge

**Date:** 2026-09-13  
**Status:** proof-only finite incidence reduction; theorem-state authority unchanged  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note types the non-two-phase boundary population forced by the audited
two-phase outer-walk variation lemma. It does not identify that population with one
canonical currency; it proves the exact alternatives that remain.

Let `G` be a connected plane unit-contact graph with its occurrence-counted outer-face
walk `W`. Fix two unit directions `[u]` and `[v]`. Assume every bounded quadrilateral
face of `G` is a strict rhombus all of whose edge occurrences have projective direction
`[u]` or `[v]`. Let

- `N_o` be the number of outer-walk edge occurrences whose projective direction is
  neither `[u]` nor `[v]`;
- `P_exc` be the total degree of bounded nonquadrilateral faces; and
- `B_o` be the number of bridge edges of `G` which occur on the outer face.

The exact finite charge is

\[
\boxed{N_o\le P_{exc}+2B_o.}
\tag{BC.1}
\]

Combining this with the audited two-phase variation payment gives the source-level
dichotomy

\[
\boxed{
(4-\pi)D-o(D)\le P_{exc}+2B_o
}
\tag{BC.2}
\]

whenever the outer walk has near-disk width `D-o(D)` in the two reciprocal normals and
length at most `\pi D+o(D)`.

## 1. Exact face/bridge partition

Take an outer-walk occurrence `e` counted by `N_o`.

If its underlying edge is a bridge, it is charged to that bridge. In a connected plane
graph every bridge appears exactly twice in the boundary walk of the unique outer face:
the facial traversal enters the bridge into one side of the cut and returns along the
same edge occurrence on the other side. Hence all such occurrences contribute at most
`2B_o`.

Now suppose the underlying edge is not a bridge. The outer-face occurrence has a unique
other incident face `F`, and `F` is bounded. If `F` were quadrilateral, the hypothesis
would make the edge direction `[u]` or `[v]`, contrary to its being counted by `N_o`.
Therefore `F` is nonquadrilateral. Charge the occurrence to the corresponding edge
occurrence in the boundary of `F`.

This charge is injective: an outer edge occurrence has only one opposite face-edge
occurrence, and distinct outer edge occurrences are distinct incidences in the plane
embedding. There are exactly `P_exc` such nonquadrilateral face-edge occurrences.
This proves (BC.1).

No simple-boundary assumption is used. Repeated vertices and repeated bridge traversals
are precisely why the count is by occurrences.

## 2. Variation-to-incidence consequence

The audited two-phase outer-variation lemma gives

\[
N_o\ge(4-\pi)D-o(D)
\tag{BC.3}
\]

under its explicit near-geodesic/near-disk hypotheses. Substitution into (BC.1) gives
(BC.2).

Thus every such two-phase near-geodesic carrier has one of the following:

1. at least `(4-\pi)D-o(D)` exceptional-face boundary degree;
2. a linear population of outer bridge edges; or
3. both, with the exact tradeoff (BC.2).

In the canonical Type-II notation, whenever the carrier is one of the harmonic induced
graphs to which the Section-123 payment applies,

\[
P_{exc}\le10(e_{BB}-k)
\]

turns (BC.2) into

\[
\boxed{
(4-\pi)D-o(D)\le10(e_{BB}-k)+2B_o.
}
\tag{BC.4}
\]

Equation (BC.4) is deliberately only a necessary inequality. It does not assert that
`B_o` is bounded by a diameter or response currency.

## 3. Scope and remaining closure gate

- A bounded quadrilateral face outside the selected two-phase carrier is excluded by
  the phase-purity hypothesis; if such a face is present, it is an interface defect and
  the hypothesis must be enlarged before applying (BC.1).
- A non-bridge outer edge bordering a bounded nonquadrilateral face is charged once,
  even if that face has repeated vertices elsewhere.
- Bridges are counted as underlying edges, not as boundary occurrences; the factor two
  is exact for a connected plane graph.
- Contact-isolated source points are not used or deleted.
- The result makes no global-minimizer claim and supplies no strict-diameter motion.

The live next theorem is now sharply stated: control the bridge term `B_o`, or combine
(BC.4) with the loaded-hull/diameter ledger strongly enough to force a source-preserving
descent. Theorem state remains unchanged and C-II remains open.

**Classification:** proved candidate awaiting hostile audit; proof-only.
