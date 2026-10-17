> Generated reading edition · [exact source](../../../docs/reports/target_c_antitone_interval_scc_release_2026-10-03.md) · source SHA-256 `38edafb753427da0bafdbf935a2de7808122da6fae674f221f8bd8fecec157a0`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-47E171EDF5D1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — antitone interval SCCs and exact contact release

**Date:** 2026-10-03
**Base:** `7a327e1ad95cd2e9cb035b9b96fb34fd8f12114d`
**Classification:** proved candidate awaiting promotion; source consequence
conditional on the explicitly listed physical cut hypotheses.
**Level I / C-II:** STILL OPEN. No canonical status is changed by this report.

## 1. Exact chain and scope

The chain attacked is

`actual full-span open-cell witness + ordered physical crosscuts -> antitone
directed diameter relation -> proper interval terminal SCC -> inactive
inverse-D witness or exact contact release -> exclusion of the interleaved
non-strong branch when inactive near-activity is absent`.

The graph theorem below is unconditional for every finite antitone directed
relation. The geometric lift is proved from explicit actual-hull crosscut
hypotheses. The source move checks every source point and every source pair.
Its application to the current fixed-star complete O--O branch depends on
that branch's still-unpromoted source cut/co-embedding reductions. It is not
an unconditional C-II closure or a promotion of those reductions.

After this proof was written, the next all-refs overlap check found commit
`ae4a8657`, containing `target_c_open_cell_antitone_condensation_2026-10-03.md`.
That concurrent report already proves the graph theorem, source fork using
core rigidity, and open-cell paired-staircase extension. We make **no
first-discovery claim** for those conclusions. This report independently
audits them and adds the exact finite contact-release mechanism below, which
avoids the core rank input, and the stronger two-rail physical packet count.
The threshold exact-phase staircase predecessor is also credited below.

## 2. Finite ordered graph theorem

Let G be a finite directed multigraph on an ordered vertex set
`{0,...,m}`. Loops may be ignored. Call its directed support **antitone** if

```math
(a\to b),(c\to d),\quad a<c\quad\Longrightarrow\quad b\ge d.
\tag{AI.1}
```

Parallel edges do not alter this condition or the SCCs.

**Theorem AI.** Every minimum-span source or sink SCC is an interval of
the ordered vertex set. Consequently, if G is not strongly connected,
it has a proper interval SCC with no incoming edge or no outgoing edge.

**Proof.** First every simple directed cycle has length at most two.
On the vertices of a simple cycle its successor map is a bijection.
Condition AI.1 makes it order-reversing; a finite order-reversing bijection
is the unique reversal of the ordered set and its square is the identity.
A cycle of length greater than two is therefore impossible.

Every directed edge internal to an SCC with distinct endpoints lies on a
simple directed cycle. Thus its reverse edge is present. The collapsed
internal undirected graph of each SCC is connected and has no cycle:
an undirected cycle, with its paired orientations, would give a directed
simple cycle of length at least three. Hence each nontrivial SCC has a
paired underlying tree.

Choose, among all source and sink SCCs, one C minimizing
`span(C)=max(C)-min(C)`. Suppose C is not an interval. Write its extremes
as l,r and let H=`{l,...,r}\C`, which is nonempty. For every x in H, the
connected internal tree of C has an edge a--b with `a<x<b`: along a tree
path from l to r some edge crosses the gap at x. Both a->b and b->a exist.

If x->y is any edge, comparison with a->b and b->a in AI.1 gives
`a<=y<=b`. If y->x is any edge, `y<a` would give `x>=b`, while `y>b`
would give `x<=a`; both are impossible. Thus **every edge incident to x
stays within [a,b]**, in particular within [l,r].

If C is a source SCC, no edge from H goes to C. The preceding confinement
also excludes edges from H to outside [l,r]. Therefore H is closed under
outgoing edges and contains a globally sink SCC. Its span is strictly
smaller than r-l, since neither extreme belongs to H. This contradicts
the choice of C. If C is a sink SCC, H is closed under incoming edges and
contains a globally source SCC of smaller span. The contradiction proves
the interval assertion. If G has more than one SCC, the chosen interval
is proper. QED.

This argument does not require an Euler path, node balance, stress weights,
or full rank. It also covers isolated weak components: they are both source
and sink components and participate in the minimum-span choice.

## 3. Exact geometric lift from a full-span open-cell wall

Assume all the following statements about the **same** finite source:

1. Every actual diameter endpoint is on the boundary of the actual loaded
   convex hull F. The diameter chords are a geometric thrackle: disjoint
   actual diameter chords cross properly.
