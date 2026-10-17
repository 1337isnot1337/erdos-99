> Generated reading edition · [exact source](../../../docs/reports/target_c_density_sensitive_pi_jc_surplus_2026-09-09.md) · source SHA-256 `02bbf2851c904142d16cf8b1b7c6f4687f15d9e29571491a243966dd98a6ceaf`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 21 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-B7A756568D7D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — DJC: diameter-density-sensitive PI/JC coupling raises the post-ZF surplus floor

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-density-sensitive-cavity`  
**Base:** `cf790155660ad46797e53c7f44371b078f7eab7b`  
**Run type:** exact asymptotic feasible-region optimization  
**Target:** Target C C-II after ZF/DB/PI/JC  
**Depends on:** PI exact diameter-density area floor, JC density-sensitive joint cavity bound, GU/ZG attachment-gap charging, DB only for the lower range of `h/D`  
**New external literature:** none  
**Computation:** decimal evaluation only; the minimizer and inequality are analytic

## LEVEL I STATUS

**STILL OPEN.**

JC records a diameter-density-sensitive cavity inequality but retains PI's universal area constant `A_PI`, obtained by replacing the actual diameter-edge density by its DB lower bound. PI itself is stronger: its exact area floor depends monotonically on the actual density `h/D` until the projective angle reaches `pi/2`.

Keeping the same density variable in **both** estimates gives a one-dimensional feasible-region problem whose worst case occurs exactly at

```math
\frac hD\to\frac\pi2.
```

This raises the unconditional post-ZF pinned/contact surplus floor to

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{DJC}
=0.4653518453960140852\ldots .
}
\tag{DJC.1}
```

This is stronger than

- JC: `0.4633168953789...`;
- GS on current main: `0.464792250394...`; and
- the separately optimized GS split: `0.464797445655...`.

No new convex-stability input is needed.

---

## 1. Subsequence parameters

Assume an unbounded post-ZF survivor sequence. Pass to a subsequence on which

```math
y:=\lim\frac hD,
\qquad
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
\qquad
t:=\lim\frac{e_{BB}}D
\tag{1.1}
```

exist.

The diameter-thrackle and force-hull perimeter bounds give

```math
h\le q\le\pi D,
```

while DB gives

```math
\liminf\frac hD\ge2\rho,
\qquad
\rho=\cos\rho=0.7390851332\ldots .
```

Hence

```math
\boxed{2\rho\le y\le\pi.}
\tag{DJC.2}
```

Also

```math
\boxed{0\le t\le\lambda.}
\tag{DJC.3}
```

---

## 2. PI with the actual diameter density

PI gives the exact finite force-hull area bound

```math
\operatorname{area}(F)
\ge
\frac{D^2}{2}
\sin\left(
\min\left\{
(h-1)\delta_D,
\frac\pi2-\delta_D
\right\}
\right),
\tag{2.1}
```

where

```math
\delta_D=2\arcsin\frac1{2D},
\qquad
D\delta_D\to1.
```

Therefore along the subsequence (1.1),

```math
\boxed{
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge A(y),
}
\tag{DJC.4}
```

with

```math
\boxed{
A(y):=
\begin{cases}
\frac12\sin y,&2\rho\le y\le\frac\pi2,\\[4pt]
\frac12,&\frac\pi2\le y\le\pi.
\end{cases}}
\tag{DJC.5}
```

The universal PI constant is merely `A(2rho)`.

GU's attachment-cell area upper bound is unchanged:

```math
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le
\frac\pi4\lambda^2D^2+o(D^2).
```

Thus the attachment gap satisfies

```math
\boxed{
\liminf\frac GD^2
\ge
A(y)-\frac\pi4\lambda^2.
}
\tag{DJC.6}
```

---

## 3. JC with the same density variable

JC proves the density-sensitive joint cavity capacity

```math
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le
\frac{(t+\min\{y,\pi-y\})^2}{4\pi}.
\tag{3.1}
```

ZG/GU differs from this cavity area by only `O(D)` when bounding `G`. Hence

```math
\boxed{
\limsup\frac GD^2
\le
\frac{(t+m(y))^2}{4\pi},
}
\tag{DJC.7}
```

where

