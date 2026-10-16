#!/usr/bin/env python3
"""Numerical regression for proof-only Target C Section 105.

Checks only the optimized scalar/root and explicit leakage/alignment margins.  The
geometric stability lemmas remain theorem dependencies from Sections 103--104.
"""

from __future__ import annotations

import math


PI = math.pi
THETA8 = 2.7029080296483676832
MU8 = 0.9760407652670519821
SIGMA = 7.0e-7
H = 0.0011
E0 = 0.001875
RHO = 0.00019


def slack(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def bisect_root(lo: float, hi: float, target: float, iterations: int = 120) -> float:
    assert slack(lo) <= target <= slack(hi)
    for _ in range(iterations):
        mid = (lo + hi) / 2.0
        if slack(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> None:
    theta10 = bisect_root(THETA8, THETA8 + 1.0e-4, SIGMA)
    mu10 = math.sin(theta10 / 2.0)

    assert abs(theta10 - 2.7029081785266174) < 5e-15
    assert abs(mu10 - 0.9760407814640902) < 5e-15
    assert 1.61e-8 < mu10 - MU8 < 1.63e-8
    assert abs(slack(theta10) - SIGMA) < 5e-15

    # The Section-104 scalar stability window grows only microscopically.
    assert theta10 - THETA8 < (4.0 / 15.0) * SIGMA

    # Re-optimized good/bad tooth cutoff.
    w_h = PI / 3.0 - math.acos((1.0 + H) / 2.0)
    leak = w_h + (1.0 / H + 169.0 / 6.0) * SIGMA
    assert 0.000635 < w_h < 0.000636
    assert leak < 0.001292
    remaining = E0 - leak
    assert remaining > 0.000583
    assert remaining / 3.0 > 0.000194
    assert remaining / 3.0 > RHO

    # Principal corridor geometry remains far from pi/3.
    endpoint_margin = THETA8 / 2.0 - PI / 3.0
    corridor_margin = endpoint_margin - (73.0 / 6.0) * SIGMA
    assert corridor_margin > 0.304247

    # Sharpened principal-route excess <= sigma gives the phase alignment bound.
    delta = PI * math.sqrt(SIGMA / (2.0 * RHO))
    assert delta < 0.13484
    assert 2.0 * delta < 0.26968
    assert corridor_margin - 2.0 * delta > 0.0345

    # Section-103 area concentration is still comfortably positive at theta10.
    k = math.floor(2.0 * PI / theta10)
    rem = 2.0 * PI - k * theta10
    cap = (2.0 * PI - k * math.sin(theta10) - math.sin(rem)) / 8.0
    gamma = PI / 4.0 - cap
    assert k == 2
    assert gamma > 0.2023
    assert gamma > 0.19

    # Coarse Section-104 gap-stability comparisons remain safely valid.
    phi = 2.0 * PI - 2.0 * theta10
    barrier = (
        math.sin((theta10 - 0.1) / 2.0)
        + math.sin((phi + 0.1) / 2.0)
        - math.sin(theta10 / 2.0)
        - math.sin(phi / 2.0)
    )
    assert barrier > 0.0326
    assert (13.0 / 3.0) * SIGMA < phi

    print(f"theta10={theta10:.16f}")
    print(f"mu10={mu10:.16f}")
    print(f"mu10-mu8={mu10 - MU8:.16e}")
    print(f"w_h={w_h:.16e}")
    print(f"phase_endpoint_leak={leak:.16e}")
    print(f"per_corridor_available={remaining / 3.0:.16e}")
    print(f"alignment_delta={delta:.16e}")
    print(f"corridor_margin={corridor_margin:.16e}")
    print(f"contradiction_margin={corridor_margin - 2.0 * delta:.16e}")
    print(f"Gamma(mu10)={gamma:.16f}")


if __name__ == "__main__":
    main()
