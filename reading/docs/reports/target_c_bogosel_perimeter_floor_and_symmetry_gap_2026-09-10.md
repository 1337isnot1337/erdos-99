> Generated reading edition · [exact source](../../../docs/reports/target_c_bogosel_perimeter_floor_and_symmetry_gap_2026-09-10.md) · source SHA-256 `b17f1ca707e938dd687c2a9a8b50c25a239d07bd8823a6326676a6d45ba01c0b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DE3A40C37D44","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — sharp disk reverse isoperimetry raises the C-II floor and excludes its endpoint

**Date:** 2026-09-10  
**Repository state:** branch `research/fs-perimeter-cavity-20260910`, after `ac81bc9112f37135755e847d771084a60c08badc`  
**Run type:** literature import / closing-proof continuation / equality audit  
**Target:** Target C, C-II after ZF/FS/FSDB/FSJC/FDJ/PS  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** used; primary source checked directly  
**Computation:** decimal root evaluation only; no numerical computation is a proof dependency

## LEVEL I STATUS

`STILL OPEN`

The preceding PS report gave the explicit report-level floor

```math
\frac{e_{BB}+2s_C}{D}\ge
0.5933612807422635\ldots-o(1)
```

from an elementary support-function lower bound for the force-hull central symmetral.
This report replaces that nonsharp area bound by the sharp reverse-isoperimetric theorem
of Beniamin Bogosel for convex bodies contained in a disk.

The result has two parts.

First, define `rho` by `rho=cos rho` and define the sharp normalized disk area function
`B(p)` below.  There is a unique

```math
\boxed{y_B\in(2\rho,\pi/2)}
```

such that

```math
\boxed{\mathcal B(2y_B)=\Phi(y_B),
\qquad
\Phi(y)=\frac{y+\sin y}{4}.}
\tag{B.1}
```

Let `lambda_B` be the positive root of

```math
\boxed{
(\pi^2+1)\lambda^2+2y_B\lambda+y_B^2
-\pi(y_B+\sin y_B)=0.
}
\tag{B.2}
```

Then every unbounded post-ZF survivor sequence satisfies

```math
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}\ge\lambda_B.
}
\tag{B.3}
```

Numerically,

```math
\boxed{
y_B=1.4835328716014096\ldots,}
```

```math
\boxed{
\lambda_B=0.5934834602360914\ldots.}
```

This is strictly stronger than the PS floor.

Second, the endpoint `lambda_B` itself is impossible.  Any sequence approaching it
would force the normalized central symmetral of the actual force hull to approach a
Bogosel extremizer.  Here that extremizer is a nonregular six-gon with exactly one
exceptional side.  A nondegenerate centrally symmetric polygon has its sides in
opposite equal pairs, so such a six-gon cannot be centrally symmetric.  Since every
central symmetral is centrally symmetric, compactness gives a contradiction.

Hence there exist absolute constants

```math
\boxed{\varepsilon_B>0,\qquad D_0<\infty}
```

such that every sufficiently large post-ZF survivor satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge\lambda_B+\varepsilon_B.}
\tag{B.4}
```

The new gap is nonexplicit.  Level I remains open because no contradictory universal
upper bound for this currency is known.

---

## 1. Exact closing implication

Write

```math
P_F=\operatorname{per}F,
\qquad
p=\lim P_F/D,
\qquad
y=\lim h/D,
```

```math
t=\lim e_{BB}/D,
\qquad
\lambda=\lim(e_{BB}+2s_C)/D.
```

The audited FS/FSDB/JC/GU chain gives

```math
2\rho\le y\le p\le\pi,
\qquad 0\le t\le\lambda.
\tag{1.1}
```

The PS report used the elementary force-hull area lower bound

```math
\Psi(p)=\frac{p^2}{2\pi}-\frac\pi4.
```

The present implication is

```text
Bogosel Theorem 6 + Proposition 5(c)
    -> sharp area floor B(p) for every convex body in a disk
FS central symmetral S=(F-F)/2
    -> area(F)/D^2 >= B(p)-o(1)
FSDB
    -> independent area floor Phi(y)
actual-perimeter JC + GU
    -> sharp two-parameter necessary inequality
monotonicity of B
    -> unique scalar optimizer y_B and lambda_B
equality audit + exact central symmetry of S
    -> Bogosel endpoint impossible
    -> uniform nonexplicit gap above lambda_B.
```

