# Target C shard 2: cyclic, capacity, and diameter candidates

**Status: unreviewed research.** The source-main reports below are preserved at their original paths from commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; the four exact verifiers are byte-identical to that source commit. Destination theorem-state remains authoritative. No claim in this track is promoted, and C-II and Level I remain open.

## How to read this batch

The authors’ internal labels such as “proved” describe the arguments as written in source reports. They are not independent destination audits. Exact verifier passes establish only their finite stated checks. Treat each result below as a candidate with the hypotheses and missing bridge shown here. The [machine-readable candidate registry](../../targets/target-c/candidate-registry.json) records claims, source/destination hashes, dependencies, obstructions, and next proof obligations. The [central migration ledger](../migration/2026-10-16/ledger/source-main-artifacts.jsonl) contains one exact source-main artifact disposition per indexed report.

## Strongest candidate results and remaining bridges

### Cyclic endpoint and D2/P2 stress branch

Reports 211–214 derive a weighted-cycle transfer identity, isolate the primitive-sixth-root trace case in the D2/P2 equation, force equal transition stresses, and give a positive word-independent KKT stress for nontrivial staircase blocks. These results are restricted to their cyclic/P2 hypotheses. They do not show that every global minimizer enters that branch or produce a finite strict competitor. Continue by proving branch extraction or joining the stress constraints to a source-wide feasible displacement.

### D6 affine windows

Report 216 gives an exact same-cardinality equilateralization comparison for non-equilateral affine windows whose index difference set is D6 invariant. Report 215 gives an approximate diameter inequality under an affine-lattice and orbit-defect hypothesis. The missing bridge is a theorem extracting a D6 window or controlled affine source from arbitrary global minimizers while preserving the full source and its pair constraints. The vanishing-shear and residual-window regressions remain relevant; this package does not close them.

### Quantitative post-ZF bounds

- **DB+NM branch:** report 217 claims `liminf (2h-q)/D >= c_*`, with `c_* = cos(3c_*/2) = 0.6099043189…`, under its unbounded post-ZF survivor hypotheses. The scalar bound still needs an incompatible global capacity or replacement estimate.

- **Density-sensitive PI/JC and pocket routes:** reports 222, 223, and 233 claim the improved floor `liminf (e_BB+2s_C)/D >= 0.465351845396014…`, above the cited Groemer value `0.464792250394…`. The h/D-dependent near-equality configuration remains; reconcile simultaneous PI, JC cavity-capacity, and loaded-attachment equality.

- **Dirichlet/PI feedback:** report 238 claims a `0.4702` floor from its PF/ED two-step bootstrap and diameter-capped moment inequality. It is a branch bound, not an optimal constant or a universal contradiction.

- **Dido pocket envelope:** report 237 proves the stated fixed-chord circular-arc area inequality internally and claims a post-ZF floor `0.831687041775533…` after its global envelope hypotheses. Audit the chain from the source geometry to those hypotheses and close the resulting equality branch.

These numeric improvements are distinct from theorem promotion: they do not change the canonical manifest or C-II status.

### Diameter geometry, stress, and population routes

- **Ball-hull lattice discrepancy (224):** exact support-chart and thin-lattice bounds are paired with a rational verifier; the report leaves the full-core branch open.

- **Diameter-first response (232):** under its triangle-free global-minimizer and lexicographic tie-break hypotheses, the report derives a connected nonisolated core containing every actual diameter endpoint and quadratic joint blockers. It retains isolated source labels. The missing step is an all-pairs feasible source motion with strict endpoint progress.

- **Loaded-chord atlas (235):** its unconditional geometric lemma says a unit pair among actual diameter endpoints must be consecutive in the convex hull of those endpoints when `D>=2`. This is a structural constraint, not a source deformation.

- **Contact-core response (227–229) and diameter graph structure (230, 234, 236):** stress resultants, contracted rigidity, cycle/spine structure, and thrackle completion all have explicit graph or C-II hypotheses. The macroscopic diameter-connectivity and cardinality-preserving endpoint remain open.

