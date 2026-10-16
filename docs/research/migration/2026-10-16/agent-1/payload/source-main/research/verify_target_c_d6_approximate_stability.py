#!/usr/bin/env python3
"""Exact certificate for approximate sixfold affine-window stability.

The test windows have exact D6 symmetry, so their orbit defect is zero and
therefore also satisfies the declared defect E=1. Scaling the index window
makes the finite stability margin visible. This is a restricted affine-source
comparison, not a theorem about arbitrary global minimizers.
"""

from __future__ import annotations

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location


_SPEC = spec_from_file_location(
    "d6_exact", "research/verify_target_c_d6_affine_window_comparison.py"
)
if _SPEC is None or _SPEC.loader is None:
    raise RuntimeError("cannot load the exact D6 certificate")
_D6 = module_from_spec(_SPEC)
_SPEC.loader.exec_module(_D6)


def check_approximate_bound(points: set[tuple[int, int]], c: Fraction, E: int) -> None:
    differences = _D6.difference_set(points)
    de2 = max(_D6.qform(p, Fraction(1, 2)) for p in differences)
    # Exact squared form of ((1-2c)/3)de2 > 3E(2de+E).
    alpha = Fraction(1 - 2 * c, 3)
    left_after_constant = alpha * de2 - Fraction(3 * E * E)
    if left_after_constant <= 0:
        raise AssertionError("test margin is not positive")
    if left_after_constant * left_after_constant <= Fraction(36 * E * E) * de2:
        raise AssertionError("approximate-orbit margin failed")

    sheared = max(_D6.qform(p, c) for p in differences)
    equilateral = de2
    if not sheared > equilateral:
        raise AssertionError((c, E, sheared, equilateral))


def main() -> None:
    for R in (5, 10, 20, 40):
        points = _D6.orbit_window(((R, 0), (2 * R, R)))
        # Exact D6 symmetry gives defect zero, hence E=1 is a valid upper bound.
        check_approximate_bound(points, Fraction(0), 1)
        print(
            "PASS R={} n={} D_eq^2={} declared_E=1".format(
                R,
                len(points),
                max(_D6.qform(p, Fraction(1, 2)) for p in _D6.difference_set(points)),
            )
        )
    print("PASS: exact approximate-orbit stability margin with K_c<=3")
    print("Scope: affine sources with explicit orbit-defect hypothesis; no Level-I closure")


if __name__ == "__main__":
    main()
