# Target C support-seven: minimal directed-cycle templates on the reciprocal segment graph

Date: 2026-09-19

Status: exact finite refinement of the global segment-order obstruction. The theorem-state authority is unchanged. C-II remains open.

## Result

The reciprocal-segment comparison graph is

\[
G=L(K_8),
\]

with 28 segment vertices and 168 rooted length-comparison edges. In the strict-length branch, a sign assignment is metrically order-consistent exactly when the induced orientation of `G` is acyclic.

A generic acyclicity test can of course be done by topological sorting. For certificate discovery it is useful to know the complete family of minimal directed-cycle obstructions.

Every directed cycle in an oriented graph contains a directed chordless cycle. Indeed, choose a directed cycle of minimum length. If its underlying undirected cycle has a chord, either orientation of that chord combines with one of the two directed arcs to produce a shorter directed cycle, contradiction.

Thus only induced cycles of `L(K8)` need be targeted.

The exact induced-cycle census is

```text
length 3      336
length 4      210
length 5      672
length 6     1680
length 7     2880
length 8     2520
```

There are no induced cycles of larger length because an induced cycle of length at least four in a line graph `L(K8)` uses distinct underlying vertices and therefore has length at most eight.

The 336 triangles split as

```text
280 root-star triangles
 56 side triangles of reciprocal K8 triangles
```

The 56 side triangles are order-tautological on the complete-angle system: their three segment comparisons are the comparisons of the three opposite ordinary angles of one Euclidean triangle. Since those three angle values are ordinary real scalars summing to `pi`, they cannot form a strict directed comparison cycle. They do not need a separate metric-order branch.

Consequently the strict global segment-order layer has only

\[
\boxed{280+(210+672+1680+2880+2520)=8242}
\]

nontrivial minimal directed-cycle templates.

## Classification of induced cycles

Let an induced cycle of `L(K8)` have segment vertices

\[
e_0,e_1,\ldots,e_{k-1}.
\]

Consecutive segment vertices share one endpoint in `K8`; nonconsecutive segment vertices are disjoint, because any shared endpoint would be a chord in the line graph.

For `k>=4`, let `v_i` be the common endpoint of `e_{i-1}` and `e_i`. The no-chord condition forces the `v_i` to be distinct, and

\[
e_i=\{v_i,v_{i+1}\}.
\]

Hence every induced `k`-cycle of `L(K8)`, for `k>=4`, is exactly the edge set of a simple `k`-cycle of `K8`. The converse is immediate: nonconsecutive edges of a simple cycle are disjoint, so its edge set gives an induced line-graph cycle.

Therefore the number of induced cycles of length `k>=4` is the standard number of undirected labelled simple `k`-cycles in `K8`:

\[
N_k=\binom8k\frac{(k-1)!}{2}
=\frac{8!}{2k(8-k)!}.
\]

This gives

\[
N_4=210,
\quad N_5=672,
\quad N_6=1680,
\quad N_7=2880,
\quad N_8=2520,
\]

and

\[
\sum_{k=4}^8N_k=7962.
\]

For `k=3`, a clique of three edges in a line graph comes from exactly one of two configurations in the underlying graph: three `K8` edges through one common endpoint, or the three sides of one `K8` triangle. Their counts are

\[
8\binom73=280,
\qquad
\binom83=56.
\]

## Directed-cycle certificate consequence

Suppose all 28 segment lengths are distinct and each of the 168 affine rooted comparisons has been assigned a strict sign. Orient the corresponding line-graph edge from the shorter segment to the longer segment.

Then the assignment extends to one strict global order of all 28 segment lengths if and only if none of the 8,242 nontrivial templates is directed cyclically.

Necessity follows from a scalar length order. For sufficiency, if the orientation were cyclic, a shortest directed cycle would be chordless. It is therefore one of the induced cycles classified above. A length-three side cycle is impossible already on the complete-angle triangle equations, leaving exactly the 8,242 listed templates.

This is a finite exact replacement for reasoning about arbitrary directed cycles.

Equal segment lengths remain a separate case. As proved in `target_c_support7_global_segment_order_2026-09-19.md`, zero comparisons must first be contracted. A strict edge inside a zero class is impossible, and the strict quotient must be acyclic. The 8,242-template statement is specifically the all-strict branch; it does not silently assume generic segment lengths from generic point position.

## Nonlinear metric use

Every induced cycle also supplies a short log-sine metric identity. For a simple `K8` cycle

\[
v_0v_1\cdots v_{k-1}v_0,
\]

let

\[
e_i=\{v_i,v_{i+1}\}.
\]

The adjacent segment lengths `lambda_{e_i}` and `lambda_{e_{i+1}}` are compared at root `v_{i+1}`. The sine law in triangle

\[
v_i,v_{i+1},v_{i+2}
\]

gives one ratio `lambda_{e_{i+1}}/lambda_{e_i}`. Multiplying around the cycle telescopes exactly to one.

Thus the same induced-cycle list is an overcomplete family of nonlinear metric certificates. The shortest useful cross-root family is the 210 four-cycles; if those do not close the remaining H6 cells, the exact next layers have 672 five-cycles, 1,680 six-cycles, 2,880 seven-cycles, and 2,520 eight-cycles.

These identities are redundant with the fifteen complete ground-root sine-law equations once the complete angular equations hold, but redundancy is useful for exclusion. The exact rational sine-interval engine can choose whichever short cycle admits the strongest certified angle box.

## Computational consequence for H6

The current explicit generic-H6 endpoint is 4,704 cells, with the exact reflection-closed upper bound 4,582. For each surviving affine/physical branch:

1. certify as many of the 168 rooted comparison signs as possible by exact Farkas duals;
2. reject immediately when a completed root-star or simple-cycle template is directed;
3. use the fourteen all-root interior-domination disjunctions as early branch choices because they directly constrain the same comparison graph;
4. on sign-consistent branches, scan the induced cycles in increasing length and use exact rational sine interval bounds to test the corresponding product identity;
5. fall back to the complete fifteen-equation metric system only for branches surviving the short-cycle tests.

The template family can be preindexed by comparison edge, so a branch decision only revisits cycles containing the newly oriented edge. A full topological-sort check remains an independent cheap guard.

Certificate: `research/verify_target_c_support7_global_segment_chordless_cycles_2026_09_19.py`.

## Scope

This note refines the generic reciprocal metric-order layer. It does not by itself exclude a new H6 cell and does not address reciprocal-collinearity walls. Its contribution is an exact finite classification of every minimal strict segment-order cycle and the corresponding short nonlinear sine-cycle search family.