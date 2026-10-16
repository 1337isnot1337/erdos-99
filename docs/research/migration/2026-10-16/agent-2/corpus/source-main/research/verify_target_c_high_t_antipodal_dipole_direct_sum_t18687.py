#!/usr/bin/env python3
"""Regression checks for the high-t antipodal dipole direct-sum theorem."""

from math import cos, sin

alpha = [0.0, 0.0, 0.0, 0.07, 0.07, 0.12]
E = [i for i in range(len(alpha) - 1) if alpha[i] == alpha[i + 1]]
assert E == [0, 1, 3]

# Critical coefficients: each maximal equal-phase block has zero sum.
c = [2.0, -3.0, 1.0, 4.0, -4.0, 0.0]

# Canonical dipole coefficients are proper prefix sums within each phase block.
recon = [0.0] * len(c)
blocks = [(0, 2), (3, 4), (5, 5)]
coords = {}
for p, q in blocks:
    assert abs(sum(c[p : q + 1])) < 1e-15
    s = 0.0
    for i in range(p, q):
        s += c[i]
        coords[i] = s
        recon[i] += s
        recon[i + 1] -= s
assert recon == c
assert set(coords) == set(E)

# A dipole e_i-e_{i+1} is seen by an interval exactly when the interval
# contains one but not both of the two consecutive cuts.
for i in E:
    d = [0.0] * len(c)
    d[i] = 1.0
    d[i + 1] = -1.0
    for a in range(len(c)):
        for b in range(a, len(c)):
            value = sum(d[a : b + 1])
            expected_nonzero = ((a <= i <= b) != (a <= i + 1 <= b))
            assert (abs(value) > 0.5) == expected_nonzero
            if expected_nonzero:
                assert b == i or a == i + 1

# Synthetic antipodal sign pair: a common nonzero transverse switching
# velocity gives opposite first derivative signs.
u = (cos(0.2), sin(0.2))
J = (-u[1], u[0])


def dot(x, y):
    return x[0] * y[0] + x[1] * y[1]


d_plus = (cos(0.5), sin(0.5))
d_minus = (cos(-0.1), sin(-0.1))
assert dot(d_plus, J) > 0
assert dot(d_minus, J) < 0
speed = -1.7
ell_plus = 2 * speed * dot(d_plus, J)
ell_minus = 2 * speed * dot(d_minus, J)
assert ell_plus * ell_minus < 0

print("PASS: antipodal dipole direct-sum algebra and interval localization")
print("equal-phase interfaces =", E)
print("dipole coordinates =", coords)
print("synthetic sign product =", ell_plus * ell_minus)
