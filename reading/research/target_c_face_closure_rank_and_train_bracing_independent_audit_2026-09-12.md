> Generated reading edition · [exact source](../../research/target_c_face_closure_rank_and_train_bracing_independent_audit_2026-09-12.md) · source SHA-256 `2ea7a32bf6f36ad0444cc9ea94dd4fc367f084dd32b7764d0a271179f82586bb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "700c2fc1fa4183ad9b3d1de853ef428eaeb72441", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_face_closure_rank_and_train_bracing_independent_audit_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "16c9274dabff6ae93819a495e450b4548c0dcd0e42c51ca2410951b81ee71168"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — independent audit of exceptional-face closure rank and outer-train bracing

**Date:** 2026-09-12  
**Scope:** `research/target_c_exceptional_face_closure_rank_2026-09-12.md` and `research/target_c_outer_train_two_sided_bracing_2026-09-12.md`.  
**Disposition:** PASS at proof-only audited-working scope.  
**Theorem authority:** unchanged; C-II remains open.

## 1. Exceptional-face closure rank

Let `T` be the complete stopped-train count, `R` the bounded strict-rhombus face count, `f` the bounded nonquadrilateral face count, and `C_face` the two-coordinate exceptional-face closure matrix.

The train-rate parametrization is exact: opposite sides of a strict rhombus have equal infinitesimal angular rate, so one scalar is attached to each complete train. Conversely, if all nonquadrilateral bounded-face vector-closure equations vanish, bounded facial cycles generate the real cycle space of the connected plane contact graph, including in the presence of bridges and articulation vertices. The assigned edge derivatives therefore integrate to a contact flex, unique modulo translation.

Hence

```math
\dim\ker R_C=T-\operatorname{rank}C_{\rm face}+2.
```

With `T=e-2R` and Euler `e-v=R+f-1`, rank-nullity gives exactly

```math
\boxed{2f-\operatorname{rank}C_{\rm face}=\dim\ker R_C^T=:\sigma_C.}
```

Canonical mixed rigidity has left nullity `s_Z+1`. Every pure contact self-stress extends by zero diameter coordinates, while the normalized KKT stress has nonzero diameter part. Therefore

```math
\boxed{0\le\sigma_C\le s_Z}
```

and

```math
\boxed{\operatorname{rank}C_{\rm face}\ge 2f-s_Z.}
```

For every defect-face set `S`, row dependencies of the restricted matrix extend by zero to row dependencies of the full matrix. Thus

```math
|N(S)|\ge \operatorname{rank}C_S\ge 2|S|-\sigma_C\ge2|S|-s_Z.
```

The Hall-type expansion claim is valid.

## 2. Outer-to-outer train capacity

Outer-to-outer trains are zero columns of `C_face`; the separately audited no-bounded-return theorem is needed only for the converse zero-column identification. Consequently

```math
L_{OO}\le T-\operatorname{rank}C_{\rm face}\le h.
```

If `f>0`, the coordinate subspace supported only on outer-to-outer trains has trivial intersection with the all-trains rotation line. Mixed rigidity therefore maps this `L_OO`-dimensional non-Euclidean flex space injectively into the `h` diameter first-variation coordinates. KKT stationarity puts the image in the codimension-one hyperplane perpendicular to the positive diameter multiplier vector, so

```math
\boxed{L_{OO}\le h-1.}
```

This dimension argument is valid.

## 3. Two-sided diameter bracing

For one outer-to-outer train, the audited finite train primitive supplies a Jordan shore cut whose contact cut is exactly the train, with all crossing contact vectors parallel to one unit vector `u`. Summing positive KKT equilibrium over one shore gives

```math
A_\tau u=\sum_{h\pitchfork\tau}\beta_h r_h,
\qquad A_\tau>0,
\qquad \beta_h>0.
```

Taking the `Ju` component yields zero weighted transverse sum. If the crossing diameter vectors did not occur with both transverse signs, positivity forces every transverse component to vanish. All crossing diameter segments would then be parallel to `u`.

A finite diameter-`D` set has at most one unordered diameter segment in any projective direction: if `b-a=Du` and `d-c=Du`, the two cross-distance bounds imply

```math
|Du-v|^2+|Du+v|^2=2D^2+2|v|^2\le2D^2,
```

so `v=0`.

Thus the zero-transverse case has exactly one crossing diameter pair, oriented as `Du` by the vector KKT resultant. The exact one-train shear translates one shore by `R_\theta u-u`, preserves every old contact, and changes that crossing diameter to a vector of squared length

```math
D^2-2(D-1)(1-\cos\theta)<D^2
```

for small nonzero `theta`. Same-shore diameter pairs are unchanged; all old strict noncontacts and nondiameter pairs retain their slack for sufficiently small `theta`. Since canonical C65 exposes every actual diameter pair and contact-isolated points cannot be hidden diameter endpoints, the full source either acquires strictly smaller diameter or the same diameter with fewer actual diameter pairs, contradicting the lexicographic normalization.

Therefore every outer-to-outer train is crossed by actual diameter pairs of both transverse signs.

## 4. Scope

- No response-conductance estimate is used.
- Contact-isolated source points are retained in the full-source shear and excluded from the core rigidity matrices.
- No coefficient lower bound beyond positivity of the relative-interior KKT multipliers is used.
- The result is structural only. Exact rank does not provide a quantitative singular-value lower bound, so near-degenerate corridor blocks remain possible.

**Final verdict:** both theorem files are valid at audited-working proof-only scope. They should be integrated as current research dependencies, but they do not by themselves close C-II or justify theorem-state promotion beyond the audited dependency stack.
