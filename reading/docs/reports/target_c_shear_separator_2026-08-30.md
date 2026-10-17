> Generated reading edition · [exact source](../../../docs/reports/target_c_shear_separator_2026-08-30.md) · source SHA-256 `c8c7e9ce240d46052e092d7241cb10c72cea0ab332d0d6cc52e550da94c292db`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-DC194C7EDEA6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: the diameter-shear separator

**Date:** 2026-08-30  
**Repository state:** `research/target-c-force-hull-2026-08-30`  
**Run type:** proof / dual-certificate reduction  
**Target:** Level I candidate route C  
**Depends on:** `target_c_force_hull_2026-08-30.md`, `target_c_critical_cone_duality_2026-08-30.md`  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The preceding addendum reduces failure of finite weak-contact release to nonconstant
angular velocities of the KKT-supported diameter chords.  This note dualizes that
obstruction.

If no relative-interior critical direction has zero diameter shear, there is a
nontrivial **self-equilibrated tangential load** on the strong diameter chords, with
zero total torque, that can be carried by a nonnegative combination of the ordinary
radial active-constraint rows.  At least one weak active constraint is used in that
radial carrier.

This is an exact alternative.  It turns the remaining nonlinear-looking obstruction
into a finite boundary statics problem.

---

## 1. Setup

Keep the notation of Theorems C6-C7.  Thus

```math
\mathcal K_D(A)=\{v:Rv\ge0\}
\tag{C9.1}
```

is the fixed-diameter critical cone, `E_*=C_*\cup H_*` is the maximal KKT support,
and `W` is the universally zero-KKT active set.

By Theorem C6, every row in `E_*` vanishes identically on `\mathcal K_D(A)`, while
there is a point of the cone where every row in `W` is strictly positive.  Therefore

```math
\operatorname{ri}\mathcal K_D(A)
=
\{v\in\mathcal K_D(A):\phi_e(v)>0\text{ for every }e\in W\},
\tag{C9.2}
```

where relative interior is taken in the linear span of the cone.

For `h=ij\in H_*`, put

```math
\omega_h(v)
=
\frac{J(p_i-p_j)\cdot(v_i-v_j)}{D^2}.
\tag{C9.3}
```

Since the radial first variation of every strong diameter edge is zero throughout the
critical cone, this is its exact first-order angular velocity.

Let

```math
Y:=\mathbb R^{H_*}/\langle\mathbf1\rangle
\tag{C9.4}
```

and define the shear map

```math
\Omega:\mathcal K_D(A)\to Y,
\qquad
\Omega(v)=[(\omega_h(v))_{h\in H_*}].
\tag{C9.5}
```

The common-rotation class is quotiented out.  Theorem C7 says that any
`v\in\operatorname{ri}\mathcal K_D(A)` with `\Omega(v)=0` integrates to a same-`D`
finite release of every weak active constraint.

---

## 2. Exact separator alternative

### Theorem C9 (diameter-shear separator)

Exactly one of the following alternatives holds.

### Release alternative

There exists

```math
v\in\operatorname{ri}\mathcal K_D(A)
\qquad\text{with}\qquad
\Omega(v)=0.
\tag{C9.6}
```

Then Theorem C7 gives a finite same-diameter release of every weak active constraint.

### Separator alternative

There exist coefficients

```math
\gamma_h\in\mathbb R
\qquad(h\in H_*),
\tag{C9.7}
```

not all zero, and nonnegative coefficients

```math
\lambda_e\ge0
\qquad(e\in C\cup H),
\tag{C9.8}
```

such that

```math
\boxed{
\sum_{h\in H_*}\gamma_h=0,
}
\tag{C9.9}
```

```math
\boxed{
\sum_{h=ij\in H_*}
\frac{\gamma_h}{D^2}
J(p_i-p_j)\cdot(v_i-v_j)
=
\sum_{c=ij\in C}\lambda_c
(p_i-p_j)\cdot(v_i-v_j)
-
\sum_{h=ij\in H}\lambda_h
(p_i-p_j)\cdot(v_i-v_j)
}
\tag{C9.10}
```

for every velocity `v`, and at least one weak coordinate is used:

```math
\boxed{
\lambda_e>0
\quad\text{for some }e\in W.
}
\tag{C9.11}
```

Moreover the left side is strictly positive on every relative-interior critical
velocity:

```math
\boxed{
\sum_{h\in H_*}\gamma_h\omega_h(v)>0
\qquad
(v\in\operatorname{ri}\mathcal K_D(A)).
}
\tag{C9.12}
```

Thus persistent diameter shear is witnessed by a signed angular functional that has
one sign on the entire strict weak-release stratum.

#### Proof

The linear image

```math
L:=\Omega(\mathcal K_D(A))\subseteq Y
\tag{C9.13}
```

is a polyhedral convex cone.  A standard relative-interior property of linear maps on
polyhedral convex sets gives

```math
\Omega(\operatorname{ri}\mathcal K_D(A))
=
\operatorname{ri}L.
\tag{C9.14}
```

If the release alternative fails, then

```math
0\notin\operatorname{ri}L.
\tag{C9.15}
```

For a convex cone, the origin lies in its relative interior exactly when the cone is a
linear subspace.  Hence `L` is not a subspace.  Separate `L` from a direction opposite
its pointed part.  Equivalently, there is a nonzero functional
`\bar\gamma\in Y^*` satisfying

```math
\bar\gamma(y)\ge0\quad(y\in L),
\qquad
\bar\gamma(y)>0\quad(y\in\operatorname{ri}L).
\tag{C9.16}
```

Represent `\bar\gamma` by a vector `\gamma\in\mathbb R^{H_*}`.  Because it descends
to the quotient by the common-rotation vector, it necessarily satisfies (C9.9).
Pulling (C9.16) back by `\Omega` gives

```math
(\Omega^{\mathsf T}\bar\gamma)(v)\ge0
\qquad(v\in\mathcal K_D(A)),
\tag{C9.17}
```

with strict inequality on the relative interior.

The dual cone of
`\mathcal K_D(A)=\{v:Rv\ge0\}` is the nonnegative row cone of `R`.  Therefore there
is `\lambda\ge0` such that

```math
\Omega^{\mathsf T}\bar\gamma
=
R^{\mathsf T}\lambda.
\tag{C9.18}
```

Expanding the definitions of the signed contact and diameter rows gives exactly
(C9.10).

If `\lambda` were supported entirely on `E_*`, then every row appearing on the right
side of (C9.10) would vanish identically on `\mathcal K_D(A)` by Theorem C6.  The
right side would therefore vanish on the relative interior, contradicting the strict
inequality in (C9.16).  Hence some weak coordinate has positive `\lambda`, proving
(C9.11).  Equation (C9.12) is the pulled-back strict part of (C9.16). `\square`

---

## 3. Static interpretation

For each oriented strong diameter edge `h=ij`, write

```math
r_h=p_i-p_j.
```

The left side of (C9.10) is the virtual work of the endpoint force pair

```math
 f_i^{(h)}=\frac{\gamma_h}{D^2}Jr_h,
\qquad
 f_j^{(h)}=-\frac{\gamma_h}{D^2}Jr_h.
\tag{C9.19}
```

Each pair has zero resultant.  Its scalar moment about any origin is

```math
(p_i-p_j)\times\frac{\gamma_h}{D^2}Jr_h
=
\gamma_h.
\tag{C9.20}
```

Therefore (C9.9) says exactly that the entire tangential diameter load has zero total
torque.

The right side of (C9.10) is the virtual work of nonnegative **radial** active-edge
forces: outward along unit contacts in the signed convention and inward along diameter
pairs.  Equality for every `v` is vertexwise static equilibrium between those radial
forces and the tangential diameter loads.

Hence the separator branch can be read as

```math
\boxed{
\text{nonconstant force-hull diameter shear}
\Longrightarrow
\text{zero-resultant, zero-torque tangential boundary load}
\text{ carried by nonnegative radial active forces}.
}
\tag{C9.21}
```

At least one universally zero-KKT active constraint participates in the radial
carrier.

This is not an ordinary KKT stress: its radial row combination does not vanish.  Its
failure to vanish is exactly the tangential load on the strong diameter chords.

