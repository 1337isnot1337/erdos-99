> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_reinhardt_completion_core_growth_2026-09-09.md) · source SHA-256 `40378418f85f79054b9b873105e18591f83b405a41fbf49aac1cfc21e26a2ef5`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-9702F2441320","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Reinhardt completion traps all rattlers and forces a growing diameter core

**Date:** 2026-09-09  
**Repository branch:** PR #118 after RE/US  
**Run type:** exact completion theorem plus quantitative population consequence  
**Target:** cyclic primitive endpoint, `d_H=0`  
**Depends on:** RE exact Reinhardt equality, C65 full diameter visibility, Oler packing bound, canonical strict global diameter comparison  
**External literature:** Reinhardt equality classification; maximal-area theorem for Reuleaux polygons with a fixed number of arcs  
**Computation:** displayed decimal only

## LEVEL I STATUS

`STILL OPEN`

RE puts the full force hull `F` exactly on the Reinhardt equality locus. The classical equality classification therefore supplies a width-`D` Reuleaux polygon `R` such that

1. every vertex of the defining Reuleaux polygon is a vertex of `F`;
2. every vertex of `F` lies on `partial R`;
3. `F` is the equilateral clipped-Reuleaux/Reinhardt polygon inscribed in `R`.

This removes a major ambiguity in the cyclic branch: although the `Theta(D^2)` C65 rattlers may lie outside `F`, they cannot lie outside the constant-width completion `R`.

### Theorem RC — exact diameter completion

Let `V(F)` be the force-hull vertex set. Then

```math
\boxed{
\bigcap_{p\in V(F)}\overline B(p,D)=R.}
\tag{RC.1}
```

Consequently the entire source satisfies

```math
\boxed{A\subseteq R.}
\tag{RC.2}
```

Every C65 rattler lies in the strict interior of `R`.

If `nu` is the odd cycle length of the full diameter graph, equivalently the number of defining vertices/arcs of the Reinhardt Reuleaux polygon, then

```math
\boxed{
\nu^2>
\frac{\pi^3D^2}{12\sqrt3(\pi D+2)}.}
\tag{RC.3}
```

In particular

```math
\boxed{
\liminf\frac{\nu}{\sqrt D}
\ge
\frac{\pi}{\sqrt{12\sqrt3}}
=0.6890947417\ldots .}
\tag{RC.4}
```

Thus the exact cyclic survivor cannot hide all diameter complexity in a fixed or slowly growing Reuleaux core: its odd diameter cycle has at least order `sqrt(D)` vertices.

---

## 1. The Reuleaux completion is an intersection of diameter disks

Let

```math
S=\{c_1,\ldots,c_\nu\}
\subseteq V(F)
```

be the defining vertices of the width-`D` Reuleaux polygon from the Reinhardt equality classification.

By the standard disk-polygon definition of a Reuleaux polygon,

```math
\boxed{
R=\bigcap_{c\in S}\overline B(c,D).}
\tag{1.1}
```

Because `S subseteq V(F)`, adding all force-hull centers can only shrink the intersection:

```math
\bigcap_{p\in V(F)}\overline B(p,D)
\subseteq R.
\tag{1.2}
```

Conversely `R` has diameter exactly `D`. Every `p in V(F)` lies in `R`, so for every `x in R`,

```math
|x-p|\le D.
```

Hence

```math
R\subseteq\overline B(p,D)
\qquad(p\in V(F)),
```

and therefore

```math
R\subseteq
\bigcap_{p\in V(F)}\overline B(p,D).
\tag{1.3}
```

Equations (1.2)-(1.3) prove RC.1.

---

## 2. Every source point lies in the same completion

Every source point `x in A` is at distance at most the source diameter `D` from every force-hull vertex `p in V(F)`. Thus

```math
x\in\bigcap_{p\in V(F)}\overline B(p,D).
```

RC.1 gives

```math
\boxed{x\in R.}
```

This proves RC.2.

C65 says no contact-isolated point is an actual diameter endpoint. Every boundary point of `R` lies on at least one defining radius-`D` circular arc, hence is at distance exactly `D` from one of the defining centers `c in S subset V(F)`. Therefore a C65 rattler cannot lie on `partial R`.

### Corollary RC.1 — strict completion interior

If `Z=A\setminus V(C)` is the C65 rattler set, then

```math
\boxed{Z\subset\operatorname{int}R.}
\tag{2.1}
```

