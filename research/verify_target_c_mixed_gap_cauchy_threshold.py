#!/usr/bin/env python3
"""Scalar regression certificate for Target C proof-only Section 99.

The geometry is proved in the theorem module. This script checks the one-dimensional
root and the numerical inequalities used to record

    H(theta) = (7/2) sin(theta)
             + sin(2 theta - pi - (3/2) sin(theta))
             - pi sin(theta/2),

with the unique live root theta_6 and mu_6=sin(theta_6/2).
"""

import math


def H(theta: float) -> float:
    return (
        3.5 * math.sin(theta)
        + math.sin(2.0 * theta - math.pi - 1.5 * math.sin(theta))
        - math.pi * math.sin(theta / 2.0)
    )


def Hprime(theta: float) -> float:
    a = 2.0 * theta - math.pi - 1.5 * math.sin(theta)
    return (
        3.5 * math.cos(theta)
        + (2.0 - 1.5 * math.cos(theta)) * math.cos(a)
        - 0.5 * math.pi * math.cos(theta / 2.0)
    )


def bisect(lo: float, hi: float, steps: int = 120) -> float:
    assert H(lo) > 0.0 > H(hi)
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        if H(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    theta5 = 2.0 * math.acos(math.pi / 9.0)
    mu5 = math.sqrt(1.0 - (math.pi / 9.0) ** 2)
    hi = 2.5

    assert H(theta5) > 0.0
    assert H(hi) < 0.0

    # Regression check for the analytic monotonicity proof in Section 99.5.
    # The theorem proves H'<0 by a closed-form upper bound; this dense check is only
    # intended to catch transcription/sign regressions in H and H'.
    for i in range(10001):
        t = theta5 + (hi - theta5) * i / 10000.0
        assert Hprime(t) < 0.0

    theta6 = bisect(theta5, hi)
    mu6 = math.sin(theta6 / 2.0)

    assert abs(theta6 - 2.4452001949244801) < 5e-15
    assert abs(mu6 - 0.9399896933531978) < 5e-15
    assert abs(H(theta6)) < 5e-15
    assert mu6 > mu5
    assert mu6 > 0.9362157414095831

    print(f"theta_5={theta5:.16f}")
    print(f"mu_5={mu5:.16f}")
    print(f"H(theta_5)={H(theta5):.16e}")
    print(f"theta_6={theta6:.16f}")
    print(f"mu_6={mu6:.16f}")
    print(f"H(theta_6)={H(theta6):.3e}")
    print(f"improvement_over_mu5={mu6-mu5:.16f}")


if __name__ == "__main__":
    main()