2. Selected proper crosscuts `tau_1,...,tau_m` are disjoint and ordered
   along one complement-dual path. Their physical layers are `0,...,m`.
   There is an actual diameter h- joining layers 0,m and crossing every
   selected cut. Each cut is a crosscut of F with its two boundary ends
   on the different arcs between the endpoints of h-.
3. Every source point has its actual physical layer, including every
   contact-isolated point. On both boundary arcs directed from the
   layer-0 endpoint z to the layer-m endpoint a, layer labels are
   nondecreasing. This is supplied by proper, nested physical crosscuts,
   not by a formal grid drawing.
4. All selected train directions have coherent lifts in one open global
   diameter-direction cell J, whose lower projective wall is h-. There
   is a second full-span actual diameter h+ with the opposite transverse
   sign throughout J. No actual diameter direction lies inside J.

Direct each nonzero-support actual diameter by the sign of its transverse
projection at any `e=u(mu)` in J, exactly as in the phase-flux reports.

**Lemma AI-G.** The resulting directed gap relation is antitone.

**Proof.** Split the boundary at z,a into arcs L,U, with L below the line
za and U above it. An actual diameter other than h- either crosses h-
and has one endpoint on each arc, or shares z or a with h-. A diameter
with both endpoints strictly on one arc cannot cross h- and cannot
share an endpoint with it, contrary to the actual diameter thrackle.

At the projective direction of h-, the nonzero transverse sign of every
other actual diameter is its physical L-to-U sign. That sign cannot
change as the direction enters J, since a change would give an actual
diameter direction inside J. Depending on the chosen coherent vector
lift, the directed support is the physical L-to-U relation or its
transpose. The transpose of an antitone relation is again antitone.
The h- row itself gives an extreme-layer edge, 0->m or m->0, which
is compatible with either antitone relation.

Consider two physical chords `L_a U_b` and `L_c U_d`, with `a<c`.
If `b<d`, the monotone order on both arcs makes their endpoint orders
agree, so their endpoints do not alternate. They cannot share an
endpoint: equal physical endpoints have equal layer labels; the arc
junction exceptions z,a would force an impossible strict inequality
past the minimum 0 or maximum m. Thus the two disjoint diameter chords
would not cross. This contradicts the thrackle property, proving b>=d.
Adding the extreme-layer h- edge preserves this inequality. QED.

The physical arc assignment and monotone **actual** layer labels are the
essential hypotheses. The thirteen-point regression in the companion
report also has an antitone graph; Theorem AI locates its isolated
interval `{3}`. It therefore does not contradict AI or AI-G. Its absence
of actual contact cuts prevents the source release below.

## 4. Isolated interval contact release on the complete source

**General finite parallel-cut theorem.** Let X be any finite unit-separated
triangle-free planar source of diameter D>1. Suppose a nonempty proper
subset Y has no actual diameter pair to its complement, has at least one
unit contact to its complement, and all such crossing unit-contact vectors
are parallel to one unit vector u. Then translating every point of Y by
`tJu`, for all sufficiently small t>0, retains cardinality and diameter D,
opens every crossing unit contact, preserves every other old contact, and
creates no contact or diameter. Consequently X cannot be contact-minimal
among the triangle-free global minimizers of its cardinality.

**Proof.** Every crossing contact vector is `u` or `-u`; after translation
its squared length is `1+t^2`. Every actual diameter has both endpoints
on the same side of the cut and is unchanged. Every other moving source
pair is previously strict; its two positive distance margins to 1,D
are preserved for t smaller than their finite minimum. Also choose t
so that `sqrt(1+t^2)<D`. All same-side vectors are unchanged. Thus at
least one contact opens, none is added, every old diameter stays exact,
and no diameter is added. Removing contacts cannot create a unit triangle.
This proves the assertion and its contact-minimality contradiction. QED.

This theorem is source-level and finite. It assumes no KKT weights, affine
kernel, train graph, contact-core connectedness, or exclusion of isolates.
Every point of Y is translated, whether contact-isolated or not. It supplies
the exact finite motion in the SCC application rather than inferring one
from infinitesimal rigidity.

Add these explicit source hypotheses:

- D>1. The source is contact-minimal, then diameter-pair-minimal among
  the triangle-free global minimizers of its cardinality.
- On cut i every old unit contact crossing it has the vector `u_i`
  from layer i-1 toward layer i, and no contact crosses two selected
  cuts. Every remaining old contact is unchanged when a physical layer
  slab is translated. Equivalently, for a slab `{p,...,q-1}`, its only
  changing unit contacts are the two nonempty boundary train families,
  with vectors `u_p` and `-u_q` from the fixed exterior into the slab.
- The exact all-source KKT cut identity is valid with `A_i>0` and
  positive actual-diameter coefficients:
  `A_i u_i=sum_{a_h<i<=b_h} beta_h r_h`. No point is omitted from its
  subset equilibrium or from the motions below.

