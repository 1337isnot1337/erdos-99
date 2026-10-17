> Generated reading edition · [exact source](../../../docs/reports/target_c_explicit_diameter_angle_gap_2026-08-31.md) · source SHA-256 `f21996527a907a74107b56e2773257e42448fb00f50eac0f61abff2d028e493b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4BE768702C8B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: explicit diameter-angle gap from a three-disk container

**Date:** 2026-08-31  
**Repository state:** `research/target-c-force-hull-v2-2026-08-30`  
**Run type:** proof / explicit global geometric inequality  
**Target:** Level I candidate route C  
**Computation:** not used in the proof

## LEVEL I STATUS

`STILL OPEN`

Target C16 proved nonconstructively that large global minimizers have a uniform angular gap below `60` degrees between distinct diameter chords incident to one point.  The exact three-disk geometry gives a much stronger explicit result.

If

```math
|b-y|=|b-z|=D=D(n),
```

and `theta=angle(ybz)`, then every global minimizer satisfies

```math
\boxed{
\theta
<
\frac{
D\left(\frac{5\pi}{6}-\sqrt3\right)
+\frac{4\pi}{3}
+\frac{\pi}{2D}
}{D+1}.
}
\tag{C18.1}
```

Consequently

```math
\boxed{
\limsup_{n\to\infty}\theta
\le
\theta_\infty
:=
\frac{5\pi}{6}-\sqrt3
=0.8859430704\ldots
=50.7607988\ldots^\circ.
}
\tag{C18.2}
```

Thus the true asymptotic exclusion obtained from global packing area is about `9.24` degrees stronger than the elementary diameter-graph bound `theta<=60` degrees.

No triangle-free or KKT hypothesis is used.

---

## 1. The exact three-disk intersection

Scale `D` to one and place

```math
b=(0,0),
\qquad
y=(1,0),
\qquad
z=(\cos\theta,\sin\theta),
\qquad
0<\theta\le\frac\pi3.
\tag{C18.3}
```

The upper bound `theta<=pi/3` is elementary: `|y-z|<=1` because the source diameter is one.

Put

```math
K_\theta
=
\overline B(b,1)
\cap
\overline B(y,1)
\cap
\overline B(z,1).
\tag{C18.4}
```

Every point of the normalized source belongs to `K_theta`.

### Lemma C18.1 (exact area and perimeter)

For `0<theta<=pi/3`,

```math
\boxed{
\operatorname{area}(K_\theta)
=
\frac{2\pi}{3}-\frac{\sqrt3}{2}-\frac\theta2,
}
\tag{C18.5}
```

and

```math
\boxed{
\operatorname{per}(K_\theta)
=
\frac{4\pi}{3}-\theta.
}
\tag{C18.6}
```

#### Proof

Let `p` be the intersection of the unit circles centered at `b` and `y` lying on the same side of `by` as `z`.  Then `p` lies on the unit circle about `b` at polar angle `pi/3` and also lies in the disk centered at `z` because the angular difference from `z` is at most `pi/3`.

Similarly, let `r` be the intersection of the unit circles centered at `b` and `z` lying toward `y`.  Its polar angle about `b` is `theta-pi/3`, and it lies in the disk centered at `y`.

The two unit circles centered at `y` and `z` intersect at `b` and at `y+z`; the latter point has distance

```math
|y+z|=2\cos(\theta/2)>1
```

from `b`, so it lies outside `K_theta`.  Hence the boundary of `K_theta` consists of exactly three circular arcs:

1. the radius-one arc centered at `y` from `b` to `p`, of central angle `pi/3`;
2. the radius-one arc centered at `b` from `r` to `p`, of central angle
   ```math
   \phi=\frac{2\pi}{3}-\theta;
   
   ```
3. the radius-one arc centered at `z` from `r` to `b`, again of central angle `pi/3`.

This immediately gives the perimeter

```math
\frac\pi3+\left(\frac{2\pi}{3}-\theta\right)+\frac\pi3
=
\frac{4\pi}{3}-\theta.
```

For the area, start with the Euclidean triangle `bpr`.  Since `|bp|=|br|=1` and the included angle is `phi`, its area is

```math
\frac12\sin\phi.
```

Add the three circular segments between the chords and the boundary arcs.  The segment centered at `b` has area

```math
\frac12(\phi-\sin\phi),
```

while each of the two `pi/3` segments has area

```math
\frac12\left(\frac\pi3-\frac{\sqrt3}{2}\right).
```

The sine terms cancel, leaving

```math
\frac\phi2+rac\pi3-\frac{\sqrt3}{2}
=
\frac{2\pi}{3}-\frac{\sqrt3}{2}-\frac\theta2.
```
`\square`

At `theta=pi/3`, this is the Reuleaux triangle area `(pi-sqrt3)/2`; as `theta->0`, it tends to the area of the intersection lens of two unit disks whose centers are one unit apart.

---

## 2. The entire global minimizer is trapped in this body

Return to diameter `D`.  Since every source point `a` satisfies

```math
|a-b|,|a-y|,|a-z|\le D,
```

we have

```math
\operatorname{conv}A
\subseteq
D K_\theta
\tag{C18.7}
```

up to translation and rotation.  Hence

```math
\operatorname{conv}A+B(0,1/2)
\subseteq
D K_\theta+B(0,1/2).
\tag{C18.8}
```

Steiner's formula and Lemma C18.1 give

```math
\boxed{
\operatorname{area}(DK_\theta+B(0,1/2))
=
\left(
\frac{2\pi}{3}-\frac{\sqrt3}{2}-\frac\theta2
\right)D^2
+
\frac12\left(\frac{4\pi}{3}-\theta\right)D
+
\frac\pi4.
}
\tag{C18.9}
```

---

## 3. Global packing lower area yields the explicit angle bound

For a global minimizer, the canonical Fejes Toth lower area estimate and strict upper bound on `D(n)` imply

```math
\boxed{
\operatorname{area}(\operatorname{conv}A+B(0,1/2))
>
\frac\pi4D^2.
}
\tag{C18.10}
```

Combining (C18.9) and (C18.10),

```math
\frac\pi4D^2
<
\left(
\frac{2\pi}{3}-\frac{\sqrt3}{2}-\frac\theta2
\right)D^2
+
\frac12\left(\frac{4\pi}{3}-\theta\right)D
+
\frac\pi4.
\tag{C18.11}
```

Divide by `D^2`, collect the `theta` terms, and multiply by two:

```math
\theta\left(1+\frac1D\right)
<
\frac{5\pi}{6}-\sqrt3
+
\frac{4\pi}{3D}
+
\frac{\pi}{2D^2}.
\tag{C18.12}
```

Therefore

```math
\boxed{
\theta
<
\frac{
D\left(\frac{5\pi}{6}-\sqrt3\right)
+\frac{4\pi}{3}
+\frac{\pi}{2D}
}{D+1},
}
```

which is (C18.1). `\square`

Since `D(n)->infinity`, the right side tends to `theta_infty=5pi/6-sqrt3`, proving (C18.2).

For reference,

```math
\theta_\infty=50.7607988\ldots^\circ.
```

The finite-`D` bound becomes stronger than the elementary `60`-degree bound once `D` is approximately `20`; the canonical lower estimate for `D(n)` already gives `D(n)>20` for `n>=400`.

---

## 4. Explicit improvement of the Target C force-perimeter lower bound

At a positive KKT diameter endpoint `b`, all incident diameter reaction vectors have pairwise angular separation at most the bound in C18.1.  Therefore they lie in one angular interval of that width.  If `Theta(D)` denotes the right side of C18.1, then projection onto the interval bisector gives

```math
|g_b|
\ge
D s_b\cos\frac{\Theta(D)}2,
\tag{C18.13}
```

where `s_b` is the total incident positive `beta` weight.  Since `sum_b s_b=2`,

```math
\boxed{
P_*
\ge
2D\cos\frac{\Theta(D)}2.
}
\tag{C18.14}
```

In particular,

```math
\boxed{
\liminf_{n\to\infty}\frac{P_*}{D(n)}
\ge
2\cos\left(\frac{5\pi}{12}-\frac{\sqrt3}{2}\right)
=
1.8069639529\ldots.
}
\tag{C18.15}
```

This replaces the old universal lower endpoint `sqrt3=1.7320508...` by an explicit asymptotic global-minimizer bound larger by about `0.07491 D`.

Thus the nonconstructive epsilon in Target C16 can be made explicit asymptotically:

```math
\liminf\frac{P_*}{D}-\sqrt3
\ge
0.0749131453\ldots.
\tag{C18.16}
```

The finite-`n` version is (C18.14), with `Theta(D)` truncated at `pi/3` when the displayed global bound is weaker than the elementary diameter bound.

---

## 5. Consequences for the diameter graph

For every sufficiently large global minimizer, all distinct diameter partners of a fixed point lie in a cone of angular width at most

```math
50.761^\circ+o(1).
\tag{C18.17}
```

Equivalently, if `|b-y|=|b-z|=D`, then

```math
\frac{|y-z|}{D}
=2\sin\frac\theta2
\le
2\sin\left(
\frac{5\pi}{12}-\frac{\sqrt3}{2}
\right)+o(1)
=
0.85716\ldots+o(1).
\tag{C18.18}
```

So two distinct diameter partners of the same vertex are separated by a uniform fraction **strictly below the diameter**.

This is a source-wide global-optimality restriction; it applies to the full diameter graph, not only to KKT-supported diameter edges.

---

## 6. Target C significance

The higher-order weak-contact obstruction C13 is paid for by angular variance among supported diameter chords.  C18 says those chords are locally much more coherent than arbitrary planar diameter geometry permits.  The supported diameter system therefore has two simultaneous properties:

1. every vertex star lies in a uniformly acute cone of asymptotic width at most `50.761` degrees;
2. any cyclic subsystem has length `Omega(sqrt D)` by C17.

This is now a concrete geometric input for an angular Poincare/Korn inequality on the diameter-shear field.

A direct local variance bound is impossible at a high-degree diameter vertex because scalar angular rates can cancel in two vector dimensions.  Any closing inequality must therefore use the global thrackle/tree structure of the diameter graph together with the connected positive contact network, not local cone geometry alone.

---

## 7. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Theorem C18:
If two diameter chords by and bz of a global minimizer meet at b with angle theta, then

  theta < [ D(5pi/6-sqrt3) + 4pi/3 + pi/(2D) ]/(D+1).

The exact normalized three-disk container is
  K_theta=B(b,1) cap B(y,1) cap B(z,1),
with
  area(K_theta)=2pi/3-sqrt3/2-theta/2,
  per(K_theta)=4pi/3-theta.
Steiner plus Fejes Toth and D(n)^2<n/Delta_2 gives the bound directly.

As n->infinity:
  theta <= 5pi/6-sqrt3+o(1) = 50.7607988... degrees,
not merely 60 degrees.

KKT force consequence:
  liminf P_force/D >= 2 cos((5pi/6-sqrt3)/2)
                       = 1.8069639529...,
which is an explicit improvement over sqrt3=1.73205...

Combined C17+C18 boundary geometry:
- any diameter cycle has length Omega(sqrt D);
- every incident diameter star has width <=50.761 degrees+o(1).
This is the current geometric input for the diameter-shear variance problem.
```
