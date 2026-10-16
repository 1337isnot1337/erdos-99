#!/usr/bin/env python3
"""Regression checks for the high-t multirow cusp-injectivity theorem."""

from math import cos, hypot, sin
from random import Random


def u(a):
    return (cos(a), sin(a))


def J(v):
    return (-v[1], v[0])


def dot(x, y):
    return x[0] * y[0] + x[1] * y[1]


def det(x, y):
    return x[0] * y[1] - x[1] * y[0]


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def smul(c, v):
    return (c * v[0], c * v[1])


def solve_last_two(us, free):
    """Complete arbitrary first coefficients to sum_j c_j u_j = 0."""
    total = (0.0, 0.0)
    for c, v in zip(free, us[:-2]):
        total = add(total, smul(c, v))
    rhs = (-total[0], -total[1])
    a, b = us[-2], us[-1]
    den = det(a, b)
    assert abs(den) > 1e-4
    ca = det(rhs, b) / den
    cb = det(a, rhs) / den
    return free + [ca, cb]


rng = Random(20260917)
max_kernel_residual = 0.0
max_total_balance_residual = 0.0
max_first_interface_residual = 0.0

for r in range(2, 9):
    n = r + 1
    for _ in range(1000):
        # A narrow coherent real phase block with every adjacent gap nonzero.
        a0 = rng.uniform(-0.2, 0.1)
        gaps = [rng.uniform(0.02, 0.07) for _ in range(r)]
        alpha = [a0]
        for gap in gaps:
            alpha.append(alpha[-1] + gap)

        us = [u(a) for a in alpha]
        masses = [rng.uniform(0.1, 2.0) for _ in range(n)]
        resultants = [smul(m, v) for m, v in zip(masses, us)]

        free = [rng.uniform(-1.0, 1.0) for _ in range(n - 2)]
        coeffs = solve_last_two(us, free)

        kernel = (0.0, 0.0)
        for c, v in zip(coeffs, us):
            kernel = add(kernel, smul(c, v))
        max_kernel_residual = max(max_kernel_residual, hypot(*kernel))

        prefix = (0.0, 0.0)
        interface = []
        for i in range(r):
            prefix = add(prefix, smul(coeffs[i], us[i]))
            fresh = (
                resultants[i + 1][0] - resultants[i][0],
                resultants[i + 1][1] - resultants[i][1],
            )
            interface.append(-2.0 * dot(fresh, J(prefix)))

        max_total_balance_residual = max(
            max_total_balance_residual,
            abs(sum(interface)),
        )

        # MI.30: the first nonzero coefficient immediately exposes a cusp.
        k = next(i for i, c in enumerate(coeffs) if abs(c) > 1e-9)
        assert k < r
        target = (
            -2.0
            * coeffs[k]
            * masses[k + 1]
            * sin(alpha[k + 1] - alpha[k])
        )
        max_first_interface_residual = max(
            max_first_interface_residual,
            abs(interface[k] - target),
        )

        # The strict-phase theorem says a nonzero kernel vector cannot map to
        # the zero interface vector.
        assert max(abs(value) for value in interface) > 1e-10

assert max_kernel_residual < 2e-13
assert max_total_balance_residual < 2e-12
assert max_first_interface_residual < 2e-12

print("PASS: high-t multirow exact-kernel cusp injectivity algebra")
print("max kernel residual =", max_kernel_residual)
print("max total interface-balance residual =", max_total_balance_residual)
print("max first-interface formula residual =", max_first_interface_residual)
