> Generated reading edition · [exact source](../../../docs/reports/target_c_adjacent_chain_cut_transition_2026-09-05.md) · source SHA-256 `84fae2e25c1d8797c9b5c7c3cfb3a92ff7757a32a860829e51181692f42ac777`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-3879851E38B8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: exact adjacent chain-cut transitions

**Date:** 2026-09-05  
**Base:** `6e9d4467` (`main`, exact C96 chain-cut load profile)  
**Branch:** `research/target-c-c97-adjacent-cut-transition-2026-09-05`  
**Status:** LEVEL I STILL OPEN

## 1. Setup

Use the C88 staircase normal form

`D=t_0>=t_1>=...>=t_s=s`

with simple prefix edges

`E(G_P)={(i-1,b): t_i<=b<=t_(i-1), 1<=i<=s}`.

Fix once and for all, for every simple staircase edge `e`, one actual active diameter in each of the two C87 hull-arc orientations. For chain train `tau_j`, let `E_j` be the simple staircase edges whose intervals contain `tau_j`, and let `S_j` be the selected physical crossing graph consisting of the chain diameter `za` together with both fixed physical orientations above every edge of `E_j`.

The previous load-profile report proves

`|E_j|=N_j`

and

`|E(S_j)|=2N_j+1`.

The point here is that the adjacent-cut change is not merely a change in cardinality. It is an exact nested row/column operation.

## 2. Before the pivot: one full paired row is added

Take `1<=j<s`.

An edge in staircase row `i` has the form

`(i-1,b]`, with `t_i<=b<=t_(i-1)`.

Because `j<s` and `t_i>=s` for every `i<=s`, every edge in a row `i<=j` contains both `tau_j` and `tau_(j+1)`. No edge can stop at `j` in this range.

The only new eligible row when the cut moves from `j` to `j+1` is row `j+1`, namely

`{(j,b): t_(j+1)<=b<=t_j}`.

Hence

`E_j subset E_(j+1)`

and

`E_(j+1) \ E_j = {(j,b): t_(j+1)<=b<=t_j}`.

Therefore

`|E_(j+1)\E_j|=t_j-t_(j+1)+1`.

At the physical diameter level, `S_(j+1)` is obtained from `S_j` by adjoining exactly the two fixed C87 orientations above every edge in that row. Thus exactly

`2(t_j-t_(j+1)+1)`

selected diameter edges are added.

## 3. After the pivot: one full paired endpoint-column is deleted

Take `s<=j<D`.

All staircase row indices already satisfy `i<=j`, so moving from `j` to `j+1` creates no new eligible row. An edge disappears exactly when its right endpoint is `b=j`.

Thus

`E_(j+1) subset E_j`

and

`E_j \ E_(j+1) = {(i-1,j): t_i<=j<=t_(i-1)}`.

The C88 row intervals `[t_i,t_(i-1)]` cover each integer `j in [s,D]` once, with one extra occurrence for every internal staircase junction `t_i=j`, `1<=i<=s-1`. Consequently

`|E_j\E_(j+1)| = 1 + #{i in {1,...,s-1}: t_i=j}`.

At the physical level, `S_(j+1)` is obtained from `S_j` by deleting both fixed C87 orientations above precisely those endpoint-column edges. Exactly

`2(1+#{i:t_i=j})`

selected diameter edges are deleted.

## 4. The pivot graph contains every selected paired edge

Every C88 staircase interval contains `tau_s`, so

`E_s=E(G_P)`

and

`S_s={za} union {the two fixed C87 orientations above every staircase edge}`.

Thus `S_s` has exactly `2D+1` edges. The whole family is nested into this pivot graph:

`S_1 subset ... subset S_s`

before the pivot and

`S_s supset S_(s+1) supset ... supset S_D`

after it.

More precisely, for every `j`,

`S_j` is obtained from `S_s` by deleting exactly

`2(D-N_j)`

selected physical diameter edges.

This is a stronger statement than strict unimodality of the load profile: it gives the exact edge identities that enter and leave at every adjacent train cut.

## 5. Exact endpoint-floor consequence

Assume the minimum C96 endpoint case

`q=2D+2`.

C96 says that the complete crossing graph at `tau_s` is a forest containing at least `2D+1` edges. A forest on at most `q=2D+2` source diameter endpoints with `2D+1` edges must be one spanning tree. Since `S_s` already has exactly `2D+1` edges, there is no room for any additional diameter edge crossing `tau_s`:

`H_(tau_s)=S_s=:T_*`,

and `T_*` is a spanning tree on all `q` diameter endpoints.

For any chain cut `tau_j`, the selected graph `S_j` is therefore a subgraph of this same spanning tree obtained by deleting exactly `2(D-N_j)` edges. If isolated diameter endpoints are retained as vertices, `S_j` has exactly

`1+2(D-N_j)`

connected components.

There is a second exact rigidity. Hopf--Pannwitz gives at most `q` edges in the complete source diameter graph. The spanning tree `T_*` already contributes `q-1` edges. Therefore the complete source diameter graph contains at most one edge outside `T_*`.

Consequently, for every `j`, the complete train-cut graph `H_(tau_j)` differs from `S_j` by at most one edge. Since C90 makes every `H_(tau_j)` a forest, adjoining that possible edge can merge at most two components. On the full `q`-vertex endpoint set,

`c(H_(tau_j)) >= 2(D-N_j)`

for every `j!= s`, while `H_(tau_s)=T_*` is connected.

In particular, in the exact endpoint case the pivot is the unique chain cut whose complete crossing diameter graph can be connected.

## 6. Why this matters

The equality problem is now a dynamic tree problem rather than a collection of unrelated train cuts.

- Before `tau_s`, the selected diameter forest grows by whole paired staircase rows.
- After `tau_s`, it shrinks by whole paired right-endpoint columns.
- At `q=2D+2`, the pivot object is one spanning diameter tree `T_*`.
- Every other selected cut is an explicitly prescribed edge-deletion of `T_*`.
- The entire diameter graph has only one possible edge outside `T_*`.

Any proposed equality geometry must therefore realize the two C87 physical orientations over all staircase edges inside one straight-line thrackle tree, while the adjacent train cuts expose the exact deletion filtration above.

## 7. Remaining gate

This theorem does not yet contradict the equality case. The principal escape is still physical endpoint splitting inside one prefix level: the two oriented realizations of adjacent staircase edges need not concatenate through the same source vertex even though they meet at the same prefix level.

The next target is to quantify that splitting. The exact tree filtration gives a clean currency: every split needed to prevent the two-sheet lift of the unique `0`-to-`D` prefix path from closing a diameter cycle must be supported by distinct physical diameter endpoints, while the equality case has no endpoint slack beyond the `2D+2` vertices of `T_*`.
