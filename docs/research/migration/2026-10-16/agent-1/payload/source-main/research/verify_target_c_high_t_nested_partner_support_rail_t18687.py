#!/usr/bin/env python3
"""Regression checks for the nested partner-support rail theorem.

The proof is symbolic for arbitrary size. This script exhaustively checks the
unimodal two-block implication on small integer words and checks the current
quantitative constants.
"""
from fractions import Fraction as Q
from itertools import product
import math


def nondecreasing(xs):
    return all(a <= b for a, b in zip(xs, xs[1:]))


def nonincreasing(xs):
    return all(a >= b for a, b in zip(xs, xs[1:]))


def unimodal(xs):
    n = len(xs)
    return any(nondecreasing(xs[: p + 1]) and nonincreasing(xs[p:]) for p in range(n))


# If S=(b_M^+,...,b_1^+ | b_1^-,...,b_M^-) is unimodal, then either
# the displayed first block is nondecreasing (so natural + order is
# nonincreasing) or the displayed second block is nonincreasing (so natural
# - order is nonincreasing).
for M in range(1, 5):
    for S in product(range(4), repeat=2 * M):
        if not unimodal(S):
            continue
        A = S[:M]
        B = S[M:]
        assert nondecreasing(A) or nonincreasing(B), (M, S)

        plus_natural = tuple(reversed(A))
        minus_natural = B
        assert nonincreasing(plus_natural) or nonincreasing(minus_natural), (M, S)

# Current 90%-density / half-quantile constants.
c0 = Q(113, 20_000_000)
rho = c0 / 100
delta = c0 / 100
eta = c0 / 50
lam = c0 - 6 * rho - eta - 2 * delta
sigma = Q(1, 2)
assert lam == Q(1017, 200_000_000)

kappa = 3 ** (1 / 8)
full_nested = float(lam) / (16 * kappa)
coherent_nested = float(lam) / (32 * kappa)
post_budget = (1 - sigma) * lam
budget_nested = float(post_budget) / (16 * kappa)
budget_coherent = float(post_budget) / (32 * kappa)

assert abs(full_nested - 2.770325615939235e-7) < 5e-20
assert abs(coherent_nested - 1.3851628079696176e-7) < 5e-20
assert abs(budget_nested - 1.3851628079696176e-7) < 5e-20
assert abs(budget_coherent - 6.925814039848088e-8) < 5e-21

K = 1 / (sigma * lam)
assert K == Q(400_000_000, 1017)
assert abs(float(K) - 393313.66764995083) < 1e-9

limit_coherent = float(c0) / (32 * kappa)
assert abs(limit_coherent - 1.5390697866329083e-7) < 5e-20

print("PASS: nested partner-support rail regressions")
print("exhaustive unimodal words checked through M=4 over alphabet {0,1,2,3}")
print("90% full nested coefficient =", full_nested)
print("90% coherent-sign nested coefficient =", coherent_nested)
print("half-quantile nested coefficient =", budget_nested)
print("half-quantile coherent-sign coefficient =", budget_coherent)
print("half-quantile reaction ceiling =", float(K))
print("limiting coherent-sign nested coefficient =", limit_coherent)