- **Direction measure (231):** the compactness theorem assumes positive separation density for exact diameter directions; deriving that density from global minimizers remains a separate obligation.

- **Squaregraph/trains (220), rhombic bulk curvature (221), capped moment (226), and endpoint moment (218):** these provide supporting branch estimates and exact reductions. Their full-core, source extraction, or branch-coverage gaps remain as detailed in each report.

### Regression that blocks a local repair route

Report 219 and its exact verifier preserve a 13-point deep-isolate/octagon-flip regression: deep diameter slack alone does not give the proposed strict local isolate repair. The fixtures are not global minimizers and do not disprove the conjecture. Any repaired route must add a new source-wide or nonlocal hypothesis and continue to check every lower and upper pair.

## Exact verifier evidence

| Verifier | Result | Limit |
| --- | --- | --- |
| `research/verify_target_c_deep_isolate_octagon_flip_2026_10_02.py` | PASS: seven exact 13-point sources and three exact Q(sqrt(3)) degree-five stars | No global optimality certificate |
| `research/verify_target_c_ball_hull_lattice_2026_10_02.py` | PASS: 360 rational source pairs, 720 support margins, 5,947 thin-parabola pairs, and additional exact checks | No full-core or global-optimum certificate |
| `research/verify_diameter_first_joint_depth_2026_10_02.py` | PASS: 7,260 exact depth/interpolation states, 12 sharpness packets, 125 protected axial states | Finite checks only |
| `research/verify_target_c_annular_atlas_2026_09_26.py` | PASS: 3,822 exact separation/diameter pairs and further finite atlas checks | No global or Level I certificate |

These were replayed with the batch receipt’s Python 3.14.7 environment; this is not a registered Python 3.12 replay. See the [coordinator verification receipt](../migration/2026-10-16/receipts/shard-2-batch-211-238-coordinator.json).

## Complete report map (frozen worklist indexes 211–238)

