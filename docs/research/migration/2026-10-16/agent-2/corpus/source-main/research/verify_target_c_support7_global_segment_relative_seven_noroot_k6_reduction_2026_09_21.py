#!/usr/bin/env python3
"""Pure arithmetic certificate for the seven-no-root k=6 reduction."""

TARGETS = {
    -2: ((0, 9), (1, 6), (2, 3), (3, 0)),
    -1: ((0, 10), (1, 7), (2, 4), (3, 1)),
}


def global_bound(p, dv, q):
    return 7 + p + 3 * dv - 3 * q


def six_bound(p_i, d_i, q_i):
    return 6 + p_i + 3 * d_i - 3 * q_i


def min_singletons(q, p):
    # q virtual-complete incomplete blocks are nonempty, hence cost 1 or 2.
    # The p selected incomplete rows are a budget for them (other blocks can
    # only make the available budget smaller).
    return max(0, 2 * q - p)


def min_singletons_in_subset(global_q, global_singletons, subset_q):
    return max(0, subset_q - (global_q - global_singletons))


def main():
    # Arithmetic boundary lists from D=7+p+3*d_actual-3*k with k=6.
    for D, tuples in TARGETS.items():
        got = []
        for d in range(4):
            p = D - 7 - 3 * d + 18
            if p >= 0:
                got.append((d, p))
        assert tuple(got) == tuples

    # Global virtual-canonical lift gives dv>=2 and q<=p.
    closed_by_crude = []
    for D, tuples in TARGETS.items():
        for d_actual, p in tuples:
            lower = global_bound(p, 2, p)
            if lower > D:
                closed_by_crude.append((D, d_actual, p, lower))
    assert closed_by_crude == [
        (-2, 1, 6, 1),
        (-2, 2, 3, 7),
        (-2, 3, 0, 13),
        (-1, 2, 4, 5),
        (-1, 3, 1, 11),
    ]

    # p=7: target D=-1 forces dv=2,q=7. A good deletion with p_i=7
    # exists by the deletion-loss budget. Then d_i=2 and q_i>=6.
    assert global_bound(7, 2, 7) == -1
    assert six_bound(7, 2, 5) == 4
    assert six_bound(7, 2, 6) == 1
    assert min_singletons(6, 7) == 5  # coarse local cost bound alone
    assert min_singletons_in_subset(7, 7, 6) == 6
    # Stronger globally: all seven q blocks are singletons, so q_i>=6 means
    # at least six singleton-compatible blocks. Exact d=2 capacity is <=3.

    # p=9: global target D=-2 leaves only (dv,q)=(2,8/9) or (3,9).
    p9 = []
    for dv in range(2, 8):
        for q in range(0, 10):
            if global_bound(9, dv, q) <= -2:
                p9.append((dv, q))
    assert p9 == [(2, 8), (2, 9), (3, 9)]
    # A p_i=9 deletion has q_i>=7 at d_i=2 and q_i>=8 at d_i=3.
    assert min(q for q in range(10) if six_bound(9, 2, q) <= 0) == 7
    assert min(q for q in range(10) if six_bound(9, 3, q) <= 0) == 8
    # In global dv=2 cases there are at least 7 global q-singletons; any
    # q_i>=7 subset contains >=6 singleton blocks. This beats d2 capacity 3.
    assert min_singletons(8, 9) == 7
    assert min_singletons(9, 9) == 9
    assert min_singletons_in_subset(8, 7, 7) == 6
    assert min_singletons_in_subset(9, 9, 7) == 7
    # Therefore only dv=3,q=9 remains, and the chosen deletion must have
    # d_i=3, q_i>=8: it needs singleton capacity >=8.

    # p=10: global target D=-1 permits dv<=4. A good p_i=10 deletion cannot
    # have d_i=2 because q_i>=7 requires >=4 singleton blocks, while d2
    # capacity is <=3. Thus d_i is 3 or 4, with the following thresholds.
    p10 = []
    for dv in range(2, 8):
        for q in range(0, 11):
            if global_bound(10, dv, q) <= -1:
                p10.append((dv, q))
    assert p10 == [(2, 8), (2, 9), (2, 10), (3, 9), (3, 10), (4, 10)]
    q2 = min(q for q in range(11) if six_bound(10, 2, q) <= 1)
    q3 = min(q for q in range(11) if six_bound(10, 3, q) <= 1)
    q4 = min(q for q in range(11) if six_bound(10, 4, q) <= 1)
    assert (q2, q3, q4) == (7, 8, 9)
    assert (min_singletons(q2, 10), min_singletons(q3, 10), min_singletons(q4, 10)) == (4, 6, 8)
    # Once dv=2 is excluded, the global possibilities sharpen those local
    # singleton minima: dv=3,q=9 has >=8 singleton blocks; dv=4,q=10 has 10.
    assert min_singletons_in_subset(9, 8, 8) == 7
    assert min_singletons_in_subset(10, 10, 9) == 9

    # Loss-budget pigeonhole checks. Good deletion count is 7 for D=-2
    # and at least 5 for D=-1. If every good deletion dropped to the next
    # lower allowed p band, each loses at least 3 selected rows.
    assert 7 * 3 > 9
    assert 5 * 3 > 7
    assert 5 * 3 > 10

    # Exact all-touch six-row capacity audit targets.
    d3_cap_ge6 = {6: 485, 7: 78, 8: 116, 9: 144, 10: 64}
    d4_cap_ge8 = {8: 15366, 9: 13536, 10: 12922, 11: 11898, 12: 8614, 13: 3733, 14: 762}
    assert sum(v for c, v in d3_cap_ge6.items() if c >= 8) == 324
    assert sum(v for c, v in d3_cap_ge6.items() if c >= 7) == 402
    assert sum(v for c, v in d4_cap_ge8.items() if c >= 9) == 51465

    print("PASS: seven-no-root k=6 reduction arithmetic")
    print("closed_arithmetic_branches", 6)
    print("remaining", ((-2, 0, 9), (-1, 0, 10)))
    print("p9_d3_capacity_ge8_cover", 324)
    print("p10_d3_capacity_ge7_cover", 402)
    print("p10_d4_capacity_ge9_cover", 51465)


if __name__ == "__main__":
    main()
