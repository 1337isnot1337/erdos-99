> Generated reading edition · [exact source](../../../docs/reports/target_c_nearcircle_giant_face_dichotomy_2026-09-09.md) · source SHA-256 `dc47b58f4e3283ba1f07f05f5f794cc2821cccd5a6d0b039b965d492987e375e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AB4EC0FC3933","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_nearcircle_giant_face_dichotomy_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=4927e0a0139714d0b00be1019e8024acf426a1c5; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — near-circle core-or-giant-face dichotomy

**Date:** 2026-09-09  
**Repository base:** PR #119 after DG/DC/DS/OW  
**Run type:** exact population localization  
**Target:** post-ZF `x_B=o(D)` endpoint  
**Depends on:** C49/C51/C52, DB exceptional-perimeter bound, DC, OW  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The DG/DC endpoint has a near-circular force hull. OW removes quadratic population from the internal outer face and DC removes quadratic population outside the force hull. Since C65's points outside the positive contact core are exactly contact-isolated rattlers, any remaining quadratic population deficit of the core must lie inside bounded nonquadrilateral contact faces.

Facewise Oler then forces a macroscopic convex exceptional face.

Precisely, if

```math
\zeta:=\liminf\frac{n-v}{D^2}>0,
```

then along a subsequence some bounded exceptional face has perimeter

```math
\boxed{
 k_{max}\ge\left(\frac{2\sqrt3}{5}\zeta-o(1)\right)D.
}
```

Thus the `x_B=o(D)` endpoint has only two population regimes:

1. `n-v=o(D^2)`, an asymptotically full positive contact core;
2. a single bounded strict-convex defect face of perimeter `Omega(D)` containing a macroscopic part of the invisible population.

---

## 1. Population partition

Let `v=|V(C)|` be the C65 positive contact-core population. Every source point outside `C` is contact-isolated. C49/C52 partition these isolated points into

- `Z_def`: points in bounded nonquadrilateral contact faces;
- `Z_in`: points in the outer contact face but inside the force hull `F`;
- `Z_ext`: points outside `F`.

Therefore exactly

```math
\boxed{
n-v=Z_{def}+Z_{in}+Z_{ext}.}
\tag{1.1}
```

Quadrilateral contact faces contain no isolated points in this decomposition; all bounded-face rattlers lie in exceptional faces.

---

## 2. The DG endpoint removes both outer populations at quadratic scale

Assume

```math
x_B=o(D).
```

OW proves

```math
Z_{in}
\le\frac8{\pi\sqrt3}x_B^2
=o(D^2).
\tag{2.1}
```

DC proves

```math
Z_{ext}=o(D^2).
\tag{2.2}
```

Hence (1.1) becomes

```math
\boxed{
Z_{def}=n-v-o(D^2).
}
\tag{2.3}
```

In particular, if along a subsequence

```math
n-v\ge(\zeta-o(1))D^2
```

for some `zeta>0`, then

```math
\boxed{
Z_{def}\ge(\zeta-o(1))D^2.
}
\tag{2.4}
```

---

## 3. Each isolated point in an exceptional face costs face area

Let `f` be one bounded exceptional contact face. C51 makes its closure a strict convex unit-edge polygon. Write

- `k_f>=5` for its perimeter/number of boundary vertices;
- `z_f` for the isolated source points in its interior;
- `A_f` for its area.

The `k_f+z_f` points consisting of its boundary vertices and assigned isolated points are unit-separated inside the convex body `f`. Oler gives

```math
k_f+z_f
\le
\frac2{\sqrt3}A_f+rac12k_f+1.
```

Therefore

```math
z_f
\le
\frac2{\sqrt3}A_f+1-\frac{k_f}{2}
\le
\frac2{\sqrt3}A_f,
```

because `k_f>=5`.

Thus

```math
\boxed{
A_f\ge\frac{\sqrt3}{2}z_f.
}
\tag{3.1}
```

Summing over all exceptional faces,

```math
\boxed{
A_{exc}:=\sum_fA_f
\ge\frac{\sqrt3}{2}Z_{def}.
}
\tag{3.2}
```

Hence (2.4) implies

```math
A_{exc}
\ge
\left(\frac{\sqrt3}{2}\zeta-o(1)\right)D^2.
\tag{3.3}
```

---

## 4. Total exceptional perimeter is only linear

Let

```math
Q=\sum_f(k_f-4).
```

If `f_count` is the number of exceptional faces, their total perimeter is

```math
K_{exc}:=\sum_fk_f
=Q+4f_{count}.
```

Since every exceptional face has `k_f>=5`,

```math
f_{count}\le Q,
```

so

```math
K_{exc}\le5Q.
\tag{4.1}
```

DB proves post-ZF

```math
Q<\pi D+O(1).
```

Therefore

```math
\boxed{
K_{exc}\le5\pi D+O(1).
}
\tag{4.2}
```

---

## 5. Quadratic exceptional area forces one giant face

Let

```math
k_{max}:=\max_fk_f.
```

Every exceptional face is convex, so the isoperimetric inequality gives

```math
A_f\le\frac{k_f^2}{4\pi}.
```

Hence

```math
A_{exc}
\le
\frac1{4\pi}\sum_fk_f^2
\le
\frac{k_{max}}{4\pi}K_{exc}.
\tag{5.1}
```

Combine (3.3) and (4.2):

```math
\left(\frac{\sqrt3}{2}\zeta-o(1)\right)D^2
\le
\left(\frac54+o(1)\right)k_{max}D.
```

Therefore:

### Theorem GF — core-or-giant-face dichotomy

If `x_B=o(D)` and

```math
\liminf\frac{n-v}{D^2}=\zeta>0,
```

then along a subsequence

```math
\boxed{
\liminf\frac{k_{max}}D
\ge\frac{2\sqrt3}{5}\zeta.
}
\tag{GF.1}
```

Since any convex body of perimeter `k` has diameter at least `k/pi`, the same face has

```math
\boxed{
\operatorname{diam}(f)
\ge
\left(\frac{2\sqrt3}{5\pi}\zeta-o(1)\right)D.
}
\tag{GF.2}
```

Thus the invisible quadratic population cannot be dispersed among microscopic defect faces.

---

## 6. Stronger version retaining `Q`

Before using `Q<=pi D`, (3.3), (4.1), and (5.1) give

```math
k_{max}
\ge
\frac{4\pi A_{exc}}{5Q}
\ge
\left(
\frac{2\pi\sqrt3}{5}
\frac{\zeta D}{Q}
-o(1)
\right)D.
\tag{6.1}
```

Thus if `Q/D->xi>0`,

```math
\boxed{
\liminf\frac{k_{max}}D
\ge
\frac{2\pi\sqrt3}{5\xi}\zeta.
}
\tag{6.2}
```

The universal coefficient in GF.1 is the weaker specialization `xi<=pi`.

---

## 7. Interaction with the full-core branch

GF leaves exactly two branches in the DG endpoint.

### Branch I — full core

```math
n-v=o(D^2).
```

Then the existing DE/DF train asymptotics apply directly. In addition DG/DC already provide the stronger near-circle boundary profile

```math
q/D\to\pi,
\quad
per(F)/D\to\pi,
\quad
area(F)/D^2\to\pi/4,
\quad
e_{BB}/D\to\pi.
```

### Branch II — giant defect face

There is a bounded strict convex unit-edge face with perimeter `Omega(D)` and diameter `Omega(D)` containing a quadratic isolated population.

This branch is the large-scale analogue of the finite regular-shell-plus-rattler regression: mechanically visible stress can remain on an outer/core shell while a macroscopic population sits invisibly inside one convex cavity.

A closing theorem must now eliminate either the full-core near-circle phase or this one giant convex cavity.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

C65 population identity:
    n-v=Z_def+Z_in+Z_ext.
In x_B=o(D):
    OW -> Z_in=o(D^2),
    DC -> Z_ext=o(D^2),
so
    Z_def=n-v-o(D^2).

For an exceptional convex k-face with z isolated interior points, facewise Oler gives
    area(f)>=(sqrt3/2) z.
Thus if (n-v)/D^2->zeta>0,
    A_exc>=(sqrt3/2 zeta-o(1))D^2.

DB gives total exceptional perimeter
    K_exc<=5Q<=5pi D+O(1).
Isoperimetry gives
    A_exc<=k_max K_exc/(4pi).
Therefore
    k_max/D>=2sqrt3 zeta/5-o(1).

So the x_B=o(D) endpoint is:
    asymptotically full positive core,
or
    one bounded convex exceptional face of perimeter Omega(D) containing quadratic
    invisible population.
```
