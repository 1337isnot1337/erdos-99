#!/usr/bin/env python3
"""Scalar regression check for proof-only Target C Section 100.

The geometry is proved in the theorem module. This script only checks the unique
root of

    G(theta) = 3 theta - 2 pi - 3 sin(theta)

on [2 pi/3, pi), and the recorded value mu_7=sin(theta_7/2).

Baseline note: the mixed-gap Cauchy value below is now canonical Section 99 in
theorem-state audit.39. Section 100 is independent of that proof and only uses the
value as a regression comparison.
"""

import math


def G(theta: float) -> float:
    return 3.0 * theta - 2.0 * math.pi - 3.0 * math.sin(theta)


def bisect(lo: float, hi: float, steps: int = 120) -> float:
    assert G(lo) < 0.0 < G(hi)
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        if G(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    lo = 2.0 * math.pi / 3.0
    hi = math.pi - 1.0e-8

    # G'(theta)=3-3 cos(theta)>0 on the whole live interval.
    for i in range(10001):
        t = lo + (hi - lo) * i / 10000.0
        assert 3.0 - 3.0 * math.cos(t) > 0.0

    theta_7 = bisect(lo, hi)
    mu_7 = math.sin(theta_7 / 2.0)

    assert abs(theta_7 - 2.6053256746009027) < 5.0e-15
    assert abs(mu_7 - 0.9642670742838973) < 5.0e-15
    assert abs(G(theta_7)) < 5.0e-15

    # Regression comparisons against the lower established thresholds.
    mu_cauchy = math.sqrt(1.0 - (math.pi / 9.0) ** 2)
    mu_mixed = 0.9399896933531978
    mu_4 = 0.9362157414095831
    assert mu_7 > mu_mixed > mu_cauchy > mu_4

    print(f"theta_7={theta_7:.16f}")
    print(f"mu_7={mu_7:.16f}")
    print(f"G(theta_7)={G(theta_7):.3e}")
    print(f"improvement_over_mixed={mu_7-mu_mixed:.16f}")


if __name__ == "__main__":
    main()