```math
\boxed{m(y):=\min\{y,\pi-y\}.}
\tag{DJC.8}
```

Because `t<=lambda` and the right side increases in `t`, every survivor must satisfy the weaker but one-parameter necessary inequality

```math
\boxed{
A(y)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m(y))^2}{4\pi}.
}
\tag{DJC.9}
```

For each fixed `y`, the left-minus-right side is strictly decreasing in `lambda>=0`, so DJC.9 is equivalent to

```math
\lambda\ge\Lambda(y),
\tag{3.2}
```

where `Lambda(y)` is its unique positive root.

---

## 4. The root decreases up to `pi/2`

For

```math
2\rho\le y\le\frac\pi2,
```

we have

```math
A(y)=\frac12\sin y,
\qquad
m(y)=y.
```

Define

```math
F(y,\lambda)
:=
\frac12\sin y
-\frac\pi4\lambda^2
-\frac{(\lambda+y)^2}{4\pi}.
\tag{4.1}
```

The root is characterized by

```math
F(y,\Lambda(y))=0.
```

For all `lambda>=0`,

```math
\frac{\partial F}{\partial y}
=
\frac12\cos y
-\frac{\lambda+y}{2\pi}
\le
\frac12\cos y-\frac y{2\pi}.
\tag{4.2}
```

On the whole interval `y>=2rho=1.47817...`, the final expression is strictly negative. For example the elementary function

```math
g(y)=y-\pi\cos y
```

is strictly increasing for `y>0` and already positive at `y=4/3`; while `2rho>4/3`. Hence

```math
\boxed{F_y<0.}
\tag{DJC.10}
```

Also

```math
F_\lambda
=-\frac\pi2\lambda-rac{\lambda+y}{2\pi}<0.
```

Implicit differentiation gives

```math
\Lambda'(y)=-\frac{F_y}{F_\lambda}<0.
```

Therefore

```math
\boxed{
\Lambda(y)\text{ is strictly decreasing on }[2\rho,\pi/2].
}
\tag{DJC.11}
```

---

## 5. The root increases after `pi/2`

For

```math
\frac\pi2\le y\le\pi,
```

we have

```math
A(y)=\frac12,
\qquad
m(y)=\pi-y.
```

Put

```math
F(y,\lambda)
:=
\frac12
-\frac\pi4\lambda^2
-\frac{(\lambda+\pi-y)^2}{4\pi}.
\tag{5.1}
```

Then

```math
F_y
=
\frac{\lambda+\pi-y}{2\pi}>0
\tag{5.2}
```

for the positive root, while again `F_lambda<0`. Hence

```math
\boxed{
\Lambda'(y)>0
\quad(\pi/2\le y\le\pi).
}
\tag{DJC.12}
```

Thus the unique global minimum of the required surplus root on the entire allowed density interval is attained at

```math
\boxed{y=\frac\pi2.}
\tag{DJC.13}
```

This is the key point missed by replacing the density-sensitive JC term by `pi/2` while simultaneously freezing PI at its DB endpoint value.

---

## 6. Exact optimized constant

At

```math
y=\frac\pi2,
```

DJC.9 becomes

```math
\frac12-\frac\pi4\lambda^2
\le
\frac{(\lambda+\pi/2)^2}{4\pi}.
\tag{6.1}
```

Equality is

```math
\boxed{
(\pi^2+1)\lambda^2
+\pi\lambda
+\frac{\pi^2}{4}
-2\pi
=0.
}
\tag{DJC.14}
```

Its positive root is

```math
\boxed{
\lambda_{DJC}
=
\frac{
-\pi+
\sqrt{\pi^2-4(\pi^2+1)(\pi^2/4-2\pi)}
}{2(\pi^2+1)}.
}
\tag{DJC.15}
```

Numerically,

```math
\boxed{
\lambda_{DJC}
=0.4653518453960140852136767671\ldots .
}
\tag{DJC.16}
```

Since every convergent subsequence of the normalized surplus has limit at least this value, we obtain DJC.1.

---

## 7. Comparison with the current constants

The current explicit floors are

```math
\lambda_{JC}=0.4633168953789\ldots,
```

```math
\lambda_{GS}=0.464792250394\ldots .
```

The optimized Groemer split separately gives