This uses the global-source FS.4 theorem.  Dense isolated fillings do not supply that
global-minimizer certificate by themselves.

---

## 2. Literature import: Bogosel's reverse isoperimetric theorem

### Source

Beniamin Bogosel, *A reverse isoperimetric inequality for convex shapes with inclusion
constraint*, arXiv:2402.05648v1 (2024), later published in *Journal of Mathematical
Analysis and Applications* 540 (2024), 128636.

Primary source:

`https://arxiv.org/abs/2402.05648`

The imported results are Theorem 6 and Proposition 5(c).

### Exact problem and hypotheses

Let `D_1` be the closed Euclidean unit disk.  For a prescribed area
`A in (0,pi)`, Bogosel considers convex planar bodies

```math
\Omega\subseteq D_1,
\qquad |\Omega|=A,
```

and maximizes `Per(Omega)`.

Theorem 6 proves that a maximizer is an inscribed polygon.  If it has `m` positive
sides, then

```math
(m-1)\sin\frac{2\pi}{m-1}<2A
\le m\sin\frac{2\pi}{m},
\tag{2.1}
```

and its central angles have the form

```math
0<\theta\le \varphi=\cdots=\varphi,
\qquad
\varphi=\frac{2\pi-\theta}{m-1},
\tag{2.2}
```

up to permutation.  Proposition 5(c), applied with total angle `2pi`, proves that the
maximal perimeter is strictly increasing with the prescribed area.

For the polygon in (2.2),

```math
\operatorname{Per}=2\left(
\sin\frac\theta2+(m-1)\sin\frac\varphi2
\right),
\tag{2.3}
```

```math
A=\frac12\left(
\sin\theta+(m-1)\sin\varphi
\right).
\tag{2.4}
```

No lattice, packing, KKT, or symmetry hypothesis occurs in this external theorem.

### Applicability to the force symmetral

For

```math
S=\frac12((F-o)-(F-o)),
```

FD proves

```math
\operatorname{diam}S=D,
\qquad
\operatorname{per}S=P_F,
```

and `S=-S`.  Hence

```math
S\subseteq B(0,D/2).
```

Therefore

```math
\Omega:=\frac2D S
```

is a convex body contained in `D_1`, exactly the container in Bogosel's theorem.
The scaling gives

```math
\operatorname{Per}(\Omega)=2p,
\qquad
|\Omega|=4\operatorname{area}(S)/D^2.
\tag{2.5}
```

Thus the external hypotheses match exactly.

---

## 3. The sharp disk area function

Let

```math
M(A)=\max\{\operatorname{Per}(\Omega):
\Omega\subseteq D_1\text{ convex},\ |\Omega|=A\}.
```

By Bogosel, `M` is strictly increasing on `(0,pi)`.  Extend continuously to the
segment and disk endpoints.  For

```math
2\le p\le\pi
```

define

```math
\boxed{
\mathcal B(p):=\frac14 M^{-1}(2p).}
\tag{3.1}
```

Thus `4 B(p)` is the least area that a convex subset of the unit disk can have while
having perimeter `2p`.

If `Omega subset D_1` has perimeter `2p` and area `A`, then

```math
2p\le M(A),
```

so strict monotonicity gives

```math
A\ge M^{-1}(2p)=4\mathcal B(p).
\tag{3.2}
```

Apply this to (2.5):

```math
\boxed{
\frac{\operatorname{area}S}{D^2}
\ge\mathcal B(P_F/D).}
\tag{3.3}
```

FS.4 and FD give

```math
0\le \operatorname{area}S-\operatorname{area}F=o(D^2),
\tag{3.4}
```

uniformly along unbounded post-ZF survivor sequences.  Therefore if `P_F/D->p`,

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge\mathcal B(p).}
\tag{3.5}
```

Together with FSDB,

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge A_B(y,p):=\max\{\Phi(y),\mathcal B(p)\}.}
\tag{3.6}
```

---

## 4. Monotonicity of the sharp area function

Inside one Bogosel `m`-gon branch, let `theta` be the exceptional central angle and

```math
\varphi=\frac{2\pi-\theta}{m-1}.
```

Equations (2.3)--(2.4), after the normalization in (3.1), give

```math
p(\theta)=
\sin\frac\theta2+(m-1)\sin\frac\varphi2,
\tag{4.1}
```

