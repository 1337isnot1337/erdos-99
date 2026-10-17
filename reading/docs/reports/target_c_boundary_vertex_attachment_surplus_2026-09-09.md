> Generated reading edition · [exact source](../../../docs/reports/target_c_boundary_vertex_attachment_surplus_2026-09-09.md) · source SHA-256 `4c7fa4b8c8ac716eef0eefc1b253c11a1776fcb95b8279433964cd60877386e3`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 4 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-22542587B65C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — BAS: boundary-vertex attachment penalty raises the explicit post-ZF surplus floor

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-e43-scalar-stability`  
**Run type:** quantitative attachment-area upgrade / scalar reoptimization  
**Target:** Target C C-II after ENS  
**Depends on:** ENS, BVP, ZK/ZG attachment-cell estimate, JC joint cavity capacity, HKS sharp Hemmi branch  
**External literature:** Bonnesen only through BVP; no additional source  
**Computation:** decimal evaluation of explicit quadratic roots only

## LEVEL I STATUS

**STILL OPEN.**

ENS proves

```math
\liminf\frac{e_{BB}+2s_C}{D}
\ge
0.48072358047.
```

The attachment-area estimate used there treats every harmonic attachment hull as though it could independently approach its isodiametric disk. BVP proves this is false in exactly the relevant diameter range: every attachment polygon has all of its vertices among the extreme vertices of the containing force hull, and that nesting costs a fixed normalized area `1/2500` whenever the attachment diameter lies in `[0.48D,0.50D]`.

If no attachment cell reaches `0.48D`, the square-sum estimate loses even more area because the total component-diameter budget is already above `0.48072358047D`.

Consequently, throughout the only slope window in which the new scalar minimum could occur,

```math
\boxed{
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le
\left(
\frac\pi4\lambda^2-\frac1{2500}+o(1)
\right)D^2,
}
\tag{BAS.1}
```

where

```math
\lambda=\lim\frac{e_{BB}+2s_C}{D}.
```

Inserting BAS.1 into the ENS/JC feasible region raises the explicit universal floor to

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
0.48109619577.
}
\tag{BAS.2}
```

The optimized root is

```math
\lambda_{BAS}
=0.4810961957739277\ldots,
```

while the rational perimeter split `p=3.0353134001` independently certifies the conservative displayed value.

This improves ENS by about `3.72615e-4`, more than two hundred times the ENS-over-HKS improvement.

---

## 1. Normalize the component-diameter budget

Let

```math
L:=e_{BB}+2s_C,
\qquad
k:=d_H+s_Z,
```

and pass to a subsequence with

```math
\frac LD\to\lambda.
\tag{1.1}
```

ZK defines

```math
L_2=6-3k+L
```

and proves

```math
\sum_r\delta_r\le L_2.
\tag{1.2}
```

Since `k>=0`,

```math
\boxed{
\limsup\frac1D\sum_r\delta_r\le\lambda.
}
\tag{BAS.3}
```

C40 gives

```math
\operatorname{diam}(A_r)\le\delta_r+2.
\tag{1.3}
```

Also `c_I=O(D)`: ZK gives `k=O(D)` from `3k<=6+L`, while ZU gives

```math
c_I+e_{BB}+s_C=q-2+k
```

and `q=O(D)`.

Therefore

```math
\sum_r(\delta_r+2)^2
=\sum_r\delta_r^2+O(D).
\tag{1.4}
```

---

## 2. The ordinary attachment-area bound

Write

```math
P_r:=\operatorname{conv}(A_r),
\qquad
\ell_r:=\operatorname{diam}(P_r).
```

By isodiametry,

```math
\operatorname{area}(P_r)
\le\frac\pi4\ell_r^2
\le\frac\pi4(\delta_r+2)^2.
\tag{2.1}
```

Summing, using (1.4) and

```math
\sum_r\delta_r^2
\le\left(\sum_r\delta_r\right)^2,
```

gives the old asymptotic capacity

```math
\sum_r\operatorname{area}(P_r)
\le
\left(\frac\pi4\lambda^2+o(1)\right)D^2.
\tag{2.2}
```

BAS proves that this upper bound always loses a fixed amount near the ENS slope.

---

## 3. Case A: one attachment hull reaches `0.48D`

Assume

```math
0.48072358047\le\lambda<0.49.
\tag{3.1}
```

Suppose along a subsequence there is a component `r_*` with

```math
\ell_{r_*}\ge0.48D.
\tag{3.2}
```

By BAS.3 and (1.3),

```math
\frac{\ell_{r_*}}D
\le\lambda+o(1)<0.50
```

for all sufficiently large members of the subsequence.

