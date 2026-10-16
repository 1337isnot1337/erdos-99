#!/usr/bin/env python3
"""Regression certificate for proof-only Target C Section 109."""

import math

THETA8 = 2.7029080296483676832
MU8 = math.sin(THETA8 / 2.0)
SIGMA_STAR = 5.0e-5


def sigma(theta: float) -> float:
    return 3.0 * theta - 2.0 * math.pi - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def root_for_sigma(target: float) -> float:
    lo = THETA8
    hi = THETA8 + 0.01
    assert sigma(lo) <= target <= sigma(hi)
    for _ in range(180):
        mid = (lo + hi) / 2.0
        if sigma(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    theta = root_for_sigma(SIGMA_STAR)
    mu = math.sin(theta / 2.0)

    assert abs(theta - 2.702918663796103) < 5e-15
    assert abs(mu - 0.9760419221833405) < 5e-15
    assert mu - MU8 > 1.15e-6
    assert SIGMA_STAR < 1.0e-3

    # Explicit realization of the asymptotically sharp shore lemma.
    retained_after_phase_cut = 0.47199
    phase_defect_constant = 5.317
    K = 30000.0
    m = 3000.0
    good = retained_after_phase_cut - phase_defect_constant / K
    one_label_pair = good / 3.0
    internal_bin = (1.0 - 1.0 / m) * one_label_pair

    shore = 0.0131
    train_constant = 6.0
    small_shore_capacity = 2.0 * shore * train_constant
    endpoint_supply = 2.0 * shore

    assert shore < 0.472 / (6.0 * train_constant)
    assert abs(good - 0.47181276666666666) < 1e-15
    assert internal_bin > 0.15721849
    assert small_shore_capacity == 0.1572
    assert internal_bin - small_shore_capacity > 1.8e-5
    assert endpoint_supply == 0.0262

    # Audited Section-104 leakage formula at a near-optimal simple cutoff.
    h = 0.0093
    w_h = math.pi / 3.0 - math.acos((1.0 + h) / 2.0)
    leakage = w_h + (1.0 / h + 169.0 / 6.0) * SIGMA_STAR
    remaining = endpoint_supply - leakage
    corridor_share = remaining / 3.0
    rho = 0.00467

    assert abs(w_h - 0.005377731888944304) < 5e-15
    assert leakage < 0.01216241
    assert remaining > 0.0140375
    assert corridor_share > 0.0046791
    assert corridor_share > rho

    # Exact corridor projection loss and the inherited gap-geometry margin.
    delta = math.acos(1.0 - SIGMA_STAR / rho)
    geometric_margin = (
        THETA8 / 2.0
        - math.pi / 3.0
        - (73.0 / 6.0) * SIGMA_STAR
    )
    contradiction_margin = geometric_margin - 2.0 * delta

    assert delta < 0.146464
    assert 2.0 * delta < 0.292928
    assert geometric_margin > 0.3036481
    assert contradiction_margin > 0.01072
    assert 2.0 * delta < math.pi / 3.0

    print(f"theta_13={theta:.16f}")
    print(f"mu_13={mu:.16f}")
    print(f"mu_13_minus_mu_8={mu - MU8:.16e}")
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
