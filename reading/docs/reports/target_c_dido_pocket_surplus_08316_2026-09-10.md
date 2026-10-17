> Generated reading edition · [exact source](../../../docs/reports/target_c_dido_pocket_surplus_08316_2026-09-10.md) · source SHA-256 `2152876cd7c11567067c9174bd2e85e6375e1122732834459bc9330aff927657`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-79B0CDCCA1EA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — sharp Dido pocket envelope raises the post-ZF surplus floor to 0.831687

**Date:** 2026-09-10  
**Repository state:** branch `research/c99-c2-dpc-20260910-sol`, after commit `6e008464e479ca21032dbb386ea391eaf4e445a2`; `main` separately advanced to `f977f2d0d25f5022c2a587e59cab38375d85caee` during the run  
**Run type:** closing proof / exact geometric sharpening / asymptotic branch exclusion  
**Target:** Target C, C-II after ZF/DB/FSDB  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** no external theorem imported  
**Computation:** decimal evaluation of one analytically defined root only; no floating-point sign is a proof dependency

## LEVEL I STATUS

`STILL OPEN`

The preceding DPC report proved a new unit-edge pocket bound and obtained

```math
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge0.7739547058568927\ldots .
```

This report replaces the coarse quadratic pocket envelope in that proof by the exact fixed-chord Dido envelope. The resulting report-level lower bound is

```math
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{DIDO}
=0.8316870417755330\ldots .
}
\tag{DIDO.1}
```

The optimization is analytic. The constant is the unique root of a one-parameter minimum described in Section 5, equivalently the unique solution of the explicit three-equation system in Section 6.

Level I remains open in this report. A later structural argument may exclude the equality endpoint.

## 1. Starting endpoint

Retain the C-II lexicographic source and post-ZF notation of the DPC report. In particular

```math
L=e_{BB}+2s_C,
\qquad
\lambda=\lim L/D,
\qquad
y=\lim h/D,
```

and

```math
\Phi(y)=\frac{y+\sin y}{4},
\qquad
g(y)=y-2\cos(y/2).
```

FSDB/GU gives the whole-source lower gap

```math
\liminf\frac GD^2
\ge
\Phi(y)-\frac\pi4\lambda^2.
\tag{1.1}
```

PC and DB give, after passage to a convergent subsequence,

```math
\tau:=\lim d_P/D,
\qquad
\nu:=\lim Q/D,
\qquad
\tau+\nu\le\lambda,
\tag{1.2}
```

and for the total outer-pocket chain-chord detour

```math
U:=b-P_F,
\qquad
\limsup\frac UD\le g(y)-\nu.
\tag{1.3}
```

The DPC report bounded the outer pockets by a discrete Dirichlet estimate. Here the exact fixed-length/fixed-chord extremal problem is solved and inserted into the same source-level gap comparison.

The implication is

```text
fixed-chord Dido extremal theorem
    -> concave one-pocket coefficient as a function of detour ratio
    -> exact asymptotic multi-pocket capacity
    -> eliminate Q analytically
    -> one-dimensional y-minimization for each lambda
    -> explicit larger forbidden interval.
```

## 2. Exact one-pocket Dido theorem

Let a convex outer pocket have an old contact-chain arc `gamma` of length `ell` and its force-hull chord of length `s`, with `0<s<=ell`.

### Theorem DI.1 — fixed-chord circular-arc maximum

There is a unique `theta in (0,pi)` satisfying

```math
\frac{s}{\ell}=\frac{\sin\theta}{\theta}.
\tag{DI.1}
```

Every such pocket satisfies

```math
\boxed{
area(P)
\le
\ell^2 f(\theta),
\qquad
f(\theta):=
\frac{\theta-\sin\theta\cos\theta}{4\theta^2}.
}
\tag{DI.2}
```

Equality in the unrestricted rectifiable-arc problem is attained by the circular arc of length `ell` subtending central angle `2theta`.

#### Proof

The function `sin(theta)/theta` decreases continuously from `1` to `0` on `(0,pi)`, so DI.1 has a unique solution.

