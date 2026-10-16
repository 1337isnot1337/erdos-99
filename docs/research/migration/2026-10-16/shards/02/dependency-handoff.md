# Shard 2 dependency handoff

This note records report and code references outside shard 2. No other worker's report or shared verifier was modified.

## Report links

| Owned report | Frozen backlog target | Current destination / owner |
|---|---|---|
| Index 224, `target_c_diameter_ball_hull_lattice_discrepancy_2026-10-02.md` | Index 4, `target_c_affine_lattice_boundary_vertex_exclusion_2026-09-11.md` | Resolved on current `main` by merged shard 1 PR [#40](https://github.com/1337isnot1337/erdos-99/pull/40); absent at the frozen baseline, as recorded per file. |
| Index 281, `target_c_exact_phase_exterior_train_far_arc_2026-10-01.md` | Index 674, `target_c_star_ray_staircase_reactions_2026-10-01.md` | Present in open shard 5 PR [#49](https://github.com/1337isnot1337/erdos-99/pull/49); coordinate the cross-PR link. |
| Index 287, `target_c_exact_phase_support_caps_2026-10-01.md` | Index 508, `target_c_odd_shell_gap_regression_2026-10-01.md` | Present in open shard 4 PR [#36](https://github.com/1337isnot1337/erdos-99/pull/36). |
| Index 287 and index 315 | Index 511, `target_c_oo_dual_tree_complete_rectangle_2026-10-01.md` | Present in open shard 4 PR [#36](https://github.com/1337isnot1337/erdos-99/pull/36). |
| Index 287, `target_c_exact_phase_support_caps_2026-10-01.md` | Index 658, `target_c_small_swap_face_endpoint_localization_2026-10-01.md` | Present in open shard 5 PR [#49](https://github.com/1337isnot1337/erdos-99/pull/49). |
| Index 287, `target_c_exact_phase_support_caps_2026-10-01.md` | Index 747, `target_c_unit_cut_stress_projection_regression_2026-10-01.md` | Present in open shard 5 PR [#56](https://github.com/1337isnot1337/erdos-99/pull/56). |

These reports are excluded from shard 2 because they are outside its exact index interval. Their presence or future merge does not change any shard 2 report’s source lifecycle.

## Shared code

| Path | Owned consumer(s) | Treatment |
|---|---|---|
| `research/verify_target_c_d6_affine_window_comparison.py` | Indexes 215–216 | Shared verifier referenced outside shard 2; coordinator handoff, not copied or modified. |
| `research/verify_target_c_d6_approximate_stability.py` | Index 215 | Paired shared D6 verifier; coordinator handoff, not copied or modified. |
| `research/verify_ordered_gap_circulation_2026_10_01.py` | Index 280 | Also used by `target_c_single_gap_stationary_diameter_core_2026-10-01.md`; coordinator handoff. |
| `research/verify_target_c_star_ray_staircase_2026_10_01.py` | Index 281 | Also used by `target_c_star_ray_staircase_hostile_audit_2026-10-01.md` and the index 674 reaction report; coordinator handoff. |
| `research/verify_target_c_two_halfdisk_scalar_regression.py` | Index 302 | Shared with report index 28, `target_c_boundary_defect_to_source_refill_frontier_2026-09-30.md` (now present on `main` after PR #40). The helper is absent from the frozen destination and is not copied here. Its frozen blob SHA-256 is `43bb8a6e3e90ca7b131d16cfff7a348bf54ddcd6c9de910d626430267274a0de`; the exterior-cap verifier was run with a temporary exact copy from source. |

Unique code is included and hash-ledgered in its batch PR: eleven verifier scripts across indexes 219, 224, 232, 235, 254, 259, 283, 286, 291, 302, and 285/315. Existing destination scripts `research/target_c_s1_q13_shell_regression.py` and `research/target_c_five_arc_pin_threshold_check.py` were left unchanged and rerun for indexes 198 and 321 respectively.
