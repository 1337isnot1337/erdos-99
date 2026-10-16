#!/usr/bin/env python3
"""Arithmetic/regression checks for the two-normal directional-defect refinement."""

from __future__ import annotations

import math
import random

H_STAR = math.sqrt(303.0) / 52.0
C_STAR = 0.129220199818177
DELTA_STAR = 2.0 * (1.0 - math.cos(C_STAR / 2.0))
OPPOSITE_FLOOR = 2.0 - math.sqrt(2.0)


def defect_bound(theta: float, ell: float, eta: int, u_angle: float, d1: float, d2: float) -> tuple[float, float]:
    """Return the exact algebraic defect sum and the Cauchy lower bound.

    We use N1 at angle 0, N2 at angle theta, and an arbitrary original edge
    direction u. Positive d1,d2 stand for the activation increments. The identity
    checked here is the algebraic step used in the proof; event feasibility only
    restricts this test set further.
    """
    u = (math.cos(u_angle), math.sin(u_angle))
    n1 = (1.0, 0.0)
    n2 = (math.cos(theta), math.sin(theta))
    dot1 = n1[0] * u[0] + n1[1] * u[1]
    dot2 = n2[0] * u[0] + n2[1] * u[1]
    exact = 2.0 - ell * (dot1 + eta * dot2) + d1 + d2
    norm = math.sqrt(
        (n1[0] + eta * n2[0]) ** 2 + (n1[1] + eta * n2[1]) ** 2
    )
    lower = 2.0 - ell * norm
    return exact, lower


def check_two_normal_inequality() -> None:
    rng = random.Random(0xDD99)
    for _ in range(250_000):
        theta = rng.uniform(C_STAR, math.pi / 2.0)
        ell = 1.0 + rng.random() * 0.02
        eta = rng.choice((-1, 1))
        u_angle = rng.uniform(-math.pi, math.pi)
        d1 = rng.random() * H_STAR
        d2 = rng.random() * H_STAR
        exact, lower = defect_bound(theta, ell, eta, u_angle, d1, d2)
        assert exact + 1e-12 >= lower


def check_constants() -> None:
    assert math.isclose(H_STAR, 0.33474798433710024, rel_tol=0.0, abs_tol=5e-16)
    assert math.isclose(DELTA_STAR, 0.004173013032473083, rel_tol=0.0, abs_tol=5e-16)
    assert OPPOSITE_FLOOR > DELTA_STAR

    alpha1 = 1.0 - H_STAR
    surplus1 = DELTA_STAR * alpha1 / 4.0
    assert math.isclose(surplus1, 0.0006940263328100671, rel_tol=0.0, abs_tol=5e-16)

    limit_matching = 0.5 + DELTA_STAR / 8.0
    assert math.isclose(limit_matching, 0.5005216266290591, rel_tol=0.0, abs_tol=5e-16)

    kcrit = H_STAR + 4.0 * H_STAR / DELTA_STAR
    assert math.isclose(kcrit, 321.20408793817484, rel_tol=0.0, abs_tol=5e-12)

    k = 400.0
    alpha = 1.0 - H_STAR / k
    coeff = 0.5 - H_STAR / (2.0 * k) + DELTA_STAR * alpha / 8.0
    assert coeff > 0.5
    assert math.isclose(coeff, 0.5001027551149811, rel_tol=0.0, abs_tol=5e-16)


def check_threshold_equivalence() -> None:
    rng = random.Random(0x400)
    kcrit = H_STAR + 4.0 * H_STAR / DELTA_STAR
    for _ in range(100_000):
        k = rng.uniform(H_STAR + 1e-6, 1000.0)
        alpha = 1.0 - H_STAR / k
        coeff = 0.5 - H_STAR / (2.0 * k) + DELTA_STAR * alpha / 8.0
        assert (coeff > 0.5) == (k > kcrit)


def main() -> None:
    check_two_normal_inequality()
    check_constants()
    check_threshold_equivalence()

    alpha1 = 1.0 - H_STAR
    print("PASS: two-normal FREE directional-defect arithmetic/regression")
    print(f"h_*={H_STAR:.15f}")
    print(f"delta_*={DELTA_STAR:.15f}")
    print(f"opposite floor={OPPOSITE_FLOOR:.15f}")
    print(f"K=1 lower-edge surplus coefficient={DELTA_STAR * alpha1 / 4.0:.15f}")
    print(f"half-plus envelope={0.5 + DELTA_STAR / 8.0:.15f}")
    print(f"K_1/2={H_STAR + 4.0 * H_STAR / DELTA_STAR:.15f}")
    k = 400.0
    alpha = 1.0 - H_STAR / k
    coeff = 0.5 - H_STAR / (2.0 * k) + DELTA_STAR * alpha / 8.0
    print(f"K=400 matching coefficient={coeff:.15f}")


if __name__ == "__main__":
    main()
