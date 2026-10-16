<!-- theorem-state: {"artifact_id":"ART-5F13015CE50D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C51: every bounded force-visible contact face is a strict convex unit polygon

**Date:** 2026-08-31  
**Target:** C-II / force-bulk  
**Depends on:** C3 finite contraction rigidity, C10 force-hull boundary, C26, positive KKT equilibrium  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

In the fully force-visible contact core, every bounded contact face has a simple strictly convex boundary cycle. In particular no contact bridge or one-vertex articulation branch can protrude into a bounded face.

This converts the bounded defect cavities of C49-C50 from arbitrary nonconvex face regions into genuine convex unit-edge containers, allowing exact facewise Oler in C52.

---

## 1. Every articulation branch contains a loaded vertex

Let `G=C` be the connected positive contact graph in fully force-visible C-II. Let `x` be any vertex, and let `S` be one connected component of `G-x`.

### Lemma C51.1

`S` contains at least one vertex of `B_+`.

#### Proof

Suppose `S cap B_+=empty`. Fix every vertex outside `S`, including `x`, and contract the vertices of `S` homothetically toward `x`:

`y_v = x + (1-t)(p_v-x)` for `v in S`, with `0<t<1`.

Every positive contact internal to `S` shortens by the factor `1-t`. Every positive contact from `S` to the rest of the graph has its outside endpoint equal to `x`, because `S` is a component of `G-x`; those contacts also shorten by `1-t`. All other positive contacts are unchanged.

Every positive diameter-load vertex belongs to `B_+`, and by assumption none lies in `S`, so all vertices of `B_+` are fixed.

Thus this is a nontrivial finite assignment fixing `B_+` and making every positive contact length at most one. Target C3 finite contraction rigidity says the only such assignment is the original one. Contradiction. `square`

The same argument includes the bridge case: both sides of every positive contact bridge contain loaded vertices, recovering the nonemptiness part of C20.

---

## 2. No articulation branch can be trapped inside a bounded face

Every vertex of `B_+` is a vertex of the convex force hull `F=conv V(G)` and therefore lies on the outer face of the straight-line plane graph `G`.

Suppose a bounded face boundary walk repeated a vertex `x`. The two occurrences split the walk into two nonempty closed subwalks. Standard plane block topology then gives a component `S` of `G-x` drawn entirely in the bounded region cut off by one of these subwalks; in particular `S` contains no outer-face vertex.

This contradicts Lemma C51.1, because every component of `G-x` contains a point of `B_+` and every such point is on the outer face.

Equivalently: all one-vertex articulation branches of `G` are exposed to the outer face; none can be enclosed behind a bounded face.

Therefore:

### Lemma C51.2

Every bounded face boundary is a simple cycle with distinct vertices and distinct edges.

In particular, a bridge is incident only with the outer face; no bridge occurs on a bounded face boundary.

---

## 3. Unloaded bounded-face vertices cannot be reflex

Let

`v_1,...,v_k`

be the simple cycle bounding a bounded face `f`, and fix boundary vertex `x=v_i` with face neighbors `y=v_{i-1}`, `z=v_{i+1}`.

Because `f` is a face, no contact edge from `x` lies in the open angular sector of the face between the rays `xy` and `xz`.

Assume first `x notin B_+`. Positive KKT equilibrium has no diameter reaction at `x`:

`sum_{xu in C} alpha_xu (x-u)=0`, with all `alpha_xu>0`.

If the interior face angle at `x` were greater than `pi`, then every contact direction from `x` would lie in the complementary open cone of width less than `pi`. A positive combination of nonzero vectors in such a cone cannot vanish.

If the face angle were exactly `pi`, all contact directions would lie in one closed halfplane bounded by the line through `y,x,z`. Zero positive resultant would force every contact direction onto that line. Unit separation allows at most one unit neighbor in each direction along the line, so `deg_C(x)<=2`. This contradicts C26, which forces every unloaded contact vertex in C-II to have full degree `3`, `4`, or `5`.

Hence every unloaded bounded-face vertex has face angle strictly less than `pi`.

---

## 4. Loaded bounded-face vertices cannot be reflex

Now let `x in B_+`. Then `x` is an extreme vertex of the convex force hull `F`. The entire embedded graph and every bounded face lie inside the convex polygon `F`.

The tangent cone of `F` at `x` has opening equal to the convex interior angle of `F`, strictly less than `pi`. The local interior sector of a bounded face at `x` lies inside that tangent cone. Therefore its angle is also strictly less than `pi`.

---

## 5. Theorem C51

Every bounded contact face has a simple polygon boundary, and every one of its interior angles is strictly less than `pi`.

Therefore:

`closure(f)` is a strictly convex polygon.

Every boundary edge is a unit contact, so every bounded contact face is a strict convex unit-edge polygon.

This holds for quadrilateral and nonquadrilateral faces alike.

---

## 6. Immediate consequences

1. A bounded face of walk length `k` has exactly `k` distinct boundary vertices.
2. Its perimeter is exactly `k`.
3. Every contact-isolated source point assigned to that face lies inside this convex polygon, so ordinary Oler applies to the union of its `k` boundary vertices and all isolated points in the face.
4. C49's bounded defect faces are therefore convex; the nonconvex giant-hole regression is removed.

## Regression audit

- The outer contact face may still have a repeated/nonconvex boundary walk; C51 deliberately concerns only bounded faces.
- Articulation branches on the outer face remain allowed.
- A bounded convex pentagonal or larger contact face remains allowed and can contain isolated source points.
- The proof uses C3 finite contraction rigidity and therefore the positive force-visible support; it is not a generic theorem for arbitrary penny graphs.
