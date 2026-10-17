<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "564d29a9df1a669596cda220742dc02780b09919", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_complement_rhombus_incidence_energy_refinement_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "8bf070d8176d564569d04d3da00bf6b7fc09fb40cf9a6cfc459b696732350f21"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — restore dominant energy inside complement rhombus incidence

**Date:** 2026-09-15  
**Status:** proof-only strengthening of the complement O–O rhombus-incidence theorem  
**Scope:** fully force-visible no-container/full-core Type-II branch  
**LEVEL I STATUS:** `STILL OPEN`

The conservative rhombus-incidence theorem proved

\[
\liminf {q-k\over D}\ge1.84209
\]

by discarding the positive dominant-occurrence energy from the complement-incidence
budget.  That discard is unnecessary.

Let `zD` be retained dominant outer-occurrence mass and `pD` retained complement O–O
pair mass.  The dominant selected occurrences already consume at least

\[
F(z)D-o(D),
\qquad F(z)=z-6\sin(z/6),
\]

of the total outer directional energy `delta D`.  Hence the exact terminal energy
available to complement pairs is at most

\[
(\delta-F(z))D+o(D),
\]

not `delta D`.  Feeding this into the train-length/rhombus-incidence inequality makes
the complement pair ceiling depend monotonically on `z`.  Eliminating `p` gives one
implicit scalar inequality and raises the safe floor to

\[
\boxed{
\liminf {q-k\over D}\ge1.84283.
}
\]

The scalar root is

\[
1.84283805523\ldots .
\]

Only the rounded value `1.84283` is claimed.

---

## 1. Retained-mass and residual-rhombus notation

Retain the notation of the audited coarse theorem:

\[
t={q-k\over D},\qquad
\kappa={k\over D},\qquad
\delta={d_{out}\over D},
\]

\[
U={9t\over2}-2\pi-2\delta-\kappa/2,
\qquad
\Delta_2={\pi\over2\sqrt3},
\]

\[
C_0=2\sqrt{\Delta_2}+0.0050,
\]

\[
m_2(U)={U+\sqrt{8\Delta_2-U^2}\over2},
\qquad
r_2(U)=U-m_2(U).
\]

The network constraint is

\[
C_0\le U,
\tag{ER.1}
\]

and the hostile-audited two-bin/shared-retention theorem gives

