> Generated reading edition · [exact source](../../../../docs/targets/target-c/84-typeII-interface-collapse-audit.md) · source SHA-256 `7668c73cc78818856483f50f6ef52e78d57152ff89012ef8e52a004862b11b15`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — Type-II inactive-interface collapse audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module is the theorem originally merged as the Type-II interface-collapse
Section 83. A concurrent later merge independently used Section 83 for the
attachment-cell disjointness theorem, so this file is the canonical numbering repair.
No mathematical statement is changed.

Work in the Type-II branch of Section 80:

```math
n-m=o(D^2),\qquad
A_F={\pi D^2\over4}-o(D^2),\qquad
A_4={\pi D^2\over4}-o(D^2),
\tag{84.1}
```

and, after translations,

```math
D^{-1}F\to B_{1/2}
\tag{84.2}
```

in Hausdorff distance.

The remaining inactive geometry has `o(D^2)` total area but may still have `O(D)`
total perimeter. The theorem classifies every residual piece with linear perimeter:

1. every exterior cap has diameter and perimeter `o(D)`;
2. every internal inactive chamber with perimeter `lambda D+o(D)`, `lambda>0`,
   collapses to a segment of length `lambda D/2` after scaling;
3. a linear-degree exceptional bounded contact face is two near-geodesic unit-contact
   paths between the same far-apart endpoints; and
4. a linear-perimeter outer pocket is an out-and-back pair of near-geodesic
   unit-contact paths from an `o(D)` force-hull side to one deep extreme.

Thus the linear Type-II inactive interface consists, at each fixed scale, of only
finitely many doubled near-geodesic contact corridors.

No local contradiction is inferred from near-geodesicity; the known near-chain
regression remains binding.

---

# 84. Type-II interface collapse

Let

```math
K=\operatorname{conv}A,
\qquad
F=\operatorname{conv}V(G).
\tag{84.3}
```

Canonical Section 68 gives

```math
0\le {\pi D^2\over4}-\operatorname{area}K=O(D).
\tag{84.4}
```

## 84.1 The source hull and force hull have the same disk limit

Use the translations in (84.2). Since `F subset K` and `diam K=D`, every Hausdorff
limit `K_infty` of `D^{-1}K` contains `B_{1/2}` and has diameter at most one. If
`x in K_infty` had `|x|>1/2`, then the antipodal disk point

```math
y=-{x\over2|x|}\in B_{1/2}
```

would satisfy `|x-y|=|x|+1/2>1`, contradiction. Hence

```math
\boxed{D^{-1}K\to B_{1/2}}
\tag{84.5}
```

with the same limiting center as `F`.

## 84.2 Exterior caps are sublinear

Let `K_i` be the convex exterior caps of canonical Section 77. Their interiors lie in
`K\setminus F` and Type II gives

```math
A_{ext}:=\operatorname{area}K-\operatorname{area}F=o(D^2).
\tag{84.6}
```

### Theorem 84.1

```math
\boxed{
\max_i\operatorname{diam}(K_i)=o(D),
\qquad
\max_i\operatorname{per}(K_i)=o(D).
}
\tag{84.7}
```

### Proof

If some cap had diameter at least `eta D` along a subsequence, scale by `D` and use
Blaschke selection. Its limit would be a nondegenerate convex set of zero area, hence
a segment. Every compact subset of `int(B_{1/2})` lies in the normalized force hull
for all large indices, so the cap limit cannot meet the disk interior. But the cap is
contained in the source hull, whose limit is the disk by (84.5). Thus the limit
segment would lie in `partial B_{1/2}`, impossible because a Euclidean circle contains
no nondegenerate segment. This proves the diameter assertion. Cauchy's bound
`per(C)<=pi diam(C)` proves the perimeter assertion. `square`

## 84.3 Linear-perimeter internal chambers collapse to segments

Let `C_j` be internal inactive chambers with

```math
{\operatorname{per}(C_j)\over D_j}\to\lambda>0.
\tag{84.8}
```

Type II gives total internal inactive area `A_ch=o(D^2)`, so
`area(C_j)=o(D_j^2)`. After scaling and a Blaschke subsequence,

```math
D_j^{-1}C_j\to S\subset B_{1/2}.
```

The limit has zero area. Perimeter is continuous under Hausdorff convergence of
planar convex bodies by Cauchy's width formula, including degenerate limits, so
`per(S)=lambda`. Therefore `S` is a segment of length `lambda/2`, and

```math
\boxed{
{\operatorname{diam}(C_j)\over D_j}\to{\lambda\over2}.
}
\tag{84.9}
```

## 84.4 Exceptional bounded faces are doubled near-geodesics

Suppose `C_j` is a bounded nonquadrilateral contact face of degree `k_j` with
`k_j/D_j->lambda>0`. It is a simple convex unit-edge polygon, hence
`per(C_j)=k_j`. Choose a farthest pair of boundary vertices `a_j,b_j`. Equation
(84.9) gives

```math
|a_j-b_j|=\left({\lambda\over2}+o(1)\right)D_j.
\tag{84.10}
```

The two unit-contact boundary arcs between `a_j,b_j` have lengths `L_j^+,L_j^-`.
Each is at least the chord, while their sum is `(lambda+o(1))D_j`. Hence

```math
\boxed{
L_j^+=L_j^-
=\left({\lambda\over2}+o(1)\right)D_j.
}
\tag{84.11}
```

Both arcs are therefore near-geodesic at the global scale.

