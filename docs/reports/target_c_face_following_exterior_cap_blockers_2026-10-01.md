<!-- theorem-state: {"artifact_id":"ART-0F16990AFDE8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: face-following dispatch and exterior cap blockers

```text
complete O–O face protection + loaded cap threshold
 -> at most 170(per(F)-q) exterior lower-blocker labels
 -> r-d_H-170(per(F)-q) partial-rhombus / inner outer-pocket labels
 -> unresolved simultaneous release of that actual source system
 -> strict same-cardinality competitor / exact triangle / Level I consequence
```

**Date:** 2026-10-01.
**Original research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`.
**Starting checkpoint for this extension:** `bc965ea38ec30e9f24214517f7c7f8b36e144533`.
**State version:** `2026-09-14.audit.51`.
**Branch / mission:** `swarm/sol/gap-leaf-release-20261001`; continuation from
the exhausted finite in-cell exact-phase release to the nonconstant-phase
source blocker system.
**Classification:** proved candidates awaiting promotion for the standalone
geometry and the explicitly hypothesized finite dispatch; conditional C-II
application. Default artifact lifecycle: unreviewed.
**Level I:** OPEN. C-I CLOSED. C-II OPEN.
**Active prompt:** [Target C continuation](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md).

## 1. Authority and dependencies

Canonical inputs used here are:

- [Section 56](../targets/target-c/56-ci-restored-frontier.md): lexicographic
  triangle-free source normalization and full active support;
- [Section 67](../targets/target-c/67-rhombus-population-transport-audit.md):
  `F=conv B=conv V(G)`, convex bounded faces and convex outer pockets,
  retained isolates, and no source point inside a strict unit rhombus;
- [Section 77](../targets/target-c/77-inactive-chamber-saturation-audit.md):
  the exterior caps between consecutive loaded hull vertices;
- [local structure, Theorem 6.1 and Theorem 10.6](../theory/01-local-structure.md):
  contact trapping and stopped rhombus trains, including their two boundary ends.

The actual complete global O–O cut/chart hypotheses and ONE-SIGN finite swap
are **unpromoted**:
[block transposition](target_c_open_cell_block_transposition_2026-10-01.md),
[complete rectangle](target_c_oo_dual_tree_complete_rectangle_2026-10-01.md),
and [local immunity](target_c_tb1_swap_grid_local_immunity_2026-10-01.md).

The rooted isolate extension and blocker-tree arguments were inspected at
these exact research commits, and the useful steps are reproduced below:

- [PR #600 dispatch proof at `6b89f72e`](https://github.com/1337isnot1337/e-99/blob/6b89f72efae088096603d2be03a53fdac6ea2993/docs/reports/target_c_ultrasmall_swap_isolate_dispatch_2026-10-01.md);
- [PR #598 blocker tree at `8ae89a3c`](https://github.com/1337isnot1337/e-99/blob/8ae89a3cb7a8d664260201e4b174505834a01c33/docs/reports/target_c_common_swap_blocker_arborescence_2026-10-01.md).

Their lifecycle remains unreviewed. This report does not import their application
as canonical. The asymptotic specialization additionally uses the unpromoted
[rooted endpoint ledger](target_c_wrapping_root_defect_stability_2026-09-30.md),
specifically `per(F)-q=o(D)` and `d_H=o(D)`. It does **not** use
`Q_local=o(D)` as a bound on the global exceptional-face degree.

## 2. A loaded hull side with an exterior point has length at least sqrt(3)-O(1/D)

Let A be any finite unit-separated planar source of diameter D. Let B contain
**all** actual diameter endpoints, let F=conv B be two-dimensional, and let
`ab` be a side of F of length L<D. A source point on the exterior side of its
supporting line forces

\[
 \boxed{(1+D^{-2})L^2+2L/D\ge3,\qquad
 L\ge\tau_D:=\frac{3D}{\sqrt{3D^2+4}+1}.}                 \tag{1}
\]

This theorem requires neither global optimality nor contact equilibrium.
It applies to every source point, including isolates. In particular,
`tau_D=sqrt(3)-D^{-1}+O(D^{-2})`.

### Proof

Put `a=(-L/2,0)`, `b=(L/2,0)`, with F below the horizontal line. Choose actual
diameter partners c,d in B with `|c-a|=|d-b|=D`. The remaining upper constraints
give `c_x>=0` and `d_x<=0`, and `c_y,d_y<=0`. Write

\[
 c-a=(A_0,-C),\qquad d-b=(-B_0,-E),
 \quad A_0,B_0\ge L/2>0,\quad C,E\ge0.
\]

Let alpha,beta in `(0,pi/2]` be the angles of these vectors from the downward
vertical on the two sides, and put theta=alpha+beta. Since

\[
 |(c-a)-(d-b)|=|c-d+(b-a)|\le D+L<2D,
\]

we have theta<pi and

\[
 2D\sin(\theta/2)\le D+L.                               \tag{2}
\]

The two diameter disks give the tangent half-plane inequalities

\[
 -A_0(x+L/2)+Cy\le0,\qquad
 B_0(x-L/2)+Ey\le0.                                    \tag{3}
\]

Together with `y>=0`, these half-planes bound a triangle T with base ab and
apex angle `pi-theta`. A vertical side is permitted if C or E is zero;
theta<pi excludes two parallel vertical sides. Every source point above ab
lies in T, and its horizontal projection lies strictly between a and b.

The circumdisk of T contains T. Any z in T above ab therefore sees ab under
an angle at least `pi-theta`. With `r=|z-a|>=1`, `s=|z-b|>=1`, the cosine law gives

\[
 L^2\ge r^2+s^2+2rs\cos\theta
       =(r-s)^2+2rs(1+\cos\theta)
       \ge4\cos^2(\theta/2).
\]

By (2), `4cos^2(theta/2)>=4-(1+L/D)^2`. Rearrangement proves (1).
The positive quadratic root equals the stated tau_D. QED.

## 3. Exterior extreme vertices and short pairs cost loaded-side excess

Put `q=|B|`, `P_F=per(F)`, and `E_F=P_F-q>=0`. Assume

\[
 \boxed{D\ge6,\qquad 1+E_F\le D/4.}                     \tag{4}
\]

Every hull side has length at least one, and at most `1+E_F`. Hence every
nonempty exterior cap has base `3/2<L<=D/4`, by (1). For its tangent triangle,
(2) gives `cos(theta/2)>=sqrt(39)/8`. The sine rule gives

\[
 \frac{\text{two apex-side lengths}}L
 =\frac{\sin\alpha+\sin\beta}{\sin(\alpha+\beta)}
 =\frac{\cos((\alpha-\beta)/2)}{\cos(\theta/2)}
 \le\frac8{\sqrt{39}}.                                 \tag{5}
\]

Each convex cap is contained in T, so convex perimeter monotonicity, after
subtracting the common base, bounds its source-hull arc by `8L/sqrt(39)`.
If that arc has t extra extreme source vertices, unit separation gives arc
length at least t+1. Since `L<=3(L-1)` on the nonempty caps,

\[
 \boxed{|Vert(conv A)\setminus B|
 \le\frac{24}{\sqrt{39}}E_F.}                           \tag{6}
\]

This is a bound on the number of extra **extreme vertices**, not on the total
exterior population. A cap can still contain a large inactive cloud.

Let `r<=13/12`, and draw all source pairs of length at most r. Every vertex
has at most nine neighbors in this graph: disjoint radius-1/2 disks at those
neighbors and the vertex lie in its radius-`r+1/2` disk, so

\[
 N+1\le4(r+1/2)^2\le361/36<11,
 \qquad N\le9.                                        \tag{7}
\]

Any exterior point having such a pair to a point in F lies at height at most r
above its cap base. Its horizontal projection lies on that base by (3).
Radius-1/2 disks at all such exterior points lie in a rectangle of area
`(L+1)(r+1)`. Using pi>3 and L>3/2 bounds their number by

\[
 \frac4\pi(L+1)(r+1)
 <\frac{25}9(L+1)\le\frac{125}{27}L<5L.
\]

Thus at most `15E_F` exterior points have a length-at-most-r pair to F, and

\[
 \boxed{\#\{xy:|xy|\le r,\ x\notin F,\ y\in F\}
 \le135E_F.}                                          \tag{8}
\]

No packing density or near-disk limit has entered (6)--(8).

## 4. Bounded exceptional faces follow every complete O–O cut

Let G be the canonical full unit-contact core, and let tau be a **complete
global** stopped O–O train with the exact cutset property. A train edge incident
to a bounded nonquadrilateral face would be a boundary edge of the global
strict-rhombus complex at which the stopped train has an I end. That is
incompatible with both ends being O. Thus no edge on such a face boundary belongs
to tau. Since its boundary is a connected contact cycle, every boundary vertex
lies on the same shore of the tau cut.

For any selected family of these cuts, all boundary vertices of a bounded
exceptional face consequently have the same full cut-indicator vector. Every
physical slab or union of disjoint slabs moves them equally. Assign every
contact isolate in the face that same displacement. Then **all** pairs between
source points in that closed face are unchanged, including inactive diagonals.

This assertion fails for a train stopped on the exceptional face, for a train
of a smaller selected rhombic complex, and for an old outer-face pocket where
an O end is allowed. Global completeness is an essential hypothesis.

## 5. Face-following is compatible with the long-pair dispatch

Set `L_D=sqrt(D^2-1)` and draw T^+ on all source pairs longer than L_D.
Here are the geometric facts and rooted construction needed from PRs #598/#600.

1. Every T^+ endpoint is extreme: for a nonextreme p, the variance identity
   for a convex combination of other source points gives
   `|p-y|^2<=D^2-1` for every y.
2. Disjoint T^+ edges cross. Otherwise their four extreme endpoints form a
   convex quadrilateral with the two long edges as opposite sides; an angle
   at least pi/2 yields a diagonal longer than D, using unit separation on
   the incident short side.
3. Every convex straight-line thrackle subgraph has `e<=v`: choose the first
   clockwise incident edge at each extreme vertex. An edge unchosen at both
   ends would have two preceding edges in opposite open half-planes, disjoint
   from each other, contradicting the thrackle condition. Thus the choices
   cover all edges.

All new T^+ endpoints outside B are contact isolates, by canonical trapping.
Let F_B comprise the components of `T^+ minus H` touching B. Root a forest
at B by directing each new vertex toward one neighbor decreasing its graph
distance to B. If Z_B is the set of new vertices here, the forest has |Z_B|
edges. The remaining edge set J satisfies

\[
 |J|\le |B|-|H|=d_H                                  \tag{9}
\]

by applying `e<=v` to `H union F_B` on `B union Z_B`. A new vertex inherits
its forest root's displacement; every isolate-only T^+ component translates
with one common fixed reference displacement. This preserves every inactive
long pair outside J.

**Modification:** every isolate in a bounded exceptional face instead follows
that face, as in Section 4. Such a point is in F but outside B and is not extreme
in `conv A`, so it has no incident T^+ edge by item 1. The modification therefore
changes neither the rooted forest nor J. Give every other nonlong isolate the
common reference displacement (zero for binary swaps).

For a binary displacement cloud `{0,Delta}` of amplitude
`s<=1/(2D)<D-L_D`, every inactive nonlong pair stays strictly below D. All old
contacts and diameters are affected exactly as in the prescribed core move.
Every source point is retained. The construction is fixed before choosing
which of the disjoint physical modules to move and commutes with their unions.

The only exterior isolates receiving a nonreference displacement belong to
T^+. They are extra extreme vertices counted by (6). All short pairs incident
to those vertices number at most `216E_F/sqrt(39)` by (7). Every other changed
short pair with an exterior endpoint has its other endpoint in F, and is counted
by (8). Thus the static universe of possible exterior lower-blocker labels has
size

\[
 \boxed{N_{\rm exterior}\le
 (135+216/\sqrt{39})E_F\le170E_F.}                     \tag{10}
\]

For this statement use `r=1+s<=13/12`, as ensured by D>=6. The total exterior
isolate population is never replaced by the count of extreme vertices.

## 6. Source-level consequence for common-vector ONE-SIGN modules

Assume r disjoint nonempty physical core slabs share one nonzero Delta with
`s<=1/(2D)`, preserve every old contact, strictly shorten every changed old
diameter, and each change at least one diameter. Assume the complete O–O
hypotheses of Section 4 and (4). Extend them by Section 5.

The source-anchored blocker tree has r distinct inactive pair labels. For
completeness: an actual diameter cannot connect two movable modules, because
its two individual changes would have squared lengths summing to
`2D^2+2s^2>2D^2`. Hence every nonempty union of modules still shortens at least
one old diameter and increases none. If all changed inactive pairs stayed
strictly between 1 and D, that union would contradict diameter minimality or
diameter-pair minimality, with contact count unchanged. Every union therefore
has an outgoing inactive blocker. Root reachability and shortest-path choice
give an outgoing arborescence toward the fixed source, with r distinct actual
source-pair labels. An unordered pair could repeat only on a forbidden two-cycle.

At most d_H labels are upper blockers, by (9). Every remaining label has
`1<|xy|<=1+s`. At most `170E_F` of these have an exterior endpoint, by (10).
Therefore

\[
 \boxed{N_{\rm residual}\ge
 \max\{0,r-d_H-170(P_F-q)\}.}                         \tag{11}
\]

For k disjoint ONE-SIGN swaps with different vectors, the same fixed dispatch
and endpoint charging instead give

\[
 N_{\rm residual}\ge
 \max\{0,\lceil k/2\rceil-d_H-170(P_F-q)\}.            \tag{12}
\]

The exact disposition of each residual label follows from short-pair planarity.
Every pair shorter than sqrt(2) is a strict Gabriel edge: a source point in its
closed diameter disk would have sum of squared distances to its ends below 2.
Two such edges cannot properly cross: an angle at least pi/2 in their endpoint
quadrilateral would yield one of the crossing diagonals at least sqrt(2).
Thus the new pair is cofacial in G, with no source point in its open segment.

Both ends of a residual label are in F. It cannot lie in a bounded exceptional
face by Section 4. A rhombus contains no isolate, so in a rhombus it is one
diagonal. Local immunity excludes every transverse train crossing both swapped
boundaries. The remaining possibilities are exactly:

1. a short diagonal in a rhombus whose transverse train crosses exactly one
   swapped boundary and whose phase threshold is in the swept interval; or
2. a short chord in an **old outer-face pocket inside F**, possibly involving
   an isolate there.

At the conditional rooted endpoint, `d_H=o(D)` and `P_F-q=o(D)`. Hence a
linear family of small ONE-SIGN attempts forces linearly many labels of these
two types. Bounded exceptional faces, exterior cap/core pairs, and dispatched
long-pair isolates contribute only zero or o(D) labels. This is a finite
source-preserving reduction; it supplies no multiplier for an inactive edge.

### 6.1 Triangular inner pockets also supply only o(D) labels in a narrow shore

Assume in addition the near-disk rooted specialization: `D^{-1}F` converges
to the radius-1/2 disk, `E_F=o(D)`, and all retained train directions lie in
one real/projective window of width o(1), as supplied by the width-4K/D shore.
Exact equality of phases is **not** required for this paragraph.

A triangular pocket has a two-unit-edge contact path. A retained end on one
of those edges forces its closing hull side of length L to make angle
`arccos(L/2)` with that edge. For L=1+o(1), the side direction lies in one of
two shrinking windows about the shore reference phase plus/minus pi/3.
The uniform near-disk directional-count proof in
[pocket budget Section 5](target_c_exact_phase_pocket_end_budget_2026-10-01.md)
gives o(D) such sides; the at-most-`E_F/epsilon` sides with L>1+epsilon
are separately o(D) for each fixed epsilon, before epsilon tends to zero.

There is no isolate in a two-unit-edge triangle: the triangle lies in the
closed unit disk about the common contact vertex, and every other point in
its interior is strictly closer than one to that vertex. Its only initially
strict corner pair is the closing hull side. If neither contact edge belongs
to a retained boundary train, all three corners have the same cut vector,
so this pair is unchanged. Otherwise the pocket has a retained end and is
one of the o(D) counted pockets. Consequently triangular pockets contribute
only o(D) distinct lower-blocker labels even on a nonconstant-phase shore.

Thus a linear disjoint ONE-SIGN population at the conditional rooted endpoint
forces linearly many partial transverse-rhombus labels or inner-pocket labels
with **at least three unit-contact boundary edges**. No bound on all pocket
perimeters or on global Q has been substituted for this narrow-direction proof.

## 7. Sharpness, failed extensions, and the remaining attack

The asymptotic sqrt(3) base threshold cannot be increased. For every integer
D>=10 put

\[
 L=\sqrt3+D^{-1},\quad r=1+(100D)^{-1},\quad
 H_0=\sqrt{D^2-(D+L)^2/4},\quad
 h_0=\sqrt{r^2-L^2/4},
\]

and take

\[
 a=(-L/2,0),\ b=(L/2,0),\
 c=(D/2,-H_0),\ d=(-D/2,-H_0),\ z=(0,h_0).
\]

The actual diameter pairs are exactly ac, bd, cd. All other distances exceed
one, so the contact graph is empty and the source is triangle-free. The point
z lies above the side ab of the loaded hull. Indeed `r^2<L^2/3` gives
`h_0<L/(2sqrt(3))`, while
`H_0<sqrt(3)D/2-L/(2sqrt(3))`; hence `|z-c|,|z-d|<D`.
The remaining squared distances are `L^2`, `r^2`, and `D^2-DL`, all strictly
between 1 and D^2. This is an exact geometric regression, not a canonical
source or global minimizer. A five-point unit-spaced line has diameter 4<D.

Rejected extensions:

- `L<2` does not imply an empty cap: the above family has L<2 and an exterior
  isolate for all D>=10.
- (6) does not bound all exterior source points. Only extreme points and the
  short-distance boundary strip were counted; inactive cap interiors survive.
- A bounded-face argument does not protect old outer pockets. Selected O–O
  train ends may lie on their contact boundary, so that boundary can have
  several physical slab labels. Global `Q` remains unrelated to `Q_local`.
- (11) does not rule out a linear number of partial transverse trains or
  inner-pocket chords. Both are still allowed by the global interface budget.

**Exact next obligation:** prove, from actual KKT equilibrium plus complete
train cut embedding and lexicographic minimality, that the two residual types
cannot provide an outgoing blocker for every nonempty union of a linear
small-swap population; or explicitly integrate a second motion releasing them.
The inner-pocket alternative must be tracked even when local harmonic face
defect vanishes. TWO-SIGN, few-phase, exact-phase staircase, split-star,
inactive-interface, macroscopic-container and other full-core branches also
remain open. No canonical route/state is changed.

## 8. Computation and promotion recommendation

[Exact verifier](../../research/verify_target_c_face_following_cap_blockers_2026_10_01.py):
finite rational sources for the cap threshold, tangent perimeter and degree
checks; radical interval certificates for the sharpness family; and exhaustive
binary face-color incidence checks. See its documented universe in
[research README](../../research/README.md). These computations do not supply
global optimality, KKT, or the complete O–O extraction. The universal claims
above have analytic proofs. No literature theorem is imported without proof.

Executed certificate results: 577 eligible finite loaded-hull packets, 248
nonempty caps, five rational five-point regressions, 58 radical sharpness
packets, and all 2,040 binary face colorings (16 monochrome survivors): PASS.

**Recommendation:** retain as unreviewed research pending an independent hostile
audit. The implication to (11)--(12) is conditional on the explicit finite
source/chart hypotheses and the checked unpromoted dispatch ancestry. The
threshold theorem itself concerns arbitrary unit-separated sources.
