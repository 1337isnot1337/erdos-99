> Generated reading edition · [exact source](../../../docs/reports/target_c_common_cut_caterpillar_2026-08-31.md) · source SHA-256 `6add9343925b1f644541fd3139f7f6e22fe25a54a22212314f2f472f3c9dead7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CC65FC5A77BF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: the common-cut diameter forest is a caterpillar forest

**Date:** 2026-08-31  
**Repository branch:** `research/target-c-two-terminal-collapse-2026-08-31`  
**Run type:** proof / diameter-graph classification inside C24 forest phase  
**Target:** C-II  
**Depends on:** C20, C24, and the geometric-thrackle property of planar diameter edges  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C24 shows that if the common positive-diameter route `I_*` contains a contact bridge,
then every positive diameter edge crosses the corresponding bridge-tree cut and
`H_+` is a forest.

The cut gives more than bipartiteness.  Its two loaded sides are complementary cyclic
intervals of the convex force-hull boundary.  Put each interval in its boundary order.
Then any two vertex-disjoint positive diameter edges must cross, so their endpoint
orders on the two intervals must agree.  This order monotonicity forces every connected
component of `H_+` to be a caterpillar.

Thus the C24 common-chain phase has the exact diameter normal form

$$
\boxed{
H_+ = \text{a disjoint union of caterpillar trees},
}
$$

with no isolated vertices in `B_+`.

---

## 1. Ordered common cut

Assume the C24 common intersection `I_*` contains a bridge-tree edge `e`.  Removing
`e` partitions the loaded vertices into complementary cyclic intervals

$$
A=\{a_1,\ldots,a_p\},
\qquad
B=\{b_1,\ldots,b_q\},
\tag{C25.1}
$$

listed in the same cyclic direction around the convex boundary.  C24.5 says every
positive diameter edge crosses this cut:

$$
H_+\subseteq A\times B.
\tag{C25.2}
$$

In particular `H_+` is bipartite and acyclic.

---

## 2. Order monotonicity of independent diameter edges

### Lemma C25.1

Let

$$
a_i b_j,\ a_k b_\ell\in H_+
\tag{C25.3}
$$

be vertex-disjoint.  If `i<k`, then

$$
\boxed{j<\ell.}
\tag{C25.4}
$$

#### Proof

The cyclic boundary order consists of the entire `A` interval followed by the entire
`B` interval.  Two chords joining `A` to `B` cross in their interiors exactly when the
relative orders of their endpoints on the two intervals agree.  Thus for `i<k`, the
chords `a_i b_j` and `a_k b_\ell` cross exactly when `j<\ell`.

The two edges are vertex-disjoint edges of the planar diameter graph, so the geometric-
thrackle property says they must cross.  Hence `j<\ell`. `\square`

Equivalently, no two independent positive diameter edges form an inversion across the
ordered common cut.

---

## 3. No diameter vertex has three non-leaf neighbors

Call a vertex of a graph **non-leaf** when its graph degree is at least two.

### Lemma C25.2

No vertex of `H_+` has three distinct non-leaf neighbors.

#### Proof

Suppose first that some `a_i in A` has three non-leaf neighbors

$$
b_{j_1},\ b_{j_2},\ b_{j_3},
\qquad
j_1<j_2<j_3.
\tag{C25.5}
$$

Because the middle neighbor `b_{j_2}` is non-leaf, it has another neighbor

$$
a_k\ne a_i.
\tag{C25.6}
$$

The graph `H_+` is a forest, so no ambiguity from a cycle arises; in particular the
four edges used below are ordinary distinct tree incidences.

If `i<k`, compare the vertex-disjoint edges

$$
a_i b_{j_3}
\quad\text{and}\quad
a_k b_{j_2}.
$$

Lemma C25.1 would require `j_3<j_2`, impossible.

If `k<i`, compare instead

$$
a_k b_{j_2}
\quad\text{and}\quad
a_i b_{j_1}.
$$

Lemma C25.1 would require `j_2<j_1`, again impossible.

Thus no `a_i` has three non-leaf neighbors.  The same argument with `A` and `B`
interchanged proves the statement for vertices of `B`. `\square`

The forest hypothesis is already supplied by C24.  The proof itself only needs that
the middle neighbor has a second endpoint distinct from the original star center and
that the relevant edges are vertex-disjoint.

---

## 4. Caterpillar classification

A tree is a **caterpillar** if deleting all leaves leaves a path, possibly empty or a
single vertex.

### Theorem C25 (common-cut caterpillar theorem)

If the C24 common diameter-route core contains a contact bridge, then every connected
component of the positive diameter graph `H_+` is a caterpillar.

#### Proof

C24.5 says `H_+` is a forest.  Let `Q` be one connected component.

Delete all leaves of `Q` and let `Q^circ` be the induced subgraph on the remaining
non-leaf vertices.  If it is empty or a singleton there is nothing to prove.

Otherwise `Q^circ` is connected.  Indeed, for any two non-leaf vertices of the tree
`Q`, every internal vertex on their unique `Q`-path has at least its two path neighbors
and is therefore also non-leaf.

By Lemma C25.2, every vertex of `Q` has at most two non-leaf neighbors.  Hence every
vertex of `Q^circ` has degree at most two in `Q^circ`.  A connected acyclic graph of
maximum degree at most two is a path.  Therefore deleting the leaves of `Q` leaves a
path, so `Q` is a caterpillar. `\square`

Since `B_+=V(H_+)` by definition, there are no isolated loaded vertices.  Thus the
positive diameter graph in this phase is exactly a disjoint union of nontrivial
caterpillars.

---

## 5. Spine geometry

For a caterpillar component `Q`, call the path `Q^circ` its **spine**.  Every edge not
on the spine is a leaf edge incident to a spine vertex (or `Q` is a single edge).

The geometry inherited from the diameter graph is:

1. spine vertices alternate between the two common-cut intervals `A` and `B`;
2. every pair of vertex-disjoint spine or leaf edges crosses;
3. along either boundary interval, independent edge endpoints occur in the same order
   as their endpoints on the opposite interval; and
4. at every spine vertex, all incident diameter directions satisfy the promoted C18
   shared-endpoint angle bound.

No uniform bound on spine length follows yet.  Unit separation only gives an
`Omega(1/D)` angular separation between distinct diameter partners, so an `O(D)` spine
remains compatible with the current estimates.

---

## 6. C-II effect

The C24 common-chain phase can now be written as

```text
positive contact articulation:
    universal exact straight constant-stress unit chain I_*, length <= D
    + C22-C23 rooted side branches

