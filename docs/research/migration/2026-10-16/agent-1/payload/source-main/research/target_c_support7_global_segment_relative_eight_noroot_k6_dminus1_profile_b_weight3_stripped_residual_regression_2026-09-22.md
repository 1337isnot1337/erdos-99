# Regression: stripped weight-three Profile-B residual has exact survivors

Date: 2026-09-22

Status: **exact regression / hostile audit**, not a closure theorem.

This note records an independent full execution of

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_weight3_five_row_residual_2026_09_22.py`.

The scan is deliberately the **stripped** five-row residual: after deleting a
minimum weight-three coefficient word it counts only the six retained incomplete
root rows.  It therefore uses `p'=6` in the child accounting.  That is not the
unstripped source accounting used by the active Profile-B closure, where all nine
selected incomplete-root rows remain in the row set and `p=9`.

## Exact execution

Command:

```text
python3 research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_weight3_five_row_residual_2026_09_22.py --assert-empty
```

The `--assert-empty` failure was removed only in a temporary copy so that the
complete counters could be printed; the committed verifier itself is unchanged.
The exact run covered all `20,451` five-no-root `S_7` orbit representatives and
reported:

```text
candidate_census {
  (6,3):56, (6,4):3077, (6,5):16, (6,6):3,
  (7,3):55, (7,4):4920, (7,5):52, (7,6):11,
  (8,3):40, (8,4):3068, (8,5):80, (8,6):73,
  (9,4):383, (9,6):122,
  (10,4):159, (10,6):96
}
candidate_count 12211
max_extra_rank 6
extra_rank_six_survivor_count 305
unique_complete_sets_ranked 13425
max_row_norm_squared 35
max_functional_width 18
hadamard_exact_rank_bound True
```

All coefficient spaces, canonical relation rows, and singleton-functional ranks
were evaluated by the verifier's exact rational/modular-Hadamard machinery.  The
first surviving orbit is already an exact rational witness; for example, orbit
`17` with extension rows `(106,109,112,105,107)` and coefficient line
`(0,0,0,1,-1)` has ten complete blocks, eight compatible singleton states, and
extra rank six.  Thus the zero-survivor assertion is false for the stripped
problem.

## Why this does not reopen the canonical closure

The active unstripped argument in
`target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_weight3_unstripped_closure_2026-09-22.md`
keeps the original nine selected incomplete-root rows after puncturing the three
external coordinates.  The transported child defect is `D_5=2`, and the exact
rank-uniform inequality is

```text
D_5 >= 5 + 9 + 3 d_5 - 3 s_5.
```

It therefore requires `s_5>=6` when `d_5=2` and `s_5>=7` when `d_5=3`.  The
committed exact five-row censuses give maxima `2` and `6`, respectively, so the
unstripped bridge excludes the weight-three source word.  The present 305
stripped survivors are precisely why replacing `p=9` by the retained-row count
`p'=6` would be an invalid shortcut.

**Disposition:** the stripped finite statement is falsified by 305 exact
survivors; the canonical unstripped weight-three closure remains valid and was
independently rerun (`verify_target_c...profile_b_weight3_unstripped_closure_2026_09_22.py` → PASS).  No theorem-state files change.  The remaining live target is the all-eight-clean Profile-B source lift.
