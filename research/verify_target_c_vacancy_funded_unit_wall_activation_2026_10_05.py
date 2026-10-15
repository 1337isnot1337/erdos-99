#!/usr/bin/env python3
"""Exact two-vacancy motion and complete unit-wall source replacements.

Packets are actual unit-separated labelled planar sets with exterior
guards, not certified global minimizers. The analytic report supplies
contact-minimality implications and robust wall neighbourhoods.
"""
from fractions import Fraction as F
from itertools import combinations

from verify_target_c_loaded_flat_pentagon_second_depletion_2026_10_05 import (
    add, dot, mul, neg, rational, sign, sub, vsub,
)
from verify_target_c_one_vacancy_collective_strictification_2026_10_05 import (
    inside, vector_add, vector_scale, verify_packet,
)

RAD = F(3)
U = rational(1), rational(0)
V0 = rational(F(1, 2)), (F(0), F(1, 2))
DIRECTIONS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]


def grid_point(i, j, v):
    return add(rational(i), mul(rational(j), v[0], RAD)), mul(rational(j), v[1], RAD)


def squared(x, y):
    d = vsub(x, y)
    return dot(d, d, RAD)


def two_vacancy_packet(m, n, boundary_holes=False):
    assert m >= 3 and n >= 3
    holes = {(1, 0), (2, 0)} if boundary_holes else {(1, 1), (2, 1)}
    original = {(i, j): grid_point(i, j, V0)
                for i in range(m+1) for j in range(n+1) if (i, j) not in holes}
    wall = {x for x in original if x[0] in (0, m) or x[1] in (0, n)}
    interior = set(original)-wall
    assert len(interior) == (m-1)*(n-1)-(0 if boundary_holes else 2)
    order = []
    for j in range(1 if boundary_holes else 2, n):
        order.append(((1, j), ((1, j-1), (2, j-1))))
        order.append(((2, j), ((1, j), (2, j-1))))
    for i in range(3, m):
        order.append(((i, 1), ((i-1, 1), (i-1, 2))))
        for j in range(2, n):
            order.append(((i, j), ((i-1, j), (i, j-1))))
    assert {x for x, _ in order} == interior and len(order) == len(interior)
    points = dict(original)
    released = set(holes)
    checking_pairs, halvings = 0, []
    for x, required_free in order:
        assert all(y in released for y in required_free)
        missing_vectors = [grid_point(y[0]-x[0], y[1]-x[1], V0) for y in required_free]
        assert squared(missing_vectors[0], missing_vectors[1]) == rational(1)
        h = vector_add(*missing_vectors)
        active_neighbours = [y for y in original if y not in released and y != x
                             and squared(original[x], original[y]) == rational(1)]
        assert all(sign(dot(vsub(original[y], original[x]), h, RAD), RAD) <= 0
                   for y in active_neighbours)
        assert dot(h, h, RAD) == rational(3)
        t, halves = F(1, (100 if boundary_holes else 1)*(m+n)**2), 0
        while True:
            candidate = vector_add(original[x], vector_scale(t, h))
            valid = inside(candidate, m, n, V0)
            for y, p in points.items():
                if y == x:
                    continue
                checking_pairs += 1
                if sign(sub(squared(candidate, p), rational(1)), RAD) <= 0:
                    valid = False
            if valid:
                points[x] = candidate
                break
            t /= 2
            halves += 1
        released.add(x)
        halvings.append(halves)
    assert set(points) == set(original) and all(points[x] == original[x] for x in wall)
    strict_pairs = 0
    for x, y in combinations(sorted(points), 2):
        gap = sign(sub(squared(points[x], points[y]), rational(1)), RAD)
        assert gap >= 0
        if x in interior or y in interior:
            assert gap > 0
            strict_pairs += 1
    return points, wall, interior, checking_pairs, strict_pairs, halvings


def basis_v(t):
    denominator = 1+t*t
    return ((F(1-t*t, 2*denominator), -t/denominator),
            (t/denominator, F(1-t*t, 2*denominator)))


