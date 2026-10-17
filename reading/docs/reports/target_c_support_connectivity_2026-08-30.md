> Generated reading edition · [exact source](../../../docs/reports/target_c_support_connectivity_2026-08-30.md) · source SHA-256 `7b2def678eded77a391baeb7e42952c3370969a750851b0ca4f91645d55fff3d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-868D5606C3C6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: positive KKT support is connected

**Date:** 2026-08-30  
**Repository state:** `research/target-c-force-hull-v2-2026-08-30`  
**Run type:** proof / structural reduction  
**Target:** Level I candidate route C  
**Depends on:** canonical KKT theory and `target_c_force_hull_2026-08-30.md`, `target_c_force_polygon_2026-08-30.md`  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This note proves a structural fact that was not used in the previous Target C reports:
for **every** normalized KKT stress, its positive unit-contact support has exactly one
nontrivial connected component.

Consequently the KKT force hull is the convex hull of one connected positive
unit-distance network, and that one contact network already contains two points at
mutual distance `D`.  In the triangle-free case Eppstein's connected penny-graph bound
therefore applies directly with graph diameter at least `ceil(D)`.

The proof uses only:

- KKT equilibrium;
- the strict normal-cone property of positive diameter reactions;
- planarity of the unit-contact graph; and
- an elementary noncrossing-partition argument on the convex-hull boundary.

No source/scaffold or rhombic-shell machinery is used.

---

## 1. Setup

Fix a normalized KKT stress `(\alpha,\beta)` of a global minimizer `A`.  Write

```math
C_+=\{ij\in C:\alpha_{ij}>0\},
\qquad
H_+=\{ij\in H:\beta_{ij}>0\},
```

and let `B_+` be the endpoint set of `H_+`.

Let

```math
F=\operatorname{conv}B_+=\operatorname{conv}V(C_+)
\tag{C12.1}
```

by Target C Theorem C3.1.  Every `b\in B_+` is a vertex of `F`.  Define the boundary
reaction

```math
g_b=\sum_{bk\in H_+}\beta_{bk}(b-k).
\tag{C12.2}
```

Target C Lemma C10.1 gives

```math
g_b\ne0,
\qquad
g_b\in\operatorname{ri}N_F(b),
\tag{C12.3}
```

where `N_F(b)` is the outward normal cone of `F` at `b`.

For a connected component `K` of `C_+`, put

```math
B_K:=B_+\cap V(K).
\tag{C12.4}
```

Canonical Proposition 5.4 gives

```math
|B_K|\ge2.
\tag{C12.5}
```

### Lemma C12.1 (component reaction balance)

For every component `K` of `C_+`,

```math
\boxed{
\sum_{b\in B_K}g_b=0.
}
\tag{C12.6}
```

#### Proof

Sum the KKT vertex equilibrium equations over all vertices of `K`.  Every positive
contact edge has both endpoints in `K`, so its two endpoint force contributions cancel.
A positive diameter reaction can occur at a vertex of `K` only at a point of `B_K`.
The remaining right side is exactly the sum in (C12.6). `\square`

Thus the outward reaction normals attached to each positive contact component must
positively wrap the origin on their own.

---

## 2. Unit-contact components give a noncrossing partition of the force-hull boundary

### Lemma C12.2 (unit contacts do not cross)

Two distinct unit-contact segments with no common endpoint cannot cross properly.

#### Proof

Suppose unit segments `ab` and `cd` cross at an interior point `x`.  Of the two numbers
`|a-x|,|b-x|`, one is at most `1/2`; choose the corresponding endpoint `u`.  Likewise
choose `v\in\{c,d\}` with `|v-x|\le1/2`.  Because the segments cross properly, the two
rays `xu` and `xv` are not opposite.  Hence the strict triangle inequality gives

```math
|u-v|<|u-x|+|x-v|\le1,
```

contradicting unit separation. `\square`

Order the vertices of `B_+` cyclically around the boundary of `F`.  Color each one by
its connected component of `C_+`.

### Lemma C12.3 (component colors form a noncrossing partition)

There do not exist distinct contact components `K,L` and four boundary vertices in
cyclic order

```math
a,b,c,d
```

with

```math
a,c\in B_K,
\qquad
b,d\in B_L.
\tag{C12.7}
```

#### Proof

Because `K` is connected, it contains a polygonal path of unit-contact edges joining
`a` to `c`.  Likewise `L` contains a polygonal path joining `b` to `d`.  Both paths lie
in the convex disk `F`.  Two paths in a disk joining alternating pairs of boundary
points must intersect.  Distinct contact components share no vertex, and by Lemma
C12.2 their edges cannot cross properly.  Contradiction. `\square`

So the sets `B_K` are the blocks of a noncrossing partition of the cyclically ordered
set `B_+`.

### Lemma C12.4 (two interval blocks)

If a noncrossing partition of a finite cyclically ordered set has at least two blocks,
then at least two blocks consist of cyclically consecutive elements.

#### Proof

Draw, for each block, noncrossing chords joining its elements into a tree.  The union
is a plane forest in the closed disk with every vertex on the boundary.  Contract each
block-tree to one node and consider the nesting relation of the complementary boundary
intervals.  A finite forest with at least two nodes has at least two leaves.  A leaf
block cannot contain elements of another block between two consecutive elements of
itself; otherwise that intervening block would lie below it in the nesting relation.
Hence every leaf block is a cyclic interval.  There are at least two leaves. `\square`

Equivalently, this is the standard elementary leaf property of noncrossing
partitions.  Only the conclusion will be used below.

---

## 3. Connectedness theorem

### Theorem C12 (positive contact support is connected)

For every normalized KKT stress of every planar global minimizer,

```math
\boxed{
C_+\text{ has exactly one nontrivial connected component.}
}
\tag{C12.8}
```

Consequently

```math
\boxed{
\operatorname{diam}V(C_+)=D.
}
\tag{C12.9}
```

#### Proof

The one-dimensional force-hull case is immediate.  If `F` is a segment, every point of
`B_+` is an extreme point of `F`, so `|B_+|=2`.  Proposition 5.4 requires every
nontrivial component of `C_+` to contain both boundary points; two different components
cannot both contain the same vertices.  Hence there is one component.

Assume now that `F` is two-dimensional.  Suppose, for contradiction, that `C_+` has at
least two components.  By Lemmas C12.3-C12.4, choose two distinct components `K,L`
such that `B_K` and `B_L` are cyclic interval blocks of the boundary order.

By (C12.3), the directions of the vectors `g_b` occur in the same strict cyclic order
as the vertices `b` of `F`: each `g_b` lies in the interior of the corresponding
vertex normal cone, and interiors of distinct vertex normal cones are disjoint.  For an
interval block `B_K`, let `\theta_K\in(0,2\pi)` be the angular span from the first to
the last reaction direction in that block, following the cyclic order and including
all reaction directions of the block.  Define `\theta_L` similarly.

Because the two blocks are disjoint cyclic intervals and the reaction directions at
distinct vertices have positive angular gaps, their spans satisfy

```math
\theta_K+\theta_L<2\pi.
\tag{C12.10}
```

Hence at least one, say `K`, has

```math
\theta_K<\pi.
\tag{C12.11}
```

All nonzero vectors `{g_b:b\in B_K}` then lie in one open half-plane through the
origin.  A positive sum of vectors from an open half-plane cannot vanish.  This
contradicts the component reaction balance (C12.6).

Therefore `C_+` is connected.

Finally `H_+` is nonempty because `\sum_H\beta=1`.  Choose `ij\in H_+`.  Canonical
Lemma 5.2 puts both `i` and `j` in `V(C_+)`, and `|p_i-p_j|=D`.  Hence the connected
positive contact support itself has Euclidean diameter `D`. `\square`

---

## 4. Triangle-free consequence

Assume now that the global minimizer is triangle-free.  Then `C_+`, being a subgraph
of the unit-contact graph, is a connected triangle-free penny graph.

Let

```math
m_+:=|V(C_+)|,
\qquad
e_+:=|C_+|.
```

The graph distance between the two vertices of any positive diameter edge is at least
`D`, because every contact edge has Euclidean length one and the Euclidean distance
between the endpoints is `D`.  Since graph distance is integral,

```math
\operatorname{diam}_{G}(C_+)\ge\lceil D\rceil.
\tag{C12.12}
```

Eppstein's canonical connected triangle-free penny-graph inequality (literature
baseline (2.3)) therefore gives:

### Corollary C12.5 (positive-support edge deficit)

```math
\boxed{
e_+
\le
2m_+-\lceil D\rceil-2.
}
\tag{C12.13}
```

Thus every KKT stress of a triangle-free global minimizer has a connected,
full-diameter positive unit-contact network with a **linear-in-`D` contact deficit**
from the planar quadrangulation ceiling.

This is stronger than applying Eppstein separately to unknown positive-stress
components: there is only one component, and its graph diameter is forced by an actual
length-`D` pair inside that component.

---

## 5. Componentwise reciprocal identity collapses to one component

Before Theorem C12, the reciprocal construction C10 could have been applied separately
to every positive contact component.  The theorem shows that this bookkeeping is
unnecessary: all positive contact stress mass

```math
\sum_{C_+}\alpha=D^2
```

belongs to one connected network and its one force polygon has

```math
2V(F,F^*)=D^2.
```

Likewise the electrical response matrix `\Lambda` of C11 is the response of one
connected contact network, rather than a block diagonal union of independent
components.

This matters for the next Target C step.  Any attempt to localize the KKT stress into
many small independently loaded islands is impossible.  The positive force-carrying
network is intrinsically macroscopic and spans the entire source diameter.

---

## 6. Regression audit

- **Unit square:** `C_+` is the four-cycle, connected and full-diameter.
- **Regular pentagon:** `C_+` is the five-cycle, connected and full-diameter.
- **Regular odd-prime shell local regressions:** their symmetric positive support is a
  single cycle, so the theorem does not falsely exclude them.
- **`n=8` heptagon plus center:** the positive support may be the heptagon cycle; the
  isolated center is not claimed to belong to `C_+`.
- **Rattler/activation regressions:** universally zero-stressed activated vertices may
  remain outside `V(C_+)`; C12 concerns positive KKT support only.
- **Five-sector pinned regression:** arbitrary pinned stresses are not normalized
  global KKT stresses with genuine diameter reactions, so the component reaction-normal
  argument does not transfer to that regression.

The theorem gives no uniform density gap and does not say that `V(C_+)=A`.

---

## 7. Revised Target C bottleneck

The positive part of a counterexample can no longer fragment into many islands.  The
configuration has a canonical macroscopic core:

```math
\boxed{
\text{one connected positive unit-contact network}
\quad\text{of Euclidean diameter }D,
}
\tag{C12.14}
```

whose convex hull is the KKT force hull and whose boundary currents are the diameter
reactions.

The unresolved class is therefore more sharply split into:

1. **force-visible vertices** in this connected full-diameter network; and
2. **KKT-invisible vertices/active constraints** outside its positive support.

Theorem C6 releases all weak active constraints simultaneously to first order; C7-C9
show that surviving weak contacts are protected only by diameter shear; C12 now says
that this shear acts against one connected macroscopic positive network.

A high-value next theorem is:

> **Target C6 (positive-core bulk theorem).**  In a sufficiently large
> contact-minimal, diametrally saturated, triangle-free global minimizer, prove that
> all but `O(D)` points belong to `V(C_*)`, where `C_*` is the maximal KKT contact
> support.

Because C12 makes `C_*` connected and full-diameter, such a theorem would put the bulk
packing density directly inside one force hull and allow C10's reciprocal perimeter
identity to interact with finite-packing area estimates.  This is structurally
different from Target A's independent-scaffold Hall transfer.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New Theorem C12:
For every normalized KKT stress, the positive contact graph C_+ has exactly one
nontrivial connected component.  Proof: summing equilibrium over a contact component
makes its positive diameter reactions sum to zero; each such reaction lies strictly in
the outward normal cone of its force-hull vertex.  Distinct contact components induce
a noncrossing partition of the cyclic force-hull boundary because unit-contact edges
cannot cross.  Any noncrossing partition with at least two blocks has two interval
blocks.  Their reaction-direction angular spans have sum <2pi, so one lies in an open
semicircle, contradicting zero resultant for that component.

Consequences:
- the single positive contact network contains both endpoints of every H_+ edge and
  therefore has Euclidean diameter exactly D;
- in the triangle-free case it is one connected triangle-free penny graph with graph
  diameter >= ceil(D), hence Eppstein gives
      |C_+| <= 2|V(C_+)| - ceil(D) - 2;
- the reciprocal force polygon and electrical response of C10-C11 belong to one
  macroscopic force-carrying network, not a union of small islands.

Remaining obstruction:
KKT-invisible vertices may still be numerous.  The next useful theorem is to force all
but O(D) source points into the maximal positive support C_*.
```
