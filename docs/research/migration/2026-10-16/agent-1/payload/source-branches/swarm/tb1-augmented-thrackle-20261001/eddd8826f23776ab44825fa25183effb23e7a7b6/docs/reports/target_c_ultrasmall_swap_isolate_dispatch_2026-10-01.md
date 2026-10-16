<!-- theorem-state: {"artifact_id":"ART-03A351C154DD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — sharp long-pair augmentation and isolate dispatch for small swaps

`candidate lemma -> full-source upper-distance feasibility of the exact block swap ->
strict sub-D competitor or smaller diameter-pair count unless a near-unit pair blocks`

**Date:** 2026-10-01  
**Starting shared HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`  
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`  
**State version:** `2026-09-14.audit.51`  
**Mission:** nonconstant-phase TB1 ONE-SIGN augmented-system closure. The separate
gap-reaction PR #594 and local gap-thrackle branch are not inputs to this packet.  
**Branch:** `swarm/tb1-augmented-thrackle-20261001`  
**Classification:** proved candidate awaiting promotion for Sections 1–5; conditional
application to the unpromoted block-swap chain in Section 6; regression in Section 8.
The artifact lifecycle is unreviewed.  
**Level I / C-II:** STILL OPEN.

## 1. Sharp long-pair theorem on the entire source

Let A be any finite unit-separated planar set with diameter D>1. Put

\[
L_D=\sqrt{D^2-1},\qquad
\gamma_D=D-L_D=\frac1{D+L_D}.
\]

Draw the simple graph T_D containing exactly the pairs with length **strictly**
greater than L_D. Then every endpoint is an extreme vertex of conv(A), and any two
edges with disjoint endpoints cross properly. Edges sharing an endpoint meet only
there. Thus, after omitting its isolated vertices, T_D is a straight-line thrackle.

### Proof: extreme endpoints

If p is not extreme, write p=sum_i lambda_i a_i, with a_i in A\\{p}, lambda_i>=0,
and sum_i lambda_i=1. For every q in A the exact variance identity gives

\[
|p-q|^2
=\sum_i\lambda_i|a_i-q|^2-\sum_i\lambda_i|a_i-p|^2
\le D^2-1.
\tag{1}
\]

The second sum is at least one by source unit separation. Thus p cannot be incident
to a T_D edge. This includes vertices on the relative interior of a hull side.

### Proof: crossing

Four different endpoints of T_D edges are four extreme source vertices, so they
form a strictly convex quadrilateral. If the two segments fail to cross, they are
opposite sides of that quadrilateral. Some interior angle is at least pi/2. Its two
incident sides comprise one of the two long sides and one source pair of length at
least one. The diagonal opposite this angle consequently has squared length

\[
\ge (\text{long side})^2+(\text{other side})^2
>L_D^2+1=D^2,
\]

contradicting the source diameter. Distinct edges at one endpoint cannot overlap,
since then one of the other two extreme endpoints would lie between source points.
This proves the theorem. No global-optimality, KKT, core-population, or lattice
hypothesis was used. All contact isolates remain in A.

## 2. Exact augmentation budget

Let H be the full actual diameter graph, B its endpoint set, q=|B|, h=|H|, and
d_H=q-h. Let Z_T be the endpoints of T_D outside B. The straight-line thrackle
edge bound gives

\[
|T_D|\le q+|Z_T|,\qquad
\boxed{|T_D\\setminus H|\le d_H+|Z_T|.}
\tag{2}
\]

In particular, the number of inactive long pairs with both endpoints in B is at
most d_H, by applying the same edge bound to the induced graph on B. In the cyclic
case d_H=0 there are **no** such pairs, so every inactive B–B distance is at most
L_D. This is a finite inverse-diameter gap, not an asymptotic activity assumption.

The graph bound used here is the classical bound |E|<=|V| for **straight-line**
thrackles, not Conway's open conjecture for arbitrary curved drawings. Concurrent
proper crossings can be removed by arbitrarily small generic perturbations of the
vertices while preserving every required crossing. This application concerns the
abstract graph and requires no preservation of its lengths during that perturbation.

## 3. Cyclic augmentation is a unique-partner extension

Assume H has an odd cycle. Woodall's classification, together with the straight-line
edge bound, implies that T_D has the same unique odd cycle and every other vertex
is a pendant leaf attached directly to that cycle.

Indeed, T_D contains the cycle of H. The classification puts every noncycle vertex
adjacent to a cycle vertex. For N incident vertices, the cycle and one such attachment
per outside vertex already give N edges; the straight-line bound allows no additional
edge. Since H already has all these mandatory edges on B, T_D has no new B–B edge.
Every z in Z_T has exactly one neighbor c(z), and c(z) is an old cycle vertex. There
are no Z_T–Z_T edges and no edges from Z_T to an old noncycle leaf.

Now assume A is the canonical contact-minimal, then diameter-pair-minimal C-II
representative, with C=C_* and H=H_*. Every hull vertex outside B is contact-isolated:
canonical Theorem 6.1 makes every nonisolated non-diameter vertex strictly surrounded
by its contact neighbors, and hence nonextreme. Therefore **each z in Z_T is an
actual contact isolate**, not an untracked core vertex.

This does not discard these points or assert that the source hull equals conv(B).

## 4. Finite isolate dispatch eliminates every inactive upper constraint

Work in the cyclic representative of Section 3. Let V be the nonisolated contact
core and Z=A\\V. Thus B is contained in V. Suppose a proposed finite core move is

\[
p\longmapsto p+f(p)\Delta\quad(p\in V),\qquad f:V\to\{0,1\},
\qquad s=|\Delta|<\gamma_D.
\tag{3}
\]

Assume it preserves every old contact and weakly shortens every old diameter, with
at least one old diameter strictly shortened. Extend it to the **entire** source by

\[
f(z)=
\begin{cases}
f(c(z)),&z\in Z_T,\\
0,&z\in Z\\setminus Z_T.
\end{cases}
\tag{4}
\]

Every inactive pair stays strictly below D after this extension.

### Proof

An inactive pair longer than L_D is precisely a unique pair zc(z) from Section 3.
Its endpoints receive the same displacement, so its length is unchanged and remains
strictly below D. Any other inactive pair has original length at most L_D. Because
all displacements are either 0 or Delta, its relative displacement has length at
most s, and its final length is at most

\[
L_D+s<D.
\tag{5}
\]

Old diameter pairs have endpoints in V and retain the assumed weak decrease.
The extension changes no old contact because every z in Z is contact-isolated.
All source points, including isolates not in T_D, are retained. This is an exact
finite construction; it neither integrates a tangent velocity nor activates a
strict pair in a KKT system.

## 5. The strengthened minimality fork

Under Section 4, the extended endpoint necessarily has a previously strict source
pair xy with

\[
\boxed{1<|xy|\le1+s,\qquad
|x+f(x)\Delta-y-f(y)\Delta|\le1.}
\tag{6}
\]

Otherwise every old noncontact remains strictly greater than one. Old contacts are
preserved, so the endpoint is triangle-free and has the same contact count. Section
4 guarantees that no inactive pair becomes diametral. If all old diameters shorten,
the endpoint has diameter <D, contradicting global minimality. If some remain, it is
another triangle-free global minimizer with the same contacts and fewer diameter
pairs, contradicting the secondary canonical selection. Hence a new contact or
overlap must occur. Its original pair was strict, its endpoint labels differ, and
the reverse triangle inequality gives (6).

This removes the **inactive near-diameter** alternative from the cyclic branch for
such small moves by a concrete full-source adjustment. It does not merely forbid
blockers with loaded endpoints. The replacement obstruction can involve an isolate
whose new displacement was assigned by (4).

## 6. Application to arbitrary phase block transpositions

Conditional on the unpromoted October 1 fixed-star extraction and arbitrary block
transposition theorem, let one open-cell shore contain r>=2 distinct phases in a
real interval of width W. Choose two phases consecutive in **angular** order with
gap at most W/(r-1); their trains need not be adjacent on the complement-dual path.
The arbitrary-block theorem applies to their physical slab and gives

\[
0<s=2\sin(\varepsilon/2)\le\frac W{r-1}.
\tag{7}
\]

If W/(r-1)<gamma_D and d_H=0, then either the old diameter support is TWO-SIGN, or
the ONE-SIGN core block swap extended by (4) forces (6). The existing theorem supplies
both exact contact preservation and strict shortening of all moving old diameters;
its KKT slab balance ensures at least one moving old diameter exists.

For W<=4K/D, the sufficient condition r-1>=8K gives
s<=1/(2D)<gamma_D. If r>=eta D for fixed eta>0, then

\[
\boxed{s\le\frac{8K}{\eta D^2}}
\tag{8}
\]

for all sufficiently large D, and the forced inactive pair in the ONE-SIGN branch
is O(D^-2)-near-unit. A nonconstant shore with only finitely many distinct phases
does not automatically satisfy either hypothesis.

The new motion agrees with the old slab swap on V. Thus the existing complete-grid
boundary-rhombus immunity is preserved: those four vertices are nonisolated core
vertices and no boundary-rhombus diagonal can supply (6). The obstruction remains
outside those retained local cells; this does not claim a global additive grid chart.

## 7. Controlled short-pair augmentation, and its limitation

For any source A and 0<s<sqrt(2)-1, form P_s from all pairs with length at most 1+s.
This graph has a planar straight-line drawing. Indeed, two crossing edges would be
the diagonals of a convex quadrilateral whose sides are at least one. An angle at
least pi/2 would force one of those diagonals to have length at least sqrt(2), a
contradiction. An edge through a third vertex, or overlapping distinct edges at a
common endpoint, would have length at least two, also impossible.

Thus the near-unit witness in (6) belongs to a geometrically controlled augmented
contact graph. If P_s is triangle-free and n=|A|>=3, planar Euler accounting gives

\[
|P_s\\setminus C|\le2n-4-|C|.
\tag{9}
\]

For the canonical core currency e=2v-delta-2-r_E and n=v+z this reads

\[
|P_s\\setminus C|\le\delta+r_E+2z-2.
\tag{10}
\]

Every pair on the left is included, including pairs between isolates or between an
isolate and the core. If P_s has a triangle, it is only a triangle with three side
lengths in [1,1+s]; this is not an exact unit triangle. No KKT multiplier is attached
to these inactive edges. Sections 7–8 specifically block either unsupported upgrade.

## 8. Exact regressions and failed closing upgrades

1. **Closed long threshold is false.** The rectangle
   (0,0),(1,0),(1,15/8),(0,15/8) is unit-separated, has D=17/8,
   and two disjoint opposite sides of length 15/8=L_D. They do not cross.
   Accordingly T_D uses strict >, not >=. This also defeats enlarging the allowable
   inactive-pair interval beyond gamma_D without another hypothesis.
2. **Extreme-endpoint threshold is sharp.** For
   (-1,0),(0,0),(1,0),(0,15/8), D=17/8 and the nonextreme point (0,0) is
   incident to a pair of length exactly L_D. The variance inequality cannot be
   improved under source unit separation alone.
3. **Near-unit planarity threshold is sharp.** At s=sqrt(2)-1, both diagonals of
   the unit square belong to P_s and cross.
4. **Near triangle does not imply exact triangle.** For t>0, the triangle
   (0,0),(1,0),(1/2,(sqrt(3)/2)(1+t)) has one unit side and two sides with squared
   length 1+(3/2)t+(3/4)t^2. It is triangle-free in the exact contact sense for
   every t>0, however small. This example is not a global minimizer and therefore
   rejects only the geometric exactness inference, not the Level I conjecture.
5. **The forest branch is separate.** A source whose H is a caterpillar forest can
   have new long pairs between old B vertices: rotate one vertex of a diameter-10
   equilateral triangle toward the other through angle 2 arctan(1/10000), keeping
   both radii from the third vertex equal to 10. The third side becomes inactive
   but remains longer than sqrt(99). All three endpoints remain in B; there is no
   isolate to dispatch. Formula (2) bounds that residue,
   but the unique-partner isolate dispatch is not asserted for d_H>0.

## 9. Dependencies and checked literature

Canonical inputs: [shared local structure](../theory/01-local-structure.md), Theorem
6.1 (contact-minimal local trapping); [restored C-I](../targets/target-c/56-ci-restored-frontier.md)
and [C-II normalization](../targets/target-c/01-force-hull-and-shear.md) (C=C_* and
H=H_*); [Woodall topology](target_c_woodall_diameter_topology_2026-09-10.md), claim
C-WOODALL. No ZR/ZF statement is extended to isolates.

Unpromoted route input:
[arbitrary block transposition](target_c_open_cell_block_transposition_2026-10-01.md),
including its [exact swap](target_c_tb1_exact_swap_fork_2026-10-01.md),
[witness cell](target_c_witness_cell_blocker_dichotomy_2026-10-01.md), and
[local immunity](target_c_tb1_swap_grid_local_immunity_2026-10-01.md) dependencies.
The application states their hypotheses explicitly and does not promote their full
extraction ancestry by association.

For the use on unequal-length long pairs, the classical |E|<=|V| theorem for finite
straight-line thrackles was rechecked in Lovasz–Pach–Szegedy,
[On Conway's Thrackle Conjecture](https://lovasz.web.elte.hu/morepapers/thrackle.pdf),
Introduction, p. 2. Woodall's odd-cycle adjacency classification was rechecked in
Collins–Roberts, [Great-circle Tree Thrackles](https://arxiv.org/html/2110.09679),
Theorem 2.3. The latter is the same reliable transcription used by canonical
C-WOODALL. The edge bound is for straight-line drawings; no spherical theorem or
unproved topological thrackle conjecture is used.

## 10. Exact verifier

[verify_ultrasmall_swap_isolate_dispatch_2026_10_01.py](../../research/verify_ultrasmall_swap_isolate_dispatch_2026_10_01.py)
checks rational geometric packets, the strict thresholds, an exact Q(sqrt(3)) cyclic
augmentation and binary isolate extension, and the near-triangle regression. All
comparisons are rational or exact in Q(sqrt(3)); no floating-point tolerance is used.
It is a finite regression verifier, not a replacement for the universal proofs,
an audit of the extraction ancestry, or a global-optimality certificate.

## 11. Frontier effect and the next attacked obligation

The cyclic, sufficiently small, ONE-SIGN branch now has only a near-unit inactive
obstruction, even when all source isolates are retained. Linear distinct-phase
population improves its scale from O(D^-1) to O(D^-2). This is a source-level
strengthening, not closure or a canonical promotion.

The repaired closing target is now: prove that an extended small ONE-SIGN block
swap has no new contact/overlap in its planar P_s graph, or give a second finite
contact-preserving move that removes all such obstructions simultaneously. Counting
alone leaves the exact budget (10), and near triangles leave Regression 4. Neither
gap is discarded.

Still open: TWO-SIGN blocks; cyclic shores with few distinct phases; forest
augmentation d_H>0; exact-phase directed cycles; split-star O–O; inactive interfaces;
macroscopic inactive-container/exterior caps; full-core sources outside this
fixed-star extraction. No global quantifier has been weakened.

Promotion recommendation: preserve as **unreviewed** pending independent audit; admit
no new canonical state or frontier claim in this change.
