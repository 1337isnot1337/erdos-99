#!/usr/bin/env python3
"""Regression certificate for Target C Section 112 aggregate projection."""

import math

PI = math.pi
THETA8 = 2.7029080296483676832
MU8 = 0.9760407652670519821
SIGMA = 1.0e-3
E0 = 0.16
H = 0.0413
CT = 1.83


def slack(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def root(target: float) -> float:
    lo, hi = THETA8, THETA8 + 0.02
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if slack(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    theta = root(SIGMA)
    mu = math.sin(theta / 2.0)
    U = 3.0 * theta - 2.0 * PI

    assert abs(theta - 2.7031207076068693) < 5e-15
    assert abs(mu - 0.9760638978066385) < 5e-15
    assert 2.31e-5 < mu - MU8 < 2.32e-5
    assert U + 2.0 * SIGMA < CT

    w = PI / 3.0 - math.acos((1.0 + H) / 2.0)
    leakage = w + (1.0 / H + 169.0 / 6.0) * SIGMA
    P = E0 - leakage
    assert abs(leakage - 0.0763930692197174) < 5e-15
    assert P > 0.08360

    mismatch = THETA8 / 2.0 - PI / 3.0 - (73.0 / 6.0) * SIGMA
    diff_case_cost = 2.0 * (1.0 - math.cos(mismatch / 2.0))
    same_case_cost = 2.0 - math.sqrt(3.0)
    forced = P * min(diff_case_cost, same_case_cost)

    assert mismatch > 0.29208
    assert diff_case_cost < same_case_cost
    assert abs(diff_case_cost - 0.0212912283958977) < 5e-15
    assert forced > 0.00178
    assert forced > SIGMA
    assert forced / SIGMA > 1.78

    print(f"theta16={theta:.16f}")
    print(f"mu16={mu:.16f}")
    print(f"gain={mu - MU8:.12e}")
    print(f"U={U:.16f}")
    print(f"T/D upper={U + 2.0 * SIGMA:.16f}")
    print(f"leakage={leakage:.16f}")
    print(f"principal endpoint density P={P:.16f}")
    print(f"corridor mismatch m={mismatch:.16f}")
    print(f"different-corridor cost={diff_case_cost:.16f}")
    print(f"same-corridor cost={same_case_cost:.16f}")
    print(f"forced projection loss={forced:.16f}")
    print(f"forced/slack={forced / SIGMA:.16f}")


if __name__ == "__main__":
    main()
