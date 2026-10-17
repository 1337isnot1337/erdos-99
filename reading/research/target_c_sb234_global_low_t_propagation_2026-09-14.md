> Generated reading edition · [exact source](../../research/target_c_sb234_global_low_t_propagation_2026-09-14.md) · source SHA-256 `6ddc1c185823f663dc35252649845c0034784d17a15dca1bf60670e57799325a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "771fa28f2a00b643fbea174d707fec62103d143f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_sb234_global_low_t_propagation_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "59b25be6db984053d6962d8764ce46baf345d62083a5459c345f135de8ea0f0a"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — `eta_grid=0.00234` global and low-`t` propagation

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Repository branch:** `research/c2-gluing-sol-20260914-r9`  
**Claim class:** proof-only propagation of the split-budget six-pair theorem  
**LEVEL I STATUS:** `STILL OPEN`

The current proof-only atomic theorem is

$$
\boxed{g=\eta_{grid}=0.00234.}
$$

This supersedes the SP1625 propagation on this branch.

Put

$$
\Delta_2={\pi\over2\sqrt3},
\quad s_2=\sqrt{\Delta_2},
\quad C_{146}={4\over9}(\pi+s_2),
$$

and `rho=0.7390851332151606...`, the positive root of `rho=cos(rho)`.

## 1. Correlated stopped-train split

The correlated identity gives

$$
\boxed{
\liminf{\rho_{rec}+\sigma_R-q\over D}\ge2g=0.00468.
}
\tag{P234.1}
$$

Hence every survivor lies in at least one of

$$
\boxed{
{S\over D}\ge{\rho\over2}+{g\over2}-o(1)
=0.370712566607580\ldots-o(1),
}
\tag{P234.2}
$$

or

$$
\boxed{
{\sigma_R\over D}\ge\rho+g-o(1)
=0.741425133215161\ldots-o(1).
}
\tag{P234.3}
$$

The rhombic missing-crossing lower bound becomes

$$
\boxed{
\liminf{M_R\over D^2}\ge0.387391276606001\ldots .
}
\tag{P234.4}
$$

The post-endpoint scalar floor is

$$
\boxed{
\liminf\mu_D\ge1.785847210824532\ldots .
}
\tag{P234.5}
$$

and the direct correlated interface floor is

$$
\boxed{
\liminf{J\over D}\ge2.150508840296357\ldots .
}
\tag{P234.6}
$$

## 2. Section-171 endpoint

Take

$$
\varepsilon_{234}=0.0017782,
\qquad
t_{234}=C_{146}+\varepsilon_{234}.
$$

Then

$$
\boxed{
t_{234}=1.8212917379794447\ldots .
}
\tag{P234.7}
$$

The feasible detour endpoint is exactly

$$
\boxed{
\delta_{234}
={{9\over2}\varepsilon_{234}-g\over2}
=0.00283095.
}
\tag{P234.8}
$$

`research/verify_target_c_sb234_global_propagation.py` certifies the Section-171 endpoint with outward negativity margin greater than `5.7e-5` and the same positive `delta`-derivative bound used in the prior propagations. Thus

$$
\boxed{
\liminf {q-k\over D}
\ge C_{146}+0.0017782
=1.8212917379794447\ldots .
}
\tag{P234.9}
$$

The numerical root of the unchanged endpoint equation is

$$
0.0017783923034325955\ldots,
$$

so decimal tuning is again irrelevant.

## 3. Chamber and residual ledgers

The mandatory chamber/interface floor is

$$
\boxed{
\liminf {J\over D}
\ge t_{234}+2(2s_2+g)-\pi
=2.493630311845481\ldots .
}
\tag{P234.10}
$$

The exact `H` relation gives

$$
\boxed{
\liminf {H\over D}
\ge1.497310567107289\ldots .
}
\tag{P234.11}
$$

Consequently

$$
\boxed{
\liminf {A_{ch}-a_0Z_{ch}\over D}
\ge0.648354494234898\ldots,
}
\tag{P234.12}
$$

$$
\boxed{
\liminf {\Delta_2D^2-R_4\over D}
\ge0.748655283553644\ldots,
}
\tag{P234.13}
$$

and the corrected residual cap is

$$
\boxed{
\limsup {R_F+\Sigma_{ext}\over D}
\le2.891097242405245\ldots .
}
\tag{P234.14}
$$

No scalar contradiction results.

## 4. Stronger low-`t` topology budget

The latest-main low-`t` network theorem uses

$$
C_0=2s_2+g,
\qquad
R(t)={9t\over2}-2\pi-C_0.
$$

At `t=t234`,

$$
\boxed{C_0=1.906965613727915\ldots,}
$$

and

$$
\boxed{R(t_{234})=4.5(0.0017782)-0.00234=0.0056619.}
\tag{P234.15}
$$

Therefore

$$
\boxed{
\delta\le0.00283095+o(1),
\qquad
\kappa={k\over D}\le0.0113238+o(1).
}
\tag{P234.16}
$$

The loaded diameter graph satisfies

$$
\boxed{
{h\over q}\ge0.993820962572169\ldots-o(1).
}
\tag{P234.17}
$$

If it is a caterpillar forest, its average component size satisfies

$$
\boxed{
{q\over d_H}\ge160.837504899\ldots-o(1).
}
\tag{P234.18}
$$

## 5. Pentagon sea

The bounded exceptional-face count satisfies

$$
\boxed{
{f\over D}\ge0.498159872369096\ldots-o(1).
}
\tag{P234.19}
$$

while

$$
\boxed{
{Q-f\over D}\le0.00283095+o(1).
}
\tag{P234.20}
$$

Hence

$$
\boxed{
{p_5\over D}\ge0.495328922369096\ldots-o(1).
}
\tag{P234.21}
$$

and the pentagon closure-rank theorem gives

$$
\boxed{
{\operatorname{rank}C_{P_5}\over D}
\ge0.979334044738192\ldots-o(1).
}
\tag{P234.22}
$$

Degree-at-least-six bounded faces carry at most

$$
\boxed{
{B_{\ge6}\over D}\le0.0169857+o(1)
}
\tag{P234.23}
$$

terminal occurrences, while distinct complete trains touching pentagons satisfy

$$
\boxed{
{N_5\over D}\ge1.238322305922740\ldots-o(1).
}
\tag{P234.24}
$$

Thus more than `99.43%` of bounded exceptional faces are forced to be pentagons at the endpoint profile.

## 6. Endpoint-network counts

For `B=Q+4f`,

$$
\boxed{
2.490799361845481\ldots
\le{B\over D}
\le2.504954111845481\ldots
}
\tag{P234.25}
$$

up to `o(1)`. Since `2T=b+B`,

$$
\boxed{
2.816196007717637\ldots
\le{T\over D}
\le2.823273382717637\ldots .
}
\tag{P234.26}
$$

The outer-to-outer train count obeys

$$
\boxed{
\liminf {L_{OO}\over D}
\ge3\pi-5t_{234}
=0.318319270872156\ldots .
}
\tag{P234.27}
$$

Each such cut remains two-sidedly diameter-braced, but diameter-edge reuse across nested cuts is still uncontrolled.

## 7. Outer-tooth / long-side burden

The latest-main dichotomy gives

$$
\boxed{
\liminf {N_2+2L_{>2}\over D}
\ge5\pi+2C_0-10t_{234}
=1.308977115610349\ldots .
}
\tag{P234.28}
$$

Therefore

$$
\boxed{
\liminf {1\over D}\max\{N_2,L_{>2}\}
\ge0.436325705203450\ldots .
}
\tag{P234.29}
$$

As before, the atomic improvement mainly tightens the topology and pentagon budgets; the tooth/long-side scalar floor is nearly stationary because the larger `g` and larger certified `t` compensate.

## 8. Current structural bottleneck

A low-`t` survivor must now simultaneously have:

- `k<=0.011324D+o(D)`;
- a loaded diameter graph within about `0.618%` of maximal Woodall density;
- `0.495329D-o(D)` actual pentagon defects;
- pentagon closure rank `0.979334D-o(D)`;
- at least `1.23832D-o(D)` pentagon-touching trains;
- at least `0.31832D-o(D)` outer-to-outer train cuts;
- and `1.30898D-o(D)` combined shallow-tooth/long-side burden.

The remaining gap is structural, not scalar. The two immediate missing theorems are still:

1. a multiplicity/cyclic-order bound limiting how often one diameter edge can brace distinct outer-to-outer train cuts in a near-extremal Woodall graph; or
2. a local incompatibility between the almost pure pentagon closure network and the linear outer-tooth/long-side burden.

**Disposition:** proof-only propagation. C-II and Level I remain open.
