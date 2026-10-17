#!/usr/bin/env python3
"""Arithmetic regression guard for the Profile B weight-three closure.

The proof uses the unstripped replacement-functional accounting already proved
for the eight-no-root k=6 reduction.  Deleting the support of a weight-three
coefficient word lowers coefficient rank from two to one, but it does not
remove any selected incomplete-root rows.  Thus the five-row child still has
p=9.

The exact five-row functional inputs are certified by:

* verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d2_functional_2026_09_21.py
* verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d3_functional_2026_09_21.py

This script only checks the arithmetic composition.  It does not re-run those
finite censuses.
"""

from math import ceil

SOURCE_DEFECT = -1
SOURCE_P = 9
DELETED_WEIGHT = 3
COEFFICIENT_RANK_LOSS = 1
CHILD_T = 5

# Exact committed finite-census bounds for the relevant five-row rank-one
# virtual-canonical states.
D2_CAPACITY_THRESHOLD = 5
D2_SINGLETON_EXTRA_RANK_MAX = 2
D3_CAPACITY_THRESHOLD = 7
D3_SINGLETON_EXTRA_RANK_MAX = 6


def transported_defect():
    # Exact no-root deletion transport: +2 per deleted row and -3 per lost
    # coefficient-space rank.
    return SOURCE_DEFECT + 2 * DELETED_WEIGHT - 3 * COEFFICIENT_RANK_LOSS


def required_extra_rank(deficiency):
    # D >= t + p + 3d - 3s.
    numerator = CHILD_T + SOURCE_P + 3 * deficiency - transported_defect()
    return ceil(numerator / 3)


def main():
    assert transported_defect() == 2

    need_d2 = required_extra_rank(2)
    need_d3 = required_extra_rank(3)
    assert (need_d2, need_d3) == (6, 7)

    # s>=6 already implies singleton capacity >=6, so the exact d=2 census at
    # capacity >=5 applies and gives s<=2.
    assert need_d2 >= D2_CAPACITY_THRESHOLD
    assert D2_SINGLETON_EXTRA_RANK_MAX < need_d2

    # s>=7 implies capacity >=7, so the exact d=3 census applies and gives
    # s<=6.
    assert need_d3 >= D3_CAPACITY_THRESHOLD
    assert D3_SINGLETON_EXTRA_RANK_MAX < need_d3

    print("PASS: Profile B weight-three unstripped composition")
    print("five_row_defect", transported_defect())
    print("required_extra_rank_d2", need_d2)
    print("certified_extra_rank_max_d2", D2_SINGLETON_EXTRA_RANK_MAX)
    print("required_extra_rank_d3", need_d3)
    print("certified_extra_rank_max_d3", D3_SINGLETON_EXTRA_RANK_MAX)
    print("consequence", "d1(P)>=4")
    print("three_clean_source_coordinates", 8)


if __name__ == "__main__":
    main()
