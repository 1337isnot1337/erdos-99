> Generated reading edition · [exact source](../../../docs/reports/target_c_centrally_symmetric_reverse_isoperimetric_floor_2026-09-10.md) · source SHA-256 `6ac2ddc60aeadf6f224b17b07c57900fb0e561dd65d44d4ceb9e7e98b085075a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2FDE4B762E23","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — centrally symmetric reverse isoperimetry sharpens C-II again

**Date:** 2026-09-10  
**Repository state:** branch `research/fs-perimeter-cavity-20260910`, after `a8cce5f9ca4ff0912a24bf5461e80138a13f1208`  
**Run type:** closing-proof continuation / convex-geometric theorem / equality audit  
**Target:** Target C, C-II after ZF/FS/FSDB/JC/GU  
**External source used:** Bogosel arXiv:2402.05648v1, especially Theorem 1 and Proposition 5  
**Computation:** decimal root evaluation only; no numerical computation is a proof dependency

## LEVEL I STATUS

`STILL OPEN`

The preceding BSG report imported Bogosel's sharp reverse-isoperimetric theorem for
**all** convex subsets of a disk and obtained

```math
\lambda:=\frac{e_{BB}+2s_C}{D}
\ge0.5934834602360914\ldots-o(1),
```

then excluded equality because the unconstrained extremizer was not centrally
symmetric.

This report removes that qualitative loss.  Bogosel's polygonal proof admits an exact
half-turn-symmetric version.  The resulting theorem completely solves the auxiliary
problem

> among origin-symmetric convex bodies contained in the unit disk and having prescribed
> area, maximize perimeter.

The optimizer is an inscribed centrally symmetric polygon whose central-angle list on
one half-circle consists of one possibly smaller angle and all remaining angles equal.
Using this sharp symmetric area floor in the post-ZF cavity budget gives a new explicit
constant

```math
\boxed{
\lambda_{CS}=0.5935048918881262\ldots .}
\tag{CS.1}
```

More importantly, the endpoint is again impossible, for a different reason.  Equality
would force the normalized force symmetral to converge to a fixed six-gon, while the
exact inclusion

```math
D\,\operatorname{conv}\{\pm u_e:e\in E(H)\}
\subseteq F-F
```

puts `h=Theta(D)` pairwise `Omega(1/D)`-separated points of the unit circle inside that
symmetral.  A fixed inscribed six-gon meets the unit circle in only six points.  C67
turns this into a quantitative counting contradiction.

Therefore there are absolute constants

```math
\boxed{\varepsilon_{CS}>0,\qquad D_0<\infty}
```

such that every sufficiently large post-ZF survivor satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge\lambda_{CS}+\varepsilon_{CS}.}
\tag{CS.2}
```

The gap `epsilon_CS` is not made explicit here.  Level I remains open because no
universal upper bound conflicts with the high-currency branch.

---

## 1. Exact target implication

Let

```math
S=\frac12((F-o)-(F-o))
```

be the exact central symmetral from FD/FS, and normalize

```math
\Omega=\frac2D S.
```

Then

```math
\Omega=-\Omega,
\qquad
\Omega\subseteq B(0,1),
\tag{1.1}
```

```math
\operatorname{Per}(\Omega)=2\frac{P_F}{D},
\qquad
|\Omega|=4\frac{\operatorname{area}S}{D^2}.
\tag{1.2}
```

The new implication is

```text
Bogosel finite-polygon argument, imposed in opposite pairs
    -> exact origin-symmetric disk reverse-isoperimetric theorem
    -> sharp force-symmetral area floor B_CS(p)
FS.4
    -> same asymptotic area floor for F
FSDB + actual-perimeter JC + GU
    -> exact two-parameter survivor inequality
slope of B_CS
    -> unique optimizer y_CS and explicit lambda_CS
endpoint equality
    -> normalized S converges to a fixed inscribed symmetric six-gon
DB/C67
    -> h~y_CS D separated unit-circle directions remain inside normalized S
    -> impossible for a Hausdorff limit meeting S^1 at only six points.
```

The last step uses actual diameter-direction population.  It is absent from a generic
reverse-isoperimetric problem and from dense isolated fillings without the full global
source theorem stack.

---

## 2. A sharp centrally symmetric disk theorem

Let `D_1` be the closed unit disk centered at the origin.  For `A in (0,pi)`, define

```math
M_{cs}(A)=
\max\{\operatorname{Per}(K):
K\subseteq D_1\text{ compact convex},\ K=-K,\ |K|=A\}.
\tag{2.1}
```

