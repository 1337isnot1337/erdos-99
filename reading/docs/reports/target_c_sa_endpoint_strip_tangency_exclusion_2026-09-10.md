> Generated reading edition · [exact source](../../../docs/reports/target_c_sa_endpoint_strip_tangency_exclusion_2026-09-10.md) · source SHA-256 `ca127b99a9f59b09809c7f3243c5eb6ca9c088baf6c7f2de266604a105c38e74`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AE90744654B7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — strip/tangency incompatibility excludes the SA/JC endpoint

**Date:** 2026-09-10  
**Branch base:** `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Depends on:** FD, QPA, SA, and SJ on this branch  
**Run type:** structural compactness theorem / endpoint exclusion  
**Target:** Target C, C-II after ZF  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`.

SJ proves the explicit post-ZF floor

$$
\lambda_{SA}=0.5906428373093669\ldots
$$

and localizes scalar equality to

$$
\frac hD\to y_*,
\qquad
\frac{\operatorname{per}F}{D}\to p_*:=2y_*,
\qquad
\frac{\operatorname{area}F}{D^2}
\to A_*:=\Phi(y_*)=\Xi(p_*).
$$

This report proves that this endpoint is impossible.  The reason is exact: simultaneous
saturation of QPA's perimeter envelope and SA's support-triangulation area bound would
force the normalized central symmetral to be a clipped disk, but that clipped disk has
strictly more area than the SA endpoint permits.

Therefore no unbounded post-ZF survivor sequence can satisfy

$$
\frac{e_{BB}+2s_C}{D}\to\lambda_{SA}.
\tag{ST.1}
$$

Consequently there are constants

$$
\boxed{
\epsilon_{ST}>0,
\qquad D_0<\infty,
}
$$

such that every sufficiently large post-ZF survivor satisfies

$$
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{SA}+\epsilon_{ST}.
}
\tag{ST.2}
$$

The new gap is nonexplicit.  The report-level explicit constant remains
`lambda_SA`; ST proves it is not the true asymptotic endpoint.

---

## 1. Endpoint data from SJ

Assume for contradiction that a post-ZF sequence has `D->infinity` and

$$
\lambda_D:=\frac{e_{BB}+2s_C}{D}
\to\lambda_{SA}.
\tag{1.1}
$$

SJ's strict compact optimization forces

$$
y_D:=\frac hD\to y_*,
\qquad
p_D:=\frac{P_D}{D}	o p_*:=2y_*,
\tag{1.2}
$$

where `P_D=per(F_D)`, and

$$
A_*:=\Phi(y_*)=\Xi(p_*).
\tag{1.3}
$$

Let

$$
a_*:=\alpha(p_*).
\tag{1.4}
$$

By definition of `alpha`,

$$
p_*=f(a_*)
=2\left(\arcsin a_*+\sqrt{1-a_*^2}\right).
\tag{1.5}
$$

Numerically only for orientation,

$$
a_*=0.8254304052515203\ldots<1.
\tag{1.6}
$$

The strict inequality is exact because `p_*<pi` and `alpha(pi)=1`.

---

## 2. Scalar equality forces actual force-hull area equality

Write

$$
\mathcal A_D:=\frac{\operatorname{area}F_D}{D^2},
\qquad
C_D:=\frac1{D^2}\sum_r\operatorname{area}(P_r),
\qquad
G_D:=\mathcal A_D-C_D.
\tag{2.1}
$$

SA gives

$$
\liminf\mathcal A_D\ge A_*.
\tag{2.2}
$$

GU gives

$$
\limsup C_D\le\frac\pi4\lambda_{SA}^2.
\tag{2.3}
$$

The actual-perimeter JC capacity and SJ localization give

$$
\limsup G_D
\le
\frac{(\lambda_{SA}+y_*)^2}{4\pi}.
\tag{2.4}
$$

By the defining SJ equality,

