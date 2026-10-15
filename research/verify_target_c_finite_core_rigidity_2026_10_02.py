#!/usr/bin/env python3
"""Exact finite witnesses for finite core rigidity and its failed strengthenings.

Encoded: a unit square's full positive stress, PSD/affine kernel, active-row
redundancy and metric determination; a higher-dimensional contact-isometry;
a locally rigid two-point hinge; every pair in a seven-point hexagonal source.
Omitted: a generic C-II extraction, large global optimality, multiplier/eigenvalue
floors, and inactive-pair protection for an arbitrary proposed source move.
The report supplies the general proofs. Requires SymPy; no floating arithmetic.
"""

from fractions import Fraction
from itertools import combinations

import sympy as sp


def dist2(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def rigidity(points, edges):
    dimension = len(points[0])
    rows = []
    for i, j in edges:
        row = [sp.Integer(0)] * (dimension * len(points))
        for k in range(dimension):
            d = points[i][k] - points[j][k]
            row[dimension * i + k] = d
            row[dimension * j + k] = -d
        rows.append(row)
    return sp.Matrix(rows)


def laplacian(n, edges, weight):
    matrix = sp.zeros(n)
    for i, j in edges:
        matrix[i, i] += weight
        matrix[j, j] += weight
        matrix[i, j] -= weight
        matrix[j, i] -= weight
    return matrix


def connected_after_deletion(n, edges, removed):
    remaining = set(range(n)) - set(removed)
    if not remaining:
        return True
    seen = {next(iter(remaining))}
    todo = list(seen)
    while todo:
        i = todo.pop()
        for a, b in edges:
            j = b if a == i else a if b == i else None
            if j is not None and j in remaining and j not in seen:
                seen.add(j)
                todo.append(j)
    return seen == remaining


def check_square():
    points = [sp.Matrix(p) for p in [(0, 0), (1, 0), (1, 1), (0, 1)]]
    contacts = [(0, 1), (1, 2), (2, 3), (3, 0)]
    diameters = [(0, 2), (1, 3)]
    edges = contacts + diameters
    half = sp.Rational(1, 2)
    omega = laplacian(4, contacts, half) - laplacian(4, diameters, half)
    z = sp.Matrix([1, -1, 1, -1])
    assert omega == half * z * z.T  # Exact PSD factorization; eigenvalue 2.
    p = sp.Matrix([list(x) for x in points])
    affine = sp.ones(4, 1).row_join(p)
    assert affine.rank() == 3
    assert omega.rank() == 1 and omega * affine == sp.zeros(4, 3)
    assert sorted(omega.eigenvals()) == [0, 2]
    r = rigidity(points, edges)
    assert r.rank() == 5
    # Remove a row while retaining all vertex columns.
    for i in range(len(edges)):
        reduced = r.copy()
        reduced.row_del(i)
        assert reduced.rank() == 5
    for k in range(3):
        for removed in combinations(range(4), k):
            assert connected_after_deletion(4, edges, removed)

    # The square is a sharp genuine-source witness for the leaf incidence floor.
    h_degree = [sum(i in e for e in diameters) for i in range(4)]
    c_degree = [sum(i in e for e in contacts) for i in range(4)]
    leaves = sum(d == 1 for d in h_degree)
    deficiency = 4 - len(diameters)
    assert sum(c_degree) == 4 + leaves == 4 + 2 * deficiency == 8
    assert all(d == 2 for d in c_degree)

    # Active edge dyads span Sym_2: no nonzero symmetric affine metric defect.
    dyads = []
    for i, j in edges:
        dx, dy = points[i] - points[j]
        dyads.append([dx * dx, 2 * dx * dy, dy * dy])
    assert sp.Matrix(dyads).rank() == 3

    # A tetrahedron retains all old contacts, but shortens both old diameters.
    # It rejects replacing mixed bar equalities by diameter inequalities.
    # It is a Euclidean-3D witness, not a planar E99 competitor.
    tetrahedron = sp.Matrix([
        [0, 0, 0],
        [1, 0, 0],
        [half, sp.sqrt(3) / 2, 0],
        [half, sp.sqrt(3) / 6, sp.sqrt(sp.Rational(2, 3))],
    ])
    q = [tetrahedron.row(i).T for i in range(4)]
    assert all(sp.simplify(dist2(q[i], q[j])) == 1 for i, j in edges)
    energy = sp.simplify(sp.trace(tetrahedron.T * omega * tetrahedron))
    gain = sum(half * (2 - dist2(q[i], q[j])) for i, j in diameters)
    assert sp.simplify(energy - gain) == 0 and energy == 1
    # Exact positive-eigenspace inequality is equality for this square stress.
    projection = affine * (affine.T * affine).inv() * affine.T
    residual = (sp.eye(4) - projection) * tetrahedron
    residual2 = sp.simplify(sp.trace(residual.T * residual))
    assert sp.simplify(energy - 2 * residual2) == 0
    return {"rank": 5, "stress_rank": 1, "positive_eigenvalue": 2,
            "lifted_contact_gain": 1, "single_row_deletions": 6,
            "puncture_checks": 11, "leaf_incidence_equality": 8}


def check_hinge():
    points = [sp.Matrix(p) for p in [(0, 0), (2, 0), (1, 1), (1, -2)]]
    bars = [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3)]
    q = points[:3] + [sp.Matrix((1, 2))]
    rank = rigidity(points, bars).rank()
    assert rank == 5
    assert all(dist2(points[i], points[j]) == dist2(q[i], q[j]) for i, j in bars)
    assert dist2(points[2], points[3]) == 9 and dist2(q[2], q[3]) == 1
    assert not connected_after_deletion(4, bars, [0, 1])
    assert len(rigidity(points, bars).T.nullspace()) == 0
    return {"rank": rank, "old_nonedge_squared": 9, "new_nonedge_squared": 1,
            "self_stress_dimension": 0}


