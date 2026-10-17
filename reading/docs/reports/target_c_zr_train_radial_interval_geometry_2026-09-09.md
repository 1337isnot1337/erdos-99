> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_train_radial_interval_geometry_2026-09-09.md) · source SHA-256 `1dfdeee1abd382390eae4525e0a41aa51473faaa178fb4d7f313f23f8064a52a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 6 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-88A7CAA60BFD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZWG: weak-rich trains contain macroscopic nonradial strips

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-weak-transverse-train`  
**Base:** stacked on PR #111  
**Run type:** exact train geometry + ZWT mechanical localization  
**Target:** Target C, ZCQ-ZRI-ZWT branch  
**Depends on:** DT, ZRP, ZRI, ZWT  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZWT proves that `Omega_eta(D)` stopped trains each contain `Omega_eta(D)` distinct weak nonradial contact edges. This report adds a geometric fact special to trains: for one fixed train direction, the strongly-radial contact edges can occur in only a bounded number of contiguous intervals along the train.

The reason is exact. Train midpoints move mainly in the direction normal to their parallel contact edges: normal progress is `>sqrt(3)/2` per rhombus while tangential drift is `<1/2`. On the other hand the locus of midpoints for which a parallel unit segment is strongly radial about `z` is the union of two hyperbolic cones whose boundary slope rapidly exceeds `1/sqrt(3)`. A train cannot weave in and out of either cone.

Consequently the nonradial edges of every train form at most three intervals. Every ZWT weak-rich train therefore has a **contiguous nonradial run of length Omega_eta(D)**. Since the total nonradial KKT stress is `o(D^2)`, on all but `o(D)` of the weak-rich trains that macroscopic run contains only `o(D)` contacts above any suitable weak threshold.

This upgrades the branch from a diffuse weak-edge population to linearly many macroscopic weak transverse strips.

---

## 1. Midpoint coordinates along one stopped train

Fix a stopped train `tau`. Let `u` be a unit vector parallel to every contact edge belonging to `tau`, and use orthonormal coordinates

```math
(x,y)=(m\cdot u,\ m\cdot Ju)
```

for contact-edge midpoints `m`, after translating the C66 center `z` to the origin.

Orient the train as in DT so that `y` increases through every rhombus. If successive train-edge midpoints are

```math
m_j=(x_j,y_j),
\qquad
m_{j+1}=(x_{j+1},y_{j+1}),
```

then the midpoint step is a unit vector making angle strictly less than `pi/6` with `Ju`. Therefore

```math
\boxed{
 y_{j+1}-y_j>\frac{\sqrt3}{2},
\qquad
|x_{j+1}-x_j|<\frac12.
}
\tag{ZWG1}
```

In particular

```math
\boxed{
\frac{|x_{j+1}-x_j|}{y_{j+1}-y_j}<\frac1{\sqrt3}.
}
\tag{ZWG2}
```

---

## 2. Exact strongly-radial locus for a parallel unit edge

The contact edge centered at `m=(x,y)` has endpoints

```math
m\pm\frac12u.
```

Let

```math
d(x,y)
:=
\left|
\left|m+\frac12u\right|
-
\left|m-\frac12u\right|
\right|.
\tag{2.1}
```

ZRP calls the edge strongly radial when

```math
d(x,y)>c_*:=\cos15^\circ.
\tag{2.2}
```

The level set `d=c_*` is the standard hyperbola with foci `+-u/2` and focal-distance difference `c_*`. Put

```math
s_*:=\sin15^\circ.
```

Its equation is

```math
\frac{x^2}{(c_*/2)^2}
-
\frac{y^2}{(s_*/2)^2}
=1.
\tag{2.3}
```

Therefore the strongly-radial locus is exactly

```math
\boxed{
|x|>g(|y|),
\qquad
g(t):=\frac{c_*}{2}
\sqrt{1+\frac{4t^2}{s_*^2}}.
}
\tag{ZWG3}
```

This is the union of the two open hyperbolic cones pointing in the `+u` and `-u` directions.

---

## 3. The hyperbola outruns the train outside an absolute central band

For `t>0`,

```math
g'(t)
=
\frac{2c_*t/s_*^2}
{\sqrt{1+4t^2/s_*^2}}.
\tag{3.1}
```

The derivative is increasing and tends to

```math
\frac{c_*}{s_*}=\cot15^\circ>\frac1{\sqrt3}.
```

Let `t_0>0` be the unique solution of

```math
g'(t_0)=\frac1{\sqrt3}.
\tag{3.2}
```

Explicitly,

```math
t_0^2
=
\frac{s_*^4}{4(3c_*^2-s_*^2)},
\tag{3.3}
```

so numerically `t_0<0.021`.

Since successive train midpoints have `y`-spacing greater than `sqrt(3)/2>0.86`, the central strip

```math
|y|\le t_0
```

contains at most one train midpoint.

For `y>=t_0`, (ZWG2) and `g'(y)>1/sqrt(3)` imply that

```math
x_j-g(y_j)
```

strictly decreases with `j`, while

```math
-x_j-g(y_j)
```

also strictly decreases.

For `y<=-t_0`, as the train advances toward zero, `g(|y|)` decreases faster than `x` can drift; both corresponding signed differences strictly increase.

