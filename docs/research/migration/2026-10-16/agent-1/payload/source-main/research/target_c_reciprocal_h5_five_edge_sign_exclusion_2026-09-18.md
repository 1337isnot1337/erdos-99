# Target C-II — every H5 reciprocal sign color has at least six edges

**Date:** 2026-09-18  
**Status:** proved candidate; theorem-state authority unchanged  
**Scope:** the five-hull-vertex branch of the minimal reciprocal `K_6` obstruction  
**Depends on:** `target_c_one_anchor_k5_reciprocal_unit_force_2026-09-18.md`; `target_c_reciprocal_hull_angle_sign_split_2026-09-18.md`  
**Supersedes in strength:** the special pentagram-class exclusion in `target_c_reciprocal_h5_pentagram_sign_exclusion_2026-09-18.md`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The H5 reciprocal hull consists of five cyclic hull vertices and one interior point.
The hull-angle theorem proves that every hull vertex has a `2+3` incident sign split.
This note combines that local degree fact with the exact reciprocal signed-length
balance to rule out *every* sign assignment in which one sign occurs on only five of
the fifteen reciprocal edges.

After global reversal of all signs, every surviving H5 reciprocal `K_6` therefore has
sign-count split either

\[
\boxed{6+9\quad\text{or}\quad7+8.}
\]

The previous pentagram exclusion is one special five-edge instance of the argument
below.

---

## 1. A minority sign color has at least five edges

Let `m` be the number of positive reciprocal edges after globally reversing all signs,
if necessary, so that

\[
m\le 15-m.
\tag{1.1}
\]

At each of the five hull vertices, the positive degree is either two or three.  Thus the
sum of positive degrees over the hull vertices is at least ten.  Since the total
positive degree over all six vertices is `2m`,

\[
2m\ge10,
\]

hence

\[
\boxed{m\ge5.}
\tag{1.2}
\]

Together with (1.1), only `m=5,6,7` are possible before the argument below.

---

## 2. Structure forced by `m=5`

Assume for contradiction that `m=5`.  Then the total positive degree is exactly ten.
But the five hull vertices already contribute at least ten positive incidences.  Hence:

1. every hull vertex has positive degree exactly two;
2. the interior reciprocal point `x` has positive degree zero; and
3. all five positive edges lie among the hull vertices.

A simple two-regular graph on five vertices is necessarily a five-cycle.  Call this
positive hull cycle `C_+`.

Inside the complete graph `K_5` on the hull vertices, the five remaining hull edges are
the complement of `C_+`.  The complement of a five-cycle is again a five-cycle; call it
`C_-`.

All five spokes from the interior point to the hull are negative.

Write

\[
L_+:=\sum_{e\in C_+}|e|,
\qquad
L_-:=\sum_{e\in C_-}|e|,
\qquad
S:=\sum_{i=0}^4|x-v_i|.
\tag{2.1}
\]

The exact signed length balance from reciprocal equilibrium would require

\[
\boxed{L_+=L_-+S.}
\tag{2.2}
\]

---

## 3. The complementary hull cycle gives `L_+<2L_-`

Every edge of `C_+` is a nonedge of the complementary five-cycle `C_-`.  In a five-cycle,
each nonedge joins two vertices at graph distance two.  Therefore each positive edge
has a two-edge path between the same endpoints using edges of `C_-`.

The three reciprocal vertices on such a path are noncollinear.  Strict triangle
inequality gives

\[
|e_+|<|e_-^{(1)}|+|e_-^{(2)}|.
\tag{3.1}
\]

Summing (3.1) over all five positive edges, every edge of `C_-` occurs exactly twice
among the chosen two-edge paths.  Hence

\[
\boxed{L_+<2L_-.}
\tag{3.2}
\]

This is the same pentagon/pentagram inequality as in the earlier special-case note, but
it is intrinsic to the complementary pair of abstract five-cycles and does not depend
on either cycle being the geometric hull boundary.

---

## 4. The interior point gives `L_+<2S`

For each positive hull edge `v_i v_j`, the interior reciprocal point `x` is not collinear
with its endpoints.  Thus

\[
|v_i-v_j|<|v_i-x|+|x-v_j|.
\tag{4.1}
\]

Every hull vertex has degree two in `C_+`.  Summing (4.1) over the five positive cycle
edges therefore counts every spoke exactly twice and gives

\[
\boxed{L_+<2S.}
\tag{4.2}
\]

---

## 5. Contradiction

From (3.2) and (4.2),

\[
L_+<2\min(L_-,S).
\tag{5.1}
\]

For positive `L_-` and `S`,

\[
2\min(L_-,S)\le L_-+S.
\tag{5.2}
\]

Therefore

\[
\boxed{L_+<L_-+S,}
\tag{5.3}
\]

contradicting the exact signed length balance (2.2).

So `m=5` is impossible.

Because global sign reversal exchanges `m` with `15-m`, the result can be stated
symmetrically:

\[
\boxed{
\text{in every H5 reciprocal unit-force equilibrium, each sign occurs on at least six
of the fifteen edges.}
}
\tag{5.4}
\]

Equivalently, the only possible sign-count splits are

\[
\boxed{6+9\ \text{or}\ 7+8.}
\tag{5.5}
\]

---

## 6. Frontier effect

The H5 finite target now has three exact filters before any coordinate solve:

1. every hull vertex has signed degree `2` or `3`;
2. both sign colors contain at least six edges; and
3. the positive and negative edge sets have exactly equal total Euclidean length and
   identical length-weighted directional second moments.

The first two are purely finite/combinatorial consequences once the reciprocal metric
equilibrium is available.  In particular, all five-edge minority patterns are removed,
not merely the symmetric geometric pentagram pattern.

The remaining H5 sign-count cases are `6+9` and `7+8`.  Their degree ledgers are already
small.  If the minority color has six edges and the interior point has minority degree
`d_x`, then the number `t` of hull vertices of minority degree three satisfies

\[
t+d_x=2.
\tag{6.1}
\]

Thus only `(t,d_x)=(0,2),(1,1),(2,0)` can occur.  If the minority color has seven edges,
then

\[
t+d_x=4.
\tag{6.2}
\]

These finite ledgers give a sharper starting point for combining cyclic edge order,
source `<120` force gaps, and the translation-surface rotation system.

No theorem-state file is changed.

**Disposition:** eliminated every H5 reciprocal signing with a five-edge minority sign
color; any H5 survivor must have sign counts `6+9` or `7+8`, with the exact hull/interior
degree ledgers above.  C-II remains open.