## 84.5 Force-hull sides are uniformly sublinear

### Lemma 84.2

If `s_max(F)` is the largest force-hull side length, then

```math
\boxed{s_{max}(F)=o(D).}
\tag{84.12}
```

### Proof

Otherwise normalized force-hull sides would have a subsequential limit joining two
distinct points of `partial B_{1/2}`. The midpoint of each side is also a force-hull
boundary point, so the limiting chord midpoint would lie on the circle. Strict
convexity of the disk puts the midpoint of a nondegenerate chord in the disk interior,
a contradiction. `square`

## 84.6 Outer pockets are out-and-back near-geodesics

Let `C_j` be a convex outer pocket with force-hull closing side `[u_j,v_j]` of length
`s_j` and complementary unit-contact path `W_j`. Assume

```math
{\operatorname{per}(C_j)\over D_j}\to\lambda>0.
\tag{84.13}
```

Lemma 84.2 gives `s_j=o(D_j)`, so the contact-path length is

```math
\ell_j=(\lambda+o(1))D_j.
\tag{84.14}
```

By Section 84.3 the pocket converges to a segment of length `lambda/2`. The normalized
closing-side endpoints coalesce at a point `p in partial B_{1/2}`. Since the limiting
segment lies in the disk and contains this extreme disk point, `p` is one endpoint of
the segment.

Choose a pocket vertex `w_j` farthest from `u_j`. Hausdorff convergence then gives

```math
|u_j-w_j|=|v_j-w_j|
=\left({\lambda\over2}+o(1)\right)D_j,
\tag{84.15}
```

where the second equality also uses `|u_j-v_j|=o(D_j)`. Splitting `W_j` at `w_j`
produces two unit-contact path lengths `L_j^u,L_j^v`; each dominates its chord and
their sum is (84.14). Therefore

```math
\boxed{
L_j^u=L_j^v
=\left({\lambda\over2}+o(1)\right)D_j.
}
\tag{84.16}
```

So a linear-perimeter outer pocket is an out-and-back doubled near-geodesic corridor
from an `o(D)` force-hull side to one common deep extreme.

## 84.7 Only finitely many macroscopic corridors occur at each scale

Canonical Section 77 gives

```math
\sum_{C\text{ internal inactive}}\operatorname{per}(C)\le13\pi D.
\tag{84.17}
```

For fixed `eta>0`, at most

```math
\boxed{13\pi/\eta}
\tag{84.18}
```

internal inactive chambers can have perimeter at least `eta D`. Every such chamber has
one of the two corridor forms above after subsequence extraction. All other chambers
have perimeter `<eta D` individually; exterior caps are already `o(D)` by Theorem
84.1.

## 84.8 Updated Type-II handoff

Together with the current Section 82 harmonic-carrier near-quadrangulation and the
current Section 83 attachment-cell disjointness theorem, the Type-II branch now has
three compatible structural layers:

```text
bulk:
    near-disk force hull
    asymptotically full positive core and strict-rhombus area

harmonic carriers:
    pairwise interior-disjoint convex attachment cells
    boundedly many macroscopic cells carry almost all cell area
    each macroscopic carrier is a boundary-order perturbation of a rhombic
    quadrangulation after local phase cuts

inactive interface:
    exterior caps are o(D) in diameter/perimeter
    every linear-perimeter internal chamber collapses to a segment
    macroscopic exceptional faces and outer pockets are doubled near-geodesic
    contact corridors
    only finitely many occur at each fixed linear scale.
```

The remaining Type-II problem is therefore a boundary-order packing/aggregation
problem for a finite collection of almost-rhombic convex harmonic cells separated by
near-geodesic inactive corridors and a diffuse sublinear-per-piece interface.

## 84.9 Binding caution and next targets

No theorem here says that a near-geodesic unloaded path is locally impossible. The
known near-chain regressions remain valid because equilibrium can use very small
positive transverse weights.

A closing argument must instead use global information. Two precise next targets are:

1. rule out a linear doubled near-geodesic inactive corridor using the disk-like
   diameter support and the adjacent near-quadrangulated harmonic carriers; or
2. if all inactive corridors are sublinear, prove that the coherent-grain / harmonic-
   cell interfaces pay the complete missing boundary coefficient in the strict
   translated-lattice comparison.

## 84.10 Dependency audit

- **Canonical Section 80 / `C-FULLCORE-NEAR-DISK`:** Type-II full-core near-disk
  alternative and `A_ch,A_ext=o(D^2)`.
- **Canonical Section 77 / `C-INACTIVE-CHAMBER`:** convex chamber/cap decomposition and
  `P_ch<=13*pi D`.
- **Canonical Section 68 / `C-PUNCTURED-PHASE`:** source-hull area deficit `O(D)`.
- **Canonical Section 82 / `C-HARMONIC-CARRIER-QUAD`:** compatible near-quadrangulation
  of the macroscopic harmonic carrier; not needed for the collapse proof.
- **Canonical Section 83 / `C-HARMONIC-CELL-TILING`:** attachment-cell disjointness/
  area additivity; not needed for the collapse proof.
- **Convex geometry:** Blaschke selection, Hausdorff continuity of area and perimeter,
  and strict convexity of the Euclidean disk.
- **Contact isolates:** retained throughout.

**Status:** canonical as `C-TYPEII-INTERFACE-COLLAPSE`; see `docs/state/theorem-state.yaml` for lifecycle authority. C-II remains open.
