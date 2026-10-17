from fractions import Fraction
from itertools import combinations, product

# Regression certificate for
# target_c_high_t_tb1_inactive_common_cut_rail_t18687_2026-09-17.md
#
# The geometric step "disjoint support intervals cannot correspond to crossing
# hull chords" is proved in the companion note.  This script exhaustively
# checks the finite interval-Helly and weak-unimodality combinatorics on small
# models and verifies the quantitative extraction constant.

# ---------------------------------------------------------------------------
# 1. Finite interval Helly: pairwise-intersecting integer intervals have a
#    common integer point.
# ---------------------------------------------------------------------------
for n in range(1, 5):
    intervals = [
        (left, right)
        for left in range(1, n + 1)
        for right in range(left, n + 1)
    ]

    for mask in range(1, 1 << len(intervals)):
        family = [
            intervals[i]
            for i in range(len(intervals))
            if (mask >> i) & 1
        ]

        pairwise = all(
            max(a, c) <= min(b, d)
            for (a, b), (c, d) in combinations(family, 2)
        )

        if pairwise:
            assert max(left for left, _ in family) <= min(
                right for _, right in family
            )

# ---------------------------------------------------------------------------
# 2. A weakly unimodal word contains a monotone prefix or suffix of at least
#    half its length (the pieces overlap at a peak plateau).
# ---------------------------------------------------------------------------
def is_weakly_unimodal(seq):
    n = len(seq)
    return any(
        all(seq[i] <= seq[i + 1] for i in range(p))
        and all(seq[i] >= seq[i + 1] for i in range(p, n - 1))
        for p in range(n)
    )


for n in range(1, 8):
    for seq in product(range(4), repeat=n):
        if not is_weakly_unimodal(seq):
            continue

        found = False
        for p in range(n):
            nondecreasing_prefix = all(
                seq[i] <= seq[i + 1] for i in range(p)
            )
            nonincreasing_suffix = all(
                seq[i] >= seq[i + 1] for i in range(p, n - 1)
            )
            if nondecreasing_prefix and nonincreasing_suffix:
                assert max(p + 1, n - p) >= (n + 1) // 2
                found = True
                break
        assert found

# ---------------------------------------------------------------------------
# 3. Quantitative extraction.
#    Parent matching coefficient:
#        s0 / (256 * 3^(1/8)).
#    Losses: 1/2 tagged shore, 1/2 physical host, 1/2 monotone run.
# ---------------------------------------------------------------------------
S0 = Fraction(791, 320_000_000)
parent_coefficient = float(S0) / (256 * (3 ** (1 / 8)))
rail_coefficient = float(S0) / (2048 * (3 ** (1 / 8)))

assert abs(parent_coefficient - 8.416787895648718e-9) < 1e-20
assert abs(rail_coefficient - 1.0520984869560897e-9) < 1e-21
assert abs(parent_coefficient / 8 - rail_coefficient) < 1e-22

print("PASS: TB1 inactive common-cut rail certificate")
print("parent matching coefficient =", parent_coefficient)
print("ordered rail coefficient =", rail_coefficient)
