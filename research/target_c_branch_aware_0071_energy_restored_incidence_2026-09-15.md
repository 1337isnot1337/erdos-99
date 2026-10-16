<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "1d543ee9ae56aeb1118833bfb0654e7de22d5066", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_branch_aware_0071_energy_restored_incidence_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "3a946fcda3081d0192e05e483da77434b5add2181b0f430a4f73e9341e60eb1d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — branch-aware `g=0.0071` propagates through rhombus incidence

**Date:** 2026-09-15  
**Status:** proof-only downstream composition  
**Scope:** fully force-visible no-container/full-core Type-II branch  
**Depends on:** hostile-audited branch-aware atomic gap `g=0.0071`; hostile-audited two-bin dominant-orbit mass; hostile-audited energy-restored complement-rhombus incidence  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The energy-restored complement-rhombus-incidence theorem was proved and hostile-audited
with the matched train floor

\[
C_{50}=2\sqrt{\Delta_2}+0.0050,
\qquad
\Delta_2={\pi\over2\sqrt3},
\]

and yielded

\[
\liminf {q-k\over D}\ge1.84283.
\]

The branch-aware iterative-pruning theorem is now independently hostile-audited and
supplies the stronger matched input

\[
\boxed{
C_{71}=2\sqrt{\Delta_2}+0.0071.
}
\tag{P71.1}

No geometric step in the rhombus-incidence proof depends on the origin of the matched
train floor.  Substituting `C71` raises the safe Type-II floor to

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.84323.
}
\tag{P71.2}

The scalar zero is

\[
1.8432353529344645040\ldots .
\]

Only `1.84323` is claimed.

---

## 1. Retained audited system

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
\tag{P71.3}

The audited branch-aware train theorem gives

\[
\boxed{U\ge C_{71}.}
\tag{P71.4}

Retain the two-bin functions

\[
m_2(U)={U+\sqrt{8\Delta_2-U^2}\over2},
\qquad
r_2(U)=U-m_2(U).
\tag{P71.5}

The hostile-audited shared-retention and rhombus-incidence stack gives retained
dominant outer mass `z` and retained complement O--O pair mass `p` satisfying

\[
z+p\ge
S(t,\delta,\kappa)
:=\pi-U-{t+\kappa\over2}+m_2(U)-o(1),
\tag{P71.6}

\[
E_{dom}\ge F(z)D-o(D),
\qquad
F(z)=z-6\sin(z/6),
\tag{P71.7}

and

\[
p(1-\delta)-{e_c\over2}
\le {r_2(U)^2\over2}+o(1).
\tag{P71.8}

The dominant and complement selected outer-edge supports are disjoint, hence

\[
e_c\le\delta-F(z)+o(1).
\tag{P71.9}

Therefore every survivor must satisfy

\[
\boxed{
G(z):=
 z+{\delta-F(z)+r_2(U)^2\over2(1-\delta)}
\ge S(t,\delta,\kappa)-o(1).
}
\tag{P71.10}

This is exactly the hostile-audited parent inequality with `C50` replaced only in the
lower bound on `U`.

---

## 2. Feasible-region reduction is unchanged

On the interval

\[
1.84283\le t\le1.84324
\]

the stronger floor `U>=C71` remains inside the conservative bounds used by the parent
hostile audit:

\[
U<2.007,
\qquad
\delta<0.051,
\qquad
r_2(U)<0.11,
\qquad
-0.06<m_2'(U)<0.
\tag{P71.11}

Consequently the same implicit-derivative proof applies:

1. `G_z>0.929`, so the threshold `Z_*` solving `G(Z_*)=S` is unique;
2. increasing `kappa` increases `Z_*`, so `kappa=0` is the weakest topology point;
3. `dZ_*/d delta<2.55` on the stated box;
4. `F'(Z_*)<=1-sqrt(3)/2`, so `F(Z_*)-delta` strictly decreases with `delta`.

Thus the weakest feasible point is

\[
\boxed{
\kappa=0,
\qquad
U=C_{71},
\qquad
\delta={R_{71}(t)\over2},
}
\tag{P71.12}

where

\[
R_{71}(t)={9t\over2}-2\pi-C_{71}.
\tag{P71.13}

---

## 3. One-variable endpoint

Put

\[
M_{71}=m_2(C_{71}),
\qquad
r_{71}=C_{71}-M_{71},
\]

\[
\delta_0(t)={R_{71}(t)\over2},
\qquad
S_0(t)=\pi-C_{71}-{t\over2}+M_{71}.
\tag{P71.14}

Let `Z_0(t)` be the unique solution of

\[
\boxed{
Z_0+{\delta_0(t)-F(Z_0)+r_{71}^2
\over2(1-\delta_0(t))}
=S_0(t).
}
\tag{P71.15}

Every survivor requires

\[
\boxed{H_0(t):=F(Z_0(t))-\delta_0(t)\le0.}
\tag{P71.16}

The parent derivative argument makes `H_0` strictly decreasing throughout the stated
interval.

The companion Decimal verifier gives

\[
H_0(1.84323)
=1.2672491\times10^{-5}>0,
\]

\[
H_0(1.84324)
=-1.1001428\times10^{-5}<0,
\]

and brackets the unique root at

\[
\boxed{
1.84323535293446450<t_*<1.84323535293446451.
}
\tag{P71.17}

At the safe endpoint,

\[
C_{71}=1.9117256137279146\ldots,
\]

\[
M_{71}=1.9046123305467757\ldots,
\qquad
r_{71}=0.0071132831811389\ldots,
\]

\[
\delta_0=0.0498120395462494\ldots,
\]

\[
Z_0=2.2128444131435564\ldots,
\]

and the retained complement O--O mass at the minimal dominant threshold is only

\[
\boxed{p=1.9957265\times10^{-5}+o(1).}
\tag{P71.18}

Thus the main structural conclusion of the parent survives: the complement O--O escape
is negligible at the low-`t` endpoint.

### Theorem P71.1

Every full-core Type-II survivor sequence in the stated proof-only scope satisfies

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.84323.
}
\]

---

## 4. Updated frontier

The scalar endpoint is no longer controlled by a balance between dominant and
complement O--O trains.  The retained dominant outer mass is about `2.213D`, while
complement retained O--O mass is only `O(10^-5 D)` at the minimizing point.

The live obstruction is therefore the almost-pure dominant exact three-phase train
orbit.  Further progress should use its endpoint pairing and rhombus-crossing geometry,
not another independent complement-energy estimate.

C-II remains open.
