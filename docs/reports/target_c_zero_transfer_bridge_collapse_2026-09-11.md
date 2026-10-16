<!-- theorem-state: {"artifact_id":"ART-05D676C261FB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - zero-transfer bridge collapse

**Date:** 2026-09-11  
**Target:** Target C, C-II common-block phase  
**Status:** STILL OPEN; hold report  
**Depends on:** promoted C53/C63 normalization, the report-level C56 zero-transfer
split localization, mixed-support 3-connectivity, and the bridge endpoint-flow
theorem  
**Scope:** the nonisolated positive contact core; contact-isolated source points are
not removed from the original configuration

## 1. Theorem

Let (C) be the positive contact graph of the C-II representative and (H) its
full actual positive diameter graph. Assume (h=|H|ge3) and that the C56
zero-transfer alternative holds:

\[
 K=Q^{\mathsf T}\Lambda^+Q=\operatorname{diag}(\beta_e^{-1}).
\tag{ZB.1}
\]

Then every contact bridge (a b) has a singleton side (for a core with at least four
vertices). Consequently every contact bridge
has a side containing at most two vertices of
the nonisolated contact core. Consequently, if the core has a 2-edge-connected
block with at least three vertices, it has exactly one such block. Every branch
attached to that block contains at most two core vertices. If (r) is the number
of such branches, then

\[
 |V(C)|=|V(B_0)|+s,
 \qquad s\le2r\le2q,
\tag{ZB.2}
\]

where (B_0) is the unique nontrivial block and (q) is the number of loaded
diameter endpoints. In particular (s=O(D)), since (q\le\pi D).

The conclusion is conditional on the report-level C56 split-localization theorem;
the mixed 3-connectivity and bridge endpoint-flow inputs are separate stated
dependencies. It does not bound the contact-isolated population (n-|V(C)|).

## 2. A bridge split cannot see three diameter edges

Fix a contact bridge (ab). Deleting it partitions the contact core into (S,T),
with (a\in S), (b\in T). Let (z\in\{-1,0,1\}^h) be the signed boundary
indicator of this cut on the oriented diameter edges:

\[
 z_e=\begin{cases}
 1,&\text{if the oriented endpoints of (e) go from (S) to (T)},\\
 -1,&\text{if they go from (T) to (S)},\\
 0,&\text{otherwise.}
 \end{cases}
\tag{ZB.3}
\]

The bridge response contributes a positive Kalmanson interval-split term with split
vector (z). This is the standard bridge term in the circular-planar response
decomposition: the bridge has positive resistance, and every selected terminal
pair crossing its cut uses that resistance. Thus (z) is one of the positive split
vectors to which C56.30 applies.

Under (ZB.1), C56.30 says that every positive split vector has support of size at
most two, with the two coordinates, if present, adjacent in projective diameter
order. Therefore

\[
\#\{e\in H:e\text{ crosses }S|T\}\le2.
\tag{ZB.4}
\]

This is the electrical part of the argument. It uses the bridge's actual positive
resistance; it does not infer a sign for an arbitrary 2-edge-connected common block.

## 3. Redundant mixed rigidity contradicts every nonsingleton bridge side

Suppose both (|S|\ge2) and (|T|\ge2). The full-support KKT relation makes every
row of the mixed rigidity matrix redundant. A rank count across the cut therefore
gives at least four mixed bars across (S|T). One of them is the contact bridge
(ab), so

\[
\#\{e\in H:e\text{ crosses }S|T\}\ge3,
\tag{ZB.5}
\]

contradicting (ZB.4). Hence

\[
\boxed{\min(|S|,|T|)=1}
\tag{ZB.6}
\]

for every contact bridge in a core with at least four vertices. This is stronger than
the 3-vertex-connectivity matching estimate: the matching estimate alone loses one
diameter edge because the contact bridge may occupy one matching slot.

The distinction between (ZB.4) and the weaker matching statement matters: a
matching of size three only forces two diameter edges because (ab) can occupy one
matching slot. The three-diameter bypass count is the separate mixed-rigidity input.

## 4. Bridge-tree consequence

Contract every maximal 2-edge-connected block of (C). The resulting graph is a
tree. A simple contact block with at least two vertices and no bridge internally has
at least three vertices; a two-vertex contact component would be a single contact
edge and hence a bridge.

If two distinct contracted blocks (B_1,B_2) each contained at least three core
vertices, every bridge on the tree path between them would have at least three core
vertices on both sides. This contradicts the conclusion of Section 3. Therefore
there is at most one block (B_0) with at least three vertices.

Every branch incident with (B_0), viewed as the full component on the far side of
its first bridge, is a singleton by (ZB.6). The bridge endpoint-flow theorem says
that every such branch contains its loaded diameter endpoint:
otherwise no positive diameter edge would cross that bridge, contrary to the fact
that every positive contact bridge separates endpoints of a positive diameter edge.
Distinct branches are disjoint, so (r\le q). If (s) is the total number of core
vertices outside (B_0), then (s=r\le q), which strengthens (ZB.2) to

\[
|V(C)|=|V(B_0)|+r,\qquad r\le q\le\pi D.
\tag{ZB.7}
\]

If no block (B_0) exists, (ZB.6) says that every edge of the contact tree has a
singleton side, so the tree is a star. The triangle-free unit-contact degree bound
then gives (|V(C)|\le6). Thus the no-(B_0) case is finite.

If no such block (B_0) exists, (C) is a tree. Since a triangle-free unit-contact
graph has maximum degree five, the same side-size conclusion implies that a tree
with at least six vertices has a centroid whose incident branches have size at most
two, and hence has at most (1+2\cdot5=11) vertices. Thus the no-(B_0) case is
finite and cannot contain a quadratic nonisolated core. This auxiliary bound is not
needed for (ZB.2), which is stated only when (B_0) exists.

The source points outside the positive contact core, including contact-isolated
points, are not included in (s). No population conclusion about them follows.

## 5. Consequences and non-consequences

The theorem removes a specific zero-transfer topology: a large bridge tree with
several macroscopic contact blocks, two-vertex bridge ears, or a long bridge-side
population. In the zero-transfer phase the nonisolated core is a single large
2-edge-connected contact block up to (O(D)) singleton bridge leaves.

It does not close any of the following:

* a large 2-edge-connected triangle-free contact block with near-quadrangulation;
* contact-isolated source points inside its convex hull;
* the strictly negative-transfer branch (min_{e\ne f}K_{ef}<0);
* the absence of an opposing upper bound for the high-surplus ledger.

In particular, (s_Z=0) does not follow from (ZB.1), and the theorem does not
justify extending any (s_Z=0) identity to the positive-(s_Z) branch.

## 6. Regression audit

* A single pendant loaded vertex is allowed: its bridge has a one-vertex far side.
* A two-vertex pendant branch is excluded in a core with at least four vertices:
  its first bridge has two vertices on the far side and at least two on the other
  side, so redundant mixed rigidity requires three diameter bypasses.
* A bridge between two large contact blocks is excluded by the same four-edge cut
  count and zero-transfer split support.
* A common 2-edge-connected block is not excluded; the weighted four-cycle sign
  regression remains applicable to that block.
* Contact-isolated source points are untouched.
* Regular odd diameter shells are not claimed to satisfy the C-II KKT and
  mixed-rigidity hypotheses.

The report is therefore a genuine zero-transfer bridge reduction, not a Level I
closure.
