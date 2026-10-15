#!/usr/bin/env python3
"""Exact actual-unit sources for outer-train determination and marked-face rank.

All pairs, contacts, pinned equilibrium and ranks are exact rational checks.
The pins include collinear boundary vertices and are not all actual diameter
endpoints. These packets certify the finite angular contract, not canonical
stress, global optimality, Groemer compactness or asymptotic depletion.
"""
from fractions import Fraction as F
from itertools import combinations, product

from verify_target_c_global_face_return_quotas_2026_10_04 import (
    adjacency, cross, edge, elimination, face_walks, sub,
)


def packet(height, t):
    assert height >= 2 and 0 < t < F(1, 10)
    a = 2*t/(1+t*t)
    b = (1-t*t)/(1+t*t)
    positions = {}
    for j in range(height+1):
        y = F(0) if j == 0 else b if j == 1 else 2*b+j-2
        for i in range(3):
            shift = a if j == 1 and i > 0 else -a if j == 1 else F(0)
            positions[3*j+i] = (F(i)+shift, y)
    vertices = set(positions)
    contacts = set()
    diameter2 = F(0)
    diameter_pairs = set()
    checks = 0
    for x, y in combinations(sorted(vertices), 2):
        r = sub(positions[y], positions[x])
        d2 = r[0]*r[0]+r[1]*r[1]
        assert d2 >= 1, (height, t, x, y, d2)
        if d2 == 1:
            contacts.add(edge(x, y))
        if d2 > diameter2:
            diameter2, diameter_pairs = d2, {(x, y)}
        elif d2 == diameter2:
            diameter_pairs.add((x, y))
        checks += 1
    expected = {
        edge(3*j+i, 3*j+i+1) for j in range(height+1) for i in range(2)
    } | {
        edge(3*j+i, 3*(j+1)+i) for j in range(height) for i in range(3)
    }
    expected.remove(edge(3, 4))
    assert contacts == expected
    assert len(contacts) == 5*height+1
    adj = adjacency(vertices, contacts)
    assert not any(adj[x] & adj[y] for x, y in contacts)
    assert (positions[4][0]-positions[3][0])**2 == (1+2*a)**2 > 1

    walks = face_walks(vertices, contacts, positions)
    outer = next(w for w, area2 in walks if area2 < 0)
    bounded = [w for w, area2 in walks if area2 > 0]
    exceptional = [w for w in bounded if len(w) != 4]
    assert len(exceptional) == 1 and len(exceptional[0]) == 6
    for w in exceptional:
        assert all(cross(sub(positions[w[(i+1)%len(w)]], positions[w[i]]),
                         sub(positions[w[(i+2)%len(w)]], positions[w[(i+1)%len(w)]])) > 0
                   for i in range(len(w)))

    pins = set(outer)
    free = vertices-pins
    assert free == {3*j+1 for j in range(1, height)}
    assert pins-{v for e in diameter_pairs for v in e}
    weights = {e: F(1) for e in contacts}
    weights[edge(4, 5)] = 2*a
    weights[edge(6, 7)] = 1+a
    for j in range(2, height):
        weights[edge(3*j+1, 3*(j+1)+1)] = b
    assert all(weight > 0 for weight in weights.values())
    for v in free:
        resultant = [F(0), F(0)]
        for w in adj[v]:
            r = sub(positions[w], positions[v])
            for coordinate in range(2):
                resultant[coordinate] += weights[edge(v, w)]*r[coordinate]
        assert resultant == [0, 0]

    parent = {e: e for e in contacts}

    def root(e):
        while parent[e] != e:
            e = parent[e]
        return e

    def join(e, f):
        x, y = root(e), root(f)
        parent[max(x, y)] = min(x, y)

    for w in bounded:
        if len(w) == 4:
            assert (positions[w[0]][0]+positions[w[2]][0],
                    positions[w[0]][1]+positions[w[2]][1]) == (
                        positions[w[1]][0]+positions[w[3]][0],
                        positions[w[1]][1]+positions[w[3]][1])
            es = [edge(w[i], w[(i+1)%4]) for i in range(4)]
            join(es[0], es[2])
            join(es[1], es[3])
    train_roots = sorted({root(e) for e in contacts})
    train_index = {tr: i for i, tr in enumerate(train_roots)}
    outer_edges = {edge(outer[i], outer[(i+1)%len(outer)]) for i in range(len(outer))}
    outer_trains = {root(e) for e in outer_edges}

    n = len(vertices)
    contact_rows = []
    for x, y in sorted(contacts):
        r = sub(positions[y], positions[x])
        row = [F(0)]*(2*n)
        for v, sign in ((x, -1), (y, 1)):
            row[2*v], row[2*v+1] = sign*r[0], sign*r[1]
        contact_rows.append(row)
    _, pivots = elimination(contact_rows, 2*n)
    rank_c = len(pivots)
    assert rank_c == len(contacts)
    sigma_c = len(contacts)-rank_c
    flex_mod_trans = 2*n-rank_c-2

    # Exact pinned rank: every free coordinate is fixed when outer pins are.
    free_columns = [2*v+i for v in sorted(free) for i in range(2)]
    _, pinned_pivots = elimination(
        [[row[c] for c in free_columns] for row in contact_rows], len(free_columns)
    )
    assert len(pinned_pivots) == len(free_columns)

    rates = []
    for tr in sorted(outer_trains):
        x, y = next(e for e in sorted(outer_edges) if root(e) == tr)
        r = sub(positions[y], positions[x])
        row = [F(0)]*(2*n)
        for v, sign in ((x, -1), (y, 1)):
            row[2*v], row[2*v+1] = -sign*r[1], sign*r[0]
        rates.append(row)
    _, combined_pivots = elimination(contact_rows+rates, 2*n)
    assert len(combined_pivots) == 2*n-2
    assert len(outer_trains) >= flex_mod_trans

    face_rows = []
    anchor_columns = set()
    marked = set(outer_trains)
    for w in exceptional:
        rows = [[F(0)]*len(train_roots) for _ in range(2)]
        for i in range(len(w)):
            x, y = w[i], w[(i+1)%len(w)]
            e = edge(x, y)
            tr = root(e)
            marked.add(tr)
            r = sub(positions[y], positions[x])
            col = train_index[tr]
            rows[0][col] -= r[1]
            rows[1][col] += r[0]
            if e in outer_edges:
                assert sum(root(f) == tr for f in contacts) == 1
                anchor_columns.add(col)
        face_rows.extend(rows)
    _, closure_pivots = elimination(face_rows, len(train_roots))
    r_b = len(closure_pivots)
    _, anchor_pivots = elimination(
        [[row[c] for c in sorted(anchor_columns)] for row in face_rows],
        len(anchor_columns),
    )
    w_b = len(anchor_pivots)
    assert r_b == w_b == 2
    assert r_b == 2*len(exceptional)-sigma_c
    assert len(train_roots)-r_b == flex_mod_trans
    assert len(marked) >= flex_mod_trans+r_b
    # These packets attain the marked-face rank payment exactly.
    assert len(marked) == flex_mod_trans+2 == len(train_roots)
    return checks, n, len(contacts), len(train_roots), len(outer_trains)


