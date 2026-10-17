> Generated reading edition · [exact source](../../research/target_c_two_singleton_support9_closure_2026-09-29.md) · source SHA-256 `3bac6a3f4a75d32bb9eae5d4d68f62cc7de6d78c0bb4710431e6e3044017ee27`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "09e77611128507a5bca6144a483e60bcd9d0267f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_two_singleton_support9_closure_2026-09-29.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7d39093dee6780a9fe13d3c60d299e05ee9436ce8a472f133e18fcfe9e305136"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: exact exclusion of two-singleton support 9

Date: 2026-09-29

Support 9 in the committed thirteen-support narrowing is

`[0123]^3 [0124] [0134] [0145] [0234] [0246] [1234]`.

This note records a complete orientation-level exclusion for that support in the nine-no-root `k=4, D=-1, d_root=0, p=2` two-selected-singleton profile.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support9_eight_empty_obstruction_2026_09_29.py`

## Structural lower bound on empty blocks

For every orientation of this support, the touched block family `T` is support-determined and has

`|T| = 16`, `rank H(T) = 10`.

Let `C` be the touched actual-complete blocks, `S` the touched selected-singleton blocks, and `E` the touched actual-empty blocks. Because `d_root=0`, the triangle rows `H(C)` are independent, so `|C|=rank H(C)`. The established four-direction capacity condition gives

`rank H(T) - rank H(C) >= 4`.

Therefore `|C| <= 6`. Since at most two selected singletons lie in `T`,

`|E| = 16 - |C| - |S| >= 16 - 6 - 2 = 8`.

Thus every realizable state contains at least eight touched actual-empty blocks.

## Exact eight-empty obstruction

There are six multiplicity-one tetrahedral supports after the triple support, hence exactly `3^6 = 729` raw orientation assignments. For each orientation, the verifier examines all `C(16,8)=12870` eight-block subsets, for a total of

`729 * 12870 = 9,382,230`

subsets.

For an eight-block set `F`, let

`U(F) = sum_{b in F} E_b`,

where `E_b` is the exact rational local empty-block constraint space in the nine external coordinates.

If `rank_Q U(F) >= 5`, then `F` cannot be contained in the actual aggregate constraint space `W`, because `dim W=4`.

The verifier first computes rank modulo 2. Reduction modulo 2 cannot increase rank, so `rank_F2 U(F) >= 5` implies `rank_Q U(F) >= 5`. The exact census is:

- `9,380,367` eight-block subsets have rank at least five already modulo 2;
- `1,863` subsets have rank four modulo 2.

For each of the 1,863 exceptional subsets, the verifier recomputes the rowspace exactly over `Q`. Every one has exact rank four.

If such a subset were eight actual-empty blocks, its exact four-dimensional span would equal the actual rank-four aggregate constraint space `W`. Every one of these 1,863 spaces fails the committed necessary generalized-weight filter `parity_profile_ok(W)`. Hence none can be the aggregate space of an actual state.

Therefore no orientation of support 9 is realizable.

## Execution provenance

The exact verifier source was executed locally and produced the fail-closed census above. Its Git blob is

`7e95d8c681489529b52fe2aef3de9250c7c8647d`.

The imported coordinate/rank helper on authoritative `main` is

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28.py`

with blob `867e8e583f6073c92b1f7afbf2aaf536e2567fa9`. The local execution used an exact transcription of the helper routines needed by this verifier. As a check on that transcription, it independently reproduced the committed support-5 census

`729, 4,691,115, 4,691,007, 108, 108, 108`

before the support-9 run.

## Consequence

Relative to authoritative `main` at `fcf3d44de552e3af8d68e98174ec05e879b09138`, this certificate additionally removes support 9. The unresolved support orbits on this branch are 6, 7, 8, 10, 11, and 13.

This closes support 9 only. It does not close the full two-singleton profile, the full `D=-1,p=2` branch, or Erdos Problem #99.
