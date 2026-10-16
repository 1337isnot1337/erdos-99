<!-- theorem-state: {"artifact_id":"ART-CE3447378ADC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — exact-phase circulation is an antitone paired tree

**Phase 2 preservation provenance:** PR #594, branch swarm/gap-reaction-cut-20261001, audited source head 02d4cc04e2df2e0f0aa1eb2a9ec3cf21cc53f18f. Preserve as an unreviewed conditional exact-phase candidate; the finite open-cell statement is not extended across threshold and the report does not close C-II.

`source force/cut order -> antitone signed gap support -> paired support tree
and global witness-cell chart isolation -> remaining tree/opposite-shore
geometry contradiction or competitor outside that chart -> Level I`

**Date:** 2026-10-01<br>
**Starting shared HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`<br>
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`<br>
**Predecessor checkpoint:** `0823faa8`<br>
**Canonical state:** `2026-09-14.audit.51`<br>
**Mission:** exact-phase signed gap cycles, their force labels, and finite release.<br>
**Classification:** proved candidate awaiting promotion; conditional on the
explicit unpromoted route inputs listed below.<br>
**LEVEL I:** OPEN. C-I closed; C-II open.<br>
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`.

## 1. Exact statement

Work with the retained exact-phase shore of the fixed-star O–O rectangle,
in its current open witness cell or singleton threshold cell. Keep the
full canonical source, including contact-isolated points. Assume the
proper nested train cuts and full-rank exact contact chart from the
October-1 rank report. Retain the positive full-support source KKT stress.

Orient each nonzero gap edge by the sign of its transverse derivative
coefficient, as in the predecessor positive-circulation report. If
$F_{pq}$ denotes the aggregate positive flow on directed gap edge $p\to q$,
then the source force/cut geometry gives

\[
F_{pq}>0,\ F_{rs}>0,\ p<r\quad\Longrightarrow\quad q\ge s. \tag{1}
\]

Thus the directed support is **antitone** in the gap order. In consequence:

1. $F_{pq}=F_{qp}$ for every pair of gaps;
2. the underlying simple support graph is a tree on $m+1$ vertices;
3. every tree edge has actual diameter rows of both transverse signs;
4. there are at least $2m$ transversely active actual diameter rows;
5. the support tree admits recursive contraction of an adjacent gap pair;
6. in an open witness cell, no nontrivial finite change of the selected
   train directions **remaining in that cell** can weakly shorten all
   old actual diameters in the exact contact-preserving chart.

The tree is the support of the **entire nonzero packet after parallel gap
edges are aggregated**, rather than an arbitrarily chosen row basis.
Each edge carries a paired positive flow. In threshold phase the graph
conclusions still hold; the finite open-cell conclusion is not extended
across the threshold.

## 2. Dependencies

Canonical inputs:

- normalized KKT equilibrium, shared theory Theorem 4.1;
- full actual support of a relative-interior stress on the lexicographic
  representative, `56-ci-restored-frontier.md`;
- mixed core rigidity, `57-zr-zf-rigidity-audit.md`;
- the convex reciprocal force polygon in cyclic loaded-terminal order,
  `01-force-hull-and-shear.md`, Section 7; in particular, for any fixed
  projection, the strictly positive and strictly negative projected
  reactions form complementary boundary arcs, with zero projections at
  their transitions;
- the convex diameter-thrackle property and uniqueness of a projective
  diameter direction.

Unpromoted inputs, explicitly used only for the route application:

- `target_c_global_diameter_star_contiguity_2026-09-30.md`;
- `target_c_local_witness_cell_2026-10-01.md`;
- `target_c_complete_grid_rank_switching_2026-10-01.md`;
- `target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md` for the
  outer-disk/cyclic layer interpretation;
- the predecessor positive-circulation theorem and its explicit contact
  chart, proved in this branch.

The star-contiguity argument is checked directly below at the point where
it is used. No prior reaction-braid report is a premise. In particular,
opposite **inward strip** signs are not silently identified with opposite
**outward vertex** signs.

## 3. Mixed outward signs occur only at extreme witness vertices

Let $v=Ju$, and orient diameter vectors outward from each incident vertex.
Every diameter star fits in an ordinary cone of aperture at most $\pi/3$:
two incident length-$D$ bars have other endpoints at distance at most $D$.
If a vertex has both signs of the projection onto $v$, its star cone
contains the projective direction $u$ in its interior.

In an open witness cell, star contiguity then puts both bounding global
diameter directions in that star. Those two edges already meet at the
fixed witness vertex $z$. As distinct edges of a simple graph, they have
only that common vertex. Hence the mixed vertex is exactly $z$.

In threshold phase, the same argument puts the unique parallel diameter
$e_0$ in every mixed star. Thus there are at most two mixed vertices,
the endpoints of $e_0$.

The common witness edges have full shore support. Their endpoints have
gap labels 0 and $m$. Consequently $z$ is in an extreme gap. In threshold
phase the two possible mixed vertices are in the two extreme gaps.
Reverse the gap order when necessary, so the open-cell mixed vertex is
in gap 0.

All other loaded vertices have one strict outward transverse sign on
every incident diameter, and their reaction has that same sign. The
only parallel edge in threshold phase joins the two extreme witness
vertices and contributes no transverse gap row.

This is a statement about the outward vectors at one actual vertex. A
reaction pair sharing an endpoint but using inconsistent inward
orientations does not satisfy its premise automatically.

## 4. Zero transverse reaction in every gap orders the sign arcs

Let $g_x=\sum_y\beta_{xy}(p_x-p_y)$ be the outward diameter reaction.
Sum KKT equilibrium over a selected train shore. Every crossing contact
has the one coherent unit direction $u$, so

\[
\sum_{x\text{ in that shore}}g_x=A_i u.
\]

Taking the $v$ projection gives zero. Differences of consecutive shore
identities, and total force balance at the two extreme gaps, give

\[
\sum_{x:\ell(x)=j}g_x\cdot v=0
\qquad(0\le j\le m). \tag{2}
\]

The cyclic sequence of loaded-vertex layer labels is bitonic: one boundary
arc increases from 0 to $m$, and the other decreases back to 0. This is
the proper nested-crosscut statement; it is not true for arbitrary
assigned labels.

The convex force polygon makes the vertices with $g_x\cdot v>0$ one arc
$P$, and those with $g_x\cdot v<0$ one complementary arc $N$. A loaded
vertex outside the mixed witness set cannot have zero projection.

For completeness, the precise force-order input also follows directly
from actual diameter geometry. If $xy$ is a diameter and $b$ is any
other loaded hull vertex, then

\[
(p_x-p_y)\cdot(p_x-p_b)\ge\tfrac12|p_x-p_b|^2>0.
\]

This follows by expanding $|p_b-p_y|^2\le D^2=|p_x-p_y|^2$.
Positive summation puts $g_x$ strictly inside the outward normal cone
of the loaded hull at $x$. Those cone interiors occur in strict cyclic
order. Thus the projected sign arcs and zero transitions used here
are exact properties of the actual diameter reactions, rather than
an assumption about a generic abstract force polygon.

Each extreme layer is a single boundary block. By (2), that block either
contains both signs, hence a transition of $P,N$, or consists solely of
zero-projection mixed witness vertices. Such a zero edge of the convex
force polygon is also at a sign transition. The two disjoint extreme
blocks therefore contain the two transitions. Between them the gap
labels are monotone on $P$ and on $N$, in opposite cyclic orders.

Full derivative rank guarantees that each gap contains a loaded endpoint;
no empty extreme block is being used. Source contact isolates remain
present, but have no diameter reaction and do not enter this boundary
force order.

## 5. Actual chords give antitone directed gap support

For a diameter not incident with a mixed witness vertex, the outward
transverse signs at its endpoints are opposite. Orient the chord from
its $N$ endpoint to its $P$ endpoint. Its transverse vector is positive,
so its directed gap edge is exactly from the $N$ layer to the $P$ layer.

Consider two such edges $p\to q$ and $r\to s$ with $p<r$ and $q<s$.
The endpoints have different gap labels in each sign arc and cannot
share an endpoint. The opposite cyclic label orders on $P,N$ make their
four endpoints nonalternating. Hence their chords do not cross,
contradicting the actual diameter-thrackle property.

The same conclusion holds with an extreme mixed witness endpoint. A
chord from an extreme layer 0 to a $P$ vertex of layer $q$ cuts off the
$P$ prefix through $q$; to cross it, another nonextreme $P$ endpoint must
have layer at most $q$. A chord from an $N$ vertex of layer $p$ to extreme
layer 0 similarly requires the other $N$ endpoint to have layer at most
$p$. Reversing the gap order proves the layer-$m$ versions. These are
exactly the inequalities needed to exclude $p<r,q<s$, including pairs
of extreme-root chords.

There is no hidden shared-endpoint exception. Strict inequalities exclude
sharing endpoints in the same directed role. Sharing in opposite roles
would require a mixed vertex with an internal gap label (the shared
label lies strictly between the other two labels); Section 3 excludes
that. An edge between the two threshold witnesses is the parallel edge
already omitted. This proves (1).

## 6. Antitone balanced flow is symmetric

This part is an independent exact finite theorem. Let $F\ge0$ be a
loop-free antitone matrix with equal row and column sums $s_j$, and put
$W=\sum_j s_j$. Define $S_i=\sum_{j\le i}s_j$.

For the rectangle of rows at most $i$ and columns at most $j$, let its
mass be $A$. Let $B$ be the mass in the complementary lower-right
rectangle. Marginal balance gives

\[
A-B=S_i+S_j-W.
\]

Antitonicity prohibits $A>0$ and $B>0$ simultaneously: any entries in
the two rectangles would have both coordinates strictly increasing.
Therefore

\[
\sum_{p\le i,q\le j}F_{pq}
=\max(0,S_i+S_j-W). \tag{3}
\]

The right side is symmetric in $i,j$. Taking two finite differences
proves $F_{pq}=F_{qp}$.

The positive-circulation theorem supplies precisely the balanced
marginals required here. Aggregation of parallel actual rows does not
discard their signs or make a source identification.

## 7. The simple support is a tree with adjacent contraction

List the distinct directed support pairs by increasing first coordinate
and, within a row, decreasing second coordinate. Antitonicity makes the
second coordinate nonincreasing across the entire list. Between
successive distinct entries the integer

\[
p+(m-q)
\]

strictly increases. It ranges from 0 to $2m$, so there are at most
$2m+1$ entries. Loop-free symmetric support has an even number of
entries, so there are at most $2m$. Its underlying simple graph has
at most $m$ edges. Connectedness forces exactly $m$, hence a tree.
Each undirected edge has rows in both directions, proving the $2m$
actual-row lower bound.

Take an edge $p<q$ of minimum span. If $q-p>1$, vertex $p+1$ has some
neighbor $t$. Symmetry and antitonicity against $p\to q$ and $q\to p$
force $p\le t\le q$. But then $|t-(p+1)|<q-p$, a contradiction.
Thus an adjacent edge exists. Contract its two adjacent vertices in the
ordered list. The support stays connected, symmetric, and antitone;
loops disappear and no strict increasing pair is introduced by a
monotone contraction. Induction gives complete adjacent elimination.

## 8. Finite isolation throughout an open witness cell

Use the exact contact chart of the predecessor report, with each new
direction $R_{t_i}u$ in the same coherent open cell $J$ as the original
$u$. The underlying support tree has an adjacent gap edge, whose actual
support interval consists of one train coordinate $i$. It has diameter
rows of both coefficient signs.

For an actual diameter vector $r$, the function

\[
f_r(t)=r\cdot R_tu
\]

has derivative $r\cdot JR_tu$. That derivative never vanishes in $J$,
since $J$ contains no actual diameter direction. Its sign is its sign
at the initial $u$.

For the singleton interval row, the finite relative displacement is
$\sigma(R_{t_i}u-u)$. Consequently, when $c_h t_i>0$,

\[
|r_h+\sigma(R_{t_i}u-u)|^2-D^2
=2\sigma[f_{r_h}(t_i)-f_{r_h}(0)]
 +|R_{t_i}u-u|^2>0.
\]

Opposite row signs therefore force $t_i=0$ in any putative weakly
nonexpansive configuration. Contract the corresponding adjacent gaps.
All remaining diameter displacements have the same interval formula
with that zero coordinate deleted. The support stays a paired antitone
tree. Repeat until every $t_i=0$.

No infinitesimal motion is being integrated. This excludes all finite
changes within $J$ in this chart, including large collective changes
whose small first variations almost cancel. It makes no assertion
about a move crossing a diameter direction, opening old contacts, or
leaving the chart.

## 9. Exact regression exposing the missing boundary order

Positive circulation by itself does not give Section 8. The certificate
uses $t=1/10000$, $D=10^6$, and the rational unit-vector parametrization

\[
U(z)=\left({1-z^2\over1+z^2},{2z\over1+z^2}\right).
\]

Take four actual diameter vectors

\[
r_k=D U(a_kt),\quad
(a_0,a_1,a_2,a_3)=(6/5,-13/10,7/5,-3/2),
\]

and the eight actual endpoints $\pm r_k/2$. Assign the lower and upper
gap labels of each oriented vector the pairs

\[
(0,3),\quad(1,3),\quad(1,2),\quad(0,2).
\]

The signed gap graph is the directed cycle

\[
0\to3\to1\to2\to0,
\]

with positive flow weights $\beta_k$ proportional to $1/|r_k\cdot Ju|$.
The derivative matrix has rank 3. Set the three new train directions
to $U(t),U(-t),U(t)$ in the assigned contact-chart formula. All are
strictly inside the old diameter witness cell. Exact arithmetic shows
that every pair stays unit-separated and the new squared diameter is
strictly below the old one by more than $239/10000$.

The source has no contacts and is not a minimizer. More decisively, its
actual circular layer-label sequence is

\[
3,2,0,1,0,1,2,3.
\]

The gap-0 vertices occupy two separate boundary arcs. These labels
cannot arise from the proper nested cuts. The directed pair
$2\to0,3\to1$ violates antitonicity. Thus the repaired theorem adds a
tested, indispensable source-embedding hypothesis; it does not claim
that arbitrary interval labels supply it.

## 10. Certificates and limits

Run `python3 research/verify_ordered_gap_circulation_2026_10_01.py`.
Exact rational/integer arithmetic checks 1,089 antitone balanced
couplings, all 31 connected loop-free symmetric antitone support
graphs through six vertices and their full adjacent elimination, the
eight-point regression, and the crossing/shared-endpoint chord-order
lemma with one or two extreme mixed vertices through nine gap labels.
The universal proofs are Sections 3–8, not an inference from finite
survival.

The certificate omits actual contact/train embedding, a full source
KKT stress, the opposite complete shore, and global optimality of its
regression. No numerical optimum, uniform multiplier floor, or
unproved finite-release theorem is used.

## 11. Exact remaining closing target

The exact-phase fixed-star gap graph is reduced to an ordered tree of
paired actual diameter packets. This changes the object to attack:
one must couple that paired tree to the opposite complete shore and
its positive reactions, or find a finite source competitor crossing a
diameter direction or leaving the contact-preserving chart.

The tree and its finite within-cell rigidity do not themselves
contradict global minimality. In particular, the predecessor rational
five-point star realizes a paired antitone support tree with nonzero
axial reaction, but has no actual train system or global optimality.
No exact unit triangle is forced here.

The nonconstant TB1, split-star O–O, inactive-interface,
macroscopic-container, and higher-surplus full-core branches are not
eliminated. Level I remains open.

**Promotion recommendation:** unreviewed research packet. Independently
audit the source antiorder bridge, especially cyclic force order and
the extreme mixed-vertex cases, before any promotion transaction.
