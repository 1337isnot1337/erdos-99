#!/usr/bin/env python3
"""Regression for corrected Target C Section 121.

Checks the exact three-fifths algebra and the binding scaling regression:
G=o(D^2) with d=Theta(D) does not imply G/d=o(1).  The finite geometric
inequalities themselves are proved analytically in the Section-121 report.
"""

import math


def main() -> None:
    c0 = math.sqrt(3.0) / 4.0

    # Exact algebra behind 5H-3J = 2[(L-p)+(Q-f)] >= 0.
    samples = [
        (0.0, 1.0, 1.0),
        (2.5, 3.0, 7.0),
        (11.0, 5.0, 8.0),
    ]
    for detour, f, q in samples:
        assert detour >= 0.0
        assert q >= f
        H = detour + 2.0 * f + q
        J = detour + 4.0 * f + q
        assert abs((5.0 * H - 3.0 * J) - 2.0 * (detour + q - f)) < 1e-12
        assert H + 1e-12 >= 0.6 * J

    # Binding counterexample to the withdrawn asymptotic inference.
    # d=D and G=D^(3/2): G/D^2 -> 0, but G/d=sqrt(D) -> infinity.
    Ds = [10.0**k for k in range(2, 9)]
    ratios_bulk = []
    ratios_boundary = []
    for D in Ds:
        d = D
        G = D ** 1.5
        ratios_bulk.append(G / (D * D))
        ratios_boundary.append(G / d)

    assert ratios_bulk[-1] < ratios_bulk[0]
    assert ratios_bulk[-1] < 1e-3
    assert ratios_boundary[-1] > ratios_boundary[0]
    assert ratios_boundary[-1] > 1e3

    # The normalized coefficient in the corrected moment inequality.
    coeff = 5.0 / (6.0 * c0)
    assert 1.9 < coeff < 2.0

    print(f"three_fifths=0.6")
    print(f"moment_error_coefficient={coeff:.16f}")
    print(f"G_over_D2_at_largest_D={ratios_bulk[-1]:.16e}")
    print(f"G_over_d_at_largest_D={ratios_boundary[-1]:.16e}")
    print("withdrawn implication G=o(D^2) => G/d=o(1): FALSE")


if __name__ == "__main__":
    main()