def full_replacement(m, n, target, holes, v, funded_labels=((0, 0),), require_all_wall=True):
    # Exterior guard labels remain at their original coordinates.
    old = {(i, j): grid_point(i, j, v)
           for i in range(-2, m+3) for j in range(-2, n+3)
           if (i, j) not in holes}
    wall = {x for x in old if 0 <= x[0] <= m and 0 <= x[1] <= n
            and (x[0] in (0, m) or x[1] in (0, n))}
    old_interior = sorted(x for x in old if 0 < x[0] < m and 0 < x[1] < n)
    replacement_labels = old_interior+list(funded_labels)
    assert len(replacement_labels) == len(target)
    new = dict(old)
    for label, p in zip(replacement_labels, target):
        new[label] = p
        assert inside(p, m, n, v)
        protected_wall = wall if require_all_wall else wall-set(funded_labels)
        assert all(sign(sub(squared(p, old[w]), rational(1)), RAD) > 0 for w in protected_wall)
    assert set(new) == set(old)
    old_max, new_max = rational(0), rational(0)
    old_contacts, new_contacts, pairs = 0, 0, 0
    external_guards = [x for x in old if x not in wall and x not in old_interior]
    for x, y in combinations(sorted(old), 2):
        old_d, new_d = squared(old[x], old[y]), squared(new[x], new[y])
        assert sign(sub(old_d, rational(1)), RAD) >= 0
        assert sign(sub(new_d, rational(1)), RAD) >= 0
        old_contacts += old_d == rational(1)
        new_contacts += new_d == rational(1)
        if x in replacement_labels or y in replacement_labels:
            assert sign(sub(new_d, rational(1)), RAD) > 0
        if sign(sub(old_d, old_max), RAD) > 0:
            old_max = old_d
        if sign(sub(new_d, new_max), RAD) > 0:
            new_max = new_d
        pairs += 1
    assert old_contacts > new_contacts and new_max == old_max
    for p in target:
        for g in external_guards:
            shield_floor = F(3) if require_all_wall else F(9, 4)
            assert sign(sub(squared(p, old[g]), rational(shield_floor)), RAD) >= 0
    # All retained contacts are inherited from the oblique bipartite grid.
    assert all(sum(abs(x[i]-y[i]) for i in range(2)) == 1
               for x, y in combinations(sorted(old), 2) if squared(old[x], old[y]) == rational(1))
    return pairs, old_contacts-new_contacts


def guard_regressions():
    a, b = (rational(0), rational(0)), U
    x, y = (rational(F(1, 2)), (F(0), F(1, 2))), (rational(F(1, 2)), (F(0), F(-1, 2)))
    assert all(squared(p, q) == rational(1) for p in (x, y) for q in (a, b))
    assert squared(x, y) == rational(3)
    # Opposite half-planes alone do not provide a shield: crossing is essential.
    x, y = (rational(2), rational(F(1, 100))), (rational(2), rational(F(-1, 100)))
    assert all(sign(sub(squared(p, q), rational(1)), RAD) > 0
               for p in (x, y) for q in (a, b))
    assert squared(x, y) == rational(F(1, 2500))


