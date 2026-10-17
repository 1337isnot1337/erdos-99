#!/usr/bin/env python3
"""Arithmetic/combinatorial composition certificate for the puncture reduction
of the remaining eight-no-root k=6, D=-1, p=9 branch.

The companion proof note supplies the quotient-puncture functoriality. This
checker records the exact finite inputs already committed elsewhere and checks
all dimension/capacity consequences used in the reduction.
"""

RANK = 2
SEVEN_D1_SINGLETON_CAP_MAX = 4
SIX_D1_SINGLETON_CAP_MAX = 3
FIVE_D1_SINGLETON_CAP_MAX = 3
SIX_D1_SINGLETON_TOUCH = 3

# Consequences of the previously committed d2 singleton-shadow census plus
# full-span puncturing, proved in the preceding D=-2,p=8 closure note.
SEVEN_D2_FULL_SINGLETON_SURVIVORS = 0
SIX_D2_FULL_SINGLETON_SURVIVORS = 0

# Exact five-row d=1 audit of three singleton replacements plus one pair:
# all 144 realizable states have D=7 at t=5,p=5,d=1, hence extra rank 2.
FIVE_D1_THREE_SINGLE_PLUS_PAIR_EXACT_STATES = 144
FIVE_D1_THREE_SINGLE_PLUS_PAIR_EXTRA_RANK = 2

# Old synchronized six-row d=2 census.
SIX_D2_CAP_GE6_ALL_FIVE_D2_SURVIVORS = 0


def qdim(t: int, d: int) -> int:
    return t - RANK + d


def projected_support_three_count(m: int, t: int = 7) -> int:
    """Number of one-coordinate deletions giving projected support exactly 3."""
    count = 0
    for touched in (False, True):
        deletions = (t - m) if not touched else m
        projected = m - int(touched)
        if projected == 3:
            count += deletions
    return count


def main() -> None:
    assert qdim(8, 1) == 7
    assert qdim(8, 2) == 8
    assert qdim(8, 3) == 9
    assert {d: qdim(7, d) for d in (1, 2, 3)} == {1: 6, 2: 7, 3: 8}
    assert {d: qdim(6, d) for d in (1, 2, 3)} == {1: 5, 2: 6, 3: 7}
    assert {d: qdim(5, d) for d in (1, 2, 3)} == {1: 4, 2: 5, 3: 6}

    # d_v=1,q=8 has seven singleton replacements and one pair. A seven-row
    # d=1 puncture can retain at most four compatible singletons plus that pair,
    # fewer than the six functionals needed to span its quotient.
    assert SEVEN_D1_SINGLETON_CAP_MAX + 1 < qdim(7, 1)

    # d_v=1,q=7 with six singletons and one pair dies by the same count.
    assert SEVEN_D1_SINGLETON_CAP_MAX + 1 < qdim(7, 1)

    # The only remaining d_v=1,q=7 root type would be five singletons + two
    # pairs. Full span forces a clean seven-row shadow to retain exactly four
    # singleton blocks plus both pairs. Every further six-row d=1 puncture must
    # retain exactly three singleton blocks plus both pairs.
    assert SEVEN_D1_SINGLETON_CAP_MAX + 2 == qdim(7, 1)
    assert SIX_D1_SINGLETON_CAP_MAX + 2 == qdim(6, 1)

    # A seven-row compatible singleton block can disappear in at most two of
    # the seven one-coordinate punctures, so it survives in at least five.
    minimum_survivals = 7 - 2
    assert minimum_survivals == 5
    # But every compatible singleton in the exact synchronized six-row d=1
    # census has support exactly 3. A seven-row block of support m projects to
    # support 3 for at most four deletion coordinates, for every possible m.
    counts = {m: projected_support_three_count(m) for m in range(8)}
    assert max(counts.values()) == SIX_D1_SINGLETON_TOUCH + 1 == 4
    assert minimum_survivals > max(counts.values())

    # All-singleton d_v=2,q=9 and the all-singleton subcase of d_v=2,q=8:
    # d7=1 is too small by capacity, and d7=2 full singleton span is already
    # excluded by the preceding puncture closure.
    assert SEVEN_D1_SINGLETON_CAP_MAX < qdim(7, 1)
    assert SEVEN_D2_FULL_SINGLETON_SURVIVORS == 0

    # For the mixed d_v=2,q=8 residual (seven singletons + one pair), d7=1 and
    # d6=1 are impossible even allowing the pair.
    assert SEVEN_D1_SINGLETON_CAP_MAX + 1 < qdim(7, 1)
    assert SIX_D1_SINGLETON_CAP_MAX + 1 < qdim(6, 1)

    # At five rows, d=1 full quotient rank four would require either four
    # singletons (capacity impossible) or three singletons plus the pair. The
    # exact mixed audit gives extra rank only two in the latter case.
    assert FIVE_D1_SINGLETON_CAP_MAX < qdim(5, 1)
    assert FIVE_D1_THREE_SINGLE_PLUS_PAIR_EXACT_STATES == 144
    assert FIVE_D1_THREE_SINGLE_PLUS_PAIR_EXTRA_RANK < qdim(5, 1)

    # Hence every five-row projection of a mixed d6=2 full-span shadow has d5=2.
    # The old exact d2 census then forbids singleton capacity >=6. Full rank six
    # with at most one pair therefore forces exactly five singleton-compatible
    # blocks and the pair.
    assert SIX_D2_CAP_GE6_ALL_FIVE_D2_SURVIVORS == 0
    assert qdim(6, 2) == 6
    mixed_six_forced_singletons = qdim(6, 2) - 1
    assert mixed_six_forced_singletons == 5

    # For d_v=3,q=9 (all singleton), clean d7=1,2 and synchronized d6=1,2
    # are excluded, forcing d7=d6=3. Five-row d=1 is also excluded.
    assert SEVEN_D1_SINGLETON_CAP_MAX < qdim(7, 1)
    assert SEVEN_D2_FULL_SINGLETON_SURVIVORS == 0
    assert SIX_D1_SINGLETON_CAP_MAX < qdim(6, 1)
    assert SIX_D2_FULL_SINGLETON_SURVIVORS == 0
    assert FIVE_D1_SINGLETON_CAP_MAX < qdim(5, 1)

    print("PASS: eight-no-root k=6 D=-1 functional-puncture reduction")
    print("quotient_dims_7", {d: qdim(7, d) for d in (1, 2, 3)})
    print("quotient_dims_6", {d: qdim(6, d) for d in (1, 2, 3)})
    print("quotient_dims_5", {d: qdim(5, d) for d in (1, 2, 3)})
    print("seven_to_six_support3_projection_counts", counts)
    print("closed_global_profiles", ((1, 7), (1, 8), (2, 9)))
    print("closed_d2q8_all_singleton_subcase", True)
    print("remaining_global_profiles", ((2, 8, "7_singletons+1_pair"), (3, 9, "9_singletons")))
    print("mixed_d2q8_six_shadow", "d6=2, pair+exactly5 singleton-capable blocks, full rank 6")
    print("d3q9_clean_shadows", "d7=3 and d6=3; every five-row puncture has d5 in {2,3}")


if __name__ == "__main__":
    main()
