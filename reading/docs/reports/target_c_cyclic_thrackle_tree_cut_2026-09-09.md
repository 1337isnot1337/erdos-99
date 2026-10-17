> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_thrackle_tree_cut_2026-09-09.md) · source SHA-256 `8dd990276d51d56ab6b1d66b324022acaf04f6b8f0b0261e5ccc7508cb46bb45`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D885AE81B4DE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic endpoint: convex-thrackle tree cuts and reciprocal parallelograms

**Date:** 2026-09-09  
**Repository base:** PR #118 after LF  
**Run type:** exact convex-thrackle cut theorem / KKT endpoint reduction  
**Target:** cyclic `d_H=1` connected-tree subcase  
**Depends on:** convex position of loaded terminals, geometric-thrackle property of the diameter graph, CY full positive contact cycle, LF/CG KKT face structure  
**External literature:** Woodall's caterpillar classification was checked for context; the cut theorem below is proved directly and does not depend on it  
**Computation:** none used in the proof

## LEVEL I STATUS

`STILL OPEN`

Let a finite tree be drawn by straight chords between vertices of a strictly convex polygon, with every pair of edges either sharing an endpoint or crossing properly. Such a drawing is a convex straight-line thrackle tree.

This report proves a new cyclic-order theorem:

### Theorem TC — two-interval cut theorem

For every edge `e` of a convex straight-line thrackle tree `T`, each connected component of

$$
T-e
$$

occupies at most two cyclic intervals of the ambient convex vertex order.

Applied to the cyclic Target C endpoint, if a full diameter-tree edge has zero KKT coefficient in a selected stress, summed equilibrium over either component gives zero contact-force resultant. TC reduces that condition to either two or four boundary cycle edges. The two-edge case is impossible; hence every such zeroed diameter edge forces an exact reciprocal parallelogram on four cycle-force vertices.

---

## 1. Mutually crossing components after deleting a tree edge

Let

$$
e=uv\in E(T)
$$

and let `A,B` be the vertex sets of the two components of `T-e`.

Any edge of `T[A]` is vertex-disjoint from any edge of `T[B]`. Since the complete tree drawing is a thrackle, every such pair of edges crosses properly.

If one component is a singleton, it occupies one cyclic interval and the other component occupies the complementary single interval. Thus assume both `T[A]` and `T[B]` contain at least one edge.

Both are trees and therefore bipartite. Write their unique bipartitions, up to swapping colors, as

$$
A=A_0\sqcup A_1,
\qquad
B=B_0\sqcup B_1.
\tag{1.1}

---

## 2. One edge of `A` separates the two colors of `B`

Fix an edge

