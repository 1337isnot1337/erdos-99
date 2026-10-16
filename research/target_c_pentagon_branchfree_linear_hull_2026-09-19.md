<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a7c338cb3acb804a8f95d79b2e9d533b4a9bfe34", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_pentagon_branchfree_linear_hull_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4de5395e61e72b5e426225c3de2751813d157973e27ccc11b817679e1bae8ded"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: branch-free linear hull of a physical equilateral pentagon

This closes one possible direction for the generic support-seven work: after forgetting the cyclic rank/order branch of a single physical pentagon, no stronger linear inequality remains. The rank-conditioned secants and the two median-hull facets are useful only while the gap order is retained.

Let `x_0,...,x_4` be the five cyclic force-direction gaps, normalized by `pi`, so `sum x_i = 2`. The established physical turn-simplex theorem gives, cyclically,

```
x_i + x_{i+1} - x_{i+3} > 1/3.
```

Let `Q` be the closed rational polytope obtained by replacing `>` by `>=` and keeping `sum x_i=2`.

## Theorem

If `P` is the set of gap vectors of strictly convex equilateral physical pentagons, then

```
closure(conv(P)) = Q.
```

Consequently, every non-strict affine inequality valid for every physical pentagon is already valid on `Q`. Equivalently, no branch-free linear cut for one pentagon can strengthen the existing turn-simplex relaxation. Any further use of the exact gap-order/median-hull information must retain a rank/order disjunction, use nonlinear information, or couple several faces.

## Exact polyhedral side

The verifier `verify_target_c_pentagon_branchfree_linear_hull_2026_09_19.py` enumerates `Q` exactly over `fractions.Fraction`. Since `sum x_i=2` leaves dimension four, a vertex is obtained by activating four of the five turn-simplex facets. There are exactly five vertices:

```
(0,   2/3, 1/3, 1/3, 2/3)
(1/3, 1/3, 2/3, 0,   2/3)
(1/3, 2/3, 0,   2/3, 1/3)
(2/3, 0,   2/3, 1/3, 1/3)
(2/3, 1/3, 1/3, 2/3, 0)
```

They are the five cyclic rotations of one vector. Thus `Q` is their convex hull.

The inclusion `closure(conv(P)) subset Q` is immediate from the already proved strict turn-simplex inequalities. It remains to show that all five vertices of `Q` lie in `closure(P)`.

## Explicit physical approach to a turn-simplex vertex

Fix

```
0 < a < pi/3,
b = arccos(cos(a) - 1/2).
```

Then `cos(a)-1/2` lies in `(0,1/2)`, hence

```
pi/3 < b < pi/2.
```

Take the five unit force directions at angles

```
-a,  a,  pi-b,  pi,  pi+b.
```

They are strictly cyclically ordered. Indeed `a+b < 5pi/6 < pi`, so every cyclic gap below is positive. Their vector sum is exactly zero:

```
u(-a)+u(a) = (2 cos(a), 0),

u(pi-b)+u(pi)+u(pi+b)
  = (-2 cos(b)-1, 0)
  = (-2(cos(a)-1/2)-1, 0)
  = (-2 cos(a), 0).
```

Therefore these five unit vectors, in cyclic order, are the edge directions of a strictly convex equilateral force pentagon. Its normalized cyclic gap vector is

```
(2a, pi-b-a, b, b, pi-b-a) / pi.
```

For `0<a<pi/3`, all five gaps lie in `(0,pi)` before normalization, so the polygon is strict. As `a -> 0+`, continuity of `arccos` gives `b -> pi/3`, hence the gap vector tends to

```
(0, 2/3, 1/3, 1/3, 2/3).
```

Cyclically rotating the construction reaches the other four vertices. Hence every vertex of `Q` belongs to `closure(P)`, so

```
Q = conv(vertices(Q)) subset closure(conv(P)).
```

Together with the opposite inclusion, this proves the theorem.

## Consequence for H6

The latest H6 complete-angle endpoint has 5,692 generic cells. A tempting next step is to convexify the ten physical gap-order branches into one branch-free LP cut per face. This theorem shows that such convexification loses all of the new rank-conditioned information: its closed linear hull is exactly the turn-simplex polytope already present in the H6 affine system.

So the next linear attack must keep the ten order branches separate and certify branch infeasibility face-by-face, rather than searching for another order-free linear inequality of one pentagon.
