> Generated reading edition · [exact source](../../../docs/reports/target_c_staircase_double_cover_caterpillar_audit_2026-09-05.md) · source SHA-256 `cfc52284d3128b7d94d5f5aa7cfffe25684cdbf806715ad7fcff11de1287a2a0`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-785DC6ECADC1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C staircase double-cover caterpillar audit

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** exact combinatorial normal form / route limitation  
**Target:** C87–C96 staircase/caterpillar intersection  
**Status:** LEVEL I STILL OPEN

## 1. Purpose

C93 and LS2 force a non-chain train to separate a linear number of the `2D` selected
paired staircase diameters.  C90 says the diameter graph across that secondary train
is a caterpillar forest.  Several continuation notes therefore phrase the next target
as an incompatibility between the C87 staircase and the C90 caterpillar.

There is an important redundancy: the exact C88 staircase is already a caterpillar,
and the two C87 physical orientations are its bipartite double cover.  Prefix-fiber
splitting only cuts this cover into smaller caterpillars.  The only cross-sheet
physical identifications can occur at `z,a`, which are endpoint fibers of the
caterpillar core; after imposing the C96 forest condition these identifications also
preserve the caterpillar property.

Thus **caterpillar graph shape by itself places no new capacity restriction on the
selected paired staircase**.  Any useful two-cut theorem must use the location/span of
the secondary train cap, physical endpoint order, equal-length geometry, or KKT/train
weights.

## 2. The C88 staircase tree is a caterpillar

Use the exact C88 parametrization.  There are integers

`t_0=D >= t_1 >= ... >= t_s=s`,

and the prefix tree has edge set

`E(G_P)={(i-1,b): t_i<=b<=t_(i-1), 1<=i<=s}`.

The low prefix vertices are

`A_i=i-1`, `1<=i<=s`,

and the high prefix vertices are `s,s+1,...,D`.

A low vertex `A_i` has degree

`deg(A_i)=t_(i-1)-t_i+1`.

Hence it is a non-leaf exactly when

`t_(i-1)>t_i`.

Now fix a high vertex `b`.  The rows containing `b` are precisely the consecutive
indices satisfying

`t_i<=b<=t_(i-1)`.

If `b` lies strictly between two consecutive values of the `t` sequence, it belongs
to one row and is a leaf.  If `b` equals a plateau value of the sequence, it can
belong to several consecutive rows.  Every interior row of that plateau satisfies

`t_(i-1)=t_i=b`,

so its low vertex has degree one.  Only the two rows at the ends of the plateau can
have non-leaf low vertices.  Therefore every high vertex has at most two non-leaf
neighbors.

Delete all leaves of `G_P`.  In a tree, the remaining induced graph is connected when
it has at least two vertices.  The preceding paragraph shows that every remaining
high vertex has degree at most two; every remaining low vertex is joined through the
two boundary values of its row and likewise has degree at most two after leaf
deletion.  The remaining graph is therefore a path (or a single vertex / empty).

### Theorem DC1 — staircase caterpillar

Every exact C88 prefix staircase tree `G_P` is a caterpillar.

The possible long rows and repeated `t_i` plateaus only attach leaves to this spine;
they do not create branching in the non-leaf core.

## 3. The two C87 orientations are the bipartite double cover

C87 gives, for every simple prefix edge `{a,b}` with `a<s<=b`, two selected physical
orientations

`L_a U_b`,

`U_a L_b`.

Before resolving physical multiplicity inside a side-level fiber, introduce abstract
vertices

`L_k,U_k`, `0<=k<=D`.

The abstract selected graph has exactly the two edges above over every edge of `G_P`.
Since `G_P` is bipartite with low shore `{0,...,s-1}` and high shore `{s,...,D}`,
this double cover splits into two connected components:

`L_low union U_high`,

`U_low union L_high`.

Each component is canonically isomorphic to `G_P`.

