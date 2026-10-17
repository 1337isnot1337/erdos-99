# Target C: two-singleton support12 orientation shard 2

Date: 2026-09-28

Status: exact executed partial orientation certificate for the explicit nine-no-root `k=4, D=-1, d_root=0, p=2` two-selected-singleton support

`[0123]^3 [0124] [0134] [0145] [0234] [1234] [2346]`.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support12_orientation_shard2_2026_09_28.py`

Executed verifier blob:

`06799629143aa8ba284694d47e57603db200db58`

The verifier imports the exact rational quotient-coordinate and generalized-weight machinery from

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28.py`,

blob `867e8e583f6073c92b1f7afbf2aaf536e2567fa9` on main.

For a fixed cycle-choice assignment, let `W` be the aggregate external coefficient rowspace. Every realizable state has rank `4` here. Its generators consist of the local spaces of actual-empty touched blocks plus the nonzero constraint lines contributed by at most two selected singleton blocks.

The verifier searches a superset of these possibilities. It permits every touched local empty space independently, and it permits up to two arbitrary nonzero singleton constraint lines from any touched blocks, without enforcing a legal root-state assignment. Zero singleton constraints are covered by simply omitting a singleton line. Deduplicating equal singleton lines cannot remove an aggregate rowspace because repeated equal lines do not change their span.

Every realizable rank-four `W` is therefore present in the searched family.

The already-audited nine-coordinate parity-check criterion implies that every realizable `W` must satisfy

`(d1,d2,d3,d4,d5) >= (2,4,5,7,8)`.

The imported `parity_profile_ok(W)` is equivalent to those lower bounds for a rank-four parity-check space: no zero column, every three columns have rank at least two, and every six columns have rank at least three.

This shard is the deterministic orientation-index interval `[54,81)` from `oriented_exts(SUPPORT)`. There are six multiplicity-one supports, each with three cycle choices, so the 729 assignments are ordered as six base-three digits. In this interval the first choices for `[0124]` and `[0134]` are fixed, the third choice for `[0145]` is fixed, and all `3^3=27` choices for `[0234]`, `[1234]`, and `[2346]` are exhausted. The repeated `[0123]^3` support already contains all three cycles.

Exact executed census:

- cycle-choice assignments: `27`;
- relaxed rank-four aggregate spaces: `40,586`;
- generalized-weight-admissible spaces: `0`.

The verifier fail-closes on the exact Counter equality

`{"orientations": 27, "rank4_spaces": 40586}`.

Therefore all 27 cycle-choice assignments in `[54,81)` are impossible.

Together with the already committed shard `[0,27)`, this rigorously excludes 54 of the 729 orientation assignments for this explicit support. The remaining 675 assignments are not closed by these two certificates.

This is a rigorous partial certificate only. It does not close support 12, the full two-singleton profile, the `D=-1,p=2` branch, or Erdos Problem #99.
