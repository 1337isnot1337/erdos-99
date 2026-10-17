# Target C: exact exclusion of two-singleton support 13

Date: 2026-09-29

Support 13 in the committed thirteen-support narrowing is

`[0123]^2 [0124]^2 [0134]^2 [0234]^2 [1234]`.

This note records a complete orientation-level exclusion for that support in the nine-no-root `k=4, D=-1, d_root=0, p=2` two-selected-singleton profile.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support13_six_empty_obstruction_2026_09_29.py`

The verifier imports the committed orientation model

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28.py`

whose blob on main is `867e8e583f6073c92b1f7afbf2aaf536e2567fa9`.

## Structural lower bound on empty blocks

The support uses all five tetrahedral supports on the label set `{0,1,2,3,4}`, so the touched block family `T` is the ten three-subsets of those five labels. Thus

`|T| = 10`.

The committed triangle-row model gives

`rank H(T) = 6`.

Let `C` be the touched actual-complete blocks, `S` the touched selected-singleton blocks, and `E` the touched actual-empty blocks. Because `d_root=0`, the triangle rows `H(C)` are independent, so `|C|=rank H(C)`. The established four-direction capacity condition gives

`rank H(T) - rank H(C) >= 4`.

Therefore `|C| <= 2`. Since at most two selected singletons lie in `T`,

`|E| = 10 - |C| - |S| >= 10 - 2 - 2 = 6`.

Every realizable state therefore contains at least six touched actual-empty blocks.

## Exact six-empty obstruction

Each multiplicity-two tetrahedral support has three possible oriented pairs, and the multiplicity-one support has three possible orientations. Hence there are exactly

`3^5 = 243`

raw orientation assignments.

For each orientation, the verifier examines every `C(10,6)=210` six-block subset, for

`243 * 210 = 51,030`

subsets total.

For a six-block set `F`, let

`U(F) = sum_{b in F} E_b`,

where `E_b` is the local empty-block constraint space in the nine external coordinates. If all six blocks were actual-empty, then every `E_b` would lie in the actual aggregate constraint space `W`, which has dimension four.

The verifier computes the row rank of `U(F)` modulo 2. The exact census is

- rank 7: `972`;
- rank 8: `1,458`;
- rank 9: `48,600`.

There are no six-block subsets of mod-2 rank at most six. Reduction modulo 2 cannot increase rank, so every one of the 51,030 six-block spans has rational rank at least seven. Such a span cannot be contained in a four-dimensional `W`.

Therefore no orientation of support 13 is realizable.

## Execution provenance

The exact persisted verifier source has Git blob

`affe3fde5bd50d195a274533ea3724cb8ce0d014`.

That exact source was executed locally and produced the census above.

The imported helper on authoritative main has blob

`867e8e583f6073c92b1f7afbf2aaf536e2567fa9`.

The local execution used a reconstructed copy of that helper rather than a byte-identical materialization. As validation, the reconstruction passed the helper's own embedded `rep6` and `rep13` fail-closed reference assertions and independently reproduced the full committed support-11 census:

- orientations: `729`;
- eight-block subsets: `9,382,230`;
- mod-2 rank at least five: `9,380,367`;
- mod-2 rank four: `1,863`;
- exact rank four: `1,863`;
- parity rejects: `1,863`.

The support-13 verifier itself is fully persisted and auditable; no unexecuted new verifier code is used in the exclusion.

## Consequence

This closes support 13 on main. Before this contribution, authoritative main already had exact exclusions for supports 1, 2, 3, 4, 5, 10, 11, and 12. Separate pushed branches contain exact exclusions for supports 6 through 9.

If those four branch certificates are integrated, all thirteen support orbits from the committed two-singleton narrowing are excluded, which closes that two-selected-singleton support frontier.

This does not by itself close the full `D=-1,p=2` branch or Erdos Problem #99.
