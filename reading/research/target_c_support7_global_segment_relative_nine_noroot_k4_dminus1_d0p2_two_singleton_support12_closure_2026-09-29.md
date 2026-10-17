> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support12_closure_2026-09-29.md) · source SHA-256 `5906527215696b120734d90be5dddf9f67267366b592baccdd46c93c556413a1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "897c4a86924eead2406b9728f4b97242a0d44681", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support12_closure_2026-09-29.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b21ad020c674b73a3c259d2288431634f71dbf627cd6481d5edffa031de1933b"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: support12 orientation closure

Date: 2026-09-29

Support: `[0123]^3 [0124] [0134] [0145] [0234] [1234] [2346]`.

This note closes this explicit support orbit in the nine-no-root `k=4, D=-1, d_root=0, p=2` two-selected-singleton profile. It does not close the full two-singleton profile.

For any fixed orientation, the rank-four search is one-sided: it allows arbitrary touched empty-block spaces and then at most two arbitrary nonzero singleton constraint lines. Every realizable aggregate coefficient space is therefore included. Every realizable space must satisfy the existing generalized-weight condition `(d1,d2,d3,d4,d5) >= (2,4,5,7,8)`.

The persisted shard verifier was executed separately for shards 5 through 9 and reproduced these fail-closed censuses:

- `[135,162)`: 46,271 rank-four spaces, 0 generalized-weight passes.
- `[162,189)`: 46,976 rank-four spaces, 0 passes.
- `[189,216)`: 44,325 rank-four spaces, 0 passes.
- `[216,243)`: 43,918 rank-four spaces, 0 passes.
- `[243,270)`: 44,403 rank-four spaces, 0 passes.

Thus every orientation in `[135,270)` is impossible.

The support automorphism group and 102-class Burnside reduction are already proved on main. The persisted closure verifier reconstructs the action and checks the orbit-size census `1^1, 2^2, 4^17, 8^82`. Saturating the existing `[0,81)` exclusion together with `[135,270)` covers 99 of the 102 symmetry classes, i.e. 720 of 729 raw assignments. The remaining classes are exactly
`(660,661,687,688)`, `(662,689,714,715)`, and `(716)`.

Exact search of representatives 660, 662, and 716 gives respectively 1,121, 1,198, and 1,394 relaxed rank-four spaces. Representatives 660 and 662 have no generalized-weight-admissible space. Representative 716 has exactly eight.

For each of those eight spaces at 716, let `V(W)={b in T:E_b<=W}` and `C0=T\V(W)`. The verifier checks uniformly `|T|=16`, `|V(W)|=2`, `|C0|=14`, and `rank H(C0)=10`; hence `H(C0)` has row nullity four. Every actual empty block lies in `V(W)`. Deleting the at most two selected singleton blocks from `C0` leaves a subset `C*` of the actual complete family and can reduce row nullity by at most two. Thus `H(C*)` still has nullity at least two, so the actual complete family is dependent, contradicting `d_root=0`.

Therefore all 102 orientation classes for this support are impossible.

Executed source blob hashes before persistence:
- midinterval shard verifier: `101a6e9373bab2c6351e1ee02f915733e66ba281`;
- closure verifier: `4bdf82b9d347950e2b1879b315267a901aa01ec6`.
