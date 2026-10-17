#!/usr/bin/env python3
"""Arithmetic/regression checks for the fixed-pair boundary/forest tri-fork.

This verifies the finite minimax inequality, optimized constants, aggregate-to-uniform
upper-defect conversion, and supercritical crossing-extraction scale. Geometric
inputs are proved in the accompanying note and its cited modules.
"""

from __future__ import annotations

import math
import random

H_STAR = math.sqrt(303.0) / 52.0
C_STAR = 0.129220199818177
B_STAR = math.sin(C_STAR / 2.0)
ALPHA_1 = 1.0 - H_STAR
C1 = math.sqrt(ALPHA_1 * B_STAR / 10.0)
LAMBDA2_SIZE = C1 / 2.0
LAMBDA2_DEFICIT = 2.0 * H_STAR / C1


def check_finite_minimax() -> None:
    rng = random.Random(0xE99BF)
    for _ in range(200_000):
        e = 10.0 ** rng.uniform(-2.0, 12.0)
        s = 10.0 ** rng.uniform(-1.0, 7.0)
        t = 10.0 ** rng.uniform(-4.0, 12.0)
        lhs = max(e / s - t, t / 4.0)
        rhs = e / (5.0 * s)
        assert lhs + 1e-12 * max(1.0, rhs) >= rhs

        threshold = 4.0 * e / (5.0 * s)
        if t >= threshold:
            assert t / 4.0 + 1e-12 * max(1.0, rhs) >= rhs
        else:
            assert e / s - t > rhs - 1e-12 * max(1.0, rhs)


def check_balanced_threshold() -> None:
    for e in (1.0, 10.0, 1e4, 1e12):
        s = math.sqrt(e / (5.0 * B_STAR))
        drift = B_STAR * s
        residual = e / (5.0 * s)
        target = math.sqrt(B_STAR * e / 5.0)
        assert math.isclose(drift, target, rel_tol=2e-15)
        assert math.isclose(residual, target, rel_tol=2e-15)


def check_k1_constants() -> None:
    assert math.isclose(H_STAR, 0.33474798433710024, rel_tol=1e-15)
    assert math.isclose(B_STAR, 0.06456515719047448, rel_tol=1e-15)
    assert math.isclose(ALPHA_1, 0.6652520156628998, rel_tol=1e-15)
    assert math.isclose(C1, 0.0655378523927624, rel_tol=1e-15)
    assert math.isclose(LAMBDA2_SIZE, 0.0327689261963812, rel_tol=1e-15)
    assert math.isclose(LAMBDA2_DEFICIT, 10.215409022895226, rel_tol=1e-15)

    # The all-run small-external coefficient is sqrt(alpha*b/2), while the
    # universal boundary/forest coefficient is smaller by sqrt(1/5).
    all_run = math.sqrt(ALPHA_1 * B_STAR / 2.0)
    assert math.isclose(C1, all_run / math.sqrt(5.0), rel_tol=2e-15)


def check_aggregate_to_uniform() -> None:
    # If M >= C1*sqrt(D) and total deficit <= h_*, Markov with Lambda=2
    # leaves M/2 edges with individual deficit <= 2 h_*/M.
    for d in (1e8, 1e12, 1e20):
        m = C1 * math.sqrt(d)
        threshold = 2.0 * H_STAR / m
        predicted = LAMBDA2_DEFICIT / math.sqrt(d)
        assert math.isclose(threshold, predicted, rel_tol=5e-15)


def check_crossing_scale() -> None:
    # Existing bounded-conflict theorem loses O(1 + D/U) when the upper
    # matching has Omega(U) edges and diameter deficit O(1/U).
    for d in (1e12, 1e18, 1e24):
        root = math.sqrt(d)
        u_critical = root
        u_super = root * math.log(d)
        critical = u_critical * u_critical / (d + u_critical)
        supercritical = u_super * u_super / (d + u_super)
        assert 0.99 < critical < 1.01
        assert supercritical > 0.8 * math.log(d) ** 2


def main() -> None:
    check_finite_minimax()
    check_balanced_threshold()
    check_k1_constants()
    check_aggregate_to_uniform()
    check_crossing_scale()
    print("PASS: fixed-pair boundary/forest tri-fork certificate")
    print(f"h_* = {H_STAR:.15f}")
    print(f"b_* = {B_STAR:.15f}")
    print(f"alpha_1 = {ALPHA_1:.15f}")
    print(f"K=1 universal sqrt(D) coefficient = {C1:.15f}")
    print(f"K=1 Lambda=2 uniform matching coefficient = {LAMBDA2_SIZE:.15f}")
    print(f"K=1 Lambda=2 upper deficit coefficient = {LAMBDA2_DEFICIT:.15f}")


if __name__ == "__main__":
    main()