Every vertex of `P_{r_*}` is a loaded force-hull vertex, hence a vertex of `F`. After scaling by `D`, BVP applies and gives

```math
\operatorname{area}(P_{r_*})
\le
\frac\pi4\ell_{r_*}^2
-\frac{D^2}{2500}.
\tag{3.3}
```

Use ordinary isodiametry on every other component and sum:

```math
\sum_r\operatorname{area}(P_r)
\le
\frac\pi4\sum_r(\delta_r+2)^2
-\frac{D^2}{2500}.
```

Equations (1.4) and BAS.3 give

```math
\boxed{
\limsup\frac1{D^2}
\sum_r\operatorname{area}(P_r)
\le
\frac\pi4\lambda^2-\frac1{2500}.
}
\tag{BAS.4}
```

---

## 4. Case B: every attachment hull stays below `0.48D`

Now suppose instead

```math
\ell_r<RD
\qquad\text{for every }r,
\qquad
R:=0.48=\frac{12}{25}.
\tag{4.1}
```

For each component,

```math
\ell_r^2
\le
\min\{(\delta_r+2)^2,R^2D^2\}.
```

The elementary bound

```math
\min\{(\delta+2)^2,R^2D^2\}
\le
\min\{\delta,RD\}^2+4\delta+4
\tag{4.2}
```

holds for every `delta>=0`. Summing and using `sum delta=O(D)`, `c_I=O(D)` gives

```math
\frac1{D^2}\sum_r\ell_r^2
\le
\sum_r\min\left\{\frac{\delta_r}{D},R\right\}^2
+o(1).
\tag{4.3}
```

For nonnegative numbers `x_i` with

```math
\sum_i x_i\le\lambda<2R,
```

mass above `R` can be discarded without decreasing `sum min{x_i,R}^2`. We may therefore assume `0<=x_i<=R`. For a fixed total mass, the ordinary convex square sum `sum x_i^2` is maximized by concentrating mass as much as the cap permits: one coordinate equals `R` and the remaining mass is placed in one second coordinate. Hence, for `lambda>=R`,

```math
\boxed{
\sum_i\min\{x_i,R\}^2
\le
R^2+(\lambda-R)^2.
}
\tag{BAS.5}
```

Apply this to `x_i=delta_i/D` with BAS.3. Then

```math
\limsup\frac1{D^2}
\sum_r\operatorname{area}(P_r)
\le
\frac\pi4\left[R^2+(\lambda-R)^2\right].
\tag{4.4}
```

The loss from the old square is exactly

```math
\frac\pi4\left[
\lambda^2-R^2-(\lambda-R)^2
\right]
=
\frac{\pi R}{2}(\lambda-R)
=0.24\pi(\lambda-0.48).
\tag{4.5}
```

ENS already gives

```math
\lambda\ge0.48072358047.
```

Using only `pi>3`,

```math
0.24\pi(\lambda-0.48)
>
0.72(0.00072358047)
>0.00052
>\frac1{2500}.
\tag{4.6}
```

Thus Case B also gives BAS.4, with room to spare.

Cases A and B prove BAS.1 for every subsequential slope in (3.1).

---

## 5. Improved lower bound for the attachment-cell gap

Let

```math
G:=\operatorname{area}(F)-
\sum_r\operatorname{area}(P_r).
```

ENS gives the force-hull area lower branch

```math
A_E(p)
=
\frac12\sin\frac p2
\left[
1+
\frac{(p-3.010)_+^2}{16\pi^2}
\right]
\tag{5.1}
```

at the fixed-perimeter worst diameter density `y=p/2`, while HKS gives the sharp Hemmi branch

```math
A_H(p)
=3(p/p_2)^2-\frac{3+\sqrt3}{2},
\qquad
p_2=12\sin\frac\pi{12}.
\tag{5.2}
```

BAS.1 upgrades the gap lower bound on either branch to

```math
\boxed{
\frac G{D^2}
\ge
A(p)-\frac\pi4\lambda^2+\frac1{2500}-o(1),
}
\tag{BAS.6}
```

where `A(p)` is the applicable force-hull lower bound.

JC retains the upper capacity

```math
\boxed{
\frac G{D^2}
\le
\frac{(\lambda+p/2)^2}{4\pi}+o(1)
}
\tag{BAS.7}
```

after the same worst-case relaxations used by ENS.

Therefore every survivor slope in the window (3.1) must satisfy

```math
\boxed{
A(p)+\frac1{2500}
-\frac\pi4\lambda^2
\le
\frac{(\lambda+p/2)^2}{4\pi}.
}
\tag{BAS.8}
```

