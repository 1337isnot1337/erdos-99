<!-- theorem-state: {"artifact_id":"ART-235AD9E8B443","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — bounded-face train simplicity and exact mixed-train transposition

`inactive-interface rhombus labels -> planar simple bounded-face train graph or mixed O-F trains -> exact mixed two-train contact swap -> TWO-SIGN diameter support or another strict inactive blocker -> full finite release still required`

**Date:** 2026-10-02  
**Shared starting HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`  
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`  
**Previous checkpoint:** `192e3a77`  
**State version:** `2026-09-14.audit.51`  
**Mission / branch:** source-level TB1 inactive-interface repair; `swarm/tb1-diameter-order-20261001`.  
**Classification:** proved candidate awaiting promotion; conditional train extraction; rejected monotone repair mechanism. Artifact lifecycle remains unreviewed.  
**Level I / C-II:** OPEN / OPEN.

## 1. Source and actual geometric train hypotheses

Use the canonical normalized triangle-free C-II source, full actual contact
graph, full actual diameter graph, and relative-interior positive KKT
stress. Every source point, including contact isolates, is retained.

The bounded contact faces are simple convex unit polygons by canonical
Section 67. They are in fact strict at their boundary vertices: a loaded
vertex is extreme, while an unloaded nonisolated vertex is strictly
surrounded by its contact neighbors by shared Theorem 6.1. A face angle
at least pi would contradict one of those statements. Consequently a
bounded face has at most one edge in any given oriented direction, and
at most two edges in a fixed projective direction.

Use complete stopped trains with their actual midpoint curves. A
nonsingleton train is an embedded path; all its contact edges are parallel,
each midpoint step has length one and angle strictly between pi/3 and
2pi/3 relative to its coherently oriented contact direction. Two trains
cross only in a strict rhombus, at most once. In particular, trains whose
projective directions lie in a window of width W<pi/3 are noncrossing.
These train facts follow from the canonical rhombic-complex argument in
shared Theorem 10.6, with singleton contact edges adjoined when needed.

The statements below concern this actual geometric train complex, not an
abstract face graph or a lattice substituted for the source.

## 2. A narrow-phase bounded-face train graph is planar and simple

Fix a projective direction window of width W<pi/3. Form G_F on the f
bounded nonquadrilateral faces. Put an edge F-G for each nonsingleton
complete train in that window with terminal faces F and G.

**Theorem.** G_F is a simple planar graph. In particular, it has at most

\[
P(f)=\begin{cases}0,&f\le1,\\1,&f=2,\\3f-6,&f\ge3\end{cases} \tag{1}
\]

edges. The same face pair cannot carry two such trains, even with
different directions.

### 2.1 No bounded-face loops

If a train ends twice on F, close its midpoint path by an arc in the
interior of the convex face. The resulting Jordan curve is inside the
source hull and crosses the contact graph exactly at the parallel edges
of that train, all with the same shore orientation. No actual diameter
endpoint lies inside the curve, because every such endpoint is extreme.
Summing positive equilibrium over its full-source inner shore therefore
gives A u=0 with A>0, impossible.

The curve avoids source vertices. Isolates inside it contribute zero;
they are not discarded. This is a direct positive-reaction proof of
the scoped bounded-loop exclusion.

### 2.2 Two nonparallel trains cannot join the same bounded faces

Suppose distinct trains tau,rho join F to G. They are noncrossing by
their narrow phase window. Join their two terminals inside F and inside
G. Since those convex face interiors are disjoint and contain no contact
edge, the two train paths and the two joining arcs make one Jordan
curve. The curve is contained in the source hull and avoids its extreme
vertices. Its contact cut is exactly E(tau) union E(rho).

The unit contact vectors oriented into the inner shore are constant
along each of the two paths. Positive equilibrium and absence of any
inner diameter endpoint give

\[
A u+B v=0,\qquad A,B>0, \tag{2}
\]

where u,v are the two shore-oriented contact directions. They must be
opposite and parallel. Thus nonparallel tau,rho are impossible.

There is no requirement that the two terminal edges have the same
boundary-occurrence sign. Equation (2) derives the necessary sign.

### 2.3 Parallel trains also cannot repeat the face pair

Let n be perpendicular to the common direction. At a terminal edge
where a train leaves F in its forward n-direction, its midpoint x is
on the supporting line max_{F} n dot p. At the other terminal y, G is
on the opposite side of its contact edge, so y is on min_{G} n dot p.
Monotonicity along a nonsingleton train gives

\[
\min_G n\cdot p>\max_F n\cdot p. \tag{3}
\]

If a second parallel train uses F, strict convexity permits only the
opposite parallel terminal edge of F. It therefore travels in the
opposite n-direction and yields

\[
\max_G n\cdot p<\min_F n\cdot p. \tag{4}
\]

Equations (3) and (4) contradict each other. Two trains cannot use one
terminal contact edge because that edge belongs to one complete train.
This proves simplicity. Contract the disjoint bounded face interiors to
vertices; the remaining noncrossing train paths give a planar embedding.
The planar simple edge bound proves (1).

This does not assert that G_F is a forest. An acyclic orientation is
different from an acyclic underlying graph.

## 3. Ultrasmall bounded-face trains have a strict height potential

Assume now D>=2 and W<=1/(2D). Choose the midpoint normal n_0 of the
direction window. Orient an F-G train so that its midpoint steps have
positive projection on the corresponding normal n, with
angle(n,n_0)<=W/2. Define the face height

\[
c(F)=\tfrac12(\min_F n_0\cdot p+\max_F n_0\cdot p).
\]

**Theorem.** Every oriented nonsingleton F-G edge obeys

\[
\boxed{c(G)-c(F)>1/5.} \tag{5}
\]

Thus this orientation is a directed acyclic graph, and every directed
path has fewer than 5D edges.

### Proof

Let x,y be terminal midpoints. F supports x in the +n direction and G
supports y in the -n direction. Each of at least one unit midpoint steps
has n_0 projection greater than cos(pi/6+W/2), so

\[
n_0\cdot(y-x)>\cos(\pi/6+W/2).
\]

For any z in F, support in n gives
n_0 dot(z-x)<=(n_0-n) dot(z-x)<=2D sin(W/4).
The analogous lower support error at y in G has the same bound. The
nonnegative half-widths of F,G in n_0 can be dropped. Consequently

\[
\begin{aligned}
c(G)-c(F)
&>\cos(\pi/6+W/2)-4D\sin(W/4)\\
&\ge\sqrt3/2-W/2-DW\\
&\ge\sqrt3/2-1/8-1/2>1/5.
\end{aligned}
\]

All face heights lie in a projection interval of length at most D,
which proves the path bound. The proof uses actual unit steps and actual
convex face supports. It does not require KKT coefficient bounds.

## 4. An exact mixed O-F transposition

Let tau,rho be two noncrossing complete trains with one terminal each
on the same bounded face F and the other terminal each on the global
outer face. Choose a common projective lift with distinct unit directions
u,v and angle epsilon<pi/3. Require that the terminal occurrences on the
oriented boundary of F have the same sign in this lift.

Join the two terminal midpoints by an arc inside F. The concatenated
tau-path, joining arc, and reversed rho-path is a proper outer-to-outer
crosscut. One full-source shore S has its cut contacts exactly

\[
u\quad\text{on tau},\qquad -v\quad\text{on rho}. \tag{6}
\]

Translate S by Delta=v-u. Every old contact remains unit, since

\[
u+\Delta=v,\qquad -v+\Delta=-u. \tag{7}
\]

The move has displacement oscillation |Delta|=2sin(epsilon/2). It is
an exact finite move, not an infinitesimal face-closure argument.

If u,v belong to one open cell between consecutive global actual
diameter directions, the entire TB1 fork extends to this mixed pair.
Set s=|Delta| and w=(u-v)/s. For every moving old diameter r_h oriented
into S,

\[
|r_h\cdot w|>Ds/2. \tag{8}
\]

This is the exact projective non-grazing estimate: no actual diameter
direction lies between u and v, and w is normal to their angular
midpoint. Positive equilibrium across the composite cut gives

\[
A u-B v=\sum_h\beta_h r_h,
\qquad (A u-B v)\cdot w=(A+B)s/2>0. \tag{9}
\]

There is therefore a positive-sign moving diameter. Either a negative
sign also occurs, or every changed diameter strictly shortens because

\[
|r_h-sw|^2-D^2=-2s(r_h\cdot w)+s^2
<-(D-1)s^2<0. \tag{10}
\]

In the latter case minimality forces a strict inactive pair with old
length in (1,1+s] or [D-s,D). When s<=1/(2D), the move-independent
isolate forest leaves at most d_H exceptional upper pairs. In the
cyclic d_H=0 case the mixed ONE-SIGN move necessarily has a near-unit
lower blocker. Isolates may be dispatched differently from their
geometric shore; old contacts and diameters, hence (8)-(10), are
unaffected by that reassignment.

Opposite face-terminal signs instead give contact vectors u and v on
one shore. The second rigid translation solution is Delta=-(u+v),
which is large for a narrow phase window. The ultrasmall theorem
deliberately requires matching signs.

## 5. Apply the two theorems to the cap-expelled blocker population

Return to the alternating common-swap family in
[the cap reaction report](target_c_disjoint_cap_reaction_capacity_2026-10-01.md).
Let N_nr be its chosen lower labels that are not rhombus diagonals.
The chosen rhombus labels use distinct transverse trains in two narrow
phase bands, each of width epsilon<=1/(2D).

At most fourteen chosen labels use O-O trains. In each band at most
P(f) use F-F trains, by (1). Therefore the mixed O-F label population
satisfies

\[
\boxed{N_{OF}\ge r-d_H-N_{nr}-14-2P(f).} \tag{11}
\]

A band of width less than delta_D contains at most one actual diameter
direction. Remove the mixed trains parallel to that direction. At most
two can terminate on any one bounded face, by strict convexity, so at
most 2f per band are removed. The others fall in at most two open
global diameter cells. Group by terminal face, occurrence sign, and
cell: at most 4f groups per band. Distinct trains in one group have
distinct directions, again by strict convexity of their terminal face.

Pair trains inside each group. In both bands together this gives at
least

\[
\boxed{\max\{0,\lfloor(N_{OF}-12f)/2\rfloor\}} \tag{12}
\]

exact mixed transpositions satisfying the hypotheses of Section 4.
This does not assert that their source shores are pairwise disjoint,
that their swap vectors coincide, or that every pair is ONE-SIGN.
Those conditions must be proved before reusing an arborescence bound.

Consequently, under the additional f=o(D), N_nr=o(D) hypotheses, a
linear alternating common-vector ONE-SIGN family forces a linear
number of actual mixed-pair TB1 forks. The inactive ends have not been
treated merely as abstract obstruction labels: they supply exact new
finite contact moves. The hypotheses f=o(D) and N_nr=o(D) are not
current universal C-II consequences.

## 6. Hostile repair audit: face-vector conservation blocks a naive fix

The mixed phase exchange does not automatically repair the original
u-to-v rhombus blockers. Their transverse thresholds lie between x
and y. Permuting thresholds that all lie there leaves them there.

More generally, suppose a collection of mixed trains has identical
oriented face-terminal signatures and no other bounded terminal.
Keeping all other train directions fixed, exact vector closure at F
requires

\[
\sum_j u_j'=\sum_j u_j. \tag{13}
\]

For two distinct, nonopposite directions this has only the original
unordered pair as its unit-vector solutions: dotting u_1'+u_2'=a
with u_1' fixes u_1' dot a=|a|^2/2; the line intersects the unit
circle at exactly u_1 and u_2. Thus a two-train correction is only
the transposition, not an arbitrary rotation past a blocking threshold.

For any larger class whose old and proposed new phases remain in one
interval of width less than pi, choose its midpoint tangent w. The
function w dot u(theta)=sin(theta-midpoint) is strictly increasing
throughout the interval. If every phase increased and at least one
increased strictly, (13) would fail after dotting with w. The same
holds for decreasing every phase. Thus raising every problematic
transverse threshold while fixing all other terminal classes is a
rejected repair mechanism.

This is a finite vector-closure obstruction, not an asymptotic rank
claim. It identifies the necessary compensating train class. It does
not prove that all possible compensations are blocked.

## 7. Dependencies and precise remaining gap

Canonical dependencies are positive full-support source equilibrium,
shared Theorem 6.1 strict trapping, the rhombic-complex pseudosegment
proof, and [Section 67 convex bounded faces](../targets/target-c/67-rhombus-population-transport-audit.md).
The current diameter direction spacing is in
[Section 66](../targets/target-c/66-forest-doubled-gap-audit.md).
The core convention remains that of Section 57; no isolate is inserted
into its matrix and no source point is dropped.

The actual rectangle/alternating-swap extraction and the prior
cap/dispatch reports are unpromoted dependencies only in the application
(11)-(12). The abstract geometric face graph and the exact composite
crosscut move have their full proofs here. No finite computation is used
to claim those universal results. The preceding exact tooth verifier
remains a regression showing why source equilibrium cannot be omitted.

The next attack must couple terminal-sign classes through the actual
bounded-face closure system, or prove enough disjoint ONE-SIGN mixed
pairs to obtain another source-anchored blocker tree. A smallest phase
gap alone is insufficient: rhombus blockers may occur at a half-open
threshold endpoint in another phase label, and non-rhombic or isolate
pairs need not be controlled by any train phase. The finite fork has
been carried into the mixed inactive-interface branch, but its lower
constraints have not been released.

No global f=o(D), simultaneous compatibility, forced original unit
triangle, strict sub-D source competitor, or Level I closure is claimed.
The exact-phase, split-star, macroscopic inactive-container/exterior-cap,
and other full-core branches remain explicitly unresolved.
