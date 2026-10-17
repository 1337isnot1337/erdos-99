> Generated reading edition · [exact source](../../../docs/reports/target_c_antipodal_area_surplus_floor_2026-09-09.md) · source SHA-256 `0d7a420f7fcd964e6bb364bf1cd9150cf6e50dbe8a3c76dc96891222758270c4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-662E941893F9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — AAS: antipodal force-hull area raises the generic post-ZF surplus floor to 0.5882283437

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-antipodal-force-area`  
**Run type:** exact scalar feasible-region optimization  
**Target:** Target C post-ZF C-II  
**Depends on:** ADA, ZK/GU attachment-cell capacity, JC actual-perimeter cavity capacity, BAS only for a coarse monotonicity bootstrap  
**New external literature:** none  
**Computation:** decimal evaluation only; optimizer and constant are exact

## LEVEL I STATUS

**STILL OPEN.**

ADA proves that if

$$
y:=\lim h/D,
$$

then the force hull of a global minimizer satisfies

$$
\liminf\frac{area(F)}{D^2}
\ge
A_{AD}(y):=\frac{y+\sin y}{4}.
$$

Combining this global disk-limit information with the existing component and cavity ledgers raises the unconditional post-ZF pinned/contact currency substantially.

Put

$$
L:=e_{BB}+2s_C.
$$

### Theorem AAS

Every unbounded post-ZF Target C survivor sequence satisfies

$$
\boxed{
\liminf\frac{L}{D}
\ge\lambda_{AD},
}
\tag{AAS.1}
$$

where `lambda_AD` is the positive root of

$$
\boxed{
(\pi^2+1)\lambda^2
+\pi\lambda
-\frac{\pi^2}{4}-\pi=0.
}
\tag{AAS.2}
$$

Equivalently,

$$
\boxed{
\lambda_{AD}
=
\frac{-\pi+
\sqrt{\pi^2+4(\pi^2+1)(\pi^2/4+\pi)}}
{2(\pi^2+1)}
=0.5882283437736394\ldots .
}
\tag{AAS.3}
$$

In particular the conservative decimal statement

$$
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}>0.58822
}
\tag{AAS.4}
$$

holds.

This supersedes BAS's generic `0.48109619577` floor. It does not supersede RCC/QSG in the special small-response-defect phase, where the slope is at least one.

---

## 1. Generic attachment-cell capacity

Pass to a subsequence on which

$$
\frac LD\to\lambda,
\qquad
\frac hD\to y,
\qquad
\frac{P_F}{D}\to p,
\qquad
\frac{e_{BB}}D\to t.
\tag{1.1}
$$

Here `P_F=per(F)`.

ZK gives

$$
\sum_r\delta_r
\le6-3(d_H+s_Z)+L
\le6+L.
\tag{1.2}
$$

C40 gives

$$
\operatorname{diam}(A_r)\le\delta_r+2.
$$

As in GU/BAS, `c_I=O(D)`, so isodiametry and

$$
\sum_r\delta_r^2
\le\left(\sum_r\delta_r\right)^2
$$

give

$$
\boxed{
\limsup\frac1{D^2}
\sum_r area(\operatorname{conv}A_r)
\le\frac\pi4\lambda^2.
}
\tag{AAS.5}
$$

Therefore the C49 attachment gap

$$
G:=area(F)-\sum_r area(\operatorname{conv}A_r)
$$

satisfies, by ADA,

$$
\boxed{
\liminf\frac G{D^2}
\ge A_{AD}(y)-\frac\pi4\lambda^2.
}
\tag{AAS.6}
$$

---

## 2. JC gives the competing upper capacity

JC before discarding the actual force-hull perimeter gives

$$
\limsup\frac G{D^2}
\le
\frac{(t+\min\{y,p-y\})^2}{4\pi}.
\tag{2.1}
$$

Since `e_BB<=L`,

$$
0\le t\le\lambda.
\tag{2.2}
$$

