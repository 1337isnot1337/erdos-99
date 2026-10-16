<!-- theorem-state: {"artifact_id":"ART-D43687C4B8AF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: isolate-preserving finite release inside a curved unit wall

Date: 2026-10-06. Authority: `35f5843ab9f5d11327d0f4cc803ed00707806ae7`,
state `2026-10-06.audit.65`. Classification: **proved candidate awaiting
independent audit** for the conditional source exclusion; **feasible
geometry** for the constructed family. No result is promoted. C-II and
Level I remain open.

The implication being proved is

`actual curved unit wall + certified boundary clearance -> finite inward
wall motion retaining every isolate -> full-source lower/upper safety ->
strict contact loss -> exclusion from the canonical representative`.

This supplies a non-repacking finite endpoint in a specified chamber
geometry. It does not obtain that geometry from a reciprocal chart or
from leading density. Canonical inputs are the audit.63 one-vertex convex
wall shield, contact-minimal normalization and interior-hull upper safety.

## 1. Wall and source geometry

Fix an integer `M>=4` and unit vectors

\[
 u=(1,0),\qquad v=(c,s),\quad
 0<c<1/2,\quad s=\sqrt{1-c^2}>0.
\tag{1}
\]

Let `theta>0` be sufficiently small for this fixed `M,c`. The four side
base directions, in order, are `u,v,-u,-v`. On each side use the `M`
consecutive unit vectors

\[
 e_j=\operatorname{Rot}((2j-M+1)\theta)w,
 \qquad j=0,\ldots,M-1.
\tag{2}
\]

Their perpendicular components cancel. Put

\[
 L=\sum_{j=0}^{M-1}\cos((2j-M+1)\theta).
\]

The four side displacements are `Lu,Lv,-Lu,-Lv`, so the polygon closes
exactly. All cyclic direction gaps are positive and less than `pi` for
small `theta`. These balanced unit vectors in cyclic angular order give
a strictly convex polygon `F_theta` with `4M` actual unit edges. The
successive corner positions are `0,Lu,L(u+v),Lv`. Write `q_{a,i}` for
vertex `i` on side `a`, including `i=0,...,M-1`.

Set

\[
 \lambda={1\over100M},\qquad
 \ell=1+\lambda\theta+O(\theta^3),\qquad
 o={L\over2}(u+v).
\]

A particular exact choice is
`ell=1+tan(theta/2)/(50M)`. Retain the `(M-1)^2` points

\[
 z_{ij}=o+\ell\bigl((i-M/2)u+(j-M/2)v\bigr),
 \qquad 1\le i,j\le M-1.
\tag{3}
\]

For sufficiently small positive `theta`, these points are strictly
inside `F_theta`, mutually at distance greater than one, and strictly
unit-clear of every wall vertex. Thus they are actual contact isolates
in this finite packet. The packet has `(M+1)^2` points, with quadratic
isolated population and only `4M` contacts. No global optimality, KKT
completion or general source chart is asserted for this family.

### Lower clearance of the cloud

At `theta=0`, wall positions are the boundary of the `M` by `M` oblique
unit grid. Every nonbasis grid difference has squared distance strictly
greater than one because `0<c<1/2`. Finiteness preserves those margins
for small `theta`. The inner basis differences in (3) have length `ell>1`.

The only initially unit wall-to-inner distances occur in the first inner
row or column. On the bottom side, the wall vertex at index `i` has
first displacement

\[
 q_{0,i}'(0)=-i(M-i)Ju.
\tag{4}
\]

The derivative of the inner point in the first row is
`lambda[(i-M/2)u+(1-M/2)v]`; the corner shrink and center change are
second order. Its unit separation from that wall vertex therefore has
positive half-squared-length derivative

\[
 i(M-i)s+\lambda\{c(i-M/2)+(1-M/2)\}>0.
\tag{5}
\]

The absolute value of the last term is at most `3/400`. The first term
is at least `(M-1)s`, with `s>sqrt(3)/2`. The other three sides have the
same bound after their rotations and sign reversals. This proves every
old unit wall-to-inner distance becomes strict. At `theta=0` the cloud
is already strictly inside the limiting parallelogram, so interior
containment also persists.

## 2. Explicit inward sites and their full lower checks

On every side choose indices

\[
 i\in\{2,5,8,\ldots\}\cap[2,M-2].
\]

Let `B` be the resulting wall-vertex bank. Then

\[
 |B|=4\lfloor(M-1)/3\rfloor.
\tag{6}
\]

For a selected vertex on side base `w`, let

\[
 n_{a,i}=J\operatorname{Rot}((2i-M)\theta)w,
 \qquad h=3\sin\theta,
 \qquad x_{a,i}=q_{a,i}+h n_{a,i}.
\tag{7}
\]

The normal is the inward bisector of its two wall contact directions.
Each of those neighbor vectors has scalar product `sin(theta)` with
this normal. Thus their exact new squared distances are

\[
 |x_{a,i}-q_{a,i\pm1}|^2
 =1+h^2-2h\sin\theta
 =1+3\sin^2\theta>1.
\tag{8}
\]

All other wall distances of a root are strict for sufficiently small
`theta`: their limiting grid differences are nonbasis differences. Roots
on the same side are separated by at least three old steps; roots across
an adjacent corner are at least two steps from that corner and have
limiting distance at least `2sqrt(2-2c)>2`; roots on opposite sides have
limiting distance at least `M s>2`. Consequently both the selected old
vertices and the proposed roots have pairwise distance greater than two
for small `theta`. Every root is inside `F_theta`. Its displacement has
positive inward component at its two incident sides and at every edge
on its own gently curved side; all other-side supports have strictly
positive limiting slack because its index is away from the corners.

### The isolates remain fixed

For the first inner row next to a selected bottom root, subtract its
additional displacement `3Ju` in (5). The half-squared-length derivative
is now

\[
 [i(M-i)-3]s
 +\lambda\{c(i-M/2)+(1-M/2)\}.
\tag{9}
\]

Since `2<=i<=M-2`, this is at least

\[
 (2M-7)s-3/400>0.
\tag{10}
\]

The three other sides have the same estimate. Every other root-to-cloud
pair has strict limiting lower slack. Thus every isolate in (3) remains
at its old coordinate and is strictly unit-clear of every root. No
interior repacking, deletion, packet-capacity estimate or uniform chart
radius is used.

## 3. Conditional canonical-source exclusion

Suppose an actual unit-separated source contains this convex unit wall
and its only interior points are the cloud (3). The source may contain
arbitrarily many additional core points and contact isolates outside the
wall. More generally it is enough that every actual interior point is
strictly unit-clear of the selected roots; the exact cloud is one proved
sufficient geometry for that requirement.

Replace the vertices `B` by the roots (7), keeping every other source
point, including every interior isolate, fixed. Each root is in the
canonical one-deleted-vertex strict-safe region: it is in `int F_theta`
and strict-clear of every other original wall vertex. Audit.63 shields
it from every retained exterior source point. Section 2 checks every
interior point and every pair of new roots.

Every pair involving a new root is strictly below the old source diameter,
since that root is inside the old full-source convex hull. All retained
old-old pairs are unchanged. Every full-source lower constraint holds,
and no new contact is created. The `2|B|` original wall contacts incident
with `B` are distinct and disappear; any additional old exterior contacts
at those vertices disappear as well. The retained contact graph is an
induced old subgraph and the new points are isolated, so triangle-freeness
is preserved. Cardinality is unchanged.

Therefore this actual source cannot be the contact-minimal canonical
triangle-free global minimizer. This is a full-source finite contradiction
under the explicit chamber hypothesis. Its wall vertices need not be
diameter-loaded. It has no inactive upper exceptions to absorb and makes
no claim about a path through feasible smaller amplitudes: the finite
root step clears its two old contact constraints exactly by (8).

The exact family has an open robustness neighborhood. If an actual
interior cloud is perturbed by less than half the minimum root-to-cloud
distance margin in this finite construction, all root clearances remain
strict. That radius is source-dependent; no canonical theorem currently
places an arbitrary chamber cloud in that neighborhood.

## 4. Physical cost of every surviving blockade

Keep the wall geometry above, but allow an arbitrary unit-separated
interior cloud. Exact unit distance alone does not block a root. If all
interior distances from that root are at least one, its new unit contacts
can be opened while retaining every other strict pair condition.

To check this, use the local coordinates `q_b=0`, inward bisector `n`,
tangent `a`, and wall neighbors
`+cos(theta)a+sin(theta)n` and
`-cos(theta)a+sin(theta)n`. Put `h=3sin(theta)` and `x_b=hn`.
An interior old point `z=za a+zn n` has `zn>=0`. If `|z-x_b|=1` and
`zn<=h`, then

\[
 |za|\ge\sqrt{1-h^2},\qquad |z|^2\le1+h^2.
\]

Old unit separation from both wall neighbors instead requires

\[
 |z|^2\ge2\cos\theta\,|za|+2\sin\theta\,zn
 \ge2\cos\theta\sqrt{1-9\sin^2\theta}>1+9\sin^2\theta.
\]

The last strict inequality holds for `0<sin(theta)<=1/10`; squaring
positive sides reduces it to
`3-58 sin(theta)^2-45 sin(theta)^4 >= 4831/2000 > 0`.
This is a contradiction. Every new unit neighbor therefore has `zn>h`.
An arbitrarily small move of the root in direction `-n` strictly increases
all these unit distances. Its finite strict wall/exterior lower margins,
interior location and upper margins persist. Thus such a root still yields
the contact-loss contradiction.

Consequently every genuinely blocked root in a canonical source requires
an actual interior source point at distance **strictly less than one** from it.
Distinct
roots in this bank have distance greater than two, so their closed unit
disks are disjoint. One source point cannot block two roots.

If every root is blocked, there are consequently at least `|B|` distinct
physical interior source points `z_b`, with

\[
 1\le|z_b-q_b|<1+3\sin\theta,
 \qquad |z_b-x_b|<1.
\tag{11}
\]

Audit.67 corrected the original isolate-only inference: a blocker can
contact the deleted wall vertex. The lower inequality in (11) is strict
only under an explicit contact-isolate hypothesis. See the exact
nonisolate regression in
`docs/audits/target_c_curved_wall_independent_audit_2026-10-06.md`.

This is an injective blocker payment, with one distinct source point per
proposal. The source has quadratic interior population, so this linear
count is not by itself contradictory. The prescribed cloud (3) is
excluded because (9)--(10) put every such point outside the blocking
disks. For a general canonical chamber, an argument must exclude or
physically spend the wall-adapted near-unit collar (11); it may not label
the bank spare capacity or discard it as subleading.

## 5. Composition, hostile scope and exact remaining gap

The large near-triangular fixed-wall regression has unit contacts among
its interior points and retains its whole wall. Its capacity conclusion
does not cover the strict isolate cloud (3) and finite inward steps (7).
The curved family above has the full quadratic grid population; no
vacancy is needed. A small numerical vacancy search suggested the
construction, but no numerical search or solver is used in its proof or
the final verifier.

This does not exclude a general macro chamber. Its actual wall is not
forced to have (2), and its actual source cloud is not forced to have (3)
or the needed boundary clearance. Leading packing density, reciprocal
coordinates and near-unit phase agreement do not supply that positional
premise. The bent-grid transport regression is a binding warning against
that inference. Multigrain clouds and all source points outside the
chamber remain part of the open global task.

The next strengthened statement must use the actual boundary collar:
either certify at least one root's clearance in a general sufficiently
large canonical chamber, or show that a fully blocking collar such as
(11) entails a strict same-cardinality competitor or an exact unit triangle.
For the full-core branch, face-coupled heterogeneous train endpoints
remain separately open. No exhaustive branch has been closed here.

## 6. Exact finite verification

[The verifier](../../research/verify_target_c_curved_wall_isolate_motion_2026_10_06.py)
uses only rational arithmetic. Its four source sizes are 25, 49, 81 and
169, with 9, 25, 49 and 121 retained contact isolates. It certifies every
one of the 18,912 old and 18,912 new pairs, all exact old/new contacts,
strict convexity and interior inequalities, root-bank separation above
two, and every new-involving strict upper pair. The exact neighboring
contact release is `3 sin(theta)^2`. Every isolate remains at its old
coordinate. The infinite small-curvature statement and exterior shield
are analytic; no sample asserts a uniform curvature threshold or global
optimality.
