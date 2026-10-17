> Generated reading edition · [exact source](../../../docs/reports/target_c_second_order_variance_2026-08-30.md) · source SHA-256 `c55f5648c343c4f3e9ca09f5d651b8c01f2354109782520304f29839f28d0548`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-059DA5480253","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: angular variance and the higher-order obstruction

**Date:** 2026-08-30  
**Repository state:** `research/target-c-force-hull-v2-2026-08-30`  
**Run type:** proof / exact second-order reduction  
**Target:** Level I candidate route C  
**Depends on:** canonical Theorems 11.1 and 11.3, Target C Theorems C6-C7 and C12  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The first-order Target C analysis isolates the only obstruction to releasing every
universally zero-KKT active constraint: differential angular motion of the
KKT-supported diameter chords.  This note identifies the exact second-order quantity
that controls that obstruction.

For a fixed-diameter critical velocity, every KKT-supported unit contact and diameter
pair is tangent to first order.  Write `\kappa_e` for the angular velocity of a strong
unit contact and `\omega_h` for the angular velocity of a strong diameter chord.  Two
facts then hold:

1. **exact virtual-work mean identity:** the contact and diameter angular velocities
   have the same stress-weighted mean for every normalized KKT stress;
2. **direction-dependent variance inequality:** global optimality supplies at least
   one normalized KKT stress for which the stress-weighted contact angular variance is
   at most the diameter angular-shear variance.

Thus the higher-order obstruction is not arbitrary nonlinear locking.  The rotational
strain of the connected positive unit-contact network must be paid for by angular
variance on the boundary-order diameter system.

---

## 1. Angular coordinates on the strong support

Let `A={p_1,...,p_n}` be a global minimizer of diameter `D>1`.  Let

```math
\mathcal K_D(A)
=
\left\{v:
\begin{array}{ll}
(p_i-p_j)\cdot(v_i-v_j)\ge0,&ij\in C,\\
(p_i-p_j)\cdot(v_i-v_j)\le0,&ij\in H
\end{array}
\right\}
\tag{C13.1}
```

be the fixed-diameter critical cone.  Let `E_*=C_*\cup H_*` be the maximal normalized
KKT support from Target C Theorem C4.

By Target C Theorem C6, every strong active row vanishes identically on
`\mathcal K_D(A)`.  Therefore for every `v\in\mathcal K_D(A)` and every
`e=ij\in C_*` there is a unique scalar `\kappa_e(v)` with

```math
\boxed{
v_i-v_j=\kappa_e(v)J(p_i-p_j),}
\tag{C13.2}
```

while for every `h=ij\in H_*` there is a unique scalar `\omega_h(v)` with

```math
\boxed{
v_i-v_j=\omega_h(v)J(p_i-p_j).}
\tag{C13.3}
```

The contact vector has length one and the diameter vector has length `D`, so

```math
|v_i-v_j|^2=\kappa_e^2
\quad(e\in C_*),
\qquad
|v_i-v_j|^2=D^2\omega_h^2
\quad(h\in H_*).
\tag{C13.4}
```

Adding an infinitesimal rigid rotation `v_i\mapsto v_i+\eta Jp_i` adds the same scalar
`\eta` to every `\kappa_e` and every `\omega_h`.  Hence only centered angular
velocities have intrinsic meaning.

---

## 2. Exact angular-mean identity

### Theorem C13.1 (contact and diameter angular means agree)

Fix any normalized KKT stress `(\alpha,\beta)` and any
`v\in\mathcal K_D(A)`.  Then

```math
\boxed{
\sum_{e\in C_*}\alpha_e\kappa_e
=
D^2\sum_{h\in H_*}\beta_h\omega_h.
}
\tag{C13.5}
```

Since

```math
\sum_C\alpha_e=D^2,
\qquad
\sum_H\beta_h=1,
```

the common weighted mean

```math
\boxed{
\bar\omega_{\alpha,\beta}(v)
:=
\frac1{D^2}\sum_C\alpha_e\kappa_e
=
\sum_H\beta_h\omega_h
}
\tag{C13.6}
```

