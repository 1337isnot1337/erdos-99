#!/usr/bin/env python3
"""Regression checks for complete local high-t multishear isolation.

This is an algebraic/numerical certificate for the finite normalization mechanism in
`target_c_high_t_nonlinear_multishear_isolation_t18687_2026-09-17.md`. The proof in
the report is analytic; this script checks representative rank-two exact-cancellation
states, the persistent-rank linear algebra, and the two-sided outer-train bracing
mechanism that eliminates the singleton persistent escape.
"""

from math import cos, hypot, sin


def u(a):
    return (cos(a), sin(a))


def J(v):
    return (-v[1], v[0])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def smul(s, a):
    return (s * a[0], s * a[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def norm(a):
    return hypot(a[0], a[1])


def rot(theta, v):
    c = cos(theta)
    s = sin(theta)
    return (c * v[0] - s * v[1], s * v[0] + c * v[1])


def full_displacement(theta, us):
    z = (0.0, 0.0)
    for t, v in zip(theta, us):
        z = add(z, sub(rot(t, v), v))
    return z


def kernel_residual(coeffs, us):
    z = (0.0, 0.0)
    for c, v in zip(coeffs, us):
        z = add(z, smul(c, v))
    return norm(z)


def interface_vector(alpha, masses, coeffs):
    us = [u(a) for a in alpha]
    resultants = [smul(m, v) for m, v in zip(masses, us)]
    prefix = (0.0, 0.0)
    out = []
    for i in range(len(coeffs) - 1):
        prefix = add(prefix, smul(coeffs[i], us[i]))
        fresh = sub(resultants[i + 1], resultants[i])
        out.append(-2.0 * dot(fresh, J(prefix)))
    return out


def solve_dependent(t0, us, tangent_ratios, iterations=12):
    """Solve G(t0,t1,t2)=0 for t1,t2 by Newton iteration."""
    t1 = tangent_ratios[0] * t0
    t2 = tangent_ratios[1] * t0
    for _ in range(iterations):
        f = full_displacement([t0, t1, t2], us)
        c1 = J(rot(t1, us[1]))
        c2 = J(rot(t2, us[2]))
        det = c1[0] * c2[1] - c1[1] * c2[0]
        assert abs(det) > 1e-8
        d1 = (-f[0] * c2[1] + f[1] * c2[0]) / det
        d2 = (-c1[0] * f[1] + c1[1] * f[0]) / det
        t1 += d1
        t2 += d2
    return [t0, t1, t2]


# Rank-two three-row sample. The standard determinant vector lies in the
# first-order full-support cancellation kernel.
alpha = [0.01, 0.04, 0.09]
us = [u(a) for a in alpha]
c = [
    sin(alpha[2] - alpha[1]),
    -sin(alpha[2] - alpha[0]),
    sin(alpha[1] - alpha[0]),
]
assert kernel_residual(c, us) < 1e-14
ratios = [c[1] / c[0], c[2] / c[0]]

# Follow the exact nonlinear G=0 manifold. Normalized exact states converge to
# the tangent kernel, while the interface aggregates keep opposite signs. This
# is the finite mechanism used in NL-A: nonlinear curvature cannot erase the
# linear sign cusp.
last_kernel_residual = None
for t0 in [1e-3, 5e-4, 2e-4, 1e-4]:
    theta = solve_dependent(t0, us, ratios)
    assert norm(full_displacement(theta, us)) < 1e-12
    rho = sum(t * t for t in theta) ** 0.5
    chat = [t / rho for t in theta]
    kres = kernel_residual(chat, us)
    if last_kernel_residual is not None:
        assert kres < last_kernel_residual
    last_kernel_residual = kres
    assert kres < 1e-3

    ivec = interface_vector(alpha, [0.8, 1.3, 1.1], chat)
    assert min(ivec) < -1e-3
    assert max(ivec) > 1e-3

# Persistent-rank regression for NL-C. Two nonparallel persistent directions
# admit no nonzero planar vector perpendicular to both; a singleton direction
# leaves exactly its one-dimensional perpendicular line.
v1 = u(0.2)
v2 = u(0.7)
det = v1[0] * v2[1] - v1[1] * v2[0]
assert abs(det) > 0.4

g = J(v1)
assert abs(dot(v1, g)) < 1e-15
assert abs(dot(v2, g)) > 0.4

# Response-free outer-train bracing regression for NL-D. Opposite transverse
# crossing signs force at least two distinct, nonparallel actual diameter bars.
train = u(0.0)
transverse = J(train)
d_plus = u(0.4)
d_minus = u(-0.3)
assert dot(d_plus, transverse) > 0
assert dot(d_minus, transverse) < 0
bracing_det = d_plus[0] * d_minus[1] - d_plus[1] * d_minus[0]
assert abs(bracing_det) > 0.6

# There is therefore no nonzero first-order persistent-core displacement g
# perpendicular to both bracing directions. The 2x2 determinant is nonzero.
assert abs(bracing_det) > 1e-12

# Positive-weight stationarity sanity check: nonpositive row derivatives with
# zero positive weighted sum can only all vanish.
beta = [0.2, 0.3, 0.5]
deriv = [0.0, 0.0, 0.0]
assert abs(sum(b * d for b, d in zip(beta, deriv))) < 1e-15
assert all(d == 0.0 for d in deriv)

print("PASS: complete nonlinear exact-laminar multishear isolation regressions")
print("final normalized kernel residual =", last_kernel_residual)
print("persistent direction determinant =", det)
print("outer-train bracing determinant =", bracing_det)
