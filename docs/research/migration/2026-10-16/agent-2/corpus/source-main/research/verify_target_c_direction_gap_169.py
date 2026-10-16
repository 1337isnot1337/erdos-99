#!/usr/bin/env python3
"""Scalar certificate for audited-working Target C Section 169."""

from __future__ import annotations

import math

SQRT3 = math.sqrt(3.0)
PI = math.pi
S = math.sqrt(PI / (2.0 * SQRT3))
C146 = (4.0 / 9.0) * (PI + S)
ATOMIC_GAIN = 0.0004
ETA = 0.00089


def margin(eta: float) -> tuple[float, float, float, float]:
    aeta = 2.0 * S + 4.5 * eta
    reta = aeta - 4.0 * S * S / aeta
    ell = (PI - C146 - 10.0 * eta + 2.0 * ATOMIC_GAIN - 2.0 * reta) / 3.0
    lower = ell**3 / (2.0 * PI * PI + ell * ell)
    upper = 4.5 * eta
    return ell, lower, upper, lower - upper


def main() -> None:
    ell, lower, upper, strict = margin(ETA)

    lo = ETA
    hi = 0.00092
    for _ in range(160):
        mid = (lo + hi) / 2.0
        if margin(mid)[3] > 0.0:
            lo = mid
        else:
            hi = mid
    root = (lo + hi) / 2.0

    print(f"s={S:.16f}")
    print(f"C146={C146:.16f}")
    print(f"certified_floor={C146 + ETA:.16f}")
    print(f"ell={ell:.16f}")
    print(f"atom_detour_lower={lower:.16f}")
    print(f"detour_upper={upper:.16f}")
    print(f"strict_margin={strict:.16f}")
    print(f"scalar_root={root:.16f}")

    assert ell > 0.4326
    assert lower > 0.004064
    assert abs(upper - 0.004005) < 1e-15
    assert strict > 5.9e-5
    assert 0.0009024 < root < 0.0009026

    print("PASS: audited-working Section 169 q-k direction-gap certificate")


if __name__ == "__main__":
    main()
