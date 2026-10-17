#!/usr/bin/env python3
"""Regression checks for the fixed-pair lossless FREE common-run extraction.

This certificate checks only the finite arithmetic/combinatorial reductions used in
`target_c_tooth_reflection_fixed_pair_lossless_common_runs_2026-09-18.md`.
It does not certify global optimality or promote the candidate theorem.
"""

from __future__ import annotations

import math


C_STAR = 0.129220199818177
H_STAR = math.sqrt(303.0) / 52.0


def check_fixed_pair_separation() -> None:
    """Check the floor/endpoint bookkeeping behind theta >= c_* - o(1)."""
    # Write A = D^(1/4)/kappa.  If at least (c_*/2-eps)A FREE
    # modules remain and consecutive selected normals are at least 2/A apart,
    # the first/last FREE modules are separated by c_* - 2eps - O(1/A).
    for A in (1e4, 1e6, 1e8):
        eps = min(C_STAR / 8.0, A**-0.5)
        n = math.floor((C_STAR / 2.0 - eps) * A)
        assert n >= 2
        theta = 2.0 * (n - 1) / A
        lower = C_STAR - 2.0 * eps - 4.0 / A
        assert theta + 1e-15 >= lower

    assert 0.0 < C_STAR < math.pi / 2.0


def check_two_module_reuse_fork() -> None:
    """Specialize the existing m-module incidence fork to m=2, R=1."""
    for k in (0.5, 1.0, 2.0, 10.0):
        assert k > H_STAR
        alpha = 1.0 - H_STAR / k
        d = 10**9

        # The two modules contribute I >= 2 alpha D incidences asymptotically.
        incidences = 2.0 * alpha * d

        # If light incidence is at least I/2, all light edges have multiplicity
        # at most one.  The degree-six graph matching bound loses a factor 11.
        light_matching = (incidences / 2.0) / 11.0
        assert math.isclose(
            light_matching, alpha * d / 11.0, rel_tol=1e-15
        )

        # Otherwise heavy incidence is > I/2.  With only two modules, each
        # heavy edge has multiplicity exactly two, so distinct heavy edges are
        # at least (I/2)/2 = alpha D/2.
        heavy_edges = (incidences / 2.0) / 2.0
        assert math.isclose(heavy_edges, alpha * d / 2.0, rel_tol=1e-15)


def check_run_pair_pigeonhole() -> None:
    """All heavy edges can be retained; no matching thinning is needed."""
    for edges in (10, 100, 10_000):
        for external_count in (0, 1, 4, 9, 99):
            cells = (external_count + 1) ** 2
            lower = math.ceil(edges / cells)
            assert lower >= edges / cells


def check_component_minimax() -> None:
    """Check the cycle-rank versus two-normal-drift balancing."""
    b0 = math.sin(C_STAR / 2.0)

    # SAME components have coefficient sin(theta/2), while OPPOSITE
    # components have cos(theta/2).  For theta in [c_*-o(1), pi/2+o(1)], b0 is a
    # uniform lower coefficient for both cases.
    assert math.cos(math.pi / 4.0) > b0

    for q in (100.0, 1e4, 1e8, 1e16):
        threshold = math.sqrt(q / b0)
        target = math.sqrt(b0 * q)

        cycle = q / threshold - 1.0
        drift = b0 * threshold

        assert math.isclose(drift, target, rel_tol=1e-14)
        assert math.isclose(cycle + 1.0, target, rel_tol=1e-14)


def check_k1_constants() -> None:
    """Freeze the numerical constants quoted for K=1."""
    alpha = 1.0 - H_STAR
    b0 = math.sin(C_STAR / 2.0)
    matching_coefficient = alpha / 11.0
    shared_edge_coefficient = alpha / 2.0
    currency_coefficient = math.sqrt(b0 * shared_edge_coefficient)

    assert math.isclose(H_STAR, 0.33474798433710024, rel_tol=1e-15)
    assert math.isclose(alpha, 0.6652520156628998, rel_tol=1e-15)
    assert math.isclose(b0, 0.06456515719047448, rel_tol=1e-15)
    assert math.isclose(
        matching_coefficient, 0.06047745596935453, rel_tol=1e-15
    )
    assert math.isclose(
        shared_edge_coefficient, 0.3326260078314499, rel_tol=1e-15
    )
    assert math.isclose(
        currency_coefficient, 0.14654709304956395, rel_tol=1e-15
    )


def main() -> None:
    check_fixed_pair_separation()
    check_two_module_reuse_fork()
    check_run_pair_pigeonhole()
    check_component_minimax()
    check_k1_constants()
    print("PASS: fixed-pair FREE common-run extraction")


if __name__ == "__main__":
    main()
