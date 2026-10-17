#!/usr/bin/env python3
"""Exact half-line arithmetic for the global source near-triangle candidate.

This certifies rational budget deductions under the named geometric inputs.
It is not a geometric or global-optimality certificate.
"""

from fractions import Fraction as Q


def positive_quadratic_on_halfline(a, b, c, onset):
    # Coefficients after substituting D=onset+x, x>=0.
    coeffs = (a * onset * onset + b * onset + c, 2 * a * onset + b, a)
    assert coeffs[0] > 0 and all(value >= 0 for value in coeffs)
    return coeffs


def certify():
    pi_lower, pi_upper = Q(3), Q(22, 7)
    root_lower, root_upper = Q(17, 10), Q(7, 4)
    assert root_lower**2 < 3 < root_upper**2
    assert pi_lower / (2 * root_upper) == Q(6, 7)
    assert pi_upper / (2 * root_lower) < 1
    assert (2 - root_upper) / 4 == Q(1, 16)
    sigma_slope = 140 * root_upper + pi_upper * root_upper / 4
    sigma_intercept = Q(351, 2) * root_upper
    assert sigma_slope < 247 and sigma_intercept < 308
    assert 247 * 30000 + 308 < 248 * 30000
    assert 20 * 30000 + 25 <= 21 * 30000
    assert pi_upper / 2 * 30000 + 1 < 2 * 30000
    debit = 52 * 21 + 24 * 2 + 64 * 248
    assert debit == 17012
    coeffs = positive_quadratic_on_halfline(Q(6, 7), -debit, 0, 30000)
    assert Q(248) / Q(6, 7) == Q(868, 3) < 290
    assert Q(290, 30000) < Q(1, 100)
    assert 100 * 30000 - 2102500 > 0
    assert Q(580, 60000) < Q(1, 100)
    assert 200 * 60000 - 8410000 > 0
    assert 3 * 24 == 72 and 2 * 72 == 144
    print(f"PASS full half-line population polynomial coefficients: {coeffs}")
    print("PASS completion/strip/obtuse debit: 17012*D")
    print("PASS single triangle: squared clearance <3000/D for D>=30000")
    print("PASS disjoint family: >=ceil(n/144), clearance <6000/D for D>=60000")
    print("Scope: exact arithmetic under canonical geometry; no unit-triangle conclusion")


if __name__ == "__main__":
    certify()
