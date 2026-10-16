#!/usr/bin/env python3
"""Regression checks for the physical-piece support normal form."""

from fractions import Fraction
from itertools import combinations_with_replacement
from math import pow


def nondec(xs):
    return all(a <= b for a, b in zip(xs, xs[1:]))


def noninc(xs):
    return all(a >= b for a, b in zip(xs, xs[1:]))


# Restricting the weakly ordered partner incidences to either physical host
# piece makes the path-region labels monotone. Repeated selected positions
# model several chosen bars sharing one hubward partner vertex.
for m in range(2, 9):
    up = list(range(1, m + 1))
    down = list(range(m, 0, -1))

    for piece in (up, down):
        for n in range(1, 7):
            for idxs in combinations_with_replacement(range(len(piece)), n):
                labels = [piece[j] for j in idxs]
                assert nondec(labels) or noninc(labels)

    # Every incidence on the far terminal piece has the same path-region tag m.
    terminal = [m, m, m]
    for n in range(1, 7):
        for idxs in combinations_with_replacement(range(len(terminal)), n):
            labels = [terminal[j] for j in idxs]
            assert len(set(labels)) == 1
            assert labels[0] == m


# Current unconditional exact-antipodal/strong-TB1 application.
c0 = Fraction(113, 20_000_000)
s0 = Fraction(7, 16) * c0
root = pow(3.0, 1.0 / 8.0)

normal = s0 / 6
endpoint_disjoint = float(s0) / (24.0 * root)

assert normal == Fraction(791, 1_920_000_000)
assert abs(float(normal) - 4.1197916666666666e-7) < 1e-20
assert abs(endpoint_disjoint - 8.977907088691964e-8) < 1e-22

# Stronger no-fixed-margin-TB1 application: the linear nested exact-force rail
# has already paid the birth-side choice, so only the three hubward pieces cost.
lambda90 = Fraction(9, 10) * c0
no_tb1_linear = lambda90 / 3
no_tb1_disjoint = float(lambda90) / (12.0 * root)

assert abs(float(no_tb1_linear) - 1.695e-6) < 1e-20
assert abs(no_tb1_disjoint - 3.6937674879189793e-7) < 1e-21

print("PASS: physical-piece support normal-form regressions")
print(f"unconditional_linear_density={float(normal):.12g}")
print(f"unconditional_disjoint_D_quarter={endpoint_disjoint:.12g}")
print(f"no_tb1_90_linear_density={float(no_tb1_linear):.12g}")
print(f"no_tb1_90_disjoint_D_quarter={no_tb1_disjoint:.12g}")
print(f"no_tb1_limit_linear_density={float(c0 / 3):.12g}")