Let `Gamma_theta` be the circular arc of length `ell` with chord `AB` of length `s`, lying in the same half-plane of line `AB` as the pocket. Let `Gamma_theta^c` be the complementary arc of the same circle, lying in the opposite half-plane. The union `Gamma_theta union Gamma_theta^c` is the full circle.

Replace `Gamma_theta` by the pocket chain `gamma`, keeping the complementary circular arc `Gamma_theta^c`. Since the pocket chain and `Gamma_theta^c` lie on opposite sides of `AB` and each is simple, their union is a rectifiable Jordan curve. Its perimeter is exactly the circumference of the comparison circle, because `gamma` and `Gamma_theta` have the same length `ell`.

If the pocket enclosed more area with `AB` than the circular segment bounded by `Gamma_theta` and `AB`, then the new Jordan curve would enclose strictly more area than the comparison circle with the same perimeter. This contradicts the planar isoperimetric inequality. Hence the circular segment maximizes the pocket area.

If `R` is the circle radius, then `ell=2R theta`, while the segment area is

```math
R^2\bigl(\theta-\sin\theta\cos\theta\bigr).
```

Substituting `R=ell/(2theta)` proves DI.2. `square`

### A convenient detour parameter

Put

```math
z:=1-\frac{s}{\ell}
=1-\frac{\sin\theta}{\theta}.
\tag{2.1}
```

For `0<=z<=z_0`, where

```math
\boxed{z_0:=1-\frac2\pi,}
\tag{2.2}
```

one has `0<=theta<=pi/2`. Write `f(z)` for the coefficient in DI.2 under this parametrization.

For larger detour, use the reflection bound. Reflect the convex pocket across its chord. The chord disappears from the doubled boundary, which is a rectifiable Jordan curve of area `2 area(P)` and perimeter `2ell`. Isoperimetry gives

```math
2area(P)\le\frac{(2\ell)^2}{4\pi},
```

hence

```math
\boxed{area(P)\le\frac{\ell^2}{2\pi}.}
\tag{2.3}
```

At `theta=pi/2`, DI.2 has exactly the same coefficient `1/(2pi)`.

Define the capped coefficient

```math
\boxed{
\widehat f(z)=
\begin{cases}
\dfrac{\theta-\sin\theta\cos\theta}{4\theta^2},
&0\le z\le z_0,
\quad z=1-\dfrac{\sin\theta}{\theta},\\[1.2ex]
\dfrac1{2\pi},&z\ge z_0.
\end{cases}
}
\tag{2.4}
```

Then every pocket satisfies

```math
\boxed{area(P)\le\ell^2\widehat f((\ell-s)/\ell).}
\tag{2.5}
```

## 3. Concavity of the Dido coefficient

### Lemma DI.2

On `0<z<z_0`, with the parameter `theta in (0,pi/2)`, one has

```math
\boxed{
\widehat f'(z)=\frac{\cos\theta}{2\theta},
}
\tag{3.1}
```

and

```math
\boxed{
\widehat f''(z)
=-
\frac{\theta\sin\theta+\cos\theta}
{2(\sin\theta-\theta\cos\theta)}<0.
}
\tag{3.2}
```

Therefore `widehat f` is nondecreasing and concave on `[0,infinity)`.

#### Proof

Differentiate

```math
z(\theta)=1-\frac{\sin\theta}{\theta}.
```

Then

```math
\frac{dz}{d\theta}
=
\frac{\sin\theta-\theta\cos\theta}{\theta^2}>0.
\tag{3.3}
```

Direct differentiation of

```math
f(\theta)=
\frac{\theta-\sin\theta\cos\theta}{4\theta^2}
```

and division by (3.3) gives (3.1). Differentiating `cos(theta)/(2theta)` once more and dividing by (3.3) gives (3.2).

At `theta=pi/2`, the left derivative (3.1) is zero. Thus extending by the constant value `1/(2pi)` preserves concavity and monotonicity. `square`

A second identity will be used below:

