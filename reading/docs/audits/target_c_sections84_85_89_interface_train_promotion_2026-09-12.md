> Generated reading edition · [exact source](../../../docs/audits/target_c_sections84_85_89_interface_train_promotion_2026-09-12.md) · source SHA-256 `cacdec801fba58e796413285e4706917ff953b9ab48ea9d50516aba266667c8f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B560772C07D8","canonical":true,"claim_ids":["C-HARMONIC-TRAIN-BUDGET","C-TRAIN-INTERFACE-CURRENCY","C-TYPEII-INTERFACE-COLLAPSE"],"claim_statuses":{"C-HARMONIC-TRAIN-BUDGET":"canonical","C-TRAIN-INTERFACE-CURRENCY":"canonical","C-TYPEII-INTERFACE-COLLAPSE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C §§84–85 and §89 promotion audit

**Date:** 2026-09-12

This note records an independent hostile audit of the Type-II interface-collapse
module (§84), the exact train-boundary currency module (§85), and the local harmonic
train-budget module (§89).

## Section 84 — Type-II interface collapse

In the canonical full-core near-disk branch, `F/D` and `K/D` converge (after the same
translation) to the radius-`1/2` disk. The `K` conclusion follows directly from
`F subset K`, `diam(K)<=D`, and the antipodal-point test: a limit point outside the
disk would be more than unit distance from its antipodal disk point.

For an exterior cap, `area(cap)=o(D^2)`. A normalized cap subsequence therefore has a
zero-area convex limit. It cannot contain a point of the disk interior, because compact
subsets of the disk interior lie in the normalized force hull for all sufficiently
large indices. A nondegenerate segment cannot lie on a strictly convex circle, so the
cap diameter and perimeter are `o(D)`.

An internal chamber with perimeter `lambda D+o(D)` has area `o(D^2)`, hence a
zero-area convex limit. Cauchy’s width formula gives perimeter continuity for the
degenerate limit, so it is a segment of length `lambda/2`. A linear-degree exceptional
face is a convex unit-edge polygon with two boundary arcs whose lengths both equal
`(lambda/2+o(1))D`; an outer pocket has a sublinear force-hull closing side and its
complementary contact path splits into two arcs of the same asymptotic length. The
total chamber-perimeter bound gives only finitely many such corridors at every fixed
linear scale. No near-geodesic corridor is declared impossible.

## Section 85 — exact train-boundary currency

For the complete strict-rhombus complex, Theorem 10.6 gives
`B_4>=4 sqrt(R_4)`. Every rhombus boundary occurrence faces either the outer contact
walk or a bounded nonquadrilateral face, so
`B_4<=b+4f+Q`. With the canonical identity `b+Q=2(q-k)`, this gives
`q-k+2f>=2 sqrt(R_4)`. Combining with
`m=R_4+f+q-k+1` yields the exact finite deficit
`m-R_4>=sqrt(R_4)+1`.

The canonical exceptional-face and outer-pocket Oler inequalities give

`A_ch-a_0 Z_ch >= c_0[(b-P_F)+2f+Q]`.

Writing `J=(b-P_F)+4f+Q` and using `Q>=f` gives
`(b-P_F)+2f+Q >= (3/5)J`. Since
`J>=B_4-P_F`, the promoted finite inequality is

`A_ch-a_0 Z_ch >= (3c_0/5)(4 sqrt(R_4)-P_F)`.

In the canonical Type-II branch, `R_4/D^2 -> pi/(2 sqrt(3))` and
`P_F/D -> pi`, so the right side has the strict first-order lower bound

`(3 sqrt(3)/20)(4 sqrt(pi/(2 sqrt(3)))-pi) D+o(D)`,

whose coefficient is positive. This is an Oler-weighted interface surplus, not a
claim that the inactive region has linear Euclidean area.

## Section 89 — exact harmonic-cell train budget

For one unloaded harmonic carrier with `a` loaded attachments, pinned surplus `s`,
loaded-loaded contact count `c`, and boundary count `c_partial`, the exact Section-82
face identity and outer-walk lower bound give

`P_R <= 12a-30-10s-10c+4c_partial`

for the physical boundary of its full strict-rhombus complex, hence
`T_R <= 6a-15-5s-5c+2c_partial` because every train has two boundary ends. The
weaker `T_R<=6a-15-5s-3c` follows from `c_partial<=c`.

Each train’s transverse span is at most the diameter `d` of the same convex
attachment cell. Every rhombus contributes `sin(theta)` to two trains, equal to its
area, so `2 A_4 <= T_R d`. Thus

`2 A_4 <= d(6a-15-5s-5c+2c_partial)`.

On the canonical Type-II carrier supplied by `C-HARMONIC-WRAPPING`, this yields
`a=Omega(D)`, `T_R=Omega(D)`, and the exact simultaneous local area/attachment
constraints without spending the ambient diameter `D`.

## Scope and non-conclusions

All three results retain the full source and distinguish physical contacts from KKT
weights. They do not rule out doubled near-geodesic corridors, prove simultaneous
pair-closing, force a triangle, or produce a strict sub-`D` competitor. The surviving
Type-II obligation is still a boundary/interface aggregation or source-preserving
deformation theorem; the Type-I obligation remains the global coupling of a
macroscopic inactive container to diameter minimality.

## Dependency-to-obligation chain

The promoted claims have the following exact handoff into the live C-II proof:

```text
C-FULLCORE-NEAR-DISK + C-INACTIVE-CHAMBER + C-PUNCTURED-PHASE
    -> C-TYPEII-INTERFACE-COLLAPSE
    -> finitely many doubled near-geodesic corridors at each linear scale

C-RHOMBUS-POP + C-LOADED-HULL + C-INACTIVE-CHAMBER + C-FULLCORE-NEAR-DISK
    -> C-TRAIN-INTERFACE-CURRENCY
    -> A_ch-a0 Z_ch >= (3c0/5)(4 sqrt(R_4)-P_F), with positive Type-II first-order coefficient

C-HARMONIC-CARRIER-QUAD + C-HARMONIC-WRAPPING
    -> C-HARMONIC-TRAIN-BUDGET
    -> 2A_4 <= T_R diam(P) and T_R <= 6a-15-5s-5c+2c_partial
```

These arrows produce exact canonical quantities for the next interface-aggregation
or source-preserving-deformation argument. None of the three terminal quantities is
itself an exact unit-triangle certificate or a strict sub-`D` competitor; promoting
them therefore advances the frontier without changing the open C-II status.

## Disposition

The exact statements above are valid and should be promoted as
`C-TYPEII-INTERFACE-COLLAPSE`, `C-TRAIN-INTERFACE-CURRENCY`, and
`C-HARMONIC-TRAIN-BUDGET`, with dependencies restricted to the canonical modules and
standard convex/train geometry listed in the state transaction.
