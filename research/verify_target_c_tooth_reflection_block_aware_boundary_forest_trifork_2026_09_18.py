#!/usr/bin/env python3
"""Regression checks for the block-aware fixed-pair boundary/forest theorem.

This certifies arithmetic and the finite one-dimensional block bookkeeping used in the
proof note. It is not a substitute for the geometric proof.
"""

from __future__ import annotations

import itertools
import math
import random

H = math.sqrt(303.0) / 52.0
CSTAR = 0.129220199818177
BSTAR = math.sin(CSTAR / 2.0)
ALPHA1 = 1.0 - H
C_OLD = math.sqrt(ALPHA1 * BSTAR / 10.0)
C_NEW = math.sqrt(ALPHA1 * BSTAR / 6.0)

assert abs(C_NEW / C_OLD - math.sqrt(5.0 / 3.0)) < 1e-14
assert abs(C_NEW - 0.08460900362112289) < 1e-14
assert abs(C_NEW / 2.0 - 0.042304501810561446) < 1e-14
assert abs(2.0 * H / C_NEW - 7.912821804074039) < 1e-12


def upper_blocks(bits: tuple[int, ...]) -> list[tuple[int, int]]:
    """Inclusive edge-index intervals of maximal 1-blocks."""
    out: list[tuple[int, int]] = []
    i = 0
    while i < len(bits):
        if not bits[i]:
            i += 1
            continue
        j = i
        while j + 1 < len(bits) and bits[j + 1]:
            j += 1
        out.append((i, j))
        i = j + 1
    return out


def lower_runs(bits: tuple[int, ...]) -> int:
    """Number of nonempty maximal 0-blocks."""
    if not bits:
        return 0
    count = 0
    prev = 1
    for bit in bits:
        if bit == 0 and prev == 1:
            count += 1
        prev = bit
    return count


# One first edge per upper block is a matching, and B blocks create at most B+1
# nonempty lower runs. Exhaust all edge-type words through length 14.
for n in range(1, 15):
    for bits in itertools.product((0, 1), repeat=n):
        blocks = upper_blocks(bits)
        first = [a for a, _ in blocks]
        assert all(y - x >= 2 for x, y in zip(first, first[1:]))
        assert lower_runs(bits) <= len(blocks) + 1

# Exact scalar minimax: max{x-B, B/2} >= x/3 for x,B >= 0.
random.seed(20260918)
for _ in range(300_000):
    x = 10 ** random.uniform(-6, 6)
    block_count = 10 ** random.uniform(-6, 6)
    lhs = max(x - block_count, block_count / 2.0)
    assert lhs + 1e-12 * max(1.0, x, block_count) >= x / 3.0

# Equality occurs at B=2x/3.
for x in (1e-6, 0.1, 1.0, 37.0, 1e6):
    block_count = 2.0 * x / 3.0
    lhs = max(x - block_count, block_count / 2.0)
    assert abs(lhs - x / 3.0) <= 1e-12 * max(1.0, x)

# Balance E/(3s) = b*s at s=sqrt(E/(3b)).
for edge_count in (1.0, 10.0, 1e3, 1e9):
    s = math.sqrt(edge_count / (3.0 * BSTAR))
    face = edge_count / (3.0 * s)
    drift = BSTAR * s
    target = math.sqrt(BSTAR * edge_count / 3.0)
    assert abs(face - target) < 1e-12 * max(1.0, target)
    assert abs(drift - target) < 1e-12 * max(1.0, target)

print("block-aware boundary/forest certificate: PASS")
print(f"h_*={H:.15f}")
print(f"b_*={BSTAR:.15f}")
print(f"alpha_1={ALPHA1:.15f}")
print(f"old coefficient={C_OLD:.15f}")
print(f"new coefficient={C_NEW:.15f}")
print(f"improvement factor={C_NEW / C_OLD:.15f}")
print(f"K=1,Lambda=2 submatching coefficient={C_NEW / 2.0:.15f}")
print(f"K=1,Lambda=2 deficit coefficient={2.0 * H / C_NEW:.15f}")
