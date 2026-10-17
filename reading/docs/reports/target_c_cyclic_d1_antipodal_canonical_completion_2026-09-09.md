> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_antipodal_canonical_completion_2026-09-09.md) · source SHA-256 `43621ef97020b1fb22062bc5311880ea1d0a5002219076684e197e725f05bb82`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-B1301DDE4247","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — canonical antipodal completion in the cyclic `d_H=1` S1 branch

**Date:** 2026-09-09  
**Repository branch:** PR #118 after D1/AD/MT  
**Run type:** exact rotating-calipers / convex-thrackle reduction  
**Target:** cyclic primitive phase `d_H=1`, short-antipodal branch S1  
**Depends on:** AD exact difference-body defect split, D1 exact one-defect family, DC connected spanning-tree classification, standard maximal convex-thrackle structure  
**External literature:** rotating-calipers monotonicity only; the crossing argument is included below  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

In the S1 branch there are no parallel sides of the force hull `F`, and `K=F-F` has exactly `2q` vertices. AD identifies exactly one antipodal pair of vertices of `K` strictly inside the radius-`D` circle; all other `2q-2` vertices are actual diameter vectors.

The key observation is that, when `F` has no parallel sides, the complete vertex-vertex antipodal graph of `F` is itself a maximal convex thrackle. Therefore the unique short antipodal pair is not merely analogous to one of MT's possible completion chords: it is the canonical missing edge.

### Theorem AC — canonical S1 completion

Let `F` be a cyclic S1 survivor and let `g=uv` be the unique short vertex-vertex antipodal pair supplied by AD/D1. Let `A(F)` denote the graph of all vertex-vertex antipodal pairs of `F`. Then

```math
\boxed{A(F)=H\cup\{g\}.}
\tag{AC.1}
```

Moreover:

1. `A(F)` is a maximal convex thrackle with exactly `q` edges on the `q` shell vertices;
2. `A(F)` consists of one odd cycle with every remaining vertex a direct leaf;
3. `g` lies on that unique odd cycle;
4. `H=A(F)-g` is the spanning tree obtained by opening that odd cycle at the unique short antipodal chord;
5. the short length is the explicit D1 quantity
   
   ```math
   |g|
   =D\cos\frac{(s+2)\delta}{2}
   +\sqrt{1-D^2\sin^2\frac{(s+2)\delta}{2}},
   ```

   with
   
   ```math
   0<s<\frac{\Delta_2}{\delta}-2,
   \qquad
   \sqrt{D^2-1}<|g|<D.
   ```


Thus MT completion nonuniqueness disappears entirely in S1: the geometry of `F-F` itself selects the missing odd-cycle chord.

---

## 1. Vertex-vertex antipodal pairs are the projective vertices of `F-F`

Because S1 has no parallel sides, the edge directions of `F` and `-F` never merge. Hence `K=F-F` has exactly `2q` vertices.

Fix a vertex `x` of `K`. For every normal direction in the interior of the normal cone of `x`, the maximizing point of `F` and the minimizing point of `F` are unique vertices, say `p_i,p_j`, and

```math
x=p_i-p_j.
```

The two vertices admit parallel supporting lines with opposite normals, so `{p_i,p_j}` is a vertex-vertex antipodal pair of `F`.

Conversely every vertex-vertex antipodal pair persists for an open interval of support directions when there are no parallel sides, and therefore gives one antipodal vertex pair `x,-x` of `K`.

Thus the `2q` vertices of `K` correspond to exactly `q` unordered vertex-vertex antipodal pairs of `F`.

---

## 2. Antipodal chords form a convex thrackle

We include the rotating-calipers crossing argument because it is the only structural input needed here.

Let

```math
e_1=p_i p_j,
\qquad
e_2=p_k p_\ell
```

be two distinct vertex-vertex antipodal chords. Choose projective support-normal directions `theta_1,theta_2` realizing the two pairs and lift them to one interval of length `<pi` with

