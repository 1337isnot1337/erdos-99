#!/usr/bin/env python3
"""Independent exact checks for the PR #614 hostile audit.

Builds an actual strict-rhombus contact grid around the packet's star regression.
Checks every old source pair, complete train contacts, positive A-cut resultants,
strong connectivity, and both finite diameter signs. Explicitly certifies failure
of transverse B-cut KKT and vertex KKT. It does not encode a global minimizer.
Separately enumerates small antitone gap trees. See research/README.md.
"""

from fractions import Fraction as F
from itertools import combinations
import json

ZERO = (F(0), F(0))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def mul(c, a):
    return c * a[0], c * a[1]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def n2(a):
    return dot(a, a)


def circle(t):
    return (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)


def reflection(v, axis):
    return sub(mul(2 * dot(v, axis) / n2(axis), axis), v)


def rank(rows):
    matrix = [row[:] for row in rows]
    r = 0
    for col in range(len(matrix[0])):
        pivot = next((j for j in range(r, len(matrix)) if matrix[j][col]), None)
        if pivot is None:
            continue
        matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        matrix[r] = [v / matrix[r][col] for v in matrix[r]]
        for j in range(r + 1, len(matrix)):
            c = matrix[j][col]
            matrix[j] = [v - c * w for v, w in zip(matrix[j], matrix[r])]
        r += 1
    return r


def check_empty_cut_scope():
    points = [ZERO, (F(10), F(0)), (F(20), F(0))]
    moved = [points[0], (F(10), F(1)), points[2]]
    assert all(n2(sub(p, q)) > 1 for p, q in combinations(points, 2))
    assert all(n2(sub(p, q)) > 1 for p, q in combinations(moved, 2))
    # With u_1 horizontal and u_2 above it, the y-axis reflection increments
    # are either zero or negative, so fixed exteriors force the zero move.
    units = [circle(F(0)), circle(F(1, 100))]
    assert units[0][1] == 0 and units[1][1] > 0
    return "empty cuts allow a nonzero fixed-exterior translation; nonempty cuts required"


