> Generated reading edition · [exact source](../../../docs/reports/target_c_rigid_cycle_pinned_stress_and_arc_stars_slot02_2026-10-10.md) · source SHA-256 `a3c36980e3710fc84b318a90a987aaf98940a6384a7e6681cfc60d3b6e4be783`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7EEA3CB6898C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: rigid-cycle persistence from endpoint stress

**Date:** 2026-10-10. **Worker:** 02.
**Base main:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.
**State:** `2026-10-10.audit.234`.
**Previous checkpoint:** `62ad4278120750dba98b13e468e5698e81fe1153`.
**Branch / PR:** `research/sol61-slot02-20261010-integrated-fold`, [PR #948](../publication/provenance.md#source-records).
**Classification:** proved candidates awaiting independent audit; unreviewed,
noncanonical. No authority or theorem-state promotion is changed.
**External literature:** none imported.

## 1. Claim and exact closure chains

**LEVEL I: STILL OPEN.** No universally feasible nonaffine endpoint is constructed.

The main result removes a geometric embedding premise for constant-sign faces
at an already full-source feasible quarter-fold:

```text
full same-cardinality exact-contact endpoint with diameter <= D
 -> endpoint is contact-minimal and has positive contact stress
 -> an enclosed contact component is a positive pinned equilibrium net
 -> exact unit lengths and a pointwise rigid wall determine that net uniquely
 -> no old exterior component can intrude across a rigid wall
 -> every constant-sign actual face persists, with its isolate count unchanged
```

The endpoint stress is applied to the full source, not to an arbitrary reduced
core. The argument therefore does not bootstrap a feasible full source from an
unextended core placement. It is a necessary source-level endpoint condition.

A different, constructive result strengthens the previous intrusion deficit:

```text
lower-feasible core intrusion + independent old sites freed by moving its component
 -> copy the actual intruding component into the original rigid face
 -> restore some old isolates at those freed sites
 -> contract the restored isolates to remove their possible diameter equalities
 -> same cardinality and contacts, fewer actual diameter pairs
```

Finally, local contact stars force all incident signs equal at every internal
vertex of a nonconstant face arc. Such vertices are old and new unloaded
vertices. Consequently every nonconstant face avoids actual unit loaded-hull
sides, and its old loaded boundary labels occur only at its four transitions.

## 2. Inputs and notation

Let `P` be the canonical triangle-free global minimizer selected first to
minimize contacts and then actual diameter pairs, with `D>=9`. Let `G=(V,C)`
be its connected nonisolated contact core. Every actual contact has positive
weight in a relative-interior source KKT stress; every actual old diameter
endpoint belongs to `V`. Contact-isolated labels remain in the full source.

Canonical inputs:

- [C-I restoration, Section 56, items 4 and 5](../targets/target-c/56-ci-restored-frontier.md).
  **Contact minimality alone** gives `C=C_*`; secondary diameter minimality is
  separately used to give `H=H_*`. The distinction matters at the new endpoint.
- [Local KKT equilibrium and strict surrounding, shared theory 01](../theory/01-local-structure.md),
  Theorems 4.1 and 6.1; [ZR/ZF core scope](../targets/target-c/57-zr-zf-rigidity-audit.md).
- [Audit 83](../audits/target_c_face_coupled_quarter_fold_independent_audit_2026-10-07.md),
  quarter-fold edge increments `Q_j-Q_i=s_ij J(P_j-P_i)`, and the two-hop rule:
  two unit-neighbor rays whose old chord is at least `sqrt(3)` must have the
  same sign in a lower-feasible exact-graph endpoint.
- [Audit 229](../audits/target_c_minimum_face_size_local_endpoint_independent_audit_2026-10-09.md),
  the four nonconstant face arcs have at least two edges each.
- [Audit 227](../audits/target_c_rigid_face_isolate_transport_independent_audit_2026-10-09.md),
  crossing separation and convex-coefficient upper bounds for transported isolates.

The previous worker reports
[face obstructions](target_c_quarter_fold_face_obstructions_slot02_2026-10-10.md)
and [deep-face transport](target_c_deep_face_persistence_and_isolate_transport_slot02_2026-10-10.md)
remain unreviewed candidates. Any of their additional facts used below are
proved again at the needed scope.

## 3. An elementary positive pinned-net identity

**Lemma 3.1 (proved candidate; finite identity).** Let `T` be a connected finite
set of free vertices of a bar graph, with every neighbor outside `T` in a
nonempty pin set `W`. Suppose a placement `q` has positive symmetric edge
weights `a_ij` on every edge incident to `T` and satisfies

`sum_j a_ij(q_i-q_j)=0` for every `i in T`.

If a placement `r` fixes every pin pointwise and preserves the length of every
edge incident to `T`, then `r_i=q_i` for all `i in T`. It suffices that the
positive-weight edges connect every free vertex to a pin.

**Proof.** Put `d_i=r_i-q_i`, with `d_w=0` on `W`, and count each edge once.
Exact length preservation gives

`0=sum_{ij} a_ij(2(q_i-q_j) dot(d_i-d_j)+|d_i-d_j|^2)`.

The linear sum is

`2 sum_{i in T} d_i dot sum_j a_ij(q_i-q_j)=0`;

pin terms vanish because their displacements are zero. Thus

`sum_{ij} a_ij |d_i-d_j|^2=0`.

Every summand is nonnegative and every weight is positive. Displacements agree
along all edges, and each connected free component reaches a zero pin.
All displacements are zero. This proof permits arbitrary competing placements;
it does not assume lower/upper feasibility or local proximity. `QED`

The identity is the new bridge used here; it needs positive equilibrium at the
unloaded interior vertices. Local surrounding by itself does not supply a
symmetric positive stress, and is not substituted for this hypothesis.

## 4. Rigid walls pin their old interiors even before extension

**Theorem 4.1 (proved candidate).** Let `W` be any simple actual unit-contact
cycle in `P`, with bounded interior `Omega`. Let `I` be all old core vertices
strictly inside it. Consider any placement of the entire core preserving each
old contact length, whose boundary labels satisfy `Q_w=R(P_w)` for one
Euclidean isometry `R`. Then `Q_i=R(P_i)` for every `i in I`.

No endpoint separation, diameter bound, or full-source extension is needed.

**Proof.** Unit edges cannot cross nonincident unit edges in a unit-separated
source. No source label can lie in the relative interior of a unit edge.
Therefore every old contact from `I` to its complement ends in `W`.
Each old component inside the cycle reaches `W`, since the positive-contact
core is connected. Every `i in I` is inside the convex hull of the cycle, and
is nonextreme in the full source hull, hence has no actual diameter incident
to it. The old positive contact stress satisfies zero contact equilibrium
there. Apply Lemma 3.1 to `R^-1 Q`, pinned at `P(W)`, separately on each
interior contact component. Every old bar length is still one. `QED`

The theorem concerns old core vertices, not the independent coordinates of
isolates. A rigid actual face has no old interior core, so this first direction
alone does not exclude exterior intrusion.

## 5. Full-source feasibility prevents exterior intrusion into every rigid cycle

**Theorem 5.1 (proved candidate).** Let `Q` be a same-cardinality full-source
unit-separated placement with diameter at most `D`, preserving exactly the old
contact graph. If an old simple contact cycle `W` is carried pointwise by one
isometry `R`, then:

1. the core labels inside its new bounded interior are exactly its old interior
   core labels, and their coordinates are `R(P_i)`;
2. the number of contact isolates in its bounded interior is unchanged;
3. in particular, every old actual bounded face with such a rigid boundary
   remains an actual bounded face.

These assertions require no old or new isolate clearance beyond exact-graph
feasibility. The isometry must preserve the boundary labels pointwise; a mere
isometry of the boundary point set is insufficient for the stress comparison.

**Proof of core persistence.** `Q` is triangle-free because its contact graph
is unchanged. Global optimality gives its diameter exactly `D`. Its contact
count is the source minimum, so the C-I restoration yields a relative-interior
KKT stress at `Q` with a strictly positive coefficient on every contact.
Its actual diameter set may be larger than the source minimum; full positive
diameter support is not used.

Any core component `T` inside the new cycle has no contact to a core label
outside it except through `W`, and reaches `W`. Every vertex of `T` is
nonextreme in the new full hull and is incident to no actual diameter.
Thus the new positive contact weights give zero equilibrium on `T`.
Compare `Q(T)` with `R(P(T))`, fixing `Q(W)` pointwise. The graph has the same
unit lengths in both placements. Lemma 3.1 gives `Q(T)=R(P(T))`.
Consequently no old exterior component can lie in the new interior.
Theorem 4.1 already carries every old interior component into the new interior.
This proves exact core membership and coordinates.

**Proof of isolate population equality, with full pair ledger.** Let `z_P,z_Q`
be the old and new interior isolate counts. Suppose `z_Q<z_P`. Remove all new
interior isolates and insert the rigid images of the `z_P` old interior
isolates. The old interior core has just been proved to move rigidly, so all
inserted internal/core distances are unchanged and strict whenever an isolate
is involved. Every inserted isolate is strictly farther than one from all
boundary vertices. All remaining endpoint labels are outside the cycle; the
unit-wall crossing identity in Audit 227 makes every such lower distance
strictly greater than `sqrt(3)`. No contact is added or lost in this operation.

Each inserted isolate is a convex combination of the wall vertices. For any
retained label `y`, those wall vertices are within `D` of `y`; the variance
identity makes the new upper distance strict. For pairs of newly inserted
isolates, apply the identity twice, or express both in the convex hull of the
wall. These pairs also lie strictly below `D`. Thus the resulting configuration
has `n+delta` points, `delta=z_P-z_Q>=1`, diameter at most `D`, and exactly the
old number of contacts.

Delete one nonisolated core vertex, losing at least one contact, and delete
`delta-1` of the now contact-isolated labels. There are enough isolated labels
since the insertion itself supplies at least `delta`. The remaining `n` points
are unit-separated and triangle-free, with diameter at most `D` and fewer
contacts than the canonical minimum. Global optimality or contact minimality
is contradicted. Therefore `z_Q>=z_P`. Reversing `P,Q` and using `R^-1`
gives the opposite inequality; the reverse argument needs contact minimality,
not secondary diameter-pair minimality. Hence `z_Q=z_P`. `QED`

**Quarter-fold consequence.** Every constant-sign bounded face moves by one
pointwise quarter-turn and translation. At any full feasible exact-graph fold,
all these faces therefore remain actual, their interiors are automatically
pairwise disjoint, and every individual interior isolate count is unchanged.
The embedding assumption of Audit 227 is unnecessary for this bank of faces
once full-source feasibility is known. It remains unjustified for an arbitrary
core endpoint lacking an isolate extension.

**No circular construction.** If a lower/upper-feasible core endpoint intrudes
into a pointwise rigid face, this theorem says that it admits no full-source
exact-graph extension within `D`. It does not itself construct that extension.
The former outside-population payment does not supply missing outside sites.

**Corollary 5.2 (full isolate capacity of an intrusive core).** Let `z_total`
be the entire old source isolate population. Suppose a lower-feasible,
diameter-at-most-`D` core placement with the exact old contact graph intrudes
into an old pointwise rigid actual face. Define `I_D(Q)` as the maximum number
of additional points which are strictly farther than one from every core
point and one another, with the diameter of their union with the core at most
`D`. Then `z_total=0` makes such a core placement impossible, and otherwise

`I_D(Q)<=z_total-1`.

Indeed, any packet of `z_total` points would supply a full same-cardinality
exact-graph endpoint contradicting Theorem 5.1. A larger packet contains a
packet of that cardinality. The capacity is a finite integer. This is a
global simultaneous full-source capacity bound, not an inference of slots
from area and not a bound on an independently considered exterior region.

For an already full endpoint, a bank of old rigid faces also has exactly its
old isolate population outside the bank: all faces persist and retain their
individual isolate counts. Thus its outside population cannot pay for a rigid
face intrusion. The remaining work is to realize a fold which avoids this
intrusion or produce another source-level competitor.

## 6. Freed independent sites strengthen the lower-core intrusion deficit

Use an old convex actual face `F`, boundary `W`, and a lower-feasible exact-graph
core placement `Q`. Suppose a component `T` of `G-W` lies in `R(F)`, with the
boundary *point set* an isometric image under `R`; wall labels may be permuted.
Let `z` be the old interior isolate population. Put

`U=T minus N_G(W)`, `a=alpha(G[U])`,

where `alpha` is the maximum independent-set cardinality, and define

`mu=Pack_1({x in int R(F): dist(x,Q(W) union Q(T))>1})`.

**Theorem 6.1 (proved candidate; finite full-source replacement).** Such an
intrusion requires

`z>=a+1` and `mu<=z-a-1`.

No upper bound or full-source extension is assumed for `Q`. In particular, if
`a>=z`, intrusion is impossible even if the old face is occupied.

**Proof.** If `z<=a`, set `s=z`, `k=0`; otherwise set `s=a`, `k=z-a`.
Assume a guarded packet of `k` sites exists. Slightly dilate that packet about
an interior center to open its internal unit pairs; finiteness preserves strict
wall/component clearance and containment. Choose an independent set `S` of
`s` old labels in `U`.

Delete the `|T|` old component labels and all `z` old interior isolates.
Insert `R^-1 Q(T)` and the pulled-back packet in `F`. Use `s` remaining isolate
labels at the original sites `P(S)`, which are outside `F`. The point count is
`|T|+k+s=|T|+z`. The following checks are simultaneous.

- The inserted core component preserves its internal and wall contact counts.
  Wall label permutations change names, not contact count or triangle-freeness.
  Every other lower pair involving a point inside `F` crosses a unit wall and
  has distance at least `sqrt(3)`. The packet guards are strict.
- Each restored site has no contact to `W`, by `S subset U`, and no contact to
  another restored site, by independence. Its old contacts to `T` disappeared
  when `T` moved. No old contact joins `T` to a retained nonwall core vertex.
  Thus restored sites are contact isolates, with strict lower distances to
  all retained outside labels; crossing separates them from all inserted
  interior labels. No new contact is created. The total contact count is exact.
- All inserted interior points lie strictly inside the old diameter hull, so
  all their upper pairs are strict. Retained exterior points and the restored
  sites occupy original source positions. Every upper pair is at most `D`.

Now contract all current contact isolates by one sufficiently small factor
toward the full configuration centroid, fixing the core. Strict lower slack
is preserved by continuity. Isolate-isolate upper distances contract; for an
isolate-core pair, the centroid has distance strictly less than `D` from that
core point because it lies in the interior of the noncollinear full hull.
The convex norm inequality makes every such pair strict below `D`.
No core position or contact changes.

Every old component `T` contains an old actual loaded label: otherwise the old
positive harmonic maximum principle would put `P(T)` in `conv P(W)=F`, where
an actual face contains no core vertex. Moving `T` strictly inside `F` removes
all its old diameter incidences. Restored old sites, including any old loaded
site, are now isolates and have just had all diameter equalities opened.
No new core diameter is created; all other core distances are unchanged.
The final `n`-point configuration has the same contact count and strictly
fewer actual diameter pairs, a contradiction.

For `z<=a` the empty packet always exists, so intrusion is impossible. For
`z>a`, a packet of `z-a` sites is impossible. Finite integer capacity gives
the displayed inequalities. `QED`

**Explicit combinatorial weakening.** A triangle-free planar graph is
3-degenerate: every induced graph on at least three vertices has average
degree less than four by Euler's bound, while graphs with fewer vertices have
minimum degree at most one. Greedy coloring in reverse degeneracy order uses
four colors. Consequently

`a>=ceil(|U|/4)>=ceil((|T|-5|W|)_+/4)`.

The second bound uses source contact degree at most five to bound the number
of component vertices adjacent to `W`. No graph coloring theorem is imported.
Independent sites are actual deleted-source positions, rather than predicted
sites from a packing-area allowance.

## 7. Every internal arc star of a globally feasible nonconstant fold is rigid

**Theorem 7.1 (proved candidate).** In a full feasible exact-graph quarter-fold,
let `F` be an old nonconstant actual bounded face. Every vertex strictly inside
one of its four sign arcs has contact degree three or four, is unloaded both
before and after the fold, and all its incident contacts have the arc's sign.
Thus old loaded boundary labels of `F` can occur only at the four transition
vertices. No boundary edge of `F` is an actual unit loaded-hull side.

**Proof.** The local convex-face classification gives four transitions with
old turns above `pi/3`, and four constant-sign arcs. For completeness, let
`T_i` be total turn internal to arc `i`, and let `a_i,b_i` be its endpoint
tangent-to-chord deflections, so `T_i=a_i+b_i`. The four chord angles alternate
between `gamma` and `pi-gamma`. Consecutive actual transition turns satisfy

`tau_i+tau_{i+1}=pi-T_i-b_{i-1}-a_{i+1}>2pi/3`.

All deflections are nonnegative, hence `0<=T_i<pi/3`. Strict source face
convexity makes each internal vertex turn `delta` strictly between zero and
`pi/3`.

The folded cycle is simple by lower separation and has turning number `-1`:
internal arc turns remain positive, while each of the four transition turns
changes from `tau` to `tau-pi`. Their total is `2pi-4pi=-2pi`.
Thus every internal arc vertex is reflex relative to the folded clockwise
cycle, so it is nonextreme and has no new diameter. Endpoint contact minimality
forces its contact rays to strictly surround it.

Rotate old coordinates so the two face rays have angular positions `0,theta`,
where `theta=pi-delta in (2pi/3,pi)`. Every other contact lies in the complementary
empty-face angular interval, and all gaps between unit neighbors exceed
`pi/3`. There can be at most two additional contacts. Degree two would violate
the new strict surrounding, so the degree is three or four.

If there is one additional contact at angle `alpha`, then

`theta+pi/3<alpha<5pi/3`.

Flipping its sign relative to the two arc rays changes its relative direction
by `pi`. Its angle becomes `alpha-pi in (theta-2pi/3,2pi/3)`, strictly between
`0` and `theta`. All three new rays would then lie in a cone of width less
than `pi`, contradicting strict surrounding. Its sign is therefore the arc sign.
The old three rays also strictly surround: all three angular gaps are below
`pi`. Hence the old vertex is not a diameter endpoint.

If there are two additional contacts at `alpha_1<alpha_2`, their spacing gives
`alpha_1<4pi/3` and `alpha_2-theta>2pi/3`. The first extra ray has shortest
angular separation above `2pi/3` from the ray at `0`, while the second has
separation above `2pi/3` from the ray at `theta`. The two-hop rule forces both
extra signs equal to the arc sign. All old angular gaps are below `pi`, since
the one large gap is `theta<pi` and the other three gaps sum to less than
`4pi/3`, each with the other two above `pi/3`. So the old rays strictly surround
here as well, and uniform rotation preserves this at the endpoint.

Finally, every arc has at least two edges. Every boundary edge has an internal
arc vertex as at least one endpoint, which is old unloaded. Therefore no such
edge joins two old actual diameter endpoints. `QED`

Each internal arc vertex has an additional contact pointing inside the new
cycle: its whole star rotates rigidly, while the new cycle's local interior
is the old exterior sector. Thus its old exterior contact neighbor is an
actual intruding vertex at the endpoint. A single such neighbor can serve at
most five boundary vertices, so at least `ceil((m-4)/5)` distinct old exterior
core labels intrude into the folded `m`-cycle. This is a lower population bound,
not a proof that those labels fit globally.

## 8. Exact loaded-support migration law

Let `B_P,B_Q` be the actual diameter endpoints in the core at the old and new
full-source placements. Let `O` be the vertex set of the old unbounded contact
face walk, including any repeated bridge/articulation occurrences only once.
Put

`M_3={v in V: deg_G(v)=3 and its incident train signs are not all equal}`.

**Theorem 8.1 (proved candidate).** Every full-source feasible exact-graph
quarter-fold satisfies

`B_P symmetric_difference B_Q = M_3`, `M_3 subset O`, `B_Q subset O`.

Every bounded face incident to a migrating vertex is nonconstant, with that
vertex one of its four sign transitions. Any vertex incident to a constant
bounded face retains its loaded/unloaded status. Every old degree-three core
vertex outside `O` has one common sign on its whole contact star.

This is an assertion about actual diameter endpoint labels; it does not
determine their diameter partners or supply the pairwise upper ledger.
No claim about raw endpoint diameter equalities involving contact isolates
is included. Such equalities may be opened by the canonical normalization.

**Proof of the local role law.** A nonisolated contact-minimal vertex with no
actual diameter must be strictly surrounded by its contacts. A diameter
endpoint has all its unit-neighbor rays in an open half-plane. Triangle-free
unit rays have gaps strictly above `pi/3`, so a loaded vertex has degree at
most three. Consequently degrees one and two are loaded at both placements;
degrees four and five are unloaded at both.

At an old loaded degree-three vertex, place its extreme rays at `0,theta`,
with its middle ray at `alpha`. The old angular span satisfies
`2pi/3<theta<pi`, and `pi/3<alpha<theta-pi/3`. The extreme-ray chord exceeds
`sqrt(3)`, forcing their signs equal. Uniform signs rigidly rotate the old
half-plane star, which must remain loaded. In the only nonuniform pattern,
the middle ray flips by `pi` relative to the extremes. Its angle becomes
`alpha+pi`; the three new cyclic gaps are `theta`, `alpha+pi-theta`, and
`pi-alpha`. All are strictly below `pi` and above `pi/3`, so the new star
strictly surrounds the vertex and it cannot be a diameter endpoint.

At an old unloaded degree-three vertex, all three cyclic gaps lie strictly
between `pi/3` and `pi`, and at least one is at least `2pi/3`. Every such gap
forces its bounding signs equal. If more than one gap has this property,
all signs are equal. Otherwise a nonuniform pattern has the two rays bounding
the unique large gap `theta` equal, and the remaining ray opposite. Relative
to rays at `0,theta`, the remaining old ray is at `alpha` with
`pi<alpha<theta+pi`, by old strict surrounding. Its flipped direction
`alpha-pi` is strictly inside `(0,theta)`. Thus the new three rays lie in an
open half-plane. Contact minimality forces a new actual diameter incidence.
Uniform signs instead preserve strict surrounding and remain unloaded.
This proves the symmetric-difference identity.

**Proof of outer localization.** For an old unloaded migrating vertex, consider
the angular face sector of its unique large gap `theta>=2pi/3`. If it belonged
to a bounded face with constant signs, Theorem 5.1 would retain that face,
while the flipped third contact would point strictly into its empty interior;
this is impossible. If it belonged to a nonconstant face, its two bounding
edges have the same sign, making it an internal arc vertex. The folded cycle
would be reflex there, hence nonextreme; the new half-plane star could not
remain without a diameter, again a contradiction. Therefore the large sector
belongs to the old unbounded face, and the vertex lies in `O`.

An old loaded migrating vertex already lies in `O`, since every actual
diameter endpoint is strictly exposed in the full hull. Its two small
bounded sectors, if present, each use the middle ray and an extreme ray,
whose signs differ. The same holds for the small sectors at a previously
unloaded migrating vertex. Hence every bounded face incident to a migrating
vertex is nonconstant and has a transition there; a large equal-sign sector
cannot be bounded by the preceding argument. Bridges may put more than one
sector on the unbounded face and are not discarded.

Since `B_P subset O`, the local identity now gives `B_Q subset O`. No old
interior degree-three vertex migrates, so it has uniform signs. `QED`

**Source-level implication.** The replacement-diameter bank required at a
noncongruent full feasible fold can only use old outer-contact-walk labels.
Positive-core labels buried in the old contact embedding are not new diameter
ports. This restricts the previously unspecified support of the replacement
bank, but does not bound its size or prevent inactive pairs between these
outer labels from reaching `D`.

**Corollary 8.2 (a connected rigid-face bank pins the loaded set).** Suppose
there is a connected graph on **all old loaded vertices**, every one of its
edges an actual unit contact incident to a constant-sign bounded face.
Then the entire endpoint core is congruent to the source and all train signs
are one common sign.

Indeed, at a loaded vertex of degree three a constant bounded face uses an
extreme ray and the middle ray: using both extreme rays would put the middle
contact inside its empty convex sector. Equality of those two signs, together
with forced equality of the extreme signs, makes the whole star uniform.
At degree two the two face signs are already uniform. Every edge in the
connected bank thus propagates one common sign through shared loaded vertices.
The loaded vertices undergo one common quarter-turn and translation. Every
old actual diameter is preserved, and every old contact is preserved.
Canonical [`C-MIXED-CORE-FINITE-RIGIDITY`](../audits/target_c_finite_mixed_core_rigidity_independent_audit_2026-10-07.md)
makes the whole core congruent. The old loaded set affinely spans the plane,
so the congruence agreeing with its quarter-turn on that set is that same
proper quarter-turn. Its contact increments force every train sign equal. `QED`

The precise loaded-only premise covers, for example, a connected spanning
bank of nonbridge actual unit loaded-hull sides. Their incident bounded faces
are constant by Theorem 7.1. It does not cover a bank linked through arbitrary
unloaded vertices or unit-contact bridges.

## 9. A boundary certificate for every core upper pair before extension

This last result has explicit additional sign-balance hypotheses; it does not
use a stress of an as-yet-unconstructed full endpoint.

Let `a_ij>0` be the **old** canonical contact weights. Let `O` again be all
old outer-contact-walk vertices. Consider an integrated quarter-fold field on
the core. At each vertex outside `O` impose the exact condition

`sum_{j:s_ij=+1} a_ij(P_i-P_j)=0`.                 (9.1)

Old zero equilibrium makes the analogous minus-sign sum zero as well.

**Theorem 9.1 (conditional boundary certificate; proved at its stated scope).**
If (9.1) holds, then

`Q(V) subset conv Q(O)` and `diam Q(V)=diam Q(O)`.

Thus checking `|Q_o-Q_o'|<=D` for every pair of old outer-walk labels checks
**every** core upper pair, including previously inactive pairs, before any
full-source extension is assumed. If every residual isolate `y` additionally
passes `|y-Q_o|<=D` for every `o in O`, its upper pairs with all core labels
also pass. Residual isolate-isolate pairs still require their separate tests.

**Proof.** For `i outside O`, old equilibrium and (9.1) give

`sum_j a_ij(Q_i-Q_j)=J sum_j a_ij s_ij(P_i-P_j)=0`.

Each component after deleting `O` reaches `O`, by connectedness. The positive
harmonic maximum principle, applied to every supporting linear functional,
puts all its new coordinates in `conv Q(O)`. Any two points of that convex
hull have distance at most `diam Q(O)`, by taking convex combinations in
each variable and applying the triangle inequality. The reverse diameter
inequality is immediate because `O subset V`. The same convexity argument
with one argument fixed at `y` gives the residual-isolate assertion. `QED`

For a lower-feasible sign assignment, a sufficient local implementation of
(9.1) is uniform signs at every old interior contact star except a four-star
whose opposite unit rays are genuinely collinear. At such a four-star,
opposite signs agree by two-hop compatibility, and old equilibrium makes
the positive weights on each opposite pair equal. Each sign class is then
separately balanced. Uniform signs trivially balance because the entire old
star is unloaded. Degree-five compatibility already forces uniform signs;
the added rule for interior degree-three vertices agrees with Theorem 8.1.
Nonrhombic four-stars are not silently assumed to satisfy it.

This supplies an exact all-core upper certificate for a specified class of
train assignments. It constructs neither a nonconstant assignment in that
class nor its lower-feasible full-source isolate extension. In particular,
the old outer-label upper tests cannot be replaced by a weighted old-diameter
sum or by tests on only the old loaded endpoint set.

## 10. Exact checks, failure tests, and next obligation

The companion verifier checks:

- a rational 3-by-3 oblique unit-grid cycle with four old interior core
  vertices; all 120 source pairs, 24 contacts, four exact positive interior
  equilibria, and grounded contact-Laplacian determinant `192`;
- complete sign enumeration at rational degree-three and degree-four arc
  stars; the former has exactly two fully surrounded lower-feasible patterns,
  both uniform, and the latter exactly two lower-feasible patterns, both uniform;
- the earlier rational leaf-intrusion regression, which lacks a positive new
  equilibrium at the leaf and therefore cannot be used against Theorem 5.1.

Run `python3 research/verify_target_c_rigid_cycle_pinned_stress_2026_10_10.py`.
Saved output is `research/target_c_rigid_cycle_pinned_stress_certificate_2026_10_10.json`.
The saved certificate reproduces byte-for-byte. The report's relative links
resolve; the artifact index and its unreviewed metadata are generated, and
local theorem-state and PR transaction checks pass. The earlier 22 tooling
tests are unchanged. No new theorem dependency or canonical certificate
registration is altered.

The fixtures do not assert global optimality, full diameter stresses, existence
of a canonical source, or a universally feasible fold. The pinned uniqueness
and geometric persistence theorems are analytic; finite output does not prove
their quantifiers. No independent mathematical audit is claimed.

The identity fails if the pinned weights are allowed to vanish on the only
boundary attachment. The old exterior leaf can move to the inside of a
reflected rigid wall precisely because no positive equilibrium is possible
at its new degree-one position. Boundary point-set congruence with a label
permutation also does not give the pinned comparison without additional graph
symmetry; it is excluded from Theorem 5.1 but permitted in Theorem 6.1.

**Next exact obligation:** extract an integrated nonconstant source train
assignment with every core lower pair and every core upper pair at most `D`,
and a simultaneous guarded placement of every residual isolate in its
nonconstant-face or exterior region. The rigid-face embedding and population
constraints proved here must hold for such an assignment; they are not a
substitute for constructing it. No implication to a universal Level I
contradiction is claimed without this remaining full-source endpoint or an
independent exclusion of every canonical survivor.

**Further worker checkpoint:**
[nonconstant large-face quarter-fold exclusion](target_c_nonconstant_face_quarter_fold_exclusion_slot02_2026-10-10.md)
uses the arc-star result to construct a complete four-corner pin boundary
around every hypothetical active large face. Pinned rank and positive stress
bound its hull diameter by five, and exact source-contact population arguments
exclude the seven remaining arc counts. It strengthens the necessary fold
conditions here to constant signs on every old simple bounded face of degree
at least five, without constructing a full endpoint or settling Level I.
