> Generated reading edition · [exact source](../../../docs/reports/target_c_collinear_punctures_and_diameter_crossflow_2026-10-02.md) · source SHA-256 `09c38a1c302a6b2d571ba9252e8937730d117beb25ef8a35bf53cc1b9a338aca`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3FC66397D3CC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — source seam diameter budget and collinear crossflow

```text
collinear physical contact seam -> connected punctured mixed source graph
 -> actual diameter crossflow avoiding every seam vertex
 -> contradiction if a train/star extraction supplies a seam with no such flow.
The final extraction is not proved. Level I and C-II remain OPEN.
```

**Date:** 2026-10-02.
**Starting shared checkout:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.
**Isolated research base:** `0031d1d932d07ad657bf5efa34cfd16a3d249b02`.
**State version:** `2026-09-14.audit.51`.
**Branch:** `swarm/sol/diameter-stress-gap-20261002`.
**Mission:** extend source-vertex anchoring from two punctures to physical line seams,
then test the curved-seam repair. No coordination issue or assigned mission was
available. PRs #624–#627 were inspected to avoid duplicating their missions.
**Classification:** proved candidates awaiting independent audit and promotion;
artifact lifecycle **unreviewed**. Section 5 is a **regression**.
**Canonical dependencies:** Theory 01 Theorem 4.1 and the triangle-free penny
graph edge/diameter bound; C-I restoration; C-ZRF, §57 Sections 3–4;
C-FS-GEOM, §58 Sections 1 and 3. No unpromoted theorem is a premise.
**Related unpromoted work:** PR #624's finite core rigidity/two-puncture packet
motivated this attack. Its results are not needed below. The exact-phase gap,
paired-staircase, and four-host packets enter only the closing attempt.
**Active prompt:** [current C continuation](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md).
**Literature:** no import.
**Certificate:** [exact finite checks](../../../docs/research/migration/2026-10-16/shards/01/support/research/verify_target_c_collinear_punctures_2026_10_02.py).

## 1. Source hypotheses

Use the contact-minimal, then diameter-pair-minimal triangle-free global source,
with D≥9. Retain its entire configuration, including contact isolates. V denotes
only the nonisolated positive-contact core. Write P for its planar coordinate
matrix, C,H for its full actual core supports, and choose a relative-interior
normalized stress with every α_e,β_h positive. The canonical inputs are

$$
 \Omega=L_C(\alpha)-L_H(\beta)\succeq0,\quad
 \Omega P=0,\quad \Omega\mathbf1=0,\quad
 \ker\Omega=\operatorname{span}\{\mathbf1,P_x,P_y\},             \tag{1}
$$

and mixed rigidity rank 2|V|−3. P spans the plane and has distinct points.
These are assertions on V; no affine-kernel claim is made for contact isolates.

The matrix and separator theorems also apply to any finite framework satisfying
these same hypotheses, independently of global optimality. The finite regression
in Section 5 satisfies the matrix, actual-support and rigidity hypotheses, but
fails global minimality and the large-source geometry hypotheses.

## 2. Exact principal-kernel restriction

Put A=[1 P_x P_y]. For nonempty S⊆V, let T=V\S and A_S be the corresponding
row restriction. Then

$$
 \boxed{\operatorname{nullity}\Omega_{TT}=3-\operatorname{rank}A_S.} \tag{2}
$$

More precisely its kernel consists of restrictions to T of the affine scalar
functions vanishing on S.

**Proof.** Extend x∈R^T by zero on S, writing z. Then
xᵀΩ_TT x=zᵀΩz. For a PSD matrix this energy is zero exactly when z∈ker Ω.
Equation (1) identifies such z with A c satisfying A_S c=0. Restriction to T
is injective on this space: vanishing on T as well means A c=0, and A has rank
three. This proves both statements. ∎

Thus two distinct collinear pins, or any larger collinear set, leave exactly one
principal kernel mode: signed distance to their line. Three noncollinear pins
leave a positive definite grounded matrix. The latter fact does not require the
punctured graph to be connected.

## 3. Arbitrarily many collinear punctures

**Theorem CP.1.** If S contains at least two source vertices and all its source
points lie on one line L, the mixed graph G=(V,C∪H) after deleting S is connected.

