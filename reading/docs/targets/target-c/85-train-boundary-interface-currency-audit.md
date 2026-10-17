> Generated reading edition · [exact source](../../../../docs/targets/target-c/85-train-boundary-interface-currency-audit.md) · source SHA-256 `8618a1ae469f6f7c63a8afa4ef452f77edfacc3b00479282c977cfc43f28af79`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — train-boundary interface currency audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module extracts an exact boundary-order consequence of the global strict-rhombus
complex. The input is elementary but was not previously coupled to the inactive-cell
Oler ledger.

Let `R_4` be the number of bounded quadrilateral contact faces and let `B_4` be the
number of contact-edge occurrences incident to exactly one such face. Canonical
Theorem 10.6 applies to the collection of all strict rhombi, with arbitrary holes and
components, and gives

```math
B_4\ge4\sqrt{R_4}.
```

Every such boundary occurrence faces either the old outer contact face or one bounded
nonquadrilateral face. This forces a definite amount of outer-walk / exceptional-face
interface. Combining that interface count with the exact Section-67 Oler absorption
identities gives a new finite chamber-capacity inequality.

The main finite conclusions are

```math
\boxed{q-k+2f\ge2\sqrt{R_4},}
\tag{85.1}
```

```math
\boxed{m-R_4\ge\sqrt{R_4}+1,}
\tag{85.2}
```

and

```math
\boxed{
A_{ch}-a_0Z_{ch}
\ge {3c_0\over5}\bigl(4\sqrt{R_4}-P_F\bigr),
}
\tag{85.3}
```

where

- `m` is the positive-core population;
- `f` is the number of bounded nonquadrilateral contact faces;
- `q=|B|` is the loaded force-hull vertex count;
- `k=d_H+s_Z`;
- `P_F=per(F)`;
- `A_ch` is the total internal inactive-chamber area;
- `Z_ch` is the total contact-isolated population assigned to those chambers;
- `a_0=sqrt(3)/2`; and
- `c_0=sqrt(3)/4`.

In the canonical Section-80 Type-II branch,

```math
{R_4\over D^2}\to {\pi\over2\sqrt3},
\qquad
{P_F\over D}\to\pi.
```

Hence (85.3) yields a strict universal boundary-order floor

```math
\boxed{
\liminf {A_{ch}-a_0Z_{ch}\over D}
\ge
\beta_{tr}
:={3\sqrt3\over20}
\left(4\sqrt{{\pi\over2\sqrt3}}-\pi\right)
>0.1734.
}
\tag{85.4}
```

Thus Type II cannot make the entire inactive interface disappear even at first order.
The near-disk rhombus packing has too many train ends to fit on the circular force-hull
boundary; a fixed linear amount of interface currency must remain inside `F`.

This is not yet a contradiction. Thin exceptional faces, including the existing
near-degenerate pentagon regression, can pay boundary-order interface currency with
arbitrarily small additional geometric width. Section 85 therefore identifies the
precise remaining currency rather than claiming a false local closure.

---

# 85. Exact train-boundary and inactive-interface inequalities

Retain the canonical post-ZF notation of Sections 61, 63, 67, and 77.

Let

```math
\mathcal R_4
```

be the collection of every bounded quadrilateral contact face. Canonical Section 67
shows that every member is a strict unit rhombus. Put

```math
R_4:=|\mathcal R_4|.
```

Let `B_4` count contact-edge occurrences incident to exactly one member of
`\mathcal R_4`. This is the physical boundary length of the complete rhombus complex,
with all component and hole boundaries counted.

## 85.1 The global rhombus complex has many boundary edges

Canonical Theorem 10.6 applies to any finite collection of strict unit rhombi,
without connectedness or disk topology. It gives

```math
R_4\le {B_4^2\over16}.
```

Therefore

```math
\boxed{B_4\ge4\sqrt{R_4}.}
\tag{85.5}
```

Every edge occurrence counted by `B_4` has a rhombus on one side and no rhombus on
the other. The other side is either

1. the old outer contact face, or
2. a bounded nonquadrilateral contact face.

Let `b` be the outer-face boundary-walk length. Let `f` be the number of bounded
nonquadrilateral faces and

```math
Q:=\sum_{P}(\deg P-4).
```

Their total boundary degree is

```math
\sum_P\deg P=4f+Q.
```

