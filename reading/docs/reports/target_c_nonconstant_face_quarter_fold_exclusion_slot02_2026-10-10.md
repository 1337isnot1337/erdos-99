> Generated reading edition · [exact source](../../../docs/reports/target_c_nonconstant_face_quarter_fold_exclusion_slot02_2026-10-10.md) · source SHA-256 `1f7077efec74ff8372dc3ded578a1cd578f4beae1647e4e33d1dbcb99153711e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-73F983B2C2DC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: exclude every nonconstant large face at a full quarter-fold

**Date:** 2026-10-10. **Worker:** 02.
**Base main:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.
**State:** `2026-10-10.audit.234`.
**Previous checkpoint:** `b72237dc48d363bdce5d8c3c5ac3bf25463d0890`.
**Branch / PR:** `research/sol61-slot02-20261010-integrated-fold`, [PR #948](../publication/provenance.md#source-records).
**Classification:** proved candidate awaiting independent mathematical audit;
unreviewed and noncanonical. **LEVEL I: STILL OPEN.**

## 1. Main theorem and consequence

**Theorem 1.1 (proved candidate).** Let `P` be a triangle-free global minimizer
in the canonical C-II contact-first, diameter-pair-second normal form, with
`D>=9`. Let `Q` be a full-source same-cardinality unit-separated placement
of diameter at most `D`, with exactly the same contact graph. Suppose every
core contact has quarter-fold increment

`Q_j-Q_i=s_ij J(P_j-P_i)`, `s_ij in {-1,+1}`.

Then the signs on every old **simple bounded actual contact face of degree
at least five** are constant. A nonconstant large-face quarter-fold cannot
have a full-source feasible endpoint.

Every old bounded face of degree at least five therefore remains an actual
bounded face and keeps exactly its old interior isolate population, by the
pinned rigid-cycle theorem proved in the preceding worker report. This is
a full-source statement; it does not follow for arbitrary lower-feasible
core folds or nonglobal finite polygon models.

```text
nonconstant old convex face in a full-source feasible quarter-fold
 -> four transitions, each arc turn below pi/3
 -> every internal arc star rotates uniformly and points into the folded cycle
 -> the entire folded interior is an unloaded positive net pinned at four corners
 -> contact minimality gives full pinned bar rank and a positive row dependence
 -> Eppstein's edge/diameter bound gives corner-hull diameter at most 5
 -> exactly seven integer arc-count cases
 -> actual old exterior contacts force more distinct interior labels than Oler allows
 -> contradiction