### Theorem CSRI — symmetric reverse isoperimetry in a disk

For each `A in (0,pi)`, choose the unique integer `k>=2` satisfying

```math
\boxed{
(k-1)\sin\frac\pi{k-1}<A
\le k\sin\frac\pi k,}
\tag{2.2}
```

where the left side is interpreted as `0` for `k=2`.

Then a maximizer in (2.1) is an origin-symmetric inscribed `2k`-gon.  Up to rotation,
reflection, and permutation compatible with the half-turn, its central gaps are

```math
\boxed{
\alpha,\beta,\ldots,\beta,
\alpha,\beta,\ldots,\beta,}
\tag{2.3}
```

where on each half-circle there is one `alpha` and `k-1` copies of `beta`, with

```math
0<\alpha\le\frac\pi k,
\qquad
\beta=\frac{\pi-\alpha}{k-1},
\tag{2.4}
```

and

```math
\boxed{
\sin\alpha+(k-1)\sin\beta=A.}
\tag{2.5}
```

Its perimeter is

```math
\boxed{
M_{cs}(A)=
4\left(
\sin\frac\alpha2+(k-1)\sin\frac\beta2
\right).}
\tag{2.6}
```

The value `M_cs(A)` is strictly increasing in `A`.  The positive central-gap multiset
is unique.  At the upper endpoint in (2.2) the optimizer is the regular `2k`-gon.

### Source of the argument

Bogosel's Theorem 1 proves that a finite perimeter maximizer at fixed area inside a
disk has no free polygon vertex.  Proposition 5 treats, for arbitrary
`S in (0,2pi]`, the constrained angle problem

```math
\sum\theta_i=S,
\qquad
\sum\sin\theta_i=T,
\qquad
\max\sum\sin(\theta_i/2),
```

and proves that the positive optimizer has one possibly smaller angle and all
remaining angles equal; it also proves stabilization as the allowed number of angles
grows and strict monotonicity in `T`.

CSRI is the `S=pi` version of that argument after pairing every vertex with its
antipode.  The details are included because this symmetric theorem is not stated as
such in the paper.

### Proof

For an integer `n>=2`, let `P_n^{cs}(A)` be the compact class of origin-symmetric
convex polygons contained in `D_1`, having at most `2n` nonredundant vertices and area
at most `A`.  A perimeter maximizer exists.

Take a maximizing polygon and a free vertex `v` with adjacent vertices `a,b`.  Its
antipode `-v` is also a vertex, adjacent to `-a,-b`.  Move `v` along the line through
`v` parallel to `ab` and move `-v` by the opposite displacement.  Each of the two
local triangle areas is unchanged, so total polygon area is unchanged and central
symmetry is preserved.  Exactly as in Bogosel's Theorem 1, the local perimeter
contribution

```math
|v-a|+|v-b|
```

is a strictly convex function along the feasible chord.  At an endpoint either the
moved vertex reaches the unit circle or an adjacent vertex becomes redundant.  The
opposite vertex does the symmetric thing.  Repeating this operation produces a
perimeter-maximizing polygon with no free nonredundant vertices.  Thus an optimizer can
be taken inscribed in `D_1`.

A nondegenerate origin-symmetric inscribed polygon has an even number `2m` of vertices.
Order them cyclically so that

```math
v_{i+m}=-v_i.
```

Let

```math
\theta_i\in(0,\pi),\qquad i=1,\ldots,m,
```

be the central gaps from `v_i` to `v_{i+1}` on one half-circle.  The opposite half has
the same gap list and

```math
\sum_{i=1}^m\theta_i=\pi.
\tag{2.7}
```

The standard inscribed-polygon formulas become

```math
|P|=\sum_{i=1}^m\sin\theta_i,
\tag{2.8}
```

and

```math
\operatorname{Per}(P)
=4\sum_{i=1}^m\sin\frac{\theta_i}{2}.
\tag{2.9}
```

Pad the half-gap list with zeros up to length `n` when necessary.  Bogosel Proposition
5 applies with

```math
S=\pi,
\qquad T=|P|.
```

Part (c) shows that the finite optimum saturates the allowed area `A`: if it had area
`T<A`, increasing `T` within the same padded angle class would strictly increase the
maximum perimeter.  Part (a) says the positive optimizer has one angle no larger than
all others, which are equal.  Parts (b) and the interval criterion in Bogosel equation
(13) show that once `n` is large enough the positive angle list stabilizes, with its
length `k` uniquely determined by (2.2), and equations (2.4)--(2.5) hold.  Equation
(2.9) then gives (2.6).  Part (c) also gives strict increase of the stabilized optimal
perimeter with `A`.

