#!/usr/bin/env python3
"""Scalar regression for Target C Section 101.

Checks the unique root of
    F(theta)=3 theta-2 pi-sin(theta/2)-2 sin(theta)
and the resulting wrapping threshold mu_8=sin(theta_8/2).
The geometric theorem is proved in Section 101; this file only protects arithmetic.
"""

import math


def F(theta: float) -> float:
    return (
        3.0 * theta
        - 2.0 * math.pi
        - math.sin(theta / 2.0)
        - 2.0 * math.sin(theta)
    )


def bisect(lo: float, hi: float, steps: int = 120) -> float:
    assert F(lo) < 0.0 < F(hi)
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        if F(mid) <= 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def cap_capacity(theta: float) -> float:
    k = math.floor(2.0 * math.pi / theta)
    r = 2.0 * math.pi - k * theta
    return (2.0 * math.pi - k * math.sin(theta) - math.sin(r)) / 8.0


def main() -> None:
    lo = 2.0 * math.pi / 3.0
    hi = math.pi

    # F'(theta)=3-(1/2)cos(theta/2)-2cos(theta)>0 on [2pi/3,pi).
    assert F(lo) < 0.0
    assert F(hi) > 0.0
    assert 3.0 - 0.5 * math.cos(lo / 2.0) - 2.0 * math.cos(lo) > 0.0
    assert 3.0 - 0.5 * math.cos(hi / 2.0) - 2.0 * math.cos(hi) > 0.0

    theta = bisect(lo, hi)
    mu = math.sin(theta / 2.0)
    phi = 2.0 * math.pi - 2.0 * theta
    U = 3.0 * theta - 2.0 * math.pi

    assert abs(theta - 2.7029080296483677) < 5e-15
    assert abs(mu - 0.9760407652670520) < 5e-15
    assert abs(F(theta)) < 5e-15
    assert abs((math.sin(theta / 2.0) + 2.0 * math.sin(theta)) - U) < 5e-15
    assert abs((theta + 2.0 * phi) - (4.0 * math.pi - 3.0 * theta)) < 5e-15

    C = cap_capacity(theta)
    gamma = math.pi / 4.0 - C
    assert gamma > 0.20

    print(f"theta_8={theta:.16f}")
    print(f"mu_8={mu:.16f}")
    print(f"phi_8={phi:.16f}")
    print(f"U_8={U:.16f}")
    print(f"F(theta_8)={F(theta):.3e}")
    print(f"cap_gap={gamma:.16f}")


if __name__ == "__main__":
    main()
