> Generated reading edition · [exact source](../../research/target_c_support6_collapsed_ten_crossing_floor_2026-09-19.md) · source SHA-256 `cc4d2886233ea30361a07f80118b3f4e03f116cde99e0569c7ddf3a829915b3b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c0c6081689983f93fb3d82408b60306942be6f66", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_ten_crossing_floor_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "3bd6ad887cdef83c9367dca2ff23f8a29dc6ac9a62a806ec4b70a849537cddc6"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — collapsed support-six blocks consume at least ten strict rhombi

**Date:** 2026-09-19  
**Claim class:** proved candidate; exact finite/global train-topology strengthening  
**Scope:** degree-pure collapsed support-six one-anchor components after maximal two-anchor activation  
**Certificate:** `research/verify_target_c_support6_collapsed_ten_crossing_floor_2026_09_19.cpp`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The earlier exact planarization search excluded every collapsed support-six crossing
set of size at most six. The extended symmetry-reduced search now excludes every
angle-compatible, MI.1-consistent, triangle-free crossing set of sizes seven,
eight, and nine. Its exact totals are:

```text
TOTAL k=7 parity=4909 tri=3965 metric=2544 planar=0
TOTAL k=8 parity=11944 tri=9340 metric=5801 planar=0
TOTAL k=9 parity=27650 tri=19455 metric=10453 planar=0
PASS: no collapsed support-six symmetry orbit admits a planar, angle-compatible MI.1 crossing pattern with 7, 8, or 9 internal crossings.
```

Together with the independently audited `k<=6` certificate, this proves

```math
\boxed{X_K\ge10}
```

for every globally realizable collapsed support-six block `K`, where `X_K` counts
strict-rhombus crossings whose two trains are internal to `K`.

## Exact scope

The search works on all 42 conservative symmetry representatives of the 388 exact
rotation cells. For each affine MI.1 solution it retains only triangle-free
crossing graphs, imposes simultaneous strict crossing windows in the common
projective-angle variables, and uses the forced crossing rotation determined by
the coherent train orientations. It enumerates every order of multiple crossings
along every train and rejects every positive-genus planarization. The tests use
integer difference feasibility, bit arithmetic, and Euler characteristic; no
floating-point decision enters.

The local nonlinear closure equations are not used. Therefore this is a global
necessary condition for any collapsed stopped-train realization, not a claim that
the locally certified closure cells embed globally.

## Resource consequence

Distinct collapsed relation components have disjoint internal train sets, so their
internal crossing rhombi are disjoint. If `c_6` is the number of degree-pure
collapsed support-six components and `R_4` is the total bounded strict-rhombus
count, then

```math
\boxed{R_4\ge10c_6,\qquad c_6\le R_4/10.}
```

Combining this with the audited tangent payment

```math
d_C\ge M_0+2c_6+(c_6-1)_+,
\qquad M_0=(b-f)/2+E_U+p_U,
```

gives the sharpened simultaneous bound

```math
c_6\le\min\left\{\frac{d_C-M_0+1}{3},\frac{R_4}{10}\right\}.
```

Substitution into the existing support accounting yields

```math
\boxed{
\sigma_C\le 2n_0+n_2+\frac{n_1}{7}+\frac{x_U}{7}
 +\frac17\min\left\{\frac{d_C-M_0+1}{3},\frac{R_4}{10}\right\}.
}
```

This is a coupled tangent/rhombus payment, not yet a contradiction with the live
terminal diameter budgets: `R_4` is quadratic-scale in the full-core branch while
`c_6` is only known to be linear-scale. The smallest remaining task is therefore
to connect the ten required internal crossings to the actual endpoint/diameter
train budget or to classify the ten-crossing endpoint types.

**Disposition:** exact ten-crossing floor and resource coupling; theorem-state
authority unchanged; C-II remains open.
