> Generated reading edition · [exact source](../../../docs/reports/target_c_rhombic_train_track_pseudolines_2026-08-31.md) · source SHA-256 `a4b6557c37ba9aedca129ba2ebbfc20acbe049430d0f8b75523ab9cd0d474cd4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-97455706D51C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C77: strict-rhombus train-track pseudolines

**Date:** 2026-08-31  
**Repository base:** `66e53c32` (main after C76 / PR #80)  
**Run type:** exact rhombic-geometry / global combinatorial reduction  
**Target:** Target C Gate C-II, C73-C75 rhombic bulk  
**Depends on:** C42/C49 quadrangulation defect, C73 degree-four rhombic bulk  
**External audit:** Kenyon--Schlenker, *Rhombic embeddings of planar graphs with faces of degree 4*, arXiv:math-ph/0305057, especially Definition 1.1 and Theorem 3.1  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C73-C75 turn a near-capacity force-visible core into a sea of strict unit rhombi whose
missing short diagonals are almost unit. C77 gives those rhombi a global exact
combinatorial organization.

Inside the union of bounded quadrilateral contact faces, continue through opposite
edges of successive rhombi. The resulting maximal **train tracks** have three rigid
properties:

1. every track has one fixed unoriented unit-edge direction;
2. no track closes or self-crosses, and two distinct tracks cross at most once; and
3. the track-intersection graph is triangle-free.

The third statement is special to the present triangle-free unit-contact source. At a
crossing, the acute angle between the two track directions is strictly greater than
`pi/3`. Three projective directions on a circle of circumference `pi` cannot have all
three pairwise circular distances strictly greater than `pi/3`.

Thus every bounded quadrilateral face is an edge of a simple triangle-free graph on
the train tracks. If `T` is the number of tracks and `F_4` the number of bounded
quadrilateral contact faces,

```math
\boxed{F_4\le\frac{T^2}{4}.}
```

Moreover every track has two ends on the boundary of the rhombic-face union. If `h`
is the outer contact-face walk and

```math
Q=\sum_{f\text{ bounded}}(k_f-4),
```

then

```math
\boxed{2T\le h+5Q.}
```

Hence

```math
\boxed{F_4\le\frac{(h+5Q)^2}{16}.}
```

This does not close C-II by itself, because the linear face-defect budget can have a
large constant. It replaces an unstructured quadratic rhombic bulk by a finite
pseudoline arrangement with only `O(D)` tracks and no triangular triple of crossings.

---

## 1. Rhombic face complex and train tracks

Let `R` be the set of bounded degree-four faces of the complete C-II contact graph.
C49 proves that every face in `R` is a strict unit rhombus.

A **track state** is a pair `(f,{e,e'})` where `f in R` and `e,e'` are one of the two
pairs of opposite sides of `f`. Two states are consecutive when an exit side of the
first is the entry side of the second and the two rhombi lie on opposite sides of that
shared contact edge. A maximal sequence is a **rhombic train track**.

Equivalently, enter a rhombus across one edge and leave across the opposite edge; if
there is another quadrilateral contact face across that edge, continue uniquely.
Stop exactly when the next face is the outer contact face or a bounded
nonquadrilateral face.

Because opposite sides of a parallelogram are parallel, all entry/exit edges of one
track are parallel. Thus every track has a fixed unoriented transversal

```math
[u_T]\in\mathbb{RP}^1,
\qquad |u_T|=1.
\tag{C77.1}
```

Every rhombus belongs to exactly two tracks, one for each opposite-edge pair.

---

## 2. Pseudoline property

The following is the standard necessary half of the train-track criterion for a
rhombic embedding. Kenyon--Schlenker formulate it for a planar quad-graph and prove it
from monotonicity of a train track in the direction perpendicular to its common
parallel; their crossing-orientation proof is local and applies unchanged to maximal
track segments stopped at nonquadrilateral faces.

For completeness, the needed argument is short.

Orient a train track `T` and orient its transversal `u_T` so that `u_T` points from the
right side of the oriented track to the left side. In every rhombus crossed by `T`,
the displacement from the midpoint of the entry edge to the midpoint of the opposite
exit edge has strictly positive scalar product with `J u_T`. Hence the
`J u_T`-coordinate is strictly monotone along the track.

Therefore `T` cannot be periodic and cannot meet the same rhombus twice. In
particular it cannot self-cross.

Now orient two distinct tracks `T,S`. If they cross in a rhombus, choose the
orientations so that `T` crosses `S` from right to left. Their oriented transversals
then satisfy

```math
\det(u_T,u_S)>0.
\tag{C77.2}
```

If the same two simple tracks crossed again, the crossing order would be reversed at
the next crossing, while the same fixed transversals would still be attached to the
tracks. The second rhombus would therefore require

```math
\det(u_T,u_S)<0,
```

which is impossible. This is exactly the necessary-direction argument in
Kenyon--Schlenker, Theorem 3.1.

### Lemma C77.1 — rhombic pseudolines

Every rhombic train track is a finite simple path with two boundary ends. Two distinct
tracks intersect in at most one rhombus.

No assumption of periodicity, lattice structure, or stress positivity is used beyond
the fact that the relevant contact faces are embedded strict rhombi.

---

## 3. Strict unit separation forbids a track triangle

Suppose two train tracks `T,S` cross. Their crossing face is a unit rhombus whose side
directions are `[u_T]` and `[u_S]`.

Let

```math
\phi(T,S)\in(0,\pi/2]
```

be the acute projective angle between those directions. The short diagonal of the
unit rhombus has length

```math
2\sin\frac{\phi(T,S)}2.
```

That diagonal joins two source vertices. Unit separation makes its length at least
one. Equality would make it an actual unit contact drawn across the interior of the
quadrilateral face, splitting the face into contact triangles. Therefore

```math
\boxed{
\phi(T,S)>\frac\pi3.
}
\tag{C77.3}
```

Now suppose three tracks `T_1,T_2,T_3` were pairwise intersecting. Their three
unoriented directions are three points on the projective circle `R/pi Z`. Put them in
cyclic order. The three cyclic gaps are positive and sum to `pi`; one is therefore at
most `pi/3`. The acute projective distance of the corresponding pair is at most that
gap, contradicting C77.3.

### Theorem C77.2 — train-track intersection graph is triangle-free

Let `Gamma_R` have one vertex for every rhombic train track and one edge for every
crossing. Then `Gamma_R` is a simple triangle-free graph.

By Lemma C77.1, every crossing corresponds to one and only one rhombic face, and every
rhombic face is one crossing. Hence

```math
\boxed{|E(\Gamma_R)|=F_4.}
\tag{C77.4}
```

Mantel's theorem gives

```math
\boxed{
F_4\le\left\lfloor\frac{T^2}{4}\right\rfloor,
}
\tag{C77.5}
```

where `T=|V(Gamma_R)|`.

This is an exact combinatorial obstruction. Equality would force the track-intersection
graph itself to be complete bipartite.

---

## 4. Every train track consumes two rhombic-boundary edges

A maximal track cannot close by Lemma C77.1. Since the contact graph is finite, it has
two ends. Each end is a contact edge incident to exactly one bounded quadrilateral
face. On the other side of that edge lies either

- the outer contact face; or
- a bounded nonquadrilateral face.

Conversely every such boundary edge is the end of exactly one train track: use the
opposite-edge pair of its incident rhombus containing that edge.

Let `E_boundary^R` denote the number of contact edges incident to exactly one bounded
quadrilateral face. Then

```math
\boxed{2T=E_{\partial R}.}
\tag{C77.6}
```

Let `h` be the outer contact-face walk length and let

```math
L_{def}:=\sum_{\substack{f\text{ bounded}\\k_f\ge5}}k_f.
```

Every rhombic-boundary edge is represented by an incidence in the outer walk or in a
bounded nonquadrilateral face walk, so

```math
E_{\partial R}\le h+L_{def}.
\tag{C77.7}
```

For every integer `k>=5`,

```math
k\le5(k-4).
```

Therefore

```math
L_{def}\le5Q.
\tag{C77.8}
```

Combining C77.6-C77.8 gives:

### Theorem C77.3 — train-track boundary budget

```math
\boxed{
T\le\frac{h+5Q}{2}.
}
\tag{C77.9}
```

With C77.5,

```math
\boxed{
F_4\le\frac{(h+5Q)^2}{16}.
}
\tag{C77.10}
```

C49's exact face-defect budget

```math
h+Q\le4q-4
```

still implies only `T=O(D)` at the present level of constants, because `q<=pi D`.
The value of C77.10 is structural rather than a completed density gap.

---

## 5. Insert the C42 lower face count

C42 gives

```math
F_4\ge m-5q+3c_I+3e_{BB}+5.
\tag{C77.11}
```

Therefore C77.10 yields the exact new core inequality

```math
\boxed{
 m
\le
\frac{(h+5Q)^2}{16}
+5q-3c_I-3e_{BB}-5.
}
\tag{C77.12}
```

Equivalently, a large rhombic core forces many global train tracks:

```math
\boxed{
T\ge2\sqrt{F_4}
\ge2\sqrt{m-5q+3c_I+3e_{BB}+5}.
}
\tag{C77.13}
```

and therefore

```math
\boxed{
h+5Q\ge4\sqrt{F_4}.}
\tag{C77.14}
```

This turns quadratic rhombic bulk into linear pseudoline complexity.

---

## 6. Interaction with C75: near-capacity crossings are near 60 degrees

For a crossing `TS`, C75's short diagonal is

```math
s_{TS}=2\sin\frac{\phi(T,S)}2,
```

where `phi(T,S)>pi/3` is the acute track angle.

Thus C75's purely geometric slack becomes a track-intersection energy:

```math
\boxed{
\Sigma_{diag}
=
\sum_{TS\in E(\Gamma_R)}
\left(2\sin\frac{\phi(T,S)}2-1\right).
}
\tag{C77.15}
```

If the force-visible core is near capacity in the sense used in C75, then

```math
\Sigma_{diag}=O(D).
```

Since `F_4=Theta(D^2)`, the mean angular excess above the forbidden `60`-degree
threshold is `O(1/D)`. More precisely, for any fixed `eta>0`, only `O_eta(D)` track
crossings can have

```math
\phi(T,S)\ge\frac\pi3+\eta.
\tag{C77.16}
```

So the near-capacity geometry has the following exact global representation:

```text
T = O(D) rhombic pseudolines
pairwise crossing at most once
triangle-free intersection graph
Theta(D^2) crossings/rhombi
all but O_eta(D) crossings have angle in (pi/3, pi/3+eta)
```

This is much more rigid than an arbitrary collection of near-equilateral local
rhombi. The near-contact geometry is encoded by only linearly many fixed track
directions.

---

## 7. What C77 does and does not resolve

C77 does **not** by itself produce a leading density gap. A complete bipartite
arrangement of two families of tracks is compatible with a triangle-free intersection
graph, and rhombi between two direction families may have angles arbitrarily close to
`60` degrees. This is the correct oblique-grid regression.

The new obstruction is global:

- three mutually crossing direction families are impossible;
- a large rhombic bulk must be supported by a triangle-free pseudoline intersection
  graph; and
- under C75 near-capacity, almost every edge of that graph joins track directions
  separated by only `60+o(1)` degrees.

The next useful theorem should exploit one of two consequences.

1. **Angular Mantel stability.** Show that a triangle-free pseudoline arrangement with
   `Theta(D^2)` near-60 crossings is quantitatively close to two large track families.
   Then the embedded rhombic bulk is close to an oblique two-direction grid, whose
   diameter/area boundary economics are far worse than a disk.
2. **Defect-routing alternative.** Show that escaping the two-family structure requires
   a linear number of track breaks at nonquadrilateral defect faces, and charge those
   breaks using C49/C73/C75.

Either route is weight-free and is therefore compatible with the fixed-stress
limitation exposed by C72-C74.

---

## 8. Source audit

The train-track terminology and pseudoline facts agree with:

Richard Kenyon and Jean-Marc Schlenker, *Rhombic embeddings of planar graphs with
faces of degree 4*, arXiv:math-ph/0305057.

They define finite planar quad-graphs with the outer face exempt from the degree-four
condition and prove in Theorem 3.1 that a rhombic embedding necessarily has no
self-crossing or periodic train track and that two distinct train tracks cross at most
once. Their proof of necessity is exactly the fixed-transversal monotonicity and
crossing-orientation argument reproduced above. C77 uses only that necessary local
argument; no existence/classification theorem is imported.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C77:
Take all bounded quadrilateral contact faces (strict unit rhombi). Continue through
opposite edges to maximal train tracks.

Each track has one fixed projective unit-edge direction. It is monotone perpendicular
to that direction, never closes/self-crosses, and two tracks cross at most once.
At a crossing, strict triangle-free unit separation gives acute track angle >pi/3.
Therefore three tracks cannot pairwise cross. The intersection graph Gamma_R is simple
and triangle-free, with
  |E(Gamma_R)| = F_4.
Hence
  F_4 <= T^2/4.

Every track has two ends on the rhombic-face boundary. If h is outer face-walk length
and Q=sum_bounded(k_f-4),
  2T <= h+5Q,
so
  F_4 <= (h+5Q)^2/16.

C75 rewrites exactly as
  Sigma_diag = sum_(TS edge)[2 sin(phi_TS/2)-1].
Under near-capacity, Sigma_diag=O(D), so among Theta(D^2) crossings all but O_eta(D)
have angle <pi/3+eta.

Next: angular Mantel stability -> two-family oblique-grid reduction, or prove that
escaping two-family structure costs linearly many nonquadrilateral track breaks.
```
