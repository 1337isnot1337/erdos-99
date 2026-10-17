> Generated reading edition · [exact source](../../../docs/reports/target_c_zero_stress_surplus_laman_circuit_2026-09-09.md) · source SHA-256 `43d3033527cbb49c4de25afb5f042c093a3903e1e778f2d34472a913e13f62e1`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-D93B23A832A8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — zero mixed-stress surplus gives a Laman-circuit graph

**Date:** 2026-09-09  
**Run type:** exact rigidity-matroid / graph-sparsity theorem  
**Target:** Target C C-II after ZF/EC  
**Depends on:** ZF mixed rigidity rank, EC extreme-stress circuit theorem  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

EC proves that when

```math
s_Z=e+h-(2v-2)=0,
```

the entire actual mixed row set `C union H` is one circuit of the rigidity-row matroid at the source coordinates. Because ZF simultaneously gives full planar rigidity rank `2v-3`, this coordinate-matroid statement forces the underlying mixed graph to satisfy the ordinary `(2,3)` Laman-circuit sparsity counts, even though the source coordinates are not assumed generic.

The same argument gives redundant infinitesimal rigidity after deleting any one actual contact or diameter row and a four-edge lower bound across every mixed cut with at least two vertices on each side.

---

## 1. Full circuit data

Assume throughout

```math
\boxed{s_Z=0.}
\tag{LC.1}
```

Then

```math
\boxed{e+h=2v-2.}
\tag{LC.2}
```

ZF gives

```math
\boxed{\operatorname{rank}R(C\cup H)=2v-3.}
\tag{LC.3}
```

EC.4 says the full actual row set is a single circuit: its one-dimensional dependence uses every row, and every proper row subset is linearly independent.

For sufficiently large Target C sources `D>1`, a pair cannot be simultaneously a unit contact and a diameter pair, so the mixed graph is simple.

---

## 2. Every proper induced mixed subgraph satisfies the Laman count

Let `X` be a proper vertex subset with

```math
2\le |X|<v,
```

and let

```math
m(X):=|C[X]|+|H[X]|.
```

The rows supported entirely on `X` form a proper subset of the full circuit and are therefore linearly independent.

For any set of at least two distinct planar points, the rigidity matrix on those vertices has the three independent infinitesimal Euclidean motions in its kernel: two translations and one rotation. Consequently any rigidity-row family supported on `X` has rank at most

```math
2|X|-3.
```

Independence of the induced row family therefore gives

```math
\boxed{
m(X)\le2|X|-3.
}
\tag{LC.4}
```

Together with the full count LC.2, this is exactly the graph-theoretic `(2,3)`-circuit count:

```math
\boxed{
|E(C\cup H)|=2v-2,
\qquad
|E((C\cup H)[X])|\le2|X|-3
\text{ for every proper }X.
}
\tag{LC.5}
```

### Scope

LC.5 is a combinatorial consequence of the actual-coordinate circuit. It does **not** assert that arbitrary generic realizations of the same graph preserve the Target C stress signs or geometry.

---

## 3. Deleting any one mixed edge leaves an infinitesimally rigid framework

Let `f` be any actual contact or diameter edge. Since the full row set is a circuit,

```math
(C\cup H)\setminus\{f\}
```

is linearly independent. It has

```math
(2v-2)-1=2v-3
```

rows. Hence its rigidity matrix has rank exactly `2v-3`.

### Theorem LC.1 — redundant equality rigidity

For every mixed edge `f`,

```math
\boxed{
\operatorname{rank}R((C\cup H)\setminus\{f\})=2v-3.
}
\tag{LC.6}
```

Thus deleting any single active equality bar leaves an infinitesimally rigid planar framework.

This is redundancy for the **equality** framework. It does not by itself integrate to a feasible packing motion after deleting one contact or diameter inequality.

---

## 4. Minimum mixed degree and cut bounds

Take one vertex `x` and apply LC.4 to

```math
X=V\setminus\{x\}.
```

Then

```math
(2v-2)-\deg_{C\cup H}(x)
\le2(v-1)-3=2v-5.
```

Therefore

```math
\boxed{\deg_{C\cup H}(x)\ge3\quad\text{for every vertex }x.}
\tag{LC.7}
```

Now partition the vertex set as

```math
V=S\sqcup T,
\qquad |S|,|T|\ge2.
```

Let `partial(S,T)` be the mixed edges crossing the cut. Applying LC.4 to both shores,

