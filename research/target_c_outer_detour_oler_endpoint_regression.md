<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6a0a4bf3e71863d84ccd93a376799674aeea9f83", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_outer_detour_oler_endpoint_regression.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f7eb249019c8ea5b3787ed66161a6de2bb8436a668d9a8e04b04c4c088429e1d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — endpoint saturation of the local Oler detour currency

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only hostile audit of the local Oler/Section-116 route; theorem authority unchanged.

The finite Oler sandwich in `target_c_outer_detour_oler_sandwich.md` is valid. A
hostile check against the canonical Section-101/102 endpoint geometry reveals a sharper
fact than the first version of this note recorded:

> At the scalar endpoint, the local Oler inequality itself forces a **linear**
> non-rhombic/rhombus-excess currency. Its leading coefficient is exactly the area of
> the near-equilateral boundary teeth forced by Section 102.

Thus one may not test the endpoint by setting the local non-rhombic error to `o(D)`.
The correct endpoint model has a first-order boundary layer, and that boundary layer
asymptotically saturates the local Oler payment. This explains why a bare Oler upper
bound does not close Route A and identifies the currency that the later signed-return
proofs must control directionally.

---

## 1. Canonical endpoint scalars

Let `theta_8` be the Section-101 root

\[
\sin(\theta_8/2)+2\sin\theta_8=3\theta_8-2\pi,
\]

and put

\[
\lambda_8=\sin(\theta_8/2),
\qquad
\phi_8=2\pi-2\theta_8,
\qquad
U_8=3\theta_8-2\pi.
\]

Numerically,

\[
\theta_8=2.7029080296483676\ldots,
\qquad
\lambda_8=0.9760407652670520\ldots,
\]

\[
\boxed{U_8=1.8255387817655162\ldots .}
\tag{1.1}
\]

Canonical Section 102 shows that a hypothetical endpoint sequence has

\[
{a_D\over D}\to\alpha_8={U_8\over2},
\tag{1.2}
\]

and

\[
{Q_D\over D},{s_D\over D},{c_D\over D}\to0.
\tag{1.3}
\]

Its limiting support is, up to rotation,

\[
S_8=\{0\}\cup\{\theta_8\}
\cup[\theta_8+\phi_8,2\pi-\phi_8],
\]

with complement gaps `(theta_8,phi_8,phi_8)`.

---

## 2. Exact endpoint perimeter

For a compact subset of the radius-`1/2` circle, the boundary of its convex hull
follows the supported circular arcs and replaces each complementary gap `g` by its
chord of length `sin(g/2)`.

The supported arc of `S_8` has angular length `U_8`. Therefore

\[
\begin{aligned}
p_8
&:=\operatorname{per}(\operatorname{conv}S_8)\\
&={U_8\over2}
+\sin(\theta_8/2)+2\sin(\phi_8/2).
\end{aligned}
\]

Since `phi_8/2=pi-theta_8` and the endpoint equation gives

\[
\sin(\theta_8/2)+2\sin\theta_8=U_8,
\]

we obtain

\[
\boxed{p_8={3\over2}U_8}
=2.7383081726482743\ldots .
\tag{2.1}
\]

Hausdorff convergence of the normalized convex attachment polygons therefore gives

\[
{p_D\over D}\to p_8.
\tag{2.2}
\]

---

## 3. Local Oler forces a linear boundary-layer area

Use the notation of the companion Oler-sandwich note:

\[
a_0={\sqrt3\over2},
\qquad
c_0={\sqrt3\over4}={a_0\over2},
\]

\[
G_D=\operatorname{area}(P_D)-A_{4,D},
\qquad
E^{\rm loc}_{4,D}=A_{4,D}-a_0R_{4,D}.
\]

Equation (2.5) of that note is the exact finite consequence of Oler

\[
a_0(2a_D+f_D-s_D-c_D-3)
\le G_D+E^{\rm loc}_{4,D}+c_0p_D.
\tag{3.1}
\]

Since `f_D<=Q_D=o(D)`, divide by `D` and use (1.2), (1.3), and (2.2):