is well defined.

#### Proof

Use the exact virtual-work identity, canonical Theorem 11.3,

```math
\sum_C\alpha_{ij}(p_i-p_j)\cdot(\xi_i-\xi_j)
=
\sum_H\beta_{ij}(p_i-p_j)\cdot(\xi_i-\xi_j),
\tag{C13.7}
```

with

```math
\xi_i=-Jv_i.
\tag{C13.8}
```

For a positive contact edge `e=ij`, (C13.2) gives

```math
(p_i-p_j)\cdot[-J(v_i-v_j)]
=
\kappa_e|p_i-p_j|^2
=
\kappa_e.
\tag{C13.9}
```

For a positive diameter edge `h=ij`, (C13.3) gives

```math
(p_i-p_j)\cdot[-J(v_i-v_j)]
=
\omega_h|p_i-p_j|^2
=
D^2\omega_h.
\tag{C13.10}
```

Every weak active constraint has zero multiplier in every normalized KKT stress, so no
other term contributes.  Substitution into (C13.7) proves (C13.5). `\square`

### Corollary C13.2 (rotation-centered form)

Put

```math
\widehat\kappa_e=\kappa_e-\bar\omega,
\qquad
\widehat\omega_h=\omega_h-\bar\omega.
\tag{C13.11}
```

Then

```math
\boxed{
\sum_C\alpha_e\widehat\kappa_e=0,
\qquad
\sum_H\beta_h\widehat\omega_h=0.
}
\tag{C13.12}
```

Equivalently, after subtracting the infinitesimal rigid rotation
`\bar\omega Jp_i`, both the contact and diameter angular fields have zero weighted
mean.

---

## 3. Second-order optimality is a variance inequality

For a normalized KKT stress define the two normalized angular variances

```math
\operatorname{Var}_{C,\alpha}(\kappa)
:=
\frac1{D^2}
\sum_C\alpha_e(\kappa_e-\bar\omega)^2,
\tag{C13.13}
```

```math
\operatorname{Var}_{H,\beta}(\omega)
:=
\sum_H\beta_h(\omega_h-\bar\omega)^2.
\tag{C13.14}
```

Both are invariant under adding an infinitesimal rigid rotation.

### Theorem C13.3 (direction-dependent angular variance inequality)

For every fixed-diameter critical velocity `v\in\mathcal K_D(A)`, there exists a
normalized KKT stress `(\alpha,\beta)` such that

```math
\boxed{
\operatorname{Var}_{C,\alpha}(\kappa)
\le
\operatorname{Var}_{H,\beta}(\omega).
}
\tag{C13.15}
```

If `v` lies in the relative interior of `\mathcal K_D(A)`, then every weak active
constraint has strict first variation, so the multiplier supplied by the theorem is
supported entirely on the strong set `E_*`.

#### Proof

Canonical Theorem 11.1 supplies, for the chosen critical velocity, a normalized KKT
stress supported on the zero-first-derivative active edges and satisfying

```math
\sum_H\beta_h|v_i-v_j|^2
-
\sum_C\alpha_e|v_i-v_j|^2
\ge0.
\tag{C13.16}
```

Every edge carrying positive multiplier is strong by the definition of maximal KKT
support.  Using (C13.4), (C13.16) becomes

```math
D^2\sum_H\beta_h\omega_h^2
-
\sum_C\alpha_e\kappa_e^2
\ge0.
\tag{C13.17}
```

For this same stress, Theorem C13.1 gives the common mean `\bar\omega`.  Because
`\sum_H\beta=1` and `\sum_C\alpha=D^2`, expanding around that common mean gives the
exact identity

```math
\begin{aligned}
&D^2\sum_H\beta_h(\omega_h-\bar\omega)^2
-
\sum_C\alpha_e(\kappa_e-\bar\omega)^2\\
&\qquad=
D^2\sum_H\beta_h\omega_h^2
-
\sum_C\alpha_e\kappa_e^2.
\end{aligned}
\tag{C13.18}
```