```math
\lambda_{GS2}=0.464797445655\ldots .
```

DJC improves on all three:

```math
\boxed{
\lambda_{DJC}-\lambda_{GS}
=5.59595002\times10^{-4}\text{ approximately}.
}
\tag{DJC.17}
```

Unlike GS, DJC imports no quantitative stability theorem beyond the already-audited PI/JC stack.

---

## 8. Structural meaning of the optimizer

The hardest density is not the DB minimum `2rho` and not a very dense diameter graph. It is the transition

```math
\frac hD\approx\frac\pi2.
```

Below `pi/2`, increasing diameter density raises PI's force-hull area floor faster than it enlarges the joint cavity allowance, so the required pinned/contact currency decreases.

Above `pi/2`, PI has saturated at the maximal two-diameter area floor `D^2/2`, while the complementary JC perimeter term `pi-y` shrinks. The required currency therefore rises again.

Any sequence approaching the new scalar floor must consequently satisfy

```math
\boxed{
\frac hD\to\frac\pi2
}
\tag{DJC.18}
```

if all inequalities used in DJC are asymptotically tight. This gives a sharper extremal regime for the next structural attack.

---

## 9. Regression audit

### DB-endpoint density

At `y=2rho`, the density-sensitive PI/JC root is strictly larger than DJC.16, so the old worst-case relaxation was not sharp.

### Very high diameter density

For `y>pi/2`, PI saturates at `1/2`, but JC's complementary term `pi-y` decreases. Such sequences require more, not less, pinned/contact surplus.

### Regular odd shells

They remain compatible. DJC is a necessary currency inequality, not a claim that high loaded-shell contact density alone is impossible.

### Use of `t<=lambda`

This is the only relaxation eliminating the direct loaded-contact proportion. If `s_C` carries a substantial fraction of `lambda`, the exact two-parameter bound is stronger.

### No density/count confusion

`y` is introduced only after passing to a subsequence with `h/D` convergent. PI's finite angle bound is taken to the limit using `D delta_D ->1`.

---

## 10. Classification

**Status:** proved asymptotic refinement of the existing PI/JC feasible-region argument.  
**Level I:** still open.  
**New external literature:** none.  
**Computation:** only decimal evaluation of the explicit quadratic root.

## 11. Next target

The surviving post-ZF feasible region now satisfies

```math
\frac{e_{BB}+2s_C}{D}
\ge0.465351845396014\ldots-o(1).
```

Near equality, the actual diameter density is forced toward `pi/2`, the PI area bound toward `D^2/2`, and the JC joint cavity bound toward equality simultaneously.

The next high-value step is therefore a **near-equality incompatibility theorem** for this joint regime, rather than another scalar relaxation: classify or exclude sources for which

1. `h/D -> pi/2`;
2. two diameter directions are asymptotically perpendicular enough to make `area(F) -> D^2/2` from below;
3. the pocket/exceptional-face isoperimetric bound is simultaneously nearly saturated; and
4. `t=e_BB/D` is close enough to `lambda` that the `t<=lambda` relaxation loses no fixed amount.

Any fixed incompatibility in those equality conditions raises the floor again and may force a stable geometric shell class accessible to Target B.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

DJC keeps y=h/D in both PI and JC.
PI gives asymptotic force-hull area floor
    A(y)=0.5 sin y,       2rho<=y<=pi/2,
         =0.5,           pi/2<=y<=pi.
JC gives joint cavity capacity
    G/D^2 <= (t+min(y,pi-y))^2/(4pi)+o(1),
with t=e_BB/D<=lambda=(e_BB+2s_C)/D.
Thus every subsequential limit satisfies
    A(y)-pi lambda^2/4
      <= (lambda+min(y,pi-y))^2/(4pi).
The positive root Lambda(y) decreases strictly up to y=pi/2 and increases strictly
after it. Hence the universal worst case is exactly y=pi/2.

At y=pi/2:
    (pi^2+1)lambda^2 + pi lambda + pi^2/4 - 2pi = 0,
so
    lambda >= 0.4653518453960140852....
This beats current-main GS 0.464792250394... without new literature.

Next target: incompatibility of simultaneous near-equality in PI, JC cavity capacity,
and t<=lambda around h/D=pi/2.
```
