#!/usr/bin/env python3
"""Hostile finite search for the exact-phase nested-bundle candidate.

Universe: the 16 listed rational-circle vertices (radius 25), their eight
antipodal diameters, every nonempty cyclic layer-block composition for m=2,3,
and all rotations. Encoded cut conditions: all diameter weights positive,
zero transverse cut resultants, positive horizontal cut resultants, full rank.
Omitted: actual contacts, source KKT equilibrium, a grid, and global optimality.
SciPy LP discovers feasible points. Every reported point is independently checked
using Fraction; LP-infeasible cases are not certified. A zero counterexample count
is not exhaustive mathematical exclusion and is not a proof of the theorem.
"""

from fractions import Fraction as F
from itertools import combinations

import numpy as np
from scipy.optimize import linprog

from verify_target_c_gap_bundle_regression_2026_10_01 import rank


POINTS = [(24, 7), (20, 15), (15, 20), (7, 24), (-7, 24), (-15, 20),
          (-20, 15), (-24, 7), (-24, -7), (-20, -15), (-15, -20),
          (-7, -24), (7, -24), (15, -20), (20, -15), (24, -7)]


def run(m):
    word = list(range(m + 1)) + list(range(m - 1, 0, -1))
    attempted = feasible = uncertified = 0
    for div in combinations(range(1, 16), 2 * m - 1):
        ends = (0,) + div + (16,)
        raw = [j for j, a, b in zip(word, ends, ends[1:]) for _ in range(b - a)]
        for rot in range(16):
            layers = raw[-rot:] + raw[:-rot] if rot else raw
            rows, xrows, edges = [], [], []
            for a in range(8):
                b = a + 8
                if layers[a] > layers[b]:
                    a, b = b, a
                p, q = layers[a], layers[b]
                rx, ry = (POINTS[b][i] - POINTS[a][i] for i in (0, 1))
                indicator = [int(p < i <= q) for i in range(1, m + 1)]
                rows.append([ry * x for x in indicator])
                xrows.append([rx * x for x in indicator])
                edges.append((p, q, rx, ry))
            if np.linalg.matrix_rank(np.array(rows).T) < m:
                continue
            attempted += 1
            result = linprog(np.zeros(8), A_eq=np.array(rows).T, b_eq=np.zeros(m),
                             A_ub=-np.array(xrows).T, b_ub=-np.ones(m),
                             bounds=[(1, None)] * 8, method="highs")
            if not result.success:
                continue
            beta = [F(float(x)).limit_denominator(10**6) for x in result.x]
            transverse = [sum(beta[j] * rows[j][i] for j in range(8)) for i in range(m)]
            axial = [sum(beta[j] * xrows[j][i] for j in range(8)) for i in range(m)]
            if any(transverse) or min(axial) < 1 or min(beta) < 1:
                uncertified += 1
                continue
            assert rank(rows) == m
            feasible += 1
            assert all(layers[i] == 0 for i, p in enumerate(POINTS) if p[0] == -24)
            assert all(layers[i] == m for i, p in enumerate(POINTS) if p[0] == 24)
            chains = []
            for sign in (1, -1):
                chain = {(p, q) for p, q, rx, ry in edges if p < q and sign * ry > 0}
                for a, b in combinations(chain, 2):
                    assert ((a[0] <= b[0] and a[1] >= b[1]) or
                            (b[0] <= a[0] and b[1] >= a[1])), (layers, edges, beta)
                chains.append(chain)
            assert chains[0] == chains[1]
            chain = sorted(chains[0], key=lambda e: e[1] - e[0], reverse=True)
            assert len(chain) == m and chain[0] == (0, m)
            assert all((a[1] - a[0]) == (b[1] - b[0]) + 1
                       for a, b in zip(chain, chain[1:]))
            ratios = []
            for p, q in chain:
                members = [(j, rx, ry) for j, (a, b, rx, ry) in enumerate(edges)
                           if (a, b) == (p, q)]
                assert sum(beta[j] * ry for j, rx, ry in members) == 0
                w = sum(beta[j] * ry for j, rx, ry in members if ry > 0)
                k = sum(beta[j] * rx for j, rx, ry in members)
                assert w > 0 and k > 0
                ratios.append(k / w)
            assert all(a > b for a, b in zip(ratios, ratios[1:]))
            assert len(set(axial)) == m
    print(f"m={m}: LP_attempts={attempted}; exact_feasible={feasible}; "
          f"uncertified_LP_success={uncertified}; counterexamples=0", flush=True)


if __name__ == "__main__":
    for m in (2, 3):
        run(m)
