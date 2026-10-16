<!-- theorem-state: {"artifact_id":"ART-0FCAEF743359","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C all-bridge transverse interval balance

**Date:** 2026-09-13  
**Reviewed:** `research/target_c_all_bridge_transverse_interval_balance_2026-09-12.md`  
**Base state:** `2026-09-12.audit.46`  
**Disposition:** **PASS at the stated proof-only scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Scope and stress support

The candidate is applied only after the C-II contact-minimal, then diameter-pair-
minimal normalization. C65 identifies the positive contact and diameter supports with
the complete actual contact and diameter graphs. Thus a relative-interior normalized
KKT stress has strictly positive coefficients on every contact and every actual
diameter edge used in the cut sums. Contact-isolated source points are not deleted:
the finite shear moves every source point on the selected shore, including isolates.

The bridge statement concerns a bridge of the full actual unit-contact graph. A bridge
cut has no other crossing unit contact, so the only crossing force terms in the summed
equilibrium equation are the bridge contact and diameter edges. The candidate uses
`D>1`, which is automatic in the large-source regime; the strict shear inequality is
not asserted at the degenerate value `D=1`.

**Verdict:** PASS under the stated C65/full-source hypotheses.

## 2. Cut resultant and the sign argument

Summing equilibrium on one shore cancels all internal contact and diameter forces. With
the bridge vector oriented from `T` to `S`, the result is

\[
\alpha u_0=\sum_{h\pitchfork uv}\beta_h r_h,
\qquad \alpha>0,\quad \beta_h>0.
\]

Dotting with `Ju_0` gives the zero transverse sum. If the nonzero transverse values
did not include both signs, positivity would force every transverse value to vanish.
All crossing diameter vectors would then be parallel to the bridge. The projective
diameter-uniqueness lemma leaves at most one unordered crossing pair; the nonzero cut
resultant leaves exactly one and fixes its shore-oriented vector as `D u_0`.

No star assertion, diameter matching assertion, or lower bound on an individual
KKT coefficient is being used here.

**Verdict:** PASS.

## 3. Finite shore shear

Translate the selected shore by `R_theta u_0-u_0`. The bridge remains a unit contact,
and no second unit contact crosses the bridge cut. Same-shore distances are unchanged.
All other old noncontacts have strict distance greater than one and remain so for a
sufficiently small nonzero angle by finiteness and continuity. The sole crossing
diameter changes from `D u_0` to `D u_0+R_theta u_0-u_0`, and direct expansion gives

\[
|D u_0+R_\theta u_0-u_0|^2
 =D^2-2(D-1)(1-\cos\theta)<D^2.
\]

No other crossing pair can newly attain `D` for a small enough angle because all such
pairs had strict slack. If a same-shore diameter remains, the source has the same
diameter and strictly fewer actual diameter pairs, contradicting the secondary
normalization. If none remains, its diameter is strictly below `D`, contradicting
global minimality. Therefore every positive bridge has crossing diameter vectors with
both transverse signs.

The shear is a finite source operation, not a claim about a generic infinitesimal PSD
matrix. It preserves cardinality and all required unit separations.

**Verdict:** PASS.

## 4. Nested corridor identity

For a straight bridge corridor, the shores of consecutive cuts are nested. A diameter
edge path in the bridge-block tree intersects the corridor in a consecutive interval;
its endpoint orientation is constant on that interval. Applying the same bridge cut
resultant at level `j` and taking the transverse coordinate gives

\[
F_j=\sum_{h:\,\ell_h\le j\le r_h}y_h=0.
\]

With the harmless boundary convention `F_0=F_{L+1}=0`, subtracting adjacent equations
gives exactly

\[
\sum_{h:\,\ell_h=j}y_h
 =\sum_{h:\,r_h=j-1}y_h.
\]

The difference is a finite telescoping identity for the actual positive KKT weights;
it does not assume that the diameter graph is a matching or that a cut is a star.
Empty intervals simply do not occur in the sum.

**Verdict:** PASS.

## 5. Profile counting and limits

The set of diameter paths crossing a corridor cut changes only when an interval starts
or ends. If `E` levels contain an endpoint, there are at most `E+1` constant-profile
blocks. The stated dichotomy is valid (the elementary integer bound obtained from the
stronger `M-1` block-length estimate already implies the displayed
`ceil(L/M)-1` bound). On a constant block, the profile has zero signed transverse
mass and, by the all-bridge result, both signs. The canonical common-bridge theorem
excludes only the profile consisting of all diameter paths; a proper profile is not
silently excluded.

**Verdict:** PASS.

## 6. Non-implications retained

The audit finds no route from endpoint-event count or a proper constant profile to an
upper bound on `sum_r(L_r-2d_r)`, to a bound on `e_BB-k`, or to an exact equilateral
triangle. The result is therefore a structural proof-only reduction. It does not
close C-II, does not alter the theorem-state version, and does not promote any
conditional branch to canonical status.

**Final verdict:** PASS as a proof-only hostile audit; theorem state unchanged.
