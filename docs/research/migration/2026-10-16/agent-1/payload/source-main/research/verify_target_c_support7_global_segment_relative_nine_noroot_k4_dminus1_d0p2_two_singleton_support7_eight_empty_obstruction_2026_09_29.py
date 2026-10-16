#!/usr/bin/env python3
from collections import Counter
from itertools import combinations

import verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28 as B

SUPPORT = [
    ((0, 1, 2, 3), 3),
    ((0, 1, 2, 4), 1),
    ((0, 1, 3, 4), 1),
    ((0, 1, 4, 5), 1),
    ((0, 1, 5, 6), 1),
    ((0, 2, 3, 4), 1),
    ((1, 2, 3, 4), 1),
]

EXPECTED = Counter({
    "orientations": 729,
    "eight_subsets": 9382230,
    "mod2_rank_at_least_5": 9380367,
    "mod2_rank_4": 1863,
    "exact_rank_4": 1863,
    "parity_reject": 1863,
})

def mod2_rank_at_most_five(rows):
    basis = [0] * 9
    rank = 0
    for x in rows:
        while x:
            p = x.bit_length() - 1
            if basis[p]:
                x ^= basis[p]
            else:
                basis[p] = x
                rank += 1
                if rank == 5:
                    return 5
                break
    return rank

def main():
    census = Counter()
    for ext in B.oriented_exts(SUPPORT):
        census["orientations"] += 1
        touched = tuple(sorted({b for e in ext for b, v in enumerate(B.QCOMP[e]) if v != (0, 0)}))
        touched_mask = sum(1 << b for b in touched)
        assert len(touched) == 16
        assert B.h_rank(touched_mask) == 10

        mod2_rows = []
        exact_rows = []
        for b in touched:
            vals = [B.QCOMP[e][b] for e in ext]
            x = sum((int(v[0]) & 1) << i for i, v in enumerate(vals))
            y = sum((int(v[1]) & 1) << i for i, v in enumerate(vals))
            mod2_rows.append((x, y))
            exact_rows.append((tuple(v[0] for v in vals), tuple(v[1] for v in vals)))

        for eight in combinations(range(16), 8):
            census["eight_subsets"] += 1
            rows2 = []
            for j in eight:
                rows2.extend(mod2_rows[j])
            r2 = mod2_rank_at_most_five(rows2)
            if r2 == 5:
                census["mod2_rank_at_least_5"] += 1
                continue

            assert r2 == 4
            census["mod2_rank_4"] += 1
            rows = []
            for j in eight:
                rows.extend(exact_rows[j])
            W = B.rowspace_key(rows)
            assert len(W) == 4
            census["exact_rank_4"] += 1
            assert not B.parity_profile_ok(W)
            census["parity_reject"] += 1

    assert census == EXPECTED, census
    print("census", dict(census))
    print("PASS: support7 has no realizable orientation")

if __name__ == "__main__":
    main()