It remains to pass from polygons to arbitrary origin-symmetric convex bodies.  The
class in (2.1) is compact in Hausdorff distance by Blaschke selection, so a maximizer
`K_*` exists.  Approximate `K_*` from inside by origin-symmetric polygons `Q_j`
obtained by taking finitely many boundary points in antipodal pairs and their convex
hull.  Then

```math
Q_j\to K_*,
\qquad
|Q_j|\to|K_*|=A,
\qquad
\operatorname{Per}(Q_j)\to\operatorname{Per}(K_*).
\tag{2.10}
```

For large `j`, compare `Q_j` with the finite symmetric optimum having the same vertex
budget and area allowance `A`.  By the stabilization just proved, the latter is the
fixed polygon (2.3), independent of the enlarged budget.  Hence

```math
\operatorname{Per}(Q_j)\le M_{cs}(A).
```

Pass to the limit in (2.10).  The polygon (2.3) is itself feasible, so equality holds
and it is a global maximizer.  This proves CSRI. `square`

### Audit of the paired-vertex modification

The only change to Bogosel's finite proof is that a free vertex is moved together with
its antipode.  The two modified local triangles are disjoint except in degenerate
small-vertex cases, have equal area changes with opposite copies, and each area change
is zero because the motion is parallel to the corresponding adjacent diagonal.  The
half-turn therefore preserves convexity, origin symmetry, containment, and the exact
area constraint.  If an endpoint makes a vertex redundant, its antipode is redundant
as well, so the reduced polygon remains origin-symmetric.

---

## 3. Sharp symmetric area floor as a function of perimeter

Because `M_cs` is strictly increasing, define the inverse normalized area floor

```math
\boxed{
\mathcal B_{cs}(p)=\frac14M_{cs}^{-1}(2p),
\qquad 2<p<\pi.}
\tag{3.1}
```

The endpoint values are understood by continuity.  If `K=-K`, `K subset D_1`, and
`Per(K)=2p`, then

```math
\boxed{|K|/4\ge\mathcal B_{cs}(p).}
\tag{3.2}
```

For a `k`-branch, use `alpha` as parameter and put

```math
\beta=\frac{\pi-\alpha}{k-1}.
```

Then

```math
p(\alpha)=
2\left(
\sin\frac\alpha2+(k-1)\sin\frac\beta2
\right),
\tag{3.3}
```

```math
\mathcal B_{cs}(p(\alpha))
=\frac14\left(
\sin\alpha+(k-1)\sin\beta
\right).
\tag{3.4}
```

Differentiating gives

```math
\frac{dp}{d\alpha}
=\cos\frac\alpha2-\cos\frac\beta2,
\tag{3.5}
```

```math
\frac{d\mathcal B_{cs}}{d\alpha}
=\frac14(\cos\alpha-\cos\beta),
```

hence

```math
\boxed{
\mathcal B_{cs}'(p)
=\frac12\left(
\cos\frac\alpha2+\cos\frac\beta2
\right)\ge\frac12.}
\tag{3.6}
```

As in the BSG report, continuity across regular-polygon transitions gives the global
secant form

```math
\boxed{
\mathcal B_{cs}(p_2)-\mathcal B_{cs}(p_1)
\ge\frac{p_2-p_1}{2}.}
\tag{3.7}
```

Since the unconstrained Bogosel class contains the centrally symmetric class,

```math
\mathcal B_{cs}(p)\ge\mathcal B(p).
\tag{3.8}
```

The inequality is strict on the nonregular six-gon interval because BSG already
identified the unique unconstrained optimizer there as having one unpaired exceptional
side.

---

## 4. Diameter directions also force a perimeter floor

This auxiliary consequence of DB/C67 is useful for checking the normalization.

Recall

```math
P_H=D\,\operatorname{conv}\{\pm u_e:e\in E(H)\}
\subseteq F-F=2S.
\tag{4.1}
```

Therefore

```math
P_H/D\subseteq\Omega=2S/D.
\tag{4.2}
```

Let the `h` projective direction gaps be `g_i`, so

```math
\sum_i g_i=\pi,
\qquad
g_i\ge\delta_D:=2\arcsin\frac1{2D}.
```

The perimeter of the radius-one polygon `P_H/D` is

```math
4\sum_{i=1}^h\sin\frac{g_i}{2}.
```

Concavity again minimizes this at `h-1` gaps equal to `delta_D` and one residual gap.
Since convex perimeter is monotone under inclusion,