### Lemma DC2 — unsplit paired graph

With one abstract endpoint per side-level fiber and no cross-side endpoint
identifications, the `2D` selected C87 diameter edges form two disjoint copies of the
C88 caterpillar.

## 4. Physical prefix-fiber splitting cannot create a non-caterpillar

The physical graph `H_pair` may have several selected source vertices in one side-level
fiber.  Combinatorially this partitions the incidences of one abstract vertex among
several physical vertices: it is a vertex-splitting operation on the double cover.

Splitting a vertex of a caterpillar can only cut its spine and distribute its leaf
edges.  It cannot create a vertex with three non-leaf neighbors.  Consequently every
component after arbitrary side-level splitting remains a caterpillar.

This is exactly the operation counted by the FSB split excess

`S=sum_(X,k)(n_(X,k)-1)`.

Thus the split budget changes component count, but not the relevant graph class.

## 5. The only cross-sheet identifications are harmless once the graph is a forest

The arcs `L,U` meet only at the literal chain endpoints `z,a`.  Hence the only
possible physical identifications between the two double-cover sheets occur between
some split vertices in the level-`0` fibers, at `z`, and/or the level-`D` fibers, at
`a`.

In `G_P`, prefix vertices `0` and `D` are endpoints of the non-leaf core whenever they
survive leaf deletion.  Indeed `0` belongs only to the first low row, while `D`
belongs at the extreme end of the high-row ordering.  After vertex splitting, any
chosen physical piece of either endpoint fiber has at most one non-leaf neighbor.

Identifying one level-`0` or level-`D` piece from the two sheets can therefore join two
caterpillar cores only at endpoints, producing another path core.  If both endpoint
identifications close the two sheet cores into a cycle, the C96 common-cut **forest**
condition forbids that cycle; the necessary physical splitting cuts at least one of
the two core routes.  After the cut, every non-leaf core is again a path.

### Theorem DC3 — forest implies caterpillar automatically for the selected lift

Every physically realized C87 selected paired graph `H_pair` which satisfies the C96
common-cut forest condition is already a disjoint union of caterpillars, purely from
the C88 staircase normal form and prefix-fiber bookkeeping.

In particular, taking any subset of its edges, such as those additionally separated
by one secondary train, again gives a caterpillar forest.

## 6. Consequence for C93/LS2 + C90

Let `sigma` be the secondary train supplied by C93, H1, or LS2.  The selected edges
which `sigma` separates are a subgraph of `H_pair`.  By DC3 this subgraph is a
caterpillar forest **before** using the C90 caterpillar theorem.

Therefore the statement

> a secondary train carries many selected staircase edges and its cut graph is a
> caterpillar

has no graph-theoretic contradiction available from the word `caterpillar` alone.
The half-dense two-train reduction remains useful because `sigma` is one geometric
cut, but the useful data must be additional.

The nonredundant information available from one secondary train is:

1. both terminals of `sigma` lie on one boundary arc `L` or `U`;
2. its chain-neighborhood `J_sigma` is one consecutive interval of `P`;
3. the cut-off boundary cap selects a consecutive physical portion of that arc;
4. LS2 can force high load using only staircase edges of bounded chain span;
5. equal-length diameter chords across this cap retain the global thrackle order and
   C18 angle restriction.

## 7. Revised next target

The next theorem should be **cap/span-sensitive**, not graph-class-sensitive.  A useful
form is:

> Bound the number of selected C87 paired diameters of chain span at most `alpha D`
> whose physical endpoint lies in one same-side boundary cap cut off by a non-chain
> train, allowing the FSB prefix-fiber split budget.

LS2 then supplies the lower load

`((2alpha-alpha^2)/(T/D-1)-o(1))D`.

Any cap/span upper bound below this quantity for some `alpha` closes the low-train
branch.  C90 remains part of the geometric setup, but its caterpillar conclusion is
not itself the missing inequality.