def check_grid(m):
    diameter = F(100 * m)
    units = [circle(F(i, 10**6 * m**3)) for i in range(1, m + 1)]
    transverse = (F(8, 17), F(15, 17))
    assert n2(transverse) == 1
    assert all(n2(u) == 1 and 0 < dot(u, transverse) < F(1, 2) for u in units)
    prefixes = [ZERO]
    for u in units:
        prefixes.append(add(prefixes[-1], u))
    points = []
    layers = []
    labels = []
    grid_index = {}
    for a in range(m + 1):
        for b in range(m + 1):
            grid_index[a, b] = len(points)
            points.append(add(prefixes[a], mul(b, transverse)))
            layers.append(a)
            labels.append(("grid", a, b))
    assert points[0] == ZERO
    contacts = set()
    for a in range(m + 1):
        for b in range(m + 1):
            if a < m:
                contacts.add((grid_index[a, b], grid_index[a + 1, b]))
            if b < m:
                contacts.add((grid_index[a, b], grid_index[a, b + 1]))

    forces = [mul(m - i, units[i]) for i in range(m)] + [ZERO]
    bars = []
    fan_indices = []
    for j in range(1, m + 1):
        c, s = circle(F(m - j + 1, 10 * m))
        upper, lower = mul(diameter, (c, s)), mul(diameter, (c, -s))
        force = sub(forces[j - 1], forces[j])
        plus = (force[0] / upper[0] + force[1] / upper[1]) / 2
        minus = (force[0] / upper[0] - force[1] / upper[1]) / 2
        assert plus > 0 and minus > 0
        assert add(mul(plus, upper), mul(minus, lower)) == force
        for point, weight, side in ((upper, plus, "upper"), (lower, minus, "lower")):
            index = len(points)
            fan_indices.append(index)
            bars.append((j, point, weight, side))
            points.append(point)
            layers.append(j)
            labels.append((side, j, m if side == "upper" else 0))

    pairs = 0
    found_contacts = set()
    found_diameters = set()
    for i, j in combinations(range(len(points)), 2):
        distance2 = n2(sub(points[j], points[i]))
        assert 1 <= distance2 <= diameter**2
        if distance2 == 1:
            found_contacts.add((i, j))
        if distance2 == diameter**2:
            found_diameters.add((i, j))
        pairs += 1
    assert found_contacts == contacts
    assert found_diameters == {(0, j) for j in fan_indices}
    assert all(not any(j in e for e in contacts) for j in fan_indices)

    # Each selected A-cut has actual positive contact mass m-i+1.
    # Every B-contact has endpoints in one A-layer and does not cross an A-cut.
    for i in range(1, m + 1):
        resultant = ZERO
        for layer, bar, weight, side in bars:
            if layer >= i:
                resultant = add(resultant, mul(weight, bar))
        assert resultant == forces[i - 1] == mul(m - i + 1, units[i - 1])
        edge_weight = F(m - i + 1, m + 1)
        assert (m + 1) * edge_weight == m - i + 1

    matrix = [[det(units[i], bar) if i < layer else F(0)
               for i in range(m)] for layer, bar, weight, side in bars]
    assert rank(matrix) == m
    # The formal scalar cut form remains strictly positive by prefix domination.
    for i in range(m):
        prefix_bound = sum((bars[2 * j][2] + bars[2 * j + 1][2]) * (j + 1)
                           for j in range(i, m))
        assert prefix_bound < m - i

    # B-layer choices: upper fan on rail m, lower fan and root on rail 0.
    # Every B-cut sees the same positive upper-star resultant. It is not parallel
    # to the actual B-contact direction, so no positive B-cut mass can balance it.
    b_resultant = ZERO
    for layer, bar, weight, side in bars:
        if side == "upper":
            b_resultant = add(b_resultant, mul(weight, bar))
    assert b_resultant[0] > 0 and b_resultant[1] > 0
    assert det(transverse, b_resultant) < 0

    # A common empty witness cell and the bidirected star give strong connectivity.
    inner_upper, inner_lower = bars[-2][1], bars[-1][1]
    assert all(det(u, inner_upper) > 0 and det(u, inner_lower) < 0 for u in units)
    assert all(det(units[0], bar) > 0 if side == "upper"
               else det(units[0], bar) < 0 for layer, bar, weight, side in bars)

    if m > 8:
        subsets = [tuple(range(m)), (0, m - 1), (0, m // 2, m - 1)]
    else:
        subsets = [tuple(i for i in range(m) if mask >> i & 1)
                   for mask in range(1, 1 << m) if mask.bit_count() >= 2]
    sign_checks = 0
    for selected in subsets:
        axis = (sum(units[i][0] for i in selected), sum(units[i][1] for i in selected))
        new = [reflection(u, axis) if i in selected else u for i, u in enumerate(units)]
        shifts = [ZERO]
        for before, after in zip(units, new):
            shifts.append(add(shifts[-1], sub(after, before)))
            assert n2(after) == 1
        assert shifts[-1] == ZERO
        assert any(shift != ZERO for shift in shifts)
        # This proves every horizontal grid edge is still unit; vertical edges
        # have equal shifts at both endpoints and are unchanged exactly.
        for i in range(m):
            assert add(units[i], sub(shifts[i + 1], shifts[i])) == new[i]
        grow = shrink = 0
        work_sum = F(0)
        for layer, bar, weight, side in bars:
            change = n2(add(bar, shifts[layer])) - diameter**2
            work = dot(bar, shifts[layer])
            if shifts[layer] != ZERO:
                assert change * work > 0
            else:
                assert change == work == 0
            grow += int(change > 0)
            shrink += int(change < 0)
            work_sum += weight * work
            sign_checks += 1
        assert grow and shrink
        assert work_sum == sum((m - i) * dot(units[i], sub(new[i], units[i]))
                               for i in range(m)) < 0

    # A square unit lattice of side m+2 holds at least this many points and has
    # strictly smaller diameter. This works for every m>=2, unlike a line bound.
    assert len(points) <= (m + 3)**2
    assert 2 * (m + 2)**2 < diameter**2
    return {"m": m, "points": len(points), "source_pairs": pairs,
            "actual_contacts": len(contacts), "actual_diameters": 2 * m,
            "complete_rhombi": m * m, "reflection_subsets": len(subsets),
            "diameter_sign_checks": sign_checks,
            "transverse_KKT": "fails exactly", "vertex_KKT": "fails at fan isolates"}


def check_antitone_trees(m):
    edges = list(combinations(range(m + 1), 2))
    count = 0
    for family in combinations(edges, m):
        if any(a < c and b < d for (a, b), (c, d) in combinations(family, 2)):
            continue
        seen = {0}
        while True:
            expanded = seen | {b for a, b in family if a in seen} | {a for a, b in family if b in seen}
            if expanded == seen:
                break
            seen = expanded
        if len(seen) != m + 1:
            continue
        assert (0, m) in family
        assert max(a for a, b in family) < min(b for a, b in family)
        assert sum(b - a for a, b in family) == m * (m + 1) // 2
        count += 1
    assert count == 2**(m - 1)
    return {"m": m, "antitone_spanning_trees": count}


def main():
    # Do not materialize an exponential collection for the large packets.
    packets = [check_grid(m) for m in (2, 3, 4, 5, 6, 7, 8, 12, 16)]
    print(json.dumps({"arithmetic": "exact rational",
                      "empty_cut_scope": check_empty_cut_scope(),
                      "contact_grid_regressions": packets,
                      "antitone_trees": [check_antitone_trees(m) for m in range(1, 7)],
                      "scope": "no transverse/full-source KKT, no global optimality"}, indent=2))


if __name__ == "__main__":
    main()
