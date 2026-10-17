> Generated reading edition · [exact source](../../research/target_c_dominant_oo_dual_tree_region_saturation_t1860_2026-09-15.md) · source SHA-256 `b288546945e4a7b8f6d16d701b401c34d7a7ef7529a35ac73e9426c6f4f8c86c`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "84492fbd5fc0a20afbb43de1772c993f36472da9", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_dominant_oo_dual_tree_region_saturation_t1860_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "9ed6e5a8348c8d4c4e172ff1092c74eb4294e9e9f02e212df8f2b4ca58d6b33a"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — full-rank same-phase O--O shear saturates every dual region by a diameter endpoint

**Date:** 2026-09-15  
**Status:** proof-only high-`t` structural strengthening  
**Scope:** a pairwise noncrossing O--O family that is a proper subset of the complete stopped trains; applied to the dominant exact-phase family through `t<=1.860`  
**Dependencies:** exact global O--O multishear; canonical mixed infinitesimal rigidity; complement-dual tree; C65 full actual-diameter graph  
**Companion:** `target_c_dominant_oo_dual_tree_helly_hub_t1860_2026-09-15.md`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The high-`t` dominant O--O family may branch in its complement dual tree.  The new Helly-hub theorem controls all actual diameter paths on that tree.  Mixed rigidity gives another, independent restriction: the signed diameter-path incidence has full column rank.  On a tree, full path-incidence rank is possible only if **every complementary region contains an actual diameter endpoint**.

This is an exact finite statement and requires no lower bound on any KKT multiplier.

---

## 1. Signed path coordinates on the complement dual tree

Let

```math
\mathcal L=\{\tau_1,\ldots,\tau_m\}
```

be pairwise noncrossing outer-to-outer complete stopped trains, and let

```math
T=T_{\mathcal L}
```

be their complement dual tree.  Thus

```math
|E(T)|=m,
\qquad
|V(T)|=m+1.
```

Root `T` at an arbitrary vertex `r`.  For each selected edge `e_i`, let `S_i` be the descendant component of `T-e_i`, and define

```math
\chi_i(v)=1_{S_i}(v)
\qquad(v\in V(T)).
\tag{RS.1}
```

For each tree vertex put

```math
\Phi(v):=(\chi_1(v),\ldots,\chi_m(v))\in\{0,1\}^m.
\tag{RS.2}
```

If an actual diameter row `h=xy` is globally oriented, its shore-incidence vector is exactly

```math
\boxed{
\varepsilon_h
=\Phi(\rho(y))-\Phi(\rho(x)),
}
\tag{RS.3}
```

where `rho(x),rho(y)` are the complement regions containing the two source endpoints.  Equation (RS.3) is the tree form of the signed support matrix in the exact global multishear theorem.

---

## 2. The tree-region vectors are affinely independent

### Lemma RS.1

The `m+1` points

```math
\{\Phi(v):v\in V(T)\}
```

are affinely independent in `R^m`.

### Proof

The root satisfies `Phi(r)=0`.  For every nonroot vertex `v`, let `e(v)` be the last edge on the root-to-`v` path.  Order nonroot vertices by nondecreasing depth.  In the matrix whose row for `v` is `Phi(v)`, the column `e(v)` equals one on row `v`, while a shallower vertex has zero in that descendant-edge column.  Ordering edges by their child vertices gives a triangular `m x m` matrix with unit diagonal after elementary depth-respecting elimination.  Hence the `m` nonroot vectors are linearly independent.  Together with `Phi(r)=0`, all `m+1` region vectors are affinely independent. `square`

Equivalently, `Phi` realizes the tree vertices as the vertices of an `m`-simplex adapted to the rooted cut coordinates.

---

## 3. The selected O--O diameter derivative matrix has full column rank

Orient the selected train vector on cut `i` consistently with the rooted shore split and write it as `u_i`.  For an actual diameter vector

```math
r_h=p_y-p_x,
```

the first squared-length derivative under simultaneous selected-train shears is twice the matrix

```math
M_{hi}
:=\varepsilon_{hi}(r_h\cdot Ju_i).
\tag{RS.4}
```

### Lemma RS.2 — arbitrary noncrossing-family shear injectivity

Assume the selected family `L` is a proper subset of the complete stopped trains.  Then

```math
\boxed{\operatorname{rank}M=m.}
\tag{RS.5}
```

### Proof

Suppose `M theta=0`.  The corresponding simultaneous O--O shear is an infinitesimal flex of every positive contact, because each selected train shear is contact-preserving to first order and the exact global multishear superposes them.  It also has zero first derivative on every actual diameter constraint by `M theta=0`.

Canonical mixed infinitesimal rigidity therefore makes the flex Euclidean on the nonisolated positive-contact core.

In complete-train angular coordinates its rate is `theta_i` on selected trains and zero on every unselected train.  By assumption at least one complete train is unselected.  A Euclidean rotation has one common angular rate on every contact train, while a translation has zero train rates.  The unselected zero rate therefore kills the rotation component, and every selected rate must vanish:

```math
\theta=0.
```

Thus `ker M=0` and (RS.5) follows. `square`

