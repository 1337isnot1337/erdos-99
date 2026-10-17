> Generated reading edition · [exact source](../../../docs/reports/target_c_woodall_diameter_topology_2026-09-10.md) · source SHA-256 `3dce8109e6ce8c8e78c31121e38fb9773db34aa19af26e817bb2d718d6864fbd`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A8D2F9C2EC82","canonical":true,"claim_ids":["C-WOODALL"],"claim_statuses":{"C-WOODALL":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Erdős Problem #99 — Woodall classification makes `d_H` an exact diameter-topology switch

**Date:** 2026-09-10  
**Repository base:** `7e1bafe15ba51b4ec7441bf158d7c18e53759485`  
**Run type:** literature import / exact structural reduction  
**Target:** Target C, C-II after ZF  
**Depends on:** full loaded diameter graph `H`, planar diameter-thrackle property, C24, C17, SZ/E597  
**External input:** Woodall's classification of finite straight-line thrackleable graphs  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

The report stack repeatedly uses separate facts that the planar diameter graph has at
most `q` edges, has only odd cycles, and cannot contain two vertex-disjoint odd cycles.
A stronger classical theorem packages the entire graph topology.

Woodall classified finite straight-line thrackleable graphs. In the formulation quoted
as Theorem 2.3 of Collins--Roberts, *Great-circle Tree Thrackles* (arXiv:2110.09679), a
finite graph has a straight-line thrackle drawing if and only if either

1. it contains an odd cycle and every vertex is adjacent to a vertex of that cycle; or
2. it is a disjoint union of caterpillars.

The cited source attributes this classification to D. R. Woodall, *Thrackles and
deadlock*, in *Combinatorial Mathematics and its Applications*, Proc. Oxford
Combinatorial Conference 1969, Academic Press, 1971, pp. 335--347.  Woodall's own
bibliographic page states that the paper gives a complete classification of straight
thrackles without assuming Conway's conjecture.

For the actual loaded diameter graph `H`, this turns

$$
d_H:=q-h
$$

into an exact topology variable:

$$
\boxed{
 d_H=0
 \iff
 H\text{ is connected and contains one odd cycle},
}
\tag{WT.1}
$$

while

$$
\boxed{
 d_H>0
 \iff
 H\text{ is a caterpillar forest with exactly }d_H\text{ components}.
}
\tag{WT.2}
$$

In the cyclic case, every vertex outside the unique odd cycle is a leaf attached
directly to a cycle vertex.  Thus the post-ZF diameter graph has only two global
combinatorial types; there is no third pseudoforest phase with a cycle plus a separate
tree component.

This is useful in the exact `s_Z=0` circuit phase because E597 charges `d_H` with
coefficient three:

$$
\frac{e_{BB}+2s_C}{D}
\ge0.597+\epsilon_{597}+3\frac{d_H}{D}.
$$

The term `d_H/D` is therefore literally normalized caterpillar-component count in the
forest branch, and it vanishes identically in the unique cyclic branch.

---

## 1. The diameter graph is a straight-line thrackle

Let `B` be the loaded terminal set and let

$$
H=(B,E_H),
\qquad q=|B|,
\qquad h=|E_H|.
$$

Every edge of `H` is an actual diameter pair and is drawn as the corresponding
straight segment of length `D`.

Two distinct edges of `H` behave as follows.

- If they share an endpoint, their straight segments meet only at that endpoint. They
  cannot overlap: two distinct points at distance `D` from one endpoint cannot lie on
  the same ray, and opposite rays would put the two other endpoints at distance `2D`.
- If they have four distinct endpoints, the classical planar diameter-graph theorem
  says the two diameter segments cross in their interiors.

Hence every pair of edges meets exactly once, either at a common endpoint or at one
proper crossing. Therefore

$$
\boxed{H\text{ is a finite straight-line thrackle}.}
\tag{1.1}
$$

Every vertex of `H` has positive degree by the definition of the loaded terminal set.

---

## 2. Woodall gives the global dichotomy

Apply the straight-line thrackle classification to `H`.

### Case F: no odd cycle

Then `H` is a disjoint union of caterpillars.  Since every loaded terminal has positive
diameter degree, there are no isolated-vertex components.

If the component sizes are `q_1,...,q_c`, each caterpillar is a tree, so

$$
h=\sum_{j=1}^c(q_j-1)=q-c.
$$

Thus

$$
\boxed{c=q-h=d_H.}
\tag{2.1}
$$

In particular a forest phase automatically has `d_H>=1`, and `d_H` is exactly its
number of diameter components.

### Case C: an odd cycle exists

Let `Gamma` be the odd cycle supplied by Woodall and let it have `r` vertices and
edges.  Every one of the remaining `q-r` vertices is adjacent to a cycle vertex.
Therefore

$$
h\ge r+(q-r)=q.
\tag{2.2}
$$

The Hopf--Pannwitz bound for a planar diameter graph gives

$$
h\le q.
\tag{2.3}
$$

Hence equality holds throughout:

$$
\boxed{h=q,\qquad d_H=0.}
\tag{2.4}
$$

Moreover every outside vertex contributes exactly one edge to the cycle, and there can
be no other edge.  Thus every outside vertex is a leaf attached directly to a cycle
vertex.  The graph is connected and unicyclic.

This proves WT.1--WT.2.

A useful equivalent formulation is

$$
\boxed{
H\text{ contains a cycle}\iff d_H=0,
\qquad
H\text{ is a forest}\iff d_H>0.
}
\tag{2.5}
$$

---