```math
\boxed{
2\widehat f(z)-z\widehat f'(z)
=
\frac{1-\cos\theta}{2\theta}>0
}
\tag{3.4}
```

in the active Dido range. It follows by direct substitution of (2.1) and (3.1).

## 4. Global asymptotic pocket capacity

Define

```math
\Psi(L,U):=L^2\widehat f(U/L)
\qquad(L>0,U\ge0),
\tag{4.1}
```

with the continuous value `0` at `L=0`.

By monotonicity of `widehat f`, `Psi` is nondecreasing in `U`. It is also strictly increasing in `L` whenever the active coefficient is positive: in the Dido range,

```math
\frac{\partial\Psi}{\partial L}
=L\bigl(2\widehat f-z\widehat f'\bigr)>0
\tag{4.2}
```

by (3.4), while in the capped range `Psi=L^2/(2pi)`.

### Theorem DI.3 — multi-pocket asymptotic envelope

Along any post-ZF subsequence with

```math
\frac{d_P}{D}\to\tau,
\qquad
\frac{b-P_F}{D}\to u,
```

one has

```math
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
\tau^2\widehat f(u/\tau),
}
\tag{4.3}
```

with the right side interpreted as zero when `tau=0`.

#### Proof

Write for each pocket

```math
x_P=\ell_P-2,
\qquad
u_P=\ell_P-s_P.
```

Then `sum x_P=d_P`, `sum nu_P=b-P_F`, and PC gives `a=O(D)`. Also `d_P=O(D)` on every subsequence with bounded `lambda`, because `d_P<=e_BB<=L`.

Fix `epsilon>0`. Split the pockets into

```math
\mathcal S=\{P:x_P<\epsilon D\},
\qquad
\mathcal L=\{P:x_P\ge\epsilon D\}.
```

For `P in S`, the reflection bound (2.3) gives

```math
area(P)\le\ell_P^2/(2\pi).
```

Since

```math
\sum_P\ell_P=d_P+2a=O(D)
```

and `max_{S} ell_P<=epsilon D+2`, the total small-pocket area is

```math
\sum_{P\in\mathcal S}area(P)
=O(\epsilon D^2)+O(D).
\tag{4.4}
```

The number of large pockets is `O_epsilon(1)`. Put

```math
L_{\mathcal L}:=\sum_{P\in\mathcal L}\ell_P,
\qquad
U_{\mathcal L}:=\sum_{P\in\mathcal L}\nu_P.
```

Then

```math
L_{\mathcal L}\le d_P+O_\epsilon(1),
\qquad
U_{\mathcal L}\le b-P_F.
\tag{4.5}
```

If `L_L>0`, set

```math
w_P=\ell_P/L_{\mathcal L},
\qquad
z_P=\nu_P/\ell_P.
```

Using (2.5), `w_P^2<=w_P`, and concavity of `widehat f`,

```math
\begin{aligned}
\sum_{P\in\mathcal L}area(P)
&\le
L_{\mathcal L}^2
\sum_{P\in\mathcal L}w_P^2\widehat f(z_P)\\
&\le
L_{\mathcal L}^2
\sum_{P\in\mathcal L}w_P\widehat f(z_P)\\
&\le
L_{\mathcal L}^2
\widehat f\left(
\sum_{P\in\mathcal L}w_Pz_P
\right)\\
&=
\Psi(L_{\mathcal L},U_{\mathcal L}).
\end{aligned}
\tag{4.6}
```

By the monotonicity of `Psi` and (4.5), this is at most

```math
\Psi(d_P+O_\epsilon(1),b-P_F).
```

Divide by `D^2`, pass to the subsequential limit, then let `epsilon downarrow0`. Equation (4.4) disappears and yields (4.3). `square`

## 5. Eliminate exceptional-face density exactly

Let

```math
\nu=\lim Q/D,
\qquad
\tau=\lim d_P/D.
```

PC gives `tau+nu<=lambda`, and DB gives

```math
\limsup\frac{b-P_F}{D}
\le g(y)-\nu.
```

Therefore DI.3 gives

