#!/usr/bin/env python3
"""Regression certificate for proof-only Target C Section 118.

Checks only the one-variable arithmetic after the mathematical correlated-slack
reduction.  It does not certify the geometric signed-return or tangent-window lemmas.
"""

import math

PI = math.pi
SQRT3 = math.sqrt(3.0)
CRET = 2.0 - SQRT3
THETA8 = 2.7029080296483676832
PHI8 = 2.0 * PI - 2.0 * THETA8
SAFE_SIGMA = 0.0047


def slack(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def theta_for_sigma(sigma: float) -> float:
    lo, hi = THETA8, PI - 1.0e-12
    for _ in range(220):
        mid = (lo + hi) / 2.0
        if slack(mid) < sigma:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def G(x: float) -> float:
    return (x - math.sin(x)) / 8.0


def tooth_F(q: float) -> float:
    return math.sin(q) + SQRT3 * (1.0 - math.cos(q)) - q


def tooth_Q(sigma: float) -> float:
    lo, hi = 0.0, PI / 3.0
    target = sigma / 2.0
    for _ in range(220):
        mid = (lo + hi) / 2.0
        if tooth_F(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def quantities(sigma: float) -> dict[str, float]:
    theta = theta_for_sigma(sigma)
    lam = math.sin(theta / 2.0)
    U = 3.0 * theta - 2.0 * PI
    q = 13.0 * sigma / 3.0
    area = PI / 4.0 - G(theta) - 2.0 * G(PHI8 + q) - G(q)
    train = U + 2.0 * sigma
    tq = tooth_Q(sigma)
    bad = tq + 15.0 * sigma
    retained = area - 2.0 * train * bad
    forced = CRET * retained / lam
    return {
        "theta": theta,
        "lambda": lam,
        "U": U,
        "area": area,
        "train": train,
        "tooth_q": tq,
        "bad": bad,
        "retained": retained,
        "forced": forced,
        "margin": forced - sigma,
    }


def envelope_root() -> float:
    lo, hi = SAFE_SIGMA, 0.006
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
    q = quantities(SAFE_SIGMA)

    assert abs(q["theta"] - 2.703907524666705) < 2.0e-15
    assert abs(q["lambda"] - 0.9761493823116423) < 2.0e-15
    assert abs(q["area"] - 0.4714354422213568) < 2.0e-15
    assert abs(q["train"] - 1.8379372668205292) < 3.0e-15
    assert abs(q["tooth_q"] - 0.0523621835834795) < 2.0e-15
    assert abs(q["bad"] - 0.1228621835834795) < 2.0e-15
    assert abs(q["retained"] - 0.0198094704393120) < 3.0e-15
    assert abs(q["forced"] - 0.00543762225626986) < 3.0e-15
    assert q["margin"] > 7.37e-4

    # Explicit stability-room checks used by the proof.
    theta = q["theta"]
    phi = 2.0 * PI - 2.0 * theta
    assert (10.0 / 3.0) * SAFE_SIGMA < 0.1
    assert (13.0 / 3.0) * SAFE_SIGMA < phi
    assert q["U"] + (13.0 / 3.0) * SAFE_SIGMA < PI
    assert q["retained"] > 0.0

    root = envelope_root()
    qr = quantities(root)
    assert abs(root - 0.0047334052943) < 2.0e-12
    assert abs(qr["lambda"] - 0.9761501533) < 2.0e-10
    assert abs(qr["margin"]) < 2.0e-13

    # Numerical monotonicity sanity check for the deliberately coarse scalar envelope.
    previous = quantities(0.0)["margin"]
    for k in range(1, 301):
        s = root * k / 300.0
        current = quantities(s)["margin"]
        assert current < previous + 2.0e-12
        previous = current

    print("Section 118 correlated-slack regression: PASS")
    print(f"safe sigma = {SAFE_SIGMA:.16g}")
    print(f"safe theta = {q['theta']:.16g}")
    print(f"safe mu = {q['lambda']:.16g}")
    print(f"forced excess = {q['forced']:.16g}")
    print(f"margin = {q['margin']:.16g}")
    print(f"coarse envelope sigma = {root:.16g}")
    print(f"coarse envelope mu = {qr['lambda']:.16g}")


if __name__ == "__main__":
    main()