**Lemma AI-R.** A proper interval weak component of the gap graph is
impossible under these hypotheses.

**Proof.** The full-span opposite-sign witnesses put 0,m in the same
SCC. A proper interval weak component must therefore be an interior
slab S=`{p,...,q-1}`, with `1<=p<q<=m`. No actual diameter has just one
endpoint in S. The difference of the two cut-resultant identities is
zero, so `A_pu_p=A_qu_q`. Positivity and coherent unit directions give
`u_p=u_q=:u` and `A_p=A_q`.

Translate **every source point in S**, including isolates, by `tJu`.
The vectors of the two boundary contact families become `u+tJu` and
`-u+tJu`, both of squared length `1+t^2>1`. All other old contacts are
unchanged. Every old actual diameter is unchanged, since both its
endpoints are translated together or both remain fixed.

There are finitely many previously strict source pairs. Choose t>0
smaller than each positive distance margin to 1 and D, and also small
enough that `sqrt(1+t^2)<D`. A moving strict pair changes its distance
by at most t; thus every one stays strictly between 1 and D. This
tracks every source pair, without a uniform asymptotic slack premise.
There is no new contact or diameter, and at least one old contact opens.
The full-span witnesses remain at D. The resulting source has the same
cardinality and diameter D, remains triangle-free, and has fewer unit
contacts. This contradicts contact minimality. QED.

Opening two boundary families is **simultaneously** feasible because their
directions are exactly equal and the whole slab is translated once. This
is not a composition of individually feasible exchanges or a curvature
argument.

## 5. Immediate open-cell composition

Assume the audited finite block-transposition formula: a slab translation
by `u_q-u_p` preserves every old contact; because p,q lie in one open
global cell, every moving diameter has its strict finite length sign
equal to its first-order work sign. These statements are proved in
`target_c_open_cell_block_transposition_2026-10-01.md` and rechecked here
at their exact hypothesis signature. Assume the selected phase window
has width at most `4K/D<pi/2`, for a fixed K.

**Theorem AI-C (conditional source fork).** Under the hypotheses of
Sections 3--4, either the gap graph is strongly connected, or a previously
strict source pair xy satisfies

```math
1<|xy|\le1+4K/D\quad\text{or}\quad D-4K/D\le|xy|<D.
\tag{AI.2}
```

**Proof.** If the graph is not strong, Theorem AI gives a proper interval
source or sink SCC S=`{p,...,q-1}`. It excludes layers 0,m. If it has no
incident edge to its complement, it is an interval weak component and
Lemma AI-R contradicts contact minimality.

Otherwise, let `Phi(S;mu)=F_out-F_in` with positive diameter flows. The
cut identity gives
`Phi(S;mu)=A_q sin(theta_q-mu)-A_p sin(theta_p-mu)`.
If S is a source, at `mu=theta_p` its positive outgoing flow implies
`theta_q>theta_p`. The transposition displacement is
`Delta=u_q-u_p=2sin((theta_q-theta_p)/2) Ju(mu_mid)`.
Every moving diameter points out of S in this directed graph and
therefore strictly shortens under translation of S by Delta. If S is a
sink, the same evaluation gives `theta_q<theta_p`; entering edges
strictly shorten under the reversed displacement. All other old
diameters are unchanged and all old contacts are preserved.

If no strict pair reaches either activity threshold, the motion preserves
the exact contact set and decreases the number of actual diameter pairs.
This contradicts diameter-pair minimality. If a strict pair reaches or
passes a threshold, the triangle inequality puts it within `|Delta|`
of that threshold. Finally `|Delta|<=4K/D`, proving AI.2. QED.

The finite sign check is exact: for angular separation delta, put
`t=|sin(delta/2)|`. A moving diameter r obeys
`|r dot Ju(mu_mid)|>Dt`. Its shortening squared-length change is less
than `-4Dt^2+4t^2<=0`, strictly, for D>=1. This also explains why the
open-cell/non-grazing hypothesis cannot be dropped.

Thus the interleaved non-strong escape is eliminated **on this physical
cut stack**, after excluding AI.2. The remaining fork is strong
connectivity or finite inactive near-activity; it does not close either.

## 6. Strong-case and transverse-packet consequences

In the strong case every support edge is paired, and the collapsed simple
graph is an antitone tree on all m+1 layers. The staircase calculation
previously proved for threshold exact-phase shores now applies without
assuming exact phase or a conserved transverse circulation. Listing
left endpoints `a_1<...<a_s` and their right-neighbor ranges gives

`M_1>=m_1>=M_2>=...>=M_s>=m_s`.

