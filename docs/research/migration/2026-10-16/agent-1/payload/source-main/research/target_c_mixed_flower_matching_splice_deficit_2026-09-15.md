# Target C-II — vertex-disjoint mixed flower splices force a global quadratic train deficit

**Date:** 2026-09-15\
**Status:** proof-only asymptotic structural theorem\
**Scope:** any linear family of bounded-face local through pairs with vanishing phase mismatch; live input supplied by the three-dominant full-flower normal form\
**Dependencies:** finite stopped-train path/crossing theorem; bounded-face connector interiors; strict-rhombus `>pi/3` crossing criterion\
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This note removes the main global objection to complement-phase flower through pairs.
The through pairs do **not** need to belong to one common dominant orbit if we first
select them vertex-disjointly.

Let `T_D` be the number of non-singleton complete strict-rhombus trains and `R_D` the
number of strict rhombi, equivalently edges of the train-crossing graph.  Suppose
`L_D` distinct bounded exceptional faces each carry a selected local through pair of
distinct train terminals such that, uniformly over the selected pairs,

1. the two paired train projective directions differ by `epsilon_D`, with
   `epsilon_D->0`;
2. their midpoint connector lies in the face interior, joins an entering end to a
   leaving end, and has positive projection along the common limiting train normal;
3. the connector direction is within `pi/6+epsilon_D` of that common normal.

Then one can select a matching of at least

\[
\boxed{P_D\ge {L_D\over3}}
\tag{MS.1}
\]

through pairs.  Splice only those matched pairs.  The resulting two-piece supertrains
have a simple intersection graph for all sufficiently large `D`, and

\[
\boxed{
R_D
\le {T_D^2\over4}-{P_D^2\over2}+O(D).
}
\tag{MS.2}
\]

Consequently

\[
\boxed{
{T_D^2\over4}-R_D
\ge {L_D^2\over18}-o(D^2).
}
\tag{MS.3}
\]

The result is phase-agnostic: different matched splices may converge to unrelated
projective directions.  Pairwise simplicity is proved using a projection chosen
separately for each pair of supertrains.

Combining with the three-dominant flower theorem, if `M_D` is a full-flower
population and `C_D` is its complement terminal-occurrence count relative to one
shrinking dominant orbit, then the locally through-spliceable population satisfies

\[
L_D\ge M_D-{C_D\over3}-o(D),
\]

and hence

\[
\boxed{
{T_D^2\over4}-R_D
\ge {1\over18}
\left(M_D-{C_D\over3}\right)_+^2-o(D^2).
}
\tag{MS.4}
\]

This is the first quadratic train-crossing penalty in the flower branch that survives
when the through pairs themselves have mixed complement phases.

---

## 1. The splice-incidence graph has maximum degree two

Build a multigraph `H_D` whose vertices are complete stopped trains and whose edges are
the `L_D` selected local through-pair faces.  One edge joins the two distinct trains
selected at that face.

There are no loops: the two selected sides are distinct sides of one bounded face, and
a complete train cannot have both terminal occurrences on the same bounded face.

Every complete train has exactly two terminal occurrences, so it is incident with at
most two selected splice faces.  Therefore

\[
\boxed{\Delta(H_D)\le2.}
\tag{MS.5}
\]

This remains true with parallel edges; no endpoint-simplicity theorem between two
different bounded faces is required.

---

## 2. A greedy matching keeps one third of all local through pairs

In any loopless multigraph of maximum degree two, greedily select an edge and delete
all edges incident with either endpoint.  Each selected edge deletes at most three
edges total: itself and at most one other edge at each endpoint.

Starting from `L_D` edges therefore produces a matching of size

\[
P_D\ge\lceil L_D/3\rceil,
\]

which proves (MS.1).  No cycle analysis or common global phase is needed.

For every matched edge, replace its two stopped trains and the chosen face connector
by one polygonal supertrain.  Since the matching is vertex-disjoint, every nonsingleton
supertrain contains exactly two original trains and one connector.  Every other train
remains a singleton supertrain.

---

## 3. Each matched supertrain is simple

The two train directions in a matched pair have projective separation at most
`epsilon_D`.  For large `D` this is strictly below `pi/3`, whereas two complete trains
can cross in a strict rhombus only when their projective directions differ by more
than `pi/3`.  Thus the two constituent train midpoint paths do not cross one another.

Each stopped train midpoint path is simple.  The selected connector lies in the
interior of its bounded exceptional face and meets the contact complex only at the two
terminal midpoints.  Hence the concatenated supertrain is simple.

Different selected connectors lie in interiors of different bounded faces and are
disjoint.  An ordinary train midpoint path never enters the interior of a bounded
exceptional face.  Therefore any intersection between two different matched
supertrains is an original strict-rhombus crossing between constituent trains.

---

## 4. Any two matched supertrains meet at most once

Take two matched supertrains `A,B`.  Let `alpha,beta` be representative projective
contact directions of their first train pieces, chosen so that

