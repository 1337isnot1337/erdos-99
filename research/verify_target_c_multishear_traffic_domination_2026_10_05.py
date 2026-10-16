#!/usr/bin/env python3
"""Exact PSD cut compressions and finite energy packets.

The analytic theorem uses the canonical PSD stress. The square and cross
are finite source packets, not large canonical C-II global minimizers.
"""
from fractions import Fraction as F
from itertools import combinations


def inner(x, y):
    return sum(a*b for a, b in zip(x, y))


def determinant(a):
    a = [list(row) for row in a]
    result = F(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result *= -1
        value = a[j][j]
        result *= value
        for i in range(j+1, len(a)):
            ratio = a[i][j]/value
            for k in range(j+1, len(a)):
                a[i][k] -= ratio*a[j][k]
    return result


def rank(a):
    a = [list(row) for row in a]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        value = a[r][j]
        a[r] = [x/value for x in a[r]]
        for i in range(len(a)):
            if i != r:
                ratio = a[i][j]
                a[i] = [x-ratio*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def psd_check(a):
    count = 0
    for size in range(1, len(a)+1):
        for indices in combinations(range(len(a)), size):
            assert determinant([[a[i][j] for j in indices] for i in indices]) >= 0
            count += 1
    return count


def packet(points, contacts, diameters, alpha, beta, shores):
    count, r = len(points), len(shores)
    distance = lambda x, y: inner(tuple(a-b for a, b in zip(x, y)), tuple(a-b for a, b in zip(x, y)))
    diameter_squared = max(distance(x, y) for x, y in combinations(points, 2))
    assert all(distance(points[i], points[j]) == 1 for i, j in contacts)
    assert all(distance(points[i], points[j]) == diameter_squared for i, j in diameters)
    assert len(diameters)*beta == 1
    omega = [[F(0) for _ in points] for _ in points]
    for edges, weight in ((contacts, alpha), (diameters, -beta)):
        for i, j in edges:
            omega[i][i] += weight
            omega[j][j] += weight
            omega[i][j] -= weight
            omega[j][i] -= weight
    assert rank(omega) == count-3
    for vector in [[F(1)]*count]+[[p[c] for p in points] for c in range(2)]:
        assert all(inner(row, vector) == 0 for row in omega)
    psd_count = psd_check(omega)
    regions = [[F(i in shore) for shore in shores] for i in range(count)]
    a = [[F(0) for _ in shores] for _ in shores]
    b = [[F(0) for _ in shores] for _ in shores]
    axes = [None]*r
    unselected = []
    for edges, weight, matrix in ((contacts, alpha, a), (diameters, beta, b)):
        for i, j in edges:
            differences = [regions[j][e]-regions[i][e] for e in range(r)]
            if edges is contacts:
                support = [e for e, value in enumerate(differences) if value]
                assert len(support) <= 1
                if support:
                    e = support[0]
                    direction = tuple(differences[e]*(points[j][c]-points[i][c]) for c in range(2))
                    assert axes[e] in (None, direction)
                    axes[e] = direction
                else:
                    unselected.append(tuple(points[j][c]-points[i][c] for c in range(2)))
            for e in range(r):
                for f in range(r):
                    matrix[e][f] += weight*differences[e]*differences[f]
    assert all(a[e][f] == 0 for e in range(r) for f in range(r) if e != f)
    w = [[a[e][f]-b[e][f] for f in range(r)] for e in range(r)]
    compression = [[sum(regions[i][e]*omega[i][j]*regions[j][f]
                        for i in range(count) for j in range(count)) for f in range(r)] for e in range(r)]
    assert w == compression
    psd_count += psd_check(w)
    unselected_rank = rank(unselected) if unselected else 0
    assert r-rank(w) == 2-unselected_rank
    tangent = F(1, 50)
    cosine, sine = (1-tangent*tangent)/(1+tangent*tangent), 2*tangent/(1+tangent*tangent)
    increments = [(cosine*x-sine*y-x, sine*x+cosine*y-y) for x, y in axes]
    new = [tuple(points[i][c]+sum(regions[i][e]*increments[e][c] for e in range(r))
                 for c in range(2)) for i in range(count)]
    assert all(distance(new[i], new[j]) == 1 for i, j in contacts)
    assert all(distance(x, y) >= 1 for x, y in combinations(new, 2))
    mean = sum(beta*distance(new[i], new[j]) for i, j in diameters)
    loss = sum(increments[e][c]*w[e][f]*increments[f][c]
               for e in range(r) for f in range(r) for c in range(2))
    assert mean == diameter_squared-loss
    assert loss >= 0
    quadratic_checks = 0
    for e in range(r):
        u = axes[e]
        ju = (-u[1], u[0])
        for tangent in [F(-2), F(-1, 50), F(0), F(1, 50), F(1, 2), F(2)]:
            cosine = (1-tangent*tangent)/(1+tangent*tangent)
            sine = 2*tangent/(1+tangent*tangent)
            change = (cosine*u[0]-sine*u[1]-u[0], sine*u[0]+cosine*u[1]-u[1])
            one_cut = [tuple(points[i][c]+regions[i][e]*change[c] for c in range(2)) for i in range(count)]
            for i, j in combinations(range(count), 2):
                epsilon = regions[j][e]-regions[i][e]
                if not epsilon:
                    assert distance(one_cut[i], one_cut[j]) == distance(points[i], points[j])
                    continue
                old_vector = tuple(epsilon*(points[j][c]-points[i][c]) for c in range(2))
                length_squared = inner(old_vector, old_vector)
                axial, transverse = inner(old_vector, u), inner(old_vector, ju)
                new_squared = distance(one_cut[i], one_cut[j])
                for threshold in (F(1), diameter_squared):
                    constant = length_squared-threshold
                    polynomial = constant+4*transverse*tangent+(constant+4*(1-axial))*tangent*tangent
                    assert polynomial == (1+tangent*tangent)*(new_squared-threshold)
                    quadratic_checks += 1
    return psd_count, r, r-rank(w), loss == 0, quadratic_checks


if __name__ == "__main__":
    cross = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1))]
    c_cross, h_cross = [(0, i) for i in range(1, 5)], [(1, 3), (2, 4)]
    square = [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1))]
    c_square, h_square = [(0, 1), (1, 2), (2, 3), (0, 3)], [(0, 2), (1, 3)]
    results = [packet(cross, c_cross, h_cross, F(1), F(1, 2), [{1}, {2}]),
               packet(cross, c_cross, h_cross, F(1), F(1, 2), [{1}, {2}, {3}]),
               packet(square, c_square, h_square, F(1, 2), F(1, 2), [{1, 2}]),
               packet(cross, c_cross, h_cross, F(1), F(1, 2), [{1}, {2}, {3}, {4}])]
    print(f"PASS: {sum(r[0] for r in results)} nonnegative exact principal minors")
    print("PASS: full contact support, actual diameters, normalized equilibrium and affine scalar kernels")
    print("PASS: cut compression equals contact diagonal minus diameter path-traffic Gram")
    print(f"PASS: traffic kernel dimensions {[r[2] for r in results]} equal 2 minus unselected direction rank")
    print("PASS: exact finite contact preservation, all lower pairs and finite energy identity")
    print(f"PASS: {sum(r[4] for r in results)} full-source upper/lower quadratic checks, including inadmissible large angles")
    print("SCOPE: no large-source global optimality or common maximum-diameter descent is certified")
