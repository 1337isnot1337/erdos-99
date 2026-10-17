> Generated reading edition · [exact source](../../../docs/reports/target_c_common_chain_caterpillar_2026-09-01.md) · source SHA-256 `6a124cb3ad19f365532384d20fd430a6cece8db951a3ced83986bf04d7a37a13`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4E87F2285C7B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C96: common-chain diameter caterpillar

**Date:** 2026-09-01  
**Repository base:** `cc489821` (main after C95 / PR #100)  
**Status:** LEVEL I STILL OPEN

C87 proves that all D simple staircase intervals contain one common C80 chain train
`tau_r`. Every simple interval is represented by at least two active diameter pairs,
one in each hull-arc orientation. The chain diameter `h_0=za` is separated by every
chain train, including `tau_r`.

C96 observes that C90's train-cut forest theorem therefore applies to a much larger
canonical object than the secondary averaged cut from C88-C93: one **single chain
train** already separates at least `2D+1` active diameter edges.

Consequently the train-cut diameter forest uses at least `2D+2` distinct source
diameter endpoints. This sharpens C87's Hopf--Pannwitz endpoint floor by one and gives
an exact slack identity: every extra crossing diameter edge and every extra nontrivial
component of the common-cut forest must be paid for by additional diameter endpoints.

---

## 1. The common train cut

Let

`P={tau_1,...,tau_D}`

be the D exact C80 chain trains. C87 gives a chain index `r` such that every nonempty
simple prefix interval `I_h` contains `tau_r`.

For each of the D simple staircase edges, C87 also gives at least two actual active
diameter pairs with that interval, one in each physical hull-arc orientation. Let
`H_pair` be any selected set containing one pair of each orientation over each simple
edge. Then

`|H_pair|>=2D`.

Every `h in H_pair` has `tau_r in I_h`, so its endpoints lie on opposite sides of the
proper train arc `tau_r`.

The chain diameter

`h_0=za`

also has endpoints on opposite sides of `tau_r`, because every train in P separates
z from a.

Hence the complete source diameter subgraph crossing the cut `tau_r`, denoted
`H_(tau_r)`, contains

`H_pair union {h_0}`

and therefore

`|E(H_(tau_r))|>=2D+1`.

## 2. The crossing diameter graph is a caterpillar forest

A train is a properly embedded boundary-to-boundary arc in the rhombic disk. Removing
`tau_r` partitions all source vertices into two sides. Every edge of `H_(tau_r)` joins
opposite sides, so the graph is bipartite.

Every cycle in a planar diameter graph is odd. Therefore a bipartite diameter
subgraph contains no cycle:

`H_(tau_r)` is a forest.

The ordered-thrackle argument of C90 applies to any train cut: the diameter endpoints
on the two sides occur in complementary cyclic boundary intervals, independent
cross-cut diameter edges are order-monotone, and no vertex can have three non-leaf
neighbors. Hence every component of `H_(tau_r)` is a caterpillar.

### Theorem C96.1 — common-chain caterpillar forest

The complete source diameter graph crossing the C87 common chain train `tau_r` is a
disjoint union of caterpillar trees and contains at least `2D+1` edges.

This uses the complete C65 source diameter graph, not one selected KKT support.

## 3. Endpoint floor

Let

`m_r=|E(H_(tau_r))|`,

`c_r=number of nontrivial components of H_(tau_r)`,

and let `v_r` be the number of source vertices incident with those edges.

Because `H_(tau_r)` is a forest,

`v_r=m_r+c_r`.

Since `m_r>=2D+1` and `c_r>=1`,

`v_r>=2D+2`.

Every such vertex is a source diameter endpoint. If q denotes the full number of
source diameter endpoints, then:

### Theorem C96 — exact common-cut endpoint floor

`q>=2D+2`.

This strengthens C87's `q>=2D+1` by using the fact that all of the guaranteed diameter
edges cross one common train cut and therefore form a forest.

## 4. Exact slack bookkeeping

The same forest identity gives more than the constant improvement. Write

`e_r=m_r-(2D+1)>=0`.

Then

`q >= v_r = 2D+1+e_r+c_r`,

so

`q-(2D+2) >= e_r+(c_r-1)`.

Thus the endpoint surplus above `2D+2` pays exactly for two kinds of deviation from
the minimum common-cut object:

1. extra active diameter edges crossing `tau_r` beyond the `2D+1` guaranteed edges;
2. extra nontrivial caterpillar components beyond one.

At the minimum endpoint count `q=2D+2`, the common-cut graph has exactly `2D+1`
edges, exactly one nontrivial component, and spans all diameter endpoints. It is a
single spanning caterpillar tree containing the chain edge plus precisely the two
selected orientations over every C87 staircase edge.

## 5. Interaction with the low-train phase

C82 gives, for `x=T/D`,

`q/D <= 2x-2(1+Delta_2)+o(1)`.

Hence in C94's low-train phase `x<3+o(1)`,

`q/D <= 4-2Delta_2+o(1)`

`=2.1862006358...+o(1)`.

Combined with C96, the complete common-chain caterpillar uses at least `2D+2`
endpoints while the entire source has only at most about `2.1862D` diameter endpoints.
Thus all extra common-cut components/edges and all diameter endpoints outside the
common-cut forest together have only an `O(0.1862D)` population budget in this phase.

This does not by itself force the minimum spanning-caterpillar equality case.

## 6. Frontier effect

C88-C93 found a heavily loaded **secondary** train only by averaging a quadratic
separation budget. C96 identifies a stronger deterministic train cut already present
in every canonical chain-face survivor:

- it is one of the exact D chain trains;
- it is crossed by at least `2D+1` source diameter pairs;
- its complete crossing diameter graph is a caterpillar forest;
- it uses at least `2D+2` distinct diameter endpoints.

The next target is to exploit the near-spanning nature of this common-cut caterpillar.
A particularly sharp subcase is the minimum-slack regime `q=2D+2+o(D)`, where almost
all diameter endpoints and almost all available diameter edges must lie in one
caterpillar spanning the common chain cut. A geometric classification of such
near-spanning equal-length caterpillars could feed directly back into the C82/C92
train-shell inequalities.