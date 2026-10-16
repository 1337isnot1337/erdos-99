# Target C: exact exclusion of two-singleton support 7

Date: 2026-09-29

Support 7 in the committed thirteen-support narrowing is

`[0123]^3 [0124] [0134] [0145] [0156] [0234] [1234]`.

This note records a complete orientation-level exclusion for this support in the nine-no-root `k=4, D=-1, d_root=0, p=2` two-selected-singleton profile.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support7_eight_empty_obstruction_2026_09_29.py`

## Structural lower bound on empty blocks

For every orientation, the touched block family `T` is support-determined and has

`|T|=16`, `rank H(T)=10`.

Let `C` be the touched actual-complete blocks, `S` the touched selected-singleton blocks, and `E` the touched actual-empty blocks. Because `d_root=0`, `H(C)` is independent. The established four-direction capacity condition gives

`rank H(T)-rank H(C)>=4`.

Hence `|C|<=6`. Since at most two selected singleton blocks lie in `T`,

`|E|=16-|C|-|S|>=16-6-2=8`.

Thus every realizable state contains at least eight touched actual-empty blocks.

## Exact eight-empty obstruction

There are six multiplicity-one tetrahedral supports after the triple support, so there are exactly `3^6=729` raw orientation assignments. For each orientation the verifier examines all `C(16,8)=12870` eight-block subsets, for a total of `9,382,230` subsets.

For an eight-block set `F`, let `U(F)=sum_{b in F} E_b`, where `E_b` is the exact rational local empty-block constraint space in the nine external coordinates. If `rank_Q U(F)>=5`, then `F` cannot consist of actual-empty blocks because the actual aggregate constraint space `W` has dimension four.

The verifier first computes rank modulo 2. Reduction modulo 2 cannot increase rank, so a mod-2 rank of at least five proves rational rank at least five. The exact executed census is:

- orientations: `729`;
- eight-block subsets: `9,382,230`;
- mod-2 rank at least five: `9,380,367`;
- mod-2 rank four: `1,863`;
- exact rational rank four among those exceptions: `1,863`;
- necessary generalized-weight/parity rejects: `1,863`;
- survivors: `0`.

For each exceptional rank-four span, if those eight blocks were actual-empty then their span would equal the rank-four aggregate space `W`. Every such span fails the committed necessary generalized-weight filter `parity_profile_ok(W)`. Hence no orientation is realizable.

The exact verifier source executed before commit had Git blob `5ce88ef0ada8403005f23da702780167761bd4c9`. It uses the current-main selected-pair orientation module, GitHub blob `867e8e583f6073c92b1f7afbf2aaf536e2567fa9`.

This closes support 7 only. It does not close the full two-selected-singleton profile.
