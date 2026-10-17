> Generated reading edition · [exact source](../../../docs/reports/target_c_nested_convex_perimeter_area_stability_2026-09-09.md) · source SHA-256 `9568702d4f72050a09779ec52ef9ea5ddac1e8fee66f2b0e2a37fefd9c55e385`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D49948F4C0AF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — NCS: nested convex perimeter–area stability makes the HKN gap explicit

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-density-sensitive-cavity`  
**Run type:** exact convex stability lemma + explicit HKS refinement  
**Target:** quantitative replacement for the nonconstructive HKN gap  
**Depends on:** HKS, TQB/Tamvakis, PI, JC/GU  
**External literature:** no new theorem beyond the Tamvakis theorem already imported in TQB  
**Computation:** decimal evaluation of an explicit scalar crossover only

## LEVEL I STATUS

**STILL OPEN.**

HKN proves that the HKS threshold

$$
\lambda_{HKS}=0.4807218393889119189819\ldots
$$

is uniformly unattainable, but leaves the positive gap nonconstructive.

A simple nested-convex stability inequality makes that gap explicit.

### Theorem NCS.1 — nested perimeter gap forces area gap

Let

$$
Q\subset K\subset\mathbb R^2
$$

be convex bodies with

$$
\operatorname{diam}(K)\le1,
\qquad
A(Q)>0.
$$

Then

$$
\boxed{
A(K)-A(Q)
\ge
\frac{A(Q)}{16\pi^2}
\bigl(P(K)-P(Q)\bigr)^2.
}
\tag{NCS.1}

Here `A` and `P` denote area and perimeter.

Applying NCS.1 to the PI four-endpoint quadrilateral and Tamvakis's global quadrilateral perimeter bound gives the asymptotic Target C force-hull area floor

\[
\boxed{
A(F)/D^2
\ge
A_{PI}(y)
\left[
1+rac{(p-P_4^*)_+^2}{16\pi^2}
\right]-o(1),
}
\tag{NCS.2}

where

\[
y=h/D,
\qquad
p=P(F)/D,
$$

$$
P_4^*=2+\sqrt6-\sqrt2,
$$

and `A_PI(y)` is the density-sensitive PI floor.

Combining NCS.2 with the sharp Hemmi first branch and the JC cavity bound raises the explicit post-ZF surplus floor to

$$
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{NCS}
=0.4807218393924606486500\ldots .
}
\tag{NCS.3}

Thus the HKN gap is no longer merely existential.

---

## 1. Perimeter difference is controlled by Hausdorff distance

Let

\[
r:=d_H(K,Q).
$$

Because `Q subset K`, support functions satisfy

$$
0\le h_K(u)-h_Q(u)\le r
$$

for every unit direction `u`.

Hence directional widths satisfy

$$
0\le w_K(u)-w_Q(u)\le2r.
$$

Cauchy's perimeter formula gives

$$
P(C)=\int_0^\pi w_C(\theta)\,d\theta
$$

for every planar convex body `C`. Therefore

$$
\boxed{
P(K)-P(Q)\le2\pi r.
}
\tag{NCS.4}

Equivalently,

\[
\boxed{
r\ge\frac{P(K)-P(Q)}{2\pi}.}
\tag{NCS.5}

---

## 2. Hausdorff excess forces a quadratic area increment

Choose

\[
x\in K
$$

with

$$
\operatorname{dist}(x,Q)=r.
$$

Let `y in Q` be a nearest point. The line through `y` perpendicular to `x-y` supports `Q`. Rotate and translate so that

$$
y=(0,0),
\qquad
x=(0,r),
$$

and

$$
Q\subset\{(u,v):v\le0\}.
$$

Let the width of `Q` in the vertical direction be `w`. Since `Q subset K` and `diam(K)<=1`,

$$
0<w\le1.
$$

For `0<=s<=w`, let `L(s)` be the length of the horizontal section of `Q` at height `-s`. Cavalieri gives

$$
A(Q)=\int_0^w L(s)\,ds.
$$

Hence some `s in[0,w]` satisfies

$$
L(s)\ge\frac{A(Q)}w\ge A(Q).
\tag{2.1}

Choose a segment of length `L(s)` in that section. The convex hull of this segment with `x` lies in

\[
\operatorname{conv}(Q\cup\{x\})\subset K.
$$

The full triangle has height `r+s`. Its intersection with the supporting half-plane `v>=0` is a similar triangle of height `r` and base

$$
L(s)\frac{r}{r+s}.
$$

This entire upper triangle lies outside `Q`. Its area is

$$
\frac{L(s)r^2}{2(r+s)}.
$$

Because `s<=1` and also `r<=1` (both `x` and every point of `Q` lie in the diameter-one body `K`),

$$
2(r+s)\le4.
$$

Therefore

$$
\boxed{
A(K)-A(Q)
\ge
\frac{A(Q)r^2}{4}.}
\tag{NCS.6}

Combining NCS.5 and NCS.6 proves NCS.1.

The constant is intentionally crude. No shape regularity of `Q` is required.

---

## 3. Apply the lemma to the PI endpoint quadrilateral

Normalize the Target C force hull by its source diameter `D`, so its diameter is one. Let `K=F/D`.

PI chooses two actual diameter chords and lets `Q` be the convex hull of their four endpoints. Then

\[
Q\subset K,
\qquad
\operatorname{diam}(Q)=1.
$$

If their projective angle is `phi`, the two-diagonal area formula gives

$$
A(Q)=\frac12\sin\phi.
\tag{3.1}

Tamvakis gives, for every diameter-one convex quadrilateral,

\[
P(Q)\le P_4^*:=2+\sqrt6-\sqrt2.
\tag{3.2}

Put

\[
p=P(K)=P(F)/D.
$$

Then

$$
P(K)-P(Q)
\ge
(p-P_4^*)_+.
$$

NCS.1 gives

$$
A(K)
\ge
A(Q)
\left[
1+rac{(p-P_4^*)_+^2}{16\pi^2}
\right].
\tag{3.3}

C67/PI gives asymptotically

\[
A(Q)\ge A_{PI}(y)-o(1),
$$

where

$$
A_{PI}(y)
=
\begin{cases}
\frac12\sin y,&y\le\pi/2,\\[3pt]
\frac12,&y\ge\pi/2.
\end{cases}
$$

This proves NCS.2.

---

## 4. Fixed-perimeter diameter-density optimization survives the bonus

Define

$$
B(p):=
1+rac{(p-P_4^*)_+^2}{16\pi^2}.
$$

For fixed `p`, the NCS-enhanced PI area floor is

$$
B(p)A_{PI}(y).
$$

The multiplier `B(p)` is independent of `y`.

In the relevant range `p>=4rho`, the same fixed-perimeter argument as PDG applies:

- for `y<=p/2`, the JC term has `m=y`; the required root decreases with `y`;
- for `y>=p/2`, `A_PI(y)` does not decrease while `m=p-y` decreases, so the required root increases.

Thus the hardest density remains

$$
\boxed{y=p/2.}
\tag{NCS.7}

For completeness, the only modified derivative on the first half is

\[
\frac{B(p)}2\cos y-rac{\lambda+y}{2\pi}.
$$

On the entire perimeter range needed below, `B(p)<1.001`, while `y>=2rho`; the same strict negativity margin used in DJC remains overwhelming. No near-zero derivative issue is introduced by the tiny stability factor.

Define

$$
\boxed{
A_N(p)
:=
\frac12\sin\frac p2
\left[
1+rac{(p-P_4^*)_+^2}{16\pi^2}
\right].
}
\tag{NCS.8}

Let `L_N(p)` be the positive root of

\[
A_N(p)-\frac\pi4\lambda^2
=
\frac{(\lambda+p/2)^2}{4\pi}.
\tag{NCS.9}

Near the HKS crossover, `L_N(p)` remains strictly decreasing in `p`. The added derivative is of order `10^-6`, while the negative PI/JC monotonicity margin is of order `10^-1`.

---

## 5. New crossover with the sharp Hemmi first branch

Retain the sharp Hemmi area floor

\[
A_H(p)
=3(p/p_2)^2-\frac{3+\sqrt3}{2},
\qquad
p_2=12\sin\frac\pi{12}.
$$

As in HKS, the Hemmi/JC required-surplus function is strictly increasing on the first Hemmi branch.

Therefore the global scalar minimum is attained at the unique crossover

$$
\boxed{
A_H(p_N)=A_N(p_N).
}
\tag{NCS.10}

Numerically,

\[
\boxed{
p_N
=3.0353123194061803335626\ldots .}
\tag{NCS.11}

At this perimeter the common area floor inserted into JC gives

\[
\boxed{
\lambda_{NCS}
=0.4807218393924606486501\ldots .}
\tag{NCS.12}

The explicit increase over HKS is

\[
\boxed{
\lambda_{NCS}-\lambda_{HKS}
=3.5487296681\times10^{-12}\ldots>0.}
\tag{NCS.13}

The numerical gain is tiny because the global Tamvakis perimeter gap at `p_c` is only about `3.6e-5` and NCS.1 is quadratic. Its importance is logical: the HKN positive gap is now fully explicit.

---

## 6. Decimal certificate without trusting optimizer digits

Choose the rational decimal split

\[
\widehat p=3.03531231941.
$$

Direct evaluation of the exact formulas gives

$$
L_N(\widehat p)
=0.4807218393919419000\ldots,
$$

while the sharp-Hemmi branch gives

$$
L_H(\widehat p)
=0.4807218393986144541\ldots .
$$

Monotonicity on the two sides therefore certifies the conservative theorem

$$
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.4807218393919.
}
\tag{NCS.14}

This is strictly above the HKS value already at the displayed decimal level.

---

## 7. Relation to FAQ and remaining numerical slack

NCS deliberately uses Tamvakis's **global** quadrilateral bound `P_4^*`.

FAQ proves a much stronger angle-sensitive bound. At the HKS angle `phi_c=p_c/2`,

\[
P_4(\phi_c)
=3.034910765287770\ldots,
$$

so the angle-sensitive perimeter deficit is about `4.0e-4`, more than eleven times the global Tamvakis deficit.

If one carries the actual PI angle as another live variable in NCS.2 and optimizes using FAQ instead of `P_4^*`, the quadratic area bonus is roughly two orders of magnitude larger. This should raise the explicit surplus floor by about `4e-10` rather than `4e-12`.

That refinement is now purely finite calculus; no further compactness or literature theorem is needed.

---

## 8. Regression audit

- NCS.1 requires positive area of `Q`; PI's endpoint quadrilateral has area bounded away from zero in the post-ZF regime.
- The support-slice proof does not assume `Q` is polygonal or has bounded angles.
- The perimeter/Hausdorff estimate uses the same origin for support functions, valid because `Q subset K`.
- `r<=1` follows from `diam(K)<=1` and nonempty `Q`.
- The scalar improvement uses only an area lower bound; it does not assume near-equality shapes.
- The exact crossover improvement is tiny but genuine; no `o(1)` term is used to resolve its sign because the final statement is asymptotic `liminf`.

## 9. Classification

**Status:** proved explicit quantitative replacement for HKN's existential gap.  
**Level I:** still open.  
**New external literature:** none beyond TQB's Tamvakis theorem.  
**Computation:** scalar decimal evaluation only.

## 10. Compact handoff

```text
NCS nested convex stability:
For convex Q subset K, diam K<=1,
    A(K)-A(Q) >= A(Q)[P(K)-P(Q)]^2/(16pi^2).
Proof:
  r=d_H(K,Q), Cauchy gives P(K)-P(Q)<=2pi r.
  Choose x in K at distance r from Q and a supporting line at its nearest point.
  Some parallel slice of Q has length >=A(Q); the cone from x to that slice contributes
  at least A(Q)r^2/4 area outside Q. Combine.

Apply to the PI four-endpoint hull. Tamvakis gives P(Q)<=P4*=2+sqrt6-sqrt2, so
  area(F)/D^2 >= A_PI(y)[1+(p-P4*)_+^2/(16pi^2)]-o(1).
Optimize with JC and sharp Hemmi exactly as in HKS. The new crossover is
  p_N=3.0353123194061803336...,
and
  lambda_NCS=0.48072183939246064865....
The rational split p=3.03531231941 certifies >=0.4807218393919.

This makes HKN's positive gap explicit. FAQ can improve the tiny numerical gain further
by retaining the actual PI diagonal angle.
```