```math
2\frac{P_F}{D}=\operatorname{Per}(\Omega)
\ge
4\left[
(h-1)\sin\frac{\delta_D}{2}
+\cos\frac{(h-1)\delta_D}{2}
\right].
\tag{4.3}
```

Along `h/D->y`, `P_F/D->p`, this gives

```math
\boxed{
p\ge y+2\cos\frac y2.}
\tag{4.4}
```

The right side is increasing on `[0,pi]`.  At the DB endpoint `y=2rho`,

```math
y+2\cos(y/2)=2\rho+2\cos\rho=4\rho.
```

Thus every survivor limit satisfies

```math
\boxed{p\ge4\rho>2.956.}
\tag{4.5}
```

This places the relevant symmetric reverse-isoperimetric problem safely in the
positive-area polygonal regime.

---

## 5. Transfer to the actual force hull

Normalize the exact central symmetral as in (1.1).  By (3.2), if `P_F/D->p`,

```math
\frac{\operatorname{area}S}{D^2}
\ge\mathcal B_{cs}(p).
\tag{5.1}
```

FS.4 gives

```math
0\le\operatorname{area}S-\operatorname{area}F=o(D^2).
```

Hence

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge\mathcal B_{cs}(p).}
\tag{5.2}
```

FSDB independently gives

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge\Phi(y):=\frac{y+\sin y}{4}.
\tag{5.3}
```

Therefore

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge A_{cs}(y,p):=
\max\{\Phi(y),\mathcal B_{cs}(p)\}.}
\tag{5.4}
```

---

## 6. Cavity inequality and fixed-`y` optimizer

The actual-perimeter JC bound and GU are unchanged:

```math
\limsup\frac G{D^2}
\le\frac{(t+m)^2}{4\pi},
\qquad
m=\min\{y,p-y\},
\tag{6.1}
```

```math
\limsup\frac1{D^2}\sum_r\operatorname{area}(P_r)
\le\frac\pi4\lambda^2,
\tag{6.2}
```

with `0<=t<=lambda`.  Thus every survivor limit satisfies

```math
\boxed{
A_{cs}(y,p)-\frac\pi4\lambda^2
\le\frac{(\lambda+m)^2}{4\pi}.}
\tag{6.3}
```

For fixed `y`, let `p_c^{cs}(y)` be the unique crossing

```math
\boxed{
\mathcal B_{cs}(p_c^{cs}(y))=\Phi(y).}
\tag{6.4}
```

Existence follows exactly as in the BSG report.  Before the crossing the area floor is
constant and increasing `p` increases the cavity width until `p=2y`.  After the
crossing the area floor increases.  If the crossing occurs below `2y`, (3.6) gives

```math
2(\lambda+m)-4\pi\mathcal B_{cs}'(p)
<2-\pi<0,
```

so the threshold increases after the crossing.  Therefore

```math
\boxed{
\min_pR_{cs}(y,p)=
\begin{cases}
r(y),&p_c^{cs}(y)\ge2y,\\
R_{cs}(y,p_c^{cs}(y)),&p_c^{cs}(y)\le2y,
\end{cases}}
\tag{6.5}
```

where

```math
(\pi^2+1)r(y)^2+2yr(y)+y^2-\pi(y+\sin y)=0.
\tag{6.6}
```

The additional perimeter floor (4.4) does not cut off this optimizer; at the eventual
transition it is strict.

---

## 7. Unique transition `y_CS`

Define

```math
g_{cs}(y)=\mathcal B_{cs}(2y)-\Phi(y),
\qquad 2\rho\le y\le\pi/2.
\tag{7.1}
```

The slope bound (3.7) gives, for `y_2>y_1`,

```math
g_{cs}(y_2)-g_{cs}(y_1)
\ge\frac12(y_2-y_1)>0.
\tag{7.2}
```

At `y=pi/2`,

```math
g_{cs}(\pi/2)=\frac{\pi-2}{8}>0.
\tag{7.3}
```

It remains to certify the lower endpoint sign without floating point.

### Symmetric hexagon witness

Take the origin-symmetric inscribed hexagon whose half-circle gap list is

```math
\alpha=\frac{11\pi}{60},
\qquad
\beta=\frac{49\pi}{120},
\qquad
\beta=\frac{49\pi}{120},
\tag{7.4}
```

and repeat this list after a half-turn.  Since `alpha+2beta=pi`, this is a valid
centrally symmetric inscribed hexagon.

Its half-perimeter is

```math
p_W^{cs}
=2\left(
\sin\frac{11\pi}{120}
+2\sin\frac{49\pi}{240}
\right).
\tag{7.5}
```

Use

```math
\frac{333}{106}<\pi<\frac{355}{113}
```

and the alternating Taylor lower bound

```math
\sin x>x-\frac{x^3}{6}+\frac{x^5}{120}-\frac{x^7}{5040}
\qquad(0<x<1).
```

Substitution of the lower rational bound `333/106` into both positive arguments gives,
by exact rational arithmetic,

```math
\boxed{p_W^{cs}>\frac{2961}{1000}>\frac{74}{25}>4\rho.}
\tag{7.6}
```

Its normalized area is

```math
a_W^{cs}
=\frac14\left(
\sin\frac{11\pi}{60}
+2\sin\frac{49\pi}{120}
\right).
\tag{7.7}
```

For both arguments, the alternating upper bound

```math
\sin x<x-\frac{x^3}{6}+\frac{x^5}{120}
```

is valid.  Substituting `pi<355/113` gives by exact rational arithmetic

```math
\boxed{a_W^{cs}<\frac{61613}{100000}.}
\tag{7.8}
```

From the Dottie bounds already used in the FSJC/BSG audits,

```math
\Phi(2\rho)>
\frac{6180257}{10000000}.
\tag{7.9}
```

Thus `a_W^{cs}<Phi(2rho)`.  Shrink the witness homothetically by the factor
`4rho/p_W^{cs}<1`.  It remains origin-symmetric and contained in the unit disk, now has
half-perimeter exactly `4rho`, and has still smaller normalized area.  Therefore

```math
\boxed{
\mathcal B_{cs}(4\rho)<\Phi(2\rho).}
\tag{7.10}
```

Hence `g_cs(2rho)<0`.  By (7.2)--(7.3) there is a unique

```math
\boxed{y_{CS}\in(2\rho,\pi/2)}
```

with

```math
\boxed{\mathcal B_{cs}(2y_{CS})=\Phi(y_{CS}).}
\tag{7.11}
```

---

## 8. Global optimization and the explicit constant

For `y<=y_CS`, the crossing lies at or beyond `2y`, so the fixed-`y` threshold is
`r(y)`.  The audited FSJC calculation gives `r'(y)<0` on `[2rho,pi/2]`.

