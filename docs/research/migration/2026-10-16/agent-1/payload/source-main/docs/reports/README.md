# Research reports and audit archive

`docs/reports/` is a provenance-rich research archive, not a directory of uniformly current theorems. Start with [`../STATE.md`](../STATE.md), [`../state/theorem-state.yaml`](../state/theorem-state.yaml), and the generated [`../state/artifact-index.jsonl`](../state/artifact-index.jsonl).

## Status rule

A report is canonical only when the state lock or an active target route map explicitly promotes its exact theorem ID. A merged PR or a file present on `main` is not enough.

The conservative default is **unreviewed**. `audited-working` is never inferred from a filename, date, PR merge, or presence on `main`; an audit must explicitly earn that status. The theorem/claim vocabulary is canonical, unreviewed, audited-working, conditional, regression, superseded, rejected, and provenance.

Every research artifact in the configured report/audit/archive roots has a generated first-line `<!-- theorem-state: ... -->` metadata header. The header and `artifact-index.jsonl` are generated from the manifest by `tools/build_artifact_index.py`; do not hand-promote a report by editing its header. When one physical report is the source for claims with different theorem statuses, its artifact-level header says `status: mixed` and carries an exact `claim_statuses` map. `mixed` is an artifact container state, not an additional theorem status; use the claim ID's status for logical dependency decisions.

## Current navigation

- Target A: [`../targets/target-a/README.md`](../targets/target-a/README.md)
- Target B: [`../targets/target-b/README.md`](../targets/target-b/README.md)
- Target C: [`../targets/target-c/CURRENT.md`](../targets/target-c/CURRENT.md) and [`../targets/target-c/README.md`](../targets/target-c/README.md)
- Recovered full-core candidate: [`target_c_fullcore_detour_currency_trichotomy_2026-10-02.md`](target_c_fullcore_detour_currency_trichotomy_2026-10-02.md) (unreviewed; C-II remains open).

Target C's pre-cleanup promoted catalog remains at [`../targets/target-c/HISTORY-pre-cleanup-2026-09-11.md`](../targets/target-c/HISTORY-pre-cleanup-2026-09-11.md), subject to later state-lock overrides.

### Target B lattice restrictions and interface candidates

- [`target_b_uniform_lattice_flex_2026-09-25.md`](target_b_uniform_lattice_flex_2026-09-25.md) gives an unreviewed exact-lattice flex candidate for nontriangular planar lattices with minimum spacing at least one.
- [`global_unit_hull_lattice_boundary_loss_2026-09-26.md`](global_unit_hull_lattice_boundary_loss_2026-09-26.md) gives an unreviewed translated-lattice competitor under one-chart and stated physical-interface hypotheses. The multi-chart seam closure and the Target B joint shell-stability inequality remain open.


## Independent audits completed 2026-09-11

### Target B dense-grid / penetration / interpolation chain

[`target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md`](target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md) promotes the corrected DT1–DT4, TG1–TG3, PDG, PC1/PC3, MCP1, fixed-`lambda` MCP2, and GPI tools at their exact pure-disk/coherence scopes. The GPI conclusion is a dominant-component theorem, not a multi-grain globalization or a proof of the full shell-stability inequality.

### Target C PR #188

[`target_c_pr188_full_dependency_audit_2026-09-11.md`](target_c_pr188_full_dependency_audit_2026-09-11.md) independently certifies the all-phase renormalized-surplus chain

\[
\mu_D={e_{BB}+2s_C-3(d_H+s_Z)\over D},
\qquad
\liminf\mu_D\ge z_*>0.9604.
\]

[`target_c_attachment_perimeter_three_gap_endpoint_repair_2026-09-11.md`](target_c_attachment_perimeter_three_gap_endpoint_repair_2026-09-11.md) excludes the endpoint `mu_D->z_*`, yielding a nonexplicit absolute gap above it. The old Eppstein near-quadrangulation interpretation remains rejected. The exact five-arc threshold script `research/target_c_five_arc_pin_threshold_check.py` is registered under canonical theorem `C-MU-09604` and is executed by theorem-state CI.

### Target C PR #182

[`target_c_pr182_full_dependency_audit_2026-09-11.md`](target_c_pr182_full_dependency_audit_2026-09-11.md) independently certifies the RSR/DD and boundary-sharing chain. It also extracts the stronger HE+ coefficient already implicit in the hidden-edge proof and certifies

