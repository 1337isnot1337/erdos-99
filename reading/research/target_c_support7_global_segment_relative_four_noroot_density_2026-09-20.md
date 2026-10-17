> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_four_noroot_density_2026-09-20.md) · source SHA-256 `d9b4043a0712348ed768108a1776502362b7d66573ad8f27e0919e5da6179a63`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "1209893afff03d872fb84313ff439a9ad1e14ca6", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_four_noroot_density_2026-09-20.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1e38978e34a81aa44046b2c4f68822d9b2ac4ee2e8ddc43f9251e7e2015c0239"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: rank-density barrier through four no-root four-cycles

Date: 2026-09-20

Status: exact finite result for the global four-cycle metric-basis subproblem. This does not reduce the current 3,874-state generic-H6 endpoint and does not close C-II.

The new companion verifier is

`research/verify_target_c_support7_global_segment_relative_four_noroot_k4_2026_09_20.py`.

Together with the previously committed `t=4,k=2` and `t=4,k=3` verifiers, it closes the remaining four-no-root branch of the factor-three rank-density audit.

## Statement

Use the relative four-cycle notation from the preceding audits. Let `M` be the 85-dimensional span of the 210 simple `K8` four-cycle rows modulo the 56 automatic side-triangle rows, let `T` be the 15-dimensional ground-root star space, let `Q=M/T`, and put

`delta(A) = r_M(A) - r_Q(A)`.

The earlier audits prove

`3 delta(A) <= |A|`

for every family with at most three no-root four-cycles. For four no-root cycles, the crude defect reduction leaves only

- `k=2, p<=1`,
- `k=3, p<=4`, and
- `k=4, p<=7`,

where `k` is the extra quotient-kernel dimension supplied by the four no-root rows and `p` counts selected root-0 rows in incomplete touched quotient blocks.

The first two branches are already closed by

- `research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py`, and
- `research/verify_target_c_support7_global_segment_relative_four_noroot_k3_p01_2026_09_20.py` together with `research/verify_target_c_support7_global_segment_relative_four_noroot_k3_full_2026_09_20.py`.

The new verifier closes `k=4,p<=7`. Therefore:

> For every four-cycle family containing at most four cycles that avoid root `0`,
>
> `3 delta(A) <= |A|`.

A sufficient family has `delta(A)=15`. Hence a sufficient family with at most four no-root cycles has at least 45 rows. Consequently:

> Every hypothetical sufficient 44-cycle family contains at least five no-root four-cycles.

Since the committed 45-cycle family `F` contains only root-0 cycles, those five no-root cycles are outsiders relative to `F`. Combined with the previously certified seven-exchange barrier, any hypothetical sufficient 44-cycle replacement still requires at least eight outsiders, now with at least five of them no-root.

This is not yet a proof that 45 four-cycle identities are globally minimal. Families with five or more no-root cycles remain untreated by this density result.

## The all-complete domination lemma for `k=4`

Fix four no-root rows and let their touched root-0 quotient blocks be `B`. Let `A` be any `k=4` local state on those blocks. Form `F_A` by keeping the same four no-root rows and replacing the root-0 selection in every touched block by the complete local triple.

Then `A` is a row-subfamily of `F_A`. Every `Q`-relation among the rows of `A` is therefore a `Q`-relation among the rows of `F_A` after padding zero coefficients on the added rows. The `T`-image of that relation is unchanged. Thus

`delta(A) <= delta(F_A)`.

This gives a state-independent exact rank upper bound once the all-complete state for a no-root orbit has been ranked.

For `k=4`, the global external constraint space is zero. Hence every touched block must itself impose zero constraint on the four external coefficients. In a touched block:

- the empty state is impossible;
- every two-row pair spans the local two-dimensional quotient block and is allowed, with incomplete-row cost `2`;
- the complete triple is allowed and contributes one complete block; and
- a singleton is allowed only when every external local component lies on that singleton direction.

