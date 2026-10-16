<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9e5a5a5c4ece3970643cca87732e8701a0503284", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_2222_high_symmetry_closure_2026-09-23.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "bc81f1372933660a00c9b12efbbcc399cd2c5d3f8de94d7e6e01d9f0a9bcf50f"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close a high-symmetry shard of the `(2,2,2,2)` four-support branch

Date: 2026-09-23

Status: exact finite closure of seven support-set `S_7` orbits inside the remaining `(2,2,2,2)` multiplicity profile of the eight-no-root `k=5,D=-1,d_root=1,p=3` branch. This does **not** close the full `(2,2,2,2)` profile, the `(3,2,2,1)` profile, the full `p=3` branch, the full `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_tetrahedral_support_compression_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_support_closure_and_certificate_audit_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3311_closure_2026-09-23.md`;
- the exact K8 normal form inherited by the corresponding verifier chain.

## 1. Necessary external-rank condition

The existing `m=4` reduction forces exactly three singleton root blocks, every other touched root block complete, coefficient rank three with

```text
(d1,d2,d3) >= (2,4,5),
```

and touched-complete root nullity exactly one.

For `D=-1,d_root=1`, the five-dimensional coefficient nullspace must contribute five independent external relation directions modulo the full complete-root relation span. Consequently a touched state is impossible whenever its external rank increment over the touched complete-root span is less than five. Adding untouched complete blocks cannot increase that quotient increment.

## 2. Bounded symmetry shard

The remaining `(2,2,2,2)` profile uses four distinct tetrahedral supports, with exactly two of the three no-root four-cycle orientations chosen on each support.

This run closes every support-set `S_7` orbit whose setwise stabilizer in `S_7` has order at least 16. There are exactly seven such support-set orbits. Their stabilizer orders are

```text
16, 16, 24, 24, 36, 48, 144.
```

The last class is the common-triangle geometry represented by

```text
1234, 1235, 1236, 1237.
```

For a support-set orbit with stabilizer order `h`, there are `5040/h` labeled support sets and `3^4=81` orientation choices. The seven support classes therefore cover exactly

```text
107,730
```

raw `(2,2,2,2)` eight-cycle sets.

Quotienting the 81 orientation choices in each support class by its stabilizer leaves exactly

```text
56
```

`S_7` cycle-set orbit representatives.

## 3. Exact finite census

For each of those 56 cycle-set representatives, the verifier enumerates every triple of touched singleton blocks and keeps only those for which the remaining touched complete root rows have nullity exactly one. This leaves

```text
10,262
```

singleton triples.

There are three local singleton directions at each singleton block, giving

```text
277,074
```

direction states. All 277,074 have singleton coefficient rank three. Of these,

```text
19,513
```

satisfy

```text
(d1,d2,d3) >= (2,4,5).
```

For every one of those 19,513 generalized-weight-admissible states, the exact external relation-rank increment over the touched complete-root span is

```text
0.
```

The full increment census is therefore

```text
external rank increment 0 : 19,513.
```

The required increment is five. Hence every state in these seven high-symmetry support-set orbits is impossible.

> **Theorem.** In the eight-no-root `k=5,D=-1,d_root=1,p=3` branch, the `(2,2,2,2)` subbranch has no state whose four-support set has setwise `S_7` stabilizer of order at least 16.

The previously committed common-triangle certificate is the stabilizer-144 subcase of this theorem.

## 4. Exactness

The coefficient-rank test uses exact integer `3 x 3` minors and the generalized weights are computed directly from the eight coefficient columns.

The relation rows are integral. Across the complete high-symmetry census the maximum squared Euclidean norm of any relation row is

```text
70.
```

The verifier uses the Mersenne prime

```text
P = 2^127 - 1
```

and checks

```text
P^2 > 70^15.
```

By Hadamard's inequality, every relevant nonzero minor has absolute value below `P`, so the modular rank decisions equal the rational rank decisions.

## 5. Validation status

The committed broad certificate is

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_2222_high_symmetry_closure_2026_09_23.py`.

A standalone local reconstruction of the same exact K8 normal form and the same orbit/census logic was executed for this shard. It produced:

```text
support-set orbits: 7
raw cycle sets covered: 107730
S7 cycle-set orbits: 56
admissible singleton triples: 10262
direction states: 277074
rank-three states: 277074
generalized-weight states: 19513
external rank increment census: {0: 19513}
max relation-row squared norm: 70
```

The committed verifier source was syntax-checked before upload. The exact committed wrapper itself was not executed from a repository checkout in this run, so the local reconstruction and committed executable certificate remain explicitly distinct.

## 6. Remaining finite target

The `D=-1,k=5,d_root=1,p=3` branch still has:

```text
(3,2,2,1),
```

and the unclosed support-set orbits of

```text
(2,2,2,2).
```

The next bounded target is another symmetry or support-geometry shard of those remaining four-support states, using the same completion-independent external-rank-increment test.

The other unresolved `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

No theorem-state authority file is changed by this note.
