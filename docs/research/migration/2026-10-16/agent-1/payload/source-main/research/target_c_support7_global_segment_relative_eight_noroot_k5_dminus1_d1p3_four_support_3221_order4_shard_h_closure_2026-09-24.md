# Target C: close an eighth nullity-four order-4 `(3,2,2,1)` support class

Date: 2026-09-24

Status: exact finite closure of one additional touched-nullity-four four-support `S_7` orbit with setwise stabilizer order 4 in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1)` branch. This does not close the remaining 13 nullity-four `(3,2,2,1)` support classes, the full `p=3` branch, the `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_nullity_catalog_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order4_shard_g_closure_2026-09-24.md`;
- the exact K8 coordinate normal form in `research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py`.

## 1. Support orbit

This certificate treats

```text
S = {1234,1235,1267,3467}.
```

Its setwise stabilizer has order 4, so its labeled support orbit has size `5040/4=1260`. A fixed support set has 324 `(3,2,2,1)` cycle choices. Quotienting by the support stabilizer gives exactly 114 `S_7` cycle-set representatives, covering

```text
1260 * 324 = 408240
```

labeled eight-cycle sets.

Every representative touches the same 15 root blocks. Their complete touched-root row family has exact rank 11 and hence nullity 4.

## 2. Necessary state conditions

The established `p=3,m=4` reduction forces exactly three singleton touched root blocks. Their three nonzero singleton coefficient rows must have rank three and generalized weights

```text
(d1,d2,d3) >= (2,4,5).
```

Every other touched root block is complete. Since the full touched-root nullity is four, deleting three singleton rows leaves nullity at least one; the branch condition `d_root=1` forces the admissible touched-complete complement to have nullity exactly one.

For `D=-1,d_root=1`, the five-dimensional coefficient nullspace would have to contribute external relation-rank increment five over that complete-root span. Any state with increment below five is impossible.

## 3. Exact finite census

A standalone reconstruction of the repository K8 coordinate normal form and verifier logic was executed over all 114 cycle-set representatives of `S`, split into three disjoint bounded shards:

```text
representatives [0,50):
  admissible singleton triples       11600
  singleton-direction states        313200
  coefficient-rank-three states     239256
  generalized-weight states          11784
  external increment census       {0:11784}
  max relation-row norm^2               36

representatives [50,100):
  admissible singleton triples       11600
  singleton-direction states        313200
  coefficient-rank-three states     241416
  generalized-weight states          11736
  external increment census       {0:11736}
  max relation-row norm^2               36

representatives [100,114):
  admissible singleton triples        3248
  singleton-direction states         87696
  coefficient-rank-three states      69024
  generalized-weight states           3840
  external increment census        {0:3840}
  max relation-row norm^2               36
```

Summing the disjoint shards gives the exact orbit census

```text
S_7 cycle-set representatives        114
labeled eight-cycle sets          408240
touched root blocks                   15
admissible singleton triples       26448
singleton-direction states         714096
coefficient-rank-three states      549696
generalized-weight states           27360
external rank increment census  {0:27360}
max relation-row norm^2                36
```

Every one of the 27,360 generalized-weight-admissible states has external relation-rank increment zero. A surviving state requires increment five. Hence no state on `S` survives.

> **Theorem.** No `(3,2,2,1)` state in the eight-no-root `k=5,D=-1,d_root=1,p=3,m=4` branch can have support set in the `S_7` orbit of `{1234,1235,1267,3467}`.

This is exhaustive for that support orbit; no sampling is used.

As an implementation control, the same standalone reconstruction was run on the already-closed shard-G support `{1234,1235,1267,3456}` in two disjoint representative ranges. Their totals reproduce the committed shard-G census exactly: 93 cycle-set representatives, 21,576 admissible singleton triples, 582,552 direction states, 447,756 rank-three states, 22,068 generalized-weight states, increment census `{0:22068}`, and maximum squared relation-row norm 36.

## 4. Exactness of rank decisions

Coefficient rank three is tested by exact integer `3 x 3` minors. Generalized weights are computed directly from the eight coefficient columns. Touched support nullity is computed by exact rational elimination.

Root and full relation ranks are computed modulo

```text
P = 2^127 - 1.
```

The Lucas-Lehmer test for `P` was executed in this run and passed. The largest squared norm of any relation row in the shard is 36, and

```text
P^2 > 36^15.
```

Hadamard's inequality therefore certifies that the modular rank decisions equal the rational rank decisions.

The companion repository verifier is

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order4_shard_h_closure_2026_09_24.py`.

It checks the support orbit, touched nullity, the exact census, zero-only increment census, and Hadamard bound in the same three representative shards. The exact committed wrapper was syntax-checked but was not executed end-to-end from a repository checkout in this run; the finite census was executed by the standalone reconstruction described above.

## 5. Remaining `(3,2,2,1)` target

Before this certificate, exactly 14 touched-nullity-four support classes remained:

```text
1^2, 2^8, 4^4.
```

This theorem removes one order-4 class. Exactly 13 remain:

```text
1^2, 2^8, 4^3.
```

The next unclosed order-4 representative is

```text
{1234,1235,1456,4567},
```

with 14 touched root blocks. It is the next bounded target for the same completion-independent external-rank-increment obstruction. The other two remaining order-4 representatives are `{1234,1235,1467,2567}` and `{1234,1256,1357,2467}`.

The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

No theorem-state authority file is changed by this note.