# Target C — augmented-cell defect budget globalizes local exceptional perimeter

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** canonical from theorem-state `2026-09-12.audit.46`.

This module canonicalizes the concurrent research artifact originally numbered Section 121 as **Section 123** to avoid collision with canonical `C-LOCAL-RETURN-OLER-BRIDGE`.

Its main theorem is the exact global payment bound

\[
\boxed{
\sum_rP_{{\rm exc},r}\le10(e_{BB}-k),
\qquad k=d_H+s_Z.
}
\tag{123.1}
\]

Thus the bounded-nonquadrilateral perimeter appearing in the aggregate Section-122 detour cannot be replicated independently in many harmonic cells.

## 123.1 One augmented harmonic component

Fix an unloaded component `I_r`. Use canonical Section-62 notation

\[
n_r=|I_r|,
\qquad A_r\subset B,
\qquad a_r=|A_r|,
\]

with internal contacts `e_r`, attachment contacts `t_r`, and

\[
s_r=e_r+t_r-2n_r-1\ge0.
\tag{123.2}
\]

Start with only the internal and attachment contacts on `I_r\cup A_r`, and add every side of the convex attachment polygon `P_r=conv(A_r)`. Call the resulting connected plane graph `J_r^+`. Its outer face is the simple `a_r`-cycle `partial P_r`.

Let `T_r` be the number of triangular bounded faces and let

\[
Q_r^+:=\sum_{\deg f\ge5}(\deg f-4).
\]

There are no contact triangles, so every triangular face uses a newly added polygon side and

\[
0\le T_r\le a_r.
\tag{123.3}
\]

The vertex and edge counts are

\[
V_r^+=n_r+a_r,
\qquad
E_r^+=e_r+t_r+a_r=2n_r+1+s_r+a_r.
\tag{123.4}
\]

Euler gives `F_r^+=E_r^+-V_r^++1` bounded faces. Bounded-face incidence is

\[
2E_r^+-a_r=4F_r^+-T_r+Q_r^+.
\tag{123.5}
\]

Substitution yields the exact identity

\[
\boxed{
a_r-3-s_r
={a_r-T_r+Q_r^+\over2}.
}
\tag{123.6}
\]

The right side is nonnegative.

## 123.2 Global polygon-dissection deficit

Canonical Section 83 gives pairwise interior-disjoint attachment cells `P_r`. Triangulate each `P_r` using only its attachment vertices. The resulting noncrossing straight-line graph uses the `q` loaded vertices in convex position, so the total number of bounded triangles is at most `q-2`:

\[
\boxed{
d_{tile}:=q-2-\sum_r(a_r-2)\ge0.
}
\tag{123.7}
\]

Put

\[
a=\sum_ra_r,
\qquad c_I=\#\{I_r\},
\qquad s_C=\sum_rs_r.
\]

Then

\[
d_{tile}=q-2-a+2c_I.
\tag{123.8}
\]

Canonical Section 62 gives the exact pinned ledger

\[
c_I+e_{BB}+s_C=q-2+k.
\tag{123.9}
\]

Combining (123.8), (123.9), and the sum of (123.6),

\[
\boxed{
e_{BB}-k
={1\over2}\sum_r(a_r-T_r+Q_r^+)+d_{tile}.
}
\tag{123.10}
\]

Therefore

\[
\boxed{
\sum_rQ_r^+\le2(e_{BB}-k).
}
\tag{123.11}
\]

Canonical Section 63 also gives

\[
e_{BB}-k=Q+k+u_B+c_B,
\tag{123.12}
\]

so the local harmonic defect is paid by one global loaded-hull/topological currency.

## 123.3 Compare with the actual induced harmonic graphs

Let `H_r` be the actual induced harmonic graph, including all loaded-loaded unit contacts whose endpoints lie in `A_r`. Let

\[
Q_r=\sum_{f\text{ bounded nonquadrilateral}}(\deg f-4),
\]

and let `f_r` be the number of such faces. Then

\[
P_{{\rm exc},r}=4f_r+Q_r.
\tag{123.13}
\]

Add any missing polygon sides to `H_r`, obtaining `\widehat H_r`. This changes only the outer face, so every old bounded nonquadrilateral face remains bounded and

\[
Q_r\le Q(\widehat H_r).
\tag{123.14}
\]

Starting instead from `J_r^+`, obtain `\widehat H_r` by adding the remaining noncrossing loaded-loaded contact chords. Adding a chord splits one face of degree `m` into degrees `m_1,m_2` with `m_1+m_2=m+2`; hence

\[
(m_1-4)_+ +(m_2-4)_+\le(m-4)_+.
\tag{123.15}
\]

Thus degree-above-four defect cannot increase:

\[
Q(\widehat H_r)\le Q_r^+,
\qquad
\boxed{Q_r\le Q_r^+.}
\tag{123.16}
\]

Every bounded nonquadrilateral face has degree at least five, so `f_r<=Q_r`. Hence

\[
P_{{\rm exc},r}
=4f_r+Q_r
\le5Q_r
\le5Q_r^+.
\tag{123.17}
\]

Sum and apply (123.11):

\[
\boxed{
\sum_rP_{{\rm exc},r}
\le10(e_{BB}-k).
}
\tag{123.18}
\]

This proves (123.1).

## 123.4 Interaction with Section 122

Canonical Section 122 gives the Type-II aggregate demand

\[
\liminf {1\over D}
\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\ge {\pi\over2}(2-\sqrt3).
\tag{123.19}
\]

Section 123 pays the bounded-defect part by one global scalar:

\[
\sum_rP_{{\rm exc},r}\le10(e_{BB}-k).
\tag{123.20}
\]

The residual live target is therefore the aggregate outer-walk detour

\[
\sum_r(L_r-2d_r),
\tag{123.21}
\]

coupled to the global loaded-hull/diameter currency. No contradiction is claimed here.

## 123.5 Hostile checks

- The augmented graph is connected and its outer boundary is the attachment polygon.
- The edge count in (123.4) is correct because the starting graph excludes loaded-loaded edges; the `a_r` polygon sides are then added once geometrically.
- The cell triangulations are noncrossing because the convex attachment cells have disjoint interiors.
- Adding loaded-loaded chords cannot increase `(deg-4)_+`; triangles and quadrilaterals contribute zero to this defect.
- No local outer-walk occurrence is assumed globally injective.
- Contact-isolated source points remain globally retained.

**Theorem state:** canonical as `C-AUGMENTED-CELL-DEFECT-BUDGET` from `2026-09-12.audit.46`. C-II remains open.
