> Generated reading edition · [exact source](../../../docs/reports/target_c_bridge_reciprocal_2026-08-31.md) · source SHA-256 `175f3901a4bc97fd198b12dbc674e43977738fd93b8e60c7c5b62bad8a8e1ca6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7A999D05248E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: contact bridges as reciprocal diagonals

**Date:** 2026-08-31  
**Repository state:** `429264f9c294ef026aa722345db442155ed846ed`  
**Run type:** proof / structural reduction  
**Target:** C-II  
**Depends on:** Target C force-hull, support-connectivity, and reciprocal-polygon theorems  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This note identifies the exact reciprocal-geometric meaning of a bridge in the
positive KKT contact network.  Removing a positive unit-contact bridge partitions the
loaded force-hull vertices into two cyclic intervals.  The resultant positive diameter
reaction on either side is carried by that one bridge.  In the reciprocal force
polygon, the corresponding boundary arc therefore closes by a diagonal perpendicular
to the primal bridge, and the diagonal length is exactly the bridge stress.

A useful quantitative corollary is that every pairwise disjoint family of bridge-side
subtrees carries total bridge stress at most the reciprocal perimeter `P_*<=2D`.
In particular all leaf bridges together carry only `O(D)` of the normalized total
contact stress `D^2`.

This does not yet close C-II: nested internal bridges can still carry large total
stress.  It converts that residual articulation structure into a laminar family of
actual reciprocal diagonals, where the next quantitative theorem can operate.

---

## 1. Setup

Fix a normalized KKT stress `(alpha,beta)`.  Use the canonical notation

```math
C_+=\{ij:\alpha_{ij}>0\},
\qquad
H_+=\{ij:\beta_{ij}>0\},
\tag{C20.1}
```

```math
B_+=V(H_+),
\qquad
F=\operatorname{conv}B_+
 =\operatorname{conv}V(C_+),
\tag{C20.2}
```
and
```math
g_b=\sum_{bk\in H_+}\beta_{bk}(b-k)
   =\sum_{bc\in C_+}\alpha_{bc}(b-c)