```

This closes the nonconstant **large-face** branch of the full quarter-fold
endpoint system, subject to independent audit. It constructs no endpoint.
Mixed-sign rhombi, contact bridges, pure quadrilateral face districts, and
non-quarter finite motions remain. In particular, ruling out a proposed fold
mechanism does not itself contradict a canonical source or resolve Erdős #99.

## 2. Canonical inputs and precise literature check

The old source has connected nonisolated core `G=(V,C)`, all actual unit
contacts positively weighted in a relative-interior stress, and every actual
old diameter endpoint in the core. Isolates stay in the full source.

At `Q`, global optimality gives diameter exactly `D`, triangle-freeness follows
from its exact contact graph, and contact count is still minimal. Item 4 of
[C-I restoration](../targets/target-c/56-ci-restored-frontier.md) therefore
gives positive contact weights at `Q` too. **No secondary diameter minimum at
`Q` is assumed.** Only contact equilibrium at vertices with no actual diameter
is used from its stress.

Other inputs:

- [Shared local theory](../theory/01-local-structure.md), Theorems 4.1 and 6.1,
  and [shared shell theory](../theory/03-oler-shell.md), Lemmas 21.1 and 22.1:
  exact KKT, strict surrounding, finite Oler, and strict convexity of actual
  bounded source faces.
- [Audit 83](../audits/target_c_face_coupled_quarter_fold_independent_audit_2026-10-07.md):
  nonconstant convex faces have exactly four transitions forming an inscribed
  parallelogram; every transition turn exceeds `pi/3`; two-hop sign compatibility.
- [Audit 229](../audits/target_c_minimum_face_size_local_endpoint_independent_audit_2026-10-09.md):
  each of the four arcs has at least two unit edges.
- [Audit 100, Claim 2](../audits/target_c_generic_isolate_anchor_avoidance_independent_audit_2026-10-07.md):
  a simple unit wall of at most six edges has no additional interior point in
  a triangle-free unit-separated source. The sole weak-clearance exception,
  the regular hexagon center, creates triangles and is unavailable here.
- Eppstein's connected triangle-free penny-graph bound, already used in
  [the canonical pinned-boundary module](../targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md).
  The original journal article was checked live for this application:
  [*Edge Bounds and Degeneracy of Triangle-Free Penny Graphs and Squaregraphs*](https://www.maths.tcd.ie/EMIS/journals/JGAA/accepted/2018/463.pdf),
  JGAA 22(3), 483--499 (2018), **Theorem 2, printed page 491, PDF page 9**.
  For a connected `v`-vertex triangle-free penny graph of **graph-theoretic**
  diameter `delta`, it gives `e<=2v-delta-2`. No squaregraph equality or
  near-quadrangulation classification is imported. Scaling the equal disks to
  radius `1/2` makes the actual geometric contact edges unit length; the
  combinatorial edge/diameter theorem is unchanged by that normalization.

The prior [pinned-cycle and arc-star report](target_c_rigid_cycle_pinned_stress_and_arc_stars_slot02_2026-10-10.md)
is noncanonical; the needed new arc-star argument is proved here in full.

## 3. Four arcs, their turns, and the folded hull

Assume an old actual convex face `F` has a nonconstant fold. Write its four
transition corners in cyclic order and its arc lengths as `r_1,...,r_4>=2`.
The chord quadrilateral is a nondegenerate parallelogram, with side lengths
`A,B` and angles `gamma,pi-gamma`, where `pi/3<gamma<2pi/3`.

Let `a_i,b_i>=0` be the tangent-to-chord deflections at the first and last
edges of arc `i`, and `T_i=a_i+b_i` its total internal turn. If `tau_i` is
the actual transition turn and `kappa_i` the chord corner turn, then

`tau_i=kappa_i-b_{i-1}-a_i`.

Consecutive chord turns sum to `pi`. Thus

`tau_i+tau_{i+1}=pi-T_i-b_{i-1}-a_{i+1}>2pi/3`,

which gives `T_i<pi/3`. Strict old face convexity makes every internal arc
vertex turn strictly positive, so `T_i>0`. Projecting its unit edges onto
the bisector of their direction interval yields

`(sqrt(3)/2) r_i < L_i < r_i`,

where `L_1=L_3=A`, `L_2=L_4=B`. Consequently each opposite arc pair satisfies

`max(r_i,r_{i+2}) < (2/sqrt(3)) min(r_i,r_{i+2})`.        (3.1)

The folded cycle is simple: unit contact edges cannot cross or overlap at
nonincident labels in a unit-separated placement. Its internal arc turns
are still positive; each transition turn becomes `tau_i-pi<0`. The total
signed turn is `2pi-4pi=-2pi`, so it is clockwise. Its internal arc vertices
are reflex and its four transitions convex. A reflex vertex of a simple
polygon is not on its convex hull; a straight hull-side vertex also cannot
have a reflex sector, since the polygon lies in its vertex hull. Therefore
all internal arc vertices lie strictly inside the hull of the four transition
corners. That hull `H` is the folded chord parallelogram.

Every core label strictly inside the cycle is also strictly inside `H`.
Its distances to all full endpoint labels are strictly below `D`, by the
convex-combination variance identity for the four corners. The same is true
at every internal arc vertex. Isolates are not omitted when asserting this
strict upper slack.

The later rank computation uses only the indicated core coordinates as
variables; every isolate coordinate remains fixed and every pair with those
labels is checked by this upper slack and finite strict lower slack. The Oler
count concerns an actual subset of wall and neighboring labels. Leaving
additional isolates out of that subset weakens its lower count and deletes
no source label from the motion or from the original configuration.

## 4. Every internal arc star is uniformly rotated

Fix an internal arc vertex `v`. Its old face rays have angular positions
`0,theta`, with `theta=pi-delta in (2pi/3,pi)` and common arc sign `s`.
All other old contact rays lie outside this empty face sector. Triangle-free
unit neighbors have angular gaps strictly above `pi/3`, so there are at most
two other rays. At the endpoint, `v` is reflex and has no actual diameter;
contact minimality makes its full contact star strictly surrounding. Its
degree is therefore three or four.

If it has one extra ray at `alpha`, then

`theta+pi/3<alpha<5pi/3`.

Flipping this ray relative to the face rays places it at `alpha-pi`, strictly
between `0` and `theta`: the new three rays lie in an open half-plane.
That contradicts strict surrounding. Its sign must be `s`.

With two extra rays `alpha_1<alpha_2`, spacing gives `alpha_1<4pi/3` and
`alpha_2-theta>2pi/3`. The first has chord greater than `sqrt(3)` from the
ray at `0`; the second has such a chord from the ray at `theta`. Two-hop
compatibility forces both extra signs to be `s`.

Thus **every incident edge at an internal arc vertex has the arc sign**.
Every old nonwall neighbor points outside `F`; under this one rotation, it
points into the folded cycle's reflex interior sector. Its unit edge cannot
leave the cycle again without crossing a unit boundary edge or passing
through a source label, both impossible. All these neighbors lie strictly
inside the new cycle. There are no nonconsecutive wall contact chords in
an old convex actual face, so these neighbors are not wall labels.

Let `T` be **all** endpoint core labels strictly inside this folded cycle.
It is a union of components of `G-W`. Let `J` consist of `T` and the `m-4`
internal wall vertices. Every contact neighbor of `J` outside `J` is one of
the four transition corners: inside components cannot cross the cycle, and
all extra contacts at internal wall vertices have just been shown to enter it.
The contact graph on `J` plus the four corners is connected, since it contains
the wall cycle and every inside component reaches that cycle. It is a genuine
triangle-free penny graph on actual endpoint labels, not an auxiliary scaffold.

## 5. Four positive pins force hull diameter at most five

Put `v=|J|+4`, and let `e` count all contacts in the just-defined graph.
There are no contacts between its four pins: `A,B>sqrt(3)`, and the shorter
diagonal has square

`A^2+B^2-2AB|cos gamma| > (A-B)^2+AB >3`.

**Pinned rank is `2|J|`.** Otherwise a nonzero infinitesimal bar flex `u`
with all four pins and all other full-source labels fixed exists. At every
contact incident to `J`, the straight motion satisfies

`|Q_i+t u_i-Q_j-t u_j|^2=1+t^2|u_i-u_j|^2>=1`.

At least one of these contacts opens: if every endpoint velocity difference
were zero, connectedness to the zero pins would give `u=0`. Every inactive
lower pair has strict finite slack; every upper pair involving `J` is strict
by Section 3; all remaining pairs are fixed. A sufficiently small common
`t>0` is a full-source same-cardinality feasible motion losing contacts and
creating none, contradicting contact minimality. This checks every pair and
uses no integration of a merely first-order flex.

Every vertex of `J` has no endpoint diameter force. The positive endpoint
contact weights therefore give a nonzero row dependence of this pinned
rigidity matrix. Hence

`e>=2|J|+1=2v-7`.

Eppstein's Theorem 2 applies to this connected induced penny graph:

`e<=2v-delta-2`.

Combining the inequalities gives `delta<=5`. Unit graph paths dominate
Euclidean distances, so

`diam H<=5`.                                             (5.1)

This is a finite bound on the actual four-corner hull. It does not come from
the source's large `D`, asymptotic area, or omission of contact isolates.

## 6. Old exterior unit neighbors cannot cover short wall paths

**Lemma 6.1 (proved candidate; source contact geometry).** A source vertex
outside a convex actual bounded face cannot be unit adjacent to two wall
vertices joined by a boundary path of one, two, three, or four unit edges.

For one edge this would be a unit triangle. For two or three edges, joining
the endpoints to the exterior vertex gives a simple unit cycle of length four
or five. Its unit edges cannot cross the old wall. Audit 100's weak-clearance
theorem and triangle-freeness exclude every extra source vertex from its
interior. It has no contact chord: a chord between old wall labels lies inside
the old actual face, while any chord from the exterior vertex to an internal
path label creates a triangle at an endpoint. Thus it is another actual
bounded face, sharing at least two successive edges with the old face.
At an internal shared-path vertex its interior sector is complementary to
the old strictly convex face sector and is reflex. This contradicts strict
convexity of actual bounded faces in a contact-minimal source.

For four path edges the new cycle has six edges. The weak-clearance theorem
again excludes additional interior source vertices. The only possible chord
not already a triangle would join the exterior vertex to the path's middle
vertex; that would unit-connect two old wall vertices only two edges apart,
already excluded by the preceding case. No chord remains. The same shared-path
reflex contradiction applies. `QED`

The chord check is essential. A general unit hexagonal cycle may contain a
unit chord even with no other vertex inside; no universal faciality claim
for arbitrary short cycles is made.

## 7. Only seven arc-count cases survive the four-pin bound

From (5.1) and the strict chord projection bound, `r_i<10/sqrt(3)`, hence
`2<=r_i<=5`. In this range any unequal opposite counts violate (3.1), since
even `5/4>2/sqrt(3)`. Therefore

`(r_1,r_2,r_3,r_4)=(a,b,a,b)`, `2<=a<=b<=5`.

The larger parallelogram diagonal has square at least `A^2+B^2`, giving

`(3/4)(a^2+b^2)<25`.

The exact integer list is

`(2,2), (2,3), (2,4), (2,5), (3,3), (3,4), (4,4)`.

In every case, all `m=2(a+b)` wall points and all chosen distinct inside
neighbors belong to `H`. Oler gives the strict upper bound

`N < (2ab/sqrt(3))+a+b+1`,                            (7.1)

since `area H<=AB<ab` and `per H=2(A+B)<2(a+b)`.

### Case `(2,2)`

The four internal arc vertices are pairwise at boundary distance at most four.
Lemma 6.1 makes their old exterior unit-neighbor sets disjoint. Choose one
neighbor at each; Section 4 places four distinct labels inside `H` at the
endpoint. Thus `N>=8+4=12`, but (7.1) gives `N<8/sqrt(3)+5<10`.

### Cases `(2,b)`, `b=3,4,5`

Take the two short-arc midpoints and all `b-1` internal vertices on one long
arc. Their old exterior neighbor sets are pairwise disjoint, as follows.

Choose the short chord horizontal and write its two-edge deflection as
`alpha<pi/6`, so its old midpoints have outward height `h=sin alpha>0`.
At both long-arc ends, the transition inequality puts the unit-edge direction
strictly between `pi/3+alpha` and `2pi/3-alpha`. Every long-arc unit edge
therefore has upward projection greater than `sqrt(3)/2`.
The opposing short midpoints differ normally by `B sin gamma+2h>3b/4>2`,
so cannot share a unit neighbor. Distances between two selected long-arc
vertices are at most three boundary edges, covered by Lemma 6.1.
For a short midpoint and a long-arc vertex, being at most two steps from its
adjacent corner gives boundary distance at most three. Being at least three
steps away gives normal separation greater than `3sqrt(3)/2>2`.
The same reasoning from the upper end covers its opposite short midpoint.

These are `b+1` disjoint old neighbor sets, giving `N>=3b+5`. For `b=3,4,5`
this is respectively `14,17,20`, all strictly above (7.1).

### Cases `(3,3), (3,4), (4,4)`

Every one of the `m-4` internal arc vertices has its own old exterior neighbor.
To prove distinctness, consider two wall vertices.

- On the same arc, boundary separation one or two is covered by triangle-freeness
  or Lemma 6.1. A subarc of at least three edges has chord greater than
  `3sqrt(3)/2>2`, by its direction interval of width below `pi/3`.
- On opposite arcs, separation normal to the chord lines is greater than
  `(3sqrt(3)/2)(sqrt(3)/2)=9/4>2`.
- On adjacent arcs, let their distances from the common transition be `j,k`.
  If both are at most two, Lemma 6.1 applies to the `j+k<=4` wall path.
  Otherwise one chord from the transition has length above `3sqrt(3)/2`.
  The two outward arc chords make angle at least the parallelogram corner,
  which exceeds `pi/3` and is below `pi`. For any other positive chord length,
  their endpoint distance is at least `sqrt(3)/2` times that longer specified
  chord: use perpendicular projection for angles in `[pi/3,pi/2]`, and the
  cosine law for larger angles. Their distance exceeds `9/4>2`.

Thus no outside unit neighbor can serve two internal vertices. At the endpoint
`N>=m+(m-4)=2m-4`, namely `20,24,28`. The corresponding Oler upper bounds
are `6sqrt(3)+7`, `8sqrt(3)+8`, and `32/sqrt(3)+9`, all strictly smaller.

The seven-case contradiction proves Theorem 1.1. `QED`

## 8. Endpoint implications and limits

The proof attacks the source-realized finite geometry rather than treating
Horn feasibility as realization. At an already full feasible exact-graph
quarter-fold, every large simple bounded face is now pointwise rigid. The
previous pinned-cycle theorem then removes its embedding and isolate-count
premises. Unit rhombi also remain actual bounded faces by their strict disk
cover. All simple bounded facial cycles are consequently retained.

**Corollary 8.1 (proved candidate; precise block scope).** If the contact core
is 2-vertex-connected and has at least one bounded face of degree at least
five, every full feasible quarter-fold has one common sign on all contacts
and is a rigid quarter-turn of the core.

The outer face boundary of a 2-connected plane graph is a simple cycle.
Given points in any two bounded faces, join them by a curve inside that outer
cycle, avoiding the finitely many graph vertices and crossing edges
transversely. All traversed faces are bounded, so this gives a path in the
weak dual on bounded faces and proves it connected.
Retained bounded faces sharing an edge have the same orientation
change. A constant large face has positive orientation change, so every
rhombus in the connected weak dual must also have positive orientation,
forcing its two train signs equal. Shared edges propagate one common sign.
Every core edge belongs to a bounded face, since there is no bridge. This
proves the corollary. The corresponding conclusion for a separately specified
connected weak-dual district containing a large face needs no assumption about
the other contact blocks.

This is an obstruction to a universal quarter-fold construction in the
anchored 2-connected regime, not a contradiction to that regime itself.
A pure quadrilateral district may reverse; bridges and articulation links
are not covered by the common-sign propagation. No global minimum-diameter
source or triangle-free unbounded optimal family has been constructed.

**Next exact theorem:** settle full-source compatible motion in the remaining
pure-rhombic and bridge-linked sign domains, or extract a different finite
motion when the anchored block is quarter-fold rigid. Every source isolate,
inactive lower pair, and inactive upper pair remains part of that obligation.

## 9. Certificate and hostile checks

The companion exact verifier enumerates the seven count cases using integer
inequalities, checks each strict Oler contradiction without floating point,
and checks a rational six-cycle with an interior unit chord as a guardrail
against the false assertion that all short unit cycles are facial.
Run `python3 research/verify_target_c_nonconstant_face_quarter_fold_exclusion_2026_10_10.py`;
saved output is `research/target_c_nonconstant_face_quarter_fold_exclusion_certificate_2026_10_10.json`.
The saved output reproduces byte-for-byte, all relative report links resolve,
the unreviewed artifact metadata/index are generated, and local theorem-state
and PR transaction checks pass. The earlier 22 tooling tests are unchanged.
No canonical dependency or certificate registration is modified.
It does not model source globality, positive endpoint stress, universal pinned
rank, or the analytic no-common-exterior-neighbor argument. Those are proved
above and remain subject to independent audit.

The high-leverage premises to audit are:

1. New endpoint contact positivity follows from contact minimality alone; no
   unjustified `H=H_*` assumption is imported at `Q`.
2. Every incident sign at an internal arc vertex is uniform, making **all**
   of its extra contacts enter the new cycle. Without this, four pins are not
   the complete boundary of the net and the rank count is invalid.
3. The pinned bar-flex straight motion has strict upper slack against every
   full-source label, including isolates, and preserves every other lower pair.
4. The source exterior-neighbor lemma rules out chords before invoking faciality
   of a short cycle. A six-cycle with an interior chord is not a contradiction.
5. Eppstein's diameter is graph-theoretic; the passage to Euclidean `diam H`
   uses unit paths and connectedness of the actual induced contact graph.

No independent audit or canonical promotion is claimed. This theorem, even
if audited, leaves Level I open.
