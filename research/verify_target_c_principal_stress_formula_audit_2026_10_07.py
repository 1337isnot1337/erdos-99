#!/usr/bin/env python3
"""Exact finite checks of the explicit principal-stress correction formula.

This checks four listed symmetric profiles. The all-M force calculation is
proved in the independent audit artifact; finite cases do not imply it.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import verify_target_c_sorted_rate_packets_2026_10_06 as s

PROFILES = (
    (5, 0, -5),
    (7, 2, -2, -7),
    (11, 3, 0, -3, -11),
    (13, 8, 1, -1, -8, -13),
)


def rad(p):
    return max(abs(p[0]), abs(p[1]), abs(p[0] + p[1]))


def add_rotated(edges, p, q):
    for _ in range(6):
        edges.add(frozenset((p, q)))
        p, q = s.rotate(p), s.rotate(q)


def first_velocity(order):
    m = len(order)
    velocity = {(0, 0): (F(0), F(0))}
    for r in range(1, m + 1):
        alpha = sum(order[:r])
        for j in range(r + 1):
            value = -sum(sorted(order[:r])[:j])
            d = (F(value - alpha, 3), F(value + 2 * alpha, 3))
            p = (r - j, j)
            for _ in range(6):
                if p in velocity:
                    assert velocity[p] == d
                velocity[p] = d
                p, d = s.rotate(p), s.rotate(d)
    return velocity


def check(profile):
    order = tuple(F(x) for x in profile)
    m = len(order)
    assert len(set(order)) == m
    assert all(order[i] > order[i + 1] for i in range(m - 1))
    assert order == tuple(-x for x in reversed(order))
    velocity = first_velocity(order)
    moving = {p for p in velocity if rad(p) < m}
    columns = {p: i for i, p in enumerate(sorted(moving))}
    ncols = 2 * len(columns)

    ring_edges, axis_edges, diagonal_edges = set(), set(), set()
    for r in range(1, m + 1):
        for j in range(r):
            add_rotated(ring_edges, (r - j, j), (r - j - 1, j + 1))
    for r in range(m):
        add_rotated(axis_edges, (r, 0), (r + 1, 0))
    for a in range(1, m):
        for b in range(m - a):
            add_rotated(diagonal_edges, (a, b), (a, b + 1))

    rows, derivatives, lambda0, kappa, weak_flags = [], [], [], [], []
    active = set()
    for p, q in combinations(velocity, 2):
        delta = (p[0] - q[0], p[1] - q[1])
        if delta[0] ** 2 + delta[0] * delta[1] + delta[1] ** 2 != 1:
            continue
        if p not in moving and q not in moving:
            continue
        dv = (velocity[p][0] - velocity[q][0],
              velocity[p][1] - velocity[q][1])
        margin = (2 * delta[0] * dv[0] + delta[0] * dv[1]
                  + delta[1] * dv[0] + 2 * delta[1] * dv[1])
        assert margin >= 0
        if margin:
            continue
        edge = frozenset((p, q))
        active.add(edge)
        categories = [edge in ring_edges, edge in axis_edges,
                      edge in diagonal_edges]
        assert sum(categories) == 1
        if categories[0]:
            lam, kap, is_weak = F(0), F(0), False
        elif categories[1]:
            r = min(rad(p), rad(q))
            lam, kap, is_weak = F(1), (order[r] - order[0]) / 3, False
        else:
            lam, is_weak = F(0), True
            # Rotate the oriented edge until it is (a,b)->(a,b+1).
            pp, qq = p, q
            index = None
            for _ in range(6):
                if qq == (pp[0], pp[1] + 1) and pp[0] >= 1:
                    index = pp[0]
                    break
                if pp == (qq[0], qq[1] + 1) and qq[0] >= 1:
                    index = qq[0]
                    break
                pp, qq = s.rotate(pp), s.rotate(qq)
            assert index is not None
            kap = F(2, 3) * (order[index - 1] - order[index])
            assert kap > 0

        row, derivative = [0] * ncols, [F(0)] * ncols
        for point, sign in ((p, 1), (q, -1)):
            if point not in columns:
                continue
            j = 2 * columns[point]
            row[j] += sign * (2 * delta[0] + delta[1])
            row[j + 1] += sign * (delta[0] + 2 * delta[1])
            derivative[j] += sign * (2 * dv[0] + dv[1])
            derivative[j + 1] += sign * (dv[0] + 2 * dv[1])
        rows.append(row)
        derivatives.append(derivative)
        lambda0.append(lam)
        kappa.append(kap)
        weak_flags.append(is_weak)

    assert active <= ring_edges | axis_edges | diagonal_edges
    assert len(active) == 6 * m * m == len(rows)
    weak = [i for i, is_weak in enumerate(weak_flags) if is_weak]
    assert weak and all(kappa[i] > 0 for i in weak)
    assert min(kappa[i] for i in weak) == F(2, 3) * min(
        order[i] - order[i + 1] for i in range(m - 1)
    )
    for j in range(ncols):
        assert sum(w * row[j] for w, row in zip(lambda0, rows)) == 0
        assert sum(k * row[j] + w * d[j]
                   for k, row, w, d in zip(kappa, rows, lambda0, derivatives)) == 0
    rank = s.rank_mod(rows, ncols)
    assert rank == ncols
    return {
        'profile': list(profile),
        'M': m,
        'moving_columns': ncols,
        'active_rows': len(active),
        'strong_ring_or_axis_rows': len(active) - len(weak),
        'weak_diagonal_rows': len(weak),
        'minimum_kappa': str(min(kappa[i] for i in weak)),
        'exact_zero_order_equilibrium': True,
        'exact_first_correction_equilibrium': True,
        'modular_full_column_rank': rank,
    }


def main():
    print(json.dumps({
        'classification': 'exact finite checks of explicit stress correction formula',
        'cases': [check(profile) for profile in PROFILES],
        'scope': 'four fixed integer profiles; no universal proof or uniform onset',
    }, sort_keys=True))


if __name__ == '__main__':
    main()
