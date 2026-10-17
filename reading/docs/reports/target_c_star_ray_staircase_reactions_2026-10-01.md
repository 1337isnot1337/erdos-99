> Generated reading edition · [exact source](../../../docs/reports/target_c_star_ray_staircase_reactions_2026-10-01.md) · source SHA-256 `6a7dfa1047d6c701c4755967dff6a54059c4b2f2d31db4faa74ff72fcae9852f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-E598A709E228","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: a bracing-star ray orders the exact-phase gap circulation

**Phase 2 preservation provenance:** PR #597, branch swarm/root/c2-gap-reaction-20261001, audited source head c89adbcd2e008e1d01141fa38ff54b1bcae85678. Preserve as unreviewed/conditional proof-only work. Its exact regression does not encode full source KKT, train cuts, or global optimality; it does not close C-II.

Date: 2026-10-01
Starting checkout: `7b3fd8e2ad15532c0d40b761da381ac7d5c36074`.
Research base after fetch: `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`.
State version: `2026-09-14.audit.51`.
Branch: `swarm/root/c2-gap-reaction-20261001`.
Mission: couple the exact-phase gap circulation to actual diameter geometry and axial reactions.
Classification: proved candidate awaiting promotion; repository lifecycle remains unreviewed.
Level I: OPEN. C-I: CLOSED. C-II: OPEN.

```text
bracing-star ray -> paired staircase and ordered positive axial bundles
  -> strictly unimodal actual cut-contact masses
  -> target: contradict or deform this labeled source using the complete transverse shore
  -> strict same-cardinality competitor / exact triangle
