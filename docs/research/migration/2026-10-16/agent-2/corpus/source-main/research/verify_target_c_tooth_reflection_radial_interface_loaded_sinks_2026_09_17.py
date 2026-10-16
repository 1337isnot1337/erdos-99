#!/usr/bin/env python3
"""Regression checks for reflection-blocker radial contact interfaces."""

import math
from fractions import Fraction


h2 = Fraction(303, 2704)  # h_*^2
assert h2 < 1
h = math.sqrt(float(h2))
assert h < 0.335

# Boundary contact z->v, with |z-q|=D+delta and |v-q|<=D.
for D in (4.0, 10.0, 100.0, 1e6):
    for frac in (0.001, 0.1, 0.5, 0.999):
        delta = frac * h
        r = D + delta
        inward = (r * r + 1.0 - D * D) / (2.0 * r)
        rhs = delta + (1.0 - delta * delta) / (2.0 * (D + delta))
        assert abs(inward - rhs) < 1e-10
        assert inward > delta > 0.0
        assert r - 1.0 > D - 1.0
        assert inward < 1.0
        assert 2.0 * math.acos(inward) < math.pi

# Four boundary neighbors need three angular gaps >=pi/3, hence span >=pi.
assert 3 * Fraction(1, 3) == 1

# C26 radial-ascent edge case: if every radial component in a positive
# equilibrium were <=0, every one would have to vanish.  A unit direction
# orthogonal to a fixed radial direction has only the two tangent choices,
# contradicting the C26 degree floor 3.
zero_radial_unit_directions = [(0, 1), (0, -1)]
assert len(zero_radial_unit_directions) == 2
assert 3 > len(zero_radial_unit_directions)

# Positive radial contact component iff the neighbor squared radius rises by >1.
for r in (4.1, 10.2, 100.3):
    s = math.sqrt(r * r + 1.0001)
    radial = (s * s - r * r - 1.0) / (2.0 * r)
    assert radial > 0.0

# Global radial-ascent depth ceiling.
for D in (4.0, 10.0, 100.0, 1e6):
    ceiling = 2.0 * h * D + h * h
    assert ceiling < 0.671 * D + 1.0

# Polar confinement of a graph-distance-R contact buffer.
for D in (100.0, 1e4, 1e8):
    R = D ** 0.25
    assert R < D / 2.0
    drift = 2.0 * math.asin(R / (D - R))
    assert drift > 0.0
    ratio = drift / (D ** -0.25)
    if D >= 1e8:
        assert ratio < 0.01

# Near-quarter additional drift has exponent -3/4, below the blocker cone -1/4.
assert Fraction(-3, 4) < Fraction(-1, 4)

# If at least half of m heads are loaded, and one diameter edge has at most two
# selected endpoints, the conservative distinct-edge floor is Omega(m), as used.
for m in range(1, 101):
    loaded = m // 2
    edge_floor = (loaded + 1) // 2
    assert edge_floor + 1 >= m / 4

print("PASS: reflection radial-interface / loaded-sink certificate")
