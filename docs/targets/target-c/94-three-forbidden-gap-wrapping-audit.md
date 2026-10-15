# Target C — three forbidden wrapping gaps raise the carrier threshold to 0.919779 D

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical Section 88 does more than bound the total angular measure occupied by a wrapping attachment set. Once three wrapping anchors are fixed, each of the three anchor gaps contains a central forbidden arc of the same length. Those three empty arcs force three macroscopic sides in the attachment polygon.

Combining that fact with

- the Type-II near-circle lower spacing between all other consecutive attachments;
- canonical Section 82's finite attachment-perimeter capacity `per(P)<=4|A|-6`; and
- Section 88's six-cluster attachment-count ceiling

raises the wrapping threshold again to

\[
\boxed{
\mu_3=0.919778662688621\ldots
}
\]

where, writing `theta_3=2 asin(mu_3)`,

\[
\boxed{
\sin\theta_3=3\theta_3-2\pi.
}
\]

The same Section-88 cap-capacity argument then forces an actual locally rhombus-saturated macroscopic Type-II harmonic carrier of diameter at least `(mu_3-o(1))D`.

This proof uses only canonical Sections 80, 82, 83, and 88. It does not depend on Sections 90--93.

---

# 94. Three forbidden wrapping gaps force diameter at least 0.919778 D

## 94.1 The Section-88 six-cluster proof has a three-gap complement

Let `S` be a wrapping compact subset of the radius-`1/2` circle with

\[
\operatorname{diam}(S)=\lambda<1,
\qquad
\theta:=2\arcsin\lambda\in[2\pi/3,\pi).
\tag{94.1}
\]

Canonical Section 88 chooses three anchors `y_1,y_2,y_3 in S` whose triangle contains the origin. Let their cyclic circle gaps be

\[
g_1,g_2,g_3\in(0,\pi),
\qquad
g_1+g_2+g_3=2\pi,
\qquad g_i\le\theta.
\tag{94.2}
\]

Consider the gap `g_1` from `y_1` to `y_2`. A support point in that gap must remain within angular distance `theta` of the third anchor `y_3`. Section 88 therefore confines it to the two endpoint intervals of lengths

\[
\theta-g_3,
\qquad
\theta-g_2.
\tag{94.3}
\]

Their total length is

\[
2\theta-g_2-g_3
=g_1-(2\pi-2\theta).
\tag{94.4}
\]

Since `theta<pi`, the endpoint intervals are disjoint. Thus the middle of the `g_1` anchor gap contains a support-free open arc of exact length

\[
\boxed{
\phi:=2\pi-2\theta.
}
\tag{94.5}
\]

The same holds in each of the other two anchor gaps. The three forbidden arcs are pairwise disjoint because they lie in three different anchor gaps.

Equivalently:

> Every wrapping support set of diameter `lambda` on the radius-`1/2` circle has three pairwise disjoint support-free circular arcs, each of angular length `phi=2pi-2theta`.

This is the complement form of the Section-88 six-cluster lemma. Its total forbidden measure is

\[
3\phi=6\pi-6\theta,
\]

so the allowed measure is

\[
2\pi-3\phi=6\theta-4\pi,
\]

exactly the canonical six-cluster measure.

## 94.2 Finite Type-II attachment sets inherit three macroscopic empty arcs

Let `P_j=conv(A_j)` be Type-II harmonic cells with source diameters `D_j -> infinity` such that

\[
{\operatorname{diam}(P_j)\over D_j}\to\lambda<1
\tag{94.6}
\]

and, after passing to a subsequence, the normalized attachment sets converge to a wrapping support `S` as above.

Use the actual attachment vertices converging to the three Section-88 anchors. The compactness step in canonical Section 88 says that every attachment of `A_j` lies in an `o(1)` angular enlargement of the six allowed intervals from (94.3). Hence each of the three central forbidden arcs contains no attachment after shrinking its endpoints by `o(1)`.

Because an actual anchor attachment lies between consecutive anchor gaps in cyclic order, the three forbidden arcs belong to three distinct cyclic gaps of the finite attachment set. Therefore, if

\[
h_{1,j},\ldots,h_{a_j,j}
\qquad(a_j:=|A_j|)
\]

are the cyclic polar gaps between consecutive attachments, then for three distinct indices

