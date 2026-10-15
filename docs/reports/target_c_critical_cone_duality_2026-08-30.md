<!-- theorem-state: {"artifact_id":"ART-986E98C9A325","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: critical-cone duality and diameter shear

**Date:** 2026-08-30  
**Repository state:** `research/target-c-force-hull-2026-08-30` after `target_c_force_hull_2026-08-30.md`  
**Run type:** proof / exact reduction  
**Target:** Level I candidate route C  
**Active prompt:** `docs/prompts/erdos_problem_99_1.7.9_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** orientation only; no external theorem used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This addendum closes the first-order part of the weak-contact question left open in
`target_c_force_hull_2026-08-30.md`.

The conclusion is exact: an active unit or diameter constraint is absent from the
support of every normalized KKT stress **if and only if** it can be made strictly
feasible in a fixed-diameter first-order critical direction.  Moreover all such weak
constraints can be made strict simultaneously in one direction.

The remaining obstruction to turning that direction into an actual same-`D` path is
also exact.  It is differential angular motion among the KKT-supported diameter
chords.  If all supported diameter chords have one common angular velocity, the
first-order release integrates by a straight motion after subtracting one infinitesimal
rigid rotation.

---

## 1. Signed fixed-diameter critical cone

Let `A={p_1,...,p_n}` be any global minimizer of diameter `D>1`.  Let `C` be its unit
contacts and `H` its diameter pairs.

For a velocity `v=(v_1,...,v_n)`, define the signed active first variations

\[
\phi_{ij}(v)
=(p_i-p_j)\cdot(v_i-v_j)
\qquad(ij\in C),
\tag{C6.1}
\]

\[
\phi_{ij}(v)
=-(p_i-p_j)\cdot(v_i-v_j)
\qquad(ij\in H).
\tag{C6.2}
\]

Thus positive `\phi` means movement into the feasible side at fixed diameter:
contacts lengthen and diameter pairs shorten.

Define

\[
\boxed{
\mathcal K_D(A)
=\{v:\phi_e(v)\ge0\text{ for every }e\in C\cup H\}.
}
\tag{C6.3}
\]

This is the linearized feasible cone with the diameter variable held fixed.

Let `R` be the matrix whose rows are the linear functionals `\phi_e`.  Then

\[
\mathcal K_D(A)=\{v:Rv\ge0\}.
\tag{C6.4}
\]

Let `C_*`, `H_*` be the maximal normalized KKT supports from Theorem C4 of the
preceding report, and put

\[
E_*:=C_*\cup H_*,
\qquad
W:=(C\cup H)\setminus E_*.
\tag{C6.5}
\]

The members of `E_*` will be called **strong** active constraints and those of `W`
**weak** active constraints.  By definition, a weak active constraint has multiplier
zero in every normalized KKT stress.

---

## 2. Exact KKT-support / critical-cone duality

### Theorem C6 (simultaneous first-order weak release)

For every active constraint `e\in C\cup H`,

\[
\boxed{
e\in E_*
\iff
\phi_e(v)=0\text{ for every }v\in\mathcal K_D(A).
}
\tag{C6.6}
\]

Equivalently, the maximal KKT support is exactly the set of active constraints that
are frozen to first order throughout the fixed-`D` critical cone.

Furthermore there exists one velocity `v^\circ\in\mathcal K_D(A)` such that

\[
\boxed{
\phi_e(v^\circ)=0\quad(e\in E_*),
\qquad
\phi_e(v^\circ)>0\quad(e\in W).
}
\tag{C6.7}
\]

Thus **all** universally zero-KKT active constraints can be released strictly and
simultaneously at first order.

#### Proof

A nonnegative vector `\lambda=(\lambda_e)_{e\in C\cup H}` satisfies

\[
R^{\mathsf T}\lambda=0
\tag{C6.8}
\]

exactly when its contact and diameter coordinates give a nonnegative equilibrium
dependence of the signed active rows.  A nonzero such dependence must contain a
diameter coordinate.  Indeed, a nonzero nonnegative dependence supported only on
contacts would be a positive equilibrium stress on a finite free contact framework;
choosing a vertex uniquely extreme in a generic direction among the stressed vertices
makes all positive incident contact forces point strictly into one half-plane, so they
cannot balance.

Consequently every nonzero `\lambda\ge0` satisfying (C6.8) can be rescaled so that
its diameter coordinates sum to one.  After that normalization it is precisely a
normalized KKT stress: the vertex equilibrium equations are (4.2), and the usual
trace argument gives `\sum_C\alpha=D^2`.  Conversely every normalized KKT stress is
such a nonnegative dependence.  Therefore

\[
E_*
=
\bigcup_{\substack{\lambda\ge0\\R^{\mathsf T}\lambda=0}}
\operatorname{supp}\lambda.
\tag{C6.9}
\]

Suppose first that `e\in E_*`.  Choose a nonnegative dependence `\lambda` with
`\lambda_e>0`.  For any `v\in\mathcal K_D(A)`, every coordinate of `Rv` is
nonnegative, while

\[
0
=
\lambda^{\mathsf T}Rv
=
\sum_f\lambda_f\phi_f(v).
\tag{C6.10}
\]

Every term is nonnegative, so the term with positive coefficient `\lambda_e` must
vanish.  Hence `\phi_e(v)=0` for every `v\in\mathcal K_D(A)`.

Conversely suppose `\phi_e(v)=0` for every `v\in\mathcal K_D(A)`.  Write `r_e` for
the row vector representing `\phi_e`.  Since both `r_e` and `-r_e` vanish on the cone
`\{v:Rv\ge0\}`, the vector `-r_e` belongs to its dual cone.  Farkas duality gives

\[
-r_e=\sum_f\mu_f r_f
\qquad(\mu_f\ge0).
\tag{C6.11}
\]

Therefore

\[
(1+\mu_e)r_e+\sum_{f\ne e}\mu_f r_f=0,
\tag{C6.12}
\]

which is a nonzero nonnegative dependence with a strictly positive `e` coordinate.
By (C6.9), `e\in E_*`.  This proves (C6.6).

Now take any weak constraint `e\in W`.  By the contrapositive of (C6.6), there is a
velocity `v^{(e)}\in\mathcal K_D(A)` with

\[
\phi_e(v^{(e)})>0.
\tag{C6.13}
\]

Set

\[
v^\circ:=\sum_{e\in W}v^{(e)}.
\tag{C6.14}
\]

The cone is convex, so `v^\circ\in\mathcal K_D(A)`.  For a fixed weak `f`, every
summand satisfies `\phi_f(v^{(e)})\ge0` and the `e=f` summand is strictly positive;
hence `\phi_f(v^\circ)>0`.  Every strong constraint is identically zero on the whole
critical cone by (C6.6).  This proves (C6.7). `\square`

### Interpretation

Theorem C6 is the general first-order theorem that the activation-specific Sections
153 and 156 could not provide.  It does not say that an arbitrary weak constraint can
be removed by a finite motion.  It says that there is **no first-order locking at
all**: every weak active inequality is simultaneously pointed into its strict feasible
side.

The obstruction is therefore necessarily second-order or higher.

---

## 3. The exact second-order obstruction is diameter shear

Fix any `v\in\mathcal K_D(A)` satisfying

\[
\phi_e(v)>0\qquad(e\in W).
\tag{C7.1}
\]

Theorem C6 guarantees at least one such `v` whenever `W` is nonempty.

For every strong diameter edge `h=ij\in H_*`, Theorem C6 gives

\[
(p_i-p_j)\cdot(v_i-v_j)=0.
\tag{C7.2}
\]

In the plane there is therefore a unique scalar `\omega_h(v)` such that

\[
\boxed{
v_i-v_j
=
\omega_h(v)J(p_i-p_j)
\qquad(h=ij\in H_*),
}
\tag{C7.3}
\]

where `J` is the quarter-turn.  Explicitly,

\[
\omega_h(v)
=
\frac{J(p_i-p_j)\cdot(v_i-v_j)}{D^2}.
\tag{C7.4}
\]

These are the first-order angular velocities of the KKT-supported diameter chords.

### Theorem C7 (common-angular-rate integration)

Assume the weak-releasing velocity `v` has a common angular rate on the strong
diameter support:

\[
\boxed{
\omega_h(v)=\omega
\qquad\text{for every }h\in H_*.
}
\tag{C7.5}
\]

Then there is `\varepsilon>0` and a straight family

\[
A(t)=\{p_i+t\widetilde v_i:1\le i\le n\},
\qquad0\le t<\varepsilon,
\tag{C7.6}
\]

of global minimizers of diameter exactly `D`, where

\[
\widetilde v_i=v_i-\omega Jp_i.
\tag{C7.7}
\]

Every weak active constraint becomes strict for every sufficiently small `t>0`.
No new unit contact or diameter pair appears for sufficiently small `t`.

#### Proof

Subtracting the infinitesimal rigid rotation `\omega Jp_i` does not change any signed
first variation, since for every pair vector `r`

\[
r\cdot Jr=0.
\tag{C7.8}
\]

Hence `\widetilde v` still satisfies (C7.1), and all strong constraints still have
zero signed first variation.

For a strong diameter pair `h=ij`, equations (C7.3) and (C7.5) give

\[
\widetilde v_i-\widetilde v_j=0.
\tag{C7.9}
\]

Therefore every strong diameter pair remains **exactly** at distance `D` along the
straight family (C7.6).

For a weak diameter pair `ij`,

\[
(p_i-p_j)\cdot(\widetilde v_i-\widetilde v_j)<0.
\]
Thus

\[
|p_i(t)-p_j(t)|^2
=
D^2
+2t(p_i-p_j)\cdot(\widetilde v_i-\widetilde v_j)
+t^2|\widetilde v_i-\widetilde v_j|^2
<D^2
\tag{C7.10}
\]

for all sufficiently small positive `t`.

For a weak unit contact, the linear term has the opposite strict sign, so its squared
length is strictly larger than one for small positive `t`.  For a strong unit contact,
the linear term vanishes and

\[
|p_i(t)-p_j(t)|^2
=
1+t^2|\widetilde v_i-\widetilde v_j|^2
\ge1.
\tag{C7.11}
\]

Every initially inactive pair has strict slack between `1` and `D`, so all inactive
inequalities remain strict after shrinking `\varepsilon` uniformly.

At least one strong diameter pair exists, because every normalized KKT stress has
positive total diameter multiplier.  Equation (C7.9) keeps such a pair at distance
exactly `D`.  Hence every `A(t)` is unit-separated and has diameter exactly `D`; since
`D=D(n)`, it is again a global minimizer.  Its unit-contact graph is a subgraph of the
original one, so triangle-freeness is preserved whenever the source is triangle-free.
Every weak active constraint is strict by (C7.10) and its contact analogue. `\square`

---

## 4. Consequence for contact-minimal counterexamples

### Corollary C7.1 (weak contacts force nontrivial diameter shear)

Let `A` be a triangle-free global minimizer with the minimum possible number of unit
contacts.  If `C\setminus C_*` is nonempty, then **no** velocity satisfying strict
simultaneous weak release can have one common angular rate on `H_*`.

Equivalently, for every `v\in\mathcal K_D(A)` with

\[
\phi_e(v)>0\qquad(e\in W),
\]

there exist `h,k\in H_*` with

\[
\boxed{
\omega_h(v)\ne\omega_k(v).
}
\tag{C7.12}
\]

In particular,

\[
\boxed{
|H_*|=1
\quad\Longrightarrow\quad
C_*=C
}
\tag{C7.13}
\]

for every contact-minimal triangle-free global minimizer.

#### Proof

If a strictly weak-releasing `v` had common angular rate, Theorem C7 would produce
nearby same-`D` triangle-free global minimizers in which every weak unit contact is
strict and no new contact appears.  Since at least one weak contact exists, the new
configuration has strictly fewer unit contacts, contradicting contact minimality.
This proves (C7.12).  When `|H_*|=1`, a common angular rate is automatic, so no weak
unit contact can exist. `\square`

Thus a contact-minimal counterexample has the exact dichotomy

\[
\boxed{
C_*=C
\quad\text{or}\quad
\text{every relative-interior fixed-}D\text{ critical motion differentially rotates }
H_*.
}
\tag{C7.14}
\]

The second branch is the **diameter-shear obstruction**.

---

## 5. Linear shear map

Theorem C6 implies that every strong diameter row vanishes on the whole critical cone,
so (C7.4) defines a linear map

\[
\Omega:\mathcal K_D(A)\longrightarrow
\mathbb R^{H_*}/\langle\mathbf1\rangle,
\qquad
\Omega(v)=[(\omega_h(v))_{h\in H_*}].
\tag{C8.1}
\]

The quotient removes the common infinitesimal rotation of the whole configuration.
Theorem C7 says exactly

\[
\boxed{
\Omega(v)=0
\text{ for one strictly weak-releasing }v
\Longrightarrow
\text{all weak active constraints admit a finite same-}D\text{ release}.
}
\tag{C8.2}
\]

For a contact-minimal triangle-free minimizer with a weak contact,

\[
\boxed{
\Omega(v)\ne0
\qquad
\text{for every }v\text{ with }\phi_W(v)>0.
}
\tag{C8.3}
\]

This is a much narrower obstruction than arbitrary nonlinear rigidity.  The entire
failure of first-order weak release to integrate is carried by relative angular motion
of genuine, positively KKT-supported diameter chords on the canonical force hull.

The map is invariant under infinitesimal translations and rotations by construction.

---

## 6. Regression and scope audit

| Regression / issue | Result | Reason |
| --- | --- | --- |
| Unit square | passes | `C_*=C`, so no weak contact is predicted. |
| Regular pentagon | passes | No claim that the diameter-shear branch is absent. |
| `n=8` heptagon plus center | passes | The invisible center has no active unit contact; C7.1 concerns weak contacts. |
| Monotone activation forest | passes | Section 156 already supplies a finite release; C6 recovers the first-order release abstractly, while C7 gives only a sufficient general integration condition. |
| Locked simultaneous-transition cages | passes | C6 is first-order only; differential angular motion of `H_*` can obstruct C7. |
| Five-sector pinned regression | passes | Arbitrary pins are not the KKT-supported diameter set `B_*`. |
| Tangent-quartic regressions | passes | C7 explicitly identifies tangential diameter motion as the remaining higher-order obstruction rather than asserting it is harmless. |

Two false strengthenings are **not** claimed:

1. universal zero KKT multiplier does not by itself imply a finite release;
2. a zero first derivative on a strong diameter edge does not make a straight motion
   feasible, because tangential relative velocity increases its length at quadratic
   order.

Theorem C7 removes exactly the latter obstruction when all strong diameter tangential
motions are one common rigid rotation.

---

## 7. Revised Target C endpoint

The weak-contact release problem is no longer open at first order.  The exact missing
statement is now:

> **Target C3 (diameter-shear elimination).**  For every sufficiently large
> contact-minimal, diametrally saturated, triangle-free global minimizer, prove either
> 
> \[
> C_*=C,
> \]
> 
> or find a strictly weak-releasing `v\in\mathcal K_D(A)` with
> 
> \[
> \Omega(v)=0.
> \]
> 
> The second alternative contradicts contact minimality by Theorem C7.  Therefore a
> proof of Target C3 would force every unit contact into the support of the maximal KKT
> stress.

Forcing `C_*=C` would be a major structural upgrade.  Theorem C4 of the preceding
report would then imply that **every nonisolated contact vertex lies in the canonical
same-diameter force hull** and the maximal-support KKT stress is strictly positive on
every unit contact.  Only contact-isolated points could remain mechanically invisible.
Theorem C1 places those isolated points among genuine diameter hull vertices and gives
only boundary-order many of them.

A still stronger closing theorem would then have to show that a sufficiently large
triangle-free global minimizer cannot have a full-contact positive KKT force network
of diameter `D` without permitting a strict sub-`D` replacement.  That is a smaller
class than the present Target A/B source class.

The next mathematical object to analyze is therefore not the entire weak constraint
set but the image cone

\[
\boxed{
\Omega(\mathcal K_D(A))
\subseteq
\mathbb R^{H_*}/\langle\mathbf1\rangle.
}
\tag{C8.4}
\]

A useful theorem would show that this cone contains the origin in the image of the
strict weak-release stratum, or else derive an exact signed boundary certificate from
a separating functional on the shear cone.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New exact theorem C6:
Let K_D={v: contacts have nonnegative first-order expansion and diameter pairs have
nonnegative first-order contraction}.  An active constraint belongs to the union of
all normalized KKT supports iff its signed first variation is identically zero on
K_D.  There is one v in K_D with every universally zero-KKT active constraint strict
simultaneously and every KKT-supportable constraint exactly zero to first order.

New exact theorem C7:
For a strictly weak-releasing v, every strong diameter chord h has tangential relative
velocity omega_h J r_h.  If all omega_h are equal, subtract that one infinitesimal
rigid rotation.  Then a straight motion keeps every strong diameter exactly D,
strictly releases every weak active constraint, preserves all inequalities for small
t>0, and gives same-D global minimizers.

Contact-minimal consequence:
If any weak unit contact exists, every strictly weak-releasing direction must have
nonconstant angular rates across H_*.  In particular |H_*|=1 implies every contact is
KKT-supportable.

Exact remaining Target C obstruction:
the linear diameter-shear map
    Omega: K_D -> R^{H_*}/<1>.
Eliminate shear on one relative-interior weak-release direction, or extract a rigid
boundary certificate from the separated shear cone.

Dependencies:
docs/theory/01-local-structure.md (Theorems 4.1, 5.1-5.4)
docs/theory/02-nonlinear-and-regressions.md (virtual work context)
docs/reports/target_c_force_hull_2026-08-30.md (C3-C4 force hull)
```