$$
A_*-rac\pi4\lambda_{SA}^2
=
\frac{(\lambda_{SA}+y_*)^2}{4\pi}.
\tag{2.5}
$$

Since `mathcal A_D=G_D+C_D`, (2.3)--(2.5) imply

$$
\limsup\mathcal A_D\le A_*.
\tag{2.6}
$$

Together with (2.2),

$$
\boxed{
\mathcal A_D\to A_*.
}
\tag{2.7}
$$

Thus endpoint equality must saturate the SA force-hull area lower bound itself; there
is no room to hide positive area slack in the attachment cells.

---

## 3. Pass to the central symmetral

Let

$$
S_D:=\frac12((F_D-o_D)-(F_D-o_D))
\tag{3.1}
$$

be the FD central symmetral.  FD gives exactly

$$
\operatorname{diam}S_D=D,
\qquad
\operatorname{per}S_D=P_D,
\tag{3.2}
$$

and

$$
0\le
\operatorname{area}S_D-\operatorname{area}F_D
=o(D^2).
\tag{3.3}
$$

Hence

$$
\boxed{
\frac{\operatorname{area}S_D}{D^2}\to A_*.
}
\tag{3.4}
$$

Normalize

$$
K_D:=D^{-1}S_D.
\tag{3.5}
$$

Then every `K_D` is centrally symmetric about `0`, has diameter one, lies in the
radius-`1/2` disk, and satisfies

$$
\operatorname{per}K_D\to p_*,
\qquad
\operatorname{area}K_D\to A_*.
\tag{3.6}
$$

Let

$$
r_D:=\min_{|u|=1}h_{K_D}(u),
\qquad
a_D:=2r_D.
\tag{3.7}
$$

QPA gives

$$
a_D\ge\alpha(p_D).
\tag{3.8}
$$

SA gives

$$
\operatorname{area}K_D
\ge\frac12r_D\operatorname{per}K_D
=\frac14a_Dp_D.
\tag{3.9}
$$

Using (3.6), `p_D->p_*`, and

$$
A_*=\Xi(p_*)=\frac14a_*p_*,
$$

(3.8)--(3.9) force

$$
\boxed{a_D\to a_*.}
\tag{3.10}
$$

Thus the QPA inradius bound also saturates.

---

## 4. QPA perimeter equality forces a clipped-disk limit

For each `D`, choose a unit direction `u_D` attaining the minimum support in (3.7).
Pass to a subsequence with

$$
u_D\to u_*.
\tag{4.1}
$$

QPA gives the exact containment

$$
K_D
\subseteq
T_D:=
\overline B(0,1/2)
\cap
\{x:|x\cdot u_D|\le a_D/2\}.
\tag{4.2}
$$

By Blaschke selection, pass further so that

$$
K_D\to K_\infty
$$

in Hausdorff distance.  Equations (3.10), (4.1), and (4.2) give

$$
K_\infty
\subseteq
T_*:=
\overline B(0,1/2)
\cap
\{x:|x\cdot u_*|\le a_*/2\}.
\tag{4.3}
$$

Convex perimeter is continuous under Hausdorff convergence, so

$$
\operatorname{per}K_\infty=p_*.
\tag{4.4}
$$

The clipped-disk perimeter computation from QPA gives

$$
\operatorname{per}T_*=f(a_*)=p_*.
\tag{4.5}
$$

Both bodies are centrally symmetric about the same center.  Cauchy's width formula
and (4.3) give

$$
w_{K_\infty}(\theta)\le w_{T_*}(\theta)
$$

for every direction, while (4.4)--(4.5) give equality of their width integrals.  The
width difference is continuous and nonnegative, so it vanishes identically.  Central
symmetry then gives equality of support functions, hence

$$
\boxed{K_\infty=T_*.}
\tag{4.6}
$$

This is the rigidity statement hidden in QPA's perimeter envelope.

---

## 5. The clipped disk has too much area

