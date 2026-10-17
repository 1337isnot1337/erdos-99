> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_endpoint_one_sided_defect_2026-09-05.md) · source SHA-256 `47ff946a0f897bd35d170407a69afd06eaa680edd0db9929167bf034425c1e59`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AEA9B3A6488E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: one-sided endpoint defect and the exact D^2 component invariant

**Date:** 2026-09-05  
**Base:** exact C96 endpoint equality, together with the adjacent chain-cut filtration  
**Branch:** `research/target-c-c97-adjacent-cut-transition-2026-09-05`  
**Status:** LEVEL I STILL OPEN

## 1. Exact endpoint setting

Assume

`q=2D+2`.

Let `tau_s` be the common chain train from C87--C96. The previous adjacent-cut report gives a selected graph `S_j` at every chain cut and proves that

`S_s=T_*`

is a spanning tree on all `q` diameter endpoints, with exactly

`|E(T_*)|=2D+1=q-1`

edges.

Hopf--Pannwitz gives at most `q` edges in the entire source diameter graph. Therefore there is at most one source diameter edge outside `T_*`. Denote it by `e_*` if it exists.

Because every edge of `T_*` is one of the fixed selected edges, the complete train-cut graph has the exact form

`H_j = S_j`

or

`H_j = S_j union {e_*}`,

according as `e_*` does not or does cross `tau_j`.

There are no other possible corrections.

## 2. The possible extra edge is forbidden from the pivot

C96 equality gives

`H_s=T_*`.

Hence `e_*`, if it exists, does **not** cross `tau_s`.

By the C83 chain-track interval normal form, the set of chain trains crossed by one diameter is a consecutive integer interval

`I(e_*)=(a_*,b_*]`.

Since `s notin I(e_*)`, this interval lies wholly on one side of the pivot:

- either `b_* < s` (strictly before the pivot), or
- `a_* >= s` (strictly after the pivot),

with the empty-chain-span case allowed.

Thus one complete side of the chain-cut filtration has **no** off-tree correction at all.

This is stronger than the statement that there is only one off-tree edge: the one possible defect cannot be used to repair component structure on both sides of the common cut.

## 3. Exact component formula at every chain cut

Retain all `q` diameter endpoints as vertices, including isolated vertices after edges are deleted.

The selected cut graph `S_j` is a subgraph of the tree `T_*`, hence a forest. Its edge count is

`|E(S_j)|=2N_j+1`.

Therefore

`c(S_j)=q-|E(S_j)|`

and, because `q=2D+2`, exactly

`c(S_j)=1+2(D-N_j)`.

Let

`chi_j = 1` if `e_*` exists and crosses `tau_j`, and `chi_j=0` otherwise.

C90 says the complete train-cut graph `H_j` is a forest. Consequently, whenever `chi_j=1`, the edge `e_*` joins two distinct components of `S_j`, reducing the component count by exactly one. Hence

`c(H_j)=1+2(D-N_j)-chi_j`.        (1)

In particular `chi_s=0`, and the nonzero `chi_j` form one consecutive block entirely before or entirely after `s`.

## 4. Sum over all chain cuts

C88 gives the exact staircase interval-length identity

`sum_j N_j = D(D+1)/2`.

Summing the baseline part of (1),

`sum_(j=1)^D [1+2(D-N_j)]`

`= D + 2D^2 - 2 sum_j N_j`

`= D + 2D^2 - D(D+1)`

`= D^2`.

Let

`ell_* = sum_j chi_j`,

the number of chain trains crossed by the unique possible off-tree diameter. Then

`sum_(j=1)^D c(H_j) = D^2 - ell_*`.        (2)

This is exact.

Because the off-tree interval avoids `s`,

`0 <= ell_* <= max(s-1,D-s) <= D-1`.

Therefore

`D^2-D+1 <= sum_j c(H_j) <= D^2`.

The upper endpoint occurs exactly when no off-tree diameter crosses any chain train.

## 5. Equivalent edge-incidence derivation

There is a useful cross-check of (2).

Across all chain cuts, the chain diameter `za` contributes `D` edge-cut incidences. The paired staircase edges contribute

`2 sum_j N_j = D(D+1)`

incidences. Thus the spanning tree contributes exactly

`D + D(D+1) = D(D+2)`

edge-cut incidences.

Across `D` cuts on a fixed `q=2D+2` vertex set, the forest identity `c=v-e` gives

`Dq - D(D+2) = D(2D+2)-D(D+2)=D^2`

components before the possible off-tree correction. The extra edge contributes exactly `ell_*` further edge-cut incidences, yielding `D^2-ell_*` again.

## 6. Consequence for any equality obstruction

At the exact C96 endpoint floor, the chain-cut family is no longer free cut-by-cut data. It is determined by

1. one spanning tree `T_*`;
2. the staircase deletion filtration inside `T_*`; and
3. at most one extra diameter whose entire chain activity is confined to one side of the pivot.

Hence any mechanism that requires even one independent component-merging correction on each side of `tau_s` rules out `q=2D+2` immediately.

The remaining task is to obtain such a two-sided demand from Euclidean diameter geometry or from physical prefix-fiber incidence. Pure graph shape is insufficient, as the double-cover caterpillar audit already shows.