```math
\mathcal B(p(\theta))
=\frac18\left(\sin\theta+(m-1)\sin\varphi\right).
\tag{4.2}
```

Differentiation yields

```math
\frac{dp}{d\theta}
=\frac12\left(
\cos\frac\theta2-\cos\frac\varphi2
\right)>0
\tag{4.3}
```

away from the regular endpoint, and

```math
\frac{d\mathcal B}{d\theta}
=\frac18(\cos\theta-\cos\varphi).
\tag{4.4}
```

Using

```math
\cos\theta-\cos\varphi
=2\left(
\cos\frac\theta2-\cos\frac\varphi2
\right)
\left(
\cos\frac\theta2+\cos\frac\varphi2
\right),
```

we obtain

```math
\boxed{
\mathcal B'(p)
=\frac12\left(
\cos\frac\theta2+\cos\frac\varphi2
\right).}
\tag{4.5}
```

For `m>=3`,

```math
0\le\frac\theta2\le\frac\pi m,
\qquad
\frac\varphi2\le\frac\pi{m-1},
```

and the minimum possible sum of the two cosines occurs in the degenerate `m=3`
endpoint.  Hence

```math
\boxed{\mathcal B'(p)\ge\frac12}
\tag{4.6}
```

on every smooth branch.  By continuity across regular-polygon transition points,
this integrates to the global secant inequality

```math
\boxed{
\mathcal B(p_2)-\mathcal B(p_1)
\ge\frac{p_2-p_1}{2}
\qquad(2\le p_1\le p_2\le\pi).}
\tag{4.7}
```

This slope bound is the key fact that makes the two-parameter optimization exact.

---

## 5. The new necessary cavity inequality

The actual-perimeter JC theorem gives

```math
E_{out}+Q
\le e_{BB}+\min\{h,P_F-h\}.
\tag{5.1}
```

Hence, with

```math
m(y,p)=\min\{y,p-y\},
```

```math
\limsup\frac G{D^2}
\le\frac{(t+m(y,p))^2}{4\pi}.
\tag{5.2}
```

GU gives

```math
\limsup\frac1{D^2}\sum_r\operatorname{area}(P_r)
\le\frac\pi4\lambda^2.
\tag{5.3}
```

Since

```math
G=\operatorname{area}F-
\sum_r\operatorname{area}(P_r),
```

(3.6) and (5.3) give

```math
\liminf\frac G{D^2}
\ge A_B(y,p)-\frac\pi4\lambda^2.
\tag{5.4}
```

Using `t<=lambda`, every convergent survivor subsequence must therefore satisfy

```math
\boxed{
A_B(y,p)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m(y,p))^2}{4\pi},
\qquad
2\rho\le y\le p\le\pi.}
\tag{5.5}
```

Also every planar convex body of diameter `D` has perimeter at least `2D`, because
each of the two boundary arcs joining a diametral pair has length at least `D`.
Therefore

```math
\boxed{p\ge2.}
\tag{5.6}
```

For fixed `(y,p)`, let `R_B(y,p)` be the least nonnegative `lambda` satisfying (5.5).
It is monotone increasing in the area input `A_B` and monotone decreasing in the cavity
width `m`.

---

## 6. The unique area-floor crossing for fixed diameter density

For fixed `y`, let `p_c(y)` be the unique solution of

```math
\boxed{\mathcal B(p_c(y))=\Phi(y)}
\tag{6.1}
```

in `[max{2,y},pi]`.

### Existence

If `y<=2`, then `B(2)=0<Phi(y)`.

If `2<=y<=pi`, use the disk of radius `y/pi` inside the unit disk.  It has perimeter
`2y` and area `y^2/pi`, so

```math
\mathcal B(y)\le\frac{y^2}{4\pi}.
\tag{6.2}
```

The function

```math
f(y)=y+\sin y-\frac{y^2}{\pi}
```

is concave on `[0,pi]`, with `f(0)=f(pi)=0`.  Hence `f(y)>=0`, and therefore

```math
\mathcal B(y)\le\Phi(y).
\tag{6.3}
```

At the other endpoint,

```math
\mathcal B(\pi)=\frac\pi4\ge\Phi(y),
```

with strict inequality for `y<pi`.  Strict monotonicity of `B` proves existence and
uniqueness of `p_c(y)`.

### Fixed-y optimizer

