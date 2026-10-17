> Generated reading edition · [exact source](../../research/target_c_section123_augmented_triangle_boundary_charge.md) · source SHA-256 `13c8f929aec7a6d93bedaaee6af8b8ca886f33bc10873aaae90de92fba964092`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2e42d0e050d3a2d0ab103ecf039c85a269777322", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section123_augmented_triangle_boundary_charge.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "745f053134d4d31bb5ee7c665067e6082cecc74b109077b09b02c57f9105ed90"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — Section 123: augmented triangles charge injectively to nonunit global hull sides

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only structural theorem stacked on Sections 121--122.  
**Dependencies:** canonical Sections 63, 80, 83; proof-only Sections 121 and 122.

Section 121 introduced, for every harmonic attachment cell, the augmented graph
`J_r^+` obtained by adding the sides of `P_r=conv(A_r)`. Its exact defect identity
contains the number `T_r` of bounded triangular faces of `J_r^+`. This section uses the
Type-II near-disk geometry from Section 122 to locate those triangles globally.

The main conclusions are

$$
\boxed{\sum_rT_r\le m,}
\tag{123.1}
$$

where `m` is the number of nonunit sides of the loaded force hull, and

$$
\boxed{
\sum_r P_{{\rm exc},r}
\le5(Q+u_B)
=5(e_{BB}-2k),
\qquad k=d_H+s_Z.
}
\tag{123.2}
$$

This replaces Section 121's coarse bound `10(e_BB-k)` in Type II. The gain is
structural: the complete topology defect `k` disappears from the exceptional-face
payment.

---

## 123.1 Structure of an augmented triangular face

Fix one unloaded positive-contact component `I_r` and its augmented graph `J_r^+` from
Section 121. Recall that `J_r^+` contains

1. every internal and attachment unit contact on `I_r union A_r`; and
2. every side of the convex attachment polygon `P_r=conv(A_r)`.

The original contact graph is triangle-free.

### Lemma 123.1

For every sufficiently large Type-II survivor, every bounded triangular face of
`J_r^+` has vertices

$$
a,x,b
$$

with

- `a,b in A_r`;
- `x in I_r` unloaded;
- `ax` and `xb` unit contacts; and
- `ab` one newly added side of `P_r`, with

$$
1<|a-b|\le2.
\tag{123.3}
$$

### Proof

A triangular bounded face must use at least one newly added polygon side, because a
triangle made entirely of old edges would be a unit-contact triangle.

Suppose it uses at least two added sides. Two of those sides are consecutive sides of
`P_r`; the third edge joins the two remaining endpoints. If this third edge is not
itself a polygon side, it is an old loaded-loaded unit contact. Section 122 says every
such contact is a side of the global loaded hull `F`. But the inherited cyclic order on
`A_r subset B=Vert(F)` has a polygon vertex between the endpoints along one side of
`P_r`. If `P_r` has any further vertex, the endpoints are nonconsecutive globally on
both arcs, contradicting Section 122. The only remaining case is `|A_r|=3`, in which
the three polygon vertices form the whole boundary of `P_r`. Since `I_r` is nonempty
and lies inside `P_r`, that boundary triangle is the outer face, not a bounded face.
Thus a bounded triangular face uses exactly one added polygon side `ab`.

Its other two edges are old unit contacts. Let their common third vertex be `x`. If
`x` were loaded, then `x in A_r` and Section 122 would make both `ax` and `xb` global
hull sides. The inherited cyclic order then again forces `A_r={a,x,b}` for `ab` to be
a side of `P_r`, making the triangle the outer boundary of the cell. Hence `x` is
unloaded and belongs to `I_r`.

Finally `|a-x|=|x-b|=1`, so `|a-b|<=2`. If `|a-b|=1`, all three sides are unit contacts,
contrary to triangle-freeness. Hence (123.3). `square`

---

## 123.2 The added base must be a global hull side

Retain the Type-II near-disk notation of Section 122. After translation,

$$
B(0,r_D)\subset F_D\subset B(0,R_{+,D}),
$$

with

$$
{r_D\over R_{+,D}}\to1,
\qquad r_D\to\infty.
$$

Put

$$
\beta_D=\arccos(r_D/R_{+,D}).
$$

For any two loaded hull vertices at distance at most two, the smaller radial-angle
separation is at most

$$
\gamma_D^{(2)}:=2\arcsin(1/r_D).
$$

Exactly as in the hostile audit of Section 122, the short polar boundary arc between
them has all oriented side directions in an interval of width at most

$$
\tau_D:=2\beta_D+\gamma_D^{(2)}=o(1).
\tag{123.4}
$$

### Lemma 123.2

For all sufficiently large Type-II survivors, the added base `ab` of every triangular
face from Lemma 123.1 is a side of the global force hull `F`.

### Proof

Assume otherwise along an unbounded sequence. Let

$$
s_D:=|a-b|\in(1,2].
$$

Because `a,b` are nonconsecutive global hull vertices, their short polar boundary arc
contains at least two hull sides. Let its oriented side vectors be
`v_1,...,v_j`. Every `|v_i|>=1` by source unit separation, and their directions lie in
an interval of width `tau_D=o(1)`.

Project onto the midpoint direction of that interval:

$$
s_D\ge \sum_{i=1}^j|v_i|\cos(\tau_D/2)
\ge j\cos(\tau_D/2).
\tag{123.5}
$$

Since `s_D<=2`, for all sufficiently large `D` equation (123.5) excludes `j>=3`.
Thus `j=2`; write the unique intermediate loaded hull vertex as `y` and put

