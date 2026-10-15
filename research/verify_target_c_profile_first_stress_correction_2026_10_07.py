#!/usr/bin/env python3
"""Independently verify exact first pinned-stress corrections.

Coefficients were discovered by floating linear optimization, rounded to
rationals, then corrected by exact linear equations. This verifier uses
no numerical optimizer or tolerance. It proves only the listed exact
first corrections and ranks, not the analytic stress continuation.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import verify_target_c_sorted_rate_packets_2026_10_06 as s


def rad(p):
    return max(abs(p[0]), abs(p[1]), abs(p[0]+p[1]))


def first(order):
    result = {(0, 0): (F(0), F(0))}
    for r in range(1, len(order)+1):
        alpha = sum(order[:r])
        for j in range(r+1):
            value = -sum(sorted(order[:r])[:j])
            velocity = (F(value-alpha, 3), F(value+2*alpha, 3))
            point = (r-j, j)
            for _ in range(6):
                if point in result:
                    assert result[point] == velocity
                result[point] = velocity
                point, velocity = s.rotate(point), s.rotate(velocity)
    return result


def case(data):
    order = data['order']
    m = len(order)
    assert len(set(order)) == m and sorted(order) == sorted(-a for a in order)
    velocity = first(order)
    moving = sorted(p for p in velocity if rad(p) < m)
    assert moving == [tuple(p) for p in data['moving']]
    col = {p: i for i, p in enumerate(moving)}
    n = 2*len(moving)
    rows = []
    derivatives = []
    pairs = []
    lambda0 = []
    for p, q in combinations(velocity, 2):
        delta = (p[0]-q[0], p[1]-q[1])
        if delta[0]**2+delta[0]*delta[1]+delta[1]**2 != 1:
            continue
        if p not in col and q not in col:
            continue
        dv = (velocity[p][0]-velocity[q][0], velocity[p][1]-velocity[q][1])
        margin = 2*delta[0]*dv[0]+delta[0]*dv[1]+delta[1]*dv[0]+2*delta[1]*dv[1]
        assert margin >= 0
        if margin:
            continue
        pairs.append((p, q))
        weight = F(0)
        if rad(p) == rad(q):
            weight = F(1, 1000000)
        elif p[0]*q[1] == p[1]*q[0] and p[0]*q[0]+p[1]*q[1] >= 0:
            weight = 1+F(min(rad(p), rad(q)), 1000000)
        lambda0.append(weight)
        row = [0]*n
        derivative = [F(0)]*n
        for point, sign in ((p, 1), (q, -1)):
            if point in col:
                k = 2*col[point]
                row[k] += sign*(2*delta[0]+delta[1])
                row[k+1] += sign*(delta[0]+2*delta[1])
                derivative[k] += sign*(2*dv[0]+dv[1])
                derivative[k+1] += sign*(dv[0]+2*dv[1])
        rows.append(row)
        derivatives.append(derivative)
    assert pairs == [(tuple(p), tuple(q)) for p, q in data['pairs']]
    assert lambda0 == [F(v) for v in data['lambda0']]
    kappa = [F(v) for v in data['kappa']]
    assert len(kappa) == len(rows)
    weak = [k for k, value in enumerate(lambda0) if not value]
    assert all(kappa[k] > 0 for k in weak)
    assert min(kappa[k] for k in weak) == F(data['min_weak_kappa'])
    for j in range(n):
        assert sum(weight*row[j] for weight, row in zip(lambda0, rows)) == 0
        assert sum(k*row[j]+weight*d[j] for k, row, weight, d
                   in zip(kappa, rows, lambda0, derivatives)) == 0
    basis = data['rank_basis']
    assert len(set(basis)) == len(basis) == n
    rank = s.rank_mod([rows[k] for k in basis], n)
    assert rank == n
    return {'order': order, 'unit_rows': len(rows), 'exact_full_rank': rank,
            'weak_rows_positive': len(weak), 'minimum_weak_kappa': data['min_weak_kappa'],
            'exact_zero_order_force_checks': n, 'exact_first_order_force_checks': n,
            'lambda1_normalization': 'sqrt(3) times kappa'}


def main():
    path = Path(__file__).with_name('target_c_profile_first_stress_correction_input_2026_10_07.json')
    raw = path.read_bytes()
    print(json.dumps({'classification': 'exact finite pinned-stress first corrections',
                      'input_sha256': hashlib.sha256(raw).hexdigest(),
                      'cases': [case(c) for c in json.loads(raw)['cases']],
                      'scope': 'listed first-order identities and rank only'}, sort_keys=True))


if __name__ == '__main__':
    main()
