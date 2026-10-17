> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order6_shard_a_closure_2026-09-24.md) · source SHA-256 `58cd7bbb47a5d60c785305279366974a910c47643ae93906337fa3cef948590a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "813f35a556713a34974a0199facececeed658013", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order6_shard_a_closure_2026-09-24.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "046f7b62f682b283a03cef91640d5faf39dc8dbdf4843d40ba4ffda121a5120d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close one nullity-four order-6 `(3,2,2,1)` support class

Date: 2026-09-24

Status: exact finite closure of one touched-nullity-four four-support `S_7` orbit with setwise stabilizer order 6 in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch. This does not close the remaining 22 nullity-four `(3,2,2,1)` support classes, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_nullity_catalog_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_highsym_closure_2026-09-23.md`;
- the four order-8 shard closures;
- the exact K8 coordinate normal form in `research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py`.

## 1. Support orbit

After closure of the order-8 layer, the touched-nullity-four `(3,2,2,1)` census has exactly two support orbits of setwise stabilizer order 6. This shard closes

```text
S = {1234,1235,1246,1347}.
```

Its setwise stabilizer has order 6, hence the labeled support orbit has size

```text
5040 / 6 = 840.
```

For a fixed support set, the `(3,2,2,1)` profile has 324 cycle choices. Quotienting those choices by the support stabilizer gives exactly

```text
57 S_7 cycle-set representatives.
```

Therefore this certificate covers

```text
840 * 324 = 272160
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

A standalone reconstruction of the current repository K8 coordinate normal form and verifier logic was executed on all 57 cycle-set representatives of `S`. The exact census is

```text
S_7 cycle-set representatives         57
labeled eight-cycle sets          272160
admissible singleton triples       10488
singleton-direction states         283176
coefficient-rank-three states      230825
generalized-weight states           23293
external rank increment census  {0:23293}
max relation-row norm^2                70
```

Every one of the 23,293 generalized-weight-admissible states has external relation-rank increment zero. A surviving state requires increment five. Hence no state on `S` survives.

> **Theorem.** No `(3,2,2,1)` state in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4` branch can have support set in the `S_7` orbit of `{1234,1235,1246,1347}`.

This is exhaustive for that support orbit. No random sampling or probabilistic finite-field rank test is used.

As a reconstruction control, the same standalone code was rerun on the already-closed final order-8 support `{1234,1235,1467,4567}` and reproduced its committed census exactly:

```text
60 cycle-set representatives,
12600 admissible singleton triples,
340200 singleton-direction states,
268272 coefficient-rank-three states,
18072 generalized-weight states,
external rank increment census {0:18072},
max relation-row norm^2 50.
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

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order6_shard_a_closure_2026_09_24.py`.

It asserts the two order-6 nullity-four support classes, the selected support orbit, all census values above, the zero-only increment census, and the Hadamard bound. The exact committed wrapper was not executed end-to-end from a repository checkout in this run; the finite census was executed by the standalone reconstruction described above.

## 5. Remaining `(3,2,2,1)` target

Before this certificate, exactly 23 touched-nullity-four support classes remained:

```text
1^2, 2^8, 4^11, 6^2.
```

This theorem removes one order-6 class. Exactly 22 touched-nullity-four support classes remain:

```text
1^2, 2^8, 4^11, 6^1.
```

The final order-6 representative is

```text
{1234,1256,1357,2367}.
```

It is the next bounded target for the same completion-independent external-rank-increment test.

The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```
