#!/usr/bin/env python3
"""Finite scalar certificate for the proof-only sigma<=0.0105 sparse window.

This checks the endpoint arithmetic and conservative analytic inequalities in
`docs/reports/target_c_sparse_split_fullcore_window_0105_2026-09-12.md`.
It does not certify the inherited signed-return or geometric theorems and is not a
C-II or Level-I certificate.
"""

from __future__ import annotations

import math

PI = math.pi
SQRT3 = math.sqrt(3.0)
KAPPA = 2.0 - SQRT3
S0 = 0.0105


def bisect_root(fn, lo: float, hi: float, steps: int = 160) -> float:
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


def sigma_of_theta(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def tooth_f(q: float) -> float:
    return math.sin(q) + SQRT3 * (1.0 - math.cos(q)) - q


def tooth_q(y: float) -> float:
    if y == 0.0:
        return 0.0
    return bisect_root(lambda q: tooth_f(q) - y / 2.0, 0.0, PI / 3.0)


def segment_g(t: float) -> float:
    return (t - math.sin(t)) / 8.0


def main() -> None:
    theta8 = bisect_root(sigma_of_theta, 2.6, 2.8)
    phi8 = 2.0 * PI - 2.0 * theta8
    theta0 = bisect_root(lambda t: sigma_of_theta(t) - S0, theta8, 2.8)
    u0 = 3.0 * theta0 - 2.0 * PI
    lam0 = math.sin(theta0 / 2.0)
    phi0 = 2.0 * PI - 2.0 * theta0
    q0 = tooth_q(S0)

    area0 = (
        PI / 4.0
        - segment_g(theta0)
        - 2.0 * segment_g(phi8 + 10.0 * S0 / 3.0)
        - segment_g(10.0 * S0 / 3.0)
    )
    product0 = (u0 - S0) * (q0 + S0)

    qprime_lower = 1.0 / (2.0 * SQRT3 * 0.0785)
    pprime_lower = -0.1135 + 1.8217 * (qprime_lower - 7.0 / 3.0)

    coefficient_z = 10.0 + 1.0 / KAPPA
    exact_residual = area0 - lam0 * coefficient_z * S0 - 2.0 * product0
    rounded_residual = 0.4697 - 0.977 * 13.733 * S0 - 2.0 * 0.1622

    tangent_extent = u0 + 10.0 * S0 / 3.0
    corridor_margin = theta8 / 2.0 - PI / 3.0 - (73.0 / 6.0) * S0

    print(f"theta8={theta8:.16f}")
    print(f"theta0={theta0:.16f}")
    print(f"U0={u0:.16f}")
    print(f"lambda0={lam0:.16f}")
    print(f"phi0={phi0:.16f}")
    print(f"Q0={q0:.16f}")
    print(f"area_floor={area0:.16f}")
    print(f"product_max={product0:.16f}")
    print(f"Pprime_lower={pprime_lower:.16f}")
    print(f"tangent_extent={tangent_extent:.16f}")
    print(f"corridor_margin={corridor_margin:.16f}")
    print(f"exact_residual={exact_residual:.16f}")
    print(f"rounded_residual={rounded_residual:.16f}")

    assert S0 < 0.0326
    assert 10.0 * S0 / 3.0 < 0.1
    assert phi0 > 0.87
    assert tangent_extent < PI
    assert corridor_margin > 0.17
    assert q0 < 0.0785
    assert area0 > 0.4697
    assert product0 < 0.1622
    assert qprime_lower > 3.677
    assert pprime_lower > 2.3
    assert coefficient_z < 13.733
    assert exact_residual > 0.0047
    assert rounded_residual > 0.0044

    print("PASS: sigma<=0.0105 sparse-window endpoint certificate")


if __name__ == "__main__":
    main()
