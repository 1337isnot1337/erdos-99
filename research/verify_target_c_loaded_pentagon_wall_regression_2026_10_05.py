#!/usr/bin/env python3
"""Exact Q(sqrt(5)) checks for the actual loaded pentagon wall regression.

Global optimality is an attributed Bateman--Erdos theorem, not computed.
The covering and vacancy claims have analytic proofs in the report.
"""
from fractions import Fraction as F
from itertools import combinations


class Q5:
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, other):
        other = other if isinstance(other, Q5) else Q5(other)
        return Q5(self.a+other.a, self.b+other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, other):
        return self+-other

    def __mul__(self, other):
        other = other if isinstance(other, Q5) else Q5(other)
        return Q5(self.a*other.a+5*self.b*other.b,
                  self.a*other.b+self.b*other.a)

    __rmul__ = __mul__

    def __eq__(self, other):
        other = other if isinstance(other, Q5) else Q5(other)
        return self.a == other.a and self.b == other.b

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0)-(a < 0)
        if a == 0 or (a > 0) == (b > 0):
            return 1 if b > 0 else -1
        difference = a*a-5*b*b
        assert difference != 0  # sqrt(5) is irrational
        return ((a > 0)-(a < 0)) * ((difference > 0)-(difference < 0))


def multiply(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(5))
             for j in range(5)] for i in range(5)]


def laplacian(step):
    return [[Q5(2 if i == j else -1 if (i-j) % 5 in (step, 5-step) else 0)
             for j in range(5)] for i in range(5)]


if __name__ == "__main__":
    phi, phi2 = Q5(F(1, 2), F(1, 2)), Q5(F(3, 2), F(1, 2))
    radius2 = Q5(F(1, 2), F(1, 10))
    cosine = [Q5(1), Q5(F(-1, 4), F(1, 4)), Q5(F(-1, 4), F(-1, 4))]
    gram = [[radius2*cosine[min((i-j) % 5, (j-i) % 5)]
             for j in range(5)] for i in range(5)]
    assert multiply(gram, gram) == [[F(5, 2)*radius2*x for x in row] for row in gram]
    assert sum(gram[i][i] for i in range(5)) == 5*radius2
    contacts, diameters = [], []
    for i, j in combinations(range(5), 2):
        distance2 = gram[i][i]+gram[j][j]-2*gram[i][j]
        if (i-j) % 5 in (1, 4):
            assert distance2 == 1
            contacts.append((i, j))
        else:
            assert distance2 == phi2
            diameters.append((i, j))
    assert len(contacts) == len(diameters) == 5
    assert phi*phi == phi2

    alpha, beta = F(1, 5)*phi2, Q5(F(1, 5))
    lc, lh = laplacian(1), laplacian(2)
    omega = [[alpha*lc[i][j]-beta*lh[i][j] for j in range(5)] for i in range(5)]
    assert multiply(omega, omega) == [[phi*x for x in row] for row in omega]
    assert sum(omega[i][i] for i in range(5)) == 2*phi
    assert all(sum(row) == 0 for row in omega)
    assert all(x == 0 for row in multiply(omega, gram) for x in row)
    assert 5*beta == 1 and 5*alpha == phi2
    assert alpha.sign() > 0 and beta.sign() > 0 and phi.sign() > 0
    assert (Q5(1)-radius2).sign() > 0
    assert (Q5(1)-F(1, 4)*phi2).sign() > 0
    area2 = Q5(F(25, 16), F(5, 8))
    assert (area2-Q5(F(27, 16))).sign() > 0
    print("PASS: exact actual contact/diameter distances from rank-two algebraic Gram matrix")
    print("PASS: positive normalized KKT equilibrium and PSD stress with three affine modes")
    print("PASS: strict covering-radius and deleted-ear bounds; positive fixed-wall residual")
    print("SCOPE: finite regression only; global optimality attributed, no Type-II or unbounded family")
