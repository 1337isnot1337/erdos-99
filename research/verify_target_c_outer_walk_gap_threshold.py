#!/usr/bin/env python3
"""Finite scalar regression for Target C Section 96.

Checks the unique root of
    F(theta)=3 theta-2 pi-(3/2) sin(theta)
on [2 pi/3, pi), and records the resulting wrapping threshold
    mu_4=sin(theta_4/2).
This is a regression certificate for the numerical constant only; the theorem is
proved geometrically in Section 96.
"""

import math


def F(theta: float) -> float:
    return 3.0 * theta - 2.0 * math.pi - 1.5 * math.sin(theta)


def bisect(lo: float, hi: float, steps: int = 100) -> float:
    flo = F(lo)
    fhi = F(hi)
    assert flo < 0.0 < fhi
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        if F(mid) <= 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    lo = 2.0 * math.pi / 3.0
    hi = math.pi
    assert F(lo) < 0.0
    assert F(hi) > 0.0

    # F'(theta)=3-(3/2)cos(theta) >= 3 on this interval.
    assert 3.0 - 1.5 * math.cos(lo) > 0.0
    assert 3.0 - 1.5 * math.cos(hi) > 0.0

    theta = bisect(lo, hi)
    mu = math.sin(theta / 2.0)

    assert abs(theta - 2.423405458475313) < 5e-15
    assert abs(mu - 0.9362157414095832) < 5e-15
    assert abs(F(theta)) < 5e-15

    print(f"theta_4={theta:.16f}")
    print(f"mu_4={mu:.16f}")
    print(f"F(theta_4)={F(theta):.3e}")


if __name__ == "__main__":
    main()