```

The last implication is not proved. This report changes no canonical theorem status.
It neither discards contact-isolated points nor asserts global optimality for its regression.

The follow-up
[exterior-train far-arc report](target_c_exact_phase_exterior_train_far_arc_2026-10-01.md)
now integrates a finite move passing every old diameter constraint outside the
local chart barrier. Its source obstruction is a previously strict source pair;
it does not supply a complete feasible competitor.

## 1. Dependencies and scope

Canonical inputs used are the normal form in
[`56-ci-restored-frontier.md`](../targets/target-c/56-ci-restored-frontier.md),
mixed core rigidity in
[`57-zr-zf-rigidity-audit.md`](../targets/target-c/57-zr-zf-rigidity-audit.md),
and source-hull geometry and vanishing diameter-star angles in
[`58-full-source-geometry-audit.md`](../targets/target-c/58-full-source-geometry-audit.md).
These control the conditional application to C-II, rather than supplying the new geometric proof.

The following October 1 dependencies are unpromoted research:

- [`target_c_local_witness_cell_2026-10-01.md`](target_c_local_witness_cell_2026-10-01.md): two full-span incident witness diameters straddling the exact train direction;
- [`target_c_complete_grid_rank_switching_2026-10-01.md`](target_c_complete_grid_rank_switching_2026-10-01.md): exact global train cuts, nested layer order and full derivative rank;
- [`target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md`](target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md): outer-boundary interpretation of the layers;
- [`target_c_exact_phase_gap_graph_connectivity_2026-10-01.md`](target_c_exact_phase_gap_graph_connectivity_2026-10-01.md): connectivity.

The circulation identity is rederived below, rather than imported as a canonical theorem.
The remote circulation audit was inspected at `origin/research/exact-phase-gap-circulation-audit-2026-10-01`;
its no-bridge conclusion is consistent with this proof.

The older
[`target_c_positive_prefix_thrackle_collapse_2026-09-01.md`](target_c_positive_prefix_thrackle_collapse_2026-09-01.md)
already contains the two-cycle and staircase mechanism for a literal straight diameter chain.
It is unreviewed provenance here, not a premise. The extension proved here is that a
**ray inside a full-span bracing diameter star** supplies the required two-arc order,
even when there is no actual diameter parallel to the train direction. The positive
axial-bundle proof uses the determinant of crossing diameter vectors; it does not
assume monotonicity of the axial coordinate on hull arcs ending at this ray.

Thus this applies to an exact-phase shore in either an open or a threshold witness
cell. It does not apply to a nonconstant-phase shore. Its C-II application remains
conditional on the explicit October 1 extraction and train-cut hypotheses.

## 2. Explicit hypotheses

Let a finite unit-separated planar source have diameter $`D>1`$, hull $`K`$, and
actual diameter graph $`H`$. Consider $`m\ge1`$ nested train cuts with coherent exact
unit direction $`u`$. Write $`Ju`$ for a counterclockwise quarter-turn. Assume:

1. Diameter endpoints are extreme hull vertices. Distinct vertex-disjoint diameter
   segments cross properly; the cyclic endpoint order is the convex diameter-thrackle order.
2. The cuts define a boundary layer map $`\ell\in\{0,\ldots,m\}`$: its boundary
   layers are cyclically ordered $`0,1,\ldots,m,\ldots,1,0`$, allowing repeated
   vertices in one layer. For endpoints $`x,y`$, the nonempty signed cut support
   is exactly the interval between $`\ell(x)`$ and $`\ell(y)`$.
3. There are two distinct actual diameters $`vp^-,vp^+`$ with both partners in
   layer $`m`$ and $`v`$ in layer $`0`$, after reversing all layer indices if needed.
   Their rays strictly straddle $`u`$, and their ordinary opening angle is less
   than $`\pi/3`$. They are full-span witnesses.
4. For each $`h`$ with endpoint layers $`a<b`$, let $`n_h`$ point from layer $`a`$
   toward layer $`b`$. Its exact-phase derivative row is
   
   ```math
   M_h=(n_h\cdot Ju)\mathbf1_{(a,b]}.
   ```

   Rows with equal endpoint layers or zero transverse component are discarded.
5. Positive actual diameter weights $`\beta_h>0`$ satisfy $`\beta^TM=0`$, and
   $`M`$ has rank $`m`$.

For the current fixed-star rectangle, item 3 comes from the common witnesses; its
angle condition holds for all sufficiently large sources by the canonical star
estimate. Item 5 follows from full-support KKT virtual work and mixed rigidity,
with the opposite train shore killing common rotation. These facts are not asserted
for arbitrary feasible sources.

## 3. A ray anchor without a parallel diameter

### Lemma 1

The ray $`v+\mathbb R_+u`$ meets the hull in a segment $`[v,z]`$. Its exit point $`z`$
lies on the boundary arc from $`p^-`$ to $`p^+`$ not containing $`v`$, hence in layer
$`m`$. Every actual diameter not incident to $`v`$ intersects $`[v,z]`$. Apart from
a possible diameter $`vz`$ parallel to $`u`$, each such diameter has endpoints on
opposite sides of its supporting line, allowing one endpoint to equal $`z`$.

### Proof

The strict ray bracketing puts $`u`$ in the interior of the tangent cone of $`K`$ at
$`v`$, so the positive ray enters the hull. The chord $`[p^-,p^+]`$ meets that ray
at a positive point. The exit $`z`$ is therefore on the opposite boundary arc between
the two partners. The layer-$`m`$ boundary arc is contiguous and contains both
partners; the subarc not passing through the layer-0 vertex $`v`$ is in that layer.

Take a diameter $`h`$ not incident to $`v`$. If it is disjoint from both witness
edges, it crosses both properly. The part of $`h`$ between those crossing points
joins the two sides of the ray inside the convex sector between the witnesses;
it crosses the positive ray. If $`h`$ shares $`p^-`$ or $`p^+`$, it crosses the
other witness properly, so the same argument applies with one crossing point
replaced by its endpoint. It cannot be $`p^-p^+`$, since

```math
|p^--p^+|=2D\sin(\angle p^-vp^+/2)<D.
```

Every resulting ray intersection is in $`K\cap(v+\mathbb R_+u)=[v,z]`$.
No nonincident diameter can pass through the extreme vertex $`v`$. A diameter
lying along the line would have both hull endpoints on that line. Because the ray
enters the hull interior, those endpoints would have to be $`v,z`$. This is the
possible parallel diameter already removed in item 4. All other nonincident
diameters cross the line or end at $`z`$. QED.

Let $`L,U`$ be the lower and upper hull arcs from $`v`$ to $`z`$, ordered in that
direction, so their open portions have negative and positive $`Ju`$ coordinates,
respectively. Each train cut separates $`v,z`$; therefore its layer map is
nondecreasing on each arc. Actual diameter endpoints with nonzero transverse
component can be assigned a lower and an upper endpoint. At $`v,z`$, membership in
both arc closures is harmless, because their layer indices are the extreme values.

This is the missing geometric input for extending the old chain argument. The point
$`z`$ need not be a source point or a diameter partner of $`v`$.

## 4. Positive circulation collapses to paired intervals


**Source formatting excerpt (unbalanced inline math in the original):**

```text

