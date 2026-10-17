> Generated reading edition · [exact source](../../../docs/reports/target_c_disk_reverse_isoperimetric_floor_059348_2026-09-10.md) · source SHA-256 `2210f1babb455f9b5ec137fddd45024beedd34f3b84edd454d1327363ff8d240`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7B0FC18B7BAF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — disk reverse isoperimetry raises the post-ZF surplus floor to 0.593483

**Date:** 2026-09-10  
**Repository base:** branch `research/2026-09-10-symmetric-support-floor` after `a98154b23ff10bd344057207a3a9c153d6a84002`  
**Run type:** external-theorem import / exact inequality synthesis / explicit branch narrowing  
**Target:** Target C, C-II after ZF / FS / FSDB / JC  
**External input:** Beniamin Bogosel, *A reverse isoperimetric inequality for convex shapes with inclusion constraint*, arXiv:2402.05648v1 (2024), Theorem 6 and Proposition 5(c)  
**Computation:** decimal evaluation only; the proof is analytic once the external theorem is accepted

## LEVEL I STATUS

`STILL OPEN`.

The immediately preceding report on this branch proved the self-contained centrally symmetric support-function lower bound

```math
A\ge \frac{P^2}{2\pi}-\frac{\pi D^2}{4}
```

and used it to obtain

```math
\liminf\frac{e_{BB}+2s_C}{D}
\ge 0.5933612807422635\ldots .
```

