#!/usr/bin/env python3
"""Algebraic regression checks for complete high-t multishear cusp localization."""

from math import cos, hypot, sin


def u(a):
    return (cos(a), sin(a))


def J(v):
    return (-v[1], v[0])


def dot(x, y):
    return x[0] * y[0] + x[1] * y[1]


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def smul(c, v):
    return (c * v[0], c * v[1])


def interface_vector(alpha, masses, coeffs):
    us = [u(a) for a in alpha]
    resultants = [smul(m, v) for m, v in zip(masses, us)]
    prefix = (0.0, 0.0)
    out = []
    for i in range(len(coeffs) - 1):
        prefix = add(prefix, smul(coeffs[i], us[i]))
        fresh = (
            resultants[i + 1][0] - resultants[i][0],
            resultants[i + 1][1] - resultants[i][1],
        )
        out.append(-2.0 * dot(fresh, J(prefix)))
    return out


def kernel_residual(alpha, coeffs):
    total = (0.0, 0.0)
    for a, c in zip(alpha, coeffs):
        total = add(total, smul(c, u(a)))
    return hypot(*total)


# MC-A: a three-direction determinant kernel has nonzero interface vector,
# with zero total and hence both signs.
a0, a1, a2 = 0.01, 0.04, 0.09
alpha = [a0, a1, a2]
coeffs = [sin(a2 - a1), -sin(a2 - a0), sin(a1 - a0)]
assert kernel_residual(alpha, coeffs) < 1e-14
Dvec = interface_vector(alpha, [0.8, 1.3, 1.1], coeffs)
assert abs(sum(Dvec)) < 1e-14
assert min(Dvec) < -1e-8 < 0 < 1e-8 < max(Dvec)

# MC-B: phase-block critical vector. Each maximal equal-phase block sums to
# zero, so all interface aggregates vanish, but a nonzero proper prefix exists
# strictly inside an equal-phase block.
alpha = [0.02, 0.02, 0.02, 0.07, 0.07]
coeffs = [1.0, -2.0, 1.0, 3.0, -3.0]
assert kernel_residual(alpha, coeffs) < 1e-14
Dvec = interface_vector(alpha, [0.7, 1.0, 1.4, 0.9, 1.2], coeffs)
assert max(abs(x) for x in Dvec) < 2e-15
prefix_scalars = [coeffs[0], coeffs[0] + coeffs[1]]
assert any(abs(x) > 1e-12 for x in prefix_scalars)

# All-one-block regression: a nonzero zero-sum tangent always has a nonzero
# proper partial sum, hence exposes an internal antipodal interface.
coeffs = [2.0, -1.0, -3.0, 2.0]
assert abs(sum(coeffs)) < 1e-15
partials = []
s = 0.0
for c in coeffs[:-1]:
    s += c
    partials.append(s)
assert any(abs(x) > 1e-12 for x in partials)

# Synthetic antipodal sign check: if two inward diameter directions have
# opposite transverse components, any nonzero common transverse switching
# velocity gives opposite squared-length derivatives.
v = u(0.13)
n = J(v)
d_plus = u(0.13 + 0.4)
d_minus = u(0.13 - 0.3)
assert dot(d_plus, n) > 0
assert dot(d_minus, n) < 0
speed = -2.7
ell_plus = 2.0 * dot(d_plus, smul(speed, n))
ell_minus = 2.0 * dot(d_minus, smul(speed, n))
assert ell_plus * ell_minus < 0

print("PASS: complete high-t multishear cusp localization algebra")
print("MC-A interface vector =", Dvec if False else interface_vector([a0, a1, a2], [0.8, 1.3, 1.1], [sin(a2-a1), -sin(a2-a0), sin(a1-a0)]))
print("MC-B zero aggregate residual =", max(abs(x) for x in Dvec))
print("antipodal synthetic derivative product =", ell_plus * ell_minus)
