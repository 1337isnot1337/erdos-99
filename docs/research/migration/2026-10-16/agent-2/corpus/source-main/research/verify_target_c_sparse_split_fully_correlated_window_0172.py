#!/usr/bin/env python3
"""Scalar certificate for the fully correlated sparse-return sigma<=0.0172 theorem.

The script checks the endpoint geometry constants, the x/z monotonicity bounds, the
one-dimensional convex minimum bracket, and the numerical scalar envelope. It does not
certify the inherited geometric signed-return theorem or C-II.
"""

from __future__ import annotations

import math

PI = math.pi
SQRT3 = math.sqrt(3.0)
KAPPA = 2.0 - SQRT3
S0 = 0.0172


def bisect_root(fn, lo: float, hi: float, steps: int = 120) -> float:
    flo = fn(lo)
    fhi = fn(hi)
    assert flo * fhi <= 0.0
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        fm = fn(mid)
        if flo * fm <= 0.0:
            hi = mid
            fhi = fm
        else:
            lo = mid
            flo = fm
    return (lo + hi) / 2.0


def sigma_theta(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


THETA8 = bisect_root(sigma_theta, 2.6, 2.8)
PHI8 = 2.0 * PI - 2.0 * THETA8


def theta_for_sigma(s: float) -> float:
    return bisect_root(lambda t: sigma_theta(t) - s, THETA8, 2.9)


def tooth_f(q: float) -> float:
    return math.sin(q) + SQRT3 * (1.0 - math.cos(q)) - q


def tooth_fp(q: float) -> float:
    return math.cos(q) + SQRT3 * math.sin(q) - 1.0


def tooth_fpp(q: float) -> float:
    return -math.sin(q) + SQRT3 * math.cos(q)


def tooth_q(y: float) -> float:
    if y <= 0.0:
        return 0.0
    return bisect_root(lambda q: tooth_f(q) - y / 2.0, 0.0, 1.0)


def tooth_qp(y: float) -> float:
    q = tooth_q(y)
    return 1.0 / (2.0 * tooth_fp(q))


def tooth_qpp(y: float) -> float:
    q = tooth_q(y)
    fp = tooth_fp(q)
    return -tooth_fpp(q) / (4.0 * fp**3)


def seg_g(t: float) -> float:
    return (t - math.sin(t)) / 8.0


def seg_gp(t: float) -> float:
    return (1.0 - math.cos(t)) / 8.0


def seg_gpp(t: float) -> float:
    return math.sin(t) / 8.0


def endpoint_data(s: float) -> tuple[float, float, float, float]:
    theta = theta_for_sigma(s)
    u = 3.0 * theta - 2.0 * PI
    lam = math.sin(theta / 2.0)
    phi = 2.0 * PI - 2.0 * theta
    return theta, u, lam, phi


def h_value(s: float, y: float) -> float:
    theta, u, lam, _ = endpoint_data(s)
    w = s - y
    r = 10.0 * w / 3.0
    area = PI / 4.0 - seg_g(theta) - 2.0 * seg_g(PHI8 + r) - seg_g(r)
    b = tooth_q(y) + 10.0 * s / 3.0 - 7.0 * y / 3.0
    c = u - y
    return area - (25.0 * lam / 3.0) * w - 2.0 * c * b


def h_prime(s: float, y: float) -> float:
    theta, u, lam, _ = endpoint_data(s)
    r = 10.0 * (s - y) / 3.0
    ar = -2.0 * seg_gp(PHI8 + r) - seg_gp(r)
    b = tooth_q(y) + 10.0 * s / 3.0 - 7.0 * y / 3.0
    bp = tooth_qp(y) - 7.0 / 3.0
    c = u - y
    return (-10.0 / 3.0) * ar + 25.0 * lam / 3.0 + 2.0 * b - 2.0 * c * bp


def h_second(s: float, y: float) -> float:
    theta, u, _, _ = endpoint_data(s)
    r = 10.0 * (s - y) / 3.0
    arr = -2.0 * seg_gpp(PHI8 + r) - seg_gpp(r)
    bp = tooth_qp(y) - 7.0 / 3.0
    bpp = tooth_qpp(y)
    c = u - y
    return (100.0 / 9.0) * arr + 4.0 * bp - 2.0 * c * bpp


def min_h(s: float) -> tuple[float, float]:
    lo = 1e-12
    hi = s
    # h' is strictly increasing in the window used here.
    if h_prime(s, hi) <= 0.0:
        return h_value(s, hi), hi
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if h_prime(s, mid) < 0.0:
            lo = mid
        else:
            hi = mid
    y = (lo + hi) / 2.0
    return h_value(s, y), y


def main() -> None:
    theta0, u0, lam0, phi0 = endpoint_data(S0)
    qmax = tooth_q(S0)
    cmin = u0 - S0
    bmax = qmax + 10.0 * S0 / 3.0
    pz = 10.0 + 1.0 / KAPPA - 25.0 / 3.0
    z_derivative_lower = -lam0 * pz - 4.0 * bmax + (20.0 / 3.0) * cmin

    y_lo = 0.00669
    y_mid = 0.006695
    y_hi = 0.00670
    hp_lo = h_prime(S0, y_lo)
    hp_hi = h_prime(S0, y_hi)
    h_mid = h_value(S0, y_mid)
    hpp_mid = h_second(S0, y_mid)
    hmin, ymin = min_h(S0)

    mismatch = THETA8 / 2.0 - PI / 3.0 - (73.0 / 6.0) * S0
    tangent_extent = u0 + 10.0 * S0 / 3.0

    # Find the one-dimensional scalar envelope root.
    lo = 0.0172
    hi = 0.0174
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if min_h(mid)[0] > 0.0:
            lo = mid
        else:
            hi = mid
    scalar_root = (lo + hi) / 2.0

    print(f"theta0={theta0:.16f}")
    print(f"U0={u0:.16f}")
    print(f"lambda0={lam0:.16f}")
    print(f"phi0={phi0:.16f}")
    print(f"Qmax={qmax:.16f}")
    print(f"z_derivative_lower={z_derivative_lower:.16f}")
    print(f"mismatch={mismatch:.16f}")
    print(f"tangent_extent={tangent_extent:.16f}")
    print(f"Hprime_lo={hp_lo:.16f}")
    print(f"Hprime_hi={hp_hi:.16f}")
    print(f"H_mid={h_mid:.16f}")
    print(f"Hsecond_mid={hpp_mid:.16f}")
    print(f"H_min={hmin:.16f}")
    print(f"y_min={ymin:.16f}")
    print(f"scalar_root={scalar_root:.16f}")

    assert S0 < 0.0326
    assert 10.0 * S0 / 3.0 < 0.1
    assert phi0 > 0.87
    assert tangent_extent < PI
    assert mismatch > 0.094
    assert qmax < 0.101
    assert z_derivative_lower > 6.2
    assert hp_lo < -0.006
    assert hp_hi > 0.005
    assert hpp_mid > 1200.0
    assert h_mid > 0.0023269
    assert hmin > 0.0023268
    assert 0.00669 < ymin < 0.00670
    assert 0.01730 < scalar_root < 0.01732

    print("PASS: fully correlated sigma<=0.0172 scalar certificate")


if __name__ == "__main__":
    main()
