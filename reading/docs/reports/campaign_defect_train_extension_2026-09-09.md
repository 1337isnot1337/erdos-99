> Generated reading edition · [exact source](../../../docs/reports/campaign_defect_train_extension_2026-09-09.md) · source SHA-256 `98c25016760f127f1e231eb4b54980d5b75caf3e15302ef74be61472f96d805c`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1E0BC6EBFD51","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99: trains ending at exceptional faces

**Date:** 2026-09-09

**Base:** `7838f6c0aabe0e3d63369bda804643c3c7833426`

**Type:** proof draft and continuation audit; not a canonical promotion

**Level I status:** STILL OPEN

This continues [the campaign ledger](campaign_ledger_2026-09-09.md) and
[the zero-transfer/rigidity report](campaign_zero_transfer_and_narrow_paths_2026-09-09.md).
The new conclusion is a lower bound on exceptional-face count when the nonisolated
core contains all but a subquadratic number of source points. It does not prove that
this population hypothesis holds, or exclude the resulting linear-defect branch.

**Review update:** the merged
[C-I restoration](../targets/target-c/56-ci-restored-frontier.md) now supplies
canonical universal PSD, finite integration, and the lexicographic normal form.
The additional zero-transfer/kernel-rank arguments in the preceding campaign
report remain separately stated dependencies of DF. No simultaneous hull-saturation
normalization is imposed. See [the consolidated review](campaign_zero_transfer_defect_review_2026-09-09.md).

## 1. Endpoint and notation

For a connected triangle-free unit-contact core write

- `v,e`: numbers of vertices and contact edges;
- `R,f`: numbers of bounded quadrilateral and nonquadrilateral faces;
- `b`: length of the outer boundary walk, with bridges counted twice;
- `Q=sum_non4 (k_F-4)`, where `k_F` is the face degree;
- `q`: number of convex-hull vertices;
- `h`: number of diameter pairs.

The later-C dependencies audited in the preceding report give, in the large
lexicographically normalized hypothetical counterexample,

```math
e+h\ge 2v-2,
\qquad b+Q\le2h\le2q.
\tag{D1}
```

The second inequality improves the older pinned-rank budget `b+Q<=4q-4`.
It still has the same linear scale. The intended implication is

```
trains with exceptional-face endpoints
  -> exposed-hull lower bound on T-q
  -> f >= a positive constant times D
  -> a contradiction only if a further global defect bound is proved.
```

The point requiring proof is that the train count and crossing graph remain valid
without a pure-disk assumption. No independent train-angle realizations across holes
will be asserted.

## 2. Finite train theorem without a disk hypothesis

### Theorem DT

Let `G` be a finite connected straight-line unit-contact graph of a unit-separated
triangle-free planar point set, with at least one edge. Through each bounded
quadrilateral face join the midpoints of each pair of opposite edges. Stop these
paths at every nonquadrilateral face and at the outer face. Count an edge incident
to no quadrilateral as a train with no rhombus.

Then:

1. every train is a path, with a fixed projective transverse edge direction;
2. distinct trains share at most one rhombus;
3. the train-crossing graph is simple and triangle-free;
4. its edge count is `R`, and its vertex count `T` satisfies

```math
T=e-2R
 =\frac{b+\sum_{F\text{ non4}}k_F}{2}
 =\frac{b+Q}{2}+2f.
\tag{D2}
```

In particular the formula counts bridges, holes in the rhombic region, separate
rhombic components, and edges between two exceptional faces.

### Proof

A quadrilateral unit-contact face is a nondegenerate rhombus. Both diagonals exceed
one, since equality would give a forbidden unit triangle. Its angles therefore lie
strictly between `pi/3` and `2pi/3`.

Make a graph whose vertices are the `e` contact edges. For each rhombus connect its
two pairs of opposite edges, adding two links. Each vertex of this graph has degree
at most two, one link for each incident quadrilateral side. Opposite edges are
parallel, so each component has a fixed unoriented transverse vector `u`.

