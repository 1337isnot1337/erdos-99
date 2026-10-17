## 2026-10-12 — full-source palette transversals and exact exhaustion

`python3 research/verify_global_palette_transversal_2026_10_12.py` certifies finite
planar endpoint choices by independent-transversal constraints. Exact directed
integer intervals build a sufficient system for positive certificates and a
permissive system for negative certificates; exhaustive Boolean propagation and
branching make the final decisions. A three-translation palette improves the
43-point locally rigid rim but is impossible on its full 175-label filling,
despite an independently verified alternative full-source packet. Every source
label, inactive pair and contact isolate is retained. Public decimal fixture
coordinates are exact rational input with checked hashes. No numerical
infeasibility, global optimality or eventual Level I conclusion is certified.
A separate unlabelled cloud of all 175 contracted old sites and 174 actual
triangular-lattice sites has exact packing capacity 174: one forbidden triangle
and 173 disjoint forbidden pairs partition every site. Its complete integer
certificate is checked independently of the discovery matching solver.
See the [report](../docs/reports/global_palette_endpoints_and_full_source_exhaustion_2026-10-12.md).

## 2026-10-12 — global colour lifting, rank barrier, planar endpoints

`python3 research/verify_global_colouring_lift_rank_2026_10_12.py` checks exact
full-source contact-preserving lifts, centred-Gram rank obstructions, and supplied
planar endpoints. Rational distances and exact SymPy ranks retain every label,
pair and isolate. With `--endpoint-json FILE`, it checks rational `source`,
`target` and `t` for `(source+t*target)/sqrt(1+t^2)`, without a feasible-path
premise. Lifted descent generally needs more than two dimensions. No global
optimality, source extraction or eventual Level I conclusion is certified.
See the [report](../docs/reports/global_colouring_lift_and_planar_rank_barrier_2026-10-12.md).

## Slot 2 salvage — Groemer face stability, low-t flat centers, and Oler gluing (2026-10-04)

The recovered unreviewed reports in `docs/reports/` preserve the all-degree Groemer residual fork, pair/triple near-contact matchings, low-t flat-center extraction/stress leakage, and the exact Oler gluing correction. Independent and hostile audits are included as source reports, but no recovered claim is canonical. Run the registered finite checks with:

```bash
python3 research/verify_target_c_all_degree_groemer_face_stability.py
python3 research/verify_target_c_groemer_pair_matching_refinement.py
python3 research/verify_target_c_anchored_groemer_triple_matching_refinement.py
python3 research/verify_target_c_oler_gluing_train_surplus.py
python3 research/verify_target_c_low_t_flat_center_amplification.py
python3 research/verify_target_c_flat_center_kkt_stress_leakage.py
```

# Reproducible research tools

## 2026-10-08 — full-source isolate normalization

`python3 research/verify_target_c_isolate_diameter_normalization_2026_10_07.py`
checks exact rational squared distances for simultaneous isolate contraction, including
84 pair-at-time checks in an eight-label fixture, two rejected hypotheses, the no-isolate
case, and a six-pair near-unit-slack edge case at the largest permitted contraction
parameter. It verifies these finite examples only; the centroid inequalities and
core-diameter replacement are proved analytically in
`docs/audits/target_c_isolate_normalization_independent_audit_2026-10-08.md`. It does not
certify a canonical source, endpoint existence, global optimality, the cubic-moment
candidate in the discovery report, or C-II closure.

## 2026-10-08 — finite radial-lifting stress audit

`python3 research/verify_target_c_sorting_radial_lifting_stress_2026_10_07.py`
reconstructs exact face-gradient jumps, positive weights on the triangulation's
unit edges, and equilibrium at every moving vertex for the 33 listed sorting
packets. Its scope is those exact orders at `tan(theta/2)=1/(200M^2)`; it does
not prove positivity for all M, all orders, or a curvature interval.

`python3 research/verify_target_c_radial_lifting_support_audit_2026_10_08.py`
additionally enumerates every actual source pair and confirms that the stress
support contains every unit contact incident to a moving vertex. Both scripts
use exact rational / quadratic-field arithmetic. These triangle-containing
finite packets are not canonical minimizers and give no global-optimality or
C-II conclusion. The independent disposition is in
`docs/audits/target_c_finite_radial_lifting_stress_independent_audit_2026-10-08.md`.

## 2026-10-08 — five-row capsule packing certificate

`python3 research/verify_target_c_unit_capsule_five_row_packing_2026_10_08.py`
certifies that a set with separation at least `sqrt(3)/2` in a stadium of
length at most `21/20` has at most five points. It uses a rational `1/24`
square cover, exact integer compatibility tests, and an exhaustive
branch-and-bound search proving that the compatibility graph has no `K_6`;
an exact rational five-point set shows sharpness at length one. This proves
only the finite capsule packing statement. The supplied crosscut-path
corollary additionally uses canonical rhombus geometry. Path extraction,
exact-swap population, Horn propagation, source motion, and global optimality
are not certified. The script's additional exact arithmetic checks on later
density coefficients do not verify their theorem premises. See
`docs/audits/target_c_five_row_capsule_packing_independent_audit_2026-10-08.md`.

## 2026-10-05 — complete face elimination and contact regularity

`python3 research/verify_target_c_complete_face_closure_elimination_2026_10_05.py`
supports the [universal face elimination candidate](../docs/reports/target_c_complete_face_elimination_and_contact_regularity_2026-10-05.md).
Exact pentagon/hexagon packets check source separations, positive pinned
equilibrium and full face/contact rank. Abstract `(2,2)` endpoint graphs
test complete elimination for mixed valences. An actual triangular wheel
checks positive KKT loads and pure contact corank one, preserving the
triangle-free hypothesis. Two exact pentagon target realizations check
the full stress-energy identity and both mean-to-maximum and vertex-
collision failures. Arithmetic is rational or quadratic-field exact.
No test proves a uniform chart radius, active diameter feasibility,
asymptotic source existence or a global strict competitor. Boundary pins
in the chart packets are not certified diameter loads.


## 2026-10-05 — arbitrarily large near-triangular fixed-wall lock

`python3 research/verify_target_c_large_near_triangular_wall_lock_2026_10_05.py`
supports the [large fixed-wall regression](../docs/reports/target_c_large_near_triangular_fixed_wall_lock_2026-10-05.md).
Exact arithmetic in `Q(sqrt(3))` checks near-triangular grids, all source
pairs, triangle-free contacts, positive pinned equilibrium, pinned rank,
Oler residuals and the displacement-bound coefficients. Integer and
rational checks verify the explicit capacity-optimal container family.
The analytic uniqueness window follows from the separately checked
Groemer equality theorem, compactness and a uniform finite displacement
gap. No sample angle is asserted to lie in that nonexplicit window.
Success does not certify an effective angle threshold, actual diameter
loading, a disk force hull or minimum-diameter optimality. Container
capacity optimality is distinct from the Level I problem.


## Target C pentagon-capped locked train-bank regression (2026-10-07 audit)

`verify_target_c_pentagon_capped_lock_2026_10_05.py` uses directed rational
interval arithmetic in `Q(sqrt(3),sqrt(5))` to check all source pairs,
contacts, strict noncontacts, cap spacing, triangle-freeness, Oler residual,
source/contact counts, and selected crossing cells for `M=24,30,36,32,40`.
Its run checks 3,921,688 pairs. The `M=32,40` cases also include finite
radial-leaf attachments; those checks are not part of the promoted theorem.
The all-`M` grid/train geometry, exact container-capacity calculation, and
no-surplus bound for arbitrary interior-disjoint contact-wall packets are
proved analytically in
`docs/audits/target_c_pentagon_capped_locked_train_bank_independent_audit_2026-10-07.md`.

The checker does not certify actual diameter loads, canonical KKT stress,
global optimality, a loaded-return realization, or C-II/Level I. It does not
verify the non-effective uniqueness-window or all-`M` radial-leaf variants.


## Target C paired exterior-cap nonglobal regression (2026-10-07 Audit.94)

`python3 research/verify_target_c_paired_cap_spoke_comparison_2026_10_06.py`
checks exact integer-distance geometry for the six-spoke triangular-lattice
source and the same-cardinality lattice-disk competitor. It verifies all
source and competitor pairs, contact and diameter graphs, triangle-freeness,
positive KKT equilibrium, isolate lower/upper margins, exact opposite-cap
area/population equality, and the guard-count injection. The five finite runs
pass 6,224,805 pair checks for each configuration. The `M=5,8,12` runs are
auxiliary; the promoted family is `M>=20`. The all-`M` support bound, cap-area
asymptotics, `O(D)` population/Oler allowance, depth-one isolate cover, and
strict smaller-diameter comparison are proved analytically in
`docs/audits/target_c_paired_cap_spoke_global_comparison_independent_audit_2026-10-07.md`.
The certificate does not establish canonical mixed rigidity, global optimality
of the source, antipodal-cap extraction in canonical minimizers, C-II closure,
or Level I.

`python3 research/verify_target_c_exterior_cap_separator_refill_2026_10_06.py`
checks the exact six-spoke source, moved-core two-site endpoint, and triangle-free
finite downward endpoint for `M=20,32`. It verifies every pair with integer
triangular-basis/radical arithmetic, the exact initial diameter, contact counts,
retention of every isolate, and the chosen finite opening step. It also checks
two local wall/rhombus regressions. These fixtures do not prove the all-`M`
analytic construction, canonical mixed rigidity, cap extraction, or global
optimality; the all-`M` inequalities and scope are in
`docs/audits/target_c_exterior_cap_moved_core_refill_independent_audit_2026-10-09.md`.


## 2026-10-05 — eliminate every pentagon closure core

`python3 research/verify_target_c_pentagon_closure_core_elimination_2026_10_05.py`
supports the [global pentagon elimination candidate](../docs/reports/target_c_all_pentagon_closure_core_elimination_2026-10-05.md).
Exact quadratic-field arithmetic verifies glued unit pentagons, every
source pair, strict hidden diagonals, nonparallel sides, positive unloaded
equilibrium, contact rank and face-closure rank. Exhaustive abstract
endpoint graphs up to six nodes check sparse cuts and complete two-anchor
orders, including fixed higher-face blocks. Boundary pins are not actual
diameter loads; abstract graphs need not have source embeddings. Success
certifies the finite geometry/matrix/combinatorial contracts. It does not
certify the analytic implicit-function theorem, a uniform chart radius,
stress activation, feasibility of active upper constraints or optimality.


## 2026-10-05 — terminal-wall-disjoint quadratic pentagon bulk

`python3 research/verify_target_c_pentagon_wall_disjoint_bulk_2026_10_05.py`
supports the [global wall-reuse candidate](../docs/reports/target_c_pentagon_terminal_wall_disjoint_quadratic_bulk_2026-10-05.md).
Exact rational Bernoulli enumeration checks bounded conflict degree,
joint retention probabilities and survival of counted crossing edges
with pairwise disjoint terminal-wall vertex supports. Abstract rosters
include repeated face pairs and two terminal occurrences on one face;
they are not contact packings. The script also checks the integer
arithmetic in the four-rhombus self-overlap cutoff. It does not certify
the analytic source projection, a loaded-return theorem, geometric
realizability, stress activation, a finite feasible motion or optimality.
The conditional Type-II application uses the personally checked
pentagon-pair occurrence argument and current-main #699 hull depletion.


## 2026-10-05 — positive reciprocal internal train graph

`python3 research/verify_target_c_reciprocal_internal_train_graph_2026_10_05.py`
supports the [positive reciprocal train candidate](../docs/reports/target_c_positive_reciprocal_internal_train_graph_2026-10-05.md).
Ten rational unit-separated positive-equilibrium packets check integration
on the actual bounded augmented-face dual, exact signed train masses,
matrix scaling to reciprocal bar rigidity, three row dependencies,
simplicity and componentwise `(2,3)` cuts. Arithmetic is rational and
all assertions are exact. Boundary pins are not certified diameter loads.
Success proves the finite identities encoded in these packets; it does
not prove global optimality, a Type-II sequence, a uniform stress lower
bound, route-length currency or source deformation. All hull pockets
retain their closure rows, including those with four sides.


## 2026-10-05 — loaded flat pentagon second depletion

`python3 research/verify_target_c_loaded_flat_pentagon_second_depletion_2026_10_05.py`
supports the [loaded-corner branch candidate](../docs/reports/target_c_loaded_flat_pentagon_second_depletion_2026-10-05.md).
Exact rational quadratic-field packets verify strict unit-separated
pentagons approaching the triangular trapezoid, convexity, all hidden
diagonals, positive residual and a complete interior cover by wall disks.
The two nearly parallel marked unit columns remain exactly independent.
Integer ledgers check the attachment/degree charge and simultaneous
second-depletion cancellation. An exact formal leading-coefficient ray
satisfies the old and new scalar banks, preventing an unsupported algebraic
closure claim. These ledgers and this ray are not source embeddings.

The theorem applies to canonical Type-II `x_B=o(D)` sequences and uses
actual loaded turning angles rather than small residual to select the
marked pentagons. Source bridges on pocket paths are discarded only from
the marked count, never from the configuration. Near-unit chords are not
activated. No global optimality, compactness, independent audit or Level I
closure is certified by the computation.


## 2026-10-05 — terminal short pockets and physical unit-wall frustration

`python3 research/verify_target_c_terminal_short_pocket_physical_frustration_2026_10_05.py`
supports the [terminal branch candidate](../docs/reports/target_c_terminal_short_pocket_physical_frustration_2026-10-05.md).
Exact rational two-step pockets check unit separation, chord convergence
to one, the phase derivative bound and positive vanishing pocket residual.
Integer ledgers check long-pocket node/terminal bounds and the exact
outer-train cancellation. These ledgers are not source embeddings.

The analytic theorem uses canonical mixed rigidity and personally checked
augmented rank: in terminal Type II with `u_B=o(D)`, all outer-ended trains
deplete, and a linear direction-frustration bank must lie on physical
unit-wall faces. Hull-pocket residual cannot replace that bank. The verifier
does not certify global optimality, compactness, capacity, force activation
or Level I closure. All source points, including isolates, remain accounted
for; there is no independent audit or canonical promotion.


## 2026-10-05 — loaded pentagon fixed-wall activation regression

`python3 research/verify_target_c_loaded_pentagon_wall_regression_2026_10_05.py`
supports the [finite regression](../docs/reports/target_c_phase_frustration_fixed_wall_activation_regression_2026-10-05.md).
Exact arithmetic in `Q(sqrt(5))` verifies all actual contact/diameter
distances, positive normalized equilibrium, the correct PSD circulant
stress with three affine modes, and strict covering-radius/residual
inequalities. The analytic covering proof shows that positive residual
and phase frustration give no fixed-wall spare point, and deleting any one
boundary vertex gives no inward vacancy with the other four fixed.

The source is a genuine five-point global minimizer by the original
Bateman--Erdos theorem, rechecked on printed page 307 of the local original
paper. Global optimality and the covering proof are not numerical outputs.
This is a finite regression, not a large-diameter Type-II source, unbounded
family or negative Level I settlement. It supports the correct C53 PSD
sign and does not revive the rejected orientation argument.


## 2026-10-05 — augmented train rank and small-residual full-core exclusion

`python3 research/verify_target_c_augmented_train_phase_rank_2026_10_05.py`
supports the [branch-exclusion and phase-frustration bank candidate](../docs/reports/target_c_augmented_train_phase_rank_small_residual_exclusion_2026-10-05.md).
Twelve rational unit-separated positive boundary-pinned sources check 5,436
source pairs, hull augmentation, one added hull side per pocket, and
independent internal angular columns with auxiliary vector displacement
fixed to zero. It checks 3,114 augmented node subsets, 128,685 exact
phase-bank ledgers, and 81 bins in abstract coloured double-tree graphs.
The scalar ledgers and coloured trees have no claimed source embedding.
An additional exact four-point polygon checks that a four-sided pocket
with a nonunit chord retains both angular closure rows; it is not treated
as a strict unit rhombus. That polygon alone has no claimed positive
stress or actual diameter loading.

The analytic result excludes all canonical full-core Type-II sequences with
`R_F=o(D)`, without any degree-tail or pocket-tail hypothesis. The same
rank estimate forces linearly many bounded-degree chambers with a fixed
reduced-phase mismatch and positive residual. The actual-source packets
have boundary pins that need not be strict hull vertices or actual diameter
endpoints. The script certifies finite contracts, not canonical-source
existence, optimality, Groemer compactness, phase coarea, or asymptotic
exclusion. It uses exact rational arithmetic and imports the preceding
source/rank helpers. Every isolate stays in the full source and residual;
no independent audit or canonical promotion is claimed.

`python3 research/verify_target_c_actual_loaded_augmented_star_2026_10_05.py`
adds an actual loaded-source check for the augmented-column lemma. It
verifies all fifteen pair constraints of the six-point regular pentagon
plus center, positive actual contact/diameter equilibrium, a PSD stress
with exactly three affine modes, the mixed-rigidity angular contract, and
independence of five augmented train columns. The source has five contact
bridges and no unit hull side; all 31 nonempty augmented node subsets pass.
Arithmetic is exact `Q(sqrt(5))`. Its finite global optimality is the
original Bateman--Erdos `D(6)` theorem, not a numerical certification.
There are no rhombi and the diameter is below nine, so no large-diameter
canonical Type-II hypothesis is certified.


## 2026-10-05 — global train phase access and integrable-tail branch exclusion

`python3 research/verify_target_c_global_phase_access_2026_10_05.py`
supports the [conditional branch-exclusion candidate](../docs/reports/target_c_global_phase_access_integrable_branch_exclusion_2026-10-05.md).
Ten rational unit-separated sources with one to eight convex exceptional
hexagons check 4,308 source pairs, all actual contacts, positive equilibrium
at every unpinned vertex, full pinned and contact ranks, determination by
outer train angles, and independent opposite-sign internal train columns.
All 594 nonempty exceptional-face subsets satisfy the exact outward-cut
inequality. Abstract double-tree multigraphs check 8,338 cuts and distance
layers, including parallel edges and depth seven. Those abstract graphs
are not asserted to embed as source configurations.

The analytic exclusion assumes a canonical full-core Type-II sequence,
`R_F=o(D)`, and uniformly integrable physical exceptional-face degrees and
outer-pocket occurrence lengths. Source pins in the finite packets lie on
the hull boundary but need not be strict extreme vertices or actual diameter
endpoints. The computation verifies finite contracts, not optimality,
uniform integrability, Groemer compactness, phase coarea, or the asymptotic
branch exclusion itself. All arithmetic is exact rational arithmetic;
isolates stay outside the core matrices and in the source residual.
No independent audit or canonical promotion is claimed.


## 2026-10-05 — outer-train determination and marked-face bank synthesis

`python3 research/verify_target_c_outer_train_rank_groemer_bank_2026_10_05.py`
supports the [finite rank and conditional synthesis candidate](../docs/reports/target_c_outer_train_rank_groemer_bank_synthesis_2026-10-05.md).
Ten rational, unit-separated sources have one former grid contact now
strictly longer than one and a convex hexagonal face. It checks 2,316 source pairs, every
actual contact, triangle-freeness, positive pinned equilibrium, full pinned
rank, train decomposition, determination by outer train rates, and a sharp
two-column marked-face rank payment. It also checks 13,500 exact scalar
cancellations of the nonunit-hull term, including both possible double-good
end corrections. Those scalar packets have no asserted source realization.

The assigned pins include collinear boundary vertices and need not be actual
diameter endpoints. These finite sources certify the angular/pinned contract;
they do not certify canonical-source existence, optimality, the asymptotic
residual/tail hypotheses, phase depletion, activation, or a strict competitor.
Arithmetic is `Fraction`; the script imports the existing exact graph/rank
helpers. Isolates remain outside the core matrices and stay in the source.
No canonical promotion or certificate registration is made.


## 2026-10-05 — outer-pocket Groemer phase depletion

`python3 research/verify_target_c_outer_pocket_phase_depletion_2026_10_05.py`
supports the [conditional second-depletion theorem](../docs/reports/target_c_outer_pocket_groemer_phase_depletion_2026-10-05.md).
It checks eighteen rational three-point pockets with exact unit path edges,
strict noncontact chords, and certified residual/direction convergence;
a positive-residual phase mismatch; 44,624 terminal/payment tables; 22,499
integer Mantel consequences; and 1,000 anchor/occurrence multiplicity tables.
It also checks 59,048 tables with marked bounded-face ends, the stronger
second-depletion charge, and the exact remaining-face perimeter identity.
It uses `Fraction`, integer square roots, and no external dependencies.

The analytic proof assumes a canonical full-core Type-II sequence, total
fixed-boundary residual (R_F=o(D)), and uniformly integrable outer-pocket
occurrence lengths. Its finite packets do not certify those hypotheses,
source optimality, compactness, phase coarea, contact activation, or a strict
competitor. Positive output certifies only the stated finite geometry and
counting. Every source isolate stays accounted for; no theorem-state
promotion or canonical certificate registration is made.


## 2026-10-05 — joint bulk/face separator capacity and spatial exclusion

`python3 research/verify_target_c_joint_bulk_separator_2026_10_05.py`
supports the [joint capacity/spatial exclusion candidate](../docs/reports/target_c_joint_bulk_defect_separator_capacity_2026-10-05.md).
It checks twelve finite unit-grid separators, including nonminimal punctures
and a selected bulk of 729 rhombi, the exact Euler/perimeter budget, 1,001
annular packing bounds, and certified rational intervals for pi and sqrt(3).
It imports the first quota verifier's graph and integral-flow helpers.

The unit grids have positive unloaded equilibrium and full pinned bar rank;
their boundary pins are not all actual diameter endpoints. Positive output
checks the finite physical-perimeter and deletion bounds. It does not prove
canonical-source existence, the analytic theorem, the Type-II asymptotics,
the face-group flow theorem, global optimality, or Level I closure. Arithmetic
is integer and `Fraction`; no external dependencies or numerical solver are
used. The analytic argument retains every source isolate. No certificate
registration or canonical promotion is made.


## 2026-10-04 — global exceptional-face return quotas

`python3 research/verify_target_c_global_face_return_quotas_2026_10_04.py`
supports the [candidate proof](../docs/reports/target_c_global_exceptional_face_return_quotas_2026-10-04.md).
It checks 153,600 exact integer Euler/outer-occurrence/auxiliary-triangle
cancellations and ten rational plane-framework face-family/separator packets,
including fourteen simultaneous face demands and three packets with two
triangular faces per auxiliary chord. Each framework has exact positive
unloaded equilibrium, full pinned bar rank, strictly convex rational pins,
and verified noncrossing edges. Arithmetic is `Fraction` and integral flow;
there are no external dependencies.

The framework bars have arbitrary lengths. Unit separation, actual diameter
loading, global optimality, and canonical-source existence are omitted.
Positive output certifies the finite identities, prerequisite rank/equilibrium,
tested exposure inequalities, and tested face-labelled flow demands. The
analytic proof establishes the general quota theorem; the packets do not
prove it or C-II/Level I closure. All source isolates are outside this graph
analysis and are not deleted from a packing. No certificate registration or
canonical promotion is made.



## 2026-10-05 — recovered weighted-cover stress-concentration candidates

These six proof-only reports come from `research/weighted-cover-stress-concentration-2026-10-02` at exact tip `ab10eeda2bc16a36daacd54be7cb2cbfdeb1fe1f`. Together they record the KKT implication `alpha_max >= (sqrt(3)/6) D/(nu+1)`, the projective star-interval deficit and low-detour square-root branch, density-sensitive diameter matching, a linear actual-contact collar under leaf saturation, good-side normal-cone slack, and the balanced square-root leaf-carrier alternative. Every report remains unreviewed and noncanonical; no standalone verifier or computational certificate is claimed.

- [`target_c_weighted_cover_stress_concentration_2026-10-02.md`](target_c_weighted_cover_stress_concentration_2026-10-02.md)
- [`target_c_projective_star_tiling_2026-10-02.md`](target_c_projective_star_tiling_2026-10-02.md)
- [`target_c_density_sensitive_sqrt_braid_2026-10-02.md`](target_c_density_sensitive_sqrt_braid_2026-10-02.md)
- [`target_c_diameter_leaf_contact_collar_2026-10-02.md`](target_c_diameter_leaf_contact_collar_2026-10-02.md)
- [`target_c_good_side_normal_cone_slack_2026-10-02.md`](target_c_good_side_normal_cone_slack_2026-10-02.md)
- [`target_c_balanced_sqrt_leaf_carrier_sea_2026-10-02.md`](target_c_balanced_sqrt_leaf_carrier_sea_2026-10-02.md)

The individual scopes and limits are stated in each report. No theorem-state or Target C route file changes.

## 2026-10-02 — finite rotation cell barriers

`python3 research/verify_target_c_translation_lens_exposure_2026_10_02.py`
checks finite translation lens domination and strictness on 105 rational actual
four-point sources and 93 sampled old-upper-feasible endpoints. It also checks
five actual unit-cut rotation packets whose sole upper blocker is an unexposed,
nonisolated source vertex, and a contact-preserving collision packet. It supports
`docs/reports/target_c_finite_translation_lens_exposure_2026-10-02.md`.

Arithmetic is exact `Fraction`; the script imports basic pair/graph helpers from
`verify_target_c_rotation_cell_barriers_2026_10_02.py`. The lens census certifies
upper constraints and conditional strictness, not lower feasibility. The
uncovered packets check every old/new pair and preserve every old contact; they
fail positive full KKT and global optimality and are not actual complete O--O
extractions. The analytic packet-hull and cut-force results assume positive
contact equilibrium and retain isolates. Finite output is not a Level I proof
or a canonical-source existence certificate.

`python3 research/verify_target_c_rotation_cell_barriers_2026_10_02.py`
certifies five rational actual-source rotation packets, five equality packets
for the disjoint diameter-angle bound, and five rectangles whose two near-
diameter cross pairs each retain squared deficit one. It checks all old/new pair constraints,
old/new contact and diameter graphs, triangle-freeness, the exact contact cut,
both sides of a finite angular wall, and explicit same-cardinality strict
square-grid competitors. It supports
`docs/reports/target_c_finite_rotation_cell_barriers_2026-10-02.md`.

Arithmetic is exact `Fraction`. Positive output certifies the stated finite
regressions and identities, not global optimality. Full positive KKT, PSD,
actual complete O--O train extraction, a linear transverse shore, and quadratic
source population are omitted. The analytic report proves the finite erosion
localization theorem and eventual sharpness family separately; finite checks do
not prove those universal statements. No canonical promotion is made.

## 2026-10-02 — collinear punctures and diameter crossflow

The [proof report](../docs/reports/target_c_collinear_punctures_and_diameter_crossflow_2026-10-02.md)
proves the exact principal-kernel restriction, connectedness of the actual mixed
core after arbitrarily many collinear source punctures, a sharp actual diameter
incidence budget for arbitrary contact islands, and a signed diameter
crossflow identity for a contact island with the stated line pins. Canonical
star-degree control excludes quadratic islands behind sublinear interfaces
with bounded star covers. Its spectral
mass bound has no uniform multiplier floor. An unbounded equilateral Reuleaux
family disproves the curved-separator extension under the matrix/rigidity
hypotheses; explicit same-cardinality competitors prove every member nonglobal.
Run `python3 research/verify_target_c_collinear_punctures_2026_10_02.py`.
The verifier uses exact SymPy arithmetic for the six-point family member,
checks all distances and actual supports, full positive equilibrium,
grounded positivity/zero Schur complement, affine kernel, mixed rank,
all principal-kernel restrictions, collinear and curved punctures,
every eligible finite physical island budget and its sharpness counts, and
186 signed cut identities. Rational arithmetic checks all-family competitor
margins. Encoded hypotheses omit global minimality, quadratic population,
large-source roundness, actual train-seam extraction, and a uniform spectral
gap. Positive output certifies the finite algebra/regression and arithmetic,
not the general analytic theorems, a C-II closure, or Level I. The report
provides those general proofs and records the failed exact-phase co-embedding
and circular-seam attacks. Classification: proved candidates awaiting audit;
artifact lifecycle unreviewed.

## October 2 bulk midpoint concentration and centered actual braids

`python3 research/verify_midpoint_bulk_braid_2026_10_02.py` checks the finite
arithmetic in `docs/reports/target_c_midpoint_bulk_braid_2026-10-02.md` using
integer and `Fraction` arithmetic. It checks 256 Fourier coefficient ratios,
rational actual-diameter/projective-gap packets, all 448 subgraphs of the listed
forest and odd-unicyclic graphs, and 123 independent Lipschitz sampling cells.
For k=101,105,201 it certifies the smooth constant-width regression's exact
normal-index counts, strict unit-separation lower bound, square-root midpoint
lower bound, linear hull area deficit, constant inradius loss, and a quadratic
scaled-lattice population lower bound. Bounds `3<pi<22/7` and a sine polynomial
are used without floating trigonometry. The complete-source regression has no
contacts and is explicitly nonglobal by uniform scaling. The script omits a
canonical KKT stress, actual train extraction, and the conditional upper bound
on stress atoms. Successful output certifies the stated finite certificates,
not the infinite analytic theorem, global optimality, C-II closure, or Level I.

## October 2 simultaneous fan reflections and inactive blocker matching

`python3 research/verify_centered_fan_reflections_2026_10_02.py` certifies the
finite packets in `docs/reports/target_c_centered_fan_simultaneous_reflections_2026-10-02.md`
over the exact quadratic field `Q(sqrt(4D^2-1))`, D=100. It enumerates all 166
old/joint pairs in three full sources and checks the actual unit graph, actual
diameter graph, independent fan leaves, preserved old contacts, simultaneous
nonexpansiveness, safe moving-moving pairs, and equality of solo/joint lower
failure labels. It certifies one isolated-blocker repair and the failure of
moving only that blocker when a second isolate is added; a joint two-isolate
translation is checked as a finite repaired example. A smaller integer grid
proves every packet nonglobal. KKT support/PSD, canonical fan extraction,
general inactive-blocker repair, and Level I closure are omitted. The analytic
injective-blocker theorem and `ceil(2U/5)` canonical matching have full proofs
in the report; finite checks do not promote them.

## 2026-10-02 — actual embedded-grain wall replacement

Run `python3 research/verify_target_c_embedded_grain_replacement_2026_10_02.py`.
The [report](../docs/reports/target_c_embedded_grain_wall_replacement_2026-10-02.md)
proves simultaneous full-source wall shielding, contact-minimality replacement,
and actual diameter-cover refill for consecutive embedded rhombic patches.
The verifier uses exact `Fraction` arithmetic in `Q(sqrt(3))`. It encodes a real
seven-face square wall, 38 strict interior packing sites replacing 36 old points,
all finite distance guards, the 112-to-28 contact reduction, a real cover/refill
competitor with diameter squared 98-to-85, and adjacent-patch compatibility on a
120-point source. It also checks four rational oblique area thresholds, two-face
fixed-wall boundary packets, two rational near-square perturbations, and a
geometric marked-Hall count regression. The same packet tolerates a uniform
`1/50` Euclidean perturbation of the actual unit-contact square mesh, so the
source exclusion also covers the explicitly bounded nonconstant-phase case.
The universal proofs are in the report. The script omits global optimality,
KKT stress, arbitrary retained-grid extraction, inverse-diameter phase closure,
and packing upper bounds. Passing does not promote the candidates or close C-II.

