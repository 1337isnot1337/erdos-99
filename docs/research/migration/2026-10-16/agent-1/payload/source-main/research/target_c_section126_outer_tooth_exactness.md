# Target C — Section 126: augmented triangles are exactly the two-edge hull teeth

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**
**Status:** proof-only research candidate on theorem-state `2026-09-12.audit.46`.
**Dependencies:** canonical Sections 63, 67, 83, 123 and proof-only Sections 124--125.

This section identifies the triangular term `T` in canonical Section 123 with an
actual outer-walk statistic. In sufficiently large Type-II survivors, a bounded
triangular face of an augmented harmonic cell is exactly a nonunit loaded-hull side
whose distinguished outer contact-face route has two unit edges.

Write the loaded hull vertices in cyclic order as

\[
B=(b_1,\ldots,b_q),
\qquad s_i:=|b_i-b_{i+1}|,
\]

and let `W_i` be the canonical Section-63 outer-face interval from `b_i` to
`b_{i+1}`, with occurrence length `ell_i`. Let

\[
M:=\{i:s_i>1\},
\qquad m:=|M|.
\]

Canonical Section 63 defines

\[
x_B=\sum_i(\ell_i-1),
\qquad u_B=x_B-m\ge0.
\]

Let `T=sum_r T_r` be the number of bounded triangular faces in the augmented cell
graphs `J_r^+` of canonical Section 123.

The main theorem is

\[
\boxed{
T=\#\{i\in M:\ell_i=2\}.
}
\tag{126.1}
\]

Consequently

\[
\boxed{0\le m-T\le u_B.}
\tag{126.2}
\]

Thus `u_B` is not merely abstract outer-walk slack: it pays every nonunit loaded-hull
side that fails to be a simple two-edge tooth.

---

## 126.1 Every two-edge nonunit interval gives one augmented triangle

Fix `i in M` with `ell_i=2`. Write

\[
W_i=b_i-x-b_{i+1}.
\tag{126.3}
\]

Both edges in (126.3) are unit contacts.

For all sufficiently large Type-II survivors, `x` is unloaded. Indeed, if `x` were
loaded, proof-only Section 124 would make both contacts `b_i x` and `x b_{i+1}` sides
of the global loaded hull. Since `b_i,b_{i+1}` are already consecutive loaded-hull
vertices, this is possible only when the loaded hull has three vertices. Canonical
Section 59 gives `q>=h` and `h/D` bounded below by a positive constant, so `q>3` for
all sufficiently large Type-II survivors.

Let `I_r` be the unloaded positive-contact component containing `x`. Then
`b_i,b_{i+1} in A_r`. Because they are consecutive in the full cyclic set `B`, they
are consecutive in the subset `A_r`; therefore the chord `b_i b_{i+1}` is a side of

\[
P_r=\operatorname{conv}(A_r).
\]

It is not an old contact because `i in M`, so it is one of the polygon sides added in
forming `J_r^+`.

Canonical Section 67 forms the global hull augmentation `Ghat` by adding every missing
loaded-hull side. The added side `b_i b_{i+1}` lies on `partial F`, and its inward
incident face is the convex outer pocket cut from the old outer face. Because the
canonical distinguished old outer-face interval between its endpoints is exactly
(126.3), that pocket has boundary

\[
b_i-x-b_{i+1}-b_i.
\]

Hence it is a triangular face of `Ghat`.

The open triangle contains no positive-contact vertex. Loaded vertices are extreme
vertices of `F` and none lies in the interior. If a vertex of another unloaded
component lay there, its harmonic cell would have interior intersecting `P_r`,
contrary to canonical Section 83. Therefore the same triangle is a bounded face of the
induced augmented cell graph `J_r^+`.

Thus every `i in M` with `ell_i=2` produces a distinct augmented triangular face. The
base side identifies `i`, so the map is injective. Therefore

\[
T\ge\#\{i\in M:\ell_i=2\}.
\tag{126.4}
\]

---

## 126.2 Every augmented triangle is one of those outer teeth

Conversely, take a bounded triangular face of some `J_r^+`. Proof-only Section 125
shows that it has vertices

