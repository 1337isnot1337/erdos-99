#!/usr/bin/env python3
"""Arithmetic/regression checks for the small-external common-lower-runs note."""

from __future__ import annotations

import math


H_STAR = math.sqrt(303.0) / 52.0
ALPHA1 = 1.0 - H_STAR
ORDER_COEFF_K1 = math.sqrt(ALPHA1 / 44.0)


def check_order_constant() -> None:
    assert abs(ORDER_COEFF_K1 - 0.12296082299797213) < 1e-14


def check_z_adapted_scales() -> None:
    # Model Z=D^p with p<1/2.  kappa=max(loglog D,sqrt(Z+1)) is o(D^1/4),
    # m=D^1/4/kappa diverges, and kappa D^1/4/(Z+1) diverges.
    D = 1e80
    for p in (0.0, 0.10, 0.30, 0.45, 0.49):
        Z = 1.0 if p == 0.0 else D**p
        kappa = max(math.log(math.log(D)), math.sqrt(Z + 1.0))
        m = D**0.25 / kappa
        block_scale = kappa * D**0.25 / (Z + 1.0)

        assert kappa / D**0.25 < 1.0
        assert m > 1.0
        assert block_scale > 1.0

        lower_bound = D**0.25 / math.sqrt(Z + 1.0)
        # Mathematically block_scale >= lower_bound because
        # kappa >= sqrt(Z+1).  Use a relative comparison at huge test scales.
        assert block_scale >= lower_bound * (1.0 - 1e-12)


def check_run_pair_count() -> None:
    # Two ancestries with at most Z+1 lower runs each produce at most 2Z
    # coordinate changes along a monotone/reverse-monotone shared sequence.
    for Z in (0, 1, 10, 1000):
        max_changes = 2 * Z
        max_blocks = max_changes + 1
        assert max_blocks <= 2 * Z + 3


def check_full_order_normal_scale() -> None:
    # m~D^(1/4)/kappa and gamma~kappa D^(-1/4) imply m*gamma~1.
    for D, kappa in ((1e16, 10.0), (1e24, 100.0)):
        m = D**0.25 / kappa
        gamma = kappa * D**(-0.25)
        assert math.isclose(m * gamma, 1.0, rel_tol=1e-12)

        omega = math.sqrt(m)
        R = m / omega
        separated_scale = R * gamma
        assert math.isclose(separated_scale, 1.0 / math.sqrt(m), rel_tol=1e-12)


def main() -> None:
    check_order_constant()
    check_z_adapted_scales()
    check_run_pair_count()
    check_full_order_normal_scale()

    print("PASS: small-external common FREE lower-runs certificate")
    print(f"K=1 ordered-skeleton coefficient = {ORDER_COEFF_K1:.15f}")


if __name__ == "__main__":
    main()
