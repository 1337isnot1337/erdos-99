> Generated reading edition · [exact source](../../../docs/reports/target_c_joint_swap_horn_and_loaded_defects_2026-10-01.md) · source SHA-256 `d143bc1b129759e2a4c29614a25aa8e6cb2bd6f9be9530b2a15ff67d1dfc2c8e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7CFE1216AB27","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — simultaneous small swaps and loaded shore defects

**Phase 2 preservation provenance:** PR #600, branch swarm/tb1-augmented-thrackle-20261001, exact source head 9ddd9538c29244fd22183f9682b2835f54cde0c3. This original report records unreviewed exact joint-conflict, contact-slack, and face-following results. Current-main PR #649 generalizes the rooted isolate upper-dispatch portion; this copy preserves the report’s separate conflict geometry and exact regressions without promoting either route.

`joint isolate extension -> at most d_H upper-exception pairs -> lower-only Horn
obstruction -> source-level return/conflict certificate -> finite competitor if
the remaining obstruction is excluded`

**Date:** 2026-10-01. **Starting commit:**
`14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79` (shared checkout initially
`af823f5f8b998aadf652df9aed01b2dbc2882e75`).

**State version:** `2026-09-14.audit.51`.

**Mission:** `swarm/tb1-augmented-thrackle-20261001`; remove inactive upper
blockers and identify the exact source geometry required for the augmented
near-unit system. This continues PR #600.

**Classification:** proved candidates awaiting promotion; route applications
conditional on the unpromoted actual-train extraction. The finite counterexamples
are regressions. Repository lifecycle remains unreviewed. C-II and Level I OPEN.

## 1. Dependencies and conventions

Canonical premises are full positive support on the contact-minimal, then
diameter-pair-minimal source (`C=C_*`, `H=H_*`), the KKT equation in
[Theory 4](../theory/01-local-structure.md), the diameter-thrackle geometry, and
the retention of contact-isolated source points. The active normalization is
[Section 56](../targets/target-c/56-ci-restored-frontier.md); full diameter
visibility is [Section 21](../targets/target-c/21-full-diameter-visibility-frontier.md).

The fixed rooted forest and its exception bound are proved in the earlier
[small-swap packet](target_c_ultrasmall_swap_isolate_dispatch_2026-10-01.md).
The route application uses the unpromoted
[open-cell arbitrary block transposition](target_c_open_cell_block_transposition_2026-10-01.md)
and [local witness cell](target_c_local_witness_cell_2026-10-01.md).
The star-contiguity input is rederived in Section 6 from diameter geometry.

PR #595's simultaneous-swap 2SAT packet motivates the Boolean formulation.
The new statements below have direct proofs, do not import that packet as a
canonical premise, and keep every source point.

Write

$$
L=\sqrt{D^2-1},\qquad \gamma_D=D-L,\qquad d_H=|B|-|H|.
$$

Pairs of length greater than `L` form the convex strict-long thrackle `T_D`.
Its core-endpoint rooted forest `F` leaves a fixed set `J` of inactive long
exceptions with `|J|<=d_H`. Every vertex outside `B` in a component of `T_D`
meeting `B` is a contact isolate, assigned a root `r(z) in B`. Components not
meeting `B` can be kept fixed.

## 2. Joint extension, with one fixed forest for all patterns

### Theorem 1

Let `G_1,...,G_k` be disjoint subsets of the nonisolated contact core. Assume
their binary translations by nonzero vectors `Delta_i` preserve every old unit
contact for every binary pattern. Assume every individual move is ONE-SIGN:
it weakly shortens every old diameter and strictly shortens every diameter
whose endpoints have different movement status; at least one such diameter
exists for each `i`.

Suppose all `Delta_i` point within a cone of angular width at most `pi/3`, and
`s=max |Delta_i|<gamma_D`. Suppose also that for each old diameter vector `r`,
the numbers `r dot Delta_i` have the same strict sign for all `i`.

Extend ownership of every contact isolate `z` to the owner of its fixed forest
root `r(z)`, or to the fixed class if its root is fixed. Then, for every binary
pattern:

1. all old contacts remain unit;
2. all inactive upper constraints outside `J` remain strict;
3. all old diameters weakly shorten;
4. every nonempty selected pattern strictly shortens an old diameter.

After disabling the owners of the endpoints of `J`, at most `2d_H` groups are
removed. The remaining joint search has no inactive upper blockers at all.

### Proof

For two vectors of lengths `a>=b` making angle `theta<=pi/3`,

$$
|\Delta_i-\Delta_j|^2
=a^2+b^2-2ab\cos\theta\le a^2,
$$

because `b<=a<=2a cos(theta)`. Thus the diameter of the set
`{0,Delta_1,...,Delta_k}` is at most `s`. Every relatively changing pair moves
by at most `s`. Pairs of old length at most `L` therefore remain below `D`.
The endpoints of each forest edge share the same root and hence the same
ownership. Isolate-only long components remain fixed. The only inactive long
edges left unchecked are precisely `J`.

No old diameter can join two different moving groups. Orient such a putative
diameter from group `j` into group `i`, with vector `r`. Individual ONE-SIGN
shortening of the `i` move requires

$$
2r\cdot\Delta_i+|\Delta_i|^2<0,
$$

while shortening of the `j` move requires

$$
-2r\cdot\Delta_j+|\Delta_j|^2<0.
$$

Their projections have opposite signs, contrary to the common strict sign
hypothesis. Each old diameter is consequently either unchanged within one
ownership class or shortened by the one selected group it meets. This proves
the active-diameter claims. Isolates have no old contact or diameter incidence.

Disabling both endpoint owners of every edge of `J` fixes every such pair.
There are at most `2|J|<=2d_H` owners to disable. All other estimates are
unchanged. This proves the theorem. QED.

### Open-cell application

For disjoint phase swaps choose the subfamily with one common orientation of
phase difference. Their displacement directions are the quarter-turns of their
phase midpoints, with one common sign. If the phase window has width `W<pi/3`,
the displacement cone has width at most `W`. For an old actual diameter `r`,
its projection onto these displacements cannot change sign: its zero would
place its projective direction at a phase midpoint inside the empty open cell.
The fixed cell-boundary witness diameters have no endpoint in any middle slab.

The earlier packet supplies disjoint swaps with `s<=1/(2D)<gamma_D` by grouping
enough distinct phases per physical block. Every assertion here concerns those
actual source cuts. It does not assert that an arbitrary phase-labelled matrix
has such a source realization.

## 3. Exact lower-only Horn certificate

Restrict to the undisabled groups of Theorem 1. For a source pair with endpoints
owned by distinct moving groups `i,j`, put `r=p_i-p_j`. Its four relative
vectors are

$$
r,\quad r+\Delta_i,\quad r-\Delta_j,
\quad r+\Delta_i-\Delta_j.
\tag{1}
$$

An old noncontact pair is forbidden in a local state when its new length is
`<=1`, including creation of a new unit contact. The all-zero state is allowed.
A pair with one fixed endpoint gives a unary clause. Every bad state of a
two-owner pair gives one of

$$
10:\ i\Rightarrow j,\qquad
01:\ j\Rightarrow i,\qquad
11:\ \neg x_i\lor\neg x_j.
\tag{2}
$$

These clauses are Horn, with at most one positive literal. Every relevant pair
has old length at most `1+s`. The exact clauses contain all and only the
remaining lower obstructions. There are no active-diameter or upper-distance
clauses after the owner deletion in Theorem 1.

For each seed `i`, close `{i}` under the implication arrows. A nonzero model
exists if and only if one seed closure contains no unary-forced-false node and
does not contain both endpoints of any negative binary clause. Indeed a model
containing `i` contains its closure; conversely that closure, with all other
variables false, is a model when it passes those two tests.

Canonical minimality forces every seed to fail. The exact obstruction is
therefore either a directed path to a unary zero, or two directed paths from
the seed to the endpoints of a negative binary clause. A model that passed
would preserve all old contacts and all inactive constraints strictly while
removing an old diameter; this contradicts either global diameter minimality
or the secondary diameter-pair normalization.

No near-unit pair receives a KKT multiplier by this formulation.

### Prime pair reduction

If a pair forbids both `10` and `11`, it forces `i=0`; if it forbids both `01`
and `11`, it forces `j=0`. An acute displacement cone also excludes the truth
table with exactly `10,01` bad and `11` good. Set `f_ab=|r_ab|^2-1`. Then

$$
f_{11}=f_{10}+f_{01}-f_{00}-2\Delta_i\cdot\Delta_j.
\tag{3}
$$

If `f_10,f_01<=0`, `f_00>0`, and `Delta_i dot Delta_j>0`, then `f_11<0`.
Such a pair forces both owners to zero. After prime reduction, the only
negative binary clauses remaining are **pure joint conflicts**: `11` bad and
both singleton states good.

Equal displacement vectors have no pure joint conflict because their `11`
relative vector is `r`. Unequal parallel vectors can have such conflicts;
Section 8 gives an exact regression. A cone condition alone does not reduce
the system to ordinary implication returns.

### 3.1. Bounded chambers can follow the motion; binary clauses are exterior

### Theorem 8: face-following isolate dispatch and exterior binary support

In addition to Theorem 1 assume actual disjoint O–O slabs on one shore of
width strictly below `pi/3`. The contact core is a connected plane graph,
each bounded face has a simple strict convex unit-edge boundary, and the
selected cuts are global stopped trains. A train continues across opposite
sides of strict rhombi and stops at the outer face or a bounded nonrhombic
face. In particular an O–O train has no edge on the boundary of a bounded
nonrhombic face. These are the actual stopped-train hypotheses in
[Section 156](../targets/target-c/156-157-face-closure-and-outer-train-bracing-audited.md),
not a virtual chart.

Keep the rooted forest assignment for contact isolates incident with `T_D`.
For each contact isolate in a bounded nonrhombic face, instead assign the
ownership of that face's boundary vertices. All other isolates can keep the
assignment from Theorem 1. Then:

1. all upper conclusions and the fixed `|J|<=d_H` exception set survive;
2. no pair in a bounded nonrhombic face blocks any binary pattern;
3. every lower blocker in a bounded rhombus is a diagonal with just one
   moving owner and a fixed owner;
4. every lower pair involving two different moving owners lies in the
   original outer face of the contact core.

Thus after disabling at most `2d_H` groups the Horn system has only exterior
binary clauses, plus unary clauses supported either in the exterior or in
bounded rhombi. Every pure conflict of Section 4 is an exterior pair.

### Proof

First, all source pairs of length less than `sqrt(2)`, including all old
contacts, form one plane straight-line graph. If two such disjoint segments
crossed, their four endpoints would be a convex quadrilateral. At an angle
at least `pi/2`, the opposite diagonal has squared length at least the sum
of two adjacent squared side lengths, hence at least `2`. That contradicts
the short-diagonal hypothesis. A short segment cannot pass through another
source point, because the two intervening distances would sum to at least
`2`. Therefore the open segment of any inactive short pair lies in one face
of the old contact core.

Every unit edge on a bounded nonrhombic boundary is outside every selected
O–O train. The exact train cutset consequently gives equal shore indicator
values at its endpoints, for every selected cut. Following the entire
boundary shows that all its vertices have the same ownership. The face
undergoes a rigid translation, or remains fixed.

An isolate strictly inside this face is not an extreme point of the source
hull: it lies inside the convex hull of the boundary vertices. By the strict
long-pair theorem it is incident with no edge of `T_D`. Thus changing its
ownership has no effect on the rooted forest or `J`, and all upper distances
involving it remain below `L+s<D`. Every lower pair that can change enough
to reach one has old length at most `1+s<sqrt(2)`. If one endpoint is such
an interior isolate, the face property just proved puts the other endpoint
in the same face or on its boundary. Both have the same ownership, so their
distance is unchanged. The same is true for boundary-to-boundary pairs in
that nonrhombic face. This proves the bounded-chamber conclusion.

A unit rhombus contains no further source point in its interior. Write any
point in its parallelogram coordinates and round each coordinate to `0` or
`1`. Its distance to that corner is strictly below `1`: the squared distance
is at most `(1+|cos theta|)/2<1` for a nondegenerate rhombus. This would violate
unit separation. Hence a new short pair in a rhombus is a core diagonal.

At most one selected shore train crosses this rhombus. Its two train
directions have acute projective separation strictly greater than `pi/3`,
whereas all selected shore directions lie in a window narrower than `pi/3`.
All selected shore indicators except possibly that one are constant on the
face. The possible ownership labels therefore form at most two classes,
separated across the one train cut, each on two adjacent vertices.

Those classes cannot be two distinct moving owners. Otherwise the rhombus
has a unit edge between those two groups. Preserving its unit length in the
states `00,10,01,11` gives, by the squared-norm identity,
`Delta_i dot Delta_j=0`. This contradicts the strict acute-cone hypothesis.
A relatively moving rhombus diagonal therefore has one moving owner and a
fixed owner. It contributes a unary clause.

Every bounded face is one of these two types. The only remaining face for
a pair with two different moving owners is the old outer face. Contact
isolates there are retained, including the roots' remote ownership labels.
This proves all assertions. QED.

### Scope and interaction with PR #598

The cofacial classification in PR #598 allows nonrhombic/inactive/exterior
faces in a general source. Theorem 8 uses the stronger **global O–O stopped
cutset** condition and a face-following dispatch. It excludes bounded
nonrhombic blockers in that specific branch; it does not exclude them for
F-ending trains, arbitrary local cuts, arbitrary core motions, or a different
macroscopic-container argument. Bounded rhombus unary blockers still require
the one-boundary transverse-train phase-threshold analysis from PR #598.

This does not make the outer face convex, identify repeated outer-walk
occurrences, or bound the exterior isolate population. A motion assigned to
one isolate by its remote diameter root can still produce a binary exterior
clause. An exterior clause is still inactive in the original KKT system.

### 3.2. A binary lower pair cannot close a two-contact path

### Lemma 10

Under Theorem 8's actual one-shore hypotheses, two source vertices with
different moving owners and distance at most `13/12` have no common old
unit-contact neighbor.

### Proof

Let their owners be `i,j`, and suppose `c` is a common unit neighbor.
There is no old contact between two different moving groups: preserving
it under the four binary states would force `Delta_i dot Delta_j=0`,
contrary to the acute displacement cone. Thus `c` has neither owner `i`
nor owner `j` nor any other moving owner. It is fixed.

Both contacts to `c` therefore cross the boundaries of actual selected
slabs, so their projective directions lie in the one shore window of width
`W<pi/3`. The ordinary angle between the two unit vectors from `c` is
either less than `pi/3` or greater than `2pi/3`. The first case gives endpoint
distance below one; the second gives endpoint distance above `sqrt(3)`.
Both contradict the source pair's distance in `[1,13/12]`. QED.

Contact isolates have no common unit neighbor automatically. Consequently
any short old contact path closed by a binary near-unit pair has at least
three edges. This prevents a two-contact near-triangle from being used as
a binary conflict certificate; unilateral rhombus near-triangles remain.
It does not reject the surviving three-contact pocket mechanism or an
exterior pair without any short old contact path.

## 4. Pure joint conflicts have quadratic contact slack

### Theorem 2

Suppose `|r|>1`, `|r+Delta_i|>1`, `|r-Delta_j|>1`, and
`|r+Delta_i-Delta_j|<=1`. Let `a,b` be the two displacement lengths,
`s=max(a,b)`, and let `kappa` bound the distance between their unit directions.
Assume the angle between the displacement directions is at most `pi/3`.
Then

$$
0<|r|^2-1<s^2+2s\kappa+s^2\kappa^2.
\tag{4}
$$

If a unit vector `v` is within `kappa_0` of both displacement unit directions,
then

$$
|r\cdot v|<s+(1+s)\kappa_0.
\tag{5}
$$

Thus for an open-cell cone of width `W=O(1/D)` and swaps `s=O(1/D)`, pure
joint conflicts have squared contact slack `O(1/D^2)` and are oriented within
`O(1/D)` of the shore direction perpendicular to `v`.

### Proof

By reversing `r` and exchanging the endpoint labels if necessary, take `a>=b`.
Set `lambda=1-b/a` and

$$
h=(b/a)\Delta_i-\Delta_j,
\qquad |h|\le b\kappa.
$$

The bad `11` state implies `|r+lambda Delta_i|<=1+b kappa`. The squared-norm
identity for interpolation gives

$$
|r+\lambda\Delta_i|^2-1
=(b/a)(|r|^2-1)+\lambda(|r+\Delta_i|^2-1)
-\lambda(b/a)a^2.
$$

The second term on the right is nonnegative and is positive if `lambda>0`.
Consequently

$$
|r|^2-1\le2a\kappa+ab\kappa^2+\lambda a^2
<s^2+2s\kappa+s^2\kappa^2.
$$

Strictness remains when `a=b`, since then the `s^2` term is positive.

Subtract the good `10` and `01` squared lengths from the bad `11` length. With
`v_i=Delta_i/a`, `v_j=Delta_j/b`, this yields

$$
r\cdot v_j>-a+b/2\ge-s,\qquad
r\cdot v_i<b-a/2\le s.
$$

Also `|r|<=1+|Delta_i-Delta_j|<=1+s` in an acute cone of width at most `pi/3`.
Replacing either unit direction by `v` proves (5). QED.

## 5. A pure conflict cannot touch a two-sided shore vertex

### Lemma 3

Let a unit-separated source contain a noncontact pair with relative vector `r`
such that `|r|<=5/4` and `|r dot v|<=1/8`, where `u,v` are orthonormal. Neither
endpoint can have unit neighbors in both directions within `pi/6` of `+u` and
`-u`.

### Proof

At an endpoint choose the unit-neighbor vector `c` whose `u` component has the
same sign as the vector from this endpoint to the other endpoint. Unit
separation gives `|r|>1`. Hence

$$
r\cdot c\ge {\sqrt3\over2}\sqrt{1-(1/8)^2}-{1\over2}(1/8)
={\sqrt{189}-1\over16}>{25\over32}\ge {|r|^2\over2}.
$$

The other endpoint and this neighbor are distinct because the original pair
is a noncontact. Their squared distance is
`|r|^2+1-2r dot c<1`, impossible. The same argument reverses `r` at the other
endpoint. QED.

For sufficiently large `D`, Theorem 2 therefore places both endpoints of every
pure conflict outside this explicitly defined regular two-sided shore class.
No assertion that all other source points are few is made. In particular the
contact-isolated source population remains in the Boolean system.

## 6. Contact leaves localize to the witness hub

### Lemma 4: local star contiguity

At a source diameter vertex `p`, the rays to all diameter partners fit in a
cone of aperture at most `pi/3`: two such partners are at most `D` apart.
Every nonincident diameter chord meets both extreme rays by the diameter
thrackle property. If its intersection points are `t_-u_-`, `t_+u_+` with
`t_-,t_+>0`, its direction has coefficients `(-t_-,t_+)` in that cone basis.
Neither orientation has both coefficients nonnegative. Thus its projective
direction lies outside the star cone, including its boundary. If the star
has only one edge the assertion is immediate. This proves the needed
star-contiguity property directly.

### Theorem 5: leaf localization

Let a source have positive KKT weights on every actual contact and diameter.
Let `J` be an open cell between two consecutive global diameter directions.
If a source vertex `p` has contact degree one and its unit-contact projective
direction lies in `J`, then the two cell-boundary diameter edges are both
incident with `p`. In particular, if those edges have common witness hub `v`,
then `p=v`. If the two boundary edges are disjoint, there is no such contact
leaf.

### Proof

With unique unit neighbor `q`, KKT reads

$$
\alpha_{pq}(p-q)=\sum_{x:px\in H}\beta_{px}(p-x),
\qquad \alpha_{pq}>0.
\tag{6}
$$

The diameter load cannot be empty. Its vectors lie in a cone of aperture at
most `pi/3`. All weights are positive. The resulting contact direction is in
the strict interior of their cone unless there is only one diameter vector,
when it equals that actual diameter direction. The latter is excluded by
membership in the open cell.

The projective star arc has endpoints at global diameter directions. Since it
contains a point of the direction-empty cell, it contains that entire cell and
both boundary directions. Lemma 4 forces both boundary edges to be incident
with `p`. Distinct edges with common endpoint `v` have no second common
endpoint, so `p=v`. QED.

This is not a theorem about arbitrary contact leaves of arbitrary minimizers:
the strict-positive-support hypothesis matters. A contact direction parallel
to an actual diameter is also an explicit exception.

## 7. Two nearly opposite unit contacts exclude a small loaded slab

### Lemma 6: exact loaded-contact angular bound

If `p` has an actual diameter partner `x` and unit neighbors `p-a,p-b`, then

$$
D|a+b|\ge1.
\tag{7}
$$

Indeed for `r=p-x`, the upper constraints at both neighbors give
`|r-a|^2<=D^2`, `|r-b|^2<=D^2`, hence `r dot a,r dot b>=1/2`.
Thus `1<=r dot(a+b)<=D|a+b|`. No stress argument is used.

For a phase-swap slab the two outside-to-middle contact vectors are
`a=u_p`, `b=-u_q`. Consequently any moving diameter endpoint incident with
both boundary contact families requires

$$
|u_p-u_q|\ge1/D.
\tag{8}
$$

### Corollary 7: every ultra-small slab has an internal-contact loaded defect

Take a distinct-phase actual block swap in an open witness cell, with
`0<s=|u_p-u_q|<1/D`. Its fixed witness hub lies outside the moving slab. Every
moving old diameter endpoint has at least one old unit contact whose other
endpoint is also in the moving slab.

### Proof

Suppose a moving loaded endpoint has no internal unit contact. All of its
contacts then belong to the two boundary families. At most one contact from
each family can be incident with it, since a fixed unit vector determines one
neighbor. It has at least one contact by positive KKT support.

Two contacts contradict Lemma 6 because `s<1/D`. One contact makes it a contact
leaf with projective direction in the open cell. Theorem 5 makes it the fixed
witness hub, which is outside the slab. Both possibilities are impossible.
QED.

KKT slab balance supplies a moving diameter for every distinct-phase block.
Thus a slab all of whose loaded points have only boundary contacts is excluded.
This is a precise thin-slab criterion, not an assertion that every pair of
adjacent selected trains bounds such a slab. Arbitrary slabs may contain
transverse contacts, unselected trains, nonrhombic endpoint geometry, and long
internal contact paths.

### 7.1. Loaded-free pocket intervals force ONE-SIGN swaps

### Theorem 9: strict pocket phase order

Assume the actual fixed-witness O–O shore: two full-span diameter edges
`vx_-`, `vx_+` cross every retained cut, and their directions bracket the
open phase cell. Ordered cuts have two physical middle boundary arcs, and
their diameter-endpoint order agrees with hull order. Consider two cuts
`tau_p,tau_q`, `p<q`. Suppose the open boundary portion between their ends
on one host arc contains **no actual diameter endpoint**. The opposite host
arc is the only possible source of switching diameter endpoints.

Then the two train phases are distinct. All switching old diameters have
one common strict transverse sign, and their phase swap is ONE-SIGN.
Writing `m` for the coherent phase midpoint and `n_h` for the diameter
vectors directed into the middle slab, let `sigma` be their sign on `Jm`.
For real lifted phases in the open cell,

$$
\operatorname{sign}(\theta_p-\theta_q)=\sigma.
\tag{9}
$$

In particular, a loaded-free inner pocket on one host arc can contain many
retained train ends only with strictly monotone, pairwise distinct phases.
Every pair of its ends supplies a ONE-SIGN attempt, not a TWO-SIGN alternative.

### Proof of the geometric sign

The diameter-neighbor rays from `v` lie in a cone of aperture at most `pi/3`.
The ray of an interior cell direction separates the two hull arcs from `v`
to the witness partners. The far arc between `x_-` and `x_+` contains the
fixed exterior of every middle slab and no middle endpoint.

A diameter disjoint from both witnesses must cross them. Alternating convex
endpoint order puts its endpoints on the two opposite arcs from `v` to the
witness partners. Its vector directed to the negative arc has negative
`Jm` projection, and its vector directed to the positive arc has positive
projection. A diameter incident with `v` has the same sign by its endpoint's
side of the ray. One incident with just `x_-` or `x_+` has its other endpoint
on the opposite arc by alternation with the other witness, with the same
strict sign. The edge `x_-x_+`, if actual, has neither endpoint in the slab.
These cases exhaust the switching diameters. This is the fixed-star
transverse sign geometry proved independently in PR #599's nested-support
packet, with its actual-hull hypotheses retained.

Since the first middle arc has no loaded endpoint, every switching diameter
has its middle endpoint on the other arc. Thus all `n_h dot Jm` have the same
strict sign `sigma`.

### Proof of phase order and finite descent

Summing the full positive source KKT over the slab yields

$$
A_pu_p-A_qu_q=\sum_h\beta_h n_h,\qquad A_p,A_q,\beta_h>0.
\tag{10}
$$

There is at least one switching diameter. For unequal phases the left side
cannot vanish. If the phases were equal and there were no switching diameter,
translating the slab infinitesimally by `Ju_p` would preserve every active
contact and diameter to first order. It is a nonzero core motion and fixes
the three noncollinear witness vertices `v,x_-,x_+`, contrary to canonical
mixed core rigidity. The actual complete crossing grid guarantees a source
vertex in the slab between distinct cuts. This uses core rigidity and does
not extend a core theorem to isolated source points.

The transverse projection of (10) is

$$
(A_p+A_q)\sin((\theta_p-\theta_q)/2)
=\sum_h\beta_h(n_h\cdot Jm).
\tag{11}
$$

The right side has strict sign `sigma`, so equality of the two phases is
impossible and (9) follows. For `w=(u_p-u_q)/|u_p-u_q|`, equations (9)--(11)
give `n_h dot w>0` for every switching diameter. The open-cell non-grazing
estimate of the block-transposition theorem gives
`n_h dot w>D|u_p-u_q|/2`. Hence the exact swap strictly shortens every moving
old diameter. This proves ONE-SIGN, including when all switches are of only
one left/right type. QED.

For an actual inner pocket the loaded-free-arc condition follows from its
definition: its simple unit-contact path between consecutive loaded hull
vertices has no loaded vertex in its interior. It is enough that both cut
ends occur in the same such pocket on the same host arc. A pocket that spans
both host arcs or contains a resolved host transition is not included.

### Disjoint small-swap consequence and its limitation

On one host arc let pocket `F` contain `t_F` retained ends. Choose an integer
`R>=2` with `R-1>=8K`. Partition each such end list into disjoint consecutive
blocks of `R` ends. Their phases are strictly ordered, so the closest phase
pair in a block is also physically consecutive in that list, and its gap
is at most `4K/(D(R-1))<=1/(2D)`. The resulting physical slabs are disjoint
over the ordered host list and are all ONE-SIGN, with

$$
k\ge\sum_F\lfloor t_F/R\rfloor.
\tag{12}
$$

They can be fed directly into Theorems 1 and 8 and the Horn reduction.
Neither a linear value of (12) nor a contradiction follows merely from a
linear total end count. Many different pockets can each host one end. The
exact-phase pocket budget of PR #599 and convex contact-pocket phase order
do not eliminate this possibility. Convexity gives the same orientation as
(9), so an attempted opposite-order contradiction is rejected.

## 8. Exact regressions and verifier scope

Run

```
python3 research/verify_joint_swap_horn_loaded_defects_2026_10_01.py
```

The verifier documents finite rational truth tables and quadratic-field stress
packets; universal conclusions have the proofs above.

**Unequal parallel moves need a conflict clause.** Let `a=1/10`,
`h=1-a^2/16`, `r=(h,-a/2)`, `Delta_i=(0,a)`, `Delta_j=(0,a/2)`. The states
`00,10,01` have length strictly greater than one, while `11` has length `h<1`.
The displacements are exactly parallel. The old squared slack is positive and
of order `a^2`. This rejects ordinary implication-only closure for unequal
parallel swaps. It supplies no full train or global-optimality realization.

**The contact-leaf theorem has a genuine hub case.** The unit-separated source
`{0,(1,0),(-1/2,sqrt(3)/2),(-1/2,-sqrt(3)/2)}` has unit contact graph a three-leaf
star and diameter graph the outer equilateral triangle of side `sqrt(3)`.
Weights `alpha=1`, `beta=1/3` satisfy full positive normalized KKT. Each contact
leaf points strictly into its own diameter-star cell. The hub localization
holds, but this source is not a global minimum-diameter four-point source.

**Threshold directions admit leaves.** The collinear source `0,1,2,3` has
positive contact-path weights `alpha=3` and one diameter weight `beta=1`.
Its contact leaves point along the sole actual diameter direction. It is a
full positive first-order equilibrium, not a planar global optimum and not a
counterexample to the open-cell theorem.

**The geometric bound (7) is sharp.** With `D=41/18`, `p=0`, `x=(-41/18,0)`,
`a=(9/41,40/41)`, `b=(9/41,-40/41)`, the four rational source points
`p,x,p-a,p-b` are unit separated, have diameter `41/18`, and satisfy
`D|a+b|=1`. This packet has no full positive KKT certificate.

**A bounded isolate should follow its chamber.** The convex unit octagon

$$
(0,0),(1,0),(8/5,4/5),(8/5,9/5),(1,13/5),(0,13/5),
(-3/5,9/5),(-3/5,4/5)
$$

contains the strict isolate `(1/2,7/8)`. Translating its boundary by `(0,1/100)`
while keeping the isolate fixed produces an overlap. Translating the isolate
with the boundary preserves every source pair exactly. Its incident lengths
are all at most `sqrt(D^2-1)`, consistent with its nonextremality. This is an
exact chamber-dispatch packet, with no actual O–O train, ONE-SIGN or global
optimality certificate.

## 9. Implication chain and exact remaining gap

After actual train extraction and small-swap construction, Theorem 1 reduces
the simultaneous source competitor search to near-unit lower clauses on at
least `k-2d_H` groups. The Horn closure gives an exact finite witness for each
failed seed. Theorem 2 and Lemma 3 sharply constrain genuine conflict clauses;
Theorem 5 and Corollary 7 constrain the loaded endpoints of each attempted slab.
With the actual global stopped cuts, Theorem 8 further removes bounded
nonrhombic chambers and localizes every binary clause to the original outer
face; only unary rhombus thresholds remain in bounded faces.

The missing theorem is to exclude these return/conflict certificates in the
actual source, or to construct a second finite move that bypasses them. No
source-specific bound on the number of one-sided shore defects or contact
isolates has been proved. No unit equilateral triangle is forced by a
near-equilateral triangle of new clauses. No inactive pair is made active in
the original stress, and no source or smaller optimum is discarded.

The exact-phase gap-tree branch, split-star O–O branch, inactive-interface
branch, and macroscopic inactive-container branch remain separate obligations.
No Level I quantifier is weakened or claimed settled.