Thus (C13.17) is exactly (C13.15). `\square`

### Interpretation

The contact side of (C13.15) is the rotational strain of the KKT-positive
unit-distance network after removing the best stress-weighted rigid rotation.  The
diameter side is the angular shear among the positively loaded diameter chords, after
removing the same rigid rotation.

Global diameter optimality therefore forces the inequality

```math
\boxed{
\text{contact rotational variance}
\ \le\ 
\text{diameter-shear variance}
}
\tag{C13.19}
```

for at least one direction-dependent KKT certificate attached to every critical
velocity.

This is sharper than saying merely that tangential diameter motion is a second-order
obstruction: it gives the exact quadratic currency that pays for it.

---

## 4. Mechanism consequence for a contact-minimal counterexample

Let `A` now be a triangle-free global minimizer with the minimum possible number of
unit contacts, and use the maximal-support strong framework

```math
\mathcal F_*=(V(C_*),\ C_*\cup H_*).
\tag{C13.20}
```

Target C Theorem C12 says `C_*` is connected and already has Euclidean diameter `D`.

### Theorem C13.4 (weak contacts force a strong-support mechanism)

If

```math
C\setminus C_*\ne\varnothing,
\tag{C13.21}
```

then all of the following hold:

1. `F(A)=\operatorname{conv}V(C_*)` is two-dimensional;
2. `|H_*|\ge2`;
3. the bar framework `\mathcal F_*` has a non-Euclidean infinitesimal flex.

#### Proof

Target C Theorem C6 gives a velocity

```math
v^\circ\in\operatorname{ri}\mathcal K_D(A)
\tag{C13.22}
```

that strictly releases every weak active row while every strong row has zero first
variation.

If `F(A)` were one-dimensional, Target C Corollary C4.1 says the strong diameter graph
consists of the unique force-hull endpoint pair, so `|H_*|=1`.  More directly, Target C
Corollary C7.1 says `|H_*|=1` is incompatible with a weak unit contact in a
contact-minimal source.  Hence `F(A)` is two-dimensional and `|H_*|\ge2`.

Now suppose `\mathcal F_*` were infinitesimally rigid.  The restriction of
`v^\circ` to `V(C_*)` satisfies zero first variation on every strong contact and
strong diameter bar, so it would be an infinitesimal Euclidean motion on that vertex
set.  In particular all strong diameter chords would have one common angular velocity.
Target C Theorem C7 would then integrate `v^\circ` to a nearby same-`D`, triangle-free
global minimizer in which every weak unit contact is strict and no new unit contact
appears.  This has fewer unit contacts than the contact-minimal source, a contradiction.
Therefore `\mathcal F_*` is infinitesimally flexible. `\square`

So every surviving weak contact forces a very specific object:

```math
\boxed{
\text{one connected full-diameter positive unit network}
+
\text{at least two supported diameter chords}
+
\text{a genuine mixed-bar infinitesimal mechanism}.
}
\tag{C13.23}
```

The mechanism cannot be a common rigid rotation; its diameter angular shear must be
nonzero on every strict weak-release direction.

---

## 5. Stress-matrix form and a precise possible closure

For a normalized KKT stress let

```math
\Omega_{\alpha,\beta}
:=L_C(\alpha)-L_H(\beta),
\tag{C13.24}
```

where the two weighted Laplacians are placed on the same vertex set.  For any vector
field `z_i\in\mathbb R^2`,

```math
\operatorname{tr}(Z^{\mathsf T}\Omega_{\alpha,\beta}Z)
=
\sum_C\alpha_e|z_i-z_j|^2
-
\sum_H\beta_h|z_i-z_j|^2.
\tag{C13.25}
```

For a critical velocity `v`, rotating the field does not change squared edge
increments, so Theorem C13.3 is equivalently the existence of a normalized KKT stress
with

```math
\boxed{
\operatorname{tr}(V^{\mathsf T}\Omega_{\alpha,\beta}V)\le0.
}
\tag{C13.26}
```

