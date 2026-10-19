#!/usr/bin/env python3
"""Independent integer-arithmetic audit of six PR #106 comparators.

The source construction and exact target head are pinned in README.md and
SOURCES.json. No assertions are used, so the checks remain active under -O.
"""

from fractions import Fraction
from math import isqrt


RADII = (16, 25, 36, 64, 100, 256)
EXPECTED = {
    16: (657, 847, 190),
    25: (1809, 2135, 326),
    36: (4067, 4543, 476),
    64: (13723, 14615, 892),
    100: (34397, 35813, 1416),
    256: (232941, 236625, 3684),
}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def minimal_p(radius: int) -> int:
    """Return the least positive p with 3 p^2 > R^2 by direct search."""
    p = 1
    while 3 * p * p <= radius * radius:
        p += 1
    need(3 * (p - 1) * (p - 1) <= radius * radius < 3 * p * p,
         f"R={radius}: p is not the required strict threshold")
    return p


def norm_numerator(m: int, n: int, a_num: int, den: int) -> int:
    """Return den times |m u+n v|^2 for Gram matrix [[1,a],[a,1]]."""
    return den * (m * m + n * n) + 2 * a_num * m * n


def ring_points(radius: int, s: int) -> set[tuple[Fraction, Fraction]]:
    """Build the exact rational ring from the pinned source formula."""
    result: set[tuple[Fraction, Fraction]] = set()
    for j in range(s + 1):
        divisor = s * s + j * j
        x = Fraction(radius * (s * s - j * j), divisor)
        y = Fraction(2 * radius * j * s, divisor)
        result.update(((x, y), (-y, x), (-x, -y), (y, -x)))
    return result


def strict_competitor(population: int, source_population: int,
                      diameter_upper_twice: int, source_diameter: int) -> bool:
    return population >= source_population and diameter_upper_twice < source_diameter


