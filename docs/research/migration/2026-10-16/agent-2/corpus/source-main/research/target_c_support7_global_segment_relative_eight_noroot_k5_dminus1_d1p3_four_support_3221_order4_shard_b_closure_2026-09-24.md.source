# Target C: close a second nullity-four order-4 `(3,2,2,1)` support class

Date: 2026-09-24

Status: exact finite closure of one additional touched-nullity-four four-support `S_7` orbit with setwise stabilizer order 4 in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch. This does not close the remaining 19 nullity-four `(3,2,2,1)` support classes, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_nullity_catalog_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order4_shard_a_closure_2026-09-24.md`;
- the exact K8 coordinate normal form in `research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py`.

## 1. Support orbit

Among the touched-nullity-four `(3,2,2,1)` support orbits with setwise stabilizer order 4, this certificate treats

```text
S = {1234,1235,1236,1247}.
```

Its setwise stabilizer has order 4, hence the labeled support orbit has size

```text
5040 / 4 = 1260.
```

For a fixed support set, the `(3,2,2,1)` profile has 324 cycle choices. Quotienting those choices by the support stabilizer gives exactly

```text
90 S_7 cycle-set representatives.
```

Therefore this certificate covers

```text
1260 * 324 = 408240
```

labeled eight-cycle sets.

All 90 representatives touch the same 13 root blocks. The complete touched-root row family has exact rank 9, hence touched nullity four.

## 2. Necessary state conditions

The existing `p=3,m=4` reduction forces exactly three singleton touched root blocks. Their three nonzero singleton coefficient rows must have rank three and generalized weights

```text
(d1,d2,d3) >= (2,4,5).
```

Every other touched root block is complete. The complete touched-root complement must have nullity exactly one.

For `D=-1,d_root=1`, the five-dimensional coefficient nullspace would have to contribute external relation-rank increment five over that complete-root span. Any state with external increment below five is impossible.

## 3. Exact finite census

A standalone reconstruction of the current repository K8 coordinate normal form and verifier logic was executed on all 90 cycle-set representatives of `S`. The exact census is

```text
S_7 cycle-set representatives         90
labeled eight-cycle sets          408240
touched root blocks                   13
admissible singleton triples       15840
singleton-direction states         427680
coefficient-rank-three states      341056
generalized-weight states           31573
external rank increment census  {0:31573}
max relation-row norm^2                70
```

Every one of the 31,573 generalized-weight-admissible states has external relation-rank increment zero. A surviving state requires increment five. Hence no state on `S` survives.

> **Theorem.** No `(3,2,2,1)` state in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4` branch can have support set in the `S_7` orbit of `{1234,1235,1236,1247}`.

This is exhaustive for that support orbit. No random sampling or probabilistic finite-field rank test is used.

As a reconstruction control, the same standalone code was rerun on the already-closed shard-A support `{1234,1235,1236,1245}`. It reproduced the committed census exactly:

```text
90 cycle-set representatives,
13860 admissible singleton triples,
374220 singleton-direction states,
306057 coefficient-rank-three states,
38248 generalized-weight states,
external rank increment census {0:38248},
max relation-row norm^2 70.
```

## 4. Exactness of rank decisions

Coefficient rank three is tested by exact integer `3 x 3` minors. Generalized weights are computed directly from the eight coefficient columns. Touched support nullity is computed by exact rational elimination and equals four.

Root and full relation ranks are computed modulo

```text
P = 2^127 - 1.
```

The Lucas-Lehmer test for `P` was executed in this run. The largest squared norm of any relation row in this shard is 70, and

```text
P^2 > 70^15.
```

Hadamard's inequality therefore certifies that the modular rank decisions equal the rational rank decisions.

The companion repository verifier is

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order4_shard_b_closure_2026_09_24.py`.

It asserts the order-4 support census at the level needed here, selects `S`, asserts its 13 touched root blocks and nullity four, checks all census values above, checks the zero-only increment census, and checks the Hadamard bound. The exact committed wrapper was syntax-checked but was not executed end-to-end from a repository checkout in this run; the finite census was executed by the standalone reconstruction described above.

## 5. Remaining `(3,2,2,1)` target

Before this certificate, exactly 20 touched-nullity-four support classes remained:

```text
1^2, 2^8, 4^10.
```

This theorem removes one order-4 class. Exactly 19 touched-nullity-four support classes remain:

```text
1^2, 2^8, 4^9.
```

The next bounded finite target is another order-4 support orbit with the same completion-independent external-rank-increment test.

The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```
