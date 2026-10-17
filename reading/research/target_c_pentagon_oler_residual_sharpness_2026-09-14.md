> Generated reading edition · [exact source](../../research/target_c_pentagon_oler_residual_sharpness_2026-09-14.md) · source SHA-256 `6fbf0aa305d83b6bd93881f5942ebd6cfdedd6800dce7e405c611094fcb0a751`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3ddc04724b817abddcc2e6d721cff9eaee60fbf2", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_pentagon_oler_residual_sharpness_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "722c6c01ee89230772ee53a08dd965a64f7ab73b8b6157f6e122586f7ba054b4"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — the exceptional-pentagon Oler residual has zero local gap

**Date:** 2026-09-14
**Repository base:** `e2f62aa7`
**Run type:** regression theorem / elimination of a false closing route
**Target:** Target C-II full-core exceptional-face branch
**Claim class:** exact local construction
**External literature:** none

## LEVEL I STATUS

`STILL OPEN`

The exact chamber decomposition isolates the nonnegative absorption residual

```math
\mathcal R_{ch}
=(A_{ch}-a_0Z_{ch})-c_0[(b-P_F)+(Q+2f)].
```

Since the latest bootstrap forces `f=Omega(D)`, a tempting closure route is to seek a
uniform positive contribution to `R_ch` from each bounded exceptional face. This is
impossible at the level of one face.

For a pentagonal contact face with no interior source point, canonical Section 67.19
is

```math
\operatorname{area}(P)\ge a_0+c_0={3\sqrt3\over4}.
\tag{P.1}
```

The lower bound is sharp as an infimum even among strictly convex equilateral
pentagons whose five diagonals are all strictly longer than one. Thus triangle-freeness
alone gives no positive additive gap beyond (P.1).

## 1. Symmetric one-parameter family

Put

```math
y_0={\sqrt3\over2}.
```

For `y>y_0` sufficiently close to `y_0`, set

```math
A=(0,0),\qquad B=(1,0),\qquad D=(1/2,y).
```

Let `C` be the right-hand intersection of the two unit circles centered at `B` and
`D`, and let `E` be the reflection of `C` across the vertical line `x=1/2`.

Write

```math
d=|B-D|=\sqrt{y^2+1/4},
\qquad
s=\sqrt{1-d^2/4}.
```

The circle-intersection formula gives

```math
C=
\left(
{3\over4}+{sy\over d},
{y\over2}+{s\over2d}
\right)
=:(x_C,y_C),
\tag{P.2}
```

and

```math
E=(1-x_C,y_C).
\tag{P.3}
```

By construction

```math
|A-B|=|B-C|=|C-D|=|D-E|=|E-A|=1.
\tag{P.4}
```

At `y=y_0`,

```math
C=(3/2,y_0),\qquad D=(1/2,y_0),\qquad E=(-1/2,y_0),
```

so the limiting polygon has three collinear top vertices and area `3sqrt(3)/4`.

## 2. Strict convexity for `y>y_0`

At `y_0`, `d=1` and `s/d=sqrt(3)/2`. Put

```math
r(y):={s\over d}=\sqrt{{1\over d^2}-{1\over4}}.
```

Since `d'(y_0)=sqrt(3)/2`, direct differentiation gives

```math
r'(y_0)=-1.
```

From (P.2),

```math
y_C={y\over2}+{r(y)\over2},
```

so

```math
y_C'(y_0)=0.
```

Consequently

```math
{d\over dy}(y-y_C)\bigg|_{y=y_0}=1.
```

Thus `D` lies strictly above the horizontal segment `CE` for every sufficiently small
`y-y_0>0`. The remaining four turns are already strictly positive at the limiting
configuration. By continuity, `A,B,C,D,E` form a strictly convex pentagon for all
sufficiently small positive `y-y_0`.

## 3. Every diagonal is strictly longer than one

The two diagonals from `D` to the lower vertices have the same length

```math
|D-A|=|D-B|=d>1
\tag{P.5}
```

because `y>y_0`.

At the limiting value `y=y_0`, the remaining three diagonals have lengths

```math
|A-C|=|B-E|=\sqrt3,
\qquad
|C-E|=2.
```

They therefore remain strictly larger than one for all sufficiently small positive
`y-y_0` by continuity.

Hence the five vertices are unit-separated, adjacent pairs are exactly the five unit
contacts, and no unit equilateral triangle occurs.

## 4. Area tends to the Section-67 baseline

By symmetry and the shoelace formula,

```math
\operatorname{area}(ABCDE)
={1\over2}\left[y_C+y(2x_C-1)\right].
\tag{P.6}
```

Both coordinates in (P.2) are continuous at `y_0`, so

```math
\lim_{y\downarrow y_0}
\operatorname{area}(ABCDE)
={1\over2}\left[y_0+2y_0\right]
={3\sqrt3\over4}
=a_0+c_0.
\tag{P.7}
```

Therefore, for every `epsilon>0`, some strictly convex triangle-free equilateral
pentagon satisfies

```math
0<\operatorname{area}(P)-(a_0+c_0)<\epsilon.
\tag{P.8}
```

The strict left inequality follows from Oler/Section 67.19 and the fact that the
limiting equality configuration is degenerate.

## 5. Consequence for the C-II program

There is no constant `eta>0` such that every bounded pentagonal contact face with no
interior source point obeys

```math
\operatorname{area}(P)
\ge a_0+c_0+\eta.
```

Thus the linear face count

```math
f\ge0.1671246\ldots D-o(D)
```

cannot by itself force `R_ch=Omega(D)` through a purely local area gap. Any positive
residual theorem must use information absent from this construction, such as

- phase-conditioned adjacent rhombus directions;
- the doubled near-geodesic corridor geometry from canonical Section 84;
- diameter/KKT support; or
- interactions among many exceptional faces.

This explicitly validates the near-degenerate pentagon regression as a binding
obstruction and narrows the useful form of any residual-gluing closure theorem.

## 6. Scope

The construction is local. It does not claim that these pentagons can occur with
linear density inside a global Type-II minimizer. Its purpose is the opposite: it
proves that such a global theorem cannot be replaced by a uniform one-face gap.

**Disposition:** exact regression theorem. C-II remains open.
