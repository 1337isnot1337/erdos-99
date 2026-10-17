> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_reinhardt_force_bulk_closure_2026-09-09.md) · source SHA-256 `7713635d0bb3ff08dcb1fba3ab07b2fef283cdf2adbc028785bb0dacae48740c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-18C18FE66D37","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact cyclic Reinhardt phase has no external force-hull population

**Date:** 2026-09-09  
**Repository branch:** PR #118 after RE/RC/RD  
**Run type:** exact force-bulk closure for one cyclic subphase  
**Target:** cyclic primitive endpoint, `d_H=0`  
**Depends on:** RE exact Reinhardt shell, RC Reuleaux completion, RD rattler depth  
**External literature:** none beyond the Reinhardt completion already imported by RC  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

RC proved that every source point lies in the width-`D` Reuleaux completion `R` of the exact Reinhardt force hull `F`, but it still allowed C65 rattlers in the curved caps `R\setminus F`.

RD proves that every rattler has boundary depth asymptotic to `sqrt(3)/2`. The caps cut off by the unit Reinhardt sides have depth only `O(1/D)`. Therefore those two regions are disjoint.

### Theorem FB — force-bulk closure in the exact `d_H=0` cyclic phase

Every source point lies in the force hull:

$$
\boxed{A\subseteq F.}
\tag{FB.1}
$$

Since `V(F) subseteq A`, this gives

$$
\boxed{F=\operatorname{conv}A.}
\tag{FB.2}
$$

Thus the `d_H=0` cyclic phase has **no external force-hull population at all**. All

$$
n-q=\Theta(D^2)
$$

C65 rattlers are strictly inside the same polygonal force hull whose boundary is the positive unit contact cycle.

This closes the force-bulk localization problem completely for this exact cyclic subphase, although it does not yet create positive KKT contacts on the rattlers.

---

## 1. The Reinhardt polygon cuts only shallow circular caps from its completion

Let

$$
p_i p_{i+1}
$$

be one unit side of the force hull. By RE/RC the corresponding portion of `partial R` is a radius-`D` circular arc with the same endpoints.

The chord has length one. Its central angle is

$$
\delta_D
=2\arcsin\frac1{2D}.
$$

The maximum normal/radial distance between the minor circular arc and its chord occurs at the midpoint. It is the sagitta

$$
\boxed{
\sigma_D
:=D-D\cos\frac{\delta_D}{2}
=D-\sqrt{D^2-\frac14}.}
\tag{1.1}
$$

Rationalizing,

$$
\boxed{
\sigma_D
=
\frac1{4D\left(1+\sqrt{1-1/(4D^2)}\right)}.}
\tag{1.2}
$$

Hence

$$
\boxed{
\sigma_D
=
\frac1{8D}
+
\frac1{128D^3}
+O(D^{-5}).}
\tag{1.3}
$$

Because every defining Reuleaux corner is itself a force-hull vertex, the boundary between consecutive force-hull vertices contains no other Reuleaux corner. Therefore

$$
R\setminus F
$$

is exactly the union of these `q` circular cap regions, one above each force-hull side.

---

## 2. Every cap point is shallow relative to the completion boundary

Fix one cap, supported by a radius-`D` circle centered at `c`. A point `x` in that cap has polar angle between the two chord endpoints and radius at least the distance from `c` to the chord line:

$$
|x-c|
\ge
D\cos\frac{\delta_D}{2}.
$$

The radial point on the same ray at distance `D` from `c` lies on the corresponding arc of `partial R`. Therefore

$$
\operatorname{dist}(x,\partial R)
\le
D-|x-c|
\le
D-D\cos\frac{\delta_D}{2}
=\sigma_D.
\tag{2.1}
$$

Thus

$$
\boxed{
R\setminus F
\subseteq
\{x\in R:\operatorname{dist}(x,\partial R)\le\sigma_D\}.}
\tag{2.2}
$$

The statement includes cap boundaries; points on a force-hull side have radial boundary distance at most the same sagitta.

---

## 3. Compare cap depth with the rattler exclusion collar

RD proves that every C65 rattler `z` satisfies

$$
\operatorname{dist}(z,\partial R)>r_D,
$$

where

$$
r_D
=
\frac{\sqrt3}{2}
+
\frac1{8D}
+O(D^{-3}).
$$

By (1.3),

$$
\sigma_D
=
\frac1{8D}+O(D^{-3}).
$$

Therefore

$$
\boxed{r_D>\sigma_D}
\tag{3.1}
$$

throughout the sufficiently large Target C regime. In fact the gap tends to `sqrt(3)/2`.

Hence no C65 rattler can belong to `R\setminus F`.

RC already gives

$$
A\subseteq R.
$$

Every non-rattler source point in the C65 cyclic endpoint is a force-hull cycle vertex and therefore lies in `F`. We conclude

$$
A\subseteq F,
$$

proving FB.1. Since the vertices of `F` are source points, `conv A=F`, proving FB.2. `square`

---

## 4. Oler can now be applied directly to the actual force hull

The force hull is no longer merely a mechanical object containing only the positive core. It is the convex hull of the full unit-separated source.

Oler therefore gives directly

$$
\boxed{
 n
\le
\frac2{\sqrt3}\operatorname{area}(F)
+\frac q2+1,}
\tag{4.1}
$$

because

$$
\operatorname{per}(F)=q.
$$

Equivalently, for the `n-q` interior C65 rattlers,

$$
\boxed{
 n-q
\le
\frac2{\sqrt3}\operatorname{area}(F)
-\frac q2+1.}
\tag{4.2}
$$

Combining with the strict global diameter comparison

$$
n>\frac\pi{2\sqrt3}D^2
$$

gives the necessary force-hull area floor

$$
\boxed{
\operatorname{area}(F)
>
\frac\pi4D^2
-
\frac{\sqrt3}{4}q
-
\frac{\sqrt3}{2}.}
\tag{4.3}
$$

Since RE gives

$$
q=2q\sin\frac\pi{2q}\,D
=\pi D+O(D^{-1}),
$$

this says the exact Reinhardt force hull itself must carry essentially all the source packing capacity.

Equation (4.3) is not yet contradictory: regular odd Reinhardt shells have only a constant area deficit from the disk, comfortably inside this linear allowance.

---

## 5. Relation to the previous external-rattler branch

Before FB, Target C source-capacity arguments had to distinguish

1. contact-isolated points inside `F`;
2. contact-isolated points in the outer contact face but still inside `F`;
3. external source points outside `F` but within the source convex hull/completion.

For the exact cyclic `d_H=0` phase, category 3 is now empty.

The entire source population is geometrically subordinate to one explicit positive-contact boundary cycle. This does **not** make the rattlers KKT-positive, so ZR/ZF may not be extended to them. The gain is geometric and global rather than mechanical.

---

## 6. Regression audit

### Regular odd shell with no interior population

Trivially satisfies `A=V(F)`.

### Reinhardt shell with deep isolated points

Allowed, but all isolated points must lie inside `F`; none can occupy the shallow circular caps between `F` and `R`.

### Point just outside one unit side

Its distance to the corresponding Reuleaux arc is at most `sigma_D=O(1/D)`, contradicting RD for a C65 rattler. This is the local mechanism of FB.

### Nonregular Reinhardt completion

No regularity of `R` is used. Each force-hull side still cuts a radius-`D` unit-chord cap with the same sagitta, so the proof is uniform over the complete Reinhardt equality family.

---

## 7. What remains

The exact `d_H=0` cyclic survivor is now reduced to:

- a unit-side Reinhardt polygon `F=conv A` with
  $$
  D=1/(2\sin(\pi/(2q)));
  $$
- a positive contact graph consisting only of its boundary cycle;
- a canonical uniform full-support stress from US;
- `n-q=Theta(D^2)` actual source points strictly inside `F`, all contact-isolated in the C65 representative;
- every rattler at distance `>sqrt(3)/2+o(1)` from the Reuleaux completion boundary, hence a fortiori well inside the force polygon.

The old force-bulk problem is closed here. The remaining obstruction is a **finite packing stability theorem inside an exact Reinhardt polygon with a prescribed unit-spaced boundary cycle**.

---

## 8. Next theorem

The most direct closing target is now an Oler-slack theorem specialized to this exact geometry:

> show that a unit-separated set whose convex hull is an exact Reinhardt `q`-gon and whose `q` hull vertices form unit sides cannot attain the generic Oler boundary correction closely enough to satisfy both (4.1) and the strict global minimum-diameter lower bound.

A fixed linear improvement over the generic `q/2` boundary term would immediately force a stronger area requirement. Combined with the exact Reinhardt area/composition formula, that can potentially eliminate the branch.

A second route is to use the interior depth RD directly in a Voronoi/Delaunay proof: all non-boundary source points are shielded from `partial R` by more than the circumradius `1/sqrt3` of the triangular-lattice Voronoi hexagon, so boundary loss should be chargeable entirely to the prescribed shell vertices.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.**

FB is exact downstream of RE/RC/RD. No additional external theorem is needed for the containment result; Oler is used only for the stated consequence.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Each unit Reinhardt side cuts one radius-D circular cap from the Reuleaux completion.
Its maximum depth is the sagitta
  sigma_D=D-sqrt(D^2-1/4)
         =1/(8D)+1/(128D^3)+O(D^-5).
Every point of R\F has dist(x,partial R)<=sigma_D.

RD gives every C65 rattler
  dist(z,partial R)>r_D
with
  r_D=sqrt3/2+1/(8D)+O(D^-3).
Thus r_D>sigma_D and no rattler lies in R\F.
Since RC gives A subset R and all non-rattler core points are vertices of F,
  A subset F,
so
  F=conv A.

Therefore Oler applies to the full source directly:
  n <= (2/sqrt3) area(F)+q/2+1.
The exact cyclic force-bulk localization problem is closed; the remaining task is
an Oler/Voronoi stability improvement exploiting the prescribed unit boundary cycle.
```