For `y>=y_CS`, the crossing lies at or below `2y`.  The secant slope (3.7) and
`Phi'(y)<=1/2` imply

```math
p_c^{cs}(y_2)-p_c^{cs}(y_1)
\le y_2-y_1,
```

so

```math
p_c^{cs}(y)-y
```

is nonincreasing.  Along the crossing, `Phi(y)` strictly increases while the cavity
width does not increase.  The threshold therefore strictly increases.

Thus the unique global minimum occurs at

```math
\boxed{y=y_{CS},\qquad p=2y_{CS}.}
\tag{8.1}
```

Let `lambda_CS` be the positive root

```math
\boxed{
(\pi^2+1)\lambda^2
+2y_{CS}\lambda+y_{CS}^2
-\pi(y_{CS}+\sin y_{CS})=0.}
\tag{8.2}
```

Then every unbounded post-ZF survivor sequence satisfies

```math
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}\ge\lambda_{CS}.}
\tag{8.3}
```

Because `B_cs>=B` and the inequality is strict at the BSG six-gon optimizer,

```math
y_{CS}<y_B,
```

while `r` is strictly decreasing.  Hence

```math
\boxed{\lambda_{CS}>\lambda_B}
\tag{8.4}
```

exactly.

---

## 9. Endpoint lies in the symmetric six-gon branch

The regular origin-symmetric `2k`-gon half-perimeter is

```math
p_k=2k\sin\frac\pi{2k}.
```

At the lower domain endpoint, `2y_CS>4rho>2sqrt2=p_2`.  At `y=3/2`,

```math
\mathcal B_{cs}(3)=\frac{3\sqrt3}{8}
>\frac58>\Phi(3/2),
```

so `y_CS<3/2` and `2y_CS<3=p_3`.  Therefore the transition is strictly inside the
`k=3` branch, whose full optimizer is a centrally symmetric six-gon.

Let `alpha_CS in (0,pi/3)` and

```math
\beta_{CS}=\frac{\pi-\alpha_{CS}}2.
```

Equations (3.3)--(3.4) and (7.11) give the exact system

```math
\boxed{
y_{CS}
=\sin\frac{\alpha_{CS}}2
+2\sin\frac{\pi-\alpha_{CS}}4,}
\tag{9.1}
```

```math
\boxed{
\sin\alpha_{CS}
+2\sin\frac{\pi-\alpha_{CS}}2
=y_{CS}+\sin y_{CS}.}
\tag{9.2}
```

