<!-- theorem-state: {"artifact_id":"ART-25714D3C0C0B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Seed 90 — finite rhombus contraction rigidity and dense KKT regressions

**Date:** 2026-10-13 (local run date)

**Base commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`

**State version:** `2026-10-10.audit.234`

**Category:** Independent proof strategy

**Run type:** closing-proof attempt followed by exact falsification

**Claim classification:** proved candidates awaiting independent review;
regressions. Artifact lifecycle: **unreviewed**.

**Level I status:** **STILL OPEN**

**Prompt:** [current whole-problem prompt](../prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md)

**Computation:** [exact verifier](../../research/verify_seed090_rhombus_contraction.py)

**Literature:** a preliminary search was made; no external theorem is imported.

## 1. Closing chain and what failed

The attempted independent mechanism was a finite, possibly discontinuous
rearrangement nonexpansive on every source pair:

```
triangle-free global minimizer admits feasible strict-diameter contraction
    -> same-cardinality packing of diameter < D(n) -> Level I
```

Such a contraction automatically retains contacts, gives simultaneous upper
safety, and handles all source labels. Its existence is the missing premise.
Theorem 1 proves a finite obstruction, including a weaker set of local upper
tests. Theorem 4 constructs a contact-preserving full-source finite bow once
the unnecessary nonexpansive restriction is removed. Theorem 3 refutes the
proposed extension of the contraction mechanism to all dense
triangle-free PSD-KKT sources. It does not refute the global-minimizer-only
premise: the constructed sources have explicit smaller-diameter competitors.

No claim from an open PR is a dependency. This report does not promote or
change the canonical state, nor claim that canonical diameter endpoints have
been extracted into the complex of Theorem 1.

## 2. Finite locking theorem

**Theorem 1 (proved candidate).** Let `P=(p_i)` be any finite planar
unit-separated labelled set. Let `R` be a nonempty finite collection of unit
four-cycles on distinct source labels, with the adjacency graph connecting two
cycles when they share an edge connected. Write `V_R` for their labels.
Let `Q=(q_i)` be a planar placement of **all** original labels with every
distinct pair at distance at least one. Suppose, on each selected cycle:

1. all four edge lengths are one;
2. each of its two diagonal lengths is at most its old length.

Then one Euclidean isometry sends `p_i` to `q_i` for every `i in V_R`.
Neither triangle-freeness nor global optimality is required. The endpoint may
have new contacts and triangles; no feasible interpolation is assumed.

In particular, if `|p_a-p_b|=diam(P)` for some `a,b in V_R`, then
`diam(Q)>=diam(P)`.

### Proof: one cell

For four distinct planar points with consecutive side lengths one, the two
vertices off one diagonal are the two distinct intersections of unit circles
about its endpoints. They lie on opposite sides of that diagonal. Thus the
cycle is a convex rhombus. Its squared diagonal lengths sum to four.
The same holds at the endpoint. Nonincrease of both diagonals forces equality
of both; the complete labelled cell is congruent to its source cell.

All six pair distances in a unit-separated rhombus are at least one. Therefore
the angle between its adjacent unit vectors lies in `[pi/3,2pi/3]`.

### Proof: propagation across an edge

Normalize a common edge to endpoints `(0,0),(0,1)`. In one half-plane the
other two vertices of a unit rhombus are

```
(sqrt(1-t^2),t), (sqrt(1-t^2),t+1),   -1/2 <= t <= 1/2.
```

After aligning one cell, consider an adjacent labelled cell sharing edge
`AB`. It is individually congruent to its source cell. Its two possible
placements fixing `A,B` are the source placement and reflection in `AB`.

If the two cycles share any extra label `X`, that label is off `AB` and
already fixed by the aligned cell. Reflection changes `X`, so it is excluded.
The cycles need not occupy opposite half-planes in this case.

If the cycles share only `A,B`, all their off-edge labels are distinct.
Two such cells cannot lie on the same side: write their lower off-edge
vertices as `v(t),v(u)` in the parameterization above, with
`t=sin(phi),u=sin(psi)` and `phi,psi in [-pi/6,pi/6]`. Their distance is
`2 sin(|phi-psi|/2)<=1`. A strict inequality violates unit separation;
equality forces `t,u=-1/2,1/2`, and then the upper vertex of one cycle
coincides with the lower vertex of the other, again on distinct labels.
This exclusion applies both to the source and to the endpoint. The source
cells occupy opposite sides, so reflection of just the neighbor is impossible.

Propagate these two cases along a spanning tree of the cell-adjacency graph.
This proves Theorem 1, including the closed-angle boundary and shared-label
cases. QED.

**Correction provenance (2026-10-15).** The preceding case split incorporates
[PR #979's exact overlap audit](seed090_shared_edge_overlap_audit_2026-10-14.md)
at source `9682cab4815fd31d41b6cd2049e15c6a6966b3ca`. The original
PR #972 head `1c11b028541570cdd786fc1a8d1dfa337ca99a96` incorrectly excluded
all same-half-plane cells, even when the coincident position was the same
source label. The five-label fixture rejects that sentence; it does not
refute Theorem 1. No extra endpoint hypothesis has been added.

**Corollary 2 (proved candidate, full-source contraction and isolate bound).**
Assume instead that `Q` is unit-separated and
`|q_i-q_j|<=|p_i-p_j|` for **every** source pair. Then Theorem 1 applies.
After its isometry has been removed, put `K=conv{p_i:i in V_R}`. Every source
label in `K`, including every contact isolate there, is fixed. For any other
source label,

```
|q_i-p_i| <= 2 dist(p_i,K).
```

Consequently for every old diameter pair `a,b`,

```
|q_a-q_b| >= diam(P)-2 dist(p_a,K)-2 dist(p_b,K).
```

**Proof.** Unit separation and nonincrease force each old contact to stay one.
For `x=sum t_j p_j in K`, with nonnegative weights summing to one, the
weighted squared-distance identity and nonincrease to the anchored labels
give `|q_i-x|^2<=|p_i-x|^2`. If `p_i in K`, take `x=p_i`. Otherwise take
the closest point of `K` and use the triangle inequality. Apply that inequality
again to a diameter pair. QED.

The conclusion fixes only labels in the anchored hull, rather than silently
discarding or fixing every isolate. In a strict competitor preserving the
selected contact edges, at least one selected rhombus diagonal must increase
whenever the complex contains an old diameter pair.

## 3. Dense triangle-free PSD-KKT family blocked against contractions

**Theorem 3 (proved candidate and nonglobal regression).** For every even
integer `m>=24`, there is an explicitly specified finite planar source `A_m`
such that:

- it is unit-separated and triangle-free;
- its actual diameter is `D_m=sqrt(2)m`;
- `|A_m|/D_m^2 -> pi/(2 sqrt(3))` as `m -> infinity`;
- it admits normalized nonnegative equilibrium multipliers with a PSD signed
  stress matrix, affine kernel on its positive-contact rim, and zero rows on
  the other labels;
- no unit-separated nonexpansive placement of all its labels can strictly
  reduce its diameter;
- an independent, same-cardinality triangular-lattice packet has diameter
  strictly below `D_m`.

These are **nonglobal** sources, not Level I counterexamples, canonical C-II
sources, or a proof of local minimality.

### Construction and full pair ledger

Put `R=m/sqrt(2)`, `h=floor(R)`, `r=h-10`, `s=h-1`, and
`beta=1+1/m^2`. Let `F_m` be the square-grid frame

```
{(i-m/2,j-m/2): 0<=i,j<=m,
                    min(i,j,m-i,m-j)<=1}.
```

It has `8m-8` labels. Let `Lambda` be the unit triangular lattice with basis
`(1,0),(1/2,sqrt(3)/2)`. Form `beta Lambda intersect B_r(0)` and delete
exactly those labels whose distance from some frame label is at most one.
Call the remaining set `I_m`, and set `A_m=F_m union I_m`.

Frame pairs are integer-grid pairs, hence unit-separated and triangle-free.
Distinct fill pairs are at distance at least `beta>1`; every fill label is a
contact isolate. Cross pairs are strictly above one by the explicit deletion.
There are no triangles involving a fill label. All frame labels lie in the
radius-`R` disk, and all fill labels lie in the smaller radius-`r` disk.
Every pair is therefore at most `2R`, with strict upper slack on fill-involving
pairs. The only actual diameter pairs are the two pairs of opposite outer
corners. This accounts for every source pair and retains every surviving
isolate in all subsequent statements.

The unit square cells around the frame form one edge-connected rhombic
complex containing all four outer corners. Theorem 1 therefore blocks any
feasible nonexpansive strict-diameter rearrangement of the entire source.

### Density

A centered fundamental parallelogram of `Lambda` has area
`a0=sqrt(3)/2` and lies within distance two of its site. Tiling with these
cells gives, for disk radius `t>=2`,

```
pi(t-2)^2/a0 <= #(Lambda intersect B_t) <= pi(t+2)^2/a0.
```

The scaled lattice has the same bounds after dividing `t` by `beta`.
The deletion neighbourhood is a union of `8m-8` unit disks. A disk about any
frame label contains at most nine points of `beta Lambda`: disjoint
radius-`1/2` disks about them lie in a radius-`3/2` disk. Hence at most
`9(8m-8)=O(m)` fill labels are deleted. Since `r=R-O(1)` and
`beta=1+O(m^-2)`,

```
|A_m|=pi R^2/a0+O(m)=pi D_m^2/(4a0)+O(D_m).
```

This is the optimal **leading coefficient**, not the canonical positive
`D^(2/3)` population reserve. No claim that this family satisfies that reserve
is made.

### Normalized KKT and PSD: complete algebraic proof

The boundary-square KKT construction predates this run: see the unreviewed
[September 12 square-frame regression](target_c_inactive_chamber_kkt_activation_regression_2026-09-12.md),
Section 4. That multiplier mechanism is credited, not claimed as new. The
additions here are the connected rhombus contraction obstruction, disk-wide
leading population, the explicit PSD factorization and kernel check, and
the full-source finite bow. All needed algebra is proved here independently;
the earlier unreviewed report is not used as an unqualified premise.

On each of the `4m` outer rim edges take contact weight `alpha=m/2`; on
each opposite-corner diameter take `beta_H=1/2`; set all other weights zero.
At a noncorner rim label the two contact forces cancel. At each corner the
two inward contact vectors sum to the opposite-corner diameter vector with
the stated weights. All other labels have zero net force. Also

```
sum beta_H=1,      sum alpha=2m^2=D_m^2.
```

For a scalar vector `z` on the rim, write its successive corner values as
`a,b,c,d`. Cauchy-Schwarz on each length-`m` arc gives

```
z^T Omega z
 = (m/2) sum_rim_edges (Delta z)^2
      -(1/2)((a-c)^2+(b-d)^2)
 >= (1/2)((a-b)^2+(b-c)^2+(c-d)^2+(d-a)^2
                         -(a-c)^2-(b-d)^2)
 = (1/2)(a-b+c-d)^2 >= 0.
```

More explicitly this energy is the sum of
`(m/2)(Delta z-(end-start)/m)^2` over the four arcs and their steps,
plus `(a-b+c-d)^2/2`. Its kernel consists exactly of the linear
interpolations on the arcs with `a+c=b+d`: dimension three, spanned by
`1,x,y`. Extending by zero rows retains PSD and adds kernel directions for
**all** other labels; no full-source affine-kernel claim is made.

This stress is not positive on all actual contacts. The positive rim has
`4m` vertices and only `4m+2` mixed edges, so its rigidity rank is at most
`4m+2<8m-3`. Thus it fails the canonical full mixed-rank conclusion. The
ordinary PSD KKT data here cannot replace canonical source hypotheses.

### Strict same-cardinality competitor, including restoration

Let `B_m=Lambda intersect B_s(0)`. Its diameter is at most `2s<2R=D_m`.
The tiling bounds give

```
|A_m| <= pi(R-8)^2/a0+8m,
|B_m| >= pi(R-4)^2/a0.
```

Indeed `r<=R-10`, `s>=R-2`, and `beta>=1`. Their bound difference is

```
(8 pi/a0-8 sqrt(2))R-48 pi/a0 > 0   for m>=24.
```

For a rational verification of positivity, use `3<pi<22/7`,
`5/6<a0<1`, and `sqrt(2)<3/2`. The expression is greater than
`12R-6336/35`, while `m>=24` implies `R>16`; this is positive.
Therefore `|B_m|>|A_m|`. Choose any `|A_m|` labels of `B_m` and assign all
old source labels bijectively to them. The packet is unit-separated, has
strictly smaller diameter, and restores the **entire** cardinality, including
every old contact isolate. Old contacts may be lost and new contacts and
triangles may be created; all are permitted in a global diameter comparison.
This is an endpoint construction, not a proposed feasible motion path. QED.

## 4. A finite source-realized bow that escapes the obstruction

**Theorem 4 (proved candidate).** Let `m>=4` be even. Take the exact frame
`F_m` above and any finite planar unit-separated set `B` disjoint from it.
Suppose every frame--`B` pair is strictly above one, and every pair involving
`B` is strictly below `D=sqrt(2)m`. Then `F_m union B` has a finite
same-label, contact-preserving, strict-diameter competitor keeping every
label of `B` fixed. Thus no source satisfying these hypotheses is a global
minimum-diameter configuration.

There is no assumption that `B` consists of isolates or lattice points. Its
internal contacts are retained. The hypotheses make the two corner diameters
the entire actual diameter graph; this theorem does not provide that
hypothesis for a canonical source. In particular it does not bypass the
canonical linear loaded-diameter count by discarding its other edges.

### Exact construction and finite feasibility

For `0<t<1`, put `c=(1-t^2)/(1+t^2)`, `s_t=2t/(1+t^2)`, and
`k_i=min(i,m-i)`. Replace each frame label by

```
q_ij=(c(i-m/2)+s_t k_j, c(j-m/2)+s_t k_i).
```

Keep all `B` labels unchanged. On a horizontal grid edge the displacement
vector is `(c,+s_t)` or `(c,-s_t)`; on a vertical edge it is
`(+s_t,c)` or `(-s_t,c)`. Each has squared length one. Every original frame
contact is therefore preserved. Since `k_0=k_m=0`, the four corners form
a square of side `cm`: both old diameters have new squared length
`2m^2 c^2<2m^2`.

At `t=0` every other frame pair has squared distance at most
`2m^2-2m+1`; every noncontact frame pair is at least `sqrt(2)`.
All lower frame--`B` gaps and all upper `B`-involving gaps are strictly
positive by hypothesis and finiteness. Continuity therefore supplies one
positive interval on which every such pair remains strictly feasible and
every inactive upper pair stays below the new corner diameter `sqrt(2)mc`.
Consequently the endpoint's actual diameter is that new corner diameter,
its entire contact graph is unchanged, and it retains every source label.
This proves finite feasibility rather than relying on the infinitesimal
velocity. QED.

### Uniform explicit parameter for Theorem 3's dense sources

For `A_m`, take

```
t=1/(1000000 m^12).
```

Every frame displacement is at most `delta=3mt`. Frame noncontacts are
then above one. Their upper squared change is at most
`4D delta+4delta^2`, while the corner squared reduction is at most
`8m^2t^2`; their sum is less than one, hence less than `2m-1`.
Fill-involving old upper squared gaps exceed one, and their changes plus
the corner reduction are also less than one.

For completeness, a frame--fill squared lower gap has the form
`(a+b sqrt(3))/(4m^4)>0` with integers `a,b`. Writing the fill coordinates
as `((m^2+1)(2i+j),(m^2+1)j sqrt(3))/(2m^2)`, and using that both fill
and frame coordinates have magnitude below `m`, gives
`|a|+2|b|<=100m^6`. If `b!=0`, the integer norm `a^2-3b^2` is nonzero,
so conjugation gives `a+b sqrt(3)>=1/(100m^6)`. If `b=0`, its positive
integer numerator is at least one. Thus every surviving cross lower
squared gap is at least `1/(400m^10)`. Its possible loss is at most

```
2D delta <= 9m^2t = 9/(1000000m^10) < 1/(400m^10).
```

Every lower cross constraint stays strict. This explicit rational parameter
therefore gives a full-source finite motion certificate for every even
`m>=24`, with every fill isolate held fixed. New contacts are absent; both
old diameter pairs shorten; all inactive upper pairs remain below the new
diameter. No cardinality restoration is required.

The motion necessarily increases some inactive rhombus diagonals, by
Theorem 1. It shows that a normalized PSD stress and affine kernel on its
positive rim do not exclude this second-order finite descent when the
canonical full mixed-rank hypothesis is missing. This is a scoped regression,
not a reopening of the canonical source-specific stress theorem.

## 5. Exact scope regressions

The verifier supplies independent all-pair rational checks of these fixtures.

**Vertex-only adjacency is insufficient.** Start with the seven labels
`0,(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1)`.
Keep the first square fixed and rotate the second using cosine `24/25` and
sine `7/25`. Its nonzero vertices become
`(-24/25,-7/25),(7/25,-24/25),(-17/25,-31/25)`.
All old contact lengths and both diagonals of each cell are unchanged,
every pair remains at least one, no new contacts or triangles appear, and
diameter squared decreases from `8` to `196/25`. The cells share only a
vertex. Some inactive cross distances increase: this fixture does **not**
contradict the nonexpansive corollary.

**Outside isolates cannot be silently fixed.** A fixed unit square together
with the isolate `(4,0)` has diameter squared `17`. Moving that isolate to
`(3,0)` is feasible and nonexpansive, and gives diameter squared `10`.
The isolate is outside the anchored hull, and the old diameter is not carried
by the square complex. This verifies the need for both hypotheses.

**Planarity matters.** A spatial regular tetrahedron has every pair at one.
Its cyclic four-edge subgraph preserves the four sides of a planar unit
square while strictly shortening both diagonals. The Gram matrix on the
three nonzero vertices has diagonal one and off-diagonal `1/2`; its
determinant is `1/2>0`, so its rank is three. It is a counterexample to a
dimension-free version, not a planar endpoint.

## 6. Verification and frontier effect

Run:

```
python3 research/verify_seed090_rhombus_contraction.py
```

The script checks exact source and bowed-endpoint pair classes and comparison
counts for three dense frames; a rational sum-of-squares matrix factorization of the rim stress;
normalized equilibrium; connected cell incidence containing the diameter
corners; exact propagation-angle identities; and the three scope fixtures.
Square-root comparisons use squared rational/integer predicates, never
floating-point tolerances. The infinite theorems are proved above rather than
inferred from these finite executions.

The completed CPython 3.14.7 run certified 305, 1471, and 4519 source labels
at `m=24,40,64`, retaining respectively 121, 1159, and 4015 contact isolates.
Their full pair partitions have 46360, 1081185, and 10208421 pairs. The
independent comparison packets have 823, 2653, and 7015 labels, respectively.
The theorem-state checker, PR-state checker against the frozen base,
relative-link check, and staged whitespace check pass locally.

[Hosted run 38513960331](../publication/provenance.md#source-records)
at proof commit `97de41cb` executed **zero steps**. Its check annotation says
the job did not start because recent account payments failed or the spending
limit needs increasing. This is unavailable hosted CI, not a passing run and
not an executed theorem-state validation failure.

The three mechanisms considered were: a finite nonexpansive global
rearrangement (obstructed by Theorem 1); contact-preserving train bending
(Theorem 4 supplies a finite endpoint and the complete inactive pair ledger
in its stated source class); and propagation from separately congruent cells
or an anchored hull (the vertex hinge and outside isolate show exactly why
the stronger propagation assertions fail). These are finite geometric
questions; none assumes that first-order feasibility integrates.

**Level I and Targets A/B/C are unchanged.** This contribution rejects a
class of universal transformations under reduced inputs and constructs a
full-source finite descent for the exact frame class. That class is already
incompatible with the canonical large-source loaded-diameter count; no new
canonical branch is closed. This work does not extract
an anchored diameter pair from an arbitrary canonical source, eliminate a
canonical branch, or prove global optimality of a regression.

The next exact obligation for this approach is a source-specific simultaneous
endpoint permitting the necessary increases of rhombus diagonals while
preserving all unit lower bounds, strictly shortening every diameter pair,
and retaining the full isolate population. Neither the PSD stress certificate
nor near-optimal leading density supplies that endpoint. Independent review
is required before any theorem promotion; no promotion is requested here.

## Reconciliation and bounded review (2026-10-15)

This noncanonical artifact consolidates PR #972 at
`1c11b028541570cdd786fc1a8d1dfa337ca99a96` and its correction PR #979 at
`9682cab4815fd31d41b6cd2049e15c6a6966b3ca`. The propagation paragraph above
is corrected; the original frame motion, density, stress proof and finite
checker inputs are unchanged. The original run ledger is historical.
OpenAI Codex inspected the cell-congruence and overlap cases, convex-hull
inequality, stress factorization, finite-bow continuity and explicit-gap
arguments and replayed the supplied checkers. It also checked the overlap
fixture in a separate symbolic implementation. This is a substantive AI audit,
not independent human peer review; the report remains unreviewed.

For an independent review, first check all shared-label and exact-edge
propagation cases and the planar one-cell argument, then check Theorem 4's
full pair partition and the quadratic-field norm bound that gives the uniform
parameter for every even `m>=24`. The finite fixture replays support those
computations but do not establish the universal statements. The sources are
nonglobal and fail canonical full-support/mixed-rank conditions. A canonical
application still requires a simultaneous endpoint for its full loaded diameter
graph, all inactive lower/upper pairs and all isolates. No such extraction,
C-II closure, or theorem promotion is claimed. Original source authors and
PR #979's correction credit are retained.
