> Generated reading edition · [exact source](../../../docs/reports/target_c_e43_nested_stability_surplus_2026-09-09.md) · source SHA-256 `657ca7dd80ba6dec31875388db578f7d2ee724916bc1c060a6811172a03bbcc4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 10 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-24B46815B5F6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ENS: explicit E43 quadrilateral stability raises the post-ZF surplus floor

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-e43-scalar-stability`  
**Run type:** exact finite-certificate + scalar feasible-region optimization  
**Target:** Target C C-II after ZF/PI/JC/HKS  
**Depends on:** HKS and NCS from PR #130; E43/EFAQ from PR #132  
**External literature:** no new source beyond those dependencies  
**Computation:** exact rational interval certificate for one continuous one-variable cap; scalar decimal evaluation only

## LEVEL I STATUS

**STILL OPEN.**

> **Downstream note (2026-09-09):** ENS remains a valid independent theorem, but its explicit scalar constant is no longer the strongest result on this branch. BVP/BAS improve the attachment-cell capacity and raise the explicit floor to `0.48109619577`. RCC independently raises the conditional floor to slope `1` whenever the response defect `epsilon->0`.

PR #132 proves that the explicit anti-Reuleaux gap `r=24/25` sharply constrains the PI four-endpoint quadrilateral. For the scalar Target C argument it is enough to use a simple uniform consequence of EFAQ:

```math
\boxed{P(Q)<3.010}
\tag{ENS.1}
```

for every diameter-one PI quadrilateral whose two unit diagonals make angle in the complete post-ZF range

```math
2\rho\le\phi\le\frac\pi2.
```

The continuous inequality ENS.1 is certified by the exact rational interval checker `research/target_c_efaq_uniform_cap.py`.

Combining ENS.1 with the general nested-convex stability theorem NCS gives the area bonus

```math
\boxed{
\frac{A(F)}{D^2}
\ge
A_{PI}(y)
\left[
1+
\frac{(p-3.010)_+^2}{16\pi^2}
\right]-o(1),
}
\tag{ENS.2}
```

where

```math
p=\frac{P(F)}D,
\qquad y=\frac hD.
```

