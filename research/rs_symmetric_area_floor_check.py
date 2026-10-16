#!/usr/bin/env python3
"""Numerical diagnostics for the 2026-09-10 FSRS Target C report.

This script evaluates the exact constants defined in
`docs/reports/target_c_rs_symmetric_area_floor_059214_2026-09-10.md` and samples
the two-variable relaxed feasible region used in Theorem FSRS.1.

Encoded assumptions:
- rho is the positive solution of rho = cos(rho);
- Phi(y) = (y + sin y)/4;
- Psi(p) = pi/(pi-2)^2 * (p/2-1)^2;
- 2 rho <= y <= pi and max(2,y) <= p <= pi;
- the relaxed ZK/JC inequality (4.8) in the report.

Omitted assumptions:
- no packing coordinates, KKT system, contact graph, global optimality, or
  finite-D error terms are encoded.

Arithmetic: IEEE-754 binary64 floating point.
A successful run verifies only the displayed decimal constants and numerical
shape of the relaxed minimization. It is not a proof of FSRS.1, FSRS.2, or
Erdos Problem #99.
"""

from __future__ import annotations

import math

PI = math.pi
C_RS = PI / (PI - 2.0) ** 2


def bisect_root(func, lo: float, hi: float, iterations: int = 100) -> float:
    flo = func(lo)
    fhi = func(hi)
    if flo == 0.0:
        return lo
    if fhi == 0.0:
        return hi
    if flo * fhi > 0.0:
        raise ValueError("root is not bracketed")
    for _ in range(iterations):
        mid = (lo + hi) / 2.0
        fmid = func(mid)
        if flo * fmid <= 0.0:
            hi = mid
            fhi = fmid
        else:
            lo = mid
            flo = fmid
    return (lo + hi) / 2.0


def phi(y: float) -> float:
    return (y + math.sin(y)) / 4.0


def psi(p: float) -> float:
    return C_RS * (p / 2.0 - 1.0) ** 2


def pc(y: float) -> float:
    return 2.0 + 2.0 * (PI - 2.0) * math.sqrt(phi(y) / PI)


def threshold(area: float, m: float) -> float:
    a = PI * PI + 1.0
    b = 2.0 * m
    c = m * m - 4.0 * PI * area
    return (-b + math.sqrt(b * b - 4.0 * a * c)) / (2.0 * a)


def relaxed_threshold(y: float, p: float) -> float:
    area = max(phi(y), psi(p))
    m = min(y, p - y)
    return threshold(area, m)


def main() -> None:
    rho = bisect_root(lambda x: math.cos(x) - x, 0.7, 0.8)
    y0 = bisect_root(lambda y: psi(2.0 * y) - phi(y), 2.0 * rho, PI / 2.0)
    p0 = 2.0 * y0
    lambda_rs = threshold(phi(y0), y0)
    lambda_fsjc = bisect_root(
        lambda lam: (PI * PI + 1.0) * lam * lam
        + PI * lam
        - PI * PI / 4.0
        - PI,
        0.5,
        0.7,
    )
    perimeter_mismatch = y0 - 2.0 * math.cos(y0 / 2.0)

    print(f"rho={rho:.16f}")
    print(f"y0={y0:.16f}")
    print(f"p0={p0:.16f}")
    print(f"Phi(y0)={phi(y0):.16f}")
    print(f"lambda_RS={lambda_rs:.16f}")
    print(f"lambda_FSJC={lambda_fsjc:.16f}")
    print(f"explicit_gain={lambda_rs-lambda_fsjc:.16f}")
    print(f"perimeter_mismatch={perimeter_mismatch:.16f}")

    assert 2.0 * rho < y0 < PI / 2.0
    assert abs(pc(y0) - 2.0 * y0) < 1e-12
    assert abs(psi(p0) - phi(y0)) < 1e-12
    assert lambda_rs > lambda_fsjc
    assert perimeter_mismatch > 0.0

    # Diagnostic grid only: verify that no sampled point beats the claimed
    # exact minimizer of the relaxed two-variable region.
    sampled_min = float("inf")
    sampled_arg = None
    n_y = 1200
    n_p = 1200
    for i in range(n_y + 1):
        y = 2.0 * rho + (PI - 2.0 * rho) * i / n_y
        p_lo = max(2.0, y)
        for j in range(n_p + 1):
            p = p_lo + (PI - p_lo) * j / n_p
            value = relaxed_threshold(y, p)
            if value < sampled_min:
                sampled_min = value
                sampled_arg = (y, p)

    print(f"sampled_min={sampled_min:.16f}")
    if sampled_arg is not None:
        print(f"sampled_arg_y={sampled_arg[0]:.16f}")
        print(f"sampled_arg_p={sampled_arg[1]:.16f}")
    # The grid need not hit (y0,p0) exactly, so its minimum should be no
    # smaller than the exact minimum apart from rounding.
    assert sampled_min >= lambda_rs - 5e-12


if __name__ == "__main__":
    main()
