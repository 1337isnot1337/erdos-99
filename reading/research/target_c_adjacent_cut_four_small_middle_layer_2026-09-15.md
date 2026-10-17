> Generated reading edition · [exact source](../../research/target_c_adjacent_cut_four_small_middle_layer_2026-09-15.md) · source SHA-256 `65013bfb86192843637ba19061a1929fdcfb8341464bf931aeca896dc47dacf3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "4540c64d7e16c731e45b316402a07afe4ff59cfc", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_adjacent_cut_four_small_middle_layer_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "24bbe064b2a843157b407c6ec824b7ad3abfab5dc9b52c07aa4e3b3c7568e02e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — one phase-close low-switch pair has a bounded loaded middle layer

**Date:** 2026-09-15
**Status:** proof-only source-level structural strengthening
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.844`
**Dependencies:** `target_c_adjacent_cut_triple_small_2026-09-15.md`; exact laminar layer partition; C65 loaded force hull; Cauchy perimeter bound; `target_c_switching_cusp_middle_layer_cut_2026-09-15.md`
**Certificate:** `research/verify_target_c_middle_layer_four_small.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The triple-small adjacent-cut theorem forces three quantities to be simultaneously
bounded at one internal boundary of a linear good-leaf path: actual diameter support
change, switching KKT mass, and projective phase change.  The exact laminar layer
partition supplies a fourth global budget which can be spent in the same averaging:
loaded diameter endpoints belong to disjoint physical layers.

This forces the entire loaded terminal set of the middle layer to be finite, uniformly
in `D`.

Let the high-phase good-leaf path from the parent theorem be

$$
P=(\tau_1,\ldots,\tau_m),
\qquad m>pD-o(D),
$$

where

$$
p={278778993\over78216868750}=0.0035641799\ldots .
$$

Let `R_0,...,R_m` be the exact physical layers from the laminar shear theorem and, for
an internal boundary `i`, put

$$
L_i:=|B_+\cap R_i|,
$$

where `B_+` is the complete C65 loaded diameter-endpoint set.

### Theorem FM — four-small adjacent middle layer

For every unbounded survivor sequence in the stated scope, for all sufficiently large
members there is an internal boundary `i` for which the consecutive smallest-leaf O--O
trains `tau_i,tau_{i+1}` satisfy simultaneously

$$
\boxed{N_i<22060+o(1),}
\tag{FM.1}
$$

$$
\boxed{B_i^{\rm sw}<{22060\over D}+o(D^{-1}),}
\tag{FM.2}
$$

$$
\boxed{
d_{\mathbb{RP}^1}(u_i,u_{i+1})
<{22060\over D}+o(D^{-1}),
}
\tag{FM.3}
$$

and

$$
\boxed{L_i<22060+o(1).}
\tag{FM.4}
$$

The exact rational average is smaller than

$$
22057.339.
$$

For the Section 157 cut resultants one also has

$$
\boxed{
\|F_{i+1}-F_i\|<22060+o(1),
\qquad
|A_{i+1}-A_i|<22060+o(1).
}
\tag{FM.5}
$$

Combining this with the exact middle-layer cusp theorem gives a finite interface normal
form:

$$
\boxed{
\mathcal S_i=\delta_H(B_+\cap R_i),
}
\tag{FM.6}
$$

with both the number of middle loaded vertices and the number of diameter cut edges
less than `22060+o(1)`.

In particular, the vertex set consisting of the middle loaded terminals together with
all outside endpoints of switching diameter edges has size less than

$$
\boxed{44120+o(1).}
\tag{FM.7}
$$

The induced diameter graph on the middle terminals also has fewer than
`22060+o(1)` edges.  Thus the entire diameter-graph patch incident to the moving layer
has bounded combinatorial size, independent of `D`.

---

## 1. The loaded middle layers have one global `q` budget

The exact laminar shear theorem partitions every source vertex into one of the layers

$$
R_0,R_1,\ldots,R_m.
$$

Hence the loaded subsets `B_+ cap R_i` are disjoint and

$$
\sum_{i=1}^{m-1}L_i\le |B_+|=:q.
\tag{FM.8}
$$

Every loaded terminal is an extreme vertex of the C65 force hull `F`.  Consecutive
vertices of `F` are distinct source points and therefore are at distance at least one.
Thus

$$
q\le \operatorname{per}(F).
\tag{FM.9}
$$

The force hull has diameter `D`, so Cauchy's perimeter bound gives

$$
\operatorname{per}(F)\le\pi D.
$$

Consequently

$$
\boxed{
\sum_{i=1}^{m-1}L_i\le\pi D.
}
\tag{FM.10}
$$

No near-disk estimate is needed; this is a finite global bound.

---

## 2. Add the layer population to the parent three-cost averaging

Use the parent notation

$$
N_i=\#\{h:\varepsilon_{h,i+1}\ne\varepsilon_{hi}\},
$$

$$
B_i^{\rm sw}
=\sum_h\beta_h
 |\varepsilon_{h,i+1}-\varepsilon_{hi}|,
$$

and

$$
q_j=\beta_j-\alpha_\gamma-\pi/3>0
$$

for the phase offset of leaf `tau_j` from the selected high-phase center train.
The audited parent budgets are

$$
\sum_{i=1}^{m-1}N_i\le2\pi D,
\tag{FM.11}
$$

$$
\sum_{i=1}^{m-1}B_i^{\rm sw}\le2,
\tag{FM.12}
$$

and

$$
\sum_{j=1}^{m}q_j
\le{C_{phase}\over d_{low}}+o(1),
\tag{FM.13}
$$

where

$$
d_{low}={9891\over62500}=0.158256
$$

and

$$
C_{phase}={\pi^2\sqrt3(2+\sqrt3)\over12}.
$$

Define the four-cost quantity

$$
T_i^{(4)}
:=N_i+D B_i^{\rm sw}+D(q_i+q_{i+1})+L_i.
\tag{FM.14}
$$

All four summands are nonnegative.  Equations (FM.10)--(FM.13) give

$$
\begin{aligned}
\sum_{i=1}^{m-1}T_i^{(4)}
&\le
3\pi D+2D+{2C_{phase}\over d_{low}}D+o(D)\\
&=\left(3\pi+2+{2C_{phase}\over d_{low}}\right)D+o(D).
\end{aligned}
\tag{FM.15}
$$

Since `m>pD-o(D)`, one internal boundary satisfies

$$
T_i^{(4)}
\le
{3\pi+2+2C_{phase}/d_{low}\over p}+o(1).
\tag{FM.16}
$$

The exact certificate uses the same outward rational enclosures as the parent theorem,

$$
\pi<{355\over113},
\qquad
\sqrt3<{17321\over10000},
$$

and proves

$$
\boxed{
{3\pi+2+2C_{phase}/d_{low}\over p}
<22057.339<22060.
}
\tag{FM.17}
$$

Every summand of `T_i^(4)` is therefore less than `22060+o(1)`.
This gives (FM.1), (FM.2), and (FM.4).  The parent phase relation

$$
d_{\mathbb{RP}^1}(u_i,u_{i+1})
\le q_i+q_{i+1}
$$

gives (FM.3).  Finally,

$$
\|F_{i+1}-F_i\|
\le D B_i^{\rm sw}
$$

and reverse triangle inequality give (FM.5).

---

## 3. The whole active diameter interface is finite

Apply the exact middle-layer cut theorem to the boundary selected in Section 2.  With

$$
B_i^{mid}:=B_+\cap R_i,
$$

its switching rows are exactly

$$
\mathcal S_i=\delta_H(B_i^{mid}).
$$

Equations (FM.1) and (FM.4) give

$$
|B_i^{mid}|<22060+o(1),
\qquad
|\delta_H(B_i^{mid})|<22060+o(1).
\tag{FM.18}
$$

Every outside endpoint adjacent to the middle layer is incident to at least one cut
edge, so

$$
|N_H(B_i^{mid})\setminus B_i^{mid}|
\le|\delta_H(B_i^{mid})|.
$$

This proves the `44120+o(1)` vertex bound (FM.7).

The induced subgraph `H[B_i^{mid}]` is itself a straight-line thrackle.  Every finite
straight-line thrackle has at most as many edges as vertices; equivalently one may use
the Hopf--Pannwitz diameter-graph bound when the induced subgraph has an edge of length
`D`.  Therefore

$$
|E(H[B_i^{mid}])|
\le|B_i^{mid}|<22060+o(1).
\tag{FM.19}
$$

So both the internal diameter graph of the middle layer and its complete active
diameter interface are finite-state objects.

This is stronger than merely bounding the cusp rows.  Before (FM.4), the middle layer
could contain `Theta(D)` loaded terminals and an unbounded internal diameter subgraph
which was invisible to the opposite-shear cusp set.

---

## 4. What this reduction does not prove

A bounded combinatorial interface is not itself a contradiction.  In particular:

- the constant `22060` is far too large for a brute-force graph classification;
- middle-layer terminals may carry internal diameter edges which do not appear among
  the switching rows;
- the outside endpoints of cusp edges need not lie in one neighboring layer;
- KKT multipliers on individual cusp edges may still be arbitrarily small; and
- positive KKT stationarity still excludes a nonzero first-order feasible
  contact-preserving shear.

The point is that the remaining obstruction is now finite in **vertices as well as
edges**.  This opens source-level moves which replace the whole middle interface patch
instead of attempting to choose signs on an arbitrary asymptotic cusp family.

---

## 5. Next finite interface target

The strongest next theorem would reduce the bounded middle patch further using one of
the structures already present:

1. convex-hull cyclic order of the `B_i^{mid}` terminals plus the straight-line
   thrackle property;
2. Woodall's caterpillar/odd-unicyclic classification restricted to the middle patch;
3. the fact that the two contact sides of the layer are projectively
   `O(D^{-1})`-parallel; or
4. a direct same-cardinality replacement of a bounded loaded interface while allowing
   the old train-side contacts to break.

No local-descent or Level-I conclusion is claimed.

**Disposition:** proved proof-only finite-interface strengthening. C-II and Level I remain open.
