<!-- theorem-state: {"artifact_id":"ART-8A33E2B8AC27","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "58b9ebcd96253241332b445086ff6c224c6ba77b", "source_head": "3a80b4bd2d75a439835ab26a863521816a0f39d1", "source_lifecycle": "unreviewed", "source_path": "docs/reports/global_nonexpanding_rhombus_mesh_obstruction_2026-10-13.md", "source_pr": 967, "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "8375175cc2dacc94dcf5fcd97af1ffe461dce2bc6a01281fff28fc25616bed79"} -->

> **Imported unreviewed source research.** PR #967 is not a theorem promotion; current destination theorem state remains authoritative.

# Global nonexpanding endpoints: a rhombus-mesh obstruction

**Date:** 2026-10-13. **Seed:** 54.
**Category:** Global diameter competitors and extremal geometry.
**Research base:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.
**State:** `2026-10-10.audit.234`. **Level I:** STILL OPEN.
**Classification:** proved candidate awaiting independent audit; the constructed
families are regressions, and this report remains unreviewed and noncanonical.
**Prompt:** [whole-problem continuation](../prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md).
**Literature:** no new imports. **Computation:** two separate exact engines below.

## 1. Endpoint and claim

The closing endpoint is an actual same-cardinality unit-separated competitor
with diameter strictly below the complete source diameter. Its existence for
every sufficiently large triangle-free global minimizer would prove Level I.
The canonical population reserve, including its sharp leading coefficient,
does not construct such a competitor.

This run tested a stronger sufficient architecture: decrease every pairwise
distance, while retaining lower separation. The new result rules out that
architecture for a broad mesh class, even when a strict independent replacement
exists. It also identifies the local distances that a successful replacement
has to increase. No statement below asserts global optimality of a fixture.

```text
universal triangle-free-source nonexpanding strict replacement
    -> same-cardinality strict-diameter competitor -> Level I

new regression: asymptotically triangular-density nonglobal sources can have
    no nonexpanding strict replacement, even at arbitrary finite endpoints
```

This rejects the universal architecture for arbitrary triangle-free sources.
It does not reject a source theorem exploiting global optimality to exclude
these meshes, or an endpoint allowed to increase inactive pair distances.

## 2. Exact local-to-global endpoint rigidity

Let `u,v` be unit vectors with

\[
u\cdot v=c,\qquad 0\le c<1/2.
\]

For a finite nonempty set of indices `J` in `Z^2`, define cells

\[
F_{ij}=\{iu+jv,(i+1)u+jv,(i+1)u+(j+1)v,iu+(j+1)v\}.
\]

Assume the cell graph on `J`, in which indices differing by `(1,0)` or
`(0,1)` are adjacent, is connected. Let `V` be the union of all cell vertices.

**Theorem 1 (proved candidate).** For every map `f:V -> R^2`, suppose:

1. every two distinct source labels have image distance at least one;
2. every cell edge has image length at most one;
3. each of the two diagonals of each cell has image length at most its
   original length.

Then a single Euclidean isometry `T` satisfies `f(x)=T(x)` for all `x in V`.
This is a finite endpoint statement; no continuity, affine formula, stress,
first-order motion, or feasible interpolation is assumed.

**Proof.** Each image edge has length exactly one, by conditions 1 and 2.
Write an image cell in cyclic label order as `a,b,d,e`, so `a,d` are opposite.
Both `b,e` are intersections of the unit circles about `a,d`. Distinct-label
separation makes all four points distinct. Thus `0<|a-d|<2`, the circles
have exactly two intersections, and `b,e` occupy opposite intersections.
The image is a nondegenerate rhombus, and

\[
|a-d|^2+|b-e|^2=4.
\]

The original diagonal squares are `2+2c` and `2-2c`, also summing to four.
Both diagonal upper bounds therefore hold with equality. The labeled image
cell is congruent to the original cell.

Choose the isometry given by one cell. For an adjacent cell, there are just
two labeled congruent placements fixing their shared edge: its original
placement under this isometry, and its reflection across that edge. The
reflected choice places the two cells on the same side. For a shared edge
parallel to `u`, two distinct off-edge labels then have images
`z+v` and `z+v-2(v dot u)u`, at distance `2c<1`. For a shared edge parallel
to `v`, interchange `u,v`; the same distance results. When `c=0` these
images coincide, which also violates condition 1. Hence only the original
placement is allowed. Connectivity propagates the same isometry over every
cell and every vertex. QED.

