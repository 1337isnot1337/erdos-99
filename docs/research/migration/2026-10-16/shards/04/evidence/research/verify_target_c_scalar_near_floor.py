#!/usr/bin/env python3
"""Exact scalar near-floor compatibility regression for Target C-II.

This certificate deliberately works only with the scalar ledgers.  It does not
construct a convex loaded hull, a planar contact graph, a KKT stress, a source
configuration, or a global minimizer.  Its purpose is to show that the current
post-123 scalar package has feasible assignments with the renormalized surplus
arbitrarily close above the train-coupled floor; the actual endpoint exclusion
therefore uses geometric train information that is absent from the scalar
inequalities.
"""

from fractions import Fraction
from math import isqrt


def main() -> None:
    # The large D removes all fixed Euler constants while keeping every displayed
    # quantity integral.  The normalized target is mu=1.637563+o(1), only about
    # 8.2e-7 above the exact train floor.
    D = 10**12

    # Certified rational bounds used only in strict comparisons:
    # pi < 104348/33215 and sqrt(3) > 1732050807568/10^12.  The latter gives
    # Delta=pi/(2 sqrt(3)) < 10863/11978; 952312807/10^9 is a strict upper
    # bound for sqrt(10863/11978).
    pi_u = Fraction(104348, 33215)
    sqrt3_l = Fraction(1732050807568, 10**12)
    delta_u = pi_u / (2 * sqrt3_l)
    sqrt_delta_u = Fraction(952312807, 10**9)
    assert sqrt_delta_u * sqrt_delta_u > delta_u

    # Loaded-hull/pinned ledger.  q+m_B is fixed at 1.637563 D, while q is
    # just above the endpoint q-coordinate and m_B is a small positive linear
    # quantity.  c_B=0 is the promoted loaded-chord relation.
    q = Fraction(26201, 16000) * D       # 1.6375625 D
    m_B = Fraction(1, 2_000_000) * D     # 0.0000005 D
    d_H = 0
    s_Z = 2
    k = d_H + s_Z
    c_I = 2
    e_BB = q - m_B
    s_C = m_B + k - c_I - 2
    x_B = q - 2 * k
    Q_B = 0
    c_B = 0

    assert c_I + e_BB + s_C == q - 2 + k
    assert q - x_B == Q_B + 2 * k
    assert e_BB == q - m_B
    assert c_B == 0
    assert c_I + s_C + c_B == m_B + k - 2
    assert 2 * e_BB + m_B <= 3 * q - 4
    assert x_B > (pi_u * D - q)

    mu = (e_BB + 2 * s_C - 3 * k) / D
    mu_floor_upper = (2 * pi_u + 2 * sqrt_delta_u) / 5
    assert mu > mu_floor_upper
    assert mu < Fraction(1637563, 10**6)

    # Two abstract attachment cells.  These values satisfy the exact augmented
    # Euler/dissection identities and retain a positive (but very small) m_B.
    a = Fraction(3, 4) * D
    f = Fraction(33383, 500_000) * D       # each cell; total f/D=0.133532
    Q = f
    T = 0
    d_tile = q - 2 - 2 * (a - 2)
    e_minus_k = e_BB - k
    X = e_minus_k - d_tile                # equal X_r in each cell
    Q_plus = X - a
    s = a - 3 - X / 2
    Q_M = Q_plus - Q
    Q_C = Q
    Q_I = 0
    M = a - T + Q_M
    L = 4 * a - 6 - 2 * s - Q
    P_exc = 4 * f + Q
    d = D

    assert all(v.denominator == 1 for v in
               (q, m_B, e_BB, s_C, a, f, d_tile, X, Q_plus, s,
                Q_M, M, L, P_exc))
    assert d_tile >= 0 and s >= 0 and Q_M >= 0 and M >= 0
    assert Q_plus == Q_M + Q_C + Q_I
    assert X == 2 * (a - 3 - s)
    assert e_minus_k == X + d_tile
    assert L + Q == 4 * a - 6 - 2 * s
    assert P_exc == 5 * Q

    # The repaired Type-II payment holds exactly at the augmented-cell level.
    M_missing = 2 * M
    augmented_lhs = 2 * (L + P_exc - 2 * a)
    augmented_rhs = (
        10 * (e_minus_k - d_tile)
        - 4 * M_missing
    )
    assert augmented_lhs == augmented_rhs
    assert 2 * P_exc <= 10 * e_minus_k

    # Section 122 remains satisfied with a large positive detour.  Its canonical
    # demand is below 11/21 D because 4-sqrt(3) > 11/21.
    cell_expression = L + P_exc - 2 * d
    aggregate_expression = 2 * cell_expression
    assert cell_expression > 0
    assert aggregate_expression > Fraction(11, 21) * D

    # Both train-floor inequalities are satisfied with strict rational margin:
    # u >= p/2 + Q_total/2 and u+2 f_total >= 2 sqrt(Delta)D.
    u = (q - k) / D
    f_total = 2 * f / D
    Q_total = 2 * Q / D
    assert u > pi_u / 2 + Q_total / 2
    assert u + 2 * f_total > 2 * sqrt_delta_u

    # The local zero-host and Section-89 budget inequalities have ample room in
    # this witness; these are the same scalar forms checked by the current
    # compatibility certificate.
    assert d * cell_expression > Fraction(11, 42) * D * D
    train_budget = 6 * a - 15 - 5 * s
    assert d * train_budget > Fraction(11, 28) * D * D

    print(f"mu={mu} ({float(mu):.12f})")
    print(f"certified_floor_upper={mu_floor_upper} ({float(mu_floor_upper):.12f})")
    print(f"mu_gap_above_certified_floor={mu - mu_floor_upper}")
    print(f"aggregate_section122_expression={aggregate_expression}")
    print("PASS: exact near-floor loaded/pinned scalar ledger")
    print("PASS: exact augmented-cell and Section-123 payment ledger")
    print("PASS: positive Section-122 detour remains compatible")
    print("PASS: near-floor train inequalities have strict rational margins")
    print("PASS: witness is scalar only, not a planar/global packing")


if __name__ == "__main__":
    main()
