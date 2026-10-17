> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_two_tree_four_block_normal_form_2026-09-09.md) · source SHA-256 `7780fa4bd1f7d76a1bbae96f1ee85ab6a96dd439195b0bbec3b214bb8df8bf63`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B443F99586F2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2` collapses to a four-block two-tree normal form

**Date:** 2026-09-09  
**Repository branch:** PR #118 after DC/TC  
**Run type:** exact convex-thrackle order reduction / KKT cut equilibrium  
**Target:** cyclic primitive endpoint, `d_H=2`  
**Depends on:** DC two-tree classification, TC same-color block argument, CY full positive contact cycle and unique normalized stress  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

DC proves that the cyclic `d_H=2` phase has exactly two connected diameter-tree components. Because every edge from one component is vertex-disjoint from every edge of the other, the diameter-thrackle property makes every cross-component edge pair cross.

The block argument inside TC therefore applies directly to the two full components, without deleting an edge.

### Theorem D2 — four alternating diameter-color blocks

Let the two full diameter-tree components be `T_A,T_B`, with unique bipartitions

```math
A=A_0\sqcup A_1,
\qquad
B=B_0\sqcup B_1.
```

Each of the four color classes is a single nonempty cyclic interval of the convex force-hull order. After swapping color names and rotating the cyclic order,

```math
\boxed{
A_0\;|\;B_0\;|\;A_1\;|\;B_1
}
\tag{D2.1}
```

are the four consecutive terminal blocks around the boundary.

Thus each diameter component occupies exactly two cyclic intervals, and those intervals are precisely its two tree-bipartition classes.

Moreover, if the four contact-cycle transitions occur at indices

```math
i<j<k<\ell,
```

then the unique normalized KKT stress satisfies

```math
\boxed{
v_i+v_k=v_j+v_\ell,
\qquad
v_r:=\alpha_r t_r.}
\tag{D2.2}
```

So the four transition vertices in the reciprocal force polygon form an exact parallelogram.

This is the exact `d_H=2` normal form.

---

## 1. Every edge of one tree crosses every edge of the other

DC gives

```math
H=T_A\sqcup T_B,
```

where both components are nontrivial trees and every loaded terminal belongs to one of them.

Take

```math
e\in E(T_A),
\qquad
f\in E(T_B).
```

They share no endpoint. The full diameter graph is a straight-line geometric thrackle on strictly convex vertices, so `e` and `f` cross properly.

Hence

```math
\boxed{
\text{every A-edge crosses every B-edge}.}
\tag{1.1}
```

This is exactly the cross-component hypothesis used in TC after a tree edge was deleted.

---

## 2. Each bipartition class is a single block

Fix one A-edge

```math
xy\in E(T_A).
```

The chord `xy` divides the convex boundary into two open arcs. Every B-edge crosses `xy`, so every B-edge has one endpoint on each arc.

Because `T_B` is connected and bipartite, side relative to `xy` toggles across every B-edge. Therefore, up to swapping the bipartition labels,

```math
B_0
```

lies entirely on one `xy`-arc and

```math
B_1
```

lies entirely on the other.

Now take two vertices

```math
b,b'\in B_0.
```

They lie on the same side of every A-edge, because the same argument works for every edge of `T_A`. Thus the straight chord `bb'` crosses no A-edge.

Suppose an A-vertex occurred strictly between `b,b'` along the boundary arc containing `B_0`. The complementary `b-b'` arc contains the endpoints `x,y` of the fixed A-edge, so A would have vertices on both sides of the chord `bb'`. Since `T_A` is connected, an A-path between those sides contains an A-edge crossing `bb'`, contradiction.

No B1 vertex lies between two B0 vertices either, since B1 lies on the other `xy`-arc. Therefore `B_0` is one consecutive cyclic block.

The same argument applies to

```math
B_1,A_0,A_1.
```

Thus all four bipartition classes are single cyclic blocks. `square`

---

## 3. The four blocks alternate by component

Each tree has at least one edge, so all four color classes are nonempty.

An A-edge joins `A_0` to `A_1`. Every B-edge must cross every A-edge, so its endpoints `B_0,B_1` lie on opposite open boundary arcs between the A blocks. Hence the two B blocks separate the two A blocks cyclically.

The same statement with A and B interchanged gives the alternating order. After cyclic relabeling and color swaps,

```math
A_0,B_0,A_1,B_1
```

occur consecutively around the hull.

This proves D2.1.

A useful consequence is that the component labels themselves alternate in exactly four runs:

```math
A\;|\;B\;|\;A\;|\;B.
\tag{3.1}
```

There is no higher-run two-tree endpoint.

---

## 4. Summed equilibrium gives one reciprocal parallelogram

CY gives

```math
s_Z=0
```

in the `d_H=2` phase, so the normalized KKT stress is unique and strictly positive on every cycle contact and every full diameter edge.

Sum the KKT equilibrium equations over all vertices of `T_A`.

