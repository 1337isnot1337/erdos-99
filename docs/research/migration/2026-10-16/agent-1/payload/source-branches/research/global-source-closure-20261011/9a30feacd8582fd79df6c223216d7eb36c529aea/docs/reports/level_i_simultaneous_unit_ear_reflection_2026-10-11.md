<!-- theorem-state: {"artifact_id":"ART-D775AE32341F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Level I — simultaneous unit-ear reflection and certified blockers

**Date:** 2026-10-11  
**Base commit:** `ab6dd333`; research checkpoint `4746fe17`  
**State version:** `2026-10-10.audit.234`  
**Target:** global finite-source competitor  
**Classification:** proved candidate awaiting promotion; unreviewed report  
**Level I:** OPEN

Only the problem definition and elementary convex geometry are dependencies of
the new statements. All source labels, including contact isolates, are retained.
No other worker's solution is used.

The closing chain is concrete:

```text
an independent unit-ear diameter cover with the full retained-point lower ledger
  -> simultaneous reflection with every old contact retained and all upper pairs safe
  -> a same-cardinality strict-sub-D source competitor.
```

Neither existence of such a cover nor its lower ledger is established for every
large triangle-free minimizer. The final section names the resulting obstruction.

## 1. Geometry of one ear

Let A be a finite unit-separated set with two-dimensional convex hull K. Let b be
a strict hull vertex whose two adjacent hull vertices a,c satisfy |a-b|=|c-b|=1.
Choose coordinates

\[
 a=(-u,0),\quad b=(0,h),\quad c=(u,0),\qquad u^2+h^2=1,
\]

with h>0 and all other hull vertices on the inward side y<=0 of the chord ac.
The reflected ear is b'=(0,-h); its displacement is 2h. Its distances to a,c
remain exactly one. Its hull exterior turn is 2arcsin(h).

**Ear shield.** No other source label lies in the closed ear triangle abc,
apart from a,c. Split the triangle along its median from b. One half lies in the
closed unit disk centered at a, the other in that centered at c, by convexity of
the squared norm. The only points in those halves that can avoid distance <1
to the respective center are existing vertices: strict convexity handles the
segment interiors, and the base midpoint is at distance u<1. Hence all other
source points are in the inward closed half-plane y<=0.

Consequently for every x other than a,b,c,

\[
 |b'-x|^2-|b-x|^2=4h\,y_x\le0.
\tag{1}
\]

This proves the complete upper-distance ledger for one reflected ear. Lower
distances require a separate check; absence of old contacts is insufficient.

**Loaded-ear containment.** If b is an actual diameter endpoint and 0<h<=1/2,
then b' lies in K. Here is a direct proof. Choose k with |k-b|=D. Necessarily
D>1 when |a-c|>1, and k is not a or c. Write k=(x,-v), v>=0. The inequalities
|k-a|<=D and |k-c|<=D, compared with |k-b|=D, give

\[
 h(v+h)\ge\frac12+u|x|,
 \qquad v\ge\frac{1-2h^2}{2h}.
\tag{2}
\]

In particular v>=h. At depth h below ac, the triangle ack has horizontal
cross-section centered at hx/v with half-width u(1-h/v). It contains x=0
provided h|x|<=u(v-h). By (2), the difference between the upper bound on the
left side and the right side, multiplied by u, is at most

\[
 (2h^2-1)v+h/2\le0,
\]

where the last inequality follows from v>=(1-2h^2)/(2h) and
(1-2h^2)^2>=h^2 for h<=1/2. Thus b' belongs to triangle ack, a subset of K.

## 2. A simultaneous reflection theorem

Let D=diam(A)>2. Select a set S of pairwise nonadjacent strict hull vertices.
Suppose each b in S has the two unit hull contacts above, is an actual diameter
endpoint, and has h_b<=1/2. Set R=A minus S and replace every b by its reflection
b'. Make the following explicit assumptions:

1. Every old unit contact incident to b is one of its two hull contacts.
2. For every b in S and every retained x in R other than those two neighbors,
   |b'-x|>1.
3. For distinct b,d in S, |b'-d'|>1.

Then the reflected full source A' is unit-separated and has exactly the old
contact graph. Moreover every pair distance is at most its original value.
Every original diameter pair incident to S becomes strictly shorter. Thus if
S is a vertex cover of the entire actual diameter graph,

\[
 \boxed{\operatorname{diam}A'<D.}
\tag{3}
\]

### Proof of the simultaneous upper ledger

The lower and contact assertions follow directly from assumptions 1--3 and
the exact two preserved hull contacts.

Every b' lies in K by loaded-ear containment. For any other selected ear d,
the two neighbors of d are retained. Assumption 2 and the preserved contacts
place b' at distance at least one from both. The ear shield leaves only the
old apex d as a possible outward position: retained-point separation excludes
the two neighbors. But b'=d would give |b'-d'|=2h_d<=1, contradicting
assumption 3. Thus b' is on the inward side of d's chord.

To compare two reflected labels b',d', first apply (1) to reflect b with d
still at its original position. Then apply (1) at d with b' already in its
inward half-plane. This gives

\[
 |b'-d'|\le |b'-d|\le |b-d|.
\]

For a retained x, (1) already gives |b'-x|<=|b-x|. Retained-retained pairs
are unchanged. This proves every upper pair, including previously inactive
pairs and cross-reflection pairs.

A diameter partner x of b cannot lie on the chord line ac: its intersection
with K is the segment ac, all of whose points are at distance at most one
from b. Since D>2, that partner lies strictly in the inward half-plane, and
the first comparison in which b is reflected is strict. Subsequent reflection
cannot increase it. A diameter cover therefore makes every old maximal pair
strictly shorter; every old submaximal pair stays submaximal. Finiteness gives
the strict maximum in (3).

### A sufficient cross-reflection lower margin

Assumption 3 follows from the easily checked original-source inequality

\[
 |b-d|>1+2h_b+2h_d\qquad(b,d\in S,\ b\ne d).
\tag{4}
\]

This is the triangle inequality with the two exact displacement lengths.
It is a sufficient condition, not an asserted property of arbitrary covers.

### The global cover allows new contacts

If S covers every actual diameter pair and all h_b<1/2, assumptions 2 and 3
may instead use >=1. The resulting endpoint may create unit contacts, including
triangles; its strictly smaller diameter still contradicts global optimality.
In the simultaneous upper proof, the possibility b'=d remains excluded because
|b'-d'|=2h_d<1. All the other steps are unchanged. Thus the global cover needs
only full unit separation, rather than exact contact-graph preservation.

This distinction matters at a new-contact tie. Such a tie obstructs the
lexicographic single-ear argument below but does not obstruct a global strict-D
cover competitor.

## 3. Necessary blockers in a lexicographic triangle-free optimum

Suppose A is a triangle-free global minimizer chosen to minimize its contact
count and then its actual diameter-pair count among triangle-free minimizers.
Let b be a loaded unit ear with h<=1/2 and no other unit contacts.
Then some retained nonneighbor x satisfies

\[
 |b'-x|\le1,
 \qquad 1<|b-x|\le1+2h.
\tag{5}
\]

Otherwise the single-ear reflection preserves exactly all unit contacts,
creates no triangle, and cannot increase any distance. It removes at least one
old diameter pair and creates none. If the maximum decreases, global optimality
is contradicted. If it stays D, the endpoint is a triangle-free minimizer with
the same contact count and fewer diameter pairs. That contradicts the secondary
minimum. Inequality (5) then follows from the displacement triangle inequality.

The blocker may be a contact isolate or a nonisolated source point. It is not
permissible to discard it or count it as a vacancy. Ties |b'-x|=1 count as
blockers, since a new contact would break the contact-count comparison.

## 4. A complementary boundary-turn obstruction

The following elementary statement concerns a convex unit-sided polygon in a
triangle-free full unit-separated source. Call a hull vertex ported if it has
a unit neighbor strictly inside the hull. A ported vertex has at most one such
neighbor: its interior angle is <pi, and avoiding triangles with both adjacent
unit neighbors leaves an angular interval of width <pi/3, whereas two unit
neighbors need angular separation at least pi/3.

At a ported vertex i, let alpha_(i-1),alpha_i be the increasing lifts of its
incoming and outgoing hull-edge angles, and beta_i the angle of its interior
unit-contact vector. Strict triangle-freeness gives

\[
 \alpha_i+\pi/3<\beta_i<\alpha_{i-1}+2\pi/3.
\tag{6}
\]

For adjacent ported vertices, both port vectors have angles in
(alpha_i+pi/3,alpha_i+2pi/3). Let Delta=beta_(i+1)-beta_i and
m=(beta_i+beta_(i+1))/2-alpha_i. Their port-to-port squared distance is

\[
 1+4\sin(\Delta/2)
       \bigl(\sin(\Delta/2)-\sin m\bigr).
\]

If Delta>0, then sin(Delta/2)<1/2 while sin(m)>sqrt(3)/2, so the distance
would be less than one. Therefore beta_(i+1)<=beta_i. Equality means the
two port vectors coincide and the four vertices form a unit rhombus.

Combining this monotonicity with (6), every contiguous block of ported
vertices has total exterior hull turn strictly less than pi/3. All vertices
cannot be ported, since a lift around the whole hull must gain 2pi.

If r vertices are unported and kappa_max is the largest hull exterior turn,
there are at most r ported blocks. Therefore

\[
 2\pi<r(\pi/3+\kappa_{\max}).
\tag{7}
\]

Triangle-freeness gives kappa_max<2pi/3, hence r>=3. If kappa_max<=pi/15,
then r>=6. This is an angular count only; it does not give a linear-sized
ear family, a diameter cover, or a packing surplus.

## 5. Exact regression and the remaining global bridge

The verifier `research/verify_level_i_unit_ear_reflection_2026_10_11.py`
checks every pair before and after reflection in exact rational full-source
fixtures. It verifies a two-ear diameter-cover competitor, retained deep
isolates, the original separation margin (4), and a near-unit isolate that
blocks an ear despite having no old unit contact. A new-contact tie is checked
separately and satisfies the broader global-cover theorem. A rational unit
octagon certifies cross-ear collisions, and a finite skew-ear sweep checks
loaded-ear containment at every listed parameter. The fixtures are nonglobal;
they certify the finite calculations
and the necessity of the lower hypotheses, not arbitrary-source extraction.

**Missing global bridge:** for every sufficiently large triangle-free minimizer,
extract an eligible independent ear cover and establish the retained lower ledger,
or give a compatible full-source repair of the blockers in (5). The boundary-turn
count (7) supplies neither requirement. The macroscopic inactive-container and
full-core C-II branches therefore both remain open. No promotion is claimed.