def audit(radius: int) -> tuple[int, int, int, int, int, int]:
    need(isqrt(radius) ** 2 == radius, f"R={radius}: expected a square radius")
    s = isqrt(radius)
    p = minimal_p(radius)
    a_num = radius * radius - p * p
    den = radius * radius + p * p
    b_num = 2 * radius * p

    # These integer inequalities are exactly 0 < a_R < 1/2.
    need(0 < a_num and 2 * a_num < den,
         f"R={radius}: rational Gram parameter is outside (0, 1/2)")
    need(a_num * a_num + b_num * b_num == den * den,
         f"R={radius}: rational basis vectors are not unit vectors")

    # Count every core source label: |m u+n v| <= R-2 and |n| >= 2.
    # Since Q >= (1-a)(m^2+n^2) > (m^2+n^2)/2, every point in the
    # radius-R source core has |m|,|n| < sqrt(2)R < 2R. This box is exhaustive.
    core = 0
    core_limit = den * (radius - 2) ** 2
    for n in range(-2 * radius, 2 * radius + 1):
        if abs(n) < 2:
            continue
        for m in range(-2 * radius, 2 * radius + 1):
            if norm_numerator(m, n, a_num, den) <= core_limit:
                core += 1

    chain = 2 * radius + 1
    ring = ring_points(radius, s)
    need(len(ring) == 4 * s,
         f"R={radius}: ring has {len(ring)} distinct labels, expected {4*s}")
    for x, y in ring:
        need(x * x + y * y == radius * radius,
             f"R={radius}: a ring point is not on the radius-R circle")
    chain_points = {(Fraction(j), Fraction(0))
                    for j in range(-radius, radius + 1)}
    expected_overlap = {(Fraction(radius), Fraction(0)),
                        (Fraction(-radius), Fraction(0))}
    need(ring & chain_points == expected_overlap,
         f"R={radius}: ring-chain overlap is not exactly the two endpoints")

    # Core labels have |n|>=2, so they cannot overlap the n=0 chain labels.
    # They also lie in radius R-2, so cannot overlap any radius-R ring label.
    source_n = core + chain + len(ring) - len(expected_overlap)
    source_diameter = 2 * radius
    need(len(chain_points) == chain,
         f"R={radius}: chain cardinality mismatch")
    need(source_n == EXPECTED[radius][0],
         f"R={radius}: source population {source_n} differs from frozen replay")
    # The whole source lies in the radius-R disk and contains both antipodes
    # (R,0),(-R,0), so its diameter is exactly 2R.

    # Count the comparator disk using integer cross multiplication:
    # 4 Q <= (2R-1)^2, where Q has denominator den.
    disk_limit = den * (2 * radius - 1) ** 2
    need(4 * den <= disk_limit,
         f"R={radius}: selected unit-distance witness lies outside the disk")
    comparator_n = 0
    boundary_n = 0
    selected: list[tuple[int, int]] = []
    special = {(0, 0), (1, 0)}
    for n in range(-2 * radius, 2 * radius + 1):
        for m in range(-2 * radius, 2 * radius + 1):
            q4 = 4 * norm_numerator(m, n, a_num, den)
            if q4 <= disk_limit:
                comparator_n += 1
                if q4 == disk_limit:
                    boundary_n += 1
                if (m, n) not in special and len(selected) < source_n - 2:
                    selected.append((m, n))

    need(comparator_n == EXPECTED[radius][1],
         f"R={radius}: comparator count {comparator_n} differs from frozen replay")
    excess = comparator_n - source_n
    need(excess == EXPECTED[radius][2] and excess > 0,
         f"R={radius}: comparator has insufficient or changed excess population")

    # Select exactly N points, forcing (0,0) and (1,0) into the subset. This
    # makes its minimum distance exactly one; separation of every subset
    # follows from the all-lattice-differences proof below.
    need(len(selected) == source_n - 2,
         f"R={radius}: could not select N-2 comparator points")
    selected_set = set(selected) | special
    need(len(selected_set) == source_n,
         f"R={radius}: same-cardinality subset contains duplicate labels")
    need((0, 0) in selected_set and (1, 0) in selected_set,
         f"R={radius}: unit-distance witness missing from selected subset")
    need(norm_numerator(1, 0, a_num, den) == den,
         f"R={radius}: selected unit-distance witness is not exactly unit")

    # For any nonzero integer difference (m,n), Q>=1. If one coordinate is
    # zero this is immediate. If mn>=0 and both are nonzero, Q>=m^2+n^2>=2.
    # If mn<0, put x=|m|, y=|n|: since 2a<1,
    # Q > x^2+y^2-xy = (x-y)^2+xy >= 1.
    # Thus every selected pair is separated by at least one.
    need(2 * (den - a_num) > den,
         f"R={radius}: opposite-sign nearest offset is not strictly longer than 1")

    # Every selected center has norm <= R-1/2, so pair distances are <=2R-1.
    comparator_diameter_upper = 2 * radius - 1
    need(strict_competitor(comparator_n, source_n,
                           comparator_diameter_upper, source_diameter),
         f"R={radius}: exact comparator does not improve D(N)")

    # Adversarial controls: equality at diameter 2R is not strict, and a
    # one-label deficit cannot be repaired by a strict diameter bound.
    need(not strict_competitor(comparator_n, source_n, 2 * radius,
                               source_diameter),
         f"R={radius}: equal-diameter control was incorrectly accepted")
    need(not strict_competitor(source_n - 1, source_n,
                               comparator_diameter_upper, source_diameter),
         f"R={radius}: one-label-deficit control was incorrectly accepted")

    return source_n, comparator_n, excess, boundary_n, p, core


def main() -> None:
    print("independent exact audit of six PR #106 same-cardinality comparators")
    print("R p core chain ring source_N comparator_N excess boundary_points diameter_upper")
    for radius in RADII:
        source_n, comparator_n, excess, boundary_n, p, core = audit(radius)
        print(radius, p, core, 2 * radius + 1, 4 * isqrt(radius),
              source_n, comparator_n, excess, boundary_n,
              2 * radius - 1)
    print("PASS: all six source populations, separation checks, cardinality controls, and strict-diameter comparisons")


main()
