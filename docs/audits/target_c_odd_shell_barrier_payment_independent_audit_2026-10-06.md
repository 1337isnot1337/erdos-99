<!-- theorem-state: {"artifact_id":"ART-D1C7F917E6B8","canonical":true,"claim_ids":["C-REGULAR-SHELL-BARRIER-NONGLOBAL-FAMILY","C-REGULAR-SHELL-BLOCKER-PAYMENT"],"claim_statuses":{"C-REGULAR-SHELL-BARRIER-NONGLOBAL-FAMILY":"regression","C-REGULAR-SHELL-BLOCKER-PAYMENT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C independent audit: odd-shell wall barriers

Date: 2026-10-06. Audit authority: `4249c5abc91bbb85fb9c22d650892bf0b53d0f33`,
state `2026-10-06.audit.64`. Immutable source: Worker 1 branch
`research/sol/target-c-owner-order-closure-20261006` at
`ece938d957c42f6719276e0a2b4dc51d25dc22ea`. Classification: **PASS — promote**
for the exact blocker-payment theorem and the explicit nonglobal-family
regression. Target C C-II and Level I remain open.

## Audited statements

Let `q >= 65` be odd, `alpha=pi/q`, `R=1/(2 sin alpha)`, and let `v_j` be the
vertices of the regular unit `q`-gon. Set

`x_j=(1-2/R^2)v_j`.

For any strict interior point `z` with `|z-v_i|>1` for every wall vertex, if
`z` blocks a proposal (`|z-x_j|<=1`), it blocks at most two proposals. If it
blocks two, their wall vertices are adjacent. Consequently, any collection
covering all `q` proposals has at least `(q+1)/2` distinct blockers. Each
such blocker lies in the radial collar
`4/5 < R-|z| <= 1+2/R`; every blocked incidence is a genuine near-unit
wall-isolate pair with `1 < |z-v_j| <= 1+2/R`.

There is also, for every odd `q>=65`, an explicit source with the full wall,
`(q+1)/2` collar isolates blocking all `q` proposals, and a translated deep
triangular-lattice filling, for which the only unit contacts are the wall
sides and the actual diameter graph is the odd diameter cycle. Despite those
features, an independent triangular-lattice packet of the same cardinality
has diameter strictly below `D_q`. This family is not globally optimal. Its
positive shell equilibrium coefficients, PSD shell stress, and full mixed
core bar rank do not supply global optimality.

## Independent proof reconstruction

For a blocker, write `t=|z|`, `h=R-t`, and `r=R-2/R`. Then `|z-r u_j|<=1`
implies `t>=r-1`, hence `h<=1+2/R`. A closest wall vertex is at angular
distance at most `alpha`. Since the blocker is a strict contact isolate,

`1 < |z-v_i|^2 <= h^2 + 2R^2(1-cos alpha)
                = h^2 + 1/(2(1+cos alpha)) < h^2+1/3`,

so `h>sqrt(2/3)>4/5`.

The blocked wall proposals lie on the circle of radius `r` inside the unit
disk centered at `z`. Both `r,t>1`, so their angular differences from the
radial direction of `z` are strictly below `pi/2`; the blocked arc has width
less than `pi`. If two blocked indices are nonadjacent in wall order, their
angular separation is at least `4 alpha`, so one is at least `2 alpha` from
the radial direction. Its unit-distance condition forces

`(h-2/R)^2 + (R-h)(R-2/R)/R^2 <= 1`,

equivalently

`h^2 - 5h/R + 2/R^2 + 2h/R^3 <= 0`.

But `R>10`, and the left side is strictly greater than `h(h-1/2)>0`.
This contradiction proves the multiplicity bound. Covering an odd `q`-cycle
by sets of one or two adjacent vertices requires at least `(q+1)/2`
distinct blockers.

For the sharp construction, pair wall sides `(0,1),(2,3),...,(q-3,q-2)`.
On each side put a radial midpoint blocker of radius
`R cos(alpha)-sqrt((1+delta)^2-1/4)`, where `delta=1/(100R^2)`, and put one
final blocker at radius `R-1-delta` on the remaining vertex ray. The paired
blocker is inside the polygon and has distance exactly `1+delta` from its
two side endpoints; the unmatched blocker is exactly `1+delta` from its
wall vertex. These are the closest wall vertices to the respective radial
directions, so all other blocker-wall distances exceed one. Both radii are
greater than `R-2`. Paired blockers are separated in angle by at least
`4alpha`, giving chord distance at least
`2(R-2)sin(2alpha)=2(1-2/R)cos(alpha)>1`. The unmatched blocker is at
angular distance at least `3alpha` from each paired midpoint; since
`sin(3alpha/2)>(7/5)sin(alpha)`, those distances exceed
`(7/5)(1-2/R)>1`. Thus blockers are mutually strictly separated. Moving an
endpoint inward by `2/R` toward its proposal reduces its squared distance
from a paired blocker by more than `4(4/5)/R-4/R^2`, which exceeds the
initial excess `(1+delta)^2-1`; the unmatched proposal has distance
`1+delta-2/R<1`. Every proposal is therefore blocked. These analytic bounds
hold for every odd `q>=65`; the exact interval certificate independently
checks all pair relations for `q=65,101,201`.

Place `N=floor(pi(R-3)^2/(a_0 ell^2))` triangular-lattice sites in the open
disk of radius `R-3`, where `a_0=sqrt(3)/2` and `ell=1+q^-2`. Since
`R(1-cos(alpha))=tan(alpha/2)/2<3`, this disk lies inside the polygon.
Translation averaging supplies the count. Its radial gap exceeds one from
the wall and from every collar blocker (whose radius is greater than `R-2`);
the deep sites are mutually separated by `ell>1`. For
`n=q+(q+1)/2+N`, the disk of radius
just below `D_q/2`, with triangular-lattice spacing just above one, has
translation-average population greater than `n`: indeed the limiting
surplus is bounded below by

`pi(3R-545/48)-1/2 > 0` for `R>10`.

The averaging theorem therefore gives `n` mutually more-than-unit-separated
points of diameter strictly below `D_q`. This is a whole-source competitor;
it does not rely on refill into the old wall or on preserving its isolates.

For the shell algebra, direct radial/tangential Fourier reduction gives the
stress eigenvalue

`(4/q)(D_q^2 sin^2(l alpha)-sin^2(l k alpha))`, `k=(q-1)/2`,

which is positive except at the two translation modes, with the constant
mode also zero. The mixed step-1/step-k bar determinant has the factors
stated in the source report and vanishes only at translations and rotation.
Thus the shell stress has rank `q-3` and the mixed core framework rank
`2q-3`. These local identities are compatible with the explicit global
competitor above.

## Hostile checks and scope

- Read and reconstructed the angular multiplicity argument, including the
  strict collar bounds and odd-cycle covering count.
- Checked the exact blocker placement, source-pair classifications, actual
  diameter cycle, deep-fill separation, and whole-source independent packet.
- Re-derived the surplus estimate; the verifier checks its directed rational
  enclosure, rather than inferring an infinite-family result from samples.
- Inspected the verifier's rational interval arithmetic. The audit copy is
  self-contained and was run after removing its import of the separate
  capped-wall candidate verifier.
- The verifier covers exact finite cases `q=65,101,201` and Laurent factor
  identities for eight odd `q` values. The all-odd-`q>=65` conclusion uses
  the analytic inequalities above, not extrapolation from those cases.
- No global optimality is claimed for any shell family. This excludes the
  displayed blocked fillings only; it gives no capacity bound for arbitrary
  macroscopic interiors, exterior caps, or the live C-II finite-move branch.

Verifier output: 61,680 wall/collar source-pair checks, 27,597 blocker-site
checks, and 820 exact Fourier-factor identity checks passed. The certified
translation-average packet exceeded each constructed cardinality for all
three tested values. See
`research/verify_target_c_odd_shell_single_vertex_barriers_2026_10_06.py`.

## Canonical disposition

Promote `C-REGULAR-SHELL-BLOCKER-PAYMENT` as a geometric multiplicity theorem
and `C-REGULAR-SHELL-BARRIER-NONGLOBAL-FAMILY` as an exact regression. The
one-vertex shield remains valid; this result quantifies the number of
strict wall-clear interior points needed to obstruct every inward wall
proposal in this regular-shell geometry. Contact isolates are the canonical
source instance. The explicit family is not a counterexample to Level I. It
sharpens the guardrail that positive shell stress, mixed core
rigidity, a fully blocked one-site shield, and quadratic filling do not
imply global optimality.

The live frontier does not change: arbitrary-container packet capacity and
the source-realized face-coupled finite-move endpoint remain open.
