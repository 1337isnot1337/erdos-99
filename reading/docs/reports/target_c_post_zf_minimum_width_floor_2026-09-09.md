> Generated reading edition · [exact source](../../../docs/reports/target_c_post_zf_minimum_width_floor_2026-09-09.md) · source SHA-256 `c4ca9407f3e6e0c725e397d84432544af8739e2d736a89fcd2ca6332720c0d1c`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 8 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-2436F42A2D08","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — DWF: exact diameter directions force a post-ZF minimum-width floor

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-density-sensitive-cavity`  
**Run type:** exact convex-geometric consequence of C67/DB  
**Target:** shared post-ZF force-hull geometry  
**Depends on:** C65 full diameter visibility, C67 projective direction separation, DB for the asymptotic constant  
**External literature:** none  
**Computation:** arithmetic only

## LEVEL I STATUS

**STILL OPEN.**

The complete actual diameter graph controls not only force-hull perimeter and area but also every directional width.

Let

- `F` be the force hull of diameter `D`;
- `h` be the number of actual diameter edges;
- `a_D=arcsin(1/(2D))`;
- `w_min(F)` be the minimum Euclidean width of `F`.

C67 says the `h` projective diameter directions are separated by at least `2a_D`. Therefore the largest projective gap is at most

```math
\pi-2(h-1)a_D.
```

Every direction lies within half of that gap from an actual diameter direction. Projecting the corresponding length-`D` chord gives the exact finite bound

```math
\boxed{
 w_{\min}(F)
 \ge
 D\sin((h-1)a_D).
}
\tag{DWF.1}
```

Combining with DB's

```math
\liminf h/D\ge2\rho,
\qquad
\rho=\cos\rho,
```

gives

```math
\boxed{
\liminf_{D\to\infty}
\frac{w_{\min}(F)}D
\ge
\sin\rho
=0.6736120291832148\ldots .
}
\tag{DWF.2}
```

Thus no post-ZF force-hull subsequential limit can be arbitrarily thin in any direction.

---

## 1. Projective gap bound

Choose one projective direction from each actual diameter edge and order the `h` directions cyclically on the projective circle of circumference `pi`.

Let their gaps be

```math
g_1,\ldots,g_h.
```

C67 gives

```math
g_i\ge2a_D,
\qquad
\sum_i g_i=\pi.
\tag{1.1}
```

For the largest gap `g_max`, all other `h-1` gaps consume at least `2a_D` each. Hence

```math
\boxed{
g_{\max}\le\pi-2(h-1)a_D.}
\tag{DWF.3}
```

---

## 2. An exact diameter chord lower-bounds nearby widths

Let `u` be an arbitrary projective direction. Choose an actual diameter direction `v` nearest to `u`. Then

```math
d_{\mathbb{RP}^1}(u,v)\le\frac{g_{\max}}2.
\tag{2.1}
```

Take endpoints `x,y in F` of the corresponding actual diameter chord, so

```math
|x-y|=D
```

and `x-y` is parallel to `v`.

The width of `F` in direction `u` is the length of the orthogonal projection of `F` onto the line parallel to `u`. Since `x,y in F`, that projection contains the projected chord difference. Therefore

```math
w_F(u)
\ge
D\cos d_{\mathbb{RP}^1}(u,v)
\ge
D\cos\frac{g_{\max}}2.
\tag{2.2}
```

Use DWF.3:

```math
\cos\frac{g_{\max}}2
\ge
\cos\left(\frac\pi2-(h-1)a_D\right)
=
\sin((h-1)a_D).
```

Since `u` was arbitrary, DWF.1 follows.

This is finite and exact. It does not use KKT weights.

---

## 3. Asymptotic constant

DB gives

```math
\liminf\frac hD\ge2\rho,
```

where

```math
\rho=\cos\rho
=0.7390851332151606\ldots .
```

Also

```math
a_D=\frac1{2D}+O(D^{-3}).
```

Along any convergent subsequence with `h/D -> y`, therefore

```math
(h-1)a_D\to y/2\ge\rho.
```

Since `0<rho<pi/2` and the possible arguments remain in `[0,pi/2]` by projective packing feasibility,

```math
\liminf\frac{w_{\min}(F)}D
\ge
\sin\rho.
```

Numerically

```math
\boxed{
\sin\rho
=0.6736120291832148\ldots .
}
```

---

## 4. Defect-sensitive version

DB retains the asymptotic defect relation

```math
z\le y-2\cos(y/2),
```

where

```math
y=\lim h/D,
\qquad
z=\lim(Q+2s_Z)/D.
```

The right side is strictly increasing. Any positive defect density therefore forces `y>2rho`, and DWF correspondingly improves the width floor to

```math
\boxed{
\liminf\frac{w_{\min}(F)}D
\ge\sin(y/2)>\sin\rho.
}
\tag{DWF.4}
```

whenever the indicated limits exist and `z>0`.

Thus contact/row defect, diameter-edge density, and minimum force-hull width form one monotone chain of currencies.

---

## 5. Relation to DDM and HKN

DDM gives a limit-level statement: normalized post-ZF force-hull limits have positive-measure sets of exact diameter directions and therefore cannot be finite polygons.

DWF is a finite quantitative companion. It gives a uniform minimum-width floor before passing to a limit.

At an HKS threshold-approaching sequence, HKN forces

```math
 h/D\to p_c/2.
```

DWF would then give the sharper threshold-specific width floor

```math
\boxed{
\liminf\frac{w_{\min}(F)}D
\ge
\sin(p_c/4)
=0.688045\ldots .
}
\tag{DWF.5}
```

The exact decimal is not used elsewhere. This supplies an additional continuous shape constraint that the six-sided Hemmi equality body would have to satisfy.

Current classical `(A,D,w)` inequalities are too weak at this width to improve HKS numerically by themselves. The useful next question is the joint `(A,D,p,w)` stability problem near the HKS crossover.

---

## 6. Regression and novelty audit

The current DB report already implies the perimeter consequence

```math
\liminf per(F)/D\ge4\rho
```

through its exact difference-body perimeter inequality, so DWF does **not** claim that perimeter bound as new.

The repo search did not reveal the finite minimum-width inequality DWF.1 or the post-ZF constant DWF.2.

A disk has width `D` and trivially satisfies the theorem. Thin lens-like or oblique-grid force hulls are quantitatively constrained but not excluded: width ratio `0.674` is still compatible with many nonconstant-width bodies.

---

## 7. Classification

**Status:** proved report-level exact convex consequence of the existing direction-packing stack.  
**Level I:** still open.  
**External literature:** none.

## 8. Compact handoff

```text
DWF:
Order the h exact diameter directions on the projective circle. C67 gives every gap
>=2a_D, a_D=asin(1/(2D)), so
    g_max <= pi-2(h-1)a_D.
For any direction u, choose the nearest exact diameter chord direction v. Its length-D
chord projects onto u with length D cos d(u,v), hence
    w_F(u) >= D cos(g_max/2)
             >= D sin((h-1)a_D).
Therefore
    w_min(F) >= D sin((h-1)a_D).
DB has h/D>=2rho+o(1), rho=cos rho, so
    liminf w_min(F)/D >= sin rho = 0.67361202918....
Positive DB defect density raises this further through y>2rho.
```