\[
xy\in E(T[A]).
$$

The chord `xy` divides the convex boundary circle into two open arcs.

Every edge of `T[B]` crosses `xy`. Hence the two endpoints of every B-edge lie on opposite boundary arcs determined by `x,y`.

Choose any root of `T[B]`. As one traverses a B-edge, the side of the chord `xy` toggles. Because a tree is connected, side relative to `xy` is therefore exactly the bipartition parity on `B`, up to swapping the two colors.

Consequently:

$$
\boxed{
B_0\text{ lies entirely on one open }xy\text{-arc, and }B_1\text{ entirely on the other}.}
\tag{2.1}

This holds for every edge `xy` of `T[A]`.

A useful equivalent form is:

> any two vertices of the same B-bipartition class lie on the same side of every A-edge.

Therefore the straight chord joining two same-color B vertices crosses no edge of `T[A]`.

---

## 3. Each B-color class is one cyclic block

Return to one fixed A-edge `xy`, and let `I` be the open boundary arc containing `B_0`.

Suppose, for contradiction, that two vertices

\[
b,b'\in B_0
$$

have an A-vertex `a` strictly between them along the subarc of `I` from `b` to `b'`.

The complementary `b`-to-`b'` boundary arc contains `x` and `y`, hence contains A-vertices as well. Thus the A-vertex set has points on **both** open sides of the chord `bb'`.

Because `T[A]` is connected, some A-edge must cross `bb'`: take an A-path joining a vertex on one side to a vertex on the other and choose the first edge where the side changes.

But Section 2 proved that the chord between two same-color B vertices crosses no A-edge. Contradiction.

Therefore no A-vertex lies between two vertices of `B_0` along `I`. Since `B_1` lies on the other `xy`-arc, no B1 vertex lies there either. Hence all vertices of `B_0` form one consecutive cyclic B-block.

The same argument applies to `B_1`. Thus `B=B_0 union B_1` occupies at most two cyclic intervals.

By symmetry, `A` also occupies at most two cyclic intervals.

This proves Theorem TC. `square`

---

## 4. Selected KKT zero on a full diameter-tree edge

Now enter the cyclic Target C endpoint. The positive contact graph of every normalized stress is the full convex unit cycle

$$
C_q.
$$

Assume the **full** diameter graph `H` is a connected tree. This is a `d_H=1` cyclic subcase, so by CY

$$
s_Z=1,
\qquad
\dim\mathcal S=1.
$$

Let `s` be a KKT-polytope endpoint and let

$$
h=uv\in E(H)
$$

be a diameter edge with

$$
\beta_h(s)=0.
\tag{4.1}

LF says `h` is not a leaf edge of the full tree.

Delete `h` from `H`, with components on terminal sets `A,B`. Because `H` is a tree, `h` is the **only full diameter edge crossing the cut** `A|B`. Since its selected coefficient is zero, no selected positive diameter force crosses this cut.

Sum the KKT equilibrium equations of `s` over all vertices in `A`. Internal contact and diameter forces cancel. The diameter side has no crossing contribution, so the positive contact-cycle forces across the cut must have zero vector resultant:

\[
\boxed{
\sum_{e\in\partial_C A}F_e^{A}=0.}
\tag{4.2}

Here `F_e^A` is the unit-contact force exerted across cycle edge `e` from the A-side, with its natural sign.

TC says `A` occupies one or two cyclic terminal intervals. Therefore `partial_C A` has respectively two or four unit cycle edges.

---

## 5. One cyclic interval is impossible

Write the convex unit cycle in counterclockwise order as

\[
p_0,p_1,\ldots,p_{q-1}
$$

and define oriented unit side vectors and positive selected contact-force vectors

$$
t_i=p_{i+1}-p_i,
\qquad
v_i:=\alpha_i t_i,
\qquad
\alpha_i>0.
\tag{5.1}

Suppose `A` is one proper cyclic interval

\[
A=\{p_a,p_{a+1},\ldots,p_b\}.
$$

Exactly two contact edges cross the cut: `p_{a-1}p_a` and `p_bp_{b+1}`. Summed equilibrium (4.2) is

$$
\boxed{v_{a-1}=v_b.}
\tag{5.2}

But the two oriented side directions `t_{a-1}` and `t_b` of a strictly convex polygon are distinct. Positive scalar multiples of distinct directions cannot be equal.

Contradiction.

Thus:

### Corollary TC.1

If a full diameter-tree edge has zero coefficient in a selected cyclic KKT stress, both components of `H-h` occupy exactly two cyclic terminal intervals.

---

## 6. Two intervals force a reciprocal parallelogram

Let the four A/B transitions occur in cyclic order at cycle-edge indices

\[
i<j<k<\ell
$$

with A occupying the two intervals entered across edges `i` and `k` and exited across edges `j` and `ell`.

The signed contact-force resultant (4.2) is

$$
\boxed{
v_i-v_j+v_k-v_\ell=0.}
\tag{6.1}

Equivalently,

\[
\boxed{
v_i+v_k=v_j+v_\ell.}
\tag{6.2}

Recall that the polygon with vertices `v_i=alpha_i t_i` is, up to a fixed quarter-turn and translation, the reciprocal force polygon: its consecutive side differences are the boundary reaction vectors.

Equation (6.2) says the two diagonals of the four reciprocal vertices

\[
v_i,v_j,v_k,v_\ell
$$

have the same midpoint. Hence these four cyclically ordered reciprocal vertices form a parallelogram.

Therefore:

### Theorem TC-KKT — zeroed tree edge gives a reciprocal parallelogram

In the cyclic connected-tree `d_H=1` subcase, every full diameter edge whose beta coefficient vanishes at a KKT-polytope endpoint has a `2+2` cyclic cut, and the four corresponding contact-force vertices form an exact parallelogram in the selected reciprocal force polygon.

No asymptotic estimate is involved.

---

## 7. Both KKT endpoints supply such cuts

LF proves that the one-dimensional KKT polytope has at least two distinct diameter-coordinate facets, hence at least two distinct full nonleaf diameter edges can vanish somewhere on its boundary.

A one-dimensional compact polytope has exactly two endpoint facets. Therefore each endpoint supplies at least one zeroed nonleaf diameter edge, and the two facets require distinct coordinate faces.

By TC-KKT, each endpoint stress therefore has an exact reciprocal parallelogram associated with a nonleaf full-diameter-tree cut.

The reciprocal polygons at the two stress endpoints need not coincide, so this is not yet a contradiction. It is, however, a four-vertex equality condition replacing the previous abstract endpoint description.

---

## 8. Relation to the weighted cycle response

For later use, the positive contact network is a weighted cycle with edge conductances `alpha_i` and resistances

$$
r_i=1/\alpha_i.
$$

Thus every selected transfer coefficient can be written explicitly in cyclic arc resistances. In particular, for alternating diameter chords `(a,b)` and `(c,d)` with cyclic order

$$
a<c<b<d,
$$

let the four intervening cycle-resistance arcs have sums `A,B,C,D`. With consistent chord orientations,

\[
\boxed{
K_{(a,b),(c,d)}
=\frac{BD-AC}{A+B+C+D}.}
\tag{8.1}

A future tree-endpoint exclusion can therefore combine the primal parallelogram equality (6.2) with C56-G's strict transfer inequalities in these same cycle weights.

Equation (8.1) is recorded here as a handoff; a full derivation should be included if it becomes a promoted dependency.

---

## 9. Regression audit

### Two-run cut examples

Convex thrackle caterpillars can genuinely have tree-edge cuts for which both components occupy two cyclic intervals. TC allows them; it does not falsely strengthen the conclusion to one interval.

### Star edge

Deleting a leaf edge gives a singleton component, hence one interval. LF already says such an edge can never have zero KKT coefficient, consistently with TC.1.

### Regular shell

The full diameter graph is cyclic rather than a tree, so the tree-cut KKT argument does not apply.

### Abstract parallelogram

A strictly convex reciprocal polygon may contain four vertices forming a parallelogram. The equality is therefore a structural constraint, not by itself impossible.

---

## 10. Next theorem

The connected-tree `d_H=1` branch is now reduced to two KKT endpoint equalities:

1. each endpoint deletes a distinct nonleaf full diameter edge;
2. each deleted edge has a `2+2` cyclic cut and forces a reciprocal parallelogram;
3. every selected stress remains C56-G and maximal scalar rank by CG.

The next exact target is to combine the parallelogram equality with the weighted-cycle transfer formula (8.1) and the convex-thrackle nesting/order of the two deleted tree edges. A contradiction would close the connected-tree `d_H=1` cyclic subcase.

---

## 11. Promotion recommendation

**Hold as report pending independent audit.**

TC is a self-contained finite combinatorial theorem. The KKT consequences depend on the report-level CY/CG/LF stack.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

TC (proved directly):
Delete any edge of a straight-line thrackle tree on convex vertices. Each component
occupies at most two cyclic vertex intervals.

Proof core:
Every A-edge crosses every B-edge. For one A-edge xy, every B-edge toggles sides of
xy, so B's two tree-bipartition classes lie on opposite xy boundary arcs. Two vertices
of the same B color are on the same side of every A-edge, so their joining chord
crosses no A-edge. If an A-vertex split that B-color class along its xy arc, connectedness
of A would force an A-edge to cross that same-color chord. Contradiction. Each B color
is one cyclic block; hence B has <=2 blocks, and symmetrically A.

Cyclic d_H=1 connected-tree KKT consequence:
If beta_h=0 for a full tree edge h at a selected stress, no diameter force crosses the
H-h cut. Summed equilibrium makes the cycle-contact cut resultant zero.
- one cyclic component interval would give v_i=v_j for two distinct convex side
  directions: impossible;
- therefore both components have two intervals, and the four boundary force vectors
  satisfy v_i+v_k=v_j+v_l: an exact reciprocal parallelogram.

The stress interval has two endpoint coordinate facets, so both endpoints supply such
parallelogram cuts on distinct nonleaf diameter edges.

Next: combine these endpoint parallelograms with the explicit weighted-cycle transfer
formula and C56-G to close the connected-tree d_H=1 case.
```
