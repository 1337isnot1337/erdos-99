#!/usr/bin/env python3
"""Guard against a coefficient-rank mismatch in the k=6 puncture reduction.

The eight-no-root k=6 branch has coefficient-constraint rank two.  Three-clean
puncturing preserves that rank, so its five-row shadows are five-no-root k=3
states.  The earlier composition incorrectly imported functional-span bounds
from five-no-root k=4 audits, whose coefficient-constraint space is a line.
Those bounds do not apply to the rank-two shadows.

A separate exact witness certificate now exhibits a rank-two five-row d=2
state where four singleton replacements plus one pair have full extra rank 5:

  verify_target_c_support7_global_segment_relative_five_noroot_k3_d2_mixed_fullrank_witness_2026_09_22.py

Accordingly this file no longer certifies the invalid Profile-A/Profile-B
five-row conclusions.  It records only the branch bookkeeping needed to avoid
reintroducing the mismatch.
"""

EIGHT_ROW_K = 6
EIGHT_ROW_COEFFICIENT_RANK = 8 - EIGHT_ROW_K
FIVE_SHADOW_ROWS = 5
FIVE_SHADOW_COEFFICIENT_RANK = EIGHT_ROW_COEFFICIENT_RANK
FIVE_SHADOW_K = FIVE_SHADOW_ROWS - FIVE_SHADOW_COEFFICIENT_RANK

FIVE_K4_AUDIT_COEFFICIENT_RANK = 1


def quotient_dimension(rows: int, deficiency: int, coefficient_rank: int) -> int:
    return rows - coefficient_rank + deficiency


def main():
    assert EIGHT_ROW_COEFFICIENT_RANK == 2
    assert FIVE_SHADOW_COEFFICIENT_RANK == 2
    assert FIVE_SHADOW_K == 3
    assert FIVE_K4_AUDIT_COEFFICIENT_RANK == 1
    assert FIVE_K4_AUDIT_COEFFICIENT_RANK != FIVE_SHADOW_COEFFICIENT_RANK

    assert quotient_dimension(5, 2, FIVE_SHADOW_COEFFICIENT_RANK) == 5
    assert quotient_dimension(5, 3, FIVE_SHADOW_COEFFICIENT_RANK) == 6

    print("PASS: k6 five-row shadows are rank-two k=3 states")
    print("five_shadow_coefficient_rank", FIVE_SHADOW_COEFFICIENT_RANK)
    print("five_shadow_k", FIVE_SHADOW_K)
    print("k4_audit_coefficient_rank", FIVE_K4_AUDIT_COEFFICIENT_RANK)
    print("k4_functional_bounds_applicable", False)


if __name__ == "__main__":
    main()