Counting all possible recipients of a rhombus-boundary occurrence gives

```math
\boxed{B_4\le b+4f+Q.}
\tag{85.6}
```

No equality is asserted: an outer/nonquadrilateral boundary edge need not border a
quadrilateral face.

Canonical loaded-hull algebra gives

```math
b=q+x_B,
\qquad
q-x_B=Q+2k.
```

Hence

```math
\boxed{b+Q=2(q-k).}
\tag{85.7}
```

Combining (85.5)--(85.7),

```math
4\sqrt{R_4}
\le2(q-k)+4f,
```

which is exactly (85.1):

```math
\boxed{q-k+2f\ge2\sqrt{R_4}.}
```

## 85.2 A finite second-order population deficit

Canonical Section 67 gives the exact face count

```math
\boxed{m=R_4+f+q-k+1.}
\tag{85.8}
```

Also `q-k>=0`; in fact the canonical identity

```math
q-x_B=Q+2k
```

with `x_B,Q>=0` gives the stronger `q>=2k`.

Now

```math
f+q-k
\ge {1\over2}\bigl(2f+q-k\bigr)
\ge\sqrt{R_4},
```

where the final inequality is (85.1). Substitute in (85.8):

```math
\boxed{m-R_4\ge\sqrt{R_4}+1.}
```

This is (85.2). It is finite and branch-independent.

In Type II, Section 80 gives

```math
{R_4\over D^2}\to\Delta_2:={\pi\over2\sqrt3}.
```

Thus

```math
\boxed{
\liminf {m-R_4\over D}
\ge\sqrt{\Delta_2}
=\sqrt{{\pi\over2\sqrt3}}
>0.9523.
}
\tag{85.9}
```

So even though both `m` and `R_4` have the same quadratic leading density in Type II,
their difference is forced to remain at least linear.

## 85.3 Exact inactive-chamber area surplus

Canonical Section 77 partitions the inactive region inside `F` into

- bounded nonquadrilateral contact faces, carrying population `Z_def` and total area
  `A_exc`; and
- convex outer pockets cut from the old outer face, carrying population `Z_in` and
  total area `H_out`.

Thus

```math
A_{ch}=A_{exc}+H_{out},
\qquad
Z_{ch}=Z_{def}+Z_{in}.
\tag{85.10}
```

Section 67 proves for the exceptional bounded faces

```math
\boxed{
A_{exc}\ge a_0(Z_{def}+f)+c_0Q.
}
\tag{85.11}
```

For the outer pockets it proves

```math
Z_{in}
\le {H_{out}\over a_0}+{P_F-b\over2}.
```

Because `a_0/2=c_0`, this is equivalent to

```math
\boxed{
H_{out}-a_0Z_{in}
\ge c_0(b-P_F).
}
\tag{85.12}
```

Add (85.11) and (85.12):

```math
\boxed{
A_{ch}-a_0Z_{ch}
\ge
c_0\bigl[(b-P_F)+(2f+Q)\bigr].
}
\tag{85.13}
```

Every term on the right is nonnegative: `b>=P_F` canonically and `Q,f>=0`.

## 85.4 At least three-fifths of train-interface excess pays chamber surplus

Define

```math
d:=b-P_F\ge0,
```

and the larger raw interface currency

```math
J:=d+4f+Q.
\tag{85.14}
```

Equation (85.6) gives

```math
J\ge B_4-P_F.
\tag{85.15}
```

The currency appearing in (85.13) is

```math
H:=d+2f+Q.
\tag{85.16}
```

Since every nonquadrilateral bounded face has degree at least five,

```math
Q\ge f.
```

Therefore

```math
5H-3J
=2(d+Q-f)
\ge0,
```

so

```math
\boxed{H\ge{3\over5}J.}
\tag{85.17}
```

Combine (85.13), (85.15), (85.17), and (85.5):

```math
A_{ch}-a_0Z_{ch}
\ge {3c_0\over5}(B_4-P_F)
\ge {3c_0\over5}(4\sqrt{R_4}-P_F).
```

This proves the finite theorem (85.3).

## 85.5 Type-II numerical boundary floor

Work now in the Type-II branch of canonical Section 80. There

```math
{R_4\over D^2}\to\Delta_2={\pi\over2\sqrt3}.
\tag{85.18}
```

Section 80 also gives Hausdorff convergence, after translation,

