# Target C: five-no-root rank-density audit, k=5 branch

Date: 2026-09-20

Status: exact finite result for one branch of the global four-cycle metric-basis subproblem. This does not reduce the current 3,874-state generic-H6 endpoint and does not close C-II.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_five_noroot_k5_2026_09_20.py`

## Statement

Use the relative four-cycle notation from the preceding audits. Let `M` be the 85-dimensional span of the 210 simple `K8` four-cycle rows modulo the 56 automatic side-triangle rows, let `T` be the 15-dimensional ground-root star space, let `Q=M/T`, and put

`delta(A) = r_M(A) - r_Q(A)`.

For a family with exactly five no-root four-cycles, strip untouched root-0 quotient blocks as in the previous density audits. Write

- `c` for the number of complete touched root-0 blocks,
- `p` for the number of selected root-0 rows in incomplete touched blocks, and
- `k` for the extra quotient-kernel dimension supplied by the five no-root rows.

Then

`|A| = 5 + 3c + p`

and

`delta(A) <= c + k`.

Therefore a violation of

`3 delta(A) <= |A|`

can occur only in

- `k=2, p=0`,
- `k=3, p<=3`,
- `k=4, p<=6`, or
- `k=5, p<=9`.

The new verifier closes the last branch:

> Every five-no-root family in the `k=5` branch satisfies `3 delta(A) <= |A|`.

Equivalently, a hypothetical rank-density counterexample with exactly five no-root four-cycles must have `k<=4`.

This does **not** yet prove the factor-three density inequality for all five-no-root families. The `k=2,3,4` branches remain.

## Why k=5 is special

When `k=5`, the global external coefficient-constraint space is zero. Hence every touched root-0 quotient block must impose zero local constraint by itself.

For a touched two-dimensional quotient block:

- the empty state is impossible;
- every two-row pair spans the block and is allowed, at incomplete-row cost `2`;
- the complete local triple is allowed; and
- a singleton is allowed exactly when all five external local components lie on that singleton direction.

The three singleton directions are `(1,0)`, `(0,1)`, and `(1,-1)`, so at most one singleton state is compatible in a touched block.

Fix the five no-root rows and let `F` be the family obtained by completing every touched root-0 block. Any admissible `A` in this `k=5` branch is a row-subfamily of `F`. Hence

`delta(A) <= delta(F)`.

If `m` is the number of touched blocks, `s` the number with a compatible singleton, and `q` the number of incomplete blocks, then the minimum possible incomplete-row cost is

`p_min(q) = min(q,s) + 2 max(0,q-s)`.

Writing `r_full=delta(F)`, every state therefore satisfies

`|A| - 3 delta(A) >= 5 + 3(m-q) + p_min(q) - 3 r_full`.

Only `p<=9` can violate the crude `k=5` bound.

## Exact S7 orbit census

There are

`C(105,5) = 96,560,646`

unordered five-subsets of the 105 no-root four-cycles.

The verifier first classifies all four-subsets into the previously known 1,186 `S7` orbits, then performs stabilizer-orbit augmentation by one additional no-root cycle. A minimal-parent rule leaves 20,475 candidates. Full `S7` canonicalization removes 24 duplicates and leaves exactly

`20,451`

five-subset orbits.

The orbit-size census is

```text
126:      1
210:      1
252:      2
315:      6
420:      4
504:      2
630:     32
840:      2
1008:     1
1260:   283
2520:  2069
5040: 18048
```

The weighted orbit sizes sum exactly to `96,560,646`, so the orbit enumeration is complete.

## All-complete pruning

The all-complete upper bound on `delta(A)` gives the following minimum-defect census over the 20,451 orbit representatives:

```text
best lower bound   orbit count
-2                     16
-1                   2618
 1                    576
 2                  13770
 4                    247
 5                   3089
 7                     36
 8                     96
10                      2
13                      1
```

Thus 17,817 orbit representatives are eliminated without local-state enumeration. Exactly 2,634 orbit representatives remain potentially dangerous under this bound.

Their classes are

```text
(m,s,r_full)   best   dangerous (q,p)   orbit count
(11,7,8)        -1       (8,9)              27
(12,8,9)        -2       (8,8)              16
(13,9,9)        -1       (9,9)             226
(14,9,10)       -1       (9,9)             673
(14,10,10)      -1       (9,9)             687
(15,10,11)      -1       (9,9)             270
(15,11,11)      -1       (9,9)             561
(16,12,12)      -1       (9,9)             174
```

For `(q,p)=(8,8)` or `(9,9)`, every incomplete block must be a compatible singleton. For `(8,9)`, exactly seven incomplete blocks are compatible singletons and the eighth is a two-row pair. Therefore the entire residual branch contains only

`79,944`

local states.

## Exact residual ranks

Every residual state was reranked. The defect census is

```text
|A| - 3 delta(A)   states
8                   60,637
10                      16
11                  19,291
```

The minimum exact defect is therefore

`8`.

The rank census is

```text
(m,r_full,delta,q,p)   states
(11,8,5,8,9)              324
(12,9,5,8,8)               16
(13,9,5,9,9)               28
(13,9,6,9,9)              198
(14,10,6,9,9)            1140
(14,10,7,9,9)            6403
(15,11,7,9,9)            7683
(15,11,8,9,9)           25872
(16,12,8,9,9)           10440
(16,12,9,9,9)           27840
```

No residual state has negative defect.

## Exactness of the rank decisions

The verifier uses integer relation rows in the established 15-dimensional `T` coordinate system. Across the all-complete and residual scans, every relation row has squared Euclidean norm at most

`24`.

Ranks are computed modulo

`P = 2^127 - 1`.

The verifier independently runs the Lucas-Lehmer test for `P` and checks

`P^2 > 24^15`.

If rational rank exceeded modular rank, some nonzero integer minor of size at most 15 would be divisible by `P`. Hadamard gives squared absolute value at most `24^15`, so that nonzero minor would have absolute value strictly below `P`, a contradiction. Hence every modular rank used here equals the rank over `Q`.

NumPy is used only to batch exact integer `S7` permutation/combinadic calculations in the orbit canonicalization. It is not used for numerical rank or any proof decision.

## Remaining bottleneck

For the five-no-root density layer, the unresolved regimes are now exactly

- `k=2, p=0`,
- `k=3, p<=3`, and
- `k=4, p<=6`.

The `k=2,p=0` branch is the smallest next target: incomplete blocks are forced to be empty, so a canonical minimal-completion argument analogous to the four-no-root audit should reduce it to rank-3 external constraint spaces.

For C-II itself, the explicit generic-H6 endpoint remains

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

The state-specific forced-segment-order scan remains the computation most directly capable of removing those cells. Surviving cells then require quantitative sine-law metric compatibility. The theorem-state authority files are unchanged.
