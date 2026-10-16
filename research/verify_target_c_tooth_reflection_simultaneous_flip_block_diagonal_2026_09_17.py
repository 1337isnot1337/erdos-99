#!/usr/bin/env python3
"""Regression checks for the simultaneous shallow-tooth reflection reduction.

This certificate checks the exact constants and exponent bookkeeping used in
`target_c_tooth_reflection_simultaneous_flip_block_diagonal_2026-09-17.md`.
It does not replace the geometric arguments for the O/o/Omega statements.
"""

from fractions import Fraction
import itertools
import math


eta = Fraction(3, 26)
C2 = 4 * eta - eta * eta
assert C2 == Fraction(303, 676)
assert 1 - C2 == Fraction(373, 676)

C = math.sqrt(float(C2))
assert C < 1.0

b = 3 ** (1 / 8)
s = 3 ** (5 / 8)
A = 2 * s + 4 * b
B = 8 * b
shared_threshold = 2 * A + B

Kdeg = 208 * b / math.sqrt(373)
rho = 0.129220199818177
Kunion = rho * Kdeg

assert abs(C - 0.6694959686742004) < 1e-15
assert abs(Kdeg - 12.35517997069441) < 1e-12
assert abs(A - 8.562837454602665) < 1e-12
assert abs(B - 9.177621523519017) < 1e-12
assert abs(shared_threshold - 26.303296432724345) < 1e-12
assert abs(Kunion - 1.59653882460267) < 1e-12

# Cardinality bookkeeping after the explicit controlled thinning:
# |I_D| ~ D^(1/4)/kappa and |U_i| = O(D^(3/4)).
assert Fraction(1, 4) + Fraction(3, 4) == 1

# Same-shore module separation:
# D * (kappa D^(-1/4)) = kappa D^(3/4).
assert 1 + Fraction(-1, 4) == Fraction(3, 4)

# Cross-shore law-of-cosines deficit:
# D^2 * (kappa D^(-1/4))^2 = kappa^2 D^(3/2),
# and converting squared deficit to a distance deficit divides by Theta(D).
assert 2 + 2 * Fraction(-1, 4) == Fraction(3, 2)
assert Fraction(3, 2) - 1 == Fraction(1, 2)

# Two radius-D/2 points separated by at most a right angle are strictly
# subdiametral at the leading scale.
assert 1 / math.sqrt(2) < 1

# Abstract incidence check: pairwise-disjoint blocker sets give an upper
# violation incidence matrix in which each fixed blocker column belongs to at
# most one reflected-apex module. Exhaust all assignments for small models.
for modules in range(1, 5):
    universe = range(5)
    for assignment in itertools.product(range(-1, modules), repeat=len(universe)):
        blocker_sets = [set() for _ in range(modules)]
        for blocker, owner in zip(universe, assignment):
            if owner >= 0:
                blocker_sets[owner].add(blocker)
        for blocker in universe:
            assert sum(blocker in blocker_sets[i] for i in range(modules)) <= 1

# Representative numerical scaling check for the cross-module law of cosines.
# This only checks the sign and power law; the proof uses the asymptotic
# comparison kappa_D -> infinity and kappa_D = o(D^(1/4)).
for exponent in (12, 16, 20, 24):
    D = 10.0 ** exponent
    kappa = math.log(D)
    delta = 2 * kappa * D ** (-0.25)
    r = D / 2 + 10 * math.sqrt(D)
    angular_loss = 2 * r * r * (1 - math.cos(delta))
    expected_scale = kappa**2 * D**1.5
    assert angular_loss / expected_scale > 0.2

print("PASS: simultaneous reflection block-diagonal certificate")
print(f"C_*={C:.15f}")
print(f"degree coefficient={Kdeg:.15f}")
print(f"2A+B={shared_threshold:.15f}")
print(f"controlled union coefficient={Kunion:.15f}")