Before `p_c(y)`, the active area floor is the constant `Phi(y)`.  Increasing `p`
increases `m=p-y` until `p=2y`, after which `m=y`; thus the threshold decreases and
then is constant.

After `p_c(y)`, the active area floor is `B(p)`.  If `p>=2y`, `m=y` is fixed and the
threshold increases with `B(p)`.  If `p<2y`, differentiate the polynomial form of
(5.5) at the root.  Its derivative with respect to `p` is

```math
2(\lambda+m)-4\pi\mathcal B'(p).
```

Here `lambda<1`, `m<pi/2`, and `B'(p)>=1/2`, so

```math
2(\lambda+m)-4\pi\mathcal B'(p)
<2+\pi-2\pi=2-\pi<0.
```

Thus the threshold increases after the crossing here as well.

Consequently

```math
\boxed{
\min_pR_B(y,p)=
\begin{cases}
r(y),&p_c(y)\ge2y,\\
R_B(y,p_c(y)),&p_c(y)\le2y,
\end{cases}}
\tag{6.4}
```

where `r(y)` is the old FSJC left-branch root

```math
(\pi^2+1)r^2+2yr+y^2-\pi(y+\sin y)=0.
\tag{6.5}
```

If `p_c>2y`, any `p in[2y,p_c]` gives the same threshold; this harmless plateau does
not affect the next optimization.

---

## 7. Exact transition `y_B`

For

```math
2\rho\le y\le\pi/2
```

define

```math
g_B(y)=\mathcal B(2y)-\Phi(y).
\tag{7.1}
```

From (4.7), for `y_2>y_1`,

```math
\mathcal B(2y_2)-\mathcal B(2y_1)
\ge y_2-y_1.
```

Also

```math
\Phi'(y)=\frac{1+\cos y}{4}\le\frac12.
```

Therefore

```math
\boxed{
g_B(y_2)-g_B(y_1)\ge\frac12(y_2-y_1)>0.}
\tag{7.2}
```

So `g_B` is strictly increasing.

At the upper endpoint,

```math
\boxed{
g_B(\pi/2)=\frac{\pi-2}{8}>0.}
\tag{7.3}
```

The lower endpoint sign is certified geometrically rather than numerically.

### Exact hexagon witness for `g_B(2rho)<0`

In the unit disk take the inscribed hexagon whose six consecutive central gaps are

```math
\frac\pi{10},\quad
\frac{3\pi}{10},\quad
\frac{2\pi}{5},\quad
\frac{2\pi}{5},\quad
\frac{2\pi}{5},\quad
\frac{2\pi}{5}.
\tag{7.4}
```

Its half-perimeter is

```math
p_W=
\sin\frac\pi{20}
+\sin\frac{3\pi}{20}
+4\sin\frac\pi5
```

```math
=\frac{\sqrt5-1}{2}\cos\frac\pi{20}
+\sqrt{10-2\sqrt5}.
\tag{7.5}
```

Use the elementary rational bounds

```math
\frac{559}{250}<\sqrt5<\frac{161}{72},
\qquad
\pi<\frac{22}{7},
\qquad
\frac{739}{1000}<\rho<\frac{37}{50}.
\tag{7.6}
```

Since `cos x>1-x^2/2`,

```math
\cos\frac\pi{20}
>1-\frac12\left(\frac{11}{70}\right)^2
=\frac{9679}{9800}.
```

Also

```math
\sqrt{10-2\sqrt5}
>\sqrt{\frac{199}{36}}>\frac{47}{20}.
```

Therefore

```math
p_W>
\frac{309}{500}\frac{9679}{9800}
+\frac{47}{20}
=\frac{14505811}{4900000}
>\frac{74}{25}
>4\rho.
\tag{7.7}
```

The normalized area, meaning one quarter of its unit-disk area, is

```math
a_W=
\frac{\sqrt5}{16}
+\frac18\sqrt{10+2\sqrt5}.
\tag{7.8}
```

The same rational bounds give

```math
a_W<
\frac{161}{1152}+\frac{381}{800}
<0.616007.
\tag{7.9}
```

Because `rho=cos rho`,

```math
\Phi(2\rho)
=\frac\rho2\left(1+\sqrt{1-\rho^2}\right).
```

Using (7.6) and

```math
\sqrt{1131}>\frac{3363}{100}
```

gives

