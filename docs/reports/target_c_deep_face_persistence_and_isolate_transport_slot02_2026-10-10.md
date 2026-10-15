<!-- theorem-state: {"artifact_id":"ART-1C2B1B422853","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: face persistence, loaded intrusion, and isolate deficit

**Date:** 2026-10-10. **Worker:** 02. **Goal:** full Level I resolution, still active.
**Base main:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.
**State:** `2026-10-10.audit.234`.
**Previous worker checkpoint:** `bf706ca87f01f6dfe2971a80ec034a5c8d356f02`.
**Branch / PR:** `research/sol61-slot02-20261010-integrated-fold`, [PR #948](../publication/provenance.md#source-records).
**Classification:** proved candidates awaiting independent audit; unreviewed,
noncanonical. No theorem authority or promotion transaction is changed.
**Prompt:** [current Target C continuation](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md).
**External literature:** none imported. **Computation:** exact finite scope checks.

## Level I and exact closure chain

**LEVEL I: STILL OPEN.** A universal feasible endpoint is not constructed.

```text
actual contact component intrudes into a rigid image of an old face
 -> that component contains an old loaded diameter endpoint
 -> enough interior isolate capacity gives an explicit whole-source replacement
 -> same contacts, no new diameter, at least one old diameter removed
 -> contradiction to canonical lexicographic minimality
```

For an empty old face, the required isolate capacity is zero, so intrusion is
excluded unconditionally. For an occupied face, intrusion forces an exact
one-isolate population/capacity deficit. No outside slot is assumed.

A second chain supplies source-level embedding control:

```text
intruding component + endpoint unit packing
 -> at most C_m component vertices
 -> an old loaded label within old contact distance C_m of the face
 -> every face farther from old loads persists automatically
```

These are geometric statements about the original labeled source and an actual
unit-separated placement of its contact core. Isolates remain part of the full
source throughout every replacement argument. Component bounds below concern
only positive-contact core labels and do not bound the total isolate population.

## 1. Hypotheses and dependencies

Use the canonical triangle-free global source `A`, selected first for minimum
contact count and then minimum actual-diameter-pair count, in the `D>=9` C-II
regime. Let `G` be its connected nonisolated positive-contact core, `B` all its
actual loaded diameter endpoints, and `K=conv A`. The canonical relative-interior
stress has positive weights on every core contact; at each vertex outside `B`,
the source coordinates are positive-weight harmonic in its contact neighbors.

Dependencies:

- `C-ZRF` / the canonical normalization, and `C-RHOMBUS-POP`, including the
  positive harmonic maximum principle in
  [Section 67.2](../targets/target-c/67-rhombus-population-transport-audit.md).
  The harmonic equations are used only on the nonisolated core.
- Finite Oler inequality, [shared theory 03, Lemma 21.1](../theory/03-oler-shell.md):
  `N<=2 area(H)/sqrt(3)+per(H)/2+1` for a convex container and a unit-separated set.
  Its population bound is used as an upper bound, never as insertion capacity.
- Canonical local trapping, [shared theory 01, Theorem 6.1](../theory/01-local-structure.md),
  and the bounded-face strictness argument already recorded in shared theory 03,
  Lemma 22.1. Strict convexity is an existing local-structure consequence, not
  counted as a new discovery below.
- `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION` and the boundary-local
  `C-QUARTER-FOLD-MINIMUM-FACE-SIZE`,
  [Audit.83](../audits/target_c_face_coupled_quarter_fold_independent_audit_2026-10-07.md)
  and [Audit.229](../audits/target_c_minimum_face_size_local_endpoint_independent_audit_2026-10-09.md).
- `C-UNIT-WALL-PACKET-POPULATION-BOUND` for the non-intruded population estimate;
  `C-FULL-SOURCE-ISOLATE-NORMALIZATION` for the optional replacement-diameter
  corollary. Neither is needed for the local replacement proof itself.
- `C-SHORT-WALL-ZERO-CAPACITY`,
  [independent audit](../audits/target_c_short_unit_wall_zero_capacity_promotion_audit_2026-10-05.md),
  for the absence of interior isolates in five- and six-faces in Section 7.

The earlier worker [face-obstruction report](target_c_quarter_fold_face_obstructions_slot02_2026-10-10.md)
is an unreviewed candidate. The new strictness and persistence arguments are
proved below rather than imported as canonical statements.

## 2. Strict convexity strengthens the eight-face exclusion

**Lemma 2.1 (existing local-structure consequence, reconstructed).** Every simple bounded actual contact face of a
contact-minimal triangle-free global source is strictly convex.

**Proof.** A reflex vertex is nonextreme in the source hull. At a straight
boundary vertex `v`, its two unit face neighbors have `v` as their midpoint, so
`v` is also nonextreme. Every actual diameter endpoint is strictly exposed:
if `|v-z|=D`, the functional with direction `(v-z)/D` is uniquely maximized at
`v`, by Cauchy--Schwarz and the diameter upper bound. Thus either kind of vertex
has strict upper slack against every other source label.

At a reflex or straight actual face vertex, all contact vectors lie in the
complement of its empty face sector, a closed cone of width at most `pi`.
Choose a unit vector `d` opposite its bisector. Then `d dot(w-v)<=0` for every
unit neighbor `w`, and for every positive `epsilon`,

`|v+epsilon d-w|^2=1-2epsilon d dot(w-v)+epsilon^2>1`.

This also opens tangent contacts at a straight vertex, where the linear term
vanishes. Finiteness supplies one positive `epsilon` smaller than every incident
strict lower and upper margin. All noncontact pairs involving `v` stay above one;
all upper pairs involving it stay strictly below `D`; all other pairs are
unchanged. Every source label remains, no contact is created, and contacts are
lost. The source stays triangle-free. Global optimality or contact minimality
is contradicted. Degenerate reverse turns would repeat a vertex on two successive
unit edges and are impossible by source separation. `QED`

**Corollary 2.2 (proved candidate).** Every old convex actual eight-face has
constant sign in any full-source exact-contact-graph quarter-fold endpoint of
diameter at most `D`.

**Proof.** The previous report's Theorem 5.1 proves that a nonconstant such
eight-face must have four straight two-edge arcs: the strict transformed-hull
cover makes any bowed folded cycle an actual nonconvex face, which is excluded
by the finite reflex release. Lemma 2.1 forbids the required straight vertices
in the original source. Thus the nonconstant case is impossible. `QED`

This removes the straight-eight-face option from the previous canonical-source
handoff. The straight finite regression remains valid for nonglobal sources.

## 3. Every component outside a convex face sees an old load

Let `F` be any simple convex actual bounded contact face, with `m` boundary
labels `W`. Every component of `G-W` lies geometrically outside `F` in the old
embedding. There are no nonconsecutive unit chords of `W`.

**Lemma 3.1 (proved candidate).** Every component `T` of `G-W` contains a label
in `B`.

**Proof.** Suppose `T` contains no loaded label. Its coordinates are harmonic
with positive contact weights. All its neighbors outside `T` lie in `W`, and
at least one such edge exists because `G` is connected. For any linear
functional, a value greater than all boundary values cannot attain its maximum
inside `T`: the positive weighted average at a maximizing vertex forces every
neighbor to attain that same maximum, and propagation along the connected
component reaches a boundary edge. This is a contradiction. Applying this to
every supporting functional gives `p(T) subset conv p(W)=F`.

A nonincident source label cannot lie on a unit boundary edge, and a graph
vertex cannot lie in the interior of an actual old face. This contradicts the
location of `T`. `QED`

The argument uses old positive equilibrium, not a claim that old loads remain
loads at a new placement.

## 4. Automatic persistence of deep faces

Define the finite integer

`C_m=floor(m^2/(2*pi*sqrt(3))-m/2+1)`.

For example `C_8=2`, `C_10=5`, `C_12=8`, and `C_18=21`.

**Theorem 4.1 (proved candidate).** Let `Q` be any planar placement of the
entire core, unit-separated with exactly the old contact graph. No endpoint
diameter condition is required. If the boundary cycle `W` of `F` is not an
actual bounded face at `Q`, there is a component `T` of `G-W` entirely inside
that new cycle and a label `b in T intersect B` such that

`|T|<=C_m`, `dist_G(b,W)<=|T|`, and `dist(p_b,p(W))<=C_m`.

Consequently, if `dist(p(W),p(B))>C_m`, the old cycle persists automatically
as an actual bounded face at every such `Q`.

**Proof.** A unit-separated straight-line contact drawing is plane: crossing
unit edges would have two endpoints strictly within one, by choosing endpoints
at most `1/2` from the crossing. Thus the new cycle is simple. No new contact
chord is possible because the contact graph is exact. If the cycle is nonfacial,
its interior contains a core vertex. A component of `G-W` containing that vertex
lies wholly inside the cycle, since its edges cannot cross the boundary.

Let `H` be the convex hull of the new boundary labels. Its perimeter is at most
the boundary length `m`, and the planar isoperimetric inequality gives
`area(H)<=m^2/(4*pi)`. The `m` boundary labels and all `|T|` labels lie in `H`
and are unit-separated. Oler therefore gives

`m+|T|<=m^2/(2*pi*sqrt(3))+m/2+1`,

proving the integer bound. Lemma 3.1 supplies `b in T intersect B`. A shortest
graph path from `b` to `W` inside `T` until its last edge uses at most `|T|`
unit edges. Evaluate that same old contact path in the original source to
obtain the Euclidean distance bound. `QED`

Only the endpoint core population of an intruding component is bounded; no
contact isolate is removed or put into that component count.

**Corollary 4.2.** In a globally feasible full-source exact-graph quarter-fold,
every nonconstant old face of degree `m>=5` has an old loaded label at distance
at most `C_m` from its boundary.

**Proof.** The canonical local classification gives four transition arcs of
at least two edges. At transitions the folded turn determinant is negative.
At every internal arc vertex the old strict convexity from Lemma 2.1 and equal
signs give a positive folded determinant. Thus the folded cycle is nonconvex.
If it remained an actual bounded face, the new full placement, itself a
contact-minimal triangle-free global source, would violate Lemma 2.1. It must
be nonfacial, so Theorem 4.1 applies. `QED`

This controls the embedding hypothesis of Audit.227 on deep faces using actual
source geometry. It does not require or prove a uniformly vanishing large-face
tail.

## 5. A finite local replacement and a strict isolate deficit

**Theorem 5.1 (proved candidate; explicit full-source endpoint).** Let the new
core placement `Q` be as in Theorem 4.1. Suppose its boundary point set `Q(W)`
is the image of `p(W)` under one Euclidean isometry `R`, and let `F'=R(F)` be
the cycle interior. The boundary labels may be permuted by `R`. Let `z` count
all old source isolates in `int F`.

If a component `T` of `G-W` lies in `int F'`, then `z>=1` and

`Pack_1({x in int F': dist(x,Q(W) union Q(T))>1}) <= z-1`.

Here packet pairs need only be at least one; wall and component guards are
strict. In particular, if `z=0`, the cycle is necessarily still an actual
bounded face. If a full exact-graph lower-feasible placement is supplied, its
isolate population inside `F'` is at most `z-1` whenever such an intrusion occurs.
None of these assertions requires a diameter bound on `Q`.

**Proof.** Assume a guarded packet of `z` sites exists; for `z=0`, use the empty
packet. A sufficiently small dilation opens any packet-internal unit pairs
while preserving strict wall/component guards and containment in the convex
open region. This follows from finiteness and continuity after choosing an
interior dilation center. Now pull `Q(T)` and the strict packet back by `R^-1`
into `int F`.

Delete all `|T|` old labels of `T` and all `z` old interior isolates. Insert the
pulled-back `|T|+z` points with these labels. Every other original source label,
including every exterior isolate, remains fixed. The following is the complete
pair and count ledger.

1. **Internal / wall lower pairs:** isometry preserves all component-internal
   distances, the number of component-to-wall contacts, and strict packet guards.
   If wall labels are permuted, the contact labels may change but the number
   of contacts is the same. Packet labels create no contacts.
2. **Every retained exterior lower pair:** the segment from any inserted point
   `x` to a retained nonwall point outside `F` crosses a unit wall edge `cd` at
   `w=(1-t)c+td`. Both points are at least one from `c,d`, so
   `|x-w|^2,|a-w|^2 >= 1-t(1-t)>=3/4`. The segment is therefore at least
   `sqrt(3)>1`. A vertex crossing gives the same or stronger bound. There is
   no old retained interior label: all old interior isolates were deleted,
   and an actual old face has no core vertex in its interior.
3. **All inserted upper pairs:** every inserted point is in `int F subset int K`.
   An interior point of a convex diameter-`D` container has distance strictly
   below `D` from every point of that container. For example, express it as a
   convex combination of hull vertices with positive variance and use the
   weighted-square identity. Retained labels and the other inserted labels
   are all in `K`. Hence every inserted-involving upper pair is strict; all
   retained-retained pairs are unchanged. No formerly inactive pair becomes
   a diameter.
4. **Cardinality / contacts / triangles:** the point count is unchanged.
   Because `T` is a component of `G-W`, no old contact joins `T` to a retained
   nonwall label. Component-internal and wall-contact counts are preserved;
   deleted and inserted isolates have no contacts. Total contact count is
   exactly the old count. Inside plus wall, the contact graph is geometrically
   isomorphic to the corresponding subgraph of `Q`, hence triangle-free.
   An inserted point has no retained nonwall neighbor, so no triangle can use
   both an inserted and a retained exterior point. All exterior triangles are
   absent in the original source.
5. **Actual diameter loss:** Lemma 3.1 puts an old loaded label `b` in `T`.
   All its new distances are strictly below `D`, so at least one actual old
   diameter pair is removed. No new diameter pair was created.

This is a same-cardinality triangle-free full-source placement of diameter at
most `D`, with the same contact count and strictly fewer diameter pairs. Global
optimality or the secondary lexicographic minimum is contradicted. Thus a
packet of `z` sites cannot exist. Since all capacities are finite integers,
intrusion requires `z>=1` and the claimed bound follows. Endpoint isolates
inside `F'` form a strict guarded packet, proving the population consequence.
`QED`

This uses actual positions for the replacement and checks inactive constraints.
It does not infer packet sites from area, Oler slack, or separate exchanges.

**Corollary 5.2 (isolate payment).** For any selected old rigid-wall faces whose
new interiors are pairwise disjoint, the endpoint isolate population outside
those interiors increases by at least the number of intruded faces, provided
all other selected faces satisfy the usual rigid-wall population bound.

The proof sums `z_new<=z_old-1` on intruded faces and `z_new<=z_old` on the
others, then uses conservation of all isolate labels. No identities of evacuated
labels or outside capacity are claimed. New disjointness is an explicit premise.

**Application to quarter-folds.** A constant-sign face has a pointwise rigid
boundary and Theorem 5.1 applies. Thus every old empty constant-sign face
persists automatically even away from the deep regime. A straight subdivided
parallelogram also has a rigid *point set* image: if its adjacent chords are
`a,b`, with signs `s,-s`, use

`R(x)=U_b-s J(x-p_a)`.

It reverses the coefficient along `a`, maps the full unit-spaced boundary set
onto the new set, and transports old isolates isometrically. Such straight
actual faces of degree at least five are excluded in a canonical source by
Lemma 2.1, but the formula is useful for finite reduced models. Applying the
label-affine fold to isolates instead need not preserve their lower distances.

## 6. A bounded-degree active bank pays actual diameter loss

Let `M>=5`, and suppose a full globally feasible exact-graph quarter-fold has
`r` nonconstant old bounded faces with degrees in `[5,M]`. Put

`C=C_M`, `K_M=5(2C+1)^2`. The expression defining `C_m` is increasing for
`m>=5`, since its derivative is `m/(pi*sqrt(3))-1/2>0`.

**Theorem 6.1 (proved candidate).** At least `ceil(r/K_M)` distinct old loaded
labels lose every one of their diameter incidences. If `L` is the number of old
diameter pairs shortened, then

`L >= ceil(ceil(r/K_M)/2)`.

After canonical isolate normalization of the already feasible endpoint, at
least this many formerly inactive core pairs must become diameter pairs.

**Proof.** Every active face is nonfacial by strict convexity and has an
intruding component. Choose `b_F` as in Theorem 4.1; it is at old distance at
most `C_m<=C` from an old boundary vertex. Its new location is strictly inside
the new cycle hull, so it is nonextreme and cannot be an endpoint of a diameter
pair in a diameter-at-most-`D` full placement. Every old diameter incidence at
`b_F` is therefore lost.

For a fixed selected old load `b`, disjoint radius-`1/2` disks show that at
most `(2C+1)^2` source vertices lie within `C` of it. A triangle-free unit vertex
has degree at most five: its neighbor angles are strictly larger than `pi/3`.
It is incident to at most five bounded faces. Consequently at most
`5(2C+1)^2` of the active faces can choose this `b`. This proves the distinct-label
bound. Each old diameter edge has at most two selected endpoints, and each
selected loaded label has at least one such edge; the edge-loss bound follows.

For the last assertion, apply canonical full-source isolate normalization to
the feasible endpoint. It preserves all core coordinates and opens every
isolate-involving diameter equality. The old source's secondary minimality
gives `N>=L` by counting lost and new diameter pairs; every new pair now lies
in the core. This is an actual pair-count conclusion, not weighted mean descent.
`QED`

For fixed `M`, a linear active bank thus forces a linear old-diameter-loss bank.
It does not bound the cost of the replacement bank or construct the fold.

**Corollary 6.2 (actual loaded-port sign pattern).** Each selected intruding
old load has contact degree exactly three. In the angular order of its three
old contacts, the first and last signs are equal, and the middle sign is their
opposite.

**Proof.** An old diameter endpoint is a strict hull vertex. Its unit-neighbor
rays lie in a cone of width less than `pi`. Consecutive neighbor gaps exceed
`pi/3` by triangle-freeness, so it has at most three neighbors. Its new position
inside a cycle hull cannot carry a diameter, and contact minimality forces its
unchanged contact graph to have at least three neighbors and to positively
span the plane there. Its degree is therefore exactly three.

The old first-to-last angle is greater than `2pi/3`, making their chord greater
than `sqrt(3)`. Canonical two-hop compatibility forces their train signs equal.
If the middle sign were also equal, all three rays would undergo one rotation
and remain in a half-plane, contradicting the required new strict surrounding.
Thus the middle sign is opposite. `QED`

This gives a source-realized sign constraint at every loaded endpoint charged
by the face bank. It does not claim simultaneous feasibility of these patterns.

## 7. Orientation propagates through small-face districts

**Theorem 7.1 (proved candidate).** Form the weak dual on the old faces of
degrees four, five, and six, joining two faces when they share a contact edge.
At any lower-feasible exact-graph quarter-fold of the core, all these cycles
remain actual bounded faces. In each connected weak-dual component containing
a five- or six-face, all boundary-edge signs are one common sign. The same
conclusion holds for an all-quadrilateral component whose train-crossing graph
contains an odd cycle. No endpoint diameter assumption is needed.

**Proof.** Every folded four-cycle is a unit rhombus: its two other vertices
are the two distinct intersections of the unit circles centered at either
diagonal's endpoints. The canonical open-unit-disk cover of a unit rhombus
(Section 67.4) excludes every additional endpoint label from its interior.
With no new unit chords, it stays an actual bounded face.

The local minimum-face theorem forces constant signs on a five- or six-face,
so its wall is rigidly carried. Canonical `C-SHORT-WALL-ZERO-CAPACITY` makes
its old interior isolate population zero. Theorem 5.1 then excludes any core
intrusion and proves that it also stays a bounded face.

Orient each old cycle counterclockwise. At the endpoint, a constant-sign face
keeps this orientation, while a rhombus with the two train signs different
reverses it. Two retained bounded faces sharing an edge must have matching
orientation changes: their old boundary walks traverse that edge in opposite
directions, and their new geometric interiors must lie on opposite sides.
These orientation changes propagate over the weak dual.

A five- or six-face has positive orientation change. Thus every rhombus in
its component is also positively oriented, forcing its two train signs equal.
All face signs are then constant, and the common shared edge propagates one
sign across the component. In an all-quadrilateral component, negative
orientation would require opposite signs on the two trains at every crossing.
That is a two-coloring of the train-crossing graph and is impossible on an odd
cycle. Hence such a component must also have positive orientation and the same
constant-sign conclusion. `QED`

This is a source-realized propagation statement through actual rhombic districts,
not an assertion that the canonical source has one giant such district. Larger
faces, articulation links, and contact bridges are not silently included. A
pure quadrilateral district with bipartite train-crossing graph may still reverse.

## 8. Exact checks, failed shortcuts, and remaining work

Run:

```text
python3 research/verify_target_c_deep_face_transport_2026_10_10.py
```

Saved output:
`research/target_c_deep_face_transport_certificate_2026_10_10.json`.

- A rational 12-wall plus strict isolate proves the permuted rigid transport
  preserves all 78 full-source distances as a multiset. Old and new complete
  ledgers give 156 pair checks. The naive label-affine isolate fold instead
  has a boundary collision of squared distance `128917/130000<1`; the correct
  isometry keeps minimum squared clearance `149517/130000>1`.
- A rational 12-wall plus an exterior unit leaf has a graph-preserving
  lower-feasible fold placing that leaf inside the cycle. The old leaf is an
  actual diameter endpoint; its incident diameter disappears. A displacement
  of `1/100` at the folded leaf opens its only contact with no upper failure.
  The three full ledgers check 234 pairs. This source lacks positive unloaded
  equilibrium at a straight wall vertex and is nonglobal: it is a scope
  guardrail, not a canonical-source example.
- An explicit 13-site triangular-lattice subset has diameter squared 16, below
  18 and `324/13`, proving both fixtures nonglobal. All 78 competitor pairs
  are checked in the integral triangular Gram form.
- The component capacities for degrees 5--32 are enclosed exactly using the
  Machin alternating series for `pi` and an integer-square-root enclosure for
  `sqrt(3)`. Their floors agree at both enclosure endpoints. This verifies
  arithmetic only, not Oler, harmonic trapping, or universal persistence.
- For one rational three-ray hull pattern, all eight sign assignments are
  enumerated: four collide, two preserve the old half-plane, and two make the
  center strictly surrounded by positive weights `13,10,13`. This checks the
  local sign mechanism; actual diameter load and global source optimality are
  not modeled by this fixture.

Executed in the isolated worktree: the saved certificate reproduces byte-for-byte,
all relative report links resolve, the artifact index is regenerated, the
theorem-state PR transaction check passes, and `git diff --check` passes.
The earlier 22 tooling tests are unchanged. Hosted CI remains subject to the
previously verified account billing/spending-limit startup failure; no independent
mathematical audit or full registered-certificate rerun is claimed.

The analytic proofs are not replaced by these finite checks. No independent
mathematical referee has audited them.

**Rejected shortcuts / unresolved implications:** old loaded labels may become
unloaded, so load identity cannot itself justify embedding persistence; exact
graph preservation alone does not preserve a face in arbitrary nonglobal
models; boundary-set isometry differs from label-affine isolate transport;
new face interiors cannot be assumed disjoint when summing populations;
and no large-face tail or outside-region capacity has been discarded.

**Exact next theorem to attack:** for a canonical source and a lower-feasible
core fold, bound the achievable full-source isolate population outside a
pairwise-disjoint bank of rigid face images by its old outside population,
under the diameter budget `D`. Combined with Corollary 5.2, this would exclude
every intrusion in that bank and remove its embedding obstruction. The bound
is not proved. A source-realized nonaffine endpoint or another competitor is
still required for Level I; proving this population bound alone would not be
a full resolution.

**Subsequent worker continuation:**
[rigid-cycle pinned stress and arc stars](target_c_rigid_cycle_pinned_stress_and_arc_stars_slot02_2026-10-10.md)
proves automatic persistence and unchanged isolate populations for every
pointwise rigid cycle at an already full-source feasible exact-graph endpoint.
An intrusive rigid-face core cannot have enough simultaneous isolate capacity
for a full-source extension within `D`. This removes the rigid-face embedding
premise at that full endpoint scope. It does not produce a nonaffine fold or
an outside packet from a lower-feasible core alone; the lower-core replacement
and independent-site deficits remain separately useful.
