<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "90a9df52b6a1af5a8867d9c86f78799c79e715d5", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_six_noroot_plan_2026-09-20.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "db19a0d34d8313765304d8508247a375c63abe8f91dcbcadde926ecf0654b942"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: six-no-root rank-density layer

Date: 2026-09-20

Status: exact orbit count and exact dangerous-region reduction for the next global four-cycle metric-basis layer. This does not prove the six-no-root density inequality, does not reduce the 3,874-state generic-H6 endpoint, and does not close C-II.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_six_noroot_orbits_2026_09_20.py`

## Current position

The preceding exact audits now prove

`3 delta(A) <= |A|`

for every four-cycle family containing at most five cycles that avoid root `0`, where

`delta(A) = r_M(A) - r_Q(A)`.

Therefore every hypothetical sufficient 44-cycle family must contain at least six no-root four-cycles. The next unproved density layer is exactly `t=6`.

There are 105 no-root simple four-cycles. Hence the raw six-subset count is

`C(105,6) = 1,609,344,100`.

A blind six-subset scan is unnecessary because the natural `S_7` action is large enough to reduce this sharply.

## Exact S7 orbit count

Burnside's lemma gives exactly

`325,911`

orbits of unordered six-subsets of the 105 no-root four-cycles.

The companion verifier constructs the 105 cycles directly as edge sets on vertices `1,...,7`. For each of the 5,040 elements of `S_7`, it computes the induced permutation on those 105 cycles. If the induced permutation has object-cycle lengths `L_1,...,L_m`, the number of invariant six-subsets is the coefficient of `x^6` in

`product_i (1+x^(L_i))`.

Everything is integral. The Burnside numerator is

`1,642,591,440`,

and

`1,642,591,440 / 5,040 = 325,911`.

As an internal cross-check, the same calculation for five-subsets gives

`103,073,040 / 5,040 = 20,451`,

exactly reproducing the independently established five-no-root orbit count used by the committed `t=5` verifiers.

The six-subset fixed-point census by vertex-permutation cycle type is

```text
cycle type             class size    fixed six-subsets
(1,1,1,1,1,1,1)                1       1,609,344,100
(2,1,1,1,1,1)                 21             926,980
(2,2,1,1,1)                  105              64,036
(2,2,2,1)                    105              64,036
(3,1,1,1,1)                   70                 595
(3,2,1,1)                    420                  49
(3,2,2)                      210                  19
(3,3,1)                      280                 595
(4,1,1,1)                    210                 100
(4,2,1)                      630                 100
(4,3)                        420                   1
(5,1,1)                      504                   0
(5,2)                        504                   0
(6,1)                        840                  19
(7)                          720                   0
```

The class sizes sum to 5,040 and their fixed-count weighted sum is the Burnside numerator above.

## Dangerous `(k,p)` regimes for t=6

Retain the established local-block notation. After removing untouched blocks, write

`|A| = t + 3c + p`

and bound

`delta(A) <= c + k`,

where `k` is the extra quotient-kernel dimension supplied by the no-root rows and `p` is the number of selected root-0 rows in incomplete touched blocks.

For `t=6`,

`|A| - 3 delta(A) >= 6 + p - 3k`.

A negative defect is therefore possible only when

`p < 3k - 6`.

Since `0 <= k <= 6`, all `k<=2` cases are automatic. The only six-no-root regimes requiring any finite audit are

- `k=3, p<=2`;
- `k=4, p<=5`;
- `k=5, p<=8`;
- `k=6, p<=11`.

This is the exact analogue of the reduction that made the five-no-root layer tractable. No local-state enumeration outside these four regimes can produce a factor-three counterexample.

## Consequence for the next computation

The six-no-root orbit layer is about sixteen times larger than the five-no-root layer: `325,911` versus `20,451` `S_7` orbits. Repeating the complete five-no-root local-state enumeration without another reduction would be wasteful.

The smallest branch is `k=3,p<=2`. Its coefficient-constraint space has rank `6-3=3`, so its external coefficient nullspace has dimension three. The next useful attack should construct the rank-three analogue of the canonical-completion/containment theorem used for the five-no-root `k=3` and `k=4` branches, and enumerate only candidate rank-three spaces that can actually be generated by at most two incomplete selected rows. If a containment theorem holds, most or all of this branch should collapse without full local-state enumeration.

The `k=6` branch is also structurally simple because its coefficient-constraint space is zero; the all-complete domination method from the five-no-root `k=5` verifier should be tested there after the smaller `k=3` branch is profiled.

## Direct C-II bottleneck

The metric-basis result is auxiliary. The direct generic-H6 endpoint is still

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

The exact forced-segment-order filter remains the direct state-removal computation. Existing pilot scans show many numerical segment-order candidates but very few exact forced edges, so a full exact scan should use lazy cycle-driven branch tests rather than solve all 168 opposite halfspaces in every cell. Any surviving cells then require quantitative sine-law metric compatibility.

No theorem-state authority file is changed by this result.
