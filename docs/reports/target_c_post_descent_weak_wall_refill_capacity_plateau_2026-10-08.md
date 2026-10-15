<!-- theorem-state: {"artifact_id":"ART-270DA1D0C535","canonical":true,"claim_ids":["C-NEAR-TRIANGULAR-WALL-CAPACITY-PLATEAU-REGRESSION","C-NONCONTACT-WALL-WEAK-SHIELD","C-POST-DESCENT-WEAK-WALL-REFILL","C-UNIT-SEPARATED-MOVING-WALL-CROSSING-BARRIER"],"claim_statuses":{"C-NEAR-TRIANGULAR-WALL-CAPACITY-PLATEAU-REGRESSION":"regression","C-NONCONTACT-WALL-WEAK-SHIELD":"canonical","C-POST-DESCENT-WEAK-WALL-REFILL":"canonical","C-UNIT-SEPARATED-MOVING-WALL-CROSSING-BARRIER":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C: weak wall refill after descent and a capacity plateau

Date: 2026-10-08.
Run base: `c26d2f061a1c5ef44f1ca9a11fa7d466aeea2546`.
Canonical base: `b1b0a9a05f787a675973c36c6120530777c9040c`.
State: `2026-10-08.audit.149`.
Classification: independently audited in Audit.169. The weak wall shield, post-descent refill implication, and moving-wall barrier are canonical; the explicit flat-grid family is a regression.
Registry: mixed; see the independent audit. C-II and Level I remain open.

Rechecked after rebasing onto
`50ee4761dd8cdc04f93357d21f18ddadfdcff1e5`,
state `2026-10-08.audit.151`. The newly promoted assigned-mark
interval and singleton-terminal capacity claims alter no premise below.

## 1. Closing chain and the missing premise

A separate stress-deletion candidate remains unreviewed. The [canonical
finite-descent alternative](../audits/target_c_contact_opening_transversal_independent_audit_2026-10-07.md)
can yield a reduced full source of diameter strictly below the original
diameter. At that endpoint, a refill can have unit contacts and unit
triangles. Its upper distances are already controlled by the smaller hull.

    actual strict reduced-source endpoint
      + actual disjoint source-vertex walls of side length <=sqrt(3)
      + weakly guarded packets paying every interior and deleted label
      -> full same-cardinality unit-separated configuration of smaller diameter
      -> contradiction to global minimality.

The weak wall theorem below proves this implication. It does not produce
the packets. The regression proves that arbitrarily small grid phase error
and strict opening of every old contact do not alone increase a specified
wall's capacity, even by one site. It is not a canonical C-II source.

## 2. Closed-guard wall shielding

Let A be a finite unit-separated set. Let Q be a simple polygon whose
distinct cyclic vertices belong to A, and suppose its sides have length
at most L<=sqrt(3). If x is inside Q and at least one from every wall
vertex, then x is at least one from every point of A outside int Q.
For an outside point not itself a wall vertex the quantitative bound is

\[
 |x-q|\ge 2\sqrt{1-L^2/4}\ge1.
\]

Proof. For a wall vertex q use the guard directly. Otherwise let z be
the first exit of the segment from x towards q. If z is a wall vertex,
the two distances to z are at least one and add along this segment.
If z=(1-t)a+tb lies on a side, the exact identity

\[
 |w-z|^2=(1-t)|w-a|^2+t|w-b|^2-t(1-t)|a-b|^2
\]

gives |w-z|>=sqrt(1-L^2/4) for w=x,q. Their distances add.
This is the closed-guard version of
[Audit.88](../audits/target_c_noncontact_wall_shield_independent_audit_2026-10-07.md).
It uses no density argument at equality. With L<sqrt(3), the separation
from nonwall outside points is strict; guards at wall vertices can be equal.

Now take finitely many such polygons with pairwise disjoint interiors.
Each wall vertex of one is outside the interior of every other. Indeed,
a simple polygon has interior points arbitrarily close to each vertex;
a vertex inside another polygon would force an interior overlap.

Weakly guarded, internally unit-separated packets in their respective
interiors are jointly unit-separated. To check packets in Q_i and Q_j,
first apply the preceding shield in Q_j to each source wall vertex of
Q_i. The packet point in Q_j is at least one from all those vertices.
Then apply the same first-exit calculation in Q_i to the two packet
points. This argument permits touching boundaries and nonconvex polygons.

## 3. Exact post-descent replacement

Let A_0 be an n-point source of diameter D. Delete a label set R and
move every retained label to obtain a unit-separated A of diameter D'<D.
All retained labels, including contact isolates, remain in A.

Choose walls as in Section 2 from A. Let S_i=A intersect int Q_i.
For each i choose a finite weakly guarded, internally unit-separated
packet Y_i in int Q_i. If

\[
 \sum_i |Y_i|\ \ge\ |R|+\sum_i |S_i|,
\]

then

\[
 \bigl(A\setminus\textstyle\bigcup_i S_i\bigr)
       \ \cup\ \textstyle\bigcup_iY_i
\]

has at least n points and is unit-separated by Section 2. Every point
belongs to conv A, since a simple polygon lies in the convex hull of
its vertices. The diameter of conv A is D'. Select any n of the points
if there is a surplus. This is an actual smaller-diameter competitor.

No new-contact opening, triangle exclusion, or separate upper-pair
dispatch is needed at this endpoint. The cardinality inequality remains
essential. It includes every old interior label, irrespective of stress
support or contact degree.

There is also an elementary moving-wall conservation rule. During a
continuous unit-separated source motion, a nonwall label cannot cross a
simple source-vertex wall whose side lengths remain strictly below two.
At a first crossing it is either at a wall vertex, or on a side and
within side-length/2<1 of an endpoint. Both violate separation. This
rule assumes the wall stays simple throughout the interval. Pairwise
disjointness of several moving wall interiors is a separate hypothesis.
It is not a theorem that a strict infinitesimal descent has a prescribed
large continuation.

## 4. An unbounded near-triangular capacity plateau

For any integer M>=2 put

\[
 \tau={1\over100M^3},\quad
 c={1-\tau^2\over1+\tau^2},\quad
 s={2\tau\over1+\tau^2},\quad
 u=(1,0),\quad
 v=\left({c-\sqrt3s\over2},{s+\sqrt3c\over2}\right).
\]

The angle theta from u to v is pi/3+2 arctan tau. In particular
49/100<cos theta<1/2 and its phase defect is at most 2 tau.
Let

\[
 G_M=\{iu+jv:0\le i,j\le M\},\qquad q=(-2,-2),\quad r=(10M,0).
\]

The source A_M=G_M union {q,r} is unit-separated and triangle-free.
Its only unit pairs are adjacent grid indices along u or v: the
integer quadratic form a^2+b^2+2ab cos theta is one only at
(a,b)=(+-1,0),(0,+-1). If both indices are nonzero with opposite
signs, its minimum is 2-2 cos theta>1; equal signs give still more.
Both extra labels are contact-isolated.

The unique actual diameter is rq, with

\[
 D_M^2=(10M+2)^2+4.
\]

Distances from r to grid points attain their maximum at a corner of
the parallelogram; their squared maximum is 100M^2. Distances within
G_M union {q} are at most 3M^2+10M+8, which is smaller than D_M^2.
Thus the only diameter joins two isolates. In particular this family
has no normalized KKT stress and fails the canonical C-II hypotheses.

Delete r, and multiply every retained position, including q, by
L=1+t, where 0<t<=1/(10M^2). All retained pairs now have distance
strictly greater than one and

\[
 \operatorname{diam} A_t^2
 \le L^2(3M^2+10M+8)<20M^2<D_M^2.
\]

Use the actual 4M boundary labels of the scaled grid as a wall Q_t.
Its sides have length L<sqrt(3). Its old interior contains exactly
S=(M-1)^2 source labels.

The exact weak packet capacity of this wall is **S**, throughout
the entire displayed positive interval of t. The old scaled interior
grid realizes S with strict guards. For the upper bound, any weakly
guarded packet Y together with the 4M wall vertices is unit-separated
in the closed convex parallelogram. The canonical
[finite Oler inequality, Lemma 21.1](../theory/03-oler-shell.md) gives

\[
 |Y|+4M\le {2\over\sqrt3}L^2M^2\sin\theta+2LM+1.
\]

Since 2 sin theta/sqrt(3)=c+s/sqrt(3)<=1+2 tau, the right side
minus (M+1)^2 is at most

\[
 M^2(2t+t^2)+2\tau M^2(1+t)^2+2Mt
 \le {1\over5}+{1\over400}+{1\over50}+{1\over10}
 ={129\over400}<1.
\]

Here M>=2, t<=1/(10M^2) and (1+t)^2<2 were used term by term.
Integer rounding gives |Y|+4M<=(M+1)^2, hence |Y|<=S.
The packet cannot pay even the single deleted label r at this wall.

The source is independently certified nonglobal: n=(M+1)^2+2
ordinary square-lattice points in M+2 columns and at most M+1 rows
have squared diameter at most (M+1)^2+M^2<D_M^2.

This regression does not contradict the
[specified curved-wall root bank of Audit.68](../audits/target_c_near_triangular_curved_wall_capacity_independent_audit_2026-10-06.md).
The current wall is flat on each grid side, the deleted label is
outside it, and no root bank is supplied. It does not exclude a
different wall, several walls, a larger finite motion, or a global
repacking. It excludes the inference that strict contact opening
and o(1) phase error by themselves force an extra slot at a given wall.

## 5. Certificate and remaining obligation

`research/verify_target_c_post_descent_capacity_plateau_2026_10_08.py`
uses exact arithmetic in Q(sqrt(3)). For M=4,6,8,12 it checks every
source pair, every retained endpoint pair, and every same-cardinality
square-grid competitor pair; the actual contact/diameter graphs;
triangle-freeness; the retained isolate; boundary and interior ledgers;
strict contact opening; and the integer Oler upper bound.

The proof for every M and every t in the interval is Section 4,
not inference from those samples. The wall theorem is the exact
first-exit proof in Sections 2-3. No fixture is a global minimizer,
canonical source, or stress-deletion certificate.

The unresolved arrow is actual finite activation: produce packets
whose total wall capacity increases enough to restore all deleted
source labels, or give another same-cardinality strict competitor.
The strict reduced endpoint alone does not settle that arrow.
