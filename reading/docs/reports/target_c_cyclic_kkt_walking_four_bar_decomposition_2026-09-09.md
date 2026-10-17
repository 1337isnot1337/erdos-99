> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_kkt_walking_four_bar_decomposition_2026-09-09.md) · source SHA-256 `9b766330196b84553b4b8b287e28824a8d8353c7137df5cc53d5ee698d799954`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-C8EE18A86344","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — every `d_H=0` KKT extreme is a walking two-body four-bar circuit

**Date:** 2026-09-09  
**Run type:** exact rigidity / stress-polytope / Reinhardt-composition bridge  
**Target:** Target C cyclic `d_H=0` Reinhardt endpoint  
**Depends on:** PP exact KKT polar polygon in this PR; PR #125 LC exact Reuleaux leaf composition; maximal-rank extreme support from CG/EZ  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

PP classifies every normalized KKT extreme by deleting exactly two unique-cycle diameter edges at step-two positions. LC independently identifies the pendant-leaf counts with the integer Reuleaux composition

```math
\ell_i=p_i+1,
\qquad
\sum_i\ell_i=q.
```

Together they give a rigid body-bar normal form at **every vertex of the KKT polygon**.

Let the odd diameter-cycle vertices be

```math
v_0,v_1,\ldots,v_{r-1}
```

in graph-cycle order, and write

```math
e_i=v_iv_{i+1}
```

for the cycle edges, indices modulo `r`.

PP extreme `s_i` has

```math
\beta_{e_i}(s_i)=\beta_{e_{i+2}}(s_i)=0
```

and every other contact/selected diameter coefficient strictly positive.

Hence the selected diameter forest has one short component

```math
S_i
```

whose cycle core is the surviving middle edge

```math
e_{i+1}=v_{i+1}v_{i+2}.
```

### Theorem WF — walking four-bar decomposition

For `r>=5`, the short component `S_i` has

```math
\boxed{|S_i|=\ell_{i+1}+\ell_{i+2}.}
\tag{WF.1}
```

Its selected diameter graph is a tree with

```math
\boxed{|E_H(S_i)|=|S_i|-1,}
\tag{WF.2}
```

and the shell contact cycle induces exactly two disjoint contact paths on `S_i`, with vertex counts

```math
\boxed{\ell_{i+1}\quad\text{and}\quad\ell_{i+2}.}
\tag{WF.3}
```

Therefore

```math
\boxed{|E_C(S_i)|=|S_i|-2,}
\tag{WF.4}
```

so the complete mixed support induced on `S_i` has exactly

```math
\boxed{2|S_i|-3}
\tag{WF.5}
```

rows and is infinitesimally isostatic.

The complementary diameter component is also internally isostatic. Exactly four shell contacts cross the cut

```math
S_i\mid S_i^c,
```

and no selected diameter edge crosses it. After quotienting the two internal isostatic bodies, those four contacts form a rank-three body-bar circuit with one positive alternating KKT dependence.

Thus every KKT-polygon vertex has the exact architecture

```text
short isostatic body of size ell_{i+1}+ell_{i+2}
        ||  four unit shell bars  ||
complementary isostatic body of size q-ell_{i+1}-ell_{i+2}.
```

As `i` advances around `Z/rZ`, the short body moves once around the odd diameter cycle. The complete `r`-vertex KKT polygon is therefore an `r`-cycle of overlapping two-body/four-bar rigidity circuits whose short-body sizes are the adjacent composition sums

```math
\boxed{m_i:=\ell_{i+1}+\ell_{i+2}.}
\tag{WF.6}
```

This is the first exact bridge between the KKT-polygon vertices and the Reuleaux branching composition.

---

## 1. The short selected diameter component

The full diameter graph in `d_H=0` is one connected unicyclic graph: the odd cycle

```math
C_r=(v_0v_1\cdots v_{r-1}v_0)
```

with `p_j` degree-one leaves attached directly to `v_j`.

At extreme `s_i`, PP deletes exactly

```math
e_i=v_iv_{i+1},
\qquad
e_{i+2}=v_{i+2}v_{i+3}.
```

The unique surviving cycle segment between those deleted edges on the short side is

```math
e_{i+1}=v_{i+1}v_{i+2}.
```

Therefore one selected diameter component contains exactly

1. `v_{i+1}` and `v_{i+2}`;
2. all `p_{i+1}` leaves attached to `v_{i+1}`;
3. all `p_{i+2}` leaves attached to `v_{i+2}`.

No other diameter vertex can lie in this component because every other cycle route is cut by `e_i,e_{i+2}` and every off-cycle edge is pendant.

Thus

```math
|S_i|
=2+p_{i+1}+p_{i+2}.
```

LC gives

```math
p_j=\ell_j-1,
```

so

```math
|S_i|
=\ell_{i+1}+\ell_{i+2},
```

which proves WF.1.

The selected diameter edges inside `S_i` are

