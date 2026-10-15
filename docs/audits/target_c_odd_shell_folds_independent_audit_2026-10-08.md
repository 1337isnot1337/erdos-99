<!-- theorem-state: {"artifact_id":"ART-12E7BED49517","canonical":true,"claim_ids":["C-ODD-SHELL-CLEARANCE-FOLD-ENDPOINT","C-ODD-SHELL-COLLAR-TRANSPORT-ENDPOINT","C-ODD-SHELL-TWO-ISOLATE-FOLD-REGRESSION"],"claim_statuses":{"C-ODD-SHELL-CLEARANCE-FOLD-ENDPOINT":"canonical","C-ODD-SHELL-COLLAR-TRANSPORT-ENDPOINT":"canonical","C-ODD-SHELL-TWO-ISOLATE-FOLD-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C independent audit: odd-shell finite folds and fixed-cloud obstruction

Date: 2026-10-08. Audit cycle 167. Audit base:
`origin/main=6abf7b9a5ed93fe26c5fa80032a1bcb2cb6cd326`, state
`2026-10-08.audit.162`. Chosen target: C-II finite source endpoint claims.

## Frozen source and claims

The discovery source is `research/level-i-closure-20261007` at the exact
snapshot `12f6833725f281ce39a6d04ebcb45630b3a6768f`. Its audited artifacts
are:

- `docs/reports/target_c_two_wave_shell_fold_two_isolate_obstruction_2026-10-08.md`, SHA-256 `b0ef35a4607440f592f383aaab5595c586806b22c316c2134a6fcf7df5efb46f`;
- `research/verify_target_c_two_wave_shell_fold_2026_10_08.py`, SHA-256 `5d50a0d274940bc45085d6e789887675399acf5a7270a4f938501cec16fc6f87`;
- `docs/reports/target_c_shell_fold_collar_transport_2026-10-08.md`, SHA-256 `4d8ed2332f2d08e5ede2a13d2b412944a5dcd7216cef56a15d9f04499e6a2707`;
- `research/verify_target_c_shell_fold_collar_transport_2026_10_08.py`, SHA-256 `cd2a936ee0b97fd57bf694ebdf91e7de5d0d5f798dfa1b939bb8d81c1198e9ee`.

Verdicts:

1. **PASS — promote `C-ODD-SHELL-CLEARANCE-FOLD-ENDPOINT`.** For every odd
   `q>=21`, a regular unit `q`-gon with any unit-separated point cloud strictly
   inside its convex hull and at distance greater than `1+3/R` from every wall
   vertex admits an explicit same-label finite endpoint. It retains all wall
   contacts, creates no new unit contacts, and has full-source diameter below
   `D_q=2R cos(pi/(2q))`. The hypothesis is the stated pointwise clearance.
2. **PASS — promote `C-ODD-SHELL-COLLAR-TRANSPORT-ENDPOINT`.** For odd
   `q>=65`, the prescribed Audit.65 midpoint/vertex-ray collar, any subset of
   those strict contact isolates, and any unit-separated deep cloud in the
   open disk of radius `R-3` admit a same-label endpoint by the same wall fold
   plus inward transport of each retained collar point by `4/R`. Every old
   contact is retained, no new contact is created, and the endpoint diameter
   is at most `L=2R-1/R<D_q`.
3. **REGRESSION VALID — register
   `C-ODD-SHELL-TWO-ISOLATE-FOLD-REGRESSION`.** Two specified strict contact
   isolates block every cyclic rotation of this two-wave wall fold when the
   cloud is held fixed. This refutes universal compatibility of that endpoint
   family under fixed-cloud motion; it does not refute the collar-transport
   endpoint, which moves the collar.

Neither endpoint theorem is a theorem about arbitrary C-II sources or global
minimizers. The exact implication is only: **the stated regular-shell source
has a finite full-source endpoint of smaller diameter**. It supplies no
continuous feasible path, arbitrary-container capacity, C-II closure, or
Level I consequence.

## Independent reconstruction of the wall fold

Put `alpha=pi/q`, `R=1/(2 sin alpha)`, `c=cos(2 alpha)`, and
`t=sin(alpha)^2=1/(4R^2)`. The side chord is one. The two reflection waves
produce the radial factors

```
a=2c-1=1-4t=1-1/R^2,
b=2ac-1=1-12t+16t^2=1-3/R^2+1/R^4.
```

The first wave moves even vertices to `a v_j`; the second moves the indicated
odd vertices to `b v_j`; two consecutive vertices remain fixed. This is an
endpoint definition only; no intermediate segment is asserted feasible.
The side identities are

```
a^2+1-2ac=4t,
a^2+b^2-2abc=4t,
2(1-c)=4t.
```
After multiplication by `R^2`, each is exactly one. For `q>=21`,
`alpha<1/6`, `b>2/3`, and `a>b>0`. Every old non-side chord has length at
least `2 cos(alpha)>3/2`. For any two positive radial factors at least `b`,

```
|lambda_i v_i-lambda_j v_j|^2
 =R^2[(lambda_i-lambda_j)^2
     +2 lambda_i lambda_j(1-cos(theta_i-theta_j))]
 >= b^2 |v_i-v_j|^2 > 1
```

on every old non-side pair. Every pair other than the fixed side has a moved
endpoint with radius at most `aR`, so its endpoint length is at most
`R(1+a)=2R cos(2 alpha)`. This is strictly below
`D_q=2R cos(alpha/2)`; the fixed side has length one. Thus the wall endpoint
is strictly sub-`D_q`.

For the first theorem, each wall displacement is at most `3/R`:
`R(1-a)=1/R` and `R(1-b)=3/R-1/R^3`. The assumed cloud clearance therefore
keeps every moving wall/cloud distance strictly above one. Cloud/cloud pairs
are unchanged. Every cloud point is strictly inside the wall polygon, so no
unchanged pair involving cloud points realizes the polygon's diameter `D_q`;
all unchanged pairs have strict upper slack. Moving wall/cloud pairs are
strictly below `R+aR<D_q`. This checks all source pairs, including any
contact-isolated labels; no contact isolate is deleted or identified with a
core coordinate.

## Independent reconstruction of the collar-transport endpoint

The paired collar radius is

```
T=R cos(alpha)-sqrt((1+delta)^2-1/4), delta=1/(100R^2),
```

on the midpoint ray of sides `(0,1),(2,3),...,(q-3,q-2)`. The unmatched
point, when retained, has radius `R-1-delta` on the last wall-vertex ray.
Each paired point starts at distance `1+delta` from its two neighboring wall
vertices. The canonical Audit.65 estimates give paired depth `h=R-T` in
`(4/5,9/10)`; unmatched depth is `1+delta`. The collar rays have mutual
angular spacing at least `3 alpha`.

Transport each retained collar point radially inward by `4/R`, keeping every
deep-cloud point fixed. All new wall radii are at least `w=R-3/R`; every
transported collar radius is greater than `R-3/2`, and `w` exceeds the paired
collar radius after transport. For a paired collar point, its minimum new
wall distance occurs at radii `w,T-4/R` and angular separation `alpha`.
The difference between this squared distance and its old nearest-wall square
`(1+delta)^2` is

```
2h/R+1/R^2 - 2u[(4R+3T)/R-12/R^2], u=1-cos(alpha).
```
To make the margin explicit, `cos(alpha)>1-alpha^2/2>0.998`, hence
`u=1/[4R^2(1+cos(alpha))]<1/(7.99 R^2)`. Also `T<R`, so the bracket is
less than `7`; the subtracted term is less than `14/(7.99 R^2)<2/R^2`.
Consequently the displayed increase exceeds
`8/(5R)-1/R^2`, which is positive for `R>10`. This supplies the strict
paired-collar/wall lower bound. The unmatched point has radial gap at least
`1+delta+1/R`. Distinct transported collar points remain separated because

```
2(R-3/2) sin(3 alpha/2)
 >(7/5)(1-3/(2R)) > 1.
```
Deep-cloud radial gaps exceed one from both the new wall and transported
collar; cloud/cloud pairs are unchanged. This covers every full-source lower
pair.

All upper pairs are also checked. Wall/wall distances are at most
`L=2R-1/R`; wall/collar, collar/collar, wall/deep, collar/deep, and
deep/deep pairs are strictly below `L` by their radial-sum bounds. Finally
`L=2R cos(2 alpha)<D_q`. The original collars and deep cloud lie strictly
inside the wall polygon, so the original source diameter is exactly `D_q` as
well. Thus this is a same-cardinality strict-diameter endpoint for the entire
specified full source. If the deep cloud has internal unit contacts, they are
retained; the theorem does not require the source to be triangle-free.

The bound in the source report `>8/(5R)-5/(2R^2)` used a looser displayed
bound for `u` than suffices to justify that coefficient. The sharper estimate
above repairs this local presentation gap and proves a stronger positive
margin. No theorem statement depends on the omitted intermediate inequality.

## Fixed-cloud regression and attempted breakage

For the regression, take only the two paired midpoint isolates on sides
`(0,1)` and `(2,3)`. Each begins at squared distance `(1+delta)^2` from its
side endpoints. If such an endpoint is moved inward by `d`, where
`1/R<=d<3/R`, the squared distance decreases by

```
2d(R-T cos(alpha))-d^2 > d(8/5-3/R) > 13/(10R).
```
The old squared-distance excess is `2delta+delta^2<3/(100R^2)`, so the new
distance is strictly below one. A cyclic rotation of the fold fixes only two
consecutive wall vertices. It cannot fix the four distinct endpoints of both
selected sides, so at least one selected-side endpoint moves and collides with
its fixed isolate. The inequalities hold for every odd `q>=65`. Adding any
unit-separated cloud inside radius `R-3` leaves these collisions intact while
the cloud is fixed.

This is exactly scoped to the proposed fold endpoints and a fixed cloud. The
source branch's later clarification says the collar-transport operation moves
the cloud collar; that candidate is outside the regression's quantifiers.
Audit.65's one-site blocker payment and the existing quadratic-fill
nonglobality regression remain consistent and are not upgraded here.

## Verifier review and independent execution

Both source checkers were inspected, not treated as analytic proof. They use
Audit.65 directed rational interval arithmetic and exact polynomial
identities, then test finite shells `q=65,101,201`. The two-wave checker
certifies all wall pair lower/upper classifications, the two blocker
collisions for every cyclic cut, and the explicit deep lattice cloud. The
collar checker certifies all old/new wall and collar pair classifications,
endpoint upper bounds, and radial relations to a strict triangular-lattice
cloud. Distinct cloud pairs follow from the positive integral triangular
lattice norm; they are not pair samples. The reports' all-`q` conclusions
come from the analytic inequalities reconstructed above, not extrapolation
from those three finite shells.

I reran both source scripts in the frozen `12f68337` worktree and both copied
scripts in this promotion worktree. Their exact interval output passed in all
four executions. I also checked the wall-fold endpoint at the weakest claimed
parameter `q=21` with rational Taylor enclosures and directed interval
arithmetic; the blocker obstruction and collar transport deliberately retain
the stronger `q>=65` hypothesis.
The scripts do not encode the generic clearance cloud theorem, the universal
inequalities, or global optimality.

## Canonical disposition and frontier effect

The exact endpoint theorems and narrow fixed-cloud regression are promoted as
three separate claims so their scopes cannot be conflated. Audit.65 already
proves that the displayed fully blocked, quadratically filled shell family is
not globally optimal by a separate lattice packet. The new finite endpoints
preserve all labels and old contacts and make a specific simultaneous fold
available even where the fixed-cloud obstruction applies by transporting the
collar. The regression prevents treating the wall-only fold as universally
compatible with stationary isolates.

C-II and Level I remain open. No route obligation is discharged: arbitrary
canonical sources need not be regular shells, radial-clear clouds, or the
prescribed collar/deep-annulus family. The active next obligation remains a
source-realized finite move or discrete replacement from the face/train system
that passes every full-source lower and actual-diameter upper constraint.