positive diameter graph:
    forest
    -> in fact disjoint union of caterpillars
    -> every component has one alternating spine plus diameter leaves
    -> independent diameter edges are order-monotone across the common cut
```

This removes arbitrary positive-diameter forests from the bridge endgame.  The exact
remaining common-chain theorem is narrower:

> **Caterpillar transport theorem.**  Exclude a fully force-visible global minimizer in
> which the positive diameter graph is a common-cut caterpillar forest and every
> diameter pair is routed through the same straight contact-chain core, with the
> remaining bridge depth contained in the C22-C23 side branches.

The obvious next quantitative handles are the spine order, the C18 angle bound at
spine vertices, the unit-separated boundary order, and the exact reciprocal cut forces.
The nonuniform KKT weights remain a serious obstruction.

---

## 7. Regression audit

- **Matching phase:** every component is a single-edge caterpillar; allowed.
- **Diameter star:** a caterpillar with one-vertex spine; allowed.
- **Long diameter path:** a caterpillar whose spine is the path; allowed.
- **Branching tree with a vertex adjacent to three non-leaf neighbors:** excluded by
  C25.2 in the common-cut phase.
- **Odd diameter cycle:** not in this phase; C24 already forces the common intersection
  to one block when `H_+` has a cycle.
- **Bridge-free phase:** not in this theorem.

The theorem does not use a general classification theorem for geometric thrackles; the
needed forest statement is proved directly from the ordered common cut.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C25 (common-cut caterpillar theorem):
Assume the C24 common route I_* contains a bridge.  Then every H_+ edge crosses one
fixed bridge cut between complementary boundary intervals A=(a_i), B=(b_j).
For vertex-disjoint edges a_i b_j and a_k b_l, i<k, diameter-thrackle crossing implies
j<l.  This order monotonicity forbids a vertex from having three non-leaf neighbors:
if a_i had non-leaf neighbors b_j1<b_j2<b_j3, a second neighbor a_k of b_j2 would
violate monotonicity against the outer edge on one side or the other.

C24 already says H_+ is a forest.  In each tree component, the non-leaf induced
subgraph is connected and has maximum degree <=2, hence is a path.  Therefore every
component is a caterpillar.

Common-chain C-II phase now has:
- universal straight constant-stress contact core I_*;
- positive diameter graph = common-cut caterpillar forest;
- C22-C23 rooted side branches;
- arbitrary small/nonuniform beta weights still allowed.
```
