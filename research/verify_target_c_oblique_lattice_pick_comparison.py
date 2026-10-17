#!/usr/bin/env python3
"""Lightweight exact/algebraic checks for the oblique Pick comparison."""

from __future__ import annotations

import math


def check_threshold(D: float, theta: float) -> tuple[float, float, bool]:
    a0 = math.sqrt(3.0) / 2.0
    s = math.sin(theta)
    lhs = math.pi * D * D / 4.0 * (1.0 / a0 - 1.0 / s)
    rhs = math.pi * D / 2.0 + 1.0
    return lhs, rhs, lhs > rhs


def main() -> None:
    a0 = math.sqrt(3.0) / 2.0
    # The first two samples are fixed/mesoscopic shear and must be excluded.
    for D, delta in ((1000.0, 0.20), (1000.0, 0.01), (1000.0, 4.0 / 1000.0)):
        lhs, rhs, strict = check_threshold(D, math.pi / 3.0 + delta)
        print(
            f"D={D:.0f} delta={delta:.12g} lhs={lhs:.12f} "
            f"rhs={rhs:.12f} strict={strict}"
        )

    # Inverse-diameter shear should remain below the linear boundary cost.
    for D in (100.0, 1000.0, 10000.0):
        lhs, rhs, strict = check_threshold(D, math.pi / 3.0 + D ** -2)
        assert not strict
        print(
            f"vanishing D={D:.0f} lhs/rhs={lhs / rhs:.12g} "
            f"strict={strict}"
        )

    # Algebraic rearrangement of the uniform condition.
    D = 1000.0
    theta = math.pi / 3.0 + 4.0 / D
    s = math.sin(theta)
    rearranged = s - a0
    upper = 2.0 * a0 * s / D + 4.0 * a0 * s / (math.pi * D * D)
    assert rearranged > upper  # this sample is in the excluded regime
    print("PASS: oblique Pick comparison sanity checks")


if __name__ == "__main__":
    main()