```math
\begin{aligned}
|\partial(S,T)|
&=(2v-2)-m(S)-m(T)\\
&\ge(2v-2)-(2|S|-3)-(2|T|-3)\\
&=4.
\end{aligned}
```

Hence

```math
\boxed{
|\partial(S,T)|\ge4
\quad\text{whenever }|S|,|T|\ge2.
}
\tag{LC.8}
```

Singleton cuts have size at least three by LC.7. Thus the mixed graph is at least three-edge-connected, and every nontrivial nonsingleton cut has four-edge capacity.

---

## 5. Loaded-boundary induced sparsity

Let `B` be the `q` actual diameter endpoints. If the nonloaded set `I=V\setminus B` is nonempty, then `B` is a proper vertex subset. LC.4 gives

```math
\boxed{
e_{BB}+h\le2q-3.}
\tag{LC.9}
```

Since

```math
h=q-d_H,
```

this becomes

```math
\boxed{
e_{BB}\le q+d_H-3.}
\tag{LC.10}
```

The inequality is exact but is not by itself a contradiction; it is recorded because HB gives an independent lower bound on the same `e_BB` currency.

Similarly, every proper vertex-supported mixed subframework inherits LC.4. This can be inserted into future attachment-cell or bridge-block arguments without assuming genericity.

---

## 6. Local boundary consequences

Every loaded terminal is incident to at least one diameter edge and C35 gives

```math
1\le\deg_C(b)\le3.
```

LC.7 therefore implies, in the `s_Z=0` branch,

```math
\deg_H(b)+\deg_C(b)\ge3.
\tag{LC.11}
```

In particular a loaded vertex with only one positive/full contact incidence must satisfy

```math
\boxed{\deg_H(b)\ge2.}
\tag{LC.12}
```

Thus contact-degree-one loaded terminals necessarily contribute to the diameter branching currency

```math
r_H=\sum_{b\in B}(\deg_H(b)-1).
```

No converse is claimed; one high-degree diameter hub can carry substantial branching.

---

## 7. Equality-framework interpretation

The circuit statement means every actual mixed row is both

1. necessary for the unique full-support self-stress dependence, and
2. redundant for infinitesimal equality rigidity.

Indeed removing a row kills the unique self-stress but leaves a basis of the planar rigidity row space.

This is a strong normal form. In the `s_Z=0` branch there is no hidden linear stress-space multiplicity left: all remaining difficulty is geometric/sign/topological.

A possible next route is to combine LC.8 with the contact-planar / diameter-thrackle coloring of the cut edges. Every contact bridge must be accompanied by at least three additional mixed crossing edges; the diameter-thrackle structure may restrict how those extra edges can be distributed across nested contact cuts.

---

## 8. Regressions and cautions

### Nongeneric coordinates

The proof never assumes genericity. LC.4 follows because a proper row subset of an actual-coordinate circuit is independent, and any independent planar rigidity row family has at most `2|X|-3` rows.

### Redundant equality rigidity is not contact minimality

Deleting one contact row from the equality framework leaves only Euclidean infinitesimal flexes. This does not prove there is a finite packing motion that removes that contact while respecting all remaining one-sided inequalities.

### Mixed graph is nonplanar

The contact subgraph is planar, but diameter edges cross. LC.5 is a sparsity statement for the mixed abstract graph, not a planar Euler bound.

### `B=V`

LC.9 is stated only when `B` is proper. If every core vertex is loaded, apply the full count instead; do not treat `B` as a proper Laman subset.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| proper induced mixed Laman count | proved | EC circuit + planar rigidity rank ceiling |
| full mixed graph is a `(2,3)` circuit | proved in `s_Z=0` | LC.2 + induced counts |
| deleting any edge leaves rank `2v-3` | proved | circuit independence and row count |
| minimum mixed degree at least 3 | proved | induced complement count |
| every nonsingleton shore cut has at least 4 mixed edges | proved | two induced sparsity bounds |
| finite packing release after deleting an edge | not proved | equality rigidity is one-sidedly insufficient |
| Level I | still open | need color/geometric use of the circuit structure |

---

## 10. Next target

For `s_Z=0`, exploit the `(2,3)` circuit together with:

- planar contact cuts and C51 articulation structure;
- diameter-thrackle/caterpillar geometry;
- C35 loaded contact degree at most three;
- the post-PI lower bounds on `r_H` and `e_BB+2s_C`.

For `s_Z>0`, use EC's at-most-`s_Z+1` PSD circuit cover as the stability replacement for the exact one-circuit normal form.
