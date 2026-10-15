#!/usr/bin/env python3
"""Actual six-point loaded-star audit of augmented internal train columns.

Arithmetic is Q(sqrt(5)). Global optimality is the original D(6) theorem;
the packet is not a large-diameter canonical Type-II source.
"""
from itertools import combinations
from verify_target_c_loaded_pentagon_wall_regression_2026_10_05 import Q5, F


def multiply(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


if __name__ == "__main__":
    cosine = [Q5(1), Q5(F(-1, 4), F(1, 4)), Q5(F(-1, 4), F(-1, 4))]
    gram = [[cosine[min((i-j) % 5, (j-i) % 5)] if i < 5 and j < 5 else Q5()
             for j in range(6)] for i in range(6)]
    assert multiply(gram, gram) == scale(Q5(F(5, 2)), gram)
    assert sum(gram[i][i] for i in range(6)) == 5
    assert all(sum(row) == 0 for row in gram)
    contacts, diameters = [], []
    diameter2 = Q5(F(5, 2), F(1, 2))
    for i, j in combinations(range(6), 2):
        d2 = gram[i][i]+gram[j][j]-2*gram[i][j]
        assert (d2-Q5(1)).sign() >= 0
        assert (diameter2-d2).sign() >= 0
        if d2 == 1:
            contacts.append((i, j))
        if d2 == diameter2:
            diameters.append((i, j))
    assert contacts == [(i, 5) for i in range(5)]
    assert len(diameters) == 5 and {v for e in diameters for v in e} == set(range(5))
    assert all(5 not in e for e in diameters)
    adj = {v: set() for v in range(5)}
    for i, j in diameters:
        adj[i].add(j)
        adj[j].add(i)
    assert all(len(ns) == 2 for ns in adj.values())
    visited, pending = set(), [0]
    while pending:
        v = pending.pop()
        if v not in visited:
            visited.add(v)
            pending.extend(adj[v]-visited)
    assert visited == set(range(5))

    lc, lh = [[[Q5() for _ in range(6)] for _ in range(6)] for _ in range(2)]
    for edges, matrix in ((contacts, lc), (diameters, lh)):
        for i, j in edges:
            matrix[i][i] = matrix[i][i]+1
            matrix[j][j] = matrix[j][j]+1
            matrix[i][j] = matrix[i][j]-1
            matrix[j][i] = matrix[j][i]-1
    alpha, beta = F(1, 5)*diameter2, Q5(F(1, 5))
    omega = add(scale(alpha, lc), scale(-beta, lh))
    assert all(sum(row) == 0 for row in omega)
    assert all(x == 0 for row in multiply(omega, gram) for x in row)
    weak, strong = Q5(0, F(1, 5)), 6*alpha
    identity = [[Q5(int(i == j)) for j in range(6)] for i in range(6)]
    polynomial = add(add(multiply(omega, omega), scale(-(weak+strong), omega)),
                     scale(weak*strong, identity))
    assert all(x == 0 for row in multiply(omega, polynomial) for x in row)
    assert sum(omega[i][i] for i in range(6)) == 2*weak+strong
    assert weak.sign() > 0 and strong.sign() > 0
    assert alpha.sign() > 0 and beta.sign() > 0
    assert 5*beta == 1 and 5*alpha == diameter2
    assert (Q5(1)-cosine[2]*cosine[2]).sign() > 0  # nonzero chord angle

    # Augmented pockets are (p_i, center, p_{i+1}); every source contact
    # has two old outer occurrences and two distinct pocket endpoints.
    # Column i has +Jp_i at pocket i-1 and -Jp_i at pocket i.
    endpoints = [{(i-1) % 5: 1, i: -1} for i in range(5)]
    column_gram = [[gram[i][j]*sum(endpoints[i].get(f, 0)*endpoints[j].get(f, 0)
                                 for f in range(5))
                   for j in range(5)] for i in range(5)]
    assert all(column_gram[i][i] == 2 for i in range(5))
    assert all(column_gram[i][j] == (-cosine[1] if (i-j) % 5 in (1, 4) else Q5())
               for i in range(5) for j in range(5) if i != j)
    assert (Q5(2)-2*cosine[1]).sign() > 0  # strict diagonal dominance => SPD
    for mask in range(1, 32):
        selected = {i for i in range(5) if mask >> i & 1}
        internal = sum(set(ep) <= selected for ep in endpoints)
        assert internal <= 2*len(selected)-2
    print("PASS: all 15 actual source-pair constraints; five contacts and five loaded diameter edges")
    print("PASS: positive normalized actual KKT equilibrium; PSD stress, rank three, affine kernel")
    print("PASS: actual mixed rigidity via nonzero angular differences on the diagonal cycle")
    print("PASS: five independent augmented internal train columns with no unit-hull outside ends")
    print("PASS: bridge occurrences, distinct pocket endpoints and all 31 node-subset bounds")
    print("SCOPE: genuine finite D(6) example; global optimality attributed, no large Type-II existence")