## 2026-10-02 — deep-isolate octagon-flip regression

`verify_target_c_deep_isolate_octagon_flip_2026_10_02.py` uses exact `Fraction`
arithmetic to check a rational 13-point family, its connected contact core, actual
diameter pairs and loaded hull, a finite contact-preserving core move, and the
three-contact weak isolate repairs. It now also checks three exact
`Q(sqrt(3))` degree-five contact stars with a contact-isolated near-neighbor and
positive equilibrium at the center, but no exact unit triangle. The report proves
that within a fixed half-unit neighborhood no isolate placement is strictly
separated from every moved core point.
This is a regression only against deriving a small strict isolate repair from deep
upper-distance slack and core connectivity. The family fails canonical local
trapping at four nonloaded core vertices and does not certify a global minimizer;
the global O-O cut and Level I conclusions remain open.

The unreviewed [complete-grid collar and stress-shell report](../docs/reports/target_c_complete_grid_collar_and_stress_shell_2026-10-02.md)
contains analytical geometry and an explicit nonglobal stress-shell construction.
Its source branch named a companion exact verifier that was absent; the available
ball-hull and midpoint verifiers do not certify that report's new grid and shell
claims. No executable certificate is claimed for them.
## 2026-10-04 — Target A connected-shield tube refinement

The [five-site one-ended tube candidate](target_a_five_per_added_edge_unit_tube_2026-10-03.md)
proves that an attached unit edge adds at most five triangular-lattice sites to the
open unit tube once its shared endpoint's unit disk has already been covered. Its
exact integer verifier,
`python3 research/verify_target_a_five_per_added_edge_unit_tube_2026_10_03.py`,
checks the 19-site radius-two lattice ball, 54 anchored six-site candidates, and three
translation/dihedral orbits; the report gives the analytic exclusions of those three
orbits. The companion
[locked-triangle fan note](target_a_locked_triangle_fan_tube_2026-10-03.md) applies
the candidate to improve the deterministic Section-175 full-tube payment to `5v-6`
for that locked fan. These are noncanonical research candidates: they do not prove
the missing source/response surplus or close Target A, and the verifier does not
certify global minimum-diameter optimality.

## 2026-10-02 — full-source midpoint energy

The [proof report](../docs/reports/target_c_full_source_midpoint_energy_2026-10-02.md)
derives actual-diameter midpoint localization `O(D^(2/3))`, uniform coordinate
response error `O(D^(-1/3))`, and reciprocal-force deficit `O(D^(1/3))` from
the canonical complete-source area allowance. It retains all source points.
Run `python3 research/verify_full_source_midpoint_energy_2026_10_02.py`.
The script uses exact rational/integer polynomial arithmetic for finite Fourier
and tent identities, explicit constants, support-bump integrals and scales,
midpoint/variance identities, and odd-shell spectral parity. It corroborates
those finite reductions. It does not prove completion existence, general
support/convex geometry, infinite Fourier passages, the boundary-net construction,
source global optimality, finite motion feasibility, C-II, or Level I. The report
supplies analytic proofs and separates its nonglobal regressions. Classification:
proved candidates awaiting independent audit; artifact lifecycle unreviewed.


## 2026-09-22 — bounded Profile-B orbit-100 lift subcensus

`target_c_profile_b_partial_orbit100_global_lift_audit_2026-09-22.md` records an
exact bounded computation on the first 100 of the 20,451 `S_7` five-row orbit
representatives. The synchronized six-row Profile-B cover leaves 502 candidates
after its full-puncture/common-basis filters; the first 20 exact two-row global
lift attempts all fail before the seven-row full-span-eight stage. This is only a
partial finite subcensus and does not close Profile B or C-II. Reproduce the
subcensus with the verifier command in that note.

## 2026-09-22 — mixed-area oblique-lattice competitor

`target_c_oblique_lattice_mixed_area_competitor_2026-09-22.md` proves a restricted
finite source-level refinement of `C-OBLIQUE-LATTICE-COMPETITOR`.  For a finite
full-dimensional subset of one unit oblique lattice, the fundamental-cell Minkowski
sum has area at most `pi D^2/4 + 2D + sin(theta)`.  Combining this with the canonical
strict `D(n)^2 < (2 sqrt(3)/pi)(n-1)` bound gives the exact necessary condition
`(sin(theta)-sqrt(3)/2)D <= 4 sqrt(3)/pi` for an affine-lattice global minimizer.
The accompanying arithmetic check is
`verify_target_c_oblique_lattice_mixed_area_competitor_2026_09_22.py`.
This is a proved candidate awaiting independent audit; it leaves inverse-diameter
shear, general C-II sources, and Level I open.

## 2026-09-22 — five distinct persistent bars flatten by arithmetic

[`verify_target_b_five_bar_arithmetic_2026_09_22.py`](verify_target_b_five_bar_arithmetic_2026_09_22.py)
supports the [F5 candidate](../docs/reports/target_b_five_bar_arithmetic_flattening_2026-09-22.md).
With a balance positive on every persistent bar and at most five pairwise distinct
rotation functionals, the phase matrix is zero and all persistent diameters are
exactly flat on the backward-kernel slice. The verifier exhausts all 1024 forward
graphs, certifies the six-member support cover and rational-weight witnesses,
checks mod-16 / mod-9 descent obstructions and finite-field counts, and verifies
the geometric-to-elliptic substitutions. Run
`python3 research/verify_target_b_five_bar_arithmetic_2026_09_22.py` (SymPy required).
Completeness uses the report's source reduction and explicitly checked standard
2-isogeny descent / torsion-injection theorems, not a bounded rational-point
search. Repeated rotation classes, unsupported bars, larger supports, flat
families, and non-disk topology are not excluded. Claim: proved candidate awaiting
promotion, not canonical; no Level I or route status changes.

## 2026-09-21 — sharp tangent cubic capacity and three-bar flattening

[`verify_target_b_tangent_cubic_capacity_2026_09_21.py`](verify_target_b_tangent_cubic_capacity_2026_09_21.py)
supports the [Target B candidate](../docs/reports/target_b_tangent_cubic_capacity_2026-09-21.md).
The report proves `rank(A_h)<=floor(m_h/2)` for linear cubic-flat relative-tangent
images, classifies even-support equality, and proves a strict diameter descent
when the two persistent equality bars have nonzero coprime cubic moments.
It also proves the joint bound `rank(A_1,A_2)<=floor((m_1+m_2)/2)` for two
persistent nonzero cubics, including correlated ones, with parity refinements;
exceeding this capacity forces a finite strict diameter descent.
The stronger source-specific theorem PF proves that for `D>1`, exactly two
persistent equality bars are both exactly constant on every backward-kernel
train line. Thus neither a cubic nor a quartic blocker survives in this case.
A diameter-pair-minimal source then has no other active diameter bars. The proof
uses curved train paths and canonical tangent transfer, and explicitly handles
zero-gradient bars; it does not discard unsupported equality bars in larger sets.
For any number of persistent bars with a strictly positive balance on all of
them, AP proves exact flatness when their distinct rotation functionals are
affinely independent. Every nonflat bar forces a bounded integer affine relation,
with coefficient `l1` norm at most twice its tangent support / boundary detour.
For three fully supported persistent bars, TQ first reduces the obstruction to
a single midpoint quartic coordinate. The phase-group gradient balance PG then
eliminates that form entirely: TF proves that all three bars are exactly flat.
This does not discard unsupported equality bars, eliminate same-diameter flat
families, or close the four-or-more-bar / non-disk cases.
FF additionally eliminates four fully supported bars with four distinct rotation
functionals: the required five-edge transfer pattern contradicts planar weighted
diameter projections. The four-bar multiplicity pattern `(2,1,1)` is not excluded.
The script checks the signed Taylor expansion, paired equality models, an exact
nonpaired five-coordinate extremizer over `Q(sqrt(5))`, and all 625 / 19683
integer graph charts in its stated dimension-two / dimension-three boxes.
Run `python3 research/verify_target_b_tangent_cubic_capacity_2026_09_21.py`.
It requires SymPy and uses exact symbolic/integer arithmetic. Passing certifies
these finite identities and enumerations, not the general theorem (proved in the
report), a geometric realization of the algebraic examples, or global optimality.
The sharp bound is on a linear image modulo motions invisible to the bar, not
on an arbitrary nonlinear cubic zero set. Claims await independent promotion.

## 2026-09-22 — Direct source cover for Profile B

The [marked-triangle source cover](target_c_profile_b_direct_source_cover_2026-09-22.md)
enumerates every two-template rank-two coefficient plane and eight-cycle
support set compatible with the inherited minimum coefficient weight four.
Among 47,007 source instances with virtual deficiency three, none has nine
compatible singleton replacements. This closes the auxiliary eight-row
`k=6,D=-1,p=9` Profile B source case as a proved candidate awaiting promotion;
it does not close the other rank-density cases or C-II. Run
`python3 research/verify_target_c_profile_b_template_cover_2026_09_22.py --require-no-survivors`.
The checker combines exact integer local containment with prime-field complete
row ranks certified over `Q` by Hadamard, and checks the nine template-pair
orbits and visited-subset count independently. The companion capacity-ten
regression is an exact six-row state and is not an eight-row lift.

## 2026-10-02 — global convex-bank defect candidate and PR #609 audit

Proof and scope: [global convex-bank report](../docs/reports/target_c_global_convex_bank_defect_audit_2026-10-02.md).

Run `python3 research/verify_global_convex_bank_defect_2026_10_02.py`.
The exact verifier enumerates every simple triangle-free tripartite graph
whose three part sizes are at most two, checks the unrestricted lemma's
finite instances and sharp cases, certifies the cubic-capacity rational
coefficient and the `1/26000` area margin, and checks a positive-defect
scalar survivor. Arithmetic is integer/`Fraction`; the pi bounds use
Machin's identity and alternating rational arctangent series.

The encoded hypotheses omit Euclidean geometry, positive equilibrium,
bank topology, phase inheritance, asymptotic limits and global optimality.
A pass certifies only the finite graph instances and rational arithmetic.
It does not prove the geometric bridge, C-II or Level I. The report supplies
the human all-cell proof of the candidate necessary inequality for the
actual induced-face `Q_D` and route excess `Z_D`, including
`liminf (Z_D+Q_D)/D >= 1/26000` in the canonical full-core near-disk branch.
No theorem promotion is requested.

## 2026-10-02 -- finite subset reflections and a nonconstant signed-gap regression

The [subset-reflection report](../docs/reports/target_c_subset_reflection_gap_obstruction_2026-10-02.md)
proves an exact fixed-exterior contact motion beyond phase permutations. Reflecting
`k` selected directions across their vector sum preserves all old contacts; for
`D>=k-1`, every changed old diameter has its full finite work sign. It also
classifies all fixed-exterior layer translations along one axis, and proves that a
strongly connected signed gap graph forces TWO-SIGN for every nonzero such reflection.

Run `python3 research/verify_target_c_subset_reflections_2026_10_02.py`.
The verifier uses exact rational arithmetic and checks 1,279 original source pairs,
474 reflected subsets, 6,916 full diameter-sign comparisons, assigned positive cut
resultants, derivative rank, strong connectivity, and a three-cut reflection with
three fresh phase values. All subsets of size at least two are checked for `m<=8`;
four selected subsets are checked at `m=12,16`.
The additional five-point ONE-SIGN packet has connected but not strongly connected
gap support, positive assigned cut balances and full rank; its swap shortens one
old diameter, leaves three unchanged, and has no inactive blocker. It explicitly
fails actual source KKT and global/secondary optimality. Strong connectivity also
forbids every nonconstant layer translation along the same axis, at any amplitude,
even when old contacts are allowed to open.

Encoded hypotheses: actual rational diameter-star geometry and unit separation,
ordered layer labels, an empty direction cell, positive **aggregate** cut weights,
the restricted cut quadratic bound, and exact reflection identities.
Omitted hypotheses: actual unit-contact cutsets, vertex KKT equilibrium, the full
source stress, complete transverse trains, near-disk/quadratic population, and global
optimality. The regression has no unit contacts and is explicitly beaten by a unit
line. Positive output certifies this finite regression and the algebraic checks;
it does not prove a canonical source exists or settle C-II or Level I. The universal
reflection and sign theorems have analytic proofs in the report.
## 2026-09-14 — q-k bootstrap forces exceptional chambers

`target_c_qk_bootstrap_exceptional_chambers_2026-09-14.md` composes AG42 with the §171 `q-k` floor. It proves `f/D >= 0.1671246434...`, so full-core survivors have linearly many actual bounded nonquadrilateral contact faces, and bootstraps the all-train endpoint defect to `J_D/D >= 2.4893872118...`. Consequences include `(m-R_4)/D >= 2.3176124903...`, chamber packing surplus `>=0.6467617695...D`, total chamber perimeter `>=2.4893872118...D`, and chamber Oler-slack sum `>=2.1586344129...D`. The note identifies additive Oler-slack gluing/internal-boundary cancellation as a concrete closure target.

## 2026-09-14 — correlated interface/population consequences

`target_c_correlated_interface_population_2026-09-14.md` propagates the sharpened correlated all-train endpoint floor into canonical Sections 85 and 77. It proves, at proof-only scope, `liminf (m-R_4)/D >= 2.2147969788...`, chamber packing surplus at least `0.5577209247... D`, total inactive-chamber perimeter at least `2.1466688402... D`, chamber Oler-slack sum at least `1.7173350722... D`, and an absolute rhombus-count deficit at least `0.6440006520... D`. The note explicitly rejects the invalid comparison of the local chamber-slack sum with the single full-hull Oler slack; internal chamber perimeter must first be paid or cancelled.

## 2026-09-14 — AG42 refinement of the §171 orbit/detour floor

The [AG42/§171 refinement](target_c_orbit_detour_gap_00042_refinement_2026-09-14.md)
feeds the proof-only `eta_grid=0.00042` train gap into the audited §171 orbit/detour
scalar reduction.  An outward `Fraction` certificate gives the safe all-Type-II floor
`liminf (q-k)/D >= C146+0.0013751 > 1.82088863795`; the unchanged scalar envelope has
its first zero near `C146+0.001375190517836`.  The gain over audited §171 is small and
does not reach the separate `1.8585` endpoint/common-cap barrier.  This is a proved
candidate awaiting independent audit; C-II remains open.

## 2026-09-14 — safe 0.00042 atomic-grid refinement

The [0.00042 atomic-grid refinement](target_c_atomic_gap_00042_refinement_2026-09-14.md)
runs the audited §168 robust-grid bookkeeping at `eta_grid=0.00042`.  An exact
`Fraction` certificate verifies the final opposite-corner inequality and the inherited
triple-neighbor threshold.  This raises the proof-only rhombic-train gap to
`liminf sigma_R/D >= 0.00084`, the rhombic Mantel deficit to more than
`0.0004 D^2`, and the direct post-endpoint `mu_D` gain to `0.000084`.  The displayed
§168 bookkeeping fails near `eta=0.00042060689556...`, so `0.00042` is a safe round
endpoint for the current proof rather than an arbitrary decimal.  Run
`verify_target_c_atomic_gap_00042_exact.py` and `verify_target_c_atomic_gap_00042.py`.
This is a proved candidate awaiting independent audit; C-II remains open.

## 2026-09-14 — correlated stopped-train surplus

The [correlated train-surplus note](target_c_correlated_train_surplus_2026-09-14.md) now composes the proof-only `eta_grid=0.00042` refinement with the exact singleton/rhombic split.  It proves `(rho_rec+sigma_R-q)/D >= 0.00084-o(1)`, forces total train currency at least `1.4790102664...D`, raises the proof-only full-core floor to `liminf mu_D >= 1.785463210824532...`, and gives a sharp two-way branch: at least `0.3697525...D` singleton trains or rhombic slack at least `0.7395051...D`.  Preserving the full endpoint handshake also yields the stronger geometric floor `((b-P_F)+(Q+4f))/D >= 2.1466688402...`.  Run `verify_target_c_correlated_train_surplus.py` for arithmetic/bookkeeping checks.  These strengthened constants inherit the AG42 awaiting-audit status; C-II remains open.

## 2026-09-14 — independent audit of the explicit rhombic-train gap

The [independent audit](../docs/audits/target_c_explicit_rhombic_train_gap_independent_audit_2026-09-14.md) passes the `0.0008 D` rhombic-train boundary gap and the `0.0003809651227... D^2` rhombic Mantel-deficit floor at proof-only scope. It makes one binding notation repair: audited §142 uses `T` for all stopped trains, whereas `B_4/2` counts only non-singleton rhombic trains and must be written `T_R`. With `S` singleton trains, `T=T_R+S` and `b+4f+Q-B_4=2S` exactly. The audit verifies that §§168.1--168.4 restrict to the rhombic-only graph without using the exposed-hull step. C-II remains open.

## 2026-10-04 — conditional phase-deficit/Mantel transfer

The [phase-deficit transfer note](target_b_phase_deficit_mantel_transfer_2026-10-03.md)
proves an exact one-grain identity linking the phase deficit `Delta` to ordinary
Mantel slack, and gives conditional multi-grain train-population and concentration
inequalities when a retained grain family, positive deficit, high-mass branch, and
leading crossing-mass limit are supplied. The note does not prove those inputs,
the unpromoted 79% concentration transition, or the global Target B closure.
Classification: conditional algebra; noncanonical.

## 2026-09-14 — explicit rhombic-train Mantel gap

The [explicit rhombic-train gap](target_c_explicit_rhombic_train_gap_2026-09-14.md)
re-runs the audited §§166/168 atomic robust-grid argument on the non-singleton
rhombic train graph alone.  Because the exposed-hull step is not used in the atomic
gain, it yields `liminf T_R/D >= 2*sqrt(Delta_2)+0.0004`, hence the explicit
`liminf (B_4-4*sqrt(R_4))/D >= 0.0008` and rhombic Mantel-deficit floor
`M_R/D^2 >= 0.0003809651227...`.  It also identifies the old recipient vacancy
exactly as twice the singleton stopped-train population and upgrades the proof-only
post-endpoint scalar floor by `0.00008`.  Run
`verify_target_c_explicit_rhombic_train_gap.py` for arithmetic/bookkeeping checks.
C-II remains open.

## 2026-09-14 — exclusion of sublinear train-isoperimetric slack

The [sublinear train-slack exclusion](target_c_sublinear_train_slack_exclusion_2026-09-14.md)
observes that `sigma_D=o(D)` by itself reproduces every train-level hypothesis used by
the canonical exact-floor endpoint contradiction: `T/D -> 2*sqrt(Delta_2)` and
Mantel deficit `o(D^2)`.  Reusing the audited phase-label allocation, unbalanced
pseudosegment completion, chain-graph orientation cleanup, phase-tail trim, and
Section-76 source-hull inequality gives a contradiction.  Hence every sufficiently
large canonical full-core survivor has a non-explicit uniform `sigma_D>=epsilon*D`,
and therefore a quadratic Mantel deficit `M_D>=c*D^2`.  Run
`verify_target_c_sublinear_train_slack.py` for the non-load-bearing constant and
rationalization checks.  This is a proved candidate awaiting independent audit; C-II
remains open.

## 2026-09-14 — post-endpoint train-slack resolution

The [train-slack resolution](target_c_post_endpoint_train_slack_resolution_2026-09-14.md)
splits the post-endpoint train currency exactly into recipient-capacity waste
`rho_D=b+4f+Q-B_4` and train-isoperimetric slack
`sigma_D=B_4-4*sqrt(R_4)`.  With `T=B_4/2` and Mantel deficit
`M_D=T^2/4-R_4`, the latter satisfies the exact identity
`sigma_D=8*M_D/(T+2*sqrt(R_4))`.  Hence linear `sigma_D` forces a quadratic
Mantel deficit, while `sigma_D=o(D)` forces one rhombic component to contain
`T-o(D)` trains and `R_4-o(D^2)` rhombi and makes the full train graph
near-Mantel.  This extends the earlier Mantel structure beyond the excluded exact
`mu_TC` endpoint.  Run `verify_target_c_post_endpoint_train_slack.py` for the
finite algebra/component regressions.  This is proof-only; C-II remains open.

## 2026-09-13 — integer hull-route defect

The [integer hull-route reduction](target_c_integer_hull_route_defect_2026-09-13.md)
splits the exact Type-II outer correction into integer route surplus and one-sided
side-length rounding.  It proves `u_B >= sum_{s_i>1}(s_i-2)_+` and
`u_B >= (per(F)-q-m)_+`, together with the termwise bound
`0 <= u_B-sum_{s_i>1}(s_i-2)_+ <= b-per(F)`.  On a zero-detour subsequence, all
linear `u_B` is forced into metric loaded-hull side length above two, with only `o(D)`
arbitrary route slack.  The exact pure-tooth endpoint consequently has detour at least
`4*sqrt(pi/(2*sqrt(3)))-pi = 0.6676585...D`.  The arithmetic check is
`verify_target_c_integer_hull_route_defect.py`.  This is proof-only and leaves the
loaded-thrackle incompatibility open.

## 2026-09-13 — attachment-cell diameter-square budget

The [attachment-cell diameter-square budget](target_c_attachment_cell_diameter_square_budget_2026-09-13.md)
uses full-core strict-rhombus localization and disjoint attachment cells to prove
`sum_r d_r^2 >= D^2-o(D^2)` and hence `sum_r d_r >= D-o(D)`.  Substitution into the
exact Type-II five-currency identity gives the source-level upper budget
`G_D+e_BB-k <= 2(q-k)-D+o(D)`.  The hostile audit is
`target_c_attachment_cell_diameter_square_budget_hostile_audit_2026-09-13.md` and the
arithmetic check is `verify_target_c_attachment_cell_diameter_square_budget.py`.
This is proof-only and does not close C-II.

## 2026-09-13 — low-detour endpoint unit-side forcing

The [low-detour unit-side composition](target_c_endpoint_low_detour_unit_side_forcing_2026-09-13.md)
uses the strict aggregate endpoint floor `q-k >= 2.8406856729...D` and the audited
Section-172 detour identity. Either `(m+k)/D` is above `0.30090698...`, forcing a
linear old outer-walk detour, or the low-detour branch has
`e_BB/D >= 2.5397786922...` and `(Q+u_B)/D` at least the same amount. The
[hostile audit](target_c_endpoint_low_detour_unit_side_forcing_hostile_audit_2026-09-13.md)
passes the branch algebra; run `verify_target_c_endpoint_low_detour_unit_side_forcing.py`
for the arithmetic. No lower bound on `m` is claimed. This is proof-only endpoint
narrowing; C-II remains open.

## 2026-09-13 — strict aggregate gap forces component remainder

The [strict-gap component-remainder composition](target_c_strict_gap_component_remainder_2026-09-13.md)
combines the pushed aggregate moment gap with audited §§160--172.  With
`X_D=q-k-sum_r d_r` and `G_D=2+q+m-k-sum_r d_r`, the exact identity
`G_D=m+2+X_D` gives `liminf (G_D-m)/D >= pi(2-sqrt(3))/20`.  On the scoped Section-118
profile this yields the explicit long-side/outer-detour split
`liminf (b-per(F))/D >= (m/D+k/D-0.3009069810...)_+`.
The [hostile audit](target_c_strict_gap_component_remainder_hostile_audit_2026-09-13.md)
passes the finite algebra and same-subsequence limit bookkeeping; run
`verify_target_c_strict_gap_component_remainder.py` for the constant check.  It is proof-only;
the low-`m` branch, Type I, and C-II remain open.

## 2026-09-13 — low-response Type-II train-boundary gap

The [local train-boundary gap](target_c_low_response_typeII_train_boundary_gap_2026-09-12.md)
couples the response-selected near-diameter attachment cell to its local strict-rhombus
boundary.  Under the canonical Type-II branch and vanishing response-conductance defect
`epsilon_D -> 0`, it gives the proof-only necessary condition
`liminf (e_BB+2s_C-3(d_H+s_Z))/D >= (2*pi+sqrt(2*pi/sqrt(3)))/5 = 1.6375621841...`.
The [hostile self-audit](target_c_low_response_typeII_train_boundary_gap_self_audit_2026-09-12.md)
passes the local-face identification and boundary accounting.  This is a Type-II
low-response reduction only; Type-I and the positive-response branch remain open.

## 2026-09-13 — hostile audit of all-bridge transverse interval balance

The [all-bridge transverse interval-balance candidate](target_c_all_bridge_transverse_interval_balance_2026-09-12.md)
has passed a hostile audit ([audit](../docs/audits/target_c_all_bridge_transverse_interval_balance_hostile_audit_2026-09-13.md)).
After the C65 full-support normalization, every positive contact bridge has actual
diameter reactions on both transverse signs.  A straight nested bridge corridor obeys
the exact signed endpoint-bundle identity for those reactions, and endpoint sparsity
forces a long unchanged diameter-path profile.  The audit confirms the finite shore
shear and retains contact-isolated source points.  This remains a proof-only structural
reduction: no coupling to aggregate outer detour or `e_BB-k` is proved, so C-II remains
open.

## Target C-II finite oblique-lattice global comparison (2026-09-14)

`python3 research/verify_target_c_oblique_lattice_global_comparison.py` checks the
non-load-bearing constants in
[`target_c_oblique_lattice_global_comparison_2026-09-14.md`](../docs/reports/target_c_oblique_lattice_global_comparison_2026-09-14.md).
The independently audited canonical restricted theorem proves that every finite
full-dimensional subset of one exact two-direction unit oblique lattice with basis
angle `theta` in `(pi/3, pi/2]` is beaten by an exact same-cardinality subset of the
unit triangular lattice whenever
`(1-kappa_theta)D > 4*kappa_theta + 2/sqrt(3)`, with
`kappa_theta=sqrt((sqrt(3)/2)/sin(theta))`. The proof is a finite source-level
competitor construction using fundamental-cell area and triangular-lattice Voronoi
covering. It excludes fixed and sufficiently mesoscopic shear only in this affine
source class; it leaves inverse-diameter shear, non-affine grains, holes, interfaces,
isolates, macroscopic containers, and Level I global quantifiers open.

## Target C-II near-floor scalar compatibility regression (2026-09-14)

Run `python3 research/verify_target_c_scalar_near_floor.py` for the exact `Fraction`
certificate accompanying
[`target_c_scalar_near_floor_compatibility_2026-09-14.md`](../docs/reports/target_c_scalar_near_floor_compatibility_2026-09-14.md).
It checks a `D=10^12` abstract two-cell ledger with `mu_D=1.637562999990`, while
certified rational bounds give `mu_TC<1.637562184369`. The pinned, loaded-chord,
train-floor, augmented-cell, Section-122, and Section-123 scalar inequalities all
pass. The rational-density argument shows scalar assignments can approach the
train floor from above with positive Section-122 detour. This is a scalar-only
regression: it does not certify a planar embedding, KKT stress, source cardinality,
global optimality, or C-II closure.

## 2026-09-13 — hostile audit of bridge-subtracted isoperimetry

`target_c_bridge_subtracted_isoperimetry_2026-09-13.md` has now been checked in
`target_c_bridge_subtracted_isoperimetry_hostile_audit_2026-09-13.md`. The finite
outer-bridge subtraction and the strict-rhombus area inequality pass with occurrence
counting, but the two-phase composition remains conditional and leaves the aggregate
outer detour uncontrolled. This is proof-only and does not close C-II.

## 2026-09-12 — Section 118 correlated-slack endpoint diagnostic

`verify_target_c_correlated_slack_sharp_118.py` recomputes the displayed safe-window
and scalar-envelope values using binary64. It checks endpoint arithmetic only; the
inequalities and theorem scope belong to the accompanying hostile-audit report, which
remains unreviewed and noncanonical in this salvage.

## 2026-09-12 — all-bridge transverse bracing and interval balance

The [all-bridge transverse interval-balance candidate](target_c_all_bridge_transverse_interval_balance_2026-09-12.md)
extends the audited outer-to-outer train bracing argument to every positive-contact
bridge: the exact shore shear forces diameter reactions on both transverse signs.
On a straight nested bridge corridor, the positive KKT cut equations telescope to an
exact signed endpoint-bundle balance for the diameter-path intervals.  Endpoint
sparsity therefore forces a long unchanged bracing profile, while no-common-profile
input forces endpoint events.  This is a proved proof-only candidate; it does not yet
inject those events into the aggregate outer-walk detour or `e_BB-k`, so C-II remains
open.

## 2026-09-12 — strict thin-corridor regression

The exact [strict thin-corridor regression](target_c_strict_thin_corridor_regression_2026-09-12.md)
constructs strictly convex unit-edge polygons with linear off-phase side
occurrences and only linear area inside a near-disk ambient body.  Its verifier is
`verify_target_c_strict_thin_corridor_regression.py`.  Thus strict convexity,
near-disk containment, and subquadratic exceptional-face area do not by themselves
upgrade the audited `U >= Q/5-o(D)` corridor charge to `U=o(D)`; actual contact,
source-minimality, or boundary-order input is still required.  This is a regression,
not a C-II source or global-minimizer construction.

## 2026-09-12 — re-audit of an unimported fan/train density floor

The [all-regime fan/train re-audit](target_c_allregime_fan_train_floor_hostile_audit_2026-09-12.md)
rejects the proposed normalized density floor. The finite bounded-face fan inequality
is valid, but with `f,Q,T=O(D)` its Jensen side is `O(D)` while the strict-rhombus
crossing population is `Theta(D^2)`, so division by `D^2` removes the face term. The
finite missing-pair restriction remains proof-only structural material; no theorem
state changes.

## 2026-09-13 — two-phase bad-corridor boundary charge

`target_c_two_phase_bad_corridor_boundary_charge_2026-09-13.md` records a valid
replacement for the rejected `Q`-only hull-face capacity route. In a near-disk
full-core sequence with subquadratic exceptional-face area, shared loaded-hull
boundary is at most non-hull boundary up to `o(D)`. In the canonical contact-core
scope the exceptional faces are strict (the needed no-collinear-occurrence dependency
is explicit in the report), so each has at most four selected-direction sides. Its
bad-face loaded-hull incidence is at most five times the unpaid non-phase occurrences.
The equality corridor therefore requires `U >= Q/5-o(D)` and
`Q <= 4f+o(D)`. A strict unit-hexagon incidence regression shows the factor five is
sharp without a global hull/route argument. The finite bookkeeping regression is
`verify_target_c_two_phase_bad_corridor_boundary_charge.py`; the independent hostile
audit is `target_c_two_phase_bad_corridor_boundary_charge_hostile_audit_2026-09-13.md`.
This is audited-working proof-only research; C-II remains open.