```math
\limsup\frac{H_{out}}{D^2}
\le
(\lambda-\nu)^2
\widehat f\left(
\frac{g(y)-\nu}{\lambda-\nu}
\right),
\tag{5.1}
```

where replacing `tau` by `lambda-nu` only increases the right side. The exceptional-face estimate is

```math
\limsup\frac{A_{exc}}{D^2}
\le\frac{\nu^2}{4\pi}.
\tag{5.2}
```

We claim the sum of (5.1) and (5.2) is maximized at `nu=0`.

If

```math
\frac{g(y)}\lambda\ge z_0,
```

then the pocket term is at most `(lambda-nu)^2/(2pi)`, so

```math
\frac{(\lambda-\nu)^2}{2\pi}
+
\frac{\nu^2}{4\pi}
\le
\frac{\lambda^2}{2\pi}.
\tag{5.3}
```

If `g(y)/lambda<z_0`, feasibility requires `0<=nu<=g(y)`, and

```math
z_\nu:=\frac{g(y)-\nu}{\lambda-\nu}
```

is decreasing, so it remains in the active Dido range. Put

```math
L_\nu=\lambda-\nu,
\qquad U_\nu=g(y)-\nu.
```

Using (3.1) and (3.4),

```math
\frac{d}{d\nu}
\left[
\Psi(L_\nu,U_\nu)+\frac{\nu^2}{4\pi}
\right]
=
-
\frac{\lambda-\nu}{2\theta}
+
\frac{\nu}{2\pi},
\tag{5.4}
```

where `theta<=pi/2`. Hence

```math
\frac{d}{d\nu}(\cdots)
\le
-rac{\lambda-\nu}{\pi}+rac\nu{2\pi}
=
\frac{-\lambda+3\nu/2}{\pi}.
\tag{5.5}
```

But

```math
\nu\le g(y)<z_0\lambda<\frac23\lambda,
```

where the last inequality follows from `pi<6`. Thus (5.5) is strictly negative.

Therefore `nu=0` is the global maximizing relaxation in both cases. ZG/GU now gives

```math
\boxed{
\limsup\frac G{D^2}
\le
\lambda^2\widehat f\left(\frac{g(y)}\lambda\right).
}
\tag{5.6}
```

Combine with the full-source lower gap (1.1): every survivor limit must satisfy

```math
\boxed{
F_\lambda(y):=
\Phi(y)-\frac\pi4\lambda^2
-
\lambda^2\widehat f\left(\frac{g(y)}\lambda\right)
\le0,
\qquad
2\rho\le y\le\pi.
}
\tag{5.7}
```

## 6. Exact optimization in `y`

The preceding DPC/FSJC theorem already implies `lambda>0.58` on every survivor subsequence under consideration. Fix such a `lambda`.

Write `t=y/2`. In the active Dido range, let `theta` be defined by

```math
\frac{g(y)}\lambda
=1-\frac{\sin\theta}{\theta}.
\tag{6.1}
```

Differentiating (5.7) gives

```math
\boxed{
F_\lambda'(y)
=
\frac{1+\sin t}{2}
\left[
1-\sin t-\lambda\frac{\cos\theta}{\theta}
\right].
}
\tag{6.2}
```

Define the bracket

```math
A(y):=1-\sin t-\lambda\frac{\cos\theta}{\theta}.
\tag{6.3}
```

At `y=2rho`, one has `g(y)=0`, hence `theta=0` in the limiting sense and `A(y)->-infinity`. At the end of the active Dido range, `theta=pi/2`, so

```math
A(y)=1-\sin t>0
```

because that transition occurs before `y=pi`.

Moreover

```math
A'(y)
=-\frac12\cos t
+(1+\sin t)
\frac{\theta\sin\theta+\cos\theta}
{\sin\theta-\theta\cos\theta}.
\tag{6.4}
```

For `0<theta<pi/2`,

```math
\frac{\theta\sin\theta+\cos\theta}
{\sin\theta-\theta\cos\theta}>\frac12.
\tag{6.5}
```

Indeed, after cross-multiplication this is equivalent to

