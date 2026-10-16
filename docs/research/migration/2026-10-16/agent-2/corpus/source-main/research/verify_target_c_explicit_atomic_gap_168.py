#!/usr/bin/env python3
"""Scalar certificate for audited-working Target C Section 168.

Checks only the displayed eta_grid=0.0004 quantitative bookkeeping. It does not
certify the geometric train theorems, subsequential measure extraction, or C-II.
"""

from __future__ import annotations

import math

ETA = 0.0004
SQRT3 = math.sqrt(3.0)
S2 = math.sqrt(math.pi / (2.0 * SQRT3))
GRID_CAP = 2.0 / SQRT3


def effective_mass(eta: float) -> float:
    abar = 2.0 * S2 + eta
    m0 = 4.0 * S2 * S2 / abar
    r0 = abar - m0
    d0 = abar * abar / 4.0 - S2 * S2 + r0 * r0 / 4.0
    p0 = math.sqrt(2.0 * d0)
    s0 = m0 / 2.0 - math.sqrt(d0) - math.sqrt(6.0 * d0)
    return 1.5 * s0 - 6.0 * p0


def main() -> None:
    abar = 2.0 * S2 + ETA
    m0 = 4.0 * S2 * S2 / abar
    r0 = abar - m0
    d0 = abar * abar / 4.0 - S2 * S2 + r0 * r0 / 4.0
    p0 = math.sqrt(2.0 * d0)
    s0 = m0 / 2.0 - math.sqrt(d0) - math.sqrt(6.0 * d0)
    pair_mass = 1.5 * s0
    eff = pair_mass - 6.0 * p0
    projected = (SQRT3 / 2.0) * eff

    b_after_pruning = s0 / 2.0 - 2.0 * p0
    a_after_pruning = s0 - 2.0 * p0
    triple_missing = 3.0 * p0

    weighted_floor = (4.0 / 9.0) * (math.pi + S2) + (2.0 / 9.0) * ETA

    lo = ETA
    hi = 0.00045
    for _ in range(160):
        mid = (lo + hi) / 2.0
        if effective_mass(mid) > GRID_CAP:
            lo = mid
        else:
            hi = mid
    scalar_root = (lo + hi) / 2.0

    print(f"s2={S2:.16f}")
    print(f"Abar={abar:.16f}")
    print(f"M0={m0:.16f}")
    print(f"R0={r0:.16f}")
    print(f"d0={d0:.16f}")
    print(f"p0={p0:.16f}")
    print(f"S0={s0:.16f}")
    print(f"pair_mass={pair_mass:.16f}")
    print(f"effective_mass={eff:.16f}")
    print(f"grid_cap={GRID_CAP:.16f}")
    print(f"projected={projected:.16f}")
    print(f"A_after_pruning={a_after_pruning:.16f}")
    print(f"B_after_pruning={b_after_pruning:.16f}")
    print(f"triple_missing={triple_missing:.16f}")
    print(f"weighted_floor={weighted_floor:.16f}")
    print(f"displayed_bookkeeping_root={scalar_root:.16f}")

    assert r0 < 0.0008
    assert d0 < 0.000382
    assert p0 < 0.02761
    assert s0 > 0.8847
    assert pair_mass > 1.3271
    assert b_after_pruning > 0.3871
    assert a_after_pruning > 0.8295
    assert b_after_pruning > triple_missing
    assert a_after_pruning > triple_missing
    assert eff > 1.1614
    assert eff - GRID_CAP > 0.0067
    assert projected > 1.0058
    assert abs((2.0 / 9.0) * ETA - 1.0 / 11250.0) < 1e-15
    assert 0.0004205 < scalar_root < 0.0004207

    print("PASS: audited-working Section 168 eta_grid=0.0004 scalar certificate")


if __name__ == "__main__":
    main()