## 2026-09-13 — two-phase loaded-hull side charge

Under Type-II `c_B=0` and global two-phase purity, at most four loaded-hull unit sides
are phase-aligned. The exact remainder obeys `e_BB <= 4 + P_exc + B_o`. Combined with
the bridge-subtracted full-area bound, this gives
`e_BB <= 4 + 3 P_exc/2 + (b-pi D)/2 + o(D)`. The hostile audit is
`docs/audits/target_c_two_phase_loaded_hull_side_charge_hostile_audit_2026-09-13.md`.
This is a conditional proof-only coupling; the positive-detour branch and C-II remain
open.

## 2026-09-13 — combined two-phase three-currency gate

`target_c_two_phase_three_currency_gate_2026-09-13.md` composes the audited
two-phase variation, occurrence-safe boundary charge, bridge-subtracted
isoperimetry, and the Type-II augmented-cell payment. Under simultaneous near-disk,
near-geodesic, and global two-phase hypotheses it gives
`delta+rho+10(e_BB-2k)/D >= 4-pi-o(1)`; for the canonical full positive-contact core
the area sandwich improves the coefficient to `5`. It excludes the cheap
detour/cheap-defect subbranch but leaves the large-surplus and positive-detour
branches open. The arithmetic certificate is
`verify_target_c_two_phase_three_currency_gate.py`, with a proof-only self-audit in
`target_c_two_phase_three_currency_gate_self_audit_2026-09-13.md`. No theorem-state
change is made.

## 2026-09-12 — attachment-route signed return

`target_c_attachment_route_signed_return_2026-09-12.md` gives a finite source-level
refinement of signed return. Splitting an occurrence-counted harmonic outer walk at
every consecutive attachment vertex yields the exact excess `L+P_exc-per(P)`, and
every complete train is charged against the actual attachment-chord host set. The
resulting weighted return inequality is audited in
`target_c_attachment_route_signed_return_hostile_audit_2026-09-12.md`. Because the
host set can contain many directions, no universal positive return constant follows;
the unresolved step is an actual source-specific host-capacity or strict-descent
theorem. This does not change theorem state.

## 2026-09-13 — refined global route-surplus floor

The repaired Section-149 atomization bridge and the audited Section-155 `N=2` Fejer
bound yield an explicit
`liminf[(b-per(F))+Q+4f]/D >= 153/1250 = 0.1224`, improving the earlier `0.1` split.
The proof reduces to endpoint positivity of a concave quadratic on the short-detour
interval `[0,153/1250]`; `verify_target_c_refined_global_route_surplus_floor.py`
certifies the rational margins. The hostile audit is
`docs/audits/target_c_refined_global_route_surplus_floor_hostile_audit_2026-09-13.md`.
This remains a proof-only global route bound and does not close the positive-detour or
Type-I branches.

## 2026-09-13 — explicit rhombus-boundary route-surplus floor

`target_c_explicit_global_route_surplus_floor_2026-09-13.md` records the direct
occurrence-safe consequence of the canonical strict-rhombus boundary theorem:
`(b-per(F))+Q+4f >= (4*sqrt(pi/(2*sqrt(3)))-pi)D-o(D)`, with exact coefficient
`0.6676585738660363...`.  It is stronger than the earlier Fejer-only `0.1224` floor
because it uses the full rhombus boundary before phase atomization.  The hostile audit
is `docs/audits/target_c_explicit_global_route_surplus_floor_hostile_audit_2026-09-13.md`;
run `python3 research/verify_target_c_explicit_global_route_surplus_floor.py` for the
arithmetic check.  This is proof-only narrowing: the detour/exceptional-perimeter split
and Type-I branch remain open.

## 2026-09-12 — Section 149 phase-atomization repair

`target_c_section149_phase_atomization_repair_2026-09-12.md` supplies the missing
finite-to-limit local-Mantel lemma: if a simple triangle-free train graph has
quadratic crossing mass whose phase-quotient separation tends to zero, then only
atomic quotient phase orbits can carry that mass, with the `1/4` Mantel factor. Its
hostile audit is
`docs/audits/target_c_section149_phase_atomization_repair_hostile_audit_2026-09-12.md`.
The repair is conditional on the fixed-epsilon form of the audited §142 saturation
input and does not close C-II.

## 2026-09-13 — bridge-subtracted outer-face isoperimetry

`target_c_bridge_subtracted_isoperimetry_2026-09-13.md` proves the finite occurrence
bound `sum p_j <= L-2B_o` for the positive-area bounded-face union of a connected
unit-edge plane graph. It yields `A <= (L-2B_o)^2/(4*pi)` and therefore removes the
outer-bridge term in a near-isodiametric, near-geodesic limit. In the canonical
no-container Type-II **full core**, the strict-rhombus union is squeezed between the
bounded-face union and the near-disk force hull, so full bounded-face area saturation
holds and the two-phase charge forces `P_exc >= (4-pi)D-o(D)`. For an arbitrary
selected carrier with only strict-rhombus saturation, the safe conclusion is the
half-strength `P_exc >= (4-pi)D/2-o(D)`.
The hostile audit is
`docs/audits/target_c_bridge_subtracted_isoperimetry_hostile_audit_2026-09-13.md` and
the arithmetic check is `verify_target_c_bridge_subtracted_isoperimetry.py`. The same
incidence argument on the full strict-rhombus union gives
`2B_o <= (b-pi D)+P_exc+o(D)` in Type II, tying outer bridges to the global route
surplus. This is proof-only; the needed near-geodesic/global two-phase hypotheses do
not hold for every current C-II survivor, so C-II remains open.

## 2026-09-13 — retracted Type-II two-phase area/train tradeoff attempt

`target_c_two_phase_typeii_area_train_exclusion_2026-09-13.md` records a rejected
proof attempt.  The loaded-hull side charge `Q <= 4f + delta D + o(D)` is valid under
its explicit hypotheses, but the face-area estimate is on the `D^2` scale:
`2f/D^2 + Q/D^2 <= pi/sqrt(3)+o(1)`.  The draft incorrectly normalized it at the
`D` scale and therefore claimed a `t` upper bound and endpoint exclusion that do not
follow.  The arithmetic certificate is
`verify_target_c_two_phase_typeii_area_train_exclusion.py`, and the hostile audit is
`docs/audits/target_c_two_phase_typeii_area_train_exclusion_hostile_audit_2026-09-13.md`.
The correction changes no theorem-state entry; C-II remains open.

## 2026-09-12 — two-phase singleton-train capacity

The proof-only note [`target_c_two_phase_singleton_train_capacity_2026-09-12.md`](target_c_two_phase_singleton_train_capacity_2026-09-12.md)
keeps the `(4-pi)D-o(D)` off-phase outer occurrences from the two-phase variation
theorem in the stopped-train ledger. Under the explicit hypothesis that all but
`o(D^2)` strict rhombi use the two selected phases, those occurrences exclude at
least `(2-pi/2)D-o(D)` trains from the phase-pair crossing capacity. The quadratic
crossing density then gives `(Q+4f)/D >= 1.5260659...` at zero outer detour. More
generally, if `x=b/D`, the same proof gives
`(Q+4f)/D >= 4*sqrt(Delta_2)+4-2x-o(1)`, an exact `2 delta` loss when
`x=pi+delta`. Section 123 gives `(e_BB-k)/D >= 0.1525...` at zero slack. The certificate
`verify_target_c_two_phase_singleton_train_capacity.py` checks the rational constants
and a surviving scalar witness; it does not prove phase concentration or close C-II.
Its hostile audit is
`docs/audits/target_c_two_phase_singleton_train_capacity_hostile_audit_2026-09-12.md`;
the audit passes the finite capacity and slack algebra while retaining the explicit
two-phase hypothesis and the unresolved global payment.

## 2026-09-12 — two-phase outer-walk variation payment

The proof-only candidate [`target_c_two_phase_outer_variation_payment_2026-09-12.md`](target_c_two_phase_outer_variation_payment_2026-09-12.md)
proves the finite projection inequalities

`s N_u + N_o >= 2 width_{Jv}(P)` and
`s N_v + N_o >= 2 width_{Ju}(P)`,

for an occurrence-counted unit-edge walk using two projective unit directions with
`s=sin(theta)`. Under the separate near-disk/near-geodesic hypotheses that both
widths are `D-o(D)` and the walk length is at most `pi D+o(D)`, it gives
`N_o >= (4-pi)D-o(D)`. The certificate
`verify_target_c_two_phase_outer_variation_payment.py` checks the exact scalar
monotonicity using `pi<22/7`; it does not prove those geometric hypotheses or identify
`N_o` with exceptional-face or extra-host currency. Since every outer-face occurrence
is a terminal stopped-train occurrence, the same scope forces at least
`(2-pi/2)D-o(D)` non-two-phase stopped trains. The candidate is proof-only and does
not close C-II: the exact endpoint decomposition is only
`N_o <= 2 L_OO + P_exc`, and the crossing-versus-boundary-tooth charge remains open.

## 2026-09-12 — endpoint diameter/perimeter feedback

`target_c_endpoint_diameter_perimeter_feedback_2026-09-12.md` composes the
proof-only outer-detour endpoint floor `q-k >= 2.7985963122... D` with the audited
difference-body perimeter bound. Since `q-k=h-s_Z`, it gives
`per(F)/D >= 3.1399137779...`, leaving only `0.0016788757 D` of perimeter slack,
and the corresponding area floor `0.7837266795 D^2`. The exact rational check is
`verify_target_c_endpoint_diameter_perimeter_feedback.py`; the hostile audit is
`target_c_endpoint_diameter_perimeter_feedback_hostile_audit_2026-09-12.md`. This
is a proof-only candidate, not a canonical theorem or C-II closure.

> Target C proof-only Sections 109-113 use the normalized namespace in [`TARGET_C_PROOF_NAMESPACE_109_113.md`](TARGET_C_PROOF_NAMESPACE_109_113.md). Historical mislabeled sources are under `research/legacy/`.

## Stress-transversal deletion and reinsertion (2026-09-12)

`python3 research/verify_target_c_stress_transversal_reinsertion.py` checks the
[stress-transversal/reinsertion proof draft](../docs/reports/target_c_stress_transversal_reinsertion_2026-09-12.md).
Using exact rational arithmetic, it verifies normalized stresses on ten square
frames with an original isolate, every pair over the entire simultaneous
post-replacement motion, and strict smaller final diameter at unchanged
cardinality. It also checks finite instances of the contact-free hexagonal
zero-reserve regression, simplex coordinate-face sharpness, and a
regular-hexagon-plus-center multiple-stress negative control. The report remains
unreviewed and does not prove protected capacity, global optimality, or Level I.


## Protected simultaneous contact creation (2026-09-11)

`python3 research/verify_target_c_protected_contact_creation.py` checks the finite
motions in the [C-II closure attempt](../docs/reports/target_c_cii_closure_run_2026-09-11.md).
It uses integer coordinates in `Q(sqrt(3))` and rational arithmetic to check every
pair over the entire simultaneous motion, the exact new contact set, unchanged
diameter, and a rationally isolated first-contact time at an unintended blocker.
It encodes unit separation, deep moving points, disjoint candidate pairs, and
spatial thinning. It omits global optimality and the full C-II source hypotheses.
Passing certifies the finite examples only; the report proves the general
selection and unchanged-KKT-polytope statements separately. The examples do not
prove or disprove Erdős #99.

## C-II interface regression (2026-09-12)

`python3 research/target_c_near_geodesic_face_regression_certificate.py` checks the
exact two-chain unit-contact face used in the [near-geodesic interface regression](../docs/reports/target_c_near_geodesic_face_regression_2026-09-12.md).
It verifies the radical cap vectors, all non-boundary distances, and the linear-area
coefficient. The certificate is a local regression only; it does not establish a
global embedding, KKT equilibrium, or minimum-diameter optimality.

`python3 research/verify_target_c_cauchy_wrapping_threshold.py` checks the numerical
root and separation in the [canonical Cauchy wrapping-threshold audit](../docs/audits/target_c_cauchy_wrapping_threshold_hostile_audit_2026-09-12.md).
It certifies only the displayed scalar arithmetic; the geometric perimeter and
attachment floors remain theorem dependencies.

`python3 research/verify_target_c_quantitative_phase_gap.py` checks the scalar and
leakage constants in canonical Section 104. It certifies the reported root, cutoff,
endpoint counts, and contradiction margin only; the geometric route/phase inputs are
theorem dependencies and C-II remains open.

`python3 research/verify_target_c_optimized_phase_gap.py` checks the scalar and
leakage constants in the proof-only Section-105 optimization candidate. It certifies
the reported root, cutoff, endpoint counts, and contradiction margin only; Section
105 remains unreviewed and does not close C-II.

## Recent C-II proof-only candidates (2026-09-12)

The [two-phase boundary occurrence charge](target_c_two_phase_boundary_occurrence_charge_2026-09-13.md)
and its [hostile audit](target_c_two_phase_boundary_occurrence_charge_hostile_audit_2026-09-13.md)
type the `(4-pi)D` non-two-phase boundary floor into the exact alternatives
`N_o <= P_exc+2B_o`. This exposes the remaining bridge term instead of silently
charging bridges to exceptional faces; it is a proof-only reduction, not C-II closure.

The [two-phase outer-walk variation payment](target_c_two_phase_outer_variation_payment_2026-09-12.md)
and its [hostile audit](target_c_two_phase_outer_variation_payment_hostile_audit_2026-09-13.md)
give an occurrence-counted near-geodesic consequence: a two-phase boundary around a
near-disk must contain at least `(4-pi)D-o(D)` non-two-phase edge occurrences. This is
the current concrete extra-host/interface population target; it is not yet identified
with canonical exceptional-face currency and does not close C-II. Its scalar coefficient
check is `python3 research/verify_target_c_two_phase_outer_variation.py`.

The [Type-II exact four-host capacity dichotomy](target_c_four_host_typeii_capacity_dichotomy_2026-09-12.md)
has an independent [hostile audit](target_c_four_host_typeii_capacity_dichotomy_hostile_audit_2026-09-13.md).
It proves that exact four-host zero-return cells can occupy at most one macroscopic
centered-parallelogram carrier, with area at most `D^2/2+o(D^2)`; hence a positive-area
cell must leave that exact regression class. Additional hosts may still preserve zero
width, so this remains an audited-working proof-only bridge rather than C-II closure.

`python3 research/target_c_multigrain_endpoint_capacity.py` checks the exact
pruning/Mantel certificate for the [multi-grain Section-118 endpoint-capacity
candidate](target_c_multigrain_endpoint_capacity_2026-09-12.md). The candidate
excludes the disconnected-phase version of the proof-only Section-118 safe window;
it does not address the inactive-container branch, full-core slack above `0.0088`,
or global minimum-diameter optimality.

The [audited Section-162 direction-gap consequence](target_c_section162_explicit_direction_gap_2026-09-12.md)
records the explicit Type-II floor `liminf(q-k)/D >= 1.8203135379...`. It is an
endpoint separation only; it does not close the full-core or inactive-container
branches.

The proof-only [Section-162 gap extension](target_c_section162_gap_extension_2026-09-12.md)
repeats the audited atom-versus-detour arithmetic with `eta=9/10000`, giving the
candidate floor `liminf(q-k)/D >= 1.8204135379...`. Run
`python3 research/verify_target_c_section162_gap_extension.py` for the exact rational
certificate. The inherited geometric argument and both C-II branches remain open.

The normalized [Section-164 all-regime atomic gap](../docs/targets/target-c/164-all-regime-atomic-mantel-gap-audited.md)
is made explicit by [Section 166](../docs/targets/target-c/166-explicit-atomic-mantel-gap-audited.md):
the audited-working train-measure gap may use `eta_grid=10^-4`, with the arithmetic
checked by `python3 research/verify_target_c_explicit_atomic_gap_166.py`. This is a
Type-II quantitative strengthening, not a C-II closure.

The [five-currency conservation law](target_c_five_currency_conservation_2026-09-12.md)
and its [hostile audit](target_c_five_currency_conservation_hostile_audit_2026-09-12.md)
give the exact Type-II identity
`2(q-k)+2=sum(d_r)+G_D+Q+u_B+k` and isolate the unresolved negative
`chi_D=q+m-per(F)` long-hull-side branch. It remains proof-only.

The [near-Mantel endpoint exclusion](target_c_near_mantel_atomic_endpoint_exclusion.md),
its [proof repair](target_c_near_mantel_atomic_endpoint_proof_repair.md), and the
[hostile-audited strict train-phase gap](target_c_strict_stopped_train_phase_gap.md)
rule out equality in the §142 stopped-train floor. They give a qualitative absolute
`epsilon_SG>0` in `T-q/2 >= 2*sqrt(Delta_2)+epsilon_SG`, but no numerical modulus;
the Type-II full-core closure and the Type-I branch remain open.

The normalized [Sections 168--169 explicit gap pair](../docs/targets/target-c/168-explicit-atomic-mantel-gap-audited.md)
raises the all-regime atomic gain to `0.0004` and propagates it to the explicit
direction gap `liminf(q-k)/D >= C_146+0.00089`. Run
`python3 research/verify_target_c_explicit_atomic_gap_168.py` and
`python3 research/verify_target_c_direction_gap_169.py` for the scalar certificates.
These are audited-working Type-II bounds, not a C-II closure.

The audited-working [Section-165 Type-I diameter-cover criterion](../docs/targets/target-c/165-typeI-diameter-cover-spare-capacity-audited.md), with its full
[inactive-chamber repacking source](target_c_inactive_diameter_vertex_cover_repacking_2026-09-12.md)
and [hostile audit](target_c_inactive_diameter_vertex_cover_repacking_hostile_audit_2026-09-12.md),
reduces either inactive-container branch to the missing lower bound
`M_1(C_*)-z_* >= tau(H)`. This is a source-level criterion, not an established
spare-capacity bound. The finite Woodall cover arithmetic is checked by
`python3 research/verify_target_c_diameter_cover_bound.py`; this certificate does not
replace the geometric classification or prove the capacity bound.

The [internal contact-wall repacking reduction](target_c_inactive_contact_wall_repacking.md)
and its [hostile audit](target_c_inactive_contact_wall_repacking_hostile_audit.md)
remove the artificial one-unit collar for bounded internal exceptional faces. The
[chamber residual conservation law](target_c_inactive_chamber_residual_conservation.md)
and [hostile audit](target_c_inactive_chamber_residual_conservation_hostile_audit.md)
show exactly that all fixed-boundary spare capacity is bounded by the single
force-hull residual `R_F`; they do not provide a lower realization of that residual.
These are audited-working Type-I reductions, not a C-II closure.

The geometry-audited [Section-167 sparse full-core extension](../docs/targets/target-c/167-sparse-fullcore-window-0105-audited.md)
excludes the proof-only Type-II full-core window `sigma<=0.0105`; its scalar
certificate is `python3 research/verify_target_c_sparse_split_fullcore_window_0105.py`.
The inherited signed-return stack remains proof-only, and the Type-I branch and
positive-detour Type-II regime remain open.

The [fully correlated sparse-return extension](../docs/reports/target_c_sparse_split_fully_correlated_window_0172_2026-09-12.md)
keeps the four slack variables coupled and extends that proof-only exclusion to
`sigma<=0.0172`. The hostile audit and
`python3 research/verify_target_c_sparse_split_fully_correlated_window_0172.py`
check the endpoint geometry and one-dimensional minimum. This supersedes the
`0.0105` scalar endpoint but still leaves the large-slack full-core and Type-I
branches open.

The normalized [Section-170 module](../docs/targets/target-c/170-correlated-sparse-return-window-0172-audited.md)
records the same endpoint with the corrected current-main dependency labels; it is
audited-working proof-only material and does not change theorem-state authority.

The audited-working [Section-171 orbit atom/detour inequality](../docs/targets/target-c/171-orbit-atom-detour-explicit-gap-audited.md)
charges a complete three-direction atomic orbit before selecting an outer atom. Its
arithmetic certificate is `python3 research/verify_target_c_orbit_detour_gap_171.py`.
It raises the proof-only all-Type-II floor to
`liminf(q-k)/D >= C_146+0.00137 = 1.8208835379...`, but the center-wrapping carrier
and the source-level closure remain open.

The [all-regime half-disk dichotomy](target_c_allregime_halfdisk_dichotomy_2026-09-12.md)
and its [hostile audit](target_c_allregime_halfdisk_dichotomy_hostile_audit_2026-09-12.md)
split the remaining Type-II geometry into a center-wrapping carrier or two complementary
half-disk groups, without an outer-detour or small-slack assumption. In the latter
branch, the [groupwise atomic-train floor](target_c_halfdisk_groupwise_atomic_train_floor_2026-09-12.md)
and [audit](target_c_halfdisk_groupwise_atomic_train_floor_hostile_audit_2026-09-12.md)
raise the train floor to `2*sqrt(2*Delta_2)` and the weighted diameter-edge floor to
`1.9948294847...D`. The center-wrapping branch and the resulting source-level closure
remain open.

The proof-only [two-half-disk interface-locality reduction](target_c_two_halfdisk_interface_sublinear_locality_2026-09-12.md)
uses the full §129 local-rhombus labeling to show that every dominant-group interface
occurrence touches one of only `R_4-sum_r R_r <= 3c_I+5=o(D)` nonlocal rhombi. Hence
`I_D=o(D)` and `t+2f/D >= 2+gamma-o(1)`. The current two-half-disk scalar endpoint
already satisfies this with slack, so the result removes an interface bookkeeping
obstruction but does not close C-II. Run
`python3 research/verify_target_c_two_halfdisk_interface_sublinear_locality.py` for
the constant check.

The [contact-chain safe-area capacity theorem](target_c_contact_chain_safe_area_capacity.md)
and [audit](target_c_contact_chain_safe_area_capacity_hostile_audit.md) give a
constructive triangular-lattice capacity bound using endpoint guards on unit-contact
walls. The resulting thresholds are finite, but no theorem yet forces a Type-I
container residual above its threshold; the theorem's exterior-cap formulas are only
conditional on a certified unit-contact path.

The [two-half-disk remainder/sign localization](target_c_halfdisk_remainder_sign_173_2026-09-12.md)
and its [hostile audit](target_c_halfdisk_remainder_sign_173_hostile_audit_2026-09-12.md)
sum the Section-160 component inequalities over the two disjoint half-disk groups.
They prove, conditionally on that proof-only dichotomy,
liminf (S_D+G_D)/D >= pi/sqrt(2), hence
chi_D/D >= -pi(1-1/sqrt(2)) + k/D. This bounds the long-hull-side escape but
does not close the remaining outer-detour or center-wrapping branches. Run
python3 research/verify_target_c_halfdisk_remainder_sign_173.py for the scalar
certificate.

The [post-§173 two-half-disk scalar regression](target_c_two_halfdisk_post173_scalar_regression_2026-09-12.md)
checks the doubled groupwise train floor, the global physical-boundary floor,
the §161/§163 moment currencies, the §123 payment, and the §172 sign branch at
one exact rational normalized point.  The point is feasible, so these scalar
inequalities still do not close the half-disk branch.  Run
`python3 research/verify_target_c_two_halfdisk_post173_scalar_regression.py` for
the certificate; the missing step is geometric/source-level.

The [contact-isolate saturation theorem](target_c_contact_saturation_no_isolates.md)
and the [internal-chamber weak-component anchoring reduction](target_c_internal_chamber_weak_component_anchoring.md)
are now paired with a [hostile audit](../docs/audits/target_c_inactive_saturation_anchoring_hostile_audit_2026-09-12.md).
They prove, at proof-only scope, that contact-isolated points can be saturated into a
KKT-invisible forest and that a contact-maximized internal chamber has no floating weak
component; one anchored component is linearly large in a macroscopic chamber. The
packing exchange needed to turn this into a C-II contradiction remains open.

The [finite core escape-barrier audit](../docs/targets/target-c/core-escape-barrier-hostile-audit-2026-09-12.md)
validates the source-specific obstruction to continuous diameter-nonincreasing escape
of the positive-contact core. It does not supply a uniform lower bound across a
growing sequence and does not close C-II.

The proof-only [Section-172 hull-side sign localization](target_c_section172_hull_side_sign_localization.md)
and its [self-audit](target_c_section172_hull_side_sign_localization_self_audit.md)
rewrite the negative-`chi_D` branch using the exact identity
`chi_D=sum(d_r)+G_D+k-per(F)-2`. A negative long-side correction must be paid by the
outer-walk surplus, and the audited endpoint profile bounds that correction below by
`-0.103623D+o(D)` when `k=o(D)`. This is a tradeoff, not a C-II closure.

The scoped [force-hull outer-pocket mixed-wall candidate](target_c_outer_pocket_mixed_wall_repacking.md)
extends the same guard/capacity construction to Section-67 pockets inside the force
hull. It is proof-only and deliberately does not extend the shield across exterior
full-hull caps.

The [aggregate inactive-chamber lattice theorem](target_c_aggregate_inactive_safe_lattice_repacking.md)
and its [hostile audit](target_c_aggregate_inactive_safe_lattice_repacking_hostile_audit.md)
use one translated lattice over all force-hull inactive chambers. They remove the
per-chamber floor loss and reduce the internal Type-I survivor to the exact finite
inequality `Xi < tau(H)`. The residual/capacity comparison needed to contradict that
inequality is still not proved, and exterior full-hull caps remain separate.

The [safe-area saturation barrier](target_c_typeI_safe_area_saturation_barrier.md)
and its [hostile audit](target_c_typeI_safe_area_saturation_barrier_hostile_audit.md)
show that every strict-safe Type-I region has area at most `sqrt(3)/2` per assigned
contact isolate. Thus area averaging alone cannot pay the diameter-graph vertex cover;
any surviving capacity must use exact unit-contact structure. This is a proof-only
no-go result for the area-only closure route, not a C-II closure.

The [Type-II boundary-defect tradeoff](target_c_typeii_boundary_defect_tradeoff_2026-09-12.md)
and its [hostile audit](target_c_typeii_boundary_defect_tradeoff_hostile_audit_2026-09-12.md)
put the Section-132 cellwise payment into the exact currency
`Q+u_B=e_BB-2k`: low `(q-k)/D` forces a linear loaded-boundary residual. This is an
audited-working proof-only reduction, not a contradiction.

The proof-only [surplus--moment identity](target_c_surplus_moment_identity_2026-09-12.md)
derives the exact finite relation
`sum_r d_r+G_D=mathcal M_D+2c_I+6`, where
`mathcal M_D=e_BB+2s_C-3k`. It rewrites the §161 and §163 currencies in the same
normalized variables and gives an explicit scalar-feasibility witness. The identity
removes a bookkeeping degree of freedom but does not close the geometric outer-detour
or Type-I branches. Run `python3 research/verify_target_c_surplus_moment_identity.py`
for the exact algebra and rational-witness checks.

The [physical-boundary two-arc transport theorem](target_c_physical_boundary_two_arc_transport.md)
and its [hostile audit](target_c_physical_boundary_two_arc_transport_hostile_audit_2026-09-12.md)
replace harmonic-cell endpoint multiplicities by the actual occurrence-counted
rhombus boundary. They prove the global inequality
`h-s_Z+2f-sum_i rho_i > (2-sqrt(3)) A_4/D` and, under Type-II area saturation,
`h-s_Z+2f >= (1+(pi/4)(2-sqrt(3))-o(1))D`. The existing outer-boundary scalar is
stronger, so this is an audited-working bookkeeping reduction, not a C-II closure.

The [train closure-rank and response-free bracing theorem](target_c_train_closure_rank_and_bracing_2026-09-12.md)
and its [hostile audit](target_c_train_closure_rank_and_bracing_hostile_audit_2026-09-12.md)
prove that every global outer-to-outer stopped train has actual diameter pairs on both
sides of its shear direction and that the exceptional-face closure matrix has rank at
least `2f-s_Z`. The result exposes the exact external-row rank barrier but supplies no
conditioning estimate or finite descent, so it remains audited-working proof-only
material and does not close C-II.

The [exceptional-face closure corank identity](target_c_face_closure_self_stress_identity_2026-09-12.md)
and its [hostile audit](target_c_face_closure_self_stress_identity_hostile_audit_2026-09-12.md)
sharpen that rank bound to the exact equality
`2f-rank(C_face)=sigma_C`, where `sigma_C` is the pure-contact self-stress dimension,
and recover `sigma_C<=s_Z` from mixed rigidity and the positive KKT stress. This is an
audited-working exact structural reduction; it supplies no singular-value estimate or
finite descent and does not close C-II.

The [defect-face outer-anchor theorem](target_c_face_host_anchor_rank_2026-09-12.md)
and its [hostile audit](target_c_face_host_anchor_rank_hostile_audit_2026-09-12.md)
use the transpose closure kernel to show that each bounded-face train component with
no outer directional anchor costs two dimensions of `s_Z`, while a one-direction
component costs one. In the zero-surplus branch every bounded-face component therefore
has two independent outer directions. Rank does not give a quantitative angular mass,
so this remains audited-working proof-only material and does not close C-II.

The [exterior mixed-wall repacking theorem](target_c_exterior_mixed_wall_repacking.md)
and its [hostile audit](target_c_exterior_mixed_wall_repacking_hostile_audit.md)
replace full boundary erosion on a genuine Type-I exterior cap by a guard on the
artificial force-hull chord plus the actual unit-contact path vertices. The resulting
safe-area/lattice criterion is a valid strict-diameter competitor condition, but the
needed positive residual lower bound is still absent; this is audited-working
proof-only material and does not close C-II.

The [inactive-container augmentation obstruction](target_c_inactive_container_augmentation_obstruction.md)
and its [hostile audit](target_c_inactive_container_augmentation_obstruction_hostile_audit.md)
give disk-scale convex examples with quadratic isolated population, linear perimeter
and Oler slack, but zero room for even one extra unit-separated point. This rules out a
statistics-only Type-I augmentation argument; the actual core/container coupling must
be used, and C-II remains open.

The [defect-charged train-flex/rank-barrier theorem](target_c_defect_charged_train_flex_and_rank_barrier.md)
and its [hostile audit](target_c_defect_charged_train_flex_and_rank_barrier_hostile_audit.md)
give the injective hole charge P_hole<=4f+Q, the train-angle floor after hole loss,
and the exact nominal external-row surplus
2x-2+s_Z+r_x. The final comparison is a certified no-go for pure row counting:
geometric rank on the train-shear space is still required, so this remains
audited-working proof-only material and does not close C-II.

The [finite local Oler detour sandwich](target_c_outer_detour_oler_sandwich.md) gives
an exact upper bound for the same cellwise outer-walk detour that appears in the
Section-116 lower return inequality. Its [endpoint regression audit](target_c_outer_detour_oler_endpoint_regression.md)
shows that at the old Section-101 scalar endpoint the Oler allowance necessarily
contains a linear near-equilateral tooth-area term; setting the non-rhombic area to
`o(D)` is inconsistent with the finite ledger. This is audited-working proof-only
material. The unresolved bridge is directional control of that boundary-tooth payment
or a source-preserving diameter descent.