```math
D^{-1}F\to B_{1/2}.
```

Cauchy's width formula makes convex perimeter continuous under Hausdorff convergence,
so

```math
\boxed{{P_F\over D}\to\pi.}
\tag{85.19}
```

Apply (85.3), divide by `D`, and take the lower limit:

```math
\liminf {A_{ch}-a_0Z_{ch}\over D}
\ge
{3c_0\over5}\left(4\sqrt{\Delta_2}-\pi\right).
```

Since `c_0=sqrt(3)/4`, this is

```math
\boxed{
\beta_{tr}
={3\sqrt3\over20}
\left(4\sqrt{{\pi\over2\sqrt3}}-\pi\right)
=0.1734627\ldots>0.
}
\tag{85.20}
```

The underlying train-boundary excess itself has coefficient

```math
\boxed{
\kappa_{tr}
:=4\sqrt{{\pi\over2\sqrt3}}-\pi
=0.6676585\ldots>0.
}
\tag{85.21}
```

Thus Type II has a genuinely nonzero first-order interface obligation:

```math
B_4-P_F\ge(\kappa_{tr}-o(1))D,
\tag{85.22}
```

and at least the fixed fraction encoded by (85.20) is visible in the actual
inactive-chamber area/population surplus.

## 85.6 Interaction with Sections 82--84

Current canonical Sections 82--84 sharpen the geometric meaning of the same
interface currency.

- Section 82: a macroscopic harmonic carrier is itself a boundary-order perturbation
  of a strict-rhombus quadrangulation.
- Section 83: harmonic attachment cells have pairwise disjoint interiors and become
  area-additive in the rhombic-saturation branch.
- Section 84: in Type II, every exterior cap is `o(D)` and every internal inactive
  chamber of linear perimeter collapses to a doubled near-geodesic contact corridor.

Therefore the positive constant `kappa_tr` cannot disappear into exterior caps or
bulk inactive area. At first order it must be paid by

1. outer-contact detour `b-P_F`,
2. bounded nonquadrilateral face degree, and
3. the doubled near-geodesic corridor structure of Section 84 (when individual
   chambers are macroscopic).

This is a substantially narrower boundary problem than the original arbitrary-holed
polycrystal.

## 85.7 Binding regression: this is not yet a contradiction

The inequality (85.4) does **not** close Type II.

A near-degenerate convex pentagonal contact face can have linear perimeter/degree
currency while its width and excess area above the best one-dimensional limit are
arbitrarily small. Likewise a long doubled near-geodesic corridor can carry a linear
amount of contact-boundary length while collapsing to a segment after normalization.
These are compatible with Section 84.

Hence the invalid inference

```text
linear train-boundary excess
 -> linear Euclidean hole area
 -> contradiction with A_ch=o(D^2)
```

must not be used. Section 85 proves only the exact Oler-weighted area/population
surplus (85.3)--(85.4).

The next missing theorem must exploit information beyond generic convex packing. Two
precise targets are:

1. show that a linear doubled near-geodesic corridor adjacent to the Type-II
   near-quadrangulated harmonic cells forces additional diameter-load or phase-grid
   cost; or
2. prove a source-preserving boundary-order deformation / strict packing inequality
   whose coefficient exceeds the unavoidable train-interface floor.

## 85.8 Dependency audit

- **Theorem 10.6:** finite train-track boundary bound `B_4>=4sqrt(R_4)`, valid with
  holes and disconnected rhombus complexes.
- **Canonical Section 67 / `C-RHOMBUS-POP`:** convex face classification, exact face
  count, exceptional-face Oler bound, outer-pocket Oler bound.
- **Canonical Section 63 / `C-LOADED-HULL`:** `b=q+x_B` and
  `q-x_B=Q+2(d_H+s_Z)`.
- **Canonical Section 80 / `C-FULLCORE-NEAR-DISK`:** only for the Type-II asymptotic
  constants `R_4/D^2->Delta_2` and `F/D->B_{1/2}`.
- **Canonical Sections 82--84:** interpretation/handoff only, not dependencies of the
  finite inequalities.
- **Contact-isolated source points:** retained and explicitly counted in `Z_ch`.

**Status:** canonical as `C-TRAIN-INTERFACE-CURRENCY`; see `docs/state/theorem-state.yaml` for lifecycle authority. C-II remains open.
