#!/usr/bin/env python3
"""Arithmetic/regression checks for the multi-module FREE lower-edge reuse note.

This certificate checks only the numerical thresholds and elementary counting constants.
The geometric and incidence arguments are proved in the accompanying markdown note.
"""

from __future__ import annotations

import math


H_STAR = math.sqrt(303.0) / 52.0
L7 = math.sqrt(1.0 / (2.0 * (1.0 - math.cos(2.0 * math.pi / 7.0))))


def check_degree_threshold() -> None:
    assert 1.0 + H_STAR < math.sqrt(2.0)
    assert 1.15 < L7 < math.sqrt(2.0)

    # For fixed K, 1 + K/D eventually lies below the seven-neighbor threshold L7.
    for K in (H_STAR + 1e-3, 1.0, 2.0, 10.0, 100.0):
        D0 = math.floor(K / (L7 - 1.0)) + 2
        L = 1.0 + K / D0
        assert L < L7

        max_cos = 1.0 - 1.0 / (2.0 * L * L)
        min_angle = math.acos(max_cos)
        assert min_angle > 2.0 * math.pi / 7.0

    # Degree six is asymptotically feasible: six equally spaced neighbors at
    # radius 1+eps are unit-separated while all radial edges tend to length one.
    for eps in (1e-1, 1e-3, 1e-6):
        radius = 1.0 + eps
        assert radius < math.sqrt(2.0)
        adjacent = 2.0 * radius * math.sin(math.pi / 6.0)
        assert adjacent >= 1.0


def check_k1_constants() -> None:
    alpha = 1.0 - H_STAR
    assert abs(H_STAR - 0.33474798433710024) < 1e-14
    assert abs(alpha - 0.6652520156628998) < 1e-14
    assert abs(alpha / 22.0 - 0.030238727984677263) < 1e-14
    assert abs(alpha / 2.0 - 0.3326260078314499) < 1e-14


def check_incidence_fork_arithmetic() -> None:
    # Synthetic checks of the two counting denominators:
    # light incidence >= I/2 -> |E_light| >= I/(2R), then matching /11;
    # heavy incidence > I/2 -> |E_heavy| > I/(2m).
    alpha = 1.0 - H_STAR
    for m in (16, 100, 1000, 10_000):
        R = int(math.sqrt(m))
        D = 100_000.0
        I = alpha * m * D

        light_edge_floor = I / (2.0 * R)
        light_matching_floor = light_edge_floor / 11.0
        claimed_matching_floor = alpha * m * D / (22.0 * R)
        assert abs(light_matching_floor - claimed_matching_floor) < 1e-7

        heavy_edge_floor = I / (2.0 * m)
        assert abs(heavy_edge_floor - alpha * D / 2.0) < 1e-7

        # Dividing the heavy edge floor by C(m,2) gives the fixed-pair
        # common-edge scale alpha*D/[m(m-1)], asymptotic to alpha*D/m^2.
        pair_floor = heavy_edge_floor / (m * (m - 1.0) / 2.0)
        exact = alpha * D / (m * (m - 1.0))
        assert abs(pair_floor - exact) < 1e-9


def check_slow_scale_exponents() -> None:
    # With m ~ D^(1/4)/kappa and R ~ sqrt(m):
    # D*sqrt(m) ~ D^(9/8)/sqrt(kappa),
    # D/m^2 ~ kappa^2 D^(1/2),
    # R*kappa*D^(-1/4) ~ sqrt(kappa) D^(-1/8).
    for D, kappa in ((1e16, 10.0), (1e24, 100.0)):
        m = D ** 0.25 / kappa
        left_match = D * math.sqrt(m)
        right_match = D ** 1.125 / math.sqrt(kappa)
        assert math.isclose(left_match, right_match, rel_tol=1e-12)

        left_shared = D / (m * m)
        right_shared = kappa * kappa * D ** 0.5
        assert math.isclose(left_shared, right_shared, rel_tol=1e-12)

        left_gap = math.sqrt(m) * kappa * D ** (-0.25)
        right_gap = math.sqrt(kappa) * D ** (-0.125)
        assert math.isclose(left_gap, right_gap, rel_tol=1e-12)


def main() -> None:
    check_degree_threshold()
    check_k1_constants()
    check_incidence_fork_arithmetic()
    check_slow_scale_exponents()

    print("PASS: multi-module FREE lower-edge reuse certificate")
    print(f"h_* = {H_STAR:.15f}")
    print(f"L_7 = {L7:.15f}")
    print(f"K=1 light matching coefficient = {(1.0-H_STAR)/22.0:.15f}")
    print(f"K=1 heavy edge coefficient = {(1.0-H_STAR)/2.0:.15f}")


if __name__ == "__main__":
    main()
