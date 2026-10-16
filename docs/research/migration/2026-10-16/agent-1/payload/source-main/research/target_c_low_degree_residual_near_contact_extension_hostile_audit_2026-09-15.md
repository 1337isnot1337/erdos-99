# Hostile audit — degree-5/6 residual near-contact extension

**Date:** 2026-09-15
**Reviewed:** `research/target_c_low_degree_residual_near_contact_extension_2026-09-15.md`
**Verdict:** `PASS` at the stated proof-only scope.
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The candidate combines four already-audited ingredients: the degree-5/6 face staircase, the degree-`>=7` isolate-host theorem, exact chamber-residual conservation, and Wegner stability for equilateral pentagons/hexagons. It then uses the same factor-nine selected-pair matching argument independently audited in the short-hidden-chord theorem.

## 1. Residual normalization is exact for both degrees

For an internal exceptional `d`-face with `d in {5,6}`, the isolate-host theorem gives `z_P=0`; its fixed contact boundary has `k_P=d` vertices and perimeter `P_P=d`. Therefore

\[
r_P={A_P\over a_0}+{d\over2}+1-d,
\qquad a_0={\sqrt3\over2}.
\]

The equilateral Oler equality value is

\[
A_{min}(d)={\sqrt3\over4}(d-2)={a_0\over2}(d-2).
\]

Subtracting gives exactly

\[
r_P={A_P-A_{min}(d)\over a_0}.
\]

No boundary-credit term is omitted. Since all chamber residuals are nonnegative and sum to `R_F`, summing only the degree-5/6 chambers is bounded above by `R_F`.

**Verdict:** PASS.

## 2. Wegner compactness applies simultaneously to degrees five and six

The audited low-degree Wegner theorem proves, separately for `d=5` and `d=6`, that every zero-Oler-slack limit is a Groemer/Wegner packing and has a nonboundary unit pair. For each fixed `eta>0`, compactness therefore gives positive gaps `sigma_5(eta),sigma_6(eta)`. Taking their minimum is legitimate because only two degrees occur.

Thus every degree-5/6 face with all hidden pairs at least `1+eta` consumes at least

\[
c(eta)=\min\{\sigma_5(eta),\sigma_6(eta)\}/a_0>0
\]

of the globally conserved residual. The candidate bound `#bad <= R_F/c(eta)` follows.

**Verdict:** PASS.

## 3. The diagonal subsequence argument is legitimate

If `R_F=o(D)`, then for every fixed `eta>0` the number of faces with hidden gap at least `eta` is `o(D)`. The staircase supplies `(L_6(T)-o(1))D` total degree-5/6 faces. A standard diagonal choice of `eta_D downarrow 0` therefore retains `(L_6(T)-o(1))D` faces with maximum selected hidden gap tending to zero.

No uniform modulus for Wegner stability is assumed.

**Verdict:** PASS.

## 4. The factor-nine matching loss is safe

The independently hostile-audited short-hidden-chord theorem already verifies the exact graph point used here:

- triangle-freeness gives contact degree at most five;
- a source vertex is incident to at most five distinct bounded face boundaries;
- after choosing one candidate hidden pair per face, the candidate multigraph has maximum degree at most five, counting multiplicity;
- a maximal matching edge covers at most `5+5-1=9` candidate multiedges.

Therefore a matching of size at least one ninth of the retained face population is valid. The candidate does not require the faces themselves to be vertex-disjoint.

**Verdict:** PASS.

## 5. Arithmetic endpoint is conservative

The companion exact-rational verifier gives

\[
X_6=2.1854878451\ldots>2.1854.
\]

At `T=2.1854`, the certified face density is still `0.000120787...` and the factor-nine matching density is `1.3420e-5`, above the displayed `1e-5` row. All other displayed rows have larger margins.

**Verdict:** PASS.

## 6. Scope warning

The result upgrades the short-chord matching from a fixed upper length `sqrt(3)` to `1+o(1)` only on the `R_F=o(D)` branch. It does not realize `R_F` as packing capacity, does not activate the hidden constraints, and does not create a diameter-feasible first-order motion. C65 contact minimality also does not make activation alone contradictory, because a newly activated diagonal can leave the triangle-free normalized class.

**Final verdict:** PASS. The theorem is a genuine residual refinement of the audited short-hidden-chord matching and extends the almost-active matching frontier from the pentagon cutoff to the degree-5/6 cutoff. C-II remains open.
