#!/usr/bin/env python3
"""Arithmetic composition certificate for the eight-no-root k=6, D=-2 branch.

This script does not repeat the heavy six-row census.  It checks the exact
thresholds used to compose three already-certified repository inputs:

* synchronized six-row rank-two d=1 singleton capacity <= 3;
* repaired five-row rank-two d=1 singleton capacity <= 3;
* among synchronized six-row rank-two d=2 states of singleton capacity >= 6,
  no state has all six coordinate projections of virtual deficiency d=2.

The companion proof note supplies the deletion/lifting argument that reduces a
hypothetical eight-row D=-2,k=6,p=8 counterexample to precisely the impossible
six-row class in the third item.
"""

from math import ceil

SIX_D1_SINGLETON_CAPACITY_MAX = 3
FIVE_D1_SINGLETON_CAPACITY_MAX = 3
SIX_D2_CAP6_ALL_FIVE_D2_SURVIVORS = 0


def q_required(D: int, t: int, p: int, d: int) -> int:
    """Least integer q allowed by D >= t+p+3d-3q."""
    return ceil((t + p + 3 * d - D) / 3)


def main() -> None:
    # Start from the already-forced global branch
    # D8=-2, p=8, d_v=2, q=8, eight singleton changed blocks.
    # A three-clean coordinate makes every deletion set of size <=3 that
    # contains it coefficient-rank preserving.
    D8, p = -2, 8
    D7 = D8 + 2
    D6 = D8 + 4
    D5 = D8 + 6
    assert (D7, D6, D5) == (0, 2, 4)

    # In each synchronized six-row double-deletion shadow, monotonicity gives
    # d6 <= 2 and the six-row containment theorem gives d6 >= 1.
    q6_if_d1 = q_required(D6, 6, p, 1)
    assert q6_if_d1 == 5
    assert q6_if_d1 > SIX_D1_SINGLETON_CAPACITY_MAX

    # Therefore d6=2, where containment forces at least six singleton-capable
    # virtual-complete blocks.
    q6_if_d2 = q_required(D6, 6, p, 2)
    assert q6_if_d2 == 6

    # Every one-coordinate projection of that six-row shadow is a five-row
    # rank-two state with d5 in {1,2}.  The d5=1 option needs four singleton
    # replacements, above the certified capacity maximum 3.
    q5_if_d1 = q_required(D5, 5, p, 1)
    assert q5_if_d1 == 4
    assert q5_if_d1 > FIVE_D1_SINGLETON_CAPACITY_MAX

    q5_if_d2 = q_required(D5, 5, p, 2)
    assert q5_if_d2 == 5

    # Hence all six five-row projections have d5=2 and singleton capacity at
    # least five, exactly the parent class used by the committed d6=2 audit.
    # The exact committed synchronized d6=2 audit has zero such capacity>=6
    # states.
    assert SIX_D2_CAP6_ALL_FIVE_D2_SURVIVORS == 0

    print("PASS: eight-no-root k=6 D=-2 composition obstruction")
    print("defects_after_clean_deletions", (D7, D6, D5))
    print("six_row_d1_required_singletons", q6_if_d1)
    print("six_row_d1_capacity_max", SIX_D1_SINGLETON_CAPACITY_MAX)
    print("six_row_d2_required_singletons", q6_if_d2)
    print("five_row_d1_required_singletons", q5_if_d1)
    print("five_row_d1_capacity_max", FIVE_D1_SINGLETON_CAPACITY_MAX)
    print("five_row_d2_required_singletons", q5_if_d2)
    print(
        "six_d2_capacity6_all_five_d2_survivors",
        SIX_D2_CAP6_ALL_FIVE_D2_SURVIVORS,
    )


if __name__ == "__main__":
    main()
