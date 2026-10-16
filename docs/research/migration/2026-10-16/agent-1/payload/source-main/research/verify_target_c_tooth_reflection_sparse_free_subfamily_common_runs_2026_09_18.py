#!/usr/bin/env python3
"""Regression checks for the sparse-FREE-subfamily common-run tradeoff.

The script checks the finite counting/scaling arithmetic used in
`target_c_tooth_reflection_sparse_free_subfamily_common_runs_2026-09-18.md`.
It is not a global-optimality certificate and does not promote the candidate result.
"""

from __future__ import annotations

import math


C_STAR = 0.129220199818177
H_STAR = math.sqrt(303.0) / 52.0


def check_even_thinning_gap() -> None:
    """Synthetic check of gamma >= (c_* - o(1))/m after even thinning."""
    # A abbreviates D^(1/4)/kappa.  The FREE count is at least
    # (c_*/2-eps)A and the original gap at least (2-eps)/A.
    for a_scale in (1e6, 1e8, 1e10):
        eps = a_scale**-0.2
        free_count = math.floor((C_STAR / 2.0 - eps) * a_scale)
        selected = max(3, int(a_scale**0.15))
        assert selected < free_count / 10

        stride = (free_count - 1) // (selected - 1)
        gamma = (2.0 - eps) * stride / a_scale
        lower = (C_STAR - 3.0 * eps) / selected
        assert gamma >= lower


def check_r1_reuse_counting() -> None:
    """Specialize the incidence fork to R=1 for a growing m-family."""
    for module_count in (10, 100, 1000):
        for k in (0.5, 1.0, 2.0, 10.0):
            assert k > H_STAR
            alpha = 1.0 - H_STAR / k
            d = 1e12
            incidences = alpha * module_count * d

            # Light incidence at least half: multiplicity <=1, then /11 matching.
            matching = (incidences / 2.0) / 11.0
            assert math.isclose(
                matching,
                alpha * module_count * d / 22.0,
                rel_tol=1e-14,
            )

            # Heavy incidence > half: each distinct edge has multiplicity at
            # most m, giving alpha D/2 distinct heavy edges.
            heavy_distinct = (incidences / 2.0) / module_count
            assert math.isclose(
                heavy_distinct, alpha * d / 2.0, rel_tol=1e-14
            )

            # Assign to at most binom(m,2) first/last module pairs.
            pair_cells = module_count * (module_count - 1) / 2.0
            shared = heavy_distinct / pair_cells
            expected = alpha * d / (
                module_count * (module_count - 1)
            )
            assert math.isclose(shared, expected, rel_tol=1e-14)


def check_component_cone_scale() -> None:
    """Check sin(gamma/2) ~ c_*/(2m) for the selected-pair gap."""
    for module_count in (10, 100, 1000, 10_000):
        gamma = C_STAR / module_count
        same_coefficient = math.sin(gamma / 2.0)
        asymptotic = C_STAR / (2.0 * module_count)
        assert same_coefficient <= asymptotic
        assert same_coefficient / asymptotic > 0.999

        # The opposite-traversal coefficient is uniformly larger because all
        # base normals remain in one quadrant; canonical-normal error is o(1).
        assert math.cos(math.pi / 4.0) > same_coefficient


def check_tradeoff_scaling() -> None:
    """Verify the S/m^(3/2) heavy currency and K=1 constants."""
    alpha = 1.0 - H_STAR
    currency_coefficient = math.sqrt(alpha * C_STAR / 2.0)

    assert math.isclose(alpha / 22.0, 0.030238727984677263, rel_tol=1e-15)
    assert math.isclose(
        currency_coefficient, 0.20732100519894858, rel_tol=1e-15
    )

    for s_scale in (1e6, 1e12, 1e24, 1e48):
        omega = math.log(math.log(s_scale + math.e**math.e))

        # q ~ alpha S^2 / m^2 and b ~ c_*/(2m).
        q = alpha * s_scale**2 / omega**2
        b = C_STAR / (2.0 * omega)
        target = math.sqrt(b * q)
        expected = currency_coefficient * s_scale / omega**1.5

        assert math.isclose(target, expected, rel_tol=1e-14)
        assert omega > 1.0
        assert expected > 1.0


def check_explicit_diagonal_scale() -> None:
    """Check the displayed min{N^(1/2), S^(1/3)} diagonal choice."""
    for n_scale, s_scale in (
        (1e6, 1e4),
        (1e12, 1e8),
        (1e20, 1e16),
    ):
        omega = min(math.sqrt(n_scale), s_scale ** (1.0 / 3.0))
        assert omega > 1.0
        assert omega / n_scale < 1e-2
        assert omega**1.5 / s_scale < 1.0


def main() -> None:
    check_even_thinning_gap()
    check_r1_reuse_counting()
    check_component_cone_scale()
    check_tradeoff_scaling()
    check_explicit_diagonal_scale()
    print("PASS: sparse FREE subfamily common-run tradeoff")


if __name__ == "__main__":
    main()