```math
\theta(2\sin\theta+\cos\theta)+(2\cos\theta-\sin\theta)>0.
```

For `theta<=pi/4`, both displayed contributions make the sum positive because `2cos theta-sin theta>0`. For `theta>=pi/4`, the first contribution is at least

```math
\frac\pi4\,2\sin\frac\pi4
=rac{\pi\sqrt2}{4}>1,
```

whereas the second is greater than `-1`. Thus (6.5) holds throughout.

Using (6.5) in (6.4),

```math
A'(y)
>
\frac{1+\sin t-\cos t}{2}>0.
\tag{6.6}
```

Hence `A` has exactly one zero in the active Dido range. By (6.2), `F_lambda` strictly decreases to that point and strictly increases afterward. Once the cap `widehat f=1/(2pi)` is reached, `F_lambda'(y)=Phi'(y)>=0`. Thus:

### Theorem DI.4 — unique worst diameter density

For every fixed `lambda>0.58`, the necessary function `F_lambda(y)` has a unique global minimum `y_lambda in (2rho,pi)`. It lies in the active Dido range and is characterized by

```math
\boxed{
1-\sin(y_\lambda/2)
=
\lambda\frac{\cos\theta_\lambda}{\theta_\lambda},
}
\tag{6.7}
```

```math
\boxed{
\frac{g(y_\lambda)}\lambda
=1-rac{\sin\theta_\lambda}{\theta_\lambda},
\qquad
0<\theta_\lambda<\frac\pi2.
}
\tag{6.8}
```

## 7. Unique threshold and explicit value

For fixed `y`, the function `F_lambda(y)` is strictly decreasing in `lambda`. In the active Dido range,

```math
\frac{\partial F_\lambda}{\partial\lambda}
=-\lambda
\left[
\frac\pi2+2\widehat f-z\widehat f'
\right]<0
\tag{7.1}
```

by (3.4); in the capped range the same conclusion is immediate. Therefore

```math
m(\lambda):=\min_{2\rho\le y\le\pi}F_\lambda(y)
```

is strictly decreasing.

At `lambda=0.58`, one has `m(lambda)>0`. Indeed `rho>0.7`, because `cos(0.7)>=1-0.7^2/2>0.7`, and `rho<pi/4`. Thus

```math
2\rho>1.4,
\qquad
\sin(2\rho)>\sin(1.4)>1.4-rac{1.4^3}{6}>0.9,
```

so

```math
\Phi(y)\ge\Phi(2\rho)>0.575.
```

Also

```math
\frac\pi4+\widehat f(z)
\le\frac\pi4+rac1{2\pi}
<\frac{11}{14}+rac16
=\frac{20}{21}.
```

Hence

```math
F_{0.58}(y)
>0.575-rac{20}{21}(0.58)^2>0.
\tag{7.2}
```

At `lambda=1`, choose `y=pi`. Then `Phi(pi)=pi/4` and the cap is active, so

```math
F_1(\pi)=-\frac1{2\pi}<0.
\tag{7.3}
```

By strict monotonicity, there is a unique

```math
\boxed{\lambda_{DIDO}\in(0.58,1)}
```

with `m(lambda_DIDO)=0`.

Equivalently, there is a unique triple

```math
(y_*,\theta_*,\lambda_{DIDO})
\in(2\rho,\pi)\times(0,\pi/2)\times(0.58,1)
```

satisfying

```math
\boxed{
\frac{g(y_*)}{\lambda_{DIDO}}
=1-rac{\sin\theta_*}{\theta_*},
}
\tag{7.4}
```

```math
\boxed{
1-\sin(y_*/2)
=
\lambda_{DIDO}\frac{\cos\theta_*}{\theta_*},
}
\tag{7.5}
```

and

```math
\boxed{
\Phi(y_*)
=
\lambda_{DIDO}^2
\left(
\frac\pi4+
\frac{\theta_*-\sin\theta_*\cos\theta_*}{4\theta_*^2}
\right).
}
\tag{7.6}
```

Numerically,