```math
\theta_1<\theta_2.
```

As the support normal rotates from `theta_1` to `theta_2`, the maximizing support vertex moves monotonically forward around the counterclockwise boundary of `F`. The minimizing support vertex does the same on the opposite side. Therefore, after a cyclic relabeling, the four endpoints occur in the order

```math
p_i,\ p_k,\ p_j,\ p_\ell,
```

with equality allowed only when the two antipodal chords share an endpoint.

If all four endpoints are distinct, this alternating cyclic order is exactly the crossing criterion for two chords of a strictly convex polygon. Hence the two chords cross properly. If an endpoint agrees, they meet there.

Therefore every two edges of `A(F)` meet exactly once, at a common endpoint or in a proper crossing. Thus

```math
\boxed{A(F)\text{ is a convex straight-line thrackle}.}
\tag{2.1}
```

---

## 3. `A(F)` is maximal and has odd-cycle-plus-leaves structure

Section 1 gives

```math
|E(A(F))|=q.
```

A convex straight-line thrackle on `q` vertices has at most `q` edges. Therefore `A(F)` is edge-maximal.

The standard maximal-convex-thrackle classification applies: `A(F)` consists of one odd cycle, with every vertex outside that cycle a degree-one leaf attached directly to a cycle vertex.

This proves items 1 and 2 of AC.

---

## 4. The diameter graph is obtained by deleting exactly the short antipodal edge

AD/D1 say that among the `q` antipodal pairs represented by the `q` antipodal vertex pairs of `K`, exactly

```math
q-1
```

have Euclidean length `D`, while exactly one pair `g=uv` has length strictly below `D`.

Every length-`D` pair is an edge of the full diameter graph `H`, and every edge of `H` is one of these antipodal pairs. Hence

```math
E(H)=E(A(F))\setminus\{g\},
```

which is AC.1.

DC gives that the `d_H=1` diameter graph `H` is connected and spanning. If `g` were a leaf edge of the maximal odd-cycle-plus-leaves graph `A(F)`, deleting `g` would isolate its leaf endpoint. This contradicts connectedness and spanning of `H`.

Therefore `g` lies on the unique odd cycle of `A(F)`. Deleting it opens the odd cycle into a path while retaining every pendant edge, and the result is exactly the spanning tree `H`.

This proves items 3 and 4. `square`

---

## 5. The local defect must switch support endpoints

The canonical completion also gives a useful rotating-calipers corollary.

Let

```math
x=p_u-p_v
```

be the short vertex of one projective half of `K`, and let its two circular neighbors be `a,b`.

Because S1 has no parallel sides, each of the two unit Minkowski edges incident to `x` changes exactly one of the two support vertices. Suppose both changes occurred at the same endpoint. Up to reversing orientation, the three consecutive antipodal states would be

```math
(u_-,v),\quad (u,v),\quad (u_+,v),
```

where `u_-,u,u_+` are consecutive shell vertices. The outer two chords `vu_-` and `vu_+` are actual diameters, while `vu` is short.

Any actual diameter edge incident to `u` other than `uv` is vertex-disjoint from both `vu_-` and `vu_+`. In cyclic order

```math
u_-,u,u_+,\ldots,v,\ldots,
```

a chord from `u` cannot cross both `vu_-` and `vu_+`: crossing the first forces its other endpoint onto the `v -> u_-` arc, while crossing the second forces it onto the disjoint `u_+ -> v` arc.

Thus `u` would have no actual diameter edge. This contradicts C65 full diameter visibility of every shell vertex.

Hence the two defect steps change opposite support endpoints. After orientation the local states are

```math
\boxed{(u_-,v),\quad (u,v),\quad (u,v_+),}
\tag{AC.2}
```

where `u_-u` and `vv_+` are shell sides and the two neighboring diameter chords

```math
u_-v,\qquad uv_+
```

