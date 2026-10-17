# Target C: five-no-root k=3, p=2 c=14 completion audit

Date: 2026-09-20

Status: exact finite supplement to the five-no-root `k=3,p=2` rank-density proof. It repairs an omitted justification in the original verifier/note. It does not reduce the current 3,874-state generic-H6 endpoint and does not close C-II.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_five_noroot_k3_p2_c14_2026_09_20.py`

## The omitted slice

The original `p=2` verifier skips canonical `p=0` states with

`c >= 14`

complete root-0 quotient blocks. The skip is automatic for `c>=15`: after at most two complete-block replacements, at least 13 complete blocks remain, so the selected-row count is at least

`5 + 3*13 + 2 = 46`,

while `delta<=dim(T)=15`, giving defect at least one.

For `c=14`, a one-pair `p=2` state replaces at most one complete block and is safe by the same argument. The only potentially dangerous form is two singleton replacements at two complete blocks. That can leave

`c'=12`

complete blocks and only

`5 + 3*12 + 2 = 43`

selected rows. The ambient `delta<=15` bound is not enough there.

Thus the `c=14` two-singleton slice requires a separate rank argument.

## Exact census

Across the exact 20,451 `S7` representatives of the 96,560,646 five-subsets of no-root four-cycles, there are exactly

`10,250`

canonical rank-two-constraint states with `c=14`.

The exact rank census of their 14 complete-block `T` rows is

```text
rank  states
10     1,224
11     9,026
```

There is no rank-12, rank-13, or rank-14 state.

Therefore every 12-block subset obtained by deleting two complete blocks has rank at most 11 and is dependent.

For a two-singleton `p=2` state, the coefficient nullspace has dimension three, so

`delta <= rank_T(C') + 3 <= 11 + 3 = 14`.

Hence

`|A|-3 delta(A) >= 43 - 42 = 1`.

This closes the only slice omitted by the original `p=2` implementation. The previously stated conclusion for five-no-root `k=3,p=2` is therefore valid.

## Exactness

The complete-block rows are integer vectors in the established 15-dimensional `T` coordinate model. Their squared Euclidean norm is at most 12. Ranks are computed modulo

`P = 2^127 - 1`.

The imported exact-rank layer verifies this Mersenne prime with Lucas-Lehmer, and the verifier checks

`P^2 > 12^15`.

Hadamard's determinant bound therefore implies that the modular ranks equal the rational ranks used above.

## Remaining five-no-root bottleneck

With the `p=2` proof now complete, the five-no-root density problem remains only in

- `k=3,p=3`, and
- `k=4,p<=6`.

For C-II itself, the explicit generic-H6 endpoint remains

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

The state-specific forced-segment-order scan remains the direct endpoint computation. No theorem-state authority file is changed by this supplement.