```math
\boxed{
\begin{aligned}
y_*&=1.58064084288812522726\ldots,\\
\theta_*&=1.15657284072663330343\ldots,\\
\lambda_{DIDO}&=0.83168704177553305198\ldots .
\end{aligned}
}
\tag{7.7}
```

Thus every post-ZF survivor sequence satisfies DIDO.1.

## 8. Equality structure at the Dido endpoint

Suppose a survivor sequence approaches `lambda_DIDO`. The preceding inequalities are strict away from their equality sets, so compactness gives:

```math
\frac hD\to y_*.
\tag{8.1}
```

The exceptional-face optimization in Section 5 is strictly decreasing for `nu>0`, hence

```math
\frac QD\to0.
\tag{8.2}
```

The global pocket envelope is strictly increasing in its macroscopic length argument in the active Dido regime, so

```math
\frac{d_P}{D}\to\lambda_{DIDO}.
\tag{8.3}
```

PC.2 now forces

```math
\boxed{
\frac{e_{BB}}D\to\lambda_{DIDO},
\qquad
\frac{s_C}{D},\frac{d_H}{D},\frac{s_Z}{D},\frac{c_B}{D}\to0.
}
\tag{8.4}
```

The DB detour bound must also be sharp:

```math
\frac{b-P_F}{D}\to g(y_*)
=0.1734055086822775\ldots .
\tag{8.5}
```

Finally, equality in the large-pocket proof of DI.3 forces one outer pocket to carry asymptotically all macroscopic chain length. More precisely, if `ell_max` is the largest OP chain length, then

```math
\boxed{
\frac{\ell_{max}}D\to\lambda_{DIDO}.
}
\tag{8.6}
```

Indeed, the step `sum w_P^2 widehat f(z_P)<=sum w_P widehat f(z_P)` is strict unless the weight of every positive-area macroscopic pocket tends to `0` or `1`; the positive limiting total detour requires at least one positive-area pocket, hence one weight tends to `1`. All other macroscopic chain weight vanishes.

For this unique giant pocket,

```math
\frac{\ell-s}{\ell}
\to
z_*:=\frac{g(y_*)}{\lambda_{DIDO}}
=0.2084985096221789\ldots,
\tag{8.7}
```

so its missing hull-side length satisfies

```math
\boxed{
\frac{s}{D}
\to
\lambda_{DIDO}-g(y_*)
=0.6582815330932555\ldots .
}
\tag{8.8}
```

This endpoint structure is not yet declared contradictory in this report.

## 9. Exact target implication

The report-level full-source C-II lower bound advances from

```math
0.5882283437\ldots
\quad\text{(FSJC)}
```

to

```math
0.7739547058\ldots
\quad\text{(DPC)}
```

and now to

```math
\boxed{0.8316870418\ldots\quad\text{(DIDO)}.}
```

The improvement uses a new geometric theorem, not repeated scalar feedback. The decisive global-optimality input remains FSDB/GU, which comes from the full source and retains all contact-isolated points.

The shortest remaining implication is now to exclude the Dido endpoint/high-surplus geometry, or derive a universal C-II upper bound below `lambda_DIDO`.

## 10. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| fixed-chord Dido theorem DI.1 | proved | isoperimetric replacement argument |
| reflection cap `area<=ell^2/(2pi)` | proved | reflect and apply isoperimetry |
| coefficient derivative/concavity | proved | exact differentiation |
| multi-pocket envelope DI.3 | proved asymptotically | small/large truncation + Jensen |
| exceptional-face optimum `Q/D=0` | proved | exact derivative with wide sign margin |
| unique y-minimizer | proved | bracket derivative is strictly positive |
| unique threshold `lambda_DIDO` | proved | pointwise strict monotonicity in lambda |
| numerical value `0.831687...` | reproducible evaluation | not a proof dependency |
| endpoint has one giant pocket | proved as equality stability | strictness of the weighted-square/Jensen steps |
| Level I | still open | endpoint/high-surplus geometry not yet excluded here |