---

## 4. Contact-minimal consequence

Let `A` now be a contact-minimal triangle-free global minimizer.  If it has a weak unit
contact, Corollary C7.1 forbids the release alternative.  Therefore Theorem C9 forces
the separator alternative.

> **Corollary C9.1 (weak-contact boundary certificate).**  Every contact-minimal
> triangle-free global minimizer with `C\setminus C_*\ne\varnothing` admits a
> nonzero zero-sum diameter coefficient vector `\gamma` and a nonnegative radial
> carrier `\lambda` satisfying (C9.9)-(C9.12), with positive carrier mass on at least
> one weak active constraint.

This converts every surviving weak unit contact into an exact boundary statics
certificate.

In particular, a future proof need not analyze arbitrary weak-contact cages.  It can
attack the much smaller statement that no sufficiently large triangle-free global
minimizer supports a separator of the form (C9.10).

---

## 5. What the separator does and does not buy

Theorem C9 is a structural reduction, not yet a contradiction.

It removes two possible sources of vagueness:

1. **There is no hidden first-order bulk locking.**  Theorem C6 already gives strict
   simultaneous first-order release of every weak row.
2. **Failure to integrate has an exact dual boundary witness.**  It is not an
   unspecified higher-order phenomenon; it is a self-equilibrated tangential load on
   genuine KKT-supported diameter chords.

The remaining geometry is now concrete.  The strong diameter chords lie between
vertices of the canonical force hull `F(A)`, every such chord has length `D`, and the
radial carrier uses only actual unit contacts and actual diameter pairs.  Under the
triangle-free hypothesis, the contact part is a triangle-free penny graph.

The next desired theorem is:

> **Target C4 (no tangential separator).**  For every sufficiently large
> contact-minimal, diametrally saturated, triangle-free global minimizer, no
> nontrivial coefficients `\gamma,\lambda` satisfy (C9.9)-(C9.12).

A proof of Target C4 would eliminate the diameter-shear branch.  Theorem C7 would then
force `C_*=C`, i.e. every unit contact would be supportable by the maximal normalized
KKT stress.

The likely leverage is geometric sign/order on the convex force hull: the tangential
loads in (C9.19) live on diametral chords, while every nonnegative carrier force is
radial along an active distance constraint.  This is a planar statics problem and can
be attacked using support directions, cyclic hull order, or cut/torque identities
without introducing a lattice scaffold or rhombic train system.

---

## 6. Regression audit

- **Unit square:** no weak contact is present, so C9.1 is not invoked.
- **Activation/deactivation orthant:** the finite release alternative is available;
  no separator is required.
- **Tangent-quartic examples:** compatible.  They are precisely the kind of examples
  in which tangential diameter motion can carry a genuine higher-order obstruction.
- **Five-sector pinned regression:** arbitrary external pins do not instantiate the
  strong diameter set `H_*`; C9 uses actual KKT-supported diameter chords.
- **Near-extremal non-global regressions:** KKT support from global diameter
  optimality is an essential hypothesis.

No density gap, shell surplus, or source-to-independent-scaffold statement is used.

---

## 7. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Theorem C9 (diameter-shear separator):
If the strict weak-release stratum of the fixed-D critical cone contains no direction
with common angular velocity on all KKT-supported diameter chords, then there exist
nonzero coefficients gamma_h on H_* with sum gamma_h=0 and nonnegative active-row
coefficients lambda_e such that, for every velocity v,

  sum_{h in H_*} gamma_h/D^2 * J r_h dot dv_h
    = sum_{c in C} lambda_c r_c dot dv_c
      - sum_{h in H} lambda_h r_h dot dv_h.

At least one weak active constraint has lambda_e>0, and the angular functional is
strictly positive on every relative-interior fixed-D critical direction.

Static meaning:
the obstruction is a zero-resultant, zero-total-torque tangential load on genuine
force-hull diameter chords, carried by nonnegative radial active forces.

Contact-minimal consequence:
any surviving weak unit contact forces such a separator.  Therefore the next Target C
lemma is to exclude this tangential separator in sufficiently large triangle-free
global minimizers.
```
