<!-- theorem-state: {"artifact_id":"ART-5DB70BFE6C57","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — strict near-diameter capacity and cofacial swap blockers

`small-amplitude ONE-SIGN swaps -> at most floor(pi D)-h inactive strict-near-diameter pairs -> linear planar/cofacial near-unit blockers -> a source-preserving release is still required`

**Date:** 2026-10-01  
**Shared starting HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`  
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`  
**State version:** `2026-09-14.audit.51`  
**Branch / mission:** `swarm/tb1-diameter-order-20261001`; nonconstant-phase TB1 diameter-order and augmented inactive-system closure. Gap reaction and exact-phase thrackle missions were already claimed.  
**Classification:** proved candidates awaiting promotion for the geometric theorems; conditional for the train application; regression for the threshold extensions. Artifact lifecycle is unreviewed.  
**Level I / C-II:** OPEN / OPEN. C-I remains closed.  
**Active prompt:** [current Target C prompt](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md).  
**Computation:** [exact verifier](../../research/verify_strict_near_diameter_capacity_2026_10_01.py); finite regression checks, not a global-optimality certificate.

## 1. Sharp geometric theorem

Let A be a finite unit-separated planar set of diameter D>1, with noncollinear
convex hull K. Write v_K for the number of extreme vertices of K, H for **all**
actual diameter pairs, and h=|H|. Define

\[
 T^+(A)=\{xy:\sqrt{D^2-1}<|x-y|\le D\}.
\]

Then every endpoint of T^+(A) is an extreme hull vertex, its straight segments
form a thrackle, and

\[
 \boxed{|T^+(A)\setminus H|\le v_K-h\le\lfloor\pi D\rfloor-h.} \tag{1}
\]

No KKT, contact-minimality, triangle-freeness, or optimality hypothesis is needed.
Every source point is retained, including contact isolates. The strict threshold
cannot be replaced by a weak inequality.

### 1.1 Endpoints must be extreme

If x is not extreme, write x=sum_j lambda_j z_j using distinct source points
z_j!=x, with positive coefficients summing to one. Unit separation gives
|z_j-x|>=1. For any y in A the variance identity is

\[
 \sum_j\lambda_j|z_j-y|^2
 =|x-y|^2+\sum_j\lambda_j|z_j-x|^2
 \ge |x-y|^2+1.
\]

The left side is at most D^2. Hence |x-y|^2<=D^2-1, contrary to xy in T^+.
The same argument applies to y. This proves extremality directly; a near-diameter
pair is not being declared active.

### 1.2 Disjoint edges cross

Take ab,cd in T^+ with four distinct endpoints. All four are extreme, so they
form a strictly convex quadrilateral. If the two segments do not cross, they
are opposite sides of this quadrilateral. Put L=min(|ab|,|cd|).
Every quadrilateral angle is incident with one side of length at least L and
one side of length at least 1. At least one angle is at least pi/2. The law of
cosines across that angle gives a diagonal of squared length at least L^2+1>D^2,
a contradiction.

Edges sharing an endpoint meet only there: extreme vertices cannot have another
source hull vertex on the same ray, nor can three extreme vertices be collinear.
Thus T^+ is a straight-line thrackle on the hull vertices.

### 1.3 Edge bound, with a complete proof

At every hull vertex with incident edges, the rays to other vertices lie in a
strict angular wedge of aperture less than pi. Choose the first incident ray in
clockwise order in that wedge. Each vertex chooses at most one edge.

Every edge uv is chosen by at least one endpoint. Otherwise a ray preceding uv
at u, and a ray preceding vu at v, lie on opposite strict sides of the line uv.
Their two segments are disjoint: one leaves u into one open half-plane, the other
leaves v into the other, and their endpoints on the separating line are different.
This contradicts the thrackle property. Therefore the chosen edges cover all
edges, and |T^+|<=v_K.

This is Perles' deletion argument, checked against Pach–Sterling,
*Conway's conjecture for monotone thrackles*, Theorem 1 and its following proof,
[original author-hosted PDF](https://math.nyu.edu/~pach/publications/monotonethrackle110209.pdf).
The argument above supplies the convex-position version actually used here.

Every hull side is at least 1, so v_K<=per(K)<=pi D. Since H is contained in
T^+, subtraction proves (1).

## 2. Exact phase-amplitude threshold

For a block transposition of amplitude s=|u_q-u_p|, the existing finite swap fork
forces an inactive near-diameter pair only within [D-s,D). If

\[
 s<D-\sqrt{D^2-1}=\frac1{D+\sqrt{D^2-1}}, \tag{2}
\]

every such pair belongs to T^+\H. The convenient sufficient condition

\[
 \boxed{0<s\le\frac1{2D}} \tag{3}
\]

is strictly inside (2). In particular, two distinct train directions in a real
phase interval of width at most 1/(2D) satisfy (3), because
s=2 sin(epsilon/2)<=epsilon.

The existing 4K/D window does **not** imply (3). No linear population of swaps
satisfying (3) is asserted merely from the old window.

## 3. Finite near-unit population theorem

Assume a contact-minimal, then diameter-pair-minimal global source, and r
pairwise vertex-disjoint physical slabs admitting ONE-SIGN block transpositions.
Assume every amplitude s_j satisfies (3), every old contact is preserved at the
swap endpoint, and every moving old diameter strictly shortens. These are the
exact hypotheses of the existing block-swap application, with the additional
amplitude condition.

Set t=|T^+\H|. At most 2t slabs can have no endpoint-blocking near-unit pair.
Indeed, the finite minimality fork then supplies a pair in T^+\H; its distance
can change for at most two disjoint slabs, one per endpoint.

Every other slab has an inactive pair with

\[
 1<|xy|\le1+s_j\le1+\frac1{2D}.
\]

Again a fixed pair can change for at most two slabs. Thus the number N_1 of
distinct such near-unit pairs satisfies the exact finite bound

\[
 \boxed{N_1\ge\max\{0,\lceil r/2\rceil-t\}
 \ge\max\{0,\lceil r/2\rceil-(\lfloor\pi D\rfloor-h)\}.} \tag{4}
\]

This uses the endpoint fork, not a claimed feasible interpolation to the swap.
A new unit contact at the endpoint is included as a blocking near-unit event;
contact-minimality is not incorrectly used to prohibit creating contacts.

If h=pi D-o(D) and r>=cD-o(D), (1) and (4) give

\[
 \boxed{N_1\ge(c/2-o(1))D.} \tag{5}
\]

Consequently **inactive near-diameters cannot account for a linear disjoint
ONE-SIGN population at this smaller amplitude**. This eliminates one arm of
that conditional fork, not the whole nonconstant-phase branch.

## 4. Near-unit blockers form a planar cofacial augmentation

For any unit-separated finite set, every pair pq of length less than sqrt(2)
has an empty closed diameter disk. For z in that disk,

\[
 |z-p|^2+|z-q|^2
 =2|z-(p+q)/2|^2+|p-q|^2/2
 \le |p-q|^2<2,
\]

contradicting |z-p|,|z-q|>=1. Thus pq is a strict Gabriel edge without any
nearest-neighbor assumption.

The set of **all** pairs of length less than sqrt(2) is planar. If two such
segments crossed, their four endpoints form a convex quadrilateral with all
sides at least 1. At an angle at least pi/2, the opposite diagonal would have
length at least sqrt(2), a contradiction. A segment of length less than 2
cannot pass through another source point, since both intervening distances
would be at least 1.

For D>=2, all pairs in (4) have length at most 5/4<sqrt(2). They and every
old unit contact can therefore be drawn simultaneously with no crossings.
The open segment of a new edge stays in a single face of the original contact
graph. The endpoints are cofacial, including the possibility of an inactive
or exterior face and endpoints that were contact isolates.

This is an augmented **geometric** graph. Its new edges have length strictly
greater than 1 and have no asserted positive KKT multiplier. Planarity does not
promote them to active constraints or produce an exact unit triangle.

## 5. Push the cofacial classification into actual rhombi

Suppose a near-unit witness in (4) lies in a bounded strict-rhombus face of the
original contact graph. It is necessarily one diagonal. If its distance changes
under the slab transposition, that rhombus crosses exactly one of the two
boundary trains: two trains on the same narrow phase shore cannot cross in a
strict rhombus.

Let sigma be the other train through that rhombus. If sigma crossed both boundary
trains, swapping their directions would give old rhombus diagonal lengths again,
by the complete-grid local-immunity proof applied to sigma itself. Therefore

\[
 \boxed{\text{a rhombus near-unit blocker uses a transverse train crossing
 exactly one of the transposed boundaries}.} \tag{6}
\]

There is also an exact phase-order certificate. Orient the rhombus sides a,b
so their acute crossing angle is theta=pi/3+delta, with delta>0. Its short
diagonal has length 2 sin(theta/2). After replacing the selected side direction
by the other boundary phase, a blocking diagonal has length at most 1, so the
new delta is at most zero. Because the phase replacement is at most 1/(2D),
the same angle lift remains valid for D>=2. In that lift, the transverse
train's phase threshold is strictly beyond the old phase and weakly before
the replacing phase (or the reversed inequalities). It lies in the half-open
phase interval swept by the transposition.

Thus the remaining near-unit population splits into:

1. rhombus diagonals with a one-boundary transverse train and the explicit
   swept-phase order obstruction (6); or
2. chords within non-rhombic, inactive, or exterior faces.

The first class is broader than the retained complete rectangle: its transverse
train is necessarily outside the common-crossing family of the two boundaries.
The second includes precisely the source interfaces that may not be discarded.

## 6. Sharp regressions and failed closing extensions

**Weak near-diameter threshold fails at extremality.** Take
x=(0,0), a=(0,1), b=(0,-1), y=(3,0). The set is unit-separated and
triangle-free, D^2=10, and |xy|^2=9=D^2-1, but x is not extreme.

**Weak near-diameter threshold fails at crossing.** In the rectangle
(0,0),(3,0),(3,1),(0,1), D^2=10 and the two horizontal sides have squared
length 9. They are disjoint and do not cross. All source pairs remain separated
by at least 1, and there is no unit triangle.

**Near-unit planarity cutoff is strict.** The unit square has two crossing
diagonals of length sqrt(2). Their closed diameter disks contain other source
points. This prevents changing the '<sqrt(2)' statements to '<=sqrt(2)'.

**Linear witness count does not close C-II.** A linear family of independent
near-unit pairs can be realized without an exact unit triangle. For any integer
r>=2, use the 2r points

\[
 (3j,0),\quad (3j,1+1/(10r)),\qquad 0\le j<r.
\]

Their diameter satisfies D<=3r, so 1/(10r)<1/(2D). There are r distinct
inactive near-unit pairs, they are disjoint planar Gabriel edges, and the contact
graph is empty. This is an exact geometric regression, **not** a global minimizer
or a source satisfying the saturated diameter hypothesis h=pi D-o(D).

Therefore the planar/cofacial conclusion alone cannot be silently converted into
positive stress, an exact triangle, or global optimality. The combined canonical
source constraints, not witness count alone, must supply the remaining argument.

## 7. Dependencies and scope audit

Theorems (1), (2), and Section 4 are standalone geometric candidates with complete
proofs above. The perimeter ceiling is also available in canonical
[Section 58](../targets/target-c/58-full-source-geometry-audit.md).

The application (4) uses canonical lexicographic normalization and positive
support from [C-I restoration](../targets/target-c/56-ci-restored-frontier.md),
and the **unpromoted**
[block-transposition theorem](target_c_open_cell_block_transposition_2026-10-01.md).
It is conditional on that theorem's actual cut/chart hypotheses; this report
does not promote the extraction chain.

The rooted specialization (5) additionally assumes h=pi D-o(D). This follows
conditionally from the unpromoted
[rooted defect stability](target_c_wrapping_root_defect_stability_2026-09-30.md):
q-k=pi D+o(D), k=d_H+s_Z=o(D), h=q-d_H. It does not follow from canonical ZR/ZF
alone, which only supplies h>=ceil(D).

Section 5 uses the unpromoted actual train cutset and local-immunity hypotheses.
Its phase inequalities are derived from the unit-rhombus metric, not from an
inactive pair being assigned a multiplier.

Regressions retained: stars and paths need not be impossible; no Euler-path
inference; no full-source affine-kernel claim; no source isolates dropped;
no infinitesimal move integrated; no leading-area statement converted to
boundary-order control; no assertion that a new near-unit edge is active.

## 8. Computation and exact remaining gap

Run `python3 research/verify_strict_near_diameter_capacity_2026_10_01.py`.
It checks rational threshold regressions and finite unit-separated subsets,
including all eligible four-point subsets of a half-integer 6-by-6 grid. It
checks extremality, pairwise crossing, the edge count, Gabriel disks, and
near-unit planarity using integer squared distances and orientation signs.
The report's universal geometric claims are proved analytically; this finite
check cannot certify any global minimizer or Level I conclusion.

The exact remaining obligation is to combine the genuine source KKT/core
conditions with the one-boundary swept-phase rhombus blockers and the non-rhombic
cofacial blockers, constructing a simultaneous finite release or forcing an
exact unit triangle. In addition, the existence of a linear disjoint small-amplitude
ONE-SIGN population remains a hypothesis here. Larger-amplitude TWO-SIGN,
exact-phase, split-star O-O, inactive-interface, macroscopic-container, and
higher-surplus full-core branches all survive. No canonical state is changed.
