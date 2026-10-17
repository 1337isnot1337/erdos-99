<!-- theorem-state: {"artifact_id":"ART-05217F7EB24A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — disjoint cap reactions expel repeated-swap blockers to inactive interfaces

`disjoint cap reaction capacity -> at most fourteen outer-to-outer rhombus labels in an alternating common-swap tree -> at least r-d_H-14 genuine inactive-interface witnesses -> finite release at those interfaces still required`

**Date:** 2026-10-01  
**Shared starting HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`  
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`  
**Checkpoint before this result:** `8ae89a3cb7a8d664260201e4b174505834a01c33`  
**State version:** `2026-09-14.audit.51`  
**Mission / branch:** TB1 lower-constraint closure; `swarm/tb1-diameter-order-20261001`.  
**Classification:** proved candidate awaiting promotion; conditional train application; exact geometric regressions. Artifact lifecycle remains unreviewed.  
**Level I / C-II:** OPEN / OPEN.

## 1. Abstract cap theorem on the actual normalized source

Let A be a triangle-free global minimizer in the canonical C-II normalization
C=C_* and H=H_*, with D>=2. Retain every source point. Let B be the actual
diameter endpoints, ordered around the source convex hull, and put

\[
\delta_D=2\arcsin(1/(2D)).
\]

Let S_1,...,S_N be pairwise disjoint source shores with these properties:

1. B intersect S_i is a consecutive cyclic block in the B-order. The blocks
   occur in disjoint boundary intervals, with their chosen first-to-last order;
2. every contact crossing S_i is oriented from its complement into S_i with
   the same unit vector u_i, and at least one such contact exists;
3. the projective directions of u_i lie in a single interval J of width
   0<=W<pi/2.

Then

\[
\boxed{N\le 2\lfloor W/\delta_D\rfloor+6.} \tag{1}
\]

In particular, W<=1/(2D) gives N<=6. No lower bound on any KKT coefficient,
no diameter-count saturation, and no contact-isolate bound is assumed.
The hypothesis is about disjoint cap shores. Nested full-width train shores
do not satisfy it.

### 1.1 The cut reaction is nonzero and has both transverse signs

Take a relative-interior positive full-support normalized KKT stress on the
actual contacts and diameters. Summing its equilibrium on S_i cancels all
internal forces. Contact isolates contribute zero and stay in the source.
For A_i=sum_{e in delta_C(S_i)} alpha_e>0,

\[
A_i u_i=\sum_{h=xy\in\delta_H(S_i),\ y\in S_i}\beta_h(p_y-p_x),
\qquad\beta_h>0. \tag{2}
\]

If the diameter transverse projections on Ju_i did not have both signs,
their positive sum being zero would make every projection zero. There is
only one actual diameter segment in a given projective direction: for two
parallel segments Du with midpoint translation v, the two cross distances
|Du+v|,|Du-v|<=D imply v=0 after squaring and adding. Hence the only crossing
diameter would have oriented vector Du_i by (2).

Translate the entire full-source shore S_i by

\[
\Delta_\theta=R_\theta u_i-u_i.
\]

Every crossing old contact becomes R_theta u_i, so every old contact stays
unit. The crossing diameter satisfies

\[
|Du_i+\Delta_\theta|^2
=D^2-2(D-1)(1-\cos\theta)<D^2
\]

for nonzero small theta. Every initially strict pair retains its strict
lower and upper slack for sufficiently small theta because the source is
finite. Same-shore old diameters are unchanged. This gives either diameter
less than D, or another triangle-free global minimizer with the same
contacts and fewer diameters. Both contradict the normalization.

Thus each cut has actual diameter vectors on both sides of u_i. This is
also an independent finite proof of the scoped two-sided bracing fact
needed here; an infinitesimal velocity has not been silently integrated.

### 1.2 Disjoint loaded blocks give disjoint normal spans

For an actual diameter xy, orient n=p_y-p_x toward its endpoint y in S_i.
For every other source point z,

\[
n\cdot(p_z-p_y)
=\frac{|p_z-p_x|^2-D^2-|p_z-p_y|^2}{2}
\le-\frac{|p_z-p_y|^2}{2}<0. \tag{3}
\]

Thus y is extreme and n lies strictly inside the outward normal cone at y.
The closed vertex normal cones of the full source hull partition the normal
circle, with only endpoints shared. For each loaded block take the circular
normal span I_i from the first vertex's initial normal to the last vertex's
final normal, in its specified boundary order. Unloaded extreme isolates
between loaded vertices merely occupy gaps inside these spans. Disjoint
loaded blocks in disjoint boundary intervals give spans with disjoint
interiors. Their widths sum to at most 2pi.

The nonzero reaction (2) implies that every block is nonempty. It also rules
out a shore containing all diameter endpoints: such a shore would have
no crossing diameter. Therefore the cyclic first-to-last spans are proper.

At most two I_i have width at least pi. Discard those at a cost of at most
two shores. For each remaining span, its width is less than pi. All
positively weighted vectors in (2) belong to its pointed normal cone, so
the oriented reaction direction u_i lies between the extreme crossing
diameter directions. Let E_i be the closed interval between those extremes
on this lift. Section 1.1 makes u_i strictly interior to E_i.

Any two distinct actual diameter directions have projective separation
at least delta_D. For incident diameters this follows from unit separation
of their other endpoints; for disjoint diameters the canonical equal-diagonal
lemma gives the stronger 2delta_D separation. Consequently

\[
|E_i|\ge\delta_D. \tag{4}
\]

The E_i have disjoint interiors because E_i is contained in I_i.

### 1.3 Count normal intervals meeting the reaction window

The projective interval J lifts to two opposite oriented windows of width W
on the normal circle. An E_i either lies entirely inside its reaction's
window or crosses an endpoint of that window. At most two disjoint E_i can
cross endpoints of each window. All other E_i assigned to that window
have total width at most W, hence number at most floor(W/delta_D).

Both windows together therefore accommodate at most
2 floor(W/delta_D)+4 narrow normal spans. Restoring the at most two wide
spans proves (1). Since delta_D>1/D, W<=1/(2D) has floor(W/delta_D)=0.

This proof keeps actual vector directions, positive reactions, convex
normal order, and finite lexicographic descent. Connectivity or abstract
matrix rank alone does not imply (1).

## 2. Repeated two-phase swaps in one complete rectangle

The following application is conditional on the checked actual global
train-cut/rectangle hypotheses used in the October 1 proof-only reports.
It does not assert that every nonconstant phase shore supplies this family.

Take selected A-trains in their nested crosscut order with alternating
directions

\[
u,v,u,v,...,u,v \qquad (2r\text{ selected trains}), \tag{5}
\]

where u has angle x and v has angle y>x, and

\[
0<\varepsilon=y-x\le1/(2D).
\]

The slab between the (2i-1)-st and 2i-th selected train is L_i, and all
slabs use the same Delta=v-u. Require the ONE-SIGN conditions: every old
contact is preserved, every changed old diameter strictly shortens, and
each L_i changes at least one old diameter. Require the same actual
complete opposite shore B as in the four-host theorem. In a common phase
chart its directions have angle pi/3+b with b>y and the whole reduced
phase range has width less than pi/3.

Use the move-independent rooted isolate dispatch. It enlarges each L_i
only by contact isolates and leaves at most d_H=q-h upper-distance tree
labels. Since |Delta|=2sin(epsilon/2)<=1/(2D), the common-swap arborescence
has at least r-d_H distinct near-unit lower labels.

**Claim.** Among its chosen lower labels, at most fourteen are rhombus
diagonals whose transverse complete train is outer-to-outer. Therefore
at least

\[
\boxed{\max\{0,r-d_H-14\}} \tag{6}
\]

labels either are cofacial in a non-rhombic or exterior face, or are
rhombus diagonals whose transverse train has a bounded nonquadrilateral
terminal occurrence.

### 2.1 A blocking transverse train crosses only one selected cut

A source pair of length at most 1+|Delta| is a strict Gabriel edge for
D>=2, so a lower label lies in one face of the old contact graph. A strict
unit rhombus contains no extra source point, including an isolate: its
short-diagonal triangulation has circumradius at most 1/sqrt(2), and
vertex Voronoi regions cover it within that radius. Thus a rhombus label
is the short diagonal between two corners.

The complete-grid local immunity calculation applies whenever its
transverse train sigma crosses both swapped boundary trains. Such a
rhombus cannot block. A rhombus that blocks consequently crosses exactly
one boundary, and the phase threshold of sigma lies in the swept phase
interval. On the common lift the two possibilities are

\[
\begin{array}{c|c|c}
\text{sigma direction}&\text{allowed selected phase}&\text{forbidden phase}\\
\pi/3+t,\quad x<t\le y&u&v\\
-\pi/3+t,\quad x\le t<y&v&u.
\end{array} \tag{7}
\]

Indeed, in the first row the old acute rhombus angle is pi/3+t-x>pi/3
and the swapped angle is pi/3+t-y<=pi/3. The second row is the reversed
acute-angle lift pi/3+y-t>pi/3 versus pi/3+x-t<=pi/3.
In each row a forbidden-phase crossing would already violate the strict
rhombus angle bound.

The support of any train on the selected dual path is an interval: its
path through the complement dual tree intersects that path in a connected
interval. This uses train pseudosegment behavior, not an Euler inference
about the diameter graph. Alternation (5) then implies that sigma crosses
exactly one selected A-train.

Two different chosen rhombus labels cannot use the same sigma. Such a
sigma crosses only one selected boundary, crosses it in at most one
rhombus, and that rhombus has only one short diagonal. Also, every such
label joins L_i to the fixed core: the face contains only one selected
cut, so its four corners cannot belong to two different moving slabs.
Thus it is an i-to-0 arborescence arc. Isolate dispatch cannot alter this
fact, since all rhombus corners have old contacts. At most one chosen
label is based on each slab.

### 2.2 Interior outer-to-outer blockers are disjoint outer caps

Discard labels using the first or last selected A-train. There are at
most two, by the i-to-0 observation above.

For any remaining sigma, the single selected A crossing is internal.
Both terminal layers are adjacent interior layers. If sigma is
outer-to-outer, its boundary endpoints therefore lie on A-host intervals:
the two B-host intervals have the extreme A-layers 0 and 2r.

Sigma does not cross any retained B-train. In the first row of (7) its
projective distance from pi/3+b is b-t<pi/3. In the second row it is
pi/3+t-b<pi/3. Therefore both sigma endpoints lie on the same A-host
interval; opposite A-hosts are separated by every retained B-crosscut.

Take the cap shore bounded by sigma and the intervening arc of that host.
The boundary arc contains exactly one selected A endpoint. Within either
phase band of (7), sigma trains are noncrossing. Their host arcs cannot
nest: the larger would contain both the inner selected endpoint and its
own distinct selected endpoint, forcing two selected crossings. Hence
the cap shores in one band are disjoint and their loaded endpoints form
disjoint consecutive hull-order blocks.

The actual train cut law gives precisely the uniform oriented contact
cut in Section 1. This cut law and the four-host realization are explicit
application hypotheses, rather than assumptions about an abstract grid.
The cap reactions in each band have projective width epsilon. Equation
(1) bounds each band by six. Adding two bands and the two extreme labels
gives fourteen, proving (6).

Every non-outer-to-outer sigma here is nonsingleton because it crosses
an actual rhombus. A complete stopped train can stop at a bounded face
only when that face is nonquadrilateral. The rhombus branch of (6) thus
provides distinct actual trains reaching bounded inactive interfaces.
It does not provide distinct faces; many endpoints may lie on one face.

## 3. Exact regression: geometry permits many outer rhombus blockers

Let phi=2atan(t), t=1/(10000r), and use unit directions

\[
u=(1,0),\quad v=R_{2\phi}u,\quad
\sigma=R_\phi(1/2,\sqrt3/2),\quad
b=R_{3\phi}(1/2,\sqrt3/2).
\]

All coordinates are in Q(sqrt(3)). Make a three-column additive grid
whose successive row increments are u,u,v,v repeated r times. Along the
second u-edge of each block on the column-zero boundary, attach the unit
rhombus with transverse side -sigma. Its two new vertices form an outer
tooth cap. Swapping that u-row with the following v-row preserves every
old unit contact but makes the tooth short diagonal strictly shorter
than one.

The verifier certifies packets with r=2,3,5,10. The largest has 143
points, 232 unit contacts, one actual diameter, and ten distinct rhombus
blockers. All source pairs are checked for unit separation; the entire
old contact graph is checked to be triangle-free. Every individual swap
preserves all old contacts and the old diameter. Each cap has exactly
two crossing contacts parallel to sigma and no crossing diameter.
Thus positive KKT equilibrium fails exactly at (2); each moving slab
also fails the arborescence premise of changing an old diameter.

This is a regression against a geometry-only cap claim, not a global
minimizer and not a counterexample to Level I. Placing a tooth after an
isolated u preceded by v fails unit separation; the repeated u,u,v,v
pattern is needed for the certified packet.

Nested shores are a separate failure of the disjointness premise. A
single diameter may be used by arbitrarily many nested abstract cuts.
Their normal spans overlap, so they cannot be charged independently in
Section 1. Neither paths nor stars contradict this scoped theorem.

## 4. Dependencies, verification, and remaining obligation

Canonical inputs: the normalized full-source C-II setup, positive
relative-interior equilibrium, actual diameter endpoints, finite slack,
and the diameter-direction spacing in
[Section 66](../targets/target-c/66-forest-doubled-gap-audit.md).
The positive-contact-core/isolated-point scope is that of
[Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md);
the proof does not extend its matrix to isolates.

The train application uses checked but unpromoted actual cut/chart
statements in
[the complete O-O rectangle report](target_c_oo_dual_tree_complete_rectangle_2026-10-01.md),
[the four-host joint-switch report](target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md),
and [the exact block transposition](target_c_open_cell_block_transposition_2026-10-01.md).
The two-sided cut proof was also checked against the audited-working
[Sections 156–157](../targets/target-c/156-157-face-closure-and-outer-train-bracing-audited.md),
and is reproved in Section 1.1 from the stated cut hypothesis.
The isolate dispatch and arborescence are proved candidates in this PR,
not canonical premises.

Run
`python3 research/verify_target_c_disjoint_cap_reactions_2026_10_01.py`.
It uses exact Fraction/Q(sqrt(3)) arithmetic for every distance, old
contact, diameter, and swap in the tooth packets. It also exhausts 1,440
finite circular interval packets and 110 alternating-cut supports.
The interval calculation checks the counting reduction on a finite
mesh. It omits actual Euclidean source realization, stress, normalization,
and train extraction. The universal theorem is the analytic proof above.

The implication chain has advanced from unspecified cofacial near-unit
labels to the actual inactive-interface alternatives (6). It has not
advanced to a feasible finite release. In particular:

- the existence of a linear alternating common-vector ONE-SIGN family
  is not supplied for arbitrary nonconstant phases;
- non-rhombic chords can accumulate in one large inactive face;
- many distinct bounded-end trains can terminate on one face;
- a near-unit pair is not an active constraint and has no asserted
  positive KKT weight;
- global inactive perimeter is only O(D), and the local harmonic o(D)
  defect ledger cannot be substituted for it.

The next concrete attack is to pair bounded train ends on one actual
inactive face and determine whether an exact two-train phase swap can
repair these blockers while satisfying that face's vector closure.
The exact-phase, split-star O-O, inactive-interface, macroscopic-container,
and remaining full-core C-II branches all remain open. No promotion or
Level I closure is claimed.
