#!/usr/bin/env python3
"""Exact checks of the zero-gradient/cubic-corrector candidate.

Encodes full-gradient matrices of rank <=2 on four forward coordinates,
zero-sum correction, and signed collinear train contributions. Enumerates all
6561 two-by-four matrices with entries -1,0,1, using Fraction RREF. SymPy
certifies finite Taylor coefficients; a rational formal stress/cubic example
checks simultaneous corrections, and a three-coordinate model delimits the
dimension argument. Does not encode a physical rhombus chart, actual source
diameters, phase-transfer extraction, feasibility/global optimality, or Level I.
The arbitrary-size full-source descent is the analytic proof in the report.
"""

from fractions import Fraction as F
from itertools import product

import sympy as s


def null_vector(rows: list[list[int]]) -> list[F]:
    a = [[F(x) for x in row] for row in rows]
    n, lead = len(a[0]), 0
    pivots = []
    for col in range(n):
        pivot = next((i for i in range(lead, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[lead], a[pivot] = a[pivot], a[lead]
        divisor = a[lead][col]
        a[lead] = [x/divisor for x in a[lead]]
        for i in range(len(a)):
            if i != lead:
                factor = a[i][col]
                a[i] = [x-factor*y for x, y in zip(a[i], a[lead])]
        pivots.append(col)
        lead += 1
        if lead == len(a):
            break
    free = next((j for j in range(n) if j not in pivots), None)
    if free is None:
        return [F(0)] * n
    v = [F(0)] * n
    v[free] = F(1)
    for i, col in enumerate(pivots):
        v[col] = -a[i][free]
    return v


def main() -> None:
    checked = 0
    for entries in product((-1, 0, 1), repeat=8):
        rows = [list(entries[:4]), list(entries[4:]), [1]*4]
        a = null_vector(rows)
        assert any(a)
        assert all(sum(x*y for x, y in zip(row, a)) == 0 for row in rows)
        assert -2*4*sum(x*x for x in a) < 0
        checked += 1

    # Positive dependence of three residual gradients and a strict cubic correction.
    G = s.Matrix([[1, 0, -1, 0], [0, 1, 0, -1], [-1, -1, 1, 1]])
    mu = s.Matrix([[s.Rational(1, 3)]*3])
    a = s.Matrix([1, -1, 1, -1])
    b = s.Matrix([-s.Rational(4, 3), -s.Rational(4, 3), 0, 0])
    cubic = s.Matrix([1, 1, -4])
    assert mu*G == s.zeros(1, 4)
    assert G*a == s.zeros(3, 1) and sum(a) == 0
    assert (mu*cubic)[0] < 0
    assert all(value < 0 for value in G*b+cubic)

    t, eps = s.symbols("t eps", real=True)
    for P, N in ((4, 0), (5, 1), (8, 3)):
        D = P-N
        signs = [1]*P+[-1]*N
        av = [1, -1]+[0]*(P+N-2)
        bv = list(range(1, P+N+1))
        increments = [eps*t**2*x+t**3*y for x, y in zip(av, bv)]
        # Independent trig-series expansion of the exact zero-bar squared length.
        rx = sum(sig*s.series(s.cos(w), t, 0, 6).removeO()
                 for sig, w in zip(signs, increments))
        ry = sum(sig*s.series(s.sin(w), t, 0, 6).removeO()
                 for sig, w in zip(signs, increments))
        f = s.expand(rx*rx+ry*ry-D**2)
        assert all(s.expand(f).coeff(t, j) == 0 for j in range(4))
        assert s.expand(f).coeff(t, 4) == -2*D*eps**2
        cross = sum(sig*x*y for sig, x, y in zip(signs, av, bv))
        assert s.expand(f).coeff(t, 5) == -2*D*eps*cross

    # Sharp limit of this dimension argument: on three positive coordinates,
    # these residual gradients force only common rotation; zero-sum gives zero.
    G3 = s.Matrix([[1, -1, 0], [0, 1, -1], [-1, 0, 1]])
    assert G3.rank() == 2
    assert G3.nullspace() == [s.ones(3, 1)]
    assert G3.col_join(s.ones(1, 3)).rank() == 3

    print("PASS: exact zero-gradient cubic corrector")
    print(f"rank-two forward correction charts={checked}; trig expansions=3")
    print("simultaneous rational gradient/cubic correction and P=3 no-go verified")
    print("Scope: finite algebra check; no actual-source/global-optimality claim.")


if __name__ == "__main__":
    main()
