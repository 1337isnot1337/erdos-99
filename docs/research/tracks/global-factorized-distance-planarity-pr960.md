# Factorized transformations, planar replacements, and sharp-reserve regressions

This track reconciles source PR #960 and merged PR #995 against the destination
frontier. The frozen source main is `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.
PR #960 was an open draft at head `c75e519426e3a88839567411fe3381160f3aa3cb`
(tree `65f7e6e67cbead52038792617df9de48208d99d7`), based on
`a43c69dac7e7b0627dec2900e12c60fd4608d519`. Merged PR #995 is retained at
head `8db48831a8212dfac1e24a1d26e7f9d53a67335b` (tree
`b73c1114989079472aeeb883fee7ac9d28f8af57`), based on
`8ba00e900439a15ccd009f935f3e232f93e7480f`. The destination base for this
integration batch is `aa0a8196e88a840ef3ad2dc63626c9e76d91ebf9`.

Every imported statement remains **unreviewed, noncanonical research**. The
destination theorem-state and its canonical dependencies remain authoritative;
this integration changes no theorem or Target C status. Full source identities,
source and destination hashes, transformations, exclusions, and file mappings
are in the [PR file ledger](../migration/2026-10-16/ledger/source-pr-files.jsonl)
and [source-main ledger](../migration/2026-10-16/ledger/source-main-files.jsonl).

## What these routes establish

### Balanced factor certificates and the exact graph alternative

For a finite unit-separated source with diameter `D`, a pair of probability
weights on actual unit contacts and actual diameter pairs with equal incidence
at every label blocks every realized positive vertex-factor placement
`|q_i-q_j| = s_i s_j |p_i-p_j|`: its normalized diameter is at least `D`.
Contact isolates remain in the complete-pair minimum and maximum. This
logarithmic argument is a special realized case of the stronger formal-array
convex-hull theorem already retained in
[`global_separable_distortion_obstruction`](../../reports/global_separable_distortion_obstruction_2026-10-12.md).
The new factorized-distance report is preserved for its direct metric scope and
full source-geometry examples; this identity is not counted as a second
independent theorem.

The two-state contact/diameter digraph gives a constructive alternative. An
alternating directed cycle yields exact balanced-incidence weights. If the graph
is acyclic, longest-path potentials give half-integers `z_i` with
`z_i+z_j >= 1` on every contact and `z_i+z_j <= -1` on every diameter pair.
A sufficiently small exponential factor then makes every old lower and upper
pair inequality strict in the **abstract complete distance array**, including
pairs incident to isolates. This does not produce Euclidean coordinates, a
planar realization, or a global-minimizer conclusion. The finite graph census
and corruption controls are recorded in the local receipt.

### Dense examples that meet the sharp population reserve and still fail globally

The #960 construction gives unbounded triangle-free sources with exactly two
actual contact edges and two crossing actual diameter edges; every other label
is retained as a contact isolate. For each fixed `131/208 < theta < 2/3`, the
population obeys

`n_D - 1 - pi*D^2/(2*sqrt(3)) >= kappa_0*D^(2/3) - C*D^theta`.

Balanced incidence blocks all positive endpoint-factor maps. Yet a small
horizontal contraction keeps both unit contacts, respects every pair lower
bound, and strictly shortens both old diameter pairs, so the examples are
**nonglobal**. The constructed contact tensor also fails the KKT identity. The
population estimate uses canonical Audit.243 at its registered scope; it does
not turn these examples into global minimizers or refute a theorem about them.
Compared with the earlier leading-density-only factorization regression, this
is a distinct stronger population-reserve counterexample to that proposed
implication.

### Planarity and enclosing-radius barriers

Uniform squared-distance interpolation has centered Gram rank `n-1` for every
positive interpolation parameter, repeating the same rank obstruction already
registered for source PR #958. Keeping only two Gram eigenvalues preserves the
original affine coordinate span, so that truncation is not a nonlinear planar
replacement. A separate radius estimate shows that bounded corrections to a
contracted cloud force its enclosing radius below `alpha*R + tau`; this blocks
that particular certificate for an enclosing-radius minimizer when
`2*tau < (1-alpha)*D`.

The exact six-label unit hexagon illustrates the limit of radius-based
obstructions: it has minimum enclosing radius one and a triangle-free
pentagon-plus-center competitor with the same radius and diameter
`sqrt((5+sqrt(5))/2) < 2`. These facts reject specific universal methods. They
do not establish that large triangle-free global minimizers minimize enclosing
radius or possess such a replacement.

### Möbius classification, pole feasibility, and finite regressions

The #995 report's all-pair classification of planar vertex-factor maps as
Möbius or anti-Möbius maps overlaps the existing separable-distortion report;
both full arguments are retained as provenance. Its distinct pole test covers
every inactive pair: for an inversion pole `x`, define
`R_ij(x)=d_ij^2/(|p_i-x|^2 |p_j-x|^2)`, with `m(x)=min R_ij(x)` and
`M(x)=max R_ij(x)`. A strict-sub-`D` normalized image exists in the realized
factor class exactly when some non-source pole satisfies `M(x) < D^2*m(x)`.
Equivalently, all unordered pair-of-pairs impose explicit strict quartic
inequalities. Exact decision for a particular input needs exact real-algebraic
coordinates; no numerical oracle or unrestricted-repacking decision is claimed.

The report and verifier also preserve three distinct exact controls:

- A nine-label square-grid factor array preserves all twelve contacts and puts
  all 36 squared pairs in `[1, 40000/6561]`, below the original diameter square
  `8`, but fails the triangle inequality by `38/81`.
- A four-label cycle gives a valid three-dimensional metric with all distances
  at least one and a smaller diameter, but its four planar unit edges would
  force a rhombus whose diagonal squares sum to four; the displayed diagonal
  squares sum to less than four.
- A seven-label rod with two contact isolates has an exact planar inversion
  competitor checking all 21 pairs, reducing squared diameter from `16` to
  `202/13`. This is a finite nonglobal source, not an eventual result.

### Cross-target hull/train reconciliation

The merged #995 hull/train report maps preserved reports, audits, and exact
checkers across five older Target C research branches. It records one additional
conditional same-host/chord fork: under the proper-host-arc hypothesis, either
at least half the returns yield first-passage contacts meeting the closed chord
segment, or at least half their distinct loaded endpoints lie on the host arc.
The fork yields no diameter edge, route payment, or source replacement. Its
conditional status and exact assumptions remain visible in the
[candidate registry](../../targets/target-c/candidate-registry.json); the
reconciliation is not a global theorem.

## What remains open

The missing step for each global route is source-derived information that uses
globality while retaining all labels and every pair constraint. In particular,
one must either produce a planar strict-`D` competitor for every sufficiently
large triangle-free global minimizer, or find an exact unit triangle. A valid
finite endpoint must have the same cardinality, every distance at least one,
and every distance strictly below `D`, including inactive pairs and isolates.
An abstract distance array, a factorized-map classification, a sharp population
reserve, a radius estimate, or any finite nonglobal competitor cannot supply
that implication by itself.

The factorized route needs either an eventual argument excluding balanced
contact/diameter incidence on global minimizers or a different planar
replacement that escapes the factorized class and checks every pair. The DAG
alternative still needs a planar realization. The population route must use
global-source information beyond the stated reserve and the factorized barrier.
The radius route must derive its enclosing-radius premises from those sources.
The hull/train chord fork must gain the missing diameter or endpoint payment.

## Reproduction

Run from the repository root:

```sh
python3 research/verify_global_factorized_distance_barrier.py
python3 research/verify_global_factorized_graph_alternative.py
python3 research/verify_global_dense_factorized_barrier.py
python3 research/verify_global_planarity_and_radius_barriers.py
python3 research/verify_global_vertex_factor_relocation_2026_10_12.py
python3 research/verify_target_c_good_hull_train_depletion_2026_10_04.py
python3 research/verify_target_c_deep_port_defect_routes_2026_10_04.py
python3 research/verify_target_c_bulk_separator_2026_10_04.py
```

All five newly imported PR #960/#995 Python checkers refuse optimized Python;
run them normally, not with `-O`. Their finite outputs support the listed
fixtures and certificates only. The reports contain the analytic arguments and
their limits. The source AI audits remain provenance and do not satisfy the
destination independent exact-head AI-agent mathematical audit policy for
consequential promotions.

The live source-wide continuation is the
[Target C factorized-planar escape task](../../../tasks/target-c-factorized-planar-escape.md).