- the middle cycle edge `e_{i+1}`;
- all `p_{i+1}+p_{i+2}` pendant edges.

Hence

```math
|E_H(S_i)|
=1+p_{i+1}+p_{i+2}
=|S_i|-1.
```

They form a tree, proving WF.2.

---

## 2. The two shell intervals inside the short body

LC partitions the shell contact cycle into paths

```math
P_j:v_{j-1}\leadsto v_{j+1},
```

where the internal vertices of `P_j` are exactly the `p_j` diameter leaves centered at `v_j`, and

```math
|E(P_j)|=\ell_j.
```

Consider `P_{i+1}`. It runs

```math
v_i
\;--\;
[\text{the }p_{i+1}\text{ leaves at }v_{i+1}]
\;--\;
v_{i+2}.
```

The short component contains every vertex of this path except `v_i`. Thus its induced part of `P_{i+1}` has

```math
\ell_{i+1}
```

vertices and

```math
\ell_{i+1}-1
```

internal contact edges.

Likewise `P_{i+2}` runs

```math
v_{i+1}
\;--\;
[\text{the }p_{i+2}\text{ leaves at }v_{i+2}]
\;--\;
v_{i+3},
```

and the short component contains every vertex except `v_{i+3}`. This gives a second induced shell path with

```math
\ell_{i+2}
```

vertices and

```math
\ell_{i+2}-1
```

internal contact edges.

These two induced paths are vertex-disjoint: the first contains `v_{i+2}` but not `v_{i+1}`, while the second contains `v_{i+1}` but not `v_{i+2}`, and their internal vertices are disjoint leaf sets.

Together they exhaust `S_i`. Therefore the shell contact graph induced on `S_i` has exactly two components with vertex counts `ell_{i+1},ell_{i+2}` and

```math
|E_C(S_i)|
=(\ell_{i+1}-1)+(\ell_{i+2}-1)
=|S_i|-2.
```

This proves WF.3-WF.4.

Because `r>=5`, the complementary selected diameter component contains at least one cycle vertex on each of the two complementary shell intervals, so the `S_i` vertices really do occupy two separated shell intervals. Consequently exactly four contact-cycle edges cross the cut.

---

## 3. The short body is isostatic

The mixed rows induced on `S_i` consist of

```math
|S_i|-1
```

selected diameter-tree rows and

```math
|S_i|-2
```

shell-contact rows. Hence their total number is

```math
2|S_i|-3.
```

EZ/PP give that the full extreme mixed support is an actual-coordinate rigidity circuit: it has `2q-2` rows, rank `2q-3`, and its unique row dependence is the full-support KKT stress at the extreme.

Therefore every proper subset of the extreme support rows is independent.

The rows induced on `S_i` are a proper subset because four cross contacts and all complement rows are omitted. Thus all `2|S_i|-3` induced rows are independent.

This is the maximal planar rigidity rank on `|S_i|` vertices, so the short mixed framework is infinitesimally isostatic.

### Corollary WF.1

The short body is abstractly a Laman graph and is realized without rank degeneracy at the exact Reinhardt geometry.

No generic-coordinate assumption is used.

---

## 4. The complement is also isostatic

The selected diameter forest has exactly two components, so the complement `S_i^c` is a diameter tree on

```math
q-|S_i|
```

vertices and has

```math
q-|S_i|-1
```

diameter edges.

Because the contact cycle crosses the cut exactly four times, its induced complement contact graph also consists of two paths and has

```math
q-|S_i|-2
```

edges.

Thus the complement mixed row count is

```math
(q-|S_i|-1)+(q-|S_i|-2)
=2(q-|S_i|)-3.
```

Again this is a proper row subset of the full extreme circuit, hence independent. Therefore the complement is also isostatic.

---

## 5. Four transition contacts form the entire inter-body circuit

Delete the four shell contacts crossing

```math
S_i\mid S_i^c.
```

The remaining extreme support is the disjoint union of the two isostatic bodies. Their total rank is

```math
[2|S_i|-3]
+[2(q-|S_i|)-3]
=2q-6.
```

The complete extreme support has rank

```math
2q-3.
```

Therefore the four cross-contact rows raise rank by exactly three. Quotienting the two internal rigid bodies leaves the three-dimensional relative rigid-motion space, on which the four unit bars have rank three and one dependence.

The extreme KKT stress is strictly positive on every shell contact. Summing equilibrium over one body gives the usual alternating four-force and four-moment relation among the transition contacts.

Thus:

### Theorem WF.2 — every PP extreme is a four-bar body circuit

Each vertex of the KKT polygon is a two-rigid-body four-bar circuit, with the two body sizes given exactly by

```math
\ell_{i+1}+\ell_{i+2}
\quad\text{and}\quad
q-\ell_{i+1}-\ell_{i+2}.
```

`\square`

---

## 6. The short body walks around the diameter core

PP indexes the `r` KKT extremes cyclically by

