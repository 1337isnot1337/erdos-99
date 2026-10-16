<!-- theorem-state: {"artifact_id":"ART-E6EA510B8930","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — three unreviewed Target C-II findings

**Date:** 2026-09-13  
**Base state:** `2026-09-12.audit.46`  
**Reviewed:**

- `research/target_c_integer_hull_route_defect_2026-09-13.md`;
- `research/target_c_typeI_open_guard_one_site_2026-09-13.md`;
- `research/target_c_linear_non_tooth_boundary_deficit_2026-09-12.md`.

**Disposition:** PASS at the stated proof-only scopes. No result closes C-II, and no
canonical theorem-state file is changed.

The recent aggregate route-currency floor, explicit route-surplus floor, strict
aggregate moment gap, and exact route-surplus/stopped-train identity already have
separate hostile audits. They are not silently treated as audited by this file.

## 1. Integer hull-route defect

Let `s_i` be a loaded-hull side length and `ell_i` the occurrence-counted unit-edge
route assigned to that side. The only geometric input used is the canonical
`ell_i >= s_i` and the integrality of `ell_i`.

Define

\[
r_i=\ell_i-\lceil s_i\rceil\ge0,
\qquad
\varphi_i=\lceil s_i\rceil-s_i\in[0,1).
\]

Then, term by term,

\[
\ell_i-s_i=r_i+\varphi_i.
\]

Summing over the cyclic loaded-hull sides gives the displayed decomposition
`b-per(F)=sum r_i+sum phi_i`. No side or bridge occurrence is identified with
another one.

For `M={i:s_i>1}`, the Type-II integer slack is

\[
u_B=\sum_{i\in M}(\ell_i-2)+\sum_{i\notin M}(\ell_i-1).
\]

For `s_i>2`, the first summand dominates `s_i-2`; for `1<s_i<=2` its contribution
is nonnegative; and for `s_i=1` the contribution is exactly `ell_i-s_i`.
Therefore

\[
u_B\ge \sum_{i\in M}(s_i-2)_+,
\qquad
0\le u_B-\sum_{i\in M}(s_i-2)_+
\le b-\operatorname{per}(F).
\]

Also

\[
\sum_{i\in M}(s_i-2)=\operatorname{per}(F)-q-m,
\]

so the positive-part lower bound in the reviewed report has the correct sign. The
asymptotic identities in its zero-detour subsection follow directly from
`u_B=b-q-m`, `t=(q-k)/D`, `r=(m+k)/D`, and `per(F)/D -> pi`; no rate for the
near-disk convergence is used.

The pure-tooth corollary also checks: `m=q` and `ell_i=2` give `b=2q`, while the
named endpoint floor supplies `q/D >= 2 sqrt(Delta_2)`. Hence

\[
\frac{b-\operatorname{per}(F)}D
\ge 4\sqrt{\Delta_2}-\pi-o(1)
=0.6676585738\ldots-o(1).
\]

**Verdict:** PASS as a finite Type-II rounding reduction and as a scoped endpoint
corollary. It does not rule out a rounded long-side endpoint or give a diameter
decrease.

## 2. One-site Type-I open-guard criterion

The reviewed report starts from the audited Type-I contact-wall shield. Replacing weak
guards by strict guards removes only finitely many circle arcs and chord boundary sets,
so the safe-region area is unchanged. If `x` is in the strict safe region and a
retained source point `r` had `|x-r|<=1`, the segment from `x` to `r` would first
leave the convex container through a boundary vertex, a unit contact edge, or the
exterior closing chord. The corresponding endpoint/crossing shield contradicts source
unit separation or the strict guard. Since `x` is interior to the old source hull,
`|x-r|<D` also holds. Thus the claimed inclusion `S_C^circ subset U_R` is valid.

Choose a nonisolated positive-contact source vertex `v`, put
`R=A\(Z\cup{v})`, and use the strict safe-region hypothesis
`area(S_C^circ)>a_0 z`. Translation averaging for the unit triangular lattice gives
at least `z+1` lattice sites. A sufficiently small dilation about a common center
keeps these finitely many sites in the open safe region and makes every internal
distance strictly larger than one. Cross distances to `R` remain strictly between one
and `D`.

Replacing `Z` and `v` by any `z+1` of these sites preserves cardinality, creates no
new unit contact, and removes every contact incident to `v`. Because `v` is
nonisolated, at least one contact is removed. If the new diameter is below `D`, global
minimality is contradicted; if it remains `D`, contact-minimality is contradicted.
This is a valid one-site exchange and does not require the competitor to remain
triangle-free.

The internal and exterior residual inequalities are algebraically consistent with the
audited safe-area bounds. In particular, dividing the internal bound
`area(S)>=A_C-m c_*-h_*` by the lattice covolume gives
`r_partial-kappa_* m-C_*`, and the exterior calculation gives the displayed
`r_C-kappa_* ell-lambda_* s-h_*/a_0`. Floors are retained in the finite packing
statement.

The report does not prove that any actual Type-I container satisfies the strict
capacity inequality, and it does not cover the degenerate case with no nonisolated
positive-contact vertex. Those are scope limits, not algebraic errors.

**Verdict:** PASS as a proof-only Type-I exchange criterion. It sharpens the remaining
capacity target but does not establish the target or close C-II.

## 3. Linear non-tooth boundary deficit

In Type II, the audited loaded-hull localization gives `c_B=0` and hence
`e_BB=q-m=Q+2k+u_B`. Since every nonquadrilateral bounded face contributes at least
one degree unit, `f<=Q`. Therefore

\[
2f-k\le 2Q-k=2e_{BB}-5k-2u_B\le2e_{BB}.
\]

The audited all-defect phase gap supplies

\[
\liminf\frac{2f-k}{D}\ge
\gamma,
\qquad
\gamma=2\sqrt{\Delta_2}-\frac\pi2.
\]

Dividing the finite inequality gives
`liminf e_BB/D >= gamma/2`, with

\[
\frac\gamma2
=\sqrt{\frac\pi{2\sqrt3}}-\frac\pi4
=0.1669146434\ldots.
\]

Section 130 identifies `r_deep=m-T_triangle`, so
`q-T_triangle=e_BB+r_deep>=e_BB`. The same explicit lower bound therefore applies
to the non-two-edge-tooth boundary deficit. No assumption is made that the deficit is
all deep detour; direct loaded unit sides already contribute through `e_BB`.

**Verdict:** PASS as an audited-working Type-II stability statement, conditional on
the named audited phase-gap theorem. It excludes an asymptotically pure two-edge-tooth
boundary but leaves the unit-side geometry and the full-core source-level closure open.

## Final disposition

All three reviewed findings are mathematically consistent at their stated scopes. They
are proof-only/audited-working results, not canonical promotions. C-II remains open;
the Type-I capacity inequality, rounded long-side incompatibility, and source-level
use of the forced unit-side population are still the live obligations.
