#!/usr/bin/env python3
"""Exact rational check for the scalar multi-grain endpoint step.

The geometric extraction is proof-only and is documented in
docs/reports/target_c_multigrain_endpoint_capacity_2026-09-12.md.  This file
checks only the final scalar implication with Fraction arithmetic.  In
particular, it does not certify the carrier, the phase collapse, a planar
embedding, a KKT stress, a source cardinality, or global minimum-diameter
optimality.
"""

from __future__ import annotations

from fractions import Fraction


def quadratic(s: Fraction, cap: Fraction, train: Fraction, edges: Fraction) -> Fraction:
    """Mantel/capacity polynomial whose positive root bounds the excess S."""

    return s * s + cap * s + cap * train - 4 * edges


def main() -> None:
    # Conservative constants are written as exact rationals, rounded in the
    # safe direction from the proof-only carrier extraction.
    area_floor = Fraction(4703752, 10_000_000)
    defect = Fraction(5317, 1000)
    angle_threshold = Fraction(10_000)
    prune = Fraction(1, 100_000)
    train_precise = Fraction(18_488, 10_000)

    retained = area_floor - defect / angle_threshold - prune * train_precise
    retained_floor = Fraction(4697, 10_000)
    assert retained > retained_floor

    edge_mass = retained_floor
    train = Fraction(18_488, 10_000)
    bad = Fraction(1_163, 10_000)
    route = Fraction(18_693, 10_000)
    cap = 3 * bad
    test_excess = Fraction(9_499, 10_000)

    # If p(S)=S^2+cap*S+cap*train-4*edge_mass, then p is strictly
    # increasing on S>=0.  Its value at test_excess is negative, so the
    # positive Mantel-forced root is strictly larger than test_excess.
    p_at_test = quadratic(test_excess, cap, train, edge_mass)
    assert p_at_test < 0
    assert quadratic(Fraction(0), cap, train, edge_mass) < 0

    endpoint_margin = 2 * test_excess - route
    # The conservative test point gives equality here.  The strict inequality
    # in the proof comes from p(test_excess)<0, hence S>test_excess.
    assert endpoint_margin == Fraction(305, 10_000)

    print(f"retained_edge_mass_lower={retained}")
    print(f"polynomial_at_S_0.9499={p_at_test}")
    print(f"forced_excess_lower={test_excess}")
    print(f"route_endpoint_margin={endpoint_margin}")
    print("PASS: exact rational multi-grain scalar contradiction")


if __name__ == "__main__":
    main()
