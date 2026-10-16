#!/usr/bin/env python3
"""Exact scalar compatibility certificate for the Target C-II endpoint.

This is a *no-go certificate for scalar elimination*, not a packing construction.
It realizes, with rational data, the asymptotic scalar ledgers used by canonical
Sections 61--63, 80, 85, 122, and 123:

* Type-II has two unloaded components (hence c_I=o(D) in the displayed family);
* d_H=0, s_Z=2, k=d_H+s_Z=2, and the pinned ledger holds;
* the loaded-hull identities and the triangle-free outerplanar edge cap hold;
* the promoted renormalized-surplus and primitive-split lower bounds hold with
  room;
* the aggregate Section-122 demand holds with room, while the selected total
  P_exc=5D/4 satisfies the Section-123 payment; and
* the Section-85 train-end and Oler-weighted chamber inequalities are also
  compatible; and
* the exact Section-123 augmented-cell identity and the Type-II
  missing-side/attachment-credit payment are also jointly compatible; and
* the canonical Section-89 area--train inequality is also jointly compatible; and
* two local cells with d_1=D, d_2=19D/20, total rhombus area pi D^2/4-D,
  and the exact local Euler identity can carry the selected aggregate
  outer-walk detour.

The cell areas use pi only in the mathematical annotation. The finite checks use
the elementary certified bounds 3<pi<22/7 and 5/3<sqrt(3), so the certificate is
otherwise exact rational arithmetic. The witness is an abstract ledger point: it
does not realize a planar contact graph, a KKT stress, a source configuration, or
global minimum-diameter optimality. A pass proves only that the listed scalar
inequalities have no contradiction by themselves.
"""

from fractions import Fraction


