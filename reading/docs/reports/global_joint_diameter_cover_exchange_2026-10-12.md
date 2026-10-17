> Generated reading edition · [exact source](../../../docs/reports/global_joint_diameter_cover_exchange_2026-10-12.md) · source SHA-256 `b804a22586186c7162cbff4f028b0b2ec3185e0353f9eb47dcd7d77e57a7e8cd`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-A339F24C029F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Global joint diameter-cover exchange

**Classification:** proved candidate awaiting promotion; unreviewed, noncanonical.
**Level I:** open. The supplied-packet criterion below is proved; the universal
existence of a successful packet for large triangle-free minimizers is not proved.

## 1. State and endpoint

- Base commit: `ab6dd3336f9f8d440f2bada76edb32153391cddc`.
- State version: `2026-10-10.audit.234`.
- Route: whole-problem simultaneous source replacement, independent of A/B/C
  stress, phase, wall, or lattice hypotheses.
- Canonical dependency: `docs/problem/statement.md`, the definition of D(n) and
  its every-global-minimizer quantifier. The finite graph identities used below
  are proved here.
- Endpoint: construct at least n unit-separated points of diameter strictly
  below the diameter D of the complete n-label source.

The new implication chain is

`joint cover/matching cost <= comparison population`

`-> simultaneous mixed packet of at least n labels`

`-> strict-D competitor -> contradiction to global optimality`.

This is an exact finite equivalence for a supplied comparison packet. It does
not assume that independently feasible exchanges can be combined.

## 2. Exact full-source theorem

Let A=(a_1,...,a_n) be any finite unit-separated planar source of diameter D>0.
Let B=(b_1,...,b_m) be any finite unit-separated comparison packet with
diam(B)<D. Labels in the two families are distinct even if their coordinates
coincide.

Define the actual diameter graph H on the A labels by

    ij in H  iff  |a_i-a_j|=D.

Define the bipartite cross-conflict graph G between A and B by

    (i,j) in G  iff  |a_i-b_j|<1 or |a_i-b_j|>=D.

The second condition includes equality: the target diameter is strictly below
D. For a vertex cover T of H, let nu_T be the maximum matching size in the
bipartite graph G restricted to (A\T) union B. Put

    K(A,B) = min_{T covers H} (|T| + nu_T).

**Theorem.** The largest cardinality of a unit-separated, strict-D subset of
the labeled union A union B is exactly

    n + m - K(A,B).

In particular, this union supplies a strict-D competitor of source cardinality
if and only if there is a diameter vertex cover T with

    m - |T| - nu_T >= 0.                         (E)

If A is globally diameter minimizing, then for every such B and every cover T,

    |T| + nu_T >= m+1,                          (G)

equivalently nu_T >= m-|T|+1. All source isolates participate in G and in nu_T;
none are discarded.

### Proof of the finite matching identity

For completeness, a finite bipartite graph with parts L,R has minimum vertex
cover size equal to maximum matching size nu. A cover must meet every edge of
a matching and therefore has size at least nu.

Choose a maximum matching M. Starting at unmatched L vertices, traverse
unmatched edges from L to R and matched edges from R to L. Write Z_L,Z_R for
the reached vertices. No unmatched R vertex is reached: a shortest alternating
path to one would augment M. Every reached R vertex is matched to a reached
L vertex, and every reached matched L vertex is matched to a reached R vertex.
Thus

    (L\Z_L) union Z_R

has exactly nu vertices. It covers every edge. Indeed, an uncovered edge would
join l in Z_L to r outside Z_R. If the edge is unmatched, the traversal reaches
r. If it is matched, a reached matched l was reached through precisely that
matched edge, so r was already reached. Both cases contradict r outside Z_R.
This proves the identity and constructs the cover.

### Proof of the geometric theorem

Fix a cover T of H and forbid using its source labels. Within A\T, all distances
are at least 1 and strictly below D. Within B they have the same property by
hypothesis. A mixed subset is feasible precisely when it is an independent
set of the remaining bipartite cross-conflict graph. The complement of an
independent set is a vertex cover, so the maximum feasible cardinality for this
fixed T is

    n-|T|+m-nu_T.

Every term is attained by the matching-cover construction above. Conversely,
for any feasible subset of A union B, its omitted source labels form a cover
of H. Thus optimizing over covers T gives exactly the displayed formula.