High-precision evaluation gives

```text
y_CS       = 1.4830717169804213...
2 y_CS     = 2.9661434339608426...
alpha_CS   = 0.6074361715630996...
beta_CS    = 1.2670782410133468...
B_CS       = 0.6198065950906754...
lambda_CS  = 0.5935048918881262...
```

The exact theorem is defined by (7.11), (8.2), or equivalently (9.1)--(9.2) and
(8.2).  The decimals are not proof inputs.

---

## 10. Equality audit before the final contradiction

Assume for contradiction that an unbounded post-ZF survivor sequence has

```math
\lambda_D:=\frac{e_{BB}+2s_C}{D}\to\lambda_{CS}.
\tag{10.1}
```

By uniqueness of the optimization,

```math
\frac hD\to y_{CS},
\qquad
\frac{P_F}{D}\to2y_{CS}.
\tag{10.2}
```

Exactly as in the BSG equality ledger, the lower area bound, GU upper cell-area bound,
and JC upper cavity bound meet at equality.  Hence

```math
\boxed{
\frac{\operatorname{area}F}{D^2}
\to\mathcal B_{cs}(2y_{CS})=\Phi(y_{CS}),}
\tag{10.3}
```

and the relaxation `t<=lambda` must also saturate:

```math
\boxed{
\frac{e_{BB}}D\to\lambda_{CS},
\qquad
\frac{s_C}{D}\to0.}
\tag{10.4}
```

FS.4 gives

```math
\operatorname{area}S-\operatorname{area}F=o(D^2).
```

Normalize

```math
\Omega_D=2S/D.
```

Then

```math
|\Omega_D|\to4\mathcal B_{cs}(2y_{CS}),
\qquad
\operatorname{Per}(\Omega_D)\to4y_{CS}.
\tag{10.5}
```

Every `Omega_D` is origin-symmetric and lies in the unit disk.  By Blaschke selection,
pass to a Hausdorff-convergent subsequence

```math
\Omega_D\to\Omega_\infty.
```

Area and perimeter are continuous for planar convex bodies.  Thus `Omega_infty`
attains the CSRI maximum perimeter at area `4 B_cs(2y_CS)`.  Section 9 identifies it as
a fixed nonregular origin-symmetric inscribed six-gon of the form

```math
H_{CS}.
\tag{10.6}
```

Up to a further subsequence, its rotation and the finite choice of gap ordering are
fixed.

This is not yet a contradiction: unlike the unconstrained Bogosel optimizer, `H_CS`
is centrally symmetric.  The missing information comes from the actual diameter
population.

---

## 11. Diameter-direction crowding excludes the symmetric six-gon endpoint

DB gives the exact inclusion

```math
P_H
=D\operatorname{conv}\{\pm u_e:e\in E(H)\}
\subseteq F-F=2S.
```

After normalization,

```math
\boxed{
\pm u_e\in\Omega_D\cap S^1
\qquad\text{for every diameter edge }e.}
\tag{11.1}
```

C67 gives projective separation

```math
\operatorname{dist}_{\mathbb{RP}^1}(u_e,u_f)
\ge\delta_D=2\arcsin\frac1{2D},
\qquad e\ne f,
\tag{11.2}
```

with

```math
D\delta_D\to1.
\tag{11.3}
```

The fixed inscribed hexagon `H_CS` intersects the unit circle exactly in its six
vertices.  Modulo antipodes these are three projective directions, call their set
`V_{proj}`.

Fix any `eta>0`.  Since

```math
H_{CS}\cap S^1
```

is finite, compactness gives a positive Euclidean distance between `H_CS` and the
closed set of unit-circle points whose projective angular distance from `V_proj` is at
least `eta`.  Hausdorff convergence `Omega_D->H_CS` therefore implies that, for all
large `D`, every point of `Omega_D cap S^1` lies within projective angular distance
`eta` of one of the three directions in `V_proj`.

By (11.1), all `h` actual projective diameter directions must lie in those three
intervals.  Each interval has projective length `2eta`.  The separation (11.2) permits
at most

```math
\frac{2\eta}{\delta_D}+1
```

points in one interval.  Therefore

```math
h\le3\left(\frac{2\eta}{\delta_D}+1\right).
\tag{11.4}
```

Divide by `D` and use (11.3):

```math
\limsup\frac hD\le6\eta.
```

Since `eta>0` was arbitrary,

```math
\lim\frac hD=0.
```

But (10.2) gives

```math
\frac hD\to y_{CS}>2\rho>0.
```

Contradiction.

