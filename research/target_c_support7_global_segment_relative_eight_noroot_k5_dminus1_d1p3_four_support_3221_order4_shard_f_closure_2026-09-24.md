<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "49b68341c3a9182d914f5069094846b5f3894f15", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order4_shard_f_closure_2026-09-24.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c239a7747306d18073adb342b91b62e2a29b90cc711ae32440a7f3cccdbfeb93"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close a sixth nullity-four order-4 `(3,2,2,1)` support class

Date: 2026-09-24

Status: exact finite closure of one additional touched-nullity-four four-support `S_7` orbit with setwise stabilizer order 4 in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch. This does not close the remaining 15 nullity-four `(3,2,2,1)` support classes, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_nullity_catalog_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order4_shard_e_closure_2026-09-24.md`;
- the exact K8 coordinate normal form in `research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py`.

## 1. Support orbit

This certificate treats

```text
S = {1234,1235,1246,3456}.
```

Its setwise stabilizer has order 4, so its labeled support orbit has size `5040/4=1260`. A fixed support set has 324 `(3,2,2,1)` cycle choices. Quotienting by the support stabilizer gives exactly 96 `S_7` cycle-set representatives, covering

```text
1260 * 324 = 408240
```

labeled eight-cycle sets.

Every representative touches the same 14 root blocks. Their complete touched-root row family has exact rank 10 and hence nullity 4.

## 2. Necessary state conditions

The established `p=3,m=4` reduction forces exactly three singleton touched root blocks. Their three nonzero singleton coefficient rows must have rank three and generalized weights

```text
(d1,d2,d3) >= (2,4,5).
```

Every other touched root block is complete. Since the full touched-root nullity is four, deleting three singleton rows leaves nullity at least one; the branch condition `d_root=1` forces the admissible touched-complete complement to have nullity exactly one.

For `D=-1,d_root=1`, the five-dimensional coefficient nullspace would have to contribute external relation-rank increment five over that complete-root span. Any state with increment below five is impossible.

## 3. Exact finite census

An independent reconstruction of the repository K8 coordinate normal form and verifier logic was executed on all 96 cycle-set representatives of `S`. It produced:

```text
S_7 cycle-set representatives         96
labeled eight-cycle sets          408240
touched root blocks                   14
admissible singleton triples       19968
singleton-direction states         539136
coefficient-rank-three states      425987
generalized-weight states           29994
external rank increment census  {0:29994}
max relation-row norm^2                70
```

Every one of the 29,994 generalized-weight-admissible states has external relation-rank increment zero. A surviving state requires increment five. Hence no state on `S` survives.

> **Theorem.** No `(3,2,2,1)` state in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4` branch can have support set in the `S_7` orbit of `{1234,1235,1246,3456}`.

This is exhaustive for that support orbit; no sampling is used.

As a reconstruction control, the same standalone code was run on the already-closed shard-E support `{1234,1235,1245,1367}`. It reached the complete terminal census before the execution wrapper timed out and reproduced every committed value exactly: 126 cycle-set representatives, 22,932 admissible singleton triples, 619,164 direction states, 503,072 rank-three states, 48,260 generalized-weight states, increment census `{0:48260}`, and maximum squared relation-row norm 70.

## 4. Exactness of rank decisions

Coefficient rank three is tested by exact integer `3 x 3` minors. Generalized weights are computed directly from the eight coefficient columns. Touched support nullity is computed by exact rational elimination.

Root and full relation ranks are computed modulo

```text
P = 2^127 - 1.
```

The Lucas-Lehmer test for `P` was executed in this run. The largest squared norm of any relation row in the shard is 70, and

```text
P^2 > 70^15.
```

Hadamard's inequality therefore certifies that the modular rank decisions equal the rational rank decisions.

The companion repository verifier is

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order4_shard_f_closure_2026_09_24.py`.

It checks the support orbit, touched nullity, exact census, zero-only increment census, and Hadamard bound. It precomputes the support-level admissible singleton triples once because that root-nullity filter is independent of the cycle representative. The exact committed wrapper was syntax-checked but was not executed end-to-end from a repository checkout in this run; the finite census was executed by the standalone reconstruction described above.

## 5. Remaining `(3,2,2,1)` target

Before this certificate, exactly 16 touched-nullity-four support classes remained:

```text
1^2, 2^8, 4^6.
```

This theorem removes one order-4 class. Exactly 15 remain:

```text
1^2, 2^8, 4^5.
```

The next unclosed order-4 representative is

```text
{1234,1235,1267,3456},
```

with 93 `S_7` cycle-set representatives and 15 touched root blocks. It is the next bounded target for the same completion-independent external-rank-increment obstruction.

The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

No theorem-state authority file is changed by this note.
