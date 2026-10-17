#!/usr/bin/env python3
"""Regression certificate for Target C Section 108."""

import math


THETA8 = 2.7029080296483676832
MU8 = 0.9760407652670519821
SIGMA_STAR = 4.5e-5


def sigma(theta: float) -> float:
    return (
        3.0 * theta
        - 2.0 * math.pi
        - math.sin(theta / 2.0)
        - 2.0 * math.sin(theta)
    )


def root_for_sigma(target: float) -> float:
    lo = THETA8
    hi = THETA8 + 0.01
    assert sigma(lo) <= target <= sigma(hi)
    for _ in range(160):
        mid = (lo + hi) / 2.0
        if sigma(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    theta = root_for_sigma(SIGMA_STAR)
    mu = math.sin(theta / 2.0)

    assert abs(theta - 2.7029176003825130) < 5e-15
    assert abs(mu - 0.9760418064930821) < 5e-15
    assert mu - MU8 > 1.04e-6
    assert SIGMA_STAR < 1e-3

    # Area-boosted Section-90 extraction.
    rhombi = 0.472
    after_phase_cut = 0.471
    K = 1000.0
    phase_defect_constant = 5.317
    good = after_phase_cut - phase_defect_constant / K
    label_pair = good / 3.0
    internal_bin = (19.0 / 20.0) * label_pair

    shore = 0.012
    train_constant = 6.0
    small_shore_capacity = 2.0 * shore * train_constant
    endpoint_supply = 2.0 * shore

    assert rhombi > after_phase_cut
    assert abs(good - 0.465683) < 1e-12
    assert internal_bin > 0.1474662
    assert abs(small_shore_capacity - 0.144) < 1e-15
    assert internal_bin > small_shore_capacity
    assert abs(endpoint_supply - 0.024) < 1e-15

    # Section-104 leakage formula.
    h = 0.0088
    w_h = math.pi / 3.0 - math.acos((1.0 + h) / 2.0)
    leakage = w_h + (1.0 / h + 169.0 / 6.0) * SIGMA_STAR
    remaining = endpoint_supply - leakage
    corridor_share = remaining / 3.0
    rho = 0.00417

    assert abs(w_h - 0.005088177978642028) < 5e-15
    assert leakage < 0.01146932
    assert remaining > 0.0125306
    assert corridor_share > rho

    # Exact projection versus principal-corridor angular geometry.
    delta = math.acos(1.0 - SIGMA_STAR / rho)
    geometric_margin = (
        THETA8 / 2.0
        - math.pi / 3.0
        - (73.0 / 6.0) * SIGMA_STAR
    )
    contradiction_margin = geometric_margin - 2.0 * delta

    assert delta < 0.147044
    assert 2.0 * delta < 0.294087
    assert geometric_margin > 0.3037089
    assert contradiction_margin > 0.00962

    print(f"theta_12={theta:.16f}")
    print(f"mu_12={mu:.16f}")
    print(f"mu_12_minus_mu_8={mu - MU8:.16e}")
    print(f"good_crossings={good:.12f}")
    print(f"internal_bin={internal_bin:.12f}")
    print(f"small_shore_capacity={small_shore_capacity:.12f}")
    print(f"endpoint_supply={endpoint_supply:.12f}")
    print(f"w_h={w_h:.12f}")
    print(f"leakage={leakage:.12f}")
    print(f"corridor_share={corridor_share:.12f}")
    print(f"delta={delta:.12f}")
    print(f"geometric_margin={geometric_margin:.12f}")
    print(f"contradiction_margin={contradiction_margin:.12f}")


if __name__ == "__main__":
    main()