\[
\liminf {e_{BB}+2s_C\over D}>0.5983685.
\]

The pocket-degree Dirichlet theorem is valid; its displayed optimizer near `0.76719537` remains exploratory only.

### Target C PR #191

[`target_c_pr191_dependency_audit_2026-09-11.md`](target_c_pr191_dependency_audit_2026-09-11.md) rejects the claimed `0.99554058458...` ordinary-surplus theorem. The load-bearing cyclic Reuleaux-cap step puts an inward OP pocket in an exterior cap on the opposite side of the force-hull chord, so the general `b-P_F=O(sqrt D)` / `H_out=o(D^2)` premise is unproved.

The independently surviving cyclic structural facts are near-maximal force-hull perimeter, disk-limit force-hull area, and `E=O(D)`.

### Target C primitive cyclic-shell P1/S1 chain

[`target_c_cyclic_shell_d1_p1_s1_dependency_audit_2026-09-11.md`](target_c_cyclic_shell_d1_p1_s1_dependency_audit_2026-09-11.md) certifies the historical `d_H=1` shell chain only at the exact primitive all-loaded scope `m=0`, `d_H=1`, `s_Z=1`. P1 is completely excluded by the Littlewood/2-adic ramification argument. S1 is reduced exactly to the reciprocal-square system but is not excluded. The finite `q=13` S1 KKT/PSD package remains a numerical regression rather than a global-minimizer theorem.

## Binding corrections commonly surfaced by search

Before using an older Target C report, check whether it depends on any of these rejected inferences:

- incident diameter sequence `=>` Euler trail/path;
- FB4 force-bulk localization;
- incompatible projective cut/orientation in the old C53 pentagon objection;
- RSR equality uniqueness;
- Eppstein near-equality `=>` near quadrangulation;
- five-host measure saturation `=>` all five hosts populated;
- inward OP pocket contained in the exterior Reuleaux minor cap.

The state lock gives exact scope and surviving repaired conclusions.

## Writing new reports

Use [`REPORT_TEMPLATE.md`](REPORT_TEMPLATE.md). State exact dependencies, proof status, regressions checked, what the theorem does not prove, and the requested promotion status. New reports enter as `unreviewed` unless the same change carries an explicit completed audit and ledger classification. A frontier-changing theorem must update the state files and active route in the same change.


## Recovered unreviewed salvage reports — 2026-10-05

These reports preserve distinct research candidates and regressions from the resumed branch-cleanup pass. Their lifecycle remains unreviewed unless explicitly marked as a regression or rejection in the report. Presence here does not promote them.

- Target B: [four-bar singleton endpoint exclusion](target_b_fourbar_singleton_endpoint_exclusion_2026-10-03.md) and [zero-gradient mixed-order descent](target_b_zero_gradient_mixed_order_descent_2026-10-03.md).
- Target C settlement: [antitone interval-SCC release](target_c_antitone_interval_scc_release_2026-10-03.md), [exclusive fan-port budget](target_c_exclusive_fan_ports_augmented_budget_2026-10-03.md), and [two-unit-side completion regression](../../research/target_c_completion_two_unit_side_regression_2026-09-12.md).
- Target C interleaved SCC: [actual-diameter regression](target_c_interleaved_scc_actual_diameter_regression_2026-10-03.md) and [two nested-chain condensation](target_c_two_nested_chain_condensation_2026-10-03.md).
- Target C full-flower allocation: [mixed-phase allocation synthesis](target_c_mixed_phase_full_flower_allocation_2026-10-04.md).
- Target C good-end tradeoffs: [outer-walk tradeoff audit](target_c_good_end_outerwalk_tradeoff_audit_2026-10-03.md) and [physical hull-end capacity and high-t audit](target_c_physical_hull_end_capacity_and_high_t_audit_2026-10-03.md).
- Target C convex-width refinements: [explicit endpoint gap](target_c_convex_width_explicit_endpoint_gap_2026-09-30.md), [fixed-point endpoint exclusion](target_c_convex_width_fixed_point_endpoint_exclusion_2026-09-30.md), [near-global carrier upgrade](target_c_convex_width_nearglobal_carrier_upgrade_2026-09-30.md), and [Section-122 feedback](target_c_convex_width_section122_feedback_2026-09-30.md).
- Target C exact-phase refinements: [edgewise KKT balance](target_c_exact_phase_threshold_edgewise_kkt_balance_2026-10-02.md), [nested span flag](target_c_exact_phase_threshold_nested_span_flag_2026-10-02.md), [cross-shore escape](target_c_exact_phase_threshold_cross_shore_escape_2026-10-02.md), [fixed-angle reaction braid](target_c_exact_phase_fixed_angle_reaction_braid_2026-10-01.md), and [transverse nested matching](target_c_exact_phase_threshold_transverse_nested_matching_2026-10-02.md).
- Target C diameter structure: [spine fan-chain decomposition](target_c_diameter_spine_fan_chain_decomposition_2026-10-01.md), [switch-edge antipodal side pairs](target_c_switch_edge_antipodal_side_pairs_2026-09-30.md), and [repeated-swap witness collapse](target_c_endpoint_repeated_swap_witness_collapse_2026-10-01.md).

