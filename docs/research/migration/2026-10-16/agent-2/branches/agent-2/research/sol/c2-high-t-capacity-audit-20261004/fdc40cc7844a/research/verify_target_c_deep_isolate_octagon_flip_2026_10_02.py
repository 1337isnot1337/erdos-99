#!/usr/bin/env python3
"""Exact octagon-flip regression; no global-optimality certificate.

Encoded: unit-separated rational source, connected old core, actual loaded hull,
contact-preserving binary move, upper feasibility, amplitude, local circumcircle
cover, and weak repairs. Omitted: canonical local trapping/full positive KKT,
global O-O cuts, quadratic population, and global optimality.
"""
from fractions import Fraction as F
from itertools import combinations


def d2(p, q):
    return sum((x - y) ** 2 for x, y in zip(p, q))


def edge(a, b):
    return tuple(sorted((a, b)))


def contacts(points):
    return {edge(i, j) for i, j in combinations(points, 2)
            if d2(points[i], points[j]) == 1}


def diameters(points):
    ds = {edge(i, j): d2(points[i], points[j])
          for i, j in combinations(points, 2)}
    maximum = max(ds.values())
    return maximum, {e for e, value in ds.items() if value == maximum}


def verify(t):
    a = (1 - t * t) / (1 + t * t)
    b = 2 * t / (1 + t * t)
    r, R = a + b, a + b + 1
    assert a * a + b * b == 1 and r > 1 and 0 < b < F(1, 20)
    points = {
        "MR": (r, F(0)), "CU": (a, a), "MU": (F(0), r),
        "CL": (-a, a), "ML": (-r, F(0)), "CD": (-a, -a),
        "MD": (F(0), -r), "CR": (a, -a),
        "QR": (R, F(0)), "QU": (F(0), R),
        "QL": (-R, F(0)), "QD": (F(0), -R), "Z": (F(0), F(0)),
    }
    order = ["MR", "CU", "MU", "CL", "ML", "CD", "MD", "CR"]
    old_c = {edge(order[i], order[(i + 1) % 8]) for i in range(8)}
    old_c |= {edge("M" + q, "Q" + q) for q in ["R", "U", "L", "D"]}
    assert contacts(points) == old_c and len(old_c) == 12
    assert all(d2(p, q) >= 1 for p, q in combinations(points.values(), 2))
    assert all(d2(points["Z"], points[q]) > 1 for q in points if q != "Z")
    maximum, old_h = diameters(points)
    expected_h = {edge("QR", "QL"), edge("QU", "QD")}
    assert maximum == 4 * R * R and old_h == expected_h
    assert all(abs(x) + abs(y) <= R for x, y in points.values())
    assert R * R / 2 > F(1, 4)  # loaded-hull boundary distance squared
    s, D = 2 * b, 2 * R
    assert s < 1 / (2 * D)

    moved = dict(points)
    for q in ["MR", "QR"]:
        x, y = moved[q]
        moved[q] = (x - 2 * b, y)
    core = {q: p for q, p in moved.items() if q != "Z"}
    assert contacts(core) == old_c
    assert all(d2(p, q) >= 1 for p, q in combinations(core.values(), 2))
    new_max, new_h = diameters(moved)
    assert new_max == maximum and new_h == {edge("QU", "QD")}
    assert all(d2(moved[i], moved[j]) <= d2(points[i], points[j])
               for i, j in combinations(points, 2))
    assert d2(moved["Z"], moved["MR"]) < 1

    c = a - b
    assert c * r == 1 - 2 * b * b
    assert r * r / 2 > F(1, 4)
    assert (c * r) ** 2 / 2 > F(1, 4)
    for sign in [-1, 1]:
        z = (-b, sign * b)
        axial = ["ML", "MR", "MU" if sign == 1 else "MD"]
        assert all(d2(z, moved[q]) == 1 for q in axial)
        assert 0 < b < a  # circumcenter is inside its triangle
        fixed = dict(core)
        fixed["Z"] = z
        assert all(d2(p, q) >= 1 for p, q in combinations(fixed.values(), 2))
        new_contacts = contacts(fixed)
        assert new_contacts == old_c | {edge("Z", q) for q in axial}
        assert len(new_contacts) == 15
        assert diameters(fixed) == (maximum, {edge("QU", "QD")})
        assert not any(edge(i, j) in new_contacts and edge(i, k) in new_contacts
                       and edge(j, k) in new_contacts
                       for i, j, k in combinations(fixed, 3))

    degree = {q: sum(q in e for e in old_c) for q in core}
    loaded = {q for e in old_h for q in e}
    for q in ["CU", "CL", "CD", "CR"]:
        assert q not in loaded and degree[q] == 2
        other = [next(v for v in e if v != q) for e in old_c if q in e]
        u = tuple(points[other[0]][i] - points[q][i] for i in range(2))
        v = tuple(points[other[1]][i] - points[q][i] for i in range(2))
        assert u[0] * v[1] - u[1] * v[0] != 0


if __name__ == "__main__":
    parameters = [F(1, n) for n in [40, 50, 100, 200, 1000, 10_000, 1_000_000]]
    for t in parameters:
        verify(t)
    print(f"PASS: {len(parameters)} exact 13-point sources; contact/diameter, "
          "amplitude, loaded-hull, local-cover, and three-contact repairs.")
    print("Scope: regression only; no canonical local trapping, global O-O "
          "cutset, or global-optimality certificate.")
