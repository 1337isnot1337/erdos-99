#!/usr/bin/env python3
"""Regression checks for the all-run FREE forest-union theorem.

The script verifies the exact Euler-characteristic identity on finite path-forest
examples and the arithmetic/minimax constants in
`target_c_tooth_reflection_all_run_forest_union_2026-09-18.md`.
It does not replace the geometric proof dependencies.
"""

from __future__ import annotations

import math

C_STAR = 0.129220199818177
H_STAR = math.sqrt(303.0) / 52.0
B_STAR = math.sin(C_STAR / 2.0)
ALPHA_1 = 1.0 - H_STAR
K1_CURRENCY = math.sqrt(ALPHA_1 * B_STAR / 2.0)


def edge(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def path_edges(path: list[int]) -> set[tuple[int, int]]:
    return {edge(path[i], path[i + 1]) for i in range(len(path) - 1)}


def graph_stats(edges: set[tuple[int, int]], extra_vertices: set[int] | None = None) -> tuple[int, int, int, int]:
    vertices = set(extra_vertices or ())
    for u, v in edges:
        vertices.add(u)
        vertices.add(v)
    if not vertices:
        return 0, 0, 0, 0

    parent = {v: v for v in vertices}

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for u, v in edges:
        union(u, v)

    components = len({find(v) for v in vertices})
    n = len(vertices)
    m = len(edges)
    beta = m - n + components
    return n, m, components, beta


def forest_from_paths(paths: list[list[int]]) -> tuple[set[int], set[tuple[int, int]]]:
    vertices: set[int] = set()
    edges: set[tuple[int, int]] = set()
    for path in paths:
        vertices.update(path)
        edges.update(path_edges(path))
    return vertices, edges


def check_euler_identity_examples() -> None:
    examples = [
        # One shared trunk, no cycle.
        ([[0, 1, 2, 3]], [[4, 1, 2, 5]]),
        # Two separated shared trunks create one cycle in the union.
        ([[0, 1, 2, 3, 4, 5]], [[9, 1, 2, 7, 4, 5, 10]]),
        # Two components in each path forest, with reuse spread among them.
        (
            [[0, 1, 2, 3, 4], [20, 21, 22, 23]],
            [[8, 1, 2, 6, 4, 7], [30, 21, 22, 31]],
        ),
        # Three disjoint P-runs and two disjoint Q-runs.
        (
            [[0, 1, 2, 3], [10, 11, 12], [20, 21, 22, 23]],
            [[7, 1, 2, 8], [30, 21, 22, 31]],
        ),
    ]

    for p_paths, q_paths in examples:
        vp, ep = forest_from_paths(p_paths)
        vq, eq = forest_from_paths(q_paths)

        np, mp, cp, bp = graph_stats(ep, vp)
        nq, mq, cq, bq = graph_stats(eq, vq)
        assert bp == 0 and bq == 0
        assert cp == len(p_paths)
        assert cq == len(q_paths)

        vi = vp & vq
        ei = ep & eq
        ni, mi, ci, bi = graph_stats(ei, vi)
        assert bi == 0

        vh = vp | vq
        eh = ep | eq
        nh, mh, ch, bh = graph_stats(eh, vh)

        # V-E inclusion-exclusion and the exact FU.10 identity.
        assert nh - mh == (np - mp) + (nq - mq) - (ni - mi)
        assert bh == ch - cp - cq + ci


def check_minimax_identity() -> None:
    for e in (10.0, 100.0, 1e4, 1e10):
        for r in (1.0, 3.0, 20.0, 1000.0):
            root = math.sqrt(r * r + B_STAR * e)
            phi = (B_STAR * e) / (root + r)
            assert phi > 0.0
            s = phi / B_STAR
            cycle = e / s - 2.0 * r
            drift = B_STAR * s
            tol = 1e-11 * max(1.0, phi)
            assert abs(cycle - phi) <= tol
            assert abs(drift - phi) <= tol


def check_asymptotic_coefficients() -> None:
    assert math.isclose(H_STAR, 0.33474798433710024, rel_tol=1e-15)
    assert math.isclose(ALPHA_1, 0.6652520156628998, rel_tol=1e-15)
    assert math.isclose(B_STAR, 0.06456515719047448, rel_tol=1e-15)
    assert math.isclose(K1_CURRENCY, 0.14654709304956395, rel_tol=1e-15)

    # R=o(sqrt(D)) recovers sqrt(alpha*b/2)*sqrt(D).
    for d in (1e12, 1e18, 1e24):
        r = d ** 0.20
        e = (ALPHA_1 / 2.0) * d
        root = math.sqrt(r * r + B_STAR * e)
        phi = (B_STAR * e) / (root + r)
        ratio = phi / math.sqrt(d)
        # convergence is monotone enough at these scales for a conservative check
        assert ratio > 0.90 * K1_CURRENCY
        assert ratio < K1_CURRENCY + 1e-12


def check_z_interpolation() -> None:
    c = ALPHA_1 * B_STAR / 2.0
    previous = None
    for z in (0.0, 0.1, 0.5, 1.0, 2.0, 10.0, 100.0):
        root = math.sqrt(z * z + c)
        # Use the rationalized form to avoid cancellation at large z.
        coeff = c / (root + z)
        assert coeff > 0.0
        if previous is not None:
            assert coeff < previous
        previous = coeff

        if z <= 2.0:
            direct = root - z
            assert math.isclose(coeff, direct, rel_tol=5e-13, abs_tol=1e-15)


def main() -> None:
    check_euler_identity_examples()
    check_minimax_identity()
    check_asymptotic_coefficients()
    check_z_interpolation()
    print("PASS: all-run FREE forest-union certificate")
    print(f"h_* = {H_STAR:.15f}")
    print(f"b_* = {B_STAR:.15f}")
    print(f"alpha_1 = {ALPHA_1:.15f}")
    print(f"K=1 sqrt(D) currency coefficient = {K1_CURRENCY:.15f}")


if __name__ == "__main__":
    main()
