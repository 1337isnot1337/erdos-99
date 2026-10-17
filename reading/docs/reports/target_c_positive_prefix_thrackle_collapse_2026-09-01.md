> Generated reading edition · [exact source](../../../docs/reports/target_c_positive_prefix_thrackle_collapse_2026-09-01.md) · source SHA-256 `b6f34b9294914e5e5a9a42f806f8f1d1f69bf83ea0c94429aa8ccf26c9ae62ff`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F896532565E4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C87: positive prefix-thrackle collapse

**Date:** 2026-09-01  
**Repository base:** `ec85492f` (main after C86 / PR #91)  
**Status:** LEVEL I STILL OPEN

C86 forces the C84 prefix graph of the exact C80 chain face to be connected. C87 uses
the sign of C84's KKT circulation and the planar diameter-thrackle order to classify
that graph exactly.

Let `h0=za` be the straight diameter chain, let `u=(a-z)/D`, and let
`P={tau_1,...,tau_D}` be its ordered parallel chain trains. Split the convex-hull
boundary at `z,a` into arcs `L,U`, both ordered from `z` to `a`, and orient `Ju`
toward `U`.

## C87.1 — arc orientation

C83 gives each non-chain diameter with nonempty restriction to `P` an interval
`I_h=(a_h,b_h]`, `a_h<b_h`, and scalars

`g_h|P = eta_h 1_(a_h,b_h]`,

`c_h=sigma_h r_h dot u`.

The C83 chain level is nondecreasing along each hull arc because the `D` chain trains
are nested separators whose terminals occur in chain order. The Euclidean support
coordinate `s(v)=p_v dot u` is also nondecreasing along each convex-hull arc.

The signed vector `sigma_h r_h` points from the lower-level endpoint to the
higher-level endpoint. Diameter-thrackle geometry puts the two endpoints on opposite
hull arcs unless the diameter shares `z` or `a`. Hence

- `eta_h>0` means the physical diameter is `L_(a_h) U_(b_h)`;
- `eta_h<0` means it is `U_(a_h) L_(b_h)`.

C83 already proves `eta_h!=0` for every such non-chain interval.

## C87.2 — positive prefix circulation

For any normalized KKT stress, C84 gives

`sum_h beta_h eta_h 1_(a_h,b_h] = 0`

on the chain coordinates. Orient each prefix edge from the level of its `L` endpoint
to the level of its `U` endpoint and give it positive flow

`f_h=beta_h |eta_h|`.

The C84 node-balance equation becomes an ordinary nonnegative circulation. For a
relative-interior C65 stress every active nonempty interval has strictly positive
flow.

## C87.3 — every directed cycle is a 2-cycle

Take a simple directed cycle of prefix levels

`k_0 -> k_1 -> ... -> k_(m-1) -> k_0`.

Its physical diameter edges are

`L_(k_i) U_(k_(i+1))`.

At every cycle vertex, consecutive level increments have opposite signs. If the two
adjacent source diameters are disjoint, this follows because they must cross, so their
orders on `L` and `U` are reversed. If they share a source endpoint, it is `z` or `a`,
so the corresponding level is automatically the strict minimum `0` or maximum `D`.
Thus `m=2r` and, after relabeling,

`a_i=k_(2i)` are local minima,

`b_i=k_(2i+1)` are local maxima.

The even physical edges `L_(a_i) U_(b_i)` are pairwise vertex-disjoint and hence
cross pairwise. Therefore the bijection `F(a_i)=b_i` is strictly order-reversing. The
odd physical edges `L_(b_i) U_(a_(i+1))` give another strictly order-reversing
bijection `G(b_i)=a_(i+1)`.

Then `G o F` is an order-preserving bijection of the finite ordered set `{a_i}` to
itself, so it is the identity. But it is also the cyclic shift `a_i -> a_(i+1)`.
Hence `r=1`.

Therefore every simple directed circulation cycle has length exactly two.

## C87.4 — every interval occurs in both orientations

A finite positive circulation decomposes into directed simple cycles. Since all cycles
have length two, every used unordered prefix interval `{a,b}` has equal total
transverse flow in the two physical orientations:

`sum_(L_a U_b) beta_h |eta_h|
 = sum_(L_b U_a) beta_h |eta_h|`.

In particular every simple edge of the relative-interior C84 prefix graph is
represented by at least two actual active diameter pairs, one with each sign of
`eta_h`.

## C87.5 — antitone intervals and one common cut

Take distinct simple prefix edges `(a,b)` and `(c,d)` with `a<b`, `c<d`, `a<c`.
C87.4 supplies positive-orientation physical diameters `L_a U_b` and `L_c U_d`.
If `b<d`, their endpoint orders on both hull arcs agree, so the segments do not cross;
they also cannot share a source endpoint. This contradicts the diameter-thrackle
property. Hence

`a<c  =>  b>=d`.

Thus the simple intervals are antitone. Any two overlap, so one-dimensional Helly
gives a common chain index `r` such that

`a_h < r <= b_h`

for every nonempty simple prefix interval. All non-chain diameter pairs seen by the
chain atom cross the same train separator `tau_r`.

## C87.6 — at most D simple intervals

Let the distinct left endpoints be `a_1<...<a_s`. For each `i` let `B_i` be the set
of right endpoints, with `m_i=min B_i`, `M_i=max B_i`. Antitonicity gives

`M_1 >= m_1 >= M_2 >= ... >= M_s >= m_s`.

Hence

`|E(G_P)| <= sum_i (M_i-m_i+1) <= M_1-m_s+s`.

Since `M_1<=D`, `a_s>=s-1`, and `m_s>=a_s+1>=s`,

`|E(G_P)|<=D`.

C86 makes `G_P` connected on all `D+1` prefix vertices, so it has at least `D`
edges. Therefore

`|E(G_P)|=D`

and `G_P` is a tree. Together with C87.5 it is an ordered staircase tree across the
single cut `r`.

## C87.7 — diameter-edge doubling

Every one of those `D` simple tree edges occurs in both arc orientations. Thus the
number `|H_P|` of active non-chain diameter pairs with nonempty chain interval obeys

`|H_P|>=2D`.

Including `h0` gives

`|H|>=2D+1`.

C65 identifies `H` with the complete source diameter graph. Hopf--Pannwitz gives
`|H|<=q` for `q` diameter endpoints, hence

`q>=2D+1`.

This is not yet a contradiction with the perimeter upper bound `q<=pi D`.

## C87.8 — radial positivity on each paired interval

Fix one interval `{a,b}`, `a<b`. For any positive-orientation diameter `h+ = L_aU_b`
and reverse-orientation diameter `h- = L_bU_a`, monotonicity of `s=p dot u` along both
hull arcs gives

`c_(h+) + c_(h-)
 = [s(U_b)-s(U_a)] + [s(L_b)-s(L_a)] >=0`.

For every non-chain interval, `|eta_h|=sqrt(D^2-c_h^2)>0`. The function

`phi(c)=c/sqrt(D^2-c^2)`

is odd and strictly increasing. Therefore

`phi(c_(h+))+phi(c_(h-))>=0`.

C87.4 gives equal total transverse flow in the two orientations. Couple the two flow
measures. Since `beta_h c_h = (beta_h |eta_h|) phi(c_h)`, summing the pairwise
inequality yields

`R_I := sum_(h:I_h=I) beta_h c_h >=0`

for every normalized KKT stress and every nonempty prefix interval `I`.

Thus opposite transverse KKT flows on one prefix interval never produce net backward
radial curvature.

## Frontier

The canonical exact chain-face survivor is now:

- a connected simple prefix tree with exactly `D` edges;
- all `D` intervals cross one common chain train `tau_r`;
- each tree edge has active diameter pairs in both arc orientations;
- at least `2D+1` active diameter pairs and diameter endpoints;
- KKT-weighted radial scalar nonnegative on every paired interval bundle.

The next target is to rule out this paired staircase tree using the common train cut,
unit separation on the two hull arcs, C82 exposed-hull train bounds, or a direct
classification of the actual diameter graph.