For a nonzero row with layers $`a<b`$, taking discrete differences sends
(\mathbf1_{(a,b]}\) to (e_a-e_b). Consequently
```



```math
\sum_h\beta_h(n_h\cdot Ju)(e_a-e_b)=0.                 \tag{1}
```

Orient the gap edge from the layer of its lower physical endpoint to the layer of
its upper physical endpoint. Give it positive flow

```math
f_h=\beta_h|n_h\cdot Ju|>0.
```

Equation $`1`$ is node balance for this positive directed circulation, up to a common
choice of incidence sign. Full derivative rank gives a connected undirected gap graph.

### Lemma 2

Every directed simple circulation cycle has length two. Every used unordered interval
$`\{a,b\}`$, $`a<b`$, has diameters in both physical orientations

```math
L_aU_b,\qquad L_bU_a,                                \tag{2}
```

and their total transverse KKT flows are equal.

### Proof

In a simple cycle $`k_0\to k_1\to\cdots\to k_{s-1}\to k_0`$, the physical edges
are $`L_{k_i}U_{k_{i+1}}`$. Consecutive increments alternate signs. For disjoint
consecutive edges, proper crossing reverses their orders on the two arcs, so

```math
(k_i-k_{i+1})(k_{i+1}-k_{i+2})<0.
```

If the edges share a source endpoint despite their distinct cycle levels, that
endpoint must be $`v`$ or $`z`$, the only common points of the two arc closures.
Its level is $`0`$ or $`m`$, and the increments again alternate.

The cycle is thus even. Write its successive minima as $`a_i`$ and maxima as $`b_i`$.
The edges $`L_{a_i}U_{b_i}`$ are pairwise disjoint, since their minimum levels and
maximum levels are distinct and a minimum cannot be $`m`$ or a maximum $`0`$.
They cross pairwise. Hence their matching $`F(a_i)=b_i`$ strictly reverses order.
The other edges give another order-reversing matching $`G(b_i)=a_{i+1}`$.
Their composition is an order-preserving permutation of the finite ordered set of
minimum levels, and must be the identity. It is also the cyclic shift. There is only
one minimum, so the original cycle has two edges.

Decompose the positive circulation into directed simple cycles: follow positive
edges to a repeated vertex, subtract the smallest flow on the resulting cycle, and
repeat. Every edge is exhausted in finitely many such subtractions. All cycles are
two-cycles, proving $`2`$ and equality of their total flows. QED.

### Lemma 3

The distinct simple gap edges form an antitone staircase spanning tree with exactly
$`m`$ edges. For some $`r\in\{1,\ldots,m\}\`$, they are exactly the cells of a monotone
path

```math
(0,m)\longrightarrow\cdots\longrightarrow(r-1,r),    \tag{3}
```

whose steps are $`(a,b)\mapsto(a+1,b)`$ or $`(a,b-1)`$. Every simple edge is represented
by at least two actual diameter bars, so there are at least $`2m`$ nonzero rows.
A parallel diameter, if present, is additional.

### Proof

Take two simple edges $`(a,b),(c,d)`$ with $`a<c`$. Lemma 2 supplies diameters
$`L_aU_b,L_cU_d`$. If $`b<d`$, their two arc orders agree, preventing crossing.
Their distinct levels also prevent a shared endpoint. Thus $`b\ge d`$.
The intervals overlap, and the interval Helly property supplies a common index $`r`$.

List distinct left endpoints $`a_1<\cdots<a_s`$, and let $`B_i`$ be their sets of
right endpoints, with minima $`b_i^-`$ and maxima $`b_i^+`$. Antitonicity gives

```math
b_1^+\ge b_1^-\ge b_2^+\ge\cdots\ge b_s^-.
```

Therefore

```math
|E|\le\sum_i(b_i^+-b_i^-+1)
\le b_1^+-b_s^-+s\le m-r+r=m.
```

Connectivity on $`m+1`$ gap vertices gives the reverse inequality, so this is a tree.
Its cells are totally ordered by increasing left and decreasing right endpoint.
Consecutive cells must share a coordinate: if both coordinates change, antitonicity
partitions every earlier and every later edge into disjoint vertex sets, disconnecting
the graph. No coordinate can be skipped, as every gap vertex is incident. The first
cell is $`(0,m)`$, the last $`(r-1,r)`$, and each step is a unit step in one coordinate.
This proves $`3`$. Lemma 2 supplies two physical orientations for each cell. QED.

The tree is the **collapsed simple graph**. The full graph is bridgeless because
every tree edge is doubled. Its leaves do not give private active diameter rows.

## 5. Every paired bundle has a strictly positive axial resultant

For a fixed cell $`(a,b)`$, write each physical upward vector in its positive
orientation $`L_a\to U_b`$ as $`D(\cos\alpha,\sin\alpha)`$, and each upward vector
in the opposite orientation $`L_b\to U_a`$ as $`D(\cos\gamma,\sin\gamma)`$.
Angles are relative to $`u,Ju`$, and lie in $`(0,\pi)`$. They satisfy

```math
\alpha<\gamma                                           \tag{4}
```

for every choice of the two bars. When endpoints are distinct, their cyclic order
is $`L_a,L_b,U_b,U_a`$, with positive orientation; proper crossing gives

```math
\det(U_b-L_a,U_a-L_b)>0.
```

Both vectors have positive transverse component, so their angle difference is in
$`(-\pi,\pi)`$; positive determinant proves $`4`$. If they share $`v`$ or $`z`$, the
same determinant is the positive area of the nondegenerate triangle formed with
their two other endpoints. It cannot be zero: parallel diameters are unique, and
the transverse components are nonzero.

Let $`R_{ab}`$ be the original KKT-weighted axial component of this bundle, oriented
from lower layer to higher layer. Its transverse component is zero by Lemma 2.
In terms of the positive flows, its axial component is

```math
R_{ab}=\sum_+ f_h\cot\alpha_h-\sum_- f_h\cot\gamma_h.
```

The two flow measures have the same total mass. Couple them, for example by their
normalized product measure. Since cotangent strictly decreases on $`(0,\pi)`$,
$`4`$ makes every coupled difference strictly positive. Thus

```math
\boxed{R_{ab}>0.}                                      \tag{5}
```

This proof does not require the axial coordinate to be monotone along $`L,U`$.
That would be an unjustified assumption for a ray anchor whose exit is not a
diameter partner.

Now also assume the original KKT contact cut law. Let $`A_i>0`$ be the total positive
contact weight across train $`i`$. Then

```math
A_i u=\sum_h\beta_h n_h\mathbf1_{(a_h,b_h]}(i).
```

A possible diameter parallel to $`u`$ has endpoints $`v,z`$, and therefore full
support and a positive constant axial contribution $`R_0\ge0`$. All other bundles
are those classified above. Hence

```math
A_i=R_0+\sum_{(a,b):a<i\le b}R_{ab}.                   \tag{6}
```

Every interval contains $`r`$, and every gap vertex is incident. Equation $`5`$ gives

```math
\boxed{A_1<\cdots<A_r>\cdots>A_m.}                    \tag{7}
```

At an adjacent slab, with the outside-to-middle convention of the blocker report,

```math
G_i=(A_i-A_{i+1})u
```

points in direction $`-u`$ for $`i<r`$, and $`+u`$ for $`i\ge r`$.
There is at most one sign change in the axial strip reactions, with the appropriate
one-sided interpretation when $`r=1`$ or $`r=m`$. The inequalities are strict.

## 6. Ordered widening of the reaction cones

Number the $`m`$ cells in path order $`3`$. For cell $`t`$, choose any one upward vector
of each orientation, with angles $`\alpha_t,\gamma_t`$ as above. The same convex
crossing determinant argument, including its shared-endpoint triangle case, gives

```math
\alpha_1<\cdots<\alpha_m<\gamma_m<\cdots<\gamma_1.
                                                               \tag{8}
