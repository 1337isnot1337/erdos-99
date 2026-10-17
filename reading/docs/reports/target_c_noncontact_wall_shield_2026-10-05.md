> Generated reading edition · [exact source](../../../docs/reports/target_c_noncontact_wall_shield_2026-10-05.md) · source SHA-256 `0fe41f3f850e0734971d78b257a62a429061d51311276819c7ef174ba864d4c5`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1746FA31924A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — sharp noncontact-wall shield and finite activation threshold

Date: 2026-10-05. Base: `3c94a1a93641a5f8fa24d43068d487594d3e38cd`.
State: `2026-10-05.audit.57`. Branch:
`research/target-c-residual-closure-20261005`.
Classification: **proved candidate awaiting independent audit and promotion**;
artifact remains **unreviewed**. Exact counterexamples have regression scope.
Level I and C-II remain open. No external literature is used.

## 1. Closing implication and exact scope

```
actual source polygon with edges <= sqrt(3) and certified strict spare sites
-> simultaneous protected refill without requiring unit boundary contacts
-> candidate residual-cage release theorem
-> same-cardinality strict sub-D competitor.
```

This changes the shield hypothesis, not the requirement for actual surplus.
It permits short walls whose contacts have been opened in a feasible motion.
It does not construct that motion. Canonical inputs actually used are the
wall-crossing proof in `C-EMBEDDED-WALL-REFILL`
([report, Section 2](target_c_embedded_grain_wall_replacement_2026-10-02.md))
and the winding proof in `C-SHORT-WALL-ZERO-CAPACITY`
([report](target_c_short_unit_wall_zero_capacity_2026-10-05.md)).
The competitor corollary additionally uses the **unpromoted** finite theorem
[proved on this branch](target_c_residual_cage_release_refill_2026-10-05.md).
It is not silently claimed as a canonical dependency.

## 2. Generalized strict wall shield

Let A be any finite unit-separated source, and let C be a simple polygon
whose vertices are source points and whose cyclic edges have length at
most L<=sqrt(3). Edges need not be unit contacts. Define

    W_C = {x in int C: |x-b|>1 for each wall vertex b}.

Then every x in W_C is strictly unit-clear from every source point q
outside int C. For q not a wall vertex the quantitative bound is

    |x-q| > 2 sqrt(1-L^2/4) >= 1.                      (1)

If q is a wall vertex, strict clearance follows from the definition.
Otherwise let z be the first exit of [x,q] from the wall interior.
If z is a vertex b, then |x-q|=|x-b|+|b-q|>2. Otherwise z lies in the
relative interior of ab, with z=(1-t)a+tb, 0<t<1. The exact weighted-square
identity and the endpoint guards give

    |x-z|^2 > 1-t(1-t)|a-b|^2 >= 1-L^2/4,
    |q-z|^2 >= 1-t(1-t)|a-b|^2 >= 1-L^2/4.

Add lengths along [x,q] to obtain (1). Strictness on the packet side is
why equality L=sqrt(3) is admitted. No convexity of C is required.

For a family of such polygons with disjoint interiors, independently
chosen packets are jointly strictly unit-separated. Indeed, the vertices
of one polygon cannot lie in the open interior of another: otherwise a
small disk about that vertex inside the second polygon would meet the
first polygon's interior. Apply (1) first to a packet point and each
other wall vertex, and then use those strict endpoint guards in the
crossing proof for two points in different packets. Their distance is
strictly greater than one. As before, strictify internal packet distances
by sufficiently small dilation inside the open wall-safe sets.

Thus the finite residual-cage release/refill proof remains valid with
these noncontact polygons in place of unit-contact walls. All source
labels, old interior populations and diameter transversals are still
counted exactly. Packet sites are initially interior to the old source
hull, and their finite upper and lower margins are still the quantities
used to choose the local chart motion.

## 3. Sharpness of the uniform edge threshold

The bound sqrt(3) is optimal for a shield based only on unit clearance
from wall vertices and old-source separation.

For every sqrt(3)<L<2 choose

    sqrt(1-L^2/4) < h < 1/2,   1 <= H <= L.

Use the rectangle with vertices

    a=(-L/2,0), b=(L/2,0), c=(L/2,-H), d=(-L/2,-H),

