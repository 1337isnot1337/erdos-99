<!-- theorem-state: {"artifact_id":"ART-9D4C00332382","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — support-area/JC raises the explicit post-ZF floor to 0.590643

**Date:** 2026-09-10  
**Branch base:** `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Depends on:** FSDB, DB, FD/JC actual-perimeter cavity bound, SA on this branch  
**Run type:** exact compact optimization  
**Target:** Target C, C-II after ZF  
**External input:** none  
**Computation:** decimal evaluation only; exact implicit constants are the theorem

## LEVEL I STATUS

`STILL OPEN`.

The SA theorem strictly dominates the QPD perimeter-dependent area floor.  Re-running
the exact QJ optimization with

\[
\Xi(p)=\frac{p\alpha(p)}4
\]

raises the explicit post-ZF pinned/contact floor to

\[
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{SA}
=0.5906428373093669\ldots .
}
\tag{SJ.1}
\]

The optimizing scalar state is

\[
\boxed{
y_*=1.5354681179195452\ldots,
\qquad
p_*=2y_*=3.0709362358390904\ldots .
}
\tag{SJ.2}
\]

Thus the explicit report-level floor has moved

\[
0.5882283437736394\ldots
\quad\longrightarrow\quad
0.5894611562694627\ldots
\quad\longrightarrow\quad
0.5906428373093669\ldots
\]

through two independently proved perimeter/area refinements.  The decimal values are
not proof dependencies.

---

## 1. Necessary inequality

Along a convergent post-ZF subsequence write

\[
\lambda=\lim\frac{e_{BB}+2s_C}{D},
\qquad
y=\lim\frac hD,
\qquad
p=\lim\frac{\operatorname{per}F}{D}.
\]

The retained feasible region is

\[
\boxed{
2\rho\le y\le\pi,
\qquad
g(y):=y+2\cos(y/2)\le p\le\pi.
}
\tag{1.1}
\]

FSDB and SA give

\[
\boxed{
A(y,p):=
\max\left\{
\Phi(y),\Xi(p)
\right\}
\le
\liminf\frac{\operatorname{area}F}{D^2},
}
\tag{1.2}
\]

where

\[
\Phi(y)=\frac{y+\sin y}{4}.
\tag{1.3}
\]

The actual-perimeter JC inequality gives

\[
A(y,p)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m)^2}{4\pi},
\qquad
m:=\min\{y,p-y\}.
\tag{1.4}
\]

Equivalently

\[
(\pi^2+1)\lambda^2+2m\lambda+m^2-4\pi A(y,p)\ge0.
\tag{1.5}
\]

Let

\[
R(A,m)=
\frac{\sqrt{4\pi(\pi^2+1)A-\pi^2m^2}-m}{\pi^2+1}
\tag{1.6}
\]

be the positive threshold root.  As in QJ,

\[
\frac{\partial R}{\partial A}>0,
\qquad
\frac{\partial R}{\partial m}<0.
\tag{1.7}
\]

Thus the problem is to minimize

\[
R(A(y,p),\min\{y,p-y\})
\]

over the compact region (1.1).

---

## 2. FSDB/SA crossover

For every `y in [2rho,pi)`, SA proves

\[
\Xi(g(y))
=\frac14\left[y\sin(y/2)+\sin y\right]
<
\frac{y+\sin y}{4}
=\Phi(y).
\tag{2.1}
\]

Also `Xi(pi)=pi/4>Phi(y)` for `y<pi`.  Since `Xi` is strictly increasing, there is a
unique crossover

\[
\boxed{
c(y)\in(g(y),\pi)
\quad\text{with}\quad
\Xi(c(y))=\Phi(y).
}
\tag{2.2}
\]

Set `c(pi)=pi`.

SA gives the uniform derivative bound

\[
\Xi'(p)>\frac{17}{24}>\frac12
\tag{2.3}
\]

throughout the post-ZF perimeter range, while

\[
\Phi'(y)=\frac{1+\cos y}{4}\le\frac12.
\]

Hence

\[
\boxed{
0\le c'(y)
=\frac{\Phi'(y)}{\Xi'(c(y))}<1.
}
\tag{2.4}
\]

---

## 3. Fixed-`y` perimeter optimization

The proof of QJ Section 3 uses only the following properties of its perimeter-area
function:

1. it is strictly increasing;
2. its derivative is greater than `1/2` on the feasible range;
3. it is below `Phi(y)` at `p=g(y)` and crosses `Phi(y)` once.

SA proves all three for `Xi`, with the stronger derivative margin (2.3).  For
completeness, the key derivative after the crossover is

\[
\frac d{dp}R(\Xi(p),p-y)
=
\frac{2\pi\Xi'(p)-(R+m)}{(\pi^2+1)R+m}
\tag{3.1}
\]

whenever `p<2y`.  Since `A<=pi/4`, every positive threshold root has `R<1`; and
`p<2y` gives `m<=pi/2`.  Therefore

\[
2\pi\Xi'(p)
>
\frac{17\pi}{12}
>
1+\frac\pi2
>R+m,
\tag{3.2}
\]

so (3.1) is positive.

It follows that, for fixed `y`:

- if `c(y)>=2y`, the minimum threshold is `R(Phi(y),y)`;
- if `c(y)<2y`, the unique minimum is attained at `p=c(y)` and equals
  `R(Phi(y),c(y)-y)`.

No floating-point optimization is used.

---

## 4. Unique transition

At `y=2rho`, the equation `rho=cos rho` gives

\[
g(2\rho)=4\rho=2(2\rho).
\]

Equation (2.1) therefore gives

\[
c(2\rho)>2(2\rho).
\tag{4.1}
\]

At `y=pi/2`, `2y=pi` and

\[
\Xi(\pi)=\frac\pi4>\Phi(\pi/2),
\]

so

\[
c(\pi/2)<2(\pi/2).
\tag{4.2}
\]

Because `c'(y)<1`, the function `c(y)-2y` is strictly decreasing.  Hence there is a
unique

\[
\boxed{
y_*\in(2\rho,\pi/2)
\quad\text{such that}\quad
c(y_*)=2y_*.
}
\tag{4.3}
\]

Equivalently,

\[
\boxed{
\Xi(2y_*)=\Phi(y_*).
}
\tag{4.4}
\]

This is the exact definition of `y_*`.

If

\[
a_*:=\alpha(2y_*),
\]

then (4.4) can also be written

\[
\boxed{
2y_*a_*=y_*+\sin y_*,
\qquad
 y_*=\arcsin a_*+\sqrt{1-a_*^2}.
}
\tag{4.5}
\]

---

## 5. Global minimization

For `2rho<=y<=y_*`, the fixed-`y` optimum is

\[
M_-(y)=R(\Phi(y),y).
\]

This is exactly the left FSJC threshold.  The strict derivative argument already
proved in FSJC and reused in QJ gives

\[
M_-'(y)<0.
\tag{5.1}
\]

For `y_*<=y<=pi`, the fixed-`y` optimum is

\[
M_+(y)=R(\Phi(y),c(y)-y).
\]

Here `Phi(y)` increases and, by (2.4),

\[
(c(y)-y)'<0.
\]

Since `R` increases with its first argument and decreases with its second,

\[
M_+(y)\text{ is strictly increasing}.
\tag{5.2}
\]

Therefore the global minimum occurs exactly at

\[
y=y_*,
\qquad
p=c(y_*)=2y_*.
\tag{5.3}
\]

Define

\[
\boxed{
\lambda_{SA}:=R(\Phi(y_*),y_*).
}
\tag{5.4}
\]

Then every post-ZF subsequential limit satisfies

\[
\lambda\ge\lambda_{SA},
\]

proving SJ.1.

Equivalently, `lambda_SA` is the positive root of

\[
\boxed{
(\pi^2+1)\lambda^2
+2y_*\lambda
+y_*^2
-\pi(y_*+\sin y_*)=0.
}
\tag{5.5}
\]

Since `y_*<pi/2` and the FSJC left threshold decreases strictly toward
`lambda_FSJC` as `y` approaches `pi/2`, the strict improvement

\[
\lambda_{SA}>\lambda_{FSJC}
\]

is exact and does not depend on the displayed decimals.

---

## 6. Numerical orientation

High-precision evaluation of the exact implicit system gives

\[
y_*=1.53546811791954519242\ldots,
\]

\[
a_*=0.82543040525152030207\ldots,
\]

\[
\Phi(y_*)=\Xi(2y_*)
=0.63371103541255967521\ldots,
\]

and

\[
\boxed{
\lambda_{SA}
=0.59064283730936696903\ldots .
}
\]

The numerical increase over FSJC is

\[
0.0024144935357275\ldots .
\]

---

## 7. Endpoint localization

Any sequence approaching equality in SJ.1 must satisfy

\[
\boxed{
\frac hD\to y_*,
\qquad
\frac{\operatorname{per}F}{D}\to2y_*.
}
\tag{7.1}
\]

Because the two area floors cross at the optimizer,

\[
\boxed{
\frac{\operatorname{area}F}{D^2}
\to
\Phi(y_*)=\Xi(2y_*)
}
\tag{7.2}
\]

is necessary for scalar equality: any fixed positive area excess would make the gap
lower bound exceed the JC cavity upper bound at `lambda_SA`.

The `t<=lambda` relaxation in JC must also saturate, so

\[
\boxed{
\frac{s_C}{D}\to0.
}
\tag{7.3}
\]

Finally `p=2y` balances the two exact JC perimeter branches:

\[
y=p-y.
\tag{7.4}
\]

This endpoint is now the shortest structural target.  In particular, SA equality
requires the central symmetral to become asymptotically tangential to its centered
inball on essentially all of its perimeter, while QPA perimeter saturation forces a
specific disk-and-strip support profile.  Those conditions need not be compatible.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| FSDB/SA feasible system | proved | existing FSDB/DB/JC plus SA |
| unique crossover `c(y)` | proved | SA boundary identity and monotonicity |
| `c'(y)<1` | proved | `Xi'>17/24`, `Phi'<=1/2` |
| fixed-`y` optimum | proved | QJ argument with stronger SA derivative |
| unique global transition `y_*` | proved | endpoint signs + `c'-2<0` |
| explicit exact floor `lambda_SA` | proved asymptotically | exact compact minimization |
| decimals | numerical orientation only | not proof dependencies |
| Level I | still open | endpoint structural incompatibility not yet proved |

---

## 9. Next run

Audit simultaneous near-equality in QPA's strip perimeter envelope and SA's support
triangulation at the localized state (7.1)--(7.4).  If exact equality would force two
incompatible limit bodies, compactness excludes the `lambda_SA` endpoint and yields a
new nonexplicit gap.  A quantitative stability version would produce another explicit
increase and is preferable if it can be obtained without importing heavy convex-body
stability machinery.
