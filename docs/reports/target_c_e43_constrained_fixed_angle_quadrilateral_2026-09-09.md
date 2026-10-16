<!-- theorem-state: {"artifact_id":"ART-DDD13F0FF838","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — EFAQ: explicit anti-Reuleaux constraint sharpens the fixed-angle PI quadrilateral

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-explicit-anti-reuleaux`  
**Run type:** exact finite convex-geometry optimization  
**Target:** E43-constrained PI four-endpoint hull  
**Depends on:** E43 for the source-level triple constraint; elementary Euclidean geometry for the finite optimization  
**External literature used in proof:** none beyond E43  
**Computation:** decimal specialization only

## LEVEL I STATUS

**STILL OPEN.**

FAQ determines the largest perimeter of a diameter-one convex quadrilateral whose two diagonals have length one and prescribed angle. Its equality case contains three pairwise diametral vertices, so E43 excludes a fixed neighborhood of that optimizer.

The constrained problem can also be solved exactly.

Put

\[
r:=\frac{24}{25}
\]

and let `rho` be the canonical root `rho=cos rho`.

### Theorem EFAQ — fixed-angle quadrilateral under the explicit triple gap

Let `ABCD` be a convex quadrilateral of diameter at most one with

\[
AC=BD=1.
\]

Let

\[
\phi\in[2\rho,\pi/2]
\]

be the acute projective angle between the two diagonals. Assume every three of the four vertices contain a pair at distance at most `r`.

Then

\[
\boxed{
P(ABCD)
\le
\max\{\mathcal P_r(\cos(\phi/2)),\mathcal P_r(\sin(\phi/2))\},
}
\tag{EFAQ.1}

where for

\[
X\in[\sin\rho,\rho],
\qquad
Y:=\sqrt{1-X^2},
\qquad
\vartheta:=\arccos X,
\qquad
\gamma:=\arccos(r/2),
\]

we define

\[
\boxed{
\begin{aligned}
\mathcal P_r(X)
:=1+r
&+\sqrt{r^2+4X^2-4rX\cos(\gamma-\vartheta)}\\
&+\sqrt{r^2+1-2r\cos(\gamma-2\vartheta)}.
\end{aligned}}
\tag{EFAQ.2}

Equivalently, with

\[
h:=\sqrt{1-r^2/4},
\]

the two residual squared side lengths are

\[
\boxed{
q_X^2
=r^2+(4-2r^2)X^2-4rhXY,
}
\tag{EFAQ.3}

\[
\boxed{
s_X^2
=1+2r^2Y^2-4rhXY,
}
\tag{EFAQ.4}

so

\[
\mathcal P_r(X)=1+r+q_X+s_X.
\]

Equality is attained in the finite quadrilateral problem: one side in the constrained opposite pair has length `r`, one adjacent side has length `1`, and the other two sides have lengths `q_X,s_X`.

For the Target C HKS angle

\[
\phi_c=p_c/2=1.5176561597019888\ldots,
\]

direct substitution gives

\[
\boxed{
P(ABCD)<3.010.
}
\tag{EFAQ.5}

Thus the PI four-endpoint hull at that angle has perimeter separated from the HKS force-hull crossover perimeter by more than

\[
\boxed{
p_c-3.010>0.0253.}
\tag{EFAQ.6}

This is over sixty times the unconstrained FAQ separation `p_c-P_4(phi_c)`.

---

## 1. The triple condition is an opposite-side condition

Write the four side lengths cyclically as

\[
a=AB,
\quad b=BC,
\quad c=CD,
\quad d=DA.
\]

Every three-vertex subset contains one of the two unit diagonals:

- `ABC` and `ACD` contain `AC=1`;
- `ABD` and `BCD` contain `BD=1`.

Because `r<1`, the hypothesis that every triple contains a pair of length at most `r` becomes

\[
\min(a,b)\le r,
\quad
\min(b,c)\le r,
\quad
\min(c,d)\le r,
\quad
\min(d,a)\le r.
\tag{1.1}

The side indices whose lengths exceed `r` therefore form an independent set in the 4-cycle. Equivalently, at least one of the two opposite pairs is entirely short:

\[
\boxed{
(a,c\le r)
\quad\text{or}\quad
(b,d\le r).
}
\tag{EFAQ.7}

We optimize the two cases separately.

---

## 2. Orthogonal midpoint coordinates

Let the unit diagonal vectors be `u,v`, with acute angle `phi`. Translate so that the midpoint of `AC` is the origin and let `w` be the midpoint of `BD` relative to it.

After choosing the orientation of `v` and rotating coordinates, the four side vectors can be written as

\[
w\pm a,
\qquad
w\pm b,
\tag{2.1}

where

\[
a\perp b,
\]

and the two focus lengths are

\[
\{|a|,|b|\}
=
\left\{
\cos\frac\phi2,
\sin\frac\phi2
\right\}.
\tag{2.2}

Suppose first that the opposite pair represented by `w±a` is the short pair. Put

\[
X:=|a|,
\qquad
Y:=|b|,
\qquad X^2+Y^2=1.
\]

The other short-pair choice interchanges `X,Y`, which is why EFAQ.1 takes the maximum of the two values.

Because

\[
\phi/2\in[\rho,\pi/4],
\]

both possible focus lengths lie in

\[
\boxed{
\sin\rho\le X,Y\le\rho.
}
\tag{2.3}

Numerically this is approximately `[0.6736,0.7391]`; below we use only the coarse rigorous enclosure

\[
0.67<X,Y<0.74.
\tag{2.4}

Choose orthogonal axes with

\[
a=(X,0),
\qquad
b=(0,Y).
\]

The objective and constraints are invariant under `x->-x` and `y->-y`, so write

\[
w=(x,y),
\qquad x,y\ge0.
\]

For the short opposite pair,

\[
|w-a|\le|w+a|,
\]

and for the other pair

\[
|w-b|\le|w+b|.
\]

Thus all four diameter/anti-Reuleaux side constraints reduce exactly to

\[
\boxed{
(x+X)^2+y^2\le r^2,
}
\tag{EFAQ.8}

\[
\boxed{
x^2+(y+Y)^2\le1.}
\tag{EFAQ.9}

The perimeter objective is

\[
\boxed{
F(x,y)
=
\sqrt{(x+X)^2+y^2}
+\sqrt{(x-X)^2+y^2}
+\sqrt{x^2+(y+Y)^2}
+\sqrt{x^2+(y-Y)^2}.
}
\tag{EFAQ.10}

Each symmetric focus-pair sum is an even convex function of each coordinate separately. Therefore `F` is nondecreasing in `x` and in `y` on the first quadrant and strictly increasing away from degenerate axes where the relevant derivative vanishes.

The Pareto frontier of EFAQ.8–EFAQ.9 consists of one arc of the radius-`r` circle and one arc of the unit circle, meeting at one point in the positive quadrant. We show that `F` increases toward that intersection on both arcs.

---

## 3. Monotonicity on the short-side circle

Parameterize the radius-`r` frontier by

\[
x+X=r\cos t,
\qquad
y=r\sin t,
\tag{3.1}

starting at the positive `x`-axis and moving toward the circle intersection.

Write

\[
\vartheta:=\arccos X,
\qquad
Y=\sin\vartheta.
\]

Let

- `q` be the other short-side length;
- `R` the farther long-side length;
- `d` the nearer long-side length.

Then

\[
q^2=r^2+4X^2-4rX\cos t,
\]

\[
R^2=r^2+1-2r\cos(t+\vartheta),
\]

\[
d^2=r^2+1-2r\cos(t-\vartheta).
\]

On the feasible arc, `q<=r` and `R<=1`.

A direct differentiation and one exact cancellation give

\[
\frac1{r\sin t}\frac{dF}{dt}
=
\frac{2X}{q}
+\frac{2X}{R}
-
\frac{4rY\sin(\vartheta-t)}{(R+d)Rd}.
\tag{3.2}

The first two terms satisfy

\[
\frac{2X}{q}+\frac{2X}{R}
\ge2X\left(1+\frac1r\right).
\tag{3.3}

For the negative term, use

\[
d^2=(1-r)^2+4r\sin^2\frac{\vartheta-t}{2},
\]

so

\[
\frac{\sin(\vartheta-t)}d\le\frac1{\sqrt r}.
\tag{3.4}

Also the two long-side foci are `2Y` apart, hence

\[
R+d\ge2Y.
\]

Finally `R` increases along the arc, so

\[
R^2\ge R(0)^2=r^2+1-2rX.
\]

Therefore the magnitude of the negative term is at most

\[
\frac{2\sqrt r}{\sqrt{r^2+1-2rX}}.
\tag{3.5}

It remains to verify

\[
2X\left(1+\frac1r\right)
>
\frac{2\sqrt r}{\sqrt{r^2+1-2rX}}
\tag{3.6}

for `X in[sin rho,rho]`.

The difference between the two sides of (3.6) is concave as a function of `X`. The interval lies inside `[0.67,0.74]`. Evaluating the two rational endpoints after squaring positive quantities gives strict positivity at both endpoints; hence (3.6) holds throughout.

Thus

\[
\boxed{dF/dt>0}
\tag{EFAQ.11}

on the interior of the short-circle Pareto arc.

---

## 4. Monotonicity on the unit-side circle

Parameterize the unit-circle frontier from its positive `y`-axis endpoint toward the same intersection by

\[
x=\sin t,
\qquad
y+Y=\cos t.
\tag{4.1}

Let

- `q` be the other long-side length;
- `R` the farther short-side length;
- `d` the nearer short-side length.

Then

\[
q^2=1+4Y^2-4Y\cos t,
\]

\[
R^2=2-2\sin(\vartheta-t),
\]

\[
d^2=2-2\sin(\vartheta+t).
\]

On the feasible arc, `q<=1` and `R<=r`.

Differentiation gives

\[
\frac1{\sin t}\frac{dF}{dt}
=
\frac{2Y}{q}
+\frac{2Y}{R}
-
\frac{4X\cos(\vartheta+t)}{(R+d)Rd}.
\tag{4.2}

The positive terms satisfy

\[
\frac{2Y}{q}+\frac{2Y}{R}
\ge2Y\left(1+\frac1r\right).
\tag{4.3}

For the negative term,

\[
R+d\ge2X
\]

because the short-side foci are `2X` apart, and

\[
\frac{\cos(\vartheta+t)}d
=\sqrt{\frac{1+\sin(\vartheta+t)}2}
\le1.
\]

Also `R` increases from

\[
R(0)=\sqrt{2-2Y}.
\]

Hence the negative term is at most

\[
\frac{2}{\sqrt{2-2Y}}.
\tag{4.4}

So it suffices that

\[
2Y\left(1+\frac1r\right)
>
\frac{2}{\sqrt{2-2Y}}.
\tag{4.5}

Again the difference is concave in `Y`, and `[sin rho,rho] subset(0.67,0.74)`. The rational endpoint checks are strictly positive. Therefore

\[
\boxed{dF/dt>0}
\tag{EFAQ.12}

on the unit-circle Pareto arc.

---

## 5. The optimizer is the circle intersection

Sections 3–4 show that the perimeter increases along each Pareto arc toward their unique positive-quadrant intersection. Hence the global maximum for the chosen short opposite pair occurs exactly when

\[
\boxed{|w+a|=r,
\qquad|w+b|=1.}
\tag{5.1}

On the short-circle parameterization, the second equality is

\[
r^2+1-2r\cos(t+\vartheta)=1,
\]

so

\[
\boxed{t=\gamma-\vartheta,
\qquad\gamma=\arccos(r/2).}
\tag{5.2}

Substitution yields the two residual lengths in EFAQ.2.

Using

\[
\cos\gamma=r/2,
\qquad
\sin\gamma=h=\sqrt{1-r^2/4},
\]

produces the algebraically equivalent formulas EFAQ.3–EFAQ.4.

The alternative opposite-side choice swaps the two focus lengths. Taking the larger of the two corresponding explicit perimeter values proves EFAQ.1.

---

## 6. HKS-angle specialization

At

\[
\phi_c=p_c/2,
\]

the two focus choices are

\[
X=\cos(p_c/4),
\qquad
X=\sin(p_c/4).
\]

Substitution into EFAQ.2 gives a maximum below `3.010`, proving EFAQ.5.

Since

\[
p_c=3.0353123194\ldots,
\]

we obtain the conservative exact-decimal separation EFAQ.6.

The point is the scale: E43 turns the FAQ perimeter gap from order `4e-4` at the HKS angle into a gap exceeding `2.5e-2`.

---

## 7. Regression audit

- The triple condition is used on all four three-vertex subsets; it is not replaced by a one-side condition.
- The reduction to one short opposite pair is exact for a 4-cycle.
- The midpoint focus lengths are `cos(phi/2)` and `sin(phi/2)`; both possible assignments are retained in EFAQ.1.
- The range `phi in[2rho,pi/2]` is the post-ZF range needed for the HKS/ANS application and is used in the uniform derivative bounds.
- The boundary monotonicity proof uses only coarse `0.67<X,Y<0.74`, leaving a fixed margin.
- No claim is made here about quadrilateral angles outside the stated range.

## 8. Classification

**Status:** proved exact finite optimization conditional only on E43's source-level triple constraint.  
**Level I:** still open.  
**New external literature:** none beyond E43.  
**Computation:** only decimal specialization at `phi_c`.

## 9. Next exact target

Insert EFAQ into the nested-convex stability theorem NCS.

For the PI four-endpoint hull `Q`, EFAQ gives a perimeter deficit from the force hull of order `10^-2` near the HKS crossover, instead of FAQ's order `10^-4` deficit. NCS then converts this to an explicit area bonus quadratic in that deficit.

The resulting scalar crossover with the sharp Hemmi first-branch area curve should improve `lambda_ANS=0.480721839827...` by roughly several parts in `10^-6`.

## 10. Compact handoff

```text
EFAQ:
E43 on a unit-diagonal quadrilateral is equivalent to one opposite side pair being
<=r=24/25. In diagonal-midpoint coordinates the side vectors are w+-a,w+-b with
a perpendicular b and {|a|,|b|}={cos(phi/2),sin(phi/2)}.
For a chosen short pair put |a|=X, |b|=Y. In the first quadrant the constraints reduce
to
  (x+X)^2+y^2 <= r^2,
  x^2+(y+Y)^2 <= 1.
The perimeter is the sum of the four distances to the two symmetric focus pairs.

On the radius-r Pareto arc, direct differentiation gives
  F'/(r sin t)=2X/q+2X/R
    -4rY sin(vartheta-t)/[(R+d)Rd].
Use q<=r,R<=1, sin(vartheta-t)/d<=1/sqrt(r), R+d>=2Y, and
R>=sqrt(r^2+1-2rX). The resulting lower bound is positive uniformly for
X in[sin rho,rho].

On the unit-circle Pareto arc,
  F'/sin t=2Y/q+2Y/R
    -4X cos(vartheta+t)/[(R+d)Rd].
Use q<=1,R<=r, cos(vartheta+t)/d<=1, R+d>=2X, and
R>=sqrt(2-2Y). Again the uniform lower bound is positive.

So the maximum is the unique intersection where one short side is r and one adjacent
side is 1. This gives the explicit formula EFAQ.2, with both focus assignments retained.
At the HKS angle phi_c=p_c/2, the maximum is <3.010, so its perimeter gap from the
force-hull crossover p_c exceeds 0.0253.
```