If (E) holds, select any n labels of the resulting feasible subset. No two
selected labels have coincident coordinates, because coincidence is a lower
cross conflict. Their coordinates are a unit-separated n-point set of diameter
strictly below D. Global optimality forbids (E); integrality gives (G). QED.

### Useful equivalent Hall form

For a fixed T, the bipartite matching identity also gives

    m-nu_T = max_{S subset B} (|S|-|N_{A\T}(S)|).

Here the empty S is allowed. To check this identity directly, a matching can
match at most |N(S)| of S, giving one inequality. For the minimum cover
constructed above, take S=Z_L when L=B; its neighbors are exactly Z_R, and
|Z_L|-|Z_R| equals the number of unmatched B vertices.

Consequently (E) is precisely the existence of one *simultaneously compatible*
comparison subpacket S whose gain over its remaining source blockers pays
the forced diameter deletion |T|.

### Why only inclusion-minimal covers need be searched

If T subset T' are covers, deleting k=|T'\T| additional source vertices lowers
maximum matching size by at most k. Therefore

    |T'|+nu_T' >= |T|+nu_T.

Every cover contains an inclusion-minimal cover. An inclusion-minimal cover
contains no H-isolated source label. This observation reduces the forced
cover search; it does not remove any isolate from the matching calculation
or from the constructed packet. Minimum-*cardinality* covers alone are not
sufficient, as the next regression shows.

## 3. Exact geometric regressions

Every coordinate below is rational, and the verifier checks all pairs.

### 3.1 A nonminimum diameter cover can be essential

Take

    A = {(0,0), (-1/2,1), (1/2,1)},   D^2=5/4,
    B = {(-1/2,9/10), (1/2,9/10)}.

The source contact graph has just the edge between the two upper labels.
The bottom label is contact isolated. The actual diameter graph is the
two-edge star centered at (0,0).

Its unique minimum-cardinality cover removes the bottom label. Both comparison
labels have lower conflicts with their corresponding retained upper labels,
so nu_T=2 and m-|T|-nu_T=-1: that cover yields no competitor.

The other inclusion-minimal cover removes both upper labels. The retained
bottom label has squared distance 53/50 from each comparison label, which is
in [1,5/4). Hence nu_T=0 and m-|T|-nu_T=0. The mixed three-point competitor
has diameter squared 53/50<5/4. This source is explicitly nonglobal.

**Regression:** optimizing the minimum diameter-cover cardinality before
considering lower blockers is invalid, even with an actual star diameter
graph, a one-contact triangle-free source, and a lower-conflict graph that
is a matching.

### 3.2 A smaller comparison packet can augment the source

Take

    A = {(0,0),(2,0),(0,1),(2,1)},   D^2=5,
    B = {(1/2,0),(3/2,0),(1,1)}.

Delete the two bottom source labels. They cover both actual diameter pairs.
No comparison label conflicts with either retained top source label, so
nu_T=0. Although m=3<n=4, their union gives five unit-separated labels
of diameter squared 4<5. This is a certified simultaneous replacement,
including the inactive source and cross pairs. The source is nonglobal.

### 3.3 A known global source rejects the supplied packet

For the unit square A and

    B = {(0,1/10),(1,1/10),(1/2,11/10)},

the exact formula and exhaustive enumeration both give maximum mixed
cardinality 3, hence max_T(m-|T|-nu_T)=-1. The supplied packet cannot improve
the four-label source. This is a check on the strict inequality and integer
threshold, not a general packet-existence theorem.

### 3.4 Upper cross conflicts cannot be omitted

Translate the preceding B ten units to the right. It still has minimum
separation at least 1 and diameter squared 5/4<2. All twelve source/comparison
cross pairs have distance at least D, so G contains K_(4,3). The true maximum
mixed cardinality is 3. Keeping only lower conflicts incorrectly predicts
five labels after deleting a two-label source diameter cover.

**Regression:** the full cross-conflict graph is not generally planar and
cannot be replaced by the local unit-blocker graph.

## 4. Lower-conflict geometry

The graph with only the edges |a_i-b_j|<1 has a planar straight-line drawing,
up to the harmless separation of coincident source/comparison pairs.

Suppose two edges a-b and a'-b' meet in their relative interiors at x. Unit
separation within each family and the triangle inequality give

    1 <= |a-a'| <= |a-x|+|x-a'|,
    1 <= |b-b'| <= |b-x|+|x-b'|.

