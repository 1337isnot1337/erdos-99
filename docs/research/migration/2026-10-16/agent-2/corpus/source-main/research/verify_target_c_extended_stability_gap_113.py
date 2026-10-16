#!/usr/bin/env python3
"""Regression checks for proof-only Target C Section 113."""

from __future__ import annotations

import math

PI = math.pi
THETA8 = 2.702908029648367683220623341533134077952
MU8 = 0.9760407652670519820547242095879740469844
SIGMA = 1.4e-3
A = 0.085
C_T = 1.83
K = 5000.0
M = 500.0
C_PHASE = 5.317
H = 0.0488
E0 = 0.17


def sigma(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def root(target: float) -> float:
    lo = THETA8
    hi = THETA8 + 0.1
    for _ in range(160):
        mid = (lo + hi) / 2.0
        if sigma(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def G(x: float) -> float:
    return (x - math.sin(x)) / 8.0


def w(h: float) -> float:
    return PI / 3.0 - math.acos((1.0 + h) / 2.0)


def main() -> None:
    theta17 = root(SIGMA)
    mu17 = math.sin(theta17 / 2.0)
    phi8 = 2.0 * PI - 2.0 * THETA8
    qstar = (13.0 / 3.0) * SIGMA

    assert abs(theta17 - 2.703205775845796) < 5e-15
    assert abs(mu17 - 0.9760731474119142) < 5e-15
    assert mu17 - MU8 > 3.238e-5
    assert abs(sigma(theta17) - SIGMA) < 5e-15

    # Extended largest-gap derivative: monotonicity reduces the rectangle minimum
    # to (theta8, delta=0.1).
    delta = 0.1
    phi = 2.0 * PI - 2.0 * THETA8
    transfer_derivative = (
        0.5 * math.cos((phi + delta) / 2.0)
        - 0.5 * math.cos((THETA8 - delta) / 2.0)
    )
    assert transfer_derivative > 0.3084
    assert 0.1 * transfer_derivative > SIGMA

    # Section-107 circular-segment lower bound remains above the same 0.472 floor.
    area_floor = PI / 4.0 - G(theta17) - 2.0 * G(phi8 + qstar) - G(qstar)
    assert area_floor > 0.4729
    assert qstar < 0.0061
    phi17 = 2.0 * PI - 2.0 * theta17
    assert phi17 > 0.876
    assert qstar < phi17

    # Exact train budget.
    U = 3.0 * theta17 - 2.0 * PI
    train_ceiling = U + 2.0 * SIGMA
    assert train_ceiling < C_T

    # Finite joint-shore extraction.
    retained = 0.4719
    internal = (1.0 - 1.0 / M) * (retained - C_PHASE / K) / 3.0
    bad_capacity = A * C_T
    assert internal > bad_capacity
    assert internal - bad_capacity > 0.001

    # Wider leakage window.
    leakage = w(H) + (1.0 / H + 169.0 / 6.0) * SIGMA
    P = E0 - leakage
    assert leakage < 0.09654
    assert P > 0.07346

    # Aggregate two-family projection contradiction.
    mismatch = THETA8 / 2.0 - PI / 3.0 - (73.0 / 6.0) * SIGMA
    forced = 2.0 * P * (1.0 - math.cos(mismatch / 2.0))
    assert mismatch > 0.2872
    assert forced > 0.0015125
    assert forced - SIGMA > 0.0001125

    print(f"theta_17={theta17:.16f}")
    print(f"mu_17={mu17:.16f}")
    print(f"mu_17-mu_8={mu17 - MU8:.16e}")
    print(f"transfer_derivative_min={transfer_derivative:.16f}")
    print(f"area_floor={area_floor:.16f}")
    print(f"train_ceiling={train_ceiling:.16f}")
    print(f"internal_crossing_density={internal:.16f}")
    print(f"bad_bin_capacity={bad_capacity:.16f}")
    print(f"leakage={leakage:.16f}")
    print(f"principal_endpoint_density={P:.16f}")
    print(f"mismatch={mismatch:.16f}")
    print(f"forced_route_loss={forced:.16f}")
    print(f"contradiction_margin={forced - SIGMA:.16f}")


if __name__ == "__main__":
    main()
