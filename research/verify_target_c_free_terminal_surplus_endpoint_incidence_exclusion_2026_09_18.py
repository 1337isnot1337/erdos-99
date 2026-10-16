#!/usr/bin/env python3
"""Regression checks for terminal FREE surplus-endpoint incidence exclusion.

This checks the scalar frontier and the numerical contradiction in
`target_c_free_terminal_surplus_endpoint_incidence_exclusion_2026-09-18.md`.
It does not replace the cited geometric train-length, orbit-separation, or
surplus-stability theorems.
"""

from __future__ import annotations

import math

SQRT3 = math.sqrt(3.0)
DELTA2 = math.pi / (2.0 * SQRT3)
S2 = math.sqrt(DELTA2)
G = 0.007707
MSTAR = 4.0 * S2 + 2.0 * G
EMAX = 2.0 * G
PSTAR = math.pi / 2.0 - G


def frontier(e: float) -> tuple[float, float, float]:
    B = 0.5 * (MSTAR - e)
    disc = 8.0 * DELTA2 - B * B
    assert disc >= -1e-14
    disc = max(0.0, disc)
    w = 0.5 * (B + math.sqrt(disc))
    return B, w, B - w


def constants() -> None:
    B0, w0, r0 = frontier(0.0)
    assert abs(DELTA2 - 0.9068996821171089) < 2e-15
    assert abs(S2 - 0.9523128068639574) < 2e-15
    assert abs(MSTAR - 3.8246652274558293) < 4e-15
    assert abs(B0 - 1.9123326137279146) < 3e-15
    assert abs(w0 - 1.9046099571945176) < 3e-15
    assert abs(r0 - 0.007722656533396988) < 3e-15
    assert abs(PSTAR - 1.5630893267948965) < 3e-15
    assert abs(r0 * r0 / 2.0 - 0.00002981971196640959) < 3e-15
    assert abs(PSTAR - r0 * r0 / 2.0 - 1.5630595070829303) < 3e-15


def uniform_frontier_gap(samples: int = 200_000) -> None:
    """Check p(e) > r(e)^2/2 uniformly on 0 <= e <= 2g."""
    _B0, _w0, r0 = frontier(0.0)
    min_gap = float("inf")
    for j in range(samples + 1):
        e = EMAX * j / samples
        _B, _w, r = frontier(e)
        p = 0.5 * (math.pi - e)

        assert r <= r0 + 2e-14
        assert p + 2e-14 >= PSTAR
        assert r * r / 2.0 <= r0 * r0 / 2.0 + 2e-14

        gap = p - r * r / 2.0
        min_gap = min(min_gap, gap)
        assert gap > 1.563 - 1e-12

    assert min_gap + 2e-14 >= PSTAR


def incidence_relaxation() -> None:
    """The endpoint incidence lower and upper envelopes are disjoint."""
    _B0, _w0, r0 = frontier(0.0)
    incidence_floor = PSTAR
    incidence_ceiling = r0 * r0 / 2.0
    distinct_comp_rhombi_ceiling = r0 * r0 / 4.0
    dominant_rhombi_floor = DELTA2 - distinct_comp_rhombi_ceiling

    assert incidence_floor > incidence_ceiling
    assert incidence_floor - incidence_ceiling > 1.563

    # Equivalent distinct-rhombus accounting: O--O incidence demands at least
    # PSTAR/2 distinct complement rhombi, while the dominant orbit already uses
    # Delta2-r0^2/4 of the total Delta2 budget.
    assert dominant_rhombi_floor + incidence_floor / 2.0 > DELTA2
    assert abs(dominant_rhombi_floor - 0.9068847722611257) < 3e-15
    assert abs(
        dominant_rhombi_floor + incidence_floor / 2.0
        - 1.688429435658574
    ) < 4e-15


def main() -> None:
    constants()
    uniform_frontier_gap()
    incidence_relaxation()

    _B0, _w0, r0 = frontier(0.0)
    print("terminal FREE surplus endpoint incidence exclusion: PASS")
    print(f"p_min={PSTAR:.15f}")
    print(f"r_max={r0:.15f}")
    print(f"incidence_capacity_max={r0*r0/2.0:.15f}")
    print(f"contradiction_gap={PSTAR-r0*r0/2.0:.15f}")
    print(f"dominant_rhombi_min={DELTA2-r0*r0/4.0:.15f}")


if __name__ == "__main__":
    main()
