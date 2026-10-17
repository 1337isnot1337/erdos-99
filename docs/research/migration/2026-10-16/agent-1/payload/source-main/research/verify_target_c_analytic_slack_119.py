#!/usr/bin/env python3
"""Regression certificate for proof-only Target C Section 119."""

import math

PI = math.pi
SQRT3 = math.sqrt(3.0)
CRET = 2.0 - SQRT3
THETA8 = 2.7029080296483676832
PHI8 = 2.0 * PI - 2.0 * THETA8
SAFE_SIGMA = 0.0073


def scalar_slack(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def theta_for_sigma(sigma: float) -> float:
    lo, hi = THETA8, PI - 1.0e-12
    for _ in range(220):
        mid = (lo + hi) / 2.0
        if scalar_slack(mid) < sigma:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def G(x: float) -> float:
    return (x - math.sin(x)) / 8.0


def F(q: float) -> float:
    return math.sin(q) + SQRT3 * (1.0 - math.cos(q)) - q


def psi(q: float) -> float:
    return math.cos(q) + SQRT3 * math.sin(q) - 1.0


def solve_qstar() -> float:
    lo, hi = 0.0, PI / 3.0
    target = 1.0 / 28.0
    for _ in range(220):
        mid = (lo + hi) / 2.0
        if psi(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


QSTAR = solve_qstar()
YSTAR = 2.0 * F(QSTAR)
KSTAR = QSTAR - 14.0 * YSTAR


def quantities(sigma: float) -> dict[str, float]:
    theta = theta_for_sigma(sigma)
    lam = math.sin(theta / 2.0)
    U = 3.0 * theta - 2.0 * PI
    qtail = 13.0 * sigma / 3.0
    area = PI / 4.0 - G(theta) - 2.0 * G(PHI8 + qtail) - G(qtail)
    train = U + 2.0 * sigma
    bad = 15.0 * sigma + KSTAR
    retained = area - 2.0 * train * bad
    forced = CRET * retained / lam
    return {
        "theta": theta,
        "lambda": lam,
        "U": U,
        "area": area,
        "train": train,
        "bad": bad,
        "retained": retained,
        "forced": forced,
        "margin": forced - sigma,
    }


def envelope_root() -> float:
    lo, hi = SAFE_SIGMA, 0.008
    assert quantities(lo)["margin"] > 0.0
    assert quantities(hi)["margin"] < 0.0
    for _ in range(220):
        mid = (lo + hi) / 2.0
        if quantities(mid)["margin"] > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    assert abs(QSTAR - 0.0207453732819050) < 3.0e-15
    assert abs(YSTAR - 0.000742420858663266) < 3.0e-16
    assert abs(KSTAR - 0.0103514812606193) < 3.0e-16
    assert abs(psi(QSTAR) - 1.0 / 28.0) < 3.0e-15

    q = quantities(SAFE_SIGMA)
    assert abs(q["theta"] - 2.704460337165959) < 3.0e-15
    assert abs(q["lambda"] - 0.9762093528016385) < 3.0e-15
    assert abs(q["area"] - 0.4702300098665401) < 3.0e-15
    assert abs(q["train"] - 1.8447957043182923) < 4.0e-15
    assert abs(q["bad"] - 0.1198514812606193) < 3.0e-15
    assert abs(q["retained"] - 0.0280270142949906) < 4.0e-15
    assert abs(q["forced"] - 0.00769283333031559) < 4.0e-15
    assert q["margin"] > 3.92e-4

    phi = 2.0 * PI - 2.0 * q["theta"]
    assert (10.0 / 3.0) * SAFE_SIGMA < 0.1
    assert (13.0 / 3.0) * SAFE_SIGMA < phi
    assert q["U"] + (13.0 / 3.0) * SAFE_SIGMA < PI

    root = envelope_root()
    qr = quantities(root)
    assert abs(root - 0.0073238173272) < 3.0e-12
    assert abs(qr["lambda"] - 0.976209901782) < 3.0e-12
    assert abs(qr["margin"]) < 3.0e-13

    previous = quantities(0.0)["margin"]
    for k in range(1, 401):
        s = root * k / 400.0
        current = quantities(s)["margin"]
        assert current < previous + 3.0e-12
        previous = current

    print("Section 119 analytic correlated-slack regression: PASS")
    print(f"Q* = {QSTAR:.16g}")
    print(f"y* = {YSTAR:.16g}")
    print(f"K* = {KSTAR:.16g}")
    print(f"safe sigma = {SAFE_SIGMA:.16g}")
    print(f"safe mu = {q['lambda']:.16g}")
    print(f"safe forced excess = {q['forced']:.16g}")
    print(f"safe margin = {q['margin']:.16g}")
    print(f"envelope sigma = {root:.16g}")
    print(f"envelope mu = {qr['lambda']:.16g}")


if __name__ == "__main__":
    main()
