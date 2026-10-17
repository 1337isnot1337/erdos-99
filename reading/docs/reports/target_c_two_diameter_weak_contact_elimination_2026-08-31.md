> Generated reading edition · [exact source](../../../docs/reports/target_c_two_diameter_weak_contact_elimination_2026-08-31.md) · source SHA-256 `b129e164f7e16a3d2e1dfafe1012f73630be5d3012e81a88280bdd17c851eac5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E73683BF750A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: elimination of the two-diameter weak-contact phase

**Date:** 2026-08-31  
**Repository state:** `research/target-c-low-diameter-prestress-2026-08-31`  
**Run type:** proof / second-order duality / finite integration  
**Target:** Target C Gate C-I  
**Depends on:** C6–C7, C13, `target_c_low_diameter_prestress_2026-08-31.md` (C20), and `target_c_two_direction_cross_chain_2026-08-31.md` (C24)  
**Literature cross-check:** Connelly–Whiteley, *Second-Order Rigidity and Prestress Stability for Tensegrity Frameworks*, SIAM J. Discrete Math. 9 (1996), second-order stress test. The Farkas step is reproduced below in the present notation.

## LEVEL I STATUS

`STILL OPEN`

This report closes the entire low-diameter-support part of Target C Gate C-I.

> **Main theorem C25.**  Let `A` be a contact-minimal triangle-free global minimizer of
> diameter `D>1`.  If `A` has a weak unit contact, then
> 

```math
> \boxed{|H_*|\ge3.}
> 
```
> Equivalently, if `|H_*|<=2`, then every unit contact is strong:
> 

```math
> \boxed{C=C_*.}
> 
```

The proof combines four ingredients.

1. C20: with at most two positive diameter edges, every signed KKT matrix
   `Omega=L_C(alpha)-L_H(beta)` is PSD.
2. A direct Farkas second-order test: PSD means every critical velocity admits a
   feasible second-order acceleration; all non-blocked strong rows can be made strict.
3. C20/C24: for a strict weak-release velocity with nonconstant diameter angular rate,
   every zero-energy blocking stress is supported on one full diameter unit chain or on
   the exact two-chain cross.
4. The blocking contact graph is therefore a forest.  Its second-order bar jet can be
   integrated exactly by recursively rotating its unit edges.  Long blocking diameter
   chords stay `<=D` by the chain triangle inequality, while every other active
   constraint is strict at first or second order.

The resulting nearby configuration is unit-separated, has diameter at most `D`, and
has strictly fewer unit contacts unless its diameter is already `<D`.  Either outcome
contradicts global optimality/contact minimality.

This is a genuine C-I advance.  It does not settle the remaining `|H_*|>=3`
diameter-shear separator phase.

---

## 1. Signed first- and second-order constraints

For an active contact `c=ij`, put

```math
r_c=p_i-p_j.
```

For an active diameter pair `h=ij`, put

```math
R_h=p_i-p_j,
\qquad |R_h|=D.
```

Use the canonical signed first-order rows

```math
\phi_c(v)=r_c\cdot(v_i-v_j),
\qquad
\phi_h(v)=-R_h\cdot(v_i-v_j).
\tag{C25.1}
```

Then the fixed-D critical cone is

```math
\mathcal K_D(A)=\{v:\phi_e(v)\ge0\text{ for every active }e\}.
\tag{C25.2}
```

Let `a=(a_i)` be a candidate acceleration.  For a row whose first derivative is zero,
the favorable signed second-order coefficient is

```math
\psi_c(v,a)
=|v_i-v_j|^2+r_c\cdot(a_i-a_j)
\tag{C25.3}
```

for a contact, and

```math
\psi_h(v,a)
=-|v_i-v_j|^2-R_h\cdot(a_i-a_j)
\tag{C25.4}
```

for a diameter pair.  Second-order feasibility requires

```math
\psi_e(v,a)\ge0
\tag{C25.5}
```

on every active row with `phi_e(v)=0`.  Rows with `phi_e(v)>0` are already strict at
first order and impose no second-order condition.

For the strict weak-release velocity supplied by C6, every strong row `e in E_*` has
`phi_e(v)=0`, while every weak active row has `phi_e(v)>0`.

---

## 2. Farkas form of the second-order stress test

Fix `v in K_D(A)` and restrict to the strong rows `E_*`.  Let `R_*` be the matrix whose
contact row is `r_c` and whose diameter row is `-R_h`, acting on the acceleration
variables.  Define

```math
b_c(v)=-|dv_c|^2,
\qquad
b_h(v)=|dv_h|^2.
\tag{C25.6}
```

Then (C25.5) is exactly

```math
\boxed{R_*a\ge b(v).}
\tag{C25.7}
```

A nonnegative row dependency

```math
\lambda R_*=0,
\qquad
\lambda\ge0
\tag{C25.8}
```

is precisely an unnormalized KKT stress: write its contact coefficients as `alpha` and
its diameter coefficients as `beta`.  Every nonzero such dependency has
`sum_h beta_h>0`; the virial identity

```math
\sum_c\alpha_c=D^2\sum_h\beta_h
\tag{C25.9}
```

excludes a nonzero contact-only dependency.  Hence it can be normalized to a point of
the KKT polytope.

For such a stress,

```math
\lambda\cdot b(v)
=\sum_h\beta_h|dv_h|^2
-\sum_c\alpha_c|dv_c|^2.
\tag{C25.10}
```

On the other hand C20 gives

```math
\sum_c\alpha_c|dv_c|^2
-\sum_h\beta_h|dv_h|^2
=v^{\mathsf T}(\Omega_s\otimes I_2)v
\ge0
\tag{C25.11}
```

whenever `|H_*|<=2`.  Therefore

```math
\boxed{\lambda\cdot b(v)\le0}
\tag{C25.12}
```

for every nonnegative dependency.

By the Farkas alternative, (C25.12) is exactly the necessary and sufficient condition
for (C25.7) to have a solution.

### Lemma C25.1 (second-order feasibility)

If `|H_*|<=2`, every fixed-D critical velocity admits a second-order feasible
acceleration on all strong rows.

This is the present special case of the Connelly–Whiteley second-order stress test, but
(C25.6)–(C25.12) give the complete proof needed here.

---

## 3. Partial strictness and zero-energy blockers

Define the artificial KKT energy

```math
E_s(v)
:=
\sum_c\alpha_c|dv_c|^2
-
\sum_h\beta_h|dv_h|^2
\ge0
\tag{C25.13}
```

for a normalized KKT stress `s`; nonnegativity is C20.  Let

```math
\mathcal Z(v)
:=\{s:E_s(v)=0\}.
\tag{C25.14}
```

Call a strong active member **blocked** for `v` if it is positive in some stress of
`Z(v)`.  Let

```math
X(v)=\bigcup_{s\in\mathcal Z(v)}\operatorname{supp}s.
\tag{C25.15}
```

The following strict Farkas variant is standard but we record the exact form.

### Lemma C25.2 (strictness off the blocking face)

There exists a solution `a` of (C25.7) such that

```math
\boxed{
\psi_e(v,a)>0
\qquad
(e\in E_*\setminus X(v)).
}
\tag{C25.16}
```

#### Proof

For a finite linear system `Ax>=b`, a feasible point can be chosen strict on a selected
set `S` of rows iff every nonnegative dependency `lambda A=0` satisfying
`lambda·b=0` has `lambda_i=0` for all `i in S`.  One proof is to maximize a common
slack `epsilon` under

```math
A_i x\ge b_i+\epsilon\quad(i\in S),
\qquad
A_i x\ge b_i\quad(i\notin S).
```

If the maximal `epsilon` were zero, LP duality supplies a nonnegative dependency with
zero `lambda·b` and positive mass on `S`.

Apply this to `A=R_*`, `b=b(v)`, and `S=E_*\\X(v)`.  Equality
`lambda·b=0` is exactly `E_s(v)=0` after normalization, so by definition every such
dependency is supported inside `X(v)`.  The strictness criterion holds. `square`

### Lemma C25.3 (blocked rows are automatically second-order equalities)

For the acceleration in Lemma C25.2,

```math
\boxed{
\psi_e(v,a)=0
\qquad
(e\in X(v)).
}
\tag{C25.17}
```

#### Proof

Take a blocked row `e`.  Some zero-energy stress `s in Z(v)` has positive multiplier on
`e`.  All second-order signed slacks are nonnegative.  Their multiplier-weighted sum is

```math
\sum_{c}\alpha_c\psi_c(v,a)
+\sum_h\beta_h\psi_h(v,a)
=E_s(v)=0,
\tag{C25.18}
```

because acceleration terms cancel by equilibrium.  Every positively weighted
nonnegative term must therefore be zero, including the term for `e`. `square`

---

## 4. A strict weak-release velocity has a zero-energy stress

Assume from now on that `A` is contact-minimal and has a weak unit contact.  Choose the
C6 relative-interior velocity `v` that releases every weak active row strictly.

C13.3 gives a normalized KKT stress `s` with

```math
\sum_h\beta_h|dv_h|^2
-
\sum_c\alpha_c|dv_c|^2
\ge0.
\tag{C25.19}
```

C20 gives the reverse inequality when `|H_*|<=2`.  Hence equality holds:

```math
\boxed{E_s(v)=0.}
\tag{C25.20}
```

Thus `Z(v)` is nonempty and `X(v)` contains at least one positive diameter edge and at
least one positive contact chain.

If all strong diameter chords had one common angular rate under `v`, C7 would already
integrate the strict weak release and contradict contact minimality.  Therefore in the
only case still needing analysis,

```math
|H_*|=2
\tag{C25.21}
```

and the two strong diameter angular rates are different.

---

## 5. Classification of every zero-energy blocking stress

Fix `s in Z(v)`.

Because `Omega_s` is PSD, `E_s(v)=0` implies

```math
v\in\ker(\Omega_s\otimes I_2)
\tag{C25.22}
```

on its positive support.

### Case 1: `|H_s|=1`

C20.1 says the complete positive contact support is the exact full-D straight unit
chain joining that diameter pair.

### Case 2: `|H_s|=2`

C20 says the scalar kernel is `span{1,x,y}`, so `v` is affine on the support:

```math
v_i=Ap_i+t.
\tag{C25.23}
```

Let `S=(A+A^T)/2`.  All stressed members are strong, hence

```math
r^TSr=0
\tag{C25.24}
```

for every stressed member direction.  The two diameter directions are distinct.  If a
third projective stressed direction occurred, the planar quadratic form
`r -> r^T S r` would have three distinct projective zeros and therefore vanish
identically.  Then `A` would be infinitesimally Euclidean on the support and the two
diameter angular rates would agree, contrary to (C25.21).

Hence every positive contact is parallel to one of the two diameter directions.  C24
then applies: the support is exactly two full-D unit chains crossing at a common source
point.

We have proved:

### Lemma C25.4 (blocking-chain classification)

For the non-common-rate strict weak-release velocity, every stress in `Z(v)` has contact
support equal to either

1. the full unit chain along one member of `H_*`; or
2. the exact cross of the two full unit chains along both members of `H_*`.

Consequently the blocked **contact** set

```math
X_C(v):=X(v)\cap C_*
\tag{C25.25}
```

is the union of one or two full-D unit chains.

If both chains occur in the union, they meet in exactly one source vertex.  Indeed, if
they arise from one two-diameter zero-energy stress this is C24.  If they first arise
from two one-diameter zero-energy stresses, their positive convex combination is itself
a zero-energy two-diameter KKT stress, so C24 again forces the same crossing.

Therefore:

```math
\boxed{
X_C(v)\text{ is a forest.}
}
\tag{C25.26}
```

It is either one path or two paths meeting at one vertex.

---

## 6. Exact analytic integration of the blocking contact forest

Lemma C25.3 says the second-order jet `[v,a]` preserves every blocked contact through
second order:

```math
r_{ij}\cdot(v_i-v_j)=0,
\tag{C25.27}
```

```math
|v_i-v_j|^2+r_{ij}\cdot(a_i-a_j)=0
\tag{C25.28}
```

for every `ij in X_C(v)`.

We now integrate these bar equalities exactly, without invoking any generic rigidity
claim.

### Lemma C25.5 (forest 2-jet integration)

Let `T` be any forest of unit bars.  Suppose a velocity/acceleration pair `[v,a]`
satisfies the first- and second-order bar equalities on every edge.  Then there is a
real-analytic path `q(t)` with

```math
q(0)=p,
\qquad
q'(0)=v,
\qquad
q''(0)=a,
\tag{C25.29}
```

that preserves every bar of `T` at length exactly one for all sufficiently small `t`.

#### Proof

Root each tree component and orient its edges away from the root.  For one oriented
unit edge `ij`, write `r=p_j-p_i`.  First-order equality gives

```math
v_j-v_i=\kappa Jr
\tag{C25.30}
```

for a scalar `kappa`.  Second-order equality implies that for some scalar `eta`,

```math
a_j-a_i=-\kappa^2r+\eta Jr.
\tag{C25.31}
```

Define the exact unit edge vector

```math
r_{ij}(t)
=\operatorname{Rot}\!\left(\kappa t+\frac12\eta t^2\right)r.
\tag{C25.32}
```

It has the required first two derivatives.  Choose an analytic root curve with the
prescribed root position, velocity and acceleration, and recursively set

```math
q_j(t)=q_i(t)+r_{ij}(t).
\tag{C25.33}
```

A forest has no cycle-consistency condition, so this defines every vertex uniquely and
preserves each unit edge exactly.  Isolated vertices may use their quadratic Taylor
polynomial. `square`

Apply the lemma to `T=X_C(v)`.

---

## 7. Blocking diameter pairs remain feasible automatically

If a diameter edge `h in X(v)` is positive in a zero-energy stress, Lemma C25.4 says
its endpoints are joined in `X_C(v)` by a full chain of exactly `D` unit bars.  The
analytic path of Lemma C25.5 preserves those bars exactly, so the triangle inequality
gives

```math
\boxed{
|q_i(t)-q_j(t)|\le D
}
\tag{C25.34}
```

for every blocked diameter pair and all small `t`.

Thus there is no need to preserve the long diameter member as a bar.  The unit chain
itself protects the upper diameter constraint.

This is the key finite-integration point: the zero-energy stresses identify exactly the
members that cannot be made second-order strict, and their contact supports provide an
independent unit-bar forest whose endpoint path lengths dominate their diameter chords.

---

## 8. Every other constraint is strict

Use the analytic path from Lemma C25.5, which matches the chosen first two derivatives
on **all** vertices.

- Every weak active contact or diameter row is strict at first order by the C6 choice of
  `v`.
- Every strong active row outside `X(v)` is strict at second order by Lemma C25.2.
- Every blocked contact is held exactly at unit length by Lemma C25.5.
- Every blocked diameter is at most `D` by (C25.34).
- Every inactive contact has initial distance `>1`, and every inactive diameter pair has
  initial distance `<D`; compact finiteness preserves these strict slacks for small
  `t`.

Therefore for all sufficiently small positive `t`,

```math
\boxed{
\min_{i\ne j}|q_i(t)-q_j(t)|\ge1,
\qquad
\operatorname{diam}q(t)\le D.
}
\tag{C25.35}
```

At least one original weak unit contact is now strictly longer than one.  No previously
inactive pair can become a new unit contact for sufficiently small `t`.

If `diam q(t)<D`, then (C25.35) is an `n`-point unit-separated configuration with
strictly smaller diameter, contradicting the definition of `D(n)`.

Otherwise `diam q(t)=D`.  Then `q(t)` is another global minimizer at the same
cardinality and diameter, but it has strictly fewer unit contacts than the chosen
contact-minimal source.  Contradiction.

This completes the proof.

### Theorem C25 (two-diameter weak-contact elimination)

Let `A` be a contact-minimal triangle-free global minimizer with `D>1`.  Then

```math
\boxed{
C\ne C_*
\quad\Longrightarrow\quad
|H_*|\ge3.
}
\tag{C25.36}
```

Equivalently,

```math
\boxed{
|H_*|\le2
\quad\Longrightarrow\quad
C=C_*.
}
\tag{C25.37}
```

Since C19 already excludes the one-dimensional force-hull phase, the only remaining
low-diameter-support source is the fully force-visible `|H_*|=2` C-II phase studied in
C23.

---

## 9. Relation to Connelly–Whiteley second-order duality

The linear-algebra step in Sections 2–3 is exactly the specialized content of the
Connelly–Whiteley second-order stress test: a first-order tensegrity motion extends to a
second-order motion iff every proper self-stress has nonpositive quadratic energy, with
a strictness refinement controlled by zero-energy stresses.

In the physical packing tensegrity, contacts are lower-bound members (struts) and
active diameter pairs are upper-bound members (cables).  Its proper stress matrix is

```math
-\Omega_s.
```

C20 therefore says every proper stress matrix is negative semidefinite when
`|H_*|<=2`.  The report reproduces the needed Farkas argument explicitly so that no
sign-convention translation is hidden in the proof.

The additional forest integration in Sections 6–8 is specific to the present packing
problem and is what upgrades a second-order flex to the finite contradiction required
by contact minimality/global diameter optimality.

---

## 10. Revised Target C-I endpoint

C-I no longer needs to handle one- or two-diameter KKT support.

A weak-contact counterexample must satisfy all of:

```math
\boxed{
\begin{array}{c}
\dim F=2,\\
|H_*|\ge3,\\
C_*\text{ connected and spanning diameter }D,\\
\text{the C9 diameter-shear separator exists for every strict weak-release direction.}
\end{array}
}
\tag{C25.38}
```

The immediate next question is therefore a **three-or-more-diameter stress theorem**.
C20 fails to give global PSD automatically once the boundary response has five or more
loaded vertices.  A useful next result would show that the negative eigenspace of
`Omega_s=L_C-L_H` is controlled by the cycle/branching structure of `H_s`, or that the
C9 zero-resultant tangential separator is incompatible with the acute diameter-star
bound C18 and the long-cycle theorem C17.

---

## 11. Audit table

| Claim | Status | Reason |
| --- | --- | --- |
| Second-order Farkas feasibility C25.1 | **proved** | Every nonnegative row dependency is a KKT stress; C20 gives the required sign. |
| Strictness outside zero-energy support C25.2 | **proved** | Standard strict Farkas/LP facial alternative. |
| Blocked rows have zero second-order slack C25.3 | **proved** | Nonnegative weighted slacks sum to zero for a zero-energy stress. |
| Zero-energy supports are chain/cross-chain C25.4 | **proved** | C20 kernel + noncommon H angular rates + C24. |
| Blocker contact graph is a forest | **proved** | One chain or two unique straight chains meeting once. |
| Exact forest 2-jet integration C25.5 | **proved** | Explicit recursive edge rotations. |
| Blocked diameters remain `<=D` | **proved** | Endpoints joined by D preserved unit bars. |
| Finite feasible contact-reducing motion | **proved** | First/second-order strictness plus exact blocker integration and inactive slack. |
| Weak contact implies `|H_*|>=3` | **proved** | Theorem C25. |
| Target C-I fully closed | **not proved** | The `|H_*|>=3` separator phase remains. |

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

NEW THEOREM C25:
For a contact-minimal triangle-free global minimizer with D>1,

    weak unit contact  ==>  |H_*| >= 3.

Equivalently, if |H_*|<=2 then C=C_*.

Proof architecture:
1. For strong active rows and critical v, the second-order acceleration system is
       R_* a >= b(v).
   Nonnegative dependencies are exactly KKT stresses, and
       lambda.b = sum_H beta|dv_H|^2 - sum_C alpha|dv_C|^2.
   C20 PSD makes this <=0 for every stress, so Farkas gives a feasible acceleration.
2. Define zero-energy stresses by equality. Strict Farkas makes every strong row outside
   their union strict at second order. Rows in a zero-energy stress automatically have
   zero second-order slack.
3. For the C6 strict weak-release v, C13 guarantees at least one zero-energy stress.
   If H angular rates were common, C7 already contradicts contact minimality. With two
   noncommon rates, every zero-energy stress is either a one-H full-D unit chain or the
   C24 exact cross of the two full-D chains. Hence blocked contacts form a forest.
4. Any first/second-order bar jet on a unit forest integrates analytically by recursively
   rotating each edge. Preserve the blocker contacts exactly. Every blocked diameter has
   endpoints joined by D such unit bars, hence remains <=D by triangle inequality.
5. Weak rows are strict first order; all other strong rows are strict second order;
   inactive rows retain slack. The finite path is unit-separated, diameter <=D, and
   loses a weak unit contact. If diameter drops, contradict D(n); if not, contradict
   contact-minimality.

C-I is now reduced to |H_*|>=3 only.
Next target: control the inertia/negative modes of Omega=L_C-L_H for three-or-more
positive diameter edges, or contradict C9 using C17/C18 diameter geometry.
```