```math
\Phi(2\rho)>
\frac{739}{2000}
\left(1+\frac{3363}{5000}\right)
=\frac{6180257}{10000000}
>0.618025.
\tag{7.10}
```

The exact rational gap between the upper bound in (7.9) and the lower bound in
(7.10) is

```math
\frac{22711}{11250000}>0.
\tag{7.11}
```

Now homothetically shrink the witness by the factor `4rho/p_W<1`.  The resulting
convex body remains in the unit disk, has half-perimeter exactly `4rho`, and has
normalized area strictly below `Phi(2rho)`.  Hence

```math
\boxed{\mathcal B(4\rho)<\Phi(2\rho),}
\tag{7.12}
```

so `g_B(2rho)<0`.

By (7.2), (7.3), and (7.12), there is a unique `y_B` satisfying (B.1).

---

## 8. Global optimization in `y`

For `y<=y_B`, `p_c(y)>=2y`, so (6.4) gives the old root `r(y)`.  The audited FSJC
monotonicity calculation proves

```math
\boxed{r'(y)<0\quad(2\rho\le y\le\pi/2).}
\tag{8.1}
```

For `y>=y_B`, the minimizing perimeter is `p_c(y)<=2y`.  The crossing relation and
(4.7) imply for `y_2>y_1`

```math
\frac{p_c(y_2)-p_c(y_1)}{2}
\le
\Phi(y_2)-\Phi(y_1)
\le\frac{y_2-y_1}{2}.
```

Thus

```math
\boxed{p_c(y)-y\text{ is nonincreasing}.}
\tag{8.2}
```

Along the crossing, the active area floor is `Phi(y)`, which is strictly increasing
for `y<pi`, while the cavity width

```math
m=p_c(y)-y
```

is nonincreasing.  The threshold is increasing in area and decreasing in cavity width.
Therefore

```math
\boxed{R_B(y,p_c(y))\text{ is strictly increasing for }y_B\le y<\pi.}
\tag{8.3}
```

The unique global minimum is therefore attained at

```math
\boxed{p=2y=y_B\cdot2.}
\tag{8.4}
```

At this point `m=y_B` and `B(2y_B)=Phi(y_B)`, so the threshold equation is exactly
(B.2).  This proves (B.3).

---

## 9. Exact improvement over the elementary PS floor

The support-function argument in PS in fact has the following general unit-disk form:
for every convex `Omega subset D_1` with perimeter `L`,

```math
|\Omega|\ge\frac{L^2}{2\pi}-\pi.
\tag{9.1}
```

Indeed, for the support function `h` about the disk center,
`h^2+(h')^2<=1` almost everywhere,

```math
|\Omega|
=\frac12\int_0^{2\pi}(h^2-(h')^2)
\ge\int_0^{2\pi}h^2-\pi
\ge\frac{L^2}{2\pi}-\pi.
```

Equality in both steps forces `h` constant and `h^2=1`, hence the unit disk.  Thus for

```math
2<p<\pi
```

Bogosel's attained minimum satisfies the strict inequality

```math
\boxed{\mathcal B(p)>\Psi(p).}
\tag{9.2}
```

Let `y_0` be the PS transition, so

```math
\Psi(2y_0)=\Phi(y_0),
\qquad y_0<\pi/2.
```

Then

```math
g_B(y_0)=\mathcal B(2y_0)-\Phi(y_0)>0.
```

Because `g_B` is increasing and vanishes at `y_B`,

```math
\boxed{y_B<y_0.}
\tag{9.3}
```

Since the old root `r(y)` is strictly decreasing,

```math
\boxed{
\lambda_B=r(y_B)>r(y_0)=\lambda_{PS}.}
\tag{9.4}
```

The improvement is therefore exact, not a floating-point artifact.

---

## 10. Six-gon localization and numerical values

The endpoint lies in Bogosel's six-gon branch.

First,

```math
5\sin\frac\pi5<2.95<4\rho<2y_B.
\tag{10.1}
```

For the first inequality use

```math
\sin\frac\pi5=\frac14\sqrt{10-2\sqrt5}
```

and the lower bound `sqrt5>559/250`; the middle inequality follows from
`rho>739/1000`.

Second, at `y=3/2`,

```math
\mathcal B(3)=\frac{3\sqrt3}{8}
>\frac58
>\Phi(3/2),
\tag{10.2}
```