**Proof.** Let y_i be signed distance from P_i to L. Every mixed component W of
G−S has a vertex off L. Otherwise all active edge vectors incident to any chosen
i∈W lie along L. Give i a nonzero normal velocity and fix every other vertex.
This preserves every mixed bar to first order. It fixes two distinct vertices
of S, so a Euclidean infinitesimal motion fixing those vertices is zero. The
velocity therefore contradicts the canonical mixed rigidity rank.

Since y=0 on S and Ωy=0, restriction gives Ω_WW y_W=0 on each mixed component;
its y_W is nonzero. Different components supply independent principal kernel
vectors, because Ω_TT is block diagonal on them. But (2) says its nullity is
one. There can consequently be only one component. ∎

This is an arbitrary-cardinality physical line-separator obstruction. It does
not bound the connectivity of a quotient formed by identifying source points.

**Corollary CP.2 (contact-component crossflow).** If C−S has r components,
at least r−1 distinct actual diameter edges, none incident to S, connect different
components. Their component quotient contains a spanning tree.

**Proof.** G−S is connected, so adding the surviving H edges connects those
r contact components. A connected quotient has a spanning tree. ∎

In particular, if every diameter between different contact components is
incident to a single hub lying in S, then r=1. This holds even when S is much
larger than two vertices. It is a condition on actual source endpoints.

### 3.1 An arbitrary physical seam pays diameter-incidence currency

Collinearity is unnecessary for the following bound. Let W be a nonempty
connected contact island. Let S=N_C(W)\W be its distinct actual contact
attachment vertices, s=|S|≥2. Thus K=C[W∪S] is connected. Write w=|W|,
e_SS=|C[S]|, and h_W for the number of distinct actual diameter bars with at
least one endpoint in W. An internal diameter is counted once; an external
diameter need not end in S. Let δ_K be the graph diameter of K.

**Theorem CP.4 (sharp local diameter-incidence budget).**

$$
 \boxed{\delta_K\le 2s+h_W-e_{SS}-3.}                   \tag{7}
$$

**Proof.** Restrict the full mixed rigidity rows to velocity columns of W.
They have rank 2w: a pinned flex extends by zero outside W to a mixed flex
of the full source. It fixes at least the two distinct vertices in S, so
the canonical ZF rank makes it zero. Only rows incident to W are nonzero.
Write e_W for the number of contact rows incident to W. The full positive
equilibrium stress restricts to a row dependence with a nonzero coefficient
on every one of these e_W+h_W rows. Hence

$$
 e_W+h_W\ge2w+1.
$$

The induced contact graph K has w+s vertices and e_W+e_SS edges. The
canonical triangle-free penny-graph diameter bound gives

$$
 e_W+e_{SS}\le2(w+s)-\delta_K-2.
$$

Eliminating e_W proves (7). ∎

The count uses actual full-source rows, including every diameter to a vertex
outside S. Omitting those rows invalidates (7). This is a localized ZF
currency, with the one-row surplus supplied by the full nonzero stress.

For b=2s+h_W−e_SS−3, Euclidean diameter of W∪S is at most b. The finite
Oler inequality, isodiametric area bound and perimeter bound therefore give

$$
 \boxed{w+s\le {\pi\over2\sqrt3}b^2+{\pi\over2}b+1.}     \tag{8}
$$

If h_W=0, this gives diameter at most 2s−e_SS−3, improving the older
3s−1 attachment-diameter estimate under the canonical ZF normalization.
In particular, a diameter-free positive-contact island attached to exactly
three source vertices has w≤10: b≤3, and the right side of (8) is strictly
less than 14. This does not bound contact-isolated populations.

### 3.2 Fixed-star support cannot carry a quadratic thin-interface island

Let Δ_D be the canonical §58 FS.5 maximum actual diameter degree, so
Δ_D=O(D^(3/4)). Suppose t source hubs cover every actual diameter incident
to W. Then h_W≤tΔ_D, even if a bar has both endpoints in the hub set.
Equations (7)–(8) show

$$
 s+t\Delta_D=o(D)\quad\Longrightarrow\quad w=o(D^2).     \tag{9}