Also

$$
p\le\pi
$$

by Cauchy's perimeter-diameter inequality, while `p>=y` because `h<=q<=P_F` asymptotically.

For fixed `y`, define

$$
M(y):=\min\{y,\pi-y\}.
\tag{2.3}
$$

Then for every admissible `p`,

$$
\min\{y,p-y\}\le M(y).
$$

Replacing `t` by `lambda` and the actual minimum by `M(y)` only enlarges the upper capacity. Hence every survivor obeys the necessary inequality

$$
\boxed{
A_{AD}(y)-\frac\pi4\lambda^2
\le
\frac{(\lambda+M(y))^2}{4\pi}.
}
\tag{AAS.7}
$$

DB gives

$$
2\rho\le y\le\pi,
\qquad \rho=\cos\rho.
\tag{2.4}
$$

Thus it remains to minimize the positive root of equality in AAS.7 on this compact interval.

---

## 3. The required root decreases up to `pi/2`

For

$$
2\rho\le y\le\pi/2,
$$

we have `M(y)=y`. Define

$$
\Phi(y,\lambda)
:=
\frac{y+\sin y}{4}
-\frac\pi4\lambda^2
-\frac{(\lambda+y)^2}{4\pi}.
\tag{3.1}
$$

For fixed `y`, `Phi` is strictly decreasing in positive `lambda`, so its positive zero is the required lower-bound function.

Its `y` derivative is

$$
\Phi_y
=\frac{1+\cos y}{4}
-\frac{\lambda+y}{2\pi}.
\tag{3.2}
$$

We only need a coarse pre-existing lower bound on `lambda` to fix the sign. BAS gives `lambda>0.481` on every post-ZF survivor. Also

$$
y\ge2\rho>1.47,
\qquad
\cos y\le\cos(2\rho)<0.1.
$$

Therefore

$$
\frac{1+\cos y}{4}<0.275,
$$

while

$$
\frac{\lambda+y}{2\pi}
>
\frac{0.481+1.47}{2\pi}
>0.31.
$$

Hence

$$
\boxed{\Phi_y<0}
\tag{AAS.8}
$$

throughout the lower half. Since `Phi_lambda<0`, implicit differentiation shows that the required root is strictly decreasing on `[2rho,pi/2]`.

The use of BAS here is only a monotonicity bootstrap. Any previous generic floor above about `0.26` would suffice.

---

## 4. The required root increases after `pi/2`

For

$$
\pi/2\le y\le\pi,
$$

we have

$$
M(y)=\pi-y.
$$

Define

$$
\Psi(y,\lambda)
:=
\frac{y+\sin y}{4}
-\frac\pi4\lambda^2
-\frac{(\lambda+\pi-y)^2}{4\pi}.
\tag{4.1}
$$

Then

$$
\Psi_y
=
\frac{1+\cos y}{4}
+
\frac{\lambda+\pi-y}{2\pi}
>0
\tag{4.2}
$$

for `y<pi`; at the endpoint the limiting statement is harmless. Again `Psi_lambda<0`, so the positive root is strictly increasing on `[pi/2,pi]`.

Therefore the global minimum occurs exactly at

$$
\boxed{y=\pi/2.}
\tag{AAS.9}
$$

---

## 5. Exact optimizer and constant

At `y=pi/2`,

$$
A_{AD}(\pi/2)
=\frac{\pi+2}{8},
\qquad
M(\pi/2)=\frac\pi2.
$$

Equality in AAS.7 becomes

$$
\frac{\pi+2}{8}
-\frac\pi4\lambda^2
=
\frac{(\lambda+\pi/2)^2}{4\pi}.
\tag{5.1}
$$

Multiplying by `4pi` and rearranging gives AAS.2:

$$
(\pi^2+1)\lambda^2
+\pi\lambda
-\frac{\pi^2}{4}-\pi=0.
$$

The positive root is AAS.3. Monotonicity on both sides of `pi/2` proves AAS.1.