For the high-`t` dominant same-phase O--O family, the proper-subset hypothesis is automatic in the full-core branch: the selected trains are pairwise noncrossing in one phase, whereas the branch has a quadratic strict-rhombus population and hence contains crossing trains outside this family.

---

## 4. Exact phase factors the matrix through signed tree paths

Now assume the selected family has one exact projective phase.  Fix one unit representative `u`.  Since the rooted shore orientation may reverse a train vector, write

```math
u_i=s_i u,
\qquad
s_i\in\{-1,+1\}.
\tag{RS.6}
```

For each diameter row put

```math
d_h:=r_h\cdot Ju.
```

Then

```math
M_{hi}=d_h\,\varepsilon_{hi}s_i.
```

In matrix form,

```math
\boxed{
M=\operatorname{diag}(d_h)\,E\,\operatorname{diag}(s_i),
}
\tag{RS.7}
```

where `E` is the signed tree-path incidence matrix with rows `epsilon_h`.

Hence

```math
\operatorname{rank}M\le\operatorname{rank}E.
```

By Lemma RS.2,

```math
\boxed{\operatorname{rank}E=m.}
\tag{RS.8}
```

In particular diameter rows perpendicular to `Ju` may disappear from `M`, but the remaining signed endpoint differences still span the entire `m`-dimensional tree cut space.

---

## 5. Full rank forces a loaded endpoint in every complement region

Let

```math
B_T:=\{v\in V(T):\text{region }v\text{ contains an endpoint of some }h\in H\}.
```

Put

```math
b:=|B_T|.
```

Every row of `E` is, by (RS.3), a difference of two region vectors `Phi(v)` with `v in B_T`.  Therefore the row space of `E` lies in the translation space of the affine hull of

```math
\{\Phi(v):v\in B_T\}.
```

A set of `b` points has affine dimension at most `b-1`, so

```math
\boxed{\operatorname{rank}E\le b-1.}
\tag{RS.9}
```

Combine (RS.8) and (RS.9):

```math
m\le b-1.
```

But the whole tree has only `m+1` regions, so `b<=m+1`.  Hence equality is forced throughout:

```math
\boxed{b=m+1.}
\tag{RS.10}
```

### Theorem RS — dual-region diameter saturation

Every complementary region of the selected same-phase O--O family contains at least one endpoint of an actual diameter edge:

```math
\boxed{
B_T=V(T).
}
\tag{RS.11}
```

Since C65 makes every actual diameter edge force-visible under the canonical relative-interior stress, every region contains positive diameter endpoint incidence, not merely a KKT-invisible diameter vertex.

---

## 6. Combine with the Helly hub

Use the companion Helly-hub theorem and root `T` at its common diameter-routing region `R_*`.

Then the two conclusions coexist:

1. **region saturation:** every one of the `m+1` regions contains at least one actual diameter endpoint;
2. **hub routing:** no actual diameter edge has both endpoint regions inside the same component of `T-R_*`.

Therefore every nonhub region contains a loaded endpoint whose incident actual diameter edges all leave its hub branch in the dual-tree sense.  In particular, no branch can be a genuinely inactive collection of same-phase strips hidden behind one braced cut.

The exact rooted endpoint-mass flow from the hub theorem consequently has **positive source mass in every tree vertex**.  The masses may be arbitrarily small with `D`; no uniform lower bound is asserted.

---

## 7. Quantitative high-`t` consequence

The current dominant same-phase O--O staircase gives

```math
\begin{array}{c|c|c}
\text{window} & m/D & \text{forced distinct loaded regions}\\ \hline
 t\le1.850 & >0.0700-o(1) & >0.0700D-o(D)\\
 t\le1.855 & >0.0466-o(1) & >0.0466D-o(D)\\
 t\le1.860 & >0.0246-o(1) & >0.0246D-o(D).
\end{array}
\tag{RS.12}
```

Thus even at the widest current high-`t` window, a survivor cannot hide the dominant O--O family inside a few loaded complement chambers.  A linear number of distinct regions are individually touched by the actual diameter graph, while every diameter path is simultaneously routed through one common hub.

This is the high-`t` branching normal form:

```text
linear same-phase noncrossing O-O cuts
 -> m-edge complement dual tree
 -> full-rank signed diameter path incidence
 -> every one of m+1 regions contains an actual diameter endpoint
and
 -> all actual diameter support paths contain one common hub region.
```

---

## 8. Remaining obstruction

The theorem does not lower-bound the KKT endpoint mass in each saturated region.  A linear number of regions carrying `Theta(1/D)` or smaller masses remains possible.  Nor does it by itself force a long dual-tree path: a heavily branched saturated tree is still abstractly possible.

The next useful closing input must exploit one of the facts that the present rank argument ignores:

- loaded endpoints are cyclically ordered extreme vertices of one convex force hull;
- the actual diameter graph has the Woodall thrackle topology;
- the hub theorem forbids diameter edges internal to a branch; and
- every rooted cut resultant is parallel to the same projective phase direction.

These constraints now act on a dual tree in which **no region is empty of diameter support**.

No C-II closure is claimed.

**Disposition:** proved proof-only high-`t` dual-region saturation for the dominant same-phase O--O family. C-II and Level I remain open.
