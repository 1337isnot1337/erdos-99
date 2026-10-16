# Target C — Section 152 candidate: carrier area slack forces a stronger diameter-edge density tradeoff

**Date:** 2026-09-12  
**Base:** hostile-audited proof-only Sections 148 and 151  
**Status:** proof-only Type-II frontier tradeoff; C-II remains open

Section 148 eliminated the nonunit-side variable after dropping the exact nonnegative component remainder

\[
G_D:=2+q+m-k-\sum_rd_r.
\]

Section 150 identifies

\[
G_D=R_I+s_B+\sum_r(\delta_r+2-d_r)\ge0,
\]

and Section 151 gives a quantitative lower bound on `G_D` from the strict-rhombus area of any one harmonic component.

Keeping this currency instead of discarding it gives the exact strengthened elimination

\[
\boxed{
5q-7k
\ge
3\sum_rd_r+2G_D+c_{det}D-O(1)-o(D),
}
\tag{152.1}
\]

where

\[
c_{det}:={\pi\over4}(2-\sqrt3).
\]

Equivalently,

\[
\boxed{
5h-2d_H-7s_Z
\ge
3\sum_rd_r+2G_D+c_{det}D-o(D).
}
\tag{152.2}
\]

For any selected harmonic carrier `r`, Section 151 gives

\[
G_D
\ge r_r+(\delta_r+2-d_r)
\ge\sqrt{\pi A_{4,r}^{int}}+2-d_r.
\tag{152.3}
\]

Hence a carrier with normalized diameter `lambda`, internal strict-rhombus area density at least `A`, and a global harmonic diameter moment at least `S` forces

\[
\boxed{
5h-2d_H-7s_Z
\ge
\left[3S+2(\sqrt{\pi A}-\lambda)+c_{det}\right]D-o(D).
}
\tag{152.4}
\]

whenever the bracketed area-slack term is positive; replacing it by its positive part gives a universally safe form.

At the sharp Section-118 frontier,

\[
\lambda_*=0.9762439137425688\ldots,
\]

\[
A_*=0.4703752868004241\ldots,
\]

and hostile-audited Section 148 gives

\[
S_*=2.798596312209462\ldots .
\]

Therefore

\[
\sqrt{\pi A_*}-\lambda_*
=0.239374260456223\ldots
\]

and (152.4) becomes

\[
\boxed{
5h-2d_H-7s_Z
\ge
9.084984261160066\ldots D-o(D).
}
\tag{152.5}
\]

In particular

\[
\boxed{
\liminf {h\over D}
\ge1.816996852232013\ldots
}
\tag{152.6}
\]

for a Type-II countersequence whose selected wrapping carrier tends to the Section-118 frontier profile.

This is a structural improvement of nearly `0.096D` in the diameter-edge density, coming from planar internal-face geometry rather than carrier-decimal optimization.

---

## 152.1 Exact retained-remainder elimination

Section 150's finite identity is

\[
G_D
:=2+q+m-k-\sum_rd_r
=R_I+s_B+\sum_r\eta_r,
\qquad
\eta_r:=\delta_r+2-d_r.
\tag{152.7}
\]

Thus

\[
\boxed{
m
=G_D+\sum_rd_r-q+k-2.}
\tag{152.8}
\]

Hostile-audited Section 148 gives

\[
3q-2m-5k
\ge
\sum_rd_r+c_{det}D-o(D).
\tag{152.9}
\]

Insert (152.8):

\[
\begin{aligned}
3q
-2\left(G_D+\sum_rd_r-q+k-2\right)
-5k
&\ge\sum_rd_r+c_{det}D-o(D),
\end{aligned}
\]

so

\[
5q-7k-2G_D-3\sum_rd_r+4
\ge c_{det}D-o(D).
\]

Absorb the constant `4` into `o(D)` along an unbounded sequence to obtain (152.1).

Using

\[
q=h+d_H,
\qquad
k=d_H+s_Z
\]

gives (152.2).

---

## 152.2 Insert one carrier's internal-face slack

For every harmonic component,

\[
0\le r_r\le R_I,
\qquad
0\le\eta_r\le\sum_s\eta_s.
\]

Therefore

\[
G_D=R_I+s_B+\sum_s\eta_s
\ge r_r+\eta_r.
\tag{152.10}
\]

Section 151 gives

\[
r_r+\eta_r
\ge\sqrt{\pi A_{4,r}^{int}}+2-d_r.
\tag{152.11}
\]

Suppose

\[
A_{4,r}^{int}\ge(A-o(1))D^2,
\qquad
{d_r\over D}\to\lambda,
\qquad
{1\over D}\sum_sd_s\ge S-o(1).
\]

Divide (152.11) by `D` and retain only a positive lower bound:

\[
\liminf {G_D\over D}
\ge[\sqrt{\pi A}-\lambda]_+.
\tag{152.12}
\]

Insert this and the diameter moment in (152.2) to obtain the safe general tradeoff

\[
\boxed{
5h-2d_H-7s_Z
\ge
\left[
3S+2[\sqrt{\pi A}-\lambda]_++c_{det}
\right]D-o(D).
}
\tag{152.13}
\]

Equation (152.4) is the positive-slack specialization.

---

## 152.3 Section-118 frontier evaluation

For a countersequence whose selected wrapping carrier tends to the safe Section-118 frontier, the canonical/hostile-reviewed carrier data are

\[
\lambda=\lambda_*
=0.9762439137425688\ldots,
\]

\[
A_{4,*}^{int}/D^2
\ge A_*-o(1),
\qquad
A_*=0.4703752868004241\ldots,
\]

where the transfer from full carrier rhombus area to internal-only rhombus area is hostile-audited in Section 151.

Hostile-audited Section 148 gives

\[
S\ge S_*=2.798596312209462\ldots .
\]

The area slack is

\[
\sqrt{\pi A_*}-\lambda_*
=0.239374260456223\ldots .
\]

Thus the right side of (152.13) is at least

\[
3S_*+2(0.239374260456223\ldots)+c_{det}
=9.084984261160066\ldots,
\]

proving (152.5).

Since `d_H,s_Z>=0`, dropping their negative terms on the left gives (152.6).

---

## 152.4 Immediate branch split

The old Section-148 lower edge `h/D=1.721247...` is not merely unattainable. Any Type-II sequence retaining the Section-118 frontier wrapping profile satisfies the much stronger alternative

\[
\boxed{h/D\ge1.8169968522\ldots-o(1).}
\]

Thus the live full-core analysis splits naturally into:

1. **frontier wrapping geometry:** pay at least `1.81699D` diameter edges, with the corresponding cyclic/forest topology and loaded-boundary consequences; or
2. **wrapping parameter separated from the Section-118 frontier:** re-evaluate the complement-gap diameter moment and carrier area at the separated parameter.

This is the correct continuation. A tiny improvement of `lambda_*` is no longer the useful variable.

---

## 152.5 Scope

- The finite retained-remainder identity is exact.
- The only area input is Section 151's audited internal-face inequality.
- The numerical specialization is a **frontier-profile tradeoff**, not an all-Type-II theorem.
- No source point is removed and no contact isolate is placed in an unloaded positive-contact component.
- The theorem does not address the inactive-container branch.

**Theorem state:** unchanged; proof-only candidate pending hostile audit.
