> Generated reading edition · [exact source](../../research/target_c_support7_reciprocal_collinearity_2026-09-19.md) · source SHA-256 `dc0da77eda2b04d46a4bdd7d4b6bb41c79f07965430208ae15183276af466cf6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cf24b28fd12b0c6a142dbea10ce3edec287085f2", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_reciprocal_collinearity_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "88bed6d9baf3a751588a3c619f57ae40ea43d1519930a53284119bf678852d97"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — exact collinearity classification at the support-seven reciprocal endpoint

**Date:** 2026-09-19  
**Claim class:** exact degeneracy classification inside the audited degree-pure support-seven endpoint  
**Depends on:** `target_c_support7_endpoint_reduction_2026-09-19.md`; bounded contact-pentagon no-parallel-side theorem  
**Certificate:** `research/verify_target_c_support7_reciprocal_collinearity_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The audited support-seven endpoint theorem gives pairwise distinct non-ground reciprocal values `y_1,...,y_7` and relation graph

```math
R=K_7-L,
\qquad
L=C_7\ \text{or}\ C_3\sqcup C_4.
```

The remaining nonconvex `H6/H7` branches can contain collinear reciprocal points. This note classifies exactly which non-ground collinearities are even combinatorially possible.

---

## 1. A collinear non-ground set induces relation degree at most one

Let `S` be a set of at least three pairwise distinct non-ground reciprocal points lying on one line. If some `i in S` had two relation neighbors `j,k in S`, then

```math
y_i-y_j\parallel y_i-y_k.
```

The two corresponding nonzero relation sides of the physical pentagon `F_i` would be projectively parallel. The bounded-pentagon no-parallel-side theorem forbids this. Hence

```math
\boxed{\Delta(R[S])\le1.}
\tag{1.1}
```

Equivalently, every vertex of `L[S]` is missing all but at most one of the other vertices in `S`.

Because `L` has degree two, (1.1) immediately implies `|S|<=4`.

---

## 2. Complete classification by missing-graph type

The exact possibilities are:

### Missing graph `L=C_7`

A collinear triple can only be three consecutive vertices of the missing 7-cycle. There are exactly seven such triples. No four non-ground reciprocal points can be collinear.

Thus

```math
\boxed{
L=C_7:\quad
|S|\ge3\text{ collinear}\Longrightarrow
|S|=3\text{ and }L[S]\cong P_3.
}
\tag{2.1}
```

### Missing graph `L=C_3\sqcup C_4`

A collinear triple can only be either

- all three vertices of the missing `C_3`; or
- three consecutive vertices of the missing `C_4`.

There are exactly five such triples: one triangle and four length-two paths in `C_4`.

A collinear four-set, if it occurs, must be exactly the four vertices of the missing `C_4`. No other four-set passes (1.1), and no five-set can.

Hence

```math
\boxed{
L=C_3\sqcup C_4:\quad
S\text{ collinear},\ |S|\ge3
\Longrightarrow
L[S]\in\{C_3,P_3,C_4\},
}
\tag{2.2}
```

with `C_4` occurring only when `S` is the entire missing four-cycle.

These are necessary conditions only. The note does not assert that every listed degeneracy is geometrically realizable.

---

## 3. Collinearity through the reciprocal ground is even more rigid

Put `y_0=0`. Suppose a set `S` of non-ground reciprocal points lies on one line through `y_0`.

If `ij` were a relation edge with `i,j in S`, then the reciprocal difference `y_i-y_j` would be projectively parallel to `y_i-y_0=y_i`. At the physical face `F_i`, the relation side `ij` would therefore be projectively parallel to its outside anchor side. This is forbidden.

Thus

```math
\boxed{R[S]\text{ has no edges}.}
\tag{3.1}
```

Equivalently `L[S]` is complete. Since `L` is 2-regular,

```math
\boxed{|S|\le3.}
\tag{3.2}
```

More precisely:

- two non-ground points can be collinear with the ground only if their pair is an edge of `L`;
- three non-ground points can be collinear with the ground only in the `C_3\sqcup C_4` graph type, and then they must be exactly the vertices of the missing `C_3`;
- four non-ground points can never lie on one line through the ground.

Thus a radial four-point reciprocal degeneracy `0,y_i,y_j,y_k` is possible only on the missing triangle, and any radial line contains at most three non-ground reciprocal points.

---

## 4. Use in the remaining endpoint

The fully convex `H8` branch does not need these restrictions because it has no collinear triples. They are aimed at the remaining nonconvex branches:

- `H6`: ground on the hull and two non-ground points interior;
- `H7`: either ground on the hull with one non-ground point interior, or ground interior with all seven non-ground points on the hull.

Any order-type enumeration for those branches can now delete all degeneracy walls except the finite list in (2.1), (2.2), and (3.1)--(3.2).

No support-seven exclusion or `1/8` support coefficient is claimed.

**Disposition:** all possible support-seven reciprocal collinear subsets are confined to consecutive missing-cycle triples, the missing `C4`, and the missing `C3`; a line through the ground can contain at most three non-ground points and a radial triple exists only on the missing `C3`. C-II remains open.
