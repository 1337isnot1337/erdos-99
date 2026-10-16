# Target C — Section 125: augmented triangles sharpen the global defect payment

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**
**Status:** proof-only research candidate on theorem-state `2026-09-12.audit.46`.
**Dependencies:** canonical Sections 63, 80, 83, 122, 123 and proof-only Section 124.

Canonical Section 123 pays all harmonic-cell nonquadrilateral perimeter by
`10(e_BB-k)`. Section 124 removes every nonconsecutive loaded unit chord in Type II.
That extra geometry lets the triangular faces in Section 123's augmented graphs be
charged injectively to nonunit sides of the **global** loaded hull.

The resulting exact improvement is

\[
\boxed{
\sum_rP_{{\rm exc},r}
\le5(Q+u_B)
=5(e_{BB}-2k),
\qquad k=d_H+s_Z.
}
\tag{125.1}
\]

Thus topology defect `k` cannot pay bounded exceptional-face perimeter in the refined
Type-II ledger.

## 125.1 Augmented triangles have one unloaded apex

Use canonical Section-123 notation. For each unloaded component `I_r`, the graph
`J_r^+` contains internal and attachment contacts plus every side of
`P_r=conv(A_r)`. Let `T_r` count its bounded triangular faces.

### Lemma 125.1

For all sufficiently large Type-II survivors, every bounded triangular face of
`J_r^+` is `a-x-b`, where

\[
a,b\in A_r,
\qquad x\in I_r,
\qquad |a-x|=|x-b|=1,
\]

and `ab` is an added noncontact side of `P_r` with

\[
1<|a-b|\le2.
\tag{125.2}
\]

### Proof

A triangular bounded face must use an added polygon side, because the old contact graph
is triangle-free.

If it used two polygon sides, its third edge would join the endpoints of a two-edge
ear of `P_r`. Unless `|A_r|=3`, those endpoints have attachment vertices on both
inherited global boundary arcs and are therefore nonconsecutive loaded vertices. If
the third edge is an old contact, this contradicts Section 124. If `|A_r|=3`, the
triangle is the full polygon boundary and cannot be a bounded face because the nonempty
component `I_r` lies inside it. Three polygon sides are excluded for the same reason.
Hence exactly one face side is an added polygon side `ab`.

The other two sides are old unit contacts through a third vertex `x`. If `x` were
loaded, both contacts would be global hull sides by Section 124. The inherited cyclic
order then forces `A_r={a,x,b}` for `ab` to remain a side of `P_r`, again making the
triangle the outer boundary rather than a bounded face. Thus `x` is unloaded.

The two unit sides give `|a-b|<=2`. Equality `|a-b|=1` would make a forbidden unit
contact triangle, so (125.2) follows. `square`

## 125.2 The base is a nonunit global hull side

For the Type-II hull write, as in Section 124,

\[
B(0,r_D)\subset F_D\subset B(0,R_{+,D}),
\qquad r_D/R_{+,D}\to1.
\]

For any pair of loaded vertices at distance at most two, the short polar boundary arc
has all side directions in an interval of width

\[
\tau_D
\le2\arccos(r_D/R_{+,D})+2\arcsin(1/r_D)
=o(1).
\tag{125.3}
\]

### Lemma 125.2

The side `ab` from Lemma 125.1 is a side of the global force hull `F_D` for all
sufficiently large Type-II survivors.

### Proof

Suppose not along an unbounded sequence. Put `s_D=|a-b|<=2`. Since `a,b` are
nonconsecutive globally, their short polar arc has at least two hull sides. Let its
oriented side vectors be `v_1,...,v_j`. Projection onto the midpoint direction of their
common interval gives

\[
s_D\ge j\cos(\tau_D/2).
\tag{125.4}
\]

For large `D`, (125.4) excludes `j>=3`, so `j=2`. Let `y` be the unique intermediate
loaded vertex and put

\[
\ell_1=|a-y|,
\qquad \ell_2=|y-b|.
\]

Unit separation and the projection bound give

\[
2\cos(\tau_D/2)\le s_D\le2,
\]

and

\[
2\le\ell_1+\ell_2
\le{s_D\over\cos(\tau_D/2)}.
\]

Hence

\[
s_D\to2,
\qquad \ell_1,\ell_2\to1.
\tag{125.5}
\]

Let `M=(a+b)/2`. The unloaded face apex `x` satisfies