$$

Thus a quadratic positive-contact island with finitely many such hubs needs
linearly many actual contact attachment vertices. More generally, if w≥cD²
for fixed c>0, then

$$
 \liminf {2s+t\Delta_D\over D}
 \ge\sqrt{{2\sqrt3\,c\over\pi}}.                       \tag{10}
$$

Indeed (8), divided by D², contradicts any smaller subsequential coefficient.
No multiplier floor or asymptotic conversion of o(D²) into o(D) is used.
This excludes the stated fixed-star thin-interface source-island subclass.
It does not say that a selected complete train rectangle has a thin physical
attachment interface; the extraction of that property remains a separate gap.

## 4. A signed and quantitative crossing law

Fix any line L and signed distances y. Let W⊂V be a nonempty proper source set
such that every contact crossing W has its exterior endpoint on L. Suppose both
W and V\W contain a point off L, and V\W contains two distinct points on L.
Put f_i=y_i for i∈W and f_i=0 otherwise.
Let Π project onto the affine scalar subspace in (1), and let λ_+>0 be the
least positive eigenvalue of Ω. The hypotheses imply |V|>3 and f is nonaffine.

**Theorem CP.3.** With δ_H(W) the actual diameters crossing the source cut,

$$
 \boxed{-\sum_{ij\in\delta_H(W)}\beta_{ij}y_i y_j
 =f^T\Omega f
 \ge\lambda_+\|(I-\Pi)f\|^2>0.}                         \tag{3}
$$

Consequently at least one crossing actual diameter has endpoints strictly on
opposite sides of L, neither on L. If X denotes all such crossing diameters,

$$
 \boxed{\sum_{h\in X}\beta_h
 \ge{4\lambda_+\over D^2}\|(I-\Pi)f\|^2>0.}             \tag{4}
$$

**Proof.** For signed edge weights ω=α on C and ω=−β on H, the scalar
equilibrium Ωy=0, multiplied by y_i and summed over i∈W, gives

$$
 0=\sum_{ij\in E[W]}\omega_{ij}(y_i-y_j)^2
   +\sum_{i\in W,j\notin W}\omega_{ij}y_i(y_i-y_j).
$$

Subtract this from the quadratic-form expansion for f to obtain the exact cut
identity fᵀΩf=Σ_cut ω_ij y_i y_j. Every crossing contact has y_j=0,
so only diameters remain, with the negative sign in (3).

The zero set of f contains two distinct outside points on L and an outside
point off L. Those three noncollinear points force any affine f to be zero;
its nonzero value in W contradicts that. Thus f is nonaffine, and the spectral
inequality proves (3).

Finally, for each opposite-side diameter, a=|y_i|,b=|y_j| obey a+b≤D. Thus
ab≤D²/4. Same-side terms are nonpositive contributions to the left of (3).
Discarding them and applying this bound proves (4). ∎

The convenient application is a contact component W of C−S with S⊂L, |S|≥2,
and an off-line source point in another component. This supplies all pins.

Equivalently, reflecting W across L changes the signed stress energy by
4fᵀΩf. All crossing contacts preserve their lengths when their exterior endpoint
is on L. If all crossing diameters also ended on L, all mixed lengths would
be preserved and the strictly positive energy would be impossible. Formula (3)
retains the actual Euclidean signs; CP.2 alone is only a graph count.

No lower bound uniform in D is asserted for λ_+. Equation (4) cannot be used
as a uniform diameter-multiplier floor.

## 5. Exact curved-separator regression, including full stress and rigidity

Replacing “collinear” by “cocircular” in CP.1 is false under the matrix/source
hypotheses. Here is an unbounded explicit family. This is a regression, not a
family of global minimizers.

For k≥2 let

$$
 a={\pi\over3k},\qquad D={1\over2\sin(a/2)}.
$$

Take three carriers B_0,B_1,B_2 forming an equilateral triangle of side D.
On the radius-D minor circular arc centered at B_i between the other two
carriers, take k−1 equally angular-spaced interior points. Together with the
three carriers, the source has N=3k points on the boundary of an equilateral
Reuleaux triangle. Its C consists exactly of the 3k consecutive arc chords;
its H consists of the three carrier edges and 3(k−1) carrier-to-own-arc bars.

