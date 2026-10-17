> Generated reading edition · [exact source](../../../docs/reports/target_c_outer_pocket_oler_2026-09-09.md) · source SHA-256 `faa5c204863b42bea733e834d4a5d039926bf631c6b1f503f5b10fd8d47b7edc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D3C2F0127493","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — internal outer-pocket Oler absorption

**Date:** 2026-09-09  
**Repository state:** `be9cbfb78cbda059fb4c2581118b236729cfad84`  
**Run type:** exact geometric / packing theorem  
**Target:** Target C C-II / outer-shell force-bulk frontier  
**Depends on:** C26, C42, C51, C52, canonical Oler finite-packing inequality  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C52 leaves one KKT-invisible population: contact-isolated source points in the outer contact face. This report proves that the part of that population lying **inside the force hull** is already absorbed exactly by the C52 outer-area gap.

Let

- `G=C` be the connected fully force-visible positive contact core;
- `F=conv V(G)` be its force hull;
- `B=|\partial_\infty G|` be the outer contact-face boundary-walk length, counted with multiplicity; since every contact edge has length one, `B` is also the geometric length of that closed walk;
- `A_bnd` be the total area of the bounded contact faces;
- `H=area(F)-A_bnd` be the C52 outer-area gap;
- `Z_in` be the number of contact-isolated source points that lie in `F` and in the outer face of `G`.

Then

```math
\boxed{
Z_{in}
\le
\frac{2}{\sqrt3}H
+\frac{\operatorname{per}(F)-B}{2}
\le
\frac{2}{\sqrt3}H.
}
\tag{OP.1}
```

Consequently, if `Z_def` denotes the contact-isolated points in bounded contact faces, C52 and OP.1 give

```math
\boxed{
 m+Z_{def}+Z_{in}
\le
\frac{2}{\sqrt3}\operatorname{area}(F)
+\frac12\operatorname{per}(F)+1.
}
\tag{OP.2}
```

The second display is algebraically the ordinary Oler bound on all source points lying in `F`, but the first display is the useful result: it charges the **internal outer-face population itself** against exactly the missing area `H`, with a favorable perimeter correction. Hence the sole force-bulk population still not absorbed is

```math
\boxed{
Z_{ext}:=|\{a\in A\setminus V(G):a\notin F\}|,
}
```

i.e. contact-isolated source points outside the force hull.

This removes the shell-like `Theta(D^2)` population **inside** the force hull from the active Target C obstruction.

---

## 1. Inputs from the audited Target C stack

C26 and C42 give

```math
B_+=\operatorname{Vert}(F),
```

and every vertex of `B_+` lies on the outer contact-face walk. Every unloaded contact-core vertex has positive contact equilibrium and contact degree `3`, `4`, or `5`.

C51 proves the stronger articulation fact:

> for every core vertex `x`, every connected component of `G-x` contains at least one loaded force-hull vertex from `B_+`.

It also proves every bounded contact face is a simple strict convex unit-edge polygon.

C52 writes

```math
H=\operatorname{area}(F)-A_{bnd}
```

and proves

```math
\boxed{
 m+Z_{def}
\le
\frac{2}{\sqrt3}(\operatorname{area}(F)-H)
+\frac B2+1.
}
\tag{1.1}
```

The open issue in C52 is exactly the isolated population in the outer contact face.

---

## 2. Add the force-hull cycle

Write the loaded hull vertices in cyclic order as

```math
b_1,\ldots,b_q,
\qquad q=|B_+|.
```

Add every missing hull side `b_i b_{i+1}` to the straight-line plane graph `G`, retaining a hull side only once if it is already a unit contact edge. Call the resulting graph

```math
\widehat G:=G\cup\partial F.
```

No added edge crosses `G`, because every added segment lies on `\partial F` while `G\subseteq F`.

### Lemma OP.1 — the hull-augmented graph is 2-connected

`\widehat G-x` is connected for every vertex `x`.

#### Proof

Fix `x`. Let `S` be any component of `G-x`. By C51, `S` contains a loaded vertex

```math
b_S\in B_+.
```

Since `x\notin S`, necessarily `b_S\ne x`.

If `x\notin B_+`, the full hull cycle `\partial F` remains in `\widehat G-x`, so all loaded vertices are connected there.

If `x\in B_+`, deleting `x` turns the hull cycle into a path through every vertex of `B_+\setminus\{x\}`. Thus all loaded vertices distinct from `x` are again connected.

Every component `S` of `G-x` is attached inside `\widehat G-x` to its loaded vertex `b_S`, and all those loaded vertices are mutually connected by the surviving hull cycle/path. Therefore all components of `G-x` lie in one component of `\widehat G-x`.

So `\widehat G-x` is connected. `square`

Hence `\widehat G` is 2-connected. In particular every face boundary of `\widehat G` is a simple cycle.

---

## 3. Every new bounded face is strictly convex

The bounded faces of `\widehat G` split into two classes:

1. the old bounded contact faces of `G`;
2. new bounded faces cut from the old outer face by the force-hull cycle.

The old faces are strict convex polygons by C51. We prove the same for each new face.

### Lemma OP.2 — convex outer pockets

Every new bounded face of `\widehat G` is a simple strict convex polygon.

#### Proof

Simplicity follows from Lemma OP.1.

Let `P` be one new bounded face and let `x` be a boundary vertex.

First suppose `x\notin B_+`. No added hull edge is incident to `x`, so every edge of `\widehat G` incident to `x` is a positive unit contact edge of `G`. The open sector of `P` at `x` contains no contact edge.

Assume its interior angle is greater than `pi`. Then all contact directions from `x` lie in the complementary open cone of width strictly less than `pi`. A positive combination of nonzero vectors in such a cone cannot vanish, contradicting positive contact equilibrium at the unloaded vertex `x`.

If the face angle equals `pi`, all contact directions lie in one closed half-plane. Vanishing of their strictly positive resultant forces every contact direction onto the boundary line of that half-plane. Unit separation permits at most one unit neighbor in each of the two line directions, so `deg_C(x)<=2`, contradicting C26.

Thus every unloaded boundary vertex of `P` has face angle strictly below `pi`.

Now suppose `x=b\in B_+`. Every bounded face of `\widehat G` lies inside the convex polygon `F`. The local face sector at `b` is therefore contained in the tangent cone of `F` at `b`, whose opening is the strict convex interior angle of the hull at `b`, hence is less than `pi`.

So every interior angle of the simple polygon `P` is strictly less than `pi`. Therefore `P` is strictly convex. `square`

This argument also shows why the augmentation is useful: C51's bounded-face convexity extends to the entire force-hull subdivision once the hull cycle is inserted.

---

## 4. Topology and perimeter of the new pockets

Let

- `e=|E(G)|`;
- `v=|V(G)|`;
- `a` be the number of force-hull sides that are not already contact edges and are therefore added to form `\widehat G`;
- `p` be the number of new bounded faces of `\widehat G`;
- `k_P` be the number of boundary edges of a new face `P`;
- `L_P` be its Euclidean perimeter.

Because `G` and `\widehat G` are connected and have the same vertices,

```math
f_b(G)=e-v+1,
```

while

```math
f_b(\widehat G)=e+a-v+1.
```

All old bounded faces remain faces because the added hull edges lie in the old outer face. Therefore

```math
\boxed{p=a.}
\tag{4.1}
```

Since `\widehat G` is 2-connected, its unbounded face has the simple hull cycle as boundary, with `q` edges. Hence

```math
\sum_{\widehat f\text{ bounded}}k_{\widehat f}
=2(e+a)-q.
\tag{4.2}
```

For the original graph,

```math
\sum_{f\text{ old bounded}}k_f=2e-B.
\tag{4.3}
```

Subtracting gives the total edge-incidence count on new pockets:

```math
\boxed{
\sum_{P}k_P=B+2a-q.
}
\tag{4.4}
```

Now let `L_add` be the total Euclidean length of the `a` added hull sides. Every old contact edge has length one. The total edge length of `\widehat G` is therefore

```math
e+L_{add}.
```

The unbounded face has Euclidean perimeter `per(F)`, so

```math
\sum_{\widehat f\text{ bounded}}L_{\widehat f}
=2(e+L_{add})-\operatorname{per}(F).
\tag{4.5}
```

The old bounded contact faces have total perimeter

```math
2e-B.
\tag{4.6}
```

Thus

```math
\boxed{
\sum_PL_P
=B+2L_{add}-\operatorname{per}(F).
}
\tag{4.7}
```

There are `q-a` hull sides already present as contact edges, each of length one. Therefore

```math
\boxed{
\operatorname{per}(F)=(q-a)+L_{add}.
}
\tag{4.8}
```

Finally, the new pockets are exactly the portions of the old outer contact face lying in `F`; their interiors are pairwise disjoint and together have total area

```math
\boxed{
\sum_P\operatorname{area}(P)=H.
}
\tag{4.9}
```

---

## 5. Oler on every new pocket

Assign each contact-isolated source point lying in `F` and the old outer contact face to the unique new pocket containing it. A point lying on a newly added hull side may be assigned to its unique interior pocket. No isolated source point lies on a unit contact edge, so no ambiguity on old graph edges occurs.

Let `z_P` be the assigned isolated population of pocket `P`. Lemma OP.2 makes `P` a convex container. Its `k_P` graph-boundary vertices together with its `z_P` isolated points are unit-separated. The canonical Oler inequality gives

```math
\frac{\sqrt3}{2}(k_P+z_P-1)
\le
\operatorname{area}(P)
+\frac{\sqrt3}{4}L_P.
\tag{5.1}
```

Equivalently,

```math
z_P
\le
\frac{2}{\sqrt3}\operatorname{area}(P)
+\frac12L_P+1-k_P.
\tag{5.2}
```

Sum over all new pockets. Using (4.1), (4.4), (4.7), and (4.9),

```math
\begin{aligned}
Z_{in}
&\le
\frac{2}{\sqrt3}H
+\frac12\bigl(B+2L_{add}-\operatorname{per}(F)\bigr)
+a-(B+2a-q)\\
&=
\frac{2}{\sqrt3}H
-\frac B2
+L_{add}
-\frac12\operatorname{per}(F)
-a+q.
\end{aligned}
\tag{5.3}
```

Using (4.8),

```math
L_{add}-a+q=\operatorname{per}(F),
```

and hence

```math
\boxed{
Z_{in}
\le
\frac{2}{\sqrt3}H
+\frac{\operatorname{per}(F)-B}{2}.
}
\tag{5.4}
```

This is the first inequality in OP.1.

---

## 6. Outer contact walk dominates the force-hull perimeter

The outer-face boundary walk of `G` is a closed polygonal walk. Every traversed edge is a unit contact edge, so its rectifiable length is exactly `B`.

Its image lies in `F` and contains every extreme vertex of `F`, because C42 puts every loaded force-hull vertex on the outer-face boundary walk. Therefore the convex hull of the walk image is exactly `F`.

### Lemma OP.3 — closed-walk convex-hull perimeter bound

For any closed polygonal walk `gamma` of length `L`,

```math
\operatorname{per}(\operatorname{conv}\gamma)\le L.
```

#### Proof

For a direction `u_theta=(cos theta,sin theta)`, let `w(theta)` be the width of `conv gamma` in that direction. The scalar projection of a closed walk must travel from its minimum value to its maximum and back, so its total variation is at least `2w(theta)`.

For one segment of length `ell` making angle `phi`, the total variation of the `u_theta` projection contributed by that segment is

```math
ell|\cos(\phi-\theta)|.
```

Integrating over `theta in [0,pi]` gives `2ell`. Summing segments,

```math
\int_0^\pi 2w(\theta)\,d\theta
\le 2L.
```

Cauchy's perimeter formula for a convex polygon is

```math
\operatorname{per}(K)=\int_0^\pi w_K(\theta)\,d\theta.
```

Hence `per(conv gamma)<=L`. `square`

Apply the lemma to the outer contact walk. Since its convex hull is `F`,

```math
\boxed{
\operatorname{per}(F)\le B.
}
\tag{6.1}
```

Insert this into (5.4):

```math
\boxed{
Z_{in}\le\frac{2}{\sqrt3}H.
}
\tag{6.2}
```

This proves OP.1.

---

## 7. Exact reconciliation with C52

C52 gives (1.1):

```math
 m+Z_{def}
