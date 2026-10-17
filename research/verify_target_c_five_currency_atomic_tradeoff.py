#!/usr/bin/env python3
"""Exact-scalar checks for the five-currency/atomic-capacity bridge.

This script checks only the displayed finite-limit algebra and the scalar
regression.  It does not construct a source, certify global optimality, or
prove the imported geometric hypotheses.
"""

from __future__ import annotations

import math


PI = math.pi
DELTA_2 = PI / (2.0 * math.sqrt(3.0))
S2 = math.sqrt(DELTA_2)


def u_n(delta: float, n: int = 7) -> float:
    total = (PI + delta) ** 2 / n
    total += (2.0 * delta * delta / n) * sum(
        (1.0 - j / n) * (36.0 * j * j - 1.0) ** 2
        for j in range(1, n)
    )
    return total


def r_n(delta: float, n: int = 7) -> float:
    return max(0.0, 4.0 * S2 - math.sqrt(u_n(delta, n)))


def check_witness() -> None:
    t = 13.0 / 5.0
    kappa = 0.0
    s = 3.0
    g = 0.5
    q = 0.7
    f = 0.7
    u_b = 1.0

    assert abs((q + u_b) - (2.0 * t - s - g - kappa)) < 1e-12
    delta = 2.0 * t - PI - q
    assert delta > 0.0
    assert abs((q + 4.0 * f) - (2.0 * t - PI - delta + 4.0 * f)) < 1e-12

    # The high-density witness is not challenged by the Fejer term: its
    # detour is large enough that the positive-part lower demand vanishes.
    assert r_n(delta) == 0.0
    rhs = 0.5 * max(PI + delta, s + g + kappa) + r_n(delta) / 10.0
    assert t > rhs


def check_frontier_branch() -> None:
    s = 2.798596312209462
    g = 0.2910434605114111
    assert s + g > PI - 0.052
    # The frontier profile is just below the activation threshold; this is a
    # regression against claiming an improvement there without extra slack.
    assert s + g < PI
    assert r_n(0.0) > 0.0


def main() -> None:
    check_witness()
    check_frontier_branch()
    print(f"Delta2={DELTA_2:.16f}")
    print(f"R7(0)={r_n(0.0):.16f}")
    print(f"witness_delta={2.0 * (13.0 / 5.0) - PI - 0.7:.16f}")
    print("five-currency atomic tradeoff: OK")


if __name__ == "__main__":
    main()