the old exterior point q=(0,h), and the new interior point x=(0,-h).
All wall vertices and q are unit-separated. Both x and q are strictly
farther than one from a,b since L^2/4+h^2>1. The bottom-wall distances
are larger, since H-h>=1-h>h. Yet |x-q|=2h<1.
The wall has maximal side L. This disproves any extension of (1) to
L>sqrt(3) without an additional hypothesis. For a proposed upper bound
at least two, use any L between sqrt(3) and two in the same construction.

A fully rational certificate takes

    L=7/4, H=3/2, h=49/100.

The nearest squared wall distance of x and q is

    49/64 + 2401/10000 = 40229/40000 > 1,

but their squared cross-distance is 2401/2500<1.
This is a finite feasible-source regression, not a global-minimizer claim.

## 4. Quantitative winding barrier for contact breaking

Let C have n edges of length at most L. If x in int C has wall clearance
r=min_i|x-v_i|>0 and r>L/2, every principal angular increment satisfies

    |theta_i| <= 2 asin(L/(2r)).

To see this, if both endpoint radii are at least r, the law of cosines gives

    |v_i-v_(i+1)|^2
      = (r_i-r_(i+1))^2
        + 4 r_i r_(i+1) sin^2(theta_i/2)
      >= 4r^2 sin^2(theta_i/2).

The wall avoids x; its winding number is +/-1, so the sum of absolute
increments is at least 2pi. Consequently

    r <= L/(2 sin(pi/n)).                              (2)

For a wall-safe point r>1, (2) implies the necessary condition

    L > 2 sin(pi/n).                                   (3)

If r<=L/2 instead, r>1 already implies L>2 and hence (3); thus the
condition holds without the auxiliary r>L/2 case assumption.

A regular n-gon gives equality in (2). Regular pentagons with common
side length L satisfying

    2 sin(pi/5) < L <= sqrt(3)

therefore have a wall-safe center and also satisfy the new shield. This
is a genuine nonempty interval. Four-edge walls become possible for
sqrt(2)<L<=sqrt(3); three-edge walls remain impossible throughout the
safe-shield regime.

In particular any five-edge original unit wall which is to acquire a
wall-safe point must lengthen at least one original side beyond

    2 sin(pi/5)=sqrt((5-sqrt(5))/2)>1.

If each original wall label moves by at most epsilon, every new side is
at most 1+2epsilon. Thus activation requires

    epsilon > (2 sin(pi/5)-1)/2.                       (4)

This is a fixed positive source-space threshold. Arbitrarily small
contact opening is insufficient, even though the contact manifold chart
may have arbitrarily small radius along an asymptotic sequence. Exact
contact-preserving motion remains excluded by canonical audit.57.
Equation (4) does not rule out a finite active-set route; it identifies
a quantitative step that such a route must actually cross.

## 5. Full-core and container consequences

The new shield can certify packets using short **noncontact** polygons
rather than extracting long actual contact cycles. This is applicable to
both branches, but source separation from those vertices and genuine
interior packet capacity must still be proved. A dense isolate container
is not automatically capacious enough to pay one extra point.

The candidate closes no branch yet. In full-core, a proposed expanded
pentagon route must construct a finite feasible opening crossing (4),
control lower constraints to the rest of the core, and provide surplus
rather than merely an empty wall-safe set. In the container branch it
must provide noncontact polygons with packets exceeding the explicitly
replaced isolate populations by the residual-cage cost.

The large-wall lock regression still applies to any claim that small
positive residual alone supplies spare sites. Positive reciprocal train
mass is not a displacement bound, and loaded-return length is not spare
capacity. No such conversion is made here.

## 6. Computation and classification

`research/verify_target_c_noncontact_wall_shield_2026_10_05.py` uses exact
rational arithmetic. It checks the feasible-source counterexample above,
a positive-capacity four-edge noncontact wall, and the weighted-square
identities used by the shield over finitely many exact parameter packets.
The universal shield and winding bound are analytic proofs; enumeration
does not prove them. No computed packet is asserted to be a canonical
C-II source or a global minimizer.

| Claim | Classification | Scope |
| --- | --- | --- |
| Edge-length sqrt(3) shield | Proved candidate awaiting promotion | Finite actual source polygons |
| Sharp threshold counterexample | Regression | Rational feasible source |
| Fixed pentagon-opening threshold | Proved candidate awaiting promotion | Finite winding and label displacements |
| Feasible activation on canonical source | Unproved | Still needs an actual motion |

Independent audit is required. No authoritative theorem state is changed.
