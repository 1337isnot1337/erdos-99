> Generated reading edition · [exact source](../../../../docs/targets/target-c/78-harmonic-cell-grid-localization-audit.md) · source SHA-256 `748ec9772789156960064c4d6d70840dbb54da3a5267e49afc845d89fe5f30d4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — harmonic-cell grid localization audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module is a quadratic-core bridge. It combines the canonical Section-69
coherent-grain theorem with the harmonic decomposition obtained by deleting the
loaded force-hull vertices `B`.

The result is stronger than merely having one quadratic physical grain: after deleting
only boundary-order many rhombi, one quadratic coherent subgrain lies entirely inside
one unloaded harmonic component `I_*`, hence inside its convex attachment cell
`P_*=conv(A_*)`. The Sections 73 and 76 complete-grid machinery can then be run inside
that one cell, and the Section-76 diameter bound localizes from the global source
diameter `D` to `diam(P_*)`.

This theorem does not use or alter canonical Section 77's inactive-chamber theorem,
which concerns the complementary subquadratic-core branch.

No source point is deleted from the minimizer. Contact-isolated source points remain
present and uncontrolled. No physical contact is assigned a positive KKT coefficient.

---

# 78. Quadratic coherent rhombus mass localizes in one harmonic cell

Retain the canonical post-ZF notation:

- `B` is the loaded force-hull vertex set and `q=|B|`;
- `I_1,...,I_{c_I}` are the connected components of the unloaded positive-contact
  graph `C[V\B]`;
- `A_r subset B` is the distinct attachment set of `I_r`;
- `P_r=conv(A_r)` and harmonic trapping gives `I_r subset P_r`;
- `a_0=sqrt(3)/2` is the minimum area of a strict unit rhombus.

Work along a quadratic positive-core subsequence. Fix

```math
0<\epsilon<\pi/6.
\tag{78.1}
```

Canonical Section 69 then supplies fixed constants `r,C>0` and an
`epsilon`-coherent physical grain `G` such that

```math
R(G)\ge rD^2,
\qquad
P(G)\le CD,
\tag{78.2}
```

where physical perimeter counts every outer and hole-boundary unit-edge occurrence.

## 78.1 Loaded vertices touch only `O(D)` rhombi

Canonical C35 gives

```math
\deg_C(b)\le3
\qquad(b\in B).
\tag{78.3}
```

Let `R_B(G)` be the number of rhombi of `G` incident to at least one loaded vertex.
A strict rhombus is a simple bounded face. At a fixed planar vertex, distinct bounded
faces occupy distinct sectors between consecutive incident contact edges. Therefore
one loaded vertex is incident to at most its contact degree many strict rhombi. Hence

```math
R_B(G)
\le\sum_{b\in B}\deg_C(b)
\le3q.
\tag{78.4}
```

The loaded vertices are unit-separated convex-hull vertices, so
`q<=per(F)<=pi D`. Thus

```math
\boxed{R_B(G)\le3\pi D.}
\tag{78.5}
```

Delete from `G` every rhombus touching `B`. Let `R^0` be the number of remaining
rhombi. Then

```math
\boxed{R^0\ge rD^2-3\pi D=(r-o(1))D^2.}
\tag{78.6}
```

Every remaining rhombus has all four vertices in `V\B`. Its four boundary contacts
connect those vertices, so they lie in one component `I_r`. Consequently every
edge-connected component of the remaining rhombi lies in one `I_r`, and hence in the
convex cell `P_r`.

## 78.2 The deletion creates only boundary-order new interface

Let `G_1,...,G_s` be the edge-connected components after the deletion. Write `R_j`
for their rhombus counts and `P_j` for their physical perimeters.

Deleting one rhombus can expose at most four new boundary-edge occurrences. Therefore

```math
\sum_jP_j
\le P(G)+4R_B(G)
\le(C+12\pi)D.
\tag{78.7}
```

This estimate includes holes and components created by the deletion.

Each `G_j` has area at least `a_0R_j`. The planar isoperimetric inequality, with all
hole boundaries included in the perimeter, gives

```math
P_j\ge2\sqrt{\pi a_0R_j}.
\tag{78.8}
```

Hence

```math
\boxed{
2\sqrt{\pi a_0}\sum_j\sqrt{R_j}
\le(C+12\pi)D.
}
\tag{78.9}
```

Let `R_*:=max_jR_j`. Since `R^0=sum_jR_j`,

```math
R^0
\le\sqrt{R_*}\sum_j\sqrt{R_j},
```

so (78.9) yields

```math
\boxed{
R_*
\ge {4\pi a_0(R^0)^2\over(C+12\pi)^2D^2}.
}
\tag{78.10}
```

Therefore

```math
\boxed{
\liminf {R_*\over D^2}
\ge r_*:={4\pi a_0r^2\over(C+12\pi)^2}>0.
}
\tag{78.11}
```

Choose a component `G_*` attaining `R_*`. By Section 78.1, all its vertices lie in
one unloaded component `I_*`; let

```math
P_*:=conv(A_*),
\qquad
d_*:=diam(P_*).
\tag{78.12}
```

Harmonic trapping and convexity give

```math
\boxed{G_*\subset P_*.}
\tag{78.13}
```

The subgrain is still `epsilon`-coherent because it is a subcomplex of the single
Section-69 grain `G` and inherits its phase bin and three-phase frame.

Its attachment cell is macroscopic. Since the rhombi of `G_*` have disjoint interiors,

```math
area(P_*)\ge a_0R_*.
\tag{78.14}
```

The isodiametric inequality `area(P_*)<=pi d_*^2/4` gives

```math
\boxed{
 d_*\ge2\sqrt{{a_0R_*\over\pi}}
 =\Omega(D).
}
\tag{78.15}
```

Thus a quadratic-core survivor contains one quadratic coherent rhombic subgrain in
one macroscopic harmonic attachment cell.

## 78.3 The complete grid can be extracted inside the same cell

Let `T_*` be the local train count of `G_*`. Canonical Theorem 10.6 applies to this
finite rhombic complex, with arbitrary holes, and gives

```math
2T_*=P(G_*).
\tag{78.16}
```

Since `P(G_*)<=sum_jP_j`, equation (78.7) gives `T_*=O(D)`, while (78.11) gives
`R_*=Omega(D^2)`.

Every local train of `G_*` is a subsegment of a train of the parent coherent grain and
inherits its phase label and reduced phase potential. Therefore the proof of canonical
Section 73 applies verbatim to `G_*`: there are internally noncrossing,
distinct-phase, all-crossing train families `A,B` with

```math
\boxed{
|A|,|B|\ge {c_{PS}\over2}{R_*\over T_*}=\Omega(D).
}
\tag{78.17}
```

Thus for some fixed `gamma_*>0`, eventually

```math
\boxed{|A|,|B|\ge\gamma_*D.}
\tag{78.18}
```

Since `d_*<=D`, these shores are also linear in the local cell diameter.

Every `A x B` crossing rhombus belongs to `G_*` and therefore lies inside `P_*`.

## 78.4 Section 76 localizes from `D` to `d_*`

Canonical Section 76 proves for a complete phase-pure grid that

```math
D\ge {\sqrt3\over2}(|A|+|B|)
      -{S_{AB}\over\min(|A|,|B|)}-2,
