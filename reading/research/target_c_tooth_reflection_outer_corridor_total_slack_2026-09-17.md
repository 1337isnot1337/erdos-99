> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_outer_corridor_total_slack_2026-09-17.md) · source SHA-256 `49b77cd807597d44163b5b02ebd7ffcd9707e201414a84b866d1614d1fb39774`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ab762f72867e8398830ea586dd7302736c46bea4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_outer_corridor_total_slack_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f52146b8835ee31a3edf1c6784bc6f33f54ca335888dce888b43c61e410715b2"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — FREE outer corridor has bounded total near-unit slack

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only strengthening of the non-anchored FREE reflection branch  
**Scope:** Type-II full-core FREE reflection modules after exact-diameter anchor removal  
**Dependencies:** linear inactive-chain theorem; FREE-blocker outer-face theorem; support-monotonicity theorem; near-halfdepth outer-corridor theorem  
**Certificate:** `research/verify_target_c_tooth_reflection_outer_corridor_total_slack_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The existing FREE-module absorption proof records, for every parent edge in the inactive ancestry chain, the amount of time for which the parent has moved before meeting the child. Previously those times were bounded separately by the clearing time. Along one ancestry chain they in fact telescope.

This gives an exact global slack budget. If

```math
z_0,z_1,\ldots,z_\ell
```

is the support-monotone outer-face ancestry chain supplied by the near-halfdepth theorem, then

```math
\boxed{
\sum_{j=0}^{\ell-1}\bigl(|z_{j+1}-z_j|-1\bigr)
\le t_D
< h_*+D^{-1/3},
}
\tag{TS.1}
```

where

```math
h_*={\sqrt{303}\over52}=0.334747984337100\ldots .
```

Thus a chain with `(1/2-o(1))D` edges has only `O(1)` total excess over unit length. This strengthens the earlier edgewise bound `|z_{j+1}-z_j|<1+h_*+o(1)` by a factor of order `D` after summation.

Two consequences follow immediately.

First, the near-halfdepth chain itself has almost `D/2` edges:

```math
\boxed{
\ell\ge
{D\over2}-3^{1/8}D^{3/4}-\omega_D\sqrt D-O(\sqrt D),
}
\tag{TS.2}
```

for every `omega_D -> infinity` with `omega_D=o(D^(1/4))`. The previous lower bound had leading coefficient `1/[2(1+h_*)]=0.37460255...`; the telescoping slack ledger raises the leading coefficient to `1/2` and removes the denominator-expansion `O(D^(2/3))` loss.

Second, every fixed inverse-diameter threshold contains a linear matching. For fixed `K>2h_*`, the same chain contains a vertex-disjoint matching of original fully inactive pairs satisfying

```math
1<|x-y|\le1+{K\over D}
```

and having size

```math
\boxed{
\left(
{1\over4}-{h_*\over2K}-o(1)
\right)D.
}
\tag{TS.3}
```

In particular `K=1` gives

```math
\boxed{
\left(0.0826260078314499\ldots-o(1)\right)D
}
\tag{TS.4}
```

vertex-disjoint old inactive pairs with distance at most `1+1/D`.

The matching is not confined to the blocker-side boundary layer. If `0<=alpha<beta<1/2` are fixed and `Delta=beta-alpha`, then for every fixed

```math
K>{h_*\over\Delta}
```

the support-depth slab from `alpha D` to `beta D` contains a vertex-disjoint matching of size

```math
\boxed{
\left(
{\Delta-h_*/K\over2}-o(1)
\right)D
}
\tag{TS.5}
```

whose pairs again satisfy `1<|x-y|<=1+K/D` and whose endpoints are original fully inactive source points on the same outer-face corridor.

For example, the quarter-depth slab `Delta=1/4` with `K=2` contains

```math
\boxed{
\left(0.0413130039157249\ldots-o(1)\right)D
}
\tag{TS.6}
```

vertex-disjoint pairs of length at most `1+2/D`.

---

## 1. Activation times telescope along one ancestry chain

Use the absorption process from the linear inactive-chain theorem. Original blockers move from time zero in direction `-N`. When an old fully inactive source point is first met at unit distance, it is absorbed and thereafter also moves with velocity `-N`.

Let

```math
0=s_0<s_1<\cdots<s_\ell\le t_D
\tag{TS.7}
```

be the absorption times along one parent ancestry chain, with `z_0` a blocker root. Put

```math
\tau_j:=s_{j+1}-s_j>0.
\tag{TS.8}
```

At time `s_{j+1}`, the parent `z_j` has moved for exactly `tau_j`, so the first-contact equation is

```math
\left|z_j-\tau_jN-z_{j+1}\right|=1.
\tag{TS.9}
```

The strict ordering in (TS.7) is already part of the parent-forest construction: a parent is moving before its child is first absorbed.

Summing (TS.8),

```math
\boxed{
\sum_{j=0}^{\ell-1}\tau_j=s_\ell-s_0=s_\ell\le t_D.
}
\tag{TS.10}
```

This is the bookkeeping point not used in the earlier length estimate.

---

## 2. Exact total strict-length excess

Define the unit vector at the first-contact event

```math
c_j:=z_j-\tau_jN-z_{j+1},
\qquad |c_j|=1.
\tag{TS.11}
```

Then in the original source

```math
z_j-z_{j+1}=c_j+\tau_jN.
\tag{TS.12}
```

Every `z_j` is fully inactive in the original source. Hence consecutive vertices are not old unit contacts, while global unit separation still applies:

```math
|z_j-z_{j+1}|>1.
\tag{TS.13}
```

By the triangle inequality and (TS.12),

```math
|z_j-z_{j+1}|\le1+\tau_j.
\tag{TS.14}
```

Therefore, with

```math
\sigma_j:=|z_j-z_{j+1}|-1>0,
```

we have

```math
0<\sigma_j\le\tau_j.
\tag{TS.15}
```

Summing and using (TS.10),

```math
\sum_j\sigma_j
\le\sum_j\tau_j
\le t_D.
\tag{TS.16}
```

The reflection clearing time is

```math
t_D=\delta+D^{-1/3},
\qquad
0<\delta<h_*.
\tag{TS.17}
```

Equations (TS.16)--(TS.17) prove (TS.1).

No asymptotic averaging enters this step. The only asymptotic term in (TS.1) comes from the standard `D^(-1/3)` clearing margin.

---

## 3. The chain length is `D/2-o(D)`

The support-depth coordinate is

```math
a_v=H-N\cdot v.
```

Support monotonicity gives positive increments and the exact telescope

```math
a_{z_\ell}-a_{z_0}
=\sum_{j=0}^{\ell-1}N\cdot(z_j-z_{j+1}).
\tag{TS.18}
```

For every edge,

```math
N\cdot(z_j-z_{j+1})
\le |z_j-z_{j+1}|=1+\sigma_j.
```

Hence

```math
a_{z_\ell}-a_{z_0}
\le \ell+\sum_j\sigma_j
\le\ell+t_D,
\tag{TS.19}
```

so

```math
\boxed{
\ell\ge a_{z_\ell}-a_{z_0}-t_D.
}
\tag{TS.20}
```

The near-halfdepth theorem supplies

```math
a_{z_\ell}>
{D\over2}-3^{1/8}D^{3/4}-\omega_D\sqrt D
\tag{TS.21}
```

and

```math
a_{z_0}=O(\sqrt D).
\tag{TS.22}
```

Since `t_D=O(1)`, substitution into (TS.20) proves (TS.2).

For the concrete slow choice `omega_D=log D`,

```math
\ell\ge
{D\over2}-3^{1/8}D^{3/4}-\sqrt D\log D-O(\sqrt D).
\tag{TS.23}
```

---

## 4. A linear `1+K/D` matching

Fix `K>0`. Call a chain edge bad if

```math
\sigma_j>{K\over D}.
```

By (TS.1), the number `B_K` of bad edges satisfies

```math
B_K{K\over D}
<\sum_j\sigma_j
\le t_D,
```

hence

```math
\boxed{
B_K\le {t_DD\over K}
=\left({h_*\over K}+o(1)\right)D.
}
\tag{TS.24}
```

Combining (TS.2) and (TS.24), the number of good edges is at least

```math
\left(
{1\over2}-{h_*\over K}-o(1)
\right)D.
\tag{TS.25}
```

The edges of a path split into the even-index and odd-index parity classes, and each parity class is vertex-disjoint. One parity therefore contains at least half of the good edges. This gives a matching of size

```math
\left(
{1\over4}-{h_*\over2K}-o(1)
\right)D.
\tag{TS.26}
```

The coefficient is positive exactly when `K>2h_*`. Every retained pair is an original strict noncontact by (TS.13), so its distance is in `(1,1+K/D]`. This proves (TS.3).

For `K=1`,

```math
{1\over4}-{h_*\over2}
=0.0826260078314499\ldots,
```

which proves (TS.4).

---

## 5. The inverse-`D` matching persists in every macroscopic depth slab

Fix

```math
0\le\alpha<\beta<{1\over2},
\qquad
\Delta:=\beta-\alpha>0.
```

For all sufficiently large `D`, the near-halfdepth endpoint lies deeper than `beta D`. Because the support depth is strictly increasing along the chain, let `i_alpha` and `i_beta` be the first indices crossing `alpha D` and `beta D`, respectively. For `alpha=0`, take `i_alpha=0` if the root already has nonnegative depth.

Every one-edge support-depth increment is at most the corresponding edge length, and the old edgewise estimate gives

```math
|z_{j+1}-z_j|<1+t_D<\frac32
\tag{TS.27}
```

for all sufficiently large `D`. Therefore the first crossing of `alpha D` overshoots by only `O(1)`, while

```math
a_{z_{i_\beta}}>\beta D.
```

The support-depth span of the subchain from `i_alpha` to `i_beta` is consequently

```math
\ge \Delta D-O(1).
\tag{TS.28}
```

Apply (TS.19) only to this subchain. Its slack sum is at most the global sum `t_D`, so if `m_{alpha,beta}` is its edge count,

```math
\boxed{
m_{\alpha,\beta}\ge\Delta D-O(1).
}
\tag{TS.29}
```

The same bad-edge estimate (TS.24) applies inside the slab. Hence the slab contains at least

```math
\left(\Delta-{h_*\over K}-o(1)\right)D
```

good edges. Parity thinning produces the matching in (TS.5). The coefficient is positive when `K>h_*/Delta`.

For `Delta=1/4` and `K=2`,

```math
{1\over2}\left({1\over4}-{h_*\over2}\right)
=0.0413130039157249\ldots,
```

which gives (TS.6).

---

## 6. Relation to the existing deep-matching theorem

Canonical `C-INACTIVE-DEEP-MATCHING` also produces linear inverse-`D` near-unit matchings, but in a different branch and by a different mechanism. It starts from a macroscopic convex inactive chamber whose isolate population nearly saturates Oler capacity, then removes a fixed-width boundary strip.

The present theorem starts in the full-core Type-II reflection branch, where no macroscopic inactive chamber is assumed. Its input is one FREE reflection module and its absorption ancestry. The resulting pairs are constrained to one simple `N`-monotone outer-face corridor, and the proof has an exact `O(1)` total-slack ledger (TS.1). Thus this is a new bridge from the reflection normal form to the inverse-`D` near-unit geometry rather than a restatement of the chamber theorem.

---

## 7. Frontier effect

The non-anchored FREE alternative is now stronger than a long outer-face corridor:

```text
one simple N-monotone outer-face ancestry chain
support depth from O(sqrt D) to D/2-(3^(1/8)+o(1))D^(3/4)
edge count D/2-o(D)
all vertices old contact- and diameter-isolates
sum over all edge length excesses above one <= h_*+o(1)
for every fixed macroscopic depth slab:
    linearly many vertex-disjoint 1+O(1/D) old-inactive pairs
```

This rules out the possibility that the linear corridor is supported by a positive density of fixed-slack edges. Almost all of its edges are much closer to unit distance, and a linear inverse-`D` matching can be extracted at every fixed depth scale.

It does **not** yet close the FREE branch. The next missing statement is source-preserving: use the ordered outer-face placement and the bounded total-slack ledger to close a positive fraction of these near-unit gaps simultaneously, or show that such a layered inverse-`D` matching forces an actual force-hull/outer-walk obstruction. A purely metric matching count is insufficient because opening one near-gap can create another inactive contact.

**Disposition:** proved the telescoping activation-time ledger, upgraded the corridor length to `D/2-o(D)`, and extracted linear inverse-`D` matchings globally and in every fixed support-depth slab. C-II remains open.
