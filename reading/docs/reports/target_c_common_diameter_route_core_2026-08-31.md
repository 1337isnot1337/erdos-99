> Generated reading edition · [exact source](../../../docs/reports/target_c_common_diameter_route_core_2026-08-31.md) · source SHA-256 `ebbc002211666e093caafaab04f718e615db2a418de158cb200330f14bb8d7a5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0A40906A9FDF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: the common diameter-route core is a straight chain

**Date:** 2026-08-31  
**Repository branch:** `research/target-c-two-terminal-collapse-2026-08-31`  
**Run type:** proof / articulation refinement  
**Target:** C-II  
**Depends on:** C20, C22, C23, and the planar diameter-cycle theorem  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C23 proves that the bridge-block paths associated with all positive diameter edges have
a common node.  This note identifies the entire common intersection.

Let `P_h` be the bridge-block-tree path between the endpoint blocks of a positive
diameter edge `h in H_+`.  Then

$$
I_*:=\bigcap_{h\in H_+}P_h
$$

is a nonempty tree path.  Every internal node of this path is reaction-free and has
degree exactly two in the **whole** bridge-block tree.  C22 therefore collapses every
internal block to one neutral vertex, and the bridges of `I_*` concatenate into one
exact straight constant-stress unit chain.

There is also a clean graph-theoretic split.  If `I_*` contains a bridge edge, every
positive diameter edge crosses that bridge cut, so `H_+` is bipartite.  But every
cycle in a planar diameter graph is odd.  Therefore `H_+` is acyclic.  Equivalently:

> if the positive diameter graph contains a cycle, all of its terminal paths meet in a
> **single** bridge block; there is no common contact bridge traversed by every positive
> diameter pair.

---

## 1. Setup

Fix a normalized KKT stress `(alpha,beta)`.  Let `G_+` be its unique nontrivial
positive-contact component.  Delete all bridges of `G_+` and contract the remaining
connected components to the bridge-block tree

$$
T.
\tag{C24.1}
$$

For every positive diameter edge `h=bk in H_+`, let `P_h` be the unique path in `T`
between the blocks containing `b` and `k`.

C23 proves

$$
\bigcap_{h\in H_+}P_h\ne\varnothing.
\tag{C24.2}
$$

Define

$$
\boxed{
I_*:=\bigcap_{h\in H_+}P_h.
}
\tag{C24.3}
$$

---

## 2. The common intersection is a path

### Lemma C24.1

`I_*` is a nonempty path in `T`, possibly consisting of one node.

#### Proof

Each `P_h` is a connected subtree of the tree `T`.  The intersection of connected
subtrees of a tree is connected whenever it is nonempty: if two vertices `x,y` lie in
the intersection, the unique tree path from `x` to `y` lies in every connected
subtree containing both, hence in the intersection.

Thus `I_*` is connected.  It is contained in every `P_h`, and every `P_h` is a path,
so every vertex of `I_*` has degree at most two inside `I_*`.  A connected subgraph of
a tree with maximum degree at most two is a path. `\square`

---

## 3. An internal common-route block cannot be loaded

Assume `I_*` has at least two edges, and let `X` be an internal node of `I_*`.  Denote
the two incident common-route edges by `e^-` and `e^+`.

### Lemma C24.2

`X` contains no positive diameter endpoint:

$$
\boxed{X\cap B_+=\varnothing.}
\tag{C24.4}
$$

#### Proof

Suppose `b in X cap B_+`.  By definition of `B_+`, some positive diameter edge

$$
h=bk\in H_+
$$

is incident to `b`.  The tree path `P_h` starts at the block `X`.  A path starting at
`X` can leave `X` through at most one of the two distinct tree edges `e^-`,`e^+`; it
cannot contain both.

But both `e^-` and `e^+` lie in `I_*`, hence by definition in **every** `P_h`, including
the path of this edge `h`.  Contradiction. `\square`

So the interior of the universal diameter route is reaction-free.

---

## 4. An internal common-route block cannot have a side branch

### Lemma C24.3

Every internal node `X` of `I_*` has degree exactly two in the whole bridge-block tree
`T`.

#### Proof

It already has the two incident edges `e^-`,`e^+` from the common path.  Suppose it had
another incident tree edge `f` leading into a side component `U` of `T-X`.

The corresponding contact bridge separates a nonempty side of the positive contact
component.  C20.1 says **both** sides of every positive-contact bridge contain a
positive diameter-reaction vertex.  Hence `U` contains some

$$
b\in B_+.
$$

Choose a positive diameter edge `h=bk in H_+` incident to `b`.  The tree path `P_h`
starts in `U`, reaches `X` through `f`, and after reaching `X` can continue through at
most one of `e^-`,`e^+`.  It cannot contain both common-route edges.

Again this contradicts `e^-,e^+ subset I_* subset P_h`.  Therefore no such side edge
`f` exists.  The degree of `X` in `T` is exactly two. `\square`

This is stronger than saying merely that `X` has degree two along `I_*`: it excludes
all hidden loaded side branches from an internal universal-route block.

---

## 5. Internal common-route blocks are single neutral vertices

By Lemmas C24.2-C24.3, every internal node `X` of `I_*` is a reaction-free degree-two
bridge block.  C22.4 therefore applies immediately.

### Corollary C24.4

Every internal node of `I_*` consists of one unloaded positive-contact vertex.  The two
incident contact bridges are collinear and carry equal positive stress.

Thus consecutive common-route bridges line up through every internal node.

---

## 6. The common diameter route is one exact straight chain

### Theorem C24 (common diameter-route chain)

If `I_*` has `L>=1` tree edges, then the corresponding `L` positive-contact bridges are
all collinear, have one common stress value, and concatenate into an exact straight unit
chain.  In particular the Euclidean distance between its endpoint bridge blocks, as
measured between the terminal bridge vertices of the chain, is exactly `L`, so

$$
\boxed{L\le D.}
\tag{C24.5}
$$

#### Proof

If `L=1`, there is one bridge and nothing to prove except the length bound, which follows
because both of its vertices lie in the force hull of diameter `D`.

If `L>=2`, every intermediate node of the path is a single neutral degree-two vertex by
Corollary C24.4.  At such a vertex, C22/C21 says the two incident unit bridge vectors are
exactly antiparallel and their stresses equal.  Induction along the path therefore
makes all bridge edges collinear and all their stresses equal.

There are `L` unit bridge edges in one straight chain, so the two terminal bridge
vertices are at Euclidean distance exactly `L`.  Both belong to `V(C_+) subset F`, and
`diam(F)=D`.  Hence `L<=D`. `\square`

Call this straight chain the **common diameter-route core** for the chosen normalized
KKT stress.  It may degenerate to one bridge block when `L=0`.

---

## 7. A nontrivial common route forces the positive diameter graph to be a forest

### Theorem C24.5

If `I_*` contains at least one bridge edge, then `H_+` is bipartite and therefore
acyclic.

#### Proof

Choose one tree edge `e` of `I_*`.  Removing `e` partitions the bridge-block tree into
two sides, and therefore partitions `B_+` into two sets `B_S,B_T`.

Because `e` lies in every path `P_h`, the two endpoint blocks of every positive
diameter edge `h in H_+` lie on opposite sides of this cut.  Hence every edge of
`H_+` joins `B_S` to `B_T`.  Thus `H_+` is bipartite.

Every cycle in the planar diameter graph is odd.  A bipartite graph has only even
cycles.  Therefore `H_+` has no cycle. `\square`

### Corollary C24.6 (cycle-supported phase has a single hub block)

If `H_+` contains a cycle, then

$$
\boxed{|V(I_*)|=1.}
\tag{C24.6}
$$

That is, all positive diameter terminal paths meet in one common bridge block, but no
positive contact bridge is common to all of them.

This includes every positive-diameter odd-cycle phase.

---

## 8. Exact cut law along a nontrivial common route

Suppose `I_*` contains at least one edge and orient its straight chain from one side of
`T-I_*` toward the other.  No internal node of `I_*` contains a loaded vertex or side
branch, so the loaded partition induced by consecutive common-route bridge edges is
constant along the interior of the chain.  Therefore C22.5 supplies one and the same
vector resultant on every common-route bridge.

If the two loaded sides are called `B_L,B_R`, then for every bridge `e` in the common
route,

$$
\boxed{
\alpha_e\nu_e
=
\sum_{\substack{bk\in H_+\\b\in B_L,\ k\in B_R}}
\beta_{bk}\frac{b-k}{D}\,D,
}
\tag{C24.7}
$$

with consistent orientation.  Since the chain theorem already says `alpha_e` and
`nu_e` are constant, this is a single global diameter-cut resultant transported
unchanged along the whole universal chain.

No useful uniform lower bound on the magnitude of this resultant is currently proved;
order-reversing families of crossing diameter chords can still exhibit cancellation.

---

## 9. C-II effect

C23 allowed an arbitrary choice of one common hub block.  C24 replaces that choice by
the exact common intersection and splits the bridge branch into two sharper phases.

### Phase C-IIa: common-chain / diameter-forest

`I_*` contains a contact bridge.  Then

- `H_+` is a forest;
- every positive diameter pair routes through the same exact straight constant-stress
  unit contact chain;
- the common chain has length at most `D`; and
- all diameter-cut reaction is transported unchanged across that chain.

The remaining question is whether a common chain of length `Omega(D)` can coexist with
`Theta(D^2)` globally minimal packing, or whether a short common chain forces most of
the C23 weighted depth into the side branches and hence into repeated loaded/branching
events.

### Phase C-IIb: single-hub-block / possible diameter cycle

`I_*` is one bridge block.  This phase contains every survivor whose positive diameter
graph has a cycle.  All positive diameter terminal paths enter the same bridgeless
positive-contact block, but bridge combinatorics alone do not control the internal
stress of that block.  This is naturally adjacent to the two-edge-connected stress-bulk
branch.

The exact next bridge theorem can therefore be stated more narrowly:

> **Common-route transport theorem.**  Exclude a fully force-visible global minimizer
> in which `H_+` is a forest and all positive diameter pairs are routed through one
> straight common contact chain plus the C22-C23 rooted side branches; or prove that
> the common intersection must be a single block and transfer the problem to the
> two-edge-connected reciprocal-response branch.

---

## 10. Regression audit

- **Single positive diameter edge:** its path itself is `I_*`; a long common straight
  chain is allowed by C24.
- **Positive diameter matching:** all matching-edge paths may share a central contact
  chain; `H_+` is a forest, as required.
- **Positive diameter star:** likewise a forest and compatible with a common chain.
- **Odd positive diameter cycle:** C24.5 forces `I_*` to be one node, not a bridge.
- **Bridge-free positive contact graph:** `T` has one node and `I_*` is that node.
- **Loaded endpoint at an endpoint of the common chain:** allowed.  Only internal nodes
  of a nontrivial common path are forced reaction-free.
- **Order-reversing crossing diameter families:** allowed; C24 does not claim that a
  bridge cut is a diameter star or that its resultant has a uniform no-cancellation
  bound.

The last item is an explicit regression against the tempting but false bridge-cut-star
shortcut.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let T be the positive-contact bridge-block tree and P_h the T-path of h in H_+.
C23 proves the common intersection I_*=intersection_h P_h is nonempty.

New C24:
- I_* is a path.
- An internal node X of I_* cannot contain B_+: an H_+ edge incident there starts at X
  and cannot traverse both common-route edges.
- X cannot have a side branch: that branch contains a loaded endpoint by C20.1, whose
  H_+ path again cannot traverse both common-route edges.
- Hence every internal X is a reaction-free degree-2 bridge block; C22 collapses it to
  one neutral vertex.
- Therefore all bridges of I_* form one exact straight constant-stress unit chain of
  length L<=D.
- If I_* contains an edge, every H_+ edge crosses the corresponding tree cut, so H_+
  is bipartite.  Diameter cycles are odd, hence H_+ is a forest.
- Contrapositive: if H_+ has a cycle, I_* is exactly one hub block.

C-II now splits more sharply into:
(A) diameter-forest + universal straight common contact chain + rooted side branches;
(B) single hub block, including every diameter-cycle phase and the bridge-free bulk.

False shortcut explicitly rejected:
complementary boundary intervals do NOT force all diameter edges crossing the cut to
share an endpoint; order-reversing crossing matchings are possible.
```
