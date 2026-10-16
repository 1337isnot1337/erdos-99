<!-- theorem-state: {"artifact_id":"ART-2DF1302B97D0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — correction to the two-direction boundary route

**Date:** 2026-09-14

**Status:** rejected route / exact regression; no theorem-state change.

The attempted conditional exclusion of a full-support two-direction rhombic disk
used the following proposed lemma:

> Every non-square simple orthogonal polygon has a convex or straight boundary
> vertex that is not a vertex of its convex hull.

That lemma is false.  The counterexample is the simple orthogonal polygon listed
counterclockwise by

\[
(0,0),(3,0),(3,1),(1,1),(1,3),(0,3).
\]

The vertex `(1,1)` is reflex.  The other five vertices are convex, and they are
all vertices of the convex hull of the L-shaped polygon.  There is no non-hull
convex or straight boundary vertex.

Consequently, the following proof pattern is invalid without an additional
diameter-endpoint argument:

```text
degree <= 3 on convex/straight square-grid boundary
    -> every such vertex is loaded
    -> every such vertex is a source-hull vertex
    -> orthogonal-boundary lemma gives a contradiction.
```

The reflex-only boundary case survives the stated degree argument: in the lattice
L-shape, the reflex notch vertex has the two boundary edges plus the two edges into
the occupied arms, so it can have degree four and need not carry a diameter row.

This does **not** disprove Erdős Problem #99.  The L-shape is only a combinatorial
and geometric counterexample to the proposed polygon lemma; no positive global KKT
stress or global minimum-diameter certificate is asserted.  It does show that a
correct two-direction branch theorem must either:

1. use the actual Euclidean diameter graph to exclude reflex-only orthogonal
   boundaries;
2. assume a convex (not merely topological disk) orthogonal boundary; or
3. charge reflex notches through the canonical detour/interface currencies.

The canonical C-II route permits holes, interfaces, carriers, exceptional faces,
and retained contact-isolated points, so this regression cannot be silently
repaired by treating a selected carrier as the full source.

## Exact remaining implication

The unresolved source-level statement is still:

\[
\text{quadratic full-core phase structure}
\Longrightarrow
\text{unit equilateral triangle, or a finite same-cardinality strict sub-}D(n)
\text{ competitor}.
\]

The reflex-notch example is specifically a warning against replacing that statement
by a purely orthogonal-boundary turn count.
