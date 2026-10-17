# Hostile audit — disjoint penetration/brace gadget extraction

**Date:** 2026-09-15  
**Reviewed:** `research/target_c_g0071_disjoint_penetration_brace_gadgets_2026-09-15.md`  
**Disposition:** **PASS at proof-only full-core Type-II blocker scope.**  
**LEVEL I STATUS:** **STILL OPEN.**

The candidate starts from the current `g=0.0071` reflection blocker branch and claims
an unbounded family of pairwise vertex-disjoint triples carrying simultaneously a unit
inward contact and a `D-1` near-diameter pair.

## 1. Physical tail count is inherited correctly

The current blocker branch has at least `0.1929093045D-o(D)` distinct selected loaded
sides.  Every beta-straight selected tail has contact degree at most four, and one
physical vertex has at most its degree many occurrences on the outer facial walk.
Therefore deduplication leaves at least

\[
0.19290930455816248/4
=0.04822732613954062
\]

distinct physical tails per diameter scale.  Every retained physical tail keeps one
original selected side occurrence and therefore one valid blocker.

**Verdict:** PASS.

## 2. Penetration-edge injection survives tail deduplication

The audited convex-route signed-penetration theorem makes a simultaneous globally
edge-injective selection for the full straight-occurrence family.  Restricting that
selection to one occurrence for each distinct physical tail preserves physical edge
injectivity.  Thus the candidate really has one distinct selected unit contact per
retained tail.

The signed inward component remains strictly larger than
`sin(pi/3-beta_0)>1/2` relative to the retained occurrence's loaded-side normal.

**Verdict:** PASS.

## 3. A linear contact matching follows from bounded contact degree

The selected penetration graph has one edge per distinct tail and is a subgraph of the
positive contact graph.  C26 bounds contact degree by five, so its maximum degree is at
most five.  Greedy edge deletion gives matching size at least `m/(2*5-1)=m/9`, namely

\[
0.04822732613954062/9
=0.00535859179328229
\]

per diameter scale up to `o(D)`.

No claim that all selected tails themselves survive the contact matching is made.

**Verdict:** PASS.

## 4. Triple-conflict degree is sublinear

The penetration matching makes all `x,w` endpoint sets pairwise disjoint.  Thus every
remaining triple conflict uses at least one blocker occurrence.

The blocker-reuse theorem is uniform over the physical source: a fixed source point is
used as blocker by only `o(D)` selected loaded sides.  The successive restrictions to
one occurrence per tail and to the penetration matching cannot increase that
multiplicity.

For one gadget:
- its blocker can equal blockers of only `o(D)` other gadgets;
- its blocker can equal an `x` or `w` endpoint of at most one other matching edge;
- either of its two contact endpoints can be the blocker for only `o(D)` other gadgets.

Hence the gadget conflict graph has maximum degree `o(D)`.

**Verdict:** PASS.

## 5. The independent-set conclusion has exactly the stated strength

There are `Omega(D)` matched penetration edges and conflict degree `o(D)`.  Greedy
vertex deletion therefore produces `Omega(D)/o(D)->infinity` mutually nonconflicting
gadgets.  Independence in this conflict graph is exactly pairwise disjointness of the
three physical source points.

The proof supplies no rate beyond divergence and correctly claims none.

**Verdict:** PASS.

## 6. Orientation statement is qualitative and valid

The blocker-reuse proof already establishes that every `D-1` blocker is uniformly
asymptotically antipodal to its selected tail and that the selected loaded-side normal
is asymptotically radial.  Therefore the long pair points in the inward normal
direction up to `o(1)`.  The unit penetration edge has a fixed signed inward component
above `1/2`.  The two legs consequently occupy the same inward macroscopic half-plane.

No stronger finite angle is asserted for the long pair.

**Final disposition:** **PASS. C-II remains open.**
