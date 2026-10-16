<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ee3666fc63eaa591ddeaec3ba66a52c809b6991f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_global_reaction_budget_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c2b1ef7c541320e2896e8323fb8c309f1e20e2007bdfbd6b5daecd7c8fac64fa"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — global one-sided KKT reaction budget for deep force cells

**Date:** 2026-09-17  
**Status:** proof-only quantitative strengthening; no canonical promotion claimed  
**Scope:** one-sided high-`t` path shore in the full-core/no-macroscopic-container Type-II branch through `t=(q-k)/D<=1.8687`  
**Dependencies:** C65-normalized full actual-diameter KKT stress; common-hub one-sided switching; exact strip-reaction identity; parameterized deep grid-force density theorem  
**Certificate:** `research/verify_target_c_high_t_global_reaction_budget_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The parameterized deep-cell theorem gives almost `c_0D` exact-force cells and an absolute per-cell reaction bound. There is a stronger global fact which does not use the local defect threshold at all.

On one side of the common diameter-routing hub, switching supports at distinct interfaces are pairwise edge-disjoint. Since the C65 KKT multipliers have total mass one, **all strip reactions on that side share one global `D`-sized `l^1` budget**. This immediately gives a density-versus-reaction quantile theorem for the parameterized deep cells and, on the growing-depth diagonal, restores a center switching-mass bound with a constant independent of the depth.

---

## 1. Exact global reaction budget

Let `I` be any set of nonhub interfaces on one fixed side of the common hub. For `i in I`, let

\[
X_i
\tag{RB.1}
\]

be the actual-diameter switching set at interface `i`, and put

\[
B_i:=\sum_{h\in X_i}\beta_h.
\tag{RB.2}
\]

Orient every one-sided switching diameter consistently inward and write

\[
n_h=Dd_h,
\qquad |d_h|=1.
\tag{RB.3}
\]

The exact strip reaction is

\[
G_i
=\sum_{h\in X_i}\beta_h n_h
=D\sum_{h\in X_i}\beta_h d_h.
\tag{RB.4}
\]

### Theorem RB.1 — one-sided reaction budget

For every such interface set `I`,

\[
\boxed{
\sum_{i\in I}B_i\le1,
\qquad
\sum_{i\in I}|G_i|\le D.
}
\tag{RB.5}
\]

Consequently, for every `K>0`,

\[
\boxed{
\#\{i\in I:B_i>K/D\}< {D\over K},
}
\tag{RB.6}
\]

and

\[
\boxed{
\#\{i\in I:|G_i|>K\}< {D\over K}.
}
\tag{RB.7}
\]

### Proof

On one side of the hub, every actual diameter support interval has at most one birth boundary. Therefore the switching sets `X_i` are pairwise disjoint. C65 normalization gives

\[
\sum_h\beta_h=1,
\qquad \beta_h>0.
\tag{RB.8}
\]

Hence

\[
\sum_{i\in I}B_i
=\sum_{i\in I}\sum_{h\in X_i}\beta_h
\le\sum_h\beta_h
=1.
\tag{RB.9}
\]

From (RB.4) and the triangle inequality,

\[
|G_i|
\le D\sum_{h\in X_i}\beta_h
=DB_i.
\tag{RB.10}
\]

Summing (RB.10) and using (RB.9) proves (RB.5). If `N` interfaces had `B_i>K/D`, then their total `B`-mass would exceed `NK/D`; (RB.9) gives `N<D/K`. Equation (RB.10) implies `|G_i|>K => B_i>K/D`, proving (RB.6)--(RB.7). `square`

This is exact. It does not use phase purity, a good-interface threshold, an asymptotic resultant plateau, or a lower bound on any individual KKT multiplier.

---

## 2. Quantile strengthening of the parameterized deep cells

Use the notation of the parameterized deep grid-force theorem. Fix

\[
0<\rho<{c_0\over6},
\qquad \eta,\delta>0,
\qquad
\lambda=c_0-6\rho-\eta-2\delta>0,
\tag{RB.11}
\]

where

\[
c_0={113\over20{,}000{,}000}.
\tag{RB.12}
\]

For every fixed depth `r`, that theorem gives a one-sided family

\[
Q_D=Q_D(r;\rho,\eta,\delta)
\tag{RB.13}
\]

with

\[
|Q_D|>\lambda D-o(D).
\tag{RB.14}
\]

Every center is a bilateral, two-sided, `rho`-wide exact-force cell locked to the same linear train grid.

Fix additionally a quantile parameter

\[
0<\sigma<1
\tag{RB.15}
\]

and put

\[
K_{\sigma,\lambda}:={1\over\sigma\lambda}.
\tag{RB.16}
\]

Delete from `Q_D` every center with

\[
B_i>{K_{\sigma,\lambda}\over D}.
\tag{RB.17}
\]

Theorem RB.1 deletes fewer than

\[
{D\over K_{\sigma,\lambda}}
=\sigma\lambda D
\tag{RB.18}
\]

centers. Thus the survivor `Q_D^{budget}` satisfies

\[
\boxed{
|Q_D^{budget}|
>(1-\sigma)\lambda D-o(D).
}
\tag{RB.19}
\]

Every surviving center retains all geometric conclusions of the parameterized theorem and also obeys the depth-independent bounds

\[
\boxed{
B_i\le {1\over\sigma\lambda D},
\qquad
0<|G_i|\le {1\over\sigma\lambda}.
}
\tag{RB.20}
\]

The crucial point is that the constant in (RB.20) does **not** contain the exact-phase depth `r` or the separator threshold `T_r`.

The same argument applies after the parameterized theorem's growing-depth diagonal extraction. Hence one may take

\[
r_D\to\infty
\tag{RB.21}
\]

while retaining (RB.19)--(RB.20) with the same fixed constants.

---

## 3. The compressed two-ray forces also have a global coefficient budget

At a selected force cell, write the exact positive two-ray compression as

\[
G_i
=D(\lambda_i^-d_i^-+\lambda_i^+d_i^+).
\tag{RB.22}
\]

Let the lifted angular deviations from the reaction direction be `p_i,q_i>0`, with `p_i+q_i<pi`. The exact force formulas are

\[
\lambda_i^-
={|G_i|\over D}{\sin q_i\over\sin(p_i+q_i)},
\qquad
\lambda_i^+
={|G_i|\over D}{\sin p_i\over\sin(p_i+q_i)}.
\tag{RB.23}
\]

The projective pair gap is at least `rho`, so

\[
\sin(p_i+q_i)\ge\sin\rho.
\tag{RB.24}
\]

Therefore

\[
\lambda_i^-+\lambda_i^+
\le {2|G_i|\over D\sin\rho}
\le {2B_i\over\sin\rho}.
\tag{RB.25}
\]

Summing over **all** parameterized centers, before the quantile deletion, gives the exact global estimate

\[
\boxed{
\sum_{i\in Q_D}(\lambda_i^-+\lambda_i^+)
\le {2\over\sin\rho}.
}
\tag{RB.26}
\]

For every center surviving (RB.19), each compressed force coefficient separately satisfies

\[
\boxed{
0<\lambda_i^\pm
\le {1\over\sigma\lambda D\sin\rho}.
}
\tag{RB.27}
\]

Thus a linear number of exact, fixed-angle, two-sided force diamonds can be retained while every compressed force coefficient is `O(D^{-1})` with a constant independent of exact-phase depth.

Equation (RB.26) is a coefficient budget for the compressed cut-reaction representation; it is **not** asserted to be a replacement global vertex-equilibrium KKT stress.

---

## 4. Explicit ninety-percent-density instance

Use the parameterized theorem's convenient choice

\[
\rho=\delta={c_0\over100},
\qquad
\eta={c_0\over50},
\qquad
\lambda={9c_0\over10}
={1017\over200{,}000{,}000}.
\tag{RB.28}
\]

Take `sigma=1/2`. Then

\[
K_{1/2,\lambda}
={2\over\lambda}
={400{,}000{,}000\over1017}
=393313.6676\ldots
\tag{RB.29}
\]

and the retained density is

\[
\boxed{
{\lambda\over2}
={1017\over400{,}000{,}000}
=2.5425\times10^{-6}.
}
\tag{RB.30}
\]

Hence more than

\[
(2.5425\times10^{-6})D-o(D)
\tag{RB.31}
\]

deep grid-locked bilateral force cells simultaneously satisfy

\[
B_i\le{393313.668\over D},
\qquad
0<|G_i|\le393313.668.
\tag{RB.32}
\]

This improves the earlier uniform absolute reaction ceiling `H=4,436,000` by a factor

\[
11.27853\ldots
\tag{RB.33}
\]

on a still-positive-density subfamily, and unlike the neighborhood threshold it stays unchanged on a growing-depth diagonal.

As the parameterized density tends to its current limit `c_0`, the half-quantile reaction constant tends to

\[
{2\over c_0}
={40{,}000{,}000\over113}
=353982.3009\ldots.
\tag{RB.34}
\]

---

## 5. Frontier effect

The deep exact-force obstruction is now globally stress-dilute in a stronger sense than the previous local threshold bounds showed:

```text
almost c0 D deep grid-locked exact-force cells
+ pairwise disjoint center switching supports
+ total center switching KKT mass <= 1
+ total absolute center reaction <= D
+ any fixed reaction quantile retains positive linear density
+ a positive linear subfamily has B_i = O(1/D) with a depth-independent constant
+ total compressed two-ray coefficient mass <= 2/sin(rho).
```

This does not remove any active diameter constraint: every selected exact-antipodal dipole remains two-sidedly jammed. It does, however, eliminate a possible explanation in which the growing-depth force-cell population is sustained by a growing per-center KKT scale. The remaining obstruction is geometric/order-theoretic: a linear population of independently jammed cells with vanishing-per-cell stress must still coexist with the same ordered near-triangular train grid and the convex diameter-thrackle endpoint order.

No C-II or Level-I closure is claimed.

**Disposition:** proved an exact global `l^1` budget for all one-sided strip reactions and used it to extract positive linear density of arbitrarily deep grid-locked force cells with depth-independent `O(D^{-1})` switching stress and bounded absolute reaction. C-II and Level I remain open.
