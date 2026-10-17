> Generated reading edition · [exact source](../../../docs/reports/target_c_local_witness_cell_2026-10-01.md) · source SHA-256 `8b9a4b2dc9e95f54455fbf97b227158b31815a37c34a4bf66cb5e1cdc3e2d058`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-774786BC22DE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- local witness-cell lemma

Base main: f076f59f9b2796e68a8b005f0451dd7ede659a14. Proof-only; C-II remains open.

## Theorem

Let tau be a non-singleton global outer-to-outer stopped train of projective direction
u, and let v be a diameter vertex whose incident diameter edges supply opposite strict
Section-157 transverse witnesses across the tau shore cut.

Then the brace is local in the global diameter-direction order. Either two
v-incident cut edges h-,h+ are consecutive global diameter directions with

    dir(h-) < u < dir(h+),

or three v-incident cut edges h-,h0,h+ are consecutive global diameter directions,
dir(h0)=u, and the outer two have opposite strict transverse signs.

Consequently, let L be any family of global O-O trains, all single-star braced by the
same v, whose directions lie in an interval J of width W. Put

    a_D = asin(1/(2D)),
    N = floor(W/(2a_D)) + 1,
    M = 2N + 1.

There is a subfamily L' with

    |L'| >= |L|/M

and two fixed actual diameter edges h-,h+ incident with v crossing every retained
train with opposite strict signs. Either h-,h+ are consecutive global directions
bracketing every retained train direction, or exactly one global diameter direction
h0 lies between them and every retained train is parallel to h0.

No laminar-path hypothesis and no endpoint limit are needed.

## Proof

Every endpoint of a diameter edge is an extreme point of the source convex hull.
Otherwise, if p=lambda x+(1-lambda)y is a nontrivial convex combination and |p-z|=D,
strict convexity of squared distance gives

    |p-z|^2 < lambda |x-z|^2 + (1-lambda)|y-z|^2 <= D^2,

a contradiction.

Represent tau by its proper Jordan crosscut of the outer-face disk. The cut divides
the outer boundary into two arcs and induces the Section-157 shore split S,T. Suppose
v is in S. A v-incident diameter edge vx crosses this cut exactly when x is in T, so
its other endpoint lies on one contiguous boundary arc.

Viewed from one fixed vertex of a convex polygon, ray direction to the other boundary
vertices is monotone in their boundary order. The diameter neighbors of v lie in a
cone of aperture at most pi/3, so projectivizing neither identifies nor reverses their
order. Hence the v-incident diameter cut edges form one contiguous block in the
v-star direction order. Current main's global diameter-star contiguity makes
consecutive members of this block consecutive global diameter directions.

Orient every crossing diameter vector from T into S, as in Section 157. For all
v-incident cut edges this differs from the ray orientation v->x by one common sign.
On a real lift of the star interval, an edge of ray direction theta therefore has
transverse sign, up to that common factor,

    sign(sin(theta-u)).

Single-star bracing supplies strict signs of both kinds. If no cut edge is parallel
to u, the last cut direction below u and first above u are consecutive and give the
first case. If one cut edge h0 is parallel to u, it is unique, and its immediate cut
neighbors give the second case.

For the family statement, current main gives separation at least 2a_D between
successive v-incident diameter directions. Thus at most N such direction thresholds
lie in J. They partition J into at most N+1 open cells and N singleton threshold
cells, hence at most M=2N+1 canonical witness cells. Pigeonhole L by this cell and
apply the local statement.

## Section-90 consequence

For a Section-90 shore W=4K/D and 2a_D>=1/D, so one may take

    M_K = 2 floor(4K) + 3.

This improves the latest common-witness extraction on main from retained fraction
1/(2M_K) to 1/M_K and removes its laminar-path hypothesis.

Applied to main's fixed-star complete O-O rectangle, where

    |A_v|, |B_w| >= (kappa^4/(16 pi^3 C_K) - o(1)) D,

one obtains a still-complete strict-rhombus subrectangle A' x B' with

    |A'|, |B'| >= (kappa^4/(16 pi^3 C_K M_K) - o(1)) D.

Each shore has one fixed opposite-sign witness pair localized to one global
diameter-direction cell.

At the exact rooted endpoint E_D=pi-2a_D q=o(1). In the open-cell case the common
witness gap is a shared consecutive gap, so its excess over 2a_D is one nonnegative
summand of E_D. Hence

    |G| = 2a_D + o(1).

This is only an o(1) angular error, not an o(1/D) claim. In the threshold case the
entire retained shore has exactly the direction of one fixed actual diameter edge
crossing all its cuts.

## Remaining bottleneck

The fixed-star branch is now a complete inverse-phase O-O grid plus two gap-local
diameter witness cells. The next obstruction should use the convex-thrackle direction
order on these consecutive or one-threshold-separated cells. The split-star and
inactive-interface branches remain open.

No computation, verifier, numerical experiment, or CI output is used.
