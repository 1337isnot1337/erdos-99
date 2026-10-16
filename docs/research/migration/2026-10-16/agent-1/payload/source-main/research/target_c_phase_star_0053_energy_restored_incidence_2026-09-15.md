# Target C-II — corrected phase-star gap strengthens energy-restored rhombus incidence

**Date:** 2026-09-15  
**Status:** proof-only composition  
**Scope:** fully force-visible no-container/full-core Type-II branch  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The hostile-audited energy-restored complement-rhombus-incidence theorem used the
matched atomic floor

\[
C_{50}=2\sqrt{\Delta_2}+0.0050,
\qquad
\Delta_2={\pi\over2\sqrt3},
\]

and obtained

\[
\liminf {q-k\over D}\ge1.84283.
\]

The corrected phase-star orbit-capacity theorem gives the stronger matched input

\[
\boxed{C_{53}=2\sqrt{\Delta_2}+0.0053.}
\tag{PSER.1}
\]

Nothing else in the hostile-audited incidence/energy argument depends on the numerical
origin of the matched floor. Replacing `C50` by `C53` raises the safe proof-only
full-core floor to

\[
\boxed{
\liminf {q-k\over D}\ge1.84289.
}
\tag{PSER.2}
\]

The scalar crossing is `1.8428948160...`; only `1.84289` is claimed.

## 1. Audited variables

Write

\[
t={q-k\over D},\qquad
\kappa={k\over D},\qquad
\delta={d_{out}\over D},
\]

\[
U={9t\over2}-2\pi-2\delta-\kappa/2.
\tag{PSER.3}
\]

The corrected matched phase-star theorem gives

\[
\boxed{U\ge C_{53}.}
\tag{PSER.4}
\]

Retain

\[
m_2(U)={U+\sqrt{8\Delta_2-U^2}\over2},
\qquad
r_2(U)=U-m_2(U).
\tag{PSER.5}
\]

The shared dominant/complement retention theorem gives retained dominant outer
occurrence mass `z` and retained complement outer-to-outer pair mass `p` with

\[
\boxed{
z+p\ge
S(t,\delta,\kappa):=
\pi-U-{t+\kappa\over2}+m_2(U)-o(1).}
\tag{PSER.6}
\]

The dominant selected edges pay

\[
E_{dom}\ge F(z)D-o(D),
\qquad F(z)=z-6\sin(z/6).
\tag{PSER.7}
\]

The hostile-audited complement rhombus-incidence theorem gives, for complement
terminal directional-energy density `e_c`,

\[
p(1-\delta)-{e_c\over2}
\le {r_2(U)^2\over2}+o(1).
\tag{PSER.8}
\]

The dominant selected outer occurrences and complement terminal occurrences belong to
disjoint stopped-train classes, so their physical outer-edge energy supports are
disjoint. Hence

\[
e_c\le\delta-F(z)+o(1).
\tag{PSER.9}
\]

Thus

\[
\boxed{
p\le
{\delta-F(z)+r_2(U)^2\over2(1-\delta)}+o(1),}
\tag{PSER.10}
\]

and every survivor must satisfy

\[
\boxed{
G(z):=
 z+{\delta-F(z)+r_2(U)^2\over2(1-\delta)}
\ge S(t,\delta,\kappa)-o(1).}
\tag{PSER.11}
\]

## 2. Feasible-region reduction

The hostile audit of the parent theorem used only the conservative bounds

\[
U<2.007,
\qquad
\delta<0.05,
\qquad
r_2(U)<0.11,
\qquad
-0.06<m_2'(U)<0.
\tag{PSER.12}
\]

The new interval `1.84283<=t<=1.84290` and stronger floor `U>=C53` remain inside all
four bounds. In particular

\[
r_2(C_{53})=0.0053073947\ldots<0.006.
\]

Therefore the parent's implicit-derivative argument applies unchanged:

- `G_z>0.929`, so the threshold `Z_*` solving `G(Z_*)=S` is unique;
- increasing `kappa` increases `Z_*`, so `kappa=0` is weakest;
- `dZ_*/d delta<2.55`;
- because `F'(Z_*)<=1-sqrt(3)/2`, the contradiction margin
  `F(Z_*)-delta` decreases with `delta`.

The weakest feasible point is therefore

\[
\boxed{
\kappa=0,
\qquad
U=C_{53},
\qquad
\delta={R_{53}(t)\over2},
}
\tag{PSER.13}
\]

where

\[
R_{53}(t)={9t\over2}-2\pi-C_{53}.
\tag{PSER.14}
\]

## 3. Boundary equation

Put

\[
M_{53}=m_2(C_{53}),
\qquad
r_{53}=C_{53}-M_{53},
\]

\[
\delta_0(t)={R_{53}(t)\over2},
\qquad
S_0(t)=\pi-C_{53}-{t\over2}+M_{53}.
\tag{PSER.15}
\]

Let `Z_0(t)` be the unique solution of

\[
\boxed{
Z_0+
{\delta_0(t)-F(Z_0)+r_{53}^2
 \over2(1-\delta_0(t))}
=S_0(t).
}
\tag{PSER.16}
\]

Every survivor requires

\[
\boxed{H_0(t):=F(Z_0(t))-\delta_0(t)\le0.}
\tag{PSER.17}
\]

The same derivative argument makes `H_0` strictly decreasing on the stated interval.

## 4. Decimal certificate

The companion verifier

`research/verify_target_c_phase_star_0053_energy_restored_incidence.py`

checks

\[
H_0(1.84289)>1.1402\times10^{-5}>0,
\]

\[
H_0(1.84290)<-1.2273\times10^{-5}<0,
\]

and

\[
\boxed{1.84289481604<t_*<1.84289481607.}
\tag{PSER.18}
\]

At `t=1.84289`,

\[
\delta_0=0.0499470395\ldots,
\qquad
Z_0=2.2148314351\ldots,
\]

and the minimal-threshold complement pair mass is only

\[
\boxed{p\approx8.82\times10^{-6}.}
\]

Hence every full-core Type-II survivor sequence in this proof-only stack satisfies

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.84289.
}
\]

## 5. Correct structural interpretation

The retained dominant occurrence mass near the weak corner is about `2.21483D`.
The two-bin quantity

\[
M_{53}=1.9046182\ldots
\]

is a **lower** bound for dominant-orbit train mass, so it cannot by itself upper-bound
the number of dominant trains. The correct upper chain is

\[
M\le A\le C\le U.
\]

At the weak corner `U=C53=1.9099256...`, which is still strictly below the retained
occurrence mass. Thus a linear family of dominant trains must have two selected outer
terminal occurrences, but the safe finite-window theorem must use `U`, not the lower
bound `M53`.

That argument is carried out in

`research/target_c_dominant_double_outer_trains_2026-09-15.md`,

which proves more than `0.3025D` such dominant outer-to-outer trains uniformly for
survivors with `t<=1.843`.

**Disposition:** proof-only downstream strengthening; C-II and Level I remain open.
