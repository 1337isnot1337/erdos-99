# Target C — unique wrapping carrier absorbs the cap deficit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** canonical after independent hostile audit and theorem-state audit.43 promotion.

Canonical Sections 83 and 88 already imply more area concentration than the current
carrier handoff records.  A wrapping circle-supported harmonic-cell limit contains the
center of the limiting diameter-one disk in its **interior**.  Distinct harmonic cells
have disjoint interiors.  Therefore a finite macroscopic limit family contains at most
one wrapping cell.

This removes the old loss from pigeonholing the cap-capacity deficit over `O(1)` long
cells.  If every macroscopic cell has normalized diameter at most `mu<1`, then all
cells except the unique wrapping one are cap type and together occupy at most the
canonical Section-88 cap capacity `C(mu)`.  The wrapping cell itself must therefore
carry the full complementary area

\[
\boxed{
\Gamma(\mu):={\pi\over4}-\mathcal C(\mu)>0.
}
\]

At the Section-101 value

\[
\mu_8=0.9760407652670519821\ldots,
\]

this gives

\[
\boxed{
\operatorname{area}(P_{\rm wrap})
\ge(0.2023197554\ldots-o(1))D^2.
}
\]

The theorem is independent of the Section-102 phase/corridor endpoint exclusion.  It
is useful for that route because it gives an explicit quadratic population constant
for the unique near-endpoint wrapping carrier before any phase-core extraction.

---

# 103. There is at most one macroscopic wrapping cell

## 103.1 Macroscopic limit family

Work in the canonical full-core near-disk Type-II branch.  Let

\[
P_{r,D}=\operatorname{conv}(A_{r,D})\subset F_D
\]

be the harmonic attachment cells.  Canonical Section 83 gives

\[
\sum_r\operatorname{area}(P_{r,D})
={\pi\over4}D^2-o(D^2),
\tag{103.1}
\]

pairwise interior disjointness, and

\[
\sum_r\sqrt{\operatorname{area}(P_{r,D})}=O(D).
\tag{103.2}
\]

Fix `eta>0` and retain the cells with

\[
\operatorname{area}(P_{r,D})\ge\eta D^2.
\tag{103.3}
\]

There are uniformly finitely many.  After passing to a subsequence, translate by the
near-disk center and scale by `D`; every retained cell and its attachment set converge
in Hausdorff distance:

\[
D^{-1}P_{r,D}\to K_r,
\qquad
D^{-1}A_{r,D}\to S_r\subset\partial B_{1/2}.
\tag{103.4}
\]

Convex-hull continuity gives

\[
K_r=\operatorname{conv}(S_r).
\tag{103.5}
\]

The positive area floor preserves nonempty interior.  Pairwise interior disjointness
also passes to the limit, exactly as in canonical Section 88:

\[
\operatorname{int}K_r\cap\operatorname{int}K_s=\varnothing
\qquad(r\ne s).
\tag{103.6}
\]

## 103.2 A wrapping support contains the disk center in the cell interior

Recall the canonical Section-88 dichotomy.  A compact circle support `S` is **cap
type** if it is contained in an open semicircle and **wrapping** otherwise.

Let `S` be wrapping and suppose

\[
\operatorname{diam}(\operatorname{conv}S)<1.
\tag{103.7}
\]

Then `S` contains no antipodal pair.  Since `S` is not contained in an open
semicircle, the origin belongs to `conv(S)`.  In fact it belongs to the interior.

Indeed, if

\[
0\in\partial\operatorname{conv}(S),
\]

there is a support line through the origin with `S` in one closed half-plane.  Any
convex combination of points of `S` equal to zero must then use only points on that
support line.  The radius-`1/2` circle meets a line through the origin in an antipodal
pair.  Hence `S` would contain both antipodes, contradicting (103.7).

Thus