This report replaces that coarse convex-area floor by the exact solution of the reverse isoperimetric problem for convex subsets of a disk. The result is the stronger explicit post-ZF bound

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{RI}
=0.59348346023609149178\ldots .
}
\tag{RI.1}
```

The improvement is small numerically but structurally useful: the force-hull area input is now the exact disk-container lower envelope rather than a quadratic support-function relaxation.

The unique scalar optimizer lies on the six-gon branch. There is a unique pair

```math
\boxed{
(y_0,\theta_0)
\in(2\rho,\pi/2)\times(0,\pi/3)
}
\tag{RI.2}
```

satisfying

```math
\boxed{
2y_0
=
\sin\frac{\theta_0}{2}
+5\sin\frac{2\pi-\theta_0}{10},
}
\tag{RI.3}
```

and

```math
\boxed{
\frac{y_0+\sin y_0}{4}
=
\frac18\left(
\sin\theta_0
+5\sin\frac{2\pi-\theta_0}{5}
\right).
}
\tag{RI.4}
```

Numerically,

```math
y_0=1.48353287160140953601\ldots,
\qquad
\theta_0=0.31683197976766354674\ldots,
\tag{RI.5}
```

so

```math
p_0:=2y_0
=2.96706574320281907201\ldots .
\tag{RI.6}
```

Then `lambda_RI` is the positive root of

```math
\boxed{
(\pi^2+1)\lambda^2
+2y_0\lambda
+y_0^2
-\pi(y_0+\sin y_0)=0.
}
\tag{RI.7}
```

No numerical optimizer is a proof dependency.

---

## 1. External theorem and exact scaling

Let `B_1` be the Euclidean unit disk. Bogosel studies convex sets

```math
\Omega\subseteq B_1
```

with prescribed area `A in (0,pi)` and maximizes their perimeter.

Theorem 6 of arXiv:2402.05648v1 states that the maximizer is an inscribed `m`-gon, unique up to permutation of its side-angle data, where

```math
(m-1)\sin\frac{2\pi}{m-1}
<2A
\le m\sin\frac{2\pi}{m},
\tag{1.1}
```

and its central angles have the form

```math
0<\theta_1\le\theta_2=\cdots=\theta_m.
\tag{1.2}
```

Writing

```math
\theta:=\theta_1,
\qquad
\vartheta:=\frac{2\pi-\theta}{m-1},
\tag{1.3}
```

the area and perimeter are

```math
A
=\frac12\bigl(\sin\theta+(m-1)\sin\vartheta\bigr),
\tag{1.4}
```

```math
P
=2\left(
\sin\frac\theta2
+(m-1)\sin\frac\vartheta2
\right).
\tag{1.5}
```

Proposition 5(c) in the same paper proves that the maximal perimeter is **strictly increasing** with the prescribed area. Therefore Theorem 6 can be inverted: for every admissible perimeter `P`, any convex subset of `B_1` with that perimeter has area at least the unique inverse-envelope value determined by (1.4)-(1.5).

### Applicability to the force hull

For the post-ZF force hull `F`, the current FS symmetral theorem defines

```math
S:=\frac12((F-o)-(F-o))
\tag{1.6}
```

and proves

```math
\operatorname{diam}S=D,
\qquad
\operatorname{per}S=\operatorname{per}F,
\tag{1.7}
```

```math
0\le
\operatorname{area}S-\operatorname{area}F
=o(D^2).
\tag{1.8}
```

Because `S` is centrally symmetric and has diameter `D`, it is contained in the radius-`D/2` disk centered at its symmetry center:

```math
S\subseteq B(0,D/2).
\tag{1.9}
```

Thus the rescaled body

```math
\widetilde S:=\frac2D S
```

satisfies exactly the containment hypothesis of Bogosel's theorem. No claim that `F` itself is centrally symmetric at finite `D` is needed.

---

## 2. The inverse disk-container area envelope

Normalize back to source diameter `D=1`. For

```math
p:=\frac{\operatorname{per}F}{D}\in[2,\pi],
```

define `B(p)` to be one quarter of the least area in the unit-disk normalization at perimeter `2p`. Equivalently, `B(p)` is the sharp area lower envelope for convex bodies contained in a radius-`1/2` disk and having perimeter `p`.

Put

```math
p_m:=m\sin\frac\pi m
\qquad(m\ge2).
\tag{2.1}
```

For

```math
p_{m-1}<p\le p_m,
\tag{2.2}
```
there is a unique

```math
0<\theta\le\frac{2\pi}{m}
```
with

```math
\boxed{
p
=
\sin\frac\theta2
+(m-1)\sin\frac{2\pi-\theta}{2(m-1)}.
}
\tag{2.3}
```

The sharp lower envelope is

```math
\boxed{
B(p)
=
\frac18\left[
\sin\theta
+(m-1)\sin\frac{2\pi-\theta}{m-1}
\right].
}
\tag{2.4}
```

The function `B` is continuous and strictly increasing from `B(2)=0` to

```math
B(\pi)=\frac\pi4.
\tag{2.5}
```

On the interior of one `m`-gon branch, differentiating (2.3)-(2.4) gives the exact derivative

```math
\boxed{
B'(p)
=
\frac12\left(
\cos\frac\theta2
+
\cos\frac{2\pi-\theta}{2(m-1)}
\right).
}
\tag{2.6}
```

Indeed, if

```math
\vartheta=\frac{2\pi-\theta}{m-1},
```
then

```math
\frac{dp}{d\theta}
=\frac12\left(
\cos\frac\theta2-
\cos\frac\vartheta2
\right)
```

and

```math
\frac{dB}{d\theta}
=\frac18(\cos\theta-\cos\vartheta),
```

so the factorization

```math
\cos\theta-\cos\vartheta
=2\left(
\cos\frac\theta2-
\cos\frac\vartheta2
\right)
\left(
\cos\frac\theta2+
\cos\frac\vartheta2
\right)
```

gives (2.6).

### Force-hull consequence

By (1.8), every convergent post-ZF subsequence with normalized force-hull perimeter `p` satisfies

```math
\boxed{
\liminf
\frac{\operatorname{area}F}{D^2}
\ge B(p).
}
\tag{2.7}
```

This is stronger than the preceding report's self-contained quadratic floor `Psi(p)` wherever the two differ in the active range.

---

## 3. Combine with FSDB and JC

Retain

```math
y:=\lim\frac hD,
\qquad
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
\qquad
p:=\lim\frac{\operatorname{per}F}{D}.
\tag{3.1}
```

DB and convexity give

```math
2\rho\le y\le p\le\pi.
\tag{3.2}
```

FSDB independently gives

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\Phi(y):=\frac{y+\sin y}{4}.
}
\tag{3.3}
```

