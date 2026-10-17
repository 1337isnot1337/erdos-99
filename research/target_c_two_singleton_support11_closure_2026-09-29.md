<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ce7b79ff78f2be38dba4cea9048376f283a02791", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_two_singleton_support11_closure_2026-09-29.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1824917ea0ca3eb228d1d3fb807b0a2c99feb274539df3bb557332445a2f4341"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: exact exclusion of two-singleton support 11

Date: 2026-09-29

Support 11 in the committed thirteen-support narrowing is

`[0123]^3 [0124] [0134] [0145] [0234] [1234] [2345]`.

This note records a complete orientation-level exclusion for that support in the nine-no-root `k=4, D=-1, d_root=0, p=2` two-selected-singleton profile.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support11_eight_empty_obstruction_2026_09_29.py`

The verifier imports the exact current-main orientation model

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28.py`

with blob `867e8e583f6073c92b1f7afbf2aaf536e2567fa9`.

## Structural lower bound on empty blocks

For every orientation of this support, the touched block family `T` is support-determined and has

`|T| = 16`, `rank H(T) = 10`.

Let `C` be the touched actual-complete blocks, `S` the touched selected-singleton blocks, and `E` the touched actual-empty blocks. Because `d_root=0`, the triangle rows `H(C)` are independent, so `|C|=rank H(C)`. The established four-direction capacity condition gives

`rank H(T) - rank H(C) >= 4`.

Therefore `|C| <= 6`. Since at most two selected singletons lie in `T`,

`|E| = 16 - |C| - |S| >= 16 - 6 - 2 = 8`.

Thus every realizable state contains at least eight touched actual-empty blocks.

## Exact eight-empty obstruction

The triple tetrahedral support has a unique orientation choice and the six multiplicity-one supports have three choices each. Hence there are exactly

`3^6 = 729`

raw orientation assignments.

For each orientation, the verifier examines every `C(16,8)=12,870` eight-block subset, for a total of

`729 * 12,870 = 9,382,230`

subsets.

For an eight-block set `F`, let

`U(F) = sum_{b in F} E_b`,

where `E_b` is the exact rational local empty-block constraint space in the nine external coordinates. If all eight blocks were actual-empty, then every `E_b` would lie in the actual aggregate constraint space `W`, which has dimension four.

The verifier first computes row rank modulo 2. Reduction modulo 2 cannot increase rank, so `rank_F2 U(F) >= 5` implies `rank_Q U(F) >= 5` and rules out that subset immediately.

The exact executed census is:

- orientations: `729`;
- eight-block subsets: `9,382,230`;
- subsets with rank at least five modulo 2: `9,380,367`;
- subsets with rank four modulo 2: `1,863`;
- all `1,863` exceptional subsets have exact rational rank four;
- all `1,863` exact rank-four spaces fail the committed necessary generalized-weight filter `parity_profile_ok`.

For an exceptional subset, if its eight blocks were actual-empty then its rank-four span would be contained in the rank-four aggregate space `W`, hence would equal `W`. Since every exceptional span violates a necessary generalized-weight condition, none can be the aggregate space of an actual state.

Therefore no orientation of support 11 is realizable.

## Execution provenance

The exact verifier source executed for this certificate has Git blob

`c48ef5c95ebf4a86f6305c561ccf5a279b18609c`.

The exact imported helper source executed with it has Git blob

`867e8e583f6073c92b1f7afbf2aaf536e2567fa9`.

Before execution, the locally reconstructed helper was checked with `git hash-object` and matched that current-main blob exactly. The verifier terminated with

`PASS: support11 has no realizable orientation`.

## Consequence

This closes support 11 only. On authoritative main before this contribution, exact exclusions are committed for supports 1, 2, 3, 4, 5, 10, and 12. Separate pushed branches contain exact exclusions for supports 6 through 9. If those branch results are integrated together with this certificate, support 13 is the only remaining support orbit in the committed two-singleton narrowing.

This does not close the full two-singleton profile, the full `D=-1,p=2` branch, or Erdos Problem #99.