\[
\boxed{
S\text{ wrapping and }\operatorname{diam}K<1
\Longrightarrow
0\in\operatorname{int}K.
}
\tag{103.8}

This is also the strict form of the three-anchor Caratheodory step used in Section 88.

## 103.3 Uniqueness of a wrapping macroscopic limit

Suppose two distinct positive-area macroscopic limits `K_r,K_s` were wrapping.  Their
diameters are at most one because both lie in the radius-`1/2` disk; in every
application below they are bounded by a fixed `mu<1`, so (103.8) applies.  Then

\[
0\in\operatorname{int}K_r
\cap\operatorname{int}K_s,
\]

contradicting (103.6).

Therefore:

\[
\boxed{
\text{among any finite positive-area macroscopic limit family of diameter }<1,
\text{ at most one cell is wrapping.}
}
\tag{103.9}

No contact-graph argument is involved; this is a direct consequence of the common
near-circle attachment geometry and cell interior disjointness.

## 103.4 The cap-family deficit belongs to that one cell

Fix

\[
0<\mu<1
\tag{103.10}
\]

and consider a subsequence for which every positive-area macroscopic cell limit
satisfies

\[
\operatorname{diam}(K_r)\le\mu.
\tag{103.11}
\]

Every nonwrapping limit is cap type.  Apply canonical Section 88, Lemmas 88.2 and 88.5,
to the finite subfamily of cap-type limits.  Their minimal support arcs have lengths at
most

\[
\theta_\mu:=2\arcsin\mu<\pi,
\]

are laminar, and their pairwise interior-disjoint convex hulls have total area at most

\[
\boxed{
\sum_{r\,\mathrm{cap}}\operatorname{area}(K_r)
\le\mathcal C(\mu),
}
\tag{103.12}

where

\[
\mathcal C(\mu)
={1\over8}
\left[2\pi-k_\mu\sin\theta_\mu-\sin r_\mu\right],
\tag{103.13}
\]

\[
k_\mu=\left\lfloor{2\pi\over\theta_\mu}\right\rfloor,
\qquad
r_\mu=2\pi-k_\mu\theta_\mu.
\]

Section 88 proves `C(mu)<pi/4` for every fixed `mu<1`.  Put

\[
\Gamma(\mu):={\pi\over4}-\mathcal C(\mu)>0.
\tag{103.14}
\]

We now let the macroscopic cutoff `eta` tend to zero. From (103.2), cells of area
below `eta D^2` carry only `O(sqrt(eta)D^2)` total area. Hence their normalized total
area can be made arbitrarily small before taking the large-`D` limit.

The cell label must be selected diagonally rather than assumed to persist as `eta`
changes. Choose `eta_j downarrow0`. For each fixed `j`, after passing to the large-`D`
limit, the preceding finite-family argument gives one unique wrapping retained cell;
otherwise all retained limits are cap type and (103.12), together with the small-cell
tail, contradicts (103.1). Choose a diagonal sequence `D_j->infinity` and the
corresponding wrapping cells. Blaschke compactness for convex subsets of the limiting
disk yields a further Hausdorff limit `K_w`. The support remains wrapping, and (103.9)
makes the wrapping limit unique on that diagonal subsequence.

For every `j`, the cap-type macroscopic cells occupy at most `C(mu)` normalized area,
while the omitted small-cell tail is `O(sqrt(eta_j))`. Therefore

\\[
\\boxed{
\\operatorname{area}(K_w)
\\ge {\\pi\\over4}-\\mathcal C(\\mu)
=\\Gamma(\\mu).
}
\\tag{103.15}
\\]

Equivalently, along the diagonal finite cell sequence,

\\[
\\boxed{
\\operatorname{area}(P_{w,D})
\\ge(\\Gamma(\\mu)-o(1))D^2.
}
\\tag{103.16}
\\]

This is the promised concentration theorem. It does not assert that one original
finite cell label is independent of the macroscopic cutoff.

## 103.5 Near the current endpoint the wrapping carrier has area at least 0.2023 D^2

At the Section-101 threshold

\[
\mu_8=0.9760407652670519821\ldots,
\qquad
\theta_8=2.7029080296483676832\ldots,
\]

we have

\[
k_{\mu_8}=2,
\qquad
r_{\mu_8}=2\pi-2\theta_8=\phi_8.
\]

Canonical Section 101 records

\[
\mathcal C(\mu_8)=0.5830784079\ldots,
\]

so

\[
\boxed{
\Gamma_8
:={\pi\over4}-\mathcal C(\mu_8)
=0.2023197554\ldots .
}
\tag{103.17}

Consequently, in any subsequential regime in which every positive-area macroscopic
cell limit has diameter at most `mu_8`, the unique wrapping cell would satisfy

\[
\boxed{
\operatorname{area}(P_{w,D})
\ge(0.2023197554\ldots-o(1))D^2.
}
\tag{103.18}

Section 102 proves that the wrapping equality regime at `mu_8` is itself impossible.
The utility of (103.18) is therefore as a **stability constant**: in a hypothetical
near-endpoint countersequence with all macroscopic cell diameters bounded by a fixed
`mu>mu_8` close to `mu_8`, continuity of `C(mu)` gives a unique wrapping carrier with
area

\[
(\Gamma(\mu)-o(1))D^2,
\]

where `Gamma(mu)` remains close to `0.20232`.

## 103.6 Stronger local train constants on the unique wrapping carrier

The concentration theorem improves the constants available to the Section-90 phase
core.  Suppose `mu>mu_8` is fixed and close enough that

\[
\Gamma(\mu)>0.19.
\tag{103.19}
\]

Then the unique wrapping carrier has area at least `(0.19-o(1))D^2`.  Canonical
Section 83's nonnegative summed local rhombic deficit implies that, along a finite
macroscopic family, this cell is locally rhombus-saturated.  Hence for all sufficiently
large members of the subsequence its strict-rhombus population obeys, for example,

\[
R_D\ge0.18D^2.
\tag{103.20}
\]

Canonical Section 89 gives

\[
T_D\le6a_D+O(1).
\tag{103.21}
\]

For a wrapping limit with `theta` close to `theta_8`, canonical Section 100 gives

\[
{a_D\over D}\le{3\theta-2\pi\over2}+o(1)<1
\]

throughout some fixed neighborhood of `theta_8`.  Thus one may take the explicit
coarse local train constant

\[
\boxed{T_D\le6D}
\tag{103.22}
\]

there.

Canonical Section 68 also gives an explicit phase-defect constant.  From

\[
{3\Delta_{train}\over\pi}
\le(2+\sqrt3)E_4
<(2+\sqrt3){\sqrt3\over4}\,\pi D,
\]

we obtain

\[
\boxed{
\Delta_{train}
< C_{phase}D,
\qquad
C_{phase}:={\pi^2\sqrt3(2+\sqrt3)\over12}
=5.3165104791\ldots .
}
\tag{103.23}

Thus the three constants needed by the cell-local Section-90 binning argument can be
taken, in a sufficiently small fixed neighborhood of the current endpoint, as

\[
\boxed{
r=0.18,
\qquad
C_T=6,
\qquad
C_{phase}=5.317.
}
\tag{103.24}

No numerical strict diameter improvement is claimed here, but these constants remove
the largest quantitative loss in such a stability calculation.

## 103.7 Scope and next use

Section 103 does not improve the scalar diameter threshold by itself.  It proves a
structural concentration fact:

```text
all macroscopic cell diameters <= mu < 1
+ Type-II near-disk area tiling
+ pairwise interior-disjoint harmonic cells
-> exactly one wrapping macroscopic cell
-> wrapping cell area >= Gamma(mu) D^2
-> all remaining macroscopic cells are a laminar cap family.
```

Near `mu_8`, `Gamma(mu)` is about `0.2023`, so the unique wrapping carrier supports a
much stronger explicit Section-90 phase core than the earlier `O(1)`-cell
pigeonholing argument.

The natural next step is to make Section 102 quantitative: transport the scalar slack

\[
\sigma(\theta)
:=3\theta-2\pi-\sin(\theta/2)-2\sin\theta
\]

into explicit bounds for

- complement-gap deviation from `(theta,phi,phi)`;
- nonquadrilateral/contact/pinning currency;
- total nonprincipal corridor length; and
- phase-family endpoint leakage away from the three principal corridors.

The fixed phase/corridor angular mismatch in Section 102 then converts a sufficiently
small positive `sigma(theta)` into a contradiction, yielding a numerical
`mu>mu_8`.

**Theorem state:** canonical from `2026-09-12.audit.43`. C-II remains open.
