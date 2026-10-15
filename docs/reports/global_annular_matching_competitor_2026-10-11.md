<!-- theorem-state: {"artifact_id":"ART-654AA3F0DE12","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Global diameter comparison by matching in an annular conflict graph

- **Date:** 2026-10-11
- **Base:** origin/main `ab6dd3336f9f8d440f2bada76edb32153391cddc`
- **Research predecessor:** `8149b276bf21be6fdc81e43a834d79d3b85d07fc`
- **State version:** `2026-10-10.audit.234`
- **Target:** whole-problem / global strict-diameter competitors
- **Classification:** proved candidate awaiting promotion; finite regressions;
  registry lifecycle unreviewed
- **Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`
- **Computation:** `research/verify_global_annular_matching_2026_10_11.py`
- **New literature imports:** none; the optional lattice corollary uses the
  canonical uniform circle estimate explicitly identified below

## Level I status and implication chain

**STILL OPEN.** This is a source-independent global comparison method. It
constructs a complete replacement packing, not a motion of selected source
labels or a response network. It accounts for the full requested cardinality,
including any contact-isolated labels of a source being compared.

```text
near-bipartite long-pair conflict graph -> matching-controlled deletion ->
certified full packing of M points with diameter strictly below D ->
any global n-point minimizer of diameter D has n >= M+1
```

The extra closing step would prove that every sufficiently large triangle-free
global source admits such a comparison packing with M >= n. It is not proved
here. The new bound is a global benchmark for that obligation, not a change
to the conjecture's quantifiers.

## 1. The exact finite competitor quantity

Let X be a finite unit-separated set in a disk B(o,S), where

\[
S=D/2+\delta<D/\sqrt2,\qquad \delta>0.
\]

Put an edge xy in G_D(X) precisely when |x-y| >= D. In particular distance-D
ties are edges. Write N=|X|, tau(G) for minimum vertex-cover cardinality,
and nu(G) for maximum matching cardinality. Then the maximum cardinality
of a strict-sub-D subset of this particular X is exactly

\[
\boxed{M_D(X)=N-\tau(G_D(X)).}
\]

Indeed, a deletion set leaves diameter strictly below D if and only if it
covers every conflict edge. Unit separation survives deletion. This is an
optimization within a specified comparison packet; no optimality over all
planar packings is asserted.

G is a comparison-packet conflict graph, not necessarily the actual diameter
graph of X: X may have pairs longer than D. The canonical Woodall topology
for actual maximal-distance pairs cannot be imported for G.

## 2. A small angular cut makes the graph bipartite

### Proposition 1

Let V_ann be the source labels in the radial band

\[
D-S\le |x-o|\le S,
\qquad N_{\rm ann}=|V_{\rm ann}|,
\]

and put alpha=2 arccos(D/(2S)). There is a subset Z of V_ann with

\[
|Z|\le r:=\left\lfloor\frac{\alpha}{\pi}N_{\rm ann}\right\rfloor
\]

such that G_D(X)-Z is bipartite. Consequently

\[
\boxed{\nu(G)\le\tau(G)\le\nu(G)+r,}
\qquad
N-\nu(G)-r\le M_D(X)\le N-\nu(G).
\]

### Proof

Translate o to zero. Every conflict endpoint lies in V_ann: otherwise its
radius plus S would be strictly below D. If phi in [0,pi] is the angle
between two conflict endpoints, phi is obtuse, since an acute or right
angle gives squared distance at most 2S^2<D^2. In the obtuse range the
squared distance is increasing in both radii. Therefore

\[
D^2\le |x-y|^2\le4S^2\sin^2(\phi/2),
\quad\text{so}\quad \phi\ge\pi-\alpha.
\]

Choose an oriented ray u and use its full line to divide the plane into
two open half-planes. Take a generic u so no source label is on the line.
Two conflict endpoints in the same half-plane must lie within angle alpha
of its opposite boundary rays. One of them is within alpha of the positive
ray u. Delete all V_ann labels within that one angular wedge, of width
2alpha. All remaining conflict edges join opposite half-planes.

For a uniformly rotating ray, each V_ann label belongs to the wedge for
fraction alpha/pi of the rotations. Averaging gives a generic ray whose
integer deletion count is at most floor(alpha N_ann/pi). This proves
the asserted bipartite deletion.

Any vertex cover must hit the vertex-disjoint edges of a maximum matching,
so tau(G)>=nu(G). For the bipartite graph H=G-Z, a maximum matching has
a vertex cover of the same size. Thus deleting Z followed by that cover
gives tau(G)<=|Z|+nu(H)<=r+nu(G).

For completeness, the bipartite cover assertion follows by starting at
unmatched left vertices and following alternating unmatched/matched edges.
With Z_L,Z_R the reachable left/right sets, (L minus Z_L) union Z_R
covers every edge. A maximum matching leaves no reachable unmatched
right vertex. Each matching edge contributes exactly one endpoint to
this cover, and every covered vertex is matched. Its cardinality is
therefore the matching cardinality. This supplies the finite matching
argument without a literature premise. QED.

### Odd-cycle check

Every odd cycle of G has at least ceil(pi/alpha) edges. Write each directed
edge's angular increment modulo 2pi as pi+epsilon_i, with
|epsilon_i|<=alpha. Along an odd cycle the epsilon sum is an odd multiple
of pi, so its absolute value is at least pi. This confirms that short
odd-cycle counterexamples cannot occur in the small-delta regime; it is
not itself the proof of a bounded deletion set.

The factor in the angular bound is sharp for the general point-set statement.
For a regular unit q-gon with q odd, write its circumradius as R and its
diameter as D=2R cos(pi/(2q)); take S=R. Its conflict graph at threshold D
is a q-cycle, alpha=pi/q, and N_ann=q. Thus the bound gives r=1, and a
deletion of zero vertices would leave an odd cycle. Also tau-nu=1 and the
odd-cycle-length bound is attained. These are geometric regressions; the
regular q-gon is not asserted globally optimal for large q.

## 3. Quantitative scope: all unit-separated clouds and lattice packets

If D-S>1/2, disjoint radius-1/2 disks about V_ann fit in the expanded
annulus from radius D-S-1/2 to S+1/2. Comparing their areas gives

\[
N_{\rm ann}\le4D(1+2\delta).
\]

The elementary inequality 1-cos x >= 2x^2/pi^2 on [0,pi/2] yields

\[
\alpha\le2\pi\sqrt{\frac{\delta}{D+2\delta}}.
\]

For delta=c D^(-1/3), with c fixed, Proposition 1 therefore gives the
following explicit bound for arbitrary unit-separated X in the stated disk:

\[
\boxed{r\le\left\lfloor8\sqrt c\,D^{1/3}+16c^{3/2}\right\rfloor.}
\]

For a translated unit triangular-lattice disk packet the bound improves
to r=O_c(1). The precise additional input is the uniform-over-translations
circle estimate explicitly used in canonical
`C-TRIANGULAR-LATTICE-STRICT-D-COMPETITOR-RESERVE`, in
`docs/audits/target_c_triangle_free_lattice_competitor_reserve_independent_audit_2026-10-10.md`:
the count in B_r is pi r^2/a0+O(r^(2/3)), a0=sqrt(3)/2. Subtract the
inner open-disk count from the outer closed-disk count. The main term in
the band is (2pi/a0)D delta and both discrepancies are O(D^(2/3)), so
N_ann=O_c(D^(2/3)). Together with alpha=O_c(D^(-2/3)), this gives a
bounded r. Distance ties at the inner radius are included using the
left-limit disk count. No translation-uniform improvement to Huxley's
smaller exponent is assumed.

### The lattice hypothesis cannot be dropped

The O(D^(1/3)) matching-cover error for general unit-separated clouds is
optimal in order. For q=k^3 with k odd and k>=3, take a regular unit
q-gon of radius S=1/(2 sin(pi/q)), set l=k, and use the threshold

\[
D=2S\cos(\pi l/q),\qquad \alpha=2\pi l/q.
\]

This obeys S<D/sqrt(2) and delta=S-D/2=Theta(D^(-1/3)). More precisely,
delta D^(1/3) tends to pi^(2/3)/4. At this threshold the conflict graph
has maximum matching (q-1)/2 and maximum independent-set cardinality

\[
\frac{q+1}{2}-l.
\]

Consequently tau-nu=l=k=Theta(D^(1/3)). To prove the independent-set
bound, put h=2pi/q and thicken each selected circular point to an arc of
length h. These arcs have disjoint interiors; their union B has length
M h for M selected labels. Independence says that any two selected
centers differ from antipodal directions by strictly more than l h.
Hence B and the (l-1)h-neighborhood of B+pi are disjoint. If B is nonempty,
this neighborhood is not the whole circle and its length is at least
|B|+2(l-1)h: at least one complementary gap survives enlargement, and
that gap alone loses 2(l-1)h. Thus

\[
2Mh+2(l-1)h\le2\pi,
\quad M\le q/2-l+1,
\quad M\le(q+1)/2-l.
\]

Consecutive (q+1)/2-l labels attain the bound. The actual diameter cycle
of the odd polygon supplies a matching of (q-1)/2 edges, which is already
maximum by cardinality. This proves the exact claimed gap without a
numerical optimization premise.

The same obstruction holds with any prescribed fixed c>0 and exactly
delta=c D^(-1/3). Take instead l=floor(beta k), with
0<beta<2sqrt(c)/pi^(1/3). For the unit polygon, its original values
delta_0,D_0 satisfy delta_0 D_0^(1/3) -> pi^(2/3)beta^2/4<c. Dilate the
entire polygon and threshold by

\[
t_k=\left(\frac{c}{\delta_0D_0^{1/3}}\right)^{3/4}\ge1
\]

for sufficiently large k. Unit separation is preserved, the conflict
graph is unchanged, and the rescaled values obey delta D^(1/3)=c
exactly. The matching-cover gap is still l=Theta(D^(1/3)). Thus the
bounded lattice error is not a theorem for arbitrary unit-separated
point sets even at a fixed c.

For large k, one may also add a spacing-(1+1/q) triangular lattice in the
open radius-(S-1) disk. Every added point is strictly separated from the
polygon and every added-added distance exceeds one. The added points are
therefore contact-isolated; the entire source is triangle-free. Since
delta<1/2 eventually, all added-involving distances are less than
2S-1<D, so the conflict graph gains only isolated vertices. The full
source now has leading population pi D^2/(2sqrt(3))+o(D^2), while its
matching-cover gap remains Theta(D^(1/3)). Thus triangle-freeness and
leading density do not replace the lattice hypothesis. These are not
asserted global minimizers; D here is a conflict threshold below their
actual diameter.

With a supplied cut Z of size r, M_D(X) is exactly computable by considering
every independent retained subset T of Z. Delete Z minus T and every
outside neighbor of T, then solve the remaining bipartite graph by matching.
Every independent set has one such intersection T with Z. The smallest
deletion count over these 2^r cases is consequently the exact optimum for
the packet. The verifier also checks each matching against its equal-sized
cover; optimality is not inferred merely from solver status.

## 4. Exact loss of edge-count currency at the natural scale

**Classification:** regression. For each integer k>=2 put m=k^3 and take
the triangular-lattice points with physical coordinates

\[
X_k=\{(j,\pm\sqrt3 m):-k\le j\le k\}.
\]

Use D=2sqrt(3)m and S=sqrt(3)(m+1/(6k)). They obey S<D/sqrt(2), are
unit-separated, and lie strictly inside B_S. Same-row distances are
less than D; every cross-row distance is at least D. Thus G_D(X_k)
is exactly K_(2k+1,2k+1), with

\[
E=(2k+1)^2,\qquad \tau=\nu=2k+1.
\]

Here delta=(1/12)^(1/3) D^(-1/3). The edge-count deletion allowance loses
E-tau=4k^2+2k=Theta(D^(2/3)), while actual required deletion is only
Theta(D^(1/3)). This is the entire order of the canonical population reserve,
not a bounded arithmetic correction. The example proves neither a larger
universal reserve coefficient nor optimality of these sparse two rows.

The saving applies inside the full lattice disk of this S as well: it
contains X_k as an induced complete bipartite conflict graph. Delete one
row of 2k+1 labels first, covering at least (2k+1)^2 conflict edges. Cover
each remaining edge by one endpoint. For the entire disk packet the
deletion allowance is therefore at most E_full-4k^2-2k. Hence the
D^(2/3)-order improvement over edge-count currency occurs in full
comparison packets for an unbounded sequence of D, not only in the
sparse two-row examples. It still does not establish a better universal
asymptotic reserve constant. The verifier checks full disks at k=2,3,4.

| k | D squared | Full input N | Conflicts E | Exact deletions | Retained M | Saving over edge allowance |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 768 | 721 | 78 | 18 | 703 | 60 |
| 3 | 8748 | 7963 | 153 | 27 | 7936 | 126 |
| 4 | 49152 | 44617 | 267 | 39 | 44578 | 228 |

The last row's retained squared diameter is exactly 49141, certifying
D(44578)<=sqrt(49141). Its cardinality is not asserted maximal among
all unit-separated planar sets at that diameter.

## 5. Certified full comparison packets and triangle-free deformation

The verifier enumerates all triangular-lattice sites in the open disk of
radius S=D/2+1/(4k), for D=8k^3 and 16 rational center offsets (a,b).
Equivalently, these are disks centered at the origin with the lattice
translated by -a u-b v in its unit basis u,v.
It checks every pair of potential conflict endpoints, including exact
distance-D ties. A point outside the radial band has distance less than D
from every other point by its radial bound. Thus no inactive upper pair
is omitted. Exact convex-hull distances independently give the final diameter.

The strongest packets found in this finite suite are:

| D | Center offset (a,b) | Input N | Conflicts E | Exact deletions tau | Retained M | Diameter squared |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 8 | (1/4,1/4) | 67 | 8 | 4 | 63 | 63 |
| 64 | (0,1/4) | 3738 | 25 | 5 | 3733 | 4093 |
| 216 | (1/4,1/4) | 42391 | 111 | 47 | 42344 | 46641 |

In particular these certify D(63)<=sqrt(63), D(3733)<=sqrt(4093), and
D(42344)<=sqrt(46641). These are upper bounds, not exact values of D(n).

For an exact triangle-free variant, let q_max<D^2 be the packet's squared
diameter and B the product of its two index-coordinate spans. Put

\[
\rho=\min\{1/4,(D^2-q_{\max})/[4(B+1)]\},\qquad a=1/2-\rho.
\]

Replace the triangular basis by two unit vectors with dot product a.
For an integer index difference (m,n), the new squared length is

\[
m^2+n^2+2amn=(m^2+n^2+mn)-2\rho mn.
\]

If mn>0 it is at least m^2+n^2>1. If mn<0 it strictly exceeds the old
positive integral squared norm, so is greater than one. If mn=0 it is
one exactly for the four coordinate-axis unit differences. Hence the
infinite deformed lattice is unit-separated, and the actual contact graph
of every subset is bipartite by index parity. No other source contact is
silently discarded. Every retained squared distance is at most
q_max+2rho B<D^2. This proves a finite triangle-free full competitor with
the same M labels and an explicit rational metric certificate.

For the three rows above the exact deformed squared diameters are,
respectively, 5193/82, 10910854/2665, and 1446076701/31001. All are
strictly below the corresponding D^2. In each listed case this value is
strictly greater than the undeformed packet's squared diameter. The
undeformed same-cardinality unit-separated packet is therefore an exact
strict competitor: all three listed triangle-free variants are certified
nonglobal. They are comparison packets, not counterexamples to Level I.

## 6. Frontier effect and exact remaining bridge

For any global n-point minimizer A of diameter D, the new competitor
quantity imposes the exact full-cardinality inequality

\[
n-1\ge M_D(X),\qquad
g_A:=n-1-\frac{\pi D^2}{2\sqrt3}
\ge M_D(X)-\frac{\pi D^2}{2\sqrt3}.
\]

This can improve finite comparison bounds relative to N-E by an entire
D^(2/3) order. No universal improvement of Audit.243's asymptotic constant
is claimed: that would require a new bound on the translation-averaged
matching cost, not merely the edge count or the two-column regression.

A Level I closure through this route still requires a source-specific
upper population/payment theorem showing M_D(X)>=n for every sufficiently
large triangle-free global source, with an actual admissible comparison
packet X. Neither a density ceiling valid for all triangle-free feasible
sets nor asymptotic closeness to a triangular lattice supplies that premise.
The previously proved equal-infimum obstruction remains binding.

## 7. Validation, classification, and promotion limit

Run `python3 research/verify_global_annular_matching_2026_10_11.py`.
The 48 finite packet cases use integer metric predicates and Fraction for
the explicit deformed metrics. Four complete-bipartite cases test shared
conflicts at unbounded-family parameter values. Three full lattice disks
also check the induced shared-conflict saving. Circular index graphs at
q=27,125,343 check the attained cover and maximum matching for the
sharpness family; their cover lower bound uses the circle-measure proof
above. An additional exact
five-cycle conflict packet has a one-label cut and exercises both exhaustive
branches; brute-force vertex-cover enumeration independently confirms its
deletion count. Its points are the lattice labels (0,0),(2,0),(2,2),(0,3),
(-1,2), centered at (3/4,5/4), with S=7/4 and D^2=7.

The general cut theorem is proved above, not established by these finite
checks. The finite exhaustive checker permits at most 12 cut labels;
this is a finite-suite limit, not a claimed universal asymptotic constant.
The uniform lattice-count estimate is the identified canonical
input. The script does not prove that estimate, unrestricted packing
optimality, a new universal asymptotic coefficient, or Level I.

The 2026-10-15 substantive audit added an optimized-Python refusal and exact
JSON matching/cover and complete cut-branch proofs. Use
`--certificate-json PATH` to save the 48 disk-packet, three full-column and
one odd-cycle graph proofs. The replay helpers check the duals and every
retained-cut branch without matching or cut search. These are proofs for the
emitted conflict graphs; the finite constructors separately verify the
metric conflicts, full input population and retained hull diameters.
An independent direct cover enumeration checks all 1,024 five-label graphs,
and four corrupted proof controls are rejected. The original aggregate JSON
results remain unchanged. See the
[exact-head audit](../audits/pr955_autonomous_proof_audit_2026-10-15.md).

**Promotion recommendation:** unreviewed. Preserve and independently audit
the cut/matching theorem and exact packets before admitting them to the
canonical ledger. No theorem state, active endpoint, or Level I status is
promoted by this report.
