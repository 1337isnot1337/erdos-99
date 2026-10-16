#!/usr/bin/env python3
"""Exact finite subset-reflection and nonconstant gap regression checks.

Encodes rational unit directions, all original source-pair distances, assigned
ordered layers, positive aggregate cut reactions, interval derivative rank,
strong connectivity, fixed-exterior reflections, and their full diameter signs.
Omits actual contact cutsets, vertex KKT, the full source stress, the transverse
complete grid, near-disk/population hypotheses, and global optimality. The formal
cut reactions are NOT a source stress. See the report and research/README.md.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
import json

Vec = tuple[F, F]
ZERO: Vec = (F(0), F(0))


def add(a: Vec, b: Vec) -> Vec:
    return a[0] + b[0], a[1] + b[1]


def sub(a: Vec, b: Vec) -> Vec:
    return a[0] - b[0], a[1] - b[1]


def scale(t: F, a: Vec) -> Vec:
    return t * a[0], t * a[1]


def dot(a: Vec, b: Vec) -> F:
    return a[0] * b[0] + a[1] * b[1]


def norm2(a: Vec) -> F:
    return dot(a, a)


def turn(a: Vec) -> Vec:
    return -a[1], a[0]


def circle(t: F) -> Vec:
    den = 1 + t * t
    return (1 - t * t) / den, 2 * t / den


def reflect(v: Vec, axis: Vec) -> Vec:
    return sub(scale(2 * dot(v, axis) / norm2(axis), axis), v)


def rank(rows: list[list[F]]) -> int:
    mat = [row[:] for row in rows]
    pivot = 0
    for col in range(len(mat[0])):
        row = next((i for i in range(pivot, len(mat)) if mat[i][col]), None)
        if row is None:
            continue
        mat[pivot], mat[row] = mat[row], mat[pivot]
        factor = mat[pivot][col]
        mat[pivot] = [x / factor for x in mat[pivot]]
        for i in range(pivot + 1, len(mat)):
            factor = mat[i][col]
            if factor:
                mat[i] = [x - factor * y for x, y in zip(mat[i], mat[pivot])]
        pivot += 1
        if pivot == len(mat):
            break
    return pivot


def check_nonpermutation() -> dict[str, int]:
    old = [circle(t) for t in (F(0), F(1, 100), F(3, 100))]
    axis = tuple(sum(v[c] for v in old) for c in (0, 1))
    new = [reflect(v, axis) for v in old]
    assert all(norm2(v) == 1 for v in old + new)
    assert [sum(v[c] for v in old) for c in (0, 1)] == [
        sum(v[c] for v in new) for c in (0, 1)
    ]
    assert all(v not in old for v in new), "this reflection must create fresh phases"
    shifts = [ZERO]
    for before, after in zip(old, new):
        shifts.append(add(shifts[-1], sub(after, before)))
    assert shifts[-1] == ZERO
    assert all(dot(shift, axis) == 0 for shift in shifts)
    assert all(add(v, sub(shifts[i + 1], shifts[i])) == new[i]
               for i, v in enumerate(old))
    return {"fresh_phase_directions": len(new)}


def check_packet(m: int, exhaustive: bool) -> dict[str, int]:
    diameter = F(100 * m)
    points = [ZERO]
    layers = [0]
    star_rows: list[tuple[int, Vec, F]] = []
    unit = [circle(F(i, 10**6 * m**3)) for i in range(1, m + 1)]
    forces = [scale(F(m - i), unit[i]) for i in range(m)] + [ZERO]
    masses = [F(m - i) for i in range(m)]
    cut_targets = forces[:-1]
    class_mass: list[F] = []

    for j in range(1, m + 1):
        c, s = circle(F(m - j + 1, 10 * m))
        pos = scale(diameter, (c, s))
        neg = scale(diameter, (c, -s))
        delta_force = sub(forces[j - 1], forces[j])
        plus = (delta_force[0] / pos[0] + delta_force[1] / pos[1]) / 2
        minus = (delta_force[0] / pos[0] - delta_force[1] / pos[1]) / 2
        assert plus > 0 and minus > 0
        assert add(scale(plus, pos), scale(minus, neg)) == delta_force
        class_mass.append(plus + minus)
        assert class_mass[-1] < 2 / diameter
        points.extend([pos, neg])
        layers.extend([j, j])
        star_rows.extend([(j, pos, plus), (j, neg, minus)])

    pair_count = 0
    actual_diameters = 0
    for a, b in combinations(range(len(points)), 2):
        distance2 = norm2(sub(points[b], points[a]))
        assert 1 < distance2 <= diameter * diameter
        if distance2 == diameter * diameter:
            assert a == 0
            actual_diameters += 1
        pair_count += 1
    assert actual_diameters == 2 * m

    matrix: list[list[F]] = []
    for layer, r, weight in star_rows:
        matrix.append([dot(r, turn(u)) if i < layer else F(0)
                       for i, u in enumerate(unit)])
    assert rank(matrix) == m
    for i, target in enumerate(cut_targets):
        resultant = ZERO
        for layer, r, weight in star_rows:
            if layer > i:
                resultant = add(resultant, scale(weight, r))
        assert resultant == target
        assert resultant == scale(masses[i], unit[i])
        assert sum(weight * dot(r, turn(unit[i]))
                   for layer, r, weight in star_rows if layer > i) == 0
        assert sum(class_mass[j - 1] * j for j in range(i + 1, m + 1)) < masses[i]

    # The innermost diameter star rays bound a direction cell containing every u_i.
    p_inner, n_inner = points[-2:]
    for u in unit:
        assert dot(p_inner, turn(u)) > 0
        assert dot(n_inner, turn(u)) < 0

    adjacency = [set() for _ in range(m + 1)]
    for layer, r, weight in star_rows:
        if dot(r, turn(unit[0])) > 0:
            adjacency[0].add(layer)
        else:
            adjacency[layer].add(0)
    for start in range(m + 1):
        reached = {start}
        pending = [start]
        while pending:
            for dest in adjacency[pending.pop()]:
                if dest not in reached:
                    reached.add(dest)
                    pending.append(dest)
        assert len(reached) == m + 1

    if exhaustive:
        selected_sets = [tuple(i for i in range(m) if mask >> i & 1)
                         for mask in range(1, 1 << m) if mask.bit_count() >= 2]
    else:
        selected_sets = [tuple(range(m)), tuple(range(0, m, 2)), (0, m - 1),
                         (0, m // 2, m - 1)]
    checked_subsets = 0
    diameter_sign_checks = 0
    for selected in selected_sets:
        axis: Vec = (sum(unit[i][0] for i in selected),
                     sum(unit[i][1] for i in selected))
        reflected = [reflect(u, axis) if i in selected else u
                     for i, u in enumerate(unit)]
        shifts = [ZERO]
        for old, new in zip(unit, reflected):
            assert norm2(new) == 1
            increment = sub(new, old)
            assert dot(increment, axis) == 0
            shifts.append(add(shifts[-1], increment))
        assert shifts[0] == shifts[-1] == ZERO
        assert any(shift != ZERO for shift in shifts)
        assert all(add(old, sub(shifts[i + 1], shifts[i])) == reflected[i]
                   for i, old in enumerate(unit))
        total_work = F(0)
        grow = shrink = 0
        for layer, r, weight in star_rows:
            displacement = shifts[layer]
            work = dot(r, displacement)
            change = norm2(add(r, displacement)) - norm2(r)
            if displacement == ZERO:
                assert change == work == 0
            else:
                assert work != 0 and work * change > 0
                grow += int(change > 0)
                shrink += int(change < 0)
            total_work += weight * work
            diameter_sign_checks += 1
        contact_work = sum(masses[i] * dot(unit[i], sub(reflected[i], unit[i]))
                           for i in range(m))
        assert total_work == contact_work < 0
        assert grow and shrink
        checked_subsets += 1

    # The unit line is an explicit nonglobality certificate, not merely a status label.
    assert 2 * m < diameter
    return {"m": m, "source_pairs": pair_count, "actual_diameters": actual_diameters,
            "reflection_subsets": checked_subsets, "diameter_sign_checks": diameter_sign_checks}


def check_one_sign_contrast() -> dict[str, int]:
    diameter = F(200)
    c1, s1 = circle(F(1, 10))
    c2, s2 = circle(F(1, 20))
    p1, n1 = scale(diameter, (c1, s1)), scale(diameter, (c1, -s1))
    p2, n2 = scale(diameter, (c2, s2)), scale(diameter, (c2, -s2))
    u1, u2 = circle(F(1, 10**6)), (F(1), F(0))
    mass2 = u1[0] - u1[1] * c1 / s1
    weight1 = u1[1] / (diameter * s1)
    weight_n1 = mass2 / (100 * diameter)
    target = sub(scale(mass2, u2), scale(weight_n1, n1))
    weight2p = (target[0] / p2[0] + target[1] / p2[1]) / 2
    weight2n = (target[0] / p2[0] - target[1] / p2[1]) / 2
    assert min(mass2, weight1, weight_n1, weight2p, weight2n) > 0
    full_resultant = add(scale(weight_n1, n1),
                         add(scale(weight2p, p2), scale(weight2n, n2)))
    assert full_resultant == scale(mass2, u2)
    assert add(full_resultant, scale(weight1, p1)) == u1
    assert rank([[dot(p1, turn(u1)), F(0)],
                 [dot(p2, turn(u1)), dot(p2, turn(u2))]]) == 2
    full_weight = weight_n1 + weight2p + weight2n
    assert weight1 + 2 * full_weight < 1
    assert 2 * full_weight < mass2
    displacement = sub(u2, u1)
    points = [ZERO, p1, n1, p2, n2]
    new_points = [ZERO, add(p1, displacement), n1, p2, n2]
    assert norm2(new_points[1]) < diameter * diameter
    for a, b in combinations(range(5), 2):
        old_distance2 = norm2(sub(points[b], points[a]))
        new_distance2 = norm2(sub(new_points[b], new_points[a]))
        assert 1 < old_distance2 <= diameter * diameter
        assert 1 < new_distance2 <= diameter * diameter
        if old_distance2 < diameter * diameter:
            assert new_distance2 < diameter * diameter
    assert norm2(add(u1, displacement)) == norm2(sub(u2, displacement)) == 1
    assert 4 < diameter
    return {"source_pairs": 10, "strictly_shortened_diameters": 1,
            "unchanged_diameters": 3, "inactive_blockers": 0}


def main() -> None:
    summary = {"arithmetic": "exact rational", "nonpermutation": check_nonpermutation(),
               "packets": [check_packet(m, exhaustive=m <= 8)
                           for m in (2, 3, 4, 5, 6, 7, 8, 12, 16)],
               "one_sign_contrast": check_one_sign_contrast(),
               "scope": "geometric and aggregate cut regression; no source KKT or global optimality"}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
