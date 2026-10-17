> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_threshold_forest_lift_2026-10-01.md) · source SHA-256 `3392d4b3b075aa92c18738b586f85d370169c0e9163607bde4e6aecede58fc30`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-220695C21558","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- threshold staircase forces physical layer splitting

Date: 2026-10-01
Base main: 14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79
Depends on: target_c_exact_phase_threshold_paired_staircase_2026-10-01.md
Status: proof-only; C-II remains open.

## Theorem

Use the threshold exact-phase paired-staircase theorem on a retained shore
tau_1,...,tau_m. Let T be its simple gap tree on layers 0,...,m.
For each of the m edges of T choose the two distinct actual-diameter
representatives supplied in the two hull-arc orientations, and add the unique
parallel full-support diameter h0. Call the resulting physical diameter graph F.

The threshold theorem gives a common retained train tau_r crossed by all 2m
chosen representatives. The full-support edge h0 also crosses tau_r. Hence

    |E(F)| = 2m+1.

Let c(F) be the number of nontrivial connected components. For layer j let n_j
be the number of distinct vertices of F in that complement-dual layer. Then

    F is a caterpillar forest,
    |V(F)| = 2m+1+c(F),

and

    sum_{j=0}^m (n_j-1) = m+c(F) >= m+1.            (1)

Thus the current threshold exact-phase quotient requires a linear number of
physical endpoint-fiber splits. Since m >= (c_* - o(1))D in the fixed-star
rectangle, the left side of (1) is at least (c_* - o(1))D.

## Proof

Every selected edge has endpoints on opposite shores of the proper O-O crosscut
tau_r. Therefore F is bipartite. The actual diameter graph is a straight-line
geometric thrackle, so it has no even graph cycle. A bipartite cycle would be
even; hence F is acyclic.

The standard ordered-thrackle argument also makes every tree component a
caterpillar. Along the two boundary intervals cut by tau_r, vertex-disjoint
diameter edges must have compatible endpoint order. A vertex cannot have three
non-leaf neighbors: the middle non-leaf has another neighbor, and comparison
with one of the two outer edges violates that crossing order. Deleting leaves
therefore leaves a path in each component.

A forest with e edges and c nontrivial components has e+c incident vertices, so

    |V(F)| = 2m+1+c(F).                              (2)

The simple gap graph T is a spanning tree on all m+1 layers. Every layer is
incident with a tree edge, and either selected physical representative over
that edge has an endpoint in that layer. Hence n_j >= 1 for every j.

The layer fibers partition V(F). Subtracting one mandatory physical endpoint
per occupied layer from (2) gives

    sum_j (n_j-1)
      = |V(F)|-(m+1)
      = m+c(F),

which proves (1).

Equivalently, after projecting physical endpoints to layer labels, the selected
quotient has two copies of every edge of T plus the full-support 0--m edge:
2m+1 edges on m+1 vertices. Its cycle rank is m+1. The physical realization is
a forest, so those quotient cycles can survive only by splitting layer fibers.

## Scope audit

The forest/splitting mechanism is analogous to the older chain-face calculation
in target_c_prefix_fiber_split_budget_2026-09-04.md. The new statement applies
it to the current October threshold exact-phase staircase, which is not a
literal length-D contact-chain quotient and sits inside one shore of the current
complete inverse-phase O-O rectangle.

No claim is made that one layer label determines one physical source vertex.

## Remaining bottleneck

Pure gap-graph counting cannot close the threshold branch. The next useful
theorem must couple the forced Omega(D) endpoint-fiber splitting in (1) to the
opposite complete O-O shore. A closure would need to turn those distinct
physical endpoints into an impossible transverse grid incidence, an exact unit
triangle, or a source-preserving strict diameter decrease.

No computation, numerical evidence, verifier execution, CI result, or
unexecuted verifier code is used.
