<!-- migration-source: path=docs/reports/target_c_flat_center_kkt_stress_leakage_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=db29dd2bddee80885bce634b757d2422305dbf01; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdos Problem #99 - flat-center KKT stress leakage

**Date:** 2026-09-14
**Target:** C-II, canonical contact-minimal full-core Type-II branch
**Dependencies:** flat-center contact-degree trichotomy; low-t flat-center amplification; normalized KKT virial identity
**Claim class:** proof-only structural refinement awaiting independent audit
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The flat-center trichotomy proves KKT multiplier collapse only for an unloaded
**degree-three** center. The same geometry actually controls degree four as well.
This removes the degree-four escape from the stress side of the argument.

Let `m` be the distinguished middle of a bounded pentagonal face with consecutive
unit-contact neighbors `l,r`, and write

\[
A:=\angle lmr=\pi-\delta,
\qquad 0<\delta\le\epsilon<\pi/3.
\tag{SL.1}
\]

Assume `m` is unloaded in a normalized nonnegative KKT stress. Let
`alpha_l,alpha_r` be the contact multipliers on `ml,mr`, and let

\[
\Gamma_m:=\sum_{mx\in C\setminus\{ml,mr\}}\alpha_{mx}
\tag{SL.2}
\]

be the total multiplier on the exterior contact rays at `m`. Define

\[
\lambda(\epsilon):=
{\sin\epsilon\over\sin(\pi/3-\epsilon)}.
\tag{SL.3}
\]

Then, after labeling the two face rays as in Section 1,

\[
\boxed{\Gamma_m\le\lambda(\epsilon)\alpha_l,}
\tag{SL.4}
\]

and

\[
\boxed{
|\alpha_r-\alpha_l|
\le\bigl(1-\cos\epsilon+\lambda(\epsilon)\bigr)\alpha_l.
}
\tag{SL.5}
\]

Since `lambda(epsilon)=O(epsilon)`, every unloaded flat center, of degree three
**or four**, therefore has

\[
\Gamma_m=o(1)\min\{\alpha_l,\alpha_r\},
\qquad
{\alpha_l\over\alpha_r}=1+o(1).
\tag{SL.6}
\]

The estimate is pointwise and uses no lower bound on an individual KKT multiplier.
It says instead that an unloaded almost-straight center transmits contact stress
almost losslessly from one face edge to the other while only `o(1)` relative stress
can leak into all exterior contacts combined.

The pointwise estimate globalizes. Let `U_D` be any family of distinct unloaded
flat centers with one designated pentagonal face per center and a common turn bound
`epsilon_D->0`. Then for every normalized KKT stress for which these vertices are
unloaded,

\[
\boxed{
\sum_{m\in U_D}\Gamma_m=o(D^2),
}
\tag{SL.7}
\]

and

\[
\boxed{
\sum_{m\in U_D}|\alpha_{mr_m}-\alpha_{ml_m}|=o(D^2).
}
\tag{SL.8}
\]

If the designated chains are pairwise vertex-disjoint, the same proof gives the
sharper finite bounds

\[
\sum_m\Gamma_m\le\lambda(\epsilon_D)D^2,
\tag{SL.9}
\]

\[
\sum_m|\alpha_{mr_m}-\alpha_{ml_m}|
\le\bigl(1-\cos\epsilon_D+\lambda(\epsilon_D)\bigr)D^2.
\tag{SL.10}
\]

For arbitrary distinct centers the right sides acquire only a factor two.

Combining this with the low-`t` flat-center population gives a clean binary
source/stress alternative. On `R_F=o(D)`, if

\[
{V_{flat}\over D}\ge P-o(1),
\tag{SL.11}
\]

then either

\[
\boxed{{V_{loaded}\over D}\ge {P\over2}-o(1),}
\tag{SL.12}
\]

or there are at least `(P/2-o(1))D` distinct unloaded flat centers satisfying the
aggregate leakage laws (SL.7)--(SL.8).

At the current proof-only low-`t` floor,

\[
P=0.4944166723690961\ldots,
\]

so the binary coefficient is

\[
\boxed{P/2=0.2472083361845480\ldots .}
\tag{SL.13}
\]

Throughout the conditional band `t<=1.8585`, the corresponding coefficient is

\[
\boxed{0.2001941336588539\ldots .}
\tag{SL.14}
\]

This does not close C-II. It replaces the previous three-way stress handoff by a
sharper one: either a macroscopic fraction of the flat-center sea is loaded into the
Woodall diameter system, or a macroscopic unloaded population carries an
asymptotically stress-null exterior contact network and almost equal stress across its
near-straight face chains.

---

## 1. Exterior rays lie in one lower angular window

