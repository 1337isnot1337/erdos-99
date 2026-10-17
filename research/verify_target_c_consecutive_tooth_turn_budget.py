#!/usr/bin/env python3
"""Arithmetic certificate for the consecutive-tooth turn budget.

The proof of the finite inequality is analytic and is recorded in
target_c_consecutive_tooth_turn_budget_2026-09-12.md.  This script checks the
monotonicity/convexity constants and the displayed small-base margins.  It does
not certify a global minimizer, the Section-124/125 inputs, or C-II closure.
"""

from __future__ import annotations

import math


def f(e: float) -> float:
    return math.pi / 3.0 - math.acos((1.0 + e) / 2.0)


def main() -> None:
    # The endpoint chord bound follows from convexity of f and f(1)=pi/3.
    grid = [i / 10000.0 for i in range(10000)]
    max_chord_error = max(f(e) - math.pi * e / 3.0 for e in grid)
    assert max_chord_error <= 1.0e-14

    for eta in (0.001, 0.01, 0.1, 0.25):
        slope = 1.0 / math.sqrt(4.0 - (1.0 + eta) ** 2)
        max_tangent_error = max(f(e) - slope * e for e in grid if e <= eta)
        assert max_tangent_error <= 1.0e-13
        lower = math.pi / slope
        print(f"eta={eta:.3f} small_base_lower={lower:.12f}")

    print(f"max_endpoint_chord_error={max_chord_error:.3e}")
    print(f"universal_all_tooth_excess_lower={3.0:.12f}")
    print(f"small_base_limit={math.pi * math.sqrt(3.0):.12f}")
    assert math.pi * math.sqrt(3.0) > 5.44


if __name__ == "__main__":
    main()