because `3sqrt3>5` and `sin(3/2)<1`.  Hence `g_B(3/2)>0`, so

```math
y_B<3/2,
\qquad 2y_B<3.
```

Thus

```math
5\sin(\pi/5)<2y_B<6\sin(\pi/6)=3,
```

which is exactly the six-gon perimeter interval.

Let `theta_B in (0,pi/3)` be its exceptional central angle and set

```math
\varphi_B=\frac{2\pi-\theta_B}{5}.
```

Then `(y_B,theta_B)` is characterized by

```math
\boxed{
2y_B=
\sin\frac{\theta_B}{2}
+5\sin\frac{2\pi-\theta_B}{10},}
\tag{10.3}
```

```math
\boxed{
\sin\theta_B
+5\sin\frac{2\pi-\theta_B}{5}
=2(y_B+\sin y_B).}
\tag{10.4}
```

High-precision evaluation gives

```text
rho       = 0.7390851332151607...
y_B       = 1.4835328716014096...
2 y_B     = 2.9670657432028192...
theta_B   = 0.3168319797676689...
phi_B     = 1.1932706654823835...
B(2 y_B) = 0.6199319579503438...
lambda_B = 0.5934834602360914...
```

These decimals are descriptive only.  Equations (B.1)--(B.2), or equivalently
(10.3)--(10.4) plus (B.2), define the constants exactly.

---

## 11. Equality audit: the Bogosel endpoint is impossible

Assume for contradiction that an unbounded post-ZF survivor sequence satisfies

```math
\lambda_D:=\frac{e_{BB}+2s_C}{D}\to\lambda_B.
\tag{11.1}
```

By uniqueness of the global optimizer in Sections 7--8, after passing to subsequences,

```math
\frac hD\to y_B,
\qquad
\frac{P_F}{D}\to2y_B.
\tag{11.2}
```

Let

```math
A_D=\frac{\operatorname{area}F}{D^2},
\qquad
C_D=\frac1{D^2}\sum_r\operatorname{area}(P_r),
\qquad
G_D=A_D-C_D.
```

Bogosel+FS gives

```math
\liminf A_D\ge\mathcal B(2y_B).
\tag{11.3}
```

GU gives

```math
\limsup C_D\le\frac\pi4\lambda_B^2.
\tag{11.4}
```

The actual-perimeter JC bound gives

```math
\limsup G_D
\le\frac{(t+y_B)^2}{4\pi}
\le\frac{(\lambda_B+y_B)^2}{4\pi}.
\tag{11.5}
```

By (B.1)--(B.2), the lower bound from (11.3)--(11.4) equals the final upper bound in
(11.5).  Therefore every inequality must saturate:

```math
\boxed{A_D\to\mathcal B(2y_B),}
\tag{11.6}
```

```math
\boxed{C_D\to\frac\pi4\lambda_B^2,}
\tag{11.7}
```

and

```math
\boxed{t\to\lambda_B.}
\tag{11.8}
```

In particular,

```math
\boxed{\frac{s_C}{D}\to0.}
\tag{11.9}
```

Thus any endpoint sequence would already have to spend asymptotically all of its
pinned/contact currency in actual loaded-loaded contacts.

Now take the exact central symmetral

```math
S_D=\frac12((F-o)-(F-o))
```

and normalize

```math
\Omega_D=\frac2D S_D\subseteq D_1.
```

FS.4 gives `area(S_D)-area(F)=o(D^2)`, so (11.6) yields

```math
|\Omega_D|\to4\mathcal B(2y_B),
\tag{11.10}
```

while (11.2) gives

```math
\operatorname{Per}(\Omega_D)\to4y_B.
\tag{11.11}
```

Every `Omega_D` is centrally symmetric about the origin.

By Blaschke selection, pass to a Hausdorff-convergent subsequence

```math
\Omega_D\to\Omega_\infty\subseteq D_1.
```

Central symmetry, area, and planar convex perimeter are preserved under the limit.
Hence

```math
|\Omega_\infty|=4\mathcal B(2y_B),
```

```math
\operatorname{Per}(\Omega_\infty)=4y_B
=M(4\mathcal B(2y_B)).
```

So `Omega_infty` is a Bogosel perimeter maximizer at its area.

Section 10 places that optimizer strictly inside the nonregular six-gon branch.
Theorem 6 therefore says its six side lengths consist of exactly one exceptional
shorter side and five equal longer sides.