Put `m` at the origin, rotate so the ray `mr` has angle zero, and orient so the
pentagonal face sector runs counterclockwise from `mr` to `ml`. Then

\[
u_r=(1,0),
\qquad
u_l=(\cos A,\sin A),
\qquad A=\pi-\delta.
\tag{SL.15}
\]

Every other contact ray at `m` lies on the complementary arc. Triangle-freeness and
unit separation imply that every cyclic gap between consecutive contact rays is
strictly larger than `pi/3`. Hence every exterior contact ray, with angle `phi`, obeys

\[
A+{\pi\over3}<\phi<{5\pi\over3}.
\tag{SL.16}
\]

Since `A>=pi-epsilon`,

\[
{4\pi\over3}-\epsilon<\phi<{5\pi\over3}.
\tag{SL.17}
\]

For `epsilon<pi/3` this interval lies strictly in the lower half-plane. Moreover

\[
-\sin\phi
\ge\sin(\pi/3-\epsilon)>0.
\tag{SL.18}
\]

This statement is independent of whether there is one exterior contact ray or two.
The existing degree theorem says there can be no more than two.

---

## 2. KKT projection proves total exterior-stress collapse

Because `m` is unloaded, its KKT stationarity equation has no diameter-force term.
Using unit rays from `m` to its contact neighbors,

\[
\alpha_r u_r+\alpha_l u_l+
\sum_j\gamma_j u_j=0,
\qquad \gamma_j\ge0,
\tag{SL.19}
\]

where the `gamma_j` are the exterior contact multipliers and
`Gamma_m=sum_j gamma_j`.

Project (SL.19) onto the vertical axis. Equations (SL.15) and (SL.18) give

\[
\alpha_l\sin A
=
\sum_j\gamma_j(-\sin\phi_j)
\ge
\sin(\pi/3-\epsilon)\Gamma_m.
\tag{SL.20}
\]

Since `sin A=sin delta<=sin epsilon`,

\[
\Gamma_m
\le
{\sin\epsilon\over\sin(\pi/3-\epsilon)}\alpha_l,
\]

which proves (SL.4).

Projecting onto the horizontal axis gives

\[
\alpha_r
=-\alpha_l\cos A-
\sum_j\gamma_j\cos\phi_j
=
\alpha_l\cos\delta-
\sum_j\gamma_j\cos\phi_j.
\tag{SL.21}
\]

Therefore

\[
|\alpha_r-\alpha_l|
\le
\alpha_l(1-\cos\delta)+\Gamma_m
\le
\bigl(1-\cos\epsilon+\lambda(\epsilon)\bigr)\alpha_l,
\]

proving (SL.5).

For completeness put

\[
\kappa(\epsilon):=\cos\epsilon-\lambda(\epsilon).
\tag{SL.22}
\]

As `epsilon->0`, `kappa(epsilon)->1`, so it is positive for all sufficiently small
`epsilon`. Equation (SL.21) then gives

\[
\alpha_r\ge\kappa(\epsilon)\alpha_l.
\tag{SL.23}
\]

Consequently

\[
{\Gamma_m\over\min\{\alpha_l,\alpha_r\}}
\le
{\lambda(\epsilon)\over\kappa(\epsilon)}
\longrightarrow0,
\tag{SL.24}
\]

and (SL.5) gives the second assertion of (SL.6).

This includes the previously isolated degree-three sine-law collapse and adds the
unloaded degree-four case. In degree four both exterior contact multipliers have
nonnegative weight, so (SL.4) forces their **sum**, not merely one chosen multiplier,
to collapse.

---

## 3. Aggregate leakage is subquadratic in the normalized stress budget

Normalize the KKT stress by

\[
\sum_{h\in H}\beta_h=1.
\]

The standard virial identity is

\[
\boxed{\sum_{e\in C}\alpha_e=D^2.}
\tag{SL.25}
\]

For each distinct center `m in U_D`, select the same labeled face edge `ml_m` used in
Section 2. A contact edge has only two endpoints, so it can occur as a selected
`ml_m` edge for at most two distinct centers. Hence

\[
\sum_{m\in U_D}\alpha_{ml_m}\le2D^2.
\tag{SL.26}
\]

Applying (SL.4) center by center yields the finite bound

\[
\boxed{
\sum_{m\in U_D}\Gamma_m
\le2\lambda(\epsilon_D)D^2.
}
\tag{SL.27}
\]

Likewise (SL.5) gives

\[
\boxed{
\sum_{m\in U_D}
|\alpha_{mr_m}-\alpha_{ml_m}|
\le
2\bigl(1-\cos\epsilon_D+\lambda(\epsilon_D)\bigr)D^2.
}
\tag{SL.28}
\]

Because `epsilon_D->0`, (SL.27)--(SL.28) are exactly (SL.7)--(SL.8).