Every diameter force is internal to `T_A` because there are no diameter edges between the two components. Hence all diameter terms cancel in the sum. Internal A-A cycle contacts also cancel.

By D2.1, exactly four cycle contacts cross the cut `A|B`. If their indices in cyclic order are

```math
i<j<k<\ell,
```

and A is entered across `i,k` and exited across `j,ell`, then the signed contact-force sum is

```math
v_i-v_j+v_k-v_\ell=0,
\qquad
v_r=\alpha_rt_r.
```

Therefore

```math
\boxed{v_i+v_k=v_j+v_\ell.}
```

This proves D2.2. `square`

The B-component sum gives the same equality with the opposite sign, so there is one cut constraint, not two independent parallelograms.

---

## 5. Internal order monotonicity

Within each tree, every two vertex-disjoint diameter edges must also cross. Since its bipartition classes occupy two opposite cyclic blocks, each component is a bipartite convex-thrackle tree drawn between its two blocks.

Hence the existing common-cut order-monotonicity/caterpillar theorem applies separately to `T_A` and `T_B`:

- each component is a caterpillar;
- its nonleaf spine is a path;
- independent edges are order-monotone between the two color blocks.

Thus D2 is not merely a four-color partition. It reduces the full diameter graph to **two ordered caterpillars connecting opposite pairs of the four blocks**, with every edge of one caterpillar crossing every edge of the other.

---

## 6. Rigidity-circuit compatibility and the rejected shortcut

The full mixed graph has

```math
q+(q-2)=2q-2
```

rows and rigidity rank `2q-3`, with one full-support KKT dependence. It is therefore a realized rigidity circuit.

Before D2 was proved, a plausible shortcut was that no two-component convex-thrackle forest could satisfy Laman-circuit sparsity. Exact small-q enumeration rejects that claim: abstract four-block examples survive the sparsity test.

D2 identifies the actual remaining structure those examples must model. The missing contradiction must use one of:

1. Euclidean diameter lengths across the four blocks;
2. the unique positive KKT stress and reciprocal parallelogram D2.2;
3. C56-G weighted-cycle transfer;
4. the near-Reinhardt perimeter/difference-body constraints from DP/RP;
5. global source packing.

---

## 7. Comparison with `d_H=1`

The two non-Reinhardt cyclic phases now have parallel exact endpoints.

### `d_H=1`

- one spanning diameter tree;
- one-dimensional KKT segment;
- at each KKT endpoint, a distinct zeroed nonleaf tree edge;
- TC gives a `2+2` cut and endpoint reciprocal parallelogram.

### `d_H=2`

- two full tree components;
- zero-dimensional normalized KKT polytope (unique stress);
- the component partition itself is `2+2`;
- D2 gives one permanent reciprocal parallelogram in the unique stress.

Thus reciprocal four-force balance is now universal across both remaining tree phases.

---

## 8. Regression audit

### Two stars

If two star components can be drawn as a diameter thrackle, their centers/leaves must respect D2's four blocks. D2 does not exclude them abstractly.

### Two paths

Allowed if each path is an ordered bipartite caterpillar between its two blocks and all cross-component edges cross.

### More than four component runs

Excluded exactly by the same-color block proof.

### One component in one cyclic interval

Excluded by D2 before KKT: the bipartition classes are nonempty separate blocks, and the other tree separates them.

---

## 9. Next theorem

The sharp `d_H=2` target is now finite:

> classify two ordered convex-thrackle caterpillars on four alternating blocks that can be realized entirely by equal Euclidean diameter chords while the unique positive cycle/diameter KKT stress satisfies D2.2 and C56-G.

A useful first attack is to combine equal-diameter geometry with the four-block order. Cross-component edges all cross, so endpoint interlacing plus the cosine law may force monotonic constraints on block positions that are incompatible with both caterpillar spines being long.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

D2 is a direct finite consequence of DC plus the self-contained TC block argument; the KKT statement uses report-level CY.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Cyclic d_H=2:
  H=T_A disjoint union T_B,
  both nontrivial trees.
Every A-edge crosses every B-edge.
Write tree bipartitions A=A0+A1, B=B0+B1.
For a fixed A-edge, every B-edge toggles sides, so B0/B1 lie on opposite boundary arcs.
Two same-color B vertices lie on the same side of every A-edge; connectedness then
shows no A vertex can split a B-color block. Thus each A0,A1,B0,B1 is one cyclic block.
The blocks necessarily alternate:
  A0 | B0 | A1 | B1.

Sum the unique KKT equilibrium over component A. No diameter edge crosses A|B, so
only the four cycle transition forces remain:
  v_i-v_j+v_k-v_l=0,
therefore
  v_i+v_k=v_j+v_l.
The unique reciprocal force polygon contains an exact transition parallelogram.

Each tree is separately an ordered bipartite caterpillar between its two opposite blocks.
Next: equal-diameter four-block geometry + unique KKT/C56-G.
```
