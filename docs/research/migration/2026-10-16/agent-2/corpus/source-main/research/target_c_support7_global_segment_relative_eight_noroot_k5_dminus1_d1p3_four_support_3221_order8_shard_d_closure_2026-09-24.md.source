# Target C: close the final nullity-four order-8 `(3,2,2,1)` support class

Date: 2026-09-24

Status: exact finite closure of the final touched-nullity-four four-support `S_7` orbit with setwise stabilizer order 8 in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch. This completes the order-8 layer of that profile. It does not close the remaining 23 nullity-four `(3,2,2,1)` support classes, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_nullity_catalog_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_highsym_closure_2026-09-23.md`;
- the three prior order-8 shard closures;
- the exact K8 coordinate normal form in `research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py`.

## 1. Support orbit

The touched-nullity-four `(3,2,2,1)` census has exactly four support orbits of setwise stabilizer order 8. Three were already closed by the prior order-8 shards. The last one is

```text
S = {1234,1235,1467,4567}.
```

Its setwise stabilizer has order 8, hence the labeled support orbit has size

```text
5040 / 8 = 630.
```

For a fixed support set, the `(3,2,2,1)` profile has 324 cycle choices. Quotienting those 324 choices by the support stabilizer gives exactly

```text
60 S_7 cycle-set representatives.
```

Therefore this certificate covers

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

For `D=-1,d_root=1`, the five-dimensional coefficient nullspace would have to contribute external relation-rank increment five over that complete-root span. Any state with external increment below five is impossible.

## 3. Exact finite census

A standalone reconstruction of the current repository K8 coordinate normal form and verifier logic was executed on all 60 cycle-set representatives of `S`. The exact census is

```text
S_7 cycle-set representatives         60
labeled eight-cycle sets          204120
admissible singleton triples       12600
singleton-direction states         340200
coefficient-rank-three states      268272
generalized-weight states           18072
external rank increment census  {0:18072}
max relation-row norm^2                50
```

Every one of the 18,072 generalized-weight-admissible states has external relation-rank increment zero. A surviving state requires increment five. Hence no state on `S` survives.

> **Theorem.** No `(3,2,2,1)` state in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4` branch can have support set in the `S_7` orbit of `{1234,1235,1467,4567}`.

This is exhaustive for that support orbit. No random sampling or probabilistic finite-field rank test is used.

As a reconstruction control, the same standalone code was rerun on the already-closed shard-C support `{1234,1235,1267,4567}` and reproduced the committed census exactly:

```text
63 cycle-set representatives,
14616 admissible singleton triples,
394632 singleton-direction states,
303144 coefficient-rank-three states,
14760 generalized-weight states,
external rank increment census {0:14760},
max relation-row norm^2 36.
```

## 4. Exactness of rank decisions

Coefficient rank three is tested by exact integer `3 x 3` minors. Generalized weights are computed directly from the eight coefficient columns. Touched support nullity is computed by exact rational elimination and equals four.

Root and full relation ranks are computed modulo

```text
P = 2^127 - 1.
```

The Lucas-Lehmer test for `P` was executed separately in this run. The largest squared norm of any relation row in this shard is 50, and

```text
P^2 > 50^15.
```

Hadamard's inequality therefore certifies that the modular rank decisions equal the rational rank decisions.

The companion repository verifier is

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order8_shard_d_closure_2026_09_24.py`.

It asserts the support orbit, all census values above, the zero-only increment census, and the Hadamard bound. Its source was syntax-checked before upload. The exact committed wrapper was not executed end-to-end from a repository checkout in this run; the finite census was executed by the standalone reconstruction described above.

## 5. Remaining `(3,2,2,1)` target

Before this certificate, exactly 24 touched-nullity-four support classes remained:

```text
1^2, 2^8, 4^11, 6^2, 8^1.
```

This theorem removes the last order-8 class. Exactly 23 touched-nullity-four support classes remain:

```text
1^2, 2^8, 4^11, 6^2.
```

The two order-6 representatives are

```text
{1234,1235,1246,1347},
{1234,1256,1357,2367}.
```

They are the next bounded targets for the same completion-independent external-rank-increment test.

The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```