If the chains `l_m-m-r_m` are pairwise vertex-disjoint, their selected face edges are
all distinct, so the factor two in (SL.26)--(SL.28) improves to one, proving
(SL.9)--(SL.10).

If `E_ext(U_D)` is the union of all exterior contact edges at the unloaded centers,
then

\[
\sum_{e\in E_{ext}(U_D)}\alpha_e
\le
\sum_{m\in U_D}\Gamma_m=o(D^2).
\tag{SL.29}
\]

Thus the statement is not merely incidence-counted: the actual union of exterior
contact rows carries `o(D^2)` total normalized contact stress.

---

## 4. Uniformity over the stress polytope

The local projection proof uses only nonnegativity and the absence of a diameter-force
term at `m`. Let `B_*` be the maximal positive diameter-endpoint support, equivalently
the support of a relative-interior normalized KKT stress. If `m notin B_*`, then every
diameter coordinate incident with `m` vanishes identically on the normalized stress
polytope. Therefore (SL.4)--(SL.5), and hence (SL.27)--(SL.29), hold for **every**
normalized nonnegative KKT stress, including boundary stresses where some contact
multipliers vanish.

In particular, on an unloaded flat-center family the exterior edge set is uniformly
asymptotically stress-null across the whole KKT polytope:

\[
\boxed{
\sup_{(\alpha,\beta)\in\mathcal P(A_D)}
{1\over D^2}
\sum_{e\in E_{ext}(U_D)}\alpha_e
\longrightarrow0.
}
\tag{SL.30}
\]

This is stronger than choosing one favorable relative-interior stress. It still does
not imply that the exterior rows can be deleted at finite `D`: a positive multiplier
may be arbitrarily small, and the repository's stress-transversal audits explicitly
warn against turning small multipliers into zero-support claims.

---

## 5. Low-t population consequence

The low-t flat-center theorem gives, on `R_F=o(D)`,

\[
{V_{flat}\over D}\ge P-o(1),
\tag{SL.31}
\]

with

\[
P=0.4944166723690961\ldots
\]

at the current proof-only `t_42` profile, and

\[
P\ge0.4003882673177079\ldots
\]

throughout the conditional band `t<=1.8585` after dropping the nonnegative detour and
topology bonuses.

Partition the distinct flat centers into loaded and unloaded centers. One class has at
least half the population. If the loaded class is larger, (SL.12) holds. If the
unloaded class is larger, it contains at least `(P/2-o(1))D` distinct centers and
Sections 2--4 apply to the whole class. This proves the binary alternative and the
constants (SL.13)--(SL.14).

The degree-four activation theorem remains compatible and complementary: every
degree-four flat center is unloaded and also supplies hidden `1+o(1)` neighbor pairs.
The new result says that its two exterior **contact** rays simultaneously carry only
`o(1)` relative KKT weight. Thus the degree-four activation branch is not a separate
stress escape.

---

## 6. Frontier effect

The small-residual low-t survivor now has a sharper KKT handoff:

```text
at least ~0.4944 D distinct flat centers at t_42
    -> either >= ~0.2472 D loaded centers
    -> or >= ~0.2472 D unloaded centers, for which
         total exterior contact stress = o(D^2),
         total face-edge stress mismatch = o(D^2),
         uniformly over the normalized KKT stress polytope.
```

A closing argument cannot dismiss the unloaded branch by an individual multiplier
floor; none exists. The next plausible finite target is instead a support or response
theorem showing that a linear family of these almost lossless two-edge stress
transmitters forces either a macroscopic loaded incidence set, an exact stress
transversal, or a forbidden diameter-response concentration.

No exact hidden contact, zero multiplier, row deletion, legal finite flex, or strict
sub-`D` competitor is asserted here.

## 7. Scope audit

- The face sector is a genuine consecutive contact-ray sector of a bounded pentagonal
  contact face.
- Strict angular gaps larger than `pi/3` use the triangle-free C-II hypothesis.
- The local theorem assumes the center is unloaded; loaded centers may have a diameter
  force and are intentionally separated in (SL.12).
- Degree four is fully covered: both exterior multipliers are included in `Gamma_m`.
- The aggregate bounds use only the normalized virial identity and edge-incidence
  multiplicity at most two.
- Uniformity over the stress polytope uses maximal-support semantics, not a uniform
  positive lower bound.
- The low-t constants inherit the proof-only low-t flat-center theorem and its
  `R_F=o(D)` hypothesis.
- C-II and Level I remain open.

---

**Recovery provenance:** copied from `research/c2-flat-stress-sol-20260914` at exact tip `92e33e034b4ae056fa51c106874ce3e9cf05b695` during the 2026-10-04 Slot 2 branch audit. This recovered claim remains unreviewed and noncanonical.
