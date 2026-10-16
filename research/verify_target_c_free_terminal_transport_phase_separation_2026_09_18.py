#!/usr/bin/env python3
"""Regression checks for terminal FREE transport/phase separation.

This certifies scalar algebra and randomized finite relaxations used in
target_c_free_terminal_transport_phase_separation_2026-09-18.md.
It does not certify the external theorem that triangle-free circle graphs
are 5-colourable.
"""

from __future__ import annotations

import math
import random

SQRT3 = math.sqrt(3.0)
DELTA2 = math.pi / (2.0 * SQRT3)
S2 = math.sqrt(DELTA2)
G = 0.007707
A0 = 2.0 * S2 + G
MSTAR = 2.0 * A0
EMAX = 2.0 * G

W0 = 0.5 * (A0 + math.sqrt(8.0 * DELTA2 - A0 * A0))
R0 = A0 - W0

ELL_MIN = math.pi / 2.0 - G
SECTOR6_MIN = math.pi / 12.0 - G
SECTOR12_MIN = math.pi / 24.0 - G


def constants() -> None:
    assert abs(DELTA2 - 0.9068996821171089) < 2e-15
    assert abs(S2 - 0.9523128068639574) < 2e-15
    assert abs(A0 - 1.9123326137279146) < 3e-15
    assert abs(MSTAR - 3.8246652274558293) < 4e-15
    assert abs(EMAX - 0.015414) < 1e-15

    assert abs(W0 - 1.9046099571945176) < 3e-15
    assert abs(R0 - 0.007722656533396988) < 3e-15
    assert abs(W0 * W0 + R0 * R0 - 4.0 * DELTA2) < 3e-15

    assert abs(ELL_MIN - 1.5630893267948965) < 3e-15
    assert abs(SECTOR6_MIN - 0.2540923877991494) < 3e-15
    assert abs(SECTOR12_MIN - 0.1231926938995747) < 3e-15

    assert abs(ELL_MIN / 5.0 - 0.3126178653589793) < 3e-15
    assert abs(SECTOR6_MIN / 5.0 - 0.05081847755982988) < 3e-15
    assert abs(SECTOR12_MIN / 5.0 - 0.02463853877991494) < 3e-15


def frontier(e: float) -> tuple[float, float, float]:
    """Return B(e), dominant-orbit floor w(e), residual ceiling r(e)."""
    B = 0.5 * (MSTAR - e)
    disc = 8.0 * DELTA2 - B * B
    assert disc >= -1e-14
    disc = max(0.0, disc)
    w = 0.5 * (B + math.sqrt(disc))
    r = B - w
    return B, w, r


def endpoint_frontier_checks() -> None:
    B0, w0, r0 = frontier(0.0)
    assert abs(B0 - A0) < 2e-15
    assert abs(w0 - W0) < 2e-15
    assert abs(r0 - R0) < 2e-15

    B1, w1, r1 = frontier(EMAX)
    assert abs(B1 - 2.0 * S2) < 3e-15
    assert abs(w1 - 2.0 * S2) < 3e-15
    assert abs(r1) < 3e-15

    prev_r = r0
    for j in range(1, 10001):
        e = EMAX * j / 10000.0
        B, w, r = frontier(e)
        assert B + 1e-14 >= 2.0 * S2
        assert w <= B + 1e-14
        assert r >= -1e-14
        assert w * w + r * r + 2e-14 >= 4.0 * DELTA2
        assert r <= prev_r + 2e-14
        prev_r = r