def synthesis_packets():
    count = 0
    # Arithmetic contract only: X denotes 4S+2sigma_R in the exact #699
    # identity. No scalar packet is asserted to have a source realization.
    for m, k, d, sigma_c, rank_b, single_u in product(
            range(10), range(10), range(3), range(3), range(5), range(3)):
        extra = max(0, m-k+d+sigma_c+rank_b)
        sqrt_r = F(7)
        remaining = extra+2*sqrt_r+single_u
        b = F(30+m)
        q_minus_f = F(4)
        x = (2*b-8*sqrt_r+5*remaining+5*k+2*q_minus_f
             -5*m-5*d)
        target = 2*b+2*sqrt_r+5*(sigma_c+rank_b+single_u)+2*q_minus_f
        assert x >= target
        if m-k+d+sigma_c+rank_b >= 0:
            assert x == target
        count += 1
    return count


if __name__ == "__main__":
    packets = [packet(h, t) for h in (2, 3, 4, 6, 12)
               for t in (F(1, 50), F(1, 40))]
    cancellation = synthesis_packets()
    print(f"PASS: {sum(p[0] for p in packets)} exact source-pair checks in {len(packets)} packets")
    print("PASS: actual unit contact graphs, genuine missing contacts, no triangles, convex hexagons")
    print("PASS: positive pinned equilibrium and full pinned/contact ranks")
    print("PASS: outer-train rates determine contact flexes modulo two translations")
    print("PASS: marked-face closure rank and sharp extra two-column payment")
    print(f"PASS: {cancellation} exact synthesis cancellations, including double-good-end constants")
    print("SCOPE: pins need not be extreme or diameter-loaded; no source optimum or asymptotic closure")
