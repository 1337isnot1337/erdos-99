#!/usr/bin/env python3
"""Numerical regression for Target C Section 107.

Checks the sigma=1e-3 stability window and the uniform circular-segment area floor.
The geometric area identity itself is proved in the accompanying report.
"""

import math


THETA8 = 2.7029080296483676832
SIGMA_STAR = 1.0e-3


def sigma(theta: float) -> float:
    return (
        3.0 * theta
        - 2.0 * math.pi
        - math.sin(theta / 2.0)
        - 2.0 * math.sin(theta)
    )


def root_for_sigma(target: float) -> float:
    lo = THETA8
    hi = THETA8 + 0.01
    assert sigma(lo) <= target <= sigma(hi)
    for _ in range(160):
        mid = (lo + hi) / 2.0
        if sigma(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def f(x: float) -> float:
    return math.sin(x / 2.0)


def segment_area(x: float) -> float:
    return (x - math.sin(x)) / 8.0


def transfer_barrier(theta: float, delta: float) -> float:
    phi = 2.0 * math.pi - 2.0 * theta
    return f(theta - delta) + f(phi + delta) - f(theta) - f(phi)


def transfer_derivative(theta: float, delta: float) -> float:
    phi = 2.0 * math.pi - 2.0 * theta
    return 0.5 * (
        math.cos((phi + delta) / 2.0)
        - math.cos((theta - delta) / 2.0)
    )


def main() -> None:
    theta_bar = root_for_sigma(SIGMA_STAR)
    mu_bar = math.sin(theta_bar / 2.0)
    phi8 = 2.0 * math.pi - 2.0 * THETA8
    q_star = (13.0 / 3.0) * SIGMA_STAR

    assert abs(theta_bar - 2.7031207076068693) < 5e-15
    assert abs(mu_bar - 0.9760638978066385) < 5e-15

    # The coarse delta=0.1 branch is separated from sigma=1e-3 by a factor > 32.
    barriers = [
        transfer_barrier(THETA8, 0.1),
        transfer_barrier(theta_bar, 0.1),
    ]
    assert min(barriers) > 0.0326

    # h'_theta(delta) decreases in delta and increases in theta, so this is the
    # relevant corner minimum on theta in [theta8, theta_bar], delta in [0,0.1].
    derivative_floor = transfer_derivative(THETA8, 0.1)
    assert derivative_floor > 0.3084
    assert derivative_floor > 0.30

    uniform_area_floor = (
        math.pi / 4.0
        - segment_area(theta_bar)
        - 2.0 * segment_area(phi8 + q_star)
        - segment_area(q_star)
    )
    endpoint_area = (
        math.pi / 4.0
        - segment_area(THETA8)
        - 2.0 * segment_area(phi8)
    )

    assert uniform_area_floor > 0.473
    assert abs(uniform_area_floor - 0.47310762602268286) < 5e-15
    assert abs(endpoint_area - 0.47355098050827765) < 5e-15

    # Sanity check for superadditivity on the small tail budget.
    a = q_star * 0.37
    b = q_star - a
    assert segment_area(a) + segment_area(b) <= segment_area(q_star)

    print(f"theta_bar={theta_bar:.16f}")
    print(f"mu_bar={mu_bar:.16f}")
    print(f"delta_01_barrier_min={min(barriers):.16f}")
    print(f"transfer_derivative_floor={derivative_floor:.16f}")
    print(f"q_star={q_star:.16f}")
    print(f"uniform_area_floor={uniform_area_floor:.16f}")
    print(f"endpoint_area={endpoint_area:.16f}")


if __name__ == "__main__":
    main()
