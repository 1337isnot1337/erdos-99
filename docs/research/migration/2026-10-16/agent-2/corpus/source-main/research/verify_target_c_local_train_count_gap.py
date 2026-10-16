#!/usr/bin/env python3
"""Scalar regression for proof-only Target C Section 110 local-train-count phase-gap candidate."""

from __future__ import annotations

import math


PI = math.pi
THETA8 = 2.7029080296483676832
MU8 = 0.9760407652670519821
SIGMA_STAR = 1.8e-4


def sigma(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def root(target: float) -> float:
    lo, hi = THETA8, THETA8 + 0.01
    assert sigma(lo) <= target <= sigma(hi)
    for _ in range(160):
        mid = (lo + hi) / 2.0
        if sigma(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    theta = root(SIGMA_STAR)
    mu = math.sin(theta / 2.0)
    U = 3.0 * theta - 2.0 * PI

    assert abs(theta - 2.7029463124571330) < 5e-15
    assert abs(mu - 0.9760449300231616) < 5e-15
    assert mu - MU8 > 4.16e-6

    # Exact outer-ledger train bound: T/D <= U + 2 sigma + o(1).
    train_bound = U + 2.0 * SIGMA_STAR
    assert train_bound < 1.83

    # Phase extraction with R >= .472 D^2, T <= 1.83 D.
    good = 0.471 - 5.317 / 5000.0
    internal = (99.0 / 100.0) * good / 3.0
    shore = 0.04
    small_capacity = 2.0 * shore * 1.83
    assert internal > 0.155079
    assert abs(small_capacity - 0.1464) < 1e-15
    assert internal > small_capacity
    endpoint_supply = 2.0 * shore
    assert abs(endpoint_supply - 0.08) < 1e-15

    # Leakage and exact-cosine projection contradiction.
    h = 0.0176
    w = PI / 3.0 - math.acos((1.0 + h) / 2.0)
    leakage = w + (1.0 / h + 169.0 / 6.0) * SIGMA_STAR
    rho = 0.018
    remaining = endpoint_supply - leakage
    assert leakage < 0.025489
    assert remaining / 3.0 > rho
    delta = math.acos(1.0 - SIGMA_STAR / rho)
    geometric = THETA8 / 2.0 - PI / 3.0 - (73.0 / 6.0) * SIGMA_STAR
    margin = geometric - 2.0 * delta
    assert delta < 0.14154
    assert geometric > 0.302066
    assert margin > 0.01898

    print(f"theta_14={theta:.16f}")
    print(f"mu_14={mu:.16f}")
    print(f"mu_14_minus_mu_8={mu - MU8:.16e}")
    print(f"train_bound={train_bound:.12f}")
    print(f"good_crossings={good:.12f}")
    print(f"internal_bin={internal:.12f}")
    print(f"small_shore_capacity={small_capacity:.12f}")
    print(f"leakage={leakage:.12f}")
    print(f"rho={rho:.12f}")
    print(f"delta={delta:.12f}")
    print(f"contradiction_margin={margin:.12f}")


if __name__ == "__main__":
    main()
