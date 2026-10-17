# Target C-II — corrected phase-star orbit-capacity gap `0.00534`

**Date:** 2026-09-15  
**Status:** proof-only matched atomic strengthening  
**Scope:** canonical full-core Type-II train-measure branch  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This note tightens the corrected `g=0.0053` phase-star theorem to the safe round value

\[
\boxed{g=0.00534.}
\]

It uses exactly the scope-corrected proof in
`target_c_phase_star_orbit_capacity_gap_0053_2026-09-15.md`: the physical pair penalty
is used only when the center phase mass is at most

\[
K=2/\sqrt3,
\]

while the formal `C>K` branch is handled only by the generic triangle-free crossing
bound `E<=C(W-C)`.  No hypothesis from the superseded `0.0052` draft is reintroduced.

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
C_{534}=2\sqrt{\Delta_2}+0.00534.
\]

Then the exact same dominant-orbit reduction proves

\[
\boxed{
\liminf {T-q/2\over D}\ge C_{534},
}
\tag{PC534.1}

and on the strict-rhombus train graph

\[
\boxed{
\liminf {T_R\over D}\ge C_{534},
\qquad
\liminf {\sigma_R\over D}\ge0.01068.
}
\tag{PC534.2}

## Exact certificate

The companion verifier

`research/verify_target_c_phase_star_orbit_capacity_gap_00534.py`

uses exact `Fraction` arithmetic, Machin bounds for `pi`, and integer-square-root
enclosures.  At

\[
c_0=0.94049
\]

it combines the strong concavity

\[
\Phi_{CC}\le-2
\]

with an outward bound on `Phi(c0)` and `Phi_C(c0)` to prove

\[
\boxed{
\Delta_2-\Psi(C_{534})>9.2\times10^{-6}.
}
\tag{PC534.3}

The same certificate checks:

- `C_{534}/2<K`, so the low-center optimizer lies inside the pair theorem's scope;
- the derivative at `C=W/3` is greater than `0.6285`, so the optimizer is interior;
- the dominant-mass envelope has positive derivative margin greater than `0.6086`;
- the entire `C>K` branch remains more than `0.0347` below `Delta_2`.

The non-load-bearing numerical crossing is near

\[
2\sqrt{\Delta_2}+0.00534997,
\]

so `0.00534` is close to, but still safely below, the capacity endpoint of this proof.

## Why the extra digits are now useful

The previous `0.0053` improvement was already enough to raise the restored-incidence
floor.  The present `0.00534` value is retained because it is used as a **stability
baseline**, not merely as a scalar floor.  If the Section-171 envelope `U` lies only a
small amount above `C534`, then the phase-star capacity forces the residual mass outside
the dominant exact orbit to be proportional to that excess.  That coupling is the
input for the next post-floor stability argument.

**Disposition:** proof-only matched atomic strengthening; C-II and Level I remain open.