**Corollary 1 (proved candidate).** Let a finite full source be `A=V union I`,
where `V` satisfies Theorem 1 and some actual diameter pair of `A` lies in `V`.
Every same-label unit-separated strict-diameter endpoint must increase at
least one cell edge or one cell diagonal. In particular, no endpoint that is
nonexpanding on every original pair can have smaller diameter, even when all
labels in `I` may move freely.

Indeed, if none of those local lengths increases, the theorem fixes `V` up
to an isometry and retains an actual diameter pair. This accounts for `I`
without extending a core matrix theorem to isolated coordinates.

The old cell diagonals are inactive for the large sources below. A correct
diameter-feasible motion may increase them while keeping them far below `D`.
The obstruction is to requiring their monotonicity, not to permitting that
increase in the real problem.

## 3. An unbounded dense family, including an off-lattice isolate

For each integer `k>=2`, put

\[
c_k=\frac12-\frac1k,\quad
s_k=\sqrt{1-c_k^2},\quad
u=(1,0),\quad v_k=(c_k,s_k),\quad R_k=16k^2.
\]

Take precisely the lattice cells whose centers obey

\[
|(i+1/2)u+(j+1/2)v_k|\le R_k,
\]

except the sixteen cells with `-2<=i,j<=1`. Let `V_k` be their vertices and
set

\[
A_k=V_k\cup\{p\},\qquad p=u/10,
\qquad n_k=|A_k|,\qquad D_k=\operatorname{diam}A_k.
\]

**Theorem 2 (proved candidate regression).** For every integer `k>=2`:

- `A_k` is unit-separated and triangle-free, and `p` is a contact isolate;
- `2R_k<=D_k<=2R_k+2`;
- `A_k` has no same-cardinality pairwise nonexpanding strict-diameter endpoint;
- there exists an independent `n_k`-point unit-separated set of diameter
  at most `2(R_k-1)<D_k`;
- along this unbounded family,
  \[
  \lim_{k\to\infty}\frac{n_k}{D_k^2}
  =\frac{\pi}{2\sqrt3}.
  \]

Thus asymptotically triangular density and failure of every pairwise
nonexpanding endpoint do not imply global optimality. The theorem makes no
sharp population-reserve, positive-stress, or canonical C-II source claim.

### 3.1 Complete lower-pair and contact check

For every lattice difference `(a,b)` its squared norm is

\[
Q_k(a,b)=a^2+b^2+2c_kab.
\]

When `ab>=0`, it is at least `a^2+b^2`. When the signs oppose, writing
`A=|a|,B=|b|` gives

\[
Q_k(a,b)=(A-B)^2+2(1-c_k)AB.
\]

For `A,B>=1`, the latter is strictly greater than one, since
`2(1-c_k)>1`. Consequently every nonzero integer difference has norm at
least one, with equality exactly at `(+/-1,0)` and `(0,+/-1)`. The contact
graph is bipartite under the parity of `i+j`; no unit triangle exists.

Removing the sixteen central cells leaves exactly the nine central lattice
sites `-1<=i,j<=1` absent. All other vertices occur in a complete cell. For
any retained lattice label, either `|j|>=2` or `|i|>=2`. Its squared distance
to `p` is

\[
(i-1/10)^2+j^2+2c_k(i-1/10)j.
\]

Minimizing this quadratic over the other real coordinate gives at least
`s_k^2 j^2` or `s_k^2(i-1/10)^2`. Since `s_k^2>=3/4`, one of these is at
least `3` or `1083/400>1`. Every isolate-involving lower pair is strict.
Every mesh vertex has at least two unit contacts in its cell, so `p` is the
only contact isolate.

### 3.2 Connectivity, anchors and the complete upper bound

Write cell-center indices as half-integers `alpha=i+1/2,beta=j+1/2`.
An admitted cell has `max(|alpha|,|beta|)>=5/2`. If this maximum is greater
than `5/2`, decrease a coordinate of largest absolute value by its sign.
The decrease in its squared physical norm is at least