The [global punctured-return master](target_c_punctured_return_master.md) replaces
per-cell route accounting by one occurrence-counted full-core ledger. Its hostile
audit confirms the exact master inequality and rotating equilateral-host averaging.
The companion [phase-atomic route-surplus theorem](target_c_phase_atomic_route_surplus.md)
and [hostile audit](../docs/audits/target_c_phase_atomic_route_surplus_self_audit_2026-09-12.md) rule out
`(b-per(F))+P_exc=o(D)` on every Type-II survivor sequence. This removes the
sublinear-route-surplus subbranch, but leaves linear boundary-order payment and the
Type-I container branch open.

The [local area/slack theorem](target_c_local_internal_rhombus_area_slack.md), its
[hostile audit](target_c_local_internal_rhombus_area_slack_hostile_audit.md), and the
[detour-to-local-face composition](target_c_local_area_slack_detour_face_dichotomy.md)
force linearly many actual harmonic-cell defect faces in the low-density
Section-118 frontier; the [composition audit](target_c_local_area_slack_detour_face_dichotomy_self_audit.md)
records the remaining train-host step. The [bounded-degree corollary](target_c_local_bounded_degree_host_corollary.md)
and its [hostile audit](target_c_local_bounded_degree_host_corollary_hostile_audit.md)
keep a linear population of those hosts uniformly bounded in degree. These are
proof-only Type-II reductions and do not close C-II.

The proof-only [gapwise local-slack payment](target_c_gapwise_local_slack_payment_2026-09-12.md)
sums the audited local area/slack theorem over the wrapping carrier and each of the
three principal complement-gap groups.  In the sharp `sigma=0.0088` endpoint window it
adds the checked large-gap term `0.0034746951...D` to the retained weighted
diameter/topology payment, giving
`5h-2d_H-7s_Z >= 9.1819490263...D-o(D)`.  Run
`python3 research/verify_target_c_gapwise_local_slack_payment.py` for the displayed
floating-point arithmetic.  The result is a proof-only endpoint tradeoff and does not
close C-II.

For the macroscopic inactive-container branch, the [blocker-multiplicity theorem](target_c_inactive_blocker_multiplicity.md)
and [hostile audit](target_c_inactive_blocker_multiplicity_hostile_audit.md) give a
linear family of disjoint blocked activation triples, while the [projected-stress
transversal bridge](target_c_projected_stress_transversal_dimension.md) and its
[audit](target_c_projected_stress_transversal_dimension_hostile_audit.md) reduce the
protected reinsertion burden to `s_Z-sigma_C+1`. The needed collective repacking or
strict-diameter implication is still absent.

The [all-defect phase/train gap](target_c_all_defect_phase_train_gap_2026-09-12.md)
records the audited full-core consequence
`2f-(d_H+s_Z) >= 0.3338292869...D-o(D)`. It is a face-population lower bound, not a
global closure.

The [explicit global route-surplus floor](target_c_explicit_global_route_surplus_floor_2026-09-12.md)
records the audited source-level bound
`liminf[(b-per(F))+Q+4f]/D >= 1/10`. Its missing bridge is the global-to-local payment
needed to close the post-§123 aggregate detour.

The [Section-125 augmented-route compression](target_c_section125_augmented_route_compression_2026-09-12.md)
records the sharper audited residual
`Delta_ad+A_*/2+3Q_* >= pi(2-sqrt(3))D/4-o(D)`. The all-tooth residual is still a
near-triangular boundary regression, not a C-II closure.

The [robust near-complete-grid endpoint theorem](target_c_robust_nearcomplete_grid_zero_detour_endpoint_2026-09-12.md)
and its [hostile audit](target_c_robust_nearcomplete_grid_zero_detour_endpoint_hostile_audit_2026-09-12.md)
exclude the zero-detour equality value from audited-working Section 154, including
the possible three-atom Mantel equality split. The result is proof-only and does not
close the positive-detour Type-II regime or the Type-I inactive-container branch.

The [finite-diagonal atomic Mantel gap](target_c_atomic_mantel_gap_finite_diagonal_2026-09-12.md)
and its [hostile audit](target_c_atomic_mantel_gap_finite_diagonal_hostile_audit_2026-09-12.md)
repair the compactness issue and give an existential all-regime gap above the
Section-142 atomic Mantel floor. The accompanying
[semicontinuity regression](target_c_atomic_mantel_uniform_gap_regression_2026-09-12.md)
records why the earlier weak-limit shortcut is invalid. This remains proof-only:
full-core slack above `0.0088` and the Type-I container repacking remain open.

The main branch also records the [diameter-vertex-cover repacking criterion](target_c_inactive_diameter_vertex_cover_repacking_2026-09-12.md)
and its [hostile audit](target_c_inactive_diameter_vertex_cover_repacking_hostile_audit_2026-09-12.md).
It reduces an internal inactive chamber to a protected spare-capacity inequality
`M_1(C)-z_C >= tau(H)`, but no lower bound proving that inequality is known.

The [sparse/directional signed-return split](target_c_sparse_directional_signed_return_split.md)
and its [audited full-core application](../docs/reports/target_c_sparse_split_fullcore_closure_2026-09-12.md)
remove the proof-only Section-118 full-core window `sigma <= 0.0088`; the
[hostile audit](../docs/audits/target_c_sparse_split_fullcore_closure_self_audit_2026-09-12.md)
confirms the correlated scalar contradiction. Run
`python3 research/verify_target_c_sparse_split_fullcore_closure.py` for the finite
arithmetic certificate. This remains proof-only and leaves full-core slack above
`0.0088` and the Type-I container branch open.

The scalar follow-up
[`target_c_sparse_split_fullcore_window_extension_2026-09-12.md`](../docs/reports/target_c_sparse_split_fullcore_window_extension_2026-09-12.md)
checks the same correlated inequality at `sigma=0.0100`, with conservative strict
margin above `0.0177`. Run
`python3 research/verify_target_c_sparse_split_fullcore_window_extension.py`.
This is a proof-only candidate conditional on the inherited geometric hypotheses on
the enlarged interval; it is not a canonical state change.

The [finite-diagonal atomic Mantel gap](target_c_atomic_mantel_gap_finite_diagonal_2026-09-12.md)
and its [hostile audit](target_c_atomic_mantel_gap_finite_diagonal_hostile_audit_2026-09-12.md)
give an existential uniform positive gap above the Section-142 atomic minimum without
using atomic-mass semicontinuity. The separate
[semicontinuity regression](target_c_atomic_mantel_uniform_gap_regression_2026-09-12.md)
records the invalid compactness shortcut that this proof avoids. The gap strengthens
the Type-II all-regime ledger but does not close C-II.

The Section-116 zero-host transport reports and the Sections 117--119 signed-return
reports are research candidates. Their scripts check only the displayed finite or
scalar implications; they do not certify a global minimizer, an exact unit
equilateral triangle, or C-II closure.

Run `verify_target_c_signed_return_transport_117.py` for the hostile-audited
Section-117 whole-area signed-return constants. Run
`verify_target_c_correlated_slack_118.py` and
`verify_target_c_correlated_slack_sharp_118.py` for the two Section-118 correlated
slack relaxations. Run `verify_target_c_analytic_slack_119.py` for the Section-119
analytic envelope. Sections 116 and 118 have no independent promotion in theorem
state; all remain proof-only or unreviewed.

## Consolidated branch certificates (2026-09-09 to 2026-09-10)

The repository-wide branch consolidation retained the scripts below because each
reproduces a finite calculation or a regression recorded in a dated report. Run a
script with `python3 research/<name>.py` unless its entry says otherwise. A pass checks
only the stated scalar, finite, or numerical claim. It does not prove the cited
geometric inputs, global minimum-diameter optimality, or Level I closure.

| Script | Arithmetic and exact scope | Report or regression |
| --- | --- | --- |
| [`midpoint_gap_currency_check.py`](midpoint_gap_currency_check.py) | Binary64 root and monotonicity diagnostics | [Midpoint-gap currency](../docs/reports/target_c_midpoint_gap_currency_floor_089327_2026-09-10.md) |
| [`p2_trace_factor_audit.py`](p2_trace_factor_audit.py) | Exact SymPy factorization for a finite `m` range; accepts `--max-m` | [P2 algebraic-degree sieve](../docs/reports/target_c_cyclic_d2_p2_algebraic_degree_sieve_2026-09-10.md) |
| [`rs_symmetric_area_floor_check.py`](rs_symmetric_area_floor_check.py) | Binary64 constants and a sampled relaxed feasible region | [FSRS symmetric-area audit](../docs/reports/target_c_rs_symmetric_area_floor_audit_2026-09-10.md) |
| [`target_c_e5981_certificate.py`](target_c_e5981_certificate.py) | Exact rational 470-cell scalar certificate | [Post-ZF `s_Z=0` certificate](../docs/reports/target_c_sz0_explicit_05981_detour_gap_2026-09-10.md) |
| [`target_c_efaq_uniform_cap.py`](target_c_efaq_uniform_cap.py) | Exact rational interval cap for the EFAQ perimeter function | [E43 nested-stability calculation](../docs/reports/target_c_e43_nested_stability_surplus_2026-09-09.md) |
| [`target_c_five_arc_pin_threshold_check.py`](target_c_five_arc_pin_threshold_check.py) | Exact rational sign checks; printed decimals are diagnostic | [Five-arc threshold](../docs/reports/target_c_five_arc_pin_delay_09604_2026-09-10.md) |
| [`target_c_general_mu05947_certificate.py`](target_c_general_mu05947_certificate.py) | Exact rational 465-cell scalar certificate | [General renormalized-surplus calculation](../docs/reports/target_c_general_renormalized_surplus_05947_2026-09-10.md) |
| [`target_c_renorm_paired_pocket_check.py`](target_c_renorm_paired_pocket_check.py) | Exact rational endpoint signs with diagnostic decimals | [Paired-pocket threshold](../docs/reports/target_c_renormalized_paired_pocket_07811_2026-09-10.md) |
| [`target_c_s1_q13_shell_regression.py`](target_c_s1_q13_shell_regression.py) | NumPy/SciPy reconstruction and LP plus SymPy spectrum checks | [Strict `q=13` S1 shell regression](../docs/reports/target_c_cyclic_s1_q13_shell_regression_2026-09-10.md) |
| [`target_c_three_arc_attachment_check.py`](target_c_three_arc_attachment_check.py) | Exact rational sign certificate; root output is diagnostic | [Three-arc threshold](../docs/reports/target_c_three_arc_attachment_floor_08995_2026-09-10.md) |
| [`verify_rsr_dd_0598.py`](verify_rsr_dd_0598.py) | Exact `Fraction` sign certificate | [RSR/DD `0.598` calculation](../docs/reports/target_c_rsr_dd_explicit_surplus_0598_2026-09-10.md) |
| [`verify_bv_rsr_dd_05983.py`](verify_bv_rsr_dd_05983.py) | Exact `Fraction` sign certificate | [BV/RSR/DD `0.5983` calculation](../docs/reports/target_c_bv_rsr_dd_explicit_surplus_05983_2026-09-10.md) |
| [`verify_bve_rsr_dd_059834.py`](verify_bve_rsr_dd_059834.py) | Exact `Fraction` sign certificate | [BVE/RSR/DD `0.59834` calculation](../docs/reports/target_c_bve_rsr_dd_feedback_surplus_059834_2026-09-10.md) |
| [`verify_hidden_edge_rsr_dd_0598366.py`](verify_hidden_edge_rsr_dd_0598366.py) | Exact `Fraction` sign certificate | [Hidden-edge/RSR/DD `0.598366` calculation](../docs/reports/target_c_hidden_edge_rsr_dd_explicit_surplus_0598366_2026-09-10.md) |

The P2 audit requires SymPy. The `q=13` S1 regression requires NumPy, SciPy, and
SymPy. The other consolidated scripts use only the Python standard library.

## Cross-target ambient-force integrator checks (2026-09-09)

Run `python3 research/integrator_ambient_force_audit.py` for finite consistency
checks supporting the [integrator run](../docs/reports/integrator_run_2026-09-09.md).
It checks midpoint and centered-polygon area/perimeter bounds on regular shells
and the noncentrally-symmetric matching regression, the exact exterior-cap Oler
identity on 675 source-hull partitions, and 20,000 points in the relaxed cavity
feasible region. Geometry and root evaluation are floating-point; one coarse
derivative sign bound is checked with exact rational arithmetic. The script
encodes enclosing-disk and convex-cap geometry, but omits global optimality, KKT
realizability, and the post-ZF hypotheses. Passing checks do not prove the
general theorems, the conditional branch exclusion, or Erdős #99; the reports
contain separate analytic proofs.
## Endpoint-aware diameter gaps and cyclic force hull (2026-09-11)

Run `python3 research/diameter_endpoint_gap_audit.py` for the checks supporting
the [endpoint-gap / cyclic-force-hull report](../docs/reports/target_c_endpoint_gap_and_cyclic_force_hull_2026-09-11.md).
It exhausts ordered subsets of at least two distinct `K_4` edges, in integer
arithmetic, for the cyclic shared-endpoint inequality `I<=2h-q+1`. It separately
checks admissible crossing diameter quadrilaterals, two-antipodal-arc and
regular-shell polygon formulas, and concave gap-simplex
examples in floating point. The combinatorial component omits geometry; the
geometric components omit global optimality and the full C-II KKT/contact hypotheses.
Passing verifies only the stated finite cases and numerical sanity checks. The
report gives the general proofs; the script does not certify Level I or a global
packing optimum.

## C53 orientation audit and exploratory stress probe (2026-09-09)

`python3 research/thrackle_interval_regression.py` now **withdraws** the former
pentagon counterexample: it checks 240 consistently cut/oriented cases exactly.
`python3 research/near_diameter_path_audit.py` additionally checks all 27,252
three-chord/interval cases needed by the geometric finite-type reduction in the
[C53/C-I restoration audit](../docs/reports/target_c_c53_orientation_and_ci_restoration_2026-09-09.md).
The reduction proof, not sampling alone, makes that finite enumeration exhaustive.

`python3 research/planar_diameter_stress_probe.py` is a separate floating-point
falsification probe using NumPy/SciPy. Its 600 sampled LP stresses are not a proof;
it omits unit contact lengths and global optimality. No output from that exploratory
probe is used in the restored PSD or finite-integration theorem.

## Near-chain vertex regressions (2026-09-09)

Run `python3 research/nearchain_vertex_regressions.py` for exact
`Q(sqrt(3))` pair-distance and contact-graph checks supporting the
[near-chain interior/vertex-defect report](../docs/reports/target_c_nearchain_interior_and_vertex_defects_2026-09-09.md).
The report proves two positive-parameter triangle-free rhombic patch families,
with arbitrarily small path turning and a positively balanced degree-three or
degree-five vertex. The script uses only the Python standard library
(`fractions`); no SymPy installation is required. Neither the script nor the
report gives these patches a global KKT stress or a global minimum-diameter
certificate.

## 2026-10-04 — Target A source-arm crossing and triangle-core rank cap

The [triangle-core source-rank note](target_a_triangle_core_source_rank_2026-10-03.md)
combines the one-sided source-shell bound, contact-lens count, rotated Voronoi tube
estimate, and canonical Sections 175–177 to obtain a conditional rank cap on the
zero-slack/locked-fan subbranch. The [one-arm refinement](target_a_one_source_arm_per_contact_edge_2026-10-03.md)
proves that a strict source matching has at most one off-shield arm crossing any one
unit contact edge, and improves the fan cap to
`rank S <= |T_Σ| + |E(Σ)| + 28d + 26` under the report's stated hypotheses. These
reports also retain the conditional sector-deficit bound
`Q_Σ <= b + |E(Σ)| + 28d + 26 - |C^partial|`. The proof candidates remain
noncanonical: they do not establish the source/response surplus needed by the current
Target A endpoint, nor close Target A or Level I.

## Tube-only response-cut audit (2026-09-08)

Run `python3 research/tube_shield_cut_audit.py` for the integer/exhaustive audit
of the [tube-only cut bound](../docs/reports/target_a_tube_only_cut_2026-09-08.md).
It checks 17,104 graph/tube/shield cases over all 1,024 prescribed-basis
bipartite graphs of the stated size. It encodes alternating paths and basis
closure; it omits unit geometry, source stress, and global optimality. A pass
verifies only those finite cases; the report supplies the general proof.

## 2026-10-04 — rotation-averaged Target A Voronoi tube

The [rotation-averaged tube candidate](target_a_rotation_averaged_voronoi_tube_2026-10-03.md)
proves that for any finite connected unit-contact shield, one lattice orientation can
be chosen from the shield geometry so that, for every translation,
`|T_Σ| <= floor(5 + 2π/√3 + (4/√3 + 4/π)|E(Σ)|)`. The proof combines Voronoi-cell
area, a connected-graph Minkowski-tube bound, and exact rotational mean width. This is
a noncanonical research candidate: it improves the canonical tube charge but does not
force the right-sector surplus needed to close Target A or Level I.

The current theorem state is documented under [`docs/`](../docs/). This directory
contains small, auditable experiments that test exact finite reductions without
pretending to certify the global optimization problem.

Before adding or interpreting a script, read [`docs/RESEARCH_WORKFLOW.md`](../docs/RESEARCH_WORKFLOW.md)
for the computational protocol. Every durable experiment should state the mathematical
claim it tests, which canonical assumptions it encodes, and what its output does **not**
prove.

## Experiment contract

A research script should make these six facts recoverable from its docstring, CLI help,
README entry, or adjacent report:

1. exact proposition/model being tested;
2. canonical theorem or regression motivating it;
3. assumptions encoded and assumptions intentionally omitted;
4. arithmetic type: exact, symbolic, interval/certified, or floating point;
5. interpretation of a positive and negative result;
6. command needed to reproduce the relevant witness/output.

When a script finds a counterexample to a universal intermediate claim, preserve the
witness in a test or report if feasible. A numerical search can kill a universal claim;
it cannot establish global minimum-diameter optimality by itself.

## Capacity flag harness

[`capacity_flag.py`](capacity_flag.py) implements the strict-conflict matching
calculation behind the v1.7 source-capacity flag. It checks unit separation and
unit equilateral triangles, computes a deterministic maximum matching, and exposes
the fundamental-circuit data used by the adjacent-cardinality exchange construction.

Run:

```sh
python3 research/capacity_flag.py --demo

# enumerate small triangular-lattice first-transition diagnostics
python3 research/transition_scan.py --width 2 --height 2

# exact axial-coordinate audit of the same finite flag
python3 research/exact_lattice_transition.py --width 3 --height 3

# unit tests for the open/closed semicircle distinction
python3 -m unittest research/test_escape_cone.py
```

The metric diagnostics use floating point only to classify the supplied examples.
The matching and cardinality identities are integer computations after the conflict
graph has been fixed. No output from this harness is a global optimality certificate.

[`escape_cone.py`](escape_cone.py) separates two geometric predicates that must not be
confused:

- an **open** semicircle gives a strict first-order one-point escape;
- a **closed** semicircle already gives a nontrivial finite one-point escape for pure
  unit-contact constraints, because first-order-neutral contacts open quadratically.

Thus fixed-neighbor local isolation by unit contacts occurs only when the contact
directions fit in no closed semicircle.

`transition_scan.py` enumerates triangle-free subshores of a finite triangular-lattice
capacity shore and classifies the first flag member containing a unit triangle using
that closed-semicircle criterion. Its `escapable` label still omits diameter and
container constraints, so it is not a full Target A feasibility certificate.

`exact_lattice_transition.py` repeats the special same-lattice-window calculation in
integer axial coordinates. Its distance, triangle, strict-conflict, and six-direction
cage predicates are exact after the geometric window has been selected. The corrected
exact counts agree with the floating-point scan.

`hall_phase_scan.py` exhaustively enumerates small monomer--dimer cell packings,
verifies the exact Hall/Euler/phase-charge identities, and reports the largest left
deficiency subject to the necessary degree-five cap. A positive scan result is only an
incidence regression: the cell pattern still needs geometric unit separation and
global diameter optimality.

The fixed degree-five witness can be inspected with

```sh
python3 research/hall_phase_scan.py --show-degree-five-witness
```

It has positive incidence nullity despite the local cap, so it guards against
promoting a local phase-charge observation into the global Target A inequality.

`homothetic_capacity.py` and its tests audit the exact free-patch lattice-capacity
formulae used in the homothetic-strain work. The stronger fixed-shape same-hull theorem
and the quantitative Kuperberg witness audit are stated in the post-v1.7 Target A
modules indexed from [`docs/targets/target-a/README.md`](../docs/targets/target-a/README.md).

## Activation/monomer regression

[`activation_monomer_regression.py`](activation_monomer_regression.py) is the exact
rational certificate behind Target A Section 152. It constructs a family with a fixed
diameter pair and \(\Theta(D^2)\) independent one-point-at-a-time activation contacts
while the same moving points occupy elementary monomer cells admitting a matching that
saturates the entire patch shore. The resulting local scaffold nullity is exactly zero.

Run:

```sh
python3 research/activation_monomer_regression.py
python3 -m unittest research/test_activation_monomer_regression.py
```

The construction uses `fractions.Fraction`; its distance and conflict checks are exact.
It intentionally **does not encode global minimum-diameter optimality**. Its purpose is
to falsify any theorem that tries to derive Schur/scaffold nullity from activation
rigidity, fixed diameter, planarity, and monomer incidence alone. See the canonical
[Section 152 module](../docs/targets/target-a/06-activation-monomer-regression.md) and
the [dated proof audit](../docs/reports/activation_monomer_regression_2026-08-30.md).

## Exact alternating-strip quadratic gap candidate

[`kuperberg_alternating_strip_exact.py`](kuperberg_alternating_strip_exact.py)
checks the new candidate in
[`target_a_alternating_strip_quadratic_gain_2026-10-02.md`](../docs/reports/target_a_alternating_strip_quadratic_gain_2026-10-02.md).
The proposition is finite gap widening in the complete center-distance-two
triangular-lattice gap packing. The strip has `4r+1` rigid triangular blocks and
gain `r^2 d^4/(128 sqrt(3))`; choosing `r=ceil(1/d)` yields quadratic gain.

```text
python3 research/kuperberg_alternating_strip_exact.py
```

The script uses exact rational arithmetic in `Q(sqrt(3))` through the existing
`Surd` class. It reconstructs the strip partition, verifies reflection and the
`r=1` five-block specialization, and checks every original nearest-neighbor
constraint with a moved endpoint, including within-block contacts. Separate
exact rational path samples check the three-stage integrated motion. The report
proves the general interface inequalities and the uniform non-neighbor clearance.

Encoded hypotheses are the complete aligned-gap lattice, the stated strip geometry,
`n>=3`, `0<d<=1/8`, `rd<=2`, and the explicit translations/path. Positive output
certifies only those finite exact bookkeeping cases. The script does not establish
global optimality, arbitrary-source exterior compatibility, the recursive collar
and support bound, a Schur deficiency, or Level I closure. The report supplies the
candidate free support bound `exp(O(d^-1 log(1/d)))` and its fixed-shape same-hull
capacity consequence. The artifact is unreviewed and has not been promoted.
## Exact Kuperberg five-block audit

[`kuperberg_five_block_exact.py`](kuperberg_five_block_exact.py) is the standard-library,
exact-arithmetic verifier for the coordinate reconstruction in
[`exact_kuperberg_five_block_rate_2026-08-30.md`](../docs/reports/exact_kuperberg_five_block_rate_2026-08-30.md).
It rebuilds the two `Delta_n`, two `nabla_n`, and middle `Delta_{n-1}` blocks from
integer triangular-lattice indices and enumerates every nearest-neighbor contact that
crosses a moved-block or moved/fixed boundary.

Run:

```sh
python3 research/kuperberg_five_block_exact.py
```

The arithmetic is exact in \(\mathbb Q(\sqrt3)[d,u,v]\) and uses only
`fractions.Fraction`. A successful run verifies that the complete cross-boundary
nearest-neighbor margin set is exactly the twelve-polynomial list in the report,
including the two controlling constraints

\[
F_d(u)=u^2-(2\sqrt3+d)u+d^2,
\qquad
G_u(v)=v^2-(2\sqrt3-u)v+u^2.
\]

The script does **not** prove global packing optimality, exterior compatibility, or
optimality of the five-block rearrangement among all possible moves. The report solves
the two small roots analytically, obtaining an explicit quartic one-step gap gain and
the resulting aligned support bound \(W(d)\le C_1\exp(C_2d^{-3})\).

## Toe-out Kuperberg series audit

[`kuperberg_five_block_toeout_exact.py`](kuperberg_five_block_toeout_exact.py) audits
the Section 160 improvement of the same five-block partition.  Instead of the
published three prescribed motions, Section 160 allows symmetric horizontal toe-out
of the outer and inner block pairs and determines five translation parameters from
five active contacts.

Run:

```sh
python3 research/kuperberg_five_block_toeout_exact.py
```

The script uses exact truncated power series over \(\mathbb Q(\sqrt3)\), through
order \(d^5\), and no third-party packages.  For block sizes `3,4,6,10` it reconstructs
every moved/fixed nearest-neighbor interface, checks that the five active margin
families vanish through the truncation order, checks that every other margin family
has a strictly positive leading coefficient, and verifies

\[
v(d)=\frac{\sqrt3}{9}d^4-\frac29d^5+O(d^6)
\]

in the paper normalization.  This is an arithmetic audit of the finite interface
calculation only.  The analytic implicit-function argument, non-neighbor clearance,
recursive support estimate, and fixed-shape corollary are proved in
[`12-toeout-kuperberg-improvement.md`](../docs/targets/target-a/12-toeout-kuperberg-improvement.md).
The script does not establish exterior compatibility or global minimum-diameter
optimality.

## September 9 campaign exact checks

[`campaign_2026_09_09_exact.py`](campaign_2026_09_09_exact.py) checks the new
[zero-transfer and narrow-path report](../docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md).
Run `python3 research/campaign_2026_09_09_exact.py`.
It enumerates convex-chord interval signs using integer coordinates, all-gap split
signatures, and the sharp 15-degree path packing family using exact arithmetic in
`Q(sqrt(3))`. It checks every pairwise distance in the finite families tested and
the entire unit-contact graph. It does not prove the general chord theorem by
enumeration, encode global optimality, or certify an infinite counterexample to
Erdős #99. General proofs and omitted hypotheses are given in the report.

## Exceptional-face train checks

Run `python3 research/campaign_2026_09_09_defect_trains.py` for the exact checks in
[the exceptional-face extension report](../docs/reports/campaign_defect_train_extension_2026-09-09.md).
It enumerates connected induced subsets of the `4 by 4` integer grid, reconstructs
face walks and trains, and checks endpoint counts, bridges, unique crossings, and
Euler identities. It also checks rational parameter data for strictly convex unit
pentagons with vanishing facewise Oler excess. Integer and rational arithmetic is
used throughout. These checks do not encode KKT or global optimality and do not
replace the report's proof for arbitrary rhombus directions.

## Phase-cut and equality certificates

[`phase_cut_certificate.py`](phase_cut_certificate.py) checks the finite models in
the [phase-cut and coherent-biclique report](../docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md).
Run `python3 research/phase_cut_certificate.py`.

Using exact rational multiples of pi, it checks all phase-cut intervals of a
30-direction graph (including right-angle crossings), the sharp five-cycle
blow-ups of sizes one and two, and all 4096 balanced tripartite graphs with two
vertices per class. It verifies the phase-cut averaging identity, acyclic lifted
potentials, the finite feedback-set lower bounds, and the corrected equality
classification. It also checks the exact sliding-interval regression at
`N=12,k=6`, obtaining 57 crossings and maximum biclique product 12. It omits
geometric realizability, unit-contact equilibrium, and
global optimality. It does not certify the general coherent-biclique diameter
theorem; that theorem has a separate geometric proof in the report.

## Target C Section 106 phase-shore certificate

Run `python3 research/verify_target_c_strong_phase_shore_gap.py` for the scalar and
finite-count checks supporting the proof-only Section 106 stronger phase-shore
candidate. It verifies the `sigma=1.2e-5` root, the `0.009D` endpoint supply, the
optimized leakage bound, and the exact-cosine corridor contradiction margin. It does
not prove the inherited geometric leakage lemmas, global minimum-diameter optimality,
or C-II closure.

## Target C Sections 107-108 area-rigidity certificates

Run `python3 research/verify_target_c_wrapping_support_area_rigidity.py` to check the
wide-window wrapping-support area floor used by proof-only Section 107. Run
`python3 research/verify_target_c_area_boosted_phase_gap.py` for the Section 108
phase/corridor arithmetic using the resulting `0.472D^2` carrier constant. These
scripts certify scalar and finite-count inequalities only; they do not certify the
support-area decomposition, inherited leakage lemmas, global optimality, or C-II
closure.

## Target C Section 109 asymptotic phase-shore certificate

Run `python3 research/verify_target_c_asymptotic_phase_shores.py` for the Section 109
regression. It checks the asymptotically sharp shore coefficient at `r=0.472` and
`C_T=6`, the `sigma=5e-5` scalar window, and the resulting projection contradiction.
The script does not prove the inherited geometric lemmas, global optimality, or C-II
closure.

Run `python3 research/verify_target_c_local_train_count_gap.py` for the companion
regression to the Section 110 local-train-count candidate. It checks the exact-ledger
bound `T_D/D<1.83`, the widened `sigma=1.8e-4` arithmetic, and the resulting
phase/corridor margin. It does not prove the ledger limit passage, global optimality,
or C-II closure.

Run `python3 research/verify_target_c_joint_shore_gap_111.py` for the Section 111
joint-shore correction. It checks the disjoint-shore capacity bound, the
`sigma=4e-4` scalar window, and the resulting projection margin. It does not prove
the inherited geometric lemmas, global optimality, or C-II closure.

Run `python3 research/verify_target_c_optimized_joint_train_legacy.py` for the
historical optimized joint-train regression (original Section-112 label; superseded by aggregate Section 112). It checks the exact-ledger train ceiling
`T_D/D<1.827`, the `sigma=4.5e-4` window, the `0.085D` shore extraction, and the
projection margin. It does not prove the inherited geometric lemmas, global
optimality, or C-II closure.

Run `python3 research/verify_target_c_aggregate_projection_gap_112.py` for the
aggregate Section 112 regression. It checks the joint principal-corridor projection
inequality across both phase families and the full `sigma=10^-3` window. It does not
prove the inherited geometric lemmas, global optimality, or C-II closure.

## Diameter-lens and near-chain audit

