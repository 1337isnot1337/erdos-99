# Reproducible research tools

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

The [all-regime fan/train re-audit](target_c_allregime_fan_train_floor_reaudit_2026-09-12.md)
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
and [hostile audit](target_c_phase_atomic_route_surplus_self_audit.md) rule out
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

## Tube-only response-cut audit (2026-09-08)

Run `python3 research/tube_shield_cut_audit.py` for the integer/exhaustive audit
of the [tube-only cut bound](../docs/reports/target_a_tube_only_cut_2026-09-08.md).
It checks 17,104 graph/tube/shield cases over all 1,024 prescribed-basis
bipartite graphs of the stated size. It encodes alternating paths and basis
closure; it omits unit geometry, source stress, and global optimality. A pass
verifies only those finite cases; the report supplies the general proof.

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
## Target C-II exact oblique-lattice Pick comparison (2026-09-14)

- Proof-only report: `docs/reports/target_c_oblique_lattice_pick_comparison_2026-09-14.md`
- Independent audit: `docs/audits/target_c_oblique_lattice_pick_comparison_independent_audit_2026-09-14.md`
- Verification: `python3 research/verify_target_c_oblique_lattice_pick_comparison.py`

The exact lattice-polygon/Pick comparison gives a source-cardinality-exact
triangular-lattice competitor whenever
\(\frac{\pi D^2}{4}(1/a_0-1/\sin\theta)>\frac{\pi D}{2}+1\).
It sharpens the earlier fundamental-cell thickening estimate but leaves the
inverse-diameter shear endpoint and does not extend to general C-II sources.

## 2026-10-01 — strict near-diameter capacity and cofacial TB1 blockers

Run `python3 research/verify_strict_near_diameter_capacity_2026_10_01.py`.
The associated proof-only report is
[`target_c_strict_near_diameter_capacity_2026-10-01.md`](../docs/reports/target_c_strict_near_diameter_capacity_2026-10-01.md).
It proves analytically that pairs longer than `sqrt(D^2-1)` join extreme hull
vertices and form a thrackle, leaving at most `floor(pi D)-h` inactive pairs at
that threshold. Under the actual ONE-SIGN swap hypotheses and amplitude at most
`1/(2D)`, this forces at least `ceil(r/2)-(floor(pi D)-h)` distinct near-unit
witnesses from `r` disjoint slabs. Those pairs form a planar Gabriel augmentation
and lie in faces of the old contact graph.

The verifier uses integer squared distances and orientations for 16,834 eligible
four-point subsets of a half-integer 6-by-6 grid, including 3,504 strict inactive
near-diameter edges in 2,944 packets. It also checks exact rational examples
showing failure at the weak diameter threshold, failure at the weak Gabriel
cutoff, and linear planar near-unit populations without exact triangles.
Encoded hypotheses are unit separation, diameter, extremality, crossing, and
strict threshold inequalities. KKT, global optimality, the train cut/chart,
rooted endpoint saturation, and the existence of a linear small-amplitude swap
population are omitted. Passing verifies these finite regressions; the universal
proof is in the report, and neither the computation nor the reduction settles
C-II or Level I.

The follow-up report
[`target_c_common_swap_blocker_arborescence_2026-10-01.md`](../docs/reports/target_c_common_swap_blocker_arborescence_2026-10-01.md)
proves a stronger simultaneous result when all disjoint ONE-SIGN slabs have the
same swap vector and each moves an old diameter. Every nonempty union then has
an outgoing inactive blocker; the layer graph has a directed tree toward the
fixed source with `r` distinct pair labels. At most `floor(pi D)-h` can be strict
near-diameter blockers, leaving at least `r-(floor(pi D)-h)` cofacial near-unit
edges. The same verifier exhausts directed graphs with up to four moving layers
and a fixed root, checking the cut/reachability equivalence and distinct tree
edges. It omits the actual finite-move/source hypotheses, which are proved in the
report and remain conditional in the train application.
The report also audits PR #600's cyclic isolate dispatch and proves that it
commutes with every common-vector union. In that cyclic branch all tree labels
are near-unit pairs and `N_1>=r` without rooted saturation. The unique-partner
dispatch does not apply to the forest branch; none of these inactive edges has
an asserted KKT multiplier.

