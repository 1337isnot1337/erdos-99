#!/usr/bin/env python3
"""Regression checks for the high-t partner-rainbow support-order theorem."""

from fractions import Fraction
from itertools import permutations, product
from math import ceil, pow


def between(a, x, b, n):
    """Whether x is strictly on the counterclockwise open arc a->b on Z/nZ."""
    if a < b:
        return a < x < b
    return x > a or x < b


def chords_cross(e1, e2, n):
    a, b = e1
    c, d = e2
    if len({a, b, c, d}) < 4:
        return False
    return between(a, c, b, n) != between(a, d, b, n)


# If N endpoints occupy one shore first and N endpoints occupy the complementary
# shore second in the ambient cyclic order, the unique perfect matching in which
# every pair of edges crosses is the order-preserving matching.
for N in range(2, 8):
    good = []
    for perm in permutations(range(N)):
        edges = [(i, N + perm[i]) for i in range(N)]
        if all(
            chords_cross(edges[i], edges[j], 2 * N)
            for i in range(N)
            for j in range(i + 1, N)
        ):
            good.append(perm)
    assert good == [tuple(range(N))], (N, good)


def is_nondecreasing(seq):
    return all(a <= b for a, b in zip(seq, seq[1:]))


def is_nonincreasing(seq):
    return all(a >= b for a, b in zip(seq, seq[1:]))


def is_monotone(seq):
    return is_nondecreasing(seq) or is_nonincreasing(seq)


def is_unimodal(seq):
    """Weakly nondecreasing then weakly nonincreasing, allowing a plateau."""
    n = len(seq)
    return any(
        is_nondecreasing(seq[: p + 1]) and is_nonincreasing(seq[p:])
        for p in range(n)
    )


# Exhaust the abstract one-peak lemma for two equal blocks through length 8.
# Any weakly unimodal 2M-word has at least one monotone M-block.
for M in range(1, 5):
    for seq in product(range(4), repeat=2 * M):
        if is_unimodal(seq):
            assert is_monotone(seq[:M]) or is_monotone(seq[M:]), (M, seq)


# A model hubward shore has region labels increasing along one host side,
# plateauing in the terminal region, and decreasing along the other host side.
# Every ordered subsequence remains unimodal and hence obeys the same two-block lemma.
for m in range(3, 8):
    k = 1
    master = list(range(k, m + 1)) + [m, m] + list(range(m - 1, k - 1, -1))
    assert is_unimodal(master)
    L = len(master)
    for mask in range(1, 1 << L):
        sub = [master[j] for j in range(L) if mask & (1 << j)]
        assert is_unimodal(sub)
        if len(sub) % 2 == 0:
            M = len(sub) // 2
            assert is_monotone(sub[:M]) or is_monotone(sub[M:])


# Interval normal form: increasing births plus monotone death indices gives
# exactly a nested lane or a proper staircase, and every interval contains hub k.
def interval_set(i, b):
    return set(range(i + 1, b + 1))


births = [2, 5, 9, 12]
k = 20
for deaths in ([31, 28, 25, 22], [22, 25, 28, 31], [24, 24, 24, 24]):
    assert all(b >= k for b in deaths)
    intervals = [interval_set(i, b) for i, b in zip(births, deaths)]
    assert all(k in I for I in intervals)
    if is_nonincreasing(deaths):
        assert all(intervals[j + 1] <= intervals[j] for j in range(len(intervals) - 1))
    if is_nondecreasing(deaths):
        assert all(
            births[j] < births[j + 1] and deaths[j] <= deaths[j + 1]
            for j in range(len(births) - 1)
        )


# Quantitative inheritance from the current parameterized deep-braid theorem.
c0 = Fraction(113, 20_000_000)
lambda90 = Fraction(9, 10) * c0
braid90 = float(lambda90) / (16.0 * pow(3.0, 1.0 / 8.0))
lane90 = float(lambda90) / (32.0 * pow(3.0, 1.0 / 8.0))
limit_lane = float(c0) / (32.0 * pow(3.0, 1.0 / 8.0))
assert braid90 > 0.0
assert lane90 > 0.0
assert abs(lane90 - braid90 / 2.0) < 1e-20
assert limit_lane > lane90

# Optional global reaction-budget quantile, sigma=1/2.
sigma = Fraction(1, 2)
budget_lane90 = float((1 - sigma) * lambda90) / (32.0 * pow(3.0, 1.0 / 8.0))
reaction_cap90 = 1.0 / float(sigma * lambda90)
assert abs(budget_lane90 - lane90 / 2.0) < 1e-20
assert abs(reaction_cap90 - 2.0 / float(lambda90)) < 1e-12
assert reaction_cap90 < 400_000

for M in range(1, 100):
    assert ceil(M / 2) >= M / 2

print("PASS: high-t partner-rainbow support-order regressions")
print(f"braid90_D_quarter_constant={braid90:.12g}")
print(f"coherent_lane90_D_quarter_constant={lane90:.12g}")
print(f"optimized_lane_limit_constant={limit_lane:.12g}")
print(f"budget_lane90_D_quarter_constant={budget_lane90:.12g}")
print(f"budget_reaction_cap90={reaction_cap90:.12g}")
