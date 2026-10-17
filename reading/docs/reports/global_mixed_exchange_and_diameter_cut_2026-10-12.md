> Generated reading edition · [exact source](../../../docs/reports/global_mixed_exchange_and_diameter_cut_2026-10-12.md) · source SHA-256 `2500066177ea855347938180e211f9fdb72b7596b016ded277476a2230d59540`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D86992FA4113","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Global mixed exchanges with a priced diameter cut

**Classification:** proved candidate awaiting promotion for the finite exchange
criterion; regression for the affine-optimal square families; conditional for
the proposed Level I implication. All material is noncanonical and unreviewed.

## Run lock and exact objective

Base commit: `ab6dd3336f9f8d440f2bada76edb32153391cddc`.
State version: `2026-10-10.audit.234`. Level I remains open. This is an
independent whole-problem run, with no unpromoted target theorem as a premise.
The objective is still **every** sufficiently large global minimizer, as in
[`../problem/statement.md`](../problem/statement.md). Finite matching duality
is proved below.

```text
triangle-free global source -> source-wide comparison cloud and upper cover
-> |X| - maximum_matching >= |T|
-> simultaneous n-point unit-separated replacement with diameter < R <= D
-> contradiction to global optimality.
```

The first arrow is unproved. The other arrows are exact.

## Global mechanisms compared

1. A uniform triangle-free density gap cannot close the problem: triangle-free
   perturbations approach triangular density. The current ledger separately
   registers a triangular-lattice population competitor and its triangle-free
   deformation, without claiming optimality.
