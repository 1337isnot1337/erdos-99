# Target C-II — fixed outer windows collapse switching diameter directions

**Date:** 2026-09-15  
**Status:** proof-only asymptotic source-level strengthening  
**Scope:** the `<469+o(1)` adjacent strip supplied by `target_c_adjacent_strip_outer_window_469_2026-09-15.md`  
**Dependencies:** global minimum-diameter packing asymptotics; finite Oler/isodiametric bounds; adjacent switching-order theorem  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The `<469` outer-window theorem localizes every switching middle endpoint to two boundary-walk intervals of fixed metric length, independent of `D`.  This note converts that position localization into direction localization.

For any sequence of global minimizers with `D->infinity`, the normalized full source convex hull converges to the unit-diameter disk.  Therefore two diameter endpoints that are `o(D)` apart have asymptotically the same antipodal partner direction.  Applied to the adjacent strip:

\[
\boxed{
\text{switching diameters whose middle endpoints lie in one short window have one common limiting oriented direction.}
}
\]

There are at most two short middle windows, so the entire switching set has at most two limiting direction clusters.  If both left- and right-switch orientations occur, the audited one-arc theorem places every switching middle endpoint in one common window, and the **whole switching set collapses to one oriented diameter direction**.

This is qualitative `o(1)` direction collapse.  No rate is claimed, and no `O(1/D)` finite deformation is inferred from it.

---

## 1. The full source hull converges to the disk

Let `A_D` be a sequence of global minimum-diameter `n_D`-point unit-separated sources with

\[
D=\operatorname{diam}A_D\to\infty,
\qquad
K_D=\operatorname{conv}A_D.
\]

The standard minimum-diameter packing asymptotic is

\[
{n_D\over D^2}\to\Delta_2={\pi\over2\sqrt3}.
\tag{DC.1}
\]

Finite Oler gives

\[
{\sqrt3\over2}(n_D-1)
\le \operatorname{area}K_D
+{\sqrt3\over4}\operatorname{per}K_D.
\tag{DC.2}
\]

Since every `K_D` has diameter `D`, the perimeter is `O(D)`.  Divide (DC.2) by `D^2` and use (DC.1):

\[
\liminf {\operatorname{area}K_D\over D^2}
\ge {\sqrt3\over2}\Delta_2
={\pi\over4}.
\tag{DC.3}
\]

The isodiametric inequality gives the reverse bound

\[
\operatorname{area}K_D\le {\pi D^2\over4}.
\tag{DC.4}
\]

Hence

\[
\boxed{
{\operatorname{area}K_D\over D^2}\to{\pi\over4}.
}
\tag{DC.5}
\]

Translate each source by an arbitrary point and divide by `D`.  By Blaschke compactness, every subsequence has a further Hausdorff-convergent convex-hull subsequence

\[
D^{-1}K_D\to K_\infty,
\qquad \operatorname{diam}K_\infty\le1.
\]

Area is continuous under convex Hausdorff convergence, so (DC.5) gives

\[
\operatorname{area}K_\infty={\pi\over4}.
\]

Equality in the planar isodiametric inequality forces `K_infty` to be the disk of radius `1/2`.  Since every convergent subsequence has the same shape up to translation, we may use:

\[
\boxed{
D^{-1}K_D\to B_{1/2}
}
\tag{DC.6}

in Hausdorff distance after suitable translations.

---

## 2. A short endpoint patch has one diameter direction

We isolate the compactness lemma actually needed downstream.

### Lemma DC.1 — diameter-direction collapse from endpoint collapse

Let

\[
x_Dy_D,\qquad x'_Dy'_D
\]

be two actual diameter pairs of `A_D`, oriented toward `x_D,x'_D` respectively:

\[
|x_D-y_D|=|x'_D-y'_D|=D.
\]

If

\[
|x_D-x'_D|=o(D),
\tag{DC.7}
\]

then

\[
\boxed{
\left|
{x_D-y_D\over D}
-
{x'_D-y'_D\over D}
\right|\to0.
}
\tag{DC.8}

### Proof

Suppose not.  Pass to a subsequence on which the left side of (DC.8) stays above some fixed `epsilon>0`.  Use the translations in (DC.6).  Compactness gives, after another subsequence,

\[
{x_D\over D},{x'_D\over D}\to x,
\qquad
{y_D\over D}\to y,
\qquad
{y'_D\over D}\to y'.
\]

Equation (DC.7) makes the two first limits equal.  By (DC.6), all three limit points lie in the radius-`1/2` disk.  The diameter equalities give

\[
|x-y|=|x-y'|=1.
\]

A radius-`1/2` disk has a unique point at distance one from a given point of the disk: if the distance is one, both points are antipodal boundary points.  Therefore

\[
y=y'.
\]

Hence

\[
(x-y)-(x-y')=0,
\]

contradicting the assumed `epsilon` separation.  `square`

The same contradiction proof gives a uniform family version: if a collection of oriented diameter pairs has all selected endpoints in a set of Euclidean diameter `o(D)`, then the diameter of the collection of normalized oriented vectors tends to zero.

---

## 3. Apply the lemma to the `<469` adjacent strip

Take the adjacent strip from the outer-window theorem.  Its middle boundary consists of two occurrence intervals

\[
J_D^+,\qquad J_D^-
\]

with

\[
\operatorname{len}_{out}(J_D^+)
+
\operatorname{len}_{out}(J_D^-)
<469+o(1).
\tag{DC.9}

Every switching diameter has exactly one middle-layer endpoint, and every such endpoint lies in

\[
J_D^+\cup J_D^-.
\]

For two source vertices on the same outer-walk interval, Euclidean distance is at most the intervening outer-walk length.  Hence the set of switching middle endpoints in each `J_D^sigma` has Euclidean diameter bounded by

\[
469+o(1)=o(D).
\tag{DC.10}

Orient every switching diameter from its endpoint outside the middle layer toward its middle-layer endpoint and write

\[
d_h={x_h-y_h\over D},
\qquad |d_h|=1.
\tag{DC.11}

Lemma DC.1 and (DC.10) give unit vectors

\[
\nu_D^+,\qquad\nu_D^-
\]

whenever the corresponding switching subfamily is nonempty, such that

\[
\boxed{
\max_{h:\,x_h\in J_D^+}|d_h-\nu_D^+|=o(1),
}
\tag{DC.12}

\[
\boxed{
\max_{h:\,x_h\in J_D^-}|d_h-\nu_D^-|=o(1).
}
\tag{DC.13}

Thus the complete switching set has at most two asymptotic oriented-direction clusters.

No bound on the number of edges in a cluster is needed.

---

## 4. Mixed switch orientations collapse to one direction

The hostile-audited adjacent switching-order theorem proves that if at least one left-switch and at least one right-switch diameter occur, then every switching middle endpoint lies on one common middle boundary arc

\[
J_D^\star\in\{J_D^+,J_D^-\}.
\]

Therefore (DC.12)--(DC.13) sharpen to

\[
\boxed{
\exists\nu_D\in S^1:\quad
\max_{h\in H_{sw}}|d_h-\nu_D|=o(1).
}
\tag{DC.14}

Equivalently, every pair of layer-oriented switching diameter directions satisfies

\[
\boxed{
\max_{h,k\in H_{sw}}|d_h-d_k|=o(1).
}
\tag{DC.15}

This is stronger than projective clustering: the orientation is fixed from the exterior endpoint into the middle layer, and the unique-antipode argument preserves that orientation.

---

## 5. Consequence for constant-size blocker certificates

Any strip-translation blocker theorem that selects only finitely many switching diameter edges may now be combined with (DC.12)--(DC.15).

For the present thin strip:

- in the general case, every selected blocker direction has one of at most two limiting rays;
- in the mixed left/right case, every selected blocker direction has one common limiting ray.

In particular, a three-ray or three-bar obstruction cannot retain three macroscopically separated diameter directions on the selected strip.  Any genuine three-direction obstruction must collapse into a degenerate limiting configuration.

This is a compactness reduction, not yet an exclusion.  Degenerate blockers can remain load-bearing at every finite `D` even while their directions coalesce.

---

## 6. Scope warning

It is tempting to combine (DC.14) with the `O(D^-1)` adjacent train-phase gap and immediately choose a translation of size `O(D^-1)` that bypasses the limiting ray.  That step is **not certified**.

The adjacent strip-opening theorem preserves all old strict noncontacts only after choosing a deformation scale smaller than the finite source's minimum inactive slack.  The proof stack has no uniform lower bound comparing that slack with `D^-1`.  Therefore an asymptotic direction separation of size `o(1)` cannot be converted into a uniform finite deformation amplitude without a new inactive-slack theorem or a direct same-cardinality replacement.

The safe frontier is instead:

```text
one adjacent strip
+ two outer windows totaling <469+o(1)
+ at most two limiting switching-diameter rays
+ one ray if both switch orientations occur
+ constant-size local blocker certificates
-> classify the degenerate one-/two-ray blocker geometries
   or bypass them by a source-preserving finite replacement.
```

**Disposition:** proved proof-only asymptotic direction-collapse theorem. C-II and Level I remain open.
