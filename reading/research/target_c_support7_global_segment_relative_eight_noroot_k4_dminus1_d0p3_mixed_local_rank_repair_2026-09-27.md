> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_mixed_local_rank_repair_2026-09-27.md) · source SHA-256 `17e2ec317520964a658f523875b390157fffb102e9a37f0f725518c52489c834`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "59020862c2017fd7dcee1c3a2ba6a106d75aa73f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_mixed_local_rank_repair_2026-09-27.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "956bdebc86d7fa061a1b24aba6f0624dbee741b3730584349e535a158499e8e7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: repair the eight-no-root k=4, D=-1, d_root=0, p=3 mixed-profile local-rank certificate

Date: 2026-09-27

Status: exact support-level repair of the mixed singleton-plus-pair closure in
`research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_mixed_closure_2026-09-26.md`.
The old verifier used the false converse that a touched block with no repeated containing tetrahedral support must have local empty rank one. This note removes that converse. The resulting larger relaxation still has zero survivors.

Companion verifier:
`research/verify_target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_mixed_local_rank_repair_2026_09_27.cpp`

## Branch data

The branch is `k=4, D=-1, d_root=0, p=3` with one selected singleton block and one selected pair block. The existing deletion argument gives
`rank(P)=4` and `(d1,d2,d3,d4)(P)>=(4,5,6,7)`.

If `h` is the number of touched root blocks and `e` the number of touched actual-empty blocks, at most two selected incomplete blocks are touched and at most fifteen touched blocks are complete. Hence `e>=h-17`. Every actual-empty block has at least four incidences, so
`32>=4e+(h-e)>=4h-51`, therefore `h<=20`.

## Sound local-rank relaxation

For a touched block `b`, write `I_b` for its set of external occurrences and `E_b` for its actual-empty coefficient space when the block is empty.

A repeated containing tetrahedral support forces `dim(E_b)=2`, but the converse is false. The repaired verifier therefore uses only:

- repeated support: rank two, requiring `|I_b|>=5` by `d2>=5`;
- no repeat and `|I_b|<4`: impossible by `d1>=4`;
- no repeat and `|I_b|=4`: rank one only, since rank two would violate `d2>=5`;
- no repeat and `|I_b|>=5`: permit both ranks one and two.

For chosen virtual ranks it uses only the necessary generalized-weight compatibility conditions:
line-line `|I intersect J|>=4` or `|I union J|>=5`;
plane-line `|I intersect J|>=4` or `|I union J|>=6`;
plane-plane `|I intersect J|>=5`, or both `|I intersect J|>=4` and `|I union J|>=6`, or `|I union J|>=7`.

The selected pair contributes no coefficient constraint. A touched selected singleton is allowed either zero constraint or one line. For a nonzero singleton line the verifier uses the full occurrence set as an upper support. This is a safe relaxation: enlarging the true line support can only increase the intersection and union quantities used by these compatibility tests and can only enlarge the generator support.

The nominal generator dimension must be at least four, and its upper support must cover at least seven external coordinates because `d4(P)>=7`.

## Root-state conditions

For every virtual empty family the verifier enumerates all four selected-block touch patterns: both untouched; singleton touched only; pair touched only; both touched on distinct blocks.

If `I` is the resulting touched incomplete family and `C=T\\I`, then `d_root=0` requires the triangle rows in `C` to be independent. The face-local relation theorem gives the necessary capacity condition
`rank H(T)-rank H(C)>=4`.
Both conditions are checked exactly.

## Executed exact certificate

Canonical augmentation reproduces the established `S_7` orbit counts
`1,1,4,14,61,268,1283,6032,27763`
for support-multiset sizes zero through eight.

The executed repaired census is:

- size-eight support orbits: `27763`;
- orbits with `h<=20`: `13574`;
- relaxed final placement tests: `2025788`;
- zero-singleton-line tests: `1045473`;
- nonzero-singleton-line tests: `980315`;
- survivors: `0`.

Therefore the mixed singleton-plus-pair branch remains closed after removing the false local-rank converse.

All support and incidence decisions are exact integer combinatorics. Triangle-row ranks are computed modulo `2^31-1`; the verifier checks the Lucas-Lehmer condition and `(2^31-1)^2>3^15`. Hadamard's inequality therefore makes every triangle-row rank decision exact over `Q`.

This repairs only the mixed `p=3` profile. The three-singleton `p=3` subcases and the separate `d_root=1,p=0` certificate still require their own audit or repaired certificates wherever they use the same false converse non-monotonically.