### Theorem CSDC — symmetric reverse-isoperimetric endpoint exclusion

There is no unbounded post-ZF survivor sequence satisfying (10.1).

This contradiction uses only three ingredients after the scalar equality ledger:

1. exact central symmetry of `S`;
2. exact containment of **every** diameter direction in `2S/D`;
3. C67's `Theta(1/D)` projective separation for `h=Theta(D)` directions.

It does not need an operator norm bound, a small-isolate hypothesis, or a matching
assumption.

---

## 12. Uniform gap above `lambda_CS`

### Corollary CSDC.1

There exist absolute constants `epsilon_CS>0` and `D_0` such that every post-ZF
survivor with `D>=D_0` satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge\lambda_{CS}+\varepsilon_{CS}.}
```

### Proof

Otherwise choose survivors with `D_j>=j` and ratios below
`lambda_CS+1/j`.  The explicit floor (8.3) forces the ratios to converge to
`lambda_CS`, contradicting CSDC. `square`

The proof is uniform over all lexicographically selected C-II sources and retains all
contact-isolated points because FS.4 does.

---

## 13. Exact effect on the Level I endpoint

The current report-level lower-bound ladder becomes

```math
0.4702
<0.5882283437\ldots
<0.5933612807\ldots
<0.5934834602\ldots
<\boxed{0.5935048918\ldots},
```

and the last displayed endpoint is itself excluded by CSDC.

This is not Level I.  The theorem still pushes the survivor currency upward rather than
proving the missing upper bound

```math
b+Q>2h
```

or constructing a strict sub-`D` competitor.

The equality audit does yield a useful near-endpoint normal form before contradiction:

```math
\lambda\downarrow\lambda_{CS}
\Longrightarrow
\frac{s_C}{D}\to0,
\quad
\frac{e_{BB}}D\to\lambda_{CS},
\quad
\frac hD\to y_{CS},
\quad
\frac{P_F}{D}\to2y_{CS}.
```

So low-currency survivors cannot spend a linear fraction of their budget in extra
pinned self-stress.

---

## 14. Regression audit

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | normalized symmetral tends to the disk, whose unit-circle contact set is continuous; no finite-polygon equality is asserted |
| dense isolated filling | yes | all source isolates are retained; FS.4 is the only source-to-symmetral transfer |
| perfect matching | yes | no matching assumption enters; the branch is independently excluded elsewhere |
| near-star response | yes | no conductance or arbitrary-boundary-data response bound is used |
| centrally symmetric hexagon | yes | a fixed symmetric hexagon can attain CSRI, but CSDC uses `h=Theta(D)` actual separated diameter directions, which such a fixed-polygon limit cannot absorb |
| FSDB arc concentration | yes | no assumption that the DB area minimizer is attained is needed for CSDC |

The decisive information absent from generic convex-geometric regressions is the
linear population of actual diameter directions and their exact inclusion in the
normalized force symmetral.

---

## 15. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| CSRI finite polygon theorem | proved from Bogosel Theorem 1 mechanism + Proposition 5 | paired free-vertex motion preserves symmetry and area |
| CSRI general convex-body theorem | proved | symmetric polygon approximation + finite stabilization |
| `B_cs'(p)>=1/2` | proved | direct branch differentiation |
| diameter-direction perimeter floor (4.4) | proved | exact DB inclusion + C67 + convex perimeter monotonicity |
| unique `y_CS` | proved | secant slope + exact symmetric hexagon witness |
| explicit `lambda_CS` floor | proved asymptotically | same exact JC/GU optimization with sharper area input |
| endpoint `s_C=o(D)` | proved | equality in `t<=lambda` relaxation |
| CSDC endpoint exclusion | proved | Blaschke compactness + finite circle-contact set + C67 crowding |
| explicit `epsilon_CS` | not proved | needs quantitative stability/crowding estimate |
| Level I closure | not proved | no universal high-currency upper bound |

---

## 16. Literature audit

Primary source checked directly:

Beniamin Bogosel, *A reverse isoperimetric inequality for convex shapes with inclusion
constraint*, arXiv:2402.05648v1 (2024), later JMAA 540 (2024), 128636.

Used facts:

- Theorem 1: a finite polygonal perimeter maximizer in the disk at fixed area has no
  free nonredundant vertex; its proof uses an area-preserving motion parallel to the
  adjacent diagonal and strict convexity of the two-edge length sum.
- Proposition 5(a): for the angle optimization with arbitrary total angle
  `S in (0,2pi]`, positive optimizing angles have one possibly smaller value and all
  remaining values equal.