---

## 6. Reoptimization keeps the same perimeter crossover

Adding the same constant `1/2500` to the lower area side does not change the fixed-`p` diameter-density derivative, so ENS's exact minimizer `y=p/2` is unchanged.

Likewise, on each side of the PI/Hemmi crossover, the required positive root remains monotone in the same direction because the added constant is independent of `p`.

The PI and Hemmi required roots are equal precisely when their area inputs are equal. Hence the global perimeter crossover remains the ENS value

```math
\boxed{
p_E=3.035313400099390755\ldots .}
\tag{BAS.9}
```

At the exact crossover put

```math
A_*=A_E(p_E)=A_H(p_E).
```

The new threshold is the positive root of

```math
\boxed{
(\pi^2+1)\lambda^2
+p_E\lambda
+\frac{p_E^2}{4}
-4\pi\left(A_*+\frac1{2500}\right)
=0.
}
\tag{BAS.10}
```

Numerically,

```math
\boxed{
\lambda_{BAS}
=0.4810961957739277330\ldots .}
\tag{BAS.11}
```

The perimeter regimes outside the first Hemmi crossover cannot improve the minimum: ENS already proves their required roots are larger than the crossover root, and adding a positive constant to the area lower bound only raises those roots.

Since `lambda_BAS<0.49`, the window assumption used in BVP is self-consistent.

---

## 7. Rational perimeter split certificate

Use the same terminating decimal as ENS:

```math
\widehat p=3.0353134001.
```

At this value the exact enhanced PI and Hemmi area formulas give, after adding `1/2500`, the positive JC roots

```math
L_E^{BVP}(\widehat p)
=0.4810961957738451151\ldots,
```

and

```math
L_H^{BVP}(\widehat p)
=0.4810961957749086690\ldots .
```

Therefore both sides certify

```math
\boxed{\lambda>0.48109619577.}
```

Combined with the already excluded lower ENS range, this proves BAS.2.

---

## 8. Structural effect

BAS is not merely another numerical optimization. The improvement comes from a new global fact:

> an attachment hull is not a free diameter-constrained convex body; every one of its vertices must stay extreme in the larger force hull.

That extra extremality condition destroys disk saturation by a fixed amount.

---

## 9. Regression audit

- BAS uses the pre-existing ENS lower bound to enter the narrow slope window where BVP is valid. There is no circularity: ENS is an independent weaker theorem.
- If no attachment cell reaches `0.48D`, BAS does not invoke BVP; the square-sum budget itself supplies a larger loss.
- The `+2` in `diam(A_r)<=delta_r+2` contributes only `O(D)` after summing squared diameters because `sum delta_r=O(D)` and `c_I=O(D)`.
- No uniqueness of a giant component is assumed.
- No equality/compactness argument is needed for BAS.1; the area penalty is finite and explicit.
- The scalar decimal evaluation is not part of the geometric proof.

## 10. Next target

There are now two quantitatively separated response regimes:

1. unconditional pinned/contact currency `(e_BB+2s_C)/D>=0.48109619577-o(1)`;
2. RCC small-response regime `epsilon->0`, where `(e_BB+2s_C)/D>=1-o(1)`.

The next high-value work should target the high pinned-contact / near-star response branch rather than marginal scalar optimization.

## 11. Compact handoff

```text
BAS improves the attachment-cell capacity.
Let lambda=lim(e_BB+2s_C)/D in [0.48072358047,0.49).
ZK: sum delta_r/D<=lambda+o(1).

Case A: some attachment hull has diameter >=0.48D.
Since its diameter is <0.50D, BVP gives a fixed area penalty D^2/2500.
Summing ordinary isodiametry on the other cells yields
    sum area(P_r)/D^2 <= pi lambda^2/4 -1/2500+o(1).

Case B: every attachment hull has diameter <0.48D.
Discard any graph-diameter mass above 0.48 because the capped square is unchanged;
then maximize an ordinary square sum under cap 0.48. This gives
    sum diam(P_r)^2/D^2
      <=0.48^2+(lambda-0.48)^2+o(1).
The area loss is
    0.24pi(lambda-0.48)>0.00052>1/2500
using the independent ENS floor.
Thus the same -1/2500 improvement holds universally in the window.

Insert into ENS/JC:
    A(p)+1/2500-pi lambda^2/4
      <=(lambda+p/2)^2/(4pi).
The crossover remains p_E=3.03531340009939... .
The new root is
    lambda_BAS=0.4810961957739277... .
At p=3.0353134001 both branch roots exceed 0.48109619577.
Therefore
    liminf (e_BB+2s_C)/D >=0.48109619577.
```
