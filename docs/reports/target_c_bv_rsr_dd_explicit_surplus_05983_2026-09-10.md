<!-- theorem-state: {"artifact_id":"ART-7FAB2E4EE903","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — boundary-vertex stability raises the generic post-ZF surplus floor above 0.5983

**Date:** 2026-09-10  
**Branch base:** `5851cd5bf74b402a29ab72c07f3e27bbdaf77c0d`  
**Depends on:** BV, RD, RX on this branch; FSDB and RSJ  
**Run type:** exact optimizer localization + explicit coefficient improvement  
**Target:** Target C, C-II after ZF

## LEVEL I STATUS

`STILL OPEN`.

BV improves the attachment-cell area coefficient throughout the current low-surplus
range from `pi/4` to

\[
\boxed{
c_{BV}:=\frac\pi4-\frac1{1600}.}
\tag{BRD.1}
\]

Re-running the RSR/DD optimization gives a new exact generic post-ZF threshold
`lambda_BRD` satisfying

\[
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge\lambda_{BRD}>0.5983.
}
\tag{BRD.2}
\]

The optimizer is unique.  Numerically, only for orientation,

\[
y_{BRD}=1.5245273793788846894\ldots,
\tag{BRD.3}
\]

\[
p_{BRD}=3.0231379585040676617\ldots,
\tag{BRD.4}
\]

and

\[
\boxed{
\lambda_{BRD}
=0.5983312494252812289\ldots .
}
\tag{BRD.5}
\]

The exact theorem is BRD.2; a companion exact-Fraction verifier certifies the displayed
`>0.5983` inequality.

---

## 1. Strengthened two-obstruction system

Retain

\[
\Phi(y)=\frac{y+\sin y}{4},
\qquad
c_R=\frac\pi{(\pi-2)^2},
\qquad
\Psi(p)=c_R\left(\frac p2-1\right)^2,
\tag{1.1}
\]

and

\[
A(y,p)=\max\{\Phi(y),\Psi(p)\}.
\tag{1.2}
\]

As in RX, enlarge the actual DB domain to

\[
\widetilde{\mathcal R}
=
\{(y,p):2\rho\le y\le\pi,\ y\le p\le\min\{2y,\pi\}\}.
\tag{1.3}
\]

Every actual post-ZF survivor lies in this larger region.

BV proves that for every survivor sequence with candidate surplus below `3/5`, the
attachment-cell area satisfies

\[
\limsup\frac1{D^2}
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le c_{BV}\lambda^2.
\tag{1.4}
\]

Since the final constant in BRD.5 is below `3/5`, this hypothesis is self-consistent in
the entire range being excluded.  RD's two cavity arguments therefore sharpen to

\[
\boxed{
A(y,p)-c_{BV}\lambda^2
\le
\frac{(\lambda+p-y)^2}{4\pi},
}
\tag{1.5}
\]

and

\[
\boxed{
A(y,p)-c_{BV}\lambda^2
\le
\frac2{\sqrt3}y^{3/2}\sqrt{2y-p}.
}
\tag{1.6}
\]

For `A>0,m>=0`, define `R_BV(A,m)` as the unique nonnegative root of

