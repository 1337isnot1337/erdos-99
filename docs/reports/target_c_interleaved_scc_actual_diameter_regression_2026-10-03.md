<!-- migration-source: path=docs/reports/target_c_interleaved_scc_actual_diameter_regression_2026-10-03.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=cefd362dbc9526ef3968a2a3925ec5a1cab62eb4; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C — actual diameter geometry permits noninterval source and sink SCCs

**Date:** 2026-10-03
**Base:** `7a327e1ad95cd2e9cb035b9b96fb34fd8f12114d`
**Source branch/tip:** `research/full-settlement-collar-20261003` @ `bc52d9f5153c8c936fd3fbf96f755c8d57bbee86`
**Classification:** exact regression; not a canonical-source counterexample.
**Level I / C-II:** STILL OPEN.

## 1. Candidate attacked and exact disposition

The attempted chain was:

`noninterval source/sink SCC -> forbidden actual diameter order/crossings ->
constant open-cell phase or inactive inverse-D blocker -> canonical source
move -> Level I`.

The first implication is false if its hypotheses are only actual diameter
geometry, Woodall topology, physical ordered layers, a common witness star,
positive diameter coefficients, positive open-cell cut resultants, and the
absence of inverse-D inactive near-activity. The family below satisfies all
those hypotheses. Both the source and the sink of its nontrivial condensation
component are noninterval in layer order. They are **nested**, not an
alternating pair of SCCs. A theorem requiring the latter stronger pattern is
not refuted.

The aggregate cut directions below are formal resultants, not directions of
actual contact trains. This regression does not supply a complete opposite
contact shore, four actual contact hosts, vertex KKT equilibrium, or global
minimality. It therefore does not refute the fully hypothesized open-cell
transposition or cut-divergence theorem. It identifies a concrete hypothesis
that a successful synthesis must use instead of inferring it from geometry.

## 2. Exact source and all-pair certificate

Put `U=2sqrt(21)`, `V=4sqrt(6)` and take these thirteen points:

| Name | Coordinates | Layer |
| --- | --- | --- |
| L | (-2,4) | 0 |
| a | (0,0) | 1 |
| p | (0,8) | 1 |
| c | (2,U-V) | 2 |
| c' | (2,U) | 2 |
| z+ | (3,U-V/2+5) | 3 |
| z- | (3,U-V/2-5) | 3 |
| d | (4,U) | 4 |
| d' | (4,U-V) | 4 |
| b | (6,8) | 5 |
| q | (6,0) | 5 |
| R | (8,4) | 6 |
| R' | (318/41,254/41) | 6 |

Straight vertical crosscuts at x coordinates `-1,1,5/2,7/2,5,7` give the
indicated physical layers in the convex source hull. Each cut crosses that
hull in one segment, and its successive left shores are nested proper
boundary intervals. These are geometric crosscuts, not contact-train paths.

The source has diameter `10`. Its actual diameter pairs are **exactly**

\[
ab,\ ad,\ pq,\ qc',\ cd,\ c'd',\ LR,\ LR',\ z^+z^-.
\tag{IS.1}
\]

Every other pair has length strictly between `201/200` and `199/20`.
The exact minimum squared distance is `50-20sqrt(6)> (201/200)^2`;
the maximum inactive squared distance is `50+20sqrt(6)<(199/20)^2`.
The verifier checks all 78 pairs by rational isolating intervals in
`Q(sqrt(6),sqrt(21))`; no floating sign test is used. Equality with 100 is
tested by exact coefficients in the four-element field basis.

Every source point is a diameter endpoint, and every source point is
contact-isolated. In particular the set is unit-separated and contains no
unit triangle. Its diameter graph consists of two 4-vertex paths, one
3-vertex star, and one matching edge: a caterpillar forest, with `q=13`,
`h=9`, `d_H=4`. Every pair of disjoint diameter chords crosses properly;
the exact orientation tests are also certified. No Euler-trail inference
is made.

This source is manifestly nonglobal: thirteen points chosen from the unit
`4 by 4` square grid have diameter at most `sqrt(18)<10`. None of the
regression's geometric statements is promoted to a global-minimizer claim.

## 3. One open cell, positive cut balance, and the condensation graph

The two diameter rays from L to R and R' form a common witness star. Their
directions bound the open projective cell

\[
J=(0,\arctan(9/40)).
\tag{IS.2}
\]

All the other projective diameter directions lie outside J. Choose the
interior rational unit vector `e=(399/401,40/401)`. For every diameter with
distinct endpoint layers, orient `r_h` from the lower to the higher layer.
Use the same gap rule as the open-cell reports: the edge points upward in
layer order when `r_h dot Je>0`, and downward when it is negative.

The directed edges are

\[
0\rightleftarrows6,\qquad
1\rightleftarrows5,\qquad
2\rightleftarrows4,\qquad
1\longrightarrow4,\qquad5\longrightarrow2.
\tag{IS.3}
\]

The within-layer vertical diameter has zero cut support and is omitted
from this gap graph. Its presence ensures that layer 3 also has loaded
source points; the regression does not rely on an empty physical layer.

