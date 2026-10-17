> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_support12_shard1_nullity_2026-09-28.md) · source SHA-256 `c5a5538be73800df05d7c72a1ff4bfa9c821251b64a5ab16d0fe8ee7639a724f`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e336fccb9931b34fdfe98660e9b0d63ae1030c7f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_support12_shard1_nullity_2026-09-28.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0df400b90a5c15577215587e6f5ea1f13a3abb90c0570baccd08b3311aea37bb"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Support12 shard [27,54) nullity obstruction

For the explicit support `[0123]^3 [0124] [0134] [0145] [0234] [1234] [2346]`, exact enumeration of orientation indices `[27,54)` gives 46,750 relaxed rank-four aggregate spaces. Exactly 32 satisfy the required nine-coordinate generalized-weight profile.

For every one of those 32 spaces `W`, let `V(W)` be the touched blocks whose local empty space is contained in `W`, and let `C0=T\V(W)`. Exact rational triangle-row rank gives `|C0|=14` and `rank H(C0)=10`, hence row nullity four.

Every actual empty block lies in `V(W)`. Removing the at most two selected singleton blocks from `C0` lowers row nullity by at most two, so the resulting subset of the actual complete family still has nullity at least two. Therefore the actual complete family is dependent, contradicting `d_root=0`.

Thus all 27 orientations in `[27,54)` are impossible. Together with the committed `[0,27)` and `[54,81)` certificates, the interval `[0,81)` is excluded.

Executed census: 27 orientations; 46,750 rank-four spaces; 32 weight-admissible spaces, occurring only at orientation indices 27, 41, and 52 with multiplicities 10, 12, and 10. All 32 have virtual-complete size/rank `(14,10)`.

The exact executed verifier source has local Git blob hash `c4f82bcc19078d82d8b5c780221aef44fff3a6fb`. The connector rejected persistence of the executable source in this run, so this note records the proved reduction and executed census but does not claim a repository-self-contained finite certificate.
