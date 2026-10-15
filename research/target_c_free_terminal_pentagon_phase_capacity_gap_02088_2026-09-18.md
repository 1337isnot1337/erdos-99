# Target C-II — failed route: exact pentagon phase capacity does not transfer to atomic windows

**Date:** 2026-09-18  
**Status:** FAILED ROUTE / correction of an invalid finite-source transfer  
**Scope:** terminal full-core Type-II FREE branch  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This file originally claimed a terminal FREE gap `epsilon=0.02088` by combining the
new bounded-pentagon no-parallel-side lemma with the dominant atomic `pi/3` train orbit.
That claim is invalid and is withdrawn.

The local geometric lemma discovered during the attempt is correct:

\[
\boxed{
\text{a strict bounded unit-contact pentagon contains at most two sides in one}
\text{ exact projective }\pi/3\text{ orbit.}
}
\tag{FR.1}
\]

The failure is the next step.  A positive atom in a limiting train-direction measure
does **not** imply that the corresponding finite-source trains have exactly the atomic
direction.  It implies only that a linear population lies in shrinking neighborhoods
of that direction after the subsequence and order of limits are fixed.  Therefore
(FR.1) cannot be applied occurrence-by-occurrence to the finite sources that carry the
atomic mass.

This is not a technical epsilon loss.  The repository already contains the matching
near-orbit regression: bounded unit pentagons can have all five side directions
arbitrarily close to one triangular-lattice three-line orbit while remaining strict
contact faces.  Their two forced `120 degree` ears become noncontact diagonals with
length tending to one from above.  Hence there is no uniform neighborhood of the
three-axis orbit in which a pentagon has only two allowed occurrences.

The attempted `0.02088` scalar certificate only verifies the algebra **conditional on
an invalid bounded-occurrence cap**.  It is not a certificate for a theorem and has
been removed from the repository.

---

## 1. The exact local lemma remains valid

Fix one exact projective `pi/3` orbit.  After rotation choose unit representatives

\[
u_0=1,
\qquad
u_1=e^{i\pi/3},
\qquad
u_2=e^{2i\pi/3}.
\]

The bounded-pentagon no-parallel-side theorem says that a strict bounded unit-contact
pentagon has no projectively parallel pair of sides.

Suppose three pentagon sides belonged exactly to the orbit.  They must use three
distinct projective axes.  Their oriented side vectors are

\[
s_0u_0,\quad s_1u_1,\quad s_2u_2,
\qquad s_j\in\{\pm1\}.
\]

For

\[
S=s_0u_0+s_1u_1+s_2u_2,
\]

a direct calculation gives

\[
|S|^2
=3+s_0s_1+s_1s_2-s_0s_2
\in\{0,4\}.
\tag{1.1}
\]

If `v,w` are the two remaining unit side vectors, polygon closure gives

\[
v+w=-S.
\]

If `|S|=0`, then `v=-w`; if `|S|=2`, equality in the triangle inequality gives
`v=w`.  Either way the last two sides are projectively parallel, contradiction.
Therefore (FR.1) is correct.

For a general strict convex face, each projective direction can occur at most twice,
so one exact three-axis orbit contributes at most six side occurrences.  These are
finite exact-direction statements.

---

## 2. The invalid transfer

Let the limiting stopped-train direction measure have an atom of mass `M` at a
direction `theta`.  Weak convergence does not say that `(M-o(1))D` finite-source
trains have direction exactly `theta`.  The valid statement is: after choosing a
small neighborhood `I_eta(theta)` whose boundary has zero limiting mass, the finite
source has `(M+o_eta(1)+o_D(1))D` train mass in that neighborhood.  The neighborhood
radius is sent to zero only after the finite-source limit.

The retracted proof silently replaced

```text
train direction lies in a shrinking window around one of three atomic axes
```

by

```text
train direction equals one of the three atomic axes.
```

That replacement is false.  It was used to claim that a pentagon could absorb at most
two dominant-orbit terminal occurrences and to force the remaining dominant mass onto
the outer walk.  Every subsequent outer-energy inequality depended on that count.

The audited dominant-orbit outer-energy theorem itself handles this issue correctly:
it freezes positive-radius windows first and only sends the radius to zero after the
measure argument.  The attempted pentagon cap did not.

---

## 3. Why the error cannot be repaired by choosing a smaller fixed window

The existing near-contact pentagon theorem proves the relevant obstruction explicitly.
For every sufficiently small fixed `eta`, there can be bounded unit pentagons whose
five projective side directions all lie within `eta` of one three-line `pi/3` orbit.
Closure forces a discrete near-sixth-root pattern, producing two `120 degree` ears.
The corresponding nonedge diagonals satisfy

\[
1<d\le2\cos(\pi/3-\eta),
\]

so `d->1` as `eta->0`.

Thus exact equality is singular here.  At `eta=0`, the complete unit-contact condition
would create a forbidden unit chord; for every positive `eta`, the chord may remain a
legal noncontact with arbitrarily small slack.  There is no fixed angular exclusion
that converts the exact cap (FR.1) into an asymptotic cap on atomic-window incidence.

Any successful continuation of this route must pay for those near-unit ear diagonals.
It would need a quantitative lower bound connecting their slack to one of the existing
currencies, for example outer detour, chamber surplus, active-diameter incidence, or a
source-preserving deformation.  The exact no-parallel theorem alone is insufficient.

---

## 4. What remains valid from this research run

The earlier live detour-pinching theorem in
`target_c_free_terminal_live_detour_pinching_2026-09-18.md` does **not** use the invalid
exact-direction transfer.  Its certificate and hostile audit remain valid.  In the
live `epsilon=0.00710` window it proves

\[
\delta>0.017609,
\qquad
a+2r<0.000282,
\qquad r<0.000141,
\]

raises the universal pair-shield exact-flex floor to

\[
\liminf m_D/D>1.1988388040,
\]

and tightens the one-anchor corank base to `0.15230481`.

The new exact local lemma (FR.1) is also valid and may be useful when an argument
produces genuine exact phase alignment at a finite source, rather than merely atomic
alignment in the limit.

---

## 5. Correct next target

The near-orbit regression identifies the actual missing bridge.  A dominant atomic
window can place five almost-triangular-lattice sides on a pentagon only by creating
near-unit noncontact ears.  The next useful theorem should quantify the aggregate cost
of a linear population of those ears, or show that their vanishing slack is
incompatible with the already forced `>1.1988D` positively locked exact contact-flex
manifold.

No `0.02088` gap is claimed.  No theorem-state file is changed.

**Disposition:** retracted the invalid atomic-window-to-exact-direction transfer,
retained the exact three-axis pentagon lemma as a finite statement, and isolated the
near-contact ear slack as the precise obstruction to this route.  C-II remains open.
