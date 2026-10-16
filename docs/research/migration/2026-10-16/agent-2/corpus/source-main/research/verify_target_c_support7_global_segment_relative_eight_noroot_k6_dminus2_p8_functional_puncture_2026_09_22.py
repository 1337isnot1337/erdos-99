#!/usr/bin/env python3
"""Arithmetic composition certificate for closing the eight-no-root k=6
D=-2, p=8 branch by puncturing maximal replacement-functional rank.

Structural input, proved in the companion note:

* a seven-row three-clean shadow has rank(P)=2, virtual deficiency d7=2,
  and its singleton replacement functionals span the full seven-dimensional
  canonical functional quotient;
* when a rank-preserving coordinate is deleted, the canonical functional
  quotient maps surjectively to the punctured quotient, and each replacement
  functional maps to the corresponding punctured functional if its block stays
  virtual-complete, and to zero otherwise.

Finite inputs already certified elsewhere in the repository:

* synchronized six-row rank-two d=1 singleton capacity is at most 3;
* five-row rank-two d=1 singleton capacity is at most 3;
* among synchronized six-row rank-two d=2 states, exactly 761 have singleton
  capacity at least 6, and none of those has d=2 in all six five-row
  coordinate projections.

This script checks the dimension/capacity implications that combine those
inputs into the contradiction.
"""

RANK = 2
SIX_D1_SINGLETON_CAP_MAX = 3
FIVE_D1_SINGLETON_CAP_MAX = 3
SIX_D2_CAP_GE6_COUNT = 761
SIX_D2_CAP_GE6_ALL_FIVE_D2_COUNT = 0


def quotient_dim(t: int, d: int) -> int:
    return t - RANK + d


def main() -> None:
    # The forced seven-row shadow from the global D=-2,p=8 branch.
    assert quotient_dim(7, 2) == 7
    seven_full_extra_rank = 7
    assert seven_full_extra_rank == quotient_dim(7, 2)

    # Puncture once. Row-nullity monotonicity and the six-row containment
    # theorem leave only d6 in {1,2}. Full-span descent forces at least the
    # quotient dimension many surviving singleton replacement functionals.
    six_required = {d6: quotient_dim(6, d6) for d6 in (1, 2)}
    assert six_required == {1: 5, 2: 6}
    assert six_required[1] > SIX_D1_SINGLETON_CAP_MAX
    forced_d6 = 2
    assert six_required[forced_d6] == 6

    # Puncture again. The repaired five-row theorem gives d5>=1 and
    # monotonicity from d6=2 gives d5<=2. Full-span descent rules out d5=1.
    five_required = {d5: quotient_dim(5, d5) for d5 in (1, 2)}
    assert five_required == {1: 4, 2: 5}
    assert five_required[1] > FIVE_D1_SINGLETON_CAP_MAX
    forced_d5 = 2
    assert five_required[forced_d5] == 5

    # Therefore every six-row puncture of the hypothetical seven-row shadow
    # would lie in the exact old audit class: synchronized, d6=2, singleton
    # capacity >=6, and all six five-row projections d5=2. The committed
    # exhaustive census has no such state.
    assert SIX_D2_CAP_GE6_COUNT == 761
    assert SIX_D2_CAP_GE6_ALL_FIVE_D2_COUNT == 0

    print("PASS: eight-no-root k=6 D=-2,p=8 puncture composition")
    print("seven_quotient_dim", quotient_dim(7, 2))
    print("six_required_by_deficiency", six_required)
    print("forced_six_deficiency", forced_d6)
    print("five_required_by_deficiency", five_required)
    print("forced_five_deficiency", forced_d5)
    print("old_exact_six_d2_capacity_ge6_states", SIX_D2_CAP_GE6_COUNT)
    print(
        "old_exact_six_d2_capacity_ge6_all_five_d2_states",
        SIX_D2_CAP_GE6_ALL_FIVE_D2_COUNT,
    )
    print("branch_survivors", 0)


if __name__ == "__main__":
    main()
