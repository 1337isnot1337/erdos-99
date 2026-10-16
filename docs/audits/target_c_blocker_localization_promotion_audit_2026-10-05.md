<!-- theorem-state: {"artifact_id":"ART-2283945E2084","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Historical proposed audit — long-pair isolate dispatch and small-move blocker localization

**Preservation status (2026-10-15):** historical proposed audit, restored from
`389c779f203758f0d15fdf64f83ca82a550ca785`, original blob
`de4b5cc03e379b38bebc91d345503ded0ccff3a7`. This file does not promote a claim.
The current manifest controls the canonical long-pair and near-unit successors;
terminal/cap statements keep their separately recorded candidate scope.
The [source reconciliation](blocker_localization_source_reconciliation_2026-10-15.md)
records the complete proof comparison and connected-core scope clarification.
Historical verdicts and proposed state updates below are provenance, not a current
independent human review or a new promotion transaction.

**Date:** 2026-10-05
**Audit base:** \`ad8809fd96c2c0af9a6de4d965e9ab33efe092c6\`
**Starting theorem state:** \`2026-10-05.audit.59\`
**Target:** C-II / full-source blocker localization for finite binary motions
**Verdict:** **PASS for the two exact claims registered below.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Audited sources:

- \`docs/reports/target_c_ultrasmall_swap_isolate_dispatch_2026-10-01.md\`;
- \`docs/reports/target_c_small_swap_face_endpoint_localization_2026-10-01.md\`;
- \`docs/reports/target_c_near_unit_faces_and_pure_conflict_paths_2026-10-01.md\`.

This historical audit proposed promoting finite geometry and full-source dispatch statements only. It does **not** promote the October 1 fixed-star extraction, arbitrary block transposition, joint-swap Horn system, or any claim that a canonical source necessarily contains a large family of such moves.

## 1. Sharp long-pair graph on the full source

Let \(A\) be any finite unit-separated planar source of diameter \(D>1\). Define

\[
L_D=\sqrt{D^2-1},
\qquad
\gamma_D=D-L_D=\frac1{D+L_D}.
\]

Let \(T_D\) be the graph whose edges are exactly source pairs of length **strictly greater** than \(L_D\).

### 1.1 Every endpoint is extreme

If \(p\) is nonextreme, write
\[
p=\sum_i\lambda_i a_i,
\qquad
\lambda_i\ge0,\quad
\sum_i\lambda_i=1,
\]
with \(a_i\in A\setminus\{p\}\).

For any \(q\in A\), the variance identity gives
\[
|p-q|^2
=
\sum_i\lambda_i|a_i-q|^2
-
\sum_i\lambda_i|a_i-p|^2.
\]

The first sum is at most \(D^2\). By unit separation, every \(a_i\ne p\) has
\[
|a_i-p|^2\ge1,
\]
so the second sum is at least one. Hence
\[
|p-q|^2\le D^2-1=L_D^2.
\]

Thus no nonextreme source point is incident with a \(T_D\)-edge.

### 1.2 Disjoint long edges cross

Take two vertex-disjoint \(T_D\)-edges. All four endpoints are strict hull vertices.

If the two edges did not cross, they would be opposite sides of their strictly convex quadrilateral. Some quadrilateral angle is at least \(\pi/2\). At that angle one incident side is a \(T_D\)-edge of length \(>L_D\), while the other is a source pair of length at least one. The opposite diagonal therefore has squared length
\[
>L_D^2+1=D^2,
\]
contradicting the source diameter.

So every two vertex-disjoint \(T_D\)-edges cross properly.

Edges sharing an endpoint cannot overlap because that would put one source endpoint between two other source points at distance \(<1\).

Therefore \(T_D\), after removing isolated vertices, is a straight-line thrackle.

### 1.3 Exact edge budget

The required straight-line bound
\[
|E(T_D)|\le|V(T_D)|
\]
has a direct proof in this setting.

At every incident extreme vertex choose the first incident \(T_D\)-ray in clockwise hull order. Every \(T_D\)-edge is chosen at one endpoint: if an edge \(uv\) were preceded at both \(u\) and \(v\), those two preceding edges would lie in opposite open half-planes of the line \(uv\) and would be vertex-disjoint without crossing, contradicting the thrackle property.

One chosen ray per incident vertex therefore covers all edges.

No use of Conway's topological thrackle conjecture is made.

## 2. Rooted isolate dispatch leaves at most \(d_H\) upper exceptions

Now work in the canonical C-II representative.

Let \(H\) be the full actual diameter graph,
\[
B=V(H),\qquad
q=|B|,\qquad
h=|E(H)|,\qquad
d_H=q-h.
\]

Since every actual diameter has length \(D>L_D\),
\[
H\subseteq T_D.
\]

Let \(Z_T=V(T_D)\setminus B\).

Canonical positive equilibrium implies that every nonisolated source point outside \(B\) is nonextreme: an unloaded nonisolated point is a positive convex combination of its contact neighbors. Since all \(T_D\)-endpoints are extreme, every point of \(Z_T\) is therefore a genuine contact isolate.

Let \(G\) be the union of components of \(T_D\) meeting \(B\), and put
\[
Z_G=V(G)\setminus B.
\]

Choose a spanning forest \(F\) of \(G\) rooted simultaneously at all vertices of \(B\): start breadth-first search from every \(B\)-vertex, and whenever a new isolate is reached, attach it through one parent edge. Thus:

- \(F\) contains exactly \(|Z_G|\) edges;
- \(F\) contains no old diameter edge between two roots;
- every \(z\in Z_G\) has one designated root \(r(z)\in B\).

Define the fixed exception set
\[
\boxed{
J=(E(G)\setminus H)\setminus E(F).
}
\]

By the straight-line thrackle edge bound,
\[
|E(G)|\le q+|Z_G|.
\]

Therefore
\[
\boxed{
|J|
=
|E(G)|-h-|Z_G|
\le q-h
=
d_H.
}
\]

The set \(J\) depends only on the original source, not on a later motion.

## 3. Full-source extension of any sufficiently small binary core motion

Let \(V\) be the nonisolated contact core.

Consider any finite binary core motion
\[
p\longmapsto p+f(p)\Delta,
\qquad
f:V\to\{0,1\},
\qquad
s=|\Delta|<\gamma_D.
\]

Assume:

1. every old unit contact is preserved;
2. every old actual diameter weakly shortens;
3. at least one old actual diameter strictly shortens.

Extend the motion to all source isolates by
\[
f(z)=f(r(z))
\qquad
(z\in Z_G),
\]
and set \(f(z)=0\) for every other isolate.

### 3.1 All inactive upper constraints outside \(J\) are strict

Any inactive old pair of length at most \(L_D\) changes by relative displacement of length at most \(s\), so its final length is at most
\[
L_D+s<D.
\]

An inactive old pair longer than \(L_D\) is a \(T_D\)-edge.

If it lies outside \(J\), then either:

- it is a forest edge in \(F\), whose endpoints inherit the same root label and therefore the same displacement; or
- it belongs to a component of \(T_D\) disjoint from \(B\), in which case both endpoints are isolates left fixed.

So every inactive pair outside \(J\) remains strictly below \(D\).

Hence:

\[
\boxed{
\text{the only inactive upper-distance pairs that can obstruct the extended move lie in }J,
\qquad
|J|\le d_H.
}
\]

This is an all-topology statement. In the cyclic Woodall branch \(d_H=0\), so the dispatch eliminates **every** inactive upper obstruction.

## 4. Near-unit lower witness forced by minimality

Suppose additionally that no edge of \(J\) reaches or exceeds \(D\) at the endpoint.

If no old noncontact reaches distance at most one, then:

- every old contact is still unit;
- every old noncontact stays \(>1\);
- every old diameter is \(\le D\), with at least one strictly shorter;
- every inactive pair is strictly below \(D\).

Thus the endpoint is a triangle-free source with the same contact graph.

If every old diameter became shorter, its diameter is \(<D\), contradicting global optimality.

If some old diameters remain, the endpoint is another global minimizer with the same number of contacts but fewer actual diameter pairs, contradicting the canonical secondary diameter-pair minimality.

Therefore an old noncontact \(xy\) must satisfy
\[
\boxed{
1<|xy|\le1+s,
\qquad
|x'-y'|\le1.
}
\]

The upper bound on the old length is the reverse triangle inequality.

This is a full-source lower-blocker fork after all isolates have been retained and dispatched.

## 5. Simultaneous charging across disjoint binary motions

Let
\[
M_1,\dots,M_k
\]
be old-contact-preserving binary core motions with pairwise disjoint moving core sets. Their displacement vectors may differ, but each amplitude is at most
\[
s_*<\gamma_D,
\]
and each motion weakly shortens every old diameter while strictly shortening at least one.

Use the **same** rooted forest \(F\), root assignment, and exception set \(J\) for every motion.

A core vertex moves in at most one motion. Every isolate inherits its root's membership, so it also moves in at most one motion.

Hence any fixed source pair changes in at most two of the \(k\) motions.

At most
\[
2|J|\le2d_H
\]
motions can have a \(J\)-edge become an upper obstruction.

Every remaining motion must have a near-unit lower witness as in Section 4. One fixed witness pair can witness at most two motions.

Therefore the number \(N_1\) of **distinct** previously strict near-unit witness pairs satisfies
\[
\boxed{
N_1
\ge
\max\left\{
0,\left\lceil\frac{k}{2}\right\rceil-|J|
\right\}
\ge
\max\left\{
0,\left\lceil\frac{k}{2}\right\rceil-d_H
\right\}.
}
\]

This is the source audit's proposed \`C-LONG-PAIR-ISOLATE-DISPATCH\` theorem; the current manifest registers its successor through a different source and audit.

It does not assert that such a family of binary motions exists or that the resulting near-unit witnesses can all be repaired.

## 6. Universal near-unit planar geometry

Now let \(A\) be any finite unit-separated planar source.

For
\[
1<t<\sqrt2,
\]
join every source pair of length at most \(t\).

Then the resulting straight-line graph \(N_t\) is plane.

Indeed, if two such edges with four distinct endpoints crossed, they would be the diagonals of a convex quadrilateral. Some quadrilateral angle is at least \(\pi/2\); the two adjacent source sides are each at least one, so the opposite diagonal has squared length at least two, contradicting \(t<\sqrt2\).

A third source point cannot lie in the interior of one such edge because the two resulting source distances would each be at least one while their sum is below two.

Thus every near-unit pair of length \(<\sqrt2\) is cofacial in the old unit-contact graph.

The threshold is sharp at the unit square.

### 6.1 Axially thin near-unit conflicts form source paths

Fix orthonormal axes \(u,v\). Form a graph \(P\) from source pairs with
\[
1<|r|\le\frac54,
\qquad
|r\cdot v|\le\frac18.
\]

Every such edge has
\[
|r\cdot u|>\sqrt{1-\frac1{64}}>\frac78.
\]

Two neighbors of one vertex on the same longitudinal side would differ by at most
\[
\frac54-\frac78=\frac38
\]
in the \(u\)-coordinate and at most \(1/4\) transversely. Their squared distance would then be at most
\[
\left(\frac38\right)^2+\left(\frac14\right)^2
=
\frac{13}{64}<1,
\]
contradicting source separation.

So every vertex has at most one neighbor in each longitudinal direction. A finite cycle has a vertex of maximal \(u\)-coordinate and would give it two neighbors on the same side.

Therefore:
\[
\boxed{
\text{every component of }P\text{ is a path or an isolated vertex}.
}
\]

## 7. Small binary contact-preserving moves cannot hide inter-owner blockers inside a strict rhombus

Assume a family of disjoint moving owners with displacement vectors \(\Delta_i\), together with zero, has displacement-cloud diameter \(<1\). Assume every old unit contact is preserved for every binary selection of owners, and distinct nonzero owner displacements have positive dot product.

A unit contact cannot join two distinct moving owners. Otherwise the four binary states of that contact would all have squared length one, but the mixed second difference is
\[
-2\Delta_i\cdot\Delta_j<0.
\]

Now let \(F\) be a bounded four-face of the triangle-free unit-contact graph. It is a strict unit rhombus.

If one rhombus vertex moves while its two contact neighbors are fixed, with old unit vectors \(a,b\), contact preservation requires
\[
a\cdot\Delta
=
b\cdot\Delta
=
-\frac{|\Delta|^2}{2}.
\]

The unique nonzero solution is
\[
\Delta=-(a+b),
\]
whose length is
\[
2\cos(\angle(a,b)/2)>1,
\]
because a strict triangle-free unit rhombus has
\[
\pi/3<\angle(a,b)<2\pi/3.
\]

This contradicts the displacement bound.

The same calculation excludes a fixed vertex with its two neighbors in one moving owner.

Thus the only possible ownership patterns on a strict rhombus are:

- all four fixed;
- all four in one owner;
- two adjacent vertices in one owner and the other two fixed.

Consequently any lower blocker joining **distinct moving owners** cannot lie in a bounded four-face.

The only bounded-four-face lower obstruction left is a unary rhombus diagonal.

## 8. Bounded-face isolate dispatch for an actual small O--O binary slab motion

Assume the nonisolated contact core is connected, as in Theorem 5 of the underlying face-localization report and the current canonical successor. Now assume an actual binary slab motion bounded by two complete stopped O--O trains, with all old contacts preserved.

Every boundary edge of a bounded nonquadrilateral contact face is uncut: an O--O train edge cannot terminate on such a face.

Therefore every boundary occurrence of one bounded nonquadrilateral face has one common binary owner label.

Assign every contact isolate in the open region of that face the same owner label.

Assume the full displacement cloud, including zero, has diameter
\[
s<
\min\left\{
\gamma_D,\sqrt2-1
\right\}.
\]

Then these bounded-face isolates create neither lower nor upper obstructions.

### 8.1 Lower safety

Suppose a reassigned isolate \(z\) formed a new contact or overlap with an old source point \(x\).

The old pair obeys
\[
1<|z-x|\le1+s<\sqrt2.
\]

By the planar near-unit theorem, the old segment \(zx\) crosses no contact edge and contains no old source point. Since \(z\) lies in one bounded contact face, \(x\) lies in the same face.

Then \(x\) is either a boundary core vertex or another isolate in that same face. Both receive the same owner translation as \(z\). Their distance is unchanged, contradiction.

### 8.2 Upper safety

A point in the open region of a bounded contact face is nonextreme in the full source hull.

By the variance argument of Section 1, every pair incident with such a point has old length at most
\[
L_D=\sqrt{D^2-1}.
\]

Relative displacement has length at most \(s<\gamma_D\), so every such pair remains strictly below \(D\).

Thus the reassignment creates no upper obstruction.

Therefore:

\[
\boxed{
\text{after bounded-face isolate dispatch, every inter-owner lower blocker lies in the outer contact face or is a unary strict-rhombus diagonal}.
}
\]

No source point is deleted.

## 9. Terminal localization of a bad unary rhombus in a two-boundary slab

Retain the actual slab transposition setup with bounding O--O trains \(\tau_p,\tau_q\), coherently oriented unit directions \(u_p,u_q\), and
\[
\Delta=u_q-u_p,
\qquad
|\Delta|<\sqrt2-1.
\]

Let a strict rhombus on one boundary, say \(\tau_p\), have opposite complete train \(\sigma\).

If \(\sigma\) also crosses \(\tau_q\) in any actual strict rhombus, neither diagonal of the first rhombus can become \(\le1\).

Indeed, if \(v\) is the direction of \(\sigma\), the old diagonal squares are
\[
2\pm2u_p\cdot v>1,
\]
while after the move they are exactly
\[
2\pm2u_q\cdot v.
\]
At the actual crossing with \(\tau_q\), triangle-freeness gives
\[
2\pm2u_q\cdot v>1.
\]

So an actually bad rhombus has an opposite train \(\sigma\) that crosses exactly one boundary.

Complete trains cross at most once; therefore \(\sigma\) enters the middle slab once and cannot leave through either boundary. Exactly one of its terminal occurrences lies in the slab.

Distinct bad rhombi inject into these middle terminal occurrences.

Thus:
\[
\boxed{
\text{every bad unary boundary-rhombus diagonal consumes a distinct transverse stopped-train terminal occurrence in the slab}.
}
\]

With a second family of opposite-shore O--O crosscuts, the same planar crosscut order shows:

- a bad train with an outer-face middle terminal lies in one of the two **exterior** opposite-shore gaps;
- a bad rhombus in an internal opposite-shore gap must terminate on a bounded nonquadrilateral face.

This is a finite localization theorem, not a sublinear terminal-capacity theorem.

## 10. Exact finite verification

The two existing exact verifier families were rerun independently.

\`research/verify_ultrasmall_swap_isolate_dispatch_2026_10_01.py\` passed:

- 2,000 rational source packets;
- 435 inactive strict-long edges;
- all sharp long/extreme/short threshold checks;
- eight near-triangle packets;
- five cyclic unique-partner dispatch amplitudes;
- 14,877 rooted exception packets, including 13,632 nonempty residues and 574 zero-deficiency packets;
- the exact old-contact-preserving isolate-collision regression.

\`research/verify_target_c_swap_face_endpoints_2026_10_01.py\` passed:

- 100 exact seven-point source packets;
- 2,100 old-distance checks;
- 800 preserved contacts;
- 100 lower-cut rhombus overlaps and 100 upper-cut strict-rhombus checks;
- 256 complete-crosscut patterns and 8,704 perimeter-only boundary arcs;
- twenty exact 41-point bounded-face isolate-dispatch repairs;
- 16,400 initial pair checks and 1,200 preserved contacts.

The finite regressions deliberately omit canonical KKT/global-optimality. The universal proposed statements above have analytic proofs; their current authority is determined separately by the manifest and the source reconciliation.

## 11. Scope and frontier effect

The promotion does **not** assert:

- existence of the October 1 arbitrary block transpositions in every canonical source;
- a linear family of binary motions;
- automatic feasibility of every unary rhombus diagonal;
- sublinear outer-face or terminal capacity;
- absence of contact isolates;
- exact-triangle forcing from near triangles.

What it does prove is a reusable blocker normal form.

For any supplied sufficiently small binary core motion:

1. all full-source inactive upper constraints can be reduced to a **fixed** set of at most \(d_H\) long-pair exceptions;
2. a family of disjoint such motions forces many **distinct** near-unit lower witnesses unless those \(d_H\) edges explain them;
3. bounded-face isolates can be assigned canonically to their face owner and disappear from both upper and lower obstruction;
4. every remaining inter-owner lower witness is on the outer face or is a unary rhombus diagonal;
5. each bad unary boundary-rhombus diagonal is charged to a distinct transverse stopped-train terminal occurrence.

This is substantially sharper than treating lower/upper blocker populations as arbitrary full-source pairs.

**Historical promotion recommendation (not executed by this preservation):** advance theorem state to \`2026-10-05.audit.60\` and register \`C-LONG-PAIR-ISOLATE-DISPATCH\` and \`C-SMALL-MOVE-FACE-LOCALIZATION\` as canonical.
