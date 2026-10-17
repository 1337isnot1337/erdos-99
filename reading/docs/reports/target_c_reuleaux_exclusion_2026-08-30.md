> Generated reading edition · [exact source](../../../docs/reports/target_c_reuleaux_exclusion_2026-08-30.md) · source SHA-256 `32a40dd81aa6f7357adb8ac39d4a0cc25f9c8435104d11a6bc9cf79ec5e29294`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-124A38BC09F5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: Reuleaux exclusion of diametral triangles

**Date:** 2026-08-30  
**Repository state:** `research/target-c-force-hull-v2-2026-08-30`  
**Run type:** proof / global packing contradiction  
**Target:** Level I candidate route C  
**Depends on:** canonical planar diameter bound and Fejes Tóth finite-packing inequality; Target C Theorem C14 for the force-perimeter corollary  
**Computation:** decimal threshold checked independently; proof below is explicit

## LEVEL I STATUS

`STILL OPEN`

This note gives the first direct global-optimality exclusion produced by the Target C
force-hull route.

A minimum-diameter configuration cannot contain an equilateral triangle whose side is
the **full diameter** once `n` is moderately large.  The reason is geometric: three
pairwise diametral points trap the entire configuration inside the Reuleaux triangle of
width `D`, whose parallel-body area is asymptotically too small to contain a globally
near-optimal unit-separated packing.

The resulting explicit bound is

```math
\boxed{
n\ge362
\quad\Longrightarrow\quad
\text{no global minimizer contains three points pairwise at distance }D(n).
}
\tag{C15.1}
```

Combining this with Target C Theorem C14 immediately rules out the lower reciprocal
force-perimeter equality `P_*=\sqrt3D` for every normalized KKT stress of every global
minimizer with `n\ge362`.

This theorem does **not** concern unit equilateral triangles directly; its side length
is `D(n)`.  Its value is that it removes one exact boundary-stress phase from the large
`n` problem by using global packing optimality rather than local rigidity.

---

## 1. Reuleaux containment

### Lemma C15.1 (three diameters force a Reuleaux container)

Let `A\subset\mathbb R^2` have diameter `D`, and suppose

```math
x,y,z\in A,
\qquad
|x-y|=|y-z|=|z-x|=D.
\tag{C15.2}
```

Then

```math
\boxed{
\operatorname{conv}A
\subseteq
\mathcal R_D
:=
\overline B(x,D)
\cap
\overline B(y,D)
\cap
\overline B(z,D),
}
\tag{C15.3}
```

where `\mathcal R_D` is the Reuleaux triangle of width `D` determined by the
equilateral triangle `xyz`.

#### Proof

Every point `a\in A` satisfies

```math
|a-x|,|a-y|,|a-z|\le D
```

because `D` is the diameter.  Hence `A\subseteq\mathcal R_D`.  The Reuleaux triangle
is convex as an intersection of closed disks, so it also contains `\operatorname{conv}A`.
`\square`

The standard area and perimeter formulas are

```math
\boxed{
\operatorname{area}(\mathcal R_D)
=
\frac{\pi-\sqrt3}{2}D^2,
\qquad
\operatorname{per}(\mathcal R_D)=\pi D.
}
\tag{C15.4}
```

For completeness, the area formula is the area of three `60`-degree radius-`D`
sectors minus twice the equilateral triangle area:

```math
3\cdot\frac{\pi D^2}{6}
-
2\cdot\frac{\sqrt3D^2}{4}
=
\frac{\pi-\sqrt3}{2}D^2.
```

The boundary consists of three `60`-degree radius-`D` arcs, so its perimeter is
`\pi D`.

---

## 2. Parallel-body capacity

Let `B_{1/2}=B(0,1/2)`.  Inclusion (C15.3) gives

```math
\operatorname{conv}A+B_{1/2}
\subseteq
\mathcal R_D+B_{1/2}.
\tag{C15.5}
```

Steiner's formula for a planar convex body `K` says

```math
\operatorname{area}(K+tB)
=
\operatorname{area}(K)+t\operatorname{per}(K)+\pi t^2.
\tag{C15.6}
```

Using (C15.4) with `t=1/2`,

```math
\boxed{
\operatorname{area}(\mathcal R_D+B_{1/2})
=
\frac{\pi-\sqrt3}{2}D^2
+
\frac\pi2D
+
\frac\pi4.
}
\tag{C15.7}
```

On the other hand, the canonical Fejes Tóth finite-packing inequality gives every
unit-separated `n`-point configuration

```math
\boxed{
\operatorname{area}(\operatorname{conv}A+B_{1/2})
\ge
\frac{\sqrt3}{2}n.
}
\tag{C15.8}
```

Therefore any unit-separated diameter-`D` configuration containing a diametral
equilateral triple must satisfy

```math
\boxed{
\frac{\sqrt3}{2}n
\le
\frac{\pi-\sqrt3}{2}D^2
+
\frac\pi2D
+
\frac\pi4.
}
\tag{C15.9}
```

This statement is independent of global optimality.  Global optimality enters only
through the sharp upper bound on `D(n)`.

---

## 3. Global minimizers: explicit threshold 362

For a planar global minimizer, the canonical strict upper bound is

```math
D(n)
<
\sqrt{\frac{n}{\Delta_2}}
=
\sqrt{\frac{2\sqrt3}{\pi}}\,\sqrt n.
\tag{C15.10}
```

Put

```math
a:=\sqrt{\frac{2\sqrt3}{\pi}}.
```

If a global minimizer contained a diametral equilateral triple, (C15.9) and (C15.10)
would imply the strict inequality

