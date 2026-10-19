#!/usr/bin/env python3
"""Exact same-cardinality strict-diameter competitors for six PR #95 cases.

Inputs and scope are pinned in SOURCES.json and README.md. All counts and
distance comparisons use rational arithmetic; no third-party modules are used.
"""

from fractions import Fraction as F
from math import isqrt


RADII = (16, 25, 36, 64, 100, 256)


def basis(radius: int) -> tuple[F, F]:
    """Copy the PR #95 rational unit basis definition for an independent count."""
    p = isqrt((radius * radius) // 3) + 1
    while 3 * p * p <= radius * radius:
        p += 1
    while 3 * (p - 1) * (p - 1) > radius * radius:
        p -= 1
    denominator = radius * radius + p * p
    a = F(radius * radius - p * p, denominator)
    b = F(2 * radius * p, denominator)
    assert a * a + b * b == 1
    assert 0 < a < F(1, 2)
    assert b * b > F(3, 4)
    return a, b


def lattice_disk_count(radius: int, a: F, radius_bound: F) -> int:
    """Count integer (m,n) with |m u+n v| <= radius_bound exactly."""
    bound2 = radius_bound * radius_bound
    count = 0
    # Since b>sqrt(3)/2 and a<1/2, any point in this disk has |m|,|n|<2R.
    for n in range(-2 * radius, 2 * radius + 1):
        for m in range(-2 * radius, 2 * radius + 1):
            norm2 = F(m * m + n * n) + 2 * m * n * a
            if norm2 <= bound2:
                count += 1
    return count


def source_population(radius: int, a: F) -> tuple[int, int, int, int]:
    """Return source, core, chain, and ring populations from the pinned formula."""
    core = 0
    bound2 = (radius - 2) ** 2
    for n in range(-2 * radius, 2 * radius + 1):
        if abs(n) < 2:
            continue
        for m in range(-2 * radius, 2 * radius + 1):
            norm2 = F(m * m + n * n) + 2 * m * n * a
            if norm2 <= bound2:
                core += 1
    chain = 2 * radius + 1
    ring = 4 * isqrt(radius)
    # The ring intersects the chain exactly at the two antipodal endpoints.
    source = core + chain + ring - 2
    return source, core, chain, ring


def valid_strict_competitor(population: int, source_population: int,
                            comparator_radius: F, source_diameter: int) -> bool:
    return population >= source_population and 2 * comparator_radius < source_diameter


def verify(radius: int) -> tuple[int, int, int, int]:
    a, b = basis(radius)
    source_n, core_n, chain_n, ring_n = source_population(radius, a)
    comparator_radius = F(2 * radius - 1, 2)
    comparator_n = lattice_disk_count(radius, a, comparator_radius)
    source_diameter = 2 * radius

    assert valid_strict_competitor(comparator_n, source_n,
                                   comparator_radius, source_diameter)
    # Failure controls: equality of diameters and a one-point population deficit
    # must never be accepted by the comparison predicate.
    assert not valid_strict_competitor(source_n, source_n, F(radius), source_diameter)
    assert not valid_strict_competitor(source_n - 1, source_n,
                                       comparator_radius, source_diameter)

    # Exact lattice geometry: for a nonzero integer difference (m,n),
    # n=0 gives |m|>=1; |n|>=2 gives |n|b>1; |n|=1 has length 1 only
    # for m=0, while the nearest other horizontal offset has squared length
    # 2-2a>1. Thus every comparator subset is unit-separated and its contact
    # graph is a subgraph of the bipartite square grid.
    assert 2 * b > 1
    assert 2 - 2 * a > 1
    assert 2 * comparator_radius == source_diameter - 1

    return source_n, comparator_n, comparator_n - source_n, core_n + chain_n + ring_n


def main() -> None:
    print("exact PR #95 globality exclusion by a same-basis lattice disk")
    print("R source_N disk_radius comparator_N excess comparator_diameter")
    for radius in RADII:
        source_n, comparator_n, excess, component_sum = verify(radius)
        assert source_n == component_sum - 2
        print(radius, source_n, F(2 * radius - 1, 2), comparator_n,
              excess, 2 * radius - 1)


main()