- Proposition 5(b): the positive angle list stabilizes as the allowed number of angles
  grows.
- Proposition 5(c): the maximal objective is strictly increasing in the sine-sum/area
  parameter.

The paper states the final theorem for arbitrary convex bodies with total angle
`S=2pi`.  The origin-symmetric theorem CSRI is new here; it is obtained by the explicit
paired-vertex reduction to `S=pi`, not quoted as a theorem from the paper.

---

## 17. Computation and reproducibility

No computation is a proof dependency.  The exact lower-end witness in Section 7 uses
alternating Taylor inequalities and rational bounds for `pi` and the Dottie number.
The numerical constants are evaluations of the exact equations (7.11), (8.2), and
(9.1)--(9.2).

The scratch numerical solution gives

```text
y_CS       = 1.4830717169804213...
2 y_CS     = 2.9661434339608426...
alpha_CS   = 0.6074361715630996...
beta_CS    = 1.2670782410133468...
B_CS       = 0.6198065950906754...
lambda_CS  = 0.5935048918881262...
```

The current theorem should be audited symbolically from its exact equations; the
decimal values are only orientation.

---

## 18. Concurrent repository change

While this branch was active, `main` advanced from `a64364e1...` to
`f977f2d0d25f5022c2a587e59cab38375d85caee`, whose commit message is

`Audit: correct FS matching-exclusion provenance`.

That change records that NB already excludes perfect matching quantitatively and
retains MFS as an independent reproof.  It does not change FS, FSDB, JC, GU, DB, C67,
or any dependency used here.  This report therefore keeps its original state lock
rather than silently rebasing mathematical inputs mid-run.

---

## 19. Promotion recommendation

**Hold pending independent audit.**  If the paired-vertex adaptation and general-body
limit survive review, CSRI is a reusable convex-geometric theorem and should be
recorded in the post-FS Target C stack.  CSDC is then the preferred endpoint audit over
the weaker unconstrained-six-gon mismatch, because it uses the exact source diameter
population and applies to the correct symmetric class.

Do not promote the numerical `epsilon_CS`; only existence is proved.

---

## 20. Exact next obligation

The immediate quantitative target is a joint area/perimeter/direction theorem.
CSDC shows why taking only

```math
\max\{\Phi(y),\mathcal B_{cs}(p)\}
```

loses information: equality in the symmetric reverse-isoperimetric bound has only
finitely many circle contacts, whereas DB supplies `Theta(D)` separated circle contacts.

A useful next theorem would lower-bound the area of an origin-symmetric
`Omega subset D_1` from the triple

```math
\left(
\frac12\operatorname{Per}\Omega,
\quad h/D,
\quad \{\pm u_e\}\subset\Omega\cap S^1
\right)
```

with the C67 separation built in.  Any explicit positive strengthening at the
`(y_CS,2y_CS)` equality geometry raises the scalar floor again.  A genuinely closing
version would instead convert the resulting large loaded-loaded contact population
into `b+Q>2h` or a strict sub-`D` competitor.

---

## 21. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New theorem CSRI:
Among origin-symmetric convex bodies K in the unit disk with fixed area A, the maximal
perimeter is attained by an inscribed centrally symmetric 2k-gon.  On one half-circle
its central gaps are alpha,beta,...,beta with alpha+(k-1)beta=pi.  This is obtained by
pairing Bogosel's free-vertex motion and applying Proposition 5 with total angle S=pi.

Define B_cs(p)=M_cs^{-1}(2p)/4.  For the exact force symmetral,
    area(F)/D^2 >= B_cs(P_F/D)-o(1).
Combining with FSDB, JC and GU yields a unique transition
    B_cs(2 y_CS)=Phi(y_CS),
    y_CS=1.4830717169804213...,
and
    lambda_CS=0.5935048918881262....
This strictly improves the Bogosel-unconstrained floor.

New theorem CSDC:
The lambda_CS endpoint cannot occur.  Equality would make normalized symmetrals
converge to a fixed inscribed symmetric six-gon.  But DB puts every diameter direction
on the unit circle inside each symmetral; C67 separates h~y_CS D projective directions
by delta_D~1/D.  A Hausdorff limit six-gon has only three projective unit-circle
vertices, whose shrinking neighborhoods can contain only o(D) such directions.
Contradiction.  Hence a uniform nonexplicit epsilon_CS>0 exists above lambda_CS.

Remaining Level I obstruction:
No contradictory upper bound for lambda=(e_BB+2s_C)/D and no direct conversion of the
high-currency branch to b+Q>2h or a strict sub-D competitor.
```