### 5.1 All lower and upper source constraints

Consecutive arc chords are unit chords. Same-arc nonconsecutive chords are
strictly longer. For different arcs sharing one carrier, use the angular
parameters s,t∈[0,π/3] measured away from that common carrier. Their squared
distance is nondecreasing separately in s and t: in coordinates with the
common carrier 0 and the other carriers D(1,0),D(1/2,√3/2), differentiation
in s gives

$$
 {\partial\over\partial s}|x(s)-z(t)|^2
 =4D^2\sin(s+t/2)\sin((\pi/3-t)/2)\ge0.                 \tag{5}
$$

If both points are interior, s,t≥a, their distance is at least the distance
between the two neighbors of the common carrier:

$$
 2\sin(\pi/3-a/2)\ge\sqrt2>1.
$$

If one is the common carrier, only its immediately adjacent chord is unit.
Thus C is exactly a cycle of length 3k and is triangle-free. The Reuleaux
triangle has diameter D. At a smooth interior arc point the unique outer
normal of the full Reuleaux body is radial from its carrier. Any diameter
pair in that body exposes its endpoints in its own vector direction. The
unique smooth-body normal therefore makes the only diameter partner that carrier. This
proves the asserted complete actual H support, including every source point.

### 5.2 Positive equilibrium and maximal affine stress kernel

Assign α=1 to each contact and β=D⁻² to every diameter. At an interior arc
vertex, the two contact reactions sum to D⁻² times its outward diameter
vector. At a carrier, the two incident contact vectors sum in the radial
direction with magnitude 2cos(π/3−a/2). The diameter reaction has magnitude

$$
 D^{-1}\left[\sqrt3+
 {\sin((k-1)a/2)\over\sin(a/2)}\right]
 =2\sqrt3\sin(a/2)+2\sin(\pi/6-a/2)
 =2\cos(\pi/3-a/2).
$$

Hence all vertex equilibrium rows hold and every actual coefficient is
positive. Scaling by D²/(3k) normalizes Σ_H β=1 and Σ_C α=D².

Ground Ω on the three carriers. Its interior principal matrix has three
independent (k−1)-by-(k−1) tridiagonal blocks, with diagonal 2cos a and
off-diagonal −1. Their eigenvalues are

$$
 2\cos a-2\cos(j\pi/k)>0,\quad j=1,\ldots,k-1.          \tag{6}
$$

The grounded matrix is positive definite. Its carrier Schur complement
annihilates the three independent carrier restrictions of 1,P_x,P_y, by
equilibrium; hence that 3-by-3 Schur complement is zero. Therefore Ω is PSD
with exactly the three affine kernel modes.

The mixed graph is infinitesimally rigid. Its carrier triangle is rigid;
fix it and proceed along each circular arc. The next vertex has a fixed-radius
bar to the carrier and a unit bar to its already fixed predecessor. Their
vectors are nonparallel, so its velocity is zero. This pins every vertex and
proves mixed rank 2N−3.

Deleting the three cocircular carriers leaves three separate contact paths
and no surviving diameter edge. Thus G−S has three components despite full
actual positive support, PSD with affine kernel, and mixed rigidity. This
disproves the curved-separator extension of CP.1 under those hypotheses.

The same family makes CP.4 exact, for every k. Let W be the k−1 interior
vertices of one circular arc. Its two contact attachments are the arc endpoints,
e_SS=0, h_W=k−1 (all to its carrier), and K is a path of k unit edges. Hence
δ_K=k=2·2+(k−1)−3. Both the diameter incidence coefficient and the one-row
surplus in (7) are attained. These sources fail the canonical sublinear star
degree bound and therefore do not contradict (9).

### 5.3 Explicit nonglobality

For k=2, D²=2+√3. A regular unit-circumradius pentagon and its center give
six unit-separated points of diameter squared (5+√5)/2<2+√3.

