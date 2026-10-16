#!/usr/bin/env python3
"""Arithmetic check for the near-density shell competitor.

The proof is in
docs/reports/target_c_near_density_shell_global_competitor_2026-09-12.md.
This script evaluates the exact floor bounds supplied by translation averaging for
large even polygon orders.  It checks the strict count margin and the fact that the
source/competitor diameters differ by a fixed amount.  It does not construct the
translates, prove the averaging lemma, or assert global optimality of any other
source.
"""

from __future__ import annotations

import math
from fractions import Fraction


def check(q: int, a: float = 1.1, c: float = 0.1) -> None:
    assert q % 2 == 0 and q >= 8
    assert 0.0 < c < a - math.sqrt(3.0) / 2.0
    D = 1.0 / math.sin(math.pi / q)
    R = D / 2.0
    assert R > a
    spacing = 1.0 + D ** -2
    density = 2.0 / math.sqrt(3.0)

    inner_count = math.floor(density * math.pi * (R - a) ** 2 / spacing ** 2)
    source_count = q + inner_count
    competitor_count = math.floor(density * math.pi * (R - c) ** 2)
    diameter_gap = D - 2.0 * c

    # Positive shell stress: alpha on every unit edge and beta on every
    # antipodal diameter pair.  The interior isolates have no active rows.
    phi = math.pi / q
    alpha = 1.0 / (q * math.sin(phi) ** 2)
    beta = 2.0 / q
    assert alpha > 0.0 and beta > 0.0
    assert abs((q / 2.0) * beta - 1.0) < 1e-12
    assert abs(q * alpha - D * D) < 1e-9
    assert abs(alpha * 4.0 * R * math.sin(phi) ** 2
               - beta * 2.0 * R) < 1e-12

    assert competitor_count > source_count
    assert diameter_gap < D
    print(
        f"q={q} D={D:.8f} source={source_count} competitor={competitor_count} "
        f"margin={competitor_count-source_count} gap={2*c:.3f} "
        f"density={source_count/D**2:.8f}"
    )


def main() -> None:
    # The displayed choices satisfy c < a - sqrt(3)/2.  The theorem is
    # asymptotic; these values simply reach the positive margin numerically.
    for q in (200, 500, 1000, 2000):
        check(q)

    # A conservative leading coefficient check using pi > 3 and
    # sqrt(3) < 26/15.  For a=11/10, c=1/10 the linear margin is positive.
    pi_lower = Fraction(3)
    sqrt3_upper = Fraction(26, 15)
    assert sqrt3_upper**2 > 3
    delta_lower = 2 / sqrt3_upper
    linear_margin_lower = delta_lower * pi_lower * (
        Fraction(11, 10) - Fraction(1, 10) - sqrt3_upper / 2
    )
    assert linear_margin_lower > 0.0
    assert linear_margin_lower == Fraction(6, 13)
    print(f"certified_linear_margin_lower={linear_margin_lower}")
    print("PASS: near-density shell competitor count is strict")


if __name__ == "__main__":
    main()