def check_interpolation():
    p = [sp.Matrix(x) for x in [(0, 0), (1, 0), (1, 1), (0, 1)]]
    f = sp.Rational
    q = [sp.Matrix(x) for x in [(0, 0), (1, 0), (f(8, 5), f(4, 5)),
                                (f(3, 5), f(4, 5))]]
    u = [b - a for a, b in zip(p, q)]
    c_edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    h_edges = [(0, 2), (1, 3)]
    assert all(dist2(q[i], q[j]) == 1 for i, j in c_edges)
    c = [dist2(u[i], u[j]) for i, j in c_edges]
    a = [dist2(u[i], u[j]) for i, j in h_edges]
    g = [dist2(q[i], q[j]) - 2 for i, j in h_edges]
    c_star = max(c)
    e_c, e_h = sum(c) / 2, sum(a) / 2
    barrier, gain = 2 * c_star - e_c, e_c - e_h
    assert c_star == f(2, 5) and e_c == e_h == f(2, 5)
    assert g == [f(6, 5), f(-6, 5)] and gain == 0
    assert barrier / (barrier + gain) == 1
    stress_fraction = sum(sp.Rational(1, 2) for c_e in c if c_e != 0) / 2
    assert stress_fraction == sp.Rational(1, 2)
    assert barrier / (barrier + gain) >= 1 - stress_fraction
    # Two-valued displacement: an endpoint blocker survives every 0<t<1.
    assert len({tuple(x) for x in u}) == 2
    assert all(a_h <= c_star for a_h in a)
    assert all(2 * c_star - a_h > 0 for a_h in a)
    assert g[0] > 0
    t = sp.Symbol("t", real=True)
    s = 1 - t * (1 - t) * c_star
    r = [x + t * y for x, y in zip(p, u)]
    for (i, j), c_e in zip(c_edges, c):
        assert sp.expand(dist2(r[i], r[j]) - (1 - t * (1 - t) * c_e)) == 0
    upper_tests = []
    for (i, j), a_h, g_h in zip(h_edges, a, g):
        test = g_h + (1 - t) * (2 * c_star - a_h)
        assert sp.expand(dist2(r[i], r[j]) - 2 * s - t * test) == 0
        upper_tests.append(test)
    assert sp.expand(sum(upper_tests) / 2 - (barrier - t * (barrier + gain))) == 0
    return {"contact_loss_max": "2/5", "weighted_gain": 0,
            "necessary_strict_threshold": "t > 1 (impossible)",
            "two_valued_endpoint_blocker_persists": True}


def check_heptagon_replacement():
    # Store (x,y/sqrt(3)), so all squared distances are rational.
    f = Fraction
    p = [(f(0), f(0)), (f(1), f(0)), (f(1, 2), f(1, 2)),
         (f(-1, 2), f(1, 2)), (f(-1), f(0)),
         (f(-1, 2), f(-1, 2)), (f(1, 2), f(-1, 2))]

    def triangular_dist2(a, b):
        return (a[0] - b[0]) ** 2 + 3 * (a[1] - b[1]) ** 2

    cycle = [tuple(sorted((i, (i + 1) % 7))) for i in range(7)]
    old_h = [tuple(sorted((i, (i + 3) % 7))) for i in range(7)]
    distances = {(i, j): triangular_dist2(p[i], p[j])
                 for i, j in combinations(range(7), 2)}
    assert len(distances) == 21 and min(distances.values()) == 1
    assert max(distances.values()) == 4
    assert all(distances[e] == 1 for e in cycle)
    old_h_lengths = [distances[e] for e in old_h]
    assert old_h_lengths == [1, 4, 4, 4, 1, 3, 3]
    assert sum(old_h_lengths) == 20
    new_contacts = [e for e, d in distances.items() if d == 1 and e not in cycle]
    assert len(new_contacts) == 5
    assert all(distances[e] == 1 for e in [(0, 1), (0, 2), (1, 2)])
    # pi<22/7 gives pi/14<11/49<1/4, hence sin(pi/14)<1/4 and D>2.
    assert f(11, 49) < f(1, 4)
    assert f(4) - f(20, 7) == f(8, 7)
    return {"pairs": len(distances), "old_contacts_preserved": 7,
            "new_contacts": len(new_contacts), "diameter_squared": 4,
            "old_diameter_squared_sum": 20,
            "weighted_gain_strict_lower_bound": "8/7"}


def main():
    print("square:", check_square())
    print("local-rigidity hinge regression:", check_hinge())
    print("restored affine-interpolation obstruction:", check_interpolation())
    print("planar finite contact-isometry regression:", check_heptagon_replacement())
    print("PASS: exact finite witnesses; general rigidity/cut theorems are analytic.")


if __name__ == "__main__":
    main()
