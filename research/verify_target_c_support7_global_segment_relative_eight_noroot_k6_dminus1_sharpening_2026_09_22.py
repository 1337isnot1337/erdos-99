#!/usr/bin/env python3
"""Arithmetic/support certificate for the eight-no-root k=6, D=-1 sharpening.

The proof note combines this arithmetic with already-certified exact inputs:

* every compatible singleton in a synchronized six-row rank-two d=1 state
  has touch support exactly 3, and six-row d=1 singleton capacity is <=3;
* repaired five-row rank-two d=1 singleton capacity is <=3;
* the synchronized six-row d=2, singleton-capacity>=6 audit has zero states
  whose six five-row projections all have d=2.

This checker records the support contradiction that improves the seven-row
rank-two d=1 capacity bound from <=4 to 0 and the containment thresholds used
for the remaining D=-1,p=9 profiles.
"""

from math import ceil

SIX_D1_CAPACITY_MAX = 3
FIVE_D1_CAPACITY_MAX = 3
SIX_D1_SINGLETON_TOUCH_SUPPORT = 3
SIX_D2_CAP6_ALL_FIVE_D2_SURVIVORS = 0


def q_required(D: int, t: int, p: int, d: int) -> int:
    return ceil((t + p + 3 * d - D) / 3)


def projected_support_hits(m: int) -> int:
    """Number of 1-deletions of a 7-set leaving support size exactly 3."""
    return (m if m - 1 == 3 else 0) + ((7 - m) if m == 3 else 0)


def main() -> None:
    # Lemma: a seven-row singleton-capable d=1 block survives in at least five
    # six-row deletions, but the exact six-row d=1 support census requires
    # projected support exactly 3.  No 7-row touch support can provide this in
    # five deletions.
    counts = {m: projected_support_hits(m) for m in range(8)}
    assert counts == {0: 0, 1: 0, 2: 0, 3: 4, 4: 4, 5: 0, 6: 0, 7: 0}
    assert max(counts.values()) == 4 < 5

    # Clean deletions in the D=-1,p=9 branch preserve coefficient rank.
    D8, p = -1, 9
    D7, D6, D5 = D8 + 2, D8 + 4, D8 + 6
    assert (D7, D6, D5) == (1, 3, 5)

    q7 = {d: q_required(D7, 7, p, d) for d in (1, 2, 3)}
    q6 = {d: q_required(D6, 6, p, d) for d in (1, 2, 3)}
    q5 = {d: q_required(D5, 5, p, d) for d in (1, 2, 3)}
    assert q7 == {1: 6, 2: 7, 3: 8}
    assert q6 == {1: 5, 2: 6, 3: 7}
    assert q5 == {1: 4, 2: 5, 3: 6}

    # In an all-singleton changed-block profile, d6=1 and d5=1 are impossible.
    assert q6[1] > SIX_D1_CAPACITY_MAX
    assert q5[1] > FIVE_D1_CAPACITY_MAX

    # Hence a d=2 clean chain has six-row singleton capacity >=6 and all six
    # five-row projections d=2, exactly the committed zero-survivor class.
    assert q6[2] == 6
    assert q5[2] == 5
    assert SIX_D2_CAP6_ALL_FIVE_D2_SURVIVORS == 0

    print("PASS: eight-no-root k=6 D=-1 sharpening arithmetic")
    print("seven_d1_projected_support3_counts", counts)
    print("seven_d1_required_survivals", 5)
    print("clean_shadow_defects", (D7, D6, D5))
    print("q7_thresholds", q7)
    print("q6_thresholds", q6)
    print("q5_thresholds", q5)
    print("six_d1_capacity_max", SIX_D1_CAPACITY_MAX)
    print("five_d1_capacity_max", FIVE_D1_CAPACITY_MAX)
    print("six_d2_cap6_all_five_d2_survivors", SIX_D2_CAP6_ALL_FIVE_D2_SURVIVORS)


if __name__ == "__main__":
    main()