\[
|x-M|^2=1-s_D^2/4\to0.
\tag{125.6}
\]

The loaded intermediate vertex satisfies the exact median identity

\[
|y-M|^2
={\ell_1^2+\ell_2^2\over2}-{s_D^2\over4}
\to0.
\tag{125.7}
\]

Thus `|x-y|->0`, contradicting source unit separation. Therefore `ab` is a global hull
side. By Lemma 125.1 it is nonunit. `square`

## 125.3 Global injection and `T<=m`

Charge each augmented triangular face to its global base side `ab`.

Inside one cell, a polygon side borders at most one bounded face. Across different
cells, the same global hull side cannot be a side of two cells: both convex cells would
lie in the same inward half-plane of the supporting line and would have positive-area
overlap in every sufficiently small neighborhood of the relative interior of that
shared side, contradicting canonical Section-83 interior disjointness.

Therefore the charge is globally injective. If

\[
T:=\sum_rT_r
\]

and `m` is the number of nonunit sides of `F`, then

\[
\boxed{T\le m.}
\tag{125.8}
\]

## 125.4 Exact refinement of canonical Section 123

Canonical Section 123 proves

\[
e_{BB}-k
={1\over2}(a-T+Q^+)+d_{tile},
\tag{125.9}
\]

where

\[
Q^+=\sum_rQ_r^+,
\qquad
d_{tile}=q-2-a+2c_I\ge0.
\]

Section 124 gives

\[
c_B=0,
\qquad e_{BB}=q-m=Q+2k+u_B.
\tag{125.10}
\]

Eliminating `a` from (125.9) with

\[
a=q-2+2c_I-d_{tile}
\]

gives the exact identity

\[
\boxed{
Q^+
=Q+u_B-(m-T)-2(c_I-1)-d_{tile}.
}
\tag{125.11}
\]

For sufficiently large Type-II survivors, `c_I>=1`: the positive core has quadratic
population while the loaded hull has only `O(D)` vertices. With (125.8) and
`d_tile>=0`,

\[
\boxed{Q^+\le Q+u_B.}
\tag{125.12}
\]

Canonical Section 123 proves pointwise

\[
P_{{\rm exc},r}\le5Q_r^+.
\]

Summing and using (125.12),

\[
\boxed{
\sum_rP_{{\rm exc},r}
\le5(Q+u_B).
}
\tag{125.13}
\]

Canonical Section 63 plus `c_B=0` gives

\[
Q+u_B=e_{BB}-2k,
\]

which proves (125.1).

## 125.5 Composition with canonical Section 122

Canonical Section 122 gives

\[
\liminf {1\over D}
\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\ge
c_{det}:={\pi\over2}(2-\sqrt3).
\tag{125.14}
\]

The pointwise upper bound (125.13) therefore yields the necessary Type-II inequality

\[
\boxed{
\liminf {1\over D}
\left[
\sum_r(L_r-2d_r)+5(Q+u_B)
\right]
\ge c_{det}.
}
\tag{125.15}
\]

Equivalently,

\[
\boxed{
\liminf {1\over D}
\left[
\sum_r(L_r-2d_r)+5(e_{BB}-2k)
\right]
\ge {\pi\over2}(2-\sqrt3).
}
\tag{125.16}
\]

Compared with canonical Section 123, bounded exceptional faces can no longer hide
behind topology defect `k` or nonconsecutive loaded chords. The full-core closing split
is sharpened to two source-level currencies:

1. aggregate actual outer-walk detour `sum_r(L_r-2d_r)`;
2. loaded-boundary surplus `Q+u_B=e_{BB}-2k`.

## 125.6 Hostile checks

- Lemma 125.2 is uniform over all triangular faces because the near-disk turning bound
  is uniform for every loaded chord of length at most two.
- The contradiction does not assume which side of `ab` contains the intermediate
  loaded vertex `y`; both `x` and `y` converge to the midpoint regardless.
- Cross-cell injection uses the fact that `ab` is a **global hull side**, so both cells
  lie on the same side of its supporting line.
- Equation (125.11) is finite exact algebra; no limsup is used.
- Contact-isolated source points remain untouched.
- Section 125 is Type II only and does not address the macroscopic-container branch.

**Conclusion:** Section 125 is a proof-only structural sharpening of canonical
Sections 122--123. It does not close C-II.
