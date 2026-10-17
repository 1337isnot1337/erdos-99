> Generated reading edition · [exact source](../../../docs/reports/target_c_difference_body_area_metric_fork_2026-09-09.md) · source SHA-256 `349b73dc0d32151b435c605f925cfc446e42825382f204c3fac55e57a7a0a497`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-05A292891F34","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — difference-body area bound and missing-side metric fork

**Date:** 2026-09-09  
**Run type:** exact convex-geometry theorem / quantitative post-ZF fork  
**Target:** Target C C-II after ZF  
**Depends on:** DB projective diameter-direction separation, NM branching inequality, PC missing-hull-side metric identity, planar Rogers--Shephard area inequality (self-contained in Target B Section 26)  
**Computation:** only evaluation of displayed constants; not used in the proof

## LEVEL I STATUS

`STILL OPEN`

DB uses the diameter-direction polygon in the difference body to obtain a perimeter lower bound. The same polygon also gives an exact **area** lower bound. This becomes stronger than the existing `sqrt(3)D^2/4` force-hull area floor once the diameter-edge density is sufficiently above its DB minimum.

At the same time, DB plus NM gives a lower bound on the total metric excess of the missing force-hull sides. The two bounds move in opposite directions as `h/D` varies, producing a quantitative fork.

---

## 1. Diameter-direction polygon area

Let the full diameter graph have `h` edges. Choose one unoriented direction for each diameter edge and write the projective directions in cyclic order as

```math
\theta_1,\ldots,\theta_h\in\mathbb R/\pi\mathbb Z.
```

Let

```math
g_i:=\theta_{i+1}-\theta_i
```

be the positive projective gaps, cyclically, so

```math
\sum_{i=1}^h g_i=\pi.
\tag{DA.1}
```

DB proves the exact separation

```math
\boxed{g_i\ge2a_D,\qquad a_D:=\arcsin\frac1{2D}.}
\tag{DA.2}
```

For every diameter edge with unit direction `u_i`, the difference body contains both vectors `+-D u_i`. Hence

```math
P_H:=D\,\operatorname{conv}\{\pm u_1,\ldots,\pm u_h\}
\subseteq F-F.
\tag{DA.3}
```

The vertices of `P_H` lie on the radius-`D` circle. Its full `2h` cyclic gap list is `g_1,...,g_h,g_1,...,g_h`. Therefore the triangle-from-the-origin area formula gives

```math
\boxed{
\operatorname{area}(P_H)
=D^2\sum_{i=1}^h\sin g_i.
}
\tag{DA.4}
```

---

## 2. Minimize the sine sum under the diameter separation

The function `sin t` is concave on `[0,pi]`. On the polytope

```math
g_i\ge2a_D,
\qquad
\sum_i g_i=\pi,
```

a concave function attains its minimum at an extreme point. Thus `h-1` gaps take the lower value `2a_D` and the remaining gap absorbs the rest.

The feasibility relation `2h a_D<=pi` follows already from summing DA.2, so the remaining gap is at least `2a_D`.

Hence

```math
\boxed{
\sum_i\sin g_i
\ge
(h-1)\sin(2a_D)
+\sin\bigl(2(h-1)a_D\bigr).
}
\tag{DA.5}
```

The second sine appears because

```math
\sin\bigl(\pi-2(h-1)a_D\bigr)
=\sin\bigl(2(h-1)a_D\bigr).
```

---

## 3. Rogers--Shephard transfers difference-body area to the force hull

The planar Rogers--Shephard inequality is

```math
\operatorname{area}(F-F)\le6\operatorname{area}(F).
\tag{DA.6}
```

Target B Section 26 contains a self-contained planar proof via the covariogram and Brunn--Minkowski, so no external equality or regularity hypothesis is being imported here.

Since `P_H subset F-F`, DA.4--DA.6 give:

### Theorem DA — exact difference-body area floor

