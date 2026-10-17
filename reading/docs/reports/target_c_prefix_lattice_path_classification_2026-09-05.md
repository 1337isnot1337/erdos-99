> Generated reading edition · [exact source](../../../docs/reports/target_c_prefix_lattice_path_classification_2026-09-05.md) · source SHA-256 `06c63e7a4f482b3393dd9c515e1856d1d02a77ec9446c148d79e5b6b15a5ad52`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DD8DCC807269","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C99: exact prefix lattice-path classification

**Date:** 2026-09-05  
**Repository base:** C98 branch after `3e839d25`  
**Status:** LEVEL I STILL OPEN  
**Depends on:** C87 positive prefix-thrackle collapse

C87 proves that the collapsed simple prefix graph `G_P` is a tree on the levels `0,...,D`, every edge crosses one common chain index `r`, and the interval edges are antitone. Those statements determine `G_P` completely: it is the incidence tree of a monotone lattice path through an `r x (D+1-r)` rectangle.

This exact normal form is stronger than the generic caterpillar description used for physical train cuts.

## 1. Bipartite grid coordinates

Fix the C87 common cut `r`, so every prefix edge is an interval

`(a,b]` with `a<r<=b`.

Set

`A={0,1,...,r-1}`

and

`B={r,r+1,...,D}`.

Thus every edge of `G_P` joins one vertex of `A` to one vertex of `B`.

Represent an edge `{a,b}` by the grid cell `(a,b)`. Order rows by increasing `a` and columns by decreasing `b`.

C87 antitonicity says that for two edges `(a,b)` and `(c,d)` with `a<c`, one has

`b>=d`.

In the chosen row/column orders, every pair of occupied cells is therefore weakly monotone: moving to a lower row can never move to a column on the wrong side.

## 2. Consecutive occupied cells must share a row or column

List the `D` occupied cells in their total monotone order.

Take two consecutive occupied cells `(a,b)` and `(c,d)`, with `a<=c` and `b>=d`.

Suppose both inequalities were strict: `a<c` and `b>d`. Then these two graph edges are vertex-disjoint.

Because there is no occupied cell between them in monotone order, no edge of `G_P` can have one endpoint in the prefix rectangle between row levels `a,...,c` and column levels `d,...,b` in a way that connects the two sides without lying between the chosen cells. More directly, split the bipartite vertex set into

`X={0,...,a} union {b,...,D}`

and its complement after choosing the immediate monotone gap. Antitonicity forbids an edge crossing the gap except through one of the four endpoint rows/columns, while the assumed strict inequalities make the two consecutive cells share none. This would disconnect `G_P`, contradicting C87.

An equivalent shorter graph argument is available: since `G_P` is connected, there is an edge sequence from `{a,b}` to `{c,d}` in which consecutive edges share a graph vertex. Every edge on such a sequence must lie between the two cells in the monotone cell order. Consecutiveness leaves no third occupied cell, so the two cells themselves must share a row or a column.

Hence every consecutive pair of occupied cells differs by changing exactly one endpoint level.

## 3. No row or column can be skipped

`G_P` is a spanning tree on all `D+1` prefix vertices. Therefore every row vertex `a in A` and every column vertex `b in B` is incident with at least one occupied cell.

Along the monotone occupied-cell sequence, row indices never decrease and column indices never increase in the original numeric order. If a row index were skipped, that prefix vertex would be isolated. The same holds for columns.

Thus when consecutive cells change row, the row increases by exactly one. When they change column, the numeric column decreases by exactly one.

The first occupied cell must therefore be

`(0,D)`,

and the last must be

`(r-1,r)`.

## 4. Exact path theorem

There are

`r-1`

required row-increment steps and

`D-r`

required column-decrement steps, for a total of

`D-1`

steps between occupied cells. Starting from one occupied cell, a monotone path with `D-1` unit steps contains exactly `D` cells, which is exactly `|E(G_P)|`.

Therefore no additional occupied cells are possible and none are missing.

### Theorem C99 — monotone lattice-path normal form

For the C87 common cut `r`, the `D` simple prefix edges are exactly the cells of a monotone lattice path

`(0,D) -> ... -> (r-1,r)`

using only the two unit moves

`(a,b)->(a+1,b)`

or

`(a,b)->(a,b-1)`.

Equivalently, after fixing `r`, `G_P` is encoded by a binary word of length `D-1` containing exactly `r-1` row moves and `D-r` column moves.

Conversely every such monotone cell path defines a connected antitone bipartite graph with `D+1` vertices and `D` edges, hence a tree satisfying the purely combinatorial C87 conditions.

Thus the combinatorial C87 conditions alone admit exactly

`binom(D-1,r-1)`

prefix trees for a fixed common cut `r`, and

`sum_(r=1)^D binom(D-1,r-1)=2^(D-1)`

across all possible cuts.

## 5. Degree/run correspondence

A left prefix vertex `a<r` has degree equal to the number of path cells in row `a`. A right prefix vertex `b>=r` has degree equal to the number of path cells in column `b`.

Hence vertex degrees are exactly the horizontal/vertical run lengths of the cell path, with a cell at a turn counted in both incident run descriptions in the natural way.

Deleting graph leaves from `G_P` leaves a path. Thus C99 also gives a direct proof that the prefix tree itself is a caterpillar, but the lattice-path encoding retains more order information than that classification.

## 6. Interaction with C98

At every C98-unsplit interior level `k`, the unique selected physical vertices `L_k,U_k` each inherit selected non-chain degree

`deg_(G_P)(k)`.

C99 therefore translates the physical diameter graph into two copies of the run structure of one binary lattice path, except at the at most `s+2` split levels allowed by C98.

There are now only two ways for the prefix tree to be complicated:

1. **long-run phase:** the binary path has long constant runs, producing high-degree paired diameter stars at unsplit levels;
2. **many-turn phase:** the binary path alternates often, producing long paired physical diameter paths through unsplit levels.

This is an exact exhaustive combinatorial dichotomy, not yet a geometric contradiction.

## 7. Next target

The useful next lemma should put geometry on the binary path. Long runs should be tested against C18's global shared-endpoint diameter-angle container and unit separation among the diameter neighbors. Many turns should be tested against the fact that the paired lift lies in a straight-line diameter thrackle and, in the zero/low-slack regime, almost every turn is physically unsplit.

C99 does not claim that either phase is impossible; it removes the arbitrary-tree ambiguity before that geometric step.