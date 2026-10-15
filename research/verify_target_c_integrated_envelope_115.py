#!/usr/bin/env python3
"""Regression checks for proof-only Target C Section 115."""

from __future__ import annotations

import math

PI = math.pi
THETA8 = 2.7029080296483676832
MU8 = 0.9760407652670519821
PHI8 = 2.0 * PI - 2.0 * THETA8
C_PHASE = 5.317
SAFE_SIGMA = 1.75e-3
SAFE_R = 0.47276
SAFE_CT = 1.8302
SAFE_A = 0.086
SAFE_E0 = 0.172


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


def q_equation(q: float) -> float:
    return math.sin(q) + math.sqrt(3.0) * (1.0 - math.cos(q)) - q


def Q(s: float) -> float:
    target = s / 2.0
    lo = 0.0
    hi = PI / 3.0
    for _ in range(180):
        mid = (lo + hi) / 2.0
        if q_equation(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def integrated_leakage(s: float) -> float:
    return Q(s) + (175.0 / 6.0) * s


def integrated_envelope_gap(s: float) -> float:
    r = area_floor(s)
    ct = train_ceiling(s)
    shore = r / (3.0 * ct)
    endpoint_supply = 2.0 * shore
    principal = endpoint_supply - integrated_leakage(s)
    forced = 2.0 * principal * (1.0 - math.cos(mismatch(s) / 2.0))
    return forced - s


def envelope_root() -> float:
    lo = 1.7e-3
    hi = 1.9e-3
    assert integrated_envelope_gap(lo) > 0.0
    assert integrated_envelope_gap(hi) < 0.0
    for _ in range(180):
        mid = (lo + hi) / 2.0
        if integrated_envelope_gap(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    theta19 = theta_of_sigma(SAFE_SIGMA)
    mu19 = math.sin(theta19 / 2.0)
    area = area_floor(SAFE_SIGMA)
    ct = train_ceiling(SAFE_SIGMA)
    extent = (3.0 * theta19 - 2.0 * PI) + (13.0 / 3.0) * SAFE_SIGMA

    assert abs(theta19 - 2.703280209175034) < 5e-15
    assert abs(mu19 - 0.9760812392179798) < 5e-15
    assert mu19 - MU8 > 4.047e-5
    assert area > SAFE_R
    assert area - SAFE_R > 1.2e-5
    assert ct < SAFE_CT
    assert extent < 1.835
    assert extent < PI
    assert SAFE_R / (3.0 * SAFE_CT) > SAFE_A

    # Finite joint-shore extraction.
    retained = 0.47275
    K = 50000.0
    bins = 5000.0
    internal = (1.0 - 1.0 / bins) * (retained - C_PHASE / K) / 3.0
    bad_capacity = SAFE_A * SAFE_CT
    assert internal - bad_capacity > 1.19e-4

    # Integrated leakage and aggregate projection.  The root itself is certified by
    # its equation residual; the archived decimal is only a cross-platform regression
    # target because libm evaluation can move the final binary root by ~1e-13.
    q = Q(SAFE_SIGMA)
    leak = integrated_leakage(SAFE_SIGMA)
    principal = SAFE_E0 - leak
    m = mismatch(SAFE_SIGMA)
    forced = 2.0 * principal * (1.0 - math.cos(m / 2.0))

    assert abs(q_equation(q) - SAFE_SIGMA / 2.0) < 5e-16
    assert abs(q - 0.03188553848859337) < 5e-13
    assert abs(leak - 0.08292720515526004) < 5e-13
    assert principal > 0.08907
    assert m > 0.28296
    assert forced - SAFE_SIGMA > 3.0e-5

    # Integrated decoupled scalar envelope.
    s_env = envelope_root()
    theta_env = theta_of_sigma(s_env)
    mu_env = math.sin(theta_env / 2.0)
    q_env = Q(s_env)
    leak_env = integrated_leakage(s_env)
    r_env = area_floor(s_env)
    ct_env = train_ceiling(s_env)
    a_env = r_env / (3.0 * ct_env)
    p_env = 2.0 * a_env - leak_env
    forced_env = 2.0 * p_env * (1.0 - math.cos(mismatch(s_env) / 2.0))

    assert abs(s_env - 0.00176783502507091) < 5e-14
    assert abs(theta_env - 2.7032840020556765) < 5e-13
    assert abs(mu_env - 0.9760816515139280) < 5e-13
    assert abs(forced_env - s_env) < 5e-13

    # The guaranteed margin deteriorates monotonically on the relevant interval.
    previous = integrated_envelope_gap(1.4e-3)
    for j in range(1, 101):
        s = 1.4e-3 + j * (0.5e-3 / 100.0)
        current = integrated_envelope_gap(s)
        assert current < previous
        previous = current

    print(f"theta_19={theta19:.16f}")
    print(f"mu_19={mu19:.16f}")
    print(f"mu_19-mu_8={mu19 - MU8:.16e}")
    print(f"safe_area_floor={area:.16f}")
    print(f"safe_train_ceiling={ct:.16f}")
    print(f"safe_tangent_extent={extent:.16f}")
    print(f"safe_internal_crossing_density={internal:.16f}")
    print(f"safe_bad_bin_capacity={bad_capacity:.16f}")
    print(f"safe_Q={q:.16f}")
    print(f"safe_integrated_leakage={leak:.16f}")
    print(f"safe_principal_density={principal:.16f}")
    print(f"safe_mismatch={m:.16f}")
    print(f"safe_forced_route_loss={forced:.16f}")
    print(f"safe_contradiction_margin={forced - SAFE_SIGMA:.16e}")
    print(f"sigma_int={s_env:.16f}")
    print(f"theta_int={theta_env:.16f}")
    print(f"mu_int={mu_env:.16f}")
    print(f"Q_int={q_env:.16f}")
    print(f"leakage_int={leak_env:.16f}")
    print(f"area_floor_int={r_env:.16f}")
    print(f"train_ceiling_int={ct_env:.16f}")
    print(f"shore_density_int={a_env:.16f}")
    print(f"principal_density_int={p_env:.16f}")


if __name__ == "__main__":
    main()
