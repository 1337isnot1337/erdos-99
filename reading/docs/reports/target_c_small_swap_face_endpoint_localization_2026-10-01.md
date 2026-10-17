> Generated reading edition · [exact source](../../../docs/reports/target_c_small_swap_face_endpoint_localization_2026-10-01.md) · source SHA-256 `93e70a8ee4cc9db989eef9e1535127d693074e02befa3852c3dcafd4c764bb01`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1D2B6FF468DE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — small-swap contact blockers require a source face or a transverse train end

**Date:** 2026-10-01<br>
**Starting local HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`<br>
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`<br>
**Checkpoint before this attack:** `5782724a812082e6aae7b4edb8df54f603005fd8`<br>
**State version:** `2026-09-14.audit.51`<br>
**Branch/mission:** `swarm/gap-thrackle-20261001`; actual unit-cut compatibility after the geometric common-pivot reduction.<br>
**Classification:** proved candidate awaiting promotion; conditional application to the unpromoted finite swap and complete-train extraction; exact regression.<br>
**Level I:** OPEN; C-I CLOSED; C-II OPEN.<br>
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`.<br>
**Literature:** none imported.

```text
source-face localization and exact opposite-train immunity -> lower-constraint
blockers of an actual finite swap need transverse terminal capacity, bounded-face
capacity, or exterior/isolate capacity -> eliminating those capacities would make
the source-preserving swap a strict competitor or contradict H-minimality ->
Level I only after the other C-II branches are also excluded.
```

The capacity elimination is not asserted. An exact seven-point source below
shows why protection of every rhombus cannot replace that obligation.

## 1. Dependencies and explicit source hypotheses

Canonical inputs for the application are contact-minimal, then diameter-pair-minimal
normalization in [Section 56](../targets/target-c/56-ci-restored-frontier.md),
the nonisolated-core convention in [Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md),
and the actual plane unit-contact graph. The elementary geometric statements below
are rederived for arbitrary unit-separated sources.

Unpromoted inputs are the exact actual-train cutsets, the at-most-one crossing
of two complete trains, and the finite displacement in the
[block-transposition report](target_c_open_cell_block_transposition_2026-10-01.md)
and its [local-immunity dependency](target_c_tb1_swap_grid_local_immunity_2026-10-01.md).
No source global-optimality theorem is imported from a shell regression.

For the train application assume the source is unit-triangle-free. Let the two
bounding actual O–O trains be `tau_p,tau_q`, with coherently oriented
unit contact vectors `u_p,u_q`, whose projective angle is less than `pi/3`.
Their middle slab is `M`. Move every point of `M` by

$$
\Delta=u_q-u_p,\qquad s=|\Delta|<\sqrt2-1.
\tag{1}
$$

Initially keep other points fixed. The exact cutsets make every old contact
unchanged: the lower cut vector changes from `u_p` to `u_q`, and the upper cut
vector from `u_q` to `u_p`. If an isolate-dispatch extension is used, the
same arguments apply to source-pair localization, while the rhombus statements
refer to the unchanged binary motion on the nonisolated core.

All source points are retained. No assertion of unit separation at the new
endpoint is made before the blockers are checked.

## 2. Every new lower-constraint blocker is cofacial in the old source

**Lemma 1.** For any unit-separated planar source and `0<=s<sqrt2-1`, all pairs
of length at most `1+s`, together with the actual unit contacts, form a simple
plane straight-line graph. A previously strict pair whose length becomes at
most one under a binary displacement of amplitude `s` has its old segment
inside the closure of one old contact face.

**Proof.** Crossing edges would be the two diagonals of a convex quadrilateral
whose four sides are at least one. Some interior angle is at least `pi/2`;
the opposite diagonal then has length at least `sqrt2`. This contradicts both
diagonals having length at most `1+s<sqrt2`. A third source vertex cannot lie
on such an edge: the two distances to its endpoints would sum to at least two.
Overlapping distinct edges are excluded by the same argument. The graph is
therefore plane.

The reverse triangle inequality gives old length at most `1+s` for a new
contact or overlap. Its open old segment crosses neither an old contact nor
an old vertex, so is in one connected contact-face region. Isolates can lie in
such a region; cofaciality does not declare them contact vertices. QED.

In particular, an inactive blocker between two corners of a bounded strict
unit rhombus is one of its two diagonals. There is no source isolate in the
interior of such a rhombus: splitting along its shorter diagonal gives two
acute or right triangles with circumradius at most `1/sqrt2`; their vertex
disks cover them. Every interior point is within distance strictly less than
one of a corner. Nor can a different source point lie on one of its unit sides.

## 3. Protection extends beyond the retained complete rectangle

**Theorem 2 (opposite-train immunity).** Suppose a strict rhombus `F` is crossed
by one bounding train, say `tau_p`, and by a complete opposite train `sigma`.
If `sigma` also crosses `tau_q` in any actual strict rhombus of the source,
neither diagonal of `F` becomes a unit contact or overlap after (1).
The two rhombi need not belong to the retained complete rectangle or lie near
each other.

**Proof.** Write the coherently oriented direction of `sigma` as `v`. Before
the move the diagonal squares of `F` are

$$
|u_p\pm v|^2=2\pm2u_p\cdot v>1.
$$

Since the two bounding trains have projective separation less than `pi/3`,
they cannot cross each other in a strict unit rhombus. Thus `F` meets only the
lower boundary, and its two moving corners differ from its two fixed corners
by `u_p`. After the move its diagonal squares are exactly

$$
2\pm2u_q\cdot v.
\tag{2}
$$

At the actual crossing of `sigma` with `tau_q`, source unit separation and
triangle-freeness give `2\pm2u_q\cdot v>1`. Thus both new diagonals are
strictly greater than one. For a face at the upper boundary exchange `p,q`.
QED.

This uses physical train directions and actual rhombus crossings, not a
virtual grid embedding. A face wholly inside or outside the slab does not
change. Every remaining quadrilateral face meets exactly one boundary in two
opposite contact edges, so the argument lists all rhombus possibilities.

## 4. Each unprotected rhombus consumes a terminal occurrence inside the slab

**Theorem 3 (terminal injection).** Suppose an originally strict rhombus
diagonal becomes at most one. Its opposite complete train `sigma` crosses
exactly one bounding train and has exactly one terminal occurrence inside
`M`. Distinct bad rhombi inject into these terminal occurrences.
The direction of `sigma` lies in one of the two projective angular intervals
between the corresponding boundary directions `theta_p+/-pi/3` and
`theta_q+/-pi/3`, modulo `pi`.

**Proof.** Theorem 2 excludes a second boundary crossing. Two complete
trains cross at most once, so `sigma` crosses the first bounding cut once
and the second zero times. Its midpoint path therefore enters the middle
component once and cannot leave it: leaving would require another crossing
of the first cut or a crossing of the second. One of its two ends is in
`M`, the other outside. The physical terminal face occurrence is in the
same component. Bounded defect faces are not traversed by an O–O cut;
outer terminal occurrences are assigned with their physical face side.

A train contributes at most one rhombus at each boundary. It cannot contribute
a bad rhombus at both by Theorem 2. Moreover at most one diagonal of a unit
parallelogram can be at most one, since its two diagonal squares sum to four.
The resulting assignment of a bad rhombus to its unique middle terminal
occurrence is injective.

For the angular statement, the old crossing imposes `|u_p dot v|<1/2`,
whereas (2) imposes `|u_q dot v|>=1/2`. Vary the boundary direction on its
short angular interval: the crossing from the open allowed region to its
complement occurs at one of the two projective boundary directions offset
by `+/-pi/3`. This gives exactly the asserted two intervals. Each has
angular length

$$
|\theta_q-\theta_p|=2\arcsin(s/2).
\tag{3}
$$

Endpoint equality in (2) creates a unit equilateral triangle at the new
endpoint; it does not imply one existed in the source. QED.

Thus the genuinely unprotected quadrilateral witnesses are not arbitrary
grid diagonals. They require a transverse train that stops before reaching
the other bounding train. In particular every opposite train of the retained
complete rectangle is protected globally.

For `k` swaps with disjoint moving core slabs, all the assigned terminal
occurrences are distinct. A complete train has only two terminal occurrences,
so `k` rhombus-blocked swaps need at least `ceil(k/2)` distinct transverse
trains outside the protected full-span family. This is an exact capacity
statement; it is not a contradiction to the available linear train population.

### Theorem 4 — an outer terminal blocker lives in an exterior opposite-shore cap

Now retain a second family of pairwise disjoint proper O–O crosscuts
`B_1,...,B_n`, with `n>=2`, each crossing both bounding `A` trains in actual
strict unit rhombi. Assume `sigma` is the train of a bad rhombus from
Theorem 3. Then `sigma` crosses none of the `B_j`. If its middle terminal
occurrence is on the outer face, `sigma` lies wholly in one of the two
exterior `B` gaps. In particular an O–O bad train and its bad rhombus
are exterior to the selected opposite-shore strip. If its bad rhombus
is in an internal `B` gap, its middle terminal occurrence must be on a
bounded nonquadrilateral face.

**Proof.** Three directions cannot have pairwise projective distance strictly
greater than `pi/3`: the three circular gaps on the projective circle have
sum `pi`. A pair of complete trains that crosses in a strict unit rhombus
has projective direction distance strictly greater than `pi/3`. Since
`sigma` crosses one bounding `A` train and each `B_j` crosses that same
train, `sigma` cannot also cross any `B_j`. This is the geometric
triangle-free train-crossing property, applied to the actual directions.

The midpoint path of `sigma` is therefore contained in one complement
region of the `B` cuts. An internal `B` gap has two outer-boundary arcs,
between successive `B` endpoint occurrences. The slab between two `A`
crosscuts that cross both walls of that `B` gap contains neither outer arc.
To see this directly, the four cuts `A_p,A_q,B_j,B_(j+1)` have, by one-time
crossing and within-shore disjointness, the cyclic endpoint pattern

```
A_p+, A_q+, B_j+, B_(j+1)+, A_q-, A_p-, B_(j+1)-, B_j-.
```

Reverse a shore's indexing if needed. The two internal `A` boundary arcs
are between the two `A` endpoints in their respective blocks; the two
internal `B` boundary arcs are between the two `B` endpoints. These arcs
are disjoint. Thus the intersection of the `A` slab with an internal
`B` gap has no outer-face boundary occurrence.

Theorem 3 places one terminal occurrence of `sigma` in that intersection.
It cannot be outer. A complete stopped train ends only on the outer face
or on a bounded nonquadrilateral face; hence it is a bounded-face end.
Conversely an outer middle end forces `sigma` into an exterior `B` gap,
which also contains its unique bad crossing with the `A` boundary.
An O–O train has no bounded end, giving the asserted special case. QED.

Repeated outer-face vertices are resolved as physical occurrences in a
small regular neighborhood before using the endpoint order. This argument
does not identify distinct occurrences of a repeated vertex or the whole
contact outer walk with the source hull.

For one swap, the number of bad rhombi in internal opposite-shore gaps is
therefore at most the bounded train-end capacity `Q+4f`. For disjoint moving
slabs their assigned bounded occurrences are distinct, so the same global
bound applies to the entire family, without a factor equal to the number
of swaps. This does not bound the two exterior `B` caps.

There is a second consequence for all outer-face witnesses. If both endpoints
are in the core and the pair changes under the swap, its moving endpoint is
an outer-boundary vertex of the `A` slab. The displayed four-block order
places that endpoint in an exterior `B` cap. Thus **every outer-face
core–core blocker has an anchor in one of the exterior opposite-shore caps**.
This does not place both endpoints there. A dispatched isolate has no
canonical boundary-layer identification and remains a separate possibility.

## 5. Bounded nonquadrilateral witnesses have a separate exact budget

Assume the nonisolated contact core is connected. For each bounded
nonquadrilateral face let `d_F>=5` be its occurrence-counted boundary degree,
and let `z_F` be the number of source isolates in its open region. Let
`l_F` be the number of previously strict pairs of length at most `1+s`
whose old open segments lie in that face. Then

$$
\boxed{l_F\le d_F-3+3z_F.}
\tag{4}
$$

To prove this, insert all these edges in the face. Lemma 1 makes them
noncrossing. Adding `l_F` edges can reduce the number of connected components
by at most `z_F`, since the old core is connected. Euler therefore gives at
least `l_F-z_F` extra bounded regions. The original bounded region is
replaced by at least `l_F-z_F+1` regions, all with boundary degree at least
three. The sum of their degrees is `d_F+2l_F`, including bridge and
articulation occurrences. Hence

$$
d_F+2l_F\ge3(l_F-z_F+1),
$$

which is (4). If `l_F<z_F`, (4) already follows from `d_F>=5`; the same
inequality still applies. A component disjoint from the old boundary must
contain a source isolate, so no hidden component loss was omitted.

Writing the **global** exceptional-face currency

$$
Q=\sum_F(d_F-4),\qquad f=\#\{F\},\qquad z_{\rm bd}=\sum_Fz_F,
$$

gives

$$
\boxed{\sum_Fl_F\le Q+f+3z_{\rm bd}\le2Q+3z_{\rm bd}.}
\tag{5}
$$

This does not count witnesses in the unbounded face. It also does not replace
global `Q` by the sum `Q_D` of harmonic-cell defects from the rooted-threshold
report; an additional comparison theorem would be required. In particular,
the near-root statement `Q_D=o(D)` alone supplies no deletion of (5).

A pair changes under at most two of a family of disjoint binary moving sets.
For isolate-dispatched swaps the same conclusion holds when one fixed root
assignment is used for all swaps. Thus bounded nonquadrilateral blockers can
explain at most `2(Q+f+3z_bd)` such failed attempts. All outer-face blockers
and all the term `3z_bd` remain explicit.

Combining this with Theorem 4 gives a finite, source-preserving escape-or-cap
reduction. Suppose `k` disjoint binary swaps have old-contact preservation,
weak decrease of every old diameter with at least one strict decrease each,
and strictly inactive upper constraints at their endpoints. Keep a fixed
isolate dispatch if one is used. Unless some swap is lower-feasible with no
new contact, every failed swap has a witness. At most

$$
\boxed{(Q+4f)+2(Q+f+3z_{\rm bd})
=3Q+6f+6z_{\rm bd}\le9Q+6z_{\rm bd}}
\tag{8}
$$

of the attempts can be explained by an internal-strip rhombus or bounded
nonquadrilateral face. Every remaining attempt has either an outer-end
rhombus wholly in an exterior `B` cap, an outer-face core–core witness
anchored there, or an outer-face isolate witness. A lower-feasible endpoint
with no new contacts contradicts the canonical global/minimal-pair selection
by the usual finite fork; a new contact is retained as a witness even when
the endpoint is feasible. No inference is drawn merely from a triangle at
that different endpoint.

This estimate does not import a near-diameter gap or an isolate extension
without proof: strict inactive upper feasibility is an explicit hypothesis.
The independently developed rooted dispatch of PR #600 can be audited and
composed to replace that hypothesis by at most `2d_H` further explained
attempts. No such composition is needed for (8), and it is not canonical here.

## 6. Rejected strengthening: every actual rhombus is immune

The following exact seven-point source has actual unit-contact cutsets and two
strict near-triangular rhombi, yet a boundary rhombus diagonal becomes less
than one under the finite contact-preserving transposition.

Let `t` be rational with `0<t<=1/100`, put `eta=2 atan(t)`, and define

$$
u=(1,0),\qquad w=R_{2\eta}u,\qquad
v=R_\eta(1/2,\sqrt3/2),\qquad
a=R_{3\eta}(1/2,\sqrt3/2).
$$

All coordinates are in `Q(sqrt3)`, using
`cos eta=(1-t^2)/(1+t^2)` and `sin eta=2t/(1+t^2)`.
The labeled source is

$$
\begin{array}{c|ccccccc}
\text{label}&0&1&2&3&4&5&6\\\hline
\text{point}&0&u&v&u+v&u+v+w&u+v+a&u+v+w+a.
\end{array}
\tag{6}
$$

Its only unit contacts are

```
01, 02, 13, 23; 34, 35, 46, 56.
```

They form two strict rhombi meeting at vertex `3`. The first has angle
`pi/3+eta` between `u,v`, the second the same angle between `w,a`.
Their two short diagonals are strictly greater than one. Every other
noncontact difference is a sum of at least two of `u,v,w,a`, all lying
in a cone of aperture less than `pi/2`; its length is greater than one.
Thus (6) is unit-separated and its actual contact graph is triangle-free.

The actual complete O–O trains of directions `u,w` are the contact pairs
`{01,23}` and `{34,56}`. Their midpoint crosscuts give layers

```
L={0,2}, M={1,3,5}, R={4,6}.
```

Move `M` by `Delta=w-u`. Both old cutsets exchange direction, and all
eight actual contacts remain unit. But

$$
|p'_1-p'_2|=|w-v|
=2\sin((\pi/3-\eta)/2)<1,
\tag{7}
$$

where the original `12` length was `2 sin((pi/3+eta)/2)>1`.
The opposite `v`-train crosses only the lower bounding train and ends in
`M`, exactly as required by Theorem 3. The second rhombus stays feasible:
its new short diagonal is `|u-a|=2 sin((pi/3+3eta)/2)>1`.

The amplitude `2 sin eta` tends to zero. All four projective directions
fall into two narrow phase windows near `0,pi/3`. This regression therefore
survives actual contact preservation, near-triangular rhombi, exact O–O cuts,
and arbitrarily small phase separation. It does not satisfy full-support
source KKT equilibrium, local trapping, the retained complete rectangle,
or global optimality. Its old diameter does not provide the required
strictly shortening moving-diameter condition. It rejects only the claimed
automatic immunity of all source rhombi, not the minimality fork or Level I.

## 7. Computation and hostile checks

[verify_target_c_swap_face_endpoints_2026_10_01.py](../../../research/verify_target_c_swap_face_endpoints_2026_10_01.py)
uses exact `Q(sqrt3)` arithmetic to certify (6)--(7), the complete original
contact graph, both actual cutsets, all old contact lengths at the endpoint,
and the unprotected/remaining-rhombus diagonal comparison for 100 rational
parameters. No numerical tolerance is used. The universal proofs above do
not depend on the finite parameter sample.

The test omits global optimality, vertex equilibrium, actual diameter
decrease, a quadratic-size core, and fixed-star full-span diameter witnesses.
It is an exact geometric regression and does not prove a source competitor.

The following tempting upgrades were attacked and rejected or kept conditional:

| Claim | Classification | Decisive issue |
| --- | --- | --- |
| All near-unit blockers are old-face diagonals | Rejected as stated | Isolates may lie inside exceptional or outer faces |
| Every actual rhombus survives the swap | Rejected | Exact seven-point source (6) |
| A full-span opposite train protects all its boundary crossings | Proved candidate | Exact replacement directions (2) |
| Bad rhombi inject into middle terminal occurrences | Proved candidate | One-crossing property plus opposite-train immunity |
| Root harmonic defects absorb all global exceptional faces | Unproved | `Q_D` and global `Q` are different quantities |
| Linear failed swaps exceed endpoint capacity | Rejected counting shortcut | The available transverse train population is also linear |
| A new equilateral triangle at a feasible endpoint proves every source minimizer triangular | Rejected | Does not preserve the universal source quantifier |

## 8. Frontier effect and next obligation

The ONE-SIGN lower-distance obstruction now has a source-level trichotomy:

1. an unprotected rhombus, charged injectively to a transverse train end in
   the moving slab in the narrow arcs (3);
2. a bounded nonquadrilateral face, with the exact budget (5);
3. the unbounded face, including any dispatched isolate there.

With a retained complete opposite shore, case 1 splits further: a bad rhombus
inside that shore's strip consumes a bounded defect-face end, while every
outer-end bad rhombus lies in its two exterior caps. This is a genuine
source-embedding restriction, beyond geometric diameter incidence and the
local retained-grid immunity. It still leaves a macroscopic exterior
capacity and the bounded-face terms.

For disjoint attempts, (8) bounds all explained interior attempts at once.
The finite checker also verifies the perimeter-only pair of layer labels
on the outer boundary of a complete pseudogrid. This explains the cap
restriction without identifying the outer contact walk with a convex hull.

The repair must exclude or release these obstructions together while using
actual positive equilibrium and the retained source embedding. For example,
a bound on terminal capacity in the narrow transverse arcs of all disjoint
ONE-SIGN slabs, strictly below the number of attempts after (5), would force
a fully lower-feasible swap. Existing geometry does not supply that bound:
the seven-point source demonstrates how a terminal witness can occur.

Other branches remain: exact phase, TWO-SIGN, split-star O–O, inactive
interfaces, macroscopic inactive containers/exterior caps, and sources
outside the fixed-star extraction. No canonical state, dependency graph,
or prompt is changed. Promotion recommendation: **unreviewed**, pending
independent audit of the new source-face and terminal proofs.

## 9. Next attack: exact face dispatch removes every nonquadrilateral lower blocker

The budget (5) is valid for an arbitrary supplied binary isolate extension.
It can be replaced by a stronger constructive statement for the actual
O–O slab cuts.

**Theorem 5 (bounded-face isolate dispatch).** Let the nonisolated core be
connected, and let the binary core motion be the actual slab transposition
above. Every bounded nonquadrilateral contact face has one common core
motion label on all boundary occurrences. Assign every source isolate in
its open region that same label. Then:

1. no previously strict source pair cofacial in a bounded nonquadrilateral
   face becomes a contact or overlap;
2. these assigned isolates introduce no upper-distance obstruction when
   `s<D-sqrt(D^2-1)`;
3. consequently every remaining lower blocker is an unprotected rhombus
   diagonal or is cofacial in the unbounded contact face.

**Proof.** An edge on a complete O–O train cannot border a bounded
nonquadrilateral face: it would be a physical train end on that face,
contrary to O–O. Neither bounding contact cut therefore contains any
edge occurrence of a bounded nonquadrilateral face. Its connected boundary
walk has one fixed layer and hence one common binary label. Articulation
and bridge repetitions do not change this conclusion. Assigning all its
interior isolates that label makes all pairs of its boundary vertices and
isolates receive exactly the same translation. By Lemma 1, every candidate
lower blocker in this face is one of those pairs, so its distance is
unchanged. Isolates in different contact-face regions cannot form a
near-unit pair whose open segment crosses the intervening contact edges.

Every point in an open bounded contact-face region lies inside the source
hull and is nonextreme. For any nonextreme source point `z`, write
`z=sum lambda_i a_i`, with `a_i` different source points, nonnegative
coefficients summing to one. For every other source point `p`, variance
and unit separation give

$$
|z-p|^2
=\sum_i\lambda_i|a_i-p|^2-\sum_i\lambda_i|a_i-z|^2
\le D^2-1.
\tag{9}
$$

Since relative binary displacement is at most `s`, all such pairs remain
strictly shorter than `D` under the stated bound. Reassigning these isolates
does not affect any old contact, any actual diameter, or a long-pair
rooted dispatch: a nonextreme point has no pair longer than
`sqrt(D^2-1)`. Exterior isolates retain whatever upper-feasible assignment
was supplied. Finally every bounded four-face is a strict rhombus, with
no interior source isolate, so the face list is exhaustive. QED.

Thus the earlier term `2(Q+f+3z_bd)` is unnecessary after this concrete
dispatch. With a complete opposite shore, at most `Q+4f` disjoint attempts
can have internal-strip lower blockers, all of them rhombi charged to
bounded terminal occurrences. Every other lower blocker has the exterior
cap localization of Theorem 4, or involves an exterior isolate. Strict
upper feasibility remains supplied separately, with the new assignment
provably preserving it.

This does not derive `Q=o(D)` from `Q_D=o(D)`. It also does not remove
the bounded-ended transverse-train obstruction or exterior-cap witnesses.
The repaired obligation is now a terminal/cap release, rather than a
generic bounded-face near-contact count.

### An exact actual-contact example where the dispatch repairs an overlap

The checker includes a square-grid ring with a bounded sixteen-edge contact
face. Use the grid vertices `(i,j)`, `0<=i,j<=6`, except the nine points
with `2<=i,j<=4`. Replace column 6 by `(5+w_x,j+w_y)`, where
`w=R_eta(1,0)` and `eta=2 atan(t)`. Add the contact isolate

$$
z=(1+\sqrt3/2+t/10,\ 7/2),\qquad 0<t\le1/1000.
\tag{10}
$$

The resulting source has forty core points, sixty actual unit contacts,
and one isolate in the bounded central face. The complete O–O trains
between columns `0,1` and `5,6` have directions `u=(1,0),w`, respectively.
Move columns `1,...,5` by `w-u`. If `z` stays fixed, it overlaps the moved
point originally at `(1,3)`. If `z` receives that same translation, every
source pair remains unit-separated and all sixty old contacts remain unit.
All corner diameters in this example stay fixed; no strict moving-diameter
improvement or global-optimality theorem is claimed. The packet certifies
the need and effectiveness of the geometric face assignment.

## 10. Push to the rooted carrier: global defect capacity is unnecessary inside the grid

**Theorem 6 (carrier-local terminal charge).** Suppose all selected complete
global `A` and `B` trains lie in one induced harmonic contact graph `J`,
and each is also a proper O–O crosscut of its local outer-face disk. Assume
every strict rhombus traversed by a selected global `A` train is a rhombus
of `J`. Denote the local nonquadrilateral boundary degree excess and face
count by `Q_J,f_J`. Across disjoint `A` swap slabs, all bad rhombi in
internal `B` gaps inject into the **local** bounded terminal occurrences
of `J`. Their total count is at most

$$
\boxed{Q_J+4f_J\le5Q_J.}
\tag{11}
$$

**Proof.** A bad rhombus belongs to `J` by the hypothesis on the bounding
`A` train. Follow its opposite train inside the middle slab in the
direction toward its unique global middle end. The global train crosses
none of the selected `B` cuts by Theorem 4; it cannot cross either
bounding `A` cut again. Its local segment remains in the intersection
of the `A` slab and its internal `B` gap until it terminates as a train
segment of `J`.

The selected curves are the same proper crosscuts in the local disk, so
the four-block endpoint argument in Theorem 4 applies to the local outer
boundary as well. That intersection has no local outer-boundary
occurrence. The first local terminal occurrence therefore borders a
local bounded nonquadrilateral face. A global continuation through that
face into another harmonic cell does not erase the local terminal
occurrence used for the charge. Each bad rhombus uses its unique local
opposite-train segment; this segment cannot supply another bad crossing
for the same two boundaries. Across disjoint middle slabs the chosen
local terminal occurrences have distinct fixed slab labels. The assignment
is injective. The sum of local face degrees is `Q_J+4f_J`, proving (11).
QED.

The selected local/global compatibility is an explicit hypothesis, not a
consequence of arbitrary complete geometric crosscuts. The October 1
[O–O/interface extraction](target_c_endpoint_oo_interface_trichotomy_2026-10-01.md)
deletes trains contaminated by missing harmonic rhombi before obtaining
the relevant global stopped trains; its carrier-label constancy and
physical local endpoint assertions are the unpromoted route inputs
required here. Without that contamination deletion, (11) cannot simply
replace the global count.

At the exact rooted endpoint the same extraction supplies `Q_J=o(D)`.
After Theorem 5's face assignment, interior isolates and bounded
nonquadrilateral source pairs introduce no lower blocker. Hence a linear
family of disjoint, upper-feasible ONE-SIGN attempts has, except for
`o(D)` attempts, only an exterior-cap rhombus, an exterior-anchored
core pair on the outer face, or an exterior isolate as its lower
obstruction. This comparison uses local `Q_J` exactly where local
terminals have been proved; it does not silently equate it with global
`Q`.

For a fully quantified statement, if `k_D>=cD` such attempts are supplied
and no finite fork succeeds, at least `k_D-5Q_J` attempts need one of
those exterior obstructions. Their rhombus terminal occurrences are
distinct; an actual previously strict pair can account for at most two
attempts under a fixed binary assignment on all vertices. Thus a linear
nonlocal exterior population survives. This is a reduction, not an
elimination: the selected opposite-shore caps can be macroscopic, and
the report proves no sublinear cap capacity.

The immediate continuing attack is a finite correction of this exterior
population, preserving the original source cardinality and all active
diameters, or a phase-coherent cap-capacity contradiction. The explicit
seven-point and forty-one-point packets prevent replacing this by
automatic lower feasibility or by silently fixing all isolates.
