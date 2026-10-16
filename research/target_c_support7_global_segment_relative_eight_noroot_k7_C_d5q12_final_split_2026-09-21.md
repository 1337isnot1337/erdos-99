<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f94dc82708c16127f11bdd998f0c227f291c0bd4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k7_C_d5q12_final_split_2026-09-21.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "00f6bbdf1eed6496c3b6c5b713658672fe8a1a65eb1a4180cca241f10279c6cc"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: final `C:(5,12,12)` finite closure split

Date opened: 2026-09-21  
Closed: 2026-09-22

Status: **closed.** Both final all-singleton profiles in the current eight-no-root `k=7` finite split are impossible. This file now records the completed split; the detailed intermediate reductions remain available in Git history and in the linked research notes.

This is a finite-layer result. It does **not** promote Target C-II or Erdős Problem #99 to solved. The canonical global state remains governed by `docs/targets/target-c/CURRENT.md` and `docs/state/theorem-state.yaml`.

## Companion profile `C:(4,11,10)`

The profile

```text
C:(d_v,q,s)=(4,11,10)
```

is closed in full.

Its `d_6=3` side is excluded by the exact target-profile reranking recorded in the `d_6=3` closure artifacts. Its only remaining `d_6=4` side is excluded by the exhaustive corrected exact-profile scan recorded in

```text
research/target_c_support7_global_segment_relative_eight_noroot_k7_C_d4q11_d4_exact_profile_2026-09-21.md
```

Therefore `C:(4,11,10)` is impossible.

## Profile `C:(5,12,12)`

The profile

```text
C:(d_v,q,s)=(5,12,12)
```

is also closed in full.

### `d_6=3`

The six-row replacement-functional inequality requires singleton-functional extra rank at least eight. The exact full-cover verifier

```text
research/verify_target_c_support7_global_segment_relative_six_noroot_k5_d3_capacity8_functional_2026_09_21.py
```

finds 324 synchronized `d_6=3` states with singleton capacity at least eight, with maximum singleton-functional extra rank only four. Hence `d_6=3` is impossible.

### `d_6=4`

The exact six-row singleton-functional obstruction excludes deficiency four for this profile. Thus no `d_6=4` shadow can realize `C:(5,12,12)`.

### `d_6=5`

For `d_6=5`, the six-row inequality forces extra rank ten, the entire six-row functional quotient. Deficiency monotonicity then forces every qualifying one-cycle restoration to have

```text
d_7=5,
singleton capacity >= 11.
```

At seven rows the replacement-functional inequality requires extra rank eleven, the entire seven-row quotient.

The exact verifier

```text
research/verify_target_c_support7_global_segment_relative_seven_noroot_k6_C_d5q12_d5_functional_lift_2026_09_22.py
```

was executed over the complete 325,955-representative six-row augmentation cover. The aggregate census is

```text
synchronized_states                 1,751,870
six_full_rank_witnesses               136,450
seven_d5_capacity_ge11_lifts           968,687
retained_six_full_span_lifts             49,249
seven_full_rank_lifts                         0
max_seven_extra_rank                         10
```

All 49,249 qualifying lifts that retain the required six-row rank-ten span remain at seven-row extra rank ten. None reaches the necessary rank eleven.

The full partitioned execution, exact-rank bounds, and macro-range census are recorded in

```text
research/target_c_support7_global_segment_relative_eight_noroot_k7_final_full_cover_closure_2026-09-22.md
```

The global observed exactness bounds are

```text
max functional-row squared norm = 45
max functional width            = 25
max relation-row squared norm   = 24
```

with `P=2^127-1` prime and

```text
P^2 > 45^25,
P^2 > 24^15,
P^2 > 12^15
```

for the complete-block relation ranks. Hadamard therefore certifies the modular ranks over `Q`.

Thus `d_6=5` is impossible, and hence

```text
C:(5,12,12) is impossible.
```

## Consequence for the finite split

The two final profiles are now both excluded:

```text
C:(4,11,10)  impossible
C:(5,12,12)  impossible
```

Therefore the current eight-no-root `k=7` finite split has no surviving profile.

The older full-span multiplicity, pair-retention, exact-profile, and codimension-one audits remain useful independent crosschecks, but none is still a completion bottleneck for this finite split.