---

## 6. Near-equality normal form

If a post-ZF sequence approaches the new AAS floor, every relaxation used above must approach equality. In particular:

$$
\boxed{h/D\to\pi/2.}
\tag{AAS.10}
$$

The JC angular capacity must satisfy

$$
\min\{y,p-y\}\to\pi/2,
$$

so

$$
\boxed{P_F/D\to\pi.}
\tag{AAS.11}
$$

Also `t<=lambda` must be tight, hence

$$
\boxed{s_C=o(D),\qquad e_{BB}/D\to\lambda_{AD}.}
\tag{AAS.12}
$$

ADA equality additionally requires the limiting projective diameter-direction set to be one interval of measure `pi/2`, up to null sets, and the force-hull limit to contain the corresponding two antipodal semicircular quarter-arcs.

But AAS.11 says the force-hull perimeter tends to the maximum `pi D`. By the equality stability of Cauchy's perimeter-diameter inequality, any Hausdorff limit with diameter one and perimeter `pi` is a constant-width-one body; combined with the ambient source-hull disk limit, the only possible limit is the radius-`1/2` disk.

Thus a true AAS threshold sequence would in fact have force-hull area tending to `pi/4`, strictly larger than the ADA equality value `(pi+2)/8`. This indicates that AAS.1 is itself not sharp: the scalar threshold is unattainable. A quantitative version of this perimeter/area stability should raise the constant further.

This nonattainment observation is not needed for AAS.1 and is not promoted here as a numerical improvement.

---

## 7. Regression audit

- AAS uses the full-source disk limit only through ADA; no finite source hull is assumed circular.
- The generic attachment-cell subtraction is retained. AAS does not assume the SCC near-zero collapse.
- JC is weakened by replacing the actual `t` by `lambda` and the actual perimeter split by `M(y)`; this can only make the lower bound weaker.
- The optimizer `y=pi/2` is proved analytically, not found by numerical search.
- The floor does not conflict with RCC/QSG. In the response-defect phase those stronger theorems give slope at least one.
- The AAS equality discussion exposes an additional incompatibility but does not claim an explicit gap without a stability estimate.

---

## 8. Next target

The AAS near-equality form forces simultaneously

$$
h/D\to\pi/2,
\qquad
P_F/D\to\pi,
$$

while the global source hull itself converges to the disk.

This makes the next theorem especially simple in principle: quantify the fact that a diameter-one convex body with perimeter `pi-o(1)` has area close to `pi/4`. Any explicit perimeter-area stability inserted into AAS.6 removes the artificial ADA equality shape and raises the `0.588228...` slope.

The repository already contains Groemer/Bonnesen stability tools for near-maximal perimeter; they should be reusable here without new literature.

## 9. Compact handoff

```text
AAS:
Let lambda=(e_BB+2s_C)/D and y=h/D along a post-ZF subsequence.
ADA gives
    area(F)/D^2 >= (y+sin y)/4.
ZK/C40/isodiametry give attachment-cell area <=(pi/4)lambda^2 D^2+o(D^2).
JC gives cavity upper <=(t+min(y,p-y))^2/(4pi), with t<=lambda, p<=pi.
Therefore
    (y+sin y)/4-(pi/4)lambda^2
      <=(lambda+min(y,pi-y))^2/(4pi).
For y<=pi/2, the required root decreases with y; BAS>0.481 gives a simple strict
derivative sign. For y>=pi/2 the root increases. Minimum is y=pi/2.
At y=pi/2:
    (pi+2)/8-(pi/4)lambda^2=(lambda+pi/2)^2/(4pi),
so
    (pi^2+1)lambda^2+pi lambda-pi^2/4-pi=0.
Positive root:
    lambda_AD=0.5882283437736394....
Thus generic post-ZF
    liminf (e_BB+2s_C)/D >= lambda_AD.
Near equality forces y->pi/2 and p->pi, so the bound is itself not sharp.
```
