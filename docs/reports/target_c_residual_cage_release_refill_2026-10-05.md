<!-- theorem-state: {"artifact_id":"ART-B3EB83949D93","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — finite residual-cage deletion and strict refill

Date: 2026-10-05. Research base: `3c94a1a93641a5f8fa24d43068d487594d3e38cd`.
Controlling state: `2026-10-05.audit.57`.
Owned branch: `research/target-c-residual-closure-20261005`.
Classification: **proved candidate awaiting independent audit and promotion**;
registry classification remains **unreviewed**. Level I and C-II remain open.
External literature: not used. This finite proof uses no computation.

## 1. Endpoint and dependencies

```
certified strict packet surplus >= a residual-cage vertex transversal
-> shorten surviving active diameters on the exact contact manifold
-> delete the transversal and replace explicitly counted packet interiors
-> same-cardinality strict sub-D competitor
-> exclude every canonical source supplying those packets.
```

The dependencies actually used are canonical `C-CONTACT-DIAMETER-COORDINATES`
([report](target_c_contact_manifold_local_diameter_coordinates_2026-10-05.md),
[finite-scope audit](../audits/target_c_local_diameter_coordinates_promotion_audit_2026-10-05.md)),
`C-CONTACT-FACE-REGULARITY`
([report](target_c_complete_face_elimination_and_contact_regularity_2026-10-05.md)),
and `C-EMBEDDED-WALL-REFILL`, Sections 2–3
([report](target_c_embedded_grain_wall_replacement_2026-10-02.md)).
The §57 core scope is retained. The graph corollaries use canonical `C-WOODALL`
([report](target_c_woodall_diameter_topology_2026-09-10.md)).
No return, phase, residual, or flower currency is assumed to be packing capacity.

## 2. Exact finite packet theorem

Let A be a canonical C-II source in the audit.56 regime, with diameter D,
nonisolated core V, and all actual active diameter edges H on V. Let M be the
smooth exact contact manifold modulo core Euclidean motions, with tangent
space T at the source and dimension m. Choose a smooth local section in
labelled core coordinates. All source labels outside V stay fixed.

Let B be any row basis of the active diameter differential G, and put
R=H\B. Let U be a vertex cover of R, chosen among its incident vertices.
Let C_1,...,C_a be actual simple unit-contact walls with disjoint polygon
interiors. Write S_i=A intersect int(C_i), S=union S_i, and let
Y_i subset W_(C_i) be finite unit-separated packet sets, of sizes M_i.
Assume

    sum_i M_i >= |S| + |U|.                            (1)

Then a unit-separated configuration of cardinality |A| and diameter
strictly less than D exists.

This is a finite conditional theorem: the packet sets are an explicit
hypothesis. It proves their spendability, not their existence.

### Proof: prepare one finite packet with positive margins

Independently dilate each finite Y_i by a factor just above one about a
fixed center. Since Y_i is a finite subset of the open W_(C_i), the dilation
can be small enough to stay in W_(C_i). Its internal pair distances become
strictly greater than one. The canonical wall shield gives strict clearance
from every old point outside int(C_i). The disjoint-wall shield gives strict
cross-packet clearance. Thus, writing Y=union Y_i, every distinct pair in Y,
and every pair consisting of y in Y and x in A\S, is strictly unit-clear.

Every y is in int(conv A): int(C_i) is an open subset of conv A. For each
x in conv A, |y-x|<D. Otherwise |y-x|=D and moving y slightly farther from
x within conv A would contradict diam(conv A)=D. This argument also handles
all new-new upper bounds. Finiteness gives strictly positive lower and upper
margins simultaneously. If one family of pairs is empty, omit that family
from the minimum rather than assigning it an undefined margin.

Every vertex of U is an actual diameter endpoint and hence an extreme
point of conv A. No such point lies in an open wall interior. Consequently
U and S are disjoint. Retain exactly |S|+|U| points from Y; inequality (1)
allows this, and taking a subset preserves every certified margin.

### Proof: move before deleting

For m>0, the canonical inverse-function chart realizes all sufficiently
small y=(-t,...,-t), t>0, as exact basis excesses

    (|p'_i-p'_j|^2-D^2)/2 = -t,   ij in B.

Choose t small enough that the labelled section displacement is within
all finite pair-margin neighborhoods just prepared. All original core
contacts remain exactly unit. Every retained contact isolate is fixed.
All originally inactive lower constraints remain >1, and all originally
inactive upper constraints remain <D. The only active upper constraints
not already strictly shortened are in R.

Keep the inserted sites at their original strictified positions Y. Their
new-old lower and upper margins persist by continuity as old labels move;
the new-new margins are unchanged. There is no need to transport an
inserted lattice or to assume the moved source hull equals the old hull.

Delete the moved labels in U union S and insert the selected |U|+|S|
fixed sites. Every edge in R loses an endpoint because U covers R. Every
surviving edge of H belongs to B and was strictly shortened. Every other
surviving old-old pair had inactive upper slack and remains <D. Every pair
involving an inserted site is <D by the finite-margin choice. Lower
constraints are at least one, by exact contact preservation, inactive
slack, and the strict packet margins. Finitely many strict upper bounds
give a global diameter <D. Cardinality is unchanged. This contradicts
minimum diameter.

For m=0, B is empty and R=H. Keep all old points stationary, delete the
cover and S, and use the same strict packet. The preceding pair audit
applies directly. A nonzero coordinate vector is neither available nor
needed in this case. QED.

### Moving walls, deleted wall vertices, and hull contact

The proof uses walls to certify margins at the original source. Deleting
a vertex of U which lies on a wall cannot reduce a previously certified
pair margin. The wall may be kept as a ghost polygon after deletion; the
final configuration need not have that polygon as a contact wall.

If pre-deletion containment is desired, choose the local displacement
smaller still. Nonadjacent segments of each original simple polygon have
positive distance, adjacent unit edges have nonzero angle, and each finite
packet point has positive distance from the polygon boundary. These finite
conditions preserve simplicity and packet winding number in the moved
walls. All original interior population labels likewise have positive
distance from their wall boundary. None of these conditions is needed
after deletion, since pair margins already prove feasibility.

A wall may share vertices or edges with the original hull boundary. Its
packet sites are nevertheless strictly inside the two-dimensional old
hull. Their upper margins against every old source label are positive,
including labels on other hull arcs and fixed contact isolates. No uniform
asymptotic margin or chart radius is asserted. Each finite source chooses
its own t after all packet margins are fixed.

Isolates in S are explicitly deleted and replaced in the cardinality
identity. Every isolate outside S stays fixed. There is no omission of an
isolate from global separation or upper-bound checks.

## 3. Exact cage cost and a stronger direct formulation

The canonical identity gives |R|=s_Z+1. Therefore the sufficient surplus
in (1) can be reduced from a cover of H to

    tau(H\B) <= |H\B| = s_Z+1.

Define

    tau_*(H,G) = min over row bases B of tau(H\B).

More directly, for U subset of loaded vertices write H_U for the edges
with neither endpoint in U, and define

    kappa(H,G) = min |U| such that there is u in T with
                 g_e(u)<0 for every e in H_U.          (2)

An empty H_U makes the condition vacuous, and u=0 is then allowed.
The finite packet theorem holds with any U satisfying (2): take a smooth
contact-chart path with derivative u. The finitely many strict negative
first derivatives shorten all surviving active diameters for sufficiently
small positive time. Repeat exactly the margin and refill proof above.

For nonempty H_U, condition (2) is equivalent to

    0 not in conv{g_e:e in H_U}.                        (3)

If zero is in that convex hull, its nonnegative weighted relation excludes
strict negative evaluation. Conversely, the compact convex hull has a
nearest point z to zero when zero is outside. With any inner product on
T*, nearest-point minimality gives <z,g_e> >= ||z||^2>0 for each surviving
row; the tangent vector dual to -z evaluates all those rows negatively.
This proves the separation statement directly without importing an
external theorem.

A positive circuit means a minimal nonempty row support admitting a
nonnegative nonzero dependence, including a singleton zero row. Every
nonnegative dependence contains a minimal support by finiteness. Thus U
satisfies (2) exactly when its incident diameter edges hit every positive
circuit. In particular,

    kappa(H,G) <= tau_*(H,G) <= s_Z+1.                  (4)

Indeed deleting a cover of H\B leaves only a subset of the independent
basis rows. Such a subset admits simultaneous negative evaluation. The
empty subset is handled as above.

Merely destroying *positive spanning of the whole tangent dual* is too
weak. Zero must leave the surviving covector convex hull altogether;
placing zero on its boundary still obstructs strict shortening. Section 4
below records an exact finite regression.

## 4. What Woodall topology alone can and cannot pay

For each R which is a forest, leaf induction gives tau(R)=nu(R). If R
contains the odd cycle of the Woodall graph, deleting one cycle vertex
and covering the remaining forest gives tau(R)<=nu(R)+1. These bounds
can improve a particular residual-edge cover, but topology alone does not
improve the universal bound s_Z+1.

For an exact abstract regression, take H to be 2r disjoint edges on 4r
vertices, and give its rows in R^r the values +e_j,-e_j, j=1,...,r.
Then rank G=r, all 2r KKT row weights can be equal and positive, and zero
is in the interior of the row convex hull. Put

    q=4r, h=2r, d_H=2r, s_Z=r-1, k=3r-1.

The exact identities m=q-k-1=r and h-m=s_Z+1=r hold. H is a Woodall-type
forest with exactly d_H caterpillar components. Every basis chooses one
row from each opposing pair. Its r residual edges are disjoint, so

    tau_*=r=s_Z+1.

To strictly shorten all surviving rows one must delete at least one edge
from each opposing pair. Each source vertex is incident to just one edge,
so kappa=r also. This is an abstract covector/topology regression, not a
plane embedding, contact framework, canonical source, or global minimizer.
It refutes an improvement from only topology, rank, positivity, and the
listed exact ledger identities. Geometry or additional canonical
structure would be required to beat (4).

For the weaker positive-spanning criterion, use rows +/-e_1,+/-e_2 and
delete +e_2. The surviving rows do not positively span R^2, yet the pair
+/-e_1 still prevents a strict negative direction. This shows precisely
why positive-circuit hitting, rather than loss of full positive spanning,
is the correct direct cage criterion.

## 5. Branch scope and audit.57

This proof is local on the canonical nonisolated core, with global pair
margins checked against the full source. It does not assume full-core
Type II, no container, no isolates, or s_Z=o(D). Consequently the same
conditional release theorem applies to the macroscopic-container branch
whenever its actual packets satisfy (1). The existence of a macroscopic
container is not the existence of a packet.

The canonical short-wall theorem remains binding: all terminal pentagons
have empty W_C, so none meets (1) with a positive surplus. Their contact-
preserving motion cannot change that fact. The large-wall lock regression
also remains binding. No residual-to-capacity implication is made here.

The next exact closing obligation is a source-specific construction of
simultaneously strict packets with aggregate surplus at least kappa(H,G),
or a nonlocal replacement that achieves the same cardinality and pair
inequalities without such packets. The audit.55 currencies by themselves
are neither sites nor a proof of this inequality.

## 6. Classification and promotion

| Claim | Classification | Scope |
| --- | --- | --- |
| Residual-cover release/refill | Proved candidate awaiting promotion | Finite canonical chart plus actual packets |
| Positive-circuit transversal formulation | Proved candidate awaiting promotion | Finite covectors and exact chart |
| Sharp topology-only cost regression | Regression, unreviewed artifact | Abstract matching and covectors |
| Loss of positive spanning suffices | Rejected formulation | Opposing-row regression |
| Packet existence from linear currency | Unproved | No claim of closure |

Independent audit is required before promotion. No authoritative state,
route, or prompt is changed by this report. The proof neither closes
full-core nor macroscopic-container, and does not settle Level I.
