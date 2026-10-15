#!/usr/bin/env python3
"""Regression checks for proof-only Target C Section 114."""

from __future__ import annotations

import math

PI = math.pi
THETA8 = 2.7029080296483676832
MU8 = 0.9760407652670519821
PHI8 = 2.0 * PI - 2.0 * THETA8
C_PHASE = 5.317
SAFE_SIGMA = 1.46e-3
SAFE_R = 0.47289
SAFE_CT = 1.8294
SAFE_A = 0.086
SAFE_E0 = 0.172
SAFE_H = 0.05


def sigma(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def theta_of_sigma(target: float) -> float:
    lo = THETA8
    hi = THETA8 + 0.1
    for _ in range(180):
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


def mismatch(s: float) -> float:
    return THETA8 / 2.0 - PI / 3.0 - (73.0 / 6.0) * s


def w(h: float) -> float:
    return PI / 3.0 - math.acos((1.0 + h) / 2.0)


def leakage(s: float, h: float) -> float:
    return w(h) + (1.0 / h + 169.0 / 6.0) * s


def optimized_h_and_leakage(s: float) -> tuple[float, float]:
    # The minimizer lies well inside (0,1) on the window of interest.  A fixed-count
    # ternary search is enough for this regression and avoids external dependencies.
    lo = 1.0e-8
    hi = 0.25
    for _ in range(220):
        h1 = (2.0 * lo + hi) / 3.0
        h2 = (lo + 2.0 * hi) / 3.0
        if leakage(s, h1) <= leakage(s, h2):
            hi = h2
        else:
            lo = h1
    h = (lo + hi) / 2.0
    return h, leakage(s, h)


def envelope_gap(s: float) -> float:
    r = area_floor(s)
    ct = train_ceiling(s)
    shore = r / (3.0 * ct)
    endpoint_supply = 2.0 * shore
    _, leak = optimized_h_and_leakage(s)
    principal = endpoint_supply - leak
    m = mismatch(s)
    forced = 2.0 * principal * (1.0 - math.cos(m / 2.0))
    return forced - s


def envelope_root() -> float:
    lo = 1.4e-3
    hi = 1.6e-3
    assert envelope_gap(lo) > 0.0
    assert envelope_gap(hi) < 0.0
    for _ in range(160):
        mid = (lo + hi) / 2.0
        if envelope_gap(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    # Safe finite theorem at sigma=1.46e-3.
    theta18 = theta_of_sigma(SAFE_SIGMA)
    mu18 = math.sin(theta18 / 2.0)
    area = area_floor(SAFE_SIGMA)
    ct = train_ceiling(SAFE_SIGMA)

    assert abs(theta18 - 2.7032185359365495) < 5e-15
    assert abs(mu18 - 0.9760745346846268) < 5e-15
    assert mu18 - MU8 > 3.3769e-5
    assert area > SAFE_R
    assert area - SAFE_R > 1.2e-5
    assert ct < SAFE_CT
    assert SAFE_R / (3.0 * SAFE_CT) > SAFE_A

    retained = 0.47288
    K = 20000.0
    bins = 2000.0
    internal = (1.0 - 1.0 / bins) * (retained - C_PHASE / K) / 3.0
    bad_capacity = SAFE_A * SAFE_CT
    assert internal - bad_capacity > 1.30e-4

    leak = leakage(SAFE_SIGMA, SAFE_H)
    principal = SAFE_E0 - leak
    m = mismatch(SAFE_SIGMA)
    forced = 2.0 * principal * (1.0 - math.cos(m / 2.0))
    assert abs(leak - 0.09943967083181753) < 5e-15
    assert principal > 0.07256
    assert m > 0.28649
    assert forced - SAFE_SIGMA > 2.63e-5

    # Decoupled scalar-envelope root.
    s_env = envelope_root()
    theta_env = theta_of_sigma(s_env)
    mu_env = math.sin(theta_env / 2.0)
    h_env, l_env = optimized_h_and_leakage(s_env)
    r_env = area_floor(s_env)
    ct_env = train_ceiling(s_env)
    a_env = r_env / (3.0 * ct_env)
    p_env = 2.0 * a_env - l_env
    forced_env = 2.0 * p_env * (1.0 - math.cos(mismatch(s_env) / 2.0))

    assert abs(s_env - 0.00147567317481145) < 5e-14
    assert abs(theta_env - 2.7032218691158647) < 5e-13
    assert abs(mu_env - 0.9760748970601998) < 5e-13
    assert abs(h_env - 0.05011776) < 2e-7
    assert abs(forced_env - s_env) < 5e-13

    # Check strict monotonic deterioration of the guaranteed scalar margin on a grid.
    previous = envelope_gap(1.40e-3)
    for j in range(1, 101):
        s = 1.40e-3 + j * (0.10e-3 / 100.0)
        current = envelope_gap(s)
        assert current < previous
        previous = current

    print(f"theta_18={theta18:.16f}")
    print(f"mu_18={mu18:.16f}")
    print(f"mu_18-mu_8={mu18 - MU8:.16e}")
    print(f"safe_area_floor={area:.16f}")
    print(f"safe_train_ceiling={ct:.16f}")
    print(f"safe_internal_crossing_density={internal:.16f}")
    print(f"safe_bad_bin_capacity={bad_capacity:.16f}")
    print(f"safe_leakage={leak:.16f}")
    print(f"safe_principal_density={principal:.16f}")
    print(f"safe_mismatch={m:.16f}")
    print(f"safe_forced_route_loss={forced:.16f}")
    print(f"safe_contradiction_margin={forced - SAFE_SIGMA:.16e}")
    print(f"sigma_env={s_env:.16f}")
    print(f"theta_env={theta_env:.16f}")
    print(f"mu_env={mu_env:.16f}")
    print(f"h_env={h_env:.16f}")
    print(f"envelope_area_floor={r_env:.16f}")
    print(f"envelope_train_ceiling={ct_env:.16f}")
    print(f"envelope_shore_density={a_env:.16f}")
    print(f"envelope_principal_density={p_env:.16f}")


if __name__ == "__main__":
    main()