```math
\boxed{
\operatorname{area}(F)
\ge
\frac{D^2}{6}
\left[
(h-1)\sin(2a_D)
+\sin\bigl(2(h-1)a_D\bigr)
\right].
}
\tag{DA.7}
```

This theorem uses the full actual diameter directions of the same post-ZF source. It is independent of contact-core population and exceptional-face topology.

---

## 4. Asymptotic form

Along a subsequence with

```math
\frac hD\to y,
```

one has

```math
2Da_D\to1,
\qquad
(h-1)\sin(2a_D)\to y,
\qquad
2(h-1)a_D\to y.
```

Thus DA gives

```math
\boxed{
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge
A_{DB}(y):=\frac{y+\sin y}{6}.
}
\tag{DA.8}
```

On the relevant range `0<y<pi`, `A_DB` is nondecreasing because

```math
A_{DB}'(y)=\frac{1+\cos y}{6}\ge0.
```

The existing DB direction-spread theorem independently gives

```math
\operatorname{area}(F)\ge\frac{\sqrt3}{4}D^2.
```

Therefore the combined floor is

```math
\boxed{
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge
\max\left\{\frac{\sqrt3}{4},\frac{y+\sin y}{6}\right\}.
}
\tag{DA.9}
```

The new area term becomes stronger at the unique solution of

```math
y+\sin y=\frac{3\sqrt3}{2},
```

namely

```math
y=1.5984587929\ldots .
\tag{DA.10}
```

---

## 5. Missing-hull-side metric excess

Let `a` be the number of missing force-hull sides and let their Euclidean lengths be `ell_1,...,ell_a`. PC/OP gives

```math
\operatorname{per}(F)
=(q-a)+\sum_{j=1}^a\ell_j.
```

Hence the entire perimeter excess over `q` unit sides is carried by the missing sides:

```math
\boxed{
M:=\operatorname{per}(F)-q
=
\sum_{j=1}^a(\ell_j-1).
}
\tag{DM.1}
```

DB gives

```math
\operatorname{per}(F)
\ge
h-1+2D\cos((h-1)a_D).
\tag{DM.2}
```

NM gives the exact branching inequality

```math
3(2h-q)\ge h-2,
```

so

```math
q\le\frac{5h+2}{3}.
\tag{DM.3}
```

Subtract DM.3 from DM.2:

### Theorem DM — exact missing-side metric floor

```math
\boxed{
M
\ge
2D\cos((h-1)a_D)
-\frac{2h}{3}
-\frac53.
}
\tag{DM.4}
```

Of course `M>=0`; the useful lower bound is the positive part of the right-hand side.

If `h/D->y`, then

```math
\boxed{
\liminf\frac MD
\ge
m_{DB}(y):=\max\left\{0,
2\cos\frac y2-\frac{2y}{3}
\right\}.
}
\tag{DM.5}
```

The untruncated expression is strictly decreasing. It vanishes exactly at

```math
y=3c_*=1.8297129569\ldots,
```

where `c_*=0.6099043189...` is the NB constant satisfying

```math
c_*=\cos\frac{3c_*}{2}.
```

At the minimum DB diameter density `y=2rho`, `rho=cos rho`,

```math
m_{DB}(2\rho)=\frac{2\rho}{3}=0.4927234221\ldots .
\tag{DM.6}
```

---

## 6. A concrete universal metric-or-area fork

The area floor `A_DB(y)` increases with `y`, while the positive metric floor in DM.5 decreases with `y` on the relevant interval.

Let `delta_0` be the unique positive solution

```math
\delta_0
=
2\cos\left(\rho+\frac{\delta_0}{2}\right)
-
\frac{2(2\rho+\delta_0)}{3}.
\tag{DF.1}
```

Numerically,

```math
\boxed{\delta_0=0.2072587352\ldots .}
\tag{DF.2}
```

Put