For k=3,4,5,6, take respectively a 3×3,4×3,4×4,5×4 unit square grid and
delete surplus points. Their squared diameter bounds are 8,13,18,25, strictly
below (21k/22)²<D². Here sin x<x and π<22/7 give D>3k/π>21k/22.
For k≥7, a square grid of side ceil(√(3k)), restricted to 3k points, has
squared diameter strictly below 6k; meanwhile D²>(21k/22)²>6k. This proves
nonglobality for the entire unbounded family. The fixed 60-degree diameter
stars also violate canonical large-source star-angle collapse. There are no
contact isolates, discarded points, or alleged global-optimality certificates.

## 6. Exact-phase application and the failed repaired attack

CP.1–CP.3 exclude a physical contact seam with collinear attachment vertices
if all diameter flow between its resulting contact components is anchored on
that seam. This is stronger than a private gap-tree leaf argument: it concerns
all actual source diameter rows and arbitrarily many collinear attachment pins.
For a component with off-line points on both sides, CP.3 forces a cross-line
diameter away from every pin, with the exact weighted identity (3).

I attempted to obtain that seam from an exact-phase retained train and its
opposite complete shore. The required implication fails at co-embedding.
Parallel train contact vectors do not put all their source endpoints on one
line. Inverse-D phase width is not exact collinearity. Four host intervals
specify layer labels of actual diameter endpoints, rather than placing every
contact attachment on the same Euclidean seam. A spanning-tree basis does not
remove the opposed nonbasis supports. No source seam with the hypotheses of
CP.1 has been extracted from the general fixed-star branch.

The next repair was to allow a circular seam centered at the witness star.
Section 5 disproves the matrix/rigidity version of that repair, including full
actual contact and diameter support. Reflection across a line fixes its pins
and every bar to them; circular inversion has distance scale factors and
cannot replace that exact finite operation. Global optimality or actual
quadratic train population must enter any such repair.

The next attack retained curved pins but charged their exact diameter-row
incidence. This succeeds in (7): a few contact attachments cannot hide a large
diameter-free island, and finitely many canonical small stars cannot carry a
quadratic island behind a sublinear interface. The attempt to apply (9) to
the fixed-star O–O rectangle fails at the actual interface size. Each global
train cut contains many source contact edges; dense transverse crossings can
give a linear attachment population. The existing complete-rectangle theorem
does not supply s=o(D), nor a contact island W with those precise boundary
and hub-cover hypotheses. The Reuleaux exact equality also prevents removing
the h_W payment purely from rank/stress logic.

The precise next obligation is therefore: extract a genuine collinear source
attachment set S whose surviving contact components have all intercomponent
diameters incident to S, or extract a quadratic actual contact island with
s+tΔ_D=o(D). CP.2 or (9), respectively, supplies the exact contradiction.
Neither source extraction is claimed here; a general curved-seam replacement
has to pay the exact h_W regression rather than assume it away.

## 7. Certificate, adversarial checks, and lifecycle

The verifier uses exact SymPy arithmetic for the k=2 source: all 15 distances,
the complete C/H supports, triangle-freeness, positive equilibrium, a positive
grounded matrix with zero Schur complement, affine kernel, mixed rank, all 63
nonempty principal-kernel restrictions, collinear-puncture connectivity, the
curved-puncture disconnection, the local diameter-incidence budget on every
eligible finite contact island, its exact Reuleaux equality, and 186 cut-energy
identities. It checks rational
competitor margins for all k. It does not enumerate general frameworks or
certify general trigonometric passages; Sections 2–5 supply those proofs.

The CP.3 pin hypothesis was corrected during self-audit: two off-line points
alone do not establish nonaffinity of the truncated height field. Two distinct
fixed pins on L plus an outside off-line point do. All applications retain it.
Stars and paths in the gap quotient are not physical line separators. The
regular unit shell and the curved Reuleaux family are nonglobal local/stress
regressions, not Level I counterexamples. Every source isolate remains outside
the core matrix statement and in any eventual full-source competitor.

No canonical state, route map or prompt is changed. Promotion is not requested
without an independent audit. The remaining exact/nonconstant-phase, split-star
O–O, inactive-interface, macroscopic-container/exterior-cap and other full-core
branches remain open. The new result is a source-level physical separator test,
not full C-II or Level I closure.
