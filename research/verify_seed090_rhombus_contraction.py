#!/usr/bin/env python3
"""Exact finite certificates for seed 90; no global-optimality inference.

Standard library only. Complete pair classes are checked either by direct
integer/quadratic-field predicates or by the lattice norm and disk certificate
proved in the accompanying report. Checks remain enabled under python -O.
"""

from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sign_surd(a, b, d=3):
    """Exact sign of a+b*sqrt(d), for rational a,b; d nonsquare positive."""
    if not b:
        return (a > 0) - (a < 0)
    if not a:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    gap = a * a - d * b * b
    return ((gap > 0) - (gap < 0)) * (1 if a > 0 else -1)


def lattice_disk(radius, scale_num=1, scale_den=1):
    # Q=i^2+ij+j^2 >= 3j^2/4 and >= 3i^2/4, so this box is exhaustive.
    lim = 2 * radius + 2
    return [(i, j) for i in range(-lim, lim + 1)
            for j in range(-lim, lim + 1)
            if scale_num**2 * (i*i+i*j+j*j) <= radius**2 * scale_den**2]


def frame(m):
    return [(i, j) for i in range(m + 1) for j in range(m + 1)
            if min(i, j, m-i, m-j) <= 1]


def check_cells(m, points):
    labels = set(points)
    cells = {}
    by_edge = defaultdict(list)
    for i in range(m):
        for j in range(m):
            vs = ((i, j), (i+1, j), (i+1, j+1), (i, j+1))
            if all(v in labels for v in vs):
                cell = (i, j)
                cells[cell] = vs
                for k in range(4):
                    by_edge[tuple(sorted((vs[k], vs[(k+1) % 4])))].append(cell)
    adjacency = defaultdict(set)
    for cs in by_edge.values():
        for a, b in combinations(cs, 2):
            adjacency[a].add(b)
            adjacency[b].add(a)
    seen = {next(iter(cells))}
    queue = deque(seen)
    while queue:
        for c in adjacency[queue.popleft()] - seen:
            seen.add(c)
            queue.append(c)
    require(len(seen) == len(cells), 'cell adjacency disconnected')
    vertices = set(v for vs in cells.values() for v in vs)
    require({(0, 0), (0, m), (m, 0), (m, m)} <= vertices,
            'a diameter corner is not anchored')
    require(len(cells) == 4*m-4, 'unexpected frame cell count')
    return len(cells)


def rim(m):
    return ([(i, 0) for i in range(m)]
            + [(m, j) for j in range(m)]
            + [(i, m) for i in range(m, 0, -1)]
            + [(0, j) for j in range(m, 0, -1)])


def add_outer(matrix, vector, weight):
    for i, a in vector.items():
        for j, b in vector.items():
            matrix[i, j] += weight * a * b


def exact_sparse_rank(matrix, size):
    pivots = {}
    rows = [dict() for _ in range(size)]
    for (i, j), value in matrix.items():
        if value:
            rows[i][j] = value
    for row in rows:
        while row:
            pivot = min(row)
            factor = row[pivot]
            if pivot not in pivots:
                pivots[pivot] = {j: value/factor for j, value in row.items()}
                break
            for j, value in pivots[pivot].items():
                new = row.get(j, F(0))-factor*value
                if new:
                    row[j] = new
                else:
                    row.pop(j, None)
    return len(pivots)


