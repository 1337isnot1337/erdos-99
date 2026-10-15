#!/usr/bin/env python3
"""Exact collective strictification of a grid with one interior vacancy.

All wall points and all remaining source labels are retained. Q(sqrt(3))
arithmetic verifies every pair and container inequality after both stages.
The example grids are not actual minimum-diameter sources. No numerical
angle is asserted to lie in the nonexplicit fixed-wall uniqueness window.
"""
from fractions import Fraction as F
from itertools import combinations

from verify_target_c_loaded_flat_pentagon_second_depletion_2026_10_05 import (
    add, dot, mul, neg, rational, sign, sub, vsub,
)

RAD = F(3)


def inverse(x):
    a, b = x
    denominator = a*a-RAD*b*b
    assert denominator != 0
    return a/denominator, -b/denominator


def vector_add(x, y):
    return add(x[0], y[0]), add(x[1], y[1])


def vector_scale(c, x):
    return mul(rational(c), x[0], RAD), mul(rational(c), x[1], RAD)


def inside(p, m, n, v):
    j = mul(p[1], inverse(v[1]), RAD)
    i = sub(p[0], mul(v[0], j, RAD))
    return (sign(i, RAD) > 0 and sign(sub(rational(m), i), RAD) > 0
            and sign(j, RAD) > 0 and sign(sub(rational(n), j), RAD) > 0)


def verify_packet(m, n, a, b, angle_t, return_points=False):
    assert 0 < a < m and 0 < b < n
    denominator = 1+angle_t*angle_t
    v = ((F(1-angle_t*angle_t, 2*denominator), -angle_t/denominator),
         (angle_t/denominator, F(1-angle_t*angle_t, 2*denominator)))
    assert dot(v, v, RAD) == rational(1)
    original = {(i, j): (add(rational(i), mul(rational(j), v[0], RAD)),
                         mul(rational(j), v[1], RAD))
                for i in range(m+1) for j in range(n+1) if (i, j) != (a, b)}
    wall = {ij for ij in original if ij[0] in (0, m) or ij[1] in (0, n)}
    interior = set(original)-wall
    assert len(interior) == (m-1)*(n-1)-1
    axis = {ij for ij in interior if ij[0] == a or ij[1] == b}
    velocity = {ij: (rational(0), rational(0)) for ij in original}
    jv = neg(v[1]), v[0]
    ju = rational(0), rational(1)
    for i, j in axis:
        if j == b:
            coefficient = -F(i, a) if i < a else F(m-i, m-a)
            velocity[i, j] = vector_scale(coefficient, jv)
        else:
            coefficient = F(j, b) if j < b else -F(n-j, n-b)
            velocity[i, j] = vector_scale(coefficient, ju)
    old_contact = {tuple(sorted((x, y))) for x, y in combinations(sorted(original), 2)
                   if dot(vsub(original[y], original[x]), vsub(original[y], original[x]), RAD) == rational(1)}
    touching_axis = {e for e in old_contact if set(e) & axis}
    assert all(sum(abs(x[i]-y[i]) for i in range(2)) == 1 for x, y in old_contact)
    pairs = list(combinations(sorted(original), 2))

    def first_valid(points):
        if any(not inside(points[x], m, n, v) for x in interior):
            return False
        for x, y in pairs:
            dsq = dot(vsub(points[y], points[x]), vsub(points[y], points[x]), RAD)
            gap_sign = sign(sub(dsq, rational(1)), RAD)
            if gap_sign < 0:
                return False
            if (x, y) in touching_axis and gap_sign <= 0:
                return False
            if (x, y) not in old_contact and gap_sign <= 0:
                return False
        return True

    step_one, first_halvings = F(1, (m+n)**2), 0
    while True:
        first = {ij: vector_add(p, vector_scale(step_one, velocity[ij]))
                 for ij, p in original.items()}
        if first_valid(first):
            break
        step_one /= 2
        first_halvings += 1
    assert all(first[x] == original[x] for x in wall)

    # Dual basis vectors u* and v*: u.u*=v.v*=1, u.v*=v.u*=0.
    inverse_sine = inverse(v[1])
    dual_u = rational(1), neg(mul(v[0], inverse_sine, RAD))
    dual_v = rational(0), inverse_sine
    second_velocity = {ij: (rational(0), rational(0)) for ij in original}
    for i, j in interior-axis:
        ix, sx = (i, 1) if i < a else (m-i, -1)
        jy, sy = (j, 1) if j < b else (n-j, -1)
        second_velocity[i, j] = vector_add(vector_scale(sx*ix, dual_u),
                                           vector_scale(sy*jy, dual_v))

    def strict_valid(points):
        if any(not inside(points[x], m, n, v) for x in interior):
            return False
        for x, y in pairs:
            dsq = dot(vsub(points[y], points[x]), vsub(points[y], points[x]), RAD)
            gap_sign = sign(sub(dsq, rational(1)), RAD)
            if x in wall and y in wall:
                if gap_sign < 0:
                    return False
            elif gap_sign <= 0:
                return False
        return True

    step_two, second_halvings = step_one*step_one/(m+n)**2, 0
    while True:
        final = {ij: vector_add(p, vector_scale(step_two, second_velocity[ij]))
                 for ij, p in first.items()}
        if strict_valid(final):
            break
        step_two /= 2
        second_halvings += 1
    assert set(final) == set(original) and all(final[x] == original[x] for x in wall)
    assert len(final) == (m+1)*(n+1)-1
    assert all(dot(vsub(final[y], final[x]), vsub(final[y], final[x]), RAD) != rational(0)
               for x, y in pairs)
    # Explicit-family container capacity has no N+1 slot by Oler.
    assert 2*m*n*angle_t < 1
    metrics = len(pairs), len(interior), first_halvings, second_halvings
    if return_points:
        return {"original": original, "wall": wall, "final": final,
                "basis_v": v, "metrics": metrics}
    return metrics


if __name__ == "__main__":
    cases = [(3, 3, 1, 1), (4, 4, 2, 2), (4, 5, 1, 3), (6, 6, 3, 3)]
    results = [verify_packet(m, n, a, b, F(1, 100*m*n*(m+n)))
               for m, n, a, b in cases]
    print(f"PASS: {sum(r[0] for r in results)} exact full source-pair checks in four strictified patches")
    print(f"PASS: {sum(r[1] for r in results)} interior points all strictly separated from one another and every wall vertex")
    print("PASS: all source labels retained, wall coordinates fixed, all interior points inside the original container")
    print("PASS: both collective stages certified by rational halving and exact Q(sqrt(3)) inequalities")
    print(f"STEPS: first halvings {[r[2] for r in results]}; second halvings {[r[3] for r in results]}")
    print("SCOPE: no uniqueness angle window or minimum-diameter optimality certified")
