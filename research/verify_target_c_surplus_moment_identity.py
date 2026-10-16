"""Exact arithmetic checks for the surplus--moment scalar audit.

This certifies the finite algebraic identities and checks one rational normalized
witness against the displayed scalar inequalities. It does not construct a geometric
source, certify global optimality, or resolve C-II.
"""

from __future__ import annotations

from fractions import Fraction as F
from math import pi, sqrt


def main() -> None:
    q, m, k, c_i = (F(7), F(3), F(2), F(1))
    s_c = m + k - 2 - c_i
    mathcal_m = q - m + 2 * s_c - 3 * k
    s_d = F(5)
    g_d = 2 + q + m - k - s_d

    assert s_d + g_d == mathcal_m + 2 * c_i + 6
    assert q - m - 2 * k == 2 * (q - k) - mathcal_m - k - 2 * c_i - 4

    # Rational normalized witness from the research note.
    t = F(1821, 1000)
    kappa = F(0)
    s = F(13993, 5000)
    g = F(1197, 5000)
    mu = s + g
    m_norm = mu - t
    e = t - m_norm
    u = F(13, 125)
    q_defect = e - 2 * kappa - u
    f = F(1, 2)

    assert m_norm >= 0
    assert e >= 0
    assert q_defect >= f >= 0
    assert q_defect + u == e - 2 * kappa

    c_star = pi * (2 - sqrt(3)) / 4
    c_det = pi * (2 - sqrt(3)) / 2
    delta2 = pi / (2 * sqrt(3))

    assert t >= 1.8208835379
    assert 5 * t - 2 * kappa >= float(s) + 2 * float(mu) + c_star
    assert 5 * t - 2 * float(mu) - 2 * float(kappa) >= 2 * sqrt(delta2)
    assert float(u + mu + kappa) >= pi
    assert 2 * (float(t + kappa) - float(s)) + 2 * float(e - kappa) + 4 * float(f) >= c_det
    assert 4 * float(f) + float(q_defect) <= 10 * float(e - kappa)

    print("surplus-moment identity: OK")
    print("scalar witness: OK")


if __name__ == "__main__":
    main()
