#!/usr/bin/env python3
"""Exact finite stress duals and a complete relaxed-packing penalty counterexample.

The 662-label relaxed cloud is not unit-separated. Its energy is certified below
the universal diameter-squared lower bound for every unit-separated 662-label
cloud, refuting the proposed global exact-penalty bridge. It is not an Erdos
counterexample. The general LP duality and unbounded claims are analytic proofs.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from itertools import combinations
from math import isqrt

from verify_global_convexity_exit_barrier_2026_10_12 import (
    Interval, PI, ROOT3, SCALE, q_geometry,
)

Point = tuple[F, F]


def distance2(p: Point, q: Point, vertical_factor: int) -> F:
    # The physical vertical coordinate is sqrt(vertical_factor) times its
    # rational coefficient, so all squared distances below are exact rationals.
    return (p[0]-q[0])**2 + vertical_factor*(p[1]-q[1])**2


def dot_edge(p: Point, q: Point, v: Point, w: Point, vertical_factor: int) -> F:
    return (p[0]-q[0])*(v[0]-w[0]) + vertical_factor*(p[1]-q[1])*(v[1]-w[1])


def finite_stress_dual(
    points: list[Point], vertical_factor: int, alpha_value: F,
    beta_value: F, dilation_dual: bool,
) -> dict[str, str | int]:
    distances = {
        (i, j): distance2(points[i], points[j], vertical_factor)
        for i, j in combinations(range(len(points)), 2)
    }
    assert all(value >= 1 for value in distances.values())
    diameter2 = max(distances.values())
    contacts = [edge for edge, value in distances.items() if value == 1]
    diameters = [edge for edge, value in distances.items() if value == diameter2]
    assert beta_value*len(diameters) == 1
    assert alpha_value*len(contacts) == diameter2
    residual = [[F(0), F(0)] for _ in points]
    for edges, value in ((contacts, alpha_value), (diameters, -beta_value)):
        for i, j in edges:
            for axis in (0, 1):
                force = value*(points[i][axis]-points[j][axis])
                residual[i][axis] += force
                residual[j][axis] -= force
    assert all(component == 0 for row in residual for component in row)
    cap = F(1, 2)
    primal = len(contacts)*max(F(0), alpha_value-cap)
    velocities = points if dilation_dual else [(F(0), F(0)) for _ in points]
    cwork = [dot_edge(points[i], points[j], velocities[i], velocities[j], vertical_factor)
             for i, j in contacts]
    hwork = [dot_edge(points[i], points[j], velocities[i], velocities[j], vertical_factor)
             for i, j in diameters]
    assert all(work <= 1 for work in cwork)
    dual = min(hwork) - cap*sum(max(F(0), work) for work in cwork)
    assert primal == dual == 0
    return {
        "labels": len(points), "contacts": len(contacts),
        "diameter_pairs": len(diameters), "squared_diameter": str(diameter2),
        "primal_excess": str(primal), "dual_work_score": str(dual),
    }


def sqrt_interval(value: Interval) -> Interval:
    assert value.lo >= 0
    lo = isqrt(value.lo*SCALE)
    hi = isqrt(value.hi*SCALE)
    if hi*hi < value.hi*SCALE:
        hi += 1
    return Interval(lo, hi)


def relaxed_cloud(k: int = 10) -> dict[str, int | str]:
    epsilon = F(1, k**3)
    spacing = 1 + 2*epsilon
    sites = [(i, j) for i in range(-k, k+1) for j in range(-k, k+1)
             if max(abs(i), abs(j), abs(i+j)) <= k]
    m = 3*k*(k+1)+1
    assert len(sites) == m
    points: list[Point] = []
    for i, j in sites:
        for sign in (-1, 1):
            points.append((spacing*(i+F(j, 2)) + sign*epsilon/2, spacing*F(j, 2)))
    n = len(points)
    assert n == 2*m
    short_pairs = pair_count = 0
    deficit = F(0)
    min_distance2: F | None = None
    max_distance2 = F(0)
    degrees = [0 for _ in points]
    for i, j in combinations(range(n), 2):
        d2 = distance2(points[i], points[j], 3)
        assert d2 > 0
        if d2 <= 1:
            assert i//2 == j//2 and d2 == epsilon**2
            short_pairs += 1
            degrees[i] += 1
            degrees[j] += 1
            deficit += 1-d2
        else:
            assert i//2 != j//2
        min_distance2 = d2 if min_distance2 is None else min(min_distance2, d2)
        max_distance2 = max(max_distance2, d2)
        pair_count += 1
    assert short_pairs == m and all(degree == 1 for degree in degrees)
    assert pair_count == n*(n-1)//2
    assert min_distance2 == epsilon**2
    assert max_distance2 == (2*k*spacing+epsilon)**2
    assert deficit == m*(1-epsilon**2)
    energy = max_distance2 + deficit/2

    b = Interval.exact(2) * ROOT3 * PI.reciprocal()
    hard_diameter_lower = sqrt_interval(
        b*Interval.exact(n-1) + Interval.exact(F(3, 4))
    ) - ROOT3.divided_by(2)
    assert hard_diameter_lower.lo > 0
    hard_squared_lower = hard_diameter_lower.squared()
    energy_interval = Interval.exact(energy)
    assert energy_interval.hi < hard_squared_lower.lo
    return {
        "hexagon_radius": k, "labels": n, "pairs_checked": pair_count,
        "short_pairs": short_pairs, "short_pair_graph_max_degree": max(degrees),
        "minimum_squared_distance": str(min_distance2),
        "maximum_squared_distance": str(max_distance2),
        "total_squared_distance_deficit": str(deficit),
        "half_penalty_energy": str(energy),
        "universal_hard_squared_diameter_lower_floor_times_1e12": (
            hard_squared_lower.lo // (SCALE // 10**12)
        ),
        "energy_advantage_lower_floor_times_1e12": (
            hard_squared_lower.lo - energy_interval.hi
        ) // (SCALE // 10**12),
    }


def main() -> None:
    # Rational checks for the D>=64 constant; sqrt(3)>173/100 and pi<22/7.
    assert F(173, 100)**2 < 3
    assert PI.hi < Interval.exact(F(22, 7)).lo
    assert F(111, 1211)-F(11, 448) > F(1, 16)
    square = [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1))]
    hexagon_with_center = [
        (F(0), F(0)), (F(1), F(0)), (F(1, 2), F(1, 2)),
        (-F(1, 2), F(1, 2)), (-F(1), F(0)),
        (-F(1, 2), -F(1, 2)), (F(1, 2), -F(1, 2)),
    ]
    _, rim_diameter, _ = q_geometry(501)
    rim_squared_diameter = rim_diameter.squared()
    rim_excess = rim_squared_diameter - Interval.exact(F(501, 2))
    assert rim_diameter.lo > 64*SCALE
    assert rim_excess.lo > rim_squared_diameter.hi//16
    print(json.dumps({
        "square_stress_dual": finite_stress_dual(square, 1, F(1, 2), F(1, 2), True),
        "hexagon_center_stress_dual": finite_stress_dual(
            hexagon_with_center, 3, F(1, 3), F(1, 3), False
        ),
        "overload_constant_rational_margin": str(F(111, 1211)-F(11, 448)-F(1, 16)),
        "q501_rim_excess_lower_floor_times_1e12": (
            rim_excess.lo // (SCALE // 10**12)
        ),
        "relaxed_penalty_counterexample": relaxed_cloud(),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