[`near_diameter_path_audit.py`](near_diameter_path_audit.py) checks the exact
regressions in the [2026-09-09 near-diameter-path report](../docs/reports/target_c_near_diameter_path_unloaded_core_2026-09-09.md).
Run `python3 research/near_diameter_path_audit.py`. It uses only standard-library
exact arithmetic: rational nearly straight degree-three local equilibrium stars,
the sharp 15-degree diameter-lens example in Q(√3), full-KKT straight chains with
strictly better L-shaped competitors, and the C53 three-chord circular-interval
sign table. The local stars deliberately omit full global KKT equilibrium and
are beaten by a unit square. The chains show sharpness of the dominant-edge
boundary endpoint term but are not contact-minimal global sources. The
[C53 dependency audit](../docs/reports/target_c_c53_sign_and_ci_dependency_audit_2026-09-09.md)
supplies a convex deformation proof reducing its universal sign lemma to this
exhaustive finite certificate. The finite chord audit alone is not an
electrical/unit-contact realization theorem. Universal path proofs are in the
unpromoted report; no test certifies global packing optimality or Level I closure.

## Adding a new tool

[`thrackle_interval_regression.py`](thrackle_interval_regression.py) retains its
historical filename but now rejects the old incompatible-orientation witness;
see the exact orientation audit documented above.

When a computational result becomes important enough to influence the research route:

- add a deterministic reproduction command here;
- add a focused test when the result guards against a known bug or false theorem;
- write a dated report under `docs/reports/` if the witness needs a proof-level audit;
- update the active theorem module only after the mathematical implication is proved;
- keep generated bulk output out of the theorem modules.

Use [`docs/reports/REPORT_TEMPLATE.md`](../docs/reports/REPORT_TEMPLATE.md) for the audit
record when the experiment materially changes the frontier.

## Target C-II low-response stress localization

The proof-only candidate report
[`target_c_low_response_mu_floor_2026-09-12.md`](../docs/reports/target_c_low_response_mu_floor_2026-09-12.md)
derives a stress-localization refinement of the existing RCC scalar floor. Using the
exact component harmonic energy identity, C41, C40, the Section-62 component-diameter
ledger, and the full-source virial partition, it shows that `D*epsilon_D -> 0`
forces `D^2-o(D^2)` contact stress into components with attachment diameter `D-o(1)`.
The report also records the weaker redundant scalar inequality
`mu_D >= sqrt(1-epsilon_D)-8/D`; RCC already gives
`mu_D >= 1/sqrt(1+epsilon_D)-8/D`. This is an unreviewed/noncanonical candidate; it
does not prove C-II, and it does not control contact-isolated source points or the
high-response branch.

The same report also records a canonical all-phase ledger cross-check: with
`lambda_D=(e_BB+2s_C)/D` and `kappa_D=k/D`,
`lambda_D>=2*rho+kappa_D-o(1)`, and Section 123 rewrites as
`sum P_exc <= 10(q-s_C)+O(D^(2/3))`. This is an algebraic restatement, not a
new promotion; it keeps the remaining aggregate-detour target tied to the current
canonical currency.

The note also records the canonical Type-II floor
`liminf (q-k)/D >= pi/2`, obtained from `per(F)<=q+x_B`,
`q-x_B>=2k`, and `per(F)/D->pi`. It does not assert the stronger stale
near-circle conclusion `q/D->pi` outside its hypotheses.

The corrected follow-up candidate
[`target_c_typeii_qk_train_hull_gap_2026-09-12.md`](../docs/reports/target_c_typeii_qk_train_hull_gap_2026-09-12.md)
combines that hull algebra with canonical Section 85. Its exact case split rules
out `liminf(q-k)/D < (2/5)*(pi+sqrt(pi/(2*sqrt(3))))`, giving the corrected
proof-only candidate floor `1.6375621842...`; the earlier `1.9046256137...`
claim is rejected by its hostile audit. It does not close the remaining
detour/interface branch.
The attachment-route refinement
[`target_c_attachment_route_signed_return_2026-09-12.md`](target_c_attachment_route_signed_return_2026-09-12.md)
cuts the occurrence-counted outer walk at every consecutive attachment vertex and
measures exact excess above the attachment-polygon perimeter. Its hostile audit
[`target_c_attachment_route_signed_return_hostile_audit_2026-09-12.md`](target_c_attachment_route_signed_return_hostile_audit_2026-09-12.md)
passes the endpoint, bridge, face-occurrence, and train-span bookkeeping. The result
is proof-only/audited-working: it leaves a weighted host-direction capacity problem,
because no universal positive width bound survives when all attachment chord directions
are retained. It does not close C-II or change theorem state.

The aggregate attachment-route payment
[`target_c_aggregate_attachment_route_payment.md`](target_c_aggregate_attachment_route_payment.md)
retains the nonnegative augmented-cell credits and yields a sharper upper bound on the
same aggregate detour. Its hostile audit
[`target_c_aggregate_attachment_route_payment_hostile_audit_2026-09-12.md`](target_c_aggregate_attachment_route_payment_hostile_audit_2026-09-12.md)
checks the exact local algebra and global `d_tile` sum without assuming injectivity of
local outer-walk occurrences. The resulting scalar condition is still feasible and
does not close C-II.

The proof-only [Section-121 aggregate detour payment](target_c_section121_aggregate_detour_payment.md)
globalizes the harmonic-cell bookkeeping: local strict-rhombus faces are physically
injective, loaded-loaded contacts have multiplicity at most two (at most one on a
force-hull side), and the aggregate return has the exact identity
`E_Sigma=4 Delta_R+4f+2(q-k-e_BB+C_att)-2 d_Sigma`.
Its hostile self-audit is
`docs/audits/target_c_section121_aggregate_detour_payment_self_audit_2026-09-12.md`.
The identity narrows the remaining source-level upper-bound target but does not close
C-II.

The Type-I pooled replacement theorem
[`target_c_typeI_global_safe_lattice_pooling.md`](target_c_typeI_global_safe_lattice_pooling.md)
uses one unit triangular-lattice translate across all safe internal chambers and any
genuine exterior-cap inner body. Its hostile audit
[`target_c_typeI_global_safe_lattice_pooling_hostile_audit.md`](target_c_typeI_global_safe_lattice_pooling_hostile_audit.md)
passes the cross-region separation, deletion count, diameter-cover, and one-floor
rounding checks. The finite survivor condition is
`Xi+Psi_E<tau(H)`; the theorem remains proof-only/audited-working because no current
state theorem forces the pooled spare above the diameter-cover size.

The Section-151 internal-face isoperimetric endpoint exclusion
[`target_c_section151_internal_face_isoperimetric_gap.md`](target_c_section151_internal_face_isoperimetric_gap.md)
uses the actual occurrence-counted internal outer walk to prove
`A_4^{int}<=(delta+r)^2/pi`. Its hostile audit
[`target_c_section151_internal_face_isoperimetric_gap_hostile_audit.md`](target_c_section151_internal_face_isoperimetric_gap_hostile_audit.md)
passes the bridge/articulation bookkeeping and the same-carrier area substitution. It
rules out the exact Section-148 lower edge with a `0.2393742604...D` margin, while
larger carrier-parameter regimes and the full C-II closure remain open.

The local-to-global face-fidelity reduction
[`target_c_section121_local_face_globalization.md`](target_c_section121_local_face_globalization.md)
proves that bounded faces of an induced harmonic graph are actual faces of the full
positive-contact core, so macroscopic defect faces are genuine inactive chambers. The
companion regression
[`target_c_section122_route_host_regressions.md`](target_c_section122_route_host_regressions.md)
gives an exact oblique unit-grid counterexample: four physical route hosts can make
signed return zero while the rhombic area is positive. Both are proof-only scope
controls; they do not close C-II.

The complement-gap cell-rigidity theorem
[`target_c_section130_complement_gap_cell_rigidity.md`](target_c_section130_complement_gap_cell_rigidity.md)
and its [hostile audit](../docs/audits/target_c_section130_complement_gap_cell_rigidity_hostile_audit_2026-09-12.md)
show that, at the Section-118 wrapping endpoint, Type-II area saturation forces a
residual harmonic cell to span every positive support gap. This gives the global
residual-diameter moment and the proof-only endpoint inequality
`4h-d_H-5s_Z >= 5.8076394280...D`.

The component-ledger amplification
[`target_c_section131_component_ledger_amplification.md`](target_c_section131_component_ledger_amplification.md)
and its [hostile audit](target_c_section131_component_ledger_amplification_hostile_audit.md)
turn that same endpoint moment into the finite inequality
`q+m-k >= sum_r d_r-2` and the endpoint bound
`5h-2d_H-7s_Z >= 8.6062357402...D`.

The cellwise rhombus-boundary payment
[`target_c_section132_cellwise_rhombus_boundary_payment.md`](target_c_section132_cellwise_rhombus_boundary_payment.md)
and its [hostile audit](target_c_section132_cellwise_rhombus_boundary_payment_hostile_audit.md)
give the partition-sensitive inequality
`3(h-s_Z)-2s_C >= 2 sum_r sqrt(R_{4,r})+6`.
These three results are audited-working proof-only Type-II endpoint/tradeoff material;
they do not change theorem state or close C-II.

The correlated augmented-defect cancellation
[`target_c_correlated_augmented_defect_cancellation_2026-09-12.md`](target_c_correlated_augmented_defect_cancellation_2026-09-12.md)
with its [hostile audit](../docs/audits/target_c_correlated_augmented_defect_hostile_audit_2026-09-12.md)
proves the exact identity
`(a-T)-Q^+ = 2k+2r_deep+4c_I-4`.
It collapses the return floor to the four-currency split
`Delta_ad+(7/2)Q^++k+r_deep`, with the component term sublinear. This is
audited-working proof-only material and does not close C-II.

The interface/augmented-defect dichotomy
[`target_c_section127_interface_augmented_defect_dichotomy.md`](target_c_section127_interface_augmented_defect_dichotomy.md)
with its [self-audit](target_c_section127_interface_augmented_defect_dichotomy_self_audit.md)
uses only canonical ledgers to prove
`(q-k)+J_aug >= 2 sqrt(R_4)` and `J_aug=2(e_BB-k)`.
Thus a Type-II survivor with sublinear augmented/tile defect must have
`(q-k)/D >= 1.9046...`; otherwise the augmented defect is linear. This remains
proof-only and does not close C-II.
The earlier `1.9046256...` floor is rejected by the hostile audit and must not be
used.

The proof-only [two-half-disk global boundary reduction](target_c_two_halfdisk_physical_interface_2026-09-12.md)
applies physical-boundary transport separately to the two complementary half-disk
strict-rhombus groups. The Type-II cell-label localization removes cross-cell
rhombus-edge overlap and proves
`2(q-k)/D+4f/D >= 4+2 gamma-o(1)`, with
`gamma=pi(4-2sqrt(3))/8`. Run
`python3 research/verify_target_c_two_halfdisk_physical_interface.py` for the constant
check. The boundary floor is weaker than the current half-disk train floor in the
known endpoint range, so the defect-face payment remains the open closure step. The
result is proof-only and does not close C-II. The independent hostile audit is
[`target_c_two_halfdisk_global_boundary_floor_hostile_audit_2026-09-12.md`](target_c_two_halfdisk_global_boundary_floor_hostile_audit_2026-09-12.md).

The proof-only [parallel-train pair cut](target_c_parallel_train_pair_cut_2026-09-12.md)
uses a two-train Jordan cut and Section 57 mixed rigidity to exclude two disjoint
same-direction trains joining the same pair of bounded stopping faces. Different
directions, outer-face repetitions, and non-globalized local train endpoints remain
outside the lemma. C-II remains open.

The corresponding [hostile self-audit](target_c_parallel_train_pair_cut_hostile_audit_2026-09-12.md)
checks same-direction disjointness, Jordan closure inside the full source hull,
diameter-endpoint extremality, and the mixed-rigidity contradiction. It confirms the
conditional scope only; no theorem-state promotion is made.

The audited [two-half-disk perimeter-rigidity strengthening](target_c_two_halfdisk_perimeter_rigidity_2026-09-12.md)
uses finite-perimeter lower semicontinuity after half-disk area saturation. It upgrades
the two-group physical-boundary floor to `(2+pi)D`, hence
`(q-k)/D+2f/D >= 1+pi/2-o(1)`. Its hostile audit is
[`target_c_two_halfdisk_perimeter_rigidity_hostile_audit_2026-09-12.md`](target_c_two_halfdisk_perimeter_rigidity_hostile_audit_2026-09-12.md).
The result is proof-only and does not close C-II. Run
`python3 research/verify_target_c_two_halfdisk_perimeter_rigidity.py` for the constant check.

The [post-perimeter two-half-disk scalar regression](target_c_two_halfdisk_scalar_regression_2026-09-12.md)
uses a corrected exact rational witness satisfying the strengthened perimeter floor, the
half-disk stopped-train floor, moment/remainder identities, strict phase, and §123
payment simultaneously. It confirms that the remaining obstruction is geometric or
source-level rather than a scalar inconsistency. Run
`python3 research/verify_target_c_two_halfdisk_scalar_regression.py` for the check.
The proof-only [bounded-face endpoint-simplicity theorem](target_c_bounded_face_endpoint_simplicity_2026-09-12.md)
handles the remaining different-direction pair: an innermost two-train Jordan cycle
has a positive KKT resultant supported on at most two train directions, forcing those
directions to be parallel and reducing to the audited pair-cut theorem. Its hostile
audit is
[`target_c_bounded_face_endpoint_simplicity_hostile_audit_2026-09-12.md`](target_c_bounded_face_endpoint_simplicity_hostile_audit_2026-09-12.md).
The result concerns bounded-face endpoints only and does not close C-II.

The proof-only [bounded-face train endpoint fan theorem](target_c_bounded_face_endpoint_fan_2026-09-12.md)
handles crossing trains by a prefix Jordan cut and disjoint trains by the two-face
cut. Its hostile audit is
[`target_c_bounded_face_endpoint_fan_hostile_audit_2026-09-12.md`](target_c_bounded_face_endpoint_fan_hostile_audit_2026-09-12.md).
It gives bounded-face endpoint simplicity and crossing-freeness; outer-face
repetitions and the aggregate detour remain open.

The proof-only [bounded-face phase-mixing capacity lemma](target_c_bounded_face_phase_mixing_capacity_2026-09-12.md)
uses those endpoint results to prove the exact interface bound
`sum_F a_F b_F <= |A||B|-X(A,B)` for any two disjoint train families. Its
[hostile audit](target_c_bounded_face_phase_mixing_capacity_hostile_audit_2026-09-12.md)
checks occurrence multiplicity and the directional rhombus-area conversion. The
lemma is useful only when an independent argument supplies near-complete crossing
capacity; it does not control outer-face endpoints or close C-II.

The proof-only [train closure-rank and response-free bracing theorem](target_c_train_closure_rank_and_bracing_2026-09-12.md)
proves two-sided diameter bracing for global outer-to-outer trains and the exact rank
bound `rank C_face >= 2f-s_Z` for bounded exceptional-face closure equations. Its
[hostile audit](target_c_train_closure_rank_and_bracing_hostile_audit_2026-09-12.md)
checks the core-only ZR/ZF scope, finite shear, KKT signs, and train-angle cycle
space. The result is a rank barrier and does not by itself close C-II.

The [bounded-face fan pair-count report](target_c_bounded_face_fan_crossing_floor_2026-09-12.md)
contains a valid finite inequality `20f <= T(T-1)-2R`, but its former normalized
density-floor conclusion is **retracted**: `f,T=O(D)`, so division by `D^2` makes
the left side `o(1)`. The [normalization correction](target_c_fan_pair_normalization_retraction_2026-09-12.md)
records the error and preserves the finite lemma for future near-Mantel uses.

The former [all-regime fan/train floor](target_c_allregime_fan_train_floor_2026-09-12.md)
and its audit are retained as **retracted provenance**; their scalar elimination used
the same invalid `D^2` normalization. The finite fan pair count itself remains usable
only with an independently supplied `O(D)` noncrossing-pair surplus.

The proof-only [harmonic internal outer-face lemma](target_c_harmonic_internal_outer_face_2026-09-12.md)
has a hostile audit in
[`docs/audits/target_c_harmonic_internal_outer_face_hostile_audit_2026-09-12.md`](../docs/audits/target_c_harmonic_internal_outer_face_hostile_audit_2026-09-12.md).
It passes the planarity/convex-separation and face-preservation checks, and validates
the local perimeter currency with its additive `2pi` loss. It does not provide global
boundary injectivity or C-II closure.

The existing [signed train-return capacity package](../docs/reports/target_c_signed_train_return_capacity_2026-09-12.md)
has now received an independent hostile audit at
[`docs/audits/target_c_signed_train_return_capacity_hostile_audit_2026-09-12.md`](../docs/audits/target_c_signed_train_return_capacity_hostile_audit_2026-09-12.md).
The finite oriented-return, three-host, and area-transport lemmas pass at their
stated scopes. Their all-regime application still requires a simultaneous physical
three-route budget and remains conditional.

The former [fan/train/hull scalar floor](target_c_fan_train_hull_scalar_floor_2026-09-12.md)
and [post-floor regression](target_c_post_fan_train_hull_scalar_regression_2026-09-12.md)
are likewise **retracted provenance** because they normalized `20f` at the wrong
scale. No fan-derived Type-II density floor is currently claimed.

The proof-only [`mu_4` endpoint package](../docs/reports/target_c_mu4_train_pairing_endpoint_exclusion_2026-09-12.md)
excludes the Section-96 wrapping endpoint even with a linear rhombus-free bridge
corridor. Its geodesic-collapse, train-end balance, bridge-independence correction,
and independent audit are linked from the report. The result is qualitative and leaves
larger wrapping diameters and the inactive-container branch open.

The exact [four-host signed-return regression](target_c_four_host_signed_return_regression.md)
shows why the all-route attachment refinement cannot supply a universal positive return
constant.  A square-grid patch has quadratic strict-rhombus area, zero
`L+P_exc-per(P)` excess, and four boundary hosts of width two in both train directions.
The finite verifier is `python3 research/verify_target_c_four_host_signed_return_regression.py`.
This is a regression, not a global-minimizer construction; the live target is an
effective fourth-host capacity theorem or an independent high-detour descent.
The [gapwise local-slack payment](target_c_gapwise_local_slack_payment_2026-09-12.md)
has now received a hostile audit. After repairing one missing plus sign in its
positive-part formula, the four-group endpoint coefficient `9.1819490263...` is
arithmetically consistent. The audit is
[`target_c_gapwise_local_slack_payment_hostile_audit_2026-09-12.md`](target_c_gapwise_local_slack_payment_hostile_audit_2026-09-12.md).
This remains a scoped proof-only tradeoff, not C-II closure.

## Target C-II five-currency atomic-capacity bridge

The proof-only note [`target_c_five_currency_atomic_tradeoff_2026-09-12.md`](target_c_five_currency_atomic_tradeoff_2026-09-12.md) combines the exact Type-II five-currency conservation law with the audited-working normalized Section-155 atomic endpoint/outer-detour estimate. It gives the remainder-aware scalar tradeoff

`t >= max(pi+delta, s+g+kappa)/2 + R_N(delta)/10`,

where `t=(q-k)/D`, `delta=(b-per(F))/D`, `s=sum d_r/D`, `g=G_D/D`, and `R_N` is the Fejer endpoint-capacity lower bound. The script `verify_target_c_five_currency_atomic_tradeoff.py` checks the algebra and the retained high-density scalar witness. This is proof-only/unreviewed research: it does not identify local/global face occurrences or close C-II.

The scoped [common-cap retained-remainder floor](target_c_common_cap_t_floor_2026-09-12.md)
keeps the `G_D` term in audited §161 and inserts the audited Section-118 carrier
profile. It gives `t=(q-k)/D >= 1.8376...` on that profile; the rational certificate
is `python3 research/verify_target_c_common_cap_t_floor.py`. This is not a universal
Type-II floor and does not close the large-detour or Type-I branches.

The [completion two-unit-side regression](target_c_completion_two_unit_side_regression_2026-09-12.md)
rejects a proposed sharpening of `e_BB-C_A <= 2*d_tile` to `d_tile+O(1)`. A regular
even polygon with unit sides and a noncrossing triangulation has linearly many ears,
each using two unit outer sides. Run `python3
research/verify_target_c_completion_two_unit_side_regression.py` to check the finite
ear construction. This is a boundary-combinatorial regression only; it does not claim
global optimality or a C-II counterexample.

The proof-only [train-cut covariance identity](target_c_train_cut_covariance_identity_2026-09-12.md)
combines the exact binary train-cut displacement matrix with the shore KKT resultant.
In the pure-tooth endpoint it gives `U^T A_alpha U = R^T B_beta R` and
`dim ker(E^T B_beta E-A_alpha) >= 2`, together with the exact angular-slack formula.
This is a metric spectral target for the odd-thrackle closure, not a closure theorem;
the note explicitly retains the missing coefficient-floor and finite-motion obligations.
Its hostile audit is
[`target_c_train_cut_covariance_identity_hostile_audit_2026-09-12.md`](target_c_train_cut_covariance_identity_hostile_audit_2026-09-12.md);
the audit passes at proof-only scope and confirms the required `1/D` in the
angular-slack identity.
The companion script `verify_target_c_train_cut_covariance_regression.py` certifies
the finite circulant odd-shell regression in the note: covariance and positive shore
resultants remain feasible near `q/D=pi/sqrt(3)`, while the construction is explicitly
not a full triangle-free rhombic contact complex.

The [stale global-face endpoint regression](target_c_stale_global_face_endpoint_regression_2026-09-12.md)
corrects an older provenance target that identified `b+Q>2h` with `T-h>2f`.
The active exact ledger gives `T=h-s_Z+2f`, hence `T-h-2f=-s_Z<=0`; the strict
endpoint is impossible with the canonical face count.  The old report remains
provenance only, and the live C-II work returns to the aggregate detour/source
coupling and the protected inactive-chamber capacity branch.  This is a rejected
stale endpoint/regression note, not a theorem-state change or a C-II closure.

The [withdrawn surplus/diameter scalar composition](target_c_surplus_diameter_scalar_composition_2026-09-12.md)
contained a normalization error: it treated the finite constant `2` in
`c_I+s_C=m+k-2` as `2D`. Its claimed `2.0585222...` floor and elimination of the
`t=1.9,k=0` witness are invalid and withdrawn. The corrected check retains the
separate moment lower bound only; run
`python3 research/verify_target_c_surplus_diameter_scalar_composition.py`.

The [outer-detour diameter-moment floor](target_c_outer_detour_diameter_moment_floor_2026-09-12.md)
uses `L_r >= 2d_r` together with the exact aggregate outer-walk decomposition and
the Type-II completion-side bound.  It gives
`liminf(q-k)/D >= liminf(sum d_r/D)`, hence the scoped endpoint floor
`q-k >= 2.7985963122...D`.  Its hostile audit keeps local `Q_loc` separate from
the global `Q`, so no unsupported defect identification is made.  The accompanying
high-`t` arithmetic witness remains scalar-feasible; this is a proof-only narrowing,
not C-II closure.

The [outer-detour topology band](target_c_outer_detour_topology_band_2026-09-12.md)
combines the audited endpoint floor `q-k >= 2.798596...D` with `q <= pi D`.  It
forces `k/D < 0.3444` and `r_H/D > 2.454` on that endpoint; in the Woodall forest
branch this is at most `0.3444D` caterpillar components carrying at least `2.454D`
aggregate excess.  This is a proof-only handoff to the common-bridge/caterpillar
geometry, not C-II closure.  Run `python3 research/verify_target_c_outer_detour_topology_band.py`.

## 2026-09-13 — strict aggregate moment gap

The [strict aggregate moment gap](target_c_strict_aggregate_moment_gap_2026-09-13.md)
keeps the positive canonical aggregate two-arc payment instead of using only
`L_r-2d_r>=0`.  Exact cancellation gives
`liminf[(q-k)-sum d_r]/D >= pi(2-sqrt(3))/20 = 0.0420893607...`.
On the Section-118 common-cap moment profile this raises the scoped floor to
`2.8406856729...D` (certified conservatively as `>2.8406D`).  The hostile audit is
`docs/audits/target_c_strict_aggregate_moment_gap_hostile_audit_2026-09-13.md` and
the arithmetic certificate is `verify_target_c_strict_aggregate_moment_gap.py`.
This remains proof-only and does not close C-II.
## 2026-09-12 — endpoint diameter/perimeter feedback

`target_c_endpoint_diameter_perimeter_feedback_2026-09-12.md` composes the
proof-only outer-detour endpoint floor `q-k >= 2.7985963122... D` with the audited
difference-body perimeter bound.  Since `q-k=h-s_Z`, it gives
`per(F)/D >= 3.1399137779...`, leaving only `0.0016788757 D` of perimeter slack,
and the corresponding area floor `0.7837266795 D^2`.  The exact arithmetic check is
`verify_target_c_endpoint_diameter_perimeter_feedback.py`.  This is a proved
candidate awaiting hostile audit, not a canonical theorem or C-II closure.

## 2026-09-12 — exact pure-tooth train-cut coordinates

`target_c_pure_tooth_train_coordinate_reconstruction_2026-09-12.md` derives an
exact displacement identity in the proof-only pure-tooth endpoint: every core
displacement is a signed sum of the unit vectors of the stopped train cuts. Hence
each actual diameter pair is separated by at least `ceil(D)` distinct train cuts,
and the diameter/train incidence matrix is macroscopically dense. Its hostile audit
is `docs/audits/target_c_pure_tooth_train_coordinate_reconstruction_hostile_audit_2026-09-12.md`;
both artifacts remain proof-only and explicitly leave the odd-thrackle angular
incompatibility or finite diameter descent open.

## Target C-II consecutive-tooth turn budget

Run `python3 research/verify_target_c_consecutive_tooth_turn_budget.py` for the
arithmetic checks supporting
[`target_c_consecutive_tooth_turn_budget_2026-09-12.md`](target_c_consecutive_tooth_turn_budget_2026-09-12.md).
The proof gives an exact exterior-turn bound for adjacent two-edge teeth and the
all-tooth base-excess consequences. It is a proof-only candidate: the resulting
constant second-order cost does not close the full-core branch or C-II.

## 2026-09-12 — Section 149 atomic-orbit audit

The hostile audit of `target_c_section149_quantitative_atomic_detour_stability.md`
accepts its outer Fourier/Fejer estimate but rejects the unproved step that converts
pair-measure concentration at projective separation `pi/3` into an `ell^2` lower
bound over only atomic phase orbits. A separate finite-to-limit atomization lemma is
required before the Section-149 all-regime detour tradeoff can be used.

## 2026-09-13 — exact route-surplus / stopped-train identity

`target_c_route_surplus_train_identity_2026-09-13.md` isolates the exact Type-II
identity `b + P_exc = 2T`, hence
`(b-per(F)+P_exc)/D = 2T/D-per(F)/D`.
Composing this with the audited all-regime train gap and the `C146` endpoint floor
gives a proof-only lower bound greater than `2.4871D` for the global route currency
(plus the unknown positive atomic-gap modulus). Its hostile audit is
`target_c_route_surplus_train_identity_hostile_audit_2026-09-13.md`; the rational
check is `verify_target_c_route_surplus_train_identity.py`. This is a stronger
necessary condition, not a C-II closure.

## 2026-09-13 — aggregate-detour endpoint floor

`target_c_aggregate_detour_endpoint_floor_2026-09-13.md` composes the exact aggregate
face-incidence identity with the audited `o(D)` full-core rhombus localization on the
Section-118 endpoint/common-cap profile. It gives `4delta <= 10t-4pi-2S_*-c_0` for
`t=(q-k)/D` and outer detour `delta=b/D-pi`. Composing that upper detour envelope
with the audited orbit-capacity feasibility inequality excludes every
endpoint/common-cap subsequential limit with `t <= 1.8585`, including positive-detour
cases. The hostile audit is
`target_c_aggregate_detour_endpoint_floor_hostile_audit_2026-09-13.md`; arithmetic is
checked by `verify_target_c_aggregate_detour_endpoint_floor.py`. This is a
proof-only endpoint strengthening; C-II and the theorem state remain open.

## 2026-09-13 — aggregate route-currency floor from the detour ledger

`target_c_aggregate_route_currency_floor_2026-09-13.md` keeps the canonical
Section-122 aggregate detour lower bound before applying `f<=Q`. On the Section-118
endpoint/common-cap profile, the exact Section-121 face identity and the endpoint
harmonic diameter-moment floor give
`(b-per(F)+Q+4f)/D >= 2.876493578...`, with a safe certified lower bound `2.8762`.
The arithmetic check is `verify_target_c_aggregate_route_currency_floor.py`; the
hostile audit is
`docs/audits/target_c_aggregate_route_currency_floor_hostile_audit_2026-09-13.md`.
This is a proof-only route-currency lower bound, not a C-II closure, and it is scoped
to the endpoint/common-cap profile.

## 2026-09-13 — hostile audit of Section 127 face fidelity

`target_c_section127_face_fidelity_global_defect_injection.md` has an independent
proof-only audit in
`target_c_section127_face_fidelity_hostile_audit_2026-09-13.md`. The audit accepts the
cell-interior and local-to-global face argument and the exact injection
`sum P_exc,r <= 4f+Q`, while preserving the distinction from the sharper Type-II
`5(e_BB-2k)` payment. It does not close C-II.
## Target C-II open-guard packing saturation

Run `python3 research/verify_target_c_open_guard_packing_saturation.py` for
exact rational regressions accompanying
[`target_c_open_guard_packing_saturation_2026-09-12.md`](../docs/reports/target_c_open_guard_packing_saturation_2026-09-12.md).
The proof-only theorem converts ordinary unit packings inside an open guarded
region into strict same-cardinality replacements after deleting one contact
vertex and selected original isolates. The script checks every pair in a
triangle-destroying insertion and an exchange involving an extreme original
isolate, including contact loss and surviving diameter pairs. Negative controls
show why cross-diameter lens membership alone and closed-container packings do
not suffice. These examples do not certify global optimality; the general proof
is in the report. No one-site reserve or C-II branch closure is certified.

## 2026-09-13 — Type-I one-site open-guard criterion

`target_c_typeI_open_guard_one_site_2026-09-13.md` composes the open-guard saturation
theorem with the audited strict contact-wall shields. For either an internal inactive
chamber or an exterior cap, the strict safe region has area at most
`(sqrt(3)/2)|Z|`; otherwise one extra lattice site can be strictified and exchanged
for all assigned isolates plus one nonisolated contact vertex. This removes the
diameter-vertex-cover cost from the Type-I necessary condition. The residual inequalities
are recorded explicitly, but the strict area surplus is not proved, so C-II remains
open.

## 2026-09-14 — finite oblique-lattice competitor

