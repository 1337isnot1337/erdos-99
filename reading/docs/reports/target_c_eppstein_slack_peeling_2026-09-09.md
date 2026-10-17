> Generated reading edition · [exact source](../../../docs/reports/target_c_eppstein_slack_peeling_2026-09-09.md) · source SHA-256 `5c35db47eef12a712223de482da45d405b73dcaa505cdd5a8a21759d0df9a8ec`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-06A95777AEF3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZEP: exact Eppstein peeling slack and the square-grid equality regression

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** exact graph-theoretic audit / near-equality reduction  
**Target:** Target C post-ZF component ledger  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

The post-ZF component identity uses, for every connected unloaded triangle-free penny component,

```math
r(G):=2|V(G)|-\operatorname{diam}(G)-2-|E(G)|\ge0
```

as the exact Eppstein edge slack.

This report extracts the exact slack accounting hidden in Eppstein's inductive proof and records a decisive equality regression. The accounting is useful: small `r(G)` means that Eppstein's deletion process has only a small number of degree-deficient or diameter-increasing steps. But equality does **not** classify the graph as a path or ladder. Square grids have `r(G)=0` exactly.

Therefore the post-ZF near-equality branch cannot be closed by graph-diameter edge extremality alone. Any closing theorem must use the additional mechanical data from ZHT/ZHN: a consecutive macroscopic-force trunk, response localization, or global packing information.

---

## 1. Eppstein's deletion step

Eppstein proves that every connected triangle-free penny graph `G` with `n` vertices, graph diameter `D_G`, and `e` edges satisfies

```math
e\le2n-D_G-2.
\tag{1.1}
```

If `G` has a cycle, his Lemma 2 supplies at least four non-articulation vertices of degree at most two. Choose a graph-diameter pair; at least one such vertex `v` is distinct from the two endpoints. Then

- `G-v` remains connected;
- `d_G(v)<=2`;
- `D_{G-v}>=D_G`.

The theorem follows by induction.

Define

```math
\boxed{r(G)=2|V(G)|-D_G-2-|E(G)|.}
\tag{1.2}
```

For one allowed deletion `G' = G-v`, put

```math
d=\deg_G(v),
\qquad
\Delta=D_{G'}-D_G\ge0.
\tag{1.3}
```

A direct calculation gives the exact recurrence

```math
\boxed{
r(G)=r(G')+(2-d)+\Delta.}
\tag{ZEP1}
```

Both added terms are nonnegative integers.

---

## 2. Full peeling identity

Repeat Eppstein's deletion while the current graph contains a cycle. Let

```math
G=G_0\supset G_1\supset\cdots\supset G_m=T
\tag{2.1}
```

where `T` is the final tree. At step `i`, delete `v_i`, put

```math
d_i=\deg_{G_i}(v_i)\le2,
\qquad
\Delta_i=D_{G_{i+1}}-D_{G_i}\ge0.
\tag{2.2}
```

For the final tree,

```math
|E(T)|=|V(T)|-1,
```

so

```math
\boxed{
r(T)=|V(T)|-D_T-1.}
\tag{2.3}
```

This is exactly the number of tree vertices in excess of a diameter-realizing path.

Telescoping ZEP1 gives:

### Theorem ZEP.1 — exact peeling slack decomposition

```math
\boxed{
 r(G)
 =
 \bigl(|V(T)|-D_T-1\bigr)
 +\sum_{i=0}^{m-1}(2-d_i)
 +\sum_{i=0}^{m-1}\Delta_i.
}
\tag{ZEP2}
```

Every term on the right is a nonnegative integer.

No asymptotic estimate is involved.

---

## 3. Consequences of small Eppstein slack

Put `r=r(G)` and `D=D_G`.

From ZEP2:

```math
\boxed{D_T-D=\sum_i\Delta_i\le r.}
\tag{ZEP3}
```

Also

```math
\boxed{|V(T)|-D_T-1\le r.}
\tag{ZEP4}
```

Hence

```math
\boxed{|V(T)|\le D+2r+1.}
\tag{ZEP5}
```

The number of deletion steps with `d_i<=1` is at most `r`, and the number of steps with `Delta_i>0` is at most `r`. Therefore all but at most `2r` non-tree deletion steps satisfy simultaneously

```math
\boxed{d_i=2,
\qquad
D_{G_{i+1}}=D_{G_i}.}
\tag{ZEP6}
```

In reverse, a graph with `r=o(D)` admits a construction from a tree on at most `D+o(D)` vertices in which all but `o(D)` exceptional additions are degree-two additions that preserve the current graph diameter.

This is the strongest direct stability statement supplied by the induction itself.

---

## 4. Equality case and why it does not classify geometry

If

```math
r(G)=0,
```

then ZEP2 forces

