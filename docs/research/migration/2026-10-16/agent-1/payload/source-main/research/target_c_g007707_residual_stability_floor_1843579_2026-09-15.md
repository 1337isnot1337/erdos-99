# Target C-II — `g=0.007707` residual stability raises the full-core floor to `1.843579`

**Date:** 2026-09-15  
**Status:** proof-only downstream strengthening  
**Scope:** full-core Type-II branch  
**Dependencies:** scope-safe matched atomic gap `g=0.007707`; hostile-audited residual-stability/shared-retention/complement-incidence stack  
**Certificate:** `research/verify_target_c_g007707_residual_stability_floor_1843579.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The exact three-branch phase-star certificate now gives the matched atomic input

\[
C_{707}:=2\sqrt{\Delta_2}+0.007707,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\]

Substituting `C707` into the already-audited residual-stability and correlated
survivor system gives the new safe proof-only floor

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.843579.
}
\tag{R707.1}

A non-load-bearing solve of the weakest-corner equation is

\[
t_*=1.84357913079\ldots .
\]

The exact certificate proves the rounded value `1.843579`; it also proves that the
same corner argument is already negative at `1.843580`, so no stronger rounded claim
is made here.

---

## 1. Residual localization is unchanged

Write

\[
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D},
\]

and

\[
U={9t\over2}-2\pi-2\delta-\kappa/2.
\tag{R707.2}
\]

Let `M` be the mass of one dominant exact projective `pi/3` orbit and put

\[
h:=U-C_{707},
\qquad
R:=U-M.
\]

The exact `g=.007707` capacity verifier retains a lower strong-branch slope above
`0.5966` after residual-square subtraction.  On the whole downstream localization
range `U<=2.013`, the generic two-bin bound still gives

\[
R<0.112.
\]

Therefore the same residual-stability calculation as at `g=.0077` gives

\[
\boxed{0\le R\le1.05h.}
\tag{R707.3}

Indeed, when `M<C707`, the one-orbit capacity loss from moving below `C707` is at least
`0.596(C707-M)`, whereas all other exact orbits carry at most `R^2/4`; using
`R<0.112` closes the same algebraic bootstrap.  If `M>=C707`, the bound is immediate
from `R=U-M<=h`.

No endpoint-margin argument is needed for the rounded floor below.  The small positive
`g=.007707` endpoint capacity margin is left unused.

---

## 2. The correlated survivor system

Put

\[
x={\kappa\over2},
\qquad c=1.05.
\]

The Section-171 envelope becomes

\[
\boxed{
2\delta+x+h
=R_t:={9t\over2}-2\pi-C_{707}.
}
\tag{R707.4}

The hostile-audited routewise retention and residual-incidence argument gives retained
dominant outer-occurrence mass `z` and complement O--O pair mass `p` with

\[
z+p\ge\pi-{t\over2}-x-ch-o(1),
\tag{R707.5}

while complement-rhombus incidence is bounded by the same residual orbit mass:

\[
p(1-\delta)-{e_c\over2}
\le{c^2h^2\over2}+o(1).
\tag{R707.6}

For

\[
F(z)=z-6\sin(z/6),
\]

the selected dominant occurrences consume at least `F(z)D-o(D)` of outer directional
energy, and the selected dominant/complement edge supports are disjoint.  Eliminating
`p` gives the same survivor-capacity function

\[
Q(t,h,x)
=
F^{-1}(\delta)
+{c^2h^2\over2(1-\delta)}
-\left(\pi-{t\over2}-x-ch\right),
\tag{R707.7}

with

\[
\delta={R_t-x-h\over2}.
\]

Every survivor requires

\[
Q(t,h,x)\ge0.
\tag{R707.8}

---

## 3. The feasible triangle again collapses to `x=h=0`

At `t<=1.843579`, the exact verifier checks

\[
U<2.013,
\qquad
\delta<0.051,
\qquad
h<0.101.
\]

On the relevant inverse branch,

\[
F'(z)<0.134.
\]

Thus the parent derivative estimates remain strictly valid:

\[
\boxed{Q_x<-2.7,}
\qquad
\boxed{Q_h<-2.5.}
\tag{R707.9}

and `Q_t>0`.  Hence for fixed `t`, the largest possible survivor capacity occurs at

\[
\boxed{x=0,\qquad h=0.}
\tag{R707.10}

This reduction is useful here because the atomic improvement has already shifted the
corner enough to certify a new rounded `t` value; spending the tiny positive endpoint
capacity deficit would only produce a still smaller secondary correction.

---

## 4. Exact corner certificate

At (R707.10),

\[
\delta_0(t)
={1\over2}\left({9t\over2}-2\pi-C_{707}\right).
\tag{R707.11}

Survival requires

\[
\boxed{
\delta_0(t)\ge F\left(\pi-{t\over2}\right).
}
\tag{R707.12}

The exact verifier uses only rational arithmetic, Machin enclosures for `pi`,
integer-square-root bounds for algebraic constants, and alternating Taylor bounds for
`sin`.  At

\[
t=1.843579
\]

it proves

\[
\boxed{
F\left(\pi-{1.843579\over2}\right)-\delta_0(1.843579)
>2\times10^{-7}.
}
\tag{R707.13}

The computed outward value is approximately

\[
2.9871\times10^{-7}.
\]

At `t=1.843580`, the same verifier proves an upper bound below zero for the corner
margin.  Since `Q_t>0`, every `t<=1.843579` is excluded, proving (R707.1).

---

## 5. Frontier effect

The numerical gain from the current proof-only `1.843578` floor is only `10^-6`, and
the phase-star architecture itself is now essentially at its exact scalar ceiling.
Further decimal tuning is not the preferred route.

The simultaneous structural work is more important.  The current `t<=1.844` branch
now has hostile-audited linear center/leaf rectangle profiles, including a balanced
`0.00831D` square and a high-product `0.00409D x 0.3004D` rectangle, while the O--O
leaf cuts retain two-sided actual-diameter bracing.  The remaining numerical strip is
therefore only

\[
1.843579\lesssim t\le1.844.
\]

A closing step should couple those ordered phase-pure rectangles to the diameter graph,
or turn their inverse-diameter phase rigidity into a source-preserving deformation.

**Disposition:** proved proof-only residual propagation of the matched `g=0.007707`
input. C-II and Level I remain open.
