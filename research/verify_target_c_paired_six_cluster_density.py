#!/usr/bin/env python3
"""Scalar regression for Target C proof-only Section 100.

This checks the unique scalar root after the exact paired-piece translation bound.
It does not certify the geometric indexing or finite-to-limit density argument.
"""

from __future__ import annotations

import math


PI = math.pi


def scalar_gap(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - 3.0 * math.sin(theta)


def bisect_root(lo: float, hi: float, iterations: int = 100) -> float:
    flo = scalar_gap(lo)
    fhi = scalar_gap(hi)
    assert flo < 0.0 < fhi
    for _ in range(iterations):
        mid = (lo + hi) / 2.0
        if scalar_gap(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    theta_6 = bisect_root(2.0 * PI / 3.0, PI)
    mu_6 = math.sin(theta_6 / 2.0)

    assert abs(3.0 * theta_6 - 2.0 * PI - 3.0 * math.sin(theta_6)) < 5e-14
    assert abs(theta_6 - 2.605325674600903) < 5e-15
    assert abs(mu_6 - 0.9642670742838973) < 5e-15

    support_measure = 3.0 * theta_6 - 2.0 * PI
    alpha = support_measure / 2.0
    assert abs(alpha - 1.5 * math.sin(theta_6)) < 5e-14

    mu_5 = math.sqrt(1.0 - (PI / 9.0) ** 2)
    assert mu_6 > mu_5

    # F(theta)=3theta-2pi-3sin(theta) is strictly increasing on the live interval.
    for j in range(1, 1000):
        theta = 2.0 * PI / 3.0 + (PI / 3.0) * j / 1000.0
        assert 3.0 * (1.0 - math.cos(theta)) > 0.0

    print(f"theta_6={theta_6:.16f}")
    print(f"mu_6={mu_6:.16f}")
    print(f"mu_6-mu_5={mu_6 - mu_5:.16e}")
    print(f"support_measure={support_measure:.16f}")
    print(f"alpha={alpha:.16f}")


if __name__ == "__main__":
    main()
