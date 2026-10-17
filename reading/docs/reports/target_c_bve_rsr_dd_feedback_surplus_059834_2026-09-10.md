> Generated reading edition · [exact source](../../../docs/reports/target_c_bve_rsr_dd_feedback_surplus_059834_2026-09-10.md) · source SHA-256 `de010e81cf8e4c7790bb76dee675748fb330a0ebeb5f41d39079f83bed254a9f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-A260BC2138D8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact boundary-vertex feedback raises the generic post-ZF surplus floor above 0.59834

**Date:** 2026-09-10  
**Branch base:** `9cdab3854ef89b366ea62c00e280f4f361ed3964`  
**Depends on:** BVE, RD, RX, FSDB, RSJ  
**Run type:** exact feedback optimization / rational lower certificate  
**Target:** Target C, C-II after ZF  
**External input:** none beyond the Bonnesen theorem already imported in BV/BVE

## LEVEL I STATUS

`STILL OPEN`.

BVE replaces the constant GU/BV attachment-cell coefficient by the
surplus-dependent function

```math
G(\lambda)
=\left(\frac\pi4-\frac{\kappa(\lambda)^2}{4}\right)\lambda^2,
\tag{BF.1}
```

where `kappa(lambda)` is the unique root in `(0,3-2sqrt(2))` of

```math
\boxed{
\lambda(1+\kappa)^3=1-6\kappa+\kappa^2.
}
\tag{BF.2}
```

The function `G` is strictly increasing on `(0,1)`.

Solving the resulting RSR/DD feedback problem gives a unique exact threshold
`lambda_BVE` such that every unbounded post-ZF survivor satisfies

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge\lambda_{BVE}>0.59834.
}
\tag{BF.3}
```

Numerically, only for orientation,

```math
\boxed{
y_{BVE}=1.5245276161497389939\ldots,}
\tag{BF.4}
```

```math
\boxed{
p_{BVE}=3.0231380087236307875\ldots,}
\tag{BF.5}
```

```math
\boxed{
\lambda_{BVE}=0.5983402429824461755\ldots .
}
\tag{BF.6}
```

The theorem claim is the rigorous inequality in BF.3.  The long decimals are not
proof dependencies.

---

## 1. Strengthened feedback feasibility system

Retain

```math
\Phi(y)=\frac{y+\sin y}{4},
\qquad
c_R=\frac\pi{(\pi-2)^2},
\qquad
\Psi(p)=c_R\left(\frac p2-1\right)^2,
\tag{1.1}
```

and

```math
A(y,p)=\max\{\Phi(y),\Psi(p)\}.
\tag{1.2}
```

As in RX, enlarge the actual DB region to

```math
\widetilde{\mathcal R}
=
\{(y,p):2\rho\le y\le\pi,\ y\le p\le\min\{2y,\pi\}\}.
\tag{1.3}
```

Every actual post-ZF survivor lies in this larger region.

For any subsequential surplus limit `lambda<1`, BVE gives

```math
\limsup\frac1{D^2}
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le G(\lambda).
\tag{1.4}
```

Therefore the two RD cavity arguments sharpen to

```math
\boxed{
A(y,p)-G(\lambda)
\le\frac{(\lambda+p-y)^2}{4\pi},
}
\tag{1.5}
```

and

```math
\boxed{
A(y,p)-G(\lambda)
\le
\Delta(y,p)
:=\frac2{\sqrt3}y^{3/2}\sqrt{2y-p}.
}
\tag{1.6}
```

For a fixed `(y,p)`, both inequalities define lower thresholds in `lambda` because
`G` is strictly increasing, and the right side of (1.5) is also strictly increasing
in `lambda`.

If a survivor has `lambda>=1`, BF.3 is immediate.  Hence no generality is lost by
working on the range where BVE applies.

---

## 2. Fixed-`y` optimizer remains at or before the FSDB/RSR crossover

The area crossover is unchanged:

```math
\boxed{
p_e(y)=2+2\sqrt{\frac{\Phi(y)}{c_R}}.}
\tag{2.1}
```

Thus

```math
\Psi(p_e(y))=\Phi(y).
\tag{2.2}
```

On `p<=p_e(y)`, `A=Phi(y)`.  Let `J_G(y,p)` be the threshold from (1.5) and
`D_G(y,p)` the threshold from (1.6).

For fixed `y` on this branch:

1. `J_G` strictly decreases with `p`, because only `m=p-y` increases;
2. `D_G` strictly increases with `p`, because `Delta(y,p)` strictly decreases.

