#!/usr/bin/env python3
"""Exact arithmetic certificate for the generic-H6 reflection-closure bound.

The 14,174-cell generic-H6 interior-force universe is invariant under the hull
reflection 0->0, 1<->5, 2<->4, 3->3, 6->6, 7->7.  At ground vertex 0 this
reverses the seven-entry radial order, so a positive-position pattern P maps to
{8-p : p in P}.  Comparing the exact symmetric universe census with the current
4,805-cell survivor census gives a lower bound on exclusions forced by closing
the current exact exclusion set under reflection.

No floating point arithmetic or optimization is used.
"""

from collections import Counter

UNIVERSE_PATTERN = Counter({
    "145": 144,
    "156": 108,
    "235": 1770,
    "236": 3630,
    "237": 108,
    "245": 1390,
    "256": 3630,
    "345": 90,
    "346": 1390,
    "347": 144,
    "356": 1770,
})

CURRENT_PATTERN = Counter({
    "145": 4,
    "156": 16,
    "235": 654,
    "236": 1278,
    "237": 16,
    "245": 474,
    "256": 1204,
    "345": 21,
    "346": 479,
    "347": 4,
    "356": 655,
})

FACE_REFLECTION = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1, 6: 6, 7: 7}


def reflect_pattern(pattern: str) -> str:
    return "".join(sorted(str(8 - int(c)) for c in pattern))


def main() -> None:
    assert sum(UNIVERSE_PATTERN.values()) == 14174
    assert sum(CURRENT_PATTERN.values()) == 4805
    assert set(UNIVERSE_PATTERN) == set(CURRENT_PATTERN)
    assert all(CURRENT_PATTERN[p] <= UNIVERSE_PATTERN[p] for p in UNIVERSE_PATTERN)

    # The exact generic-H6 universe census is invariant under reflection.
    for p in UNIVERSE_PATTERN:
        rp = reflect_pattern(p)
        assert rp in UNIVERSE_PATTERN
        assert reflect_pattern(rp) == p
        assert UNIVERSE_PATTERN[p] == UNIVERSE_PATTERN[rp]

    # The fixed recent face pair (2,3) reflects to unordered pair (3,4).
    assert {FACE_REFLECTION[2], FACE_REFLECTION[3]} == {3, 4}

    excluded = UNIVERSE_PATTERN - CURRENT_PATTERN
    assert sum(excluded.values()) == 14174 - 4805 == 9369

    seen = set()
    forced_new = 0
    rows = []
    for p in sorted(UNIVERSE_PATTERN):
        if p in seen:
            continue
        rp = reflect_pattern(p)
        seen.add(p)
        seen.add(rp)
        if p == rp:
            continue

        # Because the universe has the same cardinality on both sides,
        # |excluded[p]-excluded[rp]| equals |survivors[p]-survivors[rp]|.
        ep = excluded[p]
        er = excluded[rp]
        extra = abs(ep - er)
        assert extra == abs(CURRENT_PATTERN[p] - CURRENT_PATTERN[rp])
        forced_new += extra
        rows.append((p, rp, CURRENT_PATTERN[p], CURRENT_PATTERN[rp], ep, er, extra))

    assert rows == [
        ("145", "347", 4, 4, 140, 140, 0),
        ("156", "237", 16, 16, 92, 92, 0),
        ("235", "356", 654, 655, 1116, 1115, 1),
        ("236", "256", 1278, 1204, 2352, 2426, 74),
        ("245", "346", 474, 479, 916, 911, 5),
    ]
    assert forced_new == 80

    survivor_upper = 4805 - forced_new
    assert survivor_upper == 4725

    print("PASS")
    print("generic-H6 universe: 14174")
    print("current certified survivors: 4805")
    print("additional exclusions forced by reflection closure: >= 80")
    print("reflection-closed survivor upper bound: <= 4725")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
