#!/usr/bin/env python3
"""Exact contracts for complete exceptional-face elimination.

Positive boundary-pinned pentagon/hexagon packets test geometry and rank.
Sparse graphs are abstract incidence ledgers. The seven-point triangular
wheel is an actual unit-separated source with actual positive KKT loads,
but global optimality is not used or certified by this script.
"""
from fractions import Fraction as F
from itertools import combinations

from verify_target_c_global_phase_access_2026_10_05 import actual_packet
from verify_target_c_loaded_flat_pentagon_second_depletion_2026_10_05 import (
    add, dot, mul, neg, rational, sign, vsub,
)
from verify_target_c_pentagon_closure_core_elimination_2026_10_05 import (
    field_rank, glued_pentagons,
)
from verify_target_c_loaded_pentagon_wall_regression_2026_10_05 import Q5


def general_peeling():
    graphs, orders = 0, 0
    for n in range(1, 7):
        pairs = list(combinations(range(n), 2))
        cuts = [(mask.bit_count(), sum(1 << k for k, (a, b) in enumerate(pairs)
                                       if mask >> a & 1 and mask >> b & 1))
                for mask in range(1, 1 << n)]
        for graph in range(1 << len(pairs)):
            if graph.bit_count() > 2*n-2:
                continue
            if any((graph & inside).bit_count() > 2*size-2 for size, inside in cuts):
                continue
            adjacency = [set() for _ in range(n)]
            for k, (a, b) in enumerate(pairs):
                if graph >> k & 1:
                    adjacency[a].add(b)
                    adjacency[b].add(a)
            graphs += 1
            for valences in ([5]*n, [5+i % 3 for i in range(n)], [6+i % 4 for i in range(n)]):
                remaining = set(range(n))
                while remaining:
                    at = next((v for v in remaining if len(adjacency[v] & remaining) <= 3), None)
                    assert at is not None
                    external = valences[at]-len(adjacency[at] & remaining)
                    assert external >= 2
                    if valences[at] >= 6:
                        assert external >= 3
                        # A strictly convex physical face has at most
                        # two side occurrences in any projective direction.
                        assert external > 2
                    remaining.remove(at)
                orders += 1
    return graphs, orders


def triangular_wheel():
    rad, a0 = F(3), (F(0), F(1, 2))
    pos = [(rational(1), rational(0)), (rational(F(1, 2)), a0),
           (rational(F(-1, 2)), a0), (rational(-1), rational(0)),
           (rational(F(-1, 2)), neg(a0)), (rational(F(1, 2)), neg(a0)),
           (rational(0), rational(0))]
    contacts, diameters = [], []
    for i, j in combinations(range(7), 2):
        d = vsub(pos[j], pos[i])
        d2 = dot(d, d, rad)
        assert sign((d2[0]-1, d2[1]), rad) >= 0
        assert sign((4-d2[0], -d2[1]), rad) >= 0
        if d2 == rational(1):
            contacts.append((i, j))
        if d2 == rational(4):
            diameters.append((i, j))
    assert len(contacts) == 12 and len(diameters) == 3
    rows = []
    for i, j in contacts:
        row = [rational(0)]*14
        d = vsub(pos[j], pos[i])
        row[2*i:2*i+2] = [neg(x) for x in d]
        row[2*j:2*j+2] = d
        rows.append(row)
    assert field_rank(rows, rad) == 11
    pure = {e: rational(1 if 6 in e else -1) for e in contacts}
    for i in range(7):
        signed, kkt = [rational(0), rational(0)], [rational(0), rational(0)]
        for edges, multiplier, target in ((contacts, pure, signed),
                                           (contacts, {e: rational(F(1, 3)) for e in contacts}, kkt),
                                           (diameters, {e: rational(F(-1, 3)) for e in diameters}, kkt)):
            for e in edges:
                if i in e:
                    j = e[0] if e[1] == i else e[1]
                    d = vsub(pos[j], pos[i])
                    for c in range(2):
                        target[c] = add(target[c], mul(multiplier[e], d[c], rad))
        assert signed == kkt == [rational(0), rational(0)]
    assert len(contacts)-field_rank(rows, rad) == 1
    return 21


