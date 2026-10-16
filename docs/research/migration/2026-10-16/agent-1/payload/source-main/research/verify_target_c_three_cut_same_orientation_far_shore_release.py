#!/usr/bin/env python3
from math import cos, sin

# Layer displacements, as coefficient pairs of (Delta_alpha, Delta_beta).
layers = [(0, 0), (1, 0), (1, 1), (0, 0)]
expected = {
    (0, 0): (0, 0),
    (0, 1): (1, 0),
    (1, 2): (0, 1),
    (2, 3): (-1, -1),
    (0, 2): (1, 1),
    (1, 3): (-1, 0),
    (0, 3): (0, 0),
}
for pair, want in expected.items():
    i, j = pair
    got = (layers[j][0] - layers[i][0], layers[j][1] - layers[i][1])
    assert got == want, (pair, got, want)

# Regression for the exact third-contact identity and its lower bound.
for ia in range(-40, 41):
    for ib in range(-40, 41):
        a = ia / 200.0
        b = ib / 200.0
        if a == 0.0 and b == 0.0:
            continue
        qx = 3.0 - cos(a) - cos(b)
        qy = -sin(a) - sin(b)
        excess = qx * qx + qy * qy - 1.0
        formula = 10.0 - 6.0 * cos(a) - 6.0 * cos(b) + 2.0 * cos(a - b)
        lower = 4.0 * (sin(a / 2.0) ** 2 + sin(b / 2.0) ** 2)
        assert abs(excess - formula) < 1e-12
        assert formula + 1e-13 >= lower
        assert excess > 0.0

print('PASS: far-shore layer table and strict third-contact opening')