def one_triangular_vacancy_regression():
    # One triangular vacancy can remain locally jammed with fixed wall.
    a, b, c = (1, 2), (2, 1), (2, 2)
    weights = {}
    for x, y, w in [
        (a, b, F(1)), (a, c, F(1)), (b, c, F(1)),
        (a, (1, 3), F(1, 2)), (a, (0, 3), F(1, 2)), (a, (0, 2), F(3, 2)),
        (b, (3, 1), F(1, 2)), (b, (2, 0), F(3, 2)), (b, (3, 0), F(1, 2)),
        (c, (3, 2), F(1)), (c, (2, 3), F(1)),
        (c, (1, 3), F(1, 2)), (c, (3, 1), F(1, 2)),
    ]:
        assert w > 0
        assert squared(grid_point(*x, V0), grid_point(*y, V0)) == rational(1)
        weights[tuple(sorted((x, y)))] = w
    for x in (a, b, c):
        force = (rational(0), rational(0))
        wall_directions = []
        for (s, t), w in weights.items():
            if x not in (s, t):
                continue
            y = t if x == s else s
            d = vsub(grid_point(*y, V0), grid_point(*x, V0))
            force = vector_add(force, vector_scale(w, d))
            if y not in (a, b, c):
                wall_directions.append((y[0]-x[0], y[1]-x[1]))
        assert force == (rational(0), rational(0))
        assert any(r[0]*s[1]-r[1]*s[0] != 0 for r, s in combinations(wall_directions, 2))
    # Positive equilibrium makes every weak fixed-wall strut velocity a
    # bar flex; two independent wall rows at each label force that flex zero.


if __name__ == "__main__":
    checks, strict_checks, replacements, contacts_lost = 0, 0, 0, 0
    robustness_halvings = []
    for m, n in [(3, 3), (3, 4), (4, 3), (4, 4)]:
        points, wall, interior, checked, strict, halves = two_vacancy_packet(m, n)
        checks += checked
        strict_checks += strict
        target = [points[x] for x in sorted(interior)]
        t, halvings = F(1, 100*m*n*(m+n)), 0
        reference_wall = [grid_point(*x, V0) for x in sorted(wall)]
        wall_gaps = [sub(squared(p, w), rational(1)) for p in target for w in reference_wall]
        least_gap = wall_gaps[0]
        for gap in wall_gaps:
            if sign(sub(gap, least_gap), RAD) < 0:
                least_gap = gap
        # Each wall moves at most 2*n*t. Squared-distance loss is bounded
        # by 8*n*(m+n+1)*t. Select t with cheap exact scalar comparisons.
        gap_coefficient = 8*n*(m+n+1)
        while True:
            if sign(sub(least_gap, rational(gap_coefficient*t)), RAD) > 0:
                break
            t /= 2
            halvings += 1
        v = basis_v(t)
        actual_wall = [grid_point(*x, v) for x in sorted(wall)]
        assert all(inside(p, m, n, v) and all(sign(sub(squared(p, w), rational(1)), RAD) > 0
                                            for w in actual_wall) for p in target)
        assert dot(v, v, RAD) == rational(1)
        pair_count, lost = full_replacement(m, n, target, {(1, 1), (2, 1), (1, 2)}, v)
        replacements += pair_count
        contacts_lost += lost
        robustness_halvings.append(halvings)
    for m, n in [(3, 3), (4, 5)]:
        v = basis_v(F(1, 100*m*n*(m+n)))
        packet = verify_packet(m, n, 1, 1, F(1, 100*m*n*(m+n)), return_points=True)
        target = [packet["final"][x] for x in sorted(set(packet["final"])-packet["wall"])]
        pair_count, lost = full_replacement(m, n, target, {(1, 1), (2, 1)}, v)
        replacements += pair_count
        contacts_lost += lost
    guard_regressions()
    one_triangular_vacancy_regression()
    print(f"PASS: {checks} exact sequential-move pair checks; {strict_checks} final interior strict-pair checks")
    print(f"PASS: {replacements} complete old/new source-pair checks in six guarded replacements; {contacts_lost} contacts removed")
    print("PASS: all source labels retained, wall funding label moved into the interior, external guards fixed")
    print("PASS: every new/exterior-guard distance >= sqrt(3); full maximum diameter unchanged")
    print(f"PASS: fixed triangular targets survive positive oblique wall perturbations; halvings {robustness_halvings}")
    print("PASS: exact shield equality and noncrossing failure regression")
    print("PASS: one triangular vacancy has positive pinned stress and zero weak-motion cone")
    print("SCOPE: no guarded packet is asserted globally diameter-optimal; no actual-source vacancy is inferred")
