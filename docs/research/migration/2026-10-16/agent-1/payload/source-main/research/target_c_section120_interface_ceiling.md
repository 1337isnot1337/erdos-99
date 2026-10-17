# Target C Section 120 companion — leading-order interface ceiling

**Date:** 2026-09-12  
**Status:** proof-only method-ceiling regression.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The anisotropic two-arc theorem is exact, but in the global Type-II near-disk core its leading-order forcing power has a sharp ceiling. This note compares that ceiling to the already-canonical Section-85 train-interface floor.

## 1. Maximum possible local anisotropic return

For one strict unit rhombus let `u,v` be the two projective train directions and let

\[
\phi\in(\pi/3,\pi/2]
\]

be their acute projective angle. For a unit chord direction `q`, Section 120 uses the local return

\[
C(q;u,v)=4-2\bigl(|q\cdot u|+|q\cdot v|\bigr).
\]

For fixed `u,v`, minimizing the absolute-cosine sum over `q` gives

\[
\min_q\bigl(|q\cdot u|+|q\cdot v|\bigr)=\sin\phi.
\]

One minimizing direction is perpendicular to one of the two train directions. Hence

\[
\max_q C(q;u,v)=4-2\sin\phi.
\]

Since `phi>pi/3`,

\[
\boxed{
C(q;u,v)<4-\sqrt3
=2.26794919243112\ldots
}
\]

for every strict rhombus and every `q`; equality is approached only as `phi downarrow pi/3`.

Thus no choice of a single two-arc chord direction can make the area-weighted Section-120 return exceed

\[
(4-\sqrt3)A_4.
\]

This is an **upper ceiling on what the Section-120 right-hand side can force**, not a new lower bound on the actual outer interface.

## 2. Consequence in the full Type-II near-disk limit

Apply Section 120 to the full positive-core rhombus complex. In Type II,

\[
d=D,
\qquad
{A_4\over D^2}\to{\pi\over4},
\qquad
{P_F\over D}\to\pi.
\]

Even granting the most favorable possible diameter chord `r=D` and the pointwise maximal local return on every rhombus simultaneously, Section 120 could force at most the first-order raw-interface lower coefficient

\[
\begin{aligned}
\kappa_{120}^{\max}
&:=2-\pi+(4-\sqrt3){\pi\over4}\\
&=0.639650476824337\ldots .
\end{aligned}
\]

Indeed the theorem has the form

\[
L+P_{exc}
\ge2D+{\text{return}\over D},
\]

and the raw interface relative to the convex force hull is

\[
J=(L+P_{exc})-P_F.
\]

The best leading coefficient obtainable from Section 120 alone is therefore at most `kappa_120^max`.

## 3. Canonical Section 85 already forces more

Canonical Section 85 proves

\[
B_4-P_F\ge(\kappa_{tr}-o(1))D,
\]

with

\[
\begin{aligned}
\kappa_{tr}
&=4\sqrt{{\pi\over2\sqrt3}}-\pi\\
&=0.667658573866036\ldots .
\end{aligned}
\]

Therefore

\[
\boxed{
\kappa_{tr}-\kappa_{120}^{\max}
=0.028008097041700\ldots>0.
}
\]

So even an unrealistically perfect use of the anisotropic two-arc return on the whole near-disk core cannot reprove, much less improve, the canonical Section-85 train-boundary excess at leading order.

## 4. Binding interpretation

This does **not** invalidate Section 120. It identifies its useful scope.

Do not use Section 120 as another first-order lower-bound machine for the global Type-II interface. Section 85 is already stronger there.

A productive Section-120 continuation must instead do at least one of the following:

1. work inside one harmonic carrier, where the global near-disk perimeter cancellation is absent;
2. retain second-order/boundary-order correlations discarded by the Type-II limits;
3. combine the anisotropic return with a genuine **upper** bound or a source-preserving deformation, rather than compare it to another lower bound;
4. use failure of favorable chord/train correlation to force a rigid coherent-grain configuration that another theorem can exclude.

This regression prevents the exact anisotropic theorem from being mistaken for a global first-order closure by itself.

**Theorem state:** unchanged.