```math
i\in\mathbb Z/r\mathbb Z,
```

with zero pair

```math
\{e_i,e_{i+2}\}.
```

Therefore successive extreme short bodies have cycle cores

```math
e_{i+1},
\quad e_{i+2},
\quad e_{i+3},\ldots .
```

The short body moves one cycle edge per KKT vertex and visits every diameter-cycle edge exactly once.

Its size sequence is

```math
\boxed{
 m_i=\ell_{i+1}+\ell_{i+2}.
}
```

Hence

```math
\sum_i m_i
=2\sum_i\ell_i
=2q,
\tag{6.1}
```

so the average short-body size is

```math
\boxed{\frac{2q}{r}.}
\tag{6.2}
```

PR #125 AE gives

```math
r\ge(0.6917794-o(1))\sqrt D,
```

and `q~pi D`, so this upper information alone permits average size `O(sqrt D)`; it does not produce a contradiction.

The cubic energy gives more distributionally. Since

```math
(a+b)^3\le4(a^3+b^3)
\qquad(a,b\ge0),
```

```math
\sum_i m_i^3
\le
8\sum_i\ell_i^3.
```

Thus AE implies

```math
\boxed{
\sum_i m_i^3
\le
(384C_W+o(1))D^2.
}
\tag{6.3}
```

In particular every extreme short-body size satisfies

```math
\boxed{
 m_i=O(D^{2/3}).
}
\tag{6.4}
```

This imports the full composition-energy constraint directly into the family of extreme rigidity circuits.

---

## 7. What this changes

Before WF, the exact KKT polygon and the Reuleaux composition were parallel descriptions:

```text
PP: r extreme PSD rigidity circuits;
AE: cubic budget on r composition parts ell_i.
```

WF identifies them pointwise:

```text
KKT extreme i
  <-> delete cycle edges i and i+2
  <-> short diameter component centered on surviving edge i+1
  <-> two shell blocks of sizes ell_{i+1}, ell_{i+2}
  <-> isostatic short body of size m_i=ell_{i+1}+ell_{i+2}
  <-> four transition unit bars to the complementary isostatic body.
```

Thus every composition part participates in exactly two consecutive extreme short bodies.

---

## 8. Next theorem

The exact next mechanical target is now finite and local:

> characterize the unique four-bar body stress for the short body in terms of the two adjacent arc lengths `ell_{i+1},ell_{i+2}` and compare consecutive extremes `i,i+1`.

Because the two short bodies overlap in one diameter-cycle vertex and one pendant-star family, their four transition contacts interlace on the same Reinhardt shell. A recurrence for the transition stress ratios around the `r` KKT extremes could convert the cubic composition budget into a global stress incompatibility.

A second source-wide route is to use the fact that **every** extreme circuit cuts off a body of size `O(D^(2/3))` while the complete source contains `Theta(D^2)` interior rattlers invisible to all these circuit cuts.

---

## 9. Regression audit

- The theorem is stated for `r>=5`. The large-source branch has `r=Omega(sqrt D)`, so this is automatic eventually. The triangular `r=3` edge case can be handled separately and is already excluded asymptotically.
- `S_i` is a selected-diameter component, not a full-source component. Contact-isolated interior source points are not vertices of the mechanical framework and are not assigned to either body.
- The two shell intervals inside `S_i` can be singletons when the corresponding `ell` equals one; the edge counts remain valid.
- No claim is made that the four transition contact weights depend only on the two integers `ell_{i+1},ell_{i+2}`. Their exact positions in the global Reinhardt shell can matter.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

PP extreme i zeros cycle edges e_i and e_{i+2}. The short selected-diameter component
has core edge e_{i+1}=v_{i+1}v_{i+2} plus all leaves at those two cycle vertices.
LC gives p_j=ell_j-1, so
  |S_i|=ell_{i+1}+ell_{i+2}=:m_i.
Its diameter graph is a tree with m_i-1 edges.

LC shell paths show S_i occupies two disjoint contact intervals of vertex counts
ell_{i+1},ell_{i+2}; hence it has m_i-2 internal contact edges and exactly four
crossing shell contacts. Mixed induced rows =2m_i-3.

The whole PP extreme support is a full-support rigidity circuit, so every proper row
subset is independent. Therefore S_i is isostatic. The complement has the same count
and is isostatic. The four cross contacts have body-bar rank 3 and one positive
alternating KKT dependence.

Thus every KKT-polygon vertex is a two-isostatic-body/four-bar circuit. As i advances,
the short body walks around the odd diameter cycle. Its size sequence is
  m_i=ell_{i+1}+ell_{i+2}, sum m_i=2q.
AE further gives
  sum m_i^3 <= (384 C_W+o(1))D^2,
so every extreme cuts off only O(D^(2/3)) mechanical vertices.

Next: derive a recurrence for the four transition stress ratios across consecutive
walking extremes and couple it to the ell_i composition.
```
