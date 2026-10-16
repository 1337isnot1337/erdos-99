# Target C: escape factorized barriers with a planar global-source endpoint

## Objective

For every sufficiently large triangle-free global minimizer, either prove that
its actual source geometry yields a same-cardinality planar competitor with
minimum distance at least one and diameter strictly below the source diameter,
or derive a unit equilateral triangle. Preserve the universal quantifier over
global minimizers and include every label, contact isolate, lower pair bound,
and upper pair bound.

The focused source-to-destination research is in the
[factorized-distance/planarity track](../docs/research/tracks/global-factorized-distance-planarity-pr960.md).
Start with the destination [theorem state](../docs/state/theorem-state.yaml),
[problem statement](../docs/problem/statement.md),
[Target C frontier](../docs/targets/target-c/CURRENT.md), and
[candidate registry](../docs/targets/target-c/candidate-registry.json).

## Exact route questions

1. **Balanced incidence:** Can global-minimizer structure rule out probability
   weights on actual unit contacts and actual diameter pairs with identical
   incidence at every label? If not, state what further geometric information
   a balanced certificate supplies or fails to supply.
2. **Acyclic alternative:** If the two-state contact/diameter graph is acyclic,
   its half-integral potential gives only an abstract all-pair distance array.
   Can that array be realized by planar coordinates, or can a different
   source-global construction escape the factorized class?
3. **Sharp population reserve:** The unbounded triangle-free family in the
   track meets the sharp `D^(2/3)` population reserve and is still nonglobal.
   Identify a globality-specific condition not already implied by the reserve,
   triangle-freeness, or factorized-map stability.
4. **Planar realization and radius:** Uniform squared-distance interpolation
   has centered rank `n-1`; rank-two truncation is affine. The six-point
   equal-radius replacement and the radius bound block specific universal
   shortcuts. Find a nonlinear planar endpoint that checks all pairs, or prove
   the needed radius premise from global diameter optimality.
5. **Vertex-factor pole test:** The #995 quartic pole criterion decides only
   the realized Möbius/anti-Möbius class. Establish source-derived pole
   feasibility for every large global minimizer or construct an endpoint
   outside that class.

## Required proof boundary

Every proposed finite endpoint must retain the source cardinality and satisfy
`|q_i-q_j| >= 1` and `|q_i-q_j| < D` for every distinct pair, not only the old
contacts and diameter pairs. Verify newly active pairs and isolates explicitly.
An abstract metric array, a higher-dimensional embedding, a local motion, a
finite nonglobal example, or a leading-density/population estimate alone does
not resolve this task.

The task is resolved only by a source-wide argument with the exact eventual
global-minimizer hypotheses, a proof of the planar full-pair endpoint or unit
triangle, and any computational witnesses needed to make the argument
independently checkable. A counterexample to a proposed intermediate route is
useful and should be recorded in the candidate registry, but it does not close
the task unless it settles the global problem statement.

## Prior evidence and boundaries

- [Global formal-array separable obstruction](../docs/reports/global_separable_distortion_obstruction_2026-10-12.md)
- [PR #960 factorized, graph, dense, and planarity reports](../docs/research/tracks/global-factorized-distance-planarity-pr960.md)
- [PR #995 vertex-factor pole test and finite inversion report](../docs/reports/global_vertex_factor_relocation_2026-10-12.md)
- [PR #995 hull/train conditional reconciliation](../docs/reports/hull_train_preservation_reconciliation_2026-10-15.md)
- Exact checker commands and local receipts: [research README](../research/README.md) and [migration receipt directory](../docs/research/migration/2026-10-16/receipts/)

These reports and registry entries remain unreviewed and noncanonical. The
destination theorem state remains authoritative. Do not reinstate the withdrawn
global `K'/D` chart or `q=O(D^(4/5))` inference while using the factorized route.