```

For example, between consecutive positive-orientation cells, one layer strictly
increases or the other strictly decreases. Crossing forces the other physical
endpoint order, even if its layer stays fixed. The resulting convex quadrilateral
or triangle gives a positive determinant of the two upward vectors. For the
reverse orientations, the determinant order is reversed. This proves $`8`$.

The actual force pair is the first upward vector and the negative of the second.
Its positive cone contains $`u`$, with ordinary opening

```math
\Theta_t=\pi-\gamma_t+\alpha_t\in(0,\pi).
```

Thus these axial reaction cones strictly widen in staircase order, for **every**
choice of one representative in each orientation bundle.

Unit separation gives the projective direction spacing

```math
\delta_D=2\arcsin(1/(2D)).
```

For completeness, when diameters share an endpoint, their ordinary angle is at
most $`\pi/3`$, and partner separation gives this bound directly. For disjoint
diameters, orient their unit vectors at the minor projective angle $`\varepsilon`$
and write their midpoint difference as $`d`$. The two far cross-endpoint distances
are at most $`D`$, so averaging their squares gives

```math
|d|^2\le D^2\sin^2(\varepsilon/2).
```

The two near cross-endpoint distances are at least one. Averaging their squares
then gives $`1\le2D^2\sin^2(\varepsilon/2)`$, which is stronger than the stated
bound. Consequently each strict angular increment in $`8`$ is at least $`\delta_D`$,
and

```math
\boxed{\Theta_t\ge\Theta_1+2(t-1)\delta_D.}            \tag{9}
```

In particular $`2(m-1)\delta_D<\pi`$, and the last half of the bundles have opening
at least $`(m-2)\delta_D`$. If $`m\ge(c_*-o(1))D`$, that half is a linear family
of edge-disjoint axial bundles with opening at least $`c_*-o(1)`$. Their two bars
have distinct endpoints for large $`D`$, by the canonical vanishing star aperture.
Bars in different bundles may still share endpoints; no matching-size assertion
or uniform positive KKT weight is inferred.

At this scale $`9`$ does not contradict $`h\le\pi D+o(D)`$. The staircase can occupy
a short part of the available direction range when $`c_*`$ is small.

## 7. Zero-row diameters occupy one common central gap

### Lemma 4

Every actual diameter with empty selected-cut support has both endpoints in one
of the two gap layers $`r-1,r`$. If any such diameters exist, there is one common
layer $`k_0\in\{r-1,r\}`$ containing both endpoints of every one of them.
Its upward physical angle lies strictly between
the angles of every choice of the two innermost orientation representatives:

```math
\alpha_m<\theta_{\rm empty}<\gamma_m.                 \tag{10}
```

The only other zero derivative row is a possible parallel diameter $`vz`$, which
has full support. Therefore no actual zero-row diameter connects an outer gap to
another region.

### Proof

An empty-support diameter has two endpoints of the same layer $`k`$. By the ray
anchor they are on opposite arc closures. Compare it with a paired interval
$`(a,b)`$. If $`k<a`$, both its arc endpoints precede the corresponding endpoints
of each orientation of that interval. If $`k>b`$, both follow. In either case the
diameters are disjoint and cannot cross, contrary to the diameter-thrackle property.
Thus $`a\le k\le b`$ for every paired interval. Apply this to the innermost cell
$`(r-1,r)`$.

The two possible layers cannot both carry an empty-support diameter. One
diameter in layer $`r-1`$ and another in layer $`r`$ have different endpoint
layers, hence are vertex-disjoint. On each ray-anchor arc, the first diameter's
endpoint strictly precedes the second's endpoint. Their four endpoints therefore
do not alternate on the hull boundary, so the segments cannot cross. This
contradicts the actual diameter-thrackle property. Thus all empty-support
diameters use one common $`k_0`$.

For $`k=r-1`$, compare the empty upward vector $`L_k\to U_k`$ first to
$`L_{r-1}\to U_r`$, then to $`L_r\to U_{r-1}`$. The strict order on one arc forces
the other arc order by crossing, even when one layer agrees. The positive
quadrilateral determinant, or triangle determinant for a shared endpoint, puts
the empty vector strictly between the two nonempty vectors. The case $`k=r`$
is the same with the roles of the arcs interchanged. This gives (10).

Any transverse-zero diameter is parallel to $`u`$. Parallel diameter uniqueness
and the ray-anchor hull intersection identify it with $`vz`$, if that segment
is actually a source diameter. Its endpoints have layers $`0,m`$. QED.

This is a statement about the **actual diameter graph**, including rows omitted
from its derivative matrix. It does not omit those endpoints from population
or pretend that every diameter is seen by the retained shore.

### Odd-cycle localization

Partition the source vertices by layer into $`\ell<r`$ and $`\ell\ge r`$,
retaining contact-isolated vertices. Every nonempty-support diameter crosses
this partition, since every staircase interval contains the cut $`r`$.
The possible parallel diameter $`vz`$ also crosses it. After deleting the
empty-support diameters, the full actual diameter graph is therefore bipartite.
Consequently every odd actual diameter cycle must use an empty-support
diameter, whose two endpoints belong to the one common layer $`k_0`$.
In particular, in the canonical odd-unicyclic Woodall branch, its unique odd
cycle must pass through that central layer. No conclusion about its cycle
length, number of central edges, or contact isolation follows.

The concurrent support-cap packet in PR #596 also localizes odd cycles using
actual cut-cap reactions. The argument here gives a direct consequence of
the paired staircase and then confines *all* empty-support diameters to one
of its two central gap vertices. It does not use that packet as a premise.

### What this gives for a second star

For a source vertex other than $`v,z`$, all its nonempty-support diameter edges
belong to one physical orientation class. Indeed, every nonempty simple gap edge
joins a left layer $`<r`$ to a right layer $`\ge r`$. The positive physical class
joins $`L_{\rm left}`$ to $`U_{\rm right}`$; the negative class joins
$`L_{\rm right}`$ to $`U_{\rm left}`$. These source endpoint sets are disjoint away
from $`v,z`$. Empty-support incidences can occur only in the two central gaps.

Thus a second bracing star has three possible types relative to this shore:
all its selected witness bars are in the positive staircase class; all are in
the negative class; or its star center is in a central gap and some selected
witness bars are invisible to this shore. This is not an exhaustive trichotomy
for arbitrary endpoints at $`v,z`$, which are explicitly excluded here.
In the current inverse-phase rectangle the opposite-star center differs from
$`v`$ for sufficiently large $`D`$, by vanishing star width and the transverse
direction gap. If it happens to be the auxiliary ray exit $`z`$, the endpoint
exception must still be handled rather than dropped.

## 8. An explicit finite barrier for the proposed train-leaf release

Use the exact finite cut chart: rotate selected train $`i`$ by angle $`\theta_i`$,
and translate layer $`k`$ by

```math
W_k=\sum_{i\le k}\big[(\cos\theta_i-1)u+\sin\theta_i\,Ju\big].
```

This preserves every old contact when the declared actual global cutsets hold.
For a diameter with interval $`I`$, its new relative vector is

```math
n_h+\sum_{i\in I}\big[(\cos\theta_i-1)u+\sin\theta_i\,Ju\big].       \tag{11}
```

Let $`\gamma>0`$ be the minimum absolute transverse component among the finitely
many nonzero rows. Then every nonzero angle vector with

```math
0<T:=\|\theta\|_\infty\le\frac{\gamma}{4Dm}
```

lengthens at least one old actual diameter. This conclusion is about a full finite
endpoint substitution, without assuming feasibility along an intermediate path.

To prove it, write the successive nested staircase intervals as $`I_1,\ldots,I_m`$.
They have lengths $`m,m-1,\ldots,1`$, and consecutive intervals delete one column.
Put $`s_t=\sum_{i\in I_t}\theta_i`$. Every deleted coordinate is $`s_t-s_{t+1}`$,
and the remaining coordinate is $`s_m`$. Hence some $`|s_t|\ge T/2`$.
That interval has an actual row with transverse component $`\eta_h`$ of the same
sign as $`s_t`$, and $`|\eta_h|\ge\gamma`$.
For its exact change (11), set $`X=\sum_{I_t}(\cos\theta_i-1)`$,
$`Y=\sum_{I_t}\sin\theta_i`$, and $`c_h=n_h\cdot u`$. Then

```math
|n_h+Xu+YJu|^2-D^2=2c_hX+2\eta_hY+X^2+Y^2.
```

Using $`|X|\le mT^2/2`$, $`|Y-s_t|\le mT^3/6`$, $`|c_h|,|\eta_h|\le D`$, gives

```math
|n_h+Xu+YJu|^2-D^2
\ge \gamma T-DmT^2-\frac{Dm}{3}T^3.
```

Since $`\gamma\le D`$, the stated radius is at most $`1/(4m)\le1`$.
The lower bound is therefore at least $`2\gamma T/3>0`$.

In a **threshold** cell, the unique parallel diameter has already been removed.
Projective separation gives

```math
\gamma\ge g_D:=D\sin\delta_D=\sqrt{1-\frac1{4D^2}}.
```

Thus $`g_D/(4Dm)`$ is a uniform finite isolation radius, independent of KKT weights
and inactive slack.

In an **open** cell, the two cell-boundary diameters have full support. A proper
interval diameter is neither boundary edge, so its projective distance from $`u`$
is at least $`\delta_D`$, and its transverse magnitude is at least $`g_D`$.
Let $`j_0\in\{1,m\}`$ be the one column deleted from the full interval to form the
second staircase interval. If $`m\ge2`$ and $`\theta_{j_0}=0`$, the proper nested
intervals alone recover all remaining coordinates by successive differences.
Repeating the proof gives uniform finite isolation radius

```math
\frac{g_D}{4D(m-1)}
```

on that codimension-one chart. Only the one exterior coordinate can retain a
small source-dependent transverse barrier.

This sharpens the general source-dependent chart-isolation mechanism in PR #595
using the new staircase inverse, rather than a matrix singular-value estimate.
It rules out a small finite train-leaf release even after replacing the basis by
the full active system. It does not rule out moves outside this chart, moves
beyond its radius, or changes that release old contacts.

## 9. Exact geometric regression: the staircase is realizable

Let $`s=\sqrt{42}`$, $`D=13`$, $`u=(1,0)`$, and use seven points

```math
v=(0,0),\quad p^\pm=(12,\pm5),\quad
L_1=(6,-s),\ U_1=(6,s),\ L_2=(7,-s),\ U_2=(7,s).
```

Their hull order is

```math
v,L_1,L_2,p^-,p^+,U_2,U_1.
```

Every pair is at least unit distance. The only unit contacts are $`L_1L_2,U_1U_2`$,
so the source is triangle-free. Its actual diameter edges are exactly

```math
vp^-,\ vp^+,\ L_1U_2,\ U_1L_2,
```

all of length 13. Assign layer 0 to $`v`$, layer 1 to $`L_1,U_1`$, and layer 2 to
all remaining vertices. The exact-phase derivative rows are

```math
(-5,-5),\ (5,5),\ (0,2s),\ (0,-2s).
```

They have rank two and the positive normalized weights $`\beta_h=1/4`$ give zero
virtual work. The collapsed gap graph is the staircase $`\{0,2\},\{1,2\}`$;
its full graph doubles both edges. Its bundle resultants are $`R_{02}=6`$ and
$`R_{12}=1/2`$, giving formal cut masses $`A_1=6,A_2=13/2`$. Its two reaction
cone openings are $`2\arctan(5/12)`$ and $`2\arctan(2s)`$, in increasing order.
The actual diameter graph is one two-edge star and two isolated edges, a caterpillar forest.

This example obeys unit separation, convex actual-diameter geometry, a common
full-span bracing star, cyclic layer order, full graphic rank and positive projected
circulation. It kills a contradiction based solely on those properties, including
the strengthened paired staircase and cone order.

It does **not** encode two complete actual train cuts or a complete transverse grid.
It has no full-source positive KKT stress: $`v`$ has no unit contacts and cannot
balance its positive diameter forces. It is not claimed globally optimal. These
are exactly the source hypotheses a closing proof must add.

## 10. Computation and self-audit

The two central-gap possibilities in Lemma 4 are both realizable at geometric
and projected-balance scope. Double the seven-point coordinates in Section 9
and add the points $`(13,-13),(13,13)`$. The nine-point source has diameter 26
and exactly five diameter edges: the doubled four old edges and the new vertical
edge. Assign both new endpoints to layer 1, or both to layer 2. Either assignment
preserves boundary layer monotonicity and gives a zero row for that actual edge,
with its angle strictly inside the innermost interval. All 36 distances are
strictly greater than one and at most 26. The exact verifier checks both variants.
These examples encode no actual train cuts or full-source KKT equilibrium.

[`verify_target_c_star_ray_staircase_2026_10_01.py`](../../../research/verify_target_c_star_ray_staircase_2026_10_01.py)
uses exact arithmetic in $`\mathbb Q(\sqrt{42})`$ for every pair distance, convex
hull orientation, contact/diameter set, row, KKT projection and axial resultant
in the regression. It also exhaustively checks the connected antitone simple
graphs on gap sets $`0,\ldots,m`$, $`1\le m\le5`$, against the binary staircase
path classification. Those finite checks support, but do not replace, the proof
for arbitrary $`m`$.

Executed results: all 21 source-pair distances and all hull orientation checks pass;
the actual contact and diameter sets match Section 9; the derivative rank is 2;
both projected components cancel exactly; the two axial resultants are 6 and 1/2.
The finite graph enumeration inspects 2, 8, 64, 1024 and 32768 graphs for the five
successive values of $`m`$, with 1, 2, 4, 8 and 16 connected antitone survivors.
Each survivor is exactly a staircase path. The theorem-state and relative-link
checker passes after regenerating the artifact index and its pre-existing stale
October 1 headers. This generated repair leaves every such report unreviewed.
The updated verifier also checks eight small finite chart substitutions, a larger
exterior-train substitution reducing the four diameters to two, 820 rational
oblique-grid pair vectors, and the five-point empty-arc regression in the
follow-up report.

Binding checks:

- A path or star can be the collapsed simple graph; the full positive circulation
  doubles its edges. No private spanning-tree-leaf motion is asserted.
- Neither a circulation cycle nor incident diameter sequences are treated as an
  Euler trail of the actual diameter graph.
- The ray exit $`z`$ may be an auxiliary hull point. It is not inserted into the
  source or counted as a diameter endpoint.
- Equal endpoint layers yield zero rows and are excluded from the staircase,
  while remaining part of the actual source and actual diameter graph.
- Every original KKT multiplier used in the application has its declared scope;
  the regression weights only satisfy projected train balance.
- No first-order motion is claimed to integrate to a finite feasible release.
- No assertion about isolated population, near-active pairs or global packing
  density is used in this geometric theorem.

## 11. Exact remaining obligation

| Claim | Classification | Scope |
| --- | --- | --- |
| Star-ray anchor and two-cycle collapse | proved candidate awaiting promotion | Explicit hypotheses 1–5 |
| Paired staircase, strict axial positivity and cone order | proved candidate awaiting promotion | Same geometric hypotheses; contact law added for cut masses |
| Zero-row diameter endpoints and directions | proved candidate awaiting promotion | One common central gap chosen from two; innermost angular interval; possible parallel diameter retained |
| Explicit finite train-chart isolation radius | proved candidate awaiting promotion | Exact finite cut chart; uniform threshold radius and open-cell codimension-one radius |
| C-II fixed-star application | conditional | October 1 extraction and exact global cuts remain unpromoted |
| Seven-point source | regression | Diameter geometry and projected circulation only |
| Private spanning-tree leaf release | rejected attempt | Full active system doubles each collapsed edge |
| Level I or C-II closure | not claimed | Transverse shore and other branches remain unresolved |

The full-span star supplies more than a connected bridgeless graph: in exact phase
it supplies a doubled staircase with ordered widening cones and a single peak in
the actual cut-contact masses. A closure must show that this labeled staircase,
**with its actual contact cutsets and complete transverse O-O shore**, cannot
occur in the contact-minimal, then diameter-pair-minimal global source, or construct
a finite feasible deformation/replacement of that full source. Section 9 shows
why projected balance and diameter geometry alone cannot supply that implication.

Nonconstant-phase TB1, split-star O-O, inactive interfaces and the macroscopic
inactive-container branch are not eliminated. Promotion would require an independent
audit of this proof and the unpromoted extraction dependencies, followed by the
repository promotion transaction. Until then this is an unreviewed research packet.