This is stronger than the earlier force-hull localization: rattlers may be external to `F`, but only inside the curved Reinhardt completion.

---

## 3. Oler forces the Reuleaux completion to be nearly disk-area

The source is unit-separated and lies in the convex body `R`. Oler's planar packing inequality gives

```math
n
\le
\frac2{\sqrt3}\operatorname{area}(R)
+\frac12\operatorname{per}(R)+1.
\tag{3.1}
```

By Barbier's theorem, every width-`D` body has perimeter

```math
\operatorname{per}(R)=\pi D.
\tag{3.2}
```

The canonical strict global diameter comparison gives

```math
D^2<\frac n\Delta,
\qquad
\Delta=\frac\pi{2\sqrt3},
```

or

```math
n>\frac\pi{2\sqrt3}D^2.
\tag{3.3}
```

Combine (3.1)-(3.3):

```math
\frac\pi{2\sqrt3}D^2
<
\frac2{\sqrt3}\operatorname{area}(R)
+\frac\pi2D+1.
```

Multiplying by `sqrt(3)/2` gives the finite area floor

```math
\boxed{
\operatorname{area}(R)
>
\frac\pi4D^2
-
\frac{\pi\sqrt3}{4}D
-
\frac{\sqrt3}{2}.}
\tag{3.4}
```

Equivalently the isodiametric disk-area deficit obeys

```math
\boxed{
0\le
\frac\pi4D^2-\operatorname{area}(R)
<
\frac{\pi\sqrt3}{4}D+\frac{\sqrt3}{2}.}
\tag{3.5}
```

Thus the completion is forced to be disk-area to within `O(D)`, a much stronger statement than normalized `o(D^2)` roundness.

---

## 4. Reuleaux core size from maximal-area stability

A classical extremal theorem for Reuleaux polygons states that, among Reuleaux `nu`-gons of a fixed width, the regular Reuleaux `nu`-gon has maximum area.

For width `D`, its area is

```math
\boxed{
A_\nu^{\rm reg}
=D^2\left[
\frac\pi2
-
\frac\nu2\tan\frac\pi{2\nu}
\right].}
\tag{4.1}
```

For completeness, (4.1) follows by decomposing the regular Reuleaux polygon into its regular core polygon plus `nu` congruent circular segments. Writing

```math
a=\frac\pi{2\nu},
```

the regular-core side length is `2D sin a`, the boundary-arc angle is `2a=pi/nu`, and the terms simplify to (4.1).

Therefore every width-`D` Reuleaux `nu`-gon satisfies

```math
\operatorname{area}(R)
\le
D^2\left[
\frac\pi2
-
\frac\nu2\tan\frac\pi{2\nu}
\right].
\tag{4.2}
```

Subtract from disk area:

```math
\frac\pi4D^2-\operatorname{area}(R)
\ge
D^2\left[
\frac\nu2\tan\frac\pi{2\nu}
-
\frac\pi4
\right].
\tag{4.3}
```

Using

```math
\tan x\ge x+\frac{x^3}{3}
\qquad(0<x<\pi/2),
```

with `x=pi/(2nu)`,

```math
\frac\nu2\tan\frac\pi{2\nu}-\frac\pi4
\ge
\frac{\pi^3}{48\nu^2}.
\tag{4.4}
```

Hence

```math
\boxed{
\frac\pi4D^2-\operatorname{area}(R)
\ge
\frac{\pi^3D^2}{48\nu^2}.}
\tag{4.5}
```

Combine (4.5) with the strict upper bound (3.5):

```math
\frac{\pi^3D^2}{48\nu^2}
<
\frac{\pi\sqrt3}{4}D+\frac{\sqrt3}{2}.
```

Rearranging gives

```math
\nu^2
>
\frac{\pi^3D^2}
{12\pi\sqrt3 D+24\sqrt3}
=
\frac{\pi^3D^2}
{12\sqrt3(\pi D+2)},
```

which is RC.3. Dividing by `D` and taking lower limits proves RC.4.

---

## 5. Diameter-graph interpretation

The Reinhardt equality classification identifies the diameter graph as

- one odd cycle on the `nu` defining Reuleaux vertices;
- `q-nu` degree-one diameter vertices attached to that cycle.

RC.4 therefore says the nonleaf diameter core itself grows:

```math
\boxed{|V(H^{core})|=\nu\ge(0.6890947-o(1))\sqrt D.}
\tag{5.1}
```

