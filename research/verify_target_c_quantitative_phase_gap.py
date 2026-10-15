#!/usr/bin/env python3
"""Numerical regression for proof-only Target C Section 104.

This script checks only scalar constants used by the proof.  The geometric stability,
outer-ledger bookkeeping, and directional-length arguments remain theorem work.
"""

from __future__ import annotations

import math


PI = math.pi
SIGMA_TARGET = 1.0e-7


def sigma(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def bisect_level(target: float, lo: float, hi: float, steps: int = 140) -> float:
    assert sigma(lo) <= target <= sigma(hi)
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        if sigma(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def cap_capacity(mu: float) -> float:
    theta = 2.0 * math.asin(mu)
    k = math.floor(2.0 * PI / theta)
    rem = 2.0 * PI - k * theta
    return (2.0 * PI - k * math.sin(theta) - math.sin(rem)) / 8.0


def f(x: float) -> float:
    return math.sin(x / 2.0)


def main() -> None:
    theta8 = bisect_level(0.0, 2.0 * PI / 3.0, PI)
    mu8 = math.sin(theta8 / 2.0)
    theta9 = bisect_level(SIGMA_TARGET, theta8, PI)
    mu9 = math.sin(theta9 / 2.0)

    assert abs(theta8 - 2.7029080296483677) < 5e-15
    assert abs(mu8 - 0.9760407652670520) < 5e-15
    assert abs(theta9 - 2.7029080509166894) < 5e-15
    assert abs(mu9 - 0.9760407675809150) < 5e-15
    assert mu9 - mu8 > 2.31e-9
    assert abs(sigma(theta9) - SIGMA_TARGET) < 5e-15

    gamma9 = PI / 4.0 - cap_capacity(mu9)
    assert gamma9 > 0.2023

    # Lemma 104.1: the coarse 0.1 displacement already costs >0.0326,
    # and the derivative of the transfer cost stays >0.30 on the whole box.
    coarse_cost = (
        f(theta9 - 0.1)
        + f((2.0 * PI - 2.0 * theta9) + 0.1)
        - f(theta9)
        - f(2.0 * PI - 2.0 * theta9)
    )
    assert coarse_cost > 0.0326
    for i in range(101):
        theta = theta8 + (theta9 - theta8) * i / 100.0
        phi = 2.0 * PI - 2.0 * theta
        for j in range(101):
            delta = 0.1 * j / 100.0
            derivative = (
                0.5 * math.cos((phi + delta) / 2.0)
                - 0.5 * math.cos((theta - delta) / 2.0)
            )
            assert derivative > 0.30

    # Section-90 pre-pruning shores from r=0.18 and C_T=6.
    r = 0.18
    c_t = 6.0
    alpha0 = r / (32.0 * c_t)
    endpoint_density = 2.0 * alpha0
    assert abs(alpha0 - 0.0009375) < 1e-15
    assert abs(endpoint_density - 0.001875) < 1e-15

    # Section 104.8 leakage constants.
    h = 1.0 / 2000.0
    w_h = PI / 3.0 - math.acos((1.0 + h) / 2.0)
    leakage = w_h + (12169.0 / 6.0) * SIGMA_TARGET
    assert w_h < 0.000289
    assert leakage < 0.000492
    remaining = endpoint_density - leakage
    assert remaining > 0.001383
    assert remaining / 3.0 > 0.00045

    # Principal corridor geometry remains very far from pi/3.
    endpoint_margin = theta8 / 2.0 - PI / 3.0
    assert endpoint_margin > 0.30425
    # The proof uses sharper 43/6 and 73/6 coefficients; this coarse check is enough.
    assert endpoint_margin - (73.0 / 6.0) * SIGMA_TARGET > 0.3042

    # Section 104.9 alignment estimate using rho=0.00045 and route slack 19 sigma/6.
    rho = 0.00045
    route_slack = (19.0 / 6.0) * SIGMA_TARGET
    delta_bound = math.sqrt(PI * PI * route_slack / (2.0 * rho))
    assert delta_bound < 0.059
    assert 2.0 * delta_bound < 0.118
    assert 2.0 * delta_bound < 0.3042

    print(f"theta_8={theta8:.16f}")
    print(f"mu_8={mu8:.16f}")
    print(f"theta_9={theta9:.16f}")
    print(f"mu_9={mu9:.16f}")
    print(f"mu_9-mu_8={mu9 - mu8:.16e}")
    print(f"sigma(theta_9)={sigma(theta9):.16e}")
    print(f"Gamma(mu_9)={gamma9:.16f}")
    print(f"coarse_gap_cost={coarse_cost:.16f}")
    print(f"w_h={w_h:.16e}")
    print(f"leakage={leakage:.16e}")
    print(f"remaining_endpoint_density={remaining:.16e}")
    print(f"alignment_delta_bound={delta_bound:.16e}")


if __name__ == "__main__":
    main()