\le
\frac{2}{\sqrt3}(\operatorname{area}(F)-H)
+\frac B2+1.
```

Add the sharper form (5.4), not merely (6.2):

```math
\begin{aligned}
 m+Z_{def}+Z_{in}
&\le
\frac{2}{\sqrt3}\operatorname{area}(F)
+\frac B2
+\frac{\operatorname{per}(F)-B}{2}
+1\\
&=
\boxed{
\frac{2}{\sqrt3}\operatorname{area}(F)
+\frac12\operatorname{per}(F)+1.
}
\end{aligned}
\tag{7.1}
```

This is OP.2.

The cancellation is exact: C52's outer-contact-boundary term `+B/2` is paid by the pocket theorem's correction `(per(F)-B)/2`, leaving only the true convex force-hull perimeter.

---

## 8. What changes in the force-bulk frontier

Split C52's outer-face invisible population as

```math
Z_{out}=Z_{in}+Z_{ext},
```

where

```math
Z_{ext}:=|A\setminus F|
```

because every source point outside `F` is necessarily absent from the contact core.

The old frontier had two live outer-shell subphases:

1. isolated points in the outer contact face but inside `F`;
2. isolated points outside `F`.

OP removes the first subphase exactly. The only remaining force-bulk population obligation is now the external population `Z_ext`.

A sufficient next theorem is therefore no longer a generic bound on `Z_out`; it is specifically:

> **External force-hull theorem.** Bound the number of source points outside the force hull sharply enough, using the global diameter geometry and lexicographically normalized C-II source, to combine OP.2 with the global minimum-diameter comparison.

This is a strict reduction of the canonical C52 frontier.

---

## 9. Regression audit

### Regular odd shell with interior isolated population

If the contact core is exactly a convex shell, its interior is a bounded contact face, not the outer contact face. C52, rather than OP, absorbs that population. No false claim that the isolated points are diametral is made.

### Tree / star contact core

For a tree, there are no old bounded faces and `H=area(F)`. Adding the force-hull cycle produces ordinary convex pockets between the tree and the hull. C51's articulation theorem makes the augmentation 2-connected, and OP applies. A balanced three-arm star gives three convex triangular pockets, exactly as the proof predicts.

### Hull contact edges

Some force-hull sides may already be unit contact edges. They are not duplicated. The parameter `a` counts only missing hull sides, and (4.8) explicitly keeps the existing unit hull sides. Bridge and nonbridge hull contacts are therefore both included.

### Repeated outer-face walks / bridges

The original outer walk may repeat vertices and bridge edges. OP never assumes it is simple. Its multiplicity is retained in `B`, while the hull augmentation is 2-connected and has simple face boundaries.

### Heptagon plus isolated center

The isolated center lies in the bounded heptagonal contact face, so `Z_in=0`. The theorem does not declare it diametral and is compatible with the exact September 8 regression.

### Source points outside the force hull

Deliberately not controlled. They are the remaining obstruction.

---

## 10. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| hull augmentation is 2-connected | proved | C51 articulation theorem plus the force-hull cycle |
| every new pocket is strict convex | proved | positive equilibrium at unloaded vertices; convex tangent cone at loaded hull vertices |
| pocket Oler identity (5.4) | proved | exact Euler/face-incidence/perimeter bookkeeping |
| `B>=per(F)` | proved | closed-walk projection variation / Cauchy perimeter formula |
| `Z_in<=2H/sqrt3` | proved | (5.4) plus `B>=per(F)` |
| all outer-face isolated points are controlled | false / not claimed | external points outside `F` remain |
| Level I | still open | external force-hull population and final exact contradiction remain |

---

## 11. Promotion recommendation

**Hold as report pending independent audit.**

If promoted, the natural target is `docs/targets/target-c/07-outer-shell-force-bulk-frontier.md`. Replace the two-way internal/external phase split by the external force-hull population alone, while retaining the warning that OP does not control points outside `F`.

Do not infer `n-m=O(D)` from OP.

---

## 12. Next run

Attack `Z_ext` only.

Useful inputs that specifically concern the external population are:

1. C1 contact-preserving hull saturation, with the warning that it cannot be silently combined with secondary diameter-pair minimization;
2. C2 one-point diameter-preserving insertion body at right plateau endpoints;
3. the C-I-restored lexicographic source `C=C_*`, `H=H_*`;
4. the fact that the fixed positive contact core already realizes the full diameter `D`;
5. source convex-hull / diameter-endpoint geometry.

The immediate question is whether an external isolated point can be moved or charged to a source-hull arc without changing the lexicographic active set, or whether a new source-specific container argument bounds all such points by only `O(D)`.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

New theorem OP:
Let G=C be the fully force-visible contact core, F=conv V(G),
B=outer contact-face walk length, A_bnd=total bounded-face area,
H=area(F)-A_bnd, and Z_in=isolated source points in the outer contact
face that lie inside F.

Add the force-hull cycle to G. C51 implies the augmented graph is
2-connected. Every new bounded face is a strict convex polygon.
Summing Oler over the new pockets gives exactly

    Z_in <= 2H/sqrt(3) + (per(F)-B)/2.

The outer contact walk has geometric length B and convex hull F, so

    B >= per(F).

Therefore

    Z_in <= 2H/sqrt(3).

Combining with C52:

    m+Z_def+Z_in
      <= 2 area(F)/sqrt(3) + per(F)/2 + 1.

Thus the internal outer-shell population is fully absorbed. The sole
remaining force-bulk population is

    Z_ext = number of source points outside the force hull F.

Next: prove an external force-hull population theorem using the actual
global-diameter / lexicographic source geometry.
```