```math
y_0:=2\rho+\delta_0
=1.6854290017\ldots .
\tag{DF.3}
```

Then

```math
m_{DB}(y_0)=\delta_0,
```

and

```math
A_{DB}(y_0)
=\frac{y_0+\sin y_0}{6}
=0.4464776447\ldots .
\tag{DF.4}
```

Thus every unbounded post-ZF sequence satisfies the following asymptotic alternative: for every fixed `eta>0`, all sufficiently large members obey at least one of

```math
\boxed{
\operatorname{per}(F)-q
\ge(0.2072587352\ldots-\eta)D
}
\tag{DF.5}
```

or

```math
\boxed{
\operatorname{area}(F)
\ge(0.4464776447\ldots-\eta)D^2.
}
\tag{DF.6}
```

### Proof

If `h/D<=y_0+o(1)`, monotonicity of `m_DB` and DM.5 give DF.5. If `h/D>=y_0-o(1)`, monotonicity of `A_DB` and DA.8 give DF.6. The `o(1)` overlap is absorbed by `eta`. `square`

The area branch improves the previous universal floor

```math
\frac{\sqrt3}{4}=0.4330127019\ldots
```

by

```math
0.0134649428\ldots
```

on the `D^2` scale.

---

## 7. Effect on the GU component-gap threshold

GU's proof uses only a force-hull area floor `A_0D^2` and the attachment-cell upper bound

```math
\sum_r\operatorname{area}(P_r)
\le\frac\pi4\lambda_2^2D^2+o(D^2),
\qquad
\lambda_2=\limsup\frac{e_{BB}+2s_C}{D}.
```

In the DF.6 high-area branch one may replace `A_0=sqrt3/4` by

```math
A_0=0.4464776447\ldots .
```

The positive-gap transition therefore improves from

```math
\lambda_*=
\sqrt{\frac{\sqrt3}{\pi}}
=0.7425152492\ldots
```

to

```math
\boxed{
\lambda_{*,area}
=
\sqrt{\frac{4A_0}{\pi}}
=0.7539714803\ldots .
}
\tag{DF.7}
```

So the high-diameter-density branch enlarges the interval in which GU forces a quadratic attachment-cell gap.

This does not close the complementary high-surplus phase.

---

## 8. Regression audit

- At the bare DB density `h/D=2rho`, DA gives only `(2rho+sin(2rho))/6`, below `sqrt3/4`; DA.9 correctly keeps the stronger old direction-spread floor.
- A regular near-circular shell can have many diameter directions and large difference-body area. DA does not falsely exclude it without global/contact input.
- DM is allowed to become zero when `h/D` approaches `3c_*`; this is the genuine high-diameter-density escape.
- Missing hull sides can be long and pockets thin. DM charges metric side excess, not pocket area.
- Rogers--Shephard is used only in the safe direction `area(F-F)<=6 area(F)`. No symmetry of `F` is assumed.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| exact diameter-polygon area DA.4 | proved | cyclic polygon area formula |
| sine-sum minimum DA.5 | proved | concavity under lower gap bounds |
| force-hull area DA.7 | proved | inclusion in `F-F` + planar Rogers--Shephard |
| metric excess DM.4 | proved | DB perimeter + NM branching |
| asymptotic metric-or-area fork | proved | monotonicity and one-dimensional threshold split |
| GU threshold improves to `0.753971...` in high-area branch | proved conditional on GU inputs | substitute the stronger area floor |
| either branch closes Level I | not proved | need a metric-shell theorem in DF.5 or a high-surplus exclusion in DF.6 |

---

## 10. Next target

DF exposes two quantitatively different survivors:

1. at least `0.207258D` total excess length on the missing loaded hull sides; or
2. force-hull area at least `0.446477D^2`, which strengthens every area-gap/population argument.

The first branch should be coupled to the PC family of convex outer pockets; the second should be coupled to GU/ER with the upgraded `0.753971` surplus threshold.
