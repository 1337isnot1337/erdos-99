> Generated reading edition · [exact source](../../../docs/reports/target_c_antipodal_direction_area_floor_2026-09-09.md) · source SHA-256 `07a677cfaf6bc0bcfab43b8fa2d227a160a8b9c81e73d692cd8630b9b947f2fe`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5F6FB3D0DE4A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ADA: antipodal diameter-direction measure gives a new force-hull area floor

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-antipodal-force-area`  
**Run type:** global-minimizer compactness / convex-area theorem  
**Target:** Target C post-ZF force hull  
**Depends on:** canonical Oler and isodiametric bounds; C67 diameter-direction separation; DDM from PR #130; DB  
**New external literature:** none  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

The previous PI/DB force-hull area estimates use a finite number of actual diameter chords. A global minimum-diameter source has more structure: its complete convex hull is asymptotically a disk, while the post-ZF force hull contains `Theta(D)` exact diameter pairs with `Theta(1/D)` angular spacing. In the disk limit those exact diameter pairs become antipodal boundary pairs. Their positive direction measure forces a substantially larger force-hull area.

Let

- `K=conv(A)` be the full source hull;
- `F=conv V(C)` be the C65 force hull;
- `D=diam(A)=diam(F)`;
- `h` be the number of actual diameter edges in the post-ZF diameter graph.

Suppose along an unbounded post-ZF subsequence

$$
\frac hD\to y.
\tag{ADA.1}
$$

Then

$$
\boxed{
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge A_{AD}(y):=\frac{y+\sin y}{4}.
}
\tag{ADA.2}
$$

Since DB gives `y>=2rho`, where `rho=cos rho`, this is already strictly stronger than the existing DB/PI force-area floors.

---

## 1. Every global-minimizer source hull converges to the diameter disk

Normalize by `D` and translate each source hull so that it lies in a fixed bounded set. Write

$$
\widehat K_D:=D^{-1}(K-c_D).
$$

The canonical global asymptotic gives

$$
\frac n{D^2}\to\Delta:=\frac\pi{2\sqrt3}.
\tag{1.1}
$$

Oler's finite packing inequality applied to the `n` source points in `K` gives

$$
n\le\frac2{\sqrt3}\operatorname{area}(K)+\frac12\operatorname{per}(K)+1.
\tag{1.2}
$$

Cauchy's perimeter-diameter inequality gives `per(K)<=pi D`. Divide (1.2) by `D^2` and use (1.1). The perimeter term vanishes, so

$$
\liminf\frac{\operatorname{area}(K)}{D^2}
\ge\frac{\sqrt3}{2}\Delta
=\frac\pi4.
$$

The isodiametric inequality gives the reverse bound. Hence

$$
\boxed{
\frac{\operatorname{area}(K)}{D^2}\to\frac\pi4.
}
\tag{ADA.3}
$$

By Blaschke selection, every normalized subsequence has a Hausdorff-convergent further subsequence. Diameter and area are continuous for planar convex bodies. Every limit therefore has diameter one and area `pi/4`. Equality in the planar isodiametric inequality is unique, so after translation the limit is the radius-`1/2` disk

$$
\boxed{B:=\overline B(0,1/2).}
\tag{ADA.4}
$$

---

## 2. Force-hull diameter directions survive in the same disk limit

Use the same translations for

$$
\widehat F_D:=D^{-1}(F-c_D)\subseteq\widehat K_D.
$$

Pass to a further Hausdorff-convergent subsequence

$$
\widehat F_D\to F_\infty.
$$

Then `F_infty subset B`.

C67 proves that distinct actual diameter edges have distinct projective directions and that those directions are separated by at least

$$
\delta_D:=2\arcsin\frac1{2D}.
\tag{2.1}
$$

Since `D delta_D ->1`, ADA.1 gives

$$
h\delta_D\to y.
\tag{2.2}
$$

DDM from PR #130 applies to the exact diameter-direction sets of `widehat F_D`. Therefore the projective set `S(F_infty)` of exact unit-diameter chord directions of `F_infty` has Haar length at least

$$
\boxed{\mu(S(F_\infty))\ge y.}
\tag{ADA.5}
$$

Now use `F_infty subset B`. A chord of length one inside the radius-`1/2` disk must be a full disk diameter. Consequently, for every projective direction `theta in S(F_infty)`,

$$
\boxed{\pm\frac12u_\theta\in F_\infty.}
\tag{ADA.6}
$$

Thus `F_infty` contains the convex hull of a positive-measure antipodal subset of the boundary circle.

---

## 3. Antipodal arc-hull area lemma

### Lemma ADA.1

Let `S subset R/pi Z` be a nonempty closed projective direction set of measure `s`. Put

$$
U:=\{\pm Ru_\theta:\theta\in S\}\subset\partial B(0,R),
\qquad P:=\operatorname{conv}(U).
$$

Then

$$
\boxed{\operatorname{area}(P)\ge R^2(s+\sin s).}
\tag{ADA.7}
$$

Equality is attained when `S` is one projective interval, up to null sets and closure.

#### Proof

Lift `S` to the antipodal closed subset of the full angular circle. Its open complement is a countable union of disjoint circular gaps. Antipodality pairs the gaps. Choose one gap from each pair and let their angular lengths be `g_i`. Then

$$
\sum_i g_i=\pi-s,
\qquad 0\le g_i<\pi.
\tag{3.1}
$$

The convex hull `P` is obtained from the radius-`R` disk by replacing each missing boundary gap by its chord. A full-circle gap of angle `g` cuts off a circular segment of area

$$
\frac{R^2}{2}(g-\sin g).
$$

Each projective gap occurs twice antipodally. Hence

$$
\operatorname{area}(P)
=R^2\left[s+\sum_i\sin g_i\right].
\tag{3.2}
$$

For nonnegative `a,b` with `a+b<=pi`,

$$
\sin a+\sin b-\sin(a+b)
=4\sin\frac a2\sin\frac b2\sin\frac{a+b}{2}\ge0.
\tag{3.3}
$$

Iterating (3.3), then passing to the countable limit,

$$
\sum_i\sin g_i
\ge\sin\left(\sum_i g_i\right)
=\sin(\pi-s)=\sin s.
\tag{3.4}
$$

Substitution into (3.2) proves ADA.7. `square`

---

## 4. Apply the antipodal lemma

Take `S=S(F_infty)` and `R=1/2`. By ADA.6,

$$
\operatorname{conv}\{\pm\tfrac12u_\theta:\theta\in S\}\subseteq F_\infty.
$$

Let `s=mu(S)>=y`. ADA.1 gives

$$
\operatorname{area}(F_\infty)\ge\frac{s+\sin s}{4}.
$$

The function `s+sin s` is nondecreasing on `[0,pi]`, because its derivative is `1+cos s>=0`. Therefore

$$
\operatorname{area}(F_\infty)\ge\frac{y+\sin y}{4}.
$$

Area is continuous under planar Hausdorff convergence. This proves ADA.2.

---

## 5. Comparison with previous force-hull floors

At `y=pi/2`,

$$
\boxed{A_{AD}(\pi/2)=\frac{\pi+2}{8}=0.642699\ldots .}
\tag{ADA.8}
$$

At the universal DB endpoint `y=2rho=1.47817...`, ADA is already above `0.618`.

For comparison, PI gives only `(1/2)sin y` below `pi/2` and `1/2` thereafter. The difference is macroscopic. ADA uses global optimality through the disk limit of the complete source hull; it is therefore not available for arbitrary unit-separated configurations.

---

## 6. Regression audit

- The disk limit is for the complete source hull `K`, not asserted directly for `F`.
- A diameter chord of `F_infty` becomes antipodal only because `F_infty subset B(0,1/2)`; without the global disk containment ADA.6 is false.
- DDM is used with `delta_D->0`, exactly its corrected hypothesis.
- No finite force hull is claimed to be centrally symmetric. Symmetry appears only in the limiting hull generated by antipodal diameter endpoints.
- The direction set may be disconnected or fractal. Lemma ADA.1 handles arbitrary closed sets through complementary gaps.
- The theorem is asymptotic. A finite quantitative version requires a quantitative disk-stability estimate for the full source hull.

---

## 7. Next use

Insert ADA.2 into the ZK attachment-cell/JC cavity feasible region. Since the generic attachment cells have asymptotic area at most `(pi/4)lambda^2D^2`, the new area floor raises the unconditional pinned/contact slope substantially above BAS's `0.481096...`.

## 8. Compact handoff

```text
ADA:
Global minimizer hull K has area(K)/D^2 -> pi/4 by Oler + n/D^2->pi/(2sqrt3)
and isodiametry. Hence every normalized Hausdorff limit of K is the radius-1/2 disk.

Take F/D -> F_inf inside that disk and h/D->y. C67 gives h distinct exact diameter
directions separated by delta_D=2asin(1/(2D)), D delta_D->1. DDM therefore gives
mu(S(F_inf))>=y.

Every length-1 chord of F_inf inside the radius-1/2 disk is a full antipodal disk
diameter, so F_inf contains {+-u_theta/2: theta in S}.

For projective S of measure s, let complementary projective gaps have lengths g_i,
sum g_i=pi-s. The convex hull of the antipodal radius-R circle points has area
    R^2[s+sum sin g_i]
    >= R^2[s+sin s].
With R=1/2 and s>=y:
    liminf area(F)/D^2 >= (y+sin y)/4.
```