Choose an orientation of `u`, and orient passage through every rhombus toward the
same normal `Ju`. A midpoint-to-midpoint step is a unit vector making angle strictly
less than `pi/6` with `Ju`: it is parallel to the other pair of rhombus sides, with
positive normal component. At a shared edge this rule continues consistently from
the rhombus on one side to the rhombus on the other. Projection onto `Ju` increases
strictly. Thus a component cannot be a cycle; its midpoint curve cannot self-intersect.
It is a path, including a singleton for a contact edge with no links.

Suppose two trains cross in a rhombus, and let `delta` be the acute projective angle
between their transverse directions. Then `pi/3<delta<=pi/2`. Orient their normals
to make the angle between the normals equal to `delta`. The two trains' step cones
have half-angle strictly less than `pi/6`. Project both curves onto the bisector of
the two normals. Both projections increase strictly: the angle from the bisector
is less than `delta/2+pi/6<=5pi/12<pi/2`.

In coordinates with this bisector horizontal, the slope intervals of the two curves
are disjoint and ordered. Their angular separation is at least
`delta-pi/3>0`. Each curve is a piecewise-linear graph on an interval. On the common
interval the difference of their height functions is strictly monotone. Hence they
intersect at most once. This proof applies to their complete paths even when the
endpoints lie on different exceptional faces.

If three trains crossed pairwise, their three projective directions on a circle of
length `pi` would have every pair at distance greater than `pi/3`. The three cyclic
gaps would then all exceed `pi/3`, an impossibility. Thus the crossing graph is
triangle-free. Each rhombus is its unique crossing for two distinct trains.

The edge-link graph is a forest with `e` vertices and `2R` links. Consequently
`T=e-2R`. Finally face-incidence counting gives
`2e=4R+b+sum_non4 k_F`, proving (D2). QED.

The classical train theorem of Kenyon and Schlenker concerns quad-graphs. DT gives
the exact finite form needed here, with trains stopped at arbitrary exceptional
faces; its narrow-cone argument avoids importing a disk-wide coordinate system.

## 3. Extending the phase and exposed-hull estimate

### Theorem DE

Consider a sequence of graphs satisfying DT, of diameters `D->infinity`. Suppose

```math
T=\Theta(D),\qquad R/D^2\longrightarrow r>0,
\tag{D3}
```

the sum of their rhombus area excesses is `o(D^2)`, and their convex hulls, after
translation and division by `D`, converge to the disk of diameter one. Let `q` be
their hull-vertex counts. Then

```math
\liminf\frac{T-q}{D}\ge 2\sqrt r-\frac\pi2.
\tag{D4}
```

The hypotheses concern the actual core embedding. They do not require a simply
connected rhombic region or a train-angle parametrization.

### Proof

Take any subsequence on which `T/D`, `q/T`, and the empirical probability measure
of projective train directions converge, to `tau`, `y`, and `mu`. Let `s` be the
total atomic mass of `mu`.

For a rhombus with acute angle `a in (pi/3,pi/2]`, its excess is
`sin(a)-sqrt(3)/2`. For any fixed positive distance away from `pi/3`, this excess
has a positive lower bound. Since its total is `o(D^2)=o(T^2)`, the normalized
ordered crossing measures have limits supported on

```math
\mathcal S=\{(x,y):y-x\equiv\pm\pi/3\pmod\pi\}.
```

By DT the crossing graph is simple, so its normalized ordered edge measure is
bounded by the product of its empirical direction measures. In the limit it is
bounded by `mu times mu`. This product has mass on `S` only at pairs of atoms.

Here is the finite-graph step needed to retain triangle-freeness in that limit.
Choose finitely many atoms carrying all but `epsilon` of the atomic mass, and take
small disjoint neighborhoods of them with `mu`-null boundaries. The limiting
crossing mass outside the square of those neighborhoods is bounded by the product
mass on `S` involving an omitted atom, hence by `2 epsilon`. Apply Mantel's bound
to the finite induced crossing graph on trains in the chosen neighborhoods. First
pass to the sequence limit, then shrink the neighborhoods, then let `epsilon` tend
to zero. This proves

```math
\frac r{\tau^2}\le\frac{s^2}{4}.
\tag{D5}
```

