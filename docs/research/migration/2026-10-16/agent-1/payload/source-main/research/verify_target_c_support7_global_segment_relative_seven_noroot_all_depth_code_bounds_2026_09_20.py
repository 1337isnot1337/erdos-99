#!/usr/bin/env python3
"""Arithmetic certificate for all-depth deletion/code bounds in the seven-no-root layer.

Assume B is a hypothetical seven-no-root counterexample after the established
six-no-root closure. Then D(B) is -2 or -1, every external row is an M-coloop,
and every deletion shadow with at most six no-root rows has nonnegative defect.
For a deleted coordinate set S of size s, let q_S be the quotient-rank drop.
The exact defect transport identity is

    D(B\S) = D(B) + 2*s - 3*q_S.

Hence q_S <= floor((D+2*s)/3). In coefficient-space language q_S is exactly
the dimension of the subspace of P supported inside S. This script checks the
resulting shortened-dimension caps, generalized Hamming-weight lower bounds,
and the 30 arithmetic boundary tuples already present in the repository.
"""
from math import ceil, floor


def boundary_cases(D):
    out = []
    for k in range(3, 8):
        d = 0
        while True:
            p = D - 7 - 3 * d + 3 * k
            if p < 0:
                break
            out.append((k, d, p))
            d += 1
    return out


def q_cap(D, s):
    assert D in (-2, -1)
    assert 1 <= s <= 7
    return floor((D + 2 * s) / 3)


def generalized_weight_lower(D, j):
    """Least support size forced for a j-dimensional subcode of P."""
    assert D in (-2, -1)
    assert 1 <= j <= 4
    by_formula = ceil((3 * j - D) / 2)
    by_scan = next(s for s in range(1, 8) if q_cap(D, s) >= j)
    assert by_formula == by_scan
    return by_formula


def projection_rank_lower(D, rank_P, s):
    return rank_P - min(rank_P, q_cap(D, s))


EXPECTED_BOUNDARIES = {
    -2: [
        (3, 0, 0),
        (4, 0, 3), (4, 1, 0),
        (5, 0, 6), (5, 1, 3), (5, 2, 0),
        (6, 0, 9), (6, 1, 6), (6, 2, 3), (6, 3, 0),
        (7, 0, 12), (7, 1, 9), (7, 2, 6), (7, 3, 3), (7, 4, 0),
    ],
    -1: [
        (3, 0, 1),
        (4, 0, 4), (4, 1, 1),
        (5, 0, 7), (5, 1, 4), (5, 2, 1),
        (6, 0, 10), (6, 1, 7), (6, 2, 4), (6, 3, 1),
        (7, 0, 13), (7, 1, 10), (7, 2, 7), (7, 3, 4), (7, 4, 1),
    ],
}

EXPECTED_Q_CAPS = {
    -2: [0, 0, 1, 2, 2, 3, 4],
    -1: [0, 1, 1, 2, 3, 3, 4],
}

EXPECTED_WEIGHTS = {
    -2: [3, 4, 6, 7],
    -1: [2, 4, 5, 7],
}

for D in (-2, -1):
    assert boundary_cases(D) == EXPECTED_BOUNDARIES[D]
    caps = [q_cap(D, s) for s in range(1, 8)]
    assert caps == EXPECTED_Q_CAPS[D]
    weights = [generalized_weight_lower(D, j) for j in range(1, 5)]
    assert weights == EXPECTED_WEIGHTS[D]

# Branch-specific tables for ranks P=7-k.
branch_weights = {}
for D in (-2, -1):
    for k in range(3, 8):
        r = 7 - k
        branch_weights[(D, k)] = tuple(
            generalized_weight_lower(D, j) for j in range(1, r + 1)
        )

assert branch_weights[(-2, 3)] == (3, 4, 6, 7)
assert branch_weights[(-2, 4)] == (3, 4, 6)
assert branch_weights[(-2, 5)] == (3, 4)
assert branch_weights[(-2, 6)] == (3,)
assert branch_weights[(-2, 7)] == ()
assert branch_weights[(-1, 3)] == (2, 4, 5, 7)
assert branch_weights[(-1, 4)] == (2, 4, 5)
assert branch_weights[(-1, 5)] == (2, 4)
assert branch_weights[(-1, 6)] == (2,)
assert branch_weights[(-1, 7)] == ()

# Two current finite targets get stronger projection filters than the old
# one-/two-deletion tests alone.
assert [projection_rank_lower(-2, 3, s) for s in range(1, 8)] == [3, 3, 2, 1, 1, 0, 0]
assert [projection_rank_lower(-1, 4, s) for s in range(1, 8)] == [4, 3, 3, 2, 1, 1, 0]

print("PASS: seven-no-root all-depth deletion/code bounds")
for D in (-2, -1):
    print("D", D)
    print("q_caps_s1_to_s7", EXPECTED_Q_CAPS[D])
    print("generalized_weight_lower_j1_to_j4", EXPECTED_WEIGHTS[D])
    for k in range(3, 8):
        print("k", k, "rank_P", 7-k, "weight_bounds", branch_weights[(D, k)])