## 3. Compatibility with the existing Target C stack

The new statement strengthens several earlier local descriptions but does not conflict
with them.

### 3.1 C17 cycle girth

In the cyclic case the unique cycle is an actual diameter cycle. C17 therefore gives

$$
 r>
 \frac{\pi D}{\sqrt{12(2D+1)}}
 =\Omega(\sqrt D).
\tag{3.1}
$$

Thus the cyclic Woodall core cannot have bounded size in an unbounded global-minimizer
sequence.

### 3.2 C24 common-route split

The relative-interior normalization makes `H` the positive diameter support used by
C24.  Since the cyclic case contains an odd cycle, C24.6 forces the common
bridge-block intersection `I_*` to be exactly one block.  Therefore

$$
\boxed{
 d_H=0
 \Longrightarrow
 \text{all positive diameter routes meet in one contact bridge block, not a common bridge}.
}
\tag{3.2}
$$

If `d_H>0`, Woodall says `H` is globally a caterpillar forest whether or not the C24
common intersection degenerates to one block.  This removes the need to derive
caterpillar structure only after assuming a universal bridge cut.

### 3.3 No cycle-plus-forest hybrid

Earlier pseudoforest language allowed, at the level of edge counts alone, the picture

```text
one odd unicyclic component + one or more separate tree components.
```

Woodall excludes it for a straight-line thrackle.  A post-ZF loaded diameter graph is
either wholly in the cyclic connected case or wholly in the caterpillar-forest case.

---

## 4. Consequence for the `s_Z=0` circuit phase

E597 proves that for some absolute `epsilon_597>0`, every sufficiently large
`s_Z=0` survivor satisfies

$$
\frac{e_{BB}+2s_C}{D}
\ge
0.597+\epsilon_{597}+3\frac{d_H}{D}.
\tag{4.1}
$$

Woodall now gives the exact interpretation

$$
\boxed{
\frac{d_H}{D}
=
\frac{\#\{\text{diameter caterpillar components}\}}D
}
\tag{4.2}
$$

throughout the forest branch.

Thus, for any fixed `L`, a hypothetical circuit-phase sequence satisfying

$$
\frac{e_{BB}+2s_C}{D}\le L+o(1)
$$

has at most

$$
\boxed{
\left(\frac{L-0.597}{3}+o(1)\right)D
}
\tag{4.3}
$$

diameter components, unless it is in the single connected cyclic branch.

For example, any sequence with ordinary surplus at most `0.600D+o(D)` has either the
unique cyclic topology or at most `0.001D+o(D)` caterpillar components.

This is not an upper bound on the ordinary surplus, so it is not a Level I closure.
Its role is to make the next case split topologically exact.

---

## 5. Regression audit

- **Crossing diameter matching:** allowed. It is a disjoint union of two-vertex
  caterpillars and has `d_H=q/2`.
- **Diameter star:** allowed. It is one caterpillar and has `d_H=1`.
- **Regular odd shell:** its diameter graph is the cyclic Woodall case with `d_H=0`.
  It remains a valid graph regression, although it lies in `s_Z=2`, not the exact
  circuit phase.
- **Cycle with pendant diameter leaves:** allowed. The theorem does not force the
  cyclic component to be a bare cycle.
- **Cycle plus separate tree:** excluded by the straight-line thrackle classification.
- **Contact-isolated source points:** irrelevant to the statement. `H` is the loaded
  terminal graph used by the post-ZF stress; no assertion is made about diameter edges
  whose endpoints are absent from that terminal set outside the restored C-II scope.

---

## 6. Exact next branch split

The `s_Z=0` circuit phase can now be attacked as two disjoint cases.

### WT-C: cyclic diameter support

$$
d_H=0,
$$

`H` is one odd cycle of length `Omega(sqrt D)` with possible pendant leaves, and C24
puts every diameter route through one bridgeless contact hub block.  The E597 currency
reduces to

$$
\frac{e_{BB}+2s_C}{D}>0.597.
$$

A useful next theorem here must use the cycle/leaf geometry, not a generic thrackle
edge count.

### WT-F: caterpillar forest

$$
d_H\ge1,
$$

`H` has exactly `d_H` caterpillar components.  Every component-count unit is already
charged three times in E597.  A useful next theorem is a contact-bypass or circuit
sparsity bound that sums over those caterpillar components without reusing the same
contact attachment currency.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Woodall classifies finite straight-line thrackles.  The full loaded diameter graph H
is such a thrackle.

Therefore exactly one of the following holds.

F: H is a disjoint union of caterpillar trees.
   If c_H is its component count, h=q-c_H, so
       d_H=q-h=c_H>=1.

C: H contains an odd cycle.
   Woodall says every vertex is adjacent to that cycle.  Counting one cycle edge per
   cycle vertex and at least one attachment edge per outside vertex gives h>=q;
   Hopf-Pannwitz gives h<=q.  Hence h=q, d_H=0, and every outside vertex is exactly a
   pendant leaf.  H is connected and unicyclic.

So
    d_H=0 iff H is the connected cyclic Woodall case,
    d_H>0 iff H is a caterpillar forest with exactly d_H components.

C17 makes the unique cycle Omega(sqrt D).  C24 says the cyclic case has a single
common contact hub block rather than a universal common bridge.

In s_Z=0, E597 becomes an exact topology charge:
    (e_BB+2s_C)/D >= 0.597+epsilon + 3 c_H/D
in the forest branch.

Next split:
    WT-C = connected odd cycle + leaves;
    WT-F = d_H caterpillar components.
```