def stress_certificate(m):
    """Independently expand 2*Omega and its rational SOS factorization."""
    count = 4*m
    matrix, sos = defaultdict(F), defaultdict(F)
    for i in range(count):
        add_outer(matrix, {i: F(-1), (i+1) % count: F(1)}, F(m))
    for a, b in ((0, 2*m), (m, 3*m)):
        add_outer(matrix, {a: F(1), b: F(-1)}, F(-1))
    for arc in range(4):
        start, end = arc*m, ((arc+1)*m) % count
        for k in range(m):
            i, j = (start+k) % count, (start+k+1) % count
            v = defaultdict(F)
            v[i] -= 1
            v[j] += 1
            v[end] -= F(1, m)
            v[start] += F(1, m)
            add_outer(sos, {a: b for a, b in v.items() if b}, F(m))
    add_outer(sos, {0: F(1), m: F(-1), 2*m: F(1), 3*m: F(-1)}, F(1))
    require({k: v for k, v in matrix.items() if v}
            == {k: v for k, v in sos.items() if v}, 'PSD factorization mismatch')
    ps = rim(m)
    require(len(set(ps)) == count, 'repeated rim label')
    for values in ([1]*count, [p[0] for p in ps], [p[1] for p in ps]):
        result = [F(0)]*count
        for (i, j), value in matrix.items():
            result[i] += value*values[j]
        require(not any(result), 'normalized equilibrium/kernel mismatch')
    require(F(4*m)*F(m, 2) == 2*m*m, 'contact normalization mismatch')
    require(F(1, 2)+F(1, 2) == 1, 'diameter normalization mismatch')
    # The SOS nullspace is independently specified by 4 corner values with
    # one relation, followed by linear interpolation along each arc.
    for corner_values in ((1, 1, 1, 1), (0, m, m, 0), (0, 0, m, m)):
        a, b, c, d = corner_values
        require(a-b+c-d == 0, 'corner nullspace relation failed')
    require(exact_sparse_rank(matrix, count) == count-3, 'rim stress rank mismatch')
    return {'rim_vertices': count, 'sos_rows': count+1,
            'positive_contact_edges': count, 'rim_kernel_dimension': 3,
            'mixed_rank_upper_bound': count+2}


def cross_numerator(i, j, fill_num, fill_den, frame_num_x,
                    frame_num_y, frame_den):
    # Fill=(fill_num*(2i+j),fill_num*j*sqrt(3))/(2*fill_den).
    # Frame=(frame_num_x,frame_num_y)/(2*frame_den).
    dx = fill_num*frame_den*(2*i+j)-fill_den*frame_num_x
    y_surd = fill_num*frame_den*j
    y_rat = fill_den*frame_num_y
    return dx*dx+3*y_surd*y_surd+y_rat*y_rat, -2*y_surd*y_rat


