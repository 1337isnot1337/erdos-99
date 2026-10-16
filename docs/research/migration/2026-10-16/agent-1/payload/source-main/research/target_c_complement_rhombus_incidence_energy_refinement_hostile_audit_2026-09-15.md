# Hostile audit — energy-restored complement rhombus incidence

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_complement_rhombus_incidence_energy_refinement_2026-09-15.md`
- `research/verify_target_c_complement_rhombus_incidence_energy_refinement.py`

**Disposition:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The refinement keeps the dominant selected-edge energy that the conservative
rhombus-incidence theorem discarded and raises the safe floor to

\[
\boxed{(q-k)/D\ge1.84283-o(1)}.
\]

No new geometric lemma is introduced.  The only new issue is whether the dominant
energy can be subtracted from the complement terminal-energy budget without reusing an
outer-edge occurrence.  It can.

## 1. Disjoint energy supports

The shared-retention construction partitions selected outer occurrences by complete
stopped-train class: dominant-window trains versus complement trains.  A physical
outer edge occurrence belongs to one complete train.  Hence the dominant selected
occurrences and complement terminal occurrences are disjoint in the occurrence-counted
outer walk.

The dominant bathtub theorem charges at least `F(z)D-o(D)` on the first set.  If `e_cD`
is the weighted exact terminal energy on the second set, then

\[
F(z)+e_c\le\delta+o(1).
\]

Thus

\[
e_c\le\delta-F(z)+o(1)
\]

is valid.  This uses additive edge energy `F`, not the joint capacity function `Phi`.
There is no double counting of route detour.

**Verdict:** PASS.

## 2. Elimination of `p`

The audited incidence theorem gives

\[
p(1-\delta)-e_c/2\le r_2(U)^2/2+o(1).
\]

Substituting the preceding upper bound on `e_c` yields

\[
p\le{\delta-F(z)+r_2(U)^2\over2(1-\delta)}+o(1).
\]

Together with shared retention `z+p>=S-o(1)`, every feasible `z` satisfies

\[
z+{\delta-F(z)+r_2(U)^2\over2(1-\delta)}\ge S-o(1).
\]

The left side has derivative

\[
1-{F'(z)\over2(1-\delta)}>0.929
\]

throughout the certified range, so it is strictly increasing.  The implicit threshold
`Z_*` is therefore unique whenever it is load-bearing.  If the formal threshold moves
outside the retained-mass interval, dominant energy alone is stronger, not weaker.

**Verdict:** PASS.

## 3. Feasible-region derivatives

The candidate differentiates the implicit equation rather than numerically scanning
the feasible triangle.  The signs are correct.

At fixed `t,delta`, increasing `kappa` lowers `U`.  Since `m_2'<0`, the required shared
retained mass increases while the residual-orbit allowance decreases.  Implicit
differentiation gives `dZ_*/dkappa>0`, so `kappa=0` is weakest.

At fixed `t,kappa`, the certificate gives

\[
U<2.007,
\quad\delta<0.05,
\quad r_2(U)<0.11,
\quad-0.06<m_2'(U)<0.
\]

These imply

\[
G_z>0.929,
\qquad G_U<0.123,
\qquad {dZ_*\over d\delta}<2.55.
\]

Since

\[
F'(Z_*)\le1-\sqrt3/2<0.134,
\]

\[
{d\over d\delta}[F(Z_*)-\delta]
<2.55(0.134)-1<0.
\]

Thus maximal detour is weakest and the whole feasible region reduces to

\[
\kappa=0,
\qquad U=C_0,
\qquad \delta=R_{50}(t)/2.
\]

**Verdict:** PASS.

## 4. Numerical certificate

The Decimal verifier solves the monotone implicit equation by 300 bisection steps.  It
checks

\[
H(1.84283)>1.90\times10^{-5},
\]

\[
H(1.84284)<-4.60\times10^{-6},
\]

and

\[
1.84283805523<t_*<1.84283805525.
\]

At `t=1.84283`, the minimal threshold leaves only

\[
p\approx3.1545\times10^{-6}
\]

of retained complement pair mass.  The tiny value is a consequence, not an assumption.

**Verdict:** PASS.

## 5. Scope

The theorem remains proof-only because the two-bin atomic and low-`t` parents remain
proof-only.  It does not use the additional complement convex-energy term `J(p)`;
near the new root that term is cubic in an already tiny `p` and numerically negligible.
The substantive remaining branch is the dominant three-phase orbit itself.

**Final verdict:** PASS. C-II remains open.