The subsequent report
[`target_c_deficiency_bounded_isolate_dispatch_2026-10-01.md`](../docs/reports/target_c_deficiency_bounded_isolate_dispatch_2026-10-01.md)
generalizes dispatch to every diameter topology. A forest rooted at the original
diameter endpoints assigns every incident isolate to one root, leaving at most
`d_H=q-h` inactive upper-distance exceptions for any finite core displacement
cloud of diameter less than `D-sqrt(D^2-1)`. The forest and exception set are
independent of the move. The common-swap tree consequently has at least
`r-d_H` near-unit labels, including in forest branches. The verifier checks
finite abstract multi-root graphs, every binary root assignment, and an exact
quadratic-field geometric residue with `d_H=1`. It encodes the subgraph edge
budget and omits geometric realizability, optimality and KKT. The report proves
the universal geometric and source premises analytically; the lower constraints
and the complete Level I objective remain unresolved.

## 2026-10-01 — disjoint cap reactions and inactive-interface swap blockers

Run `python3 research/verify_target_c_disjoint_cap_reactions_2026_10_01.py`.
The report
[`target_c_disjoint_cap_reaction_capacity_2026-10-01.md`](../docs/reports/target_c_disjoint_cap_reaction_capacity_2026-10-01.md)
proves that disjoint actual-source cap shores with uniform contact-cut
directions in a projective window of width `W` number at most
`2 floor(W/delta_D)+6`. It uses positive KKT reactions, convex normal order,
diameter-direction spacing, and an explicit finite one-cut release.
Under the unpromoted actual rectangle/cut chart and an alternating two-phase
common-vector ONE-SIGN family of amplitude at most `1/(2D)`, at most fourteen
chosen rhombus blocker labels have outer-to-outer transverse trains.
At least `r-d_H-14` labels therefore meet genuine inactive interfaces.

The verifier checks every distance, contact, diameter and individual swap
in four exact quadratic-field tooth packets, including a 143-point example
with ten outer rhombus blockers. Those packets lack positive KKT and do not
move an old diameter; they falsify a geometry-only variant. It also checks
1,440 exact finite angular interval packets and 110 alternating supports.
It omits global optimality, positive stress, core rigidity, actual train
extraction, and a finite inactive-interface repair. The analytical theorem
is in the report; the finite computations are scoped regressions and do not
settle C-II or Level I.

The next report
[`target_c_bounded_face_train_graph_and_mixed_transposition_2026-10-02.md`](../docs/reports/target_c_bounded_face_train_graph_and_mixed_transposition_2026-10-02.md)
proves analytically that nonsingleton trains in one phase window of width
less than `pi/3` form a planar simple graph on their bounded terminal
faces. Positive equilibrium rules out two nonparallel trains joining
the same face pair; convex support and train monotonicity exclude parallel
duplicates. Ultrasmall windows also give a strict directed face-height
potential. Matching signed O-F terminal occurrences supply an exact
composite two-train contact transposition and the same actual-diameter
TWO-SIGN / inactive-blocker fork as O-O TB1. The proof retains all isolates.
It does not assert disjoint source shores or a common swap vector.
Face-vector conservation rejects raising all problematic thresholds while
fixing every other terminal class. No numerical evidence is used for these
claims, and the finite inactive-interface release remains unresolved.
An exact monotone phase repair in one ultrasmall band induces a nonnegative
circulation on the terminal-face graph. Its bounded part has a strict
height potential, so every changed bounded-bounded train lies on a route
entering and leaving through mixed outer/face trains. This is a necessary
finite vector-closure condition, not a feasible motion construction.
The isolate-forest proof now includes bounded-face-following dispatch:
interior isolates are not incident with strict-long pairs, so they can
follow a rigid face boundary without changing the forest exceptions.
Complete selected O-O cuts leave each bounded nonquadrilateral face in
one layer. Thus the remaining non-rhombic lower tree labels lie in the
old outer contact face. Mixed O-F swaps need an additional chamber
argument because they can split that bounded terminal face.
A short bounded-face direction arc between matching mixed ends has no
loaded internal vertex: two nearly opposite unit contacts at a diameter
endpoint require a turn of at least `1/D`. Pure positive equilibrium
then bounds boundary stress variation by `exp(3 epsilon)` and the sum
of non-face incident contact weights by
`(4/3) epsilon exp(3 epsilon)` times the first boundary weight.
This relative reaction estimate does not give an absolute multiplier
floor or a finite release theorem.
