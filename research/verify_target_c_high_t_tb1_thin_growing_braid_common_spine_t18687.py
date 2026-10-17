#!/usr/bin/env python3
"""Regression checks for the THIN growing-braid common-spine theorem."""

from __future__ import annotations

import itertools
import math
from fractions import Fraction


def check_constants() -> None:
    gamma = Fraction(791, 9_600_000_000)
    p0 = Fraction(1609, 2500)
    tstar = Fraction(6121, 2000)

    # After the two-phase split, fixed-r row coefficient in N scale.
    def kappa_r(r: int) -> Fraction:
        return 3 * p0 / (4 * tstar * (5**r))

    # In D scale use N > (gamma/16-o(1)) D.
    def c_r(r: int) -> Fraction:
        return kappa_r(r) * gamma / 16

    # r=1 must reproduce the existing common-spine theorem.
    assert c_r(1) == Fraction(1_272_719, 7_834_880_000_000_000)
    assert abs(float(c_r(1)) - 1.624426921663127e-10) < 1e-24

    # r=2 is the explicit two-chord crossing-spine coefficient.
    assert c_r(2) == Fraction(1_272_719, 39_174_400_000_000_000)
    assert abs(float(c_r(2)) - 3.248853843326254e-11) < 1e-25

    for r in range(1, 6):
        assert c_r(r + 1) * 5 == c_r(r)


def matching_count(n: int, edges: tuple[tuple[int, int], ...], r: int) -> int:
    count = 0
    for chosen in itertools.combinations(edges, r):
        verts: set[int] = set()
        ok = True
        for u, v in chosen:
            if u in verts or v in verts:
                ok = False
                break
            verts.add(u)
            verts.add(v)
        if ok:
            count += 1
    return count


def check_greedy_matching_bound() -> None:
    # Exhaust every simple graph through five vertices.
    for n in range(2, 6):
        all_edges = tuple(itertools.combinations(range(n), 2))
        for mask in range(1 << len(all_edges)):
            edges = tuple(e for i, e in enumerate(all_edges) if (mask >> i) & 1)
            E = len(edges)
            deg = [0] * n
            for u, v in edges:
                deg[u] += 1
                deg[v] += 1
            Delta = max(deg, default=0)
            for r in range(1, min(3, n // 2) + 1):
                ordered_lb = 1
                for j in range(r):
                    ordered_lb *= max(E - 2 * j * Delta, 0)
                lhs = matching_count(n, edges, r) * math.factorial(r)
                assert lhs >= ordered_lb


def check_tuple_pigeonhole() -> None:
    # Small finite incidence sanity for the abstract count:
    # total row-matching-train incidences / candidate (matching,train) pairs
    # cannot exceed the maximum codegree.
    blockers = tuple(range(4))
    trains = tuple(range(3))
    r = 2
    matchings = tuple(itertools.combinations(blockers, r))

    row_types = []
    for ms_mask in range(1, 1 << len(matchings)):
        ms = tuple(m for i, m in enumerate(matchings) if (ms_mask >> i) & 1)
        for bs_mask in range(1, 1 << len(trains)):
            bs = tuple(b for i, b in enumerate(trains) if (bs_mask >> i) & 1)
            row_types.append((ms, bs))

    # Sample all pairs of row types; exhaustive over longer products is unnecessary.
    for row1 in row_types:
        for row2 in row_types:
            counts = {(m, b): 0 for m in matchings for b in trains}
            total = 0
            for ms, bs in (row1, row2):
                for m in ms:
                    for b in bs:
                        counts[(m, b)] += 1
                        total += 1
            max_codeg = max(counts.values())
            candidates = len(matchings) * len(trains)
            assert max_codeg * candidates >= total


def check_diagonal_example() -> None:
    # A concrete admissible growth rate illustrates the asymptotic conditions
    # when the hidden o(1) terms permit it. The proof itself uses a slower
    # diagonal if necessary to absorb those errors.
    for exponent in (40, 80, 120):
        D = 10.0**exponent
        r = max(1, int(math.log(math.log(D))))
        assert r / math.log(D) < 0.1
        assert r * r * D ** (-0.25) < 1e-2
        # 5^r is subpolynomial for this choice.
        assert math.log(5.0**r) / math.log(D) < 0.1


def main() -> None:
    check_constants()
    check_greedy_matching_bound()
    check_tuple_pigeonhole()
    check_diagonal_example()
    print("PASS: THIN growing-braid common-spine certificate")


if __name__ == "__main__":
    main()
