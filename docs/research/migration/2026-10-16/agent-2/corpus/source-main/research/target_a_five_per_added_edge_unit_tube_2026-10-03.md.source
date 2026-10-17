# Target A: five new lattice tube sites per attached unit edge

Date: 2026-10-03
Base main: 7a327e1ad95cd2e9cb035b9b96fb34fd8f12114d
Status: proof plus complete exact finite certificate; noncanonical. Target A and Level I remain open.

This note is independent of the active Target B fractional-GPI/coarea route and the
nine-no-root k=6 finite-support route. It sharpens only the geometric tube cost in
Target A Section 175.

Section 175.1 currently gives

    |T_Σ| ≤ 9 |E(Σ)|.

That union bound pays nine sites on every edge. If a new edge is attached at a shield
vertex already exposed by an earlier edge, the open unit disk around that shared
endpoint is already inside the old tube. The genuinely new cost is at most five sites.

## 1. One-ended incremental tube

Let Λ be a unit triangular lattice. For a unit segment e=[p,q], define

    R_p(e) = { y in Λ : dist(y,e) < 1 and |y-p| ≥ 1 }.

### Theorem 1

For every placement and orientation of e,

    |R_p(e)| ≤ 5.

The endpoint p need not be a lattice point.

### 1.1 Six hypothetical sites have only three lattice shapes

Translate p to the origin and let w be the unit segment direction. Write each point as

    y = x w + s n,

where n is a unit normal. Membership in R_p(e) forces x>0. If x≤0, the closest point
of the segment is p, so dist(y,e)<1 would imply |y-p|<1.

For 0<x≤1, the tube condition gives |s|<1. For x≥1, it gives

    (x-1)^2 + s^2 < 1.

Take two points in R_p(e).

- If both have x≤1, their squared separation is less than 1+4=5.
- If both have x≥1, they lie in the same open unit disk around q, so their separation
  is less than 2.
- In the mixed case write the right-hand point as x'=1+t, with 0≤t<1. Then

      |s'| < sqrt(1-t^2)

  and

      |y-y'|^2
      < (1+t)^2 + (1+sqrt(1-t^2))^2
      = 3 + 2(t+sqrt(1-t^2))
      ≤ 3 + 2 sqrt(2)
      < 7.

Thus every pair in a hypothetical six-site subset has distance strictly below sqrt(7).

In triangular-lattice coordinates (a,b), squared distances are

    Q(a,b) = a^2 + ab + b^2.

The only nonzero represented values below 7 are 1, 3, and 4. After translating one of
six sites to the origin, the other five lie in the 19-point lattice ball Q≤4.

The exact certificate

    research/verify_target_a_five_per_added_edge_unit_tube_2026_10_03.py

enumerates all five-subsets of the remaining 18 points, keeps those with every
pairwise squared distance at most 4, and quotients by translations and the 12
dihedral symmetries of the triangular lattice. It finds exactly 54 anchored six-sets
and exactly three symmetry orbits:

1. the six points of a side-two equilateral triangular patch;
2. a lattice center together with five of its six unit neighbors;
3. the six unit neighbors of a missing lattice center.

The enumeration is integer-only. Each orbit is now excluded analytically.

### 1.2 Side-two triangular patch

Let o be the center of the side-two equilateral triangle. Three of the six sites are
the side midpoints. They form an equilateral triangle of circumradius 1/sqrt(3).

Every site y in R_p(e) satisfies |y-p|≥1. Put R=|p-o|. One midpoint m makes angle at
most pi/3 with p-o, so

    1 ≤ |p-m|^2 ≤ R^2 + 1/3 - R/sqrt(3).

Therefore

    R^2 - R/sqrt(3) - 2/3 ≥ 0,

hence R≥2/sqrt(3).

The three corner vertices have circumradius 2/sqrt(3). One corner c makes angle at
least 2pi/3 with p-o. Therefore

    |p-c|^2 ≥ R^2 + 4/3 + 2R/sqrt(3) ≥ 4.

But every point in the open unit tube of a unit segment satisfies |y-p|<2, by the
triangle inequality through a closest point of the segment. Contradiction.

