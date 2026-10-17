> Generated reading edition · [exact source](../../../docs/audits/target_c_uneven_wall_packet_independent_audit_2026-10-06.md) · source SHA-256 `473f56d4ea54a53950cc79ecaf7466125a017162dbb006eb55ee8357adb913cd`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-885E0DDD5FE9","canonical":true,"claim_ids":["C-UNEVEN-CURVED-WALL-EXACT-CAPACITY-EXCLUSION","C-UNEVEN-WALL-CORNER-ROOT-REGRESSION","C-UNEVEN-WALL-GREEN-MIDDLE-MARGIN"],"claim_statuses":{"C-UNEVEN-CURVED-WALL-EXACT-CAPACITY-EXCLUSION":"canonical","C-UNEVEN-WALL-CORNER-ROOT-REGRESSION":"regression","C-UNEVEN-WALL-GREEN-MIDDLE-MARGIN":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent promotion audit — uneven convex-wall packet

**Date:** 2026-10-06
**Audit base:** `b0fa38a495028ccf446df98f2f0a5650b1a376bc` (`2026-10-06.audit.68`)
**Audited source snapshot:** `research/sol/target-c-owner-order-closure-20261006` at
`d7395e799fa26505c5b9da06a16d9043d101ce5b`
**Candidate:** `docs/reports/target_c_uneven_convex_wall_bending_and_exact_packet_2026-10-06.md`
**Verdict:** PASS for the Green middle-bank margin and the exact conditional packet exchange; REGRESSION VALID for the corner-adjacent root failure.
**Frontier effect:** excludes an expanded explicit chamber class but supplies no extraction from an arbitrary canonical source. C-II and Level I remain open.

## Exact promoted statements

### C-UNEVEN-WALL-GREEN-MIDDLE-MARGIN — PASS

Let `M>=8` and let
`a_0<a_1<...<a_(M-1)` satisfy `a_j=-a_(M-1-j)`. Put
`d_i=a_i-a_(i-1)>0`, `B_0=B_M=0`, and
`B_i=-sum_(j=0)^(i-1) a_j` for `1<=i<M`. Then

`2B_i-B_(i-1)-B_(i+1)=d_i`.

The inverse Dirichlet Green kernel is

`G_ij=min(i,j)*(M-max(i,j))/M`,

so `B_i=sum_j G_ij d_j >= G_ii d_i = i(M-i)d_i/M`. For
`3<=i<=M-3`,
`i(M-i)/M >= 3(M-3)/M = 3-9/M >= 15/8 > 3/2`.
Therefore `B_i>3d_i/2` throughout the selected middle bank. The argument
uses positivity of every profile increment; it does not require uniform
curvature or a return-path/defect charge.

### C-UNEVEN-CURVED-WALL-EXACT-CAPACITY-EXCLUSION — PASS

Fix `M>=8`, `u dot v=c in (0,1/2)`, and any two fixed strictly increasing
antisymmetric profiles `a_j` and `b_j`. On the four side bases
`u,v,-u,-v`, use the same profile on opposite sides of each axis and edges
`Rot(a_j theta)w` or `Rot(b_j theta)w`. Antisymmetry cancels each side's
transverse displacement, so the four side chords close. At sufficiently
small positive `theta`, the direction gaps are strictly between zero and
`pi`; the result is a strictly convex actual unit wall with `4M` vertices.
The limiting nonconsecutive wall distances are strictly greater than one
because `c<1/2`.

At each side vertex `i` in
`{3,6,9,...} intersect [3,M-3]`, move the vertex by
`h_i=3 sin(d_i theta/2)` along the inward bisector of its two incident
edges. Its two old unit contacts become squared distance
`1+3 sin^2(d_i theta/2)`. The moved root's absolute derivative is
`(-B_i+3d_i/2)Jw`; relative to its old wall vertex, its displacement
derivative is `3d_i/2 Jw`, strictly inward. Opposite
the first interior grid row, the first-order half-squared-distance gain
is

`(B_i-3d_i/2)*sqrt(1-c^2) + lambda*(c(i-M/2)+(1-M/2))`,

for a selected root, and has `B_i` in place of the first factor at an
unmoved wall vertex. Set `mu` to the minimum of all positive `B_i` and
selected `B_i-3d_i/2`, and
`lambda=min(1,mu)/(100M)`. The absolute value of the `lambda` term is
below `3M lambda/4 <=3mu/400`, while the first term is at least
`mu sqrt(3)/2`; hence every limiting unit wall-to-site lower constraint
opens. Basis grid distances become strict because the scale is
`ell=1+2lambda tan(theta/2)>1`; every other limiting pair has strict
slack. Continuity supplies a strict packet for each fixed `M,c` and
profile pair at sufficiently small positive angle. Its sites and moved
roots lie in the wall interior; the selected old vertices are pairwise
farther than two, and the proposed roots are pairwise farther than two.

Assume additionally
`area(F_theta)<(sqrt(3)/2)(M^2+1)`. The audit.68 Oler bound gives at
most `(M-1)^2` actual source points inside the wall, with arbitrary
positions and contact graph. Replace all of them by distinct sites from
the explicit `(M-1)^2` packet and replace the selected wall vertices by
their roots. The embedded-wall shield protects packet sites from retained
exterior source points; the one-deleted-vertex shield applies separately
to each root. All new-to-new distances are strict by the packet proof.
Every inserted point is strictly inside the old source hull, so every
inserted-involving upper pair is strictly shorter than the old diameter.
The exchange preserves cardinality, creates no contacts, and removes the
selected wall vertices' `2|B|` distinct contacts. It remains triangle-free
and contradicts global minimality or contact-minimality.

For each fixed `M` and fixed profile pair, the strict area condition is
nonempty: as `c` tends to `1/2` from below, the limiting parallelogram
area `M^2 sqrt(1-c^2)` tends to `(sqrt(3)/2)M^2`, strictly below the
threshold. Choose `c` sufficiently close and then choose positive
curvature small enough to retain both area slack and packet margins.
This proves a nonempty chamber family at every fixed `M`; it does not
show a canonical source contains one.

### C-UNEVEN-WALL-CORNER-ROOT-REGRESSION — REGRESSION VALID

The exact profile `(-101,-5,-3,-1,1,3,5,101)` has, at `i=1`,
`B_1-3d_1/2=-43`. The report's exact rational source has a first interior
site strictly farther than one from the old wall vertex but strictly
closer than one to the proposed inward root. Thus turn size alone does
not justify adding corner-adjacent vertices to the moved bank. This is a
local source-pair regression, not a globally optimal source or a C-II
counterexample. The audited middle bank remains valid.

## Verification and scope

The independent verifier is
`research/verify_target_c_uneven_wall_packet_audit_2026_10_06.py`. It
reuses only the already audited audit.67 curved-wall exact geometry and
audit.68 rational area-basis helper. Exact cases include `M=8,9,10,12`
with unequal profiles and an `M=8` corner-concentration regression. It
checks 32,886 old and 32,886 new source pairs, 84 Green identities, 369
integer population values, exact areas, unit contacts, convexity,
containment, all moved-point upper pairs, and the two retained-neighbor
contact openings. Oler and the outside-source shields are canonical
analytic inputs; the finite verifier does not simulate arbitrary old
interiors or prove global optimality.

The exact D(8) heptagon capacity regression remains outside this
four-side family. No arbitrary canonical face is shown to have two
opposite profile pairs, the specified chart, or the required area slack.
Full-core and generic macroscopic-container closure remain open.