Reoptimizing the PI/JC side against the sharp first Hemmi branch yields

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{ENS}
=0.4807235804783056468\ldots .
}
\tag{ENS.3}
```

A rational decimal split independently certifies the conservative theorem

```math
\boxed{
\liminf
\frac{e_{BB}+2s_C}{D}
\ge0.48072358047.
}
\tag{ENS.4}
```

The rest of this report records the original ENS proof. Downstream reports `target_c_boundary_vertex_isodiametric_penalty_2026-09-09.md` and `target_c_boundary_vertex_attachment_surplus_2026-09-09.md` sharpen the attachment-area side without changing any ENS step.

---

## 1. Uniform EFAQ perimeter cap

EFAQ gives, for one choice of short opposite-side pair,

```math
P_r(X)=1+r+q_X+s_X,
\qquad r=\frac{24}{25},
\tag{1.1}
```

where

```math
q_X^2=r^2+(4-2r^2)X^2-4rhXY,
```

```math
s_X^2=1+2r^2Y^2-4rhXY,
```

```math
X^2+Y^2=1,
\qquad h=\sqrt{1-r^2/4}=\frac{\sqrt{481}}{25}.
```

The two possible opposite-side assignments correspond to replacing `X` by `Y`; therefore it suffices to bound the same function for

```math
X^2\in[\sin^2\rho,\rho^2].
```

Because `rho=cos rho<0.74`,

```math
[\sin^2\rho,\rho^2]\subset[0.4524,0.5476].
\tag{1.2}
```

Put

```math
t=X^2,
\qquad z=XY=\sqrt{t(1-t)}.
```

Then exactly

```math
q^2
=\frac{576}{625}
+\frac{1348}{625}t
-\frac{96\sqrt{481}}{625}z,
\tag{1.3}
```

```math
s^2
=\frac{1777}{625}
-\frac{1152}{625}t
-\frac{96\sqrt{481}}{625}z.
\tag{1.4}
```

The checker subdivides the rational interval `[0.4524,0.5476]` into exactly 1000 equal rational intervals. On each interval `[a,b]`:

1. `t(1-t)` is concave, so its minimum occurs at an endpoint;
2. an exact rational lower enclosure for `sqrt(t(1-t))` is obtained with `math.isqrt` at denominator `10^18`;
3. the coefficient `96 sqrt(481)/625` is also enclosed below rationally;
4. (1.3) is bounded above using `t=b` and the lower product enclosure;
5. (1.4) is bounded above using `t=a` and the same lower product enclosure;
6. the final two square roots are enclosed above rationally.

No floating-point number is used in the pass/fail assertion.

The largest resulting rational upper bound is

```math
\boxed{
\frac{3009480763847760179}{10^{18}}
=3.009480763847760179
<\frac{301}{100}=3.010.
}
\tag{ENS.5}
```

Thus ENS.1 is an exact exhaustive interval certificate for the complete EFAQ angle range.

---

## 2. Insert the perimeter cap into NCS

Let `K=F/D` be the diameter-one normalized force hull and let `Q` be the PI four-endpoint hull.

NCS proves for every convex `Q subset K` with `diam K<=1`:

```math
A(K)-A(Q)
\ge
\frac{A(Q)}{16\pi^2}
\bigl(P(K)-P(Q)\bigr)^2.
\tag{2.1}
```

PI gives

```math
A(Q)\ge A_{PI}(y)-o(1),
\tag{2.2}
```

where

```math
A_{PI}(y)
=\begin{cases}
\frac12\sin y,&y\le\pi/2,\\[3pt]
\frac12,&y\ge\pi/2.
\end{cases}
```

E43 applies to the four actual source vertices forming `Q`, and EFAQ plus ENS.1 gives

```math
P(Q)<3.010.
\tag{2.3}
```

Since `P(K)=p`, equations (2.1)--(2.3) imply ENS.2.

The strict inequality in (2.3) may be weakened to `<=3.010` in ENS.2; this only weakens the valid area lower bound.

---

## 3. Fixed-perimeter diameter-density minimization remains unchanged

Define

```math
B(p):=1+\frac{(p-3.010)_+^2}{16\pi^2}.
```

For fixed `p`, the enhanced PI area floor is simply `B(p)A_PI(y)`.

For `p>=4rho`, combine this area floor with JC:

```math
B(p)A_{PI}(y)-\frac\pi4\lambda^2
\le
\frac{(\lambda+\min\{y,p-y\})^2}{4\pi},
\tag{3.1}
```

where

```math
\lambda=\frac{e_{BB}+2s_C}{D}
```

in the subsequential limit.

For `y<=p/2`, the left-minus-right derivative in `y` is

```math
\frac{B(p)}2\cos y
-\frac{\lambda+y}{2\pi}.
```

On the entire range needed below,

```math
p\le p_2=12\sin(\pi/12)<3.106,
```

so `B(p)<1.0001`. Also `y>=2rho>4/3`, hence `cos y<cos(4/3)<1/4`, while

```math
\frac{\lambda+y}{2\pi}
\ge\frac{y}{2\pi}
>\frac{2}{3\pi}>0.21.
```

Thus the derivative is strictly negative. The required positive root decreases up to `y=p/2`.

For `y>=p/2`, the area floor does not decrease while `p-y` decreases, so the required root strictly increases. Therefore the unique fixed-perimeter worst density remains

```math
\boxed{y=p/2.}
\tag{ENS.6}
```

For `p<=4rho`, the older PDG analysis gives the worst density `y=2rho`; that entire perimeter range has a much larger required surplus and cannot contain the global ENS minimum.

---

## 4. Enhanced PI branch as a function of perimeter

For `p>=4rho`, define

```math
\boxed{
A_E(p)
:=
\frac12\sin\frac p2
\left[
1+
\frac{(p-3.010)_+^2}{16\pi^2}
\right].
}
\tag{ENS.7}
```

Let `L_E(p)` be the positive root of

```math
A_E(p)-\frac\pi4\lambda^2
=
\frac{(\lambda+p/2)^2}{4\pi}.
\tag{ENS.8}
```

The function `L_E(p)` is strictly decreasing on the relevant interval up to the Hemmi crossover.

Indeed, write the left-minus-right side as `F(p,lambda)`. Then `F_lambda<0` and

```math
F_p=A_E'(p)-\frac{\lambda+p/2}{4\pi}.
```

For `3.010<=p<=p_2`,

```math
A_E'(p)
=\frac14\cos\frac p2\,B(p)
+\frac12\sin\frac p2\frac{2(p-3.010)}{16\pi^2}.
```

Using `p>=3.010`, `cos(p/2)<0.07`, `B(p)<1.0001`, and `p-3.010<0.096`,

```math
A_E'(p)<0.019.
```

But

```math
\frac{\lambda+p/2}{4\pi}
>\frac{p}{8\pi}
>0.119.
```

Hence `F_p<0`, and because `F_lambda<0`, implicit differentiation gives

```math
\boxed{L_E'(p)<0.}
\tag{ENS.9}
```

---

## 5. Cross with the sharp first Hemmi branch

HKS imports the sharp first Hemmi area floor

```math
A_H(p)
=3(p/p_2)^2-\frac{3+\sqrt3}{2},
\qquad
3<p\le p_2.
\tag{5.1}
```

The corresponding Hemmi/JC required-surplus function `L_H(p)` is strictly increasing, as proved in HKS.

The difference `A_H(p)-A_E(p)` is strictly increasing on the crossover neighborhood because

```math
A_H'(p)>\frac{18}{10}=1.8,
\qquad
A_E'(p)<0.019.
```

Therefore there is at most one crossover.

Direct evaluation of the exact expressions at rational decimals on either side gives a sign change, hence a unique

```math
\boxed{
p_E
=3.0353134000993907553728\ldots .}
\tag{ENS.10}
```

At this point

```math
A_H(p_E)=A_E(p_E),
```

and the common JC root is

```math
\boxed{
\lambda_{ENS}
=0.4807235804783056467865\ldots .}
\tag{ENS.11}
```

For `p<p_E`, monotonicity of `L_E` gives a required surplus at least `L_E(p_E)`. For `p>p_E` up to `p_2`, monotonicity of `L_H` gives at least `L_H(p_E)`. The `p>=p_2` Hemmi regime has the much larger floor already recorded in HKI.

This proves ENS.3.

---

## 6. Rational decimal certificate

Choose

```math
\widehat p=3.0353134001.
```

Substitution into the exact formulas gives

```math
L_E(\widehat p)
=0.4807235804782229961\ldots,
```

```math
L_H(\widehat p)
=0.4807235804792865501\ldots.
```

Both exceed `0.48072358047`.

The sign of `A_H-A_E` changes at `p_E`, so the smaller of the two roots at the rational split is a conservative lower certificate for the exact crossover minimum. This proves ENS.4 independently of the displayed decimal root.

---

## 7. Improvement over the preceding scalar floors

The explicit sequence is

```math
0.464792250394\ldots
<0.465351845396\ldots
<0.466817604403\ldots
<0.470735339540\ldots
<0.480721839389\ldots
<0.480723580478\ldots .
```

These correspond respectively to current-main GS, DJC, PDG, coarse Hemmi `n=2`, HKS, and ENS. Downstream BAS adds `0.48109619577`.

---

## 8. Near-equality regime

A sequence approaching the ENS scalar threshold must satisfy

```math
\frac{P(F)}D\to p_E,
\qquad
\frac hD\to\frac{p_E}{2},
\tag{8.1}
```

```math
\frac{A(F)}{D^2}\to A_E(p_E)=A_H(p_E),
\tag{8.2}
```

and near-equality in EFAQ/NCS, the sharp first Hemmi area lower bound, JC's joint cavity capacity, and the relaxation `e_BB/D <= (e_BB+2s_C)/D`.

The downstream ESN report restores those relaxations and proves this exact endpoint is impossible. BAS then obtains a stronger finite explicit exclusion by improving the attachment-area capacity itself.

---

## 9. Regression audit

- The interval checker covers a strict superset `[0.4524,0.5476]` of the true `X^2` range. No angular sample grid is used without interval enclosure.
- The theorem does not depend on the last digits of the optimizer. The rational split `p_hat=3.0353134001` certifies the conservative displayed floor.
- No new external result is introduced here. Hemmi/Kripfganz enters through HKS and Kneser-Poulsen through E43.
- A larger linear pinned/contact surplus is a stronger necessary condition, not by itself a contradiction. BAS/RCC are the current downstream directions.

---

## 10. Classification

**Status:** proved quantitative strengthening under the stacked PR #130/#132 dependencies; superseded numerically but not logically by BAS.  
**Level I:** still open.  
**New external literature:** none.  
**Computation:** exact rational interval checker plus decimal scalar evaluation.
