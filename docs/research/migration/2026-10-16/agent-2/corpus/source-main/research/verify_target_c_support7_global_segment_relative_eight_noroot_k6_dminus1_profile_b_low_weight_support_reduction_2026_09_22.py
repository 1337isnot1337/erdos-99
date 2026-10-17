#!/usr/bin/env python3
"""Arithmetic/projective certificate for Profile B low-weight coefficient words.

This checker contains no new large finite census. It composes exact bounds
already certified elsewhere in the repository with the deletion identity for
the remaining eight-no-root k=6, D=-1, p=9 all-singleton Profile B.
"""

from collections import defaultdict


def partitions(n, minimum=1):
    if n == 0:
        yield ()
        return
    for first in range(minimum, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def child_profiles(weight):
    # A minimum word of weight r<4 spans the one-dimensional kernel killed by
    # deleting its support. d2(P)>=4 keeps one coefficient direction alive.
    t = 8 - weight
    rank_p = 1
    k = t - rank_p
    D = -1 + 2 * weight - 3
    assert D == 2 * weight - 4

    out = []
    for d_root in range(4):
        p = 9 - 3 * d_root
        if p < 0:
            continue
        assert D == t + p + 3 * d_root - 3 * k
        out.append((p, d_root))
    assert out == [(9, 0), (6, 1), (3, 2), (0, 3)]
    return t, k, D, out


def required_extra_rank(t, p, deficiency, D):
    numerator = t + p + 3 * deficiency - D
    return (numerator + 2) // 3


def weight_two_cases():
    t, k, D, p_options = child_profiles(2)
    assert (t, k, D) == (6, 5, 0)

    # Exact committed six-row inputs:
    # d=2 synchronized rank-one singleton capacity <=3;
    # d=3, capacity>=8 singleton-functional extra rank <=4.
    d2_capacity_max = 3
    d3_high_capacity_extra_max = 4

    survivors = []
    for p, d_root in p_options:
        for deficiency in (2, 3):
            need = required_extra_rank(t, p, deficiency, D)
            if deficiency == 2:
                possible = need <= d2_capacity_max
            else:
                if need > p:
                    possible = False
                elif need >= 8:
                    possible = d3_high_capacity_extra_max >= need
                else:
                    # This branch is never reached for p in {9,6,3,0}.
                    possible = True
            if possible:
                survivors.append((p, d_root, deficiency, need))
    assert survivors == []
    return survivors


def weight_three_cases():
    t, k, D, p_options = child_profiles(3)
    assert (t, k, D) == (5, 4, 2)

    # Exact committed five-row inputs:
    # d=2, capacity>=5 singleton-functional extra rank =2 (max 2);
    # d=3, capacity>=7 singleton-functional extra rank <=6.
    d2_extra_max = 2
    d3_capacity7_extra_max = 6

    survivors = []
    for p, d_root in p_options:
        for deficiency in (2, 3):
            need = required_extra_rank(t, p, deficiency, D)
            if need > p:
                possible = False
            elif deficiency == 2 and need >= 5:
                possible = d2_extra_max >= need
            elif deficiency == 3 and need >= 7:
                possible = d3_capacity7_extra_max >= need
            else:
                possible = True
            if possible:
                survivors.append((p, d_root, deficiency, need))

    assert survivors == [(6, 1, 3, 6)]
    return survivors


def projective_minimum_weight_profiles():
    """Classify rank-two Q^8 projective multiplicities after d2>=4,d1>=3."""
    profiles = defaultdict(set)
    for zero_columns in range(5):
        support = 8 - zero_columns
        for multiplicities in partitions(support):
            if len(multiplicities) < 2:
                continue
            d1 = support - max(multiplicities)
            if d1 < 3:
                continue
            low = tuple(m for m in multiplicities if support - m <= 3)
            if not low:
                clean = 8
                min_supports = 0
            elif len(low) == 1:
                clean = zero_columns + low[0]
                min_supports = sum(
                    1 for m in multiplicities if support - m == d1
                )
            else:
                clean = zero_columns
                min_supports = sum(
                    1 for m in multiplicities if support - m == d1
                )
            profiles[d1].add(
                (zero_columns, multiplicities, clean, min_supports)
            )

    d1_3 = profiles[3]
    assert {clean for _, _, clean, _ in d1_3} == {2, 3, 4, 5}
    assert {count for _, _, _, count in d1_3} == {1, 2, 4}
    assert all(
        clean == 8
        for d1, rows in profiles.items()
        if d1 >= 4
        for _, _, clean, _ in rows
    )
    return profiles


def main():
    assert weight_two_cases() == []
    residual = weight_three_cases()
    profiles = projective_minimum_weight_profiles()

    print("PASS: Profile B low-weight coefficient reduction")
    print("weight2_survivors", 0)
    print("weight3_survivors", residual)
    print("source_minimum_distance_lower_bound", 3)
    print(
        "d1_eq_3_three_clean_counts",
        sorted({clean for _, _, clean, _ in profiles[3]}),
    )
    print("d1_ge_4_three_clean_count", 8)


if __name__ == "__main__":
    main()