- **211** — [Erdős Problem #99 — cyclic endpoint: exact weighted-cycle transfer formulas](../../reports/target_c_cyclic_weighted_cycle_transfer_2026-09-09.md)
- **212** — [Erdos Problem #99 — D2/P2 has only one extraneous cyclotomic trace](../../reports/target_c_d2_p2_cyclotomic_trace_collapse_2026-09-10.md)
- **213** — [Erdos Problem #99 — cyclic D2/P2 forces equal stress on all four transition contacts](../../reports/target_c_d2_p2_transition_stress_equalization_2026-09-10.md)
- **214** — [Erdos Problem #99 — D2/P2 has a universal word-independent positive KKT stress](../../reports/target_c_d2_p2_universal_staircase_stress_2026-09-10.md)
- **215** — [Erdős Problem #99 — approximate sixfold affine-window stability](../../reports/target_c_d6_approximate_orbit_stability_2026-09-14.md)
- **216** — [Erdős Problem #99 — exact (D_6)-symmetric affine-window comparison](../../reports/target_c_d6_symmetric_affine_window_comparison_2026-09-14.md)
- **217** — [Erdős Problem #99 — sharp DB+NM diameter-branching constant](../../reports/target_c_db_nm_branching_constant_2026-09-09.md)
- **218** — [Erdős Problem #99 — DCJC endpoint excluded by one-gap moment rigidity](../../reports/target_c_dcjc_endpoint_one_gap_moment_exclusion_2026-09-10.md)
- **219** — [Target C — deep diameter slack does not supply a strict isolate repair](../../reports/target_c_deep_isolate_octagon_flip_regression_2026-10-02.md)
- **220** — [Erdős Problem #99 — stopped trains give a defect-stable squaregraph inequality](../../reports/target_c_defect_squaregraph_train_inequality_2026-09-09.md)
- **221** — [Erdős Problem #99 — Target C C73: degree-four rhombic bulk](../../reports/target_c_degree_four_rhombic_bulk_2026-08-31.md)
- **222** — [Erdős Problem #99 — DJC: diameter-density-sensitive PI/JC coupling raises the post-ZF surplus floor](../../reports/target_c_density_sensitive_pi_jc_surplus_2026-09-09.md)
- **223** — [Erdős Problem #99 — pocket detour raises the explicit pinned/contact floor to 0.465](../../reports/target_c_detour_explicit_surplus_0465_2026-09-09.md)
- **224** — [Target C — logarithm-free diameter-endpoint lattice capacity](../../reports/target_c_diameter_ball_hull_lattice_discrepancy_2026-10-02.md)
- **225** — [Erdős Problem #99 — diameter-capped pockets raise the post-ZF floor to 0.634058](../../reports/target_c_diameter_cap_joint_floor_0634057_2026-09-10.md)
- **226** — [Erdős Problem #99 — source diameter caps the outer-pocket cubic moment](../../reports/target_c_diameter_capped_outer_pocket_moment_2026-09-10.md)
- **227** — [Erdős Problem #99 — Target C addendum: positive stress on diameter classes](../../reports/target_c_diameter_class_stress_2026-08-31.md)
- **228** — [Erdős Problem #99 — Target C addendum: diameter-component reciprocal decomposition](../../reports/target_c_diameter_component_reciprocal_2026-08-31.md)
- **229** — [Erdős Problem #99 — Target C addendum: diameter-contracted contact rigidity](../../reports/target_c_diameter_contraction_rigidity_2026-08-31.md)
- **230** — [Erdős Problem #99 — Target C addendum: Reuleaux trapping and diameter-cycle girth](../../reports/target_c_diameter_cycle_girth_2026-08-31.md)
- **231** — [Erdős Problem #99 — DDM: separated exact diameter directions survive as positive measure in convex-body limits](../../reports/target_c_diameter_direction_measure_limit_2026-09-09.md)
- **232** — [Target C — diameter-first rigidity transfer and quadratic joint blockers](../../reports/target_c_diameter_first_transfer_and_joint_depth_2026-10-02.md)
- **233** — [Erdős Problem #99 — diameter-sensitive PI optimization raises the surplus floor](../../reports/target_c_diameter_sensitive_pi_surplus_floor_2026-09-09.md)
- **234** — [Target C-II — diameter-spine order and fan-chain decomposition](../../reports/target_c_diameter_spine_fan_chain_decomposition_2026-10-01.md)
- **235** — [Erdős Problem #99 — global loaded-chord exclusion and diameter-support atlas obstruction](../../reports/target_c_diameter_support_atlas_obstruction_2026-09-26.md)
- **236** — [Erdős Problem #99 — the loaded diameter graph is a deleted odd-cycle spine with pendant leaves](../../reports/target_c_diameter_thrackle_cycle_leaf_completion_2026-09-09.md)
- **237** — [Erdős Problem #99 — sharp Dido pocket envelope raises the post-ZF surplus floor to 0.831687](../../reports/target_c_dido_pocket_surplus_08316_2026-09-10.md)
- **238** — [Erdős Problem #99 — Dirichlet pocket functional plus PI feedback raises the surplus floor to 0.4702](../../reports/target_c_dirichlet_pi_feedback_surplus_04702_2026-09-09.md)

## Dependencies, integrity, and continuation

The source-relative links recorded in this batch resolve in destination main `e1f8ba75b4e9a04c613dcdd3c8fabd6c51e8efd6`; exact edges and supporting-verifier mappings are in the central dependency ledger. Source report bytes and four helper files are hash-matched with no transformation. Rights and source provenance are additive rows in the coordinator addendum.

Next, finish source-main batch reconciliation against the frozen 813-path worklist; consume the next completed shard PR only after refreshing its exact head and independently checking every source blob and destination-tree result. Preserve every report as noncanonical until its proof is separately audited under the exact-head review policy.
