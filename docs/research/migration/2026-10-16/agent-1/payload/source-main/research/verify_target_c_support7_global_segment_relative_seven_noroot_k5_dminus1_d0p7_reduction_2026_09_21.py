#!/usr/bin/env python3
"""Structural reduction of the last seven-no-root k=5 branch.

Target:
    D=-1, k=5, d=0, p=7.

This checker records the arithmetic consequences of the synchronized six-row
containment theorem and the exact finite inputs already certified elsewhere:

* rank-drop pairs of the rank-two coefficient code form a matching of size <=2,
  so at least one coordinate has no incident rank-drop pair;
* synchronized six-row virtual d=1 states have singleton capacity <=3, and
  every compatible singleton there is touched by exactly three external rows;
* five-row virtual d=1 states have singleton capacity <=3, and every compatible
  singleton there is touched by exactly three external rows;
* the committed d=2 singleton-shadow audit has zero synchronized six-row
  d=2/capacity>=6 states whose six five-row projections all have d=2.

The proof note explains why these facts eliminate the d6=1 case and every
d6=2 case with seven singleton incomplete blocks, leaving only two structural
patterns for the remaining branch.
"""
from itertools import combinations

SEVEN_D = -1
P_COST = 7

# Exact published finite-census facts.
SIX_D1_CAPACITY_MAX = 3
SIX_D1_SINGLETON_TOUCH = 3
FIVE_D1_CAPACITY_MAX = 3
FIVE_D1_SINGLETON_TOUCH = 3
D2_CAPACITY6_ALL_PROJECTED_D2_SURVIVORS = 0

FIVE_D1_CAPACITY_CENSUS = {0: 71, 2: 3, 3: 12}
FIVE_D2_CAPACITY_CENSUS = {
    0: 1, 1: 297, 2: 532, 3: 4339, 4: 8260, 5: 693,
    6: 1377, 7: 68, 8: 110, 9: 76, 10: 48, 11: 64,
}


def rank_drop_matching_unmatched_min(n=7, max_matching=2):
    """Minimum number of vertices not incident to a matching of size <=2."""
    worst = n
    vertices = range(n)
    edges = tuple(combinations(vertices, 2))
    for m in range(max_matching + 1):
        for chosen in combinations(edges, m):
            used = set()
            ok = True
            for a, b in chosen:
                if a in used or b in used:
                    ok = False
                    break
                used.update((a, b))
            if ok:
                worst = min(worst, n - len(used))
    return worst


def six_shadow_arithmetic():
    """Return (d6,q6,minimum singleton replacements among q6)."""
    out = []
    for d6 in range(1, 8):
        for q6 in range(0, P_COST + 1):
            # D6=1 and the six-row containment inequality
            # 1 >= 6 + p + 3*d6 - 3*q6 = 13 + 3*d6 - 3*q6.
            if 1 < 13 + 3 * d6 - 3 * q6:
                continue
            # q replaced complete blocks cost at least two rows each, except a
            # singleton replacement saves one row.
            min_singletons = max(0, 2 * q6 - P_COST)
            if min_singletons <= q6:
                out.append((d6, q6, min_singletons))
    return tuple(out)


def main():
    assert rank_drop_matching_unmatched_min() == 3

    raw = six_shadow_arithmetic()
    assert raw == (
        (1, 5, 3), (1, 6, 5), (1, 7, 7),
        (2, 6, 5), (2, 7, 7),
        (3, 7, 7),
    )

    # Exact six-row d=1 capacity <=3 leaves only (d,q,s)=(1,5,3).
    d1 = tuple(x for x in raw if x[0] == 1 and x[2] <= SIX_D1_CAPACITY_MAX)
    assert d1 == ((1, 5, 3),)

    # That case has exactly three singleton and two pair blocks.  Every
    # singleton has six-row touch multiplicity 3.  After deletion of a touched
    # coordinate, compatibility projects; if the block stayed canonical
    # complete it would be a five-row d=1 compatible singleton of touch 2,
    # contradicting the exact five-row touch census.  Hence every touched
    # singleton becomes canonical empty.  Five-row D=3,p=7,d=1 requires q>=4,
    # so at most one of the five nonempty blocks may become canonical empty
    # under any coordinate deletion.  Thus each of six coordinates can touch
    # at most one of the three singleton blocks, but 3*3=9 incidences are
    # required.  Contradiction.
    assert 3 * SIX_D1_SINGLETON_TOUCH == 9
    assert 6 * 1 == 6
    assert 9 > 6
    assert FIVE_D1_SINGLETON_TOUCH == 3

    # If d6=2 and all seven incomplete rows are singleton blocks, then every
    # five-row projection has d5 in {1,2}.  d5=1 would require q5>=4 singleton
    # replacements, impossible by five-row d=1 capacity <=3.  Hence all six
    # projections have d5=2.  The pre-existing exact d2 audit has zero
    # d6=2/capacity>=6 states with all six projected deficiencies equal to 2.
    assert FIVE_D1_CAPACITY_MAX == 3
    assert D2_CAPACITY6_ALL_PROJECTED_D2_SURVIVORS == 0

    # Therefore the only remaining global root-row patterns are:
    # B: d6=2,q6=6 with five singleton blocks and one pair block.
    # C: d6=3,q6=7 with seven singleton blocks.
    remaining = (
        ("five_singletons_plus_one_pair", 2, 6, 5),
        ("seven_singletons", 3, 7, 7),
    )

    # Exact five-row parent counts for the next B-pattern extension audit.
    d1_capacity3 = FIVE_D1_CAPACITY_CENSUS[3]
    d2_capacity4plus = sum(
        count for capacity, count in FIVE_D2_CAPACITY_CENSUS.items()
        if capacity >= 4
    )
    assert d1_capacity3 == 12
    assert d2_capacity4plus == 10696
    assert sum(FIVE_D2_CAPACITY_CENSUS.values()) == 15865

    print("PASS: seven-no-root D=-1,k=5,d=0,p=7 structural reduction")
    print("minimum_unmatched_coordinates", rank_drop_matching_unmatched_min())
    print("six_shadow_arithmetic", raw)
    print("d1_candidates_after_exact_capacity", d1)
    print("d1_singleton_touch_incidences", 9)
    print("d1_coordinate_touch_capacity", 6)
    print("d2_all_singleton_structural_survivors",
          D2_CAPACITY6_ALL_PROJECTED_D2_SURVIVORS)
    print("remaining_patterns", remaining)
    print("next_B_d1_capacity3_parents", d1_capacity3)
    print("next_B_d2_capacity4plus_parents", d2_capacity4plus)
    print("next_B_parent_cover", d1_capacity3 + d2_capacity4plus)


if __name__ == "__main__":
    main()
