<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5b12f135a3255353ab503810608783b25e1bc92e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3311_closure_2026-09-23.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "660e4b65218f82e53d6fb665b75b2c32d71748b1163d51f893d9127154488015"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the `(3,3,1,1)` four-support subbranch in the eight-no-root `k=5,D=-1,d_root=1,p=3` state

Date: 2026-09-23

Status: exact finite closure of one of the three remaining `m=4` multiplicity profiles. This does **not** close the `(3,2,2,1)` or `(2,2,2,2)` profiles, the full `p=3` branch, the full `k=5` layer, Target C-II, or Erdos Problem #99.

Inputs:

- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_singleton_basis_reduction_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_tetrahedral_support_compression_2026-09-23.md`;
- `research/target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_three_support_closure_and_certificate_audit_2026-09-23.md`;
- the exact K8 normal form in `research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py`.

## 1. Required relation increment

The preceding reductions force, throughout the remaining `m=4` branch:

- exactly three touched singleton root blocks;
- every other touched root block complete;
- a rank-three coefficient code `P <= Q^8` with
  ```text
  (d1,d2,d3) >= (2,4,5);
  ```
- touched-complete root nullity exactly one.

The last statement follows because the four tetrahedron-boundary dependencies are independent and the singleton-incidence map has rank three, so its kernel supplies one complete-root dependency, while the earlier reduction already bounds the touched-complete nullity by one.

For `D=-1`, `d_root=1`, and `rank(P)=3`, the same accounting used in the `m=3` and `m=5` closures shows that the five-dimensional coefficient nullspace would have to contribute five independent relation directions modulo the full complete-root relation span. Therefore a touched state is impossible as soon as its external relation-rank increment over the touched complete-root span is less than five. Adding untouched complete blocks cannot increase this quotient increment.

## 2. The `(3,3,1,1)` support profile

There are four distinct four-vertex supports. Two supports contribute all three four-cycle orientations and the other two contribute one orientation each. Thus the raw number of eight-cycle sets is

```text
C(35,4) * C(4,2) * 3^2 = 2,827,440.
```

The verifier first reduces the 52,360 four-support sets to 38 `S_7` orbits. For each support-set representative it then quotients the 54 `(3,3,1,1)` orientation choices by that support set's stabilizer. This gives exactly

```text
754
```

`S_7` orbits of eight-cycle sets in this multiplicity profile.

For each orbit representative, every triple of touched singleton blocks is tested. The remaining touched complete blocks are required to have root nullity exactly one. Across the 754 cycle-set representatives this leaves

```text
148,014
```

admissible singleton triples.

Each singleton has three local root-row directions, so there are

```text
148,014 * 3^3 = 3,996,378
```

direction states. Of these,

```text
2,416,118
```

have coefficient rank three, and

```text
192,611
```

also satisfy

```text
(d1,d2,d3) >= (2,4,5).
```

## 3. External-rank census

For every one of those 192,611 generalized-weight-admissible states, the verifier constructs all five external relation rows using an eight-coordinate nullspace basis and computes their rank increment over the touched complete-root span.

The exact census is

```text
external rank increment 0 : 192,611
```

and there are no states of increment 1, 2, 3, 4, or 5.

Hence every admissible `(3,3,1,1)` state has all five external relation directions already contained in the touched complete-root relation span. Since the branch requires increment five, no such state can occur.

> **Theorem.** The `(3,3,1,1)` subbranch of the four-support `m=4` part of the eight-no-root `k=5,D=-1,d_root=1,p=3` branch is empty.

## 4. Exactness of the rank decisions

The root complete-block rows are integral and have maximum squared Euclidean norm

```text
12.
```

The full relation rows encountered in the admissible census have maximum squared Euclidean norm

```text
70.
```

All modular ranks use

```text
P = 2^127 - 1,
```

whose primality is checked by the base verifier's Lucas-Lehmer routine. The verifier checks

```text
P^2 > 70^15.
```

Hadamard's inequality therefore bounds every relevant nonzero minor strictly below `P` in absolute value, so modular rank equals rational rank for every root-rank and external-rank decision used in the closure.

The rank-three coefficient test itself uses exact integer `3 x 3` minors, and the generalized weights are computed directly from the eight coefficient columns.

## 5. Validation status

The committed certificate is

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3311_closure_2026_09_23.py`.

An independent local reconstruction of the repository's exact K8 normal form was executed over the complete `(3,3,1,1)` orbit census and reproduced all counts above, including the rank-increment census `{0: 192611}` and maximum relation-row squared norm `70`. The committed verifier source was syntax-checked before upload. The exact committed file was not executed from a repository checkout in this run, so the local reconstruction and the committed executable certificate are kept distinct.

## 6. Remaining finite target

The `D=-1,k=5,d_root=1,p=3` branch now has only two four-support multiplicity profiles:

```text
(3,2,2,1),
(2,2,2,2).
```

The same completion-independent external-rank-increment test is the next finite target. Closing both profiles would close the entire `p=3` arithmetic branch.

The other open `k=5` arithmetic branches remain

```text
D=-2, (d_root,p)=(0,5),
D=-1, (d_root,p)=(0,6).
```

No theorem-state authority file is changed by this note.
