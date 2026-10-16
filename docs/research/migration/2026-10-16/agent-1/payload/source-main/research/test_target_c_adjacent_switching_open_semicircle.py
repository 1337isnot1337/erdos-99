#!/usr/bin/env python3
"""Finite regression for the support-normal open-semicircle lemma.

This is not part of the proof. It samples strictly convex point sets on ellipses,
computes actual diameter pairs, and checks every cyclic vertex interval: diameter
edges crossing the interval cut, oriented from outside to inside, have directions in
an open semicircle.
"""
import math
import random


def angle(v):
    return math.atan2(v[1], v[0]) % (2 * math.pi)


def fits_open_semicircle(angles, eps=1e-9):
    if len(angles) <= 1:
        return True
    a = sorted(angles)
    aa = a + [x + 2 * math.pi for x in a]
    n = len(a)
    return any(aa[i + n - 1] - aa[i] < math.pi - eps for i in range(n))


def diameter_edges(points, tol=1e-9):
    rows = []
    D = 0.0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = math.dist(points[i], points[j])
            rows.append((i, j, d))
            D = max(D, d)
    return D, [(i, j) for i, j, d in rows if abs(d - D) < tol]


def main():
    rng = random.Random(20260915)
    checked = 0
    for n in range(5, 16):
        for _ in range(500):
            theta = sorted(rng.random() * 2 * math.pi for _ in range(n))
            points = [(math.cos(t), 0.73 * math.sin(t)) for t in theta]
            _, edges = diameter_edges(points)
            for start in range(n):
                for length in range(1, n):
                    inside = {(start + k) % n for k in range(length)}
                    directions = []
                    for i, j in edges:
                        if (i in inside) == (j in inside):
                            continue
                        m, x = (i, j) if i in inside else (j, i)
                        directions.append(
                            angle((points[m][0] - points[x][0],
                                   points[m][1] - points[x][1]))
                        )
                    if directions:
                        checked += 1
                        assert fits_open_semicircle(directions, 1e-8)
    print(f"adjacent switching open-semicircle regression: PASS ({checked} cuts)")


if __name__ == "__main__":
    main()