\qquad(b\in B_+).
\tag{C20.3}
```
At a positive-contact vertex not in `B_+`, the corresponding right-hand side is zero.
Theorem C12 makes `C_+` connected, and every `g_b` lies strictly in the outward normal
cone of the force hull at `b`.

Order `B_+=\{b_1,\ldots,b_q\}` cyclically around `partial F`.  The reciprocal force
polygon `F^*` has, in this order, side vectors
```math
e_b=Jg_b,
\tag{C20.4}
```
where `J` is rotation by `pi/2`.  Its perimeter is
```math
P_*=\sum_{b\in B_+}|g_b|\le2D.
\tag{C20.5}
```
The normalized virial identity gives
```math
\sum_{e\in C_+}\alpha_e=D^2.
\tag{C20.6}
```

---

## 2. A contact bridge cuts a cyclic interval of loaded boundary vertices

Let `uv in C_+` be a bridge of the positive contact graph.  Removing it gives two
connected components `S,T`, with `u in S`, `v in T`.  Put
```math
B_S=B_+\cap S,
\qquad
B_T=B_+\cap T.
\tag{C20.7}
```

### Lemma C20.1 (bridge-side reaction sets are cyclic intervals)

Both `B_S` and `B_T` are nonempty cyclic intervals in the boundary order of `B_+`.

#### Proof

First sum KKT equilibrium over the vertices of `S`.  All positive contact forces
internal to `S` cancel.  The only positive contact edge leaving `S` is the bridge, so
```math
\sum_{b\in B_S}g_b
=\alpha_{uv}(u-v)\ne0.
\tag{C20.8}
```
Thus `B_S` is nonempty.  The symmetric equation for `T` makes `B_T` nonempty.

Suppose the two sets alternate on the force-hull boundary: there are boundary vertices
in cyclic order `a,b,c,d` with `a,c in B_S` and `b,d in B_T`.  Because `S` is
connected, a positive-contact path inside `S` joins `a` to `c`; similarly a path
inside `T` joins `b` to `d`.  Both polygonal paths lie in the convex disk `F`.
Alternating boundary endpoints force the two paths to intersect.  They share no vertex,
and two disjoint unit-contact edges cannot cross properly.  Contradiction.

Hence `{B_S,B_T}` is a two-block noncrossing partition of the cyclic boundary order.
For two complementary blocks this is equivalent to each block being a cyclic
interval. `\square`

Equation (C20.8) is itself an exact static cut law: one unit bridge carries the entire
resultant diameter reaction of either side.

---

## 3. Reciprocal diagonal theorem

Choose the orientation of the cyclic order so that
```math
B_S=\{b_i,b_{i+1},\ldots,b_j\}
\tag{C20.9}
```
for one consecutive arc, with indices interpreted cyclically.  Let `z_i,z_{j+1}` be
the reciprocal-polygon vertices immediately before and after that arc, so
```math
z_{j+1}-z_i
=\sum_{b\in B_S}e_b.
\tag{C20.10}
```

### Theorem C20.2 (positive contact bridge = reciprocal diagonal)

For every positive contact bridge `uv`,
```math
\boxed{
z_{j+1}-z_i
=\alpha_{uv}J(u-v).}
\tag{C20.11}
```
Consequently the reciprocal chord closing the `B_S` boundary arc is perpendicular to
the primal bridge and has length
```math
\boxed{|z_{j+1}-z_i|=\alpha_{uv}.}
\tag{C20.12}
```

Moreover the resultant reaction of the side `S` has its line of action through the
bridge endpoint `u`:
```math
\boxed{
\sum_{b\in B_S}(b-u)\times g_b=0.
}
\tag{C20.13}
```
The symmetric resultant on `T` has line of action through `v`.

#### Proof

Rotate (C20.8) by `J` and use (C20.4):
```math
\sum_{b\in B_S}e_b
=J\sum_{b\in B_S}g_b
=\alpha_{uv}J(u-v),
```
which is (C20.11).  Since `|u-v|=1`, (C20.12) follows.

For the moment identity, take scalar moments of the vertex equilibrium equations over
all vertices of `S`.  An internal contact edge `xy` contributes
```math
\alpha_{xy}\bigl(x\times(x-y)+y\times(y-x)\bigr)=0.
\tag{C20.14}
```
The bridge contributes
```math
\alpha_{uv}u\times(u-v).
\tag{C20.15}
```
Hence
```math
\sum_{b\in B_S}b\times g_b
=\alpha_{uv}u\times(u-v)
=u\times\sum_{b\in B_S}g_b,
\tag{C20.16}
```
where the last equality uses (C20.8).  Rearranging gives (C20.13).  The `T` statement
is symmetric. `\square`

Thus bridge cuts are not arbitrary graph articulations.  They are encoded as a
laminar family of diagonals of the same convex reciprocal polygon that carries the
mixed-area identity `2V(F,F^*)=D^2`.

---

## 4. Antichain stress budget

A collection of oriented contact bridges `e_r=u_rv_r` determines bridge-side
components `S_r` by choosing one component of `C_+-e_r` for each edge.

### Theorem C20.3 (disjoint bridge-side budget)

Suppose the chosen components `S_1,...,S_k` are pairwise vertex-disjoint.  Then
```math
\boxed{
\sum_{r=1}^k\alpha_{e_r}
\le
\sum_{b\in\bigcup_r B_{S_r}}|g_b|
\le P_*
\le2D.
}
\tag{C20.17}
```

#### Proof

For each `r`, Theorem C20.2 and the triangle inequality give
```math
\alpha_{e_r}
=\left|\sum_{b\in B_{S_r}}g_b\right|
\le\sum_{b\in B_{S_r}}|g_b|.
\tag{C20.18}
```
The vertex-disjointness of the `S_r` makes the boundary-reaction sets `B_{S_r}`
pairwise disjoint.  Summing (C20.18) and using the definition of `P_*` proves
(C20.17). `\square`

Equivalently, every antichain of oriented bridge cuts in the bridge-tree laminar order
has total contact stress at most `2D`.

### Corollary C20.4 (leaf-bridge stress is boundary-order)

Contract every maximal 2-edge-connected subgraph of `C_+` to obtain its bridge tree.
For each leaf edge choose the component on the leaf side.  These leaf-side components
are pairwise disjoint (with the one-edge bridge-tree case handled by choosing either
orientation once).  Therefore
```math
\boxed{
\sum_{e\in E_{\rm leaf}}\alpha_e\le P_*\le2D.
}
\tag{C20.19}
```

Since the total positive contact stress is `D^2`,
```math
\boxed{
\frac{\sum_{e\in E_{\rm leaf}}\alpha_e}
     {\sum_{e\in C_+}\alpha_e}
\le\frac2D.
}
\tag{C20.20}
```
Thus asymptotically none of the normalized contact-stress mass can be carried by leaf
bridges.

The same bound applies to every single bridge-tree frontier: orient all frontier
bridges away from a root so their descendant components are disjoint, then their total
stress is at most `2D`.

---

## 5. Target C-II consequence

In the fully force-visible branch `C=C_*`, choose a relative-interior normalized KKT
stress, so every unit contact has positive coefficient and `C_+=C`.  Theorems
C20.2--C20.4 then apply to the **entire** unit-contact graph.

This eliminates one possible C-II mechanism: the `D^2` contact-stress normalization
cannot be hidden in many dangling leaf bridges.  At most `2D` stress lies there.  Any
survivor must instead place `D^2-O(D)` stress in

- 2-edge-connected contact blocks, or
- bridges lying strictly inside the bridge tree, represented by nested reciprocal
  diagonals.

If a positive fraction `eta D^2` of the stress lies on bridges, root the bridge tree
and group bridge edges by depth.  Each depth frontier is an antichain, so C20.3 gives
at most `2D` stress per depth.  Hence the bridge tree must have depth at least
```math
\boxed{\frac{\eta D}{2}.}
\tag{C20.21}
```
This is consistent with a long force-transmission chain and is not yet a
contradiction, but it is now an exact reciprocal-geometric alternative rather than an
unstructured articulation case.

A high-value continuation is therefore:

> **Bridge-depth / reciprocal-area theorem.**  Show that a laminar chain of
> `Omega(D)` reciprocal diagonals arising from unit-contact bridges forces either a
> forbidden one-dimensional force-hull limit, an excessive reciprocal mixed area, or
> a diameter-star/cycle configuration excluded by C17--C19.

The complementary branch is that almost all stress lies in 2-edge-connected
triangle-free penny blocks; there one should combine block face structure with the
second-order angular-variance and reciprocal-response identities.

---

## 6. Regression audit

- **Straight chain:** every edge is a bridge and the reciprocal polygon degenerates;
  this is exactly the one-dimensional phase already excluded by C19, so it does not
  contradict the new theorem.
- **Unit square:** the contact graph is a cycle, so there are no contact bridges.
- **Regular pentagon:** likewise bridge-free.
- **Honeycomb tree with imposed boundary loads:** bridge diagonals and the antichain
  bound are compatible; such a framework is not claimed to be a global minimizer.
- **KKT-invisible rattlers:** not touched; C20 concerns only the positive contact
  network of the chosen stress.
- **Diameter-star reactions:** allowed.  The theorem records their resultant on each
  bridge side but does not assume the diameter graph is a matching or cycle.

No generic rigidity, lower bound on individual stress coefficients, or unproved PSD
comparison is used.

---

## 7. Promotion recommendation

**Promote now** as a Target C structural theorem.  It is an exact consequence of the
canonical force-hull and reciprocal-polygon identities and materially narrows the
fully force-visible articulation branch.

Suggested edits after audit:

- index this report from `docs/targets/target-c/README.md`;
- add the bridge/reciprocal theorem and C-II split to
  `docs/targets/target-c/01-force-hull-and-shear.md`;
- refresh the Target C continuation prompt if no stronger concurrent theorem
  supersedes it.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New Target C theorem:
Every positive unit-contact bridge uv cuts the loaded force-hull vertices into two
cyclic intervals.  On either side S,
    sum_{b in B_S} g_b = alpha_uv (u-v).
Therefore the reciprocal boundary arc for B_S closes by a diagonal
    Delta z = alpha_uv J(u-v),
so the reciprocal diagonal is perpendicular to uv and has length exactly alpha_uv.
Torque balance gives
    sum_{b in B_S}(b-u) x g_b = 0.

For any pairwise disjoint family of bridge-side components,
    sum alpha_bridge <= P_* <= 2D.
In particular all leaf bridges together carry at most 2D of the total contact stress
D^2, so their stress fraction is at most 2/D.

C-II split:
- substantial bridge stress -> Omega(D)-deep laminar chain of reciprocal diagonals;
- otherwise almost all stress lies in 2-edge-connected triangle-free penny blocks.

Exact next lemma:
Rule out the deep reciprocal-diagonal chain or derive a contradiction in the
2-edge-connected block branch using the existing angular/reciprocal identities.
```
