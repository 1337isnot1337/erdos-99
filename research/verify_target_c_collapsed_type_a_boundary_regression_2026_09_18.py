#!/usr/bin/env python3
"""Exact boundary regression for the type-A common-host crossing cycle.

The six internal train directions are sixth roots of unity.  The certificate
checks the collapsed six-face equilibrium exactly in Q(sqrt(3)), verifies that
all six type-A forced crossing pairs have projective gap exactly pi/3, and
records an incident-ray coincidence.  Thus the boundary satisfies equilibrium
but is not a strict force-pentagon realization.

This is a regression/sharpness certificate, not an exclusion theorem and not a
global source realization.
"""

from sympy import Rational, simplify, sqrt

EDGES = ((0, 1), (0, 2), (0, 4), (0, 5), (1, 2), (1, 3),
         (1, 5), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5))
EXPONENTS = (2, 4, 2, 5, 1, 3, 3, 2, 4, 1, 3, 1)
TYPE_A = ((1, 5), (1, 6), (2, 6), (2, 10), (5, 8), (8, 10))
ROOTS = (
    (Rational(1), 0),
    (Rational(1, 2), sqrt(3) / 2),
    (-Rational(1, 2), sqrt(3) / 2),
    (-Rational(1), 0),
    (-Rational(1, 2), -sqrt(3) / 2),
    (Rational(1, 2), -sqrt(3) / 2),
)


def add(a, b):
    return simplify(a[0] + b[0]), simplify(a[1] + b[1])


def neg(a):
    return -a[0], -a[1]


def dot(a, b):
    return simplify(a[0] * b[0] + a[1] * b[1])


vectors = [ROOTS[k % 6] for k in EXPONENTS]
assert all(dot(v, v) == 1 for v in vectors)

for face, sign in enumerate((1, 1, 1, -1, -1, -1)):
    total = (Rational(sign), Rational(0))
    for edge, (u, v) in enumerate(EDGES):
        if face == u:
            total = add(total, vectors[edge])
        elif face == v:
            total = add(total, neg(vectors[edge]))
    assert total == (0, 0), (face, total)

for i, j in TYPE_A:
    assert abs(dot(vectors[i], vectors[j])) == Rational(1, 2)

incident_rays = {}
for edge, (u, v) in enumerate(EDGES):
    incident_rays.setdefault(u, []).append((edge, EXPONENTS[edge] % 6))
    incident_rays.setdefault(v, []).append((edge, (EXPONENTS[edge] + 3) % 6))
duplicates = []
for face, rays in incident_rays.items():
    for left in range(len(rays)):
        for right in range(left + 1, len(rays)):
            if rays[left][1] == rays[right][1]:
                duplicates.append((face, rays[left], rays[right]))
assert (0, (0, 2), (2, 2)) in duplicates

print("faces_checked", 6)
print("type_a_pairs_checked", len(TYPE_A))
print("projective_threshold", "exact equality pi/3")
print("incident_ray_duplicates", len(duplicates))
print("PASS: exact type-A equilibrium boundary regression")