It remains to relate `s` to the hull. The outer boundary walk can be partitioned
into `q` walks between consecutive hull vertices, with total length `b<=2T`.
At a repeated hull vertex use its distinguished outer-face visit, the one whose
sector contains the exterior of the convex hull. These distinguished visits occur
in hull order: disjoint outward rays from the hull vertices meet an offset outer
boundary in that order. Other occurrences, including bridge excursions, remain
inside the resulting walks. The displacement of each walk is exactly its hull
side, of length at least one.

Fix an integer `M`. At most `2T/(M+1)` of these walks have more than `M` unit edges.
Choose finitely many atoms carrying at least `s-epsilon` of the atomic mass and
let `U_delta` be small neighborhoods of their projective directions. A walk of
length at most `M` whose directions all belong to `U_delta` has displacement within
`M delta` of one of finitely many signed sums of the chosen unit directions. Its
length is at least one. For sufficiently small `delta`, zero limiting sums cannot
occur, and the normals of the remaining sums lie in finitely many arcs of total
length `O_M(delta)`.

The hulls scaled by `D` converge to a disk. Their perimeter measures therefore
converge to its nonatomic circular measure. For completeness, their support
functions converge uniformly, so the measures `h+h''` converge in distributions
and weakly; the limiting support function is constant. Each hull side contributes
its length, at least one, to the measure at its normal. Hence the number of the
preceding atom-only short walks is `O_M(delta D)+o_delta(D)`.

Every other short walk uses an outer occurrence of a train outside `U_delta`.
Each train has at most two outer occurrences, including the two occurrences of
an isolated bridge. After division by `T`, passage to the sequence limit, and
then `delta->0`, `M->infinity`, and `epsilon->0`, this gives

```math
y\le2(1-s).
\tag{D6}
```

Combine (D5) and (D6):

```math
2\sqrt r\le\tau(1-y/2)
=\lim\frac{T-q/2}{D}.
```

The convex-hull perimeter is at most `pi D`, and its `q` sides have lengths at
least one, so `q/D<=pi`. Subtracting `q/(2D)` proves (D4) on every convergent
subsequence, hence proves the stated liminf. QED.

## 4. A necessary linear number of exceptional faces

### Corollary DF

Assume the later-C inputs audited in the preceding report, including the ZF
rigidity conclusion. Let `A_j` be triangle-free global minimizers, chosen first to
minimize contact count and then diameter-pair count. Put `D_j=D(n_j)->infinity`.
If their nonisolated cores satisfy

```math
n_j-v_j=o(D_j^2),
\tag{D7}
```

then the number `f_j` of bounded nonquadrilateral contact faces satisfies

```math
\boxed{
\liminf_{j\to\infty}\frac{f_j}{D_j}
\ge \sqrt{\frac{\pi}{2\sqrt3}}-\frac\pi4
=0.166914\ldots>0.}
\tag{D8}
```

Consequently, under these dependencies, an asymptotically full contact core with
only `o(D)` exceptional faces is impossible, even with holes, articulation points,
or multiple rhombic components.

### Proof

The exact global lattice bound and Oler/isodiametric upper bound give
`n/D^2 -> Delta=pi/(2sqrt(3))`. Since `f<=Q`, (D1), `b>=q`, and `h<=q` imply

```math
T=(b+Q)/2+2f\le h+2Q\le5q-2b\le3q\le3\pi D.
\tag{D9}
```

Euler and (D2) give the exact identity

```math
R=v+f-T-1.
\tag{D10}
```

Thus (D7) gives `R/D^2->Delta`. DT and Mantel give `R<=T^2/4`, so also `T=Omega(D)`.

Let `A_R` be the total rhombus area and `F` the core convex hull. Then

```math
\frac{\sqrt3}{2}R\le A_R\le\operatorname{area}(F)
\le\frac\pi4 D^2.
```

Both extremes divided by `D^2` converge to `pi/4`. The rhombus excess is therefore
`o(D^2)`, and the scaled core hull converges, up to translations, to the unit-diameter
disk. The last assertion follows by compactness of bounded convex bodies and the
equality case of the isodiametric inequality: every subsequential limit has area
`pi/4` and diameter at most one. Thus DE applies with `r=Delta`.