The canonical restricted theorem C-OBLIQUE-LATTICE-COMPETITOR is recorded in
target_c_oblique_lattice_global_comparison_2026-09-14.md and independently audited
in target_c_oblique_lattice_global_comparison_independent_audit_2026-09-14.md.
It supplies an exact same-cardinality triangular-lattice competitor for every
finite full-dimensional subset of one unit oblique lattice above the explicit
finite threshold in the report. The remaining affine possibility has only
inverse-diameter angle excess O(D^{-1}); this does not provide an affine chart for
general C-II sources and does not close C-II.

Run python3 research/verify_target_c_oblique_lattice_global_comparison.py for
non-load-bearing decimal sanity checks. No local CPU-heavy search is required.

## 2026-10-02 — threshold rail depth and local pressure regression

Run `python3 research/verify_target_c_rectangle_pressure_2026_10_02.py` for the
Fraction certificates associated with
[`target_c_threshold_rail_deep_attachment_2026-10-02.md`](../docs/reports/target_c_threshold_rail_deep_attachment_2026-10-02.md).
The script checks every pair and the complete contact graph of two finite
rhombic patches, positive interior contact-stress equilibrium, a telescoping
pressure identity, and a positive unimodal boundary-traction profile. It also
checks the exact weighted-square identity on four actual diameter endpoints.
The first regression omits realization of its external tractions by actual
equal-length diameters, full-source KKT, PSD, and global optimality. Positive
output certifies those finite algebraic and geometric checks, not a source
competitor. The report proves the general diameter-endpoint strip capacity and
the resulting macroscopic attachment-depth obstruction independently of the
script. Neither the script nor those conditional applications close C-II.

## 2026-09-14 — Voronoi-cell refinement of the affine comparison

The proof candidate docs/reports/target_c_oblique_lattice_voronoi_comparison_2026-09-14.md
replaces the radius-two fundamental parallelogram by the exact Voronoi hexagon of
an oblique unit lattice. For a finite full-dimensional subset of the exact lattice
it gives the finite same-cardinality bound

    D_triangle <= 2/sqrt(3) + kappa*sqrt(D^2 + 2*p_V(theta)*D/pi + 4/pi),

where p_V(theta)=4*tan(theta/2)+2*cos(theta)/cos(theta/2). This strictly improves
the old boundary penalty but still leaves inverse-diameter shear and does not bridge
canonical multi-grain C-II sources to one affine lattice. The report is unreviewed
and noncanonical; no computation is required.

## 2026-10-02 — ball-hull thin lattice capacity and chart ports

Report: `docs/reports/target_c_diameter_ball_hull_lattice_discrepancy_2026-10-02.md`.
Certificate: `research/verify_target_c_ball_hull_lattice_2026_10_02.py`.

Run with Python plus SymPy:
`python3 research/verify_target_c_ball_hull_lattice_2026_10_02.py`.
The verifier uses rational and exact algebraic arithmetic for actual antipodal
diameter sources, source support margins, midpoint containment, injective chart
rounding, a thin-parabola non-endpoint regression, uniform rhombic-lattice Gram
algebra, the finite two-port difference alphabet and circle intersections, and
exact one/two-port continuation regressions. It also exhausts 72 integer
circumradius polynomials and verifies their factor table and exact centers to
prove three-port chart closure throughout the continuous angle interval
`c in [9/20,1/2]`. This finite classification is load-bearing for BH.5;
register the script if that theorem is promoted. It encodes neither global optimality
nor canonical positive stress, retained train geometry or a loaded-endpoint atlas.
It corroborates the BH.6 leaf-location constants and contraction algebra with
rational inequalities; the uniform leaf theorem has the analytic proof in the report.
It does not certify the Fourier and Poisson proof: that proof is analytic in the
report. No universal conclusion is inferred from sampled algebraic sources.

The new unreviewed candidate bound is `|S|<=C(D epsilon+D^(2/3))` for actual
diameter endpoints close to one uniformly conditioned unit-rhombic chart. It
removes the logarithm in the old noise term in this restricted lattice scope.
The local two-port theorem gives chart error at most `20(1/2-c)` near the
triangular angle; its endpoint consequence leaves a linear one-port collar.
Using full-source FS.1 and actual positive leaf equilibrium, the analytic
BH.6 theorem bounds loaded contact leaves attached to one chart by `O(D^(2/3))`:
their chart neighbors lie within `O(D^(-1/2))` of the actual inner parallel
ball-hull boundary. The surviving collar can carry loaded-loaded unit edges.
Exact chart continuation through two contacts, or small-error continuation through
one contact, is rejected by the preserved nonglobal source regressions.
Level I and C-II remain open; no certificate is registered as canonical.
## Target C-II exact oblique-lattice Pick comparison (2026-09-14)

- Proof-only report: `docs/reports/target_c_oblique_lattice_pick_comparison_2026-09-14.md`
- Independent audit: `docs/audits/target_c_oblique_lattice_pick_comparison_independent_audit_2026-09-14.md`
- Verification: `python3 research/verify_target_c_oblique_lattice_pick_comparison.py`

The exact lattice-polygon/Pick comparison gives a source-cardinality-exact
triangular-lattice competitor whenever
\(\frac{\pi D^2}{4}(1/a_0-1/\sin\theta)>\frac{\pi D}{2}+1\).
It sharpens the earlier fundamental-cell thickening estimate but leaves the
inverse-diameter shear endpoint and does not extend to general C-II sources.

## 2026-09-22 — stripped weight-three Profile-B regression

An independent exact execution of
`target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_weight3_five_row_residual_2026_09_22.py`
over all 20,451 five-row orbits finds 305 extra-rank-six survivors.  This is a
deliberately stripped child audit using only the six retained incomplete rows;
it falsifies the tempting shortcut that the stripped weight-three residual is
empty.  The active unstripped closure keeps `p=9`, requires extra rank at least
6 or 7 according to the child deficiency, and is independently checked by
`...profile_b_weight3_unstripped_closure_2026_09_22.py`.
The full regression and its exact census are recorded in
`target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_weight3_stripped_residual_regression_2026-09-22.md`.
This is a regression/audit artifact, not a theorem-state promotion; Profile B,
C-II, and Level I remain open.
## 2026-10-02 — source-wide additive diameter-star cubic budget

[Report](../docs/reports/target_c_global_diameter_star_cubic_budget_2026-10-02.md)
and `verify_target_c_global_star_cubic_budget_2026_10_02.py` accompany the
unreviewed candidate `sum_(deg_H(v)>=1) (deg_H(v)-1)^3 < 12*pi*sqrt(3)*D^2`
for the full actual diameter graph of every global minimizer. The analytic
proof adds disjoint corner/antipodal-arc energy packets in a general
constant-width completion and uses the canonical complete-source Oler area
allowance. The conditional threshold application improves the boundary-heavy
carrier count to `Omega(sqrt(D))`.

The verifier uses exact `Fraction` arithmetic to check 11,692 pair distances
in four rational triangle-free actual-diameter stars, 257 rational squared
identities/bounds for the cubic-area body regression, and Hölder bookkeeping
on 1,099 finite graphs / 27,978 vertex packets. It also checks sparse star
forests showing the degree moment alone permits square-root carrier counts.
Positive output certifies those finite regressions and arithmetic only. It
does not encode general completion/support geometry, dense packing,
contact stresses, train extraction, asymptotics, or global optimality.
Neither C-II nor Level I is closed or promoted by these files.

# October 1 exact-phase gap-bundle regression

`python3 research/verify_target_c_gap_bundle_regression_2026_10_01.py` checks actual
Euclidean diameter pairs, interval rank, positive transverse circulation, axial
cut labels, nonzero two-bar reactions, and a common diameter-star witness pair
using exact `Fraction` arithmetic. It certifies a geometric counterexample to
quotient-thrackle impossibility, including finite members of an arbitrarily round
unbounded family proved in
`docs/reports/target_c_gap_bundle_geometry_regression_2026-10-01.md`.
It omits actual unit-contact crosscuts, source KKT equilibrium, stress PSD/core
rigidity, a transverse complete grid, quadratic packing population, and global
optimality. Positive output does not establish a triangle-free global minimizer.

`python3 research/search_target_c_gap_normal_order_2026_10_01.py` is a hostile
discovery search over the specified 16-point rational-circle diameter matching,
all nonempty cyclic layer-block compositions for m=2,3, and all rotations.
SciPy LP searches for positive transverse-balanced, positive axial cut weights;
reported successes are rechecked with `Fraction`. It tests the signwise nested
interval, erosion-tree, separate bundle-balance, and strict cotangent-ratio
conclusions in `docs/reports/target_c_exact_phase_nested_bundle_tree_2026-10-01.md`.
LP-infeasible cases are not exact exclusion certificates. Contacts, vertex KKT,
packing population, and global optimality are omitted; survival is not a proof.

`python3 research/verify_target_c_forest_isolate_dispatch_2026_10_01.py` checks the
fixed-anchor forest/unicyclic graph partition and every binary old-endpoint label
on all graphs through five vertices, with exact integer arithmetic. A rational
triangle certifies the need for one upper exception in the forest-diameter,
cyclic-long-pair case. It supports
`docs/reports/target_c_forest_isolate_dispatch_2026-10-01.md`; the graph universe
omits geometric realization, actual source contacts/KKT, and global optimality.
The same script compares the weighted difference-path construction with an
independent quarter-grid oracle through four variables, and checks collinear
small-total-slack regressions. This does not prove that such paths occur in a
global minimizer or that a near triangle is exact.

`docs/reports/target_c_loaded_hull_cap_attachment_budget_2026-10-01.md` proves a
finite perimeter-defect bound on short core attachments to isolates outside the
loaded hull, and a 12W bound on the nonloaded source points in a half-unit
boundary layer of the loaded hull. Their bounded near-unit degree makes them
an O(W) lower-blocker population for disjoint swaps. Deeper loaded-hull points
have a fixed diameter margin. It distinguishes hull caps from the larger exterior contact
face, and gives an exact odd regular-polygon regression against counting
noncontact hull sides from their total length excess. Its disjoint-swap
application is conditional; no global-minimizer closure is asserted.

## 2026-10-02 — diameter-first transfer and joint overlap depth

`python3 research/verify_diameter_first_joint_depth_2026_10_02.py` uses exact
`Fraction` arithmetic to check full-source binary owner translations, preserved
unit dimers, singleton feasibility, safe joint contact creation, the sharp
parallel deficit bound `eta < min(a,b)|a-b| <= epsilon^2/4`, and a connected
conflict path whose owner contraction forbids a common axial translation repair,
and 125 protected-diameter axial correction states of a nonglobal unit chain.
It supports `docs/reports/target_c_diameter_first_transfer_and_joint_depth_2026-10-02.md`.
The finite packets omit actual stopped-train ownership, source KKT, ONE-SIGN
diameter feasibility, quadratic population, and global optimality. Its finite
checks corroborate the analytic SC/QD proofs; the reverse-order ZR/ZF transfer
is proved analytically and is not certified by these examples. Positive output
establishes the listed finite packets and identities, not C-II or Level I.
The abstract graphical-cut monotonicity lemma, protected axial obstruction,
and disjoint-interval repair budget are analytic conditional results. Audit
correction: the original GO application to the strict blocker cone reversed
the longitudinal/transverse coordinates and is rejected; no owner-order
conclusion follows without a separate transverse-crossing hypothesis. The
finite chain corroborates the axial obstruction; no actual source cut chart
or blocker-load lower bound is certified by this script.

## 2026-09-22 — collapsed support-six eleven-crossing floor

`target_c_support6_collapsed_eleven_crossing_floor_2026-09-22.md` and its hostile
audit extend the exact MI.1/common-angle/forced-rotation planarization search to
weight ten. The new C++ certificate reports
`parity=58377`, `triangle-free=40324`, `metric=20349`, `planar=0` over all 42
symmetry representatives. Combined with the independently audited weights through
nine, this proves the scoped floor `X_K >= 11` and the payment `R_4 >= 11 c_6`.
This remains a proof-only local strengthening; C-II and Level I stay open.


## 2026-10-02 — positive-stress round Reuleaux leaf-fan regression

`python3 research/verify_target_c_leaf_fan_reuleaux_regression_2026_10_02.py`
certifies finite members of the exact family proved in
`docs/reports/target_c_leaf_fan_hostile_audit_2026-10-02.md`. It uses outward-rounded
integer interval arithmetic at 70 decimal places, a rational Machin-formula pi
enclosure, and explicit Taylor remainder bounds. It certifies strict unit/diameter
gaps for every inactive source pair, graph counts, a matching witness and cover,
connected actual triangle panels certifying mixed rigidity, strict grounded/Schur
spectral gaps, and a smaller same-cardinality grid for q=k=5,7,9. The additional
q=5,k=2,11 cases test short and longer fans. Exact active-pair equalities, full KKT
equilibrium, PSD/affine nullity, and the unbounded family are proved analytically in
the report; an interval containing zero is never used as an equality certificate.
The encoded sources have all source points retained and no contact isolates. They
are nonglobal shell regressions: quadratic packing population, harmonic full-core
extraction, and global optimality are omitted. Success does not solve C-II/Level I
or disprove a theorem that retains these missing global hypotheses.
## 2026-10-02 — leaf-fan stopped trains and exact collar regression

Report: `docs/reports/target_c_leaf_fan_stopped_train_and_collar_2026-10-02.md`.
Certificate: `research/verify_target_c_leaf_fan_sector_2026_10_02.py`.
Run with `python3 research/verify_target_c_leaf_fan_sector_2026_10_02.py`.

The analytic report proves a unique opposite supporting carrier for a
`(D,D,1)` fan chord, the canonical stopped-train charge
`5Q>=h-3nu(H)-3x_B`, rank-to-face transport `s_Z<=2f+3nu+x_B`,
strict interior-triangle placement of third fan neighbors, and a conditional
common-crossing area surcharge `Rg(g-1)/(8D)`.
The script uses exact rational coordinates and multipliers. Five collars
check all 3,053 source pair bounds, the complete contact/diameter sets,
triangle-freeness, 62 strict unit rhombi, 114 exact interior equilibrium rows,
positive local weights, unique opposite support, interior-triangle placement,
and the rational consequence of the area surcharge. It encodes no equilibrium
at the carrier or the four row endpoints, no PSD stress, no canonical global
normal form, and no global optimality. Success certifies a local regression
against “consecutive inward spokes force non4 faces,” not a counterexample to
Erdős #99 or a proof of the global analytic train charge. Artifact lifecycle:
unreviewed; candidates await independent audit and promotion.
## 2026-10-04 — two-singleton support 6–9 certificate verification

The proof-level composition `target_c_nine_noroot_k4_dminus1_d0p2_branch_closure_2026-09-29.md` uses four support-specific exact verifiers for supports 6–9. They import the selected-pair orientation model `verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28.py` (blob `867e8e583f6073c92b1f7afbf2aaf536e2567fa9`). Each verifier enumerates every orientation of its fixed support multiset and checks every seven- or eight-block candidate for the required empty-block rank obstruction.

Re-run on current `main` (`e7edb6d19eeb3a1d04b315f1c2fcf7eb7816e845`):

- `python3 research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support6_seven_empty_obstruction_2026_09_29.py` — 243 orientations and 416,988 seven-block subsets; all have mod-2 rank at least five.
- `python3 research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support7_eight_empty_obstruction_2026_09_29.py` — 729 orientations and 9,382,230 eight-block subsets; 9,380,367 have mod-2 rank at least five, while all 1,863 rank-four cases fail the exact rational parity-profile condition.
- `python3 research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support8_eight_empty_obstruction_2026_09_29.py` — 729 orientations and 4,691,115 eight-block subsets; 4,691,007 have mod-2 rank at least five, while all 108 rank-four cases fail the exact rational parity-profile condition.
- `python3 research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support9_eight_empty_obstruction_2026_09_29.py` — 729 orientations and 9,382,230 eight-block subsets; 9,380,367 have mod-2 rank at least five, while all 1,863 rank-four cases fail the exact rational parity-profile condition.

The rank lower bounds use integer rows reduced modulo two; rank over the rationals cannot be smaller. Exceptional rank-four spaces are checked over `Fraction` by the imported helper. These runs verify only the four finite support-orientation exclusions under the encoded nine-no-root `k=4, D=-1, d_root=0, p=2` model and its necessary parity-profile filter. They do not verify the preceding thirteen-support narrowing, the other nine support certificates, a geometric realization theorem, global-minimizer optimality, or Level I. The composite report and these research artifacts remain unreviewed and noncanonical; theorem state is unchanged.


## 2026-10-04 — collapsed support-six eight-crossing floor

`target_c_support6_collapsed_eight_crossing_floor_2026-09-27.md` and its C++
verifier strengthen the exact collapsed support-six crossing floor from seven to
eight, assuming the previously audited `<=6` certificate and the encoded MI.1,
common-angle, forced-rotation, and orientable-planarization conditions. The salvage
source was `target-c-support6-eight-crossing-floor-20260927` at
`a8d4b5d01401516e04c93a3b325ff5ace7ad5f53`.

Re-run on current main `e7edb6d19eeb3a1d04b315f1c2fcf7eb7816e845`:

```sh
g++ -std=c++17 -O2 -I research research/verify_target_c_support6_collapsed_eight_crossing_floor_2026_09_27.cpp -o /tmp/e99-support6-eight-crossing
/tmp/e99-support6-eight-crossing
```

The exact census checked 15 all-cross and 27 mixed symmetry representatives:
868,124 parity candidates, 2,544 angle-compatible seven-crossing candidates, and
zero planarizations. This verifies only exclusion of exactly seven crossings under
the stated finite model; with the prior `<=6` certificate it yields the scoped
`X_K >= 8` floor. It does not close the support-six branch, C-II, or Level I. This
is unreviewed proof-level research; theorem state is unchanged.

## 2026-10-04 — support-thirteen exact re-verification

The exact support-13 report and verifier from
`target-c-support13-closure-20260929-run11` (tip
`99314a9138509d236ce982be2343a107fc8b9fe3`) were already byte-identical to current
main. I re-ran the persisted verifier against the current-main orientation helper:

```sh
PYTHONPATH=research python3 research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support13_six_empty_obstruction_2026_09_29.py
```

It passed on 243 orientations and 51,030 six-block subsets; the mod-2 span ranks
were 7 in 972 cases, 8 in 1,458 cases, and 9 in 48,600 cases. This excludes only
the fixed support-13 orientation family under the stated two-singleton model. It
does not close the full `D=-1,p=2` branch or Level I.
## 2026-10-04 — support-7 H6 face-(2,3) finite exactifier run

`verify_target_c_support7_h6_face23_saturation_reflection_2026_09_19.py` exactifies the listed fresh candidates and checks their reflection images with rational certificates. The full run processed 298 ledger entries, discarded 106 stale after Extension VI, exactified 192 fresh candidates with 17,094 certificates, removed 284 direct/reflected candidates (100 overlap), and left 3,874 survivors. Numerical LP scans supply the embedded candidate ledger; exact arithmetic verifies each listed exclusion but does not prove that ledger complete. The result is finite support-7 algebra and gives no global-minimizer, C-II, or Level I conclusion.
## 2026-10-04 — preserved Target C geometric proof notes

`docs/reports/target_c_cyclic_cell_shape_excess_floor_2026-09-29.md` records an
unreviewed full-core Type-II candidate: near-disk harmonic-cell limits supported on
the common limiting circle give `liminf sum_r(per(P_r)-2 diam(P_r))/D >= pi-2`.
Together with the existing outer-detour ledger, the report derives a proof-only
`liminf X_D/D >= (pi-2)/2` for `X_D=q-k-sum_r d_r`. Its dependencies are listed in
the report; it does not close C-II or Level I and is not promoted.

`docs/reports/target_c_endpoint_face_angle_lemma_2026-10-01.md` records the exact
identity `sum_e(1-e dot u)=per(C)-2 diam(C)` for a convex unit-edge face with a
chosen diameter axis, and the resulting direction-count inequality. The asymptotic
phase-window application is conditional on its Section 84/90 and endpoint-interface
hypotheses. Both source branches and tip SHAs are recorded in their reports. These
artifacts remain unreviewed research; theorem state and route are unchanged.


## 2026-10-04 — Phase 2 closed-PR Target C salvage

The following artifacts are preserved as unreviewed research, scoped audits, or exact
regressions. They do not change Target C or Level I theorem state.

- [Near-floor pentagon/rank normal form](target_c_nearfloor_pentagon_rank_normal_form_2026-09-15.md) is a proof-only full-core Type-II candidate on `1.83236 <= (q-k)/D <= 1.8325`; its attached hostile audit passes at that scope. Run `python3 research/verify_target_c_nearfloor_pentagon_rank_normal_form.py`. The finite verifier checks rational constants, not the geometric hypotheses or global extraction.
- [Sparse cut-resultant profile](target_c_caratheodory_sparse_resultant_profile_2026-09-15.md) has an attached scoped hostile audit and an exact rational constant checker. Run `python3 research/verify_target_c_caratheodory_sparse_resultant_profile.py`. The certificate preserves selected cut resultants only, not full KKT equilibrium or feasible motion.
- [Profile B aligned-incidence regression](target_c_profile_b_aligned_incidence_regression_2026-09-22.md) is an exact counterexample to the claimed support inference; run `python3 research/verify_target_c_profile_b_aligned_incidence_regression_2026_09_22.py`. The abstract puncture-dimension regression is documented in [`../docs/reports/target_c_profile_b_puncture_dimension_regression_2026-10-04.md`](../docs/reports/target_c_profile_b_puncture_dimension_regression_2026-10-04.md); run `python3 research/verify_target_c_profile_b_puncture_fan_capacity_2026_09_22.py`. Neither is a geometric or global-minimizer counterexample.
- The four exact-phase / simultaneous-swap reports under `docs/reports/target_c_*2026-10-01.md` are from closed PR #595. Run `python3 research/verify_exact_phase_gap_finite_barrier.py`, `python3 research/verify_aligned_swap_horn_obstructions.py`, and `python3 research/verify_binary_contact_swap_2sat.py`. The finite actual-source regression has strict competitors for every real `D >= 13`; it is explicitly not globally optimal. The other reports retain their stated unreviewed or conditional hypotheses.

## 2026-10-04 — closed-PR exact-phase and barrier certificates

These certificates accompany unreviewed reports recovered from closed PRs #596, #599, and #617. They check finite identities, enumerations, or explicit regressions under the encoded hypotheses; none verifies a global-minimizer extraction or closes C-II.

- `verify_target_c_swap_face_endpoints_2026_10_01.py` checks exact `Q(sqrt(3))` endpoint packets for the localized face-swap report. It does not certify simultaneous compatibility with a canonical full source.
- `verify_target_c_odd_shell_gap_regression.py` checks the listed odd-shell finite families and cyclotomic certificates. These are shell regressions, not a global source classification.
- `verify_target_c_oriented_train_defect_2026_10_02.py` uses SymPy exact identities for the Green formula, jumps, and modes, then rational bounds for the stated margin and finite cycle regression. It does not prove that a canonical source embeds into the modeled train.
- `verify_target_c_nested_diameter_support_2026_10_01.py` exhausts support graphs through `m<=6` and checks the report's rational source packets. It does not settle larger support systems or global optimality.
- `verify_target_c_face_following_cap_blockers_2026_10_01.py` checks finite rational-grid counts and exact constants for the stated cap/blocker model. It does not prove KKT equilibrium, train extraction, or a global-minimizer consequence.
- `verify_open_cell_sharp_escape_2026_10_02.py` checks exact singleton barriers, paired-tree contractions/chord orders, source-pair regressions, and the encoded pentagon PSD packets. Its whole-train applications still require the unpromoted common-star, rank, boundary-layer, and exact-chart hypotheses stated in the report.
## 2026-10-04 — closed-PR incidence and source certificates

These certificates accompany unreviewed reports recovered from closed PRs #590, #593, and #620. They verify the stated finite arithmetic, enumerations, or explicit regression packets; none certifies global optimality or closes C-II.

- `verify_two_direction_stress_caps.py` checks exact KKT/source constraints and strict competitors for the finite quadratic-field cross-and-isolate family in `global_contact_direction_cone_caps_2026-09-26.md`. It does not establish global optimality or the all-positive-contact angular hypothesis for a canonical source.
- `verify_antipode_transition.py` exhausts the specified 4 by 3 grid subsets and rational fan for the finite antipode/support audit. The analytic phase-occupancy claim and transfer to global train currency are not certified by this enumeration.
- `verify_diameter_star_contiguity.py` checks 4,017 bounded grid subsets and 934 hulls. This is a finite audit, not a theorem for arbitrary sources.
- `verify_exterior_cap_population.py` checks rational coefficient and site-count arithmetic for the analytic cap bound; large populations are formula counts, not explicit enumeration, and it does not prove a global-minimizer hypothesis.
- `verify_marked_grid_corrugation.py` checks exact rational source examples pair by pair, preserving contacts and strictly shortening diameter pairs. It does not establish that a canonical source has the required single additive chart or axis-contact condition.
- `verify_oblique_lattice_corrugation_threshold.py` certifies the rational Machin/square threshold arithmetic, 174 bounded lattice-circle cases, and 914 consecutive-triple determinant checks. It does not prove the analytic corrugation theorem or a global chart extraction.
- `verify_triangular_lattice_triangle_free_face_count.py` checks the exact rational threshold and all 1,611 triangle-free occupancy patterns in the stated finite lattice patch. It does not extend the conclusion beyond the one-lattice source class and analytic hypotheses in its report.
- `verify_target_c_harmonic_cubic_window_2026_10_02.py` checks rational/cyclotomic arithmetic, dyadic capacities, antipodal interval families, and exact square/pentagon-star stress packets. It corroborates the report's estimates but does not certify completion geometry, global optimality, or the coupling of harmonic components to threshold-forest components.
- The repaired `verify_target_c_two_halfdisk_scalar_regression.py` checks only the historical scalar regression now described in `target_c_two_halfdisk_scalar_regression_2026-09-12.md`; it does not verify the later shape-detour cap system or any source-level theorem.
## 2026-10-04 — Target B closed-PR grain-chain salvage

The unreviewed reports `target_b_phase_cut_boundary_order_grain_reduction_2026-09-22.md`, `target_b_phase_cut_relative_isoperimetry_2026-09-22.md`, and `docs/reports/target_b_necessary_pocket_roughness_2026-09-25.md` were preserved from closed PRs #561, #564, and #576 at the exact source heads recorded in the reports. They record an existential quadratic retained grain, a finite relative-isoperimetric inequality, and the later correction that the proposed `Q_U=o(D)` application cannot occur in the canonical pure-disk survivor. The finite inequality remains unrefuted. The deep-boundary consequence is a proof-only candidate, not the Target B shell-stability inequality. There are no reusable scripts. State and route remain unchanged.
## 2026-10-04 — Target C loaded-hull geometry salvage