But every side of a nondegenerate centrally symmetric polygon is paired by the
half-turn with a distinct opposite parallel side of equal length.  Consequently every
side length that is unique among the sides is impossible.  The only centrally
symmetric member of Bogosel's six-gon family is the regular endpoint, where all six
sides are equal; here `2y_B<3`, so we are not at that endpoint.

This contradicts the exact central symmetry of `Omega_infty`.

Therefore:

### Theorem BSG — Bogosel/symmetry endpoint exclusion

There is no unbounded post-ZF survivor sequence satisfying (11.1).

---

## 12. Uniform gap above `lambda_B`

### Corollary BSG.1

There exist absolute `epsilon_B>0` and `D_0<infinity` such that every post-ZF survivor
with `D>=D_0` satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}\ge\lambda_B+\varepsilon_B.}
```

### Proof

If not, choose for each integer `j` a post-ZF survivor with `D_j>=j` and

```math
\frac{e_{BB}+2s_C}{D_j}<\lambda_B+\frac1j.
```

Theorem (B.3) gives liminf at least `lambda_B`, so the chosen ratios converge to
`lambda_B`.  This contradicts BSG. `square`

No value of `epsilon_B` is claimed.  Quantifying it requires either stability for
Bogosel's reverse-isoperimetric optimizer under the additional central-symmetry
constraint or a direct centrally symmetric reverse-isoperimetric theorem.

---

## 13. Exact target implication

The strongest explicit post-ZF lower bound becomes

```math
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.5934834602360914\ldots,}
```

and the printed endpoint is itself excluded.  Therefore the actual asymptotic lower
bound is strictly larger by an absolute nonzero amount.

The endpoint audit also proves the structural statement

```math
\lambda_D\to\lambda_B
\quad\Longrightarrow\quad
s_C=o(D),
\qquad e_{BB}/D\to\lambda_B,
```

before the final symmetry contradiction.

The exact Level I face endpoint is still

```math
b+Q>2h,
```

or equivalently exclusion of all post-ZF survivors.  The present theorem remains a
lower bound on a nonnegative survivor currency; there is still no global upper bound
that conflicts with it.

---

## 14. Regression audit

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | its normalized force symmetral tends to the disk, not the nonregular six-gon endpoint; its currency is above the floor |
| dense isolated filling | yes | the area transfer uses full-source FS.4 and does not assume `n-v=o(D^2)` |
| Reuleaux/constant-width limits | yes | the argument applies to the exact central symmetral inside a disk |
| perfect matching shell | yes | already excluded by MFS; no matching hypothesis is used here |
| near-star response regression | yes | no arbitrary response-operator or conductance lower bound is used |
| old FSJC endpoint | yes | already excluded independently by FDJ; the present optimizer occurs at a different perimeter/diameter density |

The decisive use of information absent from shell regressions is FS.4: the actual
force hull of a global source is asymptotically area-equivalent to an exact centrally
symmetric diameter-`D` body about the full-source circumcenter.

---

## 15. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| Bogosel Theorem 6 | literature import, hypotheses checked | exact convex unit-disk fixed-area problem |
| strict monotonicity of maximal perimeter with area | literature import | Proposition 5(c), same normalization |
| sharp force-hull floor `B(p)` | proved from literature + FS.4 | exact scaling and `o(D^2)` area transfer |
| slope `B'(p)>=1/2` | proved | direct differentiation of Bogosel branch formulas |
| unique `y_B` | proved | global slope plus exact lower-end hexagon witness |
| `lambda>=lambda_B` | proved asymptotically | exact two-parameter optimization |
| `lambda_B>lambda_PS` | proved | strict unit-disk support inequality plus monotonic old root |
| endpoint implies `s_C=o(D)` | proved | equality in `t<=lambda` relaxation |
| BSG endpoint exclusion | proved | compactness + Bogosel uniqueness + exact central symmetry |
| explicit `epsilon_B` | not proved | requires quantitative symmetry stability |
| Level I | still open | no universal upper bound on the high-currency branch |

---

## 16. Failed routes and no-go results

1. **Pure scalar iteration.**  Replacing one area constant by another without retaining
   the actual force-hull perimeter loses the optimizer geometry.  The improvement here
   requires the joint `(y,p)` optimization.
