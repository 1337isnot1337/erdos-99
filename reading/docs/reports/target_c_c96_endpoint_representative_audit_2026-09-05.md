> Generated reading edition · [exact source](../../../docs/reports/target_c_c96_endpoint_representative_audit_2026-09-05.md) · source SHA-256 `1ce8761d3cbb0f2ab01eec45e94a39f21d6373b4f65641c5022014d51582391b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1238DDA8DA92","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C96 endpoint-representative audit

**Date:** 2026-09-05  
**Repository state:** `7911d4b5` (`main`)  
**Run type:** exact finite counting / equality-model audit  
**Target:** Target C C96 near-spanning common-cut caterpillar  
**External web search:** not used  
**Computation:** used only as a finite sanity check for small staircase shapes; no computation is needed in the proofs below

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting endpoint

C87 gives a paired physical diameter above every edge of the C88 prefix tree: for each simple interval `{a,b}`, one selected diameter uses an `L`-arc endpoint at one level and a `U`-arc endpoint at the other, and the opposite physical orientation supplies the reversed arc assignment. C96 then proves `q>=2D+2` from the common train cut.

The endpoint floor does not record how many distinct physical representatives are used at each prefix level. Near equality, that bookkeeping is rigid.

## 2. Exact representative-surplus theorem

For each prefix level `k in {0,...,D}`, let

- `l_k` be the number of distinct selected paired-diameter endpoints on hull arc `L` having chain level `k`;
- `u_k` be the analogous number on hull arc `U`.

The C87 simple prefix graph is connected on all `D+1` levels. Hence every level is incident with at least one simple edge. The two physical orientations over that edge supply at least one selected endpoint on each hull arc at that level. Therefore

`l_k>=1`, `u_k>=1` for every `k`.

Define the representative surplus

`R_rep=sum_(k=0)^D [(l_k-1)+(u_k-1)]`.

Then

### Theorem 1 — near-minimum q forces one representative per arc-level

For every C87-C96 chain-face survivor,

`R_rep <= q-2D`.

More precisely, if `o` is the number (0, 1, or 2) of chain endpoints `z,a` that are counted simultaneously as an `L`-representative and a `U`-representative, then the selected paired diameters alone use

`2D+2+R_rep-o`

distinct physical endpoints, and therefore

`q >= 2D+2+R_rep-o`.

Consequently

`R_rep <= q-(2D+2)+o <= q-2D`.

In particular:

- if `q=2D+2`, then `R_rep<=2`;
- if `q=2D+2+o(D)`, then `R_rep=o(D)`;
- hence in the near-spanning C96 regime, all but `o(D)` arc-level slots use exactly one physical selected diameter endpoint.

#### Proof

C87 connectivity gives `l_k,u_k>=1`, so the total number of arc-labelled representatives counted with multiplicity is

`sum_k(l_k+u_k)=2(D+1)+R_rep`.

The two hull arcs are disjoint except at the chain endpoints `z` and `a`. Thus the only possible double counting of one physical source point in this sum occurs when `z` or `a` is used in selected paired diameters in both arc roles. Subtracting the number `o<=2` of such overlaps gives exactly

`2D+2+R_rep-o`

distinct physical endpoints of the selected paired diameters. They are source diameter endpoints, so their number is at most the full endpoint count `q`. Rearrangement proves the result. `square`

### Endpoint-incidence refinement for the selected common-cut forest

Let `c_z,c_a in {0,1,2}` denote the number of arc-role representative sets (`L_0,U_0` for `z`; `L_D,U_D` for `a`) in which the actual chain endpoint occurs. Let `c_ext=c_z+c_a`.

Adjoin the chain diameter `za` to the `2D` selected paired diameter edges. The selected graph across the common chain cut has exactly `2D+1` edges and is a forest by C90. Its incident-vertex count is

`V_sel=2D+4+R_rep-c_ext`.

Indeed `2D+2+R_rep` counts all arc-role representatives; for each chain endpoint one must add it if it appears in zero roles, do nothing if it appears in one role, and remove one duplicate if it appears in both roles. The correction is `1-c_x` at each of `z,a`.

If `c_sel` is the number of nontrivial connected components of this selected forest, then the forest identity `V_sel=(2D+1)+c_sel` gives the exact relation

`c_sel = 3+R_rep-c_ext`.

Thus representative splitting, endpoint reuse, and common-cut component slack are not independent bookkeeping defects.

At the exact C96 floor `q=2D+2`, the complete common-cut graph has one component and no extra crossing edge. Hence the selected graph is also that one spanning tree, so

`c_sel=1`,

`c_ext=R_rep+2`,

and necessarily

`R_rep in {0,1,2}`.

This leaves only three endpoint-representative defect counts at the exact floor.

## 3. Staircase trees are already caterpillars

A second audit is important before trying to contradict C96 with C90 alone.

### Theorem 2 — every C88 staircase tree is a caterpillar

Write the C88 tree as

`E(G_P)={(i-1,b): t_i<=b<=t_(i-1), 1<=i<=s}`

with `D=t_0>=...>=t_s=s`.

Then deleting the graph leaves from `G_P` leaves a path (possibly empty or a single vertex). Hence every C88 staircase tree is a caterpillar.

#### Proof

The low vertices are the row centers `0,...,s-1`; the high vertices are `s,...,D`.

A row center `i-1` has degree

`t_(i-1)-t_i+1`.

It is non-leaf exactly when the staircase drops strictly across that row, `t_(i-1)>t_i`.

For a high vertex `b`, its incident rows are exactly those whose integer intervals `[t_i,t_(i-1)]` contain `b`. Away from an internal junction value `t_i`, exactly one row contains `b`, so `b` is a leaf. If several consecutive junction values equal the same `b`, that high vertex is adjacent to the corresponding consecutive block of row centers. Every row center strictly inside such a plateau has a singleton row and is itself a leaf. Therefore after leaf deletion the high junction vertex is adjacent to at most two surviving row centers: the centers immediately before and after the plateau, when the staircase drops on those sides.

Ordering the strict drops from top to bottom therefore alternates surviving row centers and distinct junction values in one chain. No surviving vertex has three surviving neighbors, and the surviving subgraph is connected because the original graph is a tree. It is a path. `square`

## 4. The ideal two-copy equality model is graph-theoretically compatible with C90

If every arc-level has one distinct physical representative and no endpoint identifications are made, the `2D` selected paired diameter edges form the canonical bipartite double cover of the prefix tree `G_P`:

- one lift of an edge `{a,b}` joins `L_a` to `U_b`;
- the other joins `U_a` to `L_b`.

Because `G_P` is bipartite, this double cover splits into two disjoint copies of `G_P`.

Theorem 2 shows that both copies are caterpillars. Moreover the staircase edge `(0,D)` is always present, and the vertices `0,D` lie at the same end of the leaf-pruned spine in the sense needed to concatenate the two lifted caterpillars with one bridge representing the chain diameter. The resulting abstract `2D+1`-edge tree is again a caterpillar.

This gives a durable no-go conclusion:

> The C88 paired staircase and the C90 caterpillar theorem are combinatorially compatible at the C96 edge/endpoint floor. A contradiction cannot come from the abstract graph classes alone; Euclidean endpoint geometry, train coordinates, or contact/shell information is essential.

This statement does **not** assert that the ideal abstract lift has a valid planar unit-separated diameter-`D` realization. That geometric realizability is exactly what remains to be attacked.

## 5. Exact target implication

The near-spanning C96 phase can now be stated more sharply.

If

`q=2D+2+epsilon_D D`, `epsilon_D->0`,

then only `o(D)` arc-level slots split into multiple physical representatives. On all remaining levels, the two C87 physical orientations use a unique `L` endpoint and a unique `U` endpoint. Thus away from `o(D)` exceptional levels, the selected common-cut diameter graph is the literal two-sheeted lift of the C88 staircase tree.

The next theorem should therefore be a **geometric stability theorem for the two-sheeted lift**, not another forest/caterpillar classification.

A sufficient result is:

> There exists an absolute `eta>0` such that any unit-separated diameter-`D` realization of the paired C88 lift satisfying the C18 diameter-star angle restriction requires at least `(2+eta)D` distinct diameter endpoints.

To beat the current low-train endpoint ceiling from C94/C82, one ultimately needs `eta>0.1862006...`, or a smaller endpoint gain combined with an independent train/shell loss.

## 6. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| `l_k,u_k>=1` at every level | proved | C87 paired orientations plus connected prefix tree |
| `R_rep<=q-2D` | proved | only `z,a` can be shared by the two hull arcs |
| exact relation `c_sel=3+R_rep-c_ext` | proved | endpoint count plus forest identity |
| exact floor has `R_rep<=2` | proved | `q=2D+2` and one-component/no-extra-edge C96 equality |
| every C88 staircase tree is a caterpillar | proved | explicit leaf-pruned junction structure |
| abstract two-copy lift is compatible with C90 | proved as graph statement | double cover of a bipartite tree gives two copies; staircase copies are caterpillars |
| abstract equality lift has a valid Euclidean realization | not claimed | this is the live geometric question |

## 7. Regression / no-go tests

The two extremal staircase shapes both pass the caterpillar audit:

- `s=1`: one row, a star centered at level `0`;
- `s=D`: one column, a star centered at level `D`.

Intermediate staircases interpolate by a caterpillar spine through the strict junction values. Thus a proof that says merely “the common-cut graph is a caterpillar but the staircase branches” is false.

## 10. Canonical promotion recommendation

**Hold as report** until the Euclidean two-sheeted-lift theorem is obtained. The representative-surplus theorem is exact and useful, but the present run also establishes that the graph-only equality attack does not close C96.

## 11. Next run

Use the clean-level structure together with C18. At a clean level `k`, all selected lifted diameter edges incident with the corresponding arc representative share one physical endpoint. Hence all partner endpoints attached through neighboring prefix-tree levels lie in the explicit C18 angular cone and have pairwise separation at most

`rho_D D`,

where `rho_D=2 sin(Theta(D)/2)` and `rho_D->0.85716...`.

The next quantitative question is whether the C88 staircase forces enough clean high-degree or long-span neighbor sets that these repeated C18 contractions cannot coexist with the chain-level/hull order and unit separation.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New exact endpoint bookkeeping:
For level k let l_k,u_k be the numbers of selected L/U diameter endpoints at that chain level and R_rep=sum[(l_k-1)+(u_k-1)]. Then R_rep<=q-2D. Hence q=2D+2+o(D) forces R_rep=o(D): almost every level has exactly one physical endpoint on each hull arc.

For the selected 2D paired edges plus za:
c_sel=3+R_rep-c_ext,
where c_ext counts how many L/U extreme roles are occupied by z,a. At q=2D+2, R_rep<=2.

Graph no-go:
Every C88 staircase tree is itself a caterpillar. Its ideal paired two-sheeted lift consists of two staircase copies and is graph-theoretically compatible with C90/C96. Pure graph classification cannot close the endpoint phase.

Next theorem:
Exploit Euclidean geometry on the almost-everywhere unique two-sheeted lift, especially the C18 shared-endpoint angle contraction, to force a positive linear representative surplus or a shell/train contradiction.
```