def weighted_energy_regressions():
    # The genuine triangle-free unit regular pentagon has positive actual
    # diameter loads. Its two target bar realizations test both failures:
    # a separated five-point target with longer maximum, and a contracted
    # target with vertex collisions. Neither is a strict competitor.
    contacts = sorted({tuple(sorted((i, (i+1) % 5))) for i in range(5)})
    diameters = sorted({tuple(sorted((i, (i+2) % 5))) for i in range(5)})
    d2, r2 = Q5(F(3, 2), F(1, 2)), Q5(F(1, 2), F(1, 10))
    cosines = [Q5(1), Q5(F(-1, 4), F(1, 4)), Q5(F(-1, 4), F(-1, 4))]
    original = [[r2*cosines[min((i-j) % 5, (j-i) % 5)] for j in range(5)]
                for i in range(5)]
    omega = [[Q5() for _ in range(5)] for _ in range(5)]
    for edges, coefficient in ((contacts, F(1, 5)*d2), (diameters, Q5(F(-1, 5)))):
        for i, j in edges:
            omega[i][i] += coefficient
            omega[j][j] += coefficient
            omega[i][j] -= coefficient
            omega[j][i] -= coefficient
    assert all(sum(row) == 0 for row in omega)
    assert all(sum(omega[i][k]*original[k][j] for k in range(5)) == 0
               for i in range(5) for j in range(5))
    tri_gram = [[F(0), F(0), F(0)], [F(0), F(1), F(1, 2)],
                [F(0), F(1, 2), F(1)]]
    colors = [0, 1, 0, 1, 2]
    collapsed = [[tri_gram[colors[i]][colors[j]] for j in range(5)] for i in range(5)]
    # Coordinates use y coefficients of sqrt(3), so all Gram entries are rational.
    trapezoid = [(F(0), F(0)), (F(1), F(0)), (F(2), F(0)),
                 (F(3, 2), F(1, 2)), (F(1, 2), F(1, 2))]
    separated = [[x*u+3*y*v for u, v in trapezoid] for x, y in trapezoid]
    for target, expected_mean, expected_zero_pairs in (
        (separated, F(12, 5), 0), (collapsed, F(3, 5), 2),
    ):
        distance2 = lambda i, j: target[i][i]+target[j][j]-2*target[i][j]
        assert all(distance2(i, j) == 1 for i, j in contacts)
        mean = sum(distance2(i, j) for i, j in diameters)/5
        assert mean == expected_mean and (d2-mean).sign() > 0
        energy = sum(omega[i][j]*target[i][j] for i in range(5) for j in range(5))
        assert energy == d2-mean
        zeros = sum(distance2(i, j) == 0 for i, j in combinations(range(5), 2))
        assert zeros == expected_zero_pairs
        maximum = max(distance2(i, j) for i, j in combinations(range(5), 2))
        if zeros:
            assert maximum == 1 and (d2-maximum).sign() > 0
        else:
            assert all(distance2(i, j) >= 1 for i, j in combinations(range(5), 2))
            assert maximum == 4 and (Q5(maximum)-d2).sign() > 0
    return 20


if __name__ == "__main__":
    pent_checks = sum(glued_pentagons(F(1, n)) for n in (10, 50, 1000))
    hex_checks = sum(actual_packet(n, t)[0] for n in (1, 2, 3, 6, 8)
                     for t in (F(1, 50), F(1, 40)))
    graphs, orders = general_peeling()
    wheel_checks = triangular_wheel()
    energy_checks = weighted_energy_regressions()
    print(f"PASS: {pent_checks} glued-pentagon and {hex_checks} positive hexagon-packet source-pair checks")
    print("PASS: complete face row rank and pure-contact independence in both packet classes")
    print(f"PASS: {graphs} (2,2)-sparse abstract endpoint graphs and {orders} mixed-valence elimination orders")
    print(f"PASS: {wheel_checks} actual wheel source pairs, positive normalized actual KKT loads and pure corank one")
    print("PASS: triangular wheel prevents dropping the triangle-free hypothesis")
    print(f"PASS: {energy_checks} target pair checks and exact finite weighted-diameter energy identities")
    print("PASS: lower-feasible mean contraction can lengthen the maximum; full contraction can collide vertices")
    print("SCOPE: finite geometry and rank contracts; no uniform chart radius or diameter descent")
