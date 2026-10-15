<!-- theorem-state: {"artifact_id":"ART-1186EE9AD94D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — exact lattice carriers cannot account for the loaded boundary

Date: 2026-10-05. Base main: `3c94a1a93641a5f8fa24d43068d487594d3e38cd`.
State: `2026-10-05.audit.57`. Classification: **proved candidate awaiting
independent audit**; artifact lifecycle remains **unreviewed**.
C-II and Level I remain open.

## 1. Closing implication and scope

```
all but o(D) actual loaded vertices accounted for by exact lattice
attachment carriers, with only o(D) unused loaded vertices
-> canonical carrier count and total perimeter give o(D) loaded vertices
-> contradiction to q>=h>=ceil(D).
```

This excludes that exact attachment-crystal subcase in either canonical
branch. It does not assert that all sources fall into it. Approximate
phase coherence is not the exact lattice hypothesis. Source points
outside these carriers, including every contact isolate, are unrestricted
and retained. No finite packing or global optimality claim is inferred
from a scaffold.

A primary-source lead is Archit Das, *Stress, rigidity and rhombic
reductions for an Erdos minimum-diameter problem (Problem #99)*,
[author manuscript](https://zenodo.org/records/22768362), Section 6,
Lemma 6.2 and Theorem 1.5. The PDF was retrieved and its Sections 6–9
read. It uses a lattice hull-vertex bound to exclude a rigid source
contained wholly in a two-direction lattice. Below the elementary
hull bound is proved directly and applied only to loaded attachment
sets. No external theorem is a premise. The existing canonical
`C-OBLIQUE-LATTICE-COMPETITOR` concerns an entire affine-lattice source;
that is not assumed here.

## 2. Elementary integer-polygon estimate

Let K be a convex polygon with vertices in Z^2, with perimeter P and
r extreme vertices. Distinct oriented polygon sides have distinct
directions, hence their nonzero integer difference vectors are distinct.
For R>=1 there are at most (2 floor(R)+1)^2-1<=9R^2 such vectors
with Euclidean length at most R. The number of longer sides is at most
P/R. Thus r<=9R^2+P/R. An integer polygon has P>=1; choosing R=P^(1/3)
gives

    r<=10 P^(2/3).

For a set with at most two extreme vertices use the separate bound two.
If a finite set E consists entirely of extreme vertices of a larger
source hull and E lies in a+tZ^2, for an invertible linear map t, then
every point of E is extreme in conv(E). Affine transformation preserves
this property. If ||t^(-1)||<=K0 and P_E is the perimeter of conv(E),
then the transformed perimeter is at most K0 P_E. Consequently

    |E|<=2+10 K0^(2/3) P_E^(2/3).                 (2.1)

A segment has perimeter twice its length and a singleton perimeter zero.
These conventions cause no issue because of the separate two-point term.
For a basis of unit vectors with angle in [pi/3,2pi/3], the smallest
singular value is at least 1/sqrt(2), so K0=sqrt(2) is uniform, including
angles arbitrarily close to the triangular limit.

## 3. A finite boundary-carrier theorem

Let B be actual diameter endpoints of a finite source. Every b in B is
extreme in the source hull: a nontrivial convex representation of b,
paired with a point at distance D, contradicts strict convexity of
squared norm and the upper distance bound D.

Let E_1,...,E_L be subsets of B, each contained in an affine lattice
with inverse-basis norm at most K0. Put P_j=per(conv(E_j)). Let B0
contain the loaded vertices not covered by these subsets. Overlap among
subsets is allowed. Summing (2.1) and using concavity or Holder gives

    |B|<=|B0|+2L+10 K0^(2/3) L^(1/3) (sum_j P_j)^(2/3).       (3.1)

For L=0 the last two terms are zero and the assertion is just coverage.
Thus L=o(D), sum P_j=O(D), and |B0|=o(D) imply |B|=o(D).
For a canonical C-II source this contradicts q>=h>=ceil(D).
This finite inequality does not require contact rigidity on the carriers
or positive pinned stress. Its extreme-vertex requirement is essential:
a dense interior lattice patch has quadratically many nonextreme points.

As a separate consequence, if B is covered by L lattices of the stated
condition number with no total-perimeter information, each carrier has
perimeter at most pi D. Therefore

    q<=2L+10 K0^(2/3) L (pi D)^(2/3).

In particular a bounded number, or o(D^(1/3)) such lattices, cannot
contain the canonical loaded boundary of an unbounded source sequence.
No assumption places the other source points in those lattices.

## 4. Composition with the canonical harmonic attachment stack

Use [Section 75](../targets/target-c/75-all-phase-component-deatomization-audit.md).
Its unloaded positive-contact components I_r have actual loaded
attachment sets A_r, graph diameters delta_r, and c_I=O(D^(2/3)).
Harmonic trapping gives diam(A_r)<=delta_r+2. Its exact ledger yields

    sum_r delta_r+2c_I<=2+2q-e_BB-k<=2+2q.

Consequently their actual convex attachment carriers satisfy

    sum_r per(conv(A_r))<=pi(2+2q)=O(D),

using q<=per(F)<=pi D. This concerns actual source attachments and is
not an identification with an abstract harmonic scaffold.

Call r an exact lattice attachment component if A_r lies in some affine
lattice with inverse-basis norm at most a fixed K0. Only its attachment
set needs this property; its interior points can be arbitrary. Apply
(2.1) to every such A_r. There are at most c_I of them and their summed
perimeters are bounded by the full sum. Hence

    |union_{r exact lattice} A_r|
      <=2c_I+10 K0^(2/3)c_I^(1/3)[pi(2+2q)]^(2/3)
      =O(D^(8/9))=o(D).                         (4.1)

Let B_unused=B\union_r A_r. Every loaded vertex outside the union in
(4.1) belongs either to B_unused or to an attachment set lacking the
exact lattice property. Thus

    |B_unused union union_{r not exact lattice} A_r|
       >=q-O(D^(8/9))>=D-O(D^(8/9)).             (4.2)

This is a necessary condition on every canonical source sequence.
If |B_unused|=o(D), linearly many distinct actual loaded vertices must
be accounted for by attachment components without a uniformly
conditioned exact lattice. It is not claimed that these components
have linearly many independent defects, contacts, or spare sites.

## 5. What the argument does not supply

Section 69 produces fixed-width coherent phase grains. It permits
nonzero differences between train directions and does not put all
attachment vertices of a harmonic component in one exact affine lattice.
The boundary can change lattice through exceptional faces or contacts.
Neither connectedness of the unloaded component nor loaded return
paths establish the missing exact-lattice transport. Also B_unused can
be linear: the canonical loaded-loaded contact currency is not discarded.

Therefore (4.2) is not a C-II or Level I closure. A closing use must
exclude the unused-loaded alternative and force exact attachment
transport, or use the actual nonlattice transfer to construct a strict
refill or a finite strict-diameter competitor. The elementary bound
alone assigns no packing capacity to that transfer.

## 6. Dependencies and validation scope

Canonical inputs: actual diameter endpoints are hull-extreme;
q>=h>=ceil(D); Section 75 component count, trapping and ledger;
q<=pi D. The integer-polygon estimate and carrier inequality are proved
above. The exact-lattice subcase exclusion and necessary condition
(4.2) are proved candidates awaiting independent audit. No theorem
state or route is promoted. No numerical experiment is used, and no
verifier is needed for the universal elementary inequalities.

## 7. Robust exclusion of finitely many near-lattices in the near-disk branch

The full-core Type-II disk limit strengthens the exact arithmetic
obstruction. Let the actual loaded hull F satisfy

    B(0,r)<=F<=B(0,R),     alpha=acos(r/R),

with r/D,R/D tending to 1/2. Suppose that, apart from a set B_bad, its
loaded vertices are partitioned into J sets E_j. Every point of E_j
is within epsilon<1/4 of some point of an affine lattice a_j+t_j Z^2,
where ||t_j^(-1)||<=K0. Different carriers may use different lattices,
which may also vary with the source. Put

    delta=asin(2epsilon),
    Delta=2asin(L/(2r)),
    M=[2K0(L+2epsilon)+1]^2,

where 1<=L<2r and Delta+2alpha<pi. Then

    q<=|B_bad|+2J+J*pi*D/L
          +2J*M*R/cos(alpha)*(delta+alpha+Delta).       (7.1)

In particular, if J and K0 are fixed, |B_bad|=o(D), and epsilon=o(1),
then q=o(D). This contradicts the canonical q>=h>=ceil(D). Thus a
full-core survivor cannot place all but o(D) loaded endpoints within
o(1) of a bounded number of uniformly conditioned affine lattices.
The assertion is about physical positional error, not reduced phase
error, and does not apply to the macroscopic-container branch without
the near-disk hull hypothesis.

### Proof of the finite estimate

Fix one E_j with at least three vertices. Its vertices are extreme in F
and hence also in conv(E_j); list them in boundary order. The radial
angles of points on F are strictly ordered because F contains the inner
disk. The forward radial gaps of successive E_j points sum to 2pi, so
at most one edge has gap at least pi. Discard that edge from the
short-edge argument.

There are at most per(conv(E_j))/L<=pi D/L edges longer than L. For
every remaining edge a,b let eta be its radial gap, so 0<eta<pi. Since
|a|,|b|>=r,

    |a-b|^2=(|a|-|b|)^2+4|a||b|sin^2(eta/2),

and |a-b|<=L gives eta<=Delta. Choose lattice approximants a',b'.
Their difference z=b'-a' is nonzero: otherwise |a-b|<=2epsilon<1.
It satisfies |z-(b-a)|<=2epsilon and |z|<=L+2epsilon. There are at
most M possible such oriented lattice vectors, because their integer
coordinate vectors have norm at most K0(L+2epsilon). The angle between
z and b-a is at most delta. This follows by intersecting the disk of
radius 2epsilon about b-a with rays through zero, using |b-a|>=1.
Thus the oriented chord normal is within delta of one of at most M
fixed oriented normals for this carrier.

At every point p of the actual hull boundary, every outward supporting
normal n satisfies

    n dot p>=r,    |p|<=R,    angle(n,p)<=alpha.

On the short forward hull arc from a to b, all radial directions lie
in an interval of width eta. Its edge tangents therefore lie in the
corresponding rotated interval enlarged by alpha at each end. This
cone has width eta+2alpha<pi. The chord b-a is the sum of these
oriented edge vectors and belongs to the same cone. Consequently every
radial direction on that arc is within alpha+eta of the chord normal.
Together with the preceding lattice-vector estimate, the entire arc
lies in the union of at most M oriented radial intervals, each of width
2(delta+alpha+Delta).

For completeness, the canonical hull-normal proof in Section 3 of
[the hull-depletion report](target_c_fullcore_hull_train_depletion_floor_2026-10-04.md)
gives the radial boundary arclength density bound

    ds/dtheta<=R/cos(alpha).

It follows directly on every polygon side from the radial formula
rho(theta)=h/[n dot e_theta] and h>=r. Integrating over the above
interval union bounds its arclength by

    2M*R/cos(alpha)*(delta+alpha+Delta).

The forward arcs belonging to consecutive E_j vertices have disjoint
interiors, and chord length is at most its actual hull-arc length. Each
short chord has length at least one. Hence the last display bounds the
number of short edges retained. Add the one discarded edge and the
long-edge bound. A set of at most two points contributes at most two
instead. Summing over all J sets and adding B_bad proves (7.1).

For the asymptotic conclusion fix L first. Then M is bounded uniformly
over all the varying lattices; delta, alpha and Delta tend to zero,
and R/D stays bounded. Equation (7.1) gives

    limsup q/D<=J*pi/L.

Let L tend to infinity only after this limsup. This proves q/D->0
without assuming a rate for the canonical disk limit or for epsilon.

### Exact scope of the new bridge

The proof uses the actual loaded hull and all side lengths, not only
unit hull sides. It permits arbitrary gaps between consecutive loaded
points and arbitrary interleaving of different lattice labels. The
separate forward-arc argument avoids assuming that a carrier itself
contains the inner disk. Every source isolate remains retained.

This removes the infinitesimal positional relaxation of the bounded
lattice-cover subcase. It does not show that canonical coherent grains
transport loaded endpoints to within o(1) of boundedly many lattices.
An angular error of order 1/D accumulated over a macroscopic train can
give an order-one positional error. The canonical O(D) angular/face
banks do not imply that this accumulated error vanishes. A closing use
still requires control of actual endpoint transport, or a spendable
refill construction from its failure. Equation (7.1) is a proved
candidate, not promotion or closure of the full exhaustive branch.

## 8. Diameter-normal cones remove the disk hypothesis

There is a stronger version of Section 7. It controls actual diameter
edges rather than counting hull vertices and needs no disk limit.

Let A be any finite unit-separated planar source of diameter D>=2, let
H be its actual diameter graph, and B its diameter endpoints. Apart from
B_bad, partition B into J sets E_j whose points are within
epsilon<1/4 of affine lattices a_j+t_j Z^2 with
||t_j^(-1)||<=K0. For any L>=1 put

    delta=asin(2epsilon),
    delta_D=2asin(1/(2D)),
    M=[2K0(L+2epsilon)+1]^2.

Then

    |H|<=|B_bad|+2J*pi*D/L+J*(2M+2)
                         +2J*M*delta/delta_D.         (8.1)

Thus an unbounded sequence with fixed J,K0, epsilon=o(1), and
|B_bad|=o(D) has |H|=o(D). For a canonical C-II source this contradicts
h>=ceil(D), in either exhaustive branch. Section 7 remains a separate
stronger conclusion about the number q of loaded vertices under its
near-disk hypothesis. Section 8 supplies the branch-independent diameter
contradiction needed when that hypothesis is unavailable.

### Proof

Every actual diameter endpoint p is strictly exposed by its diameter
normal n=(p-q)/D. For any other source point x, expanding
|x-q|^2<=D^2=|p-q|^2 gives

    n dot (x-p)<=-|x-p|^2/(2D)<0.              (8.2)

In particular this normal belongs to the interior of the outward normal
cone at p in the polygon conv(E_j) whenever p belongs to E_j and
|E_j|>=3. All E_j points are hull-extreme, so they are the vertices of
that polygon.

For this polygon, call an edge short if its length is at most L. The
same lattice-vector calculation as in Section 7 shows that all oriented
outward normals of short edges belong to a union W_j of at most M
closed circular intervals of width 2delta. This remains true if the
lattice or its translate depends on the source. The number of longer
edges is at most per(conv(E_j))/L<=pi D/L. Hence at most 2pi D/L
vertices are incident to a long edge.

Consider a vertex incident to two short edges. Its outward normal cone
is the closed circular interval between the normals of those edges,
with angular length less than pi. If its cone is not wholly contained
in W_j, its interior contains a full connected component of the open
complement of W_j: both cone endpoints are in W_j. The interiors of
different vertex normal cones are disjoint. A complementary component
can therefore be assigned to at most one such vertex. There are at
most M complementary components, including when delta=0. Thus at
most M vertices with two short edges have cones not contained in W_j.
If W_j covers the full circle, there are no such vertices.

Declare all long-edge incident vertices and these gap-spanning vertices
bad. Sets with at most two vertices are declared entirely bad. Together
with B_bad, their total cardinality is bounded by

    |B_bad|+2J*pi*D/L+J*(M+2).                 (8.3)

At every remaining endpoint, (8.2) places each incident actual diameter
direction inside W_j. On the projective circle, these are at most M
intervals of width 2delta. Canonical
[Section 59, Lemma DB.3](../targets/target-c/59-difference-body-density-audit.md)
proves that distinct actual diameter directions in any unit-separated
source with D>=2 are separated by at least delta_D. Each such projective
interval therefore contains at most 1+2delta/delta_D directions. Across
all J carriers, the number of actual diameter edges having at least
one good endpoint is at most

    J*M*(1+2delta/delta_D).                  (8.4)

The remaining diameter edges have both endpoints in the bad set. Its
induced diameter graph has at most as many edges as vertices, by the
canonical planar diameter/Woodall bound. Equivalently, the forest or
odd-unicyclic diameter topology is preserved under induced deletion
and has edges at most vertices. Apply this to (8.3), and add (8.4),
to obtain (8.1). No source point is actually deleted in this argument.

For the asymptotic consequence, fix L first. M is uniformly bounded,
D*delta_D tends to one, and delta tends to zero. Thus

    limsup |H|/D<=2J*pi/L.

Letting L tend to infinity proves |H|/D->0. This order of limits
requires no rate for the vanishing lattice error.

### Composition and surviving obstruction

The new bridge uses the actual diameter normals, not artificial pinned
reactions. Consequently it applies in the macroscopic inactive-container
branch too, without dropping any isolates or applying the affine kernel
to their coordinates. A source theorem transporting all but o(D) loaded
endpoints to o(1)-accurate positions in boundedly many uniformly
conditioned lattices would now exclude both branches directly.

Neither the canonical coherent-grain theorem nor the harmonic-carrier
localization establishes this transport. Their errors can accumulate
over macroscopic contact paths, and the number of grains need not stay
bounded. Thus the branch-independent conditional exclusion does not
yet eliminate every canonical source. It converts the missing transport
statement into an exact finite contradiction, rather than treating
nonlattice endpoints as automatic packing surplus. The result is a
proved candidate awaiting independent audit.