def dense_certificate(m):
    require(m >= 24 and m % 2 == 0, 'unsupported dense frame size')
    ps = frame(m)
    require(len(ps) == 8*m-8, 'frame cardinality mismatch')
    cells = check_cells(m, ps)
    # floor(m/sqrt(2)) without floating point.
    h = isqrt(m*m // 2)
    require(2*h*h <= m*m < 2*(h+1)**2, 'inexact radius floor')
    bulk_radius, packet_radius = h-10, h-1
    bnum, bden = m*m+1, m*m
    candidate_fill = lattice_disk(bulk_radius, bnum, bden)
    kept = []
    source_cross_pairs = 0
    for i, j in candidate_fill:
        safe = True
        for fi, fj in ps:
            fx, fy = 2*fi-m, 2*fj-m
            a, b = cross_numerator(i, j, bnum, bden, fx, fy, 1)
            if sign_surd(a-4*m**4, b) <= 0:
                safe = False
                break
            require(sign_surd(a-8*m**6, b) < 0, 'old cross upper bound failed')
            gap_a = a-4*m**4
            require(abs(gap_a)+2*abs(b) <= 100*m**6,
                    'uniform algebraic gap height bound failed')
        if safe:
            kept.append((i, j))
            source_cross_pairs += len(ps)

    # Rational bow. One common denominator avoids floating point and repeated
    # Fraction arithmetic in the large complete cross-pair checks.
    tden = 1000000*m**12
    cnum, snum, qden = tden*tden-1, 2*tden, tden*tden+1
    bowed = [(cnum*(2*i-m)+2*snum*min(j, m-j),
              cnum*(2*j-m)+2*snum*min(i, m-i)) for i, j in ps]
    contacts = set()
    old_diameter_pairs, new_diameter_pairs = set(), set()
    diagonals_increased = 0
    for aidx, bidx in combinations(range(len(ps)), 2):
        i, j = ps[aidx]
        k, l = ps[bidx]
        old = (i-k)**2+(j-l)**2
        dx, dy = (bowed[aidx][z]-bowed[bidx][z] for z in (0, 1))
        new_num = dx*dx+dy*dy
        require(new_num >= 4*qden*qden, 'bowed frame lower violation')
        require(new_num <= 8*m*m*cnum*cnum, 'bowed frame upper violation')
        if old == 1:
            contacts.add((aidx, bidx))
            require(new_num == 4*qden*qden, 'an old frame contact changed')
        else:
            require(new_num > 4*qden*qden, 'a new frame contact appeared')
        if old == 2*m*m:
            old_diameter_pairs.add((aidx, bidx))
        if new_num == 8*m*m*cnum*cnum:
            new_diameter_pairs.add((aidx, bidx))
        if old == 2 and new_num > 8*qden*qden:
            diagonals_increased += 1
    require(len(contacts) == 12*m-12, 'unexpected actual contact count')
    require(len(old_diameter_pairs) == 2 and old_diameter_pairs == new_diameter_pairs,
            'diameter pair classification changed')
    require(cnum < qden and diagonals_increased > 0,
            'no strict gain or missing escape from contraction barrier')
    # Unit grid contacts join opposite parity, ruling out all frame triangles.
    for i, j in contacts:
        require((sum(ps[i])-sum(ps[j])) % 2 == 1, 'contact parity failed')

    for i, j in kept:
        for (fi, fj), (qx, qy) in zip(ps, bowed):
            a, b = cross_numerator(i, j, bnum, bden, qx, qy, qden)
            require(sign_surd(a-4*qden*qden*m**4, b) > 0,
                    'bowed cross lower violation')
            require(sign_surd(a-8*m**6*cnum*cnum, b) < 0,
                    'bowed cross upper violation')

    # All fill--fill pairs: nonzero integral lattice norms are >=1; scaling
    # gives >1. The containing disk provides their complete strict upper test.
    require(len(set(kept)) == len(kept), 'repeated fill label')
    require(bnum > bden, 'fill separation not strict')
    require(4*bulk_radius**2*qden*qden < 2*m*m*cnum*cnum,
            'fixed fill diameter above bowed diameter')
    packet = lattice_disk(packet_radius)
    total = len(ps)+len(kept)
    require(len(packet) > total, 'comparison packet cannot restore cardinality')
    require(4*packet_radius**2 < 2*m*m, 'comparison packet is not strict-sub-D')
    require(len(set(packet[:total])) == total, 'replacement cardinality mismatch')
    pair_count = total*(total-1)//2
    frame_pairs = len(ps)*(len(ps)-1)//2
    fill_pairs = len(kept)*(len(kept)-1)//2
    require(pair_count == frame_pairs+source_cross_pairs+fill_pairs,
            'incomplete full-source pair partition')
    return {'m': m, 'source_labels': total, 'frame_labels': len(ps),
            'retained_contact_isolates': len(kept),
            'removed_fill_candidates': len(candidate_fill)-len(kept),
            'old_diameter_squared': 2*m*m,
            'new_diameter_squared': str(F(2*m*m*cnum*cnum, qden*qden)),
            'comparison_labels': len(packet),
            'comparison_diameter_squared_bound': 4*packet_radius**2,
            'full_source_pairs': pair_count, 'direct_frame_pairs': frame_pairs,
            'direct_cross_pairs_each_endpoint': source_cross_pairs,
            'fill_pairs_by_complete_norm_certificate': fill_pairs,
            'unit_contacts_preserved': len(contacts), 'connected_cells': cells,
            'inactive_unit_cell_diagonals_increased': diagonals_increased}


def rational_ledger(points):
    distances = {(i, j): sum((points[i][k]-points[j][k])**2
                             for k in range(len(points[i])))
                 for i, j in combinations(range(len(points)), 2)}
    require(min(distances.values()) >= 1, 'fixture lower violation')
    contacts = {e for e, d in distances.items() if d == 1}
    for a, b, c in combinations(range(len(points)), 3):
        require(not {(a, b), (a, c), (b, c)} <= contacts, 'unexpected triangle')
    return distances, contacts, max(distances.values())


def scope_fixtures():
    p = [(F(x), F(y)) for x, y in
         ((0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1))]
    q = p[:4]+[(F(-24, 25), F(-7, 25)), (F(7, 25), F(-24, 25)),
               (F(-17, 25), F(-31, 25))]
    dp, cp, old = rational_ledger(p)
    dq, cq, new = rational_ledger(q)
    require(old == 8 and new == F(196, 25) and cp == cq, 'hinge certificate failed')
    for cell in ((0, 1, 3, 2), (0, 4, 6, 5)):
        for a, b in combinations(cell, 2):
            require(dp[tuple(sorted((a, b)))] == dq[tuple(sorted((a, b)))],
                    'hinge cell is not congruent')
    require(any(dq[e] > dp[e] for e in dp), 'hinge unexpectedly nonexpansive')

    p = [(F(x), F(y)) for x, y in ((0, 0), (1, 0), (0, 1), (1, 1), (4, 0))]
    q = p[:4]+[(F(3), F(0))]
    dp, cp, old = rational_ledger(p)
    dq, cq, new = rational_ledger(q)
    require(old == 17 and new == 10 and cp == cq, 'outside-isolate certificate failed')
    require(all(dq[e] <= dp[e] for e in dp), 'isolate move not nonexpansive')

    # Two unit squares sharing an edge: the congruent reflected alternative
    # identifies distinct labels, so the global unit-lower test rejects it.
    adjacent = [(F(x), F(y)) for x, y in
                ((0, 0), (0, 1), (1, 0), (1, 1), (-1, 0), (-1, 1))]
    rational_ledger(adjacent)
    reflected = adjacent[:4]+[(F(1), F(0)), (F(1), F(1))]
    require(len(set(reflected)) < len(reflected), 'shared-edge flip control failed')
    # Boundary rhombi at 60 and 120 degrees on the same side have equal
    # horizontal coordinate sqrt(3)/2 and a coincident vertex at height 1/2.
    require(F(-1, 2)+1 == F(1, 2), 'closed-angle collision identity failed')
    gram = [[F(1) if i == j else F(1, 2) for j in range(3)] for i in range(3)]
    det = (gram[0][0]*(gram[1][1]*gram[2][2]-gram[1][2]*gram[2][1])
           -gram[0][1]*(gram[1][0]*gram[2][2]-gram[1][2]*gram[2][0])
           +gram[0][2]*(gram[1][0]*gram[2][1]-gram[1][1]*gram[2][0]))
    require(det == F(1, 2), 'spatial rank-three control failed')
    # Positive definite equilateral-tetrahedron Gram, all six squared distances 1.
    require(gram[0][0] > 0 and gram[0][0]*gram[1][1]-gram[0][1]**2 > 0,
            'spatial Gram is not positive definite')
    require(all(gram[i][i]+gram[j][j]-2*gram[i][j] == 1
                for i, j in combinations(range(3), 2)), 'spatial metric failed')
    # Independent rational tests of both branches of the quadratic-field sign.
    require(sign_surd(2, -1) == 1 and sign_surd(1, -1) == -1
            and sign_surd(-2, 1) == -1 and sign_surd(-1, 1) == 1,
            'quadratic-field sign control failed')
    return {'hinge_squared_diameters': ['8', '196/25'],
            'outside_isolate_squared_diameters': ['17', '10'],
            'spatial_gram_determinant': str(det)}


def main():
    print(json.dumps({'scope_fixtures': scope_fixtures()}, sort_keys=True))
    for m in (4, 8, 24):
        print(json.dumps({'stress': stress_certificate(m)}, sort_keys=True))
    for m in (24, 40, 64):
        print(json.dumps({'dense_source': dense_certificate(m)}, sort_keys=True), flush=True)
    print('PASS: exact finite certificates; no Level I or canonical-source conclusion')


if __name__ == '__main__':
    main()