This shows exactly where a tempting PSD route would have to enter.  If one could prove,
under additional **global-minimizer and triangle-free hypotheses**, that an
appropriate second-order KKT stress is positive semidefinite on the relevant strong
bar-flex space, then (C13.26) would force equality and place the mechanism in its
stress kernel.

That statement is **not** canonical and is not asserted here.  Canonical Corollary
11.2 already warns that affine shears are second-order neutral for every KKT tensor
identity, so a generic assertion that "KKT stress is PSD, therefore rigidity" would
still require an exact kernel classification.  This report does not revive that
invalid shortcut.

A more targeted possible closure is the following angular inequality.

> **Target C7 (angular Korn inequality, conjectural).**  Prove that for every
> relative-interior weak-release mechanism `v` of a sufficiently large triangle-free
> global minimizer, the actual strong contact network forces, for every normalized KKT
> stress relevant to Theorem 11.1,
> ```math
> \operatorname{Var}_{H,\beta}(\omega)
> \le
> \operatorname{Var}_{C,\alpha}(\kappa),
> \tag{C13.27}
> ```
> with equality only for a motion whose strong diameter angular velocities are all
> equal.

Combined with C13.15, this would force equality and then the common-angular-rate branch
of Theorem C7, contradicting contact minimality whenever a weak unit contact exists.

Equation (C13.27) is **not proved**.  Its advantage is that it is now an exact spectral
statement on the actual connected full-diameter unit-contact network, rather than an
unspecified higher-order deformation problem.

---

## 6. Regression and scope audit

- **Unit square:** all contacts are KKT-supportable; the weak-release premise of
  Theorem C13.4 is absent.
- **Regular pentagon / odd regular shell:** the symmetric positive support is connected
  and no weak contact is needed.  C13.15 is compatible with the rigid-rotation mode.
- **`n=8` heptagon plus center:** the invisible center has no unit contact in the
  standard representative, so C13.4 does not falsely force it into the strong network.
- **Activation/deactivation orthant:** those created weak rows have an exact finite
  release already; their weak-release direction can fall into the common-angular-rate
  branch, as expected.
- **Affine-shear regression:** C13.15 does not claim a negative affine quadratic
  energy.  The centered variance formulation is consistent with canonical affine
  second-order neutrality.
- **Five-sector pinned regression:** it is not a normalized global KKT force network,
  so it does not test C13.3 or C13.4.

The theorem does **not** show that the second-order stress has maximal support.  Its
`\alpha` and `\beta` may vanish on some edges of `C_*` and `H_*`.  Consequently one
must not replace the weighted variance in C13.15 by an unweighted variance over the
entire maximal support without a separate strict-complementarity theorem.

---

## 7. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Theorem C13.1:
For any normalized KKT stress and any fixed-D critical velocity v, write
    dv_e = kappa_e J r_e  on strong unit contacts,
    dv_h = omega_h J R_h on strong diameter chords.
Virtual work with xi=-Jv gives the exact common angular mean
    (1/D^2) sum_C alpha_e kappa_e = sum_H beta_h omega_h = bar_omega.

Theorem C13.3:
Canonical direction-dependent second-order optimality gives, for every critical v,
some normalized KKT stress satisfying
    (1/D^2) sum_C alpha_e(kappa_e-bar_omega)^2
      <= sum_H beta_h(omega_h-bar_omega)^2.
Thus contact rotational strain is paid for by diameter-shear variance.

Theorem C13.4:
In a contact-minimal triangle-free global minimizer, any weak unit contact forces the
maximal strong mixed framework C_* union H_* to be infinitesimally flexible; the force
hull is two-dimensional and |H_*|>=2.  Otherwise the strict weak-release direction is
rigid on the strong framework, all strong diameter angular rates agree, and Theorem C7
integrates it to a same-D minimizer with fewer contacts.

Exact new bottleneck:
prove a reverse angular/Poincare/Korn inequality on the actual connected full-diameter
positive unit network, strong enough to force equality in the second-order variance
inequality only for common diameter rotation.  This is a spectral boundary-shear
problem, not Target A Hall transport or Target B rhombic-shell bookkeeping.
```