Hence `|E|<=M_1-m_s+s<=m`. Connectivity gives equality m. Equality
forces `a_i=i-1`, no gaps in each right-neighbor range, consecutive
ranges meeting at one endpoint, and `m_s=s`. Writing those ranges as
`[t_i,t_{i-1}]`, with `t_0=m`, `t_s=s`, the m edge cells form a staircase
from `(0,m)` to `(s-1,s)`. Every next cell increases a or decreases b
by exactly one, so the values b-a are exactly m,m-1,...,1. Hence

```math
\sum_{\{a,b\}\in E}(b-a)=m(m+1)/2.
\tag{AI.3}
```

All these intervals are nested, so share one retained cut. Choose one
actual diameter of each physical orientation over each simple edge.
There are **2m distinct actual bars**, all crossing that common cut,
with total retained-train support incidence exactly `m(m+1)`.
The credited predecessor is
`target_c_exact_phase_threshold_paired_staircase_2026-10-01.md`, Sections
4--6; the new point is its nonconstant open-cell strong-case scope.

More generally, an internal SCC C of size r>=2 has a paired tree with
r-1 edges and at least `2r-2` distinct physical diameter rows. Under the
actual four-host condition, every internal A-row is B-full. In the
physical L-to-U orientation (or its global transpose), every layer in C
has an internal outgoing and incoming edge. These supply a physical
vertex on **each** of the two disjoint A-hosts at that layer. Distinct
layer labels mean distinct source vertices. Consequently the packet has
at least **r distinct loaded vertices on each B-extreme rail**, and at
least **2r in total**. This sharpens the `r+1` total/one-rail count in
commit `222b2302`, with the actual physical orientation and four-host
hypotheses retained. It also corrects the weaker `2r-1` count in the
first draft of this report.

The selected paired-tree lift has at least two physical components.
Color the abstract layer tree bipartitely as X,Y. Its physical rows lie
either in `L_X union U_Y` or in `L_Y union U_X`, disjoint vertex sets.
Each selected pair contributes one edge in each class. The physical
packet is a forest by canonical Woodall topology; with `2r-2` selected
edges and at least two components it again has at least 2r vertices.
This gives a second proof of the total count without claiming that the
two components are distinct unloaded contact components or tiling grains.

These counts alone do not exceed a canonical budget. In particular a
B-full bar need not have its endpoints on the retained rectangle's
grid rails. Substituting grid corner coordinates would be an invalid
co-embedding assumption. No Section-123 defect is counted from these
rows without another source-payment theorem.

## 7. Exact verification, regressions, and surviving obligation

Run:

```sh
python3 docs/research/migration/2026-10-16/shards/01/support/research/verify_target_c_antitone_interval_scc_2026_10_03.py
```

The standard-library verifier exhausts **all 487,208 labeled loopless
antitone directed relations on 2 through 7 vertices**, without symmetry
identification. It checks minimum-span terminal intervals, paired SCC
trees, compressed staircase identities, and the strong full-order count.
This is bounded corroboration; Section 2 proves all finite sizes.
The certificate proves no geometric or global-minimizer premise. It also
checks exact rational perpendicular contact-opening identities and a
three-point nonglobal motion fixture; these corroborate the finite move,
not the global-minimality hypothesis. The thirteen-point companion has
two internal r=2 SCC packets with exactly two source vertices per rail,
so the new 2r total count cannot be replaced by 2r+1 in this scope.

The companion thirteen-point regression satisfies antitonicity and
has the isolated interval `{3}`. It has no contact cuts and is nonglobal,
so AI-R does not apply; this is the precise hypothesis resolution.
The old five-point regression has an interval sink and violates source
minimality. Neither contradicts the conditional fork. Stars remain
allowed, no Euler path is asserted, all source isolates are retained,
and no Section-57 kernel is extended.

The exact surviving obligations on the fixed-star physical stack are:

```math
G_J\text{ strong with }h\ge2m
\quad\text{or}\quad\text{an inactive pair satisfying AI.2}.
```

The first gives TWO-SIGN for every nonzero one-axis layer potential;
the second remains a genuine finite source blocker. The next theorem
must change points within a layer, pay actual inactive blockers, or
turn the paired common-cut support into a source-level defect or strict
competitor. No negative curvature or assigned grid scaffold supplies
that step automatically.

## Slot 2 recovery provenance — 2026-10-05

Recovered from `research/full-settlement-collar-20261003` at exact source tip `bc52d9f5153c8c936fd3fbf96f755c8d57bbee86`; no original PR was associated with the source branch. This artifact is preserved as a unreviewed proof-only candidate. It does not change theorem state. Any conditional source hypotheses and limits remain as stated above; C-II and Level I remain open.
