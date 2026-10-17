#!/usr/bin/env python3
"""Regression checks for the strong-TB1 ordered-support trichotomy."""

from fractions import Fraction
from itertools import combinations_with_replacement
from math import pow


def nondec(xs):
    return all(a <= b for a, b in zip(xs, xs[1:]))


def noninc(xs):
    return all(a >= b for a, b in zip(xs, xs[1:]))


def unimodal(xs):
    if not xs:
        return True
    return any(nondec(xs[: p + 1]) and noninc(xs[p:]) for p in range(len(xs)))


def longest_monotone_piece(xs):
    best = 0
    n = len(xs)
    for p in range(n):
        if nondec(xs[: p + 1]):
            best = max(best, p + 1)
        if noninc(xs[p:]):
            best = max(best, n - p)
    return best


# A weakly ordered partner-incidence subsequence of the one-turn hubward
# boundary word is unimodal even when several selected bars share one partner
# vertex. Equality of selected positions models such partner ties.
for m in range(2, 8):
    k = 1
    master = [(r, "U") for r in range(k, m + 1)]
    master += [(m, "T"), (m, "T")]
    master += [(r, "D") for r in range(m, k - 1, -1)]

    for length in range(1, 7):
        for idxs in combinations_with_replacement(range(len(master)), length):
            labels = [master[j][0] for j in idxs]
            assert unimodal(labels), (m, idxs, labels)

            # Every unimodal word has a monotone prefix or suffix of at least
            # half its length. This is the staircase-versus-nested extraction.
            assert longest_monotone_piece(labels) >= (length + 1) // 2

            # Once a monotone selected lane is nested, the same one-turn
            # host/death proof applies with repeated partner incidences.
            if nondec(labels):
                wrong = [master[j][0] for j in idxs if master[j][1] != "U"]
                assert len(set(wrong)) <= 1, (m, idxs, "nondec")
            if noninc(labels):
                wrong = [master[j][0] for j in idxs if master[j][1] != "D"]
                assert len(set(wrong)) <= 1, (m, idxs, "noninc")


# Quantitative losses from the strong-TB1 fork:
# 1/2 for one fixed birth side, 1/2 for one monotone support run, and in the
# nested case another 1/2 for host versus one-death plateau.
c0 = Fraction(113, 20_000_000)
s0 = Fraction(7, 16) * c0
assert s0 == Fraction(791, 320_000_000)

root = pow(3.0, 1.0 / 8.0)
fixed_birth_side = float(s0 / 2)
monotone_support = float(s0 / 4)
uniform_trichotomy = float(s0 / 8)
endpoint_disjoint = float(s0) / (32.0 * root)
gamma = float(c0 / 32)

assert abs(fixed_birth_side - 1.2359375e-6) < 1e-20
assert abs(monotone_support - 6.1796875e-7) < 1e-20
assert abs(uniform_trichotomy - 3.08984375e-7) < 1e-20
assert endpoint_disjoint > 0.0

print("PASS: strong-TB1 ordered-support trichotomy regressions")
print(f"strong_parent_density={float(s0):.12g}")
print(f"fixed_birth_side_density={fixed_birth_side:.12g}")
print(f"monotone_support_density={monotone_support:.12g}")
print(f"uniform_trichotomy_density={uniform_trichotomy:.12g}")
print(f"endpoint_disjoint_D_quarter={endpoint_disjoint:.12g}")
print(f"strong_angle_gamma={gamma:.12g}")