### 1.3 Center plus five neighbors

Let o be the lattice center and rotate so the missing unit neighbor has angular
direction zero. Since o is one of the six sites,

    1 ≤ r:=|p-o| < 2.

Every present unit neighbor u also satisfies |p-(o+u)|≥1.

First suppose the direction of p-o lies outside the Voronoi sector [-pi/6,pi/6] of
the missing neighbor. Some present neighbor lies within angle pi/6 of p-o. Its
distance constraint gives

    r ≥ 2 cos(pi/6) = sqrt(3).

Among the six hexagon directions at least two make angle at least 2pi/3 with any
fixed direction. Deleting one direction leaves at least one such present neighbor v.
For it,

    |p-(o+v)|^2 ≥ r^2 + 1 + r > 4,

contradicting |p-(o+v)|<2.

Now suppose p-o lies in the missing-neighbor sector. By reflection write its angle as
theta in [0,pi/6]. The present neighbor at angle pi/3 gives

    r ≥ r0 := 2 cos(pi/3-theta).

The opposite neighbor at angle pi is present. Its squared distance from p is

    r^2 + 1 + 2r cos(theta).

This is increasing in r≥0, and direct substitution gives

    r0^2 + 2r0 cos(theta) - 3 = 2 sqrt(3) sin(2 theta) ≥ 0.

So the opposite neighbor is at distance at least 2 from p. Contradiction.

### 1.4 Six neighbors of a missing center

Let o be the missing lattice center. Suppose p≠o and put r=|p-o|>0. One of the six
unit neighbors lies within angle pi/6 of p-o. Since p is at least unit distance from
that site,

    r ≥ sqrt(3).

Another hexagon vertex lies within pi/6 of the direction opposite p-o. Hence

    |p-y|^2 ≥ r^2 + 1 + sqrt(3) r ≥ 7,

again contradicting |p-y|<2.

Thus the only annular possibility is p=o. But for any segment direction w, one of the
six unit neighbors y has y dot w ≤ 0. For every t in [0,1],

    |y-tw|^2 = 1 + t^2 - 2t(y dot w) ≥ 1.

So that site is not in the open unit tube. The third orbit is impossible, proving
Theorem 1.

## 2. Connected shields cost five new sites per added edge

### Theorem 2

Let Σ be any finite connected unit-contact graph with at least one edge. Then

    #{ y in Λ : dist(y,|Σ|) < 1 } ≤ 5 |E(Σ)| + 4.

Proof. Order the edges so the first edge is arbitrary and every later edge shares an
endpoint with an earlier edge. A spanning-tree order followed by the non-tree edges
has this property.

The first edge contributes at most nine lattice sites by canonical Lemma 175.1. Add
an edge e=[p,q] sharing p with the previous union. The previous tube already contains
every lattice site with |y-p|<1, because p belongs to an already exposed unit segment.
Hence every genuinely new site contributed by e belongs to R_p(e), and Theorem 1
bounds the increment by five. Therefore

    |T_Σ| ≤ 9 + 5(|E(Σ)|-1) = 5|E(Σ)| + 4.

## 3. Section-175 consequence

For the locked connected unicyclic three-channel fan, |E(Σ)|=|V(Σ)|=:v. Hence

    |T_Σ| ≤ 5v+4,
    |T_Z| ≤ 5v+4.

The exact Section-175 right-deficiency theorem remains

    ζ-s ≥ |O_iso| + Q_Σ - j_* - |T_Z|.

Therefore the pointwise sufficient locked-branch condition improves to

    |O_iso| + Q_Σ ≥ j_* + 5v + 4.

This does not close Target A. It reduces the deterministic thick-tube payment from
9v to 5v+4. The remaining theorem must still force enough actual right-sector sink
surplus.

## 4. Proof status

The reduction to three lattice shapes is analytic plus a complete exact finite integer
enumeration. All three shape exclusions and the connected-graph accumulation are
analytic. The verifier was executed locally and returned:

    radius-two lattice points: 19
    anchored six-sets: 54
    dihedral/translation orbits: 3

No floating-point computation, CI result, heuristic, or unexecuted verifier is a proof
premise.
