# Target C: five-no-root k=3, p=2 rank-density audit

Date: 2026-09-20

Status: exact finite result for one subcase of the five-no-root four-cycle density problem. This does not reduce the current 3,874-state generic-H6 endpoint and does not close C-II.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_five_noroot_k3_p2_2026_09_20.py`

## Statement

Keep the relative four-cycle notation and put

`delta(A) = r_M(A) - r_Q(A)`.

The new verifier closes

> `k=3,p=2`.

Together with the preceding `p=0` and `p=1` audits, the five-no-root `k=3` branch is now reduced to only

`p=3`.

The unresolved five-no-root density regimes are

- `k=3,p=3`, and
- `k=4,p<=6`.

## Why only independent complete sets matter

Fix the rank-two coefficient-constraint space `P`. Start with its canonical `p=0` state, and let `C` be the complete-block set. Write

`c=|C|`, `r=rank_T(C)`, and `d=c-r`.

A canonical `p=2` state has either

- one two-row incomplete block, or
- two singleton incomplete blocks.

Let `C'` be the complete-block set left after those replacements.

The coefficient nullspace has dimension three, so

`delta(A) <= rank_T(C') + 3`.

If `C'` is dependent, then

`rank_T(C') <= |C'|-1`

and therefore

`|A|-3 delta(A) >= 5 + 3|C'| + 2 - 3(|C'|+2) = 1`.

So a counterexample requires `C'` to be independent.

Since at most two complete blocks can be replaced, this is impossible unless the canonical `p=0` state has `d<=2`.

The `p=0` census contains exactly

- 86 states with `d=1`, and
- 13,349 states with `d=2`.

No other `p=0` state can contribute to the `p=2` search.

## Incomplete-state types

### One two-row incomplete block

A two-row local state imposes zero coefficient constraint. Replacing one complete block can make `C'` independent only for `d=1`.

The exact scan finds

`346`

one-block deletions for which `C'` is independent.

There are three two-row local masks, so these give

`1,038`

canonical states requiring full relation rank.

### Two singleton incomplete blocks

If either singleton lies in a block that is empty in the canonical `p=0` state, at most one complete block is removed. For `d>=2` that cannot produce an independent `C'`; for `d=1` the `p=1` audit already proved that every admissible one-block singleton deletion leaves the complete set dependent.

Thus only two singleton replacements at two complete blocks need to be scanned.

The exact scan finds no such independent state from `d=1`.

For `d=2`, it finds

`3,534`

admissible two-singleton states with independent `C'`.

## Exact residual ranks

The two state types therefore leave

`1,038 + 3,534 = 4,572`

canonical states for full exact relation rank.

Every one has defect

`|A|-3 delta(A) = 7`.

The exact `( |C'|, rank_T(C'), delta )` census is

```text
(3,3,3)       840
(5,5,5)        61
(6,6,6)       354
(7,7,7)       465
(8,8,8)     1,828
(9,9,9)     1,024
```

Thus in every residual state the three external coefficient-nullspace relation rows add no rank beyond the independent complete-block relation space.

No negative-defect state exists.

## Exactness

Coefficient-space construction and containment tests use exact rational row spaces.

Complete-block and full relation ranks are computed modulo

`P = 2^127 - 1`.

The imported rank layer runs Lucas-Lehmer for this prime. The maximum squared Euclidean norm of any relation row in the residual scan is

`44`,

and the verifier checks

`P^2 > 44^15`.

Hadamard's determinant bound therefore proves that every modular rank used in this audit equals the rank over `Q`.

## Remaining bottleneck

For `k=3`, only `p=3` remains. The same argument reduces it to canonical states whose post-replacement complete-block set is independent. Since at most three complete blocks can be removed, only canonical `p=0` states with `d<=3` can contribute.

A `p=3` state has either

- one two-row incomplete block plus one singleton, or
- three singleton incomplete blocks.

This is a finite deletion-minimal search rather than the full local-state product. The large class is the `d=3` case, where three complete singleton replacements are required.

The separate `k=4,p<=6` branch remains after that.

For C-II itself, the explicit generic-H6 endpoint remains

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

The state-specific forced-segment-order scan remains the most direct cell-removal computation. Surviving cells then require quantitative sine-law metric compatibility. The theorem-state authority files are unchanged.