\[
2(1-c_k)\max(|\alpha|,|\beta|)-1>0.
\]

The step remains outside the deleted block and inside the center disk.
Iteration reaches the square ring `max(|alpha|,|beta|)=5/2`. That ring is
edge-connected; all its centers have norm at most five and so are admitted.
The complete cell graph is therefore connected.

The labels `+/-R_k*u` and `+/-R_k*v_k` occur. For example, the cell center
`(R_k-1/2)u+(1/2)v_k` has squared norm

\[
R_k^2-(1-c_k)(R_k-1/2)<R_k^2.
\]

The other anchors follow by symmetry and interchanging coordinates. Every
mesh vertex is within one of its center, and hence lies in the radius
`R_k+1` disk. This bounds every mesh upper pair by `2R_k+2`. The isolate
`p` lies inside the convex hull of the four displayed anchors; its distances
to mesh labels cannot exceed the mesh diameter, by convexity. Thus
`D_k=diam(V_k)>=2R_k`, and all isolate-involving upper pairs are included.
Theorem 1 and Corollary 1 now prohibit a nonexpanding strict endpoint.

### 3.3 Counting the source and constructing the independent competitor

Centered unit lattice parallelograms tile the plane with area `s_k` and
have radius at most one. The disjoint tiles centered at source lattice
labels lie in the radius `R_k+2` disk. Conversely, the radius `R_k-2` disk
is covered by tiles whose centers have norm at most `R_k-1`; those centers
are source vertices except for the nine removed central sites. Therefore

\[
\frac{\pi(R_k-2)^2}{s_k}-8
\le n_k\le
\frac{\pi(R_k+2)^2}{s_k}+1.\tag{1}
\]

Together with `s_k -> a_0=sqrt(3)/2` and the diameter bounds, this proves
the claimed density limit and that `n_k` is unbounded.

A unit triangular lattice has fundamental area `a_0`. Averaging its
translations over one fundamental parallelogram gives precisely
`pi*(R_k-1)^2/a_0` sites in the radius `R_k-1` disk on average. This follows
by integrating the sum of the disk indicators of all translated lattice
sites; the translated parallelograms tile the plane. We next prove this mean
exceeds the upper bound in (1).

For `k>=2`, direct squaring gives

\[
\frac{s_k}{a_0}>1+\frac1{4k},
\]

because

\[
s_k^2-a_0^2(1+1/(4k))^2
=\frac5{8k}-\frac{67}{64k^2}>0.
\]

For `R>=10`,

\[
\frac{(R+2)^2}{(R-1)^2}<1+\frac8R.
\]

If `k>=3`, substituting `R=16k^2` gives

\[
\begin{aligned}
\frac{\pi(R-1)^2}{a_0}-\frac{\pi(R+2)^2}{s_k}
&>\frac{\pi(R-1)^2}{s_k}\frac{k-2}{4k^2}\\
&>1,
\end{aligned}
\]

using `s_k<=1`, `pi>3`, and `R-1>=15k^2`. For `k=2`, `R=64`, `s_k=1`,
and

\[
\frac{s_k}{a_0}=\frac2{\sqrt3}>\frac87,
\qquad \frac{66^2}{63^2}<\frac{11}{10};
\]

the same difference is greater than `3*63^2*(3/70)>1`.
Thus some translate contains more than `n_k` sites in the smaller disk.
Take any `n_k` of them. Every pair remains unit-separated and has distance
at most `2(R_k-1)<D_k`.

This is an independent replacement of every source label, including `p`,
by an explicit cardinality-preserving bijection. It may create unit triangles
and lose old contacts, both permitted by the definition of `D(n)`. In
particular, `A_k` is rigorously nonglobal for every `k`; these are no
counterexamples to Level I. QED.

## 4. A linear number of cells must permit distance growth

The exact obstruction has a quantitative extension. Use the source construction
in Section 3 with any `R>=24` and `0<=c<1/2`; the sixteen central cells are
still omitted and the off-lattice isolate is still included. Let `f` be any
same-label unit-separated endpoint. Call a cell **bad** when at least one of
its four edges or two diagonals is longer at the endpoint than in the source.

**Theorem 3 (proved candidate regression).** If

\[
\operatorname{diam} f(A)\le 2(R-1),
\]

