#!/usr/bin/env python3
"""Exact simultaneous full-interior refill with polynomial wall tolerance.

Deleting the lower and left side pins opens one collective motion. The
source packets have exterior guards and a linear integer population
deficit; no packet is certified globally optimal.
"""
from fractions import Fraction as F
from itertools import combinations

from verify_target_c_loaded_flat_pentagon_second_depletion_2026_10_05 import (
    add, dot, mul, rational, sign, sub, vsub,
)
from verify_target_c_one_vacancy_collective_strictification_2026_10_05 import (
    vector_add, vector_scale,
)
from verify_target_c_vacancy_funded_unit_wall_activation_2026_10_05 import (
    RAD, U, V0, basis_v, full_replacement, grid_point, inside, squared,
)


def packet(m, n, reference_v=V0):
    assert m >= 4 and n >= 4
    size = m+n
    epsilon, amplitude = F(1, 10*size**4), F(1, 100*size**3)
    gap_floor = F(3, 250000*size**14)
    wall_tolerance = gap_floor/(4*(size+1))
    assert wall_tolerance < F(1, 20)
    funded = {(i, 0) for i in range(m)} | {(0, j) for j in range(1, n)}
    assert len(funded) == m+n-1
    wall = {(i, j) for i in range(m+1) for j in range(n+1)
            if i in (0, m) or j in (0, n)}
    retained_wall = wall-funded
    interior = {(i, j) for i in range(1, m) for j in range(1, n)}
    target = {}
    scalar = {}
    direction = vector_add(U, reference_v)
    assert sign(reference_v[0], RAD) >= 0
    assert sign(sub(rational(F(1, 2)), reference_v[0]), RAD) >= 0
    assert dot(reference_v, reference_v, RAD) == rational(1)
    for i, j in interior:
        left, down = m-i, n-j
        scalar[i, j] = left*down*(1+epsilon*left)
        target[i, j] = vector_add(grid_point(i, j, reference_v), vector_scale(-amplitude*scalar[i, j], direction))
        assert inside(target[i, j], m, n, reference_v)
        assert sign(sub(rational(F(1, 10000)), squared(target[i, j], grid_point(i, j, reference_v))), RAD) > 0
    for x in retained_wall:
        scalar[x] = F(0)
        target[x] = grid_point(*x, reference_v)
    checked = 0
    for x, y in combinations(sorted(target), 2):
        old_d = squared(grid_point(*x, reference_v), grid_point(*y, reference_v))
        new_d = squared(target[x], target[y])
        assert sign(sub(new_d, rational(1)), RAD) >= 0
        if x in interior or y in interior:
            assert sign(sub(new_d, rational(1+gap_floor)), RAD) >= 0
            if old_d == rational(1):
                assert scalar[x] != scalar[y]
        checked += 1
    angle_t = wall_tolerance/(4*n)
    cosine, sine = rational((1-angle_t*angle_t)/(1+angle_t*angle_t)), rational(2*angle_t/(1+angle_t*angle_t))
    # Rotate toward the interior of the admissible angular interval.
    rotation_sign = -1 if reference_v[0] == rational(0) else 1
    sine = (rotation_sign*sine[0], rotation_sign*sine[1])
    v = (sub(mul(reference_v[0], cosine, RAD), mul(reference_v[1], sine, RAD)),
         add(mul(reference_v[0], sine, RAD), mul(reference_v[1], cosine, RAD)))
    assert dot(v, v, RAD) == rational(1)
    assert 2*n*angle_t < wall_tolerance
    target_list = [target[x] for x in sorted(interior)]
    holes = set(sorted(interior)[:len(funded)])
    assert len(holes) == len(funded)
    pairs, contacts_lost = full_replacement(m, n, target_list, holes, v,
                                          funded_labels=tuple(sorted(funded)), require_all_wall=False)
    return checked, pairs, contacts_lost, len(interior), wall_tolerance


if __name__ == "__main__":
    results = [packet(m, n) for m, n in [(4, 4), (4, 5), (6, 6), (8, 8)]]
    results += [packet(4, 5, basis_v(F(1, 20))),
                packet(5, 4, (rational(0), rational(1)))]
    print(f"PASS: {sum(r[0] for r in results)} exact local pairs and uniform squared-distance floor")
    print(f"PASS: {sum(r[1] for r in results)} complete guarded source pairs; {sum(r[2] for r in results)} contacts removed")
    print(f"PASS: {sum(r[3] for r in results)} full interior labels moved simultaneously")
    print("PASS: triangular, strict oblique and square reference frames, including nearby actual walls")
    print("PASS: polynomial gap 3/(250000*(m+n)^14) and wall tolerance gap/[4*(m+n+1)]")
    print("PASS: displacement < 1/100, all exterior labels fixed, full maximum diameter unchanged")
    print("SCOPE: actual enclosing wall and linear population deficiency remain source hypotheses")
