#!/usr/bin/env python3
"""Regression checks for the linear-density host/death-plateau lift."""

from fractions import Fraction
from itertools import combinations_with_replacement
from math import pow


def nondec(xs):
    return all(a <= b for a, b in zip(xs, xs[1:]))


def noninc(xs):
    return all(a >= b for a, b in zip(xs, xs[1:]))


# Exhaust the one-turn argument while allowing repeated partner incidences.
# U = first host side, T = terminal piece, D = second host side.
for m in range(2, 8):
    k = 1
    master = [(r, "U") for r in range(k, m + 1)]
    master += [(m, "T"), (m, "T")]
    master += [(r, "D") for r in range(m, k - 1, -1)]

    # A weakly ordered partner-incidence sequence is a nondecreasing tuple
    # of master positions; equality models several rail bars sharing one
    # physical partner vertex.
    for length in range(1, 6):
        for idxs in combinations_with_replacement(range(len(master)), length):
            sub = [master[j] for j in idxs]
            labels = [r for r, _ in sub]

            if nondec(labels):
                wrong = [r for r, tag in sub if tag != "U"]
                assert len(set(wrong)) <= 1, (m, idxs, sub, "plus")

            if noninc(labels):
                wrong = [r for r, tag in sub if tag != "D"]
                assert len(set(wrong)) <= 1, (m, idxs, sub, "minus")


# Arbitrarily long death plateaus satisfy strict support nesting even though
# all intervals have the same right endpoint.
for N in range(1, 50):
    k = N + 3
    b = 3 * N + 20
    births = list(range(1, N + 1))
    intervals = [set(range(i + 1, b + 1)) for i in births]
    assert all(k in I for I in intervals)
    assert all(intervals[j + 1] < intervals[j] for j in range(N - 1))


# Quantitative constants.
c0 = Fraction(113, 20_000_000)
lambda90 = Fraction(9, 10) * c0
root = pow(3.0, 1.0 / 8.0)

linear_branch90 = float(lambda90) / 2.0
unsigned_disjoint90 = float(lambda90) / (8.0 * root)
unsigned_disjoint_limit = float(c0) / (8.0 * root)

signed_linear90 = float(lambda90) / 4.0
signed_disjoint90 = float(lambda90) / (16.0 * root)

sigma = Fraction(1, 2)
stress_unsigned_linear90 = float((1 - sigma) * lambda90) / 2.0
stress_signed_linear90 = float((1 - sigma) * lambda90) / 4.0
stress_unsigned_disjoint90 = float((1 - sigma) * lambda90) / (8.0 * root)
stress_signed_disjoint90 = float((1 - sigma) * lambda90) / (16.0 * root)

assert abs(linear_branch90 - 2.5425e-6) < 1e-20
assert abs(signed_linear90 - linear_branch90 / 2.0) < 1e-20
assert abs(stress_unsigned_linear90 - linear_branch90 / 2.0) < 1e-20
assert abs(stress_signed_linear90 - signed_linear90 / 2.0) < 1e-20
assert abs(stress_unsigned_disjoint90 - unsigned_disjoint90 / 2.0) < 1e-20
assert abs(stress_signed_disjoint90 - signed_disjoint90 / 2.0) < 1e-20
assert unsigned_disjoint_limit > unsigned_disjoint90 > 0.0

print("PASS: linear host/death-plateau regressions")
print(f"linear_host_or_plateau90_density={linear_branch90:.12g}")
print(f"endpoint_disjoint90_D_quarter={unsigned_disjoint90:.12g}")
print(f"optimized_endpoint_disjoint_limit={unsigned_disjoint_limit:.12g}")
print(f"coherent_sign_linear90_density={signed_linear90:.12g}")
print(f"coherent_sign_disjoint90_D_quarter={signed_disjoint90:.12g}")
print(f"stress_unsigned_linear90_density={stress_unsigned_linear90:.12g}")
print(f"stress_signed_linear90_density={stress_signed_linear90:.12g}")
print(f"stress_unsigned_disjoint90_D_quarter={stress_unsigned_disjoint90:.12g}")
print(f"stress_signed_disjoint90_D_quarter={stress_signed_disjoint90:.12g}")
