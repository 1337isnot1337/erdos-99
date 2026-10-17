> Generated reading edition · [exact source](../../research/target_c_high_t_force_carrying_robust_fork_t18687_2026-09-17.md) · source SHA-256 `eb55268f0e27b60009155d49f7576ab92230417e31b1bd668809636efcac6a73`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 4 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cab702327724aaeec676b6e6068932d8201b690f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_force_carrying_robust_fork_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a11aed17260ea2284ce201b95d97313a472c64fb487e657d033bffa3f9c6b566"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the robust high-`t` antipodal fork can use exact force-carrying central diamonds

**Date:** 2026-09-17
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed
**Scope:** one-sided high-`t` obstruction shore through `t=(q-k)/D<=1.8687`
**Dependencies:** parameterized robust angle-density tradeoff; exact-antipodal exact force-pair theorem; wide-dipole central-diamond theorem
**Certificate:** `research/verify_target_c_high_t_force_carrying_robust_fork_t18687.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The parameterized robust fork was proved using an arbitrary choice of opposite-transverse blocker pair at each exact-antipodal interface.  The exact-force-pair theorem now permits a more useful choice: at every such interface, choose the opposite-transverse pair which **positively generates the exact KKT strip reaction**.

The direction-packing proof of the robust fork uses only opposite transverse signs, the common one-sided half-plane, switching-support disjointness, and C67 direction separation.  It therefore applies without change to these exact force pairs.

Fix any constant

```math
0<\rho<{c_0\over6},
\qquad
c_0={113\over20{,}000{,}000}.
\tag{FR.1}
```

Then there are families `S_D(rho)` and `E_D^{force}(rho)` satisfying

```math
\boxed{
|E_D^{\rm force}(\rho)|+|S_D(\rho)|
>(c_0-6\rho)D-o(D).
}
\tag{FR.2}
```

Here:

- every `i in S_D(rho)` is a non-antipodal TB1 interface with one switching diameter vector `n_i` satisfying
  ```math
  n_i\cdot w\ge D\sin\rho
  
  ```
  for every unit local contact-opening direction `w`;
- every `i in E_D^{force}(rho)` has two actual switching diameter bars `h_i^-,h_i^+` whose projective angle is at least `rho`, whose positive cone strictly contains the exact axial reaction direction, and for which
  ```math
  \boxed{
  G_i
  =D\bigl(\lambda_i^-d_i^-+\lambda_i^+d_i^+\bigr),
  \qquad
  \lambda_i^-,\lambda_i^+>0.
  }
  \tag{FR.3}
  
  ```

For all sufficiently large `D`, every pair in `E_D^{force}(rho)` is vertex-disjoint and crossing.  Its four-endpoint hull contains the common disk

```math
\boxed{
B\!\left(o,{D\over2}\sin{\rho\over2}-L_D\right),
\qquad
L_D=O(D^{3/4}),
}
\tag{FR.4}
```

and its two diameter diagonals intersect within

```math
\boxed{
\left(1+{2\over\sin\rho}\right)L_D
}
\tag{FR.5}
```

of the common source circumcenter `o`.

Thus the robust exact-antipodal alternative is not merely a population of wide central diameter diamonds.  Each tagged diamond carries the exact cut-resultant increment at its birth interface as a positive combination of its two diameter diagonals.

---

## 1. Make the force-pair choice before the robust packing argument

At each exact-antipodal good interface `i`, the exact-force theorem supplies switching directions `d_i^-,d_i^+` such that

```math
(d_i^-\cdot Je_i)(d_i^+\cdot Je_i)<0,
\qquad
e_i={G_i\over|G_i|},
\tag{FR.6}
```

and the exact positive identity (FR.3) holds.

All consistently oriented switching directions on the selected shore lie in the same open semicircle determined by the global one-sided separation functional.  The exact reaction direction `e_i` lies in that semicircle as well.  Hence `e_i` lies strictly between `d_i^-` and `d_i^+` in the common angular lift.

Define

```math
\eta_i=d_{\mathbb{RP}^1}([d_i^-],[d_i^+]).
\tag{FR.7}
```

Call this exact force pair `rho`-wide when `eta_i>=rho`.

---

## 2. The narrow-force-pair capacity is the same `2 rho D+o(D)`

The robust angle-density theorem bounded the number of exact-antipodal interfaces whose chosen opposite-transverse pair has gap below `rho`.  Its proof did not use any special property of the old pair beyond:

1. both bars belong to the switching support of the same exact-antipodal interface;
2. their transverse signs are opposite;
3. every switching direction lies in the common open semicircle;
4. all row projective directions lie in one shrinking window;
5. distinct actual diameter directions have C67 separation at least `1/D`.

The exact force pair satisfies all five properties.  Therefore, if `N_D^{force}(rho)` is the number of interfaces with `eta_i<rho`, then

```math
\boxed{
N_D^{\rm force}(\rho)\le2\rho D+o(D).
}
\tag{FR.8}
```

For completeness, the same dichotomy is as follows.  A `rho`-narrow pair which brackets the oriented row/reaction axis in one open semicircle has both projective directions either within `rho` of the shrinking row window or within `rho` of the projective boundary line of the common semicircle.  These are at most two projective arcs of total length `omega_D+4rho`.  C67 applied to the `2N_D^{force}` distinct bars gives (FR.8).

---

## 3. Combine with the TB1 capacity loss

The unstrengthened good-interface fork is

```math
|E_D|+|U_D|>c_0D-o(D).
\tag{FR.9}
```

Exactly as in the parameterized robust theorem, at most

```math
4\rho D+o(D)
\tag{FR.10}
```

chosen TB1 bars can fail the `rho` interior-margin condition.  Removing those and the at most `2rho D+o(D)` narrow exact force pairs gives

```math
\begin{aligned}
|E_D^{\rm force}(\rho)|+|S_D(\rho)|
&>(c_0-4\rho-2\rho)D-o(D)\\
&=(c_0-6\rho)D-o(D),
\end{aligned}
```

which proves (FR.2).

Consequently

```math
\boxed{
\max\{|E_D^{\rm force}(\rho)|,|S_D(\rho)|\}
>{c_0-6\rho\over2}D-o(D).
}
\tag{FR.11}
```

The full density-angle tradeoff therefore survives after demanding exact force generation on the antipodal side.

---

## 4. Wide exact force pairs are central macroscopic diamonds

For fixed `rho>0`, the source-wide shared-endpoint angle cap is

```math
\Theta_D=(4\,3^{1/8}+o(1))D^{-1/4}=o(1).
\tag{FR.12}
```

Eventually `Theta_D<rho`, so a `rho`-wide exact force pair cannot share an endpoint.  Its two actual diameter bars are vertex-disjoint and therefore cross.

The wide-dipole central-diamond theorem depends only on the two bars being actual diameter chords of length `D`, their projective angle being at least `rho`, and the common source circumradius/midpoint estimate.  It therefore applies directly to the exact force pair and gives (FR.4)--(FR.5), together with

```math
\operatorname{area}Q_i
\ge {D^2\over2}\sin\rho
\tag{FR.13}
```

and pairwise cross-chord endpoint separation

```math
\ge D\sin(\rho/2)-2L_D.
\tag{FR.14}
```

The new information is simultaneous with this geometry: the same two diagonals satisfy the exact positive KKT identity (FR.3).

---

## 5. Growing endpoint-disjoint force-diamond extraction

If the force-diamond side wins (FR.11), then it contains more than

```math
{c_0-6\rho\over2}D-o(D)
\tag{FR.15}
```

tagged force diamonds.  The source-wide diameter-degree bound is

```math
\Delta(H)\le(4\,3^{1/8}+o(1))D^{3/4}.
\tag{FR.16}
```

Treat each force pair as a four-endpoint bundle.  The standard bundle-conflict greedy extraction yields at least

```math
\boxed{
\left(
{c_0-6\rho\over32\,3^{1/8}}-o(1)
\right)D^{1/4}
}
\tag{FR.17}
```

bundles with pairwise disjoint endpoint sets.  Every selected diameter bar crosses every other selected diameter bar.  Every tagged pair still:

- has internal crossing angle at least `rho`;
- contains the common central disk (FR.4);
- has central diagonal intersection (FR.5);
- positively generates its exact interface reaction (FR.3).

This is an unbounded **force-carrying central braid** rather than an unweighted diameter matching.

---

## 6. A useful calibrated instance

At

```math
\rho={c_0\over12},
\tag{FR.18}
```

one has

```math
c_0-6\rho={c_0\over2}.
```

Hence one of the following has more than

```math
{c_0\over4}D-o(D)
=1.4125\times10^{-6}D-o(D)
\tag{FR.19}
```

interfaces:

1. TB1 blockers with local opening margin `D sin(c_0/12)`;
2. exact force-carrying antipodal diamonds with crossing angle at least `c_0/12`, common macroscopic central disk, and exact KKT reaction identity.

This fixed instance is small-angle numerically, but the angle is absolute and independent of `D`.

---

## 7. Frontier effect

The exact-antipodal route previously had three partially disconnected descriptions: second-order blocker pairs, central wide diamonds, and exact KKT axial reactions.  They can now be imposed on the **same two actual diameter bars** at positive linear density.

The surviving robust fork is therefore

```text
fixed-interior-margin TB1 population
OR
fixed-angle exact-force antipodal population,

where every force pair
  - is a crossing diameter pair,
  - forms a common-center macroscopic diamond,
  - is tagged by its one-sided birth interface,
  - and positively generates that interface's exact cut-resultant increment.
```

A regular-shell regression still permits many central crossing diameters, so centrality alone is not a contradiction.  The remaining exact-antipodal target is to combine the **positive force cone and birth order** with the common ordered train rectangle.  Any closing argument can now charge both geometry and exact KKT force to the same tagged pair.

No C-II or Level-I closure is claimed.

**Disposition:** upgraded the parameterized robust exact-antipodal branch to fixed-angle, force-carrying central diamonds without changing its density tradeoff. C-II and Level I remain open.