are vertex-disjoint. Since both are actual diameter edges, the diameter-thrackle property forces them to cross. Therefore their endpoints alternate on the shell.

This is the exact local combinatorial form of the unique S1 defect.

---

## 6. Relation to MT

MT proved only that there exists at least one maximal convex-thrackle completion

```math
T=H+g'
```

with a short cycle chord `g'`; small abstract examples show such a completion need not be unique in general.

AC is stronger in S1. The difference body itself provides the complete antipodal graph, and therefore

```math
\boxed{T=A(F)=H+g}
```

with the unique short antipodal pair `g` from D1.

So all later `d_H=1` arguments in S1 may use the explicit D1 length formula for the actual maximal-completion cycle edge. No arbitrary completion choice remains.

---

## 7. Regression audit

### Nonparallel hypothesis

Essential. With parallel primal sides a rotating-calipers tie creates an edge face of `F-F`, and multiple vertex-vertex antipodal pairs can correspond to the same support direction. AC is deliberately restricted to S1.

### Pairwise crossing claim

The proof uses monotone support indices, not Euclidean diameter. Thus it applies to all vertex-vertex antipodal pairs in the no-parallel case, including the unique short pair.

### Short edge as a pendant edge

Excluded only because DC already proves `H=A(F)-g` is connected and spanning. No unsupported claim that every short antipodal pair is cyclic is made in general.

### Local same-endpoint defect

The direct crossing argument uses C65 actual diameter visibility and the fact that the two outer antipodal states are actual diameter edges. It does not assume the conclusion that `g` is cyclic.

---

## 8. What this changes

S1 is now a canonical one-edge defect of an antipodal odd-cycle-plus-leaves graph:

```text
A(F): q-edge maximal antipodal convex thrackle
      = one odd cycle + direct leaves
H:    A(F) with exactly one cycle edge g deleted
|g|:  explicit one-parameter D1 formula
local defect states:
      (u_-,v) -- (u,v short) -- (u,v_+)
```

This is stronger than the arbitrary MT completion and is the correct input for either a sign-code reconstruction or the `d_H=1` KKT endpoint cuts.

---

## 9. Next theorem

There are now two sharp S1 attacks.

1. **Cycle-edge/KKT interaction.** For either KKT endpoint edge `e` of the spanning tree `H`, the four-block cut of `H-e` contains both the actual diameter edge `e` and the canonical short cycle edge `g` as cross-cut antipodal chords. Combine their forced corner locations with the four-contact wrench relation and WT.
2. **Antipodal sign code.** The maximal antipodal graph and the D1 local state AC.2 determine the rotating-calipers sign word except for the odd-cycle leaf composition. Reconstruct the primal edge closure as a signed trigonometric equation in the single scalar `s`.

Either route now works with a canonical defect edge of known length rather than an arbitrary subdiametral completion chord.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

S1 has no parallel sides, so K=F-F has 2q vertices and exactly q unordered
vertex-vertex antipodal pairs. Rotating-calipers support indices are monotone; hence
any two antipodal chords share an endpoint or cross. Thus the complete antipodal graph
A(F) is a q-edge convex thrackle, hence maximal odd-cycle-plus-leaves.

AD/D1: exactly q-1 antipodal pairs have length D and exactly one pair g is short.
Therefore A(F)=H+g. DC says H is connected spanning, so g cannot be pendant in A(F);
it lies on the unique odd cycle. Thus S1 has a canonical maximal completion, and the
completion edge has the explicit D1 length.

Local defect: the two K-boundary steps around the short state cannot move the same
support endpoint, or the middle shell vertex would have no possible actual diameter
edge (it cannot cross both neighboring diameter chords). Hence, up to orientation,
  (u_-,v), (u,v short), (u,v_+),
with u_-v and uv_+ disjoint crossing diameter chords.

Next: combine canonical g with the d_H=1 endpoint four-block/wrench equations, or
write the signed edge-closure equation from the resulting antipodal sign code.
```