US proves that contact stresses are constant through every diameter-leaf run. Hence the number of locations at which a selected contact stress can change is also at most/controlled by this growing odd core rather than the full `q=Theta(D)` boundary population.

The remaining two-dimensional KKT stress polytope is therefore supported over a core whose combinatorial size diverges at least as `sqrt(D)`.

---

## 6. Regression audit

### Regular odd shell

For the regular odd `q`-gon, the defining Reuleaux polygon has `nu=q=Theta(D)`, so RC.4 is satisfied with a large margin.

### Fixed Reuleaux triangle core with many clipped vertices

This is now impossible for an unbounded Target C survivor. A clipped-Reuleaux family with fixed `nu=3` has a fixed positive normalized area deficit from the disk, while Oler plus global diameter optimality forces only `O(1/D)` normalized deficit. RC quantifies the contradiction.

### Slowly growing core

Any `nu=o(sqrt(D))` is excluded. The theorem does not rule out `nu~c sqrt(D)` or larger.

### Rattlers outside `F`

Allowed, but RC.1 forces them into `R`. The theorem does not claim `A subset F`.

---

## 7. What this changes

Before RE/RC, the cyclic endpoint left `Theta(D^2)` force-invisible points with essentially uncontrolled placement outside the polygonal force hull.

After RC:

1. every one of them lies in one explicit constant-width completion `R`;
2. every rattler lies strictly inside `R`;
3. `R` has disk-area deficit only `O(D)`;
4. its odd Reuleaux/diameter core has at least `Omega(sqrt(D))` vertices.

Thus the exact `d_H=0` branch cannot be supported by a low-complexity Reuleaux cage.

---

## 8. Next theorem

Two high-value continuations are now concrete.

### RC-A — second-order packing against the sampled Reuleaux boundary

The `q~pi D` shell vertices lie on `partial R` at unit chord spacing, while all `n-q` rattlers are strictly interior and strictly farther than one from every shell vertex. A packing theorem exploiting these prescribed boundary points could improve Oler's generic `per(R)/2` correction and potentially contradict the strict global lower bound `n>Delta D^2`.

### RC-B — KKT core-size interaction

Combine `nu=Omega(sqrt(D))` with the two-dimensional KKT polytope, LF's fact that leaf diameter edges never vanish, and US leaf-run contact constancy. If a two-dimensional diameter-coordinate polytope on a growing odd cycle must expose many cycle-edge facets, one may obtain a response or stress contradiction.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.**

RC.1-RC.2 are exact downstream of RE and the standard Reinhardt equality classification. RC.3-RC.4 additionally import the known maximal-area theorem for Reuleaux `nu`-gons.

---

## 10. Literature note

The external facts used here are standard and have modern references:

- Reinhardt/Datta equality classification for maximum-perimeter diameter-constrained polygons;
- the disk-intersection definition of Reuleaux polygons;
- the theorem that the regular Reuleaux `nu`-gon maximizes area among width-fixed Reuleaux `nu`-gons, reviewed in modern work on Reuleaux-polygon area variation.

No 2026 unreviewed maximum-perimeter power-of-two result is used.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

RE makes F an exact Reinhardt q-gon. Let R be its width-D Reuleaux completion and
S subset V(F) the defining Reuleaux vertices. Since
  R = intersection_{c in S} B(c,D),
and R has diameter D while V(F) subset R,
  intersection_{p in V(F)} B(p,D) = R.
Every source point is within D of every p in V(F), hence A subset R.
C65 rattlers are not diameter endpoints, so they lie in int(R).

Oler + Barbier + strict global diameter comparison give
  area(R) > pi D^2/4 - (pi sqrt3/4)D - sqrt3/2.
Thus the disk-area deficit is O(D).

If nu is the odd Reuleaux/diameter-cycle core size, the regular Reuleaux nu-gon
maximizes area and has
  A_reg/D^2 = pi/2 - (nu/2) tan(pi/(2nu)).
Using tan x >= x+x^3/3,
  pi D^2/4-area(R) >= pi^3 D^2/(48nu^2).
Therefore
  nu^2 > pi^3 D^2/[12 sqrt3 (pi D+2)],
so
  liminf nu/sqrt(D) >= pi/sqrt(12sqrt3)=0.6890947417...

Next: exploit prescribed unit-spaced shell points on partial R to beat generic Oler
boundary correction, or combine the growing odd core with the 2D KKT polytope.
```
