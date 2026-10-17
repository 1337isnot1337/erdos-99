#!/usr/bin/env python3
"""Exact regressions for open-guard saturation; not optimality certificates.

Run: python3 research/verify_target_c_open_guard_packing_saturation.py
All pair tests use rational squared distances. Axial coordinates use the
triangular-lattice metric x*x+x*y+y*y; Cartesian tests use x*x+y*y.
The general theorem is proved in the companion report, not by these examples.
"""

from fractions import Fraction as Q
from itertools import combinations


def dist2(p, q, axial=False):
    x, y = p[0] - q[0], p[1] - q[1]
    return x*x + y*y + (x*y if axial else 0)


def pairs(points, axial=False):
    return [dist2(p, q, axial) for p, q in combinations(points, 2)]


def contacts(points, axial=False):
    return sum(d == 1 for d in pairs(points, axial))


def triangle_free(points, axial=False):
    near = {p: {q for q in points if q != p and dist2(p, q, axial) == 1}
            for p in points}
    return not any(near[p] & near[q] for p in points for q in near[p])


def check_exchange(old, removed, inserted, D2, axial=False):
    retained = old - removed
    assert retained and not retained & inserted
    assert min(pairs(old, axial)) >= 1
    assert max(pairs(old, axial)) == D2
    assert triangle_free(old, axial)
    assert min(pairs(inserted, axial)) > 1
    assert max(pairs(inserted, axial)) < D2
    assert all(1 < dist2(b, r, axial) < D2 for b in inserted for r in retained)
    new = retained | inserted
    assert len(new) == len(old)
    assert triangle_free(new, axial)
    assert min(pairs(new, axial)) >= 1
    # Contact-count improvement is real even without strict diameter descent.
    assert max(pairs(new, axial)) == D2
    assert contacts(new, axial) < contacts(old, axial)
    return len(old), contacts(old, axial), contacts(new, axial)


def triangle_strictification():
    m = 12
    rim = {(Q(i), Q(j)) for i in range(-m, m+1) for j in range(-m, m+1)
           if max(abs(i), abs(j), abs(i+j)) == m}
    isolates = {(Q(0), Q(0)), (Q(2), Q(0))}
    v = (Q(m), Q(0))
    old = rim | isolates
    assert all(dist2(z, a, True) > 1 for z in isolates for a in old if a != z)
    initial = {(Q(0), Q(0)), (Q(1), Q(0)), (Q(0), Q(1))}
    assert pairs(initial, True) == [Q(1)] * 3
    scale = Q(101, 100)
    inserted = {(scale*x, scale*y) for x, y in initial}
    assert pairs(inserted, True) == [scale*scale] * 3
    return check_exchange(old, isolates | {v}, inserted, Q(4*m*m), True)


def exterior_isolate():
    m = 20
    rim = {(Q(i), Q(j)) for i in range(m+1) for j in range(m+1)
           if i in (0, m) or j in (0, m)}
    z = (Q(m+2), Q(m, 2))
    old = rim | {z}
    # z is an extreme source point, not in the interior of the source hull.
    assert z[0] > max(p[0] for p in rim)
    assert all(1 < dist2(z, r) < 2*m*m for r in rim)
    inserted = {(Q(9), Q(10)), (Q(11), Q(10))}
    # Delete a noncorner contact vertex so both old diagonals certainly remain.
    return check_exchange(old, {z, (Q(1), Q(0))}, inserted, Q(2*m*m))


def negative_controls():
    # Cross-diameter lens membership does NOT bound internal diameter.
    R = {(Q(0), Q(0))}
    B = {(Q(-2), Q(0)), (Q(2), Q(0))}
    assert all(1 < dist2(b, r) < 9 for b in B for r in R)
    assert pairs(B) == [Q(16)]
    # Closed length-one segment has ordinary capacity two, strict capacity one.
    endpoints = {(Q(0), Q(0)), (Q(1), Q(0))}
    assert pairs(endpoints) == [Q(1)]
    for denominator in range(2, 20):
        scale = Q(denominator+1, denominator)
        assert scale > 1  # expanded right endpoint leaves the closed segment


if __name__ == "__main__":
    print("triangle insertion, n/contact counts:", triangle_strictification())
    print("extreme-isolate exchange, n/contact counts:", exterior_isolate())
    negative_controls()
    print("PASS: exact open-guard regressions; no global-optimality claim")
