> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_interior_diameter_descent_2026-09-09.md) · source SHA-256 `9ae7771985e77c3ec9aa4325ec5a3fb5bfc32e4f8060b9335339eea6a7a531f8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8AF01C1EF2BA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic force-bulk closure gives exact interior diameter descent

**Date:** 2026-09-09  
**Repository branch:** PR #118 after UFB  
**Run type:** exact source-population descent theorem  
**Target:** complete cyclic primitive endpoint, all `d_H=0,1,2`  
**Depends on:** UFB `F=conv A`, CY actual contact graph `C_q` plus contact-isolated source points, C-I restoration  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

UFB puts the complete source inside the cyclic force hull. The lexicographic C-I source has actual unit-contact graph equal to the positive contact cycle `C_q`, so every one of the remaining `n-q` source points is contact-isolated.

The prescribed unit hull sides then force a universal boundary collar. Removing the `q` shell points leaves a legitimate unit-separated configuration whose diameter is smaller by more than `sqrt(3)`.

### Theorem ID — universal cyclic interior descent

Let `A` be a sufficiently large cyclic primitive triangle-free global minimizer of cardinality `n` and diameter

$$
D=D(n).
$$

Let

$$
Z:=A\setminus V(F),
\qquad |Z|=n-q.
$$

Then

$$
\boxed{
\operatorname{dist}(z,\partial F)>\frac{\sqrt3}{2}
\qquad(z\in Z).}
\tag{ID.1}
$$

Consequently

$$
\boxed{
\operatorname{diam}Z<D-\sqrt3,}
\tag{ID.2}
$$

and therefore the global optimum values satisfy

$$
\boxed{
D(n-q)<D(n)-\sqrt3.}
\tag{ID.3}
$$

This holds in all three cyclic diameter-topology phases.

Because RP gives

$$
q=\pi D-\frac\pi{24D}+O(D^{-2}),
\tag{ID.4}
$$

ID is an exact one-step descent on the asymptotically natural shell scale: deleting approximately `pi D` source points decreases achievable diameter by strictly more than `sqrt(3)`.

---

## 1. Every non-shell source point is strictly farther than one from every shell vertex

CY gives the positive contact core

$$
C_q
$$

on the `q` force-hull vertices. UFB gives

$$
F=\operatorname{conv}A.
$$

The promoted C-I restoration identifies the actual unit-contact graph with the positive contact graph. Therefore every point

$$
z\in Z=A\setminus V(F)
$$

has no unit contact with any source point. Unit separation then gives

$$
\boxed{|z-p|>1\qquad(p\in A\setminus\{z\}).}
\tag{1.1}
$$

In particular this holds for every hull vertex.

---

## 2. Unit hull sides force the `sqrt(3)/2` collar

Fix `z in Z` and let

$$
r:=\operatorname{dist}(z,\partial F).
$$

Choose a nearest boundary point `y`.

If `y` is a hull vertex, then by (1.1)

$$
r=|z-y|>1>\frac{\sqrt3}{2}.
$$

Otherwise `y` lies in the relative interior of one hull side `ab`. CY gives

$$
|a-b|=1.
$$

Because `y` is the nearest point of a convex polygon side, `zy` is perpendicular to the side. One of the two endpoints, call it `p`, satisfies

$$
|y-p|\le\frac12.
$$

Thus

$$
|z-p|^2
=r^2+|y-p|^2
\le r^2+\frac14.
$$

Equation (1.1) gives `|z-p|>1`, hence

$$
r^2+\frac14>1.
$$

Therefore

$$
\boxed{r>\frac{\sqrt3}{2}.}
$$

This proves ID.1. `square`

---

## 3. Finite strict collar for the complete interior population

The set `Z` is finite. Hence the minimum collar depth

$$
r_*:=\min_{z\in Z}\operatorname{dist}(z,\partial F)
$$

exists and satisfies

$$
\boxed{r_*>\frac{\sqrt3}{2}.}
\tag{3.1}

Thus

\[
Z\subseteq F_{-r_*},
$$

where

$$
F_{-r_*}:=
\{x:x+r_*B_2\subseteq F\}
$$

is the convex inner parallel body.

---

## 4. Inner parallels lose twice the collar in every width

For every unit direction `u`, support-function inclusion

$$
F_{-r_*}+r_*B_2\subseteq F
$$

gives

$$
h_{F_{-r_*}}(u)+r_*\le h_F(u)
$$

and the same inequality for `-u`. Therefore

$$
\boxed{
w_{F_{-r_*}}(u)
\le w_F(u)-2r_*.}
\tag{4.1}

The diameter of a compact convex body is the maximum directional width. Since

\[
\operatorname{diam}F=D,
$$

we obtain

$$
\operatorname{diam}F_{-r_*}
\le D-2r_*
<D-\sqrt3.
\tag{4.2}

Because `Z subseteq F_{-r_*}`,

\[
\operatorname{diam}Z
\le\operatorname{diam}F_{-r_*}
<D-\sqrt3.
$$

This proves ID.2. `square`

---

## 5. Convert the interior set into a global optimum inequality

The set `Z` contains exactly `n-q` source points and remains unit-separated because it is a subset of the original source.

By definition of the optimum diameter function,

$$
D(n-q)
\le\operatorname{diam}Z.
$$

Using ID.2,

$$
\boxed{
D(n-q)<D(n)-\sqrt3.}
$$

This proves ID.3. `square`

The strict inequality is finite and source-specific. No asymptotic density theorem is used in its proof.

---

## 6. Why the scale is notable

Write

$$
\Delta=\frac\pi{2\sqrt3}.
$$

The leading asymptotic law is

$$
D(n)\sim\sqrt{n/\Delta}.
$$

Removing `q~pi D` points from a configuration of diameter `D` changes the leading-order radius by

$$
\frac{q}{2\Delta D}
\sim
\frac\pi{2\Delta}
=\sqrt3.
$$

Thus ID sits exactly at the first derivative of the planar packing law:

$$
\boxed{
q\sim\pi D
\quad\leftrightarrow\quad
\Delta D^2-\Delta(D-\sqrt3)^2
\sim\pi D.}
\tag{6.1}

The theorem therefore captures the correct first-order shell-removal scale with a strict finite inequality. Any second-order asymptotic control on `D(n)` strong enough to resolve this one-step comparison could close the cyclic endpoint.

---

## 7. Relation to RD

In the exact `d_H=0` Reinhardt phase, RD gives the slightly stronger explicit collar

\[
r_D
=\frac{\sqrt3}{2}+\frac1{8D}+O(D^{-3}),
$$

hence

$$
\operatorname{diam}Z
\le
D-\sqrt3-\frac1{4D}+O(D^{-3}).
$$

ID is weaker numerically there but has two advantages:

1. it applies to `d_H=1,2` as well;
2. its strictness requires no Reuleaux completion or equality classification.

---

## 8. Regression audit

### Point above a unit side midpoint

The non-strict geometric threshold `sqrt(3)/2` is sharp for a point at unit distance from both side endpoints. Actual C-I contact-isolation turns this into a strict inequality for every rattler.

### Arbitrarily small contact slack

Allowed. The theorem does not claim a uniform improvement beyond `sqrt(3)/2` in the `d_H=1,2` phases. The finite set supplies a source-dependent strict margin `r_*-sqrt(3)/2>0`, sufficient for ID.3.

### Interior pair distances

No additional assumption is needed. `Z` inherits unit separation from `A`.

### C1/C65 normalization

ID works on the existing C65 cyclic source. It does not invoke contact-preserving hull saturation.

---

## 9. New exact endpoint

Every cyclic survivor now implies the simultaneous pair

$$
\boxed{
q=\pi D-\frac\pi{24D}+O(D^{-2}),}
$$

$$
\boxed{
D(n-q)<D(n)-\sqrt3.}
$$

This converts the source-population problem from an internal Oler estimate into a direct discrete inequality for the global optimum sequence `D(n)`.

The next high-value route is to sharpen known upper/lower estimates for `D(m)` enough to compare these two sides at second order. A contradiction would eliminate the entire cyclic endpoint without resolving its three diameter-topology subphases individually.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

The proof is elementary downstream of report-level UFB/CY/RP and promoted C-I restoration.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

UFB: F=conv(A) in every cyclic phase. C-I/CY: the only actual unit contacts are the
q unit hull-cycle edges. Therefore every interior point z has |z-p|>1 for every hull
vertex p.

Let r=dist(z,partial F). If nearest point is a hull vertex, r>1. If it lies inside a
unit side, the nearer side endpoint is tangentially <=1/2 away, so
  1<|z-p|^2<=r^2+1/4,
therefore
  r>sqrt(3)/2.
For the finite interior set Z, r_*=min depth>sqrt(3)/2.
Since F_-r_* + r_* B subset F, every width drops by at least 2r_*:
  diam(Z)<=diam(F_-r_*)<=D-2r_*<D-sqrt3.
Thus
  D(n-q)<=diam(Z)<D(n)-sqrt3.

Together with RP
  q=pi D-pi/(24D)+O(D^-2),
this is an exact one-step descent at the first-derivative scale of D(n)~sqrt(n/Delta).
Next: second-order control of the global optimum sequence D(n).
```