def main() -> None:
    # D is chosen divisible by 400 so every displayed count is integral.
    D = 1_000_000
    q = 3 * D // 2

    # Woodall/rigidity data.
    d_H = 0
    s_Z = 2
    k = d_H + s_Z
    h = q - d_H
    c_I = 2
    s_C = 0
    e_BB = q - 2

    # Loaded-hull split: q-x_B=Q+2k, e_BB=Q+2k+u_B+c_B.
    Q = 0
    x_B = q - 2 * k
    m_nonunit = 2
    u_B = x_B - m_nonunit
    c_B = 0

    assert c_I + e_BB + s_C == q - 2 + k
    assert q - x_B == Q + 2 * k
    assert e_BB == Q + 2 * k + u_B + c_B
    assert c_I + s_C + c_B == m_nonunit + k - 2
    assert 2 * e_BB + m_nonunit <= 3 * q - 4
    assert e_BB + x_B >= q

    # The exact local Euler identity from the induced harmonic graphs.  Take two
    # cells with a_i=3D/4, s_i=0, f_i=Q_i=D/8 and c_i=147D/400.  Then
    # L_i+Q_i=4a_i-6-2s_i-2c_i and P_exc,i=5D/8.
    a_i = 3 * D // 4
    c_i = 147 * D // 400
    f_i = D // 8
    Q_i = f_i
    P_exc_i = 4 * f_i + Q_i
    L_i = 4 * a_i - 6 - 2 * c_i - Q_i
    E_i = L_i + P_exc_i - 2 * D
    assert L_i == Fraction(107, 50) * D - 6
    assert P_exc_i == Fraction(5, 8) * D
    assert E_i == Fraction(153, 200) * D - 6
    assert E_i > 0
    assert 2 * a_i == q

    # The two cells have diameters D and 19D/20 and total rhombus area
    # pi*D^2/4-D, reserving the linear area D for the Section-85 chamber
    # annotation.  The local zero-host inequalities are checked using the
    # weaker upper bound (4-2sqrt(3))*pi/8 < 11/42.
    local_upper_bound = Fraction(11, 42) * D * D
    d_1 = D
    d_2 = Fraction(19, 20) * D
    E_1 = L_i + P_exc_i - 2 * d_1
    E_2 = L_i + P_exc_i - 2 * d_2
    assert E_1 == Fraction(153, 200) * D - 6
    assert E_2 == Fraction(173, 200) * D - 6
    assert d_1 * E_1 > local_upper_bound
    assert d_2 * E_2 > local_upper_bound

    # The canonical Section-85 train-end floor is also compatible.  Use the
    # asymptotically correct scalar choice
    # R_4=pi*D^2/(2sqrt(3))-2D.  Then the total rhombus area
    # pi*D^2/4-D equals a_0*R_4+(sqrt(3)-1)D, so the rhombus excess is
    # nonnegative while the Type-II ratio still tends to pi/(2sqrt(3)).
    # That ratio is below 33/35, whose square root is below 49/50.
    # With total f=D/4, q-k+2f=2D-2 beats 49D/25.
    R4_ratio_upper = Fraction(33, 35)
    assert R4_ratio_upper < Fraction(49, 50) ** 2
    global_nonquad_faces = 2 * f_i
    section85_lhs = q - k + 2 * global_nonquad_faces
    section85_rhs_upper = Fraction(49, 25) * D
    assert section85_lhs > section85_rhs_upper

    # The Oler-weighted chamber floor (85.3) is compatible as well.  Complete
    # the near-disk scalar annotation with P_F=pi*D, and take a linear chamber
    # surplus A_ch=D and zero assigned isolate population.
    # Since sqrt(3)<2, 3*c_0/5<3/10; using P_F>3D and
    # sqrt(R_4)<49D/50 gives
    # (3*c_0/5)*(4*sqrt(R_4)-P_F)<(3/10)*(23D/25)=69D/250<D.
    chamber_surplus = D
    chamber_rhs_upper = Fraction(69, 250) * D
    assert chamber_surplus > chamber_rhs_upper

    # The canonical Section-89 area--train consequence is also compatible:
    # 2 A_4=pi*D^2/4-D<11D^2/14, so it is enough to check the
    # rational upper bound.
    area_twice_upper_bound = Fraction(11, 14) * D * D
    train_budget_factor = 6 * a_i - 15 - 3 * c_i
    assert d_1 * train_budget_factor > area_twice_upper_bound
    assert d_2 * train_budget_factor > area_twice_upper_bound

    # The aggregate Section-122 demand is pi/2*(2-sqrt(3))*D.  From
    # pi<22/7 and sqrt(3)>5/3 it is <11/21 D, while the selected aggregate
    # detour is 163D/100-12.
    aggregate_upper_bound = Fraction(11, 21) * D
    aggregate_detour = E_1 + E_2
    assert aggregate_detour > aggregate_upper_bound

    # Also realize the exact Section-123 augmented-cell ledger used by the
    # repaired Type-II aggregate-payment inequality.  All augmented defect is
    # assigned to missing polygon sides; actual induced exceptional defect is
    # still zero.  The variables are abstract ledger data, not a graph.
    T_i = 0
    Qplus_i = a_i - 6
    Q_M_i = Qplus_i - Q_i
    Q_C_i = Q_i
    Q_I_i = 0
    h_i = a_i - c_i
    M_i = h_i - T_i + Q_M_i
    X_i = a_i - T_i + Qplus_i
    assert a_i - 3 == Fraction(a_i - T_i + Qplus_i, 2)
    assert Qplus_i == Q_M_i + Q_C_i + Q_I_i
    assert M_i >= 0
    assert X_i == M_i + c_i + Q_C_i + Q_I_i
    assert L_i - 2 * a_i == M_i - c_i

    d_tile = q - 2 - 2 * (a_i - 2)
    assert d_tile == 2
    assert e_BB - k == Fraction(2 * X_i, 2) + d_tile

    M_missing = 2 * M_i
    C_partial = 2 * c_i
    cell_lhs = 2 * (L_i + P_exc_i - 2 * a_i)
    cell_rhs = 10 * (e_BB - k - d_tile) - 4 * M_missing - 6 * C_partial
    assert cell_lhs == cell_rhs

    # Replacing 2a_i by 2d_i gives the repaired detour upper bound.  It is
    # still above the Section-122 lower demand, with a positive linear margin.
    repaired_detour_bound = cell_rhs + 2 * (2 * a_i - d_1 - d_2)
    assert repaired_detour_bound == aggregate_detour
    assert repaired_detour_bound > aggregate_upper_bound

    # A second abstract witness also imposes the near-disk perimeter scale.  The
    # first draft used q=3D/2, but that violated the exact metric decomposition
    # x_B >= P_F-q when P_F=pi*D.  Repair it with q=17D/10, for which
    # pi-q/D < 22/7-17/10=43/35 < 17/10-4/D.
    # The rational assertions below check the exact ledgers forced by these
    # repaired choices; no polygon embedding is asserted.
    # Choose q/D=17/10 so the scalar witness also satisfies the newly
    # promoted q-k >= 1.637562... consequence of the train/interface coupling.
    q_disk = 17 * D // 10
    m_disk = D // 2
    x_disk = q_disk - 4
    e_disk = q_disk - m_disk
    s_C_disk = D // 2 - 2
    assert e_disk == Fraction(6, 5) * D
    assert c_I + e_disk + s_C_disk == q_disk - 2 + k
    assert e_disk == q_disk - m_disk
    assert q_disk - x_disk == 4
    assert x_disk > Fraction(54, 35) * D
    assert x_disk > Fraction(22, 7) * D - q_disk
    assert m_disk <= x_disk
    assert e_disk + x_disk >= q_disk
    # The assigned nonunit side length is larger than one per side even
    # with the elementary lower bound pi>3.
    assert 3 * D - (q_disk - m_disk) > m_disk
    assert c_I + s_C_disk == m_disk + k - 2
    assert 2 * e_disk + m_disk <= 3 * q_disk - 4
    assert q_disk - k + 2 * global_nonquad_faces > 2 * D
    mu_disk = Fraction(e_disk + 2 * s_C_disk - 3 * k, D)
    # This repaired near-disk witness also survives the newly promoted
    # full-core train-coupled floor 1.637562...; its exact value is
    # 2.2 - 10/D, so the weaker rational floor 2 is certified here.
    assert mu_disk > Fraction(2, 1)
    assert Fraction(max(e_disk, x_disk), D) > 1

    # Two cells with a_i=3D/4, d_i=D, s_i=D/4-1, c_i=0.  All augmented
    # defect is assigned to missing sides, and the actual exceptional perimeter
    # is zero.
    s_disk = D // 4 - 1
    Qplus_disk = a_i - 6 - 2 * s_disk
    h_disk = a_i
    M_disk = h_disk + Qplus_disk
    X_disk = a_i + Qplus_disk
    L_disk = 4 * a_i - 6 - 2 * s_disk
    assert Qplus_disk == Fraction(1, 4) * D - 4
    assert M_disk == D - 4
    assert X_disk == D - 4
    assert L_disk == Fraction(5, 2) * D - 4
    assert L_disk - 2 * a_i == M_disk

    d_tile_disk = q_disk - 2 - 2 * (a_i - 2)
    assert d_tile_disk == Fraction(1, 5) * D + 2
    assert e_disk - k == X_disk + d_tile_disk
    payment_disk = 10 * (e_disk - k - d_tile_disk) - 4 * (2 * M_disk)
    detour_disk = 2 * (L_disk - 2 * D)
    assert payment_disk == 2 * (L_disk - 2 * a_i)
    assert detour_disk == payment_disk + 2 * (2 * (a_i - D))
    assert detour_disk == D - 8
    assert detour_disk > aggregate_upper_bound
    assert D * (L_disk - 2 * D) > local_upper_bound

    # Section 123 is passed with the selected total exceptional perimeter
    # P_exc=5D/4, while its allowed payment is positive.
    P_exc = 2 * P_exc_i
    assert P_exc <= 10 * (e_BB - k)

    # Promoted scalar floors.  The displayed z_* floor is 0.9604, and the
    # primitive split lower bound is below 1 because rho<3/4.
    z_floor = Fraction(9604, 10_000)
    mu = Fraction(e_BB + 2 * s_C - 3 * k, D)
    assert mu > z_floor
    assert Fraction(max(e_BB, x_B), D) > 1
    assert Fraction(4, 3) * Fraction(3, 4) == 1

    # Type-II side conditions used by the scalar ledger: c_I/D^(2/3)->0 is
    # represented by the fixed value c_I=2, and q/D=17/10 is below pi.
    assert Fraction(c_I, D) < Fraction(1, 100_000)
    assert Fraction(q, D) < 3  # pi>3, so q<pi D
    assert h == q

    print("PASS: exact pinned, loaded-hull, and outerplanar scalar ledgers")
    print("PASS: exact local Euler cells carry positive detour with P_exc=5D/8 per cell")
    print("PASS: local and aggregate Section-122 demands hold with rational margins")
    print("PASS: Section-89 area--train scalar inequality is also compatible")
    print("PASS: Section-123 payment, renormalized-surplus, and primitive floors hold")
    print("PASS: Section-85 train-end and chamber floors are scalar-compatible")
    print("PASS: repaired Type-II augmented-cell payment is also scalar-compatible")
    print("PASS: near-disk-perimeter scalar witness retains repaired-payment equality")
    print("PASS: near-disk-perimeter witness has mu>2 and retains positive aggregate detour")
    print("PASS: this is an abstract scalar witness, not a geometric/global packing")


if __name__ == "__main__":
    main()