then there are at least `ceil(R/8)` bad cells. In particular, the independent
replacement diameter certified above forces a linear number of cells to
permit some local distance growth, for every possible labeling of that
replacement. The result does not assert this bound for an arbitrarily tiny
strict improvement whose diameter remains above `2(R-1)`.

At least `ceil(R/16)` distinct local source pairs must grow: a cell diagonal
belongs to one cell and a cell edge belongs to at most two, so each growing
pair accounts for at most two bad cells.

**Proof.** Let `b` be the number of bad cells. Each connected component of
good cells is carried by a single isometry, by Theorem 1. Its source vertex
set, and consequently its source convex hull, therefore has diameter at
most `2(R-1)`.

Assume for contradiction `b<R/8`. Every cell lies in a radius-one disk about
its center. The set of radii of circles meeting a given bad cell is a closed
interval of length at most two. The union of these intervals has length at
most `2b<R/4`. Hence there is a radius `r` in `(R/4,R/2)` whose entire circle
misses every bad cell. Choose it also to avoid the finitely many vertex and
edge tangency radii.

Put `a=sqrt((1+c)/2)<1`, the maximum distance from a cell center to its
vertices, and `rho=R-a>R-1`. The tiling by all lattice cells shows that the
annulus `R/4<=|x|<=rho` is entirely covered by admitted cells: a cell
containing such a point has center norm at most `rho+a=R`, and the deleted
central cells lie in the radius-four disk, below `R/4>=6`. The cells crossed
by the circle of radius `r` are edge-connected, since a circle chosen as
above crosses edges without passing through vertices or running along an
edge. They are all good; let `G` be their common good component.

For almost every direction `theta`, if the radial segment from `r` to `rho`
in that direction misses bad cells, its successive cells are edge-connected
good cells belonging to `G`. Its outer endpoint belongs to the convex hull
of the source vertices of `G`. Both opposite directions cannot have this
property: the two outer endpoints are `2rho>2(R-1)` apart. Therefore the
angular shadows of bad cells outside the circle must cover at least one
direction from almost every antipodal pair. Their union has angular measure
at least `pi`.

A bad cell outside this circle has center norm `t>=r-1>R/4-1>=R/6`.
It is contained in a radius-one disk. Its entire angular shadow is at most
`2 arcsin(1/t)<=4/t<=24/R`, since `1/t<=6/R<=1/4` and
`arcsin(x)<=2x` for `0<=x<=1/2`. Thus the shadow union has measure at most

\[
\frac{24b}{R}<3<\pi,
\]

a contradiction. Consequently `b>=R/8`. QED.

The proof retains every source pair through endpoint lower separation and
diameter feasibility. It neither assumes the endpoint faces form an embedded
tiling nor transports the isolate through a face: only each good component
is proved isometric. The circles and angular shadows are in the actual source
tiling and are used to force a large good component, not a fictitious endpoint
chart. No crossing count is converted into a site count.

## 5. Exact finite certificates and hostile checks

The finite certificate also uses the same formulas at `(k,R)=(2,24)` and
`(3,40)`, where actual centered comparison counts verify the replacement
directly. The general analytic onset `R=16k^2` is not asserted at those two
smaller radii.

| k | R | Full source n | Source diameter squared | Replacement diameter squared | Isolates |
| --- | --- | --- | --- | --- | --- |
| 2 | 24 | 1893 | 2420 | 2116 | 1 |
| 2 | 64 | 13141 | 16724 | 15876 | 1 |
| 3 | 40 | 5259 | 6636 | 6084 | 1 |
| 3 | 144 | 66657 | 83776 | 81796 | 1 |

The primary engine constructs cells and their vertices, checks cell-graph
connectivity, enumerates every integer displacement in the source difference
box to verify the complete lower classification, checks every isolate pair,
and computes the exact actual diameter on the convex hull. Hull extremality
certifies the upper bound for every source pair, rather than treating only
selected diameter edges. A complete centered triangular packet is enumerated;
the lexicographically first `n` sites give the equal-cardinality replacement.
Its lower pairs use the integral triangular norm and all upper pairs use
the disk bound plus an exact hull diameter. Coordinate-index hashes and
actual diameter witnesses are in the certificate.

