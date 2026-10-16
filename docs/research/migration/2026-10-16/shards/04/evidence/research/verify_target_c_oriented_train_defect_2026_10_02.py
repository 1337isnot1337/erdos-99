#!/usr/bin/env python3
"""Exact arithmetic checks for the oriented train carrier defect candidate.

Encoded: the explicit Green kernel and its first/further Fourier modes,
Machin alternating-series pi enclosures, outward rational square roots,
failure of the conditional rooted scalar necessary inequality at 0.9891349,
and an eighteen-cycle regression to a parallel-chord shortcut.
Omitted: source train embedding, hull-route selection, KKT equilibrium,
the unpromoted rooted ledger, and all Level I/global-optimality claims.
"""

from fractions import Fraction as F
from math import isqrt

import sympy as sp


def atan_interval(x, terms=18):
    value = sum((-1)**j * x**(2*j+1) / (2*j+1)
                for j in range(terms))
    other = value + (-1)**terms*x**(2*terms+1)/(2*terms+1)
    return min(value, other), max(value, other)


def pi_interval():
    # tan(4 atan(1/5)-atan(1/239)) = 1, and the argument lies in (0,pi/2).
    t = F(1, 5)
    t2 = 2*t/(1-t*t)
    t4 = 2*t2/(1-t2*t2)
    assert (t4-F(1, 239))/(1+t4*F(1, 239)) == 1
    alo, ahi = atan_interval(F(1, 5))
    blo, bhi = atan_interval(F(1, 239))
    lo, hi = 16*alo-4*bhi, 16*ahi-4*blo
    assert F(314159, 100000) < lo < hi < F(314160, 100000)
    return lo, hi


def sqrt_interval(x, digits=28):
    assert x >= 0
    denominator = 10**digits
    floor = isqrt(x.numerator*denominator*denominator//x.denominator)
    lo, hi = F(floor, denominator), F(floor+1, denominator)
    assert lo*lo <= x < hi*hi
    return lo, hi


def kernel_check():
    t = sp.symbols('t', real=True)
    p = sp.pi
    kernel = ((p-2*t)*sp.sin(t)-sp.cos(t))/(4*p)
    assert sp.simplify(sp.diff(kernel, t, 2)+kernel+sp.cos(t)/p) == 0
    assert kernel.subs(t, 0) == -1/(4*p)
    assert kernel.subs(t, p) == 1/(4*p)
    assert sp.diff(kernel, t).subs(t, 0) == F(1, 4)
    assert sp.diff(kernel, t).subs(t, p) == F(1, 4)
    # Antiperiodic continuation makes derivative jumps +1/2 and -1/2.
    assert sp.integrate(kernel*sp.sin(t), (t, 0, p)) == 0
    assert sp.integrate(kernel*sp.cos(t), (t, 0, p)) == 0
    for n in (3, 5, 7, 9):
        coefficient = 2/p*sp.integrate(kernel*sp.cos(n*t), (t, 0, p))
        assert sp.simplify(coefficient-1/(p*(1-n*n))) == 0
    for count in (1, 2, 3, 10, 100):
        assert sum(F(1, 4*j*(j+1)) for j in range(1, count+1)) \
               == F(count, 4*(count+1))


def rooted_check():
    plo, phi = pi_interval()
    lam = F(9891349, 10_000_000)
    slo, shi = sqrt_interval(1-lam*lam)
    delta_lo = plo/2-lam-4*lam*shi
    delta_hi = phi/2-lam-4*lam*slo
    assert 0 < delta_lo <= delta_hi
    _, outer_hi = sqrt_interval(delta_hi*(phi*lam+2*delta_hi))
    rhs_hi = 5*delta_hi/plo + (phi+1)*outer_hi/2
    margin = 1-lam-rhs_hi
    assert margin > F(1, 2000), "strict rational margin at the chosen cutoff"
    lower_test = F(49, 50)
    s0, _ = sqrt_interval(1-lower_test*lower_test)
    assert lower_test+4*lower_test*s0 > phi/2
    # A(lambda) decreases throughout lambda>=49/50, proving uniqueness
    # of lambda_1 and the monotone comparison used in the report.
    assert 8*lower_test*lower_test-4 > 1
    return margin


def chord_regression():
    q = 18
    vertices = (1, 5, 7, 11, 13, 17)
    differences = [min(abs(a-b), q-abs(a-b)) for i, a in enumerate(vertices)
                   for b in vertices[i+1:]]
    assert max(differences) == 8 and 9 not in differences
    gaps = [b-a for a, b in zip(vertices, vertices[1:]+(vertices[0]+q,))]
    sums = [(a+b) % (2*q)
            for a, b in zip(vertices, vertices[1:]+(vertices[0]+q,))]
    assert gaps == [4, 2, 4, 2, 4, 2]
    assert set(sums) == {0, 6, 12, 18, 24, 30}
    for index, angle in enumerate(sums):
        other = sums.index((angle+q) % (2*q))
        assert gaps[index] != gaps[other]


def main():
    kernel_check()
    margin = rooted_check()
    chord_regression()
    print('PASS: explicit Green identity, jumps, first modes and four inverse modes.')
    print('PASS: exact Machin pi and rational square-root enclosures.')
    print('PASS: rooted necessary inequality fails at lambda=0.9891349;')
    print('strict rational margin exceeds 1/2000.')
    print('PASS: eighteen-cycle support has three unequal opposite chord pairs,')
    print('no antipodes, and normalized diameter cos(pi/18)<1.')
    print('No source embedding, rooted-ledger audit, or Level I certificate asserted.')


if __name__ == '__main__':
    main()