- `docs/reports/target_c_near_lattice_loaded_hull_exclusion_2026-09-25.md` (closed PR #579, source head `ed21248321fea8f8e99d257da60ca9e11417b814`) gives a fixed-error convex near-lattice vertex bound and an exact regular-ring regression showing that lattice-shadow outliers alone do not force positive outer-walk detour. Its canonical chart-cover premise remains open; no verifier is supplied.
- `docs/reports/target_c_diameter_support_atlas_obstruction_2026-09-26.md` and `research/verify_target_c_annular_atlas_2026_09_26.py` (closed PR #591, source head `9bf2b627280a313c3fad8433ade344790ec63205`) preserve finite loaded-chord/diameter-support claims and their exact rational/integer checks. The verifier checks finite examples and rounded constants; it does not prove the analytic theorem or chart-cover premise.
- `docs/reports/target_c_convex_bank_train_capacity_2026-10-02.md` and `research/verify_convex_bank_train_capacity_2026_10_02.py` (closed PR #609, source head `72c97c32db7ca5d5cda8313ccc78dd99afd0ed9a`) preserve a conditional near-disk bank-capacity candidate. The verifier uses only integer/Fraction arithmetic for its finite grid, force-star, phase-order, and constant checks; it does not prove the general bank theorem or global optimality.

All three reports remain unreviewed, and none closes C-II or Level I.
## 2026-10-04 — audited dominant-pentagon through-splicing salvage

The proof-only report `target_c_dominant_pentagon_through_splicing_2026-09-15.md`, its scoped hostile audit, and `verify_target_c_dominant_pentagon_through_splicing.py` were preserved from closed PR #522 at source head `2346fb9c3047f26525579df9aced37bc9759e7f6`. The audit records PASS only for the fully force-visible full-core Type-II scope. The verifier enumerates the six exact triangular-ray closure patterns and checks the connector, graph-contraction, and displayed numerical calculations; the displayed scale value uses 80-digit Decimal arithmetic. It does not certify the geometric extraction or a globally optimal source. Later mainline numeric floors dominate the report's stated floor, but this distinct through-splicing/Mantel-deficit lemma is retained. Artifact lifecycle remains unreviewed.
## 2026-10-04 — exact-phase source and threshold salvage

Preserved unreviewed/conditional reports from closed PRs #594, #597, #603, and #618; exact source branch heads are recorded in each report. The duplicate `target_c_diameter_first_normal_form_2026-10-02.md` from #594 was omitted because current-main `target_c_diameter_first_transfer_and_joint_depth_2026-10-02.md` independently rederives and strengthens its source-selection claim. Basic signed gap circulation is also present in current-main PR #648; the #594 circulation report is retained only with its additional finite chart-isolation analysis and regression. Current main contains the hostile audit for the #603 full-span host-coherence step; its route application remains conditional.

Exact scripts preserved and run from their source heads:

- `verify_exact_phase_gap_circulation_2026_10_01.py`: Fraction-based positive-circulation packets, cuts, rank, and a labeled geometric regression; the example does not encode a train/contact embedding or global optimality.
- `verify_harmonic_rail_endpoint_lift_2026_10_01.py`: exact source distances, square KKT/PSD data, rails, and component moments; no large-source or global-optimum theorem.
- `verify_near_unit_face_conflicts_2026_10_01.py`: exact finite face/path regressions; omits global KKT, nested train ownership, and optimality.
- `verify_ordered_gap_circulation_2026_10_01.py`: exact Fraction-based graph enumeration and chord regressions; no contact/train embedding or Level I conclusion.
- `verify_target_c_star_ray_staircase_2026_10_01.py`: exact algebraic/rational source and graph regressions, with full-source KKT and global optimality explicitly absent.
- `verify_target_c_star_ray_hostile_audit_2026_10_01.py`: exact Q(sqrt(42),sqrt(165)) audit regressions, with global train cuts, KKT, and optimality absent.
- `verify_threshold_packet_length_stress_2026_10_02.py`: exact Fraction/rational-LDL formal cut-data models; no joint Euclidean source realization or finite release.
- `verify_threshold_packet_reaction_2026_10_02.py`: exact Fraction distances and rational enclosures for radicals; no full KKT/global-optimality source.

The source PR #594 report of algebraic no-bridge circulation overlaps #648; its additional chart/regression scope is retained without duplicate theorem-state promotion. All scripts passed in their source worktrees. None of these artifacts closes the remaining C-II source-level obligation.

### PR #600 exact small-swap and loaded-hull regressions

Three unreviewed reports from closed PR #600 at source head
9ddd9538c29244fd22183f9682b2835f54cde0c3 are preserved:
target_c_joint_swap_horn_and_loaded_defects_2026-10-01.md,
target_c_loaded_near_unit_hull_adjacency_2026-10-01.md, and
target_c_ultrasmall_swap_isolate_dispatch_2026-10-01.md. Current main's
target_c_aligned_swap_horn_and_axial_bracket_2026-10-01.md generalizes the
rooted-isolate upper-dispatch component; the other exact source-conflict and
near-unit loaded-hull statements remain supplementary, unpromoted claims.

- verify_joint_swap_horn_loaded_defects_2026_10_01.py uses Fraction arithmetic to check exact conflict packets, truth tables, KKT/threshold regressions, and an isolate collision. It does not prove a train extraction or global optimality.
- verify_loaded_near_unit_hull_adjacency_2026_10_01.py uses rational/quadratic-field arithmetic for finite loaded-hull packets and exact cap checks; it does not prove the general theorem or asymptotic source application.
- verify_ultrasmall_swap_isolate_dispatch_2026_10_01.py checks rational source packets, thresholds, dispatch examples, and isolate collisions; it encodes no train/KKT/global-optimality certificate.

All three exact scripts passed at the source head and on this salvage branch. Artifact lifecycle remains unreviewed; theorem state is unchanged.

## 2026-10-04 — nine-no-root k=5 support-7 reduction and profile closures

`python3 research/verify_target_c_support7_global_segment_relative_nine_noroot_k5_reduction_2026_09_30.py` checks the k=5 arithmetic profiles, puncture identities, sharpened weight tables, and touched-block maxima in the accompanying reduction report. It is an arithmetic consistency checker; the mathematical reductions are in the report.

`python3 research/verify_target_c_support7_global_segment_relative_nine_noroot_k5_dminus1_d0p5_corrected_orientation_closure_2026_09_29.py` checks the exact S2--S8 orientation/empty-subset census for the `D=-1, d_root=0, p=5` profile. It uses exact `Fraction` rank arithmetic through the byte-pinned current-main helper and verifies the necessary structural constraints and all possible rank-four extensions; all extension survivor counts are zero. Together with the main S1 obstruction, it excludes this one support-7 profile.

Compile and run `research/verify_target_c_support7_global_segment_relative_nine_noroot_k5_dminus2_d1p1_support_closure_2026_09_29.cpp` using `g++ -std=c++20 -O2 -Wall -Wextra -pedantic`. It enumerates the finite support-level relaxation for `D=-2, d_root=1, p=1`; the exact run reports 121458 size-nine support orbits, 2634 with `h<=16`, 2178 relaxed profile tests, and zero survivors. Triangle-row ranks are computed modulo `2^31-1`; Lucas--Lehmer verifies primality, and the Hadamard determinant bound identifies modular and rational ranks. The relaxation discards orientation/gluing constraints and keeps only necessary local-rank, incidence, and puncture-weight conditions, so zero survivors excludes actual states only in the stated arithmetic profile.

These reports are **unreviewed** conditional research candidates depending on the cited Target C support-7 reductions. Main already contains the `D=-2,d_root=0,p=4` and `D=-1,d_root=1,p=2` neighboring closures. The salvaged reductions plus closures account for the other three k=5 profiles, but do not close the remaining nine-no-root cases, Target C-II, or Level I, and do not change theorem state.

## 2026-10-03 — coupled atomic coarea train-gap candidate

The proof-only [Target B report](target_b_coupled_phase_sum_bootstrap_2026-10-03.md)
keeps the phase sum coupled to the atomic coarea concentration and local
missing-pair bound. It derives an implicit strict improvement and endpoint
exclusion for the pure-rhombic-disk train-count branch. This remains an
unreviewed, noncanonical candidate: it does not prove the global shell/Oler
stability inequality, and no verifier is supplied or claimed.

## 2026-10-02 — Target C phase swaps and cyclic rotation

`python3 research/verify_phase_swap_rhombus_threshold_currency_2026_10_02.py`
checks the exact finite blocker/phase packets described in
[`target_c_phase_swap_rhombus_threshold_currency_2026-10-02.md`](../docs/reports/target_c_phase_swap_rhombus_threshold_currency_2026-10-02.md).
It checks 180 source pairs, 3,020 threshold packets, 8,190 gap subsets, and
1,742,048 phase assignments, including the retained-grid and adjacent-only
regressions. It does not certify KKT, canonical train extraction, omission-budget
globalization, or Level I optimality. The analytical blocker theorem remains
conditional in its source application.

The [cyclic phase-rotation candidate](../docs/reports/target_c_open_cell_cyclic_phase_rotation_2026-10-02.md)
proves an exact contact-preserving inverse-diameter layer rotation under its
proof-only open-cell/O--O dependencies, then leaves a two-sign or non-grid
inactive-blocker alternative. No executable verifier is supplied. The
[defect-charge hostile audit](../docs/reports/target_c_swarm_defect_charge_hostile_audit_2026-10-02.md)
retains its scoped all-cell estimate but finds no cross-part allocation that
would close the physical payment. These claims remain unreviewed/noncanonical.

## 2026-10-05 — Target C cut-Gram and finite-deficit candidate

The unreviewed report `target_c_cut_gram_nullity_and_finite_deficit_2026-10-02.md`
gives exact scalar and angular cut-Gram kernel criteria, a finite weighted-deficit
identity, and a diameter-turnover alternative under its stated full-source
feasibility and lexicographic-minimality assumptions. Its exact Q(sqrt(3)) verifier
checks finite hexagon and square regressions; it does not certify O--O extraction,
global optimality, inactive-pair exclusion, or C-II closure. The cut-to-train
application remains conditional on unpromoted source-extraction hypotheses.

## 2026-10-05 — nine-no-root k=6 support-profile packet

`target_c_k6_nine_no_root_profile_packet_2026-10-05.md` consolidates the
unreviewed p=4 and p=5 finite-support reductions. The exact m=4 and m=6 p=4
verifiers pass; m=3 is an incidence argument. The p=4 support-compression and m=5
censuses, and the p=5 support-orbit census, lack committed verifier source, so
neither full p=4 exhaustion nor p=5 census is claimed as certified. All claims
are scoped to their displayed coefficient-space/root-block hypotheses and have
no C-II or Level I status effect.


The original nine-no-root `k=4,D=-2,d_root=0,p=1` support certificate is invalid:
distinct containing tetrahedral supports can give local rank two. Its exact
counterexample is recorded in
`docs/reports/target_c_support7_local_rank_converse_counterexample_2026-10-04.md`.
Do not rely on
`verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus2_d0p1_support_closure_2026_09_27.cpp`;
it now exits with an invalid-certificate message. The sound replacement is
`target_c_support7_global_segment_relative_nine_noroot_k4_dminus2_d0p1_local_rank_repair_2026-09-27.md`
with verifier
`verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus2_d0p1_local_rank_repair_2026_09_27.cpp`.
Compile it using `g++ -std=c++20 -O2 -Wall -Wextra -pedantic`. Its exact run
reports 121458 size-nine support orbits, 33920 with `h<=20`, 2166 relaxed profile
tests, and zero survivors. This is an unreviewed support-level candidate for that
one arithmetic profile, not a C-II closure.

The p=6 audit
`target_c_p6_local_rank_underestimate_audit_2026-09-27.md` shows why the `e=3`,
`e=5`, `e=6,m=6`, and `e=8` prefilters remain sound despite the same false converse:
tags are lower bounds on actual local ranks, pair tests are relaxations, and every
incidence-two empty block is necessarily rank one. All four exact verifiers passed.
The e=8 verifier docstring now states this monotone-tag scope instead of claiming
tag equality.

## PR #667 hull-depletion audit and canonical disposition (2026-10-04)

Audit.52 promotes the [hull-depletion theorem](../docs/reports/target_c_fullcore_hull_train_depletion_floor_2026-10-04.md)
as `C-FULLCORE-HULL-DEPLETION-FLOOR`, with its independent proof in
[`target_c_fullcore_hull_train_depletion_floor_independent_audit_2026-10-04.md`](../docs/audits/target_c_fullcore_hull_train_depletion_floor_independent_audit_2026-10-04.md),
the [finite hull-side capacity lemma](../docs/reports/target_c_hull_side_exact_train_capacity_audit_2026-10-04.md),
and [exact verifier](verify_target_c_hull_side_train_capacity_2026_10_04.py).
Every full-core near-disk Type-II sequence satisfies
\[
\liminf\mu_D\ge\frac{\pi+\sqrt{\pi/(2\sqrt3)}}2
=2.046952730226875\ldots,
\]
and convergence to that endpoint is excluded. The verifier checks finite
geometry and exact arithmetic, not the asymptotic train-depletion proof or
global optimality. The later open PR #667 reuses this same theorem, verifier,
and report; its branch-local report header incorrectly demotes the canonical
claim and contributes no new theorem. Since `m_B<=x_B`, its
`x_B=O(sqrt(D))` premise and the canonical finite inequality force
`liminf t_D>=(3pi+2sqrt(pi/(2sqrt(3))))/5=2.2658807149...`; hence the
additional `t_D<=1.860+o(1)` scope is empty. Type I and higher-surplus Type II
remain open.

The new [post-endpoint synthesis](target_c_hull_depletion_post_endpoint_synthesis_2026-10-04.md)
extracts the stronger physical frontier
\[
5m_B+4S+2\sigma_R
\ge
2\left(\pi+\sqrt{\frac{\pi}{2\sqrt3}}\right)D
+5k+2(Q-f)+2(b-P_F)-o(D).
\]
Thus \(Q-f\) and global outer detour are penalties rather than escape currencies.
Deleting singleton trains left after the hull-train depletion costs zero rhombi and
adds an additional \(5S_0\) to the right-hand side.

More importantly, the same finite ledger has the exact form
\[
2t_DD=M_D+3k+m_B+2u_B+2(Q-f)-d_D.
\]
Consequently every terminal sequence with \(q/D\to\pi\) satisfies
\[
\boxed{
\liminf t_D\ge
\frac{3\pi+2\sqrt{\pi/(2\sqrt3)}}5
=2.265880714899459\ldots.
}
\]
Therefore proof-only terminal-FREE near-floor regimes around \(t=1.96\), and any
terminal-FREE subcase imposing \(t\le2.02+o(1)\), have empty asymptotic antecedent
once #667 is admitted. Their finite conditional lemmas are not automatically false;
their former survivor scope is gone.

A linear \(m_B\) population, if forced in another live branch, still yields a
linear vertex-disjoint matching of loaded hull pairs of length \(1+o(1)\). These are
near-unit lower constraints, not the inverse-\(D\) near-diameter upper constraints
of PR #664; the direct \(m_B\to\)#664 bridge is explicitly rejected.

The exceptional-face second-depletion route remains conditional on proving
subquadratic rhombus incidence for the selected terminal family. The bounded-degree
small-residual side should be coupled to the recovered Groemer
near-contact/almost-triangle stack. On the persistent high-degree route of draft PR
#668, a normalized obstruction \(\lambda\) implies
\[
\frac{Q-f}{D}\ge\frac{\lambda}{10}-o(1),
\]
so the weighted frontier gains \(\lambda D/5\). Draft PR #671 supplies disjoint
loaded returns from a single sufficiently large convex face. The remaining global
bridge is a bounded-overlap tail-to-return charge or a direct finite replacement.

Run:
```bash
python3 research/verify_target_c_hull_side_train_capacity_2026_10_04.py
python3 research/verify_target_c_hull_depletion_post_endpoint_synthesis_2026_10_04.py
```

The synthesis verifier checks 102,496 exact ledgers and terminal bootstrap identities,
276,939 second-depletion substitutions, 1,397 high-degree-tail conversions, 2,040
cycle-edge matching cases, and exact rational enclosures for the displayed constants.
It does not certify the analytic depletion theorem, Groemer stability, the proof-only
claims of #668/#671, or global optimality.

## Terminal low-\(t\) frontier cleanup after #667 (2026-10-04)

The [terminal frontier supersession audit](target_c_terminal_low_t_frontier_supersession_2026-10-04.md)
propagates the exact post-#667 feasibility identity into the older terminal research
stack. Every full-core Type-II sequence with \(q/D\to\pi\) now satisfies
\[
\liminf t_D\ge
\frac{3\pi+2\sqrt{\pi/(2\sqrt3)}}5
=2.265880714899459\ldots.
\]

The constant has prior art: the September clean-endpoint report proves it under
(x_B=o(D)), and open PR #663 contains an equivalent exact all-unit-hull identity
whose (N_0/D\ge2\sqrt{\pi/(2\sqrt3)}-o(1)) consequence gives the same terminal
corollary after (q/D\to\pi). The #667 route is an independent proof and the
supersession audit records the resulting current frontier; no priority claim is made.

Accordingly, the old terminal FREE \(t\approx1.95\)--\(1.96\) gap theorems remain
useful provenance but are numerically superseded, while their structural descendants
whose own scope assumes a \(t\)-upper bound below \(2.26588\ldots\) have empty
asymptotic antecedent. The October high-\(t\), low-\(x_B\), square-root-matching
fan/collar chain at \(t\le1.860\) is likewise empty because that branch already has
\(q/D\to\pi\).

This cleanup is deliberately scoped: nonterminal bounded-\(t\) results such as the
modern \(t\le1.8623\) pentagon-sea theorem are **not** retired merely from the force-hull
disk limit, and the strong open-cell/deep-port routes #668/#671 remain live absent a
separate terminality theorem. Type I/macroscopic-container work is unchanged.

## Strong open-cell full-width anchor / canonical return fork (2026-10-04)

The independently audited [full-width anchor return report](../docs/reports/target_c_open_cell_full_width_anchor_return_fork_2026-10-04.md)
continues the proof-only strong open-cell host-cap branch without importing #668/#671
into its core theorem. A quadratic cap-local strict-rhombus grain of area \(A_G\)
inside one actual harmonic attachment cell forces two loaded attachments
\(a_*,b_*\) with
\[
|a_*-b_*|\ge A_G/D.
\]
Canonical Section 120 then gives the exact fork
\[
P_{{\rm exc},\cap}\ge(2-\sqrt3)A_G/D
\]
or
\[
L_\cap-2|a_*-b_*|\ge(2-\sqrt3)A_G/D.
\]
In the first branch canonical Section 123 yields
\[
e_{BB}-k\ge\frac{2-\sqrt3}{10}\frac{A_G}{D};
\]
in the second, one actual occurrence-counted outer route between the two loaded
attachments has excess at least
\[
\frac{2-\sqrt3}{2}\frac{A_G}{D}.
\]
The [independent audit](../docs/audits/target_c_open_cell_full_width_anchor_return_fork_audit_2026-10-04.md)
passes the Fubini width step, Section-120 cut-pair scope, route nonnegativity, and
Section-123 one-cell-to-global payment. The result remains conditional on the
unpromoted strong open-cell host-cap/harmonic-localization antecedent and does not
close C-II.



## 2026-10-05 — recovered salvage material

The following reports and verifier sources were copied from the exact source tips recorded in their reports and the preservation PRs. Every new claim remains unreviewed and noncanonical unless its report marks a regression or rejection. These additions do not change theorem state.

- The current-main `target_c_open_cell_quantitative_multishear_conditioning_2026-10-04.md` now adds a source-dependent local-isolation corollary for the exact laminar shear family. Its finite Taylor argument has no standalone verifier and gives neither a source-uniform bound nor a global C-II closure. Source: `automation/target-c-open-cell-strong-scc-multishear-rigidity-2026-10-04-v2` at `bd70618a69dae3664cefeb1275bfedde771eed78`.
- The current-main `target_c_open_cell_cut_divergence_condensation_2026-10-03.md` now includes the arbitrary-layer-set cut-divergence identity and endpoint KKT moment inequalities. It remains algebraic and does not prove geometric compatibility or a physical-source flex. Source: `worker-c/target-c-open-cell-arbitrary-ideal-flux-2026-10-03-v2` at `a6a1ab70937458e3ee5bc5dabc7aecbd918236dc`. The accompanying nested-chain dichotomy and exact checker cover two unequal strict interval chains for `m<=6`; run `python3 research/verify_target_c_two_nested_chain_condensation_2026_10_03.py`.
- The mixed-phase full-flower packet is summarized in `../docs/reports/target_c_mixed_phase_full_flower_allocation_2026-10-04.md`. Run `python3 research/verify_target_c_full_flower_nested_orbit_allocation.py`, `python3 research/verify_target_c_three_dominant_flower_through_pair.py`, `python3 research/verify_target_c_mixed_flower_matching_splice_deficit.py`, and `python3 research/verify_target_c_mixed_flower_half_matching_upgrade.py`. These check the displayed finite allocation, matching, and arithmetic cases; they do not establish a diameter-feasible source motion or global optimality. Source: `sol/c2-flower-blocker-20260915` at `95013b579895183089c4d2b3f0962588eda6abcd`.
- The full-flower cell-purity and escape-or-flex candidates remain conditional on the explicitly unpromoted Section-129 localization premise. Run `python3 research/verify_target_c_full_flower_escape_or_flex.py` for the finite arithmetic table only. Source: `research/c2-flower-high-t-sol-20260915` at `7de4cdc3e9aa0cac5b278c2ccc17158bd8d66bdb`.
- The full-settlement reports preserve antitone interval-SCC release, exclusive fan ports, conditional Target B endpoint/descent claims, and a rejected two-unit-side sharpening with its even-polygon counterexample. Run `python3 research/verify_target_c_antitone_interval_scc_2026_10_03.py`, `python3 research/verify_target_c_exclusive_fan_ports_2026_10_03.py`, `python3 research/verify_target_b_zero_gradient_descent_2026_10_03.py`, `python3 research/verify_target_b_zero_gradient_cubic_corrector_2026_10_03.py`, and `python3 research/verify_target_c_completion_two_unit_side_regression.py`. The scripts check finite encodings and scalar implications, not the geometric hypotheses or a global minimizer. Sources: `research/full-settlement-20261003` at `c044a07f59dbe0993d69c801f73a21f1927838b0` and `research/full-settlement-collar-20261003` at `bc52d9f5153c8c936fd3fbf96f755c8d57bbee86`.
- The good-end outer-walk tradeoff checker is `python3 research/verify_target_c_fan_train_tradeoff_2026_10_03.py`; it checks the bounded integer ledger only, not the analytic geometry. The associated source is `research/full-settlement-collar-20261003` at `bc52d9f5153c8c936fd3fbf96f755c8d57bbee86`.
- The flat-pentagon reports retain a scoped infinitesimal hidden-derivative rank reduction. Run `python3 research/verify_target_c_empty_pentagon_trapezoid_endpoint.py`, `python3 research/verify_target_c_flat_pentagon_hidden_derivative_rank.py`, and `python3 research/verify_target_c_flat_pentagon_hidden_derivative_rank_refinement.py`. They check finite geometry/algebra and scalar rank arithmetic; they do not verify compactness hypotheses, a common shortening sign, or a diameter-feasible motion. Source: `research/c2-certified-minimax-rank-sol-20260915` at `5c3f54443aff670813134251883b7dc1a6c5b19e`.

## 2026-10-05 — Target B lattice-source candidates

`docs/reports/target_b_uniform_lattice_flex_2026-09-25.md` records an unreviewed
flexibility result for finite subsets of a planar lattice with minimum spacing at
least one, excluding the unit triangular lattice. The result does not construct a
strict smaller-diameter competitor.

`docs/reports/global_unit_hull_lattice_boundary_loss_2026-09-26.md` records an
unreviewed strict-competitor candidate for one near-exact lattice chart and stated
physical-grain/interface hypotheses. It does not settle the multi-grain seam ledger
or the Target B joint shell-stability inequality.

Exact arithmetic/regression command:

```bash
python3 research/check_unit_hull_lattice_boundary_loss.py --exact

The recovered `--seam-pilot` option is a NumPy-based floating-point phase-grid scan. It is exploratory and does not certify the asymptotic seam claim.
```

This checks the encoded rational margins and identities only. The `--numerical` and
`--seam-pilot` modes use floating-point searches and are exploratory; neither is a
proof certificate or a dependency of the analytic claims. The stored JSON pilot is
likewise floating-point evidence. No theorem state or route status changes.
## Slot 2 C-II research shard recovery (2026-10-05)

A single fresh-main consolidation preserves distinct research artifacts from the 90-ref SHA-256 8-f shard. It imports 485 previously missing research files (303 reports, 180 Python verifiers, 2 C++ scans), plus two hostile audits, one exact-phase report, one superseded Target C module under `research/legacy_target_modules/`, and three finite H6 scan programs with two stored outputs. The H6 scan counts and limits are summarized in `target_c_h6_finite_reflection_scan_2026-09-19.md`. Exact source tips and per-file version selection are recorded in `target_c_c2_structural_salvage_provenance_2026-10-05.md` and `cleanup/slot2-8f-ref-artifact-map-2026-10-05.tsv`. These are unreviewed discovery artifacts; the copied verifier programs are not registered as theorem certificates and none of this changes the active route or theorem state.

## Support-seven finite profile reductions (2026-10-05)

These proof-only artifacts preserve exact support-level reductions that were absent
from current main. They do not change theorem state or close Target C-II. The finite
scripts certify only their encoded support, orientation, or rank enumeration; they do
not prove that every geometric source induces an encoded state. The nine-no-root
`k=4, D=-1, p=2` orientation audit records an executed computation whose verifier
source was not preserved, so it remains a research lead rather than a reproducible
certificate.

Preserved reports: `target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_mixed_local_rank_repair_2026-09-27.md`, `target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_three_singleton_r1_incidence_sharpening_2026-09-27.md`, `target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_three_singleton_r2_quotient_h19_2026-09-27.md`, `target_c_k4_p3_weight2_unmatched_localization_2026-09-26.txt`, `target_c_nine_noroot_k4_dminus1_p2_orientation_audit_2026-09-28.md`, and `target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_support_narrowing_2026-09-28.md`.

Run `python3 research/verify_target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_weight2_unmatched_localization_2026_09_26.py`, `python3 research/verify_target_c_h5_m3_two_singleton_promotion_2026_09_25.py`, and compile/run `research/verify_target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_mixed_local_rank_repair_2026_09_27.cpp`. Source refs: `target-c-eight-k4-p3-mixed-local-rank-repair-20260927` at `8e2f48ec75df2164ef3612b0854c3ea1a008ab73`; `target-c-eight-k4-p3-r1-incidence-sharpening-20260927` at `98fdcf89ab76158077e73a0356158deca149bfd0`; `target-c-eight-k4-p3-r2-quotient-h19-20260927` at `6f73e54162290dfec7288cd56545c9f94d89ff3f`; `target-c-eight-k4-p3-weight2-unmatched-localization-20260926` at `18c72d55ec70c93654956b9b0567a136d72bb8a9`; `target-c-h5-m3-promotion-verifier-20260925` at `e804868b22c60bce4eec59bcad7523837e21270a`; `target-c-nine-k4-dm1-p2-support-narrowing-20260928` at `ae8ebb5ee759c1b6a8f60677018dececf4d30d57`.

## 2026-10-05 — recovered subset-reflection hostile audit

`docs/reports/target_c_subset_reflection_independent_hostile_audit_2026-10-02.md`
records an independent audit of PR #614. It retains the finite packet only at its
stated nonempty-cut, narrow-span, empty-cell scope; the source application remains
conditional. Its open-cell reduction is an unreviewed candidate, and the exact
contact-grid construction is a regression against deriving closure from one-shore
aggregate force. It does not supply full-source KKT or global optimality, and makes
no canonical theorem-state change.

Run `python3 research/verify_target_c_subset_reflection_hostile_audit_2026_10_02.py`
for exact-rational source-pair, contact, cut-resultant, rank, reflection, diameter-sign,
and small antitone-tree checks. The script certifies those encoded finite objects only.
It does not verify the general open-cell proof or any global-minimizer hypothesis.
Recovered from local-only branch `audit/c2-subset-reflection-20261002` at
`a36a12d60e768ddd68ec3db8267621e22765432e`; the untracked source report and verifier
had SHA-256 `7fb8a9fcc33b32fcbb815af3935648e19189e73f44e9ecd26c4707d0f9bb2e9d` and
`38f9e1b2c6b02decf13ae0d06033ff445894e267101afcc4e7dd53e583673ced` respectively.

## Target C finite checks recovered from local worktrees (2026-10-05)

- `python3 research/verify_convex_shared_witness_outer_occurrences.py` checks the encoded two-edge shared-witness geometry, 91 source pairs, local binary states, ordered unit-chord moves, contact balance, and the stated finite diameter regression. It does not check canonical source hypotheses, a full-source KKT framework, or global optimality.
- `python3 research/verify_contact_arc_threshold.py` uses exact rational arithmetic for the regular hexagon and near-60-degree crossed chains at the displayed finite parameters. It does not certify the analytic threshold for all selected supports or global optimality.
- `python3 research/verify_target_c_star_ray_hostile_audit_2026_10_01.py` checks the finite cycle-order family and recovered exact star-ray/endpoint examples. It does not establish an arbitrary-size ordering theorem, actual global train cuts, full-source KKT, or global optimality.

These checkers certify only their encoded finite statements; their associated reports remain unreviewed research artifacts.

## Good-hull singleton face-charge candidate (2026-10-05)

The report is preserved at `docs/reports/target_c_good_hull_singleton_face_charge_2026-10-05.md`. It presents a finite good-hull singleton charge and combines it with the stated full-core Type-II hull-depletion identity. It has no standalone verifier and remains unreviewed/noncanonical. The source report was based on main b9, before the later `audit.52` promotion; recheck its exact hypotheses against the current Target C route before use. It does not settle C-II globally or prove a strict same-cardinality diameter improvement.

## Full-flower blocker k-payment candidate (2026-10-05)

The report is preserved at `docs/reports/target_c_full_flower_blocker_k_payment_2026-10-05.md`. It is a proof-only composition for the full-core Type-II branch and has no standalone verifier. The source branch was last updated at `849b9553`, based on main `cd5fabd6`; recheck its hypotheses against the current `audit.52` Target C route before relying on it. It remains unreviewed/noncanonical and does not close C-II or Level I.

## Contact-manifold local diameter coordinates (2026-10-05)

The report is preserved at `docs/reports/target_c_contact_manifold_local_diameter_coordinates_2026-10-05.md`. It derives local diameter excess coordinates and a point-dependent obstruction to keeping all old active diameters nonincreasing, under its stated audit.52 full-core hypotheses. It has no standalone verifier and remains unreviewed/noncanonical. Current main is audit.54; verify the dependencies against the current route before use. It does not close C-II or prove a global same-cardinality competitor.

## Target C zero-valid pinned 2-CNF closure (2026-10-07 Audit.99)

`python3 research/verify_target_c_zero_state_horn_closure_2026_10_05.py`
checks all 4,131 zero-valid formulas through three variables against complete
truth-table enumeration over 110,887 pinned instances. It also checks sink-SCC
classification and finite harmless-cycle/blocking-fork examples. The script
uses exact Boolean operations. The arbitrary finite-variable closure theorem
is proved analytically in
`docs/audits/target_c_zero_valid_pinned_closure_independent_audit_2026-10-07.md`;
the enumeration is a finite regression, not its proof. It does not encode
source geometry, owner extraction, a shortening diameter state, C-II closure,
or Level I closure. The source application is only conditional on the
separately stated hypotheses of canonical `C-DISJOINT-SWAP-2SAT`.


## Target C isolate-anchor localization (2026-10-07 Audit.100)

The independent audit in
`docs/audits/target_c_generic_isolate_anchor_avoidance_independent_audit_2026-10-07.md`
promotes four analytic results extracted from the proof-only
`target_c_generic_isolate_anchor_localization_2026-10-05.md`: generic isolate
perturbations avoiding unit-circumradius triples; the weak-clearance equality
case for short walls; the strictly obtuse geometry of three loaded unit
anchors for `D>=10000`; and the resulting unloaded-core-anchor requirement
for a locally pinned static singleton. No verifier is claimed. No result gives
a site, packet capacity, simultaneous move, or C-II closure. The report's
separate degree-three reflection argument remains unaudited.

## 2026-10-06 independent Target C owner/terminal/wall audit

The following exact checkers accompany `docs/audits/target_c_owner_order_and_terminal_capacity_promotion_audit_2026-10-06.md`:

- `verify_target_c_hub_owner_systems_2026_10_06.py` checks integer-tree counts, owner labels, Boolean Horn truth tables, and abstract packet counts. It verifies finite encoded combinatorics only; it supplies no source geometry, KKT equilibrium, motion, or optimality.
- `verify_target_c_terminal_oo_geometry_2026_10_06.py` checks rational two-edge-pocket angles/determinants, positive-cone sign cases, exact terminal-ledger identities, and a long-pocket regression. It does not certify the asymptotic compactness or the analytic full-source shore argument. The long-pocket fixture is registered as C-TERMINAL-LONG-POCKET-ANCHOR-REGRESSION and only blocks extending the short-pocket determinant bound from local geometry.
- `verify_target_c_binary_crossing_scope_2026_10_06.py` checks exact rational distances in coupled train and independent-owner states for one strict rhombus. It establishes that finite scope regression only.
- `verify_target_c_one_vertex_wall_shield_2026_10_06.py` checks the six-edge packet in the exact field Q(sqrt(808669)) and the two-deletion isolate regression rationally. The universal one-vertex shield and five-edge impossibility are analytic, not sampled.

All arithmetic comparisons in these verifiers are exact. Their finite outputs do not establish a source realization or global optimality beyond the separately audited arguments. Run each with `python3 research/<script>.py`.

## Target C one-corner, one-vacancy packet (2026-10-07 audit)

`verify_target_c_one_corner_vacancy_packet_2026_10_06.py` reads exact rational axial velocity data from `target_c_one_corner_vacancy_velocity_certificate_2026_10_06.json`, constructs the specified curved walls in Q(sqrt(3)), and checks the encoded strict packets and wall-plus-center source exchanges for M=3,4,6. It checks 489 exact first-variation inequalities, 9,072 inserted-pair upper constraints, 1,137 old-source pairs, 1,137 endpoint pairs, and 144 integer population choices. Its helper imports are preserved in `verify_target_c_three_direction_corner_barrier_2026_10_06.py` and `verify_target_c_nested_hexagon_packet_stress_2026_10_06.py`.

The finite checker does not prove the all-M no-positive-stress peeling, the all-M Farkas direction, arbitrary-source shield application, uniform curvature onset, or wall extraction. Those analytic arguments and their scope are in `docs/audits/target_c_one_corner_one_vacancy_independent_audit_2026-10-07.md`. Oler's bound is from canonical `docs/theory/03-oler-shell.md`, Lemma 21.1. The resulting source exclusion only covers z<=N-2; the strict-area Oler bound leaves z=N-1 or N. No C-II or Level I closure follows.

## Target C sorted-rate energy equality (2026-10-07 audit)

`verify_target_c_sorted_rate_packets_2026_10_06.py` checks 14 exact sorting packets in Q(sqrt(3)) for M=3,4,5,6: 37,773 full-pair distances, 2,412 first-row inequalities, 1,016 subset sums, all nested-ring energies, and sampled pinned ranks modulo 1,000,000,007. The saved certificate records the finite outputs. The all-M and all-permutation result comes from the explicit analytic construction in `docs/audits/target_c_sorted_rate_energy_equality_independent_audit_2026-10-07.md`, not from extrapolating the samples.

These finite packets contain exact unit triangles, including after the center is omitted for M>=3. They disprove a strict nested-energy gap under only the physical unit-lower and six-guard hypotheses. They are not triangle-free sources, global minimizers, or evidence for the source report's broader local classification or highest-population exclusion.

## Target C highest-population Oler equality limit (2026-10-07 audit)

This result has no computational certificate. It follows from fixed-M compactness, the exact count `N+6M=3M^2+3M+1`, equality in Oler's bound for the limiting regular hexagon, and the Thue–Groemer equality case recorded in the cited Böröczky-Ruzsa transcription. The coordinate scaling from radius-one disks with center spacing two to unit-separated points is recorded in `docs/audits/target_c_six_sided_wall_oler_high_population_limit_independent_audit_2026-10-07.md`. It localizes `z=N` sequences to `P_(M-1)` but gives no finite-curvature classification or triangle conclusion.

## Target C flat one-vacancy pinning/rate audit (2026-10-07)

`verify_target_c_one_vacancy_flat_pinning_2026_10_07.py` checks the exact integer equilibrium formula and triangle-propagation pinning certificate for every interior vacancy in `H_M`, `M=2,...,10`: 999 vacancies and 178,002 moving-vertex equilibrium checks. It also checks axial triangle determinants exactly. Its saved output is `target_c_one_vacancy_flat_pinning_certificate_2026_10_07.json`. The script verifies finite lattice charts only; the universal rank proof and `O(theta)` rate in `docs/audits/target_c_one_vacancy_flat_pinning_rate_independent_audit_2026-10-07.md` are analytic. It does not establish extraction from a canonical source, strong solidity, a curved-wall finite motion, or global optimality.

## Target C funded unit-wall activation audit (2026-10-09)

`verify_target_c_vacancy_funded_unit_wall_activation_2026_10_05.py` uses exact rational and `Q(sqrt(3))` arithmetic for four triangular two-interior-hole release fixtures, six guarded source-replacement fixtures, two one-vacancy strictification fixtures, one pinned-stress fixture, and crossing/noncrossing examples. The rerun checks 7,016 sequential-move pairs, 282 final strict interior pairs, and 15,244 full old/new source pairs; it records 83 lost contacts. It verifies only those finite fixtures and encoded inequalities. The general release order, wall-capacity population theorem, exact oblique wall consequence, and global/contact-minimality implications are proved analytically in [`target_c_funded_unit_wall_activation_independent_audit_2026-10-09.md`](../docs/audits/target_c_funded_unit_wall_activation_independent_audit_2026-10-09.md). The script is not registered as a theorem certificate because it does not certify those universal steps or a global-minimizer instance.

## Target C one-deficit root packets (2026-10-07)

`verify_target_c_one_deficit_symbolic_opening_2026_10_07.py` and its exact basis `target_c_one_deficit_opening_basis_M4_2026_10_07.json` certify positive Laurent leading coefficients for all 92 interior-involving unit rows in the punctured M4 chart for every sufficiently small `t=tan(theta/2)>0`; the saved output is `target_c_one_deficit_symbolic_opening_certificate_2026_10_07.json`. The checker uses exact rational-function arithmetic over `Q(sqrt(3))` with tracked truncation remainders. The analytic root/support argument and full-source shield application are in `docs/audits/target_c_one_deficit_root_packet_independent_audit_2026-10-07.md`.

`verify_target_c_one_deficit_strict_root_packet_2026_10_07.py` checks the five exact cases in `target_c_one_deficit_strict_root_velocity_certificate_2026_10_07.json` and saves `target_c_one_deficit_strict_root_packet_certificate_2026_10_07.json`. It rebuilds the exact sorting chart at each explicit half-angle parameter, then verifies every exact contact-opening margin, all new lower and upper pair bounds, wall containment, and retained-wall clearance in `Q(sqrt(3))` with rational amplitudes. This audit copy keeps the explicit-parameter geometry local rather than relying on a noncanonical update to the shared sorted-rate helper. A floating value is used only to select a candidate wall diameter; exact pairwise comparisons then certify that maximum. Finite cases do not prove a small-curvature onset for `M=5,6,8` or any arbitrary-M result.

## Target C all-M one-deficit audit (2026-10-07)

`verify_target_c_one_deficit_sector_peeling_audit_copy_2026_10_07.py` checks the exact contact-row peeling and strict-opening construction for arithmetic profiles at `M=3,...,10`, `t=1/10000`; it records the M3 method stall and does not assert that no packet exists there. `verify_target_c_one_deficit_nonuniform_profiles_2026_10_07.py` checks two nonuniform symmetric profiles at M=4 and M=6, including every chart pair, opening row, inserted lower/upper pair, and wall support in `Q(sqrt(3))`. The strict-root verifier reproduces the listed exact-curvature packets. These computations are finite checks only. The all-fixed-profile root, packet, and full-source exchange claims are proved analytically in `docs/audits/target_c_one_deficit_sector_peeling_independent_audit_2026-10-07.md`; they do not extract a wall from an arbitrary canonical source or close C-II.

## Target C exact one-deficit diffuse-strain regression (2026-10-08)

`verify_target_c_one_deficit_diffuse_strain_2026_10_07.py` checks exact old-source and equal-cardinality square-grid pair ledgers for `M=3,4,7,10` using rational signs in `Q(sqrt(M^4-6M^2-3))`; its output is saved in `target_c_one_deficit_diffuse_strain_certificate_2026_10_07.json`. It verifies those finite separation/contact/diameter cases only. The all-`M` spacing, Oler-slack, disk-cover, Delaunay, and strict sub-diameter arguments are reconstructed in `docs/audits/target_c_one_deficit_diffuse_strain_independent_audit_2026-10-08.md`. The family is nonglobal and proves no container-capacity, canonical-source, or Level I statement.

## Target C fixed-profile highest-population classification (2026-10-07)

`verify_target_c_profile_sorting_packets_2026_10_07.py` reproduces the exact
finite certificate `target_c_profile_sorting_packets_certificate_2026_10_07.json`.
It checks prefix and suffix-extension identities for all permutations of four
distinct symmetric integer profiles, then verifies 11 exact sorting packets in
`Q(sqrt(3))`: 43,110 pair distances, 1,800 unit contacts, strict wall
containment, first-ring unit triangles, and full limiting rank by exact modular
minors. The certificate checks finite formula instances only.

The all-profile maximum-population classification depends on the analytic
first-order permutahedron, central-energy equality, positive-stress
continuation, and scale-correct local isolation proved in
`docs/audits/target_c_profile_wall_sorting_classification_independent_audit_2026-10-07.md`.
The script does not prove those steps, arbitrary-cloud classification,
canonical-source optimality, arbitrary-wall extraction, C-II, or Level I.


## Target C profile principal-stress correction (2026-10-07 audit)

`verify_target_c_profile_first_stress_correction_2026_10_07.py` checks 14
listed exact first-order stress corrections and full-rank minors; its input
coefficients were discovered numerically and then exactly projected, while
the verifier itself uses exact rational arithmetic. It does not verify the
separate all-profile coefficient formula.

`verify_target_c_principal_stress_formula_audit_2026_10_07.py` implements
that explicit formula directly and checks four symmetric integer profiles at
M=3,4,5,6: all limiting active row classes, both force identities, positive
weak diagonal coefficients, and modular full column rank. Its output is
`target_c_principal_stress_formula_audit_certificate_2026_10_07.json`.
The universal coefficient identity and fixed-profile continuation are proved
analytically in
`docs/audits/target_c_profile_first_stress_correction_independent_audit_2026-10-07.md`;
finite checks do not give a uniform onset in M or profile and do not close C-II.

## Target C face-coupled quarter-fold regressions (2026-10-07 audit)

`verify_target_c_face_coupled_quarter_folds_2026_10_07.py` exactly enumerates quarter-fold sign states for a regular unit hexagon, a rectangular eight-site perimeter, and rational rhombic grids with M=2,3,4. Coordinates and squared-distance ledgers use `Q(sqrt(3))` or rational arithmetic; the full finite pair and sign spaces are checked. The saved output is `target_c_face_coupled_quarter_folds_certificate_2026_10_07.json`. Its floating maximum-key nomination is followed by exact comparisons against every pair. These examples show that weighted diameter-mean decrease can coexist with lower collisions, that an inactive pair can replace a shortened old diameter, and that convex faces can admit four-transition parallelogram patterns.

This verifier proves only the enumerated finite examples. It does not prove arbitrary face integration, the stress identity, the universal convex-face classification, existence of any feasible nonaffine state in a canonical source, global optimality, C-II, or Level I. Those analytic statements and their exact scope are in `docs/audits/target_c_face_coupled_quarter_fold_independent_audit_2026-10-07.md`.

## Target C bent-grid positional transport regression (2026-10-07 audit)

`verify_target_c_bent_grid_transport_2026_10_05.py` uses exact `Q(sqrt(3))`
arithmetic to check every pair for `M=8,12,16`: grid contacts, strict
noncontacts, contact counts, the rational midpoint bow, and total rhombus-area
excess. Its default run checks 59,052 pairs; the same checks were also run at
`M=10`. The infinite family, positive pinned equilibrium, full pinned rank,
phase bound, and uniform single-lattice positional obstruction are proved
analytically in
`docs/audits/target_c_bent_grid_positional_transport_independent_audit_2026-10-07.md`.

The checker certifies only the listed finite arithmetic. Boundary pins are not
certified actual diameter endpoints, and neither the family nor its boundary
conditions establish global minimum-diameter optimality. The regression does
not rule out bounded multiple-lattice covers or refute covers of canonical
loaded endpoint sets.

## Target C exterior loaded-tip exact checks (2026-10-07 audit)

`verify_target_c_exterior_loaded_tip_pairing_2026_10_06.py` uses only Python
`Fraction` arithmetic and reproduces
`target_c_exterior_loaded_tip_pairing_certificate_2026_10_06.json`. It checks
the right-angle tip opening, one exact half-turn unit-path pin, and the shared
loaded-tip collision for chain lengths 26 and 40; all old and replacement pair
distances and contact/triangle ledgers are exact. The script checks finite
examples only. It does not prove the universal hull-tip shield, cell structure,
acute-tip theorem, paired cross-cell gluing, canonical cap extraction, or global
optimality; those analytic claims are audited separately in
`docs/audits/target_c_exterior_hull_cell_and_tip_capacity_independent_audit_2026-10-07.md`.

## Target C common-angle hexagon and isolate regressions (2026-10-07 Audit.95)

`python3 research/verify_target_c_common_angle_train_endpoint_2026_10_06.py`
uses exact `Q(sqrt(3))` arithmetic. It enumerates all 64 independent side-bit
patterns, finds the ten closed patterns and their meet-closure failure, checks
300 core lower-distance comparisons at `tan(theta/2)=+/-1/10`, and verifies
420 pair-change identities including a retained isolate. It also checks all
15 strict upper comparisons for the six-point alternating core move and the
exact increase `(20*sqrt(3)-18)/101` in the old diameter pair when an isolate
is retained. The deterministic output is
`research/target_c_common_angle_train_endpoint_certificate_2026_10_07.json`.

The script does not check lower feasibility of every isolate-to-core pair
after the seven-point move; that result is only an upper-bound regression. It
does not establish that a canonical source has these independent side bits,
that any larger train network has a non-Horn assignment relation, global
optimality, C-II closure, or Level I closure.


## Target C capped-wall actual-diameter escape (2026-10-07 Audit.96)

`python3 research/verify_target_c_capped_wall_actual_diameter_escape_2026_10_06.py`
uses directed rational intervals at scale `10^24` to check two entire
triangle-free grid/cap packets: 649 points and 1,232 contacts at `M=24`, and
1,145 points and 2,176 contacts at `M=32` with outward leaves. It checks every
old and moved pair, the complete contact graph, unique actual diameter pair,
strict lower feasibility, and strict decrease of the actual diameter. Its 380
exact box-polynomial endpoint checks certify the upper box bound for all real
`M>=24` and `cos(phi)` in `[49/100,1/2]`; the conditional motion theorem is
proved analytically in the independent audit. The script checks the two exact
source realizations only. It does not establish that the stated contact set
occurs for every cap selection, extend motion through outside source points,
prove global optimality, or close C-II/Level I. The captured output is
`research/target_c_capped_wall_actual_diameter_escape_certificate_2026_10_07.json`.

## Target C fan-reflection strict-capacity-loss regression (2026-10-07 Audit.101)

`verify_target_c_fan_octagon_capacity_loss_2026_10_05.py` uses rational
arithmetic in `Q(sqrt((1-e^2)(1-a^2)))` and exact sign comparisons to certify
all 45 old and 45 reflected source-pair distances, the contact and actual
diameter sets, the single lower collision, and the unit-circumcircle cover
bounds for five values of `D`. The independent audit proves the full real
family for every `D>=10` by analytic inequalities and the circumradius cover
argument. The script verifies finite instances only. The source is nonglobal,
has an eight-cycle contact core plus contact isolates, and does not satisfy
canonical full-core optimality hypotheses or assert positive KKT stress; it
does not decide unrestricted isolate relocation or C-II/Level I. See
`docs/audits/target_c_fan_reflection_capacity_loss_independent_audit_2026-10-07.md`.

## Target C coupled Delaunay container crop (2026-10-07 Audit.108)

Run python3 research/verify_target_c_coupled_container_crop_2026_10_07.py.
It uses exact Fraction arithmetic in Q(sqrt(3)) to check six explicit
triangular and rational-rhombic lattice crops at M=7,13,25. It checks the
finite pair-distance geometry, strip and deep-vertex classifications,
boundary-edge/component/Euler counts, Oler allowance, triangle excess, and
crop currency bound. These are finite examples only; the verifier does not
prove the universal completion, arbitrary-convex-container, tube, Euler, or
local Delaunay estimates. Those analytic statements are independently
reconstructed in
docs/audits/target_c_coupled_delaunay_container_transfer_independent_audit_2026-10-07.md.
The theorem does not assert a source-realized packet, global minimizer, or
strict diameter improvement.

## Target C finite hinge and heptagon stress regressions (2026-10-08 Audit.122)

Run `python3 research/verify_target_c_finite_core_rigidity_2026_10_02.py`.
The exact verifier checks a rank-five two-vertex hinge and a labeled seven-point
triangular-lattice replacement for a regular unit heptagon, including every
pair distance, the preserved cycle contacts, the old diameter lengths, and
the strict weighted gain. It also retains exact finite checks for the square
and normalized-interpolation examples audited earlier. The heptagon stress
spectrum and the mixed-framework rigidity argument are analytic in the
independent audit; the finite checks do not assert global optimality, which is
explicitly false for the heptagon, or any C-II/Level I conclusion.

## Target C positive pinned face-tail regression (2026-10-08 Audit.123)

Run `python3 research/verify_target_c_positive_pinned_face_tail_2026_10_04.py`.
The exact `Fraction` verifier checks all source pairs in four packets
`L=12,16,24,32`, the contact/diameter sets, hull pins, positive equilibrium,
and explicit pinned rigidity minors, plus a same-cardinality grid competitor.
The verifier does not prove the infinite family or the limiting face-tail
ratio; those are derived analytically in the independent audit. The sources
are nonglobal and lack full-source positive KKT stress, so the regression does
not address canonical loaded Type-II sources or Level I.

## Target C monotone route debit and local regressions (2026-10-08 Audit.124)

Run `python3 research/verify_target_c_monotone_cap_routes_2026_10_04.py`.
The frozen exact verifier checks 6,966 source pairs in finite rational oblique
grids, 100 greedy routes and overlap multiplicity, 56 augmented pocket-face
walks and clipped-height ledgers, ten Pell identities, and the exact
`61/101` attachment-triangle debit. The independent audit proves the global
analytic route-debit bank from canonical ZRF and Section 123, and derives the
all-member Pell-family displacement and sharpness formulas. The verifier does
not check that analytic theorem, the full unbounded Pell grids, the proof-only
host-cap co-location premise, global optimality, or a source competitor. The
two local regressions do not refute a canonical source or Level I.

## Target C all-unit-hull finite depletion and pentagon regression (2026-10-08 Audit.125)

Run `python3 research/verify_target_c_all_unit_hull_end_currency_2026_10_04.py`.
The exact field verifier checks all pair distances, contact graphs, plane face
walks, hull support, train decompositions, and the finite train ledger in six
fixtures, including a 15-point pentagonal flower with five distinct trains
ending at actual unit hull sides. It does not encode the analytic annular
angular-defect bound, establish global optimality, or assert a canonical-source
motion. The flower is a local capacity regression only; the analytic finite
bound is reconstructed in
`docs/audits/target_c_all_unit_hull_end_finite_bound_independent_audit_2026-10-08.md`.

## Target C inactive near-diameter cubic budget (2026-10-08 Audit.126)

Run `python3 research/verify_target_c_inactive_diameter_cubic_moment_2026_10_04.py`.
The exact verifier checks three rational nonglobal source fixtures, 7,007
source-pair relations, 647 rational algebra checks, all 1,100 simple graphs
through five vertices, 39,675 finite cover checks, and 3,300 matching checks.
It does not certify the constant-width completion, analytic support-energy
argument, global cubic bound, asymptotic packet matching, phase-purity theorem,
or the all-D inactive-star family; those are reconstructed in the independent
audit. The THIN synchronized-row application remains conditional on unpromoted
packet and thinning inputs. The exact inactive-star fixtures are nonglobal and
do not refute any global-minimizer theorem.

## Target C universal unit-pentagon capacity (2026-10-08 Audit.162)

Run `python3 research/verify_target_c_unit_pentagon_capacity_2026_10_05.py`.
The exact polynomial check verifies the five-point radial distance identity;
the rational checks verify the triangle-case Oler margin, the linear chord
bound endpoints, and all ten pair distances plus four hull edges in the sharp
quadrilateral-boundary example. The universal perimeter lower bound,
strict-perimeter monotonicity, unique five-point packing, and deletion deficit
are analytic in
`docs/audits/target_c_unit_pentagon_perimeter_capacity_independent_audit_2026-10-08.md`.
The certificate does not establish a source-level replacement, exterior
isolate clearance, diameter upper bounds, or C-II/Level I closure.

## Target C full-source Voronoi spacing debit (2026-10-08 Audit.163)

Run `python3 research/verify_target_c_voronoi_spacing_debit_2026_10_08.py`.
The exact verifier checks six rational/quadratic-field grids, all source and
competitor pair distances, clipped Voronoi-cell coverage and area ledgers,
finite near-isolation surplus fixtures, the regular-hexagon equality fixture,
and exact spacing-debit arithmetic. It checks finite instances only; the
universal hull-coverage, angular-area, Voronoi-surplus, full-source population,
and Oler claims are analytic in
`docs/audits/target_c_full_source_voronoi_spacing_debit_independent_audit_2026-10-08.md`.
The verifier does not establish global optimality, bound all contact isolates,
or imply a C-II source move or refill.

## Target C full-source Delaunay strain and lower blockers (2026-10-08 Audit.164)

Run `python3 research/verify_target_c_full_source_delaunay_budget_2026_10_08.py`.
The exact verifier checks six rational/quadratic-field oblique grids, all
source and square-competitor pairs, clipped Voronoi cells, empty circumcircles,
Delaunay face and mixed-edge counts, the area ledger, six-neighbor and blocker
fixtures, finite lower-closed fronts, and a hull-covered thin-boundary-triangle
regression. It verifies only finite fixtures; the universal strain, exception,
blocker, and support-front bounds are analytic in
`docs/audits/target_c_full_source_delaunay_strain_independent_audit_2026-10-08.md`.
No fixture is globally optimal, and the results imply no common phase, source
move, or C-II/Level I closure.

## Target C translated-lattice population reserve (2026-10-08 Audit.165)

Run `python3 research/verify_growing_lattice_population_reserve_2026_10_08.py`.
The exact arithmetic checks the doubled-mode phase separation, the NIST
remainder margin at `z=8`, rational bounds for pi and sqrt(3), and the stated
constant comparison. Its separate finite-patch check enumerates 1,280
rational translations over radii 10, 20, 50, 100, and 200, certifies row
membership and 192,306 lattice points, then verifies strict expansion,
containment, and a smaller same-cardinality lattice competitor for those
finite patches. It does not prove the universal Fourier estimate, the NIST
remainder theorem, or global optimality of any patch. The universal
`g_A >= 3^(5/4)*sqrt(D)/(256*pi)` bound is analytic in
`docs/audits/target_c_lattice_population_reserve_independent_audit_2026-10-08.md`.
The estimate is a necessary global population reserve only; it yields no
source motion, C-II closure, or Level I conclusion.

## Target C circumcircle blocker depth and fan forest (2026-10-08 Audit.166)

Run `python3 research/verify_target_c_half_depth_fan_forest_2026_10_08.py`.
The exact `Fraction` checker verifies the piecewise circumcircle quadratic
identities over 966 rational parameter cases, samples 261,916 valid source
cross-pairs (including 102,148 distance-increasing moves), checks nine sharp
four-point threshold fixtures against all source pairs and square competitors,
and reconstructs six finite circular-arc fan sources and their full pair,
hull, contact, diameter, independent-set, and local fan-balance data. The arc
fixtures are nonglobal and have no normalized full-source KKT stress. These
finite checks do not prove the universal cap, closure, hull-forest, or stress
claims. Those follow analytically in
`docs/audits/target_c_half_depth_fan_forest_independent_audit_2026-10-08.md`.
No path-disjointness, shared payment, population lower bound, C-II closure, or
Level I conclusion follows.

## Target C odd-shell folds and fixed-cloud regression (2026-10-08 Audit.167)

Run `python3 research/verify_target_c_two_wave_shell_fold_2026_10_08.py` and
`python3 research/verify_target_c_shell_fold_collar_transport_2026_10_08.py`.
Both checkers use exact polynomial contact identities and directed rational
interval arithmetic inherited from the canonical Audit.65 checker. They
certify the stated finite pair relations at `q=65,101,201`, including every
wall pair, every old/new collar pair for the transport endpoint, every cyclic
fixed-cloud fold obstruction, and the listed deep triangular-lattice clouds.
All distinct lattice cloud pairs follow from a positive integral lattice norm,
not pair sampling. The scripts do not prove the universal-in-q inequalities,
the generic clearance-cloud theorem, or any global optimality statement; those
claims are analytic and their exact scope is in
`docs/audits/target_c_odd_shell_folds_independent_audit_2026-10-08.md`.

## Target C centered-cap sharpness and common-trunk regression (2026-10-08 Audit.168)

Run `python3 research/verify_target_c_cap_closure_path_congestion_2026_10_08.py`.
The exact `Fraction` verifier reconstructs the full source pair, contact,
diameter, and `1+1/D` near-unit graphs for `q=1,2,3`; checks every outgoing
arrow on each root path through its first cap crossing; and compares with an
explicit same-cardinality square grid. The all-order source family and its
path estimates are proved analytically in
`docs/audits/target_c_common_trunk_congestion_regression_independent_audit_2026-10-08.md`.
The report's centered-disk cap and closure are already subsumed by Audit.166.
The promoted sharpness and common-trunk regressions are nonglobal and have no
normalized KKT diameter stress; neither contradicts a theorem using canonical
global-source hypotheses or supplies a C-II move.

## Target C weak-wall refill and capacity plateau (2026-10-08 Audit.169)

Run `python3 research/verify_target_c_post_descent_capacity_plateau_2026_10_08.py`.
The exact `Q(sqrt(3))` checker reconstructs all source, reduced-endpoint, and
square-lattice-competitor pairs for `M=4,6,8,12`, checks the contact and
unique-diameter graphs, triangle-freeness, the weak flat-wall guards, and the
integer Oler margin at the endpoint `t=1/(10M^2)`. The independent audit also
ran its fixture at `M=2,3,5`. The verifier checks finite instances only; the
all-`M`, all-`t` capacity plateau and nonglobality are analytic in
`docs/audits/target_c_weak_wall_refill_capacity_independent_audit_2026-10-08.md`.
It does not prove the weak-wall shield, arbitrary packet capacity beyond the
Oler argument, a canonical source endpoint, or C-II/Level I closure.


## 2026-10-08 Audit.170 accessible stress-face verifier

`verify_target_c_accessible_stress_faces_2026_10_08.py` checks the exact seven-site tagged-stress regression, exact stress and rigidity ranks, finite tagged-face subsets, abstract simplex/cube examples, and sample rational defect inequalities. Its rational and `Q(sqrt(3))` arithmetic is exact. It does not prove the canonical Helly dichotomy, Section 64's circuit inequality, accessible-grid extraction, source optimality, a refill, or C-II/Level I closure. Those analytic claims were independently reconstructed in `docs/audits/target_c_accessible_stress_face_independent_audit_2026-10-08.md`.

## Target C almost-accessible stress transversal (2026-10-08 Audit.171)

Run `python3 research/verify_target_c_exceptional_star_face_2026_10_08.py`. The exact checker reconstructs seven finite planar nonglobal fixtures, full pair/contact/diameter censuses, selected equilibrium/PSD and rank data, and abstract simplex/cube-face cases for the two-stage codimension count. The face-count fixtures are abstract polytopes, not canonical planar sources. These checks do not prove the universal exposed-face lemma, contact-row independence, loaded-only stress obstruction, source-level strict-motion theorem, or global optimality. The finite transversal theorem and its source-scope argument are analytic in `docs/audits/target_c_almost_accessible_transversal_independent_audit_2026-10-08.md`; Audit.172 separately audits the one-star refinement. Audit.173 now proves approximate Type-II endpoint access, but its unweighted exceptional-edge count does not supply a stress-mass bound.

## Target C exceptional diameter-star face (2026-10-08 Audit.172)

Run `python3 research/verify_target_c_exceptional_star_face_2026_10_08.py`. The exact checker verifies straight-chain sources, the two-arm unit-triangle stress, three-arm triangle-free diameter-cycle stresses, complete source pair/contact/diameter/triangle censuses, exact equilibrium and rank data, rational PSD ranks, smaller square-grid competitors, and 64 abstract face-count fixtures. These are finite nonglobal examples; the abstract polytopes are not planar sources. The checker does not prove the universal star-stress classification, the canonical exceptional-face deletion, star extraction, global optimality, or cardinality restoration. Those claims and the exact limits of both regressions are in `docs/audits/target_c_exceptional_diameter_star_face_independent_audit_2026-10-08.md`.


## Target C uniform harmonic-cell and diameter-grid access (2026-10-08 Audit.173)

Run `python3 research/verify_target_c_uniform_cells_diameter_access_2026_10_08.py`.
The script uses exact `Fraction` arithmetic for finite pinned-star, circle/fan,
direction-spacing, weighted-count, and auxiliary-body fixtures. It checks 21
positive pinned stars and 126 star pairs; 45,643 circle/fan source pairs; 13,384
actual diameter-direction pairs; 11,792 body/port/radius cases; 24 weighted identities;
three high-degree single-port witnesses; and six impossible-cell diagnostics. The separate
`verify_target_c_face_tail_port_multiplicity_2026_10_08.py` checks exact finite
strip, weighted-incidence, and prescribed-port triangle fixtures. All fixtures are
nonglobal or auxiliary: these scripts do not certify uniform cell bounds, Type-II
asymptotics, grid extraction, the asymptotic incidence theorem, source-face
hypotheses, coherent grains, globality, or a source move. The analytic claims,
including the repaired cell-crop proof, unweighted edge-count limit, port-incidence
bound, and prescribed-port cap, are in
`docs/audits/target_c_uniform_harmonic_cells_global_diameter_access_independent_audit_2026-10-08.md`
and
`docs/audits/target_c_typeii_face_tail_port_multiplicity_independent_audit_2026-10-08.md`.

## Target C terminal-cancellation face floor (2026-10-08 Audit.174)

Run `python3 research/verify_target_c_terminal_cancellation_interior_2026_10_08.py`.
The exact `Fraction` checker exercises eight nonglobal contact fixtures, checks
7,252 full-source lower pairs and 108 terminal pairs, and verifies the facial,
component, and separate-face incidence identities across repeated outer bridges
and 52 interior terminal occurrences. It passed 620 component identities and 886
separate-face cancellation checks. The helper
`verify_target_b_terminal_cancellation_2026_10_08.py` supplies shared fixture
construction. These scripts verify finite facial identities only; they do not
prove the Type-II asymptotics, atom-selection diagonal, marked-measure argument,
global optimality, or Level I closure. The independently reconstructed theorem
and checker limits are in
`docs/audits/target_c_typeii_terminal_cancellation_face_floor_independent_audit_2026-10-08.md`.


## Target C shallow-wall packet release certificate (Audit.176)

Run `python3 research/verify_target_c_collective_shallow_wall_release_2026_10_08.py`. It checks every old and endpoint pair for a ten-site packet with an initial unit triangle and retained outside isolate, and for the 529-site rational larger-turn regression. The arithmetic is exact: rational coordinates in the large fixture and the existing `Q(sqrt(3))` helper in the small fixture. For the large fixture it checks 600,060 old pairs, 600,060 endpoint pairs, positive equilibrium at all 529 moving labels, the complete 1,097 contact rows, triangle-freeness, no common first-order translation, and a finite rotation/translation/dilation release. The verifier supports only these finite fixtures and does not prove the universal shallow-wall release, canonical cell extraction, source globality, or C-II closure. It is registered for `C-LARGER-TURN-COLLECTIVE-TRANSLATION-REGRESSION`.


## Target C shared-carrier disjoint-return regression (Audit.186)

Run `python3 research/verify_target_c_shared_carrier_disjoint_return_2026_10_08.py`. The standalone checker uses exact `Fraction` coordinates and integral vertex-split max-flow. At `m=12,16,24` it verifies all source pairs, exact contacts, positive artificial-pin equilibrium, a full pinned-rigidity minor, the `K_N` edge count, and endpoint-inclusive cut/path values in both the carrier and the full contact graph. These fixtures verify only the finite instances. The all-`m` construction, quadratic total return-length lower bound, and strict nonglobality are proved analytically in `docs/audits/target_c_shared_carrier_disjoint_return_independent_audit_2026-10-09.md`. The regression has artificial pins rather than the actual diameter-loaded set, so the certificate does not refute a canonical global-source theorem.
