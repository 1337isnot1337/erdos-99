<!-- theorem-state: {"artifact_id":"ART-9D96FCC2E053","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C90: macroscopic secondary-train caterpillar

**Date:** 2026-09-01  
**Repository base:** `3f6c6ea2` (main after C89 / PR #94)  
**Status:** LEVEL I STILL OPEN

C88 forces a non-chain train that separates a linear number of active diameter pairs.
C90 identifies the exact diameter-graph structure across any such train cut.

The result is a cross-route reuse of the C25 ordered common-cut argument, but the cut
is now a **rhombic train** rather than a positive-contact bridge. This matters because
C88 guarantees a macroscopic train cut unconditionally inside the canonical pure
chain-face branch.

## 1. A non-chain train has both terminals on one z-a boundary arc

Work in the pure simply connected rhombic disk containing the exact C80 chain from
`z` to `a`. The D chain trains `P` are exactly the train tracks separating `z` and
`a`.

Let `tau` be a train not in `P`. A train is a properly embedded boundary-to-boundary
arc in the rhombic disk. If its two boundary terminals lay on opposite boundary arcs
from `z` to `a`, Jordan separation would put `z` and `a` on different sides of
`tau`, contradicting `tau notin P`.

Hence both terminals of every non-chain train lie on the same `z`-to-`a` boundary
arc.

Removing `tau` cuts the disk into two components. On the boundary this gives two
complementary cyclic intervals. Since every convex-hull vertex of the source is a
boundary vertex of the rhombic disk, the source diameter endpoints on the two sides
form complementary cyclic intervals

`A=(a_1,...,a_p)`, `B=(b_1,...,b_q)`

in convex-hull order.

## 2. The diameter graph crossing one train cut is a forest

Let `H_tau` be the subgraph of the complete source diameter graph consisting of all
active diameter pairs whose endpoints lie on opposite sides of `tau`.

Then

`H_tau subseteq A x B`,

so `H_tau` is bipartite.

Every cycle in a planar diameter graph is odd: distinct diameter edges form a
geometric thrackle, and the standard parity argument for a straight-line thrackle
excludes even cycles. Therefore a bipartite subgraph of the diameter graph contains no
cycle.

### Theorem C90.1 — secondary-train forest

For every train `tau`, the crossing diameter graph `H_tau` is a forest.

This statement uses the complete C65 diameter graph, not one selected KKT support.

## 3. Ordered diameter edges across the train cut

List `A` and `B` in the same cyclic direction around the convex hull. If

`a_i b_j`, `a_k b_l`

are vertex-disjoint diameter edges in `H_tau` and `i<k`, the diameter-thrackle property
forces the straight chords to cross. Chords joining the two complementary boundary
intervals cross exactly when their endpoint orders agree. Hence

`i<k  =>  j<l`.

This is exactly the order monotonicity used in C25.

Suppose one `a_i` had three non-leaf neighbors

`b_j1 < b_j2 < b_j3`.

The middle neighbor is non-leaf, so it has another neighbor `a_k != a_i`. If `i<k`,
compare the independent edges `a_i b_j3` and `a_k b_j2`; order monotonicity would
require `j3<j2`. If `k<i`, compare `a_k b_j2` with `a_i b_j1`; it would require
`j2<j1`. Both are impossible. The same argument holds with A and B interchanged.

Thus no vertex has three non-leaf neighbors.

## 4. Caterpillar classification

Take one tree component Q of `H_tau`. Delete all graph leaves. The remaining induced
subgraph is connected whenever it has at least two vertices: every internal vertex on
the unique path between two non-leaves is itself non-leaf.

By the preceding section every remaining vertex has degree at most two. The remaining
connected acyclic graph is therefore a path.

### Theorem C90 — secondary-train caterpillar theorem

For every train `tau` in the pure rhombic disk,

`H_tau = disjoint union of caterpillar trees`.

In particular every active diameter pair separated by a fixed non-chain train belongs
to one ordered caterpillar component across the two complementary convex-boundary
intervals.

The theorem includes matching, star, and long-path components; none is excluded by
this classification alone.

## 5. Insert the C88 macroscopic cut

C88 selects two active diameter pairs over every one of the D C87 staircase edges and
proves at least

`D(D-1)`

incidences between those selected pairs and trains outside the chain atom `P`.

C89 and the earlier shell inequalities give

`T <= 2 pi D + o(D)`

in the asymptotic pure-rhombic branch. Therefore some non-chain train `tau_*` separates
at least

`m_* >= (1/(2pi-1)+o(1)) D`

selected active diameter pairs.

Let

`rho_0 = 1/(2pi-1) = 0.189279...`.

Since `H_(tau_*)` contains those selected pairs, C90 gives:

### Corollary C90.2 — macroscopic diameter caterpillar cut

There is a non-chain train `tau_*` such that its crossing diameter graph is a
caterpillar forest with at least

`(rho_0+o(1))D`

edges.

Any forest with m edges and c nontrivial components has m+c incident vertices.
Consequently `H_(tau_*)` uses at least

`(rho_0+o(1))D`

distinct source diameter endpoints. At least half of these lie in one of the two
ordered train-cut boundary intervals.

Thus one secondary train sees a genuinely macroscopic ordered diameter object; the
C88 incidence cannot be dispersed only into isolated local cut events.

## 6. Leaf/spine alternative

For a caterpillar forest with m edges, let L be the number of graph leaves and S the
number of non-leaf vertices. Componentwise,

`m = L + S - c`.

Hence either

`L >= m/2`

or

`S > m/2`.

Applied to `tau_*`, one of the following holds:

1. **leaf-rich phase:** at least `(rho_0/2+o(1))D` diameter leaves cross the same
   train cut; or
2. **spine-rich phase:** at least `(rho_0/2+o(1))D` non-leaf diameter vertices lie on
   the ordered caterpillar spines.

This is only a population dichotomy; a diameter star remains allowed in the first
case and a long path remains allowed in the second.

## 7. Frontier effect

The canonical pure chain-face branch now has two interacting ordered objects:

1. C87: a D-edge paired staircase tree in chain-prefix coordinates, all intervals
   crossing one chain train;
2. C90: a non-chain train whose separated active diameter graph is an
   Omega(D)-edge caterpillar forest across one complementary boundary cut.

The same selected diameter pairs participate in both descriptions. The next target is
therefore an **intersection theorem** for the staircase and caterpillar orders. A
useful endpoint would show that a D-edge paired staircase cannot place
`rho_0 D` of its selected physical diameter chords inside one secondary-train
caterpillar without forcing either a forbidden even diameter cycle, an excessive
shared-endpoint star, or an additive two-train Cartesian block.