> Generated reading edition · [exact source](../../../docs/reports/target_c_coupled_diameter_train_defect_floor_2026-09-11.md) · source SHA-256 `81d4aa84c36b030d353e5d03a91821c5ebfa10824453b1db7355e520e84490cc`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-0DAAC3FE2AD4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — coupling diameter density to the all-ZF train capacity

**Date:** 2026-09-11  
**Run type:** exact all-branch quantitative reduction  
**Target:** Target C C-II, including `s_Z>0` and contact-isolated source points  
**Status:** unpromoted research report; no route-map status is changed

## LEVEL I STATUS

`STILL OPEN`.

The all-ZF full-source cell-slack argument can be sharpened by retaining the same
quantity (k=d_H+s_Z) in both the stopped-train count and the diameter-edge count.
The earlier defect-floor estimate bounded the force-hull area below by the universal
FSDB constant and bounded the train count using only $`q\le\pi D`$.  The exact
identities instead give, for (r=(x_B+Q)/D),

```math
 \frac hD\ge r+k,
 \qquad
 \frac TD\le r+k+2\frac QD,
 \qquad
 r+2k=\frac qD\le\pi .
```

Because the difference between the resulting area upper and lower bounds is
increasing in (k), one may use the extremal value (k=(\pi-r)/2) in the
feasibility test.  This yields the stronger necessary condition

```math
 \boxed{\liminf_{D\to\infty}\frac{x_B+Q}{D}\ge
 \varepsilon_{\rm coup}=0.0649446778\ldots .}
```

Thus the report-level all-branch floor rises from (0.0476412\ldots) to
(0.0649446\ldots).  The result still leaves a linear-defect regime and does not
settle C-II.

The proof is conditional only on the already stated report-level FSDB area lower
bound and the full-source FSCS/face-pocket area upper decomposition.  It uses no
(s_Z=0) identity, no diameter-topology specialization, and no assumption that
isolated source points are diametral.

## 1. Exact variables and the target contradiction

Let (F) be the actual force hull, (D) its source diameter, (x=x_B) the
outer-walk excess, (Q) the total bounded-face degree defect, (f) the number of
exceptional bounded faces, and (R) the number of strict quadrilateral faces.  Put

```math
 a_0=\frac{\sqrt3}{2},
 \qquad X=\frac{x}{D},\qquad Y=\frac QD,
 \qquad r=X+Y.
```

Let

```math
 k=\frac{d_H+s_Z}{D},
 \qquad y=\frac hD,
 \qquad q_0=\frac qD,
 \qquad t=\frac TD.
```

The exact post-ZF identities, valid in all three diameter/topology branches, are

```math
 q=x+Q+2(d_H+s_Z),
 \tag{C.1}
```

```math
 T=q-(d_H+s_Z)+2f.
 \tag{C.2}
```

Consequently

```math
 q_0=r+2k,
 \qquad y=r+\frac{d_H}{D}+2\frac{s_Z}{D}
       \ge r+k.
 \tag{C.3}
```

The loaded vertices are vertices of a convex diameter-(D) polygon, so their
unit-separated consecutive sides give $`q\le\operatorname{per}F\le\pi D`$.  Hence

```math
 0\le r\le\pi,
 \qquad 0\le k\le \frac{\pi-r}{2}.
 \tag{C.4}
```

Since (f\le Q), (C.2) gives

```math
 t\le r+k+2Y.
 \tag{C.5}
```

The strict-rhombus train crossing graph is triangle-free.  Mantel and the FSCS
cell-slack theorem therefore give

```math
 \limsup \frac{\operatorname{area}F_{\rm quad}}{D^2}
 \le \frac{a_0}{4}(r+k+2Y)^2.
 \tag{C.6}
```

The full-source outer-pocket and exceptional-face estimates are

```math
 \limsup\frac{A_{\rm out}}{D^2}\le\frac{9X^2}{\pi},
 \qquad
 \limsup\frac{A_{\rm exc}}{D^2}\le\frac{Y^2}{4\pi}.
 \tag{C.7}
```

Thus every finite normalized subsequential limit satisfies

```math
 \frac{\operatorname{area}F}{D^2}
 \le V_r(k,X,Y):=
 \frac{a_0}{4}(r+k+2Y)^2+\frac{9X^2}{\pi}+\frac{Y^2}{4\pi}.
 \tag{C.8}
```

FSDB gives the diameter-density-sensitive lower bound

```math
 \liminf\frac{\operatorname{area}F}{D^2}
 \ge \Phi(y):=\frac{y+\sin y}{4}.
 \tag{C.9}
```

Here $`0\le y\le\pi`$, because $`h\le q\le\pi D`$, and $`\Phi`$ is increasing on
$`[0,\pi]`$.  The exact contradiction target is therefore

```math
 \Phi(y)\le V_r(k,X,Y).
 \tag{C.10}
```

## 2. Eliminate the hidden defect (k) without relaxing the two ledgers independently

Fix (r,X,Y) and write (z=r+k).  The right side of (C.8) is increasing in (k).
The lower bound (C.9), using (C.3), is at least

```math
 \Phi(\max\{2\rho,z\}),
 \qquad \rho=\cos\rho,
 \tag{C.11}
```

where (2\rho) is the independent DB lower endpoint for (h/D).  The difference

```math
 V_r(k,X,Y)-\Phi(\max\{2\rho,r+k\})
 \tag{C.12}
```
is strictly increasing in (k) throughout the allowed interval (C.4).  Indeed,
when (r+k<2\rho), the second term is constant.  When (r+k\ge2\rho), its
derivative is