Finally (D1)-(D2) give `T-q<=2f`. Equation (D4) yields

```math
2\liminf f/D\ge2\sqrt\Delta-\pi/2,
```

which is (D8). QED.

This also proves a precise alternative: for every fixed
`eta<sqrt(Delta)-pi/4`, a hypothetical sequence with `f<=eta D` must have
`liminf (n-v)/D^2>0`. Otherwise a subsequence with `(n-v)/D^2->0` contradicts DF.
No explicit lower bound for that invisible fraction is supplied here.

## 5. Attempted closure by charging each exceptional face

The next attempted implication was

```
f >= 0.1669 D
  -> at least a fixed positive Oler excess per exceptional face
  -> an outer-shell contradiction.
```

The middle implication is false as a face-local statement. The following exact
family identifies the obstruction.

### Proposition DP: strict unit pentagons with vanishing Oler excess

For `0<u<=1/4`, put

```math
c=\frac{1-u^2}{1+u^2},\quad s=\frac{2u}{1+u^2},\quad
h=\sqrt{1-(c-1/2)^2}.
```

Take the five vertices in the displayed cyclic order:

```math
(-c,0),\quad (0,-s),\quad(c,0),\quad(1/2,h),\quad(-1/2,h).
\tag{D11}
```

They form a strictly convex, unit-separated polygon whose contact graph is exactly
the five-cycle. Its area `A(u)` satisfies

```math
0<A(u)-\frac{3\sqrt3}{4}<3u.
\tag{D12}
```

The term `3sqrt(3)/4` is precisely the facewise Oler lower bound for five unit
boundary edges and no interior points.

### Proof

Here `c>=15/17>1/2`, `s>0`, `c^2+s^2=1`, and `h>sqrt(3)/2`. All five successive
side lengths are one. The five nonedge squared distances are

```math
4c^2,\quad 1/4+(h+s)^2\quad\text{(twice)},\quad
1+2c\quad\text{(twice)}.
```

Each exceeds one. The five successive cross products of edge vectors are
`2cs`, `ch+s(c-1/2)`, `h`, `h`, and `ch+s(c-1/2)`, all positive. The polygon is
strictly convex and triangle-free.

Its area is

```math
A(u)=(c+1/2)h+cs.
```

Write `a=sqrt(3)/2`. Since `h>a`,
`A(u)-3a/2 > cs-a(1-c)>0`: the last inequality follows from
`cs-a(1-c)=2u(c-au)/(1+u^2)` and `c>u>=au`.
Also

```math
h-a=\frac{c(1-c)}{h+a}<1-c,
```

so

```math
A(u)-3a/2
=(c-1)h+\tfrac32(h-a)+cs
<\tfrac32(1-c)+s
\le3u^2+2u<3u.
```

This proves (D12). QED.

DP is a regression against a **uniform local** face charge. It does not refute
a charge using the surrounding full KKT network or global optimality. In fact its
diameter is exactly `2c` throughout `0<u<=1/4`. The horizontal extreme pair has
squared distance `4c^2>=900/289`; the other diagonal types obey
`1+2c<=3<900/289` and
`1/4+(h+s)^2<1/4+(25/17)^2<900/289`. Hence the bottom vertex is never diametral,
and its two contact vectors lie in an open halfplane. The isolated five-point
packing lacks force-visible equilibrium there. It is also explicitly nonglobal:
a regular unit pentagon has diameter `(1+sqrt(5))/2<5/3<30/17<=2c`.

There is a second exact obstruction to a count-only argument. Facewise Oler, with
`z_F` isolated points in a bounded face, gives

```math
\operatorname{area}(F)\ge
\frac{\sqrt3}{2}z_F+\frac{\sqrt3}{4}k_F-\frac{\sqrt3}{2}.
```

After summing all bounded faces and using Euler, the exceptional-face terms cancel:

```math
\frac{\sqrt3}{2}(v+Z_{\rm bounded}-1)
\le A_{\rm bounded}+\frac{\sqrt3}{4}b.
\tag{D13}
```

Thus substituting the new lower bound on `f` into ordinary facewise Oler yields no
additional surplus at all. A new simultaneous shell/face inequality is needed.

