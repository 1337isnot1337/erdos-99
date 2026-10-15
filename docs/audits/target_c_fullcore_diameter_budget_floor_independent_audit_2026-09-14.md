<!-- theorem-state: {"artifact_id":"ART-94BFB8411971","canonical":true,"claim_ids":["C-FULLCORE-DIAMETER-BUDGET-FLOOR"],"claim_statuses":{"C-FULLCORE-DIAMETER-BUDGET-FLOOR":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — Target C-II full-core diameter-budget floor

**Date:** 2026-09-14
**Base state:** `2026-09-12.audit.46`
**Target:** Target C-II, full-core branch
**Audited artifact:** `docs/reports/target_c_fullcore_diameter_budget_floor_2026-09-14.md`
**Verdict:** PASS for the stated asymptotic theorem; no Level I closure.

## Audited statement

For a sequence of canonical full-core Type-II representatives with diameters
\(D_j\to\infty\), attachment cells \(P_{r,j}\), cell diameters
\(d_{r,j}\), component graph diameters \(\delta_{r,j}\), and
\[
\mu_j=\frac{e_{BB,j}+2s_{C,j}-3k_j}{D_j},
\qquad k_j=d_{H,j}+s_{Z,j},
\]
we audit
\[
\liminf_j\mu_j\ge1.
\]
The source convention is the full source, including contact-isolated points. The
cells and component diameters are auxiliary core objects only.

## Proof audit

The report uses the following hypotheses and no stronger ones:

1. \(\sum_r a_{r,j}\ge(\pi/4)D_j^2-o(D_j^2)\), from the canonical full-core
   near-disk area and attachment-cell saturation statements.
2. \(\sum_r\sqrt{a_{r,j}}\le C D_j\), from the canonical cell perimeter budget and
   planar isoperimetry.
3. \(d_{r,j}\le\delta_{r,j}+2\), with the additive two retained.
4. \(\sum_r\delta_{r,j}\le6+\mu_jD_j\), from the exact attachment currency identity
   after dropping the nonnegative \(R_I+s_B\) terms.

For a fixed area threshold \(\eta D_j^2\), the small-cell area is bounded by
\[
\sum_{a_{r,j}<\eta D_j^2}a_{r,j}
\le\sqrt\eta D_j\sum_r\sqrt{a_{r,j}}
\le C\sqrt\eta D_j^2.
\]
Thus the large cells carry at least
\((\pi/4-C\sqrt\eta)D_j^2-o(D_j^2)\) area. The planar isodiametric inequality
\[
a_{r,j}\le\pi d_{r,j}^2/4
\]
then gives
\[
\sum_{r\ {\rm large}}d_{r,j}
\ge
2\sqrt{\frac{\pi/4-C\sqrt\eta}{\pi}}D_j-o(D_j).
\]
The number of large cells is at most \(C/\sqrt\eta\). Therefore
\[
\sum_r\delta_{r,j}
\ge
2\sqrt{\frac{\pi/4-C\sqrt\eta}{\pi}}D_j-o(D_j)-O_\eta(1).
\]
Combining with the exact upper budget, then taking \(j\to\infty\) at fixed \(\eta\),
and finally \(\eta\downarrow0\), gives \(\liminf\mu_j\ge1\).

All inequality directions are correct. In particular, the use of
\(\sum d_r\ge\sqrt{\sum d_r^2}\) is valid because the diameters are nonnegative; the
fixed \(+2\) loss is harmless because the number of threshold-large cells is bounded
for fixed \(\eta\). No claim that the number of all cells is bounded is made.

## Scope and dependency audit

* `C-FULLCORE-NEAR-DISK` is used only for the full-core area asymptotic. It does
  not apply to Type-I chambers/caps.
* `C-HARMONIC-CELL-TILING` is used for cell area saturation and the square-root
  budget. It supplies actual convex attachment cells, not an abstract scaffold.
* `C-ATTACH-CURRENCY` is used for the exact component-diameter budget and
  \(d_r\le\delta_r+2\).
* No extension of the ZR/ZF affine-kernel statement to isolated source coordinates is
  used.
* Sections 122 and 123, carrier decimals, outer-walk occurrence injectivity, and
  loaded-chord simplifications are not used.

## Regression audit

* The scalar-ledger compatibility witness has \(\mu>1\), so it is compatible with the
  theorem and still blocks scalar-only closure.
* The saturated chamber/exterior-cap constructions do not satisfy full-core cell-area
  saturation, so they are outside scope.
* The square-grid and vanishing-shear regressions do not satisfy the canonical
  full-core cell/ledger hypotheses simultaneously.
* Contact-isolated points are retained globally and are not counted as core vertices.
* No equality claim is made for individual cells, nor is near-disk convergence assigned
  a rate beyond the canonical \(o(D^2)\) input.

## Promotion verdict

The theorem is a valid stronger full-core branch consequence and may be promoted as a
standalone canonical ledger entry. It does not alter `level_i_status`, `target-c`
status, or the Type-I branch. Any future use must retain the exact order of limits and
all four hypotheses above.
