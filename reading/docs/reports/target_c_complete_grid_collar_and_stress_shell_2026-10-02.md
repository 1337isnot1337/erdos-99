> Generated reading edition · [exact source](../../../docs/reports/target_c_complete_grid_collar_and_stress_shell_2026-10-02.md) · source SHA-256 `12d7a99aad408105f0e7f855b560b10d5a383dbcd55dada35f199107aa3566ee`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-76D1DB01C786","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: complete-grid collar matching and a genuine stress-shell regression

```text
complete unit grid -> matching collar and O(sqrt(D)) directly attached
diameter endpoints -> most loaded endpoints are macroscopically exterior;
weak mass >1/3 -> Omega(D^2) bad stress on exterior--exterior contacts.
An actual dense KKT/PSD stress shell rejects automatic o(D^2) exterior stress.
The missing step is a global-optimality restriction or a strict source competitor.
```

**Date:** 2026-10-02.  
**Starting checkout:** `539f5187b3cac9287f6b30cdf6b36aafb1763c5a`.  
**Research base:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.  
**Continuation main:** `3bad7c12` (PRs #622 and #623 inspected at exact scope).  
**State:** `2026-09-14.audit.51`, unchanged from the research base.  
**Branch:** `swarm/sol/threshold-global-moment-20261002`.  
**Classification:** proved candidates awaiting audit/promotion; conditional
weak-packet application; proved nonglobal regression. Artifact lifecycle unreviewed.
**Level I OPEN; C-I CLOSED; C-II OPEN.**

## 1. Scope and dependencies

This continues the [axial pressure report](target_c_weak_pivot_axial_pressure_2026-10-02.md).
The new grid and shell statements are finite source statements or explicit
nonoptimal constructions. They do not assume a source-specific stress kernel
on contact-isolated points. Canonical inputs are [Theory 01](../theory/01-local-structure.md),
Theorem 4.1 and Lemma 5.1, and the translated triangular-lattice counting
comparison in [the full-source geometry audit](../targets/target-c/58-full-source-geometry-audit.md).
The endpoint strip proof is rederived in the pressure report, Section 4.

PR #623's now-merged [ball-hull report](target_c_diameter_ball_hull_lattice_discrepancy_2026-10-02.md)
was inspected at BH.3--BH.6. Its two-port lattice alphabet is prior work;
the needed alphabet is rederived below for the larger interval `|u.v|<1/2`.
The new information is the occupancy of **every point in the coordinate
rectangle**, which excludes its off-chart two-port intersections. No Fourier
estimate or infinite-chart discrepancy bound is used. PR #613's
[row/cap report](target_c_threshold_rail_deep_attachment_2026-10-02.md), including
its one-contact row lemma, is acknowledged. The exterior rectangle bound here
concerns distance to the entire grid hull, not individual assigned row markers.

Application of the weak stress charge in Section 5 uses the earlier
[weak-packet tensor theorem](target_c_weak_packet_correction_mass_2026-10-02.md),
with its explicit unpromoted October threshold dependencies. No result below
promotes those extractions or closes any other C-II source branch.

## 2. An outside point has at most one grid contact

Let a triangle-free unit-separated source contain all the points

$$
\mathcal G=\{p_{00}+iu+jv:0\le i\le a,\ 0\le j\le b\},
\quad |u|=|v|=1,\quad |u\cdot v|<1/2,
\tag{G}
$$

with integer `a,b>=2`.

### Theorem G1

Every source point outside `G` has at most one unit contact into `G`.

Proof. Reverse one basis vector and translate the rectangle if needed to
take `c=u.v in [0,1/2)`. Suppose `p` has two distinct grid neighbors.
Translate one neighbor to zero and write the other as `w=iu+jv`.
The circles can intersect only if `|w|<=2`. The Gram bound gives
`i^2+j^2<=8`. Up to simultaneous sign and exchange of the basis vectors,
the possible differences are

$$
u,\ v,\ u+v,\ u-v,\ 2u,\ 2v,\ 2u-v,\ u-2v. \tag{12}
$$

For completeness, the two mixed vectors of type `(2,1)` have squared
length `5+4c>4`; `(2,-2)` has square `8-8c>4`; and all other vectors in
the integer disk either have these types or are in (12). The last two
listed differences are available only for `c>=1/4`.

The unit differences `u,v` would make a unit triangle, so are excluded.
For `u+v`, the two circle intersections are precisely `u,v`; for `u-v`
they are `u,-v`. For `2u,2v`, the only intersection is the midpoint.
Each corresponding lattice point has coordinates between the two neighbors'
coordinates, so is already occupied in the complete rectangle. It cannot be
a distinct source point outside `G`.

For `w=2u-v`, put `L=|w|^2=5-4c`, so `3<L<=4`. A circle intersection
has form `p=w/2+z`, with `z perpendicular w` and `|z|^2=1-L/4`.
The grid points `u,u-v` are `w/2+/-v/2`, and are both occupied in the
coordinate rectangle. At least one is at squared distance

$$
\min\{|z-v/2|^2,|z+v/2|^2\}
\le |z|^2+1/4=c<1/2<1.
$$

Neither candidate can equal `p`, since its squared distance to the other
port is `2-2c>1`. Unit separation is contradicted. The `u-2v` case is
identical with occupied candidates `-v,u-v`. Simultaneous reversal and
basis exchange preserve coordinate-rectangle occupancy. This proves G1.
It does not assert one-port continuation into the chart.

### Theorem G2 — the noncorner interface is a matching

After removing grid's four corner vertices, the contacts between `G` and
its exterior form a matching.

Proof. G1 bounds every exterior vertex's grid degree by one. Interior grid
vertices have four unit neighbors and no room for another, as proved in
the pressure report. A noncorner boundary vertex has two opposite unit
neighbors along its side and one inward grid neighbor. The two angular
gaps on the inward side are below `2pi/3`; no further unit neighbor fits
there. A neighbor on the outward side must lie more than `pi/3` from
each of the two side directions: equality would create a unit triangle.
The remaining open angular arc has length `pi/3`, and cannot contain two
unit neighbors with mutual angular separation greater than `pi/3`.
Thus at most one exterior neighbor exists. QED.

## 3. Matching-port stresses are controlled by the interior grid

Consider any normalized actual KKT stress. Use the pressure report's
interior row stresses `g_j` and interior column stresses `h_i`, and put

$$
G_u=\sum_{j=1}^{b-1}g_j,\qquad
G_v=\sum_{i=1}^{a-1}h_i,\qquad s=|u\times v|.
$$

### Theorem G3

The sum `I_nc` of contact coefficients on all noncorner grid/exterior
ports satisfies

$$
\boxed{I_{\rm nc}\le {4s\over\sqrt3}(G_u+G_v),
\qquad aG_u+bG_v\le D^2.} \tag{13}
$$

At a bottom noncorner vertex, projection of equilibrium perpendicular to
`u` gives `alpha_port |w.Ju|=h_i s`. The outward port makes an angle
between `pi/3` and `2pi/3` with the side direction, so `|w.Ju|>=sqrt3/2`.
The vertex cannot carry a diameter load: it is a convex combination of
the side's grid corners and hence is not an extreme source point. If
`h_i>0`, the projection equation forces the port to exist. In either case
its coefficient is at most `2s h_i/sqrt3`. The top side has the same
bound; the left and right sides have bounds `2s g_j/sqrt3`. Summing
proves the first inequality. There are `a` actual u edges for every
internal row and `b` actual v edges for every internal column; the two
edge sets are disjoint. The actual trace `sum alpha=D^2` proves the second.

Every source contact coefficient satisfies `alpha_e<=D`, by the genuine
perpendicular-bisector cut argument in the weak-packet report, Section 5.
A triangle-free contact star has at most five neighbors, since consecutive
angular gaps exceed `pi/3`. A grid corner already has two grid neighbors,
so its at most three exterior contacts add at most `3D`. Consequently
the **entire** interface coefficient mass satisfies

$$
\boxed{I\le {4s\over\sqrt3}(G_u+G_v)+12D
\le {4sD^2\over\sqrt3\min(a,b)}+12D.} \tag{14}
$$

For a complete grid of linear side lengths, `I=O(D)`, without any
individual positive multiplier floor. If both grid sums are `o(D)`,
all but the four corner ports have aggregate stress `o(D)`. This is an
upper bound on transmission, not a lower bound on load entering the grid.

## 4. Direct endpoint attachments have only square-root capacity

### Theorem G4

For every `d>=0`, the number of actual diameter endpoints at distance at
most `d` from `conv(G)` is at most

$$
\boxed{16\sqrt{2Dd}+16d+20.} \tag{15}
$$

Proof. An actual diameter endpoint is extreme in the full source hull.
Any such endpoint in `conv(G)` must be one of its four corners, since all
four corners are actual source points. Any other endpoint is outside that
parallelogram. If its distance from the parallelogram is at most `d`, it
violates at least one facet inequality by perpendicular distance between
zero and `d`: projection onto any violated outward normal is bounded by
its distance to any point of the parallelogram. It belongs to one of the
four outward strips of width `d`. The endpoint strip theorem bounds each
strip by `4sqrt(2Dd)+4d+4`. Add four possible corners.

In particular, at most `16sqrt(2D)+36` actual diameter endpoints can have
even one grid contact. This bound covers endpoints with additional exterior
contacts; it is not a degree-one leaf theorem or an infinite-chart bound.

For any `b_0>=64` actual diameter endpoints, put

$$
d_*={b_0^2\over16384(D+b_0)}.
$$

More than `b_0/2` have distance greater than `d_*` from the entire grid
hull. Indeed (15) at `d_*` is at most
`(sqrt2/8+1/1024)b_0+20<b_0/2`; use `sqrt2<17/12` and `b_0>=64`.
If `b_0>=cD`, these are macroscopic distances `Omega(D)`.
Any corresponding unit-contact path from a grid vertex has at least this
many edges. Sums of those path lengths are not distinct-edge counts: paths
can overlap. Nothing here creates an atlas for all outside grains.

## 5. Weak packets force genuine exterior--exterior stress

Suppose the conditional weak-packet tensor theorem applies, with normalized
weak mass `M>=1/3+delta`, `delta>0`, and projective shore angle
`pi/3+O(1/D)`. Call a contact bad if its projective direction is farther
than `epsilon_D` from both grid directions, where `epsilon_D -> 0`.
That theorem gives

$$
\sum_{e\ {\rm bad}}\alpha_e\ge(\delta-o(1))D^2. \tag{16}
$$

For an actual complete grid with `a,b>=cD`, every internal contact is in
one of its two unit directions; the port coefficients sum to `O(D)` by
(14). Therefore

$$
\boxed{
\sum_{\substack{e\ {\rm bad}\\
\text{both endpoints outside }\mathcal G}}\alpha_e
\ge(\delta-o(1))D^2.} \tag{17}
$$

There are at least `(delta-o(1))D` such actual exterior contacts, by
`alpha_e<=D`. This is a weighted exterior obstruction, not an assertion
of quadratic bad-contact population. The latter would lose exactly the
boundary stress concentration described next.

## 6. Hostile test: actual KKT allows a fully exterior stress shell

The next proposed closure was to show that near-disk geometry, leading
optimal density, a large actual complete grid and positive actual KKT
equilibrium force the left side of (17) to be `o(D^2)`. That is false.

### Theorem R — dense, triangle-free, actual KKT shells with strict competitors

For every sufficiently large odd integer `N_s`, there is a unit-separated
triangle-free source `P` of diameter `D`, with

$$
|P|={\pi D^2\over2\sqrt3}+O(D),\qquad
R(P)=D/2+O(D^{-1}),
$$

containing a complete actual unit grid with both sides `Omega(D)`, whose
actual normalized KKT stress has **all** contact stress on an exterior
unit cycle. Its shell stress matrix is PSD with kernel dimension three.
Relative to the grid directions, exterior bad-contact stress is
`(1-o(1))D^2`. A separate counting theorem gives a same-cardinality
unit-separated competitor of diameter at most `D-1`. Thus these sources
are proved nonglobal, not potential disproofs of Level I.

Proof. Take a regular odd `N_s`-gon of side length one, with

$$
t={\pi\over2N_s},\quad
R={1\over2\sin(2t)},\quad
D=2R\cos t={1\over2\sin t}.
\tag{18}
$$

Its contacts are exactly its cyclic sides. Its actual diameter edges join
index `j` to `j+(N_s-1)/2`; they form one odd cycle, because the step and
`N_s` are coprime. Put `beta=1/N_s` on each of these actual diameter
edges and `alpha=D^2/N_s` on each shell unit edge.

At each vertex `p_j`, the contact sum is
`4alpha sin^2(2t) p_j`; the diameter sum is
`4beta cos^2(t) p_j`. They agree by (18). Every coefficient is positive
on the shell; `sum beta=1` and `sum alpha=D^2` hold exactly.

Take `u=(1,0)` and `v` at angle `pi/3+1/D`. Inside radius `R-4`, retain
every point of one translate of `Zu+Zv`. For large `D`, the lattice's
only shortest nonzero vectors are `+/-u,+/-v`, and its unit-contact graph
is a subgraph of the square grid, hence triangle-free. Shell/core distances
are at least four; core/core distances are at most `2R-8<D` and cross
distances at most `2R-4<D`. The actual diameters therefore remain exactly
the shell cycle. Set every interior contact coefficient to zero. This is
a genuine full-source vertex KKT stress, not a formal contact substitution.
A central rectangle of linear side lengths lies inside radius `R-4`.

The centered lattice cells have area `s=sin(pi/3+1/D)` and radius at most
one. Their union gives the two elementary counting bounds

$$
{\pi(R-5)^2\over s}\le N_{\rm core}
\le {\pi(R-3)^2\over s},
$$

so the stated leading population follows, since `s=sqrt3/2+O(1/D)`.

The shell stress matrix has Fourier eigenvalues

$$
\lambda_k={4\over N_s}
\left(D^2\sin^2{\pi k\over N_s}
-\sin^2{\pi hk\over N_s}\right),
\quad h=(N_s-1)/2.
\tag{19}
$$

They vanish for `k=0,1,N_s-1`. For other modes,
`sin^2(pi k/N_s)>=sin^2(2pi/N_s)` and
`D^2sin^2(2pi/N_s)=4cos^2(t)cos^2(2t)>3/2` for `N_s>=5`.
The subtracted sine square is at most one, so these eigenvalues are
strictly positive. Extending by zero to the core adds kernel directions;
no full-source three-dimensional kernel is claimed.

The `N_s` shell contact directions are equally spaced on the projective
circle. At most `4epsilon N_s/pi+4` lie within `epsilon` of the two grid
directions. Each edge carries `D^2/N_s`; all shell vertices are outside
the grid. Taking `epsilon -> 0` proves the exterior bad-stress claim.

Finally, this is not just an unclassified numerical survivor. Let
`a_0=sqrt3/2`. From (18), `N_s<pi D` and
`R^2-D^2/4=1/(16cos^2t)<1/8`, whence `R<D/2+1/(8D)`.
For `D>=10`, the weaker upper cell bound gives

$$
|P|< {\pi\over a_0}(D^2/4-2D+5)+\pi D
< {\pi(D-1)^2\over4a_0}. \tag{20}
$$

The last difference is at least
`pi[(3/(2a_0)-1)D-19/(4a_0)]>0` for `D>=10`.
Average translations of the triangular lattice inside a disk of diameter
`D-1`. Its expected point count is the last quantity in (20), exceeding
the integer `|P|`; some translate contains at least that many points.
Selecting `|P|` of them is the promised strict competitor. QED.

The source with its actual unit grid omits the canonical contact-minimal
normalization `C=C_*`: the core contacts have universally zero stress since
their components have no diameter load. It also omits the weak-pivot train
extraction. It therefore rejects the stated geometric/KKT shortcut, not
(17) or a source closing theorem with those additional hypotheses.

There is a separate version with **all** actual contacts positively stressed:
scale the interior lattice by `1+D^-2`, keep only its points in radius
`R-4`, and use the same shell. All core points are contact-isolated, and
the same population, radius, actual KKT, PSD-on-positive-core and strict
competitor proofs hold. This version has no actual unit grid. The two
versions must not be combined into a fictitious source with both properties.
It records why contact-isolated points cannot be discarded in the inactive
container branch.

## 7. Certificates and remaining source obligation

No companion `verify_complete_grid_collar_2026_10_02.py` exists in the source
branch, despite the verifier path named in its initial draft. The current-main
ball-hull and full-source midpoint verifiers cover adjacent inputs only; they do
not certify Theorems G1--G4 or R. The integer-difference enumeration, distance
bounds, population estimates, spectral positivity, and strict competitor remain
analytic proof claims in this unreviewed report. No executable certificate for
those claims is asserted here.

The new bridge localizes a weak-dominated source's unavoidable stress to
contacts whose two endpoints are outside the actual grid, and places almost
all loaded rail endpoints macroscopically away from the grid hull. The hostile
shell test shows why actual KKT, PSD on the positive-contact core and leading
density do not automatically bound that exterior stress. A proof must use
global optimality, source contact-minimality/rigidity and actual exterior
population or produce a finite same-cardinality competitor. A count of
shared paths or a replacement of tiny positive stress by zero cannot do it.

No threshold branch is entirely excluded here. Boundary weak pivots,
no-weak-packet sources, open-cell exact phase, nonconstant phase, split-star,
inactive interfaces, macroscopic containers/exterior caps and the other
full-core branches remain accounted for and open. There is no Level I claim
or theorem-state promotion.
