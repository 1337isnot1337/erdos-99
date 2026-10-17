#!/usr/bin/env python3
from collections import Counter
from itertools import combinations

import verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28 as B
import verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support4_burnside_2026_09_29 as S

SUPPORT = [
    ((0, 1, 2, 3), 3),
    ((0, 1, 2, 4), 2),
    ((0, 1, 3, 4), 2),
    ((0, 2, 3, 4), 1),
    ((1, 2, 3, 4), 1),
]

def canonical_reps():
    unseen = set(S.STATES)
    out = []
    while unseen:
        state = min(unseen)
        orbit = {g(state) for g in (S.identity, S.a, S.b, S.ab)}
        out.append((state, len(orbit)))
        unseen -= orbit
    return tuple(out)

TARGET_STATES = tuple(state for state, _ in canonical_reps())
TARGET_INDICES = tuple((((a * 3 + b) * 3 + c) * 3 + d) for a, b, c, d in TARGET_STATES)
EXPECTED_RANK_CENSUS = Counter({9: 4140, 8: 818, 7: 55, 6: 27})

def main():
    assert len(TARGET_STATES) == 24
    assert Counter(size for _, size in canonical_reps()) == Counter({4: 17, 2: 6, 1: 1})

    census = Counter()
    per_index_min = {}
    for index, ext in enumerate(B.oriented_exts(SUPPORT)):
        if index not in TARGET_INDICES:
            continue
        touched = tuple(sorted({b for e in ext for b, v in enumerate(B.QCOMP[e]) if v != (0, 0)}))
        touched_mask = sum(1 << b for b in touched)
        assert len(touched) == 10
        assert B.h_rank(touched_mask) == 6

        minimum = None
        for six in combinations(touched, 6):
            W = ()
            for b in six:
                W = B.union_key(W, B.empty_key(ext, b))
            r = len(W)
            census[r] += 1
            minimum = r if minimum is None else min(minimum, r)
            assert r >= 6
        per_index_min[index] = minimum

    assert len(per_index_min) == 24
    assert set(per_index_min.values()) == {6}
    assert census == EXPECTED_RANK_CENSUS, census
    assert sum(census.values()) == 24 * 210

    print('target_indices', TARGET_INDICES)
    print('six_empty_span_rank_census', dict(sorted(census.items())))
    print('PASS: every six empty-block spaces span rank at least 6')

if __name__ == '__main__':
    main()
