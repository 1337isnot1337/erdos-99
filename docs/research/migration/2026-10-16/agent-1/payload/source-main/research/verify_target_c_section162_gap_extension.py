#!/usr/bin/env python3
"""Exact arithmetic for the Section-162 eta=9/10000 extension.

This checks only the displayed rational interval calculation in
research/target_c_section162_gap_extension_2026-09-12.md.  It assumes the
Machin-series bounds for pi and the rational square bounds for sqrt(3), and it
does not certify the inherited geometric Section-146/162 arguments, global
optimality, or C-II closure.
"""

from __future__ import annotations

from fractions import Fraction as F


def main() -> None:
    pi_lo = F(3141592653589793, 10**15)
    pi_hi = F(3141592653589794, 10**15)
    root3_lo = F(1732050807568877, 10**15)
    root3_hi = F(1732050807568878, 10**15)
    s_lo = F(9523128, 10**7)
    s_hi = F(9523129, 10**7)
    eta = F(9, 10000)
    c = F(9, 2) * eta

    assert root3_lo * root3_lo < 3 < root3_hi * root3_hi
    delta_lo = pi_lo / (2 * root3_hi)
    delta_hi = pi_hi / (2 * root3_lo)
    assert s_lo * s_lo < delta_lo
    assert s_hi * s_hi > delta_hi

    def R(s: F) -> F:
        return c * (4 * s + c) / (2 * s + c)

    r_lo = R(s_lo)
    r_hi = R(s_hi)
    ell_lo = (F(5, 9) * pi_lo - F(4, 9) * s_hi - 10 * eta - 2 * r_hi) / 3
    ell_hi = (F(5, 9) * pi_hi - F(4, 9) * s_lo - 10 * eta - 2 * r_lo) / 3
    assert ell_lo > F(4322987538, 10**10)
    assert ell_hi < F(4322987687, 10**10)

    lower_bound = ell_lo**3 / (2 * pi_hi**2 + ell_hi**2)
    target = F(9, 2) * eta
    assert lower_bound > F(405, 100000)
    assert lower_bound > target

    print(f"eta={float(eta):.10f}")
    print(f"ell_lo={float(ell_lo):.12f}")
    print(f"ell_hi={float(ell_hi):.12f}")
    print(f"certified_lower_bound={float(lower_bound):.12f}")
    print(f"detour_upper_bound={float(target):.12f}")
    print(f"margin={float(lower_bound - target):.12f}")
    print("PASS: rational Section-162 eta extension")


if __name__ == "__main__":
    main()
