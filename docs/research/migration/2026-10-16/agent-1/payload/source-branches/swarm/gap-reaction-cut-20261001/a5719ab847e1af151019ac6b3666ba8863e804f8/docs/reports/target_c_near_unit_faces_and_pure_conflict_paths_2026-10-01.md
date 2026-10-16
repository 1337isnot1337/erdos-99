<!-- theorem-state: {"artifact_id":"ART-D746BDE3FD07","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — near-unit blockers lie in contact faces; pure conflicts form source paths

`small joint swaps -> planar near-unit face graph and source conflict paths ->
actual face/owner-return obstruction -> finite competitor if that obstruction
is excluded -> Level I`

**Date:** 2026-10-01  
**Starting shared HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`  
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`  
**Predecessor checkpoint:** `608b7315`  
**State version:** `2026-09-14.audit.51`  
**Mission:** actual source geometry of the lower-only simultaneous-swap clauses.  
**Classification:** proved candidates awaiting promotion; conditional application;
exact regressions. **Level I and C-II remain OPEN.**

## 1. Inputs and source scope

The geometric statements use only a finite unit-separated planar source.
Near-unit planarity/cofaciality was already obtained in PR #598's strict
near-diameter capacity packet; Section 2 records a direct proof of that
baseline. The new refinements here are small-move ownership in all unit
rhombi, the pure-conflict source path theorem, and the O–O outer-face
localization in Section 5.
The joint-translation statements assume disjoint owners `G_i`, displacement
vectors `Delta_i`, and preservation of **every** old unit contact for **every**
binary selection of owners. Assume all nonzero vectors are mutually acute
(`Delta_i dot Delta_j>0`) and have length less than one.

For the C-II application, the unpromoted PR #600 report
`target_c_joint_swap_horn_and_loaded_defects_2026-10-01.md` at `fef16ca7`
was checked directly. Its Theorem 2 puts pure joint conflicts in
`1<|r|<=1+s`, with `|r dot v|=O(1/D)` for a common unit displacement axis
`v`, when `s=O(1/D)` and the open-cell width is `O(1/D)`.
Its Lemma 3 excludes two-sided axial contact vertices at such pairs.
These remain research dependencies, not canonical inputs. The source path
theorem below has a separate direct proof.

The route's finite contact-preserving moves are the unpromoted arbitrary
block transpositions. Canonical contact-minimality/diameter-pair-minimality
only enters when a nonzero lower-feasible pattern would be a competitor.
All contact isolates remain vertices of the source and of the near-unit graph.

## 2. The near-unit graph is planar, with a sharp threshold

For `1<t<sqrt(2)`, join every source pair of length at most `t`. The resulting
straight-line graph `N_t` is plane: distinct edges intersect only at a shared
endpoint, and no source vertex lies inside an edge.

### Proof

If two edges with four distinct endpoints cross properly, their endpoints
form a strictly convex quadrilateral. One quadrilateral angle is at least
`pi/2`. The two sides at that angle are source distances at least one, so
the opposite diagonal has squared length at least two. One of the two
crossing edges is that diagonal, contradicting `t<sqrt(2)`.

A source vertex inside an edge would split an edge shorter than two into
two source distances at least one. Collinear overlap likewise either puts
a source vertex inside an edge, or puts two distinct same-ray neighbors
of a shared endpoint at distance at most `t-1<1`. These are impossible.
∎

The threshold is sharp: both diagonals of the unit square have length
`sqrt(2)` and cross. In particular, a near-unit blocker with length at most
`1+s<sqrt(2)` crosses no actual unit contact. Its open segment is contained
in one face of the actual contact graph.

If also `t<1/(2 sin(pi/7))`, the degree of `N_t` is at most six. For two
neighbors at distances in `[1,t]`, the law of cosines gives angular
separation at least `2 asin(1/(2t))>2pi/7`. To see the radial maximum
precisely, `(a^2+b^2-1)/(2ab)` increases in each of `a,b` on `[1,t]`
when `t^2<2`, so its maximum is attained at `a=b=t`.

There is also a sharp asymmetric threshold: a segment crossing a unit
contact must have length at least `sqrt(3)`. At the two ends of the
crossing segment, the angles subtended by the unit contact are at most
`pi/3`, because both other triangle sides are at least one. The remaining
two quadrilateral angles sum to at least `4pi/3`; one is at least `2pi/3`.
Its two adjacent source sides are at least one, so the opposite segment
has squared length at least three. Equality forces those sides to be unit
and the angle to equal `2pi/3`, giving unit triangles with the short unit
diagonal. A triangle-free source therefore requires strict length greater
than `sqrt(3)` for such a crossing.

## 3. Small simultaneous translations cannot put different owners in a unit rhombus

Let `C` be the actual unit-contact graph. An edge of `C` cannot join two
distinct moving owners. Indeed the four squared-length equations for
relative vectors

\[
r,\quad r+\Delta_i,\quad r-\Delta_j,
\quad r+\Delta_i-\Delta_j
\]

all equal one, and their mixed difference is `-2 Delta_i dot Delta_j`.
Mutual acuteness makes this impossible.

Now consider a bounded four-face of a triangle-free contact graph. Its
boundary is a simple strict unit rhombus. If just one vertex of that
rhombus moves while both its neighboring vertices are fixed, let `a,b`
be its two old unit vectors from those neighbors. They make an angle
strictly between `pi/3` and `2pi/3`. Preservation requires

\[
a\cdot\Delta=b\cdot\Delta=-|\Delta|^2/2.
\]

Thus `Delta` is parallel to `a+b`, and the unique nonzero solution is
`Delta=-(a+b)`. Its length is `2 cos(angle(a,b)/2)>1`, contradicting the
small-move assumption. The same calculation applies if one vertex is
fixed and its two neighbors share one moving owner.

Consequently the only possible ownership patterns around such a face are:

- all four vertices fixed;
- all four vertices in one moving owner;
- two adjacent vertices in one moving owner, with the other two fixed.

For completeness, distinct adjacent owners were excluded by the mixed
difference. Distinct nonadjacent owners would each have two fixed
neighbors and were excluded by the two-contact calculation. A single
owner occupying one, three, or two opposite vertices is excluded by that
same calculation at an appropriate vertex.

There is no additional source point inside the rhombus. In coordinates
`p=sa+tb`, `0<=s,t<=1`, round both coefficients to a vertex. The resulting
vector has coefficients of magnitude at most `1/2` and norm strictly
less than one, since `a,b` are nonparallel unit vectors. An additional
unit-separated source point is therefore impossible.

It follows that **every lower clause joining two distinct moving owners
lies in a nonquadrilateral contact face or in the outer contact face**.
It cannot be a strict-rhombus diagonal, even outside the retained complete
grid. A contact isolate also cannot lie inside a bounded four-face.

This does not exclude unary clauses on a rhombus diagonal: the adjacent
two-vertex pattern can change that diagonal. Section 6 gives an exact
ultra-small regression. The complete-grid local immunity theorem protects
the retained boundary cells, not every source rhombus automatically.

## 4. Pure conflict pairs form a linear forest on actual source vertices

Fix orthonormal axes `u,v`. Form a graph `P` from any source pairs with

\[
1<|r|\le5/4,\qquad |r\cdot v|\le1/8.
\tag{1}
\]

Then **every component of `P` is a path or an isolated vertex**. Orient
each edge by increasing `u` coordinate; every vertex has at most one
incoming and one outgoing edge.

### Proof

An edge in (1) has longitudinal component

\[
|r\cdot u|>\sqrt{1-1/64}>7/8.
\]

Two neighbors of a vertex on the same longitudinal side would have
longitudinal coordinate difference at most `5/4-7/8=3/8`, and transverse
difference at most `1/4`. Their squared distance would be at most

\[
(3/8)^2+(1/4)^2=13/64<1,
\]

contrary to unit separation. Thus there is at most one neighbor on each
side. A finite cycle has a vertex of maximal longitudinal coordinate;
its two cycle neighbors would both be on the negative side. This is
impossible. Degree at most two and no cycles prove the result. ∎

For sufficiently large `D`, every pure joint conflict in the open-cell
small-swap Horn system satisfies (1), by the checked PR #600 slack and
projection estimates. All such pairs together, rather than each conflict
in isolation, therefore form source paths.

Both endpoints are one-sided axial defects or contact isolates by that
packet's two-sided-contact exclusion. If `W` is the set of these actual
exceptional source vertices and `c_P` is the number of nontrivial conflict
path components, then

\[
\boxed{N_{\rm pure}\le |W|-c_P.}
\tag{2}
\]

No exceptional source vertex can carry three pure conflict pairs. An
unbounded isolate or defect population remains possible; (2) is not a
sublinear capacity theorem.

## 5. O–O cuts force all core intergroup clauses into the outer face

There is a stronger conclusion for the actual global O–O train moves.
Assume the positive contact core is connected, as in the canonical
Section-67 source normalization; the separate geometric lemmas above do
not require connectedness.
Each selected train is a **stopped** rhombus train whose two end edges
are incident with the outer face of the full contact graph. Every interior
train edge has a strict rhombus on both sides; every end edge has a strict
rhombus on one side and the outer face on the other. Thus **no selected
cut edge is incident with a bounded nonquadrilateral face**.

Every edge in the boundary walk of such a bounded face is therefore
uncut. Consecutive boundary vertices have identical selected shore
indicators, hence identical slab ownership. The entire boundary walk has
one core owner. This statement uses the global stopped O–O hypothesis
from `target_c_zr_global_train_shear_2026-09-09.md`; it is not true for a
train stopped at a bounded defect face or only at a local grain boundary.

Combine this with Sections 2–3. A near-unit pair joining two distinct
moving **core** owners cannot lie in a bounded four-face, and cannot lie
in a bounded nonquadrilateral face. Therefore

\[
\boxed{\text{every core-to-core intergroup lower clause lies in the outer
contact face}.}
\tag{2a}
\]

In particular every core-to-core pure conflict edge lies there; together
these edges form a linear forest on actual outer-face core vertices.
Core-to-fixed unary pairs in bounded nonquadrilateral faces are also
unchanged and cannot block. The only bounded core-to-core obstruction
left is an unprotected unary rhombus diagonal.

An arbitrary isolate dispatch is an explicit exception to the core
statement. It may assign an isolate to a different owner from the core
boundary of its containing face. The next theorem supplies the compatible
bounded-face assignment; no isolate is removed.

### Bounded-face isolates can be reassigned without any lower or upper blocker

In fact this exception can be removed **inside every bounded contact face**.
Suppose the displacement cloud, including zero, has diameter

\[
s<\min\{D-\sqrt{D^2-1},\sqrt2-1\}.
\tag{2b}
\]

Keep the checked rooted-forest dispatch for exterior isolates, and assign
each contact isolate in a bounded nonquadrilateral face to that face's
constant core owner. Then, for every binary move pattern:

1. all old contacts remain unit;
2. the reassigned isolates create no upper-distance equality or violation;
3. the reassigned isolates create no lower-distance equality or violation.

### Proof

A point inside a bounded contact face is strictly inside the convex hull
of that face's boundary vertices, hence is nonextreme in the full source.
For any other source point `q`, write `z=sum lambda_i p_i` using distinct
boundary vertices. Source unit separation and the variance identity give

\[
|z-q|^2=\sum_i\lambda_i|p_i-q|^2
-\sum_i\lambda_i|p_i-z|^2\le D^2-1.
\tag{2c}
\]

Thus no strict-long pair of length greater than `sqrt(D^2-1)` is incident
with `z`. Changing its ownership cannot break any rooted long forest edge
or introduce an upper exception. Its relative displacement to any source
point is at most `s`, so (2b) keeps every upper constraint strict.

There are no old contacts at `z`. If a new lower equality or violation
were possible with a source point `x`, then `1<|z-x|<=1+s<sqrt(2)`.
Near-unit planarity puts the old open segment `zx` in the same bounded
contact face containing `z`; it cannot cross a contact edge or pass
through a source vertex. Therefore `x` is either a boundary core vertex
of that face or another isolate in that face. Both have been assigned
the same owner as `z`. Their distance is unchanged, a contradiction.
This proves all three assertions. ∎

This extension keeps the whole full-source population, even a large
inactive chamber. It applies only once the actual stopped O–O move and
the small displacement cloud have been proved. It neither produces those
moves in the independent inactive-interface branches nor settles them.

After this reassignment, **every intergroup lower clause on the full
source lies in the outer contact face**, and the only bounded-face lower
clauses left are the unprotected unary rhombus diagonals. Pure joint
conflict edges, including their isolate endpoints, are all outer-face
source paths.

### A precise conditional defect-capacity criterion

Suppose the contact graph is connected and triangle-free. Let `b` be its
outer-face boundary walk length and

\[
Q=\sum_{\text{bounded faces }F,\,\deg F>4}(\deg F-4).
\]

Let `Z` be the number of contact isolates in the full source, and let `W_F`
contain all nonisolated vertices incident with the outer face or a bounded
nonquadrilateral face. Then

\[
|W_F|\le b+5Q.
\tag{3}
\]

Indeed each nonquadrilateral bounded face has length `p>=5`, and
`p<=5(p-4)`. Repeated walk vertices can only lower the distinct-vertex count.

Assume all unary rhombus-diagonal states have been checked to remain strict,
all old diameters/upper constraints have already been handled, and the
joint moves strictly shorten an old diameter for every nonzero pattern.
If `k` owners remain, canonical minimality then implies

\[
\boxed{k\le |W_F|+Z\le b+5Q+Z.}
\tag{4}
\]

To prove this, test each singleton pattern. If it has no bad lower state,
it is a forbidden finite competitor. Hence it has a bad pair with an
endpoint belonging to that owner. Near-unit planarity places the pair in
one contact face. The protected unary assumption and Section 3 exclude
bounded four-faces. Each relatively moving endpoint consequently belongs
to `W_F` or is a contact isolate. Owners are disjoint even after isolate
assignment, so choose one such vertex per owner to obtain (4).

At the rooted source, canonical Section 85 permits a linear `b+Q`, and
the selected shore has only a small linear size. Thus (4) currently
supplies no contradiction. It names the exact extra capacity input needed;
we do not replace `Q` by a smaller induced harmonic-cell defect.

For the actual global stopped O–O moves, improve (4) to

\[
\boxed{k\le b+2Z.}
\tag{5}
\]

Here retain the same hypothesis that every unary rhombus-diagonal state
has been checked to remain strict. For each contact isolate `z`, record
its dispatched moving owner, if any, and the core owner of its containing
face when that face is bounded nonquadrilateral. There are at most `2Z`
owners on this list. A singleton bad pair involving a moving isolate
charges that isolate's dispatched owner. A singleton bad pair whose
moving endpoint is core and whose other endpoint is an isolate in a
bounded face charges that face's core owner. If the pair lies in the
outer face it charges a moving outer-face core vertex instead. Sections
2–3 and (2a) exhaust all other bad pairs. Thus every owner is on the
isolate list or contains an outer-face core vertex, proving (5).

If there are no isolates, all remaining lower clauses after unary-rhombus
protection are supported on the actual outer-face core. With the checked
joint upper-exception deletion of at most `2d_H` owners, a family of `r`
original swaps consequently requires `r<=b+2Z+2d_H`. This still does not
contradict the canonical linear outer-walk budget. It moves the needed
capacity theorem to the actual outer face rather than bounded defects.

Use the bounded-face reassignment to obtain the stronger full-source bound

\[
\boxed{k\le b+Z_{\rm out},\qquad
r\le b+Z_{\rm out}+2d_H,}
\tag{6}
\]

where `Z_out` counts isolates in the **outer contact face**, including
outer pockets; it is not only the population outside the core convex hull.
Every bad singleton now has a relatively moving outer-face source vertex,
and owners are disjoint, proving the first inequality; upper-exception
owner deletion gives the second. Unary rhombus protection remains an
explicit hypothesis. Canonical bounds still allow a linear outer-face
obstruction, so this is not closure.

## 6. Exact regressions: unary rhombi and owner contraction

**A unary rhombus blocker can survive arbitrarily small translation.** Put
`U(t)=((1-t^2)/(1+t^2),2t/(1+t^2))`, `u=(1,0)`,
`v=U(577351/1000000)`, and `u'=U(1/1000000)`. The four source points are
`0,u,v,u+v`. Both diagonals are strictly longer than one. Translate the
adjacent pair `u,u+v` by `Delta=u'-u`, of norm below `1/100000`.
Every old unit side is preserved exactly, but the new diagonal `u'-v`
has length strictly below one. This rejects global rhombus immunity for
unary clauses. The packet is not a positive source KKT or actual
two-boundary global train-swap certificate.

**A source path forest can become a cycle after owner identification.**
Take three well-separated near-unit pairs. Assign their endpoint owners
`(A,B)`, `(B,C)`, `(C,A)`, and translate the owners by distinct small
parallel vectors. For each pair choose its old transverse displacement
to cancel exactly in its joint state; choose its horizontal distance
slightly below one, so `00,10,01` are strict and `11` overlaps. The exact
verifier below gives rational coordinates and margins. The source conflict
graph is a matching, but its owner graph is a triangle. Consequently a
source path theorem alone cannot rule out a Boolean owner return or
conflict. This packet omits source KKT, actual nested train ownership,
and ONE-SIGN active-diameter feasibility; it blocks only the unsupported
identification of a source path forest with an owner forest.

**Leaving a bounded isolate fixed can manufacture a lower obstruction.**
Take the boundary unit-grid points of `[0,4]^2`, add the five points
`(3,j)`, `0<=j<=4`, and the contact isolate `z=(1,2-1/1000)`.
The four right-hand squares form a genuine global O–O train with edges
`(3,j)(4,j)`. Its left shore contains the large bounded nonquadrilateral
face. Rotate the cut unit direction from `u=(1,0)` to
`u'=U(1/1000)` by translating the left core shore by `u-u'`.
All old contacts are preserved. Keeping `z` fixed makes its distance to
the moved `(0,2)` strictly less than one. Assigning `z` to the bounded
face's left owner preserves that distance and every lower constraint.
Its old distances are all below `sqrt(D^2-1)` for `D^2=32`, and its
upper constraints remain strict. The verifier checks the actual contact
cut, all pair distances, and both ownership choices. Active diameters
need not shorten under this single-train shear; the example certifies
the isolate-extension mechanism, not a global competitor.

## 7. Certificate and remaining attack

Run `python3 research/verify_near_unit_face_conflicts_2026_10_01.py`.
It checks actual rhombus contacts, the strict unary overlap after a tiny
contact-preserving translation, the crossing threshold on a unit square,
and the rational source matching whose owner contraction is cyclic.
It also enumerates all 16 binary vertex ownerships of a rational strict
rhombus: each excluded one-/three-/opposite-vertex pattern would require
a displacement of norm greater than one, leaving precisely the four
adjacent-pair patterns and the two constant patterns. The global O–O
face constancy is the analytic cut-edge incidence argument above.
An actual square-strip O–O cut with one bounded-face isolate certifies
the strict lower obstruction under fixed dispatch and its removal under
the proved face-owner reassignment.
The universal plane-graph, face, and path proofs are above; finite checks
do not prove global optimality.

The next source theorem must control outer-face/isolate clauses,
protect the unretained unary rhombi, or constrain the contact paths that
identify distant points in one owner. The pure conflict graph is already
a source linear forest, so a proposed owner-cycle elimination must retain
these identifications. All other C-II branches remain open; no promotion
or Level I settlement is claimed.
