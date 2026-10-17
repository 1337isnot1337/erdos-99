# Target C — Section 127: harmonic-face fidelity and global defect injection

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**
**Status:** proof-only structural theorem on the post-ZF positive-contact core.
**Dependencies:** canonical Sections 62, 63, 77, 82, 83, 84, 122, 123.

Let `G` be the full nonisolated positive-contact core. For each unloaded component
`I_r`, let `A_r` be its loaded attachment set,

\[
P_r:=\operatorname{conv}(A_r),
\]

and let `H_r` be the induced positive-contact graph on `I_r\cup A_r`.
Canonical Section 82 gives

\[
I_r\subset\operatorname{int}P_r,
\]

and makes every bounded face of `H_r` a simple convex contact polygon. Canonical
Section 83 gives

\[
\operatorname{int}P_r\cap\operatorname{int}P_s=\varnothing
\qquad(r\ne s).
\]

The key finite fact is that local bounded faces are actual global faces, with no
multiplicity across cells.

## 127.1 Cell-interior vertex fidelity

\[
\boxed{V(G)\cap\operatorname{int}P_r=I_r.}
\tag{127.1}
\]

Indeed, if `x in I_s` with `s ne r`, then Section 82 puts
`x in int(P_s)`, so Section 83 excludes `x` from `int(P_r)`.

If `b` is loaded but not in `A_r`, then `b` is an extreme point of the force hull
`F=conv(B)`. Hence

\[
b\notin\operatorname{conv}(B\setminus\{b\})
\supseteq P_r,
\]

so `b notin P_r`. The loaded vertices in `A_r` lie on `partial P_r`. This proves
(127.1).

## 127.2 Every bounded local face is a bounded global face

Let `C` be a bounded face of `H_r`. Its open interior lies in `int(P_r)` and contains
no vertex of `I_r union A_r`; by (127.1), it therefore contains no vertex of `G`.

Suppose an edge of `G\setminus H_r` met `int(C)`. Since neither endpoint lies in the
interior, the straight segment must enter and leave the Jordan domain bounded by
`partial C`. A proper intersection with a boundary contact edge is impossible in the
straight-line planar contact graph. If both intersections are boundary vertices of
`C`, then both edge endpoints lie in `I_r union A_r`; inducedness of `H_r` says that
contact edge already belongs to `H_r`, so it cannot cut an `H_r` face. If only one or
neither intersection is a common endpoint, at least one proper crossing occurs.

Thus `int(C)` contains neither a positive-core vertex nor a positive-core edge, so
`C` is exactly a bounded face of `G`.

Contact-isolated full-source points may lie in `int(C)`; they have no contact edges and
do not split a face of the positive-contact core.

## 127.3 Global-face assignment is injective

If the same bounded global face `C` were a bounded face of both `H_r` and `H_s`, then

\[
\operatorname{int}C
\subseteq
\operatorname{int}P_r\cap\operatorname{int}P_s,
\]

contradicting Section 83. Hence each bounded global face is used by at most one
harmonic cell.

This preserves the physical face degree and all occurrence multiplicities.

## 127.4 Sharp exceptional-perimeter injection

Let `f` be the number of bounded nonquadrilateral faces of `G`, and

\[
Q:=\sum_{C\ {m bounded\ nonquad}}(\deg C-4).
\]

For cell `r`, let `P_{{\rm exc},r}` be the sum of the degrees of its bounded
nonquadrilateral faces. Face fidelity and injectivity give

\[
\boxed{
\sum_rP_{{\rm exc},r}\le4f+Q.
}
\tag{127.2}
\]

Every bounded nonquadrilateral face has degree at least five, so `f<=Q` and

\[
4f+Q\le5Q.
\]

Canonical Section 63 gives

\[
e_{BB}=Q+2k+u_B+c_B,
\qquad k=d_H+s_Z,
\]

with all retained currencies nonnegative. Therefore

\[
Q\le e_{BB}-k
\]

and hence

\[
\boxed{
\sum_rP_{{\rm exc},r}
\le4f+Q
\le5Q
\le5(e_{BB}-k).
}
\tag{127.3}
\]

This strengthens the factor-10 payment in canonical Section 123 while retaining the
strictly sharper exact currency `4f+Q`.

## 127.5 Composition with canonical Section 122

Canonical Section 122 gives

\[
\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\ge {4-2\sqrt3\over D}A_4^0.
\]

Subtracting the valid upper bound (127.2) yields

\[
\boxed{
\sum_r(L_r-2d_r)
\ge {4-2\sqrt3\over D}A_4^0-(4f+Q).
}
\tag{127.4}
\]

In Type II, `A_4^0/D^2 -> pi/4`, so

\[
\liminf {1\over D}\sum_r(L_r-2d_r)
\ge {\pi\over2}(2-\sqrt3)
-\limsup {4f+Q\over D}.
\tag{127.5}
\]

This is a lower demand, not an upper-capacity theorem, so it does not close C-II.

## 127.6 Macroscopic local defect faces are actual inactive corridors

Canonical Sections 67 and 77 classify every bounded nonquadrilateral global face as
an actual internal inactive chamber. By face fidelity, the same is true of every local
bounded nonquadrilateral face.

Thus in Type II, if such a face `C_D` has

\[
\deg(C_D)/D\to\lambda>0,
\]

canonical Section 84 applies directly and gives

\[
\deg C_D-2\operatorname{diam}(C_D)=o(D).
\tag{127.6}
\]

Cutting its cycle at a diameter pair produces two physical near-geodesic routes, but
also introduces an antipodal host pair; no old three-host return constant is retained
after that enlargement.

**Disposition:** proved proof-only finite face-fidelity theorem and Type-II corridor
corollary. C-II remains open.