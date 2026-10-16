#!/usr/bin/env python3
"""Check the scalar constants in the proof-only half-disk remainder lemma.

This certifies only the elementary asymptotic constant and sign arithmetic. It
does not certify the geometric half-disk decomposition or C-II.
"""

from __future__ import annotations

from math import pi, sqrt


def main() -> None:
    half_disk_area = pi / 8.0
    group_floor = sqrt(pi * half_disk_area)
    two_group_floor = 2.0 * group_floor
    chi_floor = two_group_floor - pi

    print(f"group_floor={group_floor:.15f}")
    print(f"moment_remainder_floor={two_group_floor:.15f}")
    print(f"chi_floor={chi_floor:.15f}")

    assert abs(group_floor - pi / (2.0 * sqrt(2.0))) < 1.0e-14
    assert abs(two_group_floor - pi / sqrt(2.0)) < 1.0e-14
    assert abs(chi_floor + pi * (1.0 - 1.0 / sqrt(2.0))) < 1.0e-14
    assert -0.921 < chi_floor < -0.920

    print("Section 173 arithmetic checks: PASS")


if __name__ == "__main__":
    main()
