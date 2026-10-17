> Generated reading edition · [exact source](../../../docs/audits/target_c_mu4_train_pairing_endpoint_audit_2026-09-12.md) · source SHA-256 `cf01a064fd62642518955ae31aef24d716caee5f291adcfab15c5d2679f4ebeb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C17DF7BB083A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit — Target C `mu_4` train-pairing endpoint exclusion

**Date:** 2026-09-12  
**Audited artifact:** `docs/reports/target_c_mu4_train_pairing_endpoint_exclusion_2026-09-12.md`  
**Classification:** proved candidate pending promotion  
**C-II status:** open

## Audit conclusion

The endpoint argument is valid under the promoted Sections 80, 82, 83, 89, and 96
scopes. It excludes a wrapping harmonic-cell sequence with normalized diameter
converging to

$$
\mu_4=0.936215741409583\ldots .
$$

The proof uses the endpoint support saturation handoff only for its area conclusion;
it does **not** use the corrected and rejected rhombus-count assertion in the older
support note. It therefore survives the correction made in `8bd0f2d`.

**Bridge correction.** Section 82/89 does not need to control outer-face bridge
occurrences. A bridge has the outer face on both sides and is incident to no bounded
rhombus, so it is not a train endpoint. Every actual train endpoint is either on the
outer attachment walk or faces a bounded nonquadrilateral face; the latter contribute
`O(Q_D)=o(D)`. Thus a linear bridge corridor can only remove possible train endpoints
and cannot create an additional area-carrying case.

## 1. Endpoint ledger

Section 96 and the endpoint geodesic-collapse handoff give, along an endpoint
sequence,

$$
 a_D/D\to\alpha_4,
 \quad
 Q_D+s_D+c_D=o(D),
 \quad
 L_D/D\to4\alpha_4,
$$

where

$$
\alpha_4=3\theta_4-2\pi={3\over2}\sin\theta_4,
\qquad
\theta_4=2\arcsin\mu_4.
$$

The three distinguished outer routes have total length

$$
3\sin\theta_4D+o(D)=2\alpha_4D+o(D),
$$

and each has `o(D)` excess over its endpoint chord. Every other attachment route is
two edges except for `o(D)` total exceptional edge occurrences.

## 2. Support and area audit

The annular unit-separation estimate gives an upper angular counting density
`D/2+o(D)` on every fixed angular interval. The Section-96 endpoint equality gives
`a_D/D -> alpha_4`, exactly the total density ceiling on the six allowed arcs. If a
fixed open subarc of an allowed arc were missing from the limiting attachment
support, the density ceiling would lose a positive multiple of `D`, contradicting
the endpoint count. The same upper-density argument gives weak convergence to
one-half Lebesgue measure on the allowed arcs.

The convex hulls therefore converge to the circle support with the three forbidden
caps removed. Since `phi_4=2*pi-2*theta_4<pi/2`, the caps are disjoint and

$$
 {\operatorname{area}(P_D)\over D^2}
 \to
 A_4={\pi\over4}-{3\over8}(\phi_4-\sin\phi_4)
 =0.618374879828757\ldots .
$$

Canonical cell saturation supplies strict-rhombus area
`A_{4,D}=area(P_D)-o(D^2)`. No conversion from area to a rhombus count is made.

## 3. Train-end pairing audit

The Section-89 train decomposition has two terminal boundary edges per train. The
nonquadrilateral-face boundary contributes `O(Q_D)=o(D)` edge occurrences. Every
remaining train endpoint lies on an outer attachment subwalk; bridge occurrences are
not train endpoints. Hence all but `o(D)` train ends lie on the outer attachment
routes without assuming `b_D=o(D)`.

The three long-route chord directions are pairwise distinct modulo `pi`. If two were
parallel, their equal-length forbidden arcs would have antipodal midpoints. Let `F`
be the union of the three forbidden arcs. Since `phi_4<pi/2`,

$$
 |F\cup(F+\pi)|\le4\phi_4<2\pi.
$$

Thus some `x` lies in neither `F` nor `F+pi`; both `x` and `x+pi` belong to the
allowed support, contradicting its limiting diameter `mu_4<1`.

The geodesic-excess identity

$$
 \sum_k(1-q\cdot z_k)=\ell-|u-v|
$$

shows that all but `o(D)` edges on each long route have direction arbitrarily close
to its chord direction. On the ordinary two-edge routes, all but `o(D)` routes have
vanishing angular endpoint gap. The local equilateral conclusion requires one detail
beyond annular convergence. Since the saturated attachment support is all of the
allowed circle arcs, the normalized attachment polygons converge in Hausdorff
distance to the convex hull of those arcs. Away from the finitely many arc
endpoints, a short side therefore has a supporting line converging to the
corresponding circle tangent. For a two-edge route `p-x-q`, that side has
`|p-q|<=2`; in tangent/normal coordinates its endpoint tangential coordinates are
`o(D)` from the tangent point and differ by at most `2`, while its normal coordinate
is `(1/2+o(1))D`. Hence `||p|-|q||=o(1)`. Combined with the angular gap
`(2+o(1))/D`, this gives `|p-q|=1+o(1)`, and the two contact directions are the
local tangent directions offset by `+/- pi/3+o(1)`. A fixed neighborhood of the
finitely many arc endpoints contains `O(eta D)+o(D)` ordinary intervals; letting
`eta` tend to zero after the normalized limit gives the required `o(D)` exceptional
family. The annular density ceiling then implies
that only `o(D)` ordinary edges can be parallel to any fixed long-route direction.

Thus, after discarding `o(D)` exceptional ends:

* a long-route end cannot pair with an ordinary-route end;
* a long-route end cannot pair with another long route;
* long-route ends pair only within their own route.

Two ends on one long route have transverse separation `o(D)`, because the whole route
has `o(D)` Hausdorff distance from its chord. Hence all same-route long-route trains
contribute `o(D^2)` total transverse span.

The ordinary routes contain `2a_D+o(D)` edge occurrences, so at most
`a_D+o(D)=alpha_4D+o(D)` trains remain with potentially macroscopic span.

## 4. Area contradiction audit

For each train, the sum of its rhombus transverse advances is its exact transverse
span. Both terminal edge midpoints lie in `P_D`, so every span is at most `d_D`. Each
strict rhombus is counted by exactly two trains. Therefore

$$
 2A_{4,D}
 \le (\alpha_4D+o(D))d_D+o(D^2).
$$

After division by `D^2`, the endpoint would require

$$
 2A_4\le\alpha_4\mu_4.
$$

The scalar sides are

$$
2A_4=1.236749759657516\ldots,
\qquad
\alpha_4\mu_4=0.924074023352554\ldots,
$$

so the inequality fails by `0.3126757363...`. This is a fixed margin; no numerical
near-equality ambiguity remains.

## 5. Scope check and promotion recommendation

The audit does not use contact-isolated points, KKT multiplier floors, or a global
triangle-free density assertion. It is local to a wrapping carrier in the full-core
near-disk branch and does not require `b_D=o(D)`. It does not exclude wrapping limits
strictly larger than `mu_4` and does not address the macroscopic inactive-container
branch.

**Recommendation:** retain this as a proved candidate pending an independent audit of
the support-saturation and distinct-direction lemmas. The endpoint exclusion does not
close C-II; quantitative stability above `mu_4`, larger wrapping cells, and the
macroscopic inactive-container branch remain open.