\[
a-x-b,
\]

where

- `a,b` are loaded vertices;
- `x` is unloaded;
- `ax` and `xb` are unit contacts; and
- `ab` is a nonunit side of the global loaded hull `F`.

In particular `a,b` are consecutive vertices of `B`, so `ab=b_i b_{i+1}` for a unique
`i in M`.

The open triangle lies in `int(P_r)`, except for its global hull base. By canonical
Section 83, no other harmonic cell has a positive-contact vertex in this open
triangle. No loaded vertex lies there because every loaded vertex is extreme in `F`.
The face assumption in `J_r^+` already excludes vertices of `I_r` and crossing edges.
Hence the open triangle contains no vertex or edge of the full positive-contact graph.

After adding the global hull side `ab`, the triangle is therefore the inward face of
`Ghat` incident to `ab`. Removing the added side shows that the old outer-face boundary
between the corresponding distinguished occurrences of `a,b` is exactly the two-edge
path

\[
a-x-b.
\]

Thus the canonical Section-63 interval has

\[
\ell_i=2.
\]

Different augmented triangular faces have different global base sides by the
cross-cell injectivity already proved in Section 125. Hence

\[
T\le\#\{i\in M:\ell_i=2\}.
\tag{126.5}
\]

Combining (126.4)--(126.5) proves (126.1).

---

## 126.3 Exact outer-slack decomposition

Canonical Section 63 gives

\[
u_B
=x_B-m
=\sum_i(\ell_i-1)-m.
\]

Split the sum into nonunit and unit hull sides:

\[
\boxed{
 u_B
 =\sum_{i\in M}(\ell_i-2)
 +\sum_{i\notin M}(\ell_i-1).
}
\tag{126.6}
\]

Every summand is nonnegative: `ell_i>=2` on `M` and `ell_i>=1` elsewhere. By (126.1),
exactly `m-T` indices in `M` have `ell_i>=3`. Each contributes at least one to the
first sum in (126.6). Therefore

\[
\boxed{m-T\le u_B.}
\]

Together with Section 125's `T<=m`, this proves (126.2).

Equation (126.6) also records the equality structure. If `u_B=0`, then

1. every nonunit loaded-hull side has a two-edge outer tooth;
2. every unit loaded-hull interval uses a single outer contact occurrence; and
3. by (126.1), `T=m`.

No claim is made that small positive `u_B` forces metric smallness of the individual
teeth; the nonunit base length may range through `(1,2]`.

---

## 126.4 Interaction with Section 125

Section 125 gives the exact identity

\[
Q^+
=Q+u_B-(m-T)-2(c_I-1)-d_{tile}.
\tag{126.7}
\]

Section 126 identifies each nonnegative subtraction term geometrically. In particular,
put

\[
r_{deep}:=m-T.
\]

Then

\[
0\le r_{deep}\le u_B
\]

and

\[
\boxed{
Q^+=Q+(u_B-r_{deep})-2(c_I-1)-d_{tile}.
}
\tag{126.8}
\]

Thus the part of `u_B` spent merely upgrading a nonunit side from a two-edge tooth to
a deeper/repeated detour does **not** pay augmented exceptional-face degree.

The remaining Type-II closure problem is correspondingly sharper: a survivor must
store the Section-122 aggregate detour floor either in actual cell route excess, in
bounded-face defect `Q`, or in the residual outer-walk multiplicity
`u_B-r_deep`, while a near-zero residual forces an almost pure chain of two-edge hull
teeth.

---

## 126.5 Scope and regressions

- The theorem is Type II only because Section 124 is used to exclude a loaded middle
  vertex in a two-edge tooth and Section 125 is used in the converse.
- Bridge and articulation repetitions are retained. They appear in the occurrence
  lengths `ell_i` and can only increase the nonnegative terms in (126.6).
- Contact-isolated source points are untouched; the theorem concerns the positive
  contact graph and its harmonic cells.
- No full-source Section-57 kernel statement is used.
- The theorem does not turn two-edge teeth into unit triangles: their bases remain
  strictly longer than one.
- C-II remains open.