\[
\boxed{
z+p\ge
S(t,\delta,\kappa):=
\pi-U-{t+\kappa\over2}+m_2(U)-o(1).}
\tag{ER.2}

The dominant retained edges contribute

\[
\boxed{E_{dom}\ge F(z)D-o(D).}
\tag{ER.3}

The audited rhombus-incidence theorem gives, for complement terminal energy density
`e_c`,

\[
\boxed{
p(1-\delta)-{e_c\over2}
\le {r_2(U)^2\over2}+o(1).}
\tag{ER.4}

---

## 2. The exact complement energy budget

Dominant selected outer-edge occurrences and retained complement terminal occurrences
belong to disjoint stopped-train classes.  Therefore their exact occurrence-counted
outer directional energies are disjoint subsets of `d_out`.

Equation (ER.3) consequently gives

\[
\boxed{
e_c\le\delta-F(z)+o(1).}
\tag{ER.5}

Insert (ER.5) into (ER.4):

\[
\boxed{
p\le
{\delta-F(z)+r_2(U)^2\over2(1-\delta)}+o(1).}
\tag{ER.6}

Any feasible survivor automatically has `F(z)<=delta+o(1)`, so the numerator is
nonnegative after the harmless `r_2(U)^2` term.  No complement terminal-energy lower
bound is needed for this refinement.

---

## 3. Eliminate the complement population

Combine (ER.2) and (ER.6).  Ignoring `o(1)` terms, every feasible `z` must satisfy

\[
\boxed{
G(z;t,\delta,\kappa):=
 z+{\delta-F(z)+r_2(U)^2\over2(1-\delta)}
\ge S(t,\delta,\kappa).}
\tag{ER.7}

On the full interval used below,

\[
0\le F'(z)\le F'(\pi)=1-\frac{\sqrt3}{2}<0.134,
\qquad \delta<0.05.
\]

Hence

\[
{\partial G\over\partial z}
=1-{F'(z)\over2(1-\delta)}
>0.929.
\tag{ER.8}

Thus `G` is strictly increasing in `z`.  Let `Z_*(t,delta,kappa)` be the unique
threshold solving

\[
G(Z_*;t,\delta,\kappa)=S(t,\delta,\kappa)
\tag{ER.9}

when that threshold lies in the relevant positive interval.  If the formal threshold
lies above the available retained mass, dominant energy alone is even larger; the same
necessary inequality below remains valid.

Every survivor must have

\[
z\ge Z_* -o(1),
\]

and therefore

\[
\boxed{
\delta\ge F(Z_*) .}
\tag{ER.10}

This is the refined one-variable necessary condition.

---

## 4. Feasible-region monotonicity

Write

\[
r(U)=r_2(U),
\qquad r'(U)=1-m_2'(U)>0.
\]

The conservative theorem and its certificate already give, throughout
`1.84209<=t<=1.84284`,

\[
C_0\le U<2.007,
\qquad 0\le\delta<0.05,
\qquad 0<r<0.11,
\qquad -0.06<m_2'(U)<0.
\tag{ER.11}

### `kappa` direction

At fixed `t,delta`, `U_kappa=-1/2`.  The total derivative of the right side `S` is

\[
{dS\over d\kappa}=-{m_2'(U)\over2}>0.
\]

At fixed `z,delta`,

\[
G_U={r r'\over1-\delta}>0.
\]

Differentiating (ER.9),

\[
G_z {dZ_*\over d\kappa}
={dS\over d\kappa}+{G_U\over2}>0.
\]

Therefore `Z_*`, hence `F(Z_*)-delta`, increases with `kappa`.  The weakest point has

\[
\boxed{\kappa=0.}
\tag{ER.12}

### `delta` direction

At fixed `t,kappa`, `U_delta=-2` and

\[
{dS\over d\delta}=2r'<2.12.
\]

The partial derivative of `G` at fixed `z,U` is positive, so dropping it only enlarges
the upper bound for `dZ_*/ddelta`.  Also

\[
G_U={r r'\over1-\delta}
< {0.11\cdot1.06\over0.95}<0.123.
\]

Hence

\[
{dZ_*\over d\delta}
< {2.12+2(0.123)\over0.929}<2.55.
\tag{ER.13}

Therefore

\[
{d\over d\delta}[F(Z_*)-\delta]
<2.55\left(1-\frac{\sqrt3}{2}\right)-1
<-0.65.
\tag{ER.14}

So maximal detour is again the weakest point.  Combining with (ER.12) and the network
boundary,

\[
\boxed{
\kappa=0,
\qquad
\delta={R_{50}(t)\over2},
\qquad
U=C_0.}
\tag{ER.15}

---

## 5. Endpoint equation

Put

\[
M_0=m_2(C_0),
\qquad
r_0=C_0-M_0,
\]

\[
\delta_0(t)=
{1\over2}\left({9t\over2}-2\pi-C_0\right),
\]

\[
S_0(t)=\pi-C_0-{t\over2}+M_0.
\]

Let `Z_0(t)` be the unique solution of

\[
\boxed{
Z_0+{\delta_0-F(Z_0)+r_0^2\over2(1-\delta_0)}
=S_0(t).}
\tag{ER.16}

Every survivor requires

\[
\boxed{H_0(t):=F(Z_0(t))-\delta_0(t)\le0.}
\tag{ER.17}

The derivative argument above makes `H_0` strictly decreasing on the stated interval.

The companion Decimal certificate gives

\[
H_0(1.84283)>1.90\times10^{-5},
\]

\[
H_0(1.84284)<-4.60\times10^{-6},
\]

and brackets the unique scalar zero by

\[
1.84283805523<t_*<1.84283805525.
\tag{ER.18}

At `t=1.84283`, the incidence constraint permits only about

\[
3.16\times10^{-6}D
\]

complement retained O–O pair mass at the minimal dominant threshold.  Near the scalar
root the corresponding value remains only about `1.32e-5 D`.  Thus the old
energy-only optimizer with roughly `0.58D` complement pairs is completely eliminated.

### Theorem ER.1 — energy-restored rhombus-incidence floor

Every full-core Type-II survivor sequence in the stated proof-only scope satisfies

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}
\ge1.84283.}
\tag{ER.19}

C-II remains open.

---

## 6. What remains after this refinement

The complement O–O escape has effectively collapsed at the new endpoint.  The
surviving low-`t` normal form is therefore dominated by outer occurrences belonging to
the single exact three-phase atomic orbit, while the residual exact-orbit train mass is
only

\[
r_0=0.0050065802\ldots
\]

per unit diameter.

Further progress should attack this almost-pure three-phase outer boundary directly.
The most promising next constraints are:

1. phase-by-phase cyclic ordering of the retained dominant outer occurrences around the
   round loaded hull; and
2. compatibility of their inward penetration contacts with the near-saturated
   dominant rhombus crossing graph.

The complement scalar branch no longer has enough mass to be the main obstruction.
