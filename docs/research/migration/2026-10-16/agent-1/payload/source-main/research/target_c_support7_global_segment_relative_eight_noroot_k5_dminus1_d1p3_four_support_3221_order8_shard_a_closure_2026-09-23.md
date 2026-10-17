# Target C: close one nullity-four order-8 `(3,2,2,1)` support class

Date: 2026-09-23

Status: exact finite closure of one touched-nullity-four four-support `S_7` orbit with setwise stabilizer order 8 in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch. This does not close the remaining 26 nullity-four `(3,2,2,1)` support classes, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_nullity_catalog_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_highsym_closure_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order12_closure_2026-09-23.md`;
- the exact K8 coordinate normal form in `research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py`.

## 1. Support orbit

The touched-nullity-four `(3,2,2,1)` census has four support orbits of setwise stabilizer order 8. This certificate closes the orbit represented by

```text
S = {1234,1235,1245,3467}.
```

Its setwise stabilizer has order 8, so its labeled support orbit has size `5040/8 = 630`.

For a fixed support set, the `(3,2,2,1)` profile has 324 cycle choices. Quotienting these by the support stabilizer gives exactly

```text
72 S_7 cycle-set representatives.
```

Thus this certificate covers

```text
630 * 324 = 204120
```

labeled eight-cycle sets.

## 2. Necessary state conditions

The existing `p=3,m=4` reduction forces exactly three singleton touched root blocks. Their three nonzero singleton coefficient rows must have rank three and generalized weights

```text
(d1,d2,d3) >= (2,4,5).
```

Every other touched root block is complete. The complete touched-root complement must have nullity exactly one.

For `D=-1,d_root=1`, the five-dimensional coefficient nullspace would have to contribute external relation-rank increment five over that complete-root span. Therefore any state with external increment less than five is impossible.

## 3. Exact finite census

A standalone reconstruction of the current repository K8 coordinate normal form and the same finite verifier logic was executed on all 72 cycle-set representatives of `S`. Before this new run, the reconstruction was checked against the just-closed order-12 support class and reproduced its repository counts exactly:

```text
cycle-set representatives             34
admissible singleton triples        6732
direction states                  181764
rank-three states                 140986
generalized-weight states           9826
external increment census       {0:9826}
max relation-row norm^2                70
```

The exact census for `S` is

```text
S_7 cycle-set representatives         72
labeled eight-cycle sets          204120
admissible singleton triples       13104
singleton-direction states         353808
coefficient-rank-three states      287381
generalized-weight states           27666
external rank increment census  {0:27666}
max relation-row norm^2                70
```

Every one of the 27666 generalized-weight-admissible states has external relation-rank increment zero. A surviving state requires increment five. Hence no state on `S` survives.

> **Theorem.** No `(3,2,2,1)` state in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4` branch can have support set in the `S_7` orbit of `{1234,1235,1245,3467}`.

This is an exhaustive statement for that support orbit. No sampling or random finite-field rank test is used.

## 4. Exactness of rank decisions

Coefficient rank three is tested by exact integer `3 x 3` minors. The generalized weights are computed directly from the eight coefficient columns. The touched support nullity is checked over `Q` and equals four.

Root and full relation ranks are computed modulo

```text
P = 2^127 - 1.
```

The base verifier supplies the Lucas-Lehmer primality check. The largest squared norm of any relation row in this shard is 70, and the certificate checks

```text
P^2 > 70^15.
```

Hadamard's inequality therefore makes the modular rank decisions identical to the corresponding rational ranks.

The companion repository verifier is

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order8_shard_a_closure_2026_09_23.py`.

It checks that there are exactly four touched-nullity-four support orbits of stabilizer order 8, identifies this support as one of them, and asserts the full census above. Its source was syntax-checked before upload. The exact committed wrapper was not executed from a checked-out repository in this run; the census above was executed by the standalone reconstruction described above.

## 5. Remaining `(3,2,2,1)` target

Before this certificate, exactly 27 touched-nullity-four support classes remained:

```text
1^2, 2^8, 4^11, 6^2, 8^4.
```

This theorem removes one order-8 class. Exactly 26 nullity-four support classes remain:

```text
1^2, 2^8, 4^11, 6^2, 8^3.
```

The next bounded target is another one of the three remaining stabilizer-order-8 classes using the same completion-independent external-rank-increment test.

The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```