Indeed, the defining equations are

```math
\Phi(y)-G(J_G)
=\frac{(J_G+p-y)^2}{4\pi},
\tag{2.3}
```

and

```math
\Phi(y)-G(D_G)=\Delta(y,p).
\tag{2.4}
```

For `p>=p_e(y)`, both thresholds strictly increase.  For `D_G`, the left area
currency `Psi(p)` increases while `Delta` decreases.  For `J_G`, differentiate

```math
\Psi(p)-G(\lambda)
=\frac{(\lambda+p-y)^2}{4\pi}.
\tag{2.5}
```

Since

```math
\Psi'(p)=\frac{c_R}{2}(p-2),
```

implicit differentiation gives

```math
\lambda'(p)
=
\frac{
\Psi'(p)-(\lambda+p-y)/(2\pi)
}{
G'(\lambda)+(\lambda+p-y)/(2\pi)
}.
\tag{2.6}
```

The denominator is positive.  RSJ gives on the active branch

```math
p\ge p_e(y_R)=2y_R>3,
\qquad c_R>2.
```

Every relevant threshold below the trivial range has `lambda<1`, while `p-y<=pi`.
Therefore

```math
\pi c_R(p-2)>2\pi>1+\pi>\lambda+p-y,
```

so the numerator in (2.6) is positive.

Hence no fixed-`y` minimizer lies strictly to the right of `p_e(y)`.

---

## 3. The two threshold values on the area crossover move oppositely

For `y>=y_R`, define

```math
u(y)=2y-p_e(y),
\tag{3.1}
```

and

```math
E(y)=
\Phi(y)-\frac2{\sqrt3}y^{3/2}\sqrt{u(y)}.
\tag{3.2}
```

RX proves

```math
\boxed{E'(y)<0
\qquad(y_R<y\le\pi/2).}
\tag{3.3}
```

That proof is independent of the attachment-area coefficient.

Define `d_G(y)` as the unique nonnegative solution, when it exists, of

```math
\boxed{G(d_G(y))=E(y).}
\tag{3.4}
```

Since `G` is strictly increasing and `E` strictly decreases,

```math
\boxed{d_G(y)\text{ strictly decreases}.}
\tag{3.5}
```

Define `r_G(y)` as the unique positive solution of

```math
\boxed{
\Phi(y)-G(r_G(y))
=
\frac{(r_G(y)+m(y))^2}{4\pi},
}
\tag{3.6}
```

where

```math
m(y)=p_e(y)-y.
\tag{3.7}
```

RSJ/RX gives

```math
p_e'(y)<1/2,
\qquad
m'(y)<-1/2.
\tag{3.8}
```

Differentiate (3.6):

```math
\left[
G'(r_G)+\frac{r_G+m}{2\pi}
\right]r_G'
=
\Phi'(y)-\frac{(r_G+m)m'}{2\pi}.
\tag{3.9}
```

The bracket on the left is positive.  The right side is strictly positive because
`Phi'>=0`, `r_G+m>0`, and `m'<0`.  Hence

```math
\boxed{r_G'(y)>0.}
\tag{3.10}
```

At `y=y_R`, `u=0`, so (3.4) gives

```math
G(d_G(y_R))=\Phi(y_R).
```

Equation (3.6) has a strictly positive cavity term, so

```math
G(r_G(y_R))<\Phi(y_R),
```

and therefore

```math
\boxed{d_G(y_R)>r_G(y_R).}
\tag{3.11}
```

At `y=pi/2`, RX proves `E(y)<0`, so the DD obstruction has already dropped to zero,
while `r_G>0`.  Thus

```math
\boxed{d_G(\pi/2)=0<r_G(\pi/2).}
\tag{3.12}
```

There is consequently a unique

```math
\boxed{y_{BVE}\in(y_R,\pi/2)}
\tag{3.13}
```

such that

```math
\boxed{d_G(y_{BVE})=r_G(y_{BVE}).}
\tag{3.14}
```

---

## 4. The pre-transition fixed-`y` minimum strictly decreases

For `y<=y_BVE`, the fixed-`y` optimum is the unique pre-crossover intersection of
(1.5) and (1.6).  Let its common threshold be `lambda` and put

```math
S=\Phi(y)-G(\lambda)>0.
\tag{4.1}
```

JC equality gives

```math
p-y=2\sqrt{\pi S}-\lambda,
\tag{4.2}
```

while DD equality gives

```math
2y-p=\frac{3S^2}{4y^3}.
\tag{4.3}
```

Eliminate `p`:

