#!/usr/bin/env python3
"""Regression checks for the common-super-swap connectivity note.

This certificate checks only the finite algebra/combinatorics and displayed constants.
It does not replace the cited geometric input theorems.
"""

from fractions import Fraction
from itertools import combinations
import math

S0 = Fraction(791, 320_000_000)


def contact_increment(Q, q, c_dot_err):
    # Worst-case bound from c.w_* <= q/2 + err.
    return Q * (Q - q - 2 * c_dot_err)


def diameter_increment(Q, inward_proj):
    return -2 * Q * inward_proj + Q * Q


def is_connected(n, edges):
    # vertices 0..n-1; root is n-1
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {n - 1}
    stack = [n - 1]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def every_root_cut_crossed(n, edges):
    # Nonempty subsets of non-root vertices must have an edge to complement/root.
    root = n - 1
    verts = list(range(root))
    for mask in range(1, 1 << root):
        S = {verts[i] for i in range(root) if (mask >> i) & 1}
        if not any((u in S) != (v in S) for u, v in edges):
            return False
    return True


def main():
    # 1. Contact opening inequality with a deliberately strict sample margin.
    D = 10**12
    Cq = 31.4e6
    Cw = 9.0e6
    K = Cq + 2 * Cw + 2.0
    Q = K / D
    q = Cq / D
    err = Cw / D
    inc = contact_increment(Q, q, err)
    assert inc > 0

    # 2. Old crossing diameter shortens once the common-axis projection is macroscopic.
    proj = 0.45 * D
    assert diameter_increment(Q, proj) < 0

    # 3. Exhaustively verify: every nonempty root cut crossed iff connected,
    # for every simple graph on up to 5 vertices.
    for n in range(2, 6):
        all_edges = list(combinations(range(n), 2))
        for mask in range(1 << len(all_edges)):
            edges = [e for k, e in enumerate(all_edges) if (mask >> k) & 1]
            assert every_root_cut_crossed(n, edges) == is_connected(n, edges)
            if is_connected(n, edges):
                assert len(edges) >= n - 1

    # 4. Near-unit degree-six angular pigeonhole has strict room.
    assert 2 * math.sin(math.pi / 7) < 1

    # 5. Superdiameter threshold used in the thin upper branch.
    for D0 in [2.0, 10.0, 100.0, 1e6]:
        assert D0 - 1 / (4 * D0) > math.sqrt(D0 * D0 - 1)

    # 6. Displayed density constants.
    m_floor = S0 / 2
    half_type = S0 / 4
    unit_match = S0 / 44
    near_diam_match_coeff = float(S0 / 64) / (3 ** (1 / 8))

    assert abs(float(m_floor) - 1.2359375e-6) < 1e-18
    assert abs(float(half_type) - 6.1796875e-7) < 1e-18
    assert abs(float(unit_match) - 5.617897727272727e-8) < 1e-20
    assert abs(near_diam_match_coeff - 3.366715158259487e-8) < 1e-20

    # 7. Stable form of the upper-witness sign law.
    K2 = 100.0
    D2 = 1e9
    Q2 = K2 / D2
    tau = 1 / (4 * K2)
    xi = tau * Q2
    ell = D2 - xi
    rhs_stable = -xi * (D2 + ell) / (2 * Q2) + Q2 / 2
    assert rhs_stable <= -(tau - 1e-12) * D2

    print("common-super-swap connectivity certificate: PASS")
    print("m/D floor =", float(m_floor))
    print("near-unit matching coefficient =", float(unit_match))
    print("near-diameter D^(1/4) matching coefficient =", near_diam_match_coeff)


if __name__ == "__main__":
    main()