\tag{78.19}
```

where `S_AB` is the sum of the acute-angle defects of the product rhombi. In that
proof, the only use of the ambient `D` in the endpoint step is the bound on the
distance between the two selected crossing centers.

For the present grid, both selected crossing centers belong to rhombi in
`G_* subset P_*`. Hence their distance is at most `d_*`, and the identical projection
argument gives the stronger local statement

```math
\boxed{
 d_*\ge {\sqrt3\over2}(|A|+|B|)
      -{S_{AB}\over\min(|A|,|B|)}-2.
}
\tag{78.20}
```

Canonical Section 68 gives the global angular-defect bound

```math
S_{AB}<C_{phase}D.
\tag{78.21}
```

Together with (78.18),

```math
{S_{AB}\over\min(|A|,|B|)}
<{C_{phase}\over\gamma_*}=O(1).
\tag{78.22}
```

Therefore

```math
\boxed{
|A|+|B|
\le {2\over\sqrt3}d_*+O(1),
}
\tag{78.23}
```

and AM-GM gives

```math
\boxed{
|A||B|
\le {d_*^2\over3}+O(d_*).
}
\tag{78.24}
```

The right-hand scale is now the diameter of one actual harmonic attachment cell,
not the full source diameter.

## 78.5 What this changes and what remains

The canonical quadratic-core branch now has the implication

```text
m=Omega(D^2)
 -> one Section-69 quadratic coherent grain
 -> delete only O(D) loaded-touching rhombi
 -> one quadratic coherent subgrain G_* contained in one I_*
 -> G_* subset P_*=conv(A_*), diam(P_*)=Omega(D)
 -> one Omega(D) x Omega(D) complete phase-pure grid in P_*
 -> local grid budget
      diam(P_*) >= (sqrt(3)/2)(a+b)-O(1).
```

This closes a structural mismatch: the train-grid theorem and the harmonic-response
cell theorem can now be applied to the same macroscopic object.

It does **not** close C-II. In particular:

1. the Fox--Pach constant does not force the extracted grid to violate (78.23);
2. no theorem yet says that one complete grid covers a near-one fraction of `G_*`;
3. local reducibility of `P_*` alone would not imply a reduction of the global source
   diameter; a closing deformation must preserve all source constraints and decrease
   the actual global diameter;
4. the complementary subquadratic-core branch is governed by canonical Section 77's
   macroscopic inactive chamber and still requires a full-source closing argument.

The next exact quadratic-core task is now local: prove a coverage/aggregation theorem
for the coherent train crossing graph of `G_*` strong enough to violate (78.23), or
couple the harmonic response structure on `I_* subset P_*` to the common-order grid
to construct a source-preserving strict global competitor.

## 78.6 Dependency audit

- **Section 69:** quadratic coherent physical grain with `R=Omega(D^2)` and `P=O(D)`.
- **C35:** `deg_C(b)<=3` for loaded vertices.
- **Harmonic trapping:** `I_r subset conv(A_r)`.
- **Theorem 10.6:** train paths, `2T=P`, pseudosegment crossing geometry with holes.
- **Section 73:** complete phase-pure grid extraction; its proof applies to any
  coherent strict-rhombus subcomplex satisfying the same inputs.
- **Section 76:** signed common order and defect-averaged complete-grid diameter bound.
- **Section 68:** `S_AB=O(D)` angular-defect budget.
- **Section 77:** not used; it is the separate subquadratic-core chamber theorem.
- **Contact isolates:** retained globally and untouched by this proof.

**Status:** canonical as `C-HARMONIC-GRID-LOCAL`; see `docs/state/theorem-state.yaml` for lifecycle authority. C-II remains open.
