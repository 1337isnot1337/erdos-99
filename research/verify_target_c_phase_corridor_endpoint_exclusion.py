#!/usr/bin/env python3
"""Numerical regression for Target C Section 102.

This only protects the scalar geometry used by the endpoint-exclusion proof:
- recompute the Section-101 root theta_8;
- verify the endpoint complement identity;
- verify the three corridor projective separations are theta_8/2,
  theta_8/2, and pi-theta_8;
- verify all stay a fixed positive distance from pi/3.
"""

import math


def F(theta: float) -> float:
    return 3.0 * theta - 2.0 * math.pi - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def bisect(lo: float, hi: float, steps: int = 120) -> float:
    assert F(lo) < 0.0 < F(hi)
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        if F(mid) <= 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def projective_distance(a: float, b: float) -> float:
    d = abs(a - b) % math.pi
    return min(d, math.pi - d)


def main() -> None:
    theta = bisect(2.0 * math.pi / 3.0, math.pi)
    phi = 2.0 * math.pi - 2.0 * theta
    U = 3.0 * theta - 2.0 * math.pi
    mu = math.sin(theta / 2.0)

    # Normalize the endpoint support as
    # {0}, gap theta, {theta}, gap phi, dense arc U, gap phi.
    mids = [
        theta / 2.0,
        theta + phi / 2.0,
        2.0 * math.pi - phi / 2.0,
    ]
    # Chord direction is midpoint + pi/2; adding pi/2 to both arguments
    # does not change projective separation.
    seps = sorted(
        projective_distance(mids[i], mids[j])
        for i in range(3)
        for j in range(i + 1, 3)
    )
    expected = sorted([math.pi - theta, theta / 2.0, theta / 2.0])

    for got, want in zip(seps, expected):
        assert abs(got - want) < 5e-15

    phase_sep = math.pi / 3.0
    margin = min(abs(s - phase_sep) for s in seps)

    assert abs(theta - 2.7029080296483677) < 5e-15
    assert abs(mu - 0.9760407652670520) < 5e-15
    assert abs(theta + 2.0 * phi + U - 2.0 * math.pi) < 5e-15
    assert margin > 0.30

    print(f"theta_8={theta:.16f}")
    print(f"mu_8={mu:.16f}")
    print("corridor_separations=" + ",".join(f"{x:.16f}" for x in seps))
    print(f"phase_separation={phase_sep:.16f}")
    print(f"minimum_margin={margin:.16f}")


if __name__ == "__main__":
    main()