## Rooted wrapping-endpoint phase and defect candidates (2026-10-05)

This proof-only packet preserves the final route-phase endpoint exclusion, its rate-free
boundary-dispersion repair, the stronger explicit (4\cdot10^{-5}) quantitative
phase gap, the wrapping-root defect ledger and consequences, and the four-cell rigidity
report. The older run5/run8/run9 endpoint derivations are superseded by the clean
run11 proof; the v3 run11 copy has a damaged formula and is not copied. The earlier
(5\cdot10^{-11}) phase-gap report was already preserved by #665 and is not duplicated.

All new reports remain unreviewed and noncanonical. They do not change theorem state,
route status, C-II, or Level I. There is no standalone exact verifier for this analytic
argument; preservation is not an audit of the proof.

Source refs: `proof/rooted-endpoint-route-phase-audit-run10-20260930` at
`334482f20128e8ff8d51d7642268c021e91183aa`; `proof/target-c-root-endpoint-exclusion-20260930`
at `2cad247fdb684394630d5cae96a455befaa15a85`; `proof/target-c-root-phase-endpoint-exclusion-20260930-run5`
at `6e4dbd5340ed64f5ffafc0fe4421987d497bcacf`; `proof/target-c-root-phase-endpoint-exclusion-run8-20260930`
at `8d983f9b53d24a8211ce0c1b65e272381947fc19`; `proof/target-c-rooted-endpoint-phase-exclusion-run11-clean-20260930`
at `77471abe61af89053951680b2f43f94d43876740`; `proof/target-c-rooted-endpoint-phase-exclusion-run11-v3-20260930`
at `852d08d41e2e7942ef74734a876652c167141c0a`; `proof/target-c-rooted-quant-gap-4e5-v2-20260930`
at `fb084e7cc2b430a6d4b70124fc4dda199a8035c2`; `proof/target-c-rooted-quant-phase-gap-20260930`
at `825131dc71aa5c984066341c7c8a6f5143104812`; `proof/target-c-rooted-route-phase-endpoint-exclusion-run9-v2-20260930`
at `ab76928fea0b4fb3ef30b4ac4bb819cfcffd1097`; `proof/target-c-wrapping-endpoint-four-cell-rigidity-20260930`
at `3b1293ad8fa2d5aa5aa1d14f8c79a740c2546c53`; `proof/wrapping-defect-stability-20260930` at `e2f8c6a1b78857d5cfc33a4a7849e52cf5222d79`; and `proof/wrapping-defect-stability-20260930-v2` at `5185bd510f89520fdcef7c68b636ec1115a170df`.

## Fixed-star bounded and stress-light cusp candidates (2026-10-05)

This proof-only packet preserves the bounded switching-cusp extraction on each
fixed-star shore, its stress-light refinement, the joint two-shore switch budget, and
the later witness-cell reduction of the genuine two-bar strip case. The clean latest
report revisions are used; earlier r2/r3 and LaTeX-corrupted variants are collapsed.

All claims remain unreviewed and noncanonical. The source reports include no standalone
verifiers or numerical certificates; preserving them does not audit the analytic or
geometric hypotheses. No theorem-state, route, prompt, C-II, or Level I status changes.