```math
 \Phi'(r+k)=\frac{1+\cos(r+k)}4\le\frac{1+\cos(2\rho)}4<\frac12,
 \tag{C.13}
```

whereas the derivative of the quadrilateral term is

```math
 \frac{a_0}{2}(r+k+2Y)
 \ge \frac{a_0\rho}{1}>\frac12.
 \tag{C.14}
```

The last strict inequality follows from (a_0\rho>0.866\cdot0.739>1/2).
Thus feasibility at some (k) implies feasibility at the largest allowed value

```math
 k_{\max}=\frac{\pi-r}{2}.
 \tag{C.15}
```

At this value,

```math
 z_{\max}=r+k_{\max}=\frac{\pi+r}{2}\ge\frac\pi2>2\rho,
 \tag{C.16}
```

so (C.10) implies the single necessary inequality

```math
 \boxed{
 L(r):=\frac{(\pi+r)/2+\sin((\pi+r)/2)}4
 \le
 \frac{a_0}{4}\left(\frac{\pi+r}{2}+2Y\right)^2
 \frac{9X^2}{\pi}+\frac{Y^2}{4\pi}.}
 \tag{C.17}
```

This is the point of the coupling: the (k) that maximizes train capacity also
raises the FSDB lower area, and the monotonicity check proves that taking its maximum
does not create an invalid independent relaxation.

## 3. Optimize the split (r=X+Y)

For fixed (r), the right side of (C.17) is a convex quadratic function of (X),
with (Y=r-X).  Hence its maximum on (0\le X\le r) is attained at an endpoint.
The endpoint values are

```math
 V_0(r)=\frac{a_0}{4}\left(\frac{\pi+r}{2}+2r\right)^2+\frac{r^2}{4\pi}
 \tag{C.18}
```

for (X=0,Y=r), and

```math
 V_1(r)=\frac{a_0}{4}\left(\frac{\pi+r}{2}\right)^2+\frac{9r^2}{\pi}
 \tag{C.19}
```

for (X=r,Y=0).  For (0\le r\le1/10),

```math
 V_0(r)-V_1(r)
 =r\left[
 a_0\frac{\pi+r}{2}
 +\left(a_0-\frac{35}{4\pi}\right)r
 \right]>0.
 \tag{C.20}
```

For example, $`a_0\pi/2>1`$, $`a_0-35/(4\pi)>-2`$, and the bracket is therefore
greater than $`1-1/5>0`$.  Hence the relaxed right side in (C.17) is at most

```math
 U(r):=V_0(r)
 =\frac{\sqrt3}{8}\left(\frac{\pi+r}{2}+2r\right)^2+\frac{r^2}{4\pi}
 \tag{C.21}
```

for $`0\le r\le1/10`$.

The function (U(r)-L(r)) is strictly increasing on this interval.  The derivative
of (U) is at least

```math
 \frac{5a_0}{4}\frac\pi2>1,
 \tag{C.22}
```

while (L'(r)=(1+\cos((\pi+r)/2))/8\le1/8).  Also

```math
 U(0)=\frac{\sqrt3\pi^2}{32}<\frac{\pi/2+1}{4}=L(0),
 \tag{C.23}
```

and direct rational bounds $`3.14<\pi<22/7`$, $`0.866<\sqrt3/2`$, and
$`\sin(1.62)>0.998`$ give $`U(1/10)>L(1/10)`$.  Therefore there is a unique

```math
 \varepsilon_{\rm coup}\in(0,1/10)
 \tag{C.24}
```

defined by (U(\varepsilon_{\rm coup})=L(\varepsilon_{\rm coup})).  Evaluation of
this one-variable equation gives

```math
 \varepsilon_{\rm coup}=0.0649446778592\ldots .
 \tag{C.25}
```

If a subsequence had $`r<\varepsilon_{\rm coup}`$, (C.17)--(C.21) would give

```math
 L(r)>U(r)\ge V_r(k,X,Y),
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
contradicting FSDB.  If (r\) is unbounded there is nothing to prove.  Hence
```



```math
 \boxed{\liminf_{D\to\infty}\frac{x_B+Q}{D}
 \ge\varepsilon_{\rm coup}.}
 \tag{C.26}
```

## 4. Branch and regression audit

* **(s_Z>0):** retained through (k=(d_H+s_Z)/D); no circuit-phase identity is
  used.
* **Cyclic and forest diameter topology:** both use only (C.1)--(C.4); no Woodall
  branch is selected.
* **Contact-isolated source points:** retained by the full-source FSCS partition and
  the FSDB lower bound.  No isolate is declared a diameter endpoint.
* **Exceptional faces:** their full quadratic capacity (Y^2/(4\pi)) is retained;
  the optimization deliberately allows all defect to be exceptional-face defect.
* **Repeated outer-walk edges and pockets:** the (9X^2/\pi) estimate is retained;
  no pure-disk transport is used.
* **Odd shells:** not excluded.  Their possible linear defect is compatible with
  (C.26), as required.
* **Near-equilateral rhombi:** the FSCS (O(D)) slack remains; no positive angular
  gap is assumed.

## 5. Exact surviving obstruction

The coupling removes the sub-(0.06494D) defect regime in every post-ZF branch, but
it does not provide an upper bound on (x_B+Q), nor does it contradict a source with
linear exceptional-face or outer-pocket capacity.  The unresolved alternatives remain

```math
 x_B+Q=\Theta(D),
 \qquad s_Z=0\text{ cyclic or forest},
 \qquad\text{or }s_Z>0,
```

with all contact-isolated population retained.  A Level-I proof still needs a global
response/competitor theorem or a reverse full-source slack inequality strong enough to
overcome that linear capacity.