```math
\boxed{
F(y,\lambda)
:=
y+\lambda-2\sqrt{\pi S}
-\frac{3S^2}{4y^3}=0.
}
\tag{4.4}
```

At fixed `y`, since `S_\lambda=-G'(\lambda)`,

```math
\boxed{
F_\lambda
=
1+
\frac{\sqrt\pi\,G'(\lambda)}{\sqrt S}
+
\frac{3S G'(\lambda)}{2y^3}>0.
}
\tag{4.5}
```

At fixed `lambda`, `S_y=Phi'(y)`, so

```math
F_y
=
1-
\frac{\sqrt\pi\,\Phi'(y)}{\sqrt S}
-
\frac{3S\Phi'(y)}{2y^3}
+
\frac{9S^2}{4y^4}.
\tag{4.6}
```

The feedback system is pointwise stronger than RX, whose global minimum is already
proved greater than `299/500`.  Hence every crossing considered here satisfies

```math
\lambda>\frac{299}{500}.
\tag{4.7}
```

Also

```math
y\ge2\rho>\frac{147}{100}>\frac75,
\qquad
\Phi'(y)<\frac7{25}
\tag{4.8}
```

on the relevant pre-transition range.  Since `G(lambda)` is stronger than the fixed BV
coefficient used in BRD, the same robust bounds from BRD apply:

```math
\boxed{\frac3{10}<S<\frac38.}
\tag{4.9}
```

For completeness, the upper bound follows from `Phi<9/14` and the old BV lower
coefficient; the lower bound follows from (4.3), which gives `2y-p<1/25`, then
`p-y>34/25`, and finally JC equality.

Using `pi<22/7`,

```math
\sqrt{\pi/S}<\sqrt{220/21}<13/4.
```

Discarding the final positive term in (4.6),

```math
\begin{aligned}
F_y
&>
1-
\frac7{25}\frac{13}{4}
-
\frac{3(3/8)(7/25)}{2(7/5)^3}\\
&=
1-\frac{91}{100}-\frac{45}{784}\\
&=
\boxed{\frac{639}{19600}>0.}
\end{aligned}
\tag{4.10}
```

Therefore implicit differentiation of (4.4) gives

```math
\boxed{
\lambda'(y)=-F_y/F_\lambda<0.
}
\tag{4.11}
```

The pre-transition fixed-`y` optimum strictly decreases with `y`.

---

## 5. Unique global optimizer and exact defining system

Sections 2--4 give the complete optimizer geometry:

- before `y_BVE`, the unique JC/DD crossing is the fixed-`y` minimum and strictly
  decreases with `y`;
- after `y_BVE`, the fixed-`y` minimum is the area-crossover JC value `r_G(y)` and
  strictly increases with `y`;
- the two branches meet exactly at `y_BVE`.

Hence the unique global minimum is

```math
\boxed{
(y,p)=(y_{BVE},p_e(y_{BVE})).
}
\tag{5.1}
```

Define

```math
\boxed{
\lambda_{BVE}:=d_G(y_{BVE})=r_G(y_{BVE}).
}
\tag{5.2}
```

Equivalently, the optimizer is the unique solution in

```math
y_R<y<\pi/2,
\qquad
p=p_e(y),
\qquad
0<\lambda<1
```

of the four equations

```math
\boxed{
\Phi(y)=c_R\left(\frac p2-1\right)^2,
}
\tag{5.3}
```

```math
\boxed{
\Phi(y)-G(\lambda)
=\frac{(\lambda+p-y)^2}{4\pi},
}
\tag{5.4}
```

```math
\boxed{
\Phi(y)-G(\lambda)
=\frac2{\sqrt3}y^{3/2}\sqrt{2y-p},
}
\tag{5.5}
```

```math
\boxed{
\lambda(1+\kappa)^3=1-6\kappa+\kappa^2,
\qquad
G(\lambda)=\frac{\pi-\kappa^2}{4}\lambda^2.
}
\tag{5.6}
```

Every post-ZF subsequential surplus limit is at least `lambda_BVE`; therefore BF.3
follows once the rational `>0.59834` certificate is supplied.

---

## 6. Exact rational certificate for `lambda_BVE>0.59834`

Take

```math
\boxed{y_0=\frac{609811}{400000}=1.5245275.}
\tag{6.1}
```

The companion verifier uses only exact `fractions.Fraction` arithmetic.  Its analytic
inputs are:

