<!-- theorem-state: {"artifact_id":"ART-A016E83809E9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — common-vector swaps force a source-anchored blocker tree

`common-vector ONE-SIGN slab swaps -> every union has an outgoing inactive blocker -> a source-anchored tree with r distinct pairs -> at least r-t cofacial near-unit edges; an actual release remains required`

**Date:** 2026-10-01  
**Shared starting HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`  
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`  
**First checkpoint:** `439d9ac9`  
**State version:** `2026-09-14.audit.51`  
**Mission / branch:** nonconstant-phase TB1 augmented inactive-system closure; `swarm/tb1-diameter-order-20261001`.  
**Classification:** proved candidate awaiting promotion under the explicit finite-move hypotheses; conditional train/rooted application. Artifact lifecycle is unreviewed.  
**Level I / C-II:** OPEN / OPEN.

## 1. Exact source-level statement

Let A be a finite unit-separated global minimum-diameter source, chosen to minimize
contact count and then diameter-pair count. Retain all source points. Suppose there
are r>=1 nonempty disjoint vertex sets L_1,...,L_r and a common nonzero vector Delta
of norm s such that translating any **one** L_i by Delta has the following properties:

1. Every old unit contact remains a unit contact.
2. Every old diameter pair changed by that translation strictly shortens.
3. At least one old diameter pair changes.

The individual endpoint need not be feasible for inactive source pairs. Let L_0
contain all remaining source points. For i!=j, draw a directed arc i->j whenever
there is an initially strict source pair xy, with x in L_i and y in L_j, for which
translating x by Delta while fixing y gives either

\[
 |x+\Delta-y|\le1\quad\text{or}\quad |x+\Delta-y|\ge D. \tag{1}
\]

Arcs out of 0 are not needed. Each arc is labelled by its actual source pair and
whether it blocks the lower or upper distance constraint. Then every vertex
i=1,...,r has a directed path to 0, and there is an outgoing arborescence toward 0
with r arcs labelled by **r distinct actual inactive source pairs**.

If D>=2 and 0<s<=1/(2D), and

\[
 t=|\{xy:\sqrt{D^2-1}<|xy|<D\}|,
\]

at least r-t tree labels satisfy

\[
 \boxed{1<|xy|\le1+s\le1+1/(2D).} \tag{2}
\]

In particular, using the preceding capacity theorem,

\[
 \boxed{N_1\ge\max\{0,r-t\}
 \ge\max\{0,r-(\lfloor\pi D\rfloor-h)\}.} \tag{3}
\]

This strengthens the disjoint-slab estimate ceil(r/2)-t when the swaps share one
vector. The labels are planar/cofacial Gabriel edges, but are not asserted to be
active or positively stressed.

## 2. All unions preserve the old active constraints

There is no old diameter pair joining two different L_i,L_j with i,j>0. If a pair
with relative vector z did so, conditions 2 for the two individual translations
would give

\[
 |z+\Delta|^2<D^2,\qquad |z-\Delta|^2<D^2,
\]

although |z|^2=D^2. Adding contradicts

\[
 |z+\Delta|^2+|z-\Delta|^2=2D^2+2s^2>2D^2. \tag{4}
\]

For any nonempty U subset {1,...,r}, translate the entire union of its L_i by
Delta. Any pair with both endpoints in that union is unchanged. Any pair with
exactly one endpoint there undergoes exactly the same change as in the
corresponding individual translation.

Thus every old unit contact stays unit. Every changed old diameter strictly
shortens; every unchanged old diameter stays unchanged. At least one old diameter
changes: choose i in U and use condition 3. Its other endpoint belongs to L_0 by
(4), so it is fixed under the union move.

This verifies simultaneous compatibility, instead of assuming that individual
feasible exchanges can be combined.

## 3. Minimality forces a blocker out of every nonempty union

Suppose U has no outgoing labelled arc to its complement, including 0. Then every
initially strict pair whose distance changes remains strictly between 1 and D at
the union endpoint. Pairs internal to the moving union or its complement are
unchanged. Section 2 handles every old contact and diameter.

The moved source is therefore unit-separated and has exactly the same contact
count. If no unchanged diameter remains, its diameter is strictly below D,
contradicting global minimality. Otherwise it has diameter D with strictly fewer
diameter pairs, contradicting the second lexicographic minimization. Therefore

\[
 \boxed{\text{every nonempty U has a labelled arc to its complement}.} \tag{5}
\]

New unit equalities are included in (1); the proof does not claim that creating a
contact by itself contradicts contact-minimality. No interpolation from zero to
Delta is assumed feasible.

If i cannot reach 0, the set U of all vertices reachable from i is nonempty,
excludes 0, and has no outgoing arc. This contradicts (5). Hence every i reaches 0.
Select at each i an outgoing edge decreasing its shortest directed distance to 0.
The chosen r arcs have no directed cycle and form a tree toward 0.

An actual source pair belongs to just one unordered layer pair {i,j}. It can
label two chosen arcs only if both i->j and j->i are selected. That would be a
two-cycle, impossible in the tree. Thus all r chosen pair labels are distinct.

If L_0 were empty, condition 3 and (4) would already contradict one another. The
fixed-source root is derived from the active-constraint hypotheses, not added as
an artificial external anchor.

## 4. Apply the sharp near-diameter budget

For every chosen pair, the endpoint changes by at most s. A lower blocker has
1<|xy|<=1+s; an upper blocker has D-s<=|xy|<D. For s<=1/(2D),

\[
 D-s>\sqrt{D^2-1}.
\]

Thus every upper blocker is one of the t actual inactive strict-near-diameter
pairs. Distinct tree labels imply that at most t of the r arcs can be upper
blockers. The remaining at least r-t are the near-unit pairs in (2).

By the [strict near-diameter capacity theorem](target_c_strict_near_diameter_capacity_2026-10-01.md),
t<=v_K-h<=floor(pi D)-h, proving (3). That report also proves planarity and
cofaciality of all lower blockers, including all contact-isolated endpoints.

For a rooted sequence with h=pi D-o(D) and r>=cD-o(D), the result is now

\[
 \boxed{N_1\ge(c-o(1))D}, \tag{6}
\]

rather than the earlier cD/2 baseline. More importantly, these are tree labels
anchoring every movable slab to the actual fixed source, not arbitrary independent
pair counts.

## 5. Actual train application and exact remaining obstruction

Two retained exact train phases u and v yield a common Delta=v-u whenever the
selected disjoint slabs have the same boundary ordering (u on the first boundary,
v on the second). The unpromoted finite block-transposition theorem gives contact
preservation. ONE-SIGN gives strict shortening, and its KKT argument supplies at
least one changed old diameter. The theorem therefore applies if
|u-v|<=1/(2D). A linear two-phase population or this amplitude condition is not
inferred from the existing wider phase window.

Canonical dependencies: C-I lexicographic normalization. Unpromoted application
dependencies: [block transposition](target_c_open_cell_block_transposition_2026-10-01.md),
the preceding standalone capacity candidate, and, for (6),
[rooted defect stability](target_c_wrapping_root_defect_stability_2026-09-30.md).

The next exact source obstruction is a tree of strict near-unit constraints
running from movable slabs to fixed source sites. Its rhombus edges have the
one-boundary swept-phase obstruction proved in the preceding report; other edges
lie in non-rhombic, inactive, or exterior faces. To close this route one must
release this source-anchored system by an additional finite move, or use the
actual positive-core/KKT geometry to force a unit triangle. A tree in the layer
quotient does not create a Schur kernel or an exact source contact.

All other C-II branches survive: TWO-SIGN, arbitrary varying phases without a
linear common-vector family, exact-phase gap cycles, split-star O-O,
inactive-interface, macroscopic-container, and higher-surplus full-core.

## 6. Verification and hostile checks

The [exact verifier](../../research/verify_strict_near_diameter_capacity_2026_10_01.py)
enumerates the directed graphs with up to four movable vertices and one fixed root.
It checks the equivalence between (5) and root reachability, constructs the tree,
and verifies that no unordered layer pair is selected twice. The continuous
geometric and finite-move arguments are the proofs above; the graph enumeration
does not encode optimality, KKT, or a train embedding.

The old star/path and planar-witness regressions remain binding. Nothing here
turns a near-unit edge into a multiplier or promotes an unreviewed chart.
Condition 3 is essential: a contact-isolate with no changed diameter cannot
invoke diameter-pair minimality. The common Delta is essential: arbitrary
one-at-a-time swaps need not combine. Canonical state is unchanged.

## 7. Verified synthesis with cyclic isolate dispatch

During the run, [PR #600](https://github.com/1337isnot1337/e-99/pull/600),
commit `eddd8826f23776ab44825fa25183effb23e7a7b6`, independently derived the same
strict long-pair geometry and supplied an explicit isolate dispatch. Its
[proof at the inspected commit](https://github.com/1337isnot1337/e-99/blob/eddd8826f23776ab44825fa25183effb23e7a7b6/docs/reports/target_c_ultrasmall_swap_isolate_dispatch_2026-10-01.md)
was checked. The useful consequence here is stronger than discarding a small
upper-blocker population: **in the cyclic branch the common-swap tree can have
only near-unit labels**, without assuming h=pi D-o(D).

Here is the complete synthesis argument. Assume the old H contains an odd
cycle and the canonical C=C_*, H=H_* normalization. The full long-pair graph T^+
is a convex straight-line thrackle containing that cycle. Woodall's classification
puts every noncycle incident vertex next to a cycle vertex. Its cycle and one
such attachment per remaining vertex already exhaust the edge bound |E|<=|V|.
Consequently every vertex is a cycle vertex or a pendant leaf, and the old H
already exhausts the allowed edges on its own endpoint set B. Every newly
incident vertex z outside B has one unique T^+ neighbor c(z), on the old cycle.

Each such z is a contact isolate. It is extreme by the long-pair theorem;
canonical [Theorem 6.1](../theory/01-local-structure.md) strictly surrounds every
non-diameter nonisolated point by its contact neighbors, making it nonextreme.
Thus all new long edges are precisely zc(z) with isolates z. No isolate is removed.

Enlarge each old moving set L_i by those z whose unique partner c(z) belongs
to L_i; put all other source isolates in L_0. These enlarged sets are disjoint.
For any union of them, both endpoints of every inactive T^+ edge receive the
same displacement, so that edge stays strict. Every other inactive pair has
length at most sqrt(D^2-1) and changes by at most s<=1/(2D), giving final length
strictly below D. Old contacts are unaffected by the isolate assignment; old
diameter moves are exactly the original core moves. Thus all the hypotheses
and union-compatibility arguments of Sections 1–3 survive.

There are now **no upper-blocker arcs** in the union graph. The outgoing
arborescence has r distinct actual near-unit labels:

\[
 \boxed{N_1\ge r\quad\text{in the cyclic dispatched common-vector branch}.} \tag{7}
\]

These edges may involve dispatched isolates far from their old physical slab.
They are still planar/cofacial in the original full-source contact graph.
The geometric graph classification was checked against Collins–Roberts,
*Great-circle Tree Thrackles*,
[Theorem 2.3](https://arxiv.org/html/2110.09679), the reliable Woodall transcription
also used by canonical C-WOODALL. This imports the straight-line graph statement,
not a spherical motion or an unproved curved-thrackle conjecture. The finite
dispatch follows directly from the explicit assignment above.

Claim status: proved candidate under cyclic normalization and the common finite-move
hypotheses; conditional train application. Neither PR is promoted by this synthesis.
The forest branch cannot use this unique-partner assignment; its residual budget
remains (3). A source-anchored tree of inactive lower constraints still needs a
release or an exact triangle theorem. No new global closure is asserted.
