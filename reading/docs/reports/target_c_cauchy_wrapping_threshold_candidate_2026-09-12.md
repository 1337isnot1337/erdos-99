> Generated reading edition · [exact source](../../../docs/reports/target_c_cauchy_wrapping_threshold_candidate_2026-09-12.md) · source SHA-256 `1bf5b754c307748e0aa2d833b3de5abe49ac7c369d8d293d7a5c13a43fbbd0bc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D3AF1166D13A","canonical":true,"claim_ids":["C-WRAP-CAUCHY"],"claim_statuses":{"C-WRAP-CAUCHY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — Cauchy perimeter wrapping threshold

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**
**Status:** canonical; promoted by the independent hostile audit recorded alongside this report.

Canonical Section 94 gives a perimeter floor for every wrapping Type-II harmonic
cell. Canonical Section 96 gives a stronger attachment-density floor. Combining those
two lower bounds with the elementary Cauchy perimeter-diameter inequality for the
convex attachment polygon gives a strictly stronger wrapping threshold than Section
96:

$$
\boxed{
\mu_5:=\sqrt{1-(\pi/9)^2}
=0.9370981976747776\ldots .
}
$$

In particular the nominal Section-96 equality value

$$
\mu_4=0.9362157414095831\ldots
$$

is not attainable by a wrapping harmonic-cell limit. Consequently any theorem whose
hypothesis is a wrapping sequence with normalized cell diameter tending to `mu_4` is
conditional on an empty asymptotic regime. This does not make the internal conditional
algebra of such a theorem false; it removes that regime from the live C-II frontier.

---

# 98. Cauchy perimeter raises the wrapping threshold to 0.937098 D

## 98.1 Setup

Let `P_j=conv(A_j)` be a wrapping Type-II harmonic-cell sequence with source diameters
`D_j -> infinity` and

$$
{\operatorname{diam}(P_j)\over D_j}\to\lambda<1.
\tag{98.1}
$$

Put

$$
\theta:=2\arcsin\lambda\in[2\pi/3,\pi).
\tag{98.2}
$$

After passing to a subsequence write

$$
{a_j\over D_j}\to\alpha,
\qquad a_j:=|A_j|.
\tag{98.3}
$$

The attachment density is positive for a macroscopic wrapping cell by the canonical
harmonic attachment multiplicity bound.

## 98.2 Canonical Sections 94 and 96 give a perimeter floor

Canonical Section 94, equation (94.14), proves

$$
\liminf_j {\operatorname{per}(P_j)\over D_j}
\ge
\alpha+3\sin\theta.
\tag{98.4}
$$

Canonical Section 96, equation (96.9), independently proves

$$
\alpha\ge {3\over2}\sin\theta.
\tag{98.5}
$$

Therefore

$$
\boxed{
\liminf_j {\operatorname{per}(P_j)\over D_j}
\ge {9\over2}\sin\theta.
}
\tag{98.6}
$$

No endpoint equality assumption is used here.

## 98.3 Cauchy perimeter-diameter inequality

For every planar convex body `K`, Cauchy's projection formula gives

$$
\operatorname{per}(K)
=\int_0^\pi w_K(u_\varphi)\,d\varphi,
$$

where `w_K` is directional width. Since every directional width is at most
`diam(K)`,

$$
\boxed{
\operatorname{per}(K)\le\pi\operatorname{diam}(K).
}
\tag{98.7}
$$

This inequality is already used elsewhere in the repository for the same attachment
polygons. Applying it to `P_j` and (98.1) gives

$$
\boxed{
\limsup_j {\operatorname{per}(P_j)\over D_j}
\le\pi\lambda
=\pi\sin(\theta/2).
}
\tag{98.8}
$$

Combining (98.6) and (98.8),

$$
{9\over2}\sin\theta
\le
\pi\sin(\theta/2).
\tag{98.9}
$$

Since `theta/2 in [pi/3,pi/2)` and hence `sin(theta/2)>0`, use
`sin(theta)=2sin(theta/2)cos(theta/2)` to cancel the positive factor:

$$
\boxed{
9\cos(\theta/2)\le\pi.
}
\tag{98.10}
$$

Thus

$$
{\theta\over2}\ge\arccos(\pi/9)
\tag{98.11}
$$

and therefore

$$
\boxed{
\lambda=\sin(\theta/2)
\ge
\sqrt{1-(\pi/9)^2}
=:\mu_5.
}
\tag{98.12}
$$

Numerically,

$$
\boxed{
\mu_5=0.9370981976747776\ldots,
\qquad
\theta_5=2\arccos(\pi/9)
=2.4284445238864523\ldots .
}
\tag{98.13}
$$

This strictly improves the canonical Section-96 threshold because

$$
\mu_5-\mu_4
=0.0008824562651944\ldots>0.
\tag{98.14}
$$

At `theta_5`, the independent Section-96 six-cluster ceiling still has positive
slack:

$$
3\theta_5-2\pi-{3\over2}\sin\theta_5
=0.020821326643998\ldots>0.
\tag{98.15}
$$

Thus the new obstruction is genuinely Cauchy/perimeter information, not a disguised
restatement of Section 96's scalar inequality.

## 98.4 The Section-96 endpoint is impossible

At the old Section-96 equality value `theta_4`, write

$$
\alpha_4={3\over2}\sin\theta_4
=0.9870310682463526\ldots .
$$

The combined canonical lower bound (98.6) would require

$$
\liminf {\operatorname{per}(P_j)\over D_j}
\ge 3\alpha_4
=2.9610932047390577\ldots,
\tag{98.16}
$$

whereas Cauchy would require

$$
\limsup {\operatorname{per}(P_j)\over D_j}
\le\pi\mu_4
=2.9412084953874680\ldots .
\tag{98.17}
$$

The gap is

$$
3\alpha_4-\pi\mu_4
=0.0198847093515897\ldots>0.
\tag{98.18}
$$

Hence no wrapping sequence can satisfy

$$
\operatorname{diam}(P_j)/D_j\to\mu_4.
\tag{98.19}
$$

This directly audits the two proof-only/unreviewed Section-97 endpoint analyses now in
the repository. Their deductions under hypothesis (98.19) may be internally valid,
but that hypothesis is incompatible with the canonical Sections 94 and 96 plus
Cauchy. They are therefore not live survivor branches.

## 98.5 Propagate the stronger threshold to an actual carrier

The Section-88 cap-family transfer does not depend specifically on `mu_0`; its proof
requires only that every macroscopic limiting cell of diameter at most a fixed `mu`
be cap type. Section 98 supplies exactly that condition for every fixed

$$
\mu<\mu_5.
$$

Indeed a wrapping limit with normalized diameter at most `mu` would contradict
(98.12). Therefore the proof of Theorem 88.6 applies with `mu_5` replacing `mu_0`:

$$
\limsup {1\over D^2}
\sum_{\operatorname{diam}(P_r)\le\mu D}
\operatorname{area}(P_r)
\le\mathcal C(\mu)<{\pi\over4}.
\tag{98.20}
$$

The strict inequality holds for every fixed `mu<1` by canonical (88.22). At `mu_5`,
for reference,

$$
\mathcal C(\mu_5)=0.4981464214216209\ldots,
\qquad
{\pi\over4}-\mathcal C(\mu_5)
=0.2872517419758274\ldots>0.
\tag{98.21}
$$

The canonical total harmonic-cell perimeter bound therefore leaves only uniformly
many cells longer than `mu D`, and Section 83 gives total local rhombic deficit
`o(D^2)`. Taking `mu upward mu_5` diagonally exactly as in Sections 88, 94, and 96
produces an actual macroscopic locally rhombus-saturated carrier `P_*` with

$$
\boxed{
\operatorname{diam}(P_*)
\ge(\mu_5-o(1))D,
\qquad
\operatorname{area}(P_*)\ge c_5D^2,
\qquad
{A_{4,*}\over\operatorname{area}(P_*)}\to1
}
\tag{98.22}
$$

for one absolute `c_5>0`.

## 98.6 What remains

Section 98 does not close C-II. It removes the old `mu_4` equality regime and raises
the guaranteed macroscopic carrier diameter. The live full-core branch must now be
analyzed at normalized carrier diameter at least `mu_5-o(1)`, while retaining the
canonical ordered-grid and interface structure.

A future endpoint analysis must start at `mu_5`, not `mu_4`. Equality in (98.9) would
simultaneously require saturation of the Section-94 perimeter floor, the Section-96
attachment-density floor, and Cauchy's perimeter-diameter inequality. That is a much
more restrictive equality stack and is the natural next hostile-audit target.

## 98.7 Dependency and regression audit

- **Canonical Section 94:** perimeter floor
  `liminf per(P_j)/D_j >= alpha+3 sin(theta)`.
- **Canonical Section 96:** attachment-density floor
  `alpha >= (3/2) sin(theta)`.
- **Cauchy perimeter-diameter inequality:**
  `per(P)<=pi diam(P)` for every planar convex attachment polygon; this inequality is
  already used elsewhere in the repository.
- **Canonical Section 88:** cap-family capacity and diagonal transfer to an actual
  macroscopic carrier.
- **Canonical Section 83:** pairwise cell disjointness and summed local rhombic
  deficit.
- **No Section-97 endpoint theorem is used.** In particular the proof is independent
  of both currently competing Section-97 endpoint analyses.
- **No KKT coefficient floor, Fox--Pach constant, rejected cap theorem, or deletion of
  contact-isolated source points is used.**

**Promotion recommendation:** hostile-audit Section 98 independently. If it passes,
promote the `mu_5` wrapping threshold and actual-carrier consequence, and mark all
`mu_4`-endpoint branches as vacuous historical conditionals rather than active
frontiers.
