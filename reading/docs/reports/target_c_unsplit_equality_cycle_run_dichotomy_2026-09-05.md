> Generated reading edition · [exact source](../../../docs/reports/target_c_unsplit_equality_cycle_run_dichotomy_2026-09-05.md) · source SHA-256 `dccdac2e7a7035d1d9ee7db6736476a12b51a3c9ca23986b915262ceba4e4c6d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-FC2EF9DA3A51","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: unsplit equality cycle/run dichotomy

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-adjacent-cut-transition-2026-09-05`  
**Status:** LEVEL I STILL OPEN

## 1. Setting

Assume the exact C96 endpoint floor

`q=2D+2`

and one of the two **unsplit** equality patterns A or B from the corrected endpoint classification:

- A: `S=0`, one literal chain endpoint is shared between the two side fibers;
- B: `S=0`, both literal chain endpoints occur, neither is shared, and the chain edge joins the two paired components.

With `S=0`, the selected paired graph is the canonical two-sheet lift of the C99 prefix tree `G_P`. Since every C99 edge joins a prefix level below the pivot `s` to one at or above `s`, the two-sheet lift is two copies of `G_P` before the permitted endpoint identification/chain-edge gluing.

Let the C99 monotone cell path have move word of length `D-1`. Let

`R`

be the number of maximal constant runs in that move word. Thus `R=1` when all moves have one type and, in general, `1<=R<=D-1` for `D>=2`.

## 2. The non-leaf spine of G_P has exactly R vertices

A maximal run of row moves keeps one column level fixed through at least two consecutive occupied cells. That fixed prefix vertex has degree at least two in `G_P`.

Likewise a maximal run of column moves keeps one row level fixed through at least two consecutive cells and gives one prefix vertex of degree at least two.

Different maximal runs give different prefix vertices. Consecutive runs meet at the turning cell, so their corresponding non-leaf vertices are adjacent. No other prefix vertex has degree at least two: a row or column represented in only one occupied cell is a leaf.

Therefore the vertices of degree at least two in `G_P` are exactly the `R` run centers, in their run order, and they induce a path.

### Lemma UR1

For `D>=2`, the C99 prefix tree has a non-leaf spine with exactly `R` vertices and `R-1` spine edges.

Every vertex in the initial cell-run lies at distance at most one from the first spine vertex, and every vertex in the final cell-run lies at distance at most one from the last spine vertex.

Consequently any path from an initial-terminal-star vertex to a final-terminal-star vertex has length at most

`R+1`.

## 3. Equality patterns A and B glue the copies at the initial end

The first C99 occupied cell is `(0,D)`. Hence prefix levels `0` and `D` belong to the initial terminal star of each copy.

The FSB bookkeeping says that a literal chain endpoint can occur in the paired graph only in its endpoint fiber: `z` at prefix level `0`, `a` at prefix level `D`.

Thus:

- in case A, the two copies are identified at one initial-terminal-star vertex (the unique shared literal endpoint), and the other literal chain endpoint is attached by the chain edge as a leaf;
- in case B, the copies remain disjoint until the chain edge joins one initial-terminal-star vertex in one copy to one initial-terminal-star vertex in the other.

So the opposite ends of the combined caterpillar are the two final terminal stars.

## 4. If an off-tree diameter exists, its cycle is short in terms of R

The preceding Woodall report proves that any possible off-tree diameter `e_*` must close a tree path containing every non-leaf vertex of the equality tree `T_*`. Therefore its endpoints must lie at the two opposite final ends just described.

In case A, the path through `T_*` from one final terminal star to the other passes through at most

`(R+1)+(R+1)=2R+2`

tree edges. Hence the odd diameter cycle created by `e_*` has length at most

`2R+3`.        (A)

In case B, the same path additionally traverses the literal chain bridge, so it has at most

`2R+3`

tree edges, and the resulting cycle has length at most

`2R+4`.        (B)

The parity constraint can improve these additive constants in individual subcases, but these safe bounds are sufficient.

## 5. Apply the C17 diameter-cycle girth theorem

C17 proves that every diameter-graph cycle in a global minimizer of diameter `D` has length strictly greater than

`L(D)=pi D/sqrt(12(2D+1))`.

Combining with (A)--(B):

### Theorem UR2 — run lower bound for an equality defect

If an off-tree diameter exists in unsplit equality case A, then

`2R+3 > L(D)`,

so

`R > (L(D)-3)/2`.

If an off-tree diameter exists in unsplit equality case B, then

`2R+4 > L(D)`,

so

`R > (L(D)-4)/2`.

As `D->infinity`, either condition implies

`R >= (pi/(2sqrt(24))+o(1))*sqrt(D)`

`= (0.3206...+o(1))*sqrt(D)`.

Equivalently, if the C99 staircase has `o(sqrt(D))` runs, then in either unsplit endpoint-equality pattern the **entire** source diameter graph is exactly the spanning tree `T_*`; the unique possible off-tree diameter cannot exist.

## 6. Interpretation

C99 gave an exact long-run / many-turn dichotomy but did not attach a quantitative threshold to it. UR2 does so at the minimum C96 endpoint count:

- **few-run phase:** the endpoint-equality diameter graph is forced to be a tree;
- **off-tree phase:** the binary staircase must alternate at least order `sqrt(D)` times.

This does not yet eliminate either phase. It does, however, remove the possibility that a single odd diameter cycle repairs an essentially one-run staircase. Any such cycle would violate the global Reuleaux/packing girth theorem C17.

The natural continuation is different in the two phases. In the few-run phase one can use the exact tree/component filtration without any hidden off-tree correction. In the many-turn phase, most run centers have small degree and the two-sheet physical lift contains a long sequence of unsplit alternating diameter quadrilaterals, where the C100 midpoint/width identities become available.
