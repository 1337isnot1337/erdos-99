<!-- theorem-state: {"artifact_id":"ART-C6EC9700ED1D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: exact population exchange for near-triangular curved unit walls

Date: 2026-10-06. Authority: `35f5843ab9f5d11327d0f4cc803ed00707806ae7`,
state `2026-10-06.audit.65`. Classification: **proved candidate awaiting
independent audit** for the conditional source exclusion. No promotion,
universal chamber chart, C-II closure or Level I result is claimed.

The implication is

`actual curved unit wall + rounded finite population bound -> explicit
strict same-cardinality packet after selected wall vertices move -> full
source lower/upper safety -> contact loss -> canonical-source exclusion`.

This strengthens the previous curved-wall endpoint: the old interior
points may have arbitrary positions and arbitrary mutual contact graph.
Every interior source label is reassigned to an explicit new site. The
entire exterior source is retained, including every contact isolate.

## 1. Explicit wall and packet

Use the wall `F_theta` from
[the isolate-preserving construction](target_c_curved_unit_wall_isolate_preserving_inward_release_2026-10-06.md).
Fix `M>=4`, unit vectors `u,v` with

\[
u\cdot v=c\in(0,1/2),\qquad s=\sqrt{1-c^2},\qquad a_0=\sqrt3/2.
\]

On each of the four side bases `u,v,-u,-v`, the consecutive unit vectors
are `Rot((2j-M+1)theta)w`, `j=0,...,M-1`. Their transverse sums vanish.
The side chord is `Lw`, where `L=sum_j cos((2j-M+1)theta)`.
For sufficiently small positive `theta` this gives a strictly convex
closed unit wall with `4M` distinct source vertices and no nonconsecutive
unit pairs.

The previous analytic construction supplies simultaneously:

* a bank `B` of `4 floor((M-1)/3)` wall vertices, mutually more than two
  apart;
* a replacement root `x_b=q_b+3sin(theta)n_b` for each `b in B`, strictly
  inside the wall and strictly unit-clear of every other original wall
  vertex;
* `N=(M-1)^2` explicit interior sites
  \[
  z_{ij}=\frac L2(u+v)+\ell[(i-M/2)u+(j-M/2)v],
  \quad 1\le i,j\le M-1,
  \quad\ell=1+\frac{\tan(\theta/2)}{50M};
  \]
* strict mutual separation of those sites, strict separation from every
  original wall vertex and from every root, and strict root-root
  separation above two.

The two original wall contacts at a selected vertex open exactly to
`1+3sin(theta)^2` in squared length. The packet is proved analytically
for every fixed `M,c` at sufficiently small positive angle. There is no
assertion of a uniform angle threshold across sources.

## 2. Exact old-population bound

Impose the additional geometric condition

\[
\boxed{\operatorname{area}(F_\theta)<a_0(M^2+1).}\tag{1}
\]

Let an actual unit-separated source contain the complete wall, and let
`z` be its number of points strictly inside the wall. There are no
additional source points in the relative interior of a wall edge: each
edge has length one, so such a point would violate original separation
from an endpoint. Oler applied to the `4M+z` actual points in the closed
convex wall, whose perimeter is exactly `4M`, gives

\[
4M+z\le\frac{\operatorname{area}(F_\theta)}{a_0}+2M+1
<M^2+2M+2=(M+1)^2+1.
\]

The count is an integer. Hence

\[
\boxed{z\le(M-1)^2=N.}\tag{2}
\]

This uses area for an upper bound on the actual old population. The
replacement capacity is furnished separately by the explicit packet in
Section 1. No positive area, residual or leading density is treated as
an unproved packing site.

## 3. Finite full-source exchange

Delete the `z` old interior points and the selected wall vertices `B`.
Assign every deleted interior label to a distinct one of the `N` sites;
assign the deleted wall labels to their roots. This is possible by (2),
and it inserts exactly `z+|B|` points. All other source points remain at
their original coordinates.

For each inserted interior site, the complete original wall is strictly
unit-clear. The canonical embedded-wall shield therefore makes it
strictly unit-clear from every old exterior source point. For a root,
the canonical one-deleted-vertex convex-wall shield applies with its own
old vertex as the missing guard: all other original wall vertices are
strictly clear. The theorem can be applied separately to each root
against every retained exterior point. The analytic packet proves every
new-new pair condition. Thus the entire full-source lower system holds
and no unit contact is created.

All inserted points lie strictly inside the old wall, hence strictly
inside the full source hull. Every pair involving an inserted point is
therefore strictly shorter than the old actual diameter `D`. Every
remaining old-old pair is unchanged. These statements include all
inactive upper pairs and all pairs involving retained contact isolates.
No local chart or upper-exception discard is needed.

At least the `2|B|` distinct original wall contacts incident with `B`
are lost. Any additional contacts incident with the deleted points are
lost as well. The retained old contact graph is induced from the old
triangle-free graph, and every inserted point is contact-isolated, so
the new source is triangle-free. Its cardinality is unchanged.

If its diameter is below `D`, global minimality fails. If its diameter
is `D`, contact-minimality among triangle-free global minimizers fails.
Consequently:

\[
\boxed{\text{No canonical triangle-free source contains a wall of
Section 1 satisfying (1).}}\tag{3}
\]

The old interior cloud is not assumed to be the explicit lattice cloud,
close to it, sparse, contact-free or free of a blocking collar. It is
replaced in full. This closes that particular collar obstruction rather
than attempting to add its count to another defect bank.

## 4. Nonempty family of arbitrarily large excluded chambers

At `theta=0`, the wall limits to the parallelogram with area `M^2 s`.
For each fixed `M`, choose `c<1/2` sufficiently close to `1/2` that

\[
M^2s<a_0(M^2+1).
\]

Continuity preserves (1) for sufficiently small positive `theta`.
Intersect this interval with the finite strict packet interval in
Section 1. Both are open intervals starting at zero, so their
intersection is nonempty. The chamber area is of order `M^2`, and all
its allowed old populations are covered by (3).

One explicit rational choice of the oblique unit basis is obtained by
putting `Q=10^6 M^4`,
`p=floor(sqrt(floor(Q^2/3)))+1` and `T=p/Q`. Then `T>1/sqrt3`,
`T-1/sqrt3<=1/Q`, and

\[
c=\frac{1-T^2}{1+T^2}\in(0,1/2),\qquad
s=\frac{2T}{1+T^2}.
\]

The derivative bound `|dc/dT|<=2` gives `1/2-c<=2/Q`. Also

\[
0<s-a_0=\frac{(1/2-c)(1/2+c)}{s+a_0}<1/2-c.
\]

Hence `M^2(s-a_0)<2/(10^6 M^2)<a_0`. This proves the required
strict area inequality at zero; a positive allowable curvature then
exists. The exact finite verifier uses rational positive curvatures
and checks the area and all packet distances directly.

## 5. Hostile scope checks and next obligation

This theorem does not reopen the fixed-wall large-grid lock. Its
replacement roots delete actual wall guard vertices and open their old
contacts. The strict curvature supplies room for the explicit expanded
interior packet. Flat locked walls do not satisfy the same packet
construction. The one- and two-wall exterior-shield distinction is
retained: each root passes its individual full original-wall guard test.

The global eight-point heptagon regression is also respected. Its wall
is not in this geometric family and supplies neither the required
population bound with this explicit packet nor these root clearances.
The theorem uses the exact old cardinality, not a packing density limit.

An arbitrary canonical macroscopic chamber is not proved to have four
side direction families, this curvature pattern, this near-triangular
area bound, or a packet of the certified cardinality. The next
strengthened statement must either extract an actual chamber in the
excluded class or certify a different strict packet meeting its full
old population. Full-core face-coupled finite motion remains separate.

## 6. Exact certificate

`research/verify_target_c_curved_wall_exact_capacity_2026_10_06.py`
builds four rational instances with `M=4,6,8,12`, near-triangular unit
bases and positive curvature. It checks all old/new source pair distances,
unit wall perimeter, strict convexity and containment, selected-wall
contact loss and every pair involving a moved point against the actual
old diameter. It independently computes polygon area by the shoelace
formula and checks (1) by squaring positive rational quantities. It
checks the count/contact/cardinality ledgers for every integer old
population from zero through `(M-1)^2`.

The verifier certifies its finite rational packets and rounding ledgers.
Oler, the universal exterior shields and the every-fixed-`M` continuity
argument are analytic inputs. No arbitrary source coordinates, global
optimality or universal chamber classification are enumerated.