Thus, on either side of the one-point central strip, a train can cross each hyperbola branch in only one direction.

---

## 4. Radial and nonradial train intervals

Consider the index set of train edges satisfying the positive-cone condition

```math
x_j>g(|y_j|).
```

By Section 3 it is one contiguous interval of train indices, up to the possible single central midpoint. The negative-cone condition

```math
-x_j>g(|y_j|)
```

likewise gives one contiguous interval. The two cone conditions are disjoint.

Absorbing the possible central index into a neighboring interval if needed gives:

### Theorem ZWG.1 — bounded radial interval complexity

Along every stopped train, the set of strongly-radial contact edges is the union of at most two contiguous index intervals, up to at most one isolated central edge.

Consequently the set of nonradial contact edges is the union of at most four intervals, and after absorbing the one central edge one may use the safe bound

```math
\boxed{
\text{nonradial train-edge indices are covered by at most four contiguous intervals.}
}
\tag{ZWG4}
```

A slightly sharper bookkeeping gives three intervals when no central exceptional edge is separated; the constant four is retained to avoid endpoint convention issues.

---

## 5. Every weak-rich train has a macroscopic contiguous nonradial run

ZWT gives constants depending only on fixed `eta` such that every weak-rich train contains at least

```math
k_\eta D
\tag{5.1}
```

distinct weak nonradial contact edges, where one can take

```math
k_\eta=\frac{c_\eta}{12\pi}+o(1)
```

at leading order.

In particular the train contains at least `k_eta D` nonradial edges total. By ZWG4, one contiguous nonradial interval has length at least one quarter of that total.

Hence:

### Corollary ZWG.2 — macroscopic nonradial strip on every weak-rich train

Every weak-rich train contains a contiguous run of at least

```math
\boxed{
\left(\frac{c_\eta}{48\pi}-o(1)\right)D
}
\tag{ZWG5}
```

consecutive train contact edges, every one of which is outside the strongly-radial path forest.

Since ZWT supplies `Omega_eta(D)` weak-rich trains, the branch contains `Omega_eta(D)` pairwise edge-disjoint macroscopic nonradial train strips.

---

## 6. Mechanical visibility is sparse on almost all such strips

Use the explicit ZLS weak threshold

```math
a_D=\sqrt{\delta_D},
\qquad
\delta_D=D\varepsilon\to0.
```

ZLS/ZRP give

```math
\#\{e\notin C_{rad}:\alpha_e\ge a_D\}
=o(D^2).
\tag{6.1}
```

For each weak-rich train choose one macroscopic nonradial run supplied by ZWG5. Distinct trains have disjoint contact-edge sets.

Fix any constant `rho>0`. A chosen run is `rho`-exceptional if at least `rho D` of its edges satisfy `alpha_e>=a_D`. The number of `rho`-exceptional runs is at most

```math
\frac{o(D^2)}{\rho D}=o(D).
\tag{6.2}
```

Therefore:

### Theorem ZWG.3 — linear family of macroscopically weak strips

For every fixed `rho>0`, all but `o(D)` of the `Omega_eta(D)` weak-rich trains contain a contiguous nonradial run of length `Omega_eta(D)` on which fewer than `rho D` contacts have stress `>=a_D`.

By diagonalizing `rho=rho_D->0` sufficiently slowly, one obtains a linear-size train family whose chosen macroscopic runs satisfy

```math
\boxed{
\#\{e\text{ in run}:\alpha_e\ge a_D\}=o(D).
}
\tag{ZWG6}
```

Thus each selected strip has weak-contact density tending to one.

---

## 7. Geometric meaning

A train is a chain of rhombi traversed in the direction normal to its parallel contact edges. ZWG says that linearly many such chains contain a macroscopic contiguous segment of rhombi whose train-side contacts remain outside the radial mechanical skeleton throughout the segment.

On almost every selected strip, all but `o(D)` of those contacts also have stress below `a_D->0`.

The near-zero branch therefore contains a linear-by-linear **strip complex**:

```text
Omega_eta(D) stopped trains,
each with one contiguous Omega_eta(D)-long nonradial segment,
weak KKT stress on a 1-o(1) fraction of contacts in that segment.
```

This is substantially stronger than a quadratic set of unrelated weak braces.

---

## 8. Binding regression and next target

An oblique rhombic grid still realizes the geometric part of ZWG: one family of long transverse trains can remain nonradial across macroscopic strips while an approximately orthogonal/radial family carries the load.

The new source-specific information not present in that abstract regression is:

- the ZSP `D+o(D)` diameter contact path;
- ZHA's linear ordered family of loaded extreme attachments;
- ZOB/HB/PC exact outer-face currency;
- current-main PI force-hull area and pocket floor;
- the fact that each selected train is **stopped** at actual outer or exceptional faces.

The next theorem should use strip endpoints, not raw crossing density:

> Prove that `Omega(D)` edge-disjoint macroscopic weak strips cannot all terminate on the available outer/exceptional face system of a globally diameter-minimal source without forcing either a forbidden large outer-pocket budget, a pure-rhombic train disk to which the Target-B exposed-hull contradiction applies, or a strict sub-`D` deformation.

---

## 9. Classification

**Status:** proved report-level train-geometry refinement.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.
