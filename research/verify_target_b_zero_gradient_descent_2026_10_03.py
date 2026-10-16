#!/usr/bin/env python3
"""Exact finite algebra supporting zero-gradient mixed-order descent.

Checks sparse neutral corrections for integer gradient matrices with a positive
three-row dependence, rational Taylor coefficients through degree 6, and one
strict cubic-corrector feasibility witness. Uses Fraction only. These algebraic
models are not embedded rhombus sources. No train-chart existence, all-source
feasibility, local/global minimality, or Level I claim follows from execution.
The report supplies the analytic conditional source-motion proof.
"""

from fractions import Fraction as F
from math import factorial

ORDER = 6


def add(a, b):
    return [a[i] + b[i] for i in range(ORDER + 1)]


def scale(c, a):
    return [c * x for x in a]


def mul(a, b):
    out = [F(0)] * (ORDER + 1)
    for i in range(ORDER + 1):
        for j in range(ORDER + 1 - i):
            out[i + j] += a[i] * b[j]
    return out


def trig(angle):
    cosine = [F(0)] * (ORDER + 1)
    sine = [F(0)] * (ORDER + 1)
    power = [F(1)] + [F(0)] * ORDER
    for k in range(ORDER + 1):
        if k % 2:
            sine = add(sine, scale(F((-1) ** ((k - 1) // 2), factorial(k)), power))
        else:
            cosine = add(cosine, scale(F((-1) ** (k // 2), factorial(k)), power))
        power = mul(power, angle)
    return cosine, sine


def kernel_vector(rows, n):
    matrix = [[F(x) for x in row] for row in rows]
    pivots = []
    for col in range(n):
        pivot = next((i for i in range(len(pivots), len(matrix))
                      if matrix[i][col]), None)
        if pivot is None:
            continue
        top = len(pivots)
        matrix[top], matrix[pivot] = matrix[pivot], matrix[top]
        factor = matrix[top][col]
        matrix[top] = [x / factor for x in matrix[top]]
        for i in range(len(matrix)):
            if i != top:
                factor = matrix[i][col]
                matrix[i] = [x - factor * y for x, y in zip(matrix[i], matrix[top])]
        pivots.append(col)
    free = next(col for col in range(n) if col not in pivots)
    answer = [F(0)] * n
    answer[free] = F(1)
    for row, col in zip(matrix, pivots):
        answer[col] = -row[free]
    assert all(sum(x * y for x, y in zip(row, answer)) == 0 for row in rows)
    return answer


def zero_bar_series(P, N, a, b, epsilon):
    D = P - N
    x = [F(0)] * (ORDER + 1)
    y = [F(0)] * (ORDER + 1)
    for i in range(P + N):
        # Common first-order rotation is deliberately nonzero.
        angle = [F(0), F(2), epsilon * a[i], b[i]] + [F(0)] * 3
        cosine, sine = trig(angle)
        sign = F(1 if i < P else -1)
        x = add(x, scale(sign, cosine))
        y = add(y, scale(sign, sine))
    result = add(mul(x, x), mul(y, y))
    result[0] -= D * D
    assert all(result[i] == 0 for i in range(4))
    expected = -D * epsilon * epsilon * sum(value * value for value in a)
    assert result[4] == expected < 0


def main():
    models = 0
    for P in range(4, 13):
        for N in range(4):
            if P - N <= 3:
                continue
            for seed in range(12):
                # Four positive coordinates suffice for rank <= 2.
                row1 = [((seed + 2) * (j + 1)) % 7 - 3 for j in range(4)]
                row3 = [((seed + 3) * (j + 2)) % 11 - 5 for j in range(4)]
                row4 = [-x - y for x, y in zip(row1, row3)]
                a4 = kernel_vector([row1, row3, row4, [1] * 4], 4)
                a = a4 + [F(0)] * (P + N - 4)
                assert sum(a) == 0 and any(a)
                b = [F((seed + i) % 5 - 2, 3) for i in range(P + N)]
                zero_bar_series(P, N, a, b, F(1, 7))
                models += 1

    # Exact cubic corrector for a three-row rank-two stress singleton.
    rows = [[F(1), 0, 0, 0], [0, F(1), 0, 0], [-F(1), -F(1), 0, 0]]
    cubic = [F(-3), F(1), F(1)]
    b = [F(5, 2), F(-5, 4), F(0), F(0)]
    coefficients = [sum(x * y for x, y in zip(row, b)) + c
                    for row, c in zip(rows, cubic)]
    assert coefficients == [F(-1, 2), F(-1, 4), F(-1, 4)]
    assert sum(cubic) < 0

    # Full Hessian cross-kernel identity, including signed tangent speeds.
    # D forward e-contributions; tangent signs (-,+,+,-), speeds (0,1,1,2).
    for D in range(4, 13):
        vectors = [(F(1), F(0))] * D + [(F(0), F(s)) for s in (-1, 1, 1, -1)]
        v = [F(2)] * D + [F(2), F(3), F(3), F(4)]
        derivative_v = (sum(-w[1] * speed for w, speed in zip(vectors, v)),
                        sum(w[0] * speed for w, speed in zip(vectors, v)))
        assert derivative_v == (0, 2 * D)
        for i in range(len(vectors)):
            derivative_z = (-vectors[i][1], vectors[i][0])
            cross_term = 2 * sum(x * y for x, y in zip(derivative_v, derivative_z))
            cross_term -= 2 * D * vectors[i][0] * v[i]
            assert cross_term == 0
    print(f'PASS: {models} exact sparse corrections and degree-6 mixed paths; '
          'strict cubic coefficients (-1/2,-1/4,-1/4); 9 full Hessian-kernel models.')


if __name__ == '__main__':
    main()
