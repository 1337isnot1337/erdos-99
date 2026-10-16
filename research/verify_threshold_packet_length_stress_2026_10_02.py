#!/usr/bin/env python3
"""Exact formal cut-data regression for the packet-length report.

Encodes all staircase trees through eight cuts, full interval rank, positive
normalized row weights, distinct formal row directions, transverse cancellation,
strict one-peak cut pressures, the interval-length reaction bounds, and positive
definiteness of the scalar cut matrix. Uses Fraction arithmetic and rational LDL.
Omits joint Euclidean source realization, actual unit contacts/port equilibrium,
full affine stress kernel and inactive-pair constraints. Does not certify any
globally optimal source, feasible finite release, C-II or Level I closure.
"""

from fractions import Fraction as F
from itertools import combinations_with_replacement


def staircases(m):
    for pivot in range(1, m+1):
        for middle in combinations_with_replacement(range(pivot, m+1), pivot-1):
            stops = [m] + list(reversed(middle)) + [pivot]
            edges = [(i-1, j) for i in range(1, pivot+1)
                     for j in range(stops[i], stops[i-1]+1)]
            yield pivot, edges


def rank(matrix):
    mat = [list(map(F, row)) for row in matrix]
    answer = 0
    for column in range(len(mat[0])):
        pivot = next((i for i in range(answer, len(mat)) if mat[i][column]), None)
        if pivot is None:
            continue
        mat[answer], mat[pivot] = mat[pivot], mat[answer]
        value = mat[answer][column]
        mat[answer] = [x/value for x in mat[answer]]
        for i in range(answer+1, len(mat)):
            value = mat[i][column]
            mat[i] = [a-value*b for a, b in zip(mat[i], mat[answer])]
        answer += 1
    return answer


def positive_ldl(matrix):
    n = len(matrix)
    L = [[F(i == j) for j in range(n)] for i in range(n)]
    diagonal = []
    for i in range(n):
        pivot = matrix[i][i] - sum(L[i][j]**2 * diagonal[j] for j in range(i))
        assert pivot > 0
        diagonal.append(pivot)
        for k in range(i+1, n):
            L[k][i] = (matrix[k][i]
                       - sum(L[k][j]*L[i][j]*diagonal[j] for j in range(i))) / pivot
    return diagonal


def check(m, pivot, edges, total_mass):
    assert len(edges) == m
    assert len(set(edges)) == m
    assert all(a < pivot <= b for a, b in edges)
    assert sum(b-a for a, b in edges) == m*(m+1)//2
    assert all(b >= d for a, b in edges for c, d in edges if a < c)
    reached = {0}
    while True:
        new = reached | {b for a, b in edges if a in reached}
        new |= {a for a, b in edges if b in reached}
        if new == reached:
            break
        reached = new
    assert reached == set(range(m+1))
    intervals = [[F(a < i <= b) for i in range(1, m+1)] for a, b in edges]
    assert rank(intervals) == m
    D = F(1024*m)
    B = total_mass/m
    beta0 = 1-total_mass
    assert beta0 > 0 and beta0 + m*B == 1
    projections = [F(b-a)+F(j+1, 10*m) for j, (a, b) in enumerate(edges)]
    assert len(set(projections)) == m
    assert all(0 < d < D/2 for d in projections)
    assert all(d >= min(D/16, F(2, 3)*(b-a))
               for d, (a, b) in zip(projections, edges))
    # Paired transverse components cancel with equal B/2 weights.
    assert all(D*D-d*d > 0 for d in projections)
    A = [beta0*D + sum(B*d*v[i] for d, v in zip(projections, intervals))
         for i in range(m)]
    assert all(A[j] < A[j+1] for j in range(pivot-1))
    assert all(A[j] > A[j+1] for j in range(pivot-1, m-1))
    K = [[(A[i] if i == j else F(0)) - beta0
          - sum(B*v[i]*v[j] for v in intervals)
          for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            decomposed = beta0*((D if i == j else 0)-1)
            for index, (v, (a, b)) in enumerate(zip(intervals, edges)):
                decomposed += B*((b-a)*(v[i] if i == j else 0)-v[i]*v[j])
                if i == j:
                    decomposed += B*F(index+1, 10*m)*v[i]
            assert K[i][j] == decomposed
    positive_ldl(K)


def main():
    trees = models = 0
    for m in range(1, 9):
        count = 0
        for pivot, edges in staircases(m):
            count += 1
            for mass in (F(1, 2), F(1, 100), F(1, 10**6)):
                check(m, pivot, edges, mass)
                models += 1
        assert count == 2**(m-1)
        trees += count
    assert F(255, 256) > F(449, 450)**2
    assert F(2)/(1+F(449, 450)) < F(16, 15)**2
    assert F(8, 105) < F(1, 13)
    assert F(1098, 1521)**2 > F(1, 2)
    assert F(15, 16)*F(1098, 1521) > F(2, 3)
    print(f"PASS: {trees} staircase trees, {models} normalized formal models, "
          "exact full ranks and positive LDL pivots, rational length constants")


if __name__ == "__main__":
    main()