def transport_randomized(trials: int = 300_000) -> None:
    rng = random.Random(0xE99A701)
    for _ in range(trials):
        e = rng.random() * EMAX
        B, w, r = frontier(e)

        loo = 0.5 * (math.pi - e)
        ebb = 0.5 * (MSTAR - e)

        # Exact endpoint transport handshakes.
        assert abs(e + 2.0 * loo - math.pi) < 2e-15
        assert abs(2.0 * ebb + e - MSTAR) < 3e-15
        assert abs(ebb - B) < 2e-15
        assert loo + 2e-15 >= ELL_MIN
        assert ebb + 2e-15 >= 2.0 * S2

        # The atomic crossing lower bound A >= 2 sqrt(Delta2) is
        # compatible with bounded-bounded capacity exactly iff e <= 2g.
        A = 2.0 * S2 + rng.random() * max(0.0, B - 2.0 * S2)
        assert A <= B + 2e-15
        assert A * A / 4.0 + 2e-15 >= DELTA2

        # Test the sharp dominant-orbit relaxation:
        # choose total atomic mass <= B and random orbit pieces; whenever
        # they can carry Delta2 quadratic crossing mass, max piece >= w.
        total = 2.0 * S2 + rng.random() * max(0.0, B - 2.0 * S2)
        k = rng.randint(1, 12)
        raw = [rng.expovariate(1.0) for _ in range(k)]
        z = sum(raw)
        masses = [total * x / z for x in raw]
        sq = sum(x * x for x in masses)
        if sq + 1e-14 >= 4.0 * DELTA2:
            assert max(masses) + 2e-12 >= w

        # Residual crossing capacity outside the dominant orbit.
        assert r * r / 4.0 >= -1e-16
        assert DELTA2 - r * r / 4.0 <= w * w / 4.0 + 2e-14


def orbit_relaxation_adversarial(trials: int = 300_000) -> None:
    """Directly test the optimization inequality without feasibility sampling."""
    rng = random.Random(0xC11E99)
    for _ in range(trials):
        e = rng.random() * EMAX
        B, w_floor, _ = frontier(e)

        # Pick A <= B, W <= A with W >= A/2; the maximum sum of squares
        # given this leading mass is W^2+(A-W)^2.
        A = (2.0 * S2) + rng.random() * max(0.0, B - 2.0 * S2)
        W = A / 2.0 + rng.random() * A / 2.0
        sq_cap = W * W + (A - W) * (A - W)
        if sq_cap + 1e-14 >= 4.0 * DELTA2:
            # Since B >= A, w_floor is the weakest floor at capacity B.
            assert W + 2e-12 >= w_floor


def measure_budget_checks(trials: int = 200_000) -> None:
    """Finite partition version of nu = beta + 2 omega."""
    rng = random.Random(0x0B0A99)
    for _ in range(trials):
        bins = rng.randint(2, 20)
        lengths = [rng.random() for _ in range(bins)]
        scale = math.pi / sum(lengths)
        lam = [x * scale for x in lengths]

        # beta is any submeasure of Lebesgue with total e <= 2g.
        caps = [rng.random() * x for x in lam]
        total_cap = sum(caps)
        e_target = rng.random() * min(EMAX, total_cap)
        if total_cap == 0.0:
            beta = [0.0] * bins
        else:
            beta = [x * e_target / total_cap for x in caps]

        omega = [(l - b) / 2.0 for l, b in zip(lam, beta)]
        assert all(x >= -1e-15 for x in omega)
        assert abs(sum(beta) + 2.0 * sum(omega) - math.pi) < 3e-15
        assert sum(omega) + 2e-15 >= ELL_MIN

        # Total-variation distance from half-Lebesgue equals beta mass / 2.
        tv = sum(abs(o - l / 2.0) for o, l in zip(omega, lam))
        assert abs(tv - sum(beta) / 2.0) < 3e-15
        assert tv <= G + 2e-15

        # Every bin gets the universal interval floor.
        e = sum(beta)
        for l, o in zip(lam, omega):
            assert o + 2e-15 >= max(0.0, (l - e) / 2.0)
            assert o + 2e-15 >= max(0.0, (l - EMAX) / 2.0)


def main() -> None:
    constants()
    endpoint_frontier_checks()
    transport_randomized()
    orbit_relaxation_adversarial()
    measure_budget_checks()

    print("terminal FREE transport/phase separation: PASS")
    print(f"Delta2={DELTA2:.15f}")
    print(f"s2={S2:.15f}")
    print(f"A0={A0:.15f}")
    print(f"M*={MSTAR:.15f}")
    print(f"e_BO,max={EMAX:.15f}")
    print(f"W(0)={W0:.15f}")
    print(f"r(0)={R0:.15f}")
    print(f"L_O,min={ELL_MIN:.15f}")
    print(f"pi/6-sector O-O floor={SECTOR6_MIN:.15f}")
    print(f"global laminar 5-color floor={ELL_MIN/5.0:.15f}")
    print(f"pi/6-sector laminar floor={SECTOR6_MIN/5.0:.15f}")


if __name__ == "__main__":
    main()