```math
|V(T)|=D_T+1,
\qquad
 d_i=2,
\qquad
\Delta_i=0
```

at every deletion step. Thus the final tree is a diameter-realizing path and every reverse addition is a degree-two, diameter-preserving ear in the evolving abstract graph.

It is tempting to infer that `G` must therefore be path-like. That inference is false.

### Proposition ZEP.2 — square-grid equality regression

Let `Q_L` be the `L x L` unit square grid graph, realized by the integer lattice points

```math
\{0,\ldots,L-1\}^2.
```

It is a triangle-free penny graph. It has

```math
n=L^2,
\qquad
 e=2L(L-1),
\qquad
 D_G=2(L-1).
```

Therefore

```math
\boxed{
e=2n-D_G-2,}
\tag{ZEP7}
```

so

```math
\boxed{r(Q_L)=0}
\tag{ZEP8}
```

for every `L>=2`.

Yet `Q_L` is a genuinely two-dimensional graph with `Theta(L^2)` vertices and cycles. In particular, zero Eppstein slack does not force bounded width, a single ladder, outerplanarity, or one-dimensional geometry.

Eppstein's paper explicitly notes that the degree-two-vertex bound underlying the induction is tight for square grids; the displayed calculation shows that the diameter edge bound itself is also attained by square grids.

---

## 5. Effect on the post-ZF captured cell

For the ZHT/ZHL harmonic cell `I_*`, current main uses

```math
r_*=2|I_*|-\delta_*-2-e_*
\tag{5.1}
```

inside the exact identity

```math
t_*-\delta_*-3=s_*+r_*.
\tag{5.2}
```

If `s_*+r_*=o(D)`, then ZEP applies to `C[I_*]` and gives an Eppstein peeling with only `o(D)` defective steps in the precise sense of ZEP6.

However ZEP.2 shows that this does **not** make the component geometrically axial. A large square-grid-like penny component may have `r_*=0` while remaining genuinely two-dimensional.

The new ZHT/ZHN mechanical information is therefore essential:

- an `Omega(D)` consecutive bridge trunk lies in the component closure;
- every trunk bridge has stress `Omega(D)`;
- almost all bounded trunk blocks have `o(D)` side load;
- those blocks have macroscopic-stress port-to-port corridors and axial normalized-stress limits.

The unresolved near-equality theorem must combine these mechanical facts with the degree-two peeling. Pure graph extremality cannot close it.

---

## 6. A useful exact branch split

For the captured cell, (5.2) gives exactly

```math
\boxed{s_*+r_*=t_*-\delta_*-3.}
\tag{6.1}
```

Hence one may split:

1. **linear local defect:** `s_*+r_*>=cD` for some fixed `c>0`; this already supplies a linear amount of exact pinned-stress/Eppstein defect currency;
2. **near-extremal local cell:** `s_*+r_*=o(D)`; then ZEP6 says all but `o(D)` of Eppstein's peeling steps are degree-two and diameter-preserving, but square-grid equality remains a binding regression.

The second branch is now a well-defined mechanical stability problem:

> exclude a near-Eppstein-extremal triangle-free penny component that simultaneously contains the ZHT/ZHN macroscopic-force trunk and near-neutral bounded block corridors.

---

## 7. Literature input

David Eppstein, *Edge Bounds and Degeneracy of Triangle-Free Penny Graphs and Squaregraphs*, Journal of Graph Algorithms and Applications 22(3), 483--499 (2018), DOI 10.7155/jgaa.00463.

The only imported facts are his Lemma 2 (four non-articulation degree-at-most-two vertices when a cycle is present) and Theorem 2 (`e<=2n-D-2`). The slack recurrence ZEP1--ZEP6 and square-grid substitution are derived here.

---

## 8. Promotion recommendation

**Hold as report.** The peeling identity is exact and reusable, but it is not a closing theorem and does not alter the canonical route map by itself.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For a connected triangle-free penny graph define
    r(G)=2|V|-diam(G)-2-|E|.
Eppstein deletes a non-articulation v of degree d<=2, preserving connectedness, with
D'=diam(G-v)>=D. Exactly
    r(G)=r(G-v)+(2-d)+(D'-D).
Iterating to a tree T gives
    r(G)=|V(T)|-D_T-1 + sum_i(2-d_i) + sum_i(D_{i+1}-D_i).
Hence if r=o(D), only o(D) peel steps have degree<2 or increase diameter.

But this does NOT classify the graph as path-like. The LxL square grid has
    n=L^2,
    e=2L(L-1),
    diam=2(L-1),
so exactly e=2n-diam-2 and r=0 for every L.

Therefore the captured-cell near-equality branch must use ZHT/ZHN force transport;
Eppstein extremality alone cannot close it.
```