2. **Treating Bogosel equality as attainable by the force symmetral.**  This is false
   at the new endpoint because the sharp unconstrained extremizer has one unpaired side.
   The equality mismatch is itself the endpoint contradiction.
3. **Claiming Level I from the lower bound.**  Even after the symmetry gap, the current
   theorem only says the survivor currency is larger.  A contradictory upper bound or
   a direct conversion to `b+Q>2h` is still absent.

---

## 17. Literature audit record

### Beniamin Bogosel (2024)

- Title: *A reverse isoperimetric inequality for convex shapes with inclusion constraint*.
- arXiv: `2402.05648v1`.
- Journal: *Journal of Mathematical Analysis and Applications* 540 (2024), 128636.
- Imported statements: Proposition 5(c), Theorem 6.
- Container: closed Euclidean unit disk.
- Objects: arbitrary planar convex bodies.
- Constraint: prescribed area in `(0,pi)`.
- Objective: maximal Euclidean perimeter.
- Conclusion: unique side-angle multiset of an inscribed polygon, one possibly shorter
  side and all remaining sides equal; maximal perimeter strictly increases with area.
- Scaling used here: `Omega=2S/D`, so `Per(Omega)=2P_F/D` and
  `area(Omega)=4area(S)/D^2`.
- Match to present setting: exact.  No relocation, packing, or optimality assertion is
  imported from the paper; it is used only as convex geometry on the force symmetral.

---

## 18. Computation and reproducibility

No numerical result is a logical proof dependency.  The displayed constants were
evaluated from the exact six-gon equations (10.3)--(10.4) and quadratic (B.2).

The lower-end sign needed for existence and uniqueness is proved by the exact rational
hexagon certificate in Section 7.  The six-gon branch is certified by the exact
inequalities in Section 10.

---

## 19. Canonical promotion recommendation

**Hold as report pending independent audit.**  The literature theorem is primary and
its hypotheses match exactly, but this is the first use of that external theorem in the
Target C stack.  Before promotion, independently check:

1. the inversion from fixed-area maximal perimeter to `B(p)`;
2. the branch derivative and global secant inequality;
3. the equality-compactness argument and Theorem 6 uniqueness wording;
4. the exact six-gon side-pair obstruction.

If those checks pass, promote the sharp force-hull perimeter-area floor and BSG into the
post-FS Target C frontier, and add the Bogosel paper to the literature ledger.

---

## 20. Next run

The strongest next target is a **centrally symmetric reverse-isoperimetric stability
bound**.  BSG proves qualitatively that the sharp unconstrained Bogosel six-gon cannot
be approached by the force symmetral.  A quantitative separation between centrally
symmetric convex bodies and that one-exceptional-side six-gon would turn the
nonexplicit `epsilon_B` into a larger explicit floor.

The more ambitious closing target remains a genuine upper bound on

```math
\frac{e_{BB}+2s_C}{D}
```

or a theorem converting large loaded-loaded contact currency directly into the face
contradiction or a strict sub-`D` competitor.

---

## 21. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Bogosel import:
For convex Omega in the unit disk at fixed area A, maximal perimeter is attained by an
inscribed m-gon with one exceptional central angle and m-1 equal angles; the maximal
perimeter is strictly increasing with A.

Define B(p)=M^{-1}(2p)/4.  For the exact force symmetral S=(F-F)/2,
    area(F)/D^2 >= B(P_F/D)-o(1).
Together with FSDB Phi(y) and actual-perimeter JC:
    max{Phi(y),B(p)}-pi lambda^2/4
      <= (lambda+min{y,p-y})^2/(4pi).
B'(p)>=1/2 on every branch.

There is a unique y_B in (2rho,pi/2) with B(2y_B)=Phi(y_B).  The global threshold is
    lambda_B=0.5934834602360914...,
    y_B=1.4835328716014096...,
strictly above the PS floor.

Endpoint equality would force normalized exact central symmetrals to converge to the
Bogosel extremizer at this area/perimeter.  It is a nonregular six-gon with exactly one
exceptional side, hence cannot be centrally symmetric.  Contradiction.  Therefore
there is a nonexplicit uniform epsilon_B>0 above lambda_B.

Remaining Level I obstruction:
No universal upper bound on lambda=(e_BB+2s_C)/D, and no theorem yet converts the
high-lambda branch to b+Q>2h or a strict sub-D competitor.
```