$$
\ell_1=|a-y|,
\qquad
\ell_2=|y-b|.
$$

Equation (123.5) gives

$$
2\cos(\tau_D/2)\le s_D\le2,
$$

so

$$
s_D\to2.
\tag{123.6}
$$

The same projection estimate with the actual lengths gives

$$
\ell_1+\ell_2
\le{s_D\over\cos(\tau_D/2)}\to2.
$$

Since `ell_1,ell_2>=1`,

$$
\ell_1,\ell_2\to1.
\tag{123.7}
$$

Let `M_D=(a+b)/2`. The unloaded face vertex `x` satisfies
`|x-a|=|x-b|=1`, hence

$$
|x-M_D|^2=1-{s_D^2\over4}\to0.
\tag{123.8}
$$

For the loaded intermediate vertex `y`, the parallelogram identity gives

$$
|y-M_D|^2
={\ell_1^2+\ell_2^2\over2}-{s_D^2\over4}\to0.
\tag{123.9}
$$

Therefore

$$
|x-y|\le|x-M_D|+|y-M_D|\to0.
$$

But `x` and `y` are distinct source points, one unloaded and one loaded, so source unit
separation requires `|x-y|>=1`. Contradiction. Thus `ab` is a global hull side.
`\square`

By Lemma 123.1 this global hull side is nonunit.

---

## 123.3 The charge is injective across harmonic cells

Assign every augmented triangular face to its added base side `ab`. Within one cell,
one polygon side borders at most one bounded face, so the assignment is injective
inside that cell.

It is also injective between distinct cells. Suppose the same global hull side `ab`
were a side of both `P_r` and `P_s`. Both convex cells lie in the same closed half-plane
bounded by the supporting line through the global hull side `ab`. Both have nonempty
interior because each contains at least three distinct extreme vertices. Near any point
in the relative interior of `ab`, two two-dimensional convex sets that contain `ab` as
a boundary side and lie on the same side of its line have overlapping interior. This
contradicts canonical Section 83:

$$
\operatorname{int}P_r\cap\operatorname{int}P_s=\varnothing.
$$

Hence a global hull side supports at most one augmented triangular face over all cells.
All charged sides are nonunit, so if

$$
T:=\sum_rT_r,
$$

then

$$
\boxed{T\le m.}
\tag{123.10}
$$

---

## 123.4 Sharp global defect algebra

Use the exact Section-121 notation

$$
Q^+:=\sum_rQ_r^+,
\qquad
T=\sum_rT_r,
$$

and the dissection deficit

$$
d_{tile}=q-2-a+2c_I\ge0.
$$

Section 121 proves

$$
e_{BB}-k
={1\over2}(a-T+Q^+)+d_{tile}.
\tag{123.11}
$$

Therefore

$$
Q^+
=2(e_{BB}-k-d_{tile})-a+T.
\tag{123.12}
$$

Section 122 gives

$$
c_B=0,
\qquad
e_{BB}=q-m,
\qquad
e_{BB}=Q+2k+u_B.
\tag{123.13}
$$

Also

$$
a=q-2+2c_I-d_{tile}.
\tag{123.14}
$$

Substituting (123.13)--(123.14) into (123.12) gives the exact identity

$$
\boxed{
Q^+
=Q+u_B-(m-T)-2(c_I-1)-d_{tile}.
}
\tag{123.15}
$$

For sufficiently large Type-II survivors there is at least one unloaded positive-
contact component: the Type-II core has quadratic population while the loaded set has
only `O(D)` vertices. Hence `c_I>=1`. Together with (123.10) and `d_tile>=0`,

$$
\boxed{Q^+\le Q+u_B.}
\tag{123.16}
$$

Section 121 already proves for the actual induced harmonic graphs

$$
P_{{\rm exc},r}\le5Q_r^+.
$$

Summing and applying (123.16),

$$
\boxed{
\sum_rP_{{\rm exc},r}
\le5(Q+u_B).
}
\tag{123.17}
$$

Finally Section 122/63 gives

$$
Q+u_B=e_{BB}-2k,
$$

so (123.2) follows.

---

## 123.5 Composition with the aggregate detour theorem

Proof-only Section 120 gives in Type II

$$
\liminf {1\over D}
\sum_r\bigl(L_r+P_{{\rm exc},r}-2d_r\bigr)
\ge
c_{det}:={\pi\over2}(2-\sqrt3).
\tag{123.18}
$$

Using (123.17), every such survivor must therefore satisfy

$$
\boxed{
\liminf {1\over D}
\left[
\sum_r(L_r-2d_r)+5(Q+u_B)
\right]
\ge c_{det}.
}
\tag{123.19}
$$

Equivalently,

$$
\boxed{
\liminf {1\over D}
\left[
\sum_r(L_r-2d_r)+5(e_{BB}-2k)
\right]
\ge {\pi\over2}(2-\sqrt3).
}
\tag{123.20}
$$

This is a genuine two-currency global obstruction. The bounded-face part can no longer
be paid by topology defect or by nonconsecutive loaded chords. A closing Route-A proof
may now split only between

1. positive aggregate actual outer-walk detour, and
2. positive loaded-boundary surplus `Q+u_B=e_{BB}-2k`.

---

## 123.6 Scope

- The theorem is Type II only and does not address the macroscopic inactive-container
  branch.
- It uses Section 122 only after its independent hostile audit.
- No contact-isolated source point is removed.
- No full-source Section-57 affine-kernel claim is made.
- Sections 121--123 remain proof-only and do not mutate audit.44.
- Equation (123.20) is not itself a contradiction; C-II remains open.
