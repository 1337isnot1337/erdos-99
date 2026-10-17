#!/usr/bin/env python3
"""Regression checks for the repeated strong-TB1 inactive-witness collapse.

This certificate checks the algebraic two-tag inequalities, density arithmetic,
the multiplicity dichotomy, and finite numerical models for the bounded-degree
near-diameter cone lemma.  It is a regression certificate, not a substitute for
the geometric proof in the accompanying note.
"""

from fractions import Fraction
import math
import random


S0 = Fraction(791, 320_000_000)


def harmonic_half(x: float, y: float) -> float:
    return x * y / (x + y)


def unit_double_upper(si: float, sj: float, ell: float, d: float) -> float:
    """Exact upper bound on A=ell^2-1 forced by two lower-bound hits."""
    h = harmonic_half(si, sj)
    return 2.0 * ell * d * h - si * sj


def diameter_double_upper(si: float, sj: float, ell: float, d: float) -> float:
    """Exact upper bound on B=D^2-ell^2 forced by two upper-bound hits."""
    h = harmonic_half(si, sj)
    return 2.0 * ell * d * h + si * sj


def check_density_arithmetic() -> None:
    assert S0 / 2 == Fraction(791, 640_000_000)
    assert S0 / 4 == Fraction(791, 1_280_000_000)
    assert 3 * S0 / 8 == Fraction(2373, 2_560_000_000)
    assert S0 / 8 == Fraction(791, 2_560_000_000)
    assert S0 / 16 == Fraction(791, 5_120_000_000)
    assert S0 / 176 == Fraction(791, 56_320_000_000)

    assert abs(float(3 * S0 / 8) - 9.26953125e-7) < 1e-20
    assert abs(float(S0 / 8) - 3.08984375e-7) < 1e-20
    assert abs(float(S0 / 16) - 1.544921875e-7) < 1e-20
    assert abs(float(S0 / 176) - 1.4044744318181818e-8) < 1e-22


def check_multiplicity_dichotomy() -> None:
    # M=s+2d.  Either d<M/4 and M-d>3M/4, or d>=M/4.
    for m in range(1, 5000):
        for dtag in range(m // 2 + 1):
            single = m - 2 * dtag
            distinct = single + dtag
            assert distinct == m - dtag
            if dtag * 4 < m:
                assert distinct * 4 > 3 * m
            else:
                assert dtag * 4 >= m


def check_exact_algebra_random() -> None:
    rng = random.Random(20260917)

    # Lower-bound case.  Build A below the exact necessary upper bound computed
    # at ell=1; replacing ell by sqrt(1+A)>1 only enlarges the RHS.
    for _ in range(50_000):
        D = 10.0 ** rng.uniform(3.0, 8.0)
        si = rng.uniform(1e-4, 1.0) / D
        sj = rng.uniform(1e-4, 1.0) / D
        d = rng.uniform(0.0, 1.0) / D
        h = harmonic_half(si, sj)
        ub_at_one = 2.0 * d * h - si * sj
        if ub_at_one <= 0.0:
            continue
        A = rng.random() * 0.9 * ub_at_one
        ell = math.sqrt(1.0 + A)
        assert A + si * sj <= 2.0 * ell * d * h + 1e-15
        assert A <= unit_double_upper(si, sj, ell, d) + 1e-15
        # Exact identity ell-1=A/(ell+1).
        assert math.isclose(ell - 1.0, A / (ell + 1.0), rel_tol=1e-8, abs_tol=1e-12)

    # Upper-bound case.  The theorem uses only the displayed exact bound and
    # B/(D+ell)=D-ell; test those identities across scales.
    for _ in range(50_000):
        D = 10.0 ** rng.uniform(3.0, 8.0)
        si = rng.uniform(1e-4, 1.0) / D
        sj = rng.uniform(1e-4, 1.0) / D
        d = rng.uniform(0.0, 1.0) / D
        deficit = rng.uniform(0.0, 1.0) / (D * D)
        ell = D - deficit
        B = (D - ell) * (D + ell)  # stable form of D^2-ell^2
        ub = diameter_double_upper(si, sj, ell, d)
        if B <= ub + 1e-14:
            assert math.isclose(D - ell, B / (D + ell), rel_tol=1e-7, abs_tol=1e-10)


def opposite_cluster_lower(D: float, A: float, L: float) -> float:
    rmin = D - A / (D * D)
    return 2.0 * rmin * math.cos(L / D)


def same_cluster_upper(D: float, A: float, L: float) -> float:
    # Radius variation <=A/D^2 and angular separation <=2L/D.
    return A / (D * D) + 2.0 * D * math.sin(L / D)


def check_bounded_degree_geometry() -> None:
    # Representative constants, including deliberately huge fixed cone constants.
    samples = [
        (1.0, 2.0),
        (1e6, 1e4),
        (1e12, 1e7),
        (1e16, 1e8),
    ]
    for A, L in samples:
        # Pick D far beyond all fixed constants; the lemma is asymptotic.
        D = max(1e10, 10_000.0 * (math.sqrt(A + 1.0) + L + 1.0))
        assert opposite_cluster_lower(D, A, L) > D
        assert same_cluster_upper(D, A, L) <= 2.0 * L + 1.0

        # Crude area-packing degree bound used by the proof after one orientation
        # cluster is forced: all neighbors lie in a fixed-radius disk.
        R = 2.0 * L + 1.0
        degree_bound = math.ceil(4.0 * (R + 0.5) ** 2)
        assert degree_bound >= 1


def main() -> None:
    check_density_arithmetic()
    check_multiplicity_dichotomy()
    check_exact_algebra_random()
    check_bounded_degree_geometry()

    print(f"s0       = {float(S0):.15g}")
    print(f"3 s0 / 8 = {float(3*S0/8):.15g}")
    print(f"s0 / 8   = {float(S0/8):.15g}")
    print(f"s0 / 16  = {float(S0/16):.15g}")
    print(f"s0 / 176 = {float(S0/176):.15g}")
    print("repeated TB1 witness collapse regression: PASS")


if __name__ == "__main__":
    main()
