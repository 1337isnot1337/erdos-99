> Generated reading edition · [exact source](../../../docs/reports/target_b_dual_tree_dense_grid_extraction_correction_2026-09-05.md) · source SHA-256 `1d0efd88648462f9cb8c83a2a4627db9b9760b504684ff88c6d6fe19fe7ce61e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C258B480E227","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Erdős Problem #99 — Target B dual-tree correction for dense coherent grid extraction

**Date:** 2026-09-05  
**Run type:** hostile audit + exact topological repair  
**Target:** unique-max / balanced / two-max coherent phase stability reports  
**Depends on:** pure simply connected train-disk topology; train tracks cross at most once  
**LEVEL I STATUS:** STILL OPEN

## 1. The problem being repaired

The recently promoted unique-max stability report states:

> A pairwise noncrossing family of proper train arcs splits the disk into a linear chain of regions, so every other train crosses a consecutive interval of that family.

That implication is false for arbitrary pairwise disjoint proper crosscuts of a disk. Their complement dual can branch: several disjoint crosscuts can cut off disjoint boundary caps from one central region. Pairwise noncrossing alone does not provide a global linear order.

The balanced and two-max reports reuse the same interval-extraction step. Therefore their existing audits do not justify that step as written.

The downstream stability algebra is salvageable. The dense-crossing hypothesis itself forces an almost-spanning **path** in the complement dual tree, and that path provides exactly the linear stack needed for the rectangle extraction.

## 2. Complement dual of a disjoint train family

Let

`B={beta_1,...,beta_b}`

be a family of pairwise noncrossing proper train tracks in a simply connected rhombic disk. Remove the train curves from the disk and form the dual graph `T_B`:

- one dual vertex for each component of the complement;
- one dual edge for each train `beta`, joining the two regions on its sides.

### Lemma DT1 — the complement dual is a tree

`T_B` is a tree with `b` edges and `b+1` vertices.

### Proof

A proper crosscut of a disk separates one component into exactly two components. Add the pairwise disjoint train arcs one at a time. Each new arc lies in one current component and splits it into two, increasing the number of complement components by one. Thus there are `b+1` regions and the dual is connected with `b` edges. Hence it is a tree. `square`

## 3. One train crosses a path in the dual tree

Let `alpha` be any other train track. It is a proper simple arc and crosses each `beta in B` at most once.

### Lemma DT2 — crossing sets are tree paths

The set

`P_B(alpha)={beta in B: alpha crosses beta}`

is the edge set of one simple path in `T_B`.

### Proof

Traverse `alpha` from one boundary terminal to the other. Between successive crossings with `B`, the arc lies in one complement region. Crossing `beta` moves across the corresponding dual edge. Thus the sequence of crossed trains is a trail in `T_B`.

No dual edge repeats because two trains cross at most once. A trail with no repeated edge in a tree cannot revisit a vertex: revisiting would create a closed trail and therefore a cycle. Hence the dual trail is a simple path. `square`

This is the correct replacement for the false global-interval statement.

## 4. A dense crossing pair forces an almost-spanning dual path

Let `A` be a second train family of size `M`. No internal topology of `A` is needed yet. Let

`q = M b - e(A,B)`

be the number of missing `A`–`B` crossings and put

`epsilon = q/(M b)`.

Assume

`epsilon -> 0`.

Averaging supplies `alpha_* in A` missing at most `epsilon b` tracks of `B`. By DT2 its crossed set is a dual path `P_*` with

`|P_*| >= (1-epsilon)b`.

Let

`B_0=P_*`

and order these tracks by their edge order along the path `P_*`.

### Lemma DT3 — every other crossing set is an interval on the backbone

For every `alpha in A`, the set of tracks of `B_0` crossed by `alpha` is a consecutive interval in the path order on `B_0`.

### Proof

By DT2, `P_B(alpha)` is a simple path in the tree `T_B`. The intersection of two simple paths in a tree is connected (possibly empty), hence is a simple path. Therefore

`P_B(alpha) cap P_*`

is a consecutive subpath of `P_*`. `square`

Thus near-completeness creates the missing linear order rather than assuming it.

## 5. Almost-full complete rectangle

Choose any sequence `eta=eta_M` such that

`eta -> 0`,

`epsilon/eta -> 0`.

Call `alpha in A` good if it misses at most `eta b` tracks of the full family `B`. Markov gives

`#bad <= q/(eta b) = (epsilon/eta) M = o(M)`.