\[
\liminf_D{G_D+E^{\rm loc}_{4,D}\over D}
\ge a_0U_8-c_0p_8.
\tag{3.2}
\]

Substitute `p_8=3U_8/2` and `c_0=a_0/2`:

\[
\boxed{
\liminf_D{G_D+E^{\rm loc}_{4,D}\over D}
\ge {a_0U_8\over4}
={\sqrt3\,U_8\over8}.
}
\tag{3.3}
\]

Numerically,

\[
\boxed{
{\sqrt3\,U_8\over8}
=0.3952407401506583\ldots .
}
\tag{3.4}
\]

So the endpoint cannot have `G_D+E^{loc}_{4,D}=o(D)`. The first version of this
hostile check incorrectly used that impossible stronger model as a regression. The
correct conclusion is (3.3).

---

## 4. The coefficient is exactly the tooth-area coefficient

Canonical Section 102 proves that, after discarding only `o(D)` exceptional intervals,
there are

\[
(\alpha_8-o(1))D={U_8\over2}D-o(D)
\tag{4.1}
\]

near-equilateral boundary teeth

\[
p_k-x_k-p_{k+1},
\qquad
|p_k-x_k|=|x_k-p_{k+1}|=1,
\qquad
|p_k-p_{k+1}|=1+o(1).
\]

The apex lies on the interior side of the attachment-polygon base. The area of each
such tooth triangle tends to

\[
c_0={\sqrt3\over4}.
\]

Their interiors are disjoint boundary pieces between consecutive attachment bases and
the corresponding two-edge outer routes. Therefore their total area is

\[
\left(c_0\alpha_8-o(1)\right)D
=\left({\sqrt3\,U_8\over8}-o(1)\right)D.
\tag{4.2}
\]

But this is exactly the lower coefficient in (3.3):

\[
\boxed{c_0\alpha_8={\sqrt3\,U_8\over8}.}
\tag{4.3}
\]

Thus the first-order local Oler deficit at the scalar endpoint is not a mysterious
bulk error. It is precisely the boundary-tooth area already forced by the endpoint
outer-walk geometry.

This equality is structurally useful: any attempted Route-A upper bound that treats
`G_D` as a disposable `o(D)` error is incompatible with the actual endpoint geometry.
The tooth boundary layer is a leading-order linear term and must be charged by
orientation/order, not discarded.

---

## 5. Interaction with the Section-116 detour theorem

At the endpoint, canonical Section 102 also gives

\[
L_D=2U_8D+o(D),
\]

while `d_D/D->lambda_8` and `P_{exc,D}=o(D)`. Hence the actual normalized Section-116
detour is

\[
\boxed{
{E_{out,D}\over D}
={L_D+P_{exc,D}-2d_D\over D}
\to2U_8-2\lambda_8
=1.6990000329969284\ldots .
}
\tag{5.1}
\]

The Oler upper formula from the companion note is asymptotically consistent with this
large detour precisely because the tooth currency in (3.3)--(4.3) contributes at
linear order. Dropping it would violate the finite Oler inequality before any
Section-116 comparison was made.

The Section-116 lower bound itself is much weaker at the scalar endpoint; that is not
a contradiction, because it was designed as an all-regime universal return estimate,
not an endpoint-sharp identity.

---

## 6. Consequence for the live closure route

The local Oler sandwich has now isolated the correct first-order obstruction:

```text
endpoint outer-walk detour
    = convex-hull perimeter/diameter term
      + a linear boundary-tooth area payment
      + lower-order face/rhombus errors.
```

The boundary-tooth payment is unavoidable and has exactly the Oler-saturation
coefficient. Therefore an all-regime closure must do something that scalar Oler does
not do:

1. exploit the **directional dispersion** of the near-equilateral teeth, as the
   signed-return route begins to do;
2. show that a comparable tooth/detour boundary layer admits a source-preserving
   diameter-decreasing deformation; or
3. derive a global-minimality constraint on the actual outer walk that is stricter
   than the generic convex Oler allowance.

This is a proof-method obstruction, not a counterexample to C-II. No theorem authority
is changed and no closure is claimed.

