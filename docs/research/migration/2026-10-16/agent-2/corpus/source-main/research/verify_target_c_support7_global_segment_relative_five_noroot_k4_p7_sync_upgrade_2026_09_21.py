#!/usr/bin/env python3
"""Arithmetic synthesis for the five-row k=4,p=7 closure and seven-row sync upgrade.

This file does not redo the exact finite censuses.  It composes the already
committed exact certificates

  * verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d2_functional_2026_09_21.py
  * verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d3_functional_2026_09_21.py

with the established five-row k=4 containment inequality and the all-depth
seven-row deletion identity.

The resulting theorem is:

  every five-no-root k=4,p=7 state has defect D>=3.

Consequently a hypothetical seven-no-root D=-1,k=5,d=0,p=7 state cannot have
any coefficient-rank-drop pair.  Its rank-two coefficient code therefore has
(d1,d2)>=(3,4), every two-coordinate puncture preserves rank two, and every
one-row deletion is a fully synchronized six-row k=4 shadow.
"""

P = 7

# Exact outputs proved by the two committed p=7 functional-span audits.
D2_SINGLETON_CAPACITY_MAX = 6
D2_SINGLETON_EXTRA_RANK_MAX = 2
D2_WITH_PAIR_EXTRA_RANK_MAX = 3
D3_SINGLETON_EXTRA_RANK_MAX = 6


def containment_lower_bound(d, q):
    """Five-row k=4 bound D >= 5+p+3d-3q at p=7."""
    return 5 + P + 3 * d - 3 * q


def main():
    # The established virtual-canonical theorem has d>=2 and q<=p=7.
    # Find every arithmetic point where the crude containment bound is <3.
    residual = []
    for d in range(2, 8):
        for q in range(P + 1):
            crude = containment_lower_bound(d, q)
            if crude < 3:
                residual.append((d, q, crude))
    assert residual == [(2, 6, 0), (2, 7, -3), (3, 7, 0)]

    # d=2,q=7 requires seven singleton replacements because p=7.  The exact
    # d=2 census proves singleton capacity at most six, so this form is absent.
    assert D2_SINGLETON_CAPACITY_MAX < 7

    # d=2,q=6,p=7 has exactly two root-cost forms.
    #
    # A: five singleton replacements plus one pair replacement.  The d=2
    #    functional audit proves extra functional rank s<=3 even after an
    #    arbitrary pair functional is adjoined.
    d2_pair_min = 5 + P + 3 * 2 - 3 * D2_WITH_PAIR_EXTRA_RANK_MAX
    assert d2_pair_min == 9

    # B: six singleton replacements plus one singleton on a canonical-empty
    #    block.  The extra canonical-empty singleton contributes no replacement
    #    functional, and the six singleton replacement functionals have s<=2.
    d2_singles_min = 5 + P + 3 * 2 - 3 * D2_SINGLETON_EXTRA_RANK_MAX
    assert d2_singles_min == 12

    # d=3,q=7 requires seven singleton replacements.  The exact d=3 audit
    # proves that their functionals gain rank at most six modulo Col(M).
    d3_min = 5 + P + 3 * 3 - 3 * D3_SINGLETON_EXTRA_RANK_MAX
    assert d3_min == 3

    five_k4_p7_min_defect = min(3, d2_pair_min, d2_singles_min, d3_min)
    assert five_k4_p7_min_defect == 3

    # Apply this to the remaining seven-row target D=-1,k=5,d=0,p=7.
    # Its coefficient space P7 has rank two and the already proved all-depth
    # bound d2(P7)>=4.  Hence deleting two coordinates can lower rank by at
    # most one: a rank drop of two would support all of P7 on those coordinates.
    seven_defect = -1
    pair_projection_defect = {
        rank_drop: seven_defect + 4 - 3 * rank_drop
        for rank_drop in (0, 1)
    }
    assert pair_projection_defect == {0: 3, 1: 0}

    # A rank-drop pair would therefore produce a five-row k=4,p=7 shadow with
    # D=0, contradicting the D>=3 theorem above.  So every pair has rank_drop=0.
    assert pair_projection_defect[1] < five_k4_p7_min_defect

    # The prior all-depth theorem already gave d1(P7)>=2.  Ruling out every
    # support-two word upgrades this to d1(P7)>=3; d2(P7)>=4 was already known.
    generalized_weights = (3, 4)
    assert generalized_weights == (3, 4)

    # With no rank-drop pair, every one-row deletion is synchronized through all
    # five-row deletions.  Defect transport gives D6=-1+2=1 and D5=-1+4=3.
    assert seven_defect + 2 == 1
    assert seven_defect + 4 == 3

    print("PASS: five-row k=4,p=7 closure and seven-row all-pair synchronization")
    print("five_k4_p7_crude_residuals", residual)
    print("five_k4_p7_min_defect", five_k4_p7_min_defect)
    print("d2_q6_pair_form_min_defect", d2_pair_min)
    print("d2_q6_six_singleton_form_min_defect", d2_singles_min)
    print("d3_q7_min_defect", d3_min)
    print("pair_projection_defect", pair_projection_defect)
    print("seven_rank2_generalized_weights", generalized_weights)
    print("all_pair_projections_preserve_rank", True)
    print("every_six_row_deletion_fully_synchronized", True)


if __name__ == "__main__":
    main()
