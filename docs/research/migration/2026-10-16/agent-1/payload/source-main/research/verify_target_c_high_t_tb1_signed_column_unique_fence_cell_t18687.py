from __future__ import annotations

import itertools


def incidence(a: int, b: int) -> tuple[int, ...]:
    lo, hi = sorted((a, b))
    return tuple(range(lo + 1, hi + 1))


def interval(a: int, b: int) -> tuple[int, int]:
    return min(a, b), max(a, b)


# Exact consecutive fence-incidence formula in finite ordered fences.
for m in range(1, 9):
    for a in range(m + 1):
        for b in range(m + 1):
            xs = incidence(a, b)
            assert len(xs) == abs(a - b)
            if xs:
                assert xs[0] == min(a, b) + 1
                assert xs[-1] == max(a, b)


# One-dimensional Helly: every pairwise-intersecting finite family of closed
# integer cell intervals has a common integer cell rank.
base = [(a, b) for a in range(6) for b in range(a, 6)]
for r in range(1, 7):
    for fam in itertools.combinations(base, r):
        pairwise = all(
            max(x[0], y[0]) <= min(x[1], y[1])
            for x, y in itertools.combinations(fam, 2)
        )
        if not pairwise:
            continue
        lo = max(x[0] for x in fam)
        hi = min(x[1] for x in fam)
        assert lo <= hi
        assert any(all(a <= g <= b for a, b in fam) for g in range(6))


def cell_type(a: int, b: int, g: int) -> str:
    lo, hi = interval(a, b)
    assert lo <= g <= hi
    if lo < g < hi:
        return "THROUGH"
    if lo == hi == g:
        return "CELL-INTERNAL"
    if hi == g:
        return "LEFT-ANCHORED"
    if lo == g:
        return "RIGHT-ANCHORED"
    raise AssertionError((a, b, g))


# The common-cell condition has exactly the four advertised normal forms.
for m in range(1, 9):
    for g in range(m + 1):
        for a in range(m + 1):
            for b in range(m + 1):
                lo, hi = interval(a, b)
                if not (lo <= g <= hi):
                    continue
                t = cell_type(a, b, g)
                assert t in {
                    "THROUGH",
                    "CELL-INTERNAL",
                    "LEFT-ANCHORED",
                    "RIGHT-ANCHORED",
                }
                if t == "THROUGH" and 0 < g < m:
                    xs = incidence(a, b)
                    assert g in xs
                    assert g + 1 in xs


# Four-way pigeonhole retains ceil(N/4), hence a constant fraction and the
# same D^(epsilon-o(1)) polynomial exponent.
for n in range(1, 1000):
    assert (n + 3) // 4 >= n / 4

print("PASS")
