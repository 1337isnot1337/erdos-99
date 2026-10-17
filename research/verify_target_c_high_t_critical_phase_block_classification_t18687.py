#!/usr/bin/env python3
"""Regression checks for the high-t critical phase-block classification."""

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


alpha = [0.0, 0.0, 0.0, 0.05, 0.05, 0.11, 0.11]
us = [u(a) for a in alpha]
masses = [1.1, 0.8, 1.4, 0.7, 1.3, 0.9, 1.2]
resultants = [smul(m, v) for m, v in zip(masses, us)]


def kernel_residual(coeffs):
    total = (0.0, 0.0)
    for c, v in zip(coeffs, us):
        total = add(total, smul(c, v))
    return hypot(*total)


def interface_vector(coeffs):
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


# PB.6 forward/converse model: zero coefficient sum on each constant-phase
# block gives both the full-support kernel and zero interface aggregates.
critical = [1.0, -2.0, 1.0, 3.0, -3.0, 4.0, -4.0]
assert abs(sum(critical[0:3])) < 1e-15
assert abs(sum(critical[3:5])) < 1e-15
assert abs(sum(critical[5:7])) < 1e-15
assert kernel_residual(critical) < 1e-14
critical_interface = interface_vector(critical)
assert max(abs(x) for x in critical_interface) < 2e-15

# A noncritical full kernel obtained from the determinant relation among the
# three distinct block directions has nonzero block sums and a nonzero
# interface vector, while the global KKT interface balance still sums to zero.
s0 = sin(0.11 - 0.05)
s1 = -sin(0.11 - 0.0)
s2 = sin(0.05 - 0.0)
noncritical = [s0, 0.0, 0.0, s1, 0.0, s2, 0.0]
assert kernel_residual(noncritical) < 1e-14
noncritical_interface = interface_vector(noncritical)
assert max(abs(x) for x in noncritical_interface) > 1e-5
assert abs(sum(noncritical_interface)) < 2e-14

# PB.22-PB.24: a nonzero zero-sum coefficient vector inside one equal-phase
# block has strictly positive quadratic radial charge Q_B.
for values in (
    (1.0, -2.0, 1.0),
    (3.0, -3.0),
    (4.0, -4.0),
):
    assert abs(sum(values)) < 1e-15
    q_block = sum(x * x for x in values)
    assert q_block > 0

print("PASS: high-t critical phase-block classification algebra")
print("critical max interface residual =", max(abs(x) for x in critical_interface))
print("noncritical interface vector =", noncritical_interface)