```math
\frac{\sqrt3}{2}n
<
\frac{\pi-\sqrt3}{2}a^2n
+
\frac\pi2a\sqrt n
+
\frac\pi4.
\tag{C15.11}
```

The leading coefficient gap is

```math
\begin{aligned}
\frac{\sqrt3}{2}
-
\frac{\pi-\sqrt3}{2}a^2
&=
\frac{\sqrt3}{2}
-
\frac{\sqrt3(\pi-\sqrt3)}{\pi}\\
&=
\boxed{\frac3\pi-\frac{\sqrt3}{2}}
=0.0889042547\ldots>0.
\end{aligned}
\tag{C15.12}
```

Thus (C15.11) is equivalent to

```math
\left(\frac3\pi-\frac{\sqrt3}{2}\right)n
<
\sqrt{\frac{\pi\sqrt3}{2}}\,\sqrt n
+
\frac\pi4.
\tag{C15.13}
```

Write `X=\sqrt n`.  The positive root of the corresponding equality

```math
\left(\frac3\pi-\frac{\sqrt3}{2}\right)X^2
-
\sqrt{\frac{\pi\sqrt3}{2}}X
-
\frac\pi4
=0
\tag{C15.14}
```

is

```math
X_0=19.0176779\ldots,
\qquad
X_0^2=361.672075\ldots.
\tag{C15.15}
```

For every integer `n\ge362`, the left side of (C15.14) is positive, contradicting the
necessary inequality (C15.13).  This proves:

### Theorem C15 (large global minimizers have no diametral equilateral triple)

```math
\boxed{
 n\ge362
\quad\Longrightarrow\quad
\nexists x,y,z\in A
\text{ with }
|x-y|=|y-z|=|z-x|=D(n)
}
\tag{C15.16}
```

for every global minimizer `A`. `\square`

No triangle-free hypothesis is used.

---

## 4. Force-polygon consequence

Target C Theorem C14 proved

```math
P_*=\sqrt3D
\iff
H_+=K_3
\text{ on an equilateral diameter triangle with }\beta\equiv1/3.
\tag{C15.17}
```

Theorem C15 therefore gives immediately:

### Corollary C15.2 (strict lower force-perimeter inequality for large minimizers)

For every normalized KKT stress of every global minimizer with `n\ge362`,

```math
\boxed{
\sqrt3D<P_*\le2D.
}
\tag{C15.18}
```

The upper equality remains possible in principle and is exactly the matching branch of
Target C Theorem C10.3.

The strictness in (C15.18) is not yet uniform: this report does not prove a constant
`\varepsilon>0` with `P_*\ge(\sqrt3+\varepsilon)D` for all large minimizers.  Obtaining
such a stability gap is a natural next problem.

---

## 5. Why this is a Target C gain

The contradiction uses a chain absent from both current endgames:

```text
three genuine global diameter chords
    -> Reuleaux intersection container
    -> exact parallel-body capacity
    -> Fejes Toth finite-packing lower area
    + global D(n) upper bound
    -> contradiction for n >= 362.
```

There is no lattice scaffold, Hall matching, Schur complement, rhombic track, or Oler
shell surplus.

The theorem says that large global minimizers must avoid the most strongly cancelling
possible KKT diameter-load geometry.  In the reciprocal force-polygon language, the
boundary stress cannot sit at the `sqrt(3)D` endpoint.

A quantitative stability version would be substantially stronger:

> **Target C8 (Reuleaux stability gap).**  Prove that there exist absolute
> `\varepsilon>0` and `n_0` such that every normalized KKT stress of every global
> minimizer with `n\ge n_0` satisfies
> ```math
> P_*\ge(\sqrt3+\varepsilon)D.
> ```

A compactness route is plausible: if `P_*/D\to\sqrt3`, the local equality analysis in
C14 forces almost all positive diameter-reaction mass into three approximately
`60`-degree reaction sectors, which should force an approximately equilateral triple
of near-diameter points.  The entire configuration would then lie in an approximate
Reuleaux intersection whose area coefficient stays strictly below the near-isodiametric
capacity required by global minimizers.  This stability implication is not proved here.

---

## 6. Regression audit

- **Unit square (`n=4`):** no conflict; it lies far below the threshold and its positive
  diameter graph is a matching, the opposite force-perimeter endpoint.
- **Regular pentagon (`n=5`):** its diameter graph is an odd cycle, not a diametral
  equilateral triangle.
- **`n=6` pentagon plus center:** same.
- **`n=7` hexagon plus center:** it has several diameter pairs but no triple of points
  mutually at distance `D=2`.
- **`n=8` heptagon plus center:** no diametral equilateral triple.
- **Near-triangular unit-contact regressions:** irrelevant; the excluded triangle has
  side `D`, not side one.

The theorem is compatible with all named small and local regressions.

---

## 7. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Theorem C15:
If a diameter-D unit-separated set contains three points pairwise at distance D, then
its convex hull lies in the width-D Reuleaux triangle R_D.  Therefore

  sqrt(3)/2 n
    <= area(conv A + B_{1/2})
    <= area(R_D+B_{1/2})
     = (pi-sqrt(3))/2 D^2 + (pi/2)D + pi/4.

For a global minimizer D=D(n)<sqrt(2sqrt(3)n/pi).  Substitution gives a quadratic in
sqrt(n) whose positive threshold is 361.672..., so every global minimizer with n>=362
has no equilateral triple of side D(n).

By C14, P_force=sqrt(3)D is equivalent to an equal-weight positive diameter K3.
Therefore every normalized KKT stress of every global minimizer with n>=362 satisfies

  sqrt(3)D < P_force <= 2D.

Next high-value target:
upgrade this strict inequality to a uniform asymptotic gap above sqrt(3)D via a
stability version of the Reuleaux-container argument.
```
