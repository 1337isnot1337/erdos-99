#!/usr/bin/env python3
"""Regression checks for proof-only Target C Section 117."""

from __future__ import annotations

import math

PI = math.pi
THETA8 = 2.7029080296483676832
MU8 = 0.9760407652670519821
PHI8 = 2.0 * PI - 2.0 * THETA8
C_RET = 2.0 - math.sqrt(3.0)
SAFE_SIGMA = 2.9e-3


def sigma(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def theta_of_sigma(target: float) -> float:
    lo = THETA8
    hi = THETA8 + 0.1
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if sigma(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def G(x: float) -> float:
    return (x - math.sin(x)) / 8.0


def area_floor(s: float) -> float:
    theta = theta_of_sigma(s)
    q = (13.0 / 3.0) * s
    return PI / 4.0 - G(theta) - 2.0 * G(PHI8 + q) - G(q)


def train_ceiling(s: float) -> float:
    theta = theta_of_sigma(s)
    return 3.0 * theta - 2.0 * PI + 2.0 * s


def lambda_of_sigma(s: float) -> float:
    return math.sin(theta_of_sigma(s) / 2.0)


def q_equation(q: float) -> float:
    return math.sin(q) + math.sqrt(3.0) * (1.0 - math.cos(q)) - q


def Q(s: float) -> float:
    target = s / 2.0
    lo = 0.0
    hi = PI / 3.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if q_equation(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def bad_direction_density(s: float) -> float:
    return Q(s) + (175.0 / 6.0) * s


def retained_area_scalar(s: float) -> float:
    return area_floor(s) - 2.0 * train_ceiling(s) * bad_direction_density(s)


def signed_return_forced_excess(s: float) -> float:
    residual = retained_area_scalar(s)
    if residual <= 0.0:
        return 0.0
    return C_RET * residual / lambda_of_sigma(s)


def signed_return_gap(s: float) -> float:
    return signed_return_forced_excess(s) - s


def envelope_root() -> float:
    lo = 2.9e-3
    hi = 3.0e-3
    assert signed_return_gap(lo) > 0.0
    assert signed_return_gap(hi) < 0.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if signed_return_gap(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    # Safe theorem at sigma=0.0029.
    theta20 = theta_of_sigma(SAFE_SIGMA)
    mu20 = lambda_of_sigma(SAFE_SIGMA)
    area = area_floor(SAFE_SIGMA)
    ct = train_ceiling(SAFE_SIGMA)
    q = Q(SAFE_SIGMA)
    bad = bad_direction_density(SAFE_SIGMA)
    residual = retained_area_scalar(SAFE_SIGMA)
    forced = signed_return_forced_excess(SAFE_SIGMA)
    tangent_extent = (3.0 * theta20 - 2.0 * PI) + (13.0 / 3.0) * SAFE_SIGMA

    assert abs(theta20 - 2.703524766763678) < 5e-15
    assert abs(mu20 - 0.9761078160770649) < 5e-15
    assert mu20 - MU8 > 6.70e-5
    assert tangent_extent < 1.84
    assert tangent_extent < PI
    assert area > 0.47225
    assert ct < 1.83319
    assert abs(q - 0.0410840313512094) < 5e-15
    assert abs(bad - 0.1256673646845427) < 5e-15
    assert residual > 0.01151
    assert abs(forced - 0.00315990413899035) < 5e-15
    assert forced - SAFE_SIGMA > 2.599e-4

    # Signed-return scalar envelope.
    s_env = envelope_root()
    theta_env = theta_of_sigma(s_env)
    mu_env = lambda_of_sigma(s_env)
    forced_env = signed_return_forced_excess(s_env)

    # The markdown values may have been generated with higher-precision decimal
    # arithmetic; binary64 agrees well inside these tolerances.
    assert abs(s_env - 0.00290687290011) < 2.0e-13
    assert abs(theta_env - 2.703526228304409) < 2.0e-13
    assert abs(mu_env - 0.976107974863521) < 2.0e-13
    assert abs(forced_env - s_env) < 5.0e-15

    # The guaranteed signed-return margin deteriorates monotonically on the live
    # neighborhood. This is a numerical regression, not the analytic proof of
    # monotonicity stated in the report.
    previous = signed_return_gap(1.5e-3)
    for j in range(1, 151):
        s = 1.5e-3 + j * (1.6e-3 / 150.0)
        current = signed_return_gap(s)
        assert current < previous
        previous = current

    print(f"theta_20={theta20:.16f}")
    print(f"mu_20={mu20:.16f}")
    print(f"mu_20-mu_8={mu20 - MU8:.16e}")
    print(f"tangent_extent={tangent_extent:.16f}")
    print(f"area_floor={area:.16f}")
    print(f"train_ceiling={ct:.16f}")
    print(f"Q={q:.16f}")
    print(f"bad_direction_density={bad:.16f}")
    print(f"retained_area_scalar={residual:.16f}")
    print(f"forced_signed_return_excess={forced:.16f}")
    print(f"safe_margin={forced - SAFE_SIGMA:.16e}")
    print(f"sigma_SR={s_env:.16f}")
    print(f"theta_SR={theta_env:.16f}")
    print(f"mu_SR={mu_env:.16f}")
    print(f"envelope_area_floor={area_floor(s_env):.16f}")
    print(f"envelope_train_ceiling={train_ceiling(s_env):.16f}")
    print(f"envelope_bad_direction_density={bad_direction_density(s_env):.16f}")
    print(f"envelope_retained_area_scalar={retained_area_scalar(s_env):.16f}")


if __name__ == "__main__":
    main()