Scale temporarily by a factor `2`, so the containing disk has radius one and the strip
is `|x\cdot u_*|<=a_*`.  Its area is

$$
2\left(
\arcsin a_*+a_*\sqrt{1-a_*^2}
\right).
$$

Scaling back by `1/2` multiplies area by `1/4`, so

$$
\boxed{
\operatorname{area}T_*
=
\frac12\left(
\arcsin a_*+a_*\sqrt{1-a_*^2}
\right).
}
\tag{5.1}
$$

On the other hand, using `p_*=f(a_*)`, the SA endpoint area is

$$
\begin{aligned}
A_*
&=\Xi(p_*)
=\frac14a_*p_*\\
&=\frac12a_*\left(
\arcsin a_*+\sqrt{1-a_*^2}
\right).
\end{aligned}
\tag{5.2}
$$

Subtracting gives the exact positive gap

$$
\boxed{
\operatorname{area}T_*-A_*
=
\frac{1-a_*}{2}\arcsin a_*
>0.
}
\tag{5.3}
$$

Numerically this gap is approximately

$$
0.08475041556.
$$

But Hausdorff convergence in Section 4 implies area convergence, so (4.6) gives

$$
\operatorname{area}K_D
\to\operatorname{area}T_*.
\tag{5.4}
$$

Section 3 instead gives

$$
\operatorname{area}K_D\to A_*.
\tag{5.5}
$$

Equations (5.3)--(5.5) contradict each other.  Therefore the endpoint assumption
(1.1) is impossible.

---

## 6. Uniform nonexplicit gap

If ST.2 failed, then for every integer `j` there would be a post-ZF survivor with
arbitrarily large `D` and

$$
\frac{e_{BB}+2s_C}{D}
<\lambda_{SA}+\frac1j.
$$

Choose a diagonal sequence with `D_j->infinity`.  SJ gives the opposite lower bound
`lambda_SA-o(1)`, so after taking a subsequence its normalized surplus tends exactly to
`lambda_SA`.  This contradicts Sections 1--5.

Hence some absolute `epsilon_ST>0` and `D_0` exist, proving ST.2.

No numerical value for `epsilon_ST` is claimed.

---

## 7. What equality conditions actually failed

The contradiction can be stated without compactness jargon:

1. QPA perimeter saturation says a centered-symmetric diameter-one body must fill the
   entire maximum-perimeter clipped disk determined by its minimum support;
2. SA area saturation says its average support, weighted by boundary length, is equal
   to the minimum support;
3. a nontrivial clipped disk has circular boundary arcs with support strictly larger
   than that minimum, producing the fixed positive excess (5.3).

The obstruction is therefore geometric, not numerical.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| SJ endpoint localization | already proved on branch | strict compact scalar optimization |
| endpoint forces `area(F)/D^2->A_*` | proved | JC upper + GU attachment upper + SA lower meet at defining equality |
| central symmetral inradius ratio `a_D->a_*` | proved | QPA lower + SA support-area saturation |
| QPA equality limit is clipped disk | proved | containment + equal perimeter + Cauchy widths + central symmetry |
| clipped-disk area exceeds SA endpoint | proved exactly | difference `(1-a_*)asin(a_*)/2>0` |
| SA endpoint excluded | proved | compactness contradiction |
| positive uniform gap above `lambda_SA` | proved nonconstructively | diagonal-sequence argument |
| Level I | still open | high-surplus survivors above the gap remain possible |

---

## 9. Next run

Turn the strip/tangency incompatibility quantitative.  A stability estimate relating
perimeter deficit inside the QPA clipped disk to support-area excess would convert the
fixed endpoint gap (5.3) into an explicit `epsilon_ST`.  In parallel, use the localized
facts `p≈2y`, `s_C=o(D)`, and the exact JC defect ledgers to see whether the same
near-endpoint regime forces a forbidden diameter/contact topology before a full
stability calculation is needed.