\[
\boxed{
h_{i,j}\ge\phi-o(1).}
\tag{94.7}

All other cyclic gaps still obey the Type-II unit-separation lower bound from Section 93's direct annular argument. For completeness, if

\[
r_j=\left({1\over2}-\epsilon_j\right)D_j,
\qquad
R_j=\left({1\over2}+\epsilon_j\right)D_j,
\qquad
\epsilon_j\to0,
\]

then the Section-88 radial arclength estimate gives

\[
\boxed{
h_{i,j}\ge\ell_j:={r_j\over R_j^2},
\qquad D_j\ell_j\to2.}
\tag{94.8}

No fixed-number-of-intervals approximation is used in (94.8).

## 94.3 Three forbidden gaps give a strong perimeter floor

Pass to a subsequence on which

\[
{a_j\over D_j}\to\alpha.
\tag{94.9}

Canonical harmonic attachment multiplicity makes `alpha>0` in a macroscopic wrapping cell.

Every attachment vertex lies on the force-hull boundary and is extreme in the attachment polygon, so its polygon sides join consecutive attachment vertices in the same cyclic order. Both endpoints have radius at least `r_j`. Therefore a side spanning angular gap `h<=pi` has length at least

\[
2r_j\sin(h/2).
\tag{94.10}

The wrapping diameter `lambda<1` implies that all cyclic attachment gaps are eventually below `pi`; alternatively only the three lower bounds below and the small-gap estimate are needed.

Choose the three distinct gaps from (94.7). Since `phi<pi` and `sin` is increasing on `[0,pi/2]`, their normalized side-length contribution is at least

\[
3\sin(\phi/2)-o(1).
\tag{94.11}

Every other one of the `a_j-3` gaps is at least `ell_j`, so its contribution is at least `sin(ell_j/2)`. Using (94.8)--(94.9),

\[
(a_j-3)\sin(\ell_j/2)
\to\alpha.
\tag{94.12}

Since `2r_j/D_j ->1`, equations (94.10)--(94.12) yield

\[
\boxed{
\liminf {\operatorname{per}(P_j)\over D_j}
\ge
\alpha+3\sin(\phi/2).
}
\tag{94.13}

But

\[
\phi/2=\pi-\theta,
\]

so

\[
\sin(\phi/2)=\sin\theta.
\]

Hence the perimeter floor is

\[
\boxed{
\liminf {\operatorname{per}(P_j)\over D_j}
\ge
\alpha+3\sin\theta.
}
\tag{94.14}

This is stronger than the three-anchor floor from Section 92 and the unconstrained full-gap floor from Section 93 because it uses the exact location of the three forbidden regions in the six-cluster geometry.

## 94.4 Attachment-perimeter capacity forces alpha >= sin(theta)

Canonical Section 82 gives the finite local capacity

\[
\operatorname{per}(P_j)\le4a_j-6.
\tag{94.15}

Divide by `D_j` and combine with (94.9), (94.14):

\[
\alpha+3\sin\theta\le4\alpha.
\]

Therefore every wrapping harmonic-cell limit satisfies

\[
\boxed{
\alpha\ge\sin\theta.
}
\tag{94.16}

Canonical Section 88's unit-separated six-cluster boundary packing gives the opposite bound

\[
\boxed{
\alpha\le {6\theta-4\pi\over2}
=3\theta-2\pi.
}
\tag{94.17}

Combining (94.16)--(94.17) gives the new scalar necessity

\[
\boxed{
\sin\theta\le3\theta-2\pi,
\qquad
\theta=2\arcsin\lambda.
}
\tag{94.18}

## 94.5 Solve the scalar threshold

Define

\[
H(\theta):=3\theta-2\pi-\sin\theta
\qquad(2\pi/3\le\theta<\pi).
\tag{94.19}

Then

\[
H'(\theta)=3-\cos\theta>0.
\tag{94.20}

At the equilateral wrapping threshold,

\[
H(2\pi/3)=-{\sqrt3\over2}<0,
\tag{94.21}

while

\[
H(\pi)=\pi>0.
\tag{94.22}

Hence there is a unique root `theta_3 in (2pi/3,pi)`. Numerically,

\[
\boxed{
\theta_3=2.335032210844538\ldots
}
\tag{94.23}

and therefore

\[
\boxed{
\mu_3:=\sin(\theta_3/2)
=0.919778662688621\ldots
}
\tag{94.24}

Every wrapping Type-II harmonic-cell limit must satisfy

\[
\boxed{
\lambda\ge\mu_3.
}
\tag{94.25}

This independently subsumes the scalar wrapping thresholds of Sections 88, 92, and 93.

## 94.6 Propagate the improved threshold to an actual macroscopic carrier

Fix any `mu<mu_3`. By (94.25), every macroscopic harmonic-cell limit of normalized diameter at most `mu` is cap type. Canonical Section 88's cap-family theorem therefore applies unchanged:

\[
\limsup {1\over D^2}
\sum_{\operatorname{diam}(P_r)\le\mu D}
\operatorname{area}(P_r)
\le\mathcal C(\mu)<{\pi\over4}.
\tag{94.26}

Thus long cells carry a positive area fraction

\[
\Gamma(\mu)D^2-o(D^2),
\qquad
\Gamma(\mu):={\pi\over4}-\mathcal C(\mu)>0.
\tag{94.27}

The canonical total harmonic-cell perimeter bound makes the number of such long cells uniformly bounded for fixed `mu`. Canonical Section 83 gives summed local rhombic deficit `o(D^2)`. Hence one long cell is macroscopic and locally rhombus-saturated.

At the new endpoint,

\[
\mathcal C(\mu_3)=0.4800322759\ldots,
\qquad
\Gamma(\mu_3)=0.3053658875\ldots>0.
\tag{94.28}

The endpoint area fraction is still uniformly positive. Taking `mu` to `mu_3` slowly gives actual cells `P_*` with

\[
\boxed{
{\operatorname{diam}(P_*)\over D}\ge\mu_3-o(1),
\qquad
\operatorname{area}(P_*)\ge c_3D^2,
\qquad
{A_{4,*}\over\operatorname{area}(P_*)}\to1
}
\tag{94.29}

for one absolute `c_3>0`.

Thus the rigorous Type-II carrier threshold becomes

\[
\boxed{0.9197786627\ldots D-o(D).}
\tag{94.30}

## 94.7 Endpoint structure and next obstruction

A sequence approaching `mu_3` must asymptotically saturate both sides of (94.16)--(94.17). In particular:

1. the attachment density satisfies
   \[
   {a\over D}\to\sin\theta_3=3\theta_3-2\pi;
   \]
2. the six allowed Section-88 boundary clusters are saturated at unit-separation density;
3. the three forbidden middle arcs have asymptotic angular length `phi_3=2pi-2theta_3`;
4. all remaining `Theta(D)` cyclic attachment gaps are asymptotically at the minimum `2/D` angular scale in aggregate; and
5. the canonical local capacity `per(P)<=4a-6` is asymptotically tight, forcing `Q+2s+2c=o(D)` through the exact Section-82 identity.

The scalar perimeter/circle-packing route has therefore reached a sharply constrained endpoint rather than a generic wrapping cell. A further improvement must use stability of one of these equality conditions, or couple them to the near-rhombic train structure inside the same cell.

The independent Sections 90--91 ordered-grid route is especially relevant here: endpoint saturation places almost all attachment boundary mass at near-minimal spacing while the interior carries a quadratic inverse-phase train core.

## 94.8 Dependency and regression audit

- **Canonical `C-FULLCORE-NEAR-DISK` / Section 80:** force-hull annular convergence to the radius-`1/2` disk.
- **Canonical `C-HARMONIC-CARRIER-QUAD` / Section 82:** finite attachment-perimeter capacity and its exact defect form.
- **Canonical `C-HARMONIC-CELL-TILING` / Section 83:** cell disjointness and local-rhombic-deficit summability used only in the propagated carrier conclusion.
- **Canonical `C-HARMONIC-WRAPPING` / Section 88:** three-anchor wrapping construction, six-cluster localization, attachment-count ceiling, cap-family capacity, and long-cell selection framework.
- **No Section 92/93 dependency:** the three-forbidden-gap argument is independent and stronger.
- **Finite-to-limit forbidden gaps:** actual anchor vertices are retained, so the three forbidden arcs lie in three distinct finite cyclic attachment gaps after an `o(1)` shrink.
- **Many small gaps:** the exact Section-88 radial arclength inequality gives the uniform `(2-o(1))/D` lower angular spacing; summing `Theta(D)` such gaps is therefore legitimate.
- **Contact-isolated source points:** untouched.
- **No KKT coefficient floor and no rejected cap theorem.**

**Status:** canonical; promoted by the independent Sections-90–94 audit.
**Theorem state:** `2026-09-11.audit.36`.
