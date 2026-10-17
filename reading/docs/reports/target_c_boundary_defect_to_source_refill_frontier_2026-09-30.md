> Generated reading edition · [exact source](../../../docs/reports/target_c_boundary_defect_to_source_refill_frontier_2026-09-30.md) · source SHA-256 `8e88b4bd1edfb44a8155419c725d734951f06ec8ab52eceb7bd90437ee8d48ae`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-35750FED0E9D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: remaining boundary-defect to source-refill theorem

**Date:** 2026-09-30<br>
**Starting main:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`<br>
**State version:** `2026-09-14.audit.51`<br>
**Classification:** conditional reduction and attempt ledger; noncanonical.<br>
**Level I:** open. C-I is canonically closed; C-II remains open.

## 1. Checkpoints and exact new frontier

This run independently derived the exact contiguity of diameter stars and the
cover of all but $`2d_H`$ loaded hull sides by consecutive diameter V's.
A concurrent independent contiguity proof appeared on remote branch
`proof/target-c-global-diameter-star-contiguity-v2-20260930` at `c2f1850d`.
It was not on main when first inspected and was subsequently merged into
main during this run. The work here was reconciled against that commit.
Its thrackle proof is consistent with the normal-cone proof here; it is not
an imported canonical dependency. The theorem-state lock did not change.
The concurrent quantitative near-endpoint V-cover at `c00bb080` was also
checked on its proof branch; it quantifies the same direction-excess budget
and does not supply the missing source replacement.

An analytic regular-Reuleaux-polygon shell then showed that $`o(D)`$
ordinary contiguous stars can carry $`(\pi+o(1))D`$ incidences, even with
an exact V-cover, $`q/D\to\pi`$, and a disk limit. The shell is not a
global-minimizer or harmonic-core certificate.

The train-boundary arguments subsequently proved candidates for:

1. four opposite straight support faces under sublinear route/face defect;
2. the finite symmetry estimate
   ```math
   d_{\rm BL}(\nu_P,\sigma_\#\nu_P)
   \le2\sqrt{2LZ}+2Z+20Q;
   
   ```
3. a centrally symmetric parallelogram limit under those defects;
4. exclusion of **every** positive-area circle-supported carrier with
   $`Z+Q=o(D)`$, including diameter-one wrapping limits, because a cyclic
   parallelogram is a rectangle while the forced phase directions differ by
   $`\pi/3`$.

For a fixed positive carrier-area floor and the canonical uniform constants,
the last result gives an existential $`\epsilon>0`$ with
$`Z+Q\ge\epsilon D`$. It does not construct a shorter source.
The exact rooted threshold is conditionally excluded through the current
unpromoted defect-stability package. Positive linear defects remain allowed.

The strongest candidate requiring independent audit is the occurrence-counted
boundary trimming and hull-extension argument in
`target_c_convex_geodesic_rhombus_limit_2026-09-30.md`. Its artificial crossings
are explicitly paid by radius-two tube counts, rather than inferred from
near-boundary alternation alone. A final hostile audit replaced the informal
per-route trimming count with a clipped-projection inequality whose endpoint
differences telescope over the entire side chain.

## 2. Exact finite source quantity

Let $`A`$ be the **entire** canonical C-II source, including contact isolates,
let $`D=\operatorname{diam}A`$, $`K=\operatorname{conv}A`$, and let $`H`$
contain every actual source diameter pair. For a vertex cover $`S`$ of $`H`$,
define
```math
\nu_A(S)=\max\bigl\{|T|:
T\subset\operatorname{int}K,\quad
\operatorname{sep}T\ge1,\quad
|t-a|\ge1\ (t\in T,a\in A\setminus S)\bigr\}.
\tag{2.1}
```
This is an integer packing capacity of actual vacant sites after removing
the specified source points. Auxiliary scaffolds, single-site feasibility,
and area budgets do not compute it.

If $`\nu_A(S)\ge|S|`$ for any such cover, choose exactly $`|S|`$ sites.
They yield $`A'=(A\setminus S)\cup T`$ with exactly $`|A|`$ points and
unit separation. Every remaining old-old pair is strictly below $`D`$.
Since finite $`T`$ lies in $`\operatorname{int}K`$, its minimum depth
$`\rho>0`$ is positive. For $`t\in T,a\in K`$, the support-width bound
gives $`|t-a|\le D-\rho`$; for two new points it gives
$`|t-t'|\le D-2\rho`$. Thus $`\operatorname{diam}A'<D`$.

This cover/refill mechanism is known; the unmerged PR #581 already proves
a source-level version. It is restated here to identify the actual missing
capacity, not claimed as a new solution mechanism.

Woodall's exact classification gives a cover of size at most
$`\lceil q/2\rceil`$: color a forest, or remove one odd-cycle vertex and
color the remaining forest. With the non-star angular bound
$`q\le\pi/(2\arcsin(1/(2D)))`$, it is at most
$`\pi D/2+1/2`$. High-degree star concentration can reduce this number;
it cannot provide the required new sites.

## 3. Exact missing theorem for the surviving full-core branch

**Defect-to-refill lemma (unproved).** Fix a positive carrier-area floor
$`\Gamma`$ and the canonical uniform constants. There exists $`D_0`$ such
that for every canonical triangle-free full-core global source with
$`D\ge D_0`$, if an actual harmonic carrier satisfies
```math
\operatorname{area}P\ge\Gamma D^2,\qquad Z_P+Q_P\ge\epsilon D
```
with the forced positive defect from this run, then
```math
\boxed{\exists S\text{ a vertex cover of the full }H:
\quad\nu_A(S)\ge|S|.}
\tag{3.1}
```

The candidate no-zero-defect theorem forces the antecedent on a quadratic
carrier. Formula (3.1) supplies an exact same-cardinality strict competitor
and would close the full-core branch. A replacement allowed to move the
entire retained core could be weaker and also sufficient; (3.1) is one
precise finite capacity target, not claimed necessary for every possible
solution.

For the macroscopic-container branch the separate sufficient missing theorem
is the same full-source cover/refill conclusion, obtained by jointly replacing
part of the old diameter-carrying core and repacking its inactive population.
The existence of a near-capacity isolate chamber alone has not proved it.

## 4. Serious closing approaches attempted and their failures

| Approach | Actual result or failure |
| --- | --- |
| Direction runs and diameter-star incidence | Contiguity is exact, so re-entry is absent. Small ordinary hub populations still have linear incidence mass in the analytic shell regression. |
| Common antipodes, curvature, constant width, and winding | The regular Reuleaux shells realize the complete V-cover, support-width behavior, and cyclic topology. These shell hypotheses supply no contradiction or source vacancies. |
| Harmonic trains and equality classification | The zero-defect regime is excluded by the new symmetry and convex train-topology arguments. Their estimates allow positive linear defect; the rooted ledger allows that regime too. |
| First-order deformation | Full-support KKT makes every feasible fixed-diameter critical variation zero on every active row. Canonical ZF has rank $`2v-3`$, so on the nonisolated core it is rigid. No nonrigid infinitesimal decrease was found. |
| Stress duality | The same positive stress freezes the critical cone. The new boundary defect supplies no additional null vector or integrable release. Contact-isolate kernel directions do not move the diameter-carrying core. |
| Triangular-lattice averaging and source count | Linear non-rhombic area is not empty source area: its isolate population and interface guards must be retained. The leading $`D^2`$ density and an unspecified positive boundary cost do not give the needed exact capacity. |
| Local refill and inactive-chamber motion | A unit-rhombus face supplies no extra unit-clear interior site (canonical Section 67). Deep isolate contact creation can preserve the old diameter core and KKT polytope (proof-only Section 95). Neither operation establishes (3.1). |

For the deformation failure, use signed active rows $`\phi_e(u)\ge0`$
and a stress positive on all of them. Stationarity gives
$`\sum_e\lambda_e\phi_e(u)=0`$, so all $`\phi_e(u)=0`$. ZF then
restricts $`u|_V`$ to Euclidean rigid motions. This is an obstruction to
the attempted **first-order** motion, not a theorem against all finite
nonlocal replacements.

For the capacity failure, the missing assertion is simultaneous clearance
against every retained source point. None of the proven boundary moment,
symmetry, or defect inequalities supplies those coordinates. I have not
proved (3.1), and the non-global shell examples do not refute it under the
global-minimizer hypothesis. This is the unresolved theorem at which these
closing attempts stop.

## 5. Case tree and lifecycle

| Canonical case / route | State after this run |
| --- | --- |
| C-I | Canonically closed before the run. |
| C-II macroscopic inactive chamber / exterior cap | Open; core replacement plus full population refill still missing. |
| C-II full core with sublinear total local $`Z+Q`$ | Excluded by a proved candidate from this run, pending independent audit and promotion. |
| Exact rooted wrapping threshold $`\lambda_1`$ | Conditionally excluded using the unpromoted rooted stability input. |
| Positive-defect wrapping carrier, including diameter-one limits | Open; (3.1) or another exact strict source replacement remains. |
| Positive-defect two-half-disk groups | Open; the defining diameter-scale cells need not have quadratic area and cannot inherit group hypotheses. |
| Target A | Open at the canonical right-deficiency / Schur-nullity endpoint. |
| Target B | Open at the canonical joint outer-shell stability inequality. |

Targets A and B are alternate routes, not additional cases that a complete
C-II solution would separately have to prove. The theorem-state manifest
remains `2026-09-14.audit.51`; no new result is called canonical.

## 6. Verification and certificate correction

The new exact finite verifier passed 4,017 grid subsets, including 934
two-dimensional loaded hulls, and a rational non-star fan of degree 81.
It is a finite audit, not the universal proof, and includes no odd-cycle
example. The analytic regular-Reuleaux family supplies the large-degree
odd-cycle regression without numerics.

The historical half-disk scalar verifier contained two inadequate checks:
a remainder threshold was halved, and a train threshold used a lower bound
where an upper bound was needed. Both were repaired with rational Machin
bounds and positive squaring. The historical witness passes the corrected
system, but violates the newer shape-detour moment cap; its scope is now
explicit. It is not a witness for the complete current frontier.

`tools/check_theorem_state.py` and `git diff --check` pass at the checkpoints.
The first state check exposed missing metadata on eight inherited current-main
reports. Their generated unreviewed headers and index entries were repaired;
their mathematical text and theorem authority were not changed. The same
metadata repair was applied to the subsequently merged independent
contiguity report. The phase radical bound in the historical arithmetic
verifier was also explicitly certified by positive rational squaring.

## 7. Files changed in the run

New mathematical reports:

- `docs/reports/target_c_exact_diameter_star_contiguity_2026-09-30.md`
- `docs/reports/target_c_contiguous_star_incidence_concentration_regression_2026-09-30.md`
- `docs/reports/target_c_geodesic_train_boundary_four_face_obstruction_2026-09-30.md`
- `docs/reports/target_c_train_boundary_symmetry_defect_2026-09-30.md`
- `docs/reports/target_c_convex_geodesic_rhombus_limit_2026-09-30.md`
- `docs/reports/target_c_boundary_defect_to_source_refill_frontier_2026-09-30.md`

Computation and index:

- `docs/research/migration/2026-10-16/shards/01/support/research/verify_diameter_star_contiguity.py`
- `docs/research/migration/2026-10-16/shards/01/support/research/verify_target_c_two_halfdisk_scalar_regression.py`
- `docs/research/migration/2026-10-16/shards/01/support/research/target_c_two_halfdisk_scalar_regression_2026-09-12.md`
- `research/README.md`
- `docs/state/artifact-index.jsonl`

Generated metadata headers only:

- `docs/reports/target_c_convex_width_outer_detour_floor_2026-09-29.md`
- `docs/reports/target_c_global_outer_detour_upper_bound_2026-09-29.md`
- `docs/reports/target_c_global_diameter_star_contiguity_2026-09-30.md`
- `docs/reports/target_c_neardisk_chord_dissection_shape_detour_2026-09-29.md`
- `docs/reports/target_c_rooted_direction_reentry_defect_2026-09-30.md`
- `docs/reports/target_c_shape_detour_nearglobal_carrier_0988676_2026-09-29.md`
- `docs/reports/target_c_wrapping_endpoint_diameter_v_cover_2026-09-30.md`
- `docs/reports/target_c_wrapping_root_defect_stability_2026-09-30.md`
- `docs/reports/target_c_wrapping_rooted_detour_2026-09-30.md`

**Run disposition:** multiple structural, equality, deformation, stress, and
capacity approaches were pursued. The exact defect-to-refill bridge remains
unproved and unrefuted under its global hypotheses. The root problem is not
solved. All defensible milestones are preserved as noncanonical checkpoints.