Adding them gives 2<=|a-b|+|a'-b'|<2, a contradiction. No edge interior can
contain another vertex: its same-family endpoint would then be less than
1 from that vertex. A coincident cross-family pair has no other lower-conflict
neighbor, by separation in the two families, and is an isolated edge.

Every lower-conflict vertex has degree at most five. Otherwise six opposite
family points in its open unit disk have a consecutive angular gap at most
pi/3. For radii r,s<1 their squared distance is at most r^2+s^2-r*s<1:
the last inequality follows by maximizing this separately convex expression
on the closed unit square, whose maximum is 1, and checking strictness when
r,s<1. A coincident opposite-family point excludes all other neighbors.
This contradicts their unit separation.

These properties apply to the full conflict graph only under an additional
strict upper-clearance condition, such as B being contained in every open
radius-D ball centered at a source point. That condition is not automatic.

## 5. Unbounded dense regression against minimum-cover-first search

The three-label obstruction is not a small-population phenomenon. The following
family has the triangular leading population coefficient, retains every
contact-isolated label, has exactly one unit contact, and has a full cross
graph that is merely a matching. It is explicitly nonglobal.

**Regression theorem.** For every integer k>=4 there are rational-coordinate
triangle-free sources A_k and packets B_k with D=k^2 and

    |A_k| = pi*D^2/(2*sqrt(3)) + O(D),
    |B_k| = |A_k|-1,

such that the unique minimum-cardinality diameter cover has exchange profit
-1, but an inclusion-minimal k-label diameter cover has profit 0 and produces
a same-cardinality competitor of diameter exactly D-1/8. The source has
exactly |A_k|-2 contact-isolated labels. The comparison cross graph, including
both upper and lower conflicts, is exactly a matching of size |B_k|.

### Complete construction

Put R=k^2, c=(R/2,0), r=R/2-4, and, for j=0,...,k-1, put t_j=j/R and

    p_j = R * ((1-t_j^2)/(1+t_j^2), 2*t_j/(1+t_j^2)).

These rational points have norm R. For the interior define

    lambda = 1+1/R^2,
    h = (floor(sqrt(3*R^4))+1)/(2*R^2),
    L = {c + lambda*(i+j/2, h*j): i,j integers},
    z_- = c+(0,-1/2),   z_+ = c+(0,1/2).

Take I to consist of z_-,z_+ and every lattice point in the closed radius-r
disk about c whose distance from each z_-,z_+ is strictly greater than 1.
Finally set

    A_k = {0} union {p_j: 0<=j<k} union I,
    s = 1-1/(8R),
    B_k = {s*p_j: 0<=j<k} union a labeled copy of I.

All formulas and disk tests have rational coordinates or rational squared
distances; the floor is an integer square-root computation. No numerical
optimality assumption is involved.

### Separation and the complete diameter graph

Since h>=sqrt(3)/2, a nonzero lattice difference has squared norm at least

    lambda^2*(i^2+i*j+j^2) >= lambda^2 > 1.

The inserted pair z_-,z_+ is at distance exactly 1. Its distances to all
retained lattice labels exceed 1 by construction. Thus I has exactly one
unit contact.

Since t_j<1/k, the circle chord formula gives, for j!=l,

    |p_j-p_l| = 2*|j-l|/sqrt((1+t_j^2)*(1+t_l^2)),
    32/17 <= |p_j-p_l| <= 2*(k-1) < R.

The bound 32/17 uses k>=4. Also

    R-p_(j,x) = 2*R*t_j^2/(1+t_j^2) <= 2,
    R/2 <= |p_j-c| <= R/2+2.

Consequently every leaf/interior distance belongs to [4,R-2]. Every
origin/interior distance belongs to [4,R-4], and every interior/interior
distance is at most R-8. These estimates verify every source pair type.
The only pairs at distance R are 0-p_j, so H is exactly the k-leaf star.
The only unit contact is z_--z_+; in particular the origin, every diameter
endpoint, and all other interior labels are contact isolated.

### Complete comparison and mixed-packet pair ledger

Each leaf moves a distance exactly 1/8. Its separation from interior labels
is therefore at least 31/8; its distances from noncorresponding old leaves
are at least 32/17-1/8>1. Distances between new leaves are at least
s*(32/17)>1. All upper cross conflicts are absent:

