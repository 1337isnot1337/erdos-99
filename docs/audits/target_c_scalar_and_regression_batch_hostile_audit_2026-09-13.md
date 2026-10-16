<!-- theorem-state: {"artifact_id":"ART-9A1EE13D0184","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — remaining scalar and regression batch

**Date:** 2026-09-13  
**Base state:** `2026-09-12.audit.46`  
**Reviewed:**

- `target_c_strict_thin_corridor_regression_2026-09-12.md`;
- `target_c_stale_global_face_endpoint_regression_2026-09-12.md`;
- `target_c_common_cap_t_floor_2026-09-12.md`;
- `target_c_post_fan_train_hull_scalar_regression_2026-09-12.md`;
- `target_c_fan_pair_normalization_retraction_2026-09-12.md`;
- `target_c_four_host_signed_return_regression.md`;
- `target_c_outer_detour_topology_band_2026-09-12.md`;
- `target_c_surplus_moment_identity_2026-09-12.md`; and
- `target_c_section122_route_host_regressions.md`.

**Disposition:** the scoped scalar identities and finite regressions pass. The
thin-corridor result requires a scope correction stated below. The two retracted fan
claims and stale endpoint claim remain rejected. Canonical state is unchanged.

## 1. Strict thin-corridor regression

The exact verifier produces a strictly convex unit-edge polygon with 70 off-phase side
occurrences, area `83.5629`, minimum nonadjacent distance `1.78885`, and bounding-box
dimensions approximately `(32.7782,3.2307)`. The construction is a valid finite
unit-separated strict-convex polygon at the checked size, and the analytic edge-vector
sequence closes and has positive turns.

The construction is sufficient against the following implication:

\[
\text{unit-separated strict convex face boundary}+
\text{containment in a convex body of diameter }D+O(1)+o(D^2)\text{ area}
\Longrightarrow U=o(D).
\]

It is **not** a counterexample to a stronger Hausdorff-near-disk hypothesis. The thin
rectangle-like polygon is contained in a disk of diameter `D+O(1)`, but is not itself
Hausdorff-close to a disk. Therefore the source report's phrase “near-disk ambient
containment” must be read as diameter-near containment, not as canonical Type-II
force-hull convergence. No source/contact graph or global minimizer is constructed.

**Verdict:** PASS as a regression against the weaker corridor-capacity strengthening;
scope narrowed explicitly. It does not refute a genuine near-disk shape theorem.

## 2. Stale global-face endpoint

The active exact identities are

\[
T=\frac{b+Q}{2}+2f,
\qquad
\frac{b+Q}{2}=h-s_Z.
\]

Thus `T-h-2f=-s_Z<=0`; in the equality case it is zero. The old strict target
`T-h>2f` is algebraically impossible under the canonical definitions. The source
report correctly rejects the older endpoint and does not change the live route.

**Verdict:** REJECTED claim confirmed.

## 3. Section-118 common-cap retained-remainder floor

The reviewed substitution starts from the audited inequality

\[
5q-7k\ge3S_D+2G_D+c_*D-o(D)
\]

and writes `q/D=t+kappa`, `k/D=kappa`. This gives
`5t-2kappa >= 3S_D+2G_D+c_*-o(1)`, with the sign of the `kappa` term correct.
Using the scoped lower bounds `S_D>=S_*` and `G_D>=G_*`, then discarding
`kappa>=0`, yields the displayed `t>=1.8376645...` floor. The verifier's rational
certificate passes. The supplied scalar witness is feasible and is not claimed
geometric.

**Verdict:** PASS at the named Section-118 common-cap scope; no universal Type-II
floor or closure follows.

## 4. Post-fan/train/hull scalar regression and fan normalization retraction

The exact fan pair inequalities may remain finite combinatorial facts, but the density
conversion is invalid because `T=O(D)` and `f=O(D)`. Dividing `20f<=T(T-1)-2R` by
`D^2` makes `20f/D^2=o(1)`, not `20(f/D)`. Therefore the old floors
`1.93599...`, `2.51478...`, and `2.30363...` are withdrawn. The post-fan scalar
witness is only compatibility data for the remaining ledgers; its verifier does not
rescue the invalid normalization.

**Verdict:** REJECTED density-floor derivation confirmed; finite fan accounting
retained only as a regression/provenance fact.

## 5. Four-host signed-return regression

For unit vectors `u,v` with angle in `(pi/3,2pi/3)`, the lattice
`{iu+jv}` is unit-separated and has exactly the four unit directions `+/-u,+/-v`.
Its finite rectangular patch is triangle-free, has quadratic strict-rhombus area, and
has an outer parallelogram walk with zero perimeter-subtracted route excess. The four
physical host directions have width two in both train directions, so the signed-return
loss is exactly zero. The verifier checks patches through sizes 1, 2, 5, 10, and 25.

**Verdict:** PASS as a finite geometric regression. It is not a global-minimizer
counterexample and only blocks a host-count-free positive return theorem.

## 6. Outer-detour topology band

On the scoped common-cap floor `t=(q-k)/D>=S_*` and the perimeter bound `q/D<=pi`,
`k/D<=pi-S_*<0.3444` follows. The identity
`r_H=2h-q=tD+s_Z-d_H` gives `r_H/D>=2t-q/D`, hence the displayed
`r_H/D>=2S_*-pi=2.4543...`. The forest interpretation
`r_H=sum_j(q_j-2)` is the canonical Woodall identity. The verifier passes.

**Verdict:** PASS as a scoped scalar/topological corollary; it does not force a
macroscopic caterpillar or close the cyclic branch.

## 7. Surplus-moment identity

From `e_BB=q-m` and the pinned ledger
`c_I+e_BB+s_C=q-2+k`, one gets
`s_C=m+k-2-c_I` and
`M_D=e_BB+2s_C-3k=q+m-k-2c_I-4`. With
`G_D=2+q+m-k-S_D`, this gives the exact cancellation
`S_D+G_D=M_D+2c_I+6`. The derived normalized identities for `Q+u_B`, the retained
remainder, and the return inequality have the correct signs. The listed scalar witness
passes exact arithmetic and is explicitly not a geometric source.

**Verdict:** PASS as a proof-only algebraic feasibility note; no geometric or
global-optimality conclusion follows.

## 8. Section-122 route-host regression

The oblique grid patch has exactly four unit directions, no unit triangles, quadratic
strict-rhombus area, and four side hosts. Its perimeter-subtracted route excess and
four-host signed-return loss are both zero. Therefore splitting a defect corridor and
silently retaining the three-host positive return constant is invalid. Any future upper
detour theorem must add source-specific minimality or a host-control theorem.

**Verdict:** PASS as a finite regression; no C-II counterexample.

## Final disposition

This batch contains no hidden closure. The only correction is the thin-corridor scope:
it refutes a diameter-near containment shortcut, not canonical Hausdorff-near-disk
geometry. All rejected claims remain explicitly rejected, and all surviving claims are
scoped proof-only results.
