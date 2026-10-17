> Generated reading edition · [exact source](../../../docs/reports/target_c_uniform_force_gap_2026-08-30.md) · source SHA-256 `35fd2920f78cabde4d6fba8810643548f1b44a991414e0e69a7a51c10919fc8e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-2578BFFA417A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: uniform asymptotic gap above the Reuleaux force endpoint

**Date:** 2026-08-30  
**Repository state:** `research/target-c-force-hull-v2-2026-08-30`  
**Run type:** proof / compactness-stability theorem  
**Target:** Level I candidate route C  
**Depends on:** Target C local force bound C14; canonical Fejes Tóth parallel-body lower bound and strict upper bound on `D(n)`  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The preceding report excluded the exact lower force-perimeter endpoint

```math
P_*=\sqrt3D
```

for `n\ge362`.  This note proves a genuinely stronger asymptotic statement: the lower
endpoint cannot even be approached by KKT stresses of large global minimizers.

### Theorem C16 (uniform large-`n` force-perimeter gap)

There exist absolute constants

```math
\boxed{\varepsilon_0>0,
\qquad n_0<\infty}
\tag{C16.1}
```

such that for every `n\ge n_0`, every planar global `n`-point minimizer `A`, and every
normalized KKT stress of `A`,

```math
\boxed{
P_*
\ge
(\sqrt3+\varepsilon_0)D(n).
}
\tag{C16.2}
```

No triangle-free hypothesis is used.

The proof is by contradiction and compactness.  If the force perimeter approached the
local lower bound, then at some positively loaded hull vertex two actual diameter
partners would make angle tending to `60` degrees.  Those three source points would
become an asymptotically equilateral diametral triple.  The entire source would then be
trapped in an asymptotic Reuleaux triangle, whose normalized area coefficient is
strictly smaller than the coefficient forced by global minimum-diameter packing.

The two constants behind the contradiction are

```math
\boxed{
\frac{\pi-\sqrt3}{2}
=0.704770\ldots
<
\frac\pi4
=0.785398\ldots.
}
\tag{C16.3}
```

---

## 1. Local coherence parameter

Fix one normalized KKT stress.  At `b\in B_+`, let

```math
s_b=\sum_{bk\in H_+}\beta_{bk}>0
\tag{C16.4}
```

and normalize the incident diameter directions by

```math
u_{bk}:=\frac{b-k}{D},
\qquad |u_{bk}|=1.
\tag{C16.5}
```

Define

```math
\boxed{
\rho_b
:=
\frac{|g_b|}{Ds_b}
=
\left|
\sum_{bk\in H_+}
\frac{\beta_{bk}}{s_b}u_{bk}
\right|.
}
\tag{C16.6}
```

Target C Lemma C14.1 says all incident diameter directions at `b` have pairwise angular
distance at most `\pi/3`.  If `\theta_b\le\pi/3` is the width of a shortest closed
angular interval containing them, projection onto the interval bisector gives

```math
\boxed{
\rho_b
\ge
\cos(\theta_b/2)
\ge
\cos(\pi/6)
=
\frac{\sqrt3}{2}.
}
\tag{C16.7}
```

The force perimeter is exactly

```math
\boxed{
\frac{P_*}{D}
=
\sum_{b\in B_+}s_b\rho_b,
\qquad
\sum_{b\in B_+}s_b=2.
}
\tag{C16.8}
```

Thus `P_*/(2D)` is the `s_b/2`-weighted mean of the local coherence parameters
`\rho_b`.

---

## 2. Near-minimal force perimeter produces a near-equilateral diametral triple

### Lemma C16.1 (local stability of the sixty-degree endpoint)

Let `(A_m)` be any sequence of diameter-`D_m` configurations with normalized KKT
stresses satisfying

```math
\frac{P_{*,m}}{D_m}\longrightarrow\sqrt3.
\tag{C16.9}
```

Then there exist, for every `m`, three points

```math
b_m,y_m,z_m\in A_m
```

such that

```math
|b_m-y_m|=|b_m-z_m|=D_m
\tag{C16.10}
```

and

```math
\boxed{
\frac{|y_m-z_m|}{D_m}\longrightarrow1.
}
\tag{C16.11}
```

Equivalently, after scaling by `D_m`, the three points converge modulo Euclidean
motions to a unit equilateral triangle.

#### Proof

By (C16.8),

```math
\min_{b\in B_{+,m}}\rho_b
\le
\frac{P_{*,m}}{2D_m}.
\tag{C16.12}
```

Together with the universal lower bound `\rho_b\ge\sqrt3/2` and (C16.9), there is a
choice `b_m` with

```math
\rho_{b_m}\longrightarrow\frac{\sqrt3}{2}.
\tag{C16.13}
```

Let `\theta_m=\theta_{b_m}`.  From (C16.7),

```math
\frac{\sqrt3}{2}
\le
\cos(\theta_m/2)
\le
\rho_{b_m}
\longrightarrow
\frac{\sqrt3}{2}.
```

Hence

```math
\boxed{\theta_m\longrightarrow\frac\pi3.}
\tag{C16.14}
```

The endpoint directions of a shortest containing interval are actual incident diameter
directions because the support is finite.  Choose corresponding diameter partners
`y_m,z_m`.  The angle between `b_m-y_m` and `b_m-z_m` is `\theta_m`, so

```math
\frac{|y_m-z_m|}{D_m}
=
2\sin(\theta_m/2)
\longrightarrow
2\sin(\pi/6)
=1.
```

This proves the lemma. `\square`

Note that no lower bound on an individual KKT multiplier is needed.  The weighted
average only identifies one loaded vertex whose **geometry** approaches the local
equality case.

---

## 3. Near-Reuleaux containers

Scale the triple in Lemma C16.1 by `D_m` and apply a rigid motion so that

```math
\tilde b_m=(0,0),
\qquad
\tilde y_m=(1,0),
\qquad
\tilde z_m=(\cos\theta_m,\sin\theta_m),
\tag{C16.15}
```

with `\theta_m\to\pi/3`.

Every normalized source point `\tilde a=a/D_m` lies within distance one of all three
centers because the original source diameter is `D_m`.  Therefore

```math
\frac1{D_m}\operatorname{conv}A_m
\subseteq
K_m,
\tag{C16.16}
```

where

```math
K_m
:=
\overline B(\tilde b_m,1)
\cap
\overline B(\tilde y_m,1)
\cap
\overline B(\tilde z_m,1).
\tag{C16.17}
```

As `\theta_m\to\pi/3`, the three disk centers converge to the vertices of a unit
equilateral triangle.  Hence the compact convex sets `K_m` converge in Hausdorff
distance to the unit Reuleaux triangle `\mathcal R_1`.

For convex bodies, area and perimeter are continuous under Hausdorff convergence.
Consequently

```math
\boxed{
\operatorname{area}(K_m)
\longrightarrow
\frac{\pi-\sqrt3}{2},
}
\tag{C16.18}
```

and the perimeters remain uniformly bounded; in fact they converge to `\pi`.

This continuity statement can be avoided if desired by enclosing `K_m` between
parallel neighborhoods of `\mathcal R_1` with radii tending to zero.  No quantitative
stability theorem is being imported.

---

## 4. Global packing forces normalized area above `pi/4`

Assume now, toward contradiction, that Theorem C16 is false.  Then there is a sequence
of cardinalities

```math
n_m\to\infty,
```

global minimizers `A_m`, and normalized KKT stresses such that

```math
\frac{P_{*,m}}{D_m}\longrightarrow\sqrt3,
\qquad
D_m:=D(n_m).
\tag{C16.19}
```

The canonical lower diameter estimate implies `D_m\to\infty`.

Let

```math
t_m:=\frac1{2D_m}\longrightarrow0.
\tag{C16.20}
```

Scaling the parallel-body inclusion obtained from (C16.16) gives

```math
\frac1{D_m}
\left(
\operatorname{conv}A_m+B(0,1/2)
\right)
\subseteq
K_m+B(0,t_m).
\tag{C16.21}
```

By Steiner's formula,

```math
\operatorname{area}(K_m+B(0,t_m))
=
\operatorname{area}(K_m)
+t_m\operatorname{per}(K_m)
+\pi t_m^2.
\tag{C16.22}
```

Using (C16.18), bounded perimeter, and `t_m\to0`,

```math
\limsup_{m\to\infty}
\frac{
\operatorname{area}(\operatorname{conv}A_m+B(0,1/2))
}{D_m^2}
\le
\boxed{
\frac{\pi-\sqrt3}{2}.
}
\tag{C16.23}
```

But Fejes Tóth gives

```math
\operatorname{area}(\operatorname{conv}A_m+B(0,1/2))
\ge
\frac{\sqrt3}{2}n_m.
\tag{C16.24}
```

For a global minimizer the strict canonical upper diameter bound

```math
D_m^2
<
\frac{n_m}{\Delta_2},
\qquad
\Delta_2=\frac\pi{2\sqrt3},
\tag{C16.25}
```

implies

```math
\frac{n_m}{D_m^2}>\Delta_2.
```

Therefore every `m` satisfies

```math
\boxed{
\frac{
\operatorname{area}(\operatorname{conv}A_m+B(0,1/2))
}{D_m^2}
>
\frac{\sqrt3}{2}\Delta_2
=
\frac\pi4.
}
\tag{C16.26}
```

The constants satisfy

```math
\frac{\pi-\sqrt3}{2}
<
\frac\pi4
\iff
\pi<2\sqrt3,
\tag{C16.27}
```

which is true.  Equations (C16.23) and (C16.26) are incompatible.  This contradiction
proves Theorem C16. `\square`

---

## 5. Strength over the exact endpoint exclusion

Theorem C15 only said

```math
P_*>\sqrt3D
```

for each sufficiently large minimizer.  Such pointwise strictness would still permit a
sequence with

```math
P_*/D\downarrow\sqrt3.
```

Theorem C16 rules that out.  There is an absolute macroscopic separation between the
KKT force polygon of a large global minimizer and the maximally cancelling equilateral
reaction phase.

The theorem is nonconstructive with respect to `\varepsilon_0` and `n_0`.  It proves
existence of a uniform gap but does not optimize or even state an explicit numerical
value.  Making the Hausdorff/area stability in Section 3 quantitative would produce an
explicit pair of constants.

---

## 6. Consequences and next use

Write

```math
\rho_b=\frac{|g_b|}{Ds_b}\in[\sqrt3/2,1].
```

Theorem C16 says that for every large global minimizer and every normalized KKT stress,

```math
\boxed{
\sum_b\frac{s_b}{2}\rho_b
\ge
\frac{\sqrt3+\varepsilon_0}{2}.
}
\tag{C16.28}
```

Thus a positive amount of endpoint-incidence mass, in a stress-weighted sense, must be
bounded away from maximal `60`-degree cancellation.

This is a new source of boundary-order currency for Target C.  It should be combined
with either:

1. the diameter-shear variance inequality C13.15; or
2. the tangential separator C9.

At a vertex with `\rho_b` close to one, the positive diameter reaction directions are
nearly coherent, so tangential shear across them is expensive.  At a vertex with
`\rho_b` near `\sqrt3/2`, the local diameter geometry is near the excluded Reuleaux
phase.  Theorem C16 says a large global minimizer cannot put essentially all stress
mass in the latter regime.

The precise next theorem to seek is a **coherence-to-shear inequality** converting the
uniform average gap in (C16.28) into a lower or upper bound on the diameter angular
variance in C13.15.  Such an inequality would connect the global area contradiction
proved here to the weak-contact mechanism.

---

## 7. Regression audit

- All fixed small minimizers are irrelevant to the asymptotic contradiction because the
  proof takes `n_m\to\infty`.
- Near-triangular unit-contact perturbations do not evade the argument: the near
  equilateral triangle produced in Lemma C16.1 is at the **diameter scale**.
- The five-sector and activation regressions are not certified global minimizers and do
  not satisfy the normalized-area lower bound (C16.26) as a global-minimizer theorem.
- No assumption is made that KKT weights are uniformly positive.  The proof survives
  arbitrarily small individual multipliers.
- No claim is made that the force hull itself is near a disk.  The Reuleaux container is
  imposed by three actual source points and therefore traps the entire configuration,
  including KKT-invisible points.

This last point is important: the theorem bypasses the force-hull/rattler separation
that blocks several other Target C arguments.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Theorem C16:
There exist absolute epsilon_0>0 and n_0 such that for every n>=n_0, every global
minimizer, and every normalized KKT stress,

    P_force >= (sqrt(3)+epsilon_0) D(n).

Proof mechanism:
At b define s_b=sum incident beta and rho_b=|g_b|/(D s_b).  Incident diameter
directions lie in a <=60-degree arc, hence rho_b>=sqrt(3)/2 and

    P_force/D = sum_b s_b rho_b,   sum_b s_b=2.

If P_force/D -> sqrt(3), some b has rho_b->sqrt(3)/2.  The containing angular arc at
that b must then have width ->60 degrees.  Two actual diameter partners y,z of b lie at
angle ->60, so |y-z|/D->1.  Thus b,y,z form an asymptotically equilateral diametral
triple.

After scaling by D, the entire source lies in the intersection of the three unit disks
centered at that triple.  These intersections converge to the unit Reuleaux triangle,
whose area is (pi-sqrt(3))/2.  Since D->infinity, the normalized half-unit parallel-body
area has limsup <=(pi-sqrt(3))/2.

But Fejes Toth plus D(n)^2<n/Delta_2 gives for every global minimizer

    area(conv A+B_{1/2})/D(n)^2 > pi/4.

And (pi-sqrt(3))/2 < pi/4.  Contradiction.

This is a uniform macroscopic exclusion of the maximally cancelling diameter-reaction
phase.  It uses actual source diameter points, so KKT-invisible rattlers cannot escape
the Reuleaux container.

Next exact target:
convert the force-reaction coherence gap into control of the diameter angular-shear
variance from C13.
```
