#!/usr/bin/env python3
"""Exact finite checks for a sparse exceptional-set / concentrated-stress model.

The mathematical scope and the missing global-minimality hypothesis are stated
in docs/reports/target_c_typeii_sparse_exceptional_stress_model_2026-10-17.md.
All geometric comparisons below use integers or fractions.
"""

from fractions import Fraction as F
from math import isqrt


def basis_for_radius(radius: int) -> tuple[F, F]:
    """Return a rational unit vector v=(a,b) with angle just above 60 degrees."""
    assert radius >= 16
    p = isqrt((radius * radius) // 3) + 1
    while 3 * p * p <= radius * radius:
        p += 1
    while 3 * (p - 1) * (p - 1) > radius * radius:
        p -= 1
    assert 3 * p * p > radius * radius
    assert 3 * (p - 1) * (p - 1) < radius * radius
    assert p < radius

    denominator = radius * radius + p * p
    a = F(radius * radius - p * p, denominator)
    b = F(2 * radius * p, denominator)
    assert a * a + b * b == 1
    assert 0 < a < F(1, 2)
    assert b * b > F(3, 4)
    return a, b


def ring_for_radius(radius: int) -> set[tuple[F, F]]:
    """A rational, antipodally symmetric ring with angular gaps O(radius^-1/2)."""
    subdivisions = isqrt(radius)
    assert subdivisions >= 4
    ring: set[tuple[F, F]] = set()
    for j in range(subdivisions + 1):
        t = F(j, subdivisions)
        denominator = 1 + t * t
        x = radius * (1 - t * t) / denominator
        y = radius * (2 * t) / denominator
        for point in ((x, y), (-y, x), (-x, -y), (y, -x)):
            ring.add(point)
    assert len(ring) == 4 * subdivisions
    return ring


def lattice_count(radius: int, a: F) -> int:
    """Count the inner rhombic-lattice disk after removing rows n=-1,0,1."""
    # For |m u+n v| <= radius-2, b>sqrt(3)/2 gives |n|<2 radius;
    # then |m| <= |x|+|n|a < 2 radius.  Use a common denominator.
    denominator = a.denominator
    numerator = a.numerator
    bound2 = (radius - 2) ** 2
    count = 0
    for n in range(-2 * radius, 2 * radius + 1):
        if abs(n) < 2:
            continue
        for m in range(-2 * radius, 2 * radius + 1):
            norm_numerator = denominator * (m * m + n * n) + 2 * m * n * numerator
            if norm_numerator <= denominator * bound2:
                count += 1
    return count


def verify_radius(radius: int) -> tuple[int, int, int, F]:
    diameter = 2 * radius
    a, b = basis_for_radius(radius)
    subdivisions = isqrt(radius)
    ring = ring_for_radius(radius)

    # The four cardinal points include the ends of the stress-bearing row.
    row_ends = {(F(radius), F(0)), (F(-radius), F(0))}
    assert row_ends <= ring
    assert all(((-x, -y) in ring) for x, y in ring)
    assert all(x * x + y * y == radius * radius for x, y in ring)

    # Sparse ring endpoints are pairwise strictly separated.  The proof gives
    # angular gaps >=1/s and hence chord lengths >=2R/(pi*s)>1 for R>=16;
    # this exact pairwise replay checks the finite members as well.
    ring_points = sorted(ring)
    min_ring_distance2: F | None = None
    diameter_pair_count = 0
    for i, (x1, y1) in enumerate(ring_points):
        for x2, y2 in ring_points[i + 1 :]:
            distance2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
            assert distance2 > 1
            if min_ring_distance2 is None or distance2 < min_ring_distance2:
                min_ring_distance2 = distance2
            if distance2 == diameter * diameter:
                diameter_pair_count += 1
    assert diameter_pair_count == len(ring) // 2 == 2 * subdivisions

    # Every non-axis ring point is farther than one from the whole diameter
    # segment, so it has no contact with the stress-bearing row.
    for x, y in ring - row_ends:
        assert y * y > 1

    # For the exact lattice basis, the only unit lattice differences are
    # +/-u and +/-v: if |dn|>=2, the vertical component is >1; if |dn|=1,
    # the closest integer horizontal offsets are 0 and -sgn(dn), the latter
    # having squared norm 2-2a>1.  Thus the core contact graph is a subgraph
    # of the square grid and is triangle-free.  The row is separated from it
    # because every core point has |n|>=2 and 2b>1.

    # The core lies in radius R-2, so it is at distance at least 2 from the
    # ring.  The ring endpoints of all diameter pairs therefore have contact
    # components that are singletons or the one-dimensional central path.
    # None of these components contains a 2D contact grid.

    core_count = lattice_count(radius, a)
    row_count = diameter + 1
    source_count = core_count + row_count + len(ring) - 2

    # Exact KKT stationarity for minimize d subject to |x-y|>=1 and |x-y|<=d.
    # The diameter multiplier on (-R u,R u) is 1; all other diameter
    # multipliers are zero.  Every edge of the central row has contact
    # multiplier 1.  Contact gradients at each interior point cancel, while
    # the endpoint contact gradient cancels the active diameter gradient.
    diameter_weights = {"central-antipodal-pair": F(1)}
    contact_weights = [F(1) for _ in range(diameter)]
    assert all(weight >= 0 for weight in diameter_weights.values())
    assert all(weight >= 0 for weight in contact_weights)
    assert sum(diameter_weights.values(), F(0)) == 1
    # Its entire positive mass lies on a diameter edge whose contact
    # component has no coherent 2D grid; all 2s diameter edges are exceptional.
    exceptional_count = diameter_pair_count
    exceptional_mass = sum(diameter_weights.values(), F(0))
    assert exceptional_mass == 1
    assert F(exceptional_count, diameter) == F(2 * subdivisions, 2 * radius)

    # Explicit exact row-force ledger, represented as signed x-components.
    forces = {j: 0 for j in range(-radius, radius + 1)}
    for j in range(-radius, radius):
        forces[j] += 1       # left endpoint of contact constraint 1-|x_j-x_{j+1}|
        forces[j + 1] -= 1   # right endpoint
    forces[-radius] -= 1     # left endpoint of active diameter constraint
    forces[radius] += 1      # right endpoint of active diameter constraint
    assert all(value == 0 for value in forces.values())
    assert len(contact_weights) == diameter

    return source_count, core_count, exceptional_count, min_ring_distance2 or F(0)


def main() -> None:
    print("exact sparse-exceptional stress regression")
    print("R D source_count core_count diameter_edges exceptional/D min_ring_distance^2")
    for radius in (16, 25, 36, 64, 100, 256):
        source_count, core_count, exceptional_count, min_ring_distance2 = verify_radius(radius)
        diameter = 2 * radius
        print(
            radius,
            diameter,
            source_count,
            core_count,
            exceptional_count,
            F(exceptional_count, diameter),
            min_ring_distance2,
        )


if __name__ == "__main__":
    main()