Both engines also check the bad-cell and distinct growing-pair counts for
an actual endpoint labeling: sorted mesh vertices map to the first `n-1`
sorted replacement sites, and the old isolate maps to the last site. The
Theorem 3 bound holds on each of these endpoints. This tests concrete
instances without claiming exhaustive enumeration of all labelings.

The separate Cartesian engine generates each vertex from its own adjacent
center predicates, uses coordinates

\[
\left(\frac{2ki+(k-2)j}{2k},
\frac{j\sqrt{3k^2+4k-4}}{2k}\right),
\]

and uses a gift-wrapping hull algorithm instead of the primary monotone-chain
algorithm. It checks every isolate upper and lower pair directly. On the
1893- and 5259-label fixtures it also checks every original and replacement
pair directly. The larger fixtures use the exact lower norm classification
and hull extremality, covering 86,336,370 and 2,221,544,496 full source pairs;
quadratic enumeration of those larger ledgers is not claimed. Both engines
use integer and rational arithmetic only.

Reproduce from repository root:

```bash
python3 research/verify_seed054_rhombus_mesh.py > /tmp/seed054-primary.json
cmp /tmp/seed054-primary.json research/seed054_rhombus_mesh_certificate.json
python3 research/check_seed054_cartesian_certificate.py
```

The primary engine includes five negative/scope controls: one diagonal can
shrink while the other grows in a valid unit rhombus; omitting label separation
permits coincident reflected square cells; disconnected meshes can move
toward one another; exact triangular-lattice contacts defeat the contact
parity claim at `c=1/2`; and the strict comparison bound is genuinely below
the source anchor distance. The last two are scope/strictness controls, not
an exhaustive independent proof of the infinite theorem. The analytic family
is proved above; its sampled algebra checks do not supply infinite quantifiers.

This result respects the binding regressions: it infers no Euler path, FB4
localization, PSD selection, full-source ZR/ZF rank, fixed-wall capacity,
or integration of a first-order release. The isolate is retained in both full
pair ledgers and explicitly replaced in the independent competitor. Adjacent
cell motions are coupled by a proved geometric gluing argument, not presumed
compatible.

## 6. Frontier effect, attempts and remaining gap

The run ledger is [seed054_run.md](../../research/seed054_run.md). Rounding
with an O(1) boundary displacement has not yielded the needed sub-D^(2/3)
population error. Weighted collective shortening has not yielded simultaneous
full-source upper feasibility. Neither failed attempt is relabeled as a new
impossibility theorem.

| New assertion | Classification | Dependency and limit |
| --- | --- | --- |
| Connected rhombus-mesh endpoint rigidity | Proved candidate, unreviewed | Circle intersection and explicit adjacent-cell exclusion |
| Every strict endpoint grows a cell edge or diagonal | Proved candidate, unreviewed | Theorem 1; actual diameter pair must lie in the mesh |
| Reaching diameter at most `2(R-1)` requires at least `ceil(R/8)` bad cells | Proved candidate regression, unreviewed | Theorem 1, actual source annulus, circle selection and antipodal angular shadows |
| Dense unbounded family, isolate, strict independent competitor | Regression, candidate proof unreviewed | Elementary lattice tiling/averaging and full pair formulas |
| Universal nonexpanding replacement for arbitrary triangle-free sources | Rejected conjectured architecture | Theorem 2 supplies exact counterexamples |
| Universal replacement for triangle-free global minimizers | Unresolved | Global optimality supplies restrictions absent in these fixtures |

No canonical theorem state, target branch, or Level I status changes.
The smallest missing lemma for the closing chain remains a source-specific
same-cardinality replacement theorem for every sufficiently large triangle-free
global minimizer, satisfying every lower pair and shortening the maximum of
every upper pair. In the packet architecture this means a certified packing
surplus paying an actual diameter cover and all cross conflicts. The new
theorem supplies neither such a packet nor an exclusion of every global
survivor. It shows that a sufficient endpoint architecture must allow growth
of some inactive local lengths, or first prove that the rigid mesh hypothesis
cannot contain the relevant diameter pair.

**Promotion recommendation:** retain as unreviewed research and request an
independent mathematical audit of Theorems 1–3. The scripts are finite
certificates, not an independent audit or proof of global optimality.