Hence

`|A_good|=M-o(M)`.

For a good `alpha`, its crossing interval on `B_0` misses at most `eta b` edges of `B_0`, because every missed backbone edge is also a missed `A`–`B` crossing. If the backbone edges are indexed

`1,...,b_0`, `b_0=|B_0|`,

then the crossing interval `[l_alpha,r_alpha]` satisfies

`(l_alpha-1)+(b_0-r_alpha) <= eta b`.

Consequently every good interval contains the common central backbone

`B_1={beta_j in B_0: eta b < j <= b_0-eta b}`.

Its size obeys

`|B_1| >= b_0-2 eta b-O(1)`

`>= (1-epsilon-2eta)b-O(1)`

`=b-o(b)`.

We have proved:

### Theorem DT4 — dense disjoint-train pairs contain an almost-full complete grid

Let `A,B` be train families in a simply connected train disk, with `B` internally pairwise noncrossing. Assume every `A` train crosses every `B` train at most once and

`M b-e(A,B)=o(Mb)`.

Then there are subfamilies

`A' subset A`, `B' subset B`

with

`|A'|=M-o(M)`,

`|B'|=b-o(b)`

such that every train in `A'` crosses every train in `B'`.

If `A` is also internally pairwise noncrossing, `A'` and `B'` form the complete topological grid required by the trimmed-grid phase-star theorem.

No global linear ordering of the original `B` family is assumed.

## 6. Consequence for the three recent phase-stability reports

The unique-max, balanced, and two-max phase reports only use their interval lemma to turn

`o(Mb)`

missing crossings in one coherent phase pair into a complete positive-density, in fact almost-full, grid. Their stability algebra that produces such a near-complete pair is independent of the interval lemma.

Coherent phase classes are internally pairwise noncrossing, and train tracks cross at most once. Therefore DT4 supplies the needed grid under exactly the same missing-crossing hypotheses.

Hence:

1. the original global statement “pairwise noncrossing proper tracks split the disk into a linear chain” is **rejected**;
2. the dense interval-bigraph extraction is replaced by DT1–DT4;
3. the downstream diameter contradictions in the unique-max, balanced, and two-max reports remain valid after this replacement, subject to their other stated hypotheses.

## 7. Audit of possible hidden failures

### 7.1 Branching is allowed

DT4 explicitly permits `T_B` to have arbitrary branching. All but `o(b)` of its edges are forced onto the single path `P_*` by one high-degree train. Off-backbone branches are discarded as part of the `o(b)` loss.

### 7.2 The second family need not be ordered in advance

The complete rectangle is extracted by first choosing the backbone in `B`, then retaining the good `A` trains. No order on `A` is used in DT4. Internal noncrossing of `A` is needed only afterward to invoke the complete-grid geometry.

### 7.3 Endpoint regions cause no problem

An `A` train may begin or end in any complement region of `B`; DT2 simply records the unique dual path between those endpoint regions.

### 7.4 Crossings at train intersections

The `B` tracks are internally noncrossing, so the complement dual is well-defined. Generic train curves may be perturbed infinitesimally away from boundary vertices if needed without changing which train pairs cross. The rhombic train convention already represents pair crossings in rhombus interiors and each pair crosses at most once.

## 8. Corrected handoff

```text
LEVEL I STATUS: STILL OPEN.

Correction:
Pairwise noncrossing proper train tracks do NOT automatically form one linear stack.
Their complement dual is a tree.

Repair:
A train crosses a simple path in that dual tree. If an A-B pair has o(Mb) missing crossings, one A train crosses a path containing b-o(b) B-tracks. Every other A crossing set meets that backbone in an interval. Markov + central trimming gives a complete

  (M-o(M)) x (b-o(b))

grid.

Therefore the unique-max, balanced, and two-max phase-stability diameter contradictions survive, but their original interval-neighborhood lemma must be read through this dual-tree replacement.
```