2. Sticky-disk crystallization and periodic jamming optimize different
   quantities. The original Connelly--Dickinson
   [Periodic Planar Disk Packings](https://pi.math.cornell.edu/~connelly/Connelly-Dickinson-V3.pdf)
   states its general triangular-torus gap as Conjectures 2--3 and proves
   specialized triangle/rhombus results. Neither the conjectures nor a transfer
   from their fixed-period hypotheses is used here.
3. A discontinuous simultaneous reassignment was selected for an actual
   certificate. The comparison cloud and source need not share a contact
   manifold, rigid component, or lattice chart. Every full-source conflict is
   counted before selecting any replacements.

## Exact source-wide exchange criterion

Let A be an n-point unit-separated source of actual diameter D > 1. Choose
1 < R <= D and a vertex cover T of

$$
J_R(A)=\{ij:|a_i-a_j|\ge R\}.
$$

For R = D this covers every actual diameter pair. For R < D it also covers
all formerly inactive pairs reaching the new threshold. Put A0 = A minus T.
Let X be a finite unit-separated cloud of diameter strictly less than R.
Make a bipartite graph B on A0 and X, with an edge precisely when

$$
|a-x|<1\quad\text{or}\quad |a-x|\ge R.
\tag{1}
$$

If nu(B) is its maximum matching size, the largest compatible union formed
from A0 and X has exactly

$$
\boxed{n-|T|+|X|-\nu(B)}
\tag{2}
$$

points. Consequently

$$
\boxed{|X|-\nu(B)\ge|T|}
\tag{3}
$$

gives an n-point unit-separated competitor with diameter < R <= D.

**Proof.** Starting from unmatched left vertices, follow unmatched edges to
the right and matching edges to the left. No unmatched right vertex is
reachable, since it would give an augmenting path. Let Z be the reachable
vertices. Then K = (left minus Z) union (right intersect Z) covers every
edge: an edge from a reached left vertex leads to a reached right vertex.
Exactly one endpoint of every matching edge belongs to K, and no unmatched
vertex belongs to K. Thus |K| = nu(B). Every vertex cover is at least as
large as a matching. The complement of K is therefore a maximum independent
set and has the cardinality (2).

Both sides separately have separation at least one and diameter < R. The
cover T ensures this for A0. Equation (1) handles every mixed pair, including
duplicate coordinates and isolated source labels. The independent set is an
actual planar packing. Any n-point subset retains strict diameter < R. This
proves (3).

The replacement may change contacts and contain triangles. A contradiction
to global optimality requires only source cardinality and strict diameter
improvement.

## The obstruction imposed by every global minimizer

Every global minimizer satisfies, for every admissible R, T, X,

$$
|X|-\nu(B)\le |T|-1.
\tag{4}
$$

In Hall form, if N(S) includes **both** lower and upper conflicts of a packet
S subset X, then

$$
|N(S)|\ge |S|-|T|+1\qquad(S\subseteq X).
\tag{5}
$$

The maximum right-side Hall deficiency is |X|-nu(B). One proof is to use
the same alternating-path construction starting on the right: the unmatched
right vertices generate a packet whose deficiency equals their number.
For the reverse inequality a matching pairs all but |X|-nu(B) cloud labels
with distinct neighbors. Thus (4) and (5) are equivalent.

This is an exact global integer obstruction. It does not assert new matching
theory or a new universal geometric extraction theorem. Its useful extension
is that the cut prices the entire source and the complete new-diameter
ledger; no fixed wall or source/scaffold identification is assumed.

## Exact global jumps out of affine optima

Take A_k = {0,...,k-1} squared. Its diameter squared is 2(k-1)^2 and its
unit-contact graph is triangle-free. No affine image improves its diameter:
writing u,v for the affine map's column vectors, the old neighbor pairs force
|u|,|v| >= 1, while its two corner diagonals force

$$
\operatorname{diam}(F(A_k))^2
\ge(k-1)^2(|u|^2+|v|^2+2|u\cdot v|)
\ge2(k-1)^2.
$$

The verifier nevertheless certifies these simultaneous replacements:

| Source | R | Cover cost | Cloud count | Matching | Compatible count | n-point witness diameter squared |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A_31, n = 961 | 38 | 32 | 817 | 745 | 1001 | 1429 |
| A_41, n = 1681 | 52 | 32 | 1159 | 1055 | 1753 | 2689 |

The first union retains 200 old labels and inserts 801 cloud labels; the
n-point witness drops 40 surplus cloud labels. The second retains 718 old
labels and inserts 1035 cloud labels; its witness drops 72 surplus cloud
labels. Each cloud alone has fewer than n points.

Each upper cover handles 420 source pairs, including formerly inactive
pairs, and has a same-sized matching certifying minimum size. Each mixed
matching also has a same-sized cover. All final n-point pairs are then
checked independently in Q(sqrt(3)). These nonglobal square sources are
regressions against affine optimality implying global optimality.

### An infinite family, with a uniform certificate

For every k >= 33 set c = floor((k-1)/2). The triangular-lattice cloud

$$
X=(c,c)+\{(i+j/2,j\sqrt3/2):i^2+ij+j^2<225\}
$$

has exactly 817 points within radius 15 of (c,c). Every source point at
distance < 1 from X lies in the open radius-16 disk around (c,c), which has
exactly 793 integer points. These are finite exact integer enumerations,
also asserted by the verifier.

Delete those at most 793 labels and the two left corners, covering both
original diameter pairs. Every retained source point is at least one from
X. For every mixed pair,

$$
|a-x|<15+\sqrt2\lceil(k-1)/2\rceil<\sqrt2(k-1).
$$

The second inequality follows from floor((k-1)/2) >= 16 and 15 < 16 sqrt(2).
The cloud's diameter is < 30, also below the original diameter. The union
therefore has at least k^2 - 795 + 817 = k^2 + 22 points with strict smaller
diameter. Taking k^2 points excludes **every** A_k with k >= 33 from global
optimality, despite its affine obstruction.

This is not an unbounded family of triangle-free global minimizers.

## Reproducible certificate and limits

```sh
python3 research/verify_global_mixed_exchange_2026_10_12.py
```

The script uses integer comparisons in Q(sqrt(3)) and separately verifies
all final pair distances. The 2026-10-15 preservation repair additionally
emits the deleted/retained/inserted label sets, matching edges and both sides
of the cover as JSON. A separate replay checks the round-tripped certificate
against all original pairs without rerunning the matching search. Dropped
labels and repeated matching endpoints are rejected. Optimized Python is
refused because the checker requires assertions. Hostile fixtures reject a cloud attaining the old
diameter, an uncovered diameter pair, and a lower violation. An actual
contact isolate blocks an insertion; another fixture counts an equal upper
pair and a formerly inactive upper pair. The unit square does not produce
a strict competitor, agreeing with its global optimality.

The missing global theorem is **source-wide cloud extraction with enough
Hall deficiency**: from any sufficiently large triangle-free global
minimizer construct R, T, X satisfying (3). Density, positive area surplus,
individual site feasibility, or separate chart matchings do not establish
that inequality. The first implication of this report's chain remains open;
the ledger and Level I status are unchanged.

The [preservation audit](global_discrete_replacement_preservation_2026-10-15.md)
records the frozen source, complete proof/history comparison and repaired
certificate interface. This remains an unreviewed noncanonical candidate.
