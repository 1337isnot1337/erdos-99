#!/usr/bin/env python3
"""Regression checks for the THIN partner-star bandwidth theorem."""

from __future__ import annotations

import itertools
import math
from decimal import Decimal, getcontext


def eta(D: float) -> float:
    return 3.0 ** 0.25 * math.sqrt(D)


def ell(D: float) -> float:
    return D - 1.0 / (4.0 * D)


def xi(D: float) -> float:
    return math.sqrt((D + 2.0 * eta(D)) ** 2 - ell(D) ** 2)


def star_cap(D: float) -> float:
    return 1.0 + (8.0 * xi(D) + 2.0 * math.pi * math.sqrt(3.0)) / 15.0


def check_acute_algebra() -> None:
    # Verify PS.9--PS.10 in high precision to avoid cancellation at large D.
    getcontext().prec = 60
    for raw in ["1.01", "2", "10", "1000", "1000000"]:
        D = Decimal(raw)
        l = D - Decimal(1) / (Decimal(4) * D)
        lhs1 = Decimal(2) * l * l - D * D
        rhs1 = D * D - Decimal(1) + Decimal(1) / (Decimal(8) * D * D)
        assert abs(lhs1 - rhs1) < Decimal("1e-50")
        assert lhs1 > 0

        lhs2 = l * l + Decimal(1) - D * D
        rhs2 = Decimal(1) / Decimal(2) + Decimal(1) / (Decimal(16) * D * D)
        assert abs(lhs2 - rhs2) < Decimal("1e-50")
        assert lhs2 > 0


def check_xi_expansion() -> None:
    # PS.18 exact expansion, checked at scales where binary-float subtraction is stable.
    for D in [2.0, 10.0, 1e2, 1e4]:
        e = eta(D)
        direct = xi(D) ** 2
        expanded = 4.0 * D * e + 4.0 * e**2 + 0.5 - 1.0 / (16.0 * D**2)
        assert math.isclose(direct, expanded, rel_tol=2e-10, abs_tol=2e-7)


def check_asymptotic_constant() -> None:
    target = 16.0 * 3.0 ** (1.0 / 8.0) / 15.0
    vals = []
    for D in [1e4, 1e6, 1e8, 1e10, 1e12]:
        vals.append(star_cap(D) / D ** 0.75)
    # The explicit finite-D coefficient approaches the claimed leading constant.
    assert abs(vals[-1] - target) < 1e-6
    assert all(abs(vals[i + 1] - target) < abs(vals[i] - target) for i in range(len(vals) - 1))

    generic = 8.0 * 3.0 ** (1.0 / 8.0)
    assert math.isclose(generic / target, 7.5, rel_tol=1e-14)


def check_density_arithmetic() -> None:
    gamma = 791.0 / 9_600_000_000.0
    star_lead = 16.0 * 3.0 ** (1.0 / 8.0) / 15.0

    sync = (gamma / 160.0) / star_lead
    host = sync / 2.0
    rail = host / 2.0

    sync_formula = 15.0 * gamma / (2560.0 * 3.0 ** (1.0 / 8.0))
    rail_formula = 15.0 * gamma / (10240.0 * 3.0 ** (1.0 / 8.0))

    assert math.isclose(sync, sync_formula, rel_tol=1e-14)
    assert math.isclose(rail, rail_formula, rel_tol=1e-14)
    assert abs(sync - 4.2083939478243584e-10) < 1e-22
    assert abs(rail - 1.0520984869560896e-10) < 1e-22


def check_spacing_extremes() -> None:
    # Exhaust small 15-spaced owner sets. Their extreme region gap is at least 15(d-1).
    universe = range(0, 91)
    for d in range(1, 7):
        checked = 0
        for comb in itertools.combinations(universe, d):
            if all(comb[k + 1] - comb[k] >= 15 for k in range(d - 1)):
                assert comb[-1] - comb[0] >= 15 * (d - 1)
                checked += 1
                if checked >= 300:
                    break
        assert checked > 0


def check_triangle_bound_numerically() -> None:
    # Numerical sanity check of PS.17 on a grid of acute common-partner triangles
    # satisfying the source circumradius cap. The written proof is algebraic; this
    # catches sign/factor regressions in the formula used by the certificate.
    for D in [10.0, 30.0, 100.0, 1000.0]:
        lo = ell(D)
        Rmax = D / 2.0 + eta(D)
        upper = 2.0 * xi(D)
        for af in [0.0, 0.25, 0.5, 0.75, 0.99]:
            a = lo + af * (D - lo)
            for bf in [0.0, 0.4, 0.8, 0.99]:
                b = lo + bf * (D - lo)
                for k in range(1, 200):
                    theta = (math.pi / 2.0) * k / 200.0
                    c2 = a * a + b * b - 2.0 * a * b * math.cos(theta)
                    if c2 <= 0.0:
                        continue
                    c = math.sqrt(c2)
                    if not (1.0 <= c <= D):
                        continue
                    # All three angles acute iff each squared side is below sum of other two.
                    if not (a * a < b * b + c * c and b * b < a * a + c * c and c * c < a * a + b * b):
                        continue
                    Rtri = c / (2.0 * math.sin(theta))
                    if Rtri <= Rmax:
                        assert c < upper * (1.0 + 1e-12)


def main() -> None:
    check_acute_algebra()
    check_xi_expansion()
    check_asymptotic_constant()
    check_density_arithmetic()
    check_spacing_extremes()
    check_triangle_bound_numerically()
    print("PASS: THIN partner-star bandwidth certificate")


if __name__ == "__main__":
    main()
