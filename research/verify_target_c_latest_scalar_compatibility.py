#!/usr/bin/env python3
"""Exact scalar regression for the current Target C-II package.

This is a no-go certificate for scalar elimination.  It is intentionally *not*
claimed to be a planar contact graph, a KKT stress, a source configuration, or a
global minimizer.  The witness satisfies the current promoted scalar ledgers,
including the loaded-chord relation and the train-coupled floor

    mu >= (2*pi + 2*sqrt(pi/(2*sqrt(3))))/5.

All assertions use rational arithmetic.  The only occurrences of pi and sqrt(3)
are bounded in comments by 3 < pi < 22/7 and 5/3 < sqrt(3); those elementary
bounds are sufficient for every displayed strict margin.
"""

from fractions import Fraction


def main() -> None:
    D = 1_000_000

    # Loaded-hull and pinned ledgers, with the promoted loaded-chord conclusion
    # c_B=0 and e_BB=q-m_B.
    q = 8 * D // 5
    d_H = 0
    s_Z = 2
    k = d_H + s_Z
    c_I = 2
    m_B = D // 2
    e_BB = q - m_B
    s_C = D // 2 - 2

    x_B = q - 2 * k
    Q_B = 0
    c_B = 0
    u_B = x_B - m_B

    assert c_I + e_BB + s_C == q - 2 + k
    assert q - x_B == Q_B + 2 * k
    assert e_BB == q - m_B
    assert c_B == 0
    assert u_B >= 0
    assert c_I + s_C + c_B == m_B + k - 2
    assert 2 * e_BB + m_B <= 3 * q - 4

    mu_num = e_BB + 2 * s_C - 3 * k
    mu = Fraction(mu_num, D)
    # With pi<22/7 and sqrt(3)>5/3,
    # mu_TC < (44/7+2)/5 = 58/35.  The witness has mu=2.09999...
    assert mu > Fraction(58, 35)

    # Near-disk scalar perimeter decomposition.  P_F=pi D and q=8D/5;
    # pi>3 gives q<P_F, while pi<22/7 gives
    # P_F-q < (54/35)D < x_B.  Thus x_B can pay both the hull perimeter
    # excess and the occurrence-counted outer-walk excess.
    assert Fraction(q, D) < 3
    assert x_B > Fraction(54, 35) * D

    # Two actual-cell ledgers.  The values satisfy the exact augmented-cell
    # identity, with f nonquadrilateral faces of degree five and no actual
    # loaded-loaded attachment chords.
    a = 3 * D // 4
    s = D // 4 - 1
    c_partial = 0
    f = D // 8
    Q = f
    T = 0
    Q_plus = a - 6 - 2 * s
    Q_M = Q_plus - Q
    Q_C = Q
    Q_I = 0
    h = a - c_partial
    M = h - T + Q_M
    X = a - T + Q_plus
    L = 4 * a - 6 - 2 * s - 2 * c_partial - Q
    P_exc = 4 * f + Q

    assert Q_plus == Q_M + Q_C + Q_I
    assert X == 2 * (a - 3 - s)
    assert M >= 0
    assert X == M + c_partial + Q_C + Q_I
    assert L + Q == 4 * a - 6 - 2 * s - 2 * c_partial
    assert P_exc == Fraction(5, 8) * D

    # Two cells leave a positive polygon-dissection slack.  Section 123 is
    # satisfied exactly at the augmented-cell level.
    d_tile = q - 2 - 2 * (a - 2)
    assert d_tile == Fraction(1, 10) * D + 2
    assert e_BB - k == (2 * X) // 2 + d_tile

    M_missing = 2 * M
    C_partial = 2 * c_partial
    augmented_lhs = 2 * (L + P_exc - 2 * a)
    augmented_rhs = (
        10 * (e_BB - k - d_tile)
        - 4 * M_missing
        - 6 * C_partial
    )
    assert augmented_lhs == augmented_rhs

    # The actual Section-122 quantity uses d_i=D.  Its aggregate value is
    # 2D-8, while the canonical lower demand is
    # pi/2*(2-sqrt(3))*D < 11D/21.
    d = D
    cell_detour = L + P_exc - 2 * d
    aggregate_detour = 2 * cell_detour
    assert cell_detour == D - 4
    assert aggregate_detour == 2 * D - 8
    assert aggregate_detour > Fraction(11, 21) * D

    # The exceptional perimeter payment is also compatible:
    # sum P_exc=5D/4 <= 10(e_BB-k).
    assert 2 * P_exc <= 10 * (e_BB - k)

    # Section 85 train-end inequality.  With total f=D/4 and the asymptotic
    # rhombus count R4=pi D^2/(2sqrt(3))-2D, the elementary bounds give
    # 2sqrt(R4)<(98/50)D, whereas q-k+2f>21D/10-2.
    total_f = 2 * f
    assert q - k + 2 * total_f > Fraction(49, 25) * D
    # The ratio pi/(2sqrt(3)) is <33/35, and (49/50)^2>33/35.
    assert Fraction(33, 35) < Fraction(49, 50) ** 2

    # The two local zero-host area inequalities have ample rational margin.
    # The total rhombus area annotation is pi D^2/4-D; each cell gets half.
    local_area_upper = Fraction(11, 42) * D * D
    assert d * cell_detour > local_area_upper

    # The exact Section-89 same-cell train budget is compatible as well:
    # 2A4_i is <(11/28)D^2, while the right side is >3D^2.
    train_budget = 6 * a - 15 - 5 * s - 5 * c_partial
    assert d * train_budget > Fraction(11, 28) * D * D

    print("PASS: current loaded-chord and pinned scalar ledgers")
    print("PASS: current train-coupled mu floor with mu=2.09999...")
    print("PASS: exact augmented-cell identity and Section-123 payment")
    print("PASS: positive Section-122 detour remains scalar-compatible")
    print("PASS: train-end, near-disk, and local area annotations are compatible")
    print("PASS: abstract scalar witness is not a planar/global packing")


if __name__ == "__main__":
    main()