- old/new leaf distances are at most 2*(k-1)+1/8<R;
- old leaf/interior distances are at most R-2;
- new leaf/interior distances are at most R-15/8;
- origin/new leaf distances are exactly R-1/8;
- the other types have the earlier upper bounds R-4 and R-8.

Thus G has exactly the edges between each old leaf and its new copy, and
between each interior label and its coincident copy. All other cross
distances are in [1,R). In particular G is a matching, not just a planar
bounded-degree graph.

The packet {0} union B_k has |A_k| labels, minimum distance 1, and diameter
exactly R-1/8. The last equality follows because the origin/new leaf pairs
attain R-1/8 and every other pair type is strictly shorter. This directly
certifies nonglobality; these sources are not proposed counterexamples to
Erdős #99.

### The joint objective

The unique minimum-cardinality cover is T={0}. Every B label matches its
corresponding retained source label, so nu_T=m and the profit is -1.

The other inclusion-minimal cover consists of all k leaves. The origin has
no cross-conflict neighbor. Precisely the |I| old interior labels can be
matched, giving nu_T=|I|. Hence

    m-|T|-nu_T = (k+|I|)-k-|I| = 0.

These are the only two inclusion-minimal star covers. The monotonicity lemma
shows that all supersets have no better profit. Therefore the full union's
maximum feasible cardinality is exactly |A_k|, while the minimum-cover-first
search misses its genuine strict-D competitor.

### Population asymptotic

The fundamental parallelograms of L have area lambda^2*h and uniformly
bounded diameter, at most 3. Their tiling gives lower and upper disk counts
between pi*(r-3)^2/(lambda^2*h) and pi*(r+3)^2/(lambda^2*h), for r>=3.
Thus the disk population is pi*r^2/(lambda^2*h)+O(r).

At most 18 lattice labels are removed near the inserted pair: the disjoint
radius-1/2 disks about labels within distance 1 of either inserted point
fit in the union of two radius-3/2 disks, whose total area bounds the count
by 18. Since lambda^2*h=sqrt(3)/2+O(R^-2), the retained interior count is

    |I| = pi*(R/2-4)^2/(sqrt(3)/2)+O(R).

Adding k+1 labels gives the claimed triangular leading coefficient. The
O(D) error is retained; no exact optimum or improved population reserve is
claimed.

### Exact finite verification

`python3 research/verify_global_exchange_star_family_2026_10_12.py` checks
all source, comparison, improved-packet, and cross pairs using rational
arithmetic. At k=4 it checks the 57-label source, including its 55 contact
isolates, and a strict competitor of diameter 127/8<16. At k=5 it checks the
256-label source, including its 254 contact isolates, and diameter
199/8<25. The all-k statement and count asymptotic rest on the proof above,
not on extrapolation from those fixtures.

## 6. Exact global frontier

The theorem is valid for arbitrary feasible sources, every actual diameter
pair, all source labels, arbitrary comparison populations, and arbitrary
simultaneous replacement sizes. It does not use contact-minimality, select a
positive-stress core, or assume a shared source/scaffold coordinate chart.

It does not prove that a large triangle-free minimizer has a successful packet.
The precise global theorem still needed is:

> There is n_0 such that every triangle-free globally diameter-minimizing
> unit-separated n-point source A with n>=n_0 admits a finite unit-separated
> packet B of diameter strictly below D and an actual diameter vertex cover
> T satisfying nu_T<=|B|-|T|.

This would close Level I directly by the proved theorem. At present it is
conditional, and no canonical frontier changes.

## 7. Verification and promotion recommendation

`python3 research/verify_global_joint_exchange_2026_10_12.py` uses rational
squared distances, complete pair ledgers, finite maximum matchings, and an
independent exhaustive search of all mixed subsets for the small fixtures.
The geometric theorem is proved above; finite verification does not prove
the universal packet-existence statement or global optimality of a numerical
packing.

No external mathematical theorem is imported. Literature reconnaissance on
jammed disk packings supplies no load-bearing premise.

Recommendation: preserve as an unreviewed proved candidate and exact
regressions. Do not promote the conditional Level I implication as a theorem.

## Autonomous audit (2026-10-15)

The [PR957 AI audit](../audits/pr957_autonomous_proof_audit_2026-10-15.md) records
the complete finite theorem, all-k construction, matching-certificate replay and
scope limits. Both checkers require assertions and refuse optimized Python.
This remains noncanonical; independent human mathematical review is pending.