The three singleton directions `(1,0)`, `(0,1)`, `(1,-1)` are pairwise distinct. Because the block is touched, at most one singleton can be compatible.

Let

- `m` be the number of touched blocks,
- `s` be the number of blocks with a compatible singleton,
- `q` be the number of incomplete touched blocks, and
- `r_full = delta(F_A)`.

The least possible incomplete-row cost for a fixed `q` is exactly

`p_min(q) = min(q,s) + 2 max(0,q-s)`.

With `c=m-q`, every `k=4` state therefore satisfies

`|A| - 3 delta(A) >= 4 + 3(m-q) + p_min(q) - 3 r_full`.

Only `p<=7` needs consideration.

## Exact orbit reduction

The 4,780,230 unordered sets of four no-root cycles split into the same 1,186 exact `S_7` orbits used by the preceding four-no-root audits.

The exact all-complete rank census `(m,r_full) -> orbit count` is

```text
(7,5):      3
(8,6):      7
(9,6):     10
(10,6):     6
(10,7):    28
(11,8):    80
(12,8):    80
(12,9):    38
(13,8):    10
(13,9):   224
(14,9):    15
(14,10):  388
(15,10):   24
(15,11):  219
(16,12):   54
```

After minimizing the all-complete lower bound over every possible `q` with `p_min(q)<=7`, the best-defect census is

```text
best lower bound   orbit count
-1                    101
 1                     39
 2                    981
 4                      8
 5                     50
 7                      7
```

Thus 1,085 of the 1,186 orbit representatives are eliminated immediately without enumerating any local states.

The 101 unresolved orbit representatives are exactly

```text
(m,s,r_full)=(11,7,8): 63 orbits
(m,s,r_full)=(12,8,9): 38 orbits
```

and in both classes the only lower-bound-negative point is

`q=7, p=7`.

Therefore every unresolved state has exactly seven incomplete blocks, every one of them a compatible singleton. There are only

`63*C(7,7) + 38*C(8,7) = 367`

such states.

## Exact rank result on the 367 residual states

All 367 residual states were reranked using the integer relation matrices from the established exact coordinate model. The result is

```text
(m,r_full,delta)   states
(11,8,5)              63
(12,9,6)             304
```

Every residual state has exact defect

`|A|-3 delta(A) = 8`.

So the lower-bound value `-1` was not close to an actual counterexample; exact `T`-rank loses three additional dimensions in every residual state.

The verifier returned

```text
PASS: four-no-root k=4,p<=7 rank-density branch
four_no_root_subsets 4780230
S7_orbits 1186
coarse_defect_census {-1: 101, 1: 39, 2: 981, 4: 8, 5: 50, 7: 7}
dangerous_class_census {(11, 7, 8, -1, ((7, 7),)): 63, (12, 8, 9, -1, ((7, 7),)): 38}
dangerous_states_exactified 367
exact_rank_census {(11, 8, 5): 63, (12, 9, 6): 304}
exact_defect_census {8: 367}
min_exact_defect 8
max_relation_row_norm_squared 12
hadamard_exact_rank_bound True
```

The rank decisions are exact over `Q`. The shared verifier uses the prime `P=2^127-1`; the new scan tracks squared Euclidean norm at most `12` for every integer relation row and verifies

`P^2 > 12^15`.

Hence no nonzero minor relevant to these at-most-15-dimensional relation matrices can vanish modulo `P`, so modular rank equals rational rank.

An independent local reconstruction also reranked all 1,186 all-complete matrices and all 367 residual matrices with exact rational elimination and obtained the same ranks.

## Remaining bottleneck

For the metric-basis route, the next density layer is five no-root cycles. The new result means a hypothetical 44-cycle sufficient family must enter that layer; no family with four or fewer no-root cycles can beat 45.

For C-II itself, the more direct bottleneck is still the frozen 3,874 generic-H6 endpoint. The exact forced-segment-order scan remains the state-specific computation most directly capable of removing those cells. Surviving cells then require quantitative sine-law metric compatibility. The theorem-state authority files are unchanged.