The SCCs are `{0,6}`, `{1,5}`, `{2,4}`, and `{3}`. In the nontrivial weak
component `{1,2,4,5}`, the source SCC `{1,5}` has two outgoing edges and no
incoming edge, and the sink SCC `{2,4}` has two incoming edges and no
outgoing edge. Both SCCs are noninterval subsets of the full layer order.
This is not a strongly connected condensation disguised by zero weights.

Give each star diameter coefficient 1 and every other actual diameter
coefficient `epsilon=1/100`. All nine coefficients are strictly positive.
For each cut i, define

\[
R_i=\sum_{a_h<i\le b_h}\beta_h r_h,\qquad
A_i=|R_i|>0,\qquad u_i=R_i/A_i.
\tag{IS.4}
\]

Put `B=(810/41,90/41)`. Direct addition gives

\[
\begin{aligned}
R_1=R_6&=B,\\
R_2&=B+\epsilon(16,U),\\
R_3=R_4&=B+\epsilon(24,0),\\
R_5&=B+\epsilon(16,-U).
\end{aligned}
\tag{IS.5}
\]

Every resultant lies strictly inside J, so these are positive coherent
nonconstant open-cell phases. Every cut has an actual directed diameter
crossing in each direction, supplied already by the full-span star.
For arbitrary `mu in J` give each diameter flow
`beta_h |r_h dot Ju(mu)|`. Then, exactly,

\[
\Phi(P_i;\mu)=R_i\mathbin{\cdot}Ju(\mu)
=A_i\sin(\theta_i-\mu),
\tag{IS.6}
\]

and interval divergence is the difference of its endpoint values. This
is ordinary finite cut summation, with no actual contact KKT interpretation.
The positive full-span star also supplies a complete pair of opposite
transverse signs; it supplies no opposite **contact shore**.

## 4. Unbounded diameter, narrow phases, and no inverse-D inactive pair

For any real `s>=1`, scale every source coordinate by s and set
`D=10s`. Retain coefficient 1 on the two star diameters and change every
other coefficient to `1/(100s)`. Formula IS.5 becomes

\[
R_i(s)=sB+C_i,
\quad
C_i\in\{0,(16,U)/100,(24,0)/100,(16,-U)/100\}.
\tag{IS.7}
\]

All phases stay strictly inside J: each wall cross-product is a positive
linear function of s, already positive at s=1. Their nonconstant order
and the directed SCC pattern remain unchanged. Since `|B|>19` and
`|C_i|<1/4`, every angle from B is less than
`arcsin(1/(76s))`. Hence the whole phase window has width less than
`1/(19s)=10/(19D)`. Narrow inverse-D phases alone do not destroy the
condensation obstruction.

Every strict pair in the scaled source has

\[
|xy|-1>s/200,\qquad D-|xy|>s/20.
\tag{IS.8}
\]

Thus, for any fixed `K>0`, once `s^2>80K` there is no previously strict
pair within `4K/D` of either activity threshold. All nine actual diameter
pairs stay exact. This is a fixed-cardinality homothetic family, not an
unbounded-cardinality disproof of Level I.

The absence of such pairs causes no contradiction: the source is not
globally or secondarily minimal, and it has no actual contact train chart.

## 5. Rank delimitation and exact computational role

At s=1, form the formal cut-angle diameter derivative matrix, scaling
column i by its positive `A_i` to avoid additional radicals:

\[
M_{hi}=1_{a_h<i\le b_h}\,[r_h,R_i].
\tag{IS.9}
\]

Its exact rank is 4. Columns 1 and 6 coincide, as do columns 3 and 4;
a certified nonzero 4-by-4 minor gives the matching lower bound. This
regression **does not include full cut derivative rank**, nor the canonical
mixed-core rigidity rank. A lemma requiring one of those hypotheses must
be separately tested. The two column relations hold throughout the
homothetic family; no uniform rank-4 claim for every s is needed here.

Run:

```sh
python3 research/verify_target_c_interleaved_scc_source_2026_10_03.py
```

The standard-library certificate checks every source pair, the complete
diameter graph and chord intersections, the common-star cell, all edge
signs and SCCs, all six exact resultants, positive flows on each cut,
the finite divergence identities, analytic-family bounds, and the stated
rank. It supplies an exact counterexample to the weakened geometry-only
lemma; it establishes no global optimality or canonical contact hypotheses.

Novelty search compared the phase-flux/cut-divergence notes and the
five-point and star regressions in
`target_c_subset_reflection_gap_obstruction_2026-10-02.md`. Those examples
give a contiguous sink or strong connectivity. This one realizes both
noninterval terminal SCCs while retaining a common star and eliminating
the inverse-D inactive escape in an unbounded-diameter family.

The remaining viable bridge must use actual contact-train co-embedding,
full mixed rigidity, stronger SCC alternation forced by those hypotheses,
or source minimality to convert the noninterval ideals into a valid
simultaneous motion. Cut balance and actual diameter topology alone are
insufficient.