## 6. Branches advanced and still missing

| Branch | Exact hypotheses | Result and remaining implication |
|---|---|---|
| Rhombic pieces with exceptional faces | DT's finite contact embedding | Closed train and repeated-crossing possibilities are excluded; (D2) is exact. No independent angle parametrization is claimed. |
| Asymptotically full core, sublinear exceptional faces | Global lexicographic source, audited C stack, (D7), `f=o(D)` | Closed by contradiction, DF. |
| Asymptotically full core, linear exceptional faces | Same source and (D7) | Reduced to a theorem contradicting `f/D>=sqrt(Delta)-pi/4`, or the original exact boundary/face inequality `b+Q>2h`. |
| Few exceptional faces, many isolated points | Same source, `f<=eta D`, `eta<sqrt(Delta)-pi/4` | Reduced to excluding a positive quadratic invisible population; DF forces `liminf(n-v)/D^2>0`. |
| Uniform excess for every exceptional face | Strict convex unit-separated face only | Disproved by DP. The missing hypothesis must involve simultaneous source geometry. |
| Bare facewise Oler plus the new count | (D8) and individual Oler inequalities | No gain: exact cancellation (D13). A joint shell correction remains necessary. |

The shortest sufficient remaining theorem from the earlier ledger remains
`b+Q>2h` for every sufficiently large hypothetical lexicographic source. A weaker
new sufficient pair would be `(n-v)=o(D^2)` and
`limsup f/D<sqrt(Delta)-pi/4`. Neither is established.

## 7. Literature, computation, and audit

The related primary source checked in this continuation was Kenyon and Schlenker,
*Rhombic embeddings of planar graphs with faces of degree 4*,
[arXiv:math-ph/0305057](https://arxiv.org/pdf/math-ph/0305057), Theorem 3.1.
Its stated finite setting requires every bounded face to be quadrilateral. It is
not imported as a theorem about exceptional-face topology. DT supplies the needed
argument under the stronger angle restriction furnished by unit separation.

DE adapts the proof in Target B Section 39, retaining finite-graph Mantel before
taking limits, the order of neighborhood limits, the lower bound of one on hull
side lengths, and the two-end count for trains. Only `o(D^2)` rhombus excess is
needed for this leading-order result. DF uses a fixed positive linear margin;
it does not absorb an uncontrolled linear error into a one-integer inequality.

The exact verifier is
[campaign_2026_09_09_defect_trains.py](../../../research/campaign_2026_09_09_defect_trains.py).
It checks all connected induced subsets of the `4 by 4` integer grid with at least
two vertices, including bridges and holes. It reconstructs planar face walks,
opposite-edge trains, unique crossings, and all identities in (D2). The coordinates
are exact integers. It also checks rational parameter data and all nonedge formulas
for DP. This tests bookkeeping; it is neither the proof of DT for arbitrary angles
nor a global-optimality certificate.

Review run: 11,490 connected grid subsets passed, including 529 with exceptional
bounded faces and 11,158 with repeated outer boundary vertices. All 997 rational
pentagon parameters `u=1/m`, `4<=m<=1000`, passed every-pair and strict-convexity
checks. No numerical tolerance is used in these results.

Regression audit:

- Regular shells have quadratic invisible fillings when they approach packing
  density; DF does not discard that missing population hypothesis.
- Disk-clipped oblique grids need not satisfy ZF or the minimizing-source hypotheses.
  DT applies to their actual rhombi without making them optimal.
- Holes and bridges are included in DT; train-angle independence across them remains
  unproved and is not used.
- Vanishing conductances play no role in DT/DE. DF retains the previously audited
  C dependencies instead of obtaining stress rank from train incidence.
- DP checks every pair and every convexity inequality; it does not claim global
  optimality or an independently valid positive KKT extension.
- No actual source point is identified with an independently chosen lattice or
  response vertex, and isolated points remain explicitly separate from `v`.

**Hold as report.** No canonical route map or active prompt is changed. A promotion
would need to audit DT/DE and DF's C-stack dependencies separately. The global
quantifiers remain unclosed, and this report does not certify exhaustion of all
possible proof routes.
