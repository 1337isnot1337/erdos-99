"""Exact arithmetic for the two-half-disk global boundary-floor reduction.

The script checks the constants in the finite-to-asymptotic boundary calculation. It
does not certify the inherited geometric group decomposition, global optimality, or
C-II closure.
"""

from __future__ import annotations

from math import pi, sqrt


def main() -> None:
    gamma = pi * (4.0 - 2.0 * sqrt(3.0)) / 8.0
    two_group_floor = 4.0 + 2.0 * gamma
    assert 0.2104 < gamma < 0.2105
    assert 4.4208 < two_group_floor < 4.4210

    # The normalized global boundary inequality is
    # 2 t + 4 f >= 4 + 2 gamma.
    t = 2.0
    f = 0.85
    boundary_margin = 2.0 * t + 4.0 * f - two_group_floor
    assert boundary_margin > 0.0

    # A lower-density diagnostic branch makes the interface obligation visible.
    t_low = 1.8
    f_low = 0.1
    low_boundary_deficit = two_group_floor - 2.0 * t_low - 4.0 * f_low
    assert low_boundary_deficit > 0.0

    print(f"gamma={gamma:.15f}")
    print(f"two_group_boundary_floor={two_group_floor:.15f}")
    print(f"diagnostic_high_branch_boundary_margin={boundary_margin:.15f}")
    print(f"diagnostic_low_branch_boundary_deficit={low_boundary_deficit:.15f}")
    print("two-half-disk global boundary-floor arithmetic: OK")


if __name__ == "__main__":
    main()