\[
\boxed{
(4\pi c_{BV}+1)\lambda^2
+2m\lambda+m^2-4\pi A=0.
}
\tag{1.7}

The root is strictly increasing in `A` and strictly decreasing in `m`.

Define

\[
J_{BV}(y,p):=R_{BV}(A(y,p),p-y)
\tag{1.8}
\]

and

\[
D_{BV}(y,p):=
\sqrt{
\max\left\{0,
\frac{A(y,p)-\frac2{\sqrt3}y^{3/2}\sqrt{2y-p}}{c_{BV}}
\right\}
}.
\tag{1.9}
\]

Every survivor with `lambda<3/5` satisfies

\[
\boxed{
\lambda\ge
M_{BV}(y,p):=\max\{J_{BV}(y,p),D_{BV}(y,p)\}.
}
\tag{1.10}

---

## 2. Fixed-`y` optimizer still lives at or before the RSR crossover

The FSDB/RSR area crossover is unchanged:

\[
\boxed{
p_e(y)=2+2\sqrt{\frac{\Phi(y)}{c_R}}.}
\tag{2.1}
\]

On `p<=p_e(y)`, `A=Phi(y)`.  Hence for fixed `y`:

- `J_BV(y,p)` strictly decreases with `p`, because only `m=p-y` changes and
  `R_BV` decreases in `m`;
- `D_BV(y,p)` strictly increases with `p`, because the DD detour term decreases.

For `p>=p_e(y)`, both functions strictly increase.  For `D_BV` this is immediate:
`Psi(p)` increases and the detour decreases.  For `J_BV`, implicit differentiation of
(1.7) on the RSR-active branch gives a positive derivative whenever

\[
\pi c_R(p-2)>\lambda+p-y.
\tag{2.2}
\]

Exactly as in RSJ, `p>=p_e(y_R)=2y_R>3`, `c_R>2`, and every relevant root satisfies
`lambda<1`.  Hence

\[
\pi c_R(p-2)>2\pi>1+\pi>\lambda+p-y,
\]

so (2.2) holds.

Therefore no fixed-`y` minimizer lies strictly to the right of `p_e(y)`.

---

## 3. The two crossover values move in opposite directions

For `y>=y_R`, put

\[
u(y):=2y-p_e(y)
\tag{3.1}
\]

and

\[
E(y):=
\Phi(y)-\frac2{\sqrt3}y^{3/2}\sqrt{u(y)}.
\tag{3.2}
\]

Define

\[
\boxed{
d_{BV}(y):=
\sqrt{\max\{0,E(y)/c_{BV}\}},}
\tag{3.3}
\]

\[
\boxed{
r_{BV}(y):=
R_{BV}(\Phi(y),p_e(y)-y).}
\tag{3.4}
\]

RX proves directly that `E'(y)<0` on `[y_R,pi/2]`; this calculation is independent
of the attachment coefficient.  Hence `d_BV` strictly decreases until it reaches zero.

The JC crossover value `r_BV` is strictly increasing.  Write

\[
m(y)=p_e(y)-y.
\]

RX/RSJ gives `p_e'(y)<1/2`, so

\[
m'(y)<-1/2.
\tag{3.5}
\]

At the root,

\[
\Phi(y)-c_{BV}r_{BV}(y)^2
=
\frac{(r_{BV}(y)+m(y))^2}{4\pi}.
\tag{3.6}
\]

Differentiate:

\[
\left[
2c_{BV}r_{BV}
+\frac{r_{BV}+m}{2\pi}
\right]r_{BV}'
=
\Phi'(y)-
\frac{(r_{BV}+m)m'}{2\pi}.
\tag{3.7}
\]

The bracket on the left is positive, while the right side is strictly positive because
`Phi'>=0`, `r_BV+m>0`, and `m'<0`.  Thus

\[
\boxed{r_{BV}'(y)>0.}
\tag{3.8}
\]

At `y=y_R`, the detour vanishes, so

\[
d_{BV}(y_R)=\sqrt{\Phi(y_R)/c_{BV}}>r_{BV}(y_R),
\tag{3.9}
\]

because the JC equation has a strictly positive cavity term.  At `y=pi/2`, RX proves
`E(y)<0`, so

\[
d_{BV}(\pi/2)=0<r_{BV}(\pi/2).
\tag{3.10}
\]

Therefore there is a unique

\[
\boxed{y_{BRD}\in(y_R,\pi/2)}
\tag{3.11}
\]

such that

\[
\boxed{d_{BV}(y_{BRD})=r_{BV}(y_{BRD}).}
\tag{3.12}
\]

---

## 4. The pre-transition optimum decreases with `y`

For `y<=y_BRD`, the fixed-`y` optimum is the unique pre-crossover intersection of
JC and DD.  Let its common value be `lambda`, and set

\[
S:=\Phi(y)-c_{BV}\lambda^2>0.
\tag{4.1}
\]

JC and DD equality give exactly

\[
p-y=2\sqrt{\pi S}-\lambda,
\tag{4.2}
\]

\[
2y-p=\frac{3S^2}{4y^3}.
\tag{4.3}
\]

Eliminating `p`, define

\[
\boxed{
F(y,\lambda)
:=y+\lambda-2\sqrt{\pi S}-\frac{3S^2}{4y^3}=0.
}
\tag{4.4}
\]

At fixed `y`,

\[
F_\lambda
=1+
\frac{2c_{BV}\sqrt\pi\,\lambda}{\sqrt S}
+
\frac{3c_{BV}\lambda S}{y^3}>0.
\tag{4.5}
\]

At fixed `lambda`,

\[
F_y
=1-
\frac{\sqrt\pi\,\Phi'(y)}{\sqrt S}
-
\frac{3S\Phi'(y)}{2y^3}
+
\frac{9S^2}{4y^4}.
\tag{4.6}
\]

We give a robust rational lower bound.  The new system is stronger pointwise than RX,
so every crossing value satisfies the already certified

\[
\lambda>299/500.
\tag{4.7}
\]

Also `y>=2rho>147/100>7/5`, and on this interval

\[
\Phi'(y)<7/25.
\tag{4.8}
\]

Since `y<pi/2`,

\[
\Phi(y)<9/14.
\]

Using `pi>3`, hence `c_BV>1199/1600`, and (4.7),

\[
S
<
\frac9{14}
-
\frac{1199}{1600}\left(\frac{299}{500}\right)^2
<\frac38.
\tag{4.9}
\]

Then (4.3) gives

\[
2y-p
<
\frac{3(3/8)^2}{4(7/5)^3}
<\frac1{25}.
\tag{4.10}
\]

Thus

\[
p-y>y-1/25>34/25.
\]

By JC equality,

\[
S=\frac{(\lambda+p-y)^2}{4\pi}
>
\left(\frac{979}{500}\right)^2\frac7{88}
>\frac3{10}.
\tag{4.11}
\]

Now `pi<22/7`, so

\[
\sqrt{\frac\pi S}
<\sqrt{\frac{220}{21}}<\frac{13}{4}.
\]

Discard the final positive term in (4.6).  Using (4.8)--(4.11),

\[
\begin{aligned}
F_y
&>
1-\frac7{25}\frac{13}{4}
-
\frac{3(3/8)(7/25)}{2(7/5)^3}\\
&=
1-\frac{91}{100}-\frac{45}{784}\\
&=\boxed{\frac{639}{19600}>0.}
\end{aligned}
\tag{4.12}
\]

Therefore implicit differentiation of (4.4) gives

\[
\boxed{
\lambda'(y)=-F_y/F_\lambda<0.
}
\tag{4.13}
\]

So the pre-transition optimum strictly decreases with `y`.

---

## 5. Unique global optimizer

Sections 2--4 give the complete picture:

- before `y_BRD`, the fixed-`y` JC/DD crossing exists and its value strictly decreases;
- after `y_BRD`, the fixed-`y` optimum occurs at the area crossover `p=p_e(y)` and
  equals `r_BV(y)`, which strictly increases;
- at `y=y_BRD`, the two branches meet.

Hence the unique global minimum over the enlarged domain is

\[
\boxed{
(y,p)=(y_{BRD},p_e(y_{BRD})).
}
\tag{5.1}

Define

\[
\boxed{
\lambda_{BRD}:=r_{BV}(y_{BRD})=d_{BV}(y_{BRD}).
}
\tag{5.2}

This proves the exact lower bound in BRD.2 except for the displayed rational decimal
certificate.

The exact defining equations are

\[
\boxed{
\Phi(y)=c_R\left(\frac p2-1\right)^2,
}
\tag{5.3}
\]

\[
\boxed{
\Phi(y)-c_{BV}\lambda^2
=\frac{(\lambda+p-y)^2}{4\pi},
}
\tag{5.4}
\]

\[
\boxed{
\Phi(y)-c_{BV}\lambda^2
=\frac2{\sqrt3}y^{3/2}\sqrt{2y-p}.
}
\tag{5.5}
\]

They have the unique solution in

\[
y_R<y<\pi/2,
\qquad
p=p_e(y),
\qquad
0<\lambda<3/5.
\]

---

## 6. Exact `>0.5983` certificate

Take the rational test point

\[
\boxed{y_0=3049/2000=1.5245.}
\tag{6.1}
\]

The companion verifier uses only exact `Fraction` arithmetic, Machin-series bounds for
`pi`, and alternating Taylor bounds for `sin(y_0)`.  It proves

\[
\boxed{
r_{BV}(y_0)>0.5983,}
\tag{6.2}
\]

while also proving

\[
\boxed{
d_{BV}(y_0)>0.5986>r_{BV}(y_0).}
\tag{6.3}
\]

Because `d_BV-r_BV` is strictly decreasing through its unique zero, (6.3) puts
`y_0<y_BRD`.  Since `r_BV` is increasing,

\[
\lambda_{BRD}
=r_{BV}(y_{BRD})
>r_{BV}(y_0)
>0.5983.
\]

This proves BRD.2 with no floating-point dependency.

---

## 7. Numerical orientation

Solving the exact system (5.3)--(5.5) at high precision gives

\[
y_{BRD}=1.5245273793788846893987925837\ldots,
\]

\[
p_{BRD}=3.0231379585040676616950256072\ldots,
\]

and

\[
\lambda_{BRD}=0.5983312494252812288712637313\ldots .
\]

The increase over the previous RSR/DD variational value is approximately

\[
1.77631\times10^{-4}.
\]

Unlike the preceding ND nonattainment epsilon, this increase is fully explicit and
comes from a uniform cellwise geometric defect.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| strengthened JC/DD system | proved | BV attachment coefficient inserted into RD |
| fixed-`y` optimizer at/before `p_e` | proved | opposite monotonicity before crossover; both increase after |
| `d_BV` decreases | proved | RX derivative of coefficient-independent `E(y)` |
| `r_BV` increases | proved | direct implicit derivative (3.7) |
| pre-transition crossing decreases | proved | rational `F_y>639/19600` |
| unique global optimizer | proved | two monotone branches meet once |
| `lambda_BRD>0.5983` | exact rational certificate | companion verifier |
| long decimal in BRD.5 | numerical orientation | not proof dependency |
| Level I | still open | high-surplus survivors above the new floor remain possible |

---

## 9. Next run

Repeat the equality audit at the BRD endpoint.  BV equality would itself require
simultaneous near-equality in Bonnesen's annulus theorem, the support-normal net, the
`d<=3D/5` coefficient relaxation, and the global attachment square concentration.
Because the optimizer has `lambda_BRD<3/5` strictly, the fixed `1/1600` coefficient is
not sharp there.  The next quantitative gain should come from replacing the coarse
`d<=3/5,x<1/20` step in BV by its exact algebraic defect function rather than another
new cavity inequality.