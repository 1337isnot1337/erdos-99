#!/usr/bin/env python3
"""Arithmetic/regression checks for the ordered two-normal FREE skeleton note."""

from __future__ import annotations

import math


H_STAR = math.sqrt(303.0) / 52.0


def check_constants() -> None:
    alpha1 = 1.0 - H_STAR
    coeff = math.sqrt(alpha1 / 44.0)
    assert abs(coeff - 0.12296082299797213) < 1e-14


def check_erdos_szekeres_scale() -> None:
    # If N >= (alpha/44) D/m^2, sqrt(N) has the asserted scale.
    alpha = 1.0 - H_STAR
    for D, m in ((1e12, 100.0), (1e16, 1000.0), (1e20, 10_000.0)):
        N = (alpha / 44.0) * D / (m * m)
        lower = math.sqrt(N)
        claimed = math.sqrt(alpha / 44.0) * math.sqrt(D) / m
        assert math.isclose(lower, claimed, rel_tol=1e-12)


def check_slow_scale_conversion() -> None:
    for D, kappa in ((1e16, 10.0), (1e24, 100.0)):
        m = D ** 0.25 / kappa
        ordered = math.sqrt(D) / m
        expected_ordered = kappa * D ** 0.25
        assert math.isclose(ordered, expected_ordered, rel_tol=1e-12)

        activation = m * m / D
        expected_activation = 1.0 / (kappa * kappa * math.sqrt(D))
        assert math.isclose(activation, expected_activation, rel_tol=1e-12)


def main() -> None:
    check_constants()
    check_erdos_szekeres_scale()
    check_slow_scale_conversion()

    alpha1 = 1.0 - H_STAR
    print("PASS: ordered two-normal FREE skeleton certificate")
    print(f"sqrt(alpha_1/44) = {math.sqrt(alpha1/44.0):.15f}")


if __name__ == "__main__":
    main()
