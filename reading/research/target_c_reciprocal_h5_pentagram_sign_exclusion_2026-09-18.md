> Generated reading edition · [exact source](../../research/target_c_reciprocal_h5_pentagram_sign_exclusion_2026-09-18.md) · source SHA-256 `60b16cee71aeb1901461521fc8a6671878dc784d931137f594f1eafba5961ad0`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "48bbb669f1d6e851aba3ce8130832cbd221b6808", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_reciprocal_h5_pentagram_sign_exclusion_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "9472df7ce3ae33077b2631df832ccabbafb5d0771bd5bb0a9f14961e69e31754"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — exclude the H5 pentagram reciprocal sign class by signed length balance

**Date:** 2026-09-18  
**Status:** proved candidate; theorem-state authority unchanged  
**Scope:** the five-hull-vertex branch of the minimal reciprocal `K_6` obstruction  
**Depends on:** `target_c_one_anchor_k5_reciprocal_unit_force_2026-09-18.md`; `target_c_reciprocal_hull_angle_sign_split_2026-09-18.md`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The reciprocal hull-angle theorem leaves an H5 regime: five reciprocal points
`v_0,...,v_4` in cyclic convex position and one interior reciprocal point `x`.
The signed inverse-distance equilibrium has the exact signed length balance

```math
\sum_{s_{ij}=+1}|y_i-y_j|
=
\sum_{s_{ij}=-1}|y_i-y_j|.
\tag{0.1}
```

One natural H5 sign class is the pentagram class: all five hull diagonals have one sign,
while all five hull-boundary edges and all five spokes from the interior point have the
opposite sign.  This class is impossible.  The proof is a strict metric inequality and
does not use the source `<120` turn-gap theorem.

Because global reversal of all reciprocal signs leaves both equilibrium and (0.1)
unchanged, it is enough to take the hull diagonals positive.

---

## 1. Three length sums

Write

```math
P:=\sum_{i\in\mathbb Z/5}|v_i-v_{i+1}|
\tag{1.1}
```

for the convex-hull perimeter,

```math
D:=\sum_{i\in\mathbb Z/5}|v_i-v_{i+2}|
\tag{1.2}
```

for the sum of the five pentagram diagonals, and

```math
S:=\sum_{i\in\mathbb Z/5}|v_i-x|
\tag{1.3}
```

for the five spoke lengths.

Under the pentagram sign assignment, the exact reciprocal signed length balance (0.1)
would require

```math
\boxed{D=P+S.}
\tag{1.4}
```

We show instead that `D<P+S` for every general-position six-point H5 configuration.

---

## 2. Boundary paths give `D<2P`

For every `i`, the three hull vertices

```math
v_i,\ v_{i+1},\ v_{i+2}
```

are noncollinear.  Strict triangle inequality gives

```math
|v_i-v_{i+2}|
<
|v_i-v_{i+1}|+|v_{i+1}-v_{i+2}|.
\tag{2.1}
```

Summing over `i mod 5`, each hull side occurs exactly twice on the right, hence

```math
\boxed{D<2P.}
\tag{2.2}
```

---

## 3. Interior two-spoke paths give `D<2S`

The reciprocal theorem gives no three collinear reciprocal points.  Therefore `x` does
not lie on any line through a hull diagonal pair `v_i,v_{i+2}`.  Strict triangle
inequality gives

```math
|v_i-v_{i+2}|
<
|v_i-x|+|x-v_{i+2}|.
\tag{3.1}
```

Summing over the five diagonals, every spoke occurs exactly twice, so

```math
\boxed{D<2S.}
\tag{3.2}
```

---

## 4. Contradiction with reciprocal signed length balance

From (2.2)--(3.2),

```math
D<2\min(P,S).
\tag{4.1}
```

For positive `P,S`,

```math
2\min(P,S)\le P+S.
\tag{4.2}
```

Therefore

```math
\boxed{D<P+S,}
\tag{4.3}
```

contradicting the exact equilibrium consequence (1.4).

Hence:

```math
\boxed{
\text{No H5 reciprocal unit-force equilibrium can have one sign on all five hull
pentagram diagonals and the opposite sign on all hull sides and all five spokes.}
}
\tag{4.4}
```

The globally reversed sign class is excluded simultaneously.

---

## 5. Why this matters for the finite reciprocal classification

The H5 hull-angle theorem already forces a `2+3` sign split at every hull vertex.  The
pentagram class is the maximally symmetric realization of that local degree condition:
with diagonals positive, every hull vertex has two positive diagonal edges and three
negative edges (its two boundary edges and its spoke).  Equivalently, after global sign
reversal, the five hull sides together with all five spokes are positive and the five
diagonals are negative.

The exclusion above shows that local signed-degree feasibility is not sufficient.  The
global tensor/trace identity rules out this entire H5 sign class before any nonlinear
coordinate solving.

The remaining H5 classes must mix the signs among diagonals and/or spokes.  They can now
be attacked using the same three independent structures already available in the repo:

- the exact signed length and second-moment balances;
- the source-derived `<120` force-direction gaps on the five non-ground vertices; and
- the orientable six-pentagon translation-surface gluing.

No theorem-state file is changed.

**Disposition:** eliminated the symmetric pentagram H5 signed `K_6` class by combining
the reciprocal signed length balance with two strict summed triangle inequalities.
C-II remains open.