## 11. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | the Dido upper bound is geometric; the contradiction interval uses the FSDB/GU full-source lower gap and does not claim shell-like local structure is impossible |
| dense isolated fillings | yes | isolates are retained in FSDB; DI itself makes no population assumption |
| many thin triangular pockets | yes | their chain lengths are `O(1)` and disappear in the small-pocket truncation at quadratic scale |
| one giant pocket | yes | DI.3 allows it and DIDO endpoint stability identifies it as the extremal case |
| giant exceptional face | yes | `Q^2/(4pi)` is retained and analytically optimized; positive `Q/D` only lowers total capacity |
| response trace / matching shell regressions | yes | no operator norm, response-trace, or diameter-matching inference is used |

## 12. Failed routes and no-go results

1. The reflection bound `area(P)<=ell^2/(2pi)` alone is valid but weaker than DI in the small-detour regime that controls the new threshold.
2. Continuous DD is not sharp enough because it ignores the fixed chord beyond the first Dirichlet-energy estimate.
3. Near-central symmetry alone does not duplicate a finite giant pocket; finite hull subdivisions can converge to a flat opposite segment. Any endpoint exclusion must use the radial localization of actual force-hull vertices, not Hausdorff symmetry by itself.

## 13. Computation and reproducibility

The proof is analytic. Decimal values in (7.7), (8.5), and (8.8) are evaluations of the uniquely defined system (7.4)-(7.6). A high-precision root solve gives

```text
y      = 1.580640842888125227260171143545394754...
theta  = 1.156572840726633303429078738170603459...
lambda = 0.831687041775533051980297218123794484...
g(y)   = 0.173405508682277524089526035170929459...
z       = 0.208498509622178949628354529251462912...
```

No numerical inequality is used to prove existence, uniqueness, or exclusion below the threshold.

## 14. Canonical promotion recommendation

**Hold as report pending independent audit.** DI.1-DI.4 are candidates for promotion if the PC/DB/FSDB/GU/ZG dependencies survive review. No route map is modified in this commit.

## 15. Next run

Exploit FS.4 more strongly. For every actual diameter edge `bk`, FS.4 places its midpoint within `L_D=o(D)` of the common source circumcenter. This appears to imply a two-sided Hausdorff estimate between `F-o` and the half diameter-direction polygon `P_H/2`. If proved, equality in FSDB should turn the concentrated projective gap into two actual macroscopic opposite force-hull sides. That would contradict the one-giant-pocket Dido endpoint structure.

## 16. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Sharp pocket theorem:
For a pocket with chain length ell and chord s, choose theta in (0,pi) by
    s/ell=sin(theta)/theta.
Then
    area(P)<=ell^2 [theta-sin(theta)cos(theta)]/(4theta^2).
For z=(ell-s)/ell<=1-2/pi, the coefficient f(z) satisfies
    f'(z)=cos(theta)/(2theta),
    f''(z)<0.
Cap it by 1/(2pi) for larger z; the result is concave.

Global asymptotic envelope:
    H_out/D^2 <= tau^2 fhat(u/tau),
    tau=d_P/D,
    u=(b-P_F)/D.
PC+DB+exceptional-face optimization gives
    G/D^2 <= lambda^2 fhat(g(y)/lambda),
    g(y)=y-2cos(y/2).
FSDB/GU gives
    G/D^2 >= Phi(y)-pi lambda^2/4,
    Phi(y)=(y+sin y)/4.
Thus every survivor needs
    F_lambda(y)<=0.
For each lambda>0.58 this function has a unique y-minimum.
The unique threshold is
    lambda_DIDO=0.83168704177553305198... .

Endpoint structure:
    h/D -> 1.5806408428881252...,
    Q,s_C,d_H,s_Z,c_B=o(D),
    d_P/D,e_BB/D -> lambda_DIDO,
and one giant pocket has
    ell/D -> lambda_DIDO,
    s/D -> 0.6582815330932555... .

Next: prove d_Haus(F-o,P_H/2)<=L_D from FS.4 and use FSDB equality to force two
macroscopic opposite hull sides, contradicting one-pocket concentration.
```
