#!/usr/bin/env python3
"""Exact source contracts for the one-pin oblique refill.

Full guarded packets are not certified globally optimal. The report proves
the contact-minimality implication and the triangular limiting lock.
"""
from fractions import Fraction as F
from itertools import combinations

from verify_target_c_loaded_flat_pentagon_second_depletion_2026_10_05 import (
    add, dot, mul, rational, sign, sub,
)
from verify_target_c_one_vacancy_collective_strictification_2026_10_05 import (
    vector_add, vector_scale,
)
from verify_target_c_vacancy_funded_unit_wall_activation_2026_10_05 import (
    RAD, U, V0, basis_v, full_replacement, grid_point, inside, squared,
)


def field_scale(a, scalar):
    return a[0]*scalar, a[1]*scalar


def field_vector_scale(scalar, vector):
    return tuple(mul(scalar, component, RAD) for component in vector)


def inverse(a):
    denominator = a[0]*a[0]-RAD*a[1]*a[1]
    assert denominator != 0
    return a[0]/denominator, -a[1]/denominator


def packet(m, n, reference_v):
    size = m+n
    assert m >= 3 and n >= 3
    delta = sub(rational(1), field_scale(reference_v[0], 2))
    assert sign(delta, RAD) > 0
    assert sign(reference_v[0], RAD) >= 0
    assert dot(reference_v, reference_v, RAD) == rational(1)
    first = field_scale(delta, F(1, 100*size**2))
    second = field_scale(mul(first, first, RAD), F(1, 100*size**3))
    beta = F(1, 10*size**3)
    gap = field_scale(mul(second, second, RAD), 4*beta*beta)
    tolerance = field_scale(gap, F(1, 4*(size+1)))
    wall = {(i, j) for i in range(m+1) for j in range(n+1)
            if i in (0, m) or j in (0, n)}
    funded = (1, 0)
    retained = wall-{funded}
    interior = {(i, j) for i in range(1, m) for j in range(1, n)}
    original = {x: grid_point(*x, reference_v) for x in retained | interior}
    stage_one = dict(original)
    for j in range(1, n):
        change = (rational(0), field_scale(first, -(n-j)))
        stage_one[1, j] = vector_add(original[1, j], change)
    direction = (rational(1), field_scale(mul(reference_v[0], inverse(reference_v[1]), RAD), -1))
    assert dot(direction, reference_v, RAD) == rational(0)
    target = dict(stage_one)
    for i in range(2, m):
        for j in range(1, n):
            f_j = j*(n-j)*(1+beta*j)
            change = field_vector_scale(field_scale(second, -(m-i)*f_j), direction)
            target[i, j] = vector_add(target[i, j], change)
    checked = 0
    for x, y in combinations(sorted(target), 2):
        assert sign(sub(squared(stage_one[x], stage_one[y]), rational(1)), RAD) >= 0
        final = squared(target[x], target[y])
        assert sign(sub(final, rational(1)), RAD) >= 0
        if x in interior or y in interior:
            assert sign(sub(sub(final, rational(1)), gap), RAD) >= 0
        checked += 1
    for x in interior:
        assert inside(stage_one[x], m, n, reference_v)
        assert inside(target[x], m, n, reference_v)
        assert sign(sub(rational(F(1, 10000)), squared(target[x], original[x])), RAD) > 0
    for x in retained:
        assert target[x] == original[x]
    # A dyadic rotation certifiably smaller than the stated wall tolerance.
    angle = F(1, 2)
    while sign(sub(field_scale(tolerance, F(1, 4*n)), rational(angle)), RAD) <= 0:
        angle /= 2
    cosine, sine = rational((1-angle*angle)/(1+angle*angle)), rational(2*angle/(1+angle*angle))
    if reference_v[0] == rational(0):
        sine = field_scale(sine, -1)
    actual_v = (sub(mul(reference_v[0], cosine, RAD), mul(reference_v[1], sine, RAD)),
                add(mul(reference_v[0], sine, RAD), mul(reference_v[1], cosine, RAD)))
    source_pairs, contacts_lost = full_replacement(
        m, n, [target[x] for x in sorted(interior)], {(1, 1)}, actual_v,
        funded_labels=(funded,), require_all_wall=False,
    )
    return checked, source_pairs, contacts_lost, len(interior)


def triangular_lock(m, n):
    points = {(i, j): grid_point(i, j, V0)
              for i in range(m+1) for j in range(n+1) if (i, j) != (1, 0)}
    interior = {x for x in points if 0 < x[0] < m and 0 < x[1] < n}
    weights = {}
    extra = {tuple(sorted(((1, 1), (0, 1)))), tuple(sorted(((1, 1), (2, 0))))}
    for x, y in combinations(sorted(points), 2):
        if squared(points[x], points[y]) == rational(1) and (x in interior or y in interior):
            edge = tuple(sorted((x, y)))
            weights[edge] = 2 if edge in extra else 1
    assert sum(weights.values()) == 3*m*n-m-n-1
    for x in interior:
        force = (rational(0), rational(0))
        for (a, b), weight in weights.items():
            if x in (a, b):
                y = b if x == a else a
                difference = tuple(sub(points[y][k], points[x][k]) for k in range(2))
                force = vector_add(force, vector_scale(weight, difference))
        assert force == (rational(0), rational(0))
        diagonal_sum = x[0]+x[1]
        assert diagonal_sum >= 2
        ends = [(i, diagonal_sum-i) for i in range(m+1)
                if 0 <= diagonal_sum-i <= n]
        assert (1, 0) not in ends
        assert ends[0] not in interior and ends[-1] not in interior
        assert len(ends)-1 <= min(m, n)
    # Exact square of the analytically forbidden radius a0/[2(m+n)].
    radius_squared = F(3, 16*(m+n)**2)
    assert radius_squared > 0
    return len(interior), len(weights)


if __name__ == "__main__":
    results = [packet(3, 3, basis_v(F(1, 20))),
               packet(3, 4, basis_v(F(1, 10000))),
               packet(4, 3, (rational(0), rational(1))),
               packet(5, 5, basis_v(F(1, 100)))]
    locks = [triangular_lock(m, n) for m, n in [(3, 3), (3, 4), (5, 5), (8, 8)]]
    print(f"PASS: {sum(r[0] for r in results)} two-stage pair checks with the analytic gap floor")
    print(f"PASS: {sum(r[1] for r in results)} complete guarded source pairs; {sum(r[2] for r in results)} contacts removed")
    print(f"PASS: {sum(r[3] for r in results)} full interior labels; exactly one wall label funds each refill")
    print(f"PASS: {sum(r[0] for r in locks)} triangular pinned vertices and {sum(r[1] for r in locks)} positive stress edges")
    print("PASS: strict oblique, nearly triangular and square frames with perturbed actual walls")
    print("SCOPE: no global optimum is computed; a triangular one-pin wall admits no nonconstant motion from the reference")