Together with (2.7),

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
M(y,p):=\max\{\Phi(y),B(p)\}.
}
\tag{3.4}
```

The GU/ZK cell estimate and actual-perimeter JC cavity inequality then give, exactly as in the preceding report,

```math
\boxed{
M(y,p)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m(y,p))^2}{4\pi},
\qquad
m(y,p):=\min\{y,p-y\}.
}
\tag{3.5}
```

Equivalently every survivor limit must satisfy

```math
\boxed{
F(y,p,\lambda):=
(\pi^2+1)\lambda^2
+2m(y,p)\lambda
+m(y,p)^2
-4\pi M(y,p)
\ge0.
}
\tag{3.6}
```

For fixed `(y,p)`, `F` is strictly increasing in `lambda>=0`.

---

## 4. Exact optimization over the force-hull perimeter

For fixed `y`, let `p_y` be the unique perimeter satisfying

```math
\boxed{B(p_y)=\Phi(y).}
\tag{4.1}
```

It exists because `B(pi)=pi/4>=Phi(y)`. It also satisfies `p_y>=y`. Indeed

```math
B(y)\le\frac{y^2}{4\pi}\le\Phi(y),
\tag{4.2}
```

where the first inequality is the ordinary isoperimetric upper bound for **any** body of perimeter `y`, and the second is equivalent to

```math
y^2\le\pi(y+\sin y),
```

which holds on `[0,pi]` with equality only at `pi`.

The relevant reverse-isoperimetric branch is always at least the six-gon branch once `B` is active. To see this, let

```math
p_5=5\sin\frac\pi5.
```

The canonical bound `rho>739/1000` gives

```math
4\rho>2.956.
```

The exact formula

```math
\sin^2\frac\pi5=\frac{5-\sqrt5}{8}
```

and `sqrt(5)>223/100` give

```math
p_5<2.95<4\rho.
\tag{4.3}
```

Section 5 below proves `p_y>=4rho` at the left endpoint and `p_y` increases thereafter. Hence all derivatives needed in the active `B` region have `m>=6`.

For any branch `m>=6`, (2.6) gives the uniform bound

```math
\boxed{B'(p)>\frac12.}
\tag{4.4}
```

For example `theta/2<=pi/6`, while the second half-angle is below `pi/5`; both cosines are positive and their sum is greater than one.

Fix `y` and fix `lambda<=1`. Consider (3.6) as a function of `p`.

### Case 1: `p<=2y` and `B(p)<=Phi(y)`

Then `M=Phi(y)` and `m=p-y`, so `F` strictly increases with `p`.

### Case 2: `p>=2y` and `B(p)<=Phi(y)`

Then `m=y` and `M=Phi(y)`, so `F` is constant in `p`.

### Case 3: `p<=2y` and `B(p)>Phi(y)`

Then

```math
\frac{\partial F}{\partial p}
=2(\lambda+p-y)-4\pi B'(p).
\tag{4.5}
```

Since `p-y<=p/2<=pi/2`, `lambda<=1`, and `B'(p)>1/2`,

```math
\frac{\partial F}{\partial p}
<2+\pi-2\pi
=2-\pi<0.
\tag{4.6}
```

### Case 4: `p>=2y` and `B(p)>Phi(y)`

Then `m=y` is fixed and `B` increases, so `F` strictly decreases.

Therefore the largest value of `F` over admissible `p` is attained as follows:

```math
\boxed{
 p_*(y)=
 \begin{cases}
 2y,&p_y\ge2y,\\
 p_y,&p_y\le2y.
 \end{cases}
}
\tag{4.7}
```

When `p_y>2y`, every point in the flat interval `[2y,p_y]` gives the same value; choosing `2y` is convenient.

Because the threshold root in `lambda` decreases when `F` increases, (4.7) gives the smallest possible survivor threshold at each fixed `y`.

---

## 5. A unique crossover between FSDB and reverse isoperimetry

On

```math
2\rho\le y\le\frac\pi2,
```
put

```math
H(y):=B(2y)-\Phi(y).
\tag{5.1}
```

At the left endpoint,

```math
\boxed{H(2\rho)<0.}
\tag{5.2}
```

A geometric proof avoids numerical evaluation. A symmetric circular slice of diameter one with parameter `y` has

```math
P_{slice}(y)=y+2\cos(y/2),
\qquad
A_{slice}(y)=\Phi(y).
\tag{5.3}
```

At `y=2rho`, the Dottie equation `rho=cos rho` gives

```math
P_{slice}(2\rho)=4\rho=2y.
\tag{5.4}
```

This circular slice is not a polygon. Bogosel's Theorem 6 says the perimeter maximizer at its fixed area is an inscribed polygon and characterizes it uniquely up to side permutation. Hence the slice is not a maximizer, so the maximal perimeter at area `Phi(2rho)` is strictly larger than `4rho`. Since that maximal-perimeter function is strictly increasing in area, inversion gives

```math
B(4\rho)<\Phi(2\rho),
```

proving (5.2).

At the right endpoint,

```math
B(\pi)=\frac\pi4,
```

while

```math
\Phi(\pi/2)=\frac{\pi/2+1}{4}.
```

Thus

```math
\boxed{
H(\pi/2)=\frac{\pi-2}{8}>0.
}
\tag{5.5}
```

Between branch transition points, (4.4) gives

```math
H'(y)
=2B'(2y)-\Phi'(y)
>1-\frac12
=\frac12.
\tag{5.6}
```

The same strict increase holds across the finitely many branch transition points by continuity and the positive one-sided derivative bounds. Therefore there is a unique

```math
\boxed{y_0\in(2\rho,\pi/2)}
\tag{5.7}
```

with

```math
\boxed{B(2y_0)=\Phi(y_0).}
\tag{5.8}
```

For `y<=y_0`, one has `p_y>=2y`; for `y>=y_0`, one has `p_y<=2y`.

Because

```math
p_5<4\rho<2y_0<3=p_6,
```

the crossover lies on the six-gon branch. Equations (2.3)-(2.4) with `m=6` are exactly RI.3-RI.4.

---

## 6. Optimize over the diameter-edge density

Define `lambda_RI` by RI.7. Since

```math
\lambda_{RI}<1,
```

all fixed-`lambda` derivative arguments in Section 4 apply. The inequality follows, for example, by evaluating (3.6) at `lambda=1`: on the relevant range its value is positive, so the unique positive threshold root is below one.

We prove that for every admissible `(y,p)`,

```math
F(y,p,\lambda_{RI})\le0.
\tag{6.1}
```

Because `F` is increasing in `lambda`, this implies every survivor threshold is at least `lambda_RI`.

### Left branch: `2rho<=y<=y_0`

By Section 4 we may take `p=2y`; then `m=y` and `M=Phi(y)`. Put

```math
F_1(y)
=(\pi^2+1)\lambda_{RI}^2
+2y\lambda_{RI}
+y^2
-\pi(y+\sin y).
\tag{6.2}
```

At `y=y_0`, RI.7 gives

```math
F_1(y_0)=0.
\tag{6.3}
```

Also

```math
F_1'(y)
=2\lambda_{RI}+2y-\pi(1+\cos y),
\tag{6.4}
```

```math
F_1''(y)=2+\pi\sin y>0.
\tag{6.5}
```

The existing FSJC audit proves (6.4) is already positive at `y=2rho` for every `lambda>1/2`. Since `lambda_RI>lambda_FSJC>1/2`, `F_1` is strictly increasing throughout this interval. Hence

```math
F_1(y)\le0.
\tag{6.6}
```

### Right branch: `y>=y_0`

Now Section 4 gives `p=p_y`, where `B(p_y)=Phi(y)`. Put

```math
m_y:=p_y-y.
```

Then

```math
F_2(y)
=(\pi^2+1)\lambda_{RI}^2
+2m_y\lambda_{RI}
+m_y^2
-4\pi\Phi(y).
\tag{6.7}
```

Differentiate the defining identity `B(p_y)=Phi(y)` away from branch-transition points:

```math
p_y'
=\frac{\Phi'(y)}{B'(p_y)}.
\tag{6.8}
```

Using `Phi'(y)<=1/2` and `B'(p_y)>1/2`,

```math
0\le p_y'<1,
\qquad
m_y'=p_y'-1<0.
\tag{6.9}
```

Therefore

```math
F_2'(y)
=2(\lambda_{RI}+m_y)m_y'
-4\pi\Phi'(y)
<0.
\tag{6.10}
```

At reverse-isoperimetric branch transitions the same conclusion follows from the one-sided derivative bounds. Since `F_2(y_0)=0`,

```math
F_2(y)\le0
\tag{6.11}
```

for every `y>=y_0`.

This proves (6.1), hence RI.1.

---

## 7. Numerical orientation and exact defining equations

Solving RI.3-RI.4 gives

```math
y_0
=1.4835328716014095360059192473\ldots,
```

```math
\theta_0
=0.3168319797676635467428160269\ldots,
```

```math
p_0=2y_0
=2.9670657432028190720118384946\ldots,
```

and

```math
\Phi(y_0)=B(p_0)
=0.6199319579503434243031685729\ldots .
```

The positive root of RI.7 is

```math
\boxed{
\lambda_{RI}
=0.5934834602360914917813991541\ldots .
}
```

The improvement over the self-contained CSA checkpoint is

```math
0.0001221794938279671961\ldots,
```

and the improvement over FSJC is approximately

```math
0.0052551164624520531\ldots .
```

The decimals only orient the reader. The proof objects are RI.3, RI.4, and RI.7 together with the monotonicity arguments above.

---

## 8. Endpoint strictness

The scalar minimum in Sections 4-6 is attained only when

```math
\frac hD\to y_0,
\qquad
\frac{\operatorname{per}F}{D}\to2y_0,
\tag{8.1}
```

and the central symmetral `S` asymptotically attains the reverse-isoperimetric lower envelope at the same perimeter.

Bogosel's theorem characterizes the corresponding sharp envelope body as a six-gon with one exceptional central angle and five equal central angles. Such a six-gon is **not centrally symmetric** for `theta_0 in (0,pi/3)`: central symmetry of an inscribed six-gon would require its six cyclic central gaps to repeat with period three, whereas the multiset `theta_0,vartheta_0,vartheta_0,vartheta_0,vartheta_0,vartheta_0` contains one exceptional gap.

But every `S` is exactly centrally symmetric. The centrally symmetric diameter-one class is Hausdorff compact, and area and perimeter are continuous. Therefore a sequence of such `S` cannot converge to the unique noncentrally symmetric reverse-isoperimetric optimizer.

Consequently the endpoint `lambda_RI` is itself unattainable, and there is again a qualitative absolute gap above RI.1.

This does **not** yet give another explicit decimal improvement. The next exact problem is the reverse-isoperimetric optimization **within the centrally symmetric subclass**. Solving that subclass should replace the noncentral six-gon lower envelope by its symmetric counterpart and quantify the gap automatically.

---

## 9. Exact remaining convex-geometric lemma

The cleanest next theorem is now independent of most Target C bookkeeping:

> **Centrally symmetric reverse isoperimetry in a disk.** For a centrally symmetric convex body `K` of diameter one and prescribed perimeter `p in [2,pi]`, determine the exact minimum area and its equality family.

At the active perimeter `p≈2.967`, numerical exploration suggests the optimizer is a centrally symmetric inscribed hexagon with two cyclic gap values, rather than the noncentral six-gon from the unrestricted theorem. A proof would feed directly into (3.5) and produce the next explicit Target C floor.

Until that theorem is proved, no sharper symmetric envelope is claimed.

---

## 10. Literature audit

**Source:** Beniamin Bogosel, *A reverse isoperimetric inequality for convex shapes with inclusion constraint*, arXiv:2402.05648v1, 8 February 2024.

**Imported statements:**

1. Theorem 6: the perimeter maximizer at prescribed area among convex subsets of the unit disk is an inscribed polygon, uniquely characterized up to permutation of its side-angle data by one exceptional angle and all remaining angles equal.
2. Proposition 5(c): the maximal perimeter is strictly increasing with the prescribed area.

**Hypothesis check:**

- convexity: `S` is a Minkowski symmetral of the convex force hull;
- unit-disk containment after scaling: exact from central symmetry plus `diam(S)=D`;
- area in `(0,pi)`: true on every nondegenerate asymptotic post-ZF branch;
- no smoothness, strict convexity, or source-point hypothesis is required by the imported theorem.

No claim from the paper about a general non-disk container is used.

---

## 11. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| inverse envelope B(p) | imported theorem + proved inversion | Bogosel Theorem 6 + Proposition 5(c) |
| derivative formula B'(p) | proved | direct differentiation of the imported extremal parameterization |
| force-hull area `>=B(p)D^2-o(D^2)` | proved from imported theorem + FS symmetral | exact containment/scaling and `o(D^2)` area transfer |
| fixed-y perimeter optimizer | proved | four monotonicity cases, using `B'(p)>1/2` in active range |
| unique crossover y_0 | proved | strict endpoint signs and `H'>1/2` |
| global explicit floor `lambda_RI` | proved under external theorem | one-dimensional monotonicity on both sides of y_0 |
| endpoint attainable | rejected qualitatively | unrestricted sharp six-gon is not centrally symmetric, while every symmetral is |
| exact symmetric reverse-isoperimetric envelope | not proved | next convex-geometric obligation |
| Level I | still open | high-surplus post-ZF branches remain |

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

External exact input (Bogosel 2024, arXiv:2402.05648, Thm 6 + Prop 5(c)):
For convex subsets of a disk, maximal perimeter at fixed area is attained by an
inscribed m-gon with one exceptional central angle theta and m-1 equal angles;
the maximal perimeter is strictly increasing in area. Invert this to get the sharp
minimum area B(p) at fixed perimeter p and circumdisk radius D/2.

For p_{m-1}<p<=p_m, p_m=m sin(pi/m):
  p = sin(theta/2)+(m-1)sin((2pi-theta)/(2(m-1))),
  B(p)=1/8[sin theta+(m-1)sin((2pi-theta)/(m-1))],
  B'(p)=1/2[cos(theta/2)+cos((2pi-theta)/(2(m-1)))].

The exact central symmetral S of the force hull has diameter D, perimeter per(F),
is contained in its radius-D/2 disk, and area(S)-area(F)=o(D^2). Therefore
  area(F)/D^2 >= B(p)-o(1), p=per(F)/D.
Combine with FSDB Phi(y)=(y+sin y)/4 and actual-perimeter JC:
  max{Phi(y),B(p)}-pi lambda^2/4
    <= (lambda+min(y,p-y))^2/(4pi).

For fixed y the optimal p is 2y until B(2y)=Phi(y), then the unique p_y with
B(p_y)=Phi(y). There is one crossover y_0 in (2rho,pi/2). It lies on m=6 and is
defined with theta_0 by
  2y_0=sin(theta_0/2)+5sin((2pi-theta_0)/10),
  Phi(y_0)=1/8[sin theta_0+5sin((2pi-theta_0)/5)].
Numerically y_0=1.4835328716014095360..., p_0=2.9670657432028190720....

Then lambda_RI is the positive root
  (pi^2+1)lambda^2+2y_0 lambda+y_0^2-pi(y_0+sin y_0)=0,
so
  liminf (e_BB+2s_C)/D >= 0.59348346023609149178....

The endpoint is not attainable because the unrestricted sharp m=6 optimizer has one
exceptional gap and five equal gaps, hence is not centrally symmetric, whereas S is.
Next exact lemma: solve reverse isoperimetry in the centrally symmetric disk subclass.
```