Source refs: `proof/target-c-fixed-star-bounded-switch-cusps-20261001` at
`9499600c4c1e0087bc053567b03253c22f188ae7`; `proof/target-c-fixed-star-stress-light-cusps-20261001-r2`
at `b58f8f4de19b98f04b00a5ae6c55014447fce12d`; `proof/target-c-fixed-star-stress-light-cusps-20261001-r3`
at `cf391aa58ed642bbb1ea84e2ef7eaf954c35c65f`; `proof/target-c-stress-light-bounded-cusps-20261001`
at `c283580833d23e4c5216cf067977777d8b11e231`; `proof/target-c-joint-grid-switch-budget-20261001` and
`proof/target-c-joint-stress-light-cusps-20261001-r11` at the shared tip
`4abd2eb3cbdeb122f8ca787cb9cdbd7522e9c978`; `proof/target-c-joint-stress-light-cusps-r11`
at `a026aef993becb7a25cf08a69fba0f8ea4820634`; `proof/target-c-joint-stress-light-cusps-r11-clean`
at `257b4d95c0ddb43b13b390c40f466eefbff6f92d`; `proof/target-c-joint-stress-light-cusps-r11-final`
and `proof/target-c-witness-cell-excludes-tb2-20261001` at the shared tip
`a8cffebb2d0ba945ec45b18a5054cb56d4422121`; and
`proof/target-c-witness-cell-tangent-reduction-20261001-r11` at
`df5d3b2ec5d89c96c0599e5a225bd4fdb186cb41`.

## Target B reports recovered from local worktrees (2026-10-05)

- [Affine source audit and exact diameter stretch](target_b_affine_audit_and_diameter_stretch_2026-09-25.md) records a conditional affine-flat-mode criterion and an independent affine-lattice audit. It does not establish that unbounded global minimizers satisfy the criterion or close the canonical shell-stability endpoint.
- [Phase-flow dual obstruction](target_b_phase_flow_dual_obstruction_2026-09-25.md) records a candidate DAG rank-work/sparse-support lemma and a geometric regression against core-only relaxation inferences. It does not give a source-preserving global diameter improvement.

Both reports remain unreviewed and noncanonical. Neither has a standalone verifier.

## Target C reports recovered from local worktrees (2026-10-05)

- [Convex shared-witness outer occurrences](target_c_convex_shared_witness_outer_occurrences_2026-10-02.md) records a candidate source multiplicity charge and a finite contact-isolated regression. Its stopped-train and near-disk applications remain conditional.
- [Sharp contact-arc threshold and failed transfer bridge](global_contact_arc_threshold_2026-09-26.md) records an unreviewed selected-support threshold candidate, exact hexagon transfer regression, and near-threshold examples.
- [Star-ray hostile-audit addendum](target_c_star_ray_hostile_audit_addendum_2026-10-05.md) describes added exact finite endpoint regressions; the original verifier is also extended.
- The existing [diameter-support atlas obstruction](target_c_diameter_support_atlas_obstruction_2026-09-26.md) includes a recovered Section-75 scope correction that remains unreviewed.

These artifacts do not change the active route, C-II, or Level I status.

## Additional Target B revisions recovered from #700 source worktrees (2026-10-05)

The dirty revisions of [uniform lattice flex](target_b_uniform_lattice_flex_2026-09-25.md) and [unit-hull boundary loss](global_unit_hull_lattice_boundary_loss_2026-09-26.md) were not included in the initial #700 merge. The first extends the candidate to all nontriangular lattices with minimum spacing at least one. The second adds nonresonant interface bounds and a seam ledger, plus exact checker assertions and an optional floating-point phase scan. Both remain unreviewed and noncanonical; the multi-chart/global Target B closure remains open.

## Target C good-hull singleton candidate (2026-10-05)

[Good-hull singleton face charge](target_c_good_hull_singleton_face_charge_2026-10-05.md) records a proof-only finite charge and a full-core Type-II strengthening. The report remains unreviewed and noncanonical, has no standalone verifier, and does not close C-II. Its source was based on the pre-`audit.52` main snapshot.

## Target C full-flower blocker candidate (2026-10-05)

[Full-flower blocker k-payment](target_c_full_flower_blocker_k_payment_2026-10-05.md) records a proof-only full-core Type-II charge from the flower-blocker route. It has no standalone verifier and remains unreviewed and noncanonical. Its source predates the later `audit.52` promotion; it does not close C-II.

## Target C contact-manifold coordinate candidate (2026-10-05)

[Local diameter coordinate normal form](target_c_contact_manifold_local_diameter_coordinates_2026-10-05.md) records a proof-only finite local result under the audit.52 full-core hypotheses. It remains unreviewed and noncanonical, has no standalone verifier, and does not establish global diameter improvement. Recheck its dependencies against the current audit.54 route.
