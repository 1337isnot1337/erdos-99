#!/usr/bin/env python3
"""Exact bounded audits of marked-grid corrugation.

All example distances and rotations use integers/Fractions. These checks
certify the listed finite competitors, not the general analytic theorem,
global optimality, or a chart for general Target C-II sources.
"""

from fractions import Fraction as F
from itertools import combinations


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def squared(a, b):
    d = sub(a, b)
    return d[0] ** 2 + d[1] ** 2


def rotated(v, cosine, sine):
    return cosine*v[0] - sine*v[1], sine*v[0] + cosine*v[1]


def marked_axis(indices, marks, vector, cosine, sine):
    lo, hi = min(indices), max(indices)
    bars = {i: vector for i in range(lo, hi)}
    unmatched = set()
    for left, right in zip(marks, marks[1:]):
        paired_end = right - (right-left) % 2
        for i in range(left, paired_end, 2):
            bars[i] = rotated(vector, cosine, sine)
            bars[i+1] = rotated(vector, cosine, -sine)
            assert add(bars[i], bars[i+1]) == (
                2*cosine*vector[0], 2*cosine*vector[1])
        if paired_end != right:
            unmatched.add(right-1)
    anchor = marks[0]
    position = {anchor: (F(anchor)*vector[0], F(anchor)*vector[1])}
    for i in range(anchor, hi):
        position[i+1] = add(position[i], bars[i])
    for i in range(anchor-1, lo-1, -1):
        position[i] = sub(position[i+1], bars[i])
    assert all(squared(b, (0, 0)) == 1 for b in bars.values())
    return position, unmatched


def audit(name, indices, u, v, t, fixed=()):
    source = [(F(i)*u[0] + F(j)*v[0], F(i)*u[1] + F(j)*v[1])
              for i, j in indices]
    all_points = source + list(fixed)
    pairs = list(combinations(range(len(all_points)), 2))
    old_distance = {(a, b): squared(all_points[a], all_points[b])
                    for a, b in pairs}
    assert min(old_distance.values()) >= 1
    diameter2 = max(old_distance.values())
    edges = [pair for pair in pairs if old_distance[pair] == diameter2]
    loaded = sorted({k for edge in edges for k in edge})
    assert all(k < len(indices) for k in loaded)
    for (a, b), d2 in old_distance.items():
        if d2 == 1 and a < len(indices):
            assert b < len(indices)
            ia, ja = indices[a]
            ib, jb = indices[b]
            assert abs(ia-ib) + abs(ja-jb) == 1
    marks_i = sorted({indices[k][0] for k in loaded})
    marks_j = sorted({indices[k][1] for k in loaded})
    cosine, sine = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    xs, unmatched_i = marked_axis([i for i, _ in indices], marks_i,
                                  u, cosine, sine)
    ys, unmatched_j = marked_axis([j for _, j in indices], marks_j,
                                  v, cosine, sine)
    unmatched_count = len(unmatched_i) + len(unmatched_j)
    assert unmatched_count ** 2 < diameter2
    new_points = [add(xs[i], ys[j]) for i, j in indices] + list(fixed)
    new_distance = {(a, b): squared(new_points[a], new_points[b])
                    for a, b in pairs}
    for pair in pairs:
        if old_distance[pair] == 1:
            assert new_distance[pair] == 1
        else:
            assert new_distance[pair] > 1
        assert new_distance[pair] < diameter2
    for a, b in edges:
        ia, ja = indices[a]
        ib, jb = indices[b]
        ei = sum(1 if ib > ia else -1 for k in unmatched_i
                 if min(ia, ib) <= k < max(ia, ib))
        ej = sum(1 if jb > ja else -1 for k in unmatched_j
                 if min(ja, jb) <= k < max(ja, jb))
        residual = (ei*u[0] + ej*v[0], ei*u[1] + ej*v[1])
        original = sub(all_points[b], all_points[a])
        moved = sub(new_points[b], new_points[a])
        assert moved == (cosine*original[0] + (1-cosine)*residual[0],
                         cosine*original[1] + (1-cosine)*residual[1])
    print(f"PASS {name}: n={len(all_points)}, h={len(edges)}, "
          f"q={len(loaded)}, unmatched={unmatched_count}; "
          "all contacts preserved, all pairs below old diameter")


def main():
    square_u, square_v = (F(1), F(0)), (F(0), F(1))
    oblique_v = (F(5, 13), F(12, 13))
    for k in (2, 3, 7, 20):
        indices = [(i, j) for i in range(k+1) for j in range(k+1)]
        audit(f"square-{k}", indices, square_u, square_v, F(1, 1000))
    for k in (7, 20):
        indices = [(i, j) for i in range(k+1) for j in range(k+1)]
        audit(f"oblique-{k}", indices, square_u, oblique_v, F(1, 10000))
    # A rational basis barely above pi/3. No decimal comparison is used.
    half_tangent = F(577351, 1000000)
    assert 3*half_tangent**2 > 1
    near_sixty = ((1-half_tangent**2)/(1+half_tangent**2),
                  2*half_tangent/(1+half_tangent**2))
    assert 0 < near_sixty[0] < F(1, 2)
    indices = [(i, j) for i in range(10) for j in range(10)]
    audit("near-sixty", indices, square_u, near_sixty, F(1, 100000000))
    # Missing vertices and many marked coordinates; negative index order.
    disk = [(i, j) for i in range(-8, 9) for j in range(-8, 9)
            if i*i + j*j <= 64]
    audit("punctured-square-disk", [p for p in disk if p != (0, 0)],
          square_u, square_v, F(1, 1000000))
    audit("collinear-row", [(i, 0) for i in range(-50, 51)],
          square_u, square_v, F(1, 1000000))
    # A full chart with two fixed contact-isolated points not loaded.
    indices = [(i, j) for i in range(11) for j in range(11)
               if not (3 <= i <= 7 and 3 <= j <= 7)]
    audit("fixed-interior-isolates", indices, square_u, square_v,
          F(1, 1000000), fixed=((F(9, 2), F(5)), (F(11, 2), F(6))))
    print("Finite example audits only; the universal proof is in the report.")


if __name__ == "__main__":
    main()