\[
0\le d:=\beta-\alpha\le\pi/2.
\]

Every train piece of `A` has direction within `O(epsilon_D)` of `alpha`; every train
piece of `B` is within `O(epsilon_D)` of `beta`.  By the stopped-train cone theorem,
every elementary midpoint displacement in `A` lies within

\[
\pi/6+O(\epsilon_D)
\]

of the normal `n_A=Jalpha`, and similarly for `B`.  The same bound holds for each
selected connector by hypothesis.

If

\[
d<\pi/3-4\epsilon_D,
\]

then every constituent train-direction pair has projective separation below `pi/3`,
so there is no strict-rhombus crossing at all.

Otherwise choose `X` along the angular bisector of `n_A,n_B`.  Since `d<=pi/2`, every
segment of either supertrain makes angle at most

\[
{d\over2}+{\pi\over6}+O(\epsilon_D)
\le {5\pi\over12}+O(\epsilon_D)
< {\pi\over2}
\]

with the positive `X` direction for large `D`.  Both supertrains are therefore
strictly `X`-monotone graphs.

At any actual rhombus intersection, the two constituent contact directions have
projective separation strictly greater than `pi/3`.  With the above oriented
representatives and `epsilon_D->0`, every such crossing uses the same orientation:
the `B` direction lies counterclockwise from the `A` direction by an angle in
`(pi/3,2pi/3)`.  The local centerline calculation from the signed monotone-grid lemma
then gives one common graph-crossing sign at every `A`--`B` intersection.

Two `X`-monotone graphs cannot have two transverse intersections with the same sign:
their vertical order would have to alternate.  Hence

\[
\boxed{
A\text{ and }B\text{ meet at most once.}
}
\tag{MS.6}

The argument includes the threshold case `d=pi/3`; no fixed angular margin from the
triangular orbit is required.

Unspliced singleton supertrains are ordinary stopped trains, so the same conclusion
with a matched supertrain follows by the identical one-piece version of the argument.
Thus the entire supertrain intersection graph is simple.

---

## 5. Every strict rhombus survives as one supertrain edge

A matched pair of constituent trains cannot cross each other because their directions
are `o(1)` apart.  Therefore no original strict rhombus becomes internal to one
supertrain.

Every original strict-rhombus crossing is consequently an intersection of two
distinct supertrains.  By (MS.6), two distinct original rhombi cannot collapse onto
the same unordered supertrain pair.  Since connectors create no intersections, the
simple supertrain intersection graph has exactly

\[
R_D
\]

edges.

---

## 6. Count edges after matching splices

Let

\[
r=P_D
\]

be the number of matched two-train supertrains and

\[
s=T_D-2P_D
\]

the number of singleton supertrains.  The induced graph on the `s` singleton
supertrains is a subgraph of the original stopped-train crossing graph, which is
triangle-free.  Mantel gives at most

\[
{s^2\over4}
\]

edges among them.

Because the whole supertrain graph is simple, the number of edges with at least one of
the `r` nonsingleton vertices is at most

\[
rs+{r(r-1)\over2}.
\]

Therefore

\[
\begin{aligned}
R_D
&\le {s^2\over4}+rs+{r(r-1)\over2}\\
&={T_D^2\over4}-{P_D^2\over2}-{P_D\over2}.
\end{aligned}
\tag{MS.7}
\]

Dropping the favorable linear term gives (MS.2).  Combining with
`P_D>=L_D/3` gives

\[
{T_D^2\over4}-R_D
\ge {L_D^2\over18}-O(D),
\]

and hence (MS.3) on the normalized scale.

---

## 7. Composition with full flowers

The three-dominant local normal form proves that if `C_D` complement terminal
occurrences occur across `M_D` full flowers, the number `L_D` of flowers carrying a
local through pair can be selected so that

\[
L_D\ge M_D-C_D/3-o(D).
\]

Insert this in (MS.3) to obtain (MS.4).

A useful coarse dichotomy is

```text
if L_D >= M_D/2:
    global train-crossing Mantel deficit >= M_D^2/72-o(D^2);
else:
    C_D > 3M_D/2-o(D),
    so >3M_D/4-o(D) distinct complement trains terminate on the flowers.
```

At the current `t<=1.8623` full-flower floor `M_D>0.1327D-o(D)`, the first branch
alone gives an additional structurally localized deficit exceeding

\[
{0.1327^2\over72}D^2>0.0002445D^2.
\]

This number is not competitive with the already-known aggregate full-flower Mantel
deficit; the point is different.  It is obtained from actual local through mechanisms
and remains valid with arbitrary complement splice phases.  The remaining high-value
step is to couple those matched supertrains to diameter bracing or exceptional-face
closure, rather than merely adding another scalar deficit.

**Disposition:** proved proof-only mixed-phase matching-splice deficit theorem,
conditional only on the stated local through-pair hypotheses.  C-II and Level I remain
open.