1. Machin's identity with alternating arctangent series for rational bounds on `pi`;
2. the alternating Taylor series for rational bounds on `sin(y_0)`;
3. monotonicity of `c_R(pi)=pi/(pi-2)^2`;
4. monotonicity in `kappa` of the cubic in BF.2;
5. rational square-root brackets checked by squaring.

It proves the area-crossover square-root bracket

```math
0.5115689920
<\sqrt{\Phi(y_0)/c_R}
<0.5115689921,
\tag{6.2}
```

and therefore a rational interval for `p_e(y_0)` and `m=p_e-y_0`.

For

```math
\lambda_0=0.59834,
```

the cubic root is bracketed by

```math
0.0512495574<\kappa(\lambda_0)<0.0512495575.
\tag{6.3}
```

Evaluating the JC residual with outward rational rounding gives

```math
\boxed{J_G(y_0,\lambda_0)<0,}
\tag{6.4}
```

so

```math
r_G(y_0)>0.59834.
```

At

```math
\lambda_1=0.598341,
```

the verifier brackets

```math
0.0512494100<\kappa(\lambda_1)<0.0512494101
\tag{6.5}
```

and proves both

```math
\boxed{J_G(y_0,\lambda_1)>0}
\tag{6.6}
```

and

```math
\boxed{E(y_0)>G(\lambda_1).}
\tag{6.7}
```

Thus

```math
0.59834<r_G(y_0)<0.598341<d_G(y_0).
\tag{6.8}
```

Because `d_G-r_G` decreases through its unique zero, `y_0<y_BVE`.  Since `r_G`
is strictly increasing,

```math
\boxed{
\lambda_{BVE}
=r_G(y_{BVE})
>r_G(y_0)
>0.59834.
}
\tag{6.9}
```

This is the exact certificate required for BF.3.

---

## 7. Numerical orientation

High-precision solution of (5.3)--(5.6) gives

```math
y_{BVE}
=1.52452761614973899392642140246\ldots,
```

```math
p_{BVE}
=3.02313800872363078753762635584\ldots,
```

```math
\lambda_{BVE}
=0.59834024298244617552970125305\ldots,
```

and

```math
\kappa(\lambda_{BVE})
=0.05124952160364505\ldots .
```

The gain over the fixed-coefficient BV optimizer is small but genuine:

```math
0.59834024298\ldots-0.59833124943\ldots
\approx8.99\times10^{-6}.
```

The larger mathematical gain is that the attachment defect is now self-consistent and
surplus-dependent rather than frozen at the arbitrary cutoff `3/5`.

---

## 8. Endpoint equality implications

BVE is strict unless the Bonnesen/support-net defect reaches exactly the root
`kappa(lambda_BVE)`.  Therefore a hypothetical sequence attaining `lambda_BVE` must
simultaneously saturate:

1. the global BVE attachment-area capacity `G(lambda_BVE)`;
2. the sum-of-squares concentration in the component-diameter budget;
3. the FSDB/RSR area crossover;
4. the JC cavity bound;
5. the DD detour bound.

As in AC, global attachment-area saturation forces one macroscopic unloaded component
to carry asymptotically all component graph diameter.  The difference is that its
attachment hull now has a fixed positive isodiametric deficit rather than converging to
a disk.  The relevant geometric endpoint is the exact Bonnesen/support-normal
configuration at

```math
x=\kappa(\lambda_{BVE})\approx0.05125.
```

This gives a finite-shape target for the next structural exclusion.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| feedback feasibility system (1.5)--(1.6) | proved | BVE capacity inserted into RD |
| fixed-`y` optimizer at/before `p_e` | proved | opposite monotonicity before crossover; both increase after |
| `d_G` decreases | proved | `E` decreases and `G` increases |
| `r_G` increases | proved | direct implicit differentiation |
| pre-transition minimum decreases | proved | same exact `F_y` formula, `F_y>639/19600` |
| unique global optimizer | proved | decreasing and increasing branches meet once |
| `lambda_BVE>0.59834` | exact rational certificate | companion verifier |
| long decimal in BF.6 | numerical orientation only | not a proof dependency |
| Level I | still open | high-surplus survivors above the feedback floor remain possible |

---

## 10. Next run

Audit equality in the exact BVE support-net theorem.  Equality requires a common
Bonnesen annulus, near-maximal angular gaps between shared attachment vertices, and a
force-hull point simultaneously realizing the extremal support-normal radius.  Combine
that finite-shape requirement with the DD endpoint, where the outer contact walk has a
small but positive chain-chord detour.  Any incompatibility excludes the exact
`lambda_BVE` endpoint; a quantitative incompatibility raises the explicit generic floor
again.
