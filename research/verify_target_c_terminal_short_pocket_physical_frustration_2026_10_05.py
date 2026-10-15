#!/usr/bin/env python3
"""Finite checks for terminal short-pocket phase depletion.

Rational triangles are geometric unit-separated packets, not loaded-source
certificates. Integer train ledgers have no asserted source embedding.
No global optimality, asymptotic convergence, Groemer compactness, spare
capacity, activation or Level I closure follows from these computations.
"""
from fractions import Fraction as F
from itertools import product


def two_step_pockets():
    q, p = 2, 1
    previous_gap = F(1)
    for _ in range(20):
        assert q*q - 3*p*p == 1
        den = q*q + p*p
        x, y = F(q*q-p*p, den), F(2*p*q, den)
        c = 2*x
        assert x*x + y*y == 1
        assert 1 < c < F(3, 2)
        assert (c-x)**2 + y*y == 1
        assert c*c > 1
        gap = c-1
        assert gap == F(1, 4*p*p+1) < previous_gap
        previous_gap = gap

        # r = c*y/sqrt(3) + c/2 - 1. Positive sides permit squaring.
        rhs = 1-c/2
        assert rhs > 0
        residual_square_gap = c*c*y*y - 3*rhs*rhs
        assert residual_square_gap == (c-1)*(12-c*c-c*c*c)/4 > 0
        # The analytic derivative for reduced phase is 1/sqrt(4-c^2)<1.
        assert 4-c*c > 1
        q, p = 2*q+3*p, q+2*p
    return 20


def pocket_tail_counts():
    count = 0
    for n in range(6):
        for lengths in product(range(2, 9), repeat=n):
            excess = sum(m-2 for m in lengths)
            long_lengths = [m for m in lengths if m >= 3]
            assert len(long_lengths) <= excess
            assert sum(long_lengths) <= 3*excess
            assert sum(lengths) == 2*n+excess
            count += 1
    return count


def train_bank_ledgers():
    count = 0
    for q in range(3, 13):
        for m in range(q+1):
            for u in range(min(4, q-m)+1):
                b = q+m+u
                for k in range(min(4, q)+1):
                    Q = q-m-u-2*k
                    if Q < 0:
                        continue
                    for f in range(Q+1):
                        T = q-k+2*f
                        for sigma in range(3):
                            lower = q-k+sigma
                            if lower > T:
                                continue
                            for d in range(min(2, q-m)+1):
                                G = q-m-d
                                if G < 0:
                                    continue
                                start = max(G, lower)
                                if start > T:
                                    continue
                                for outer in {start, T}:
                                    for single_u in {0, T-outer}:
                                        U = T-outer-single_u
                                        assert U >= 0
                                        assert U <= 2*f-sigma-single_u
                                        assert U <= 2*f-max(sigma, k-m-d)-single_u
                                        assert m+u+2*k+(F(sigma+single_u, 2)) <= q-F(U, 2)
                                        # An arbitrary rational square-root symbol
                                        # tests cancellation, not a rhombus count.
                                        root_r = F(q+1, 7)
                                        S = single_u
                                        sigma_R = 2*(T-S)-4*root_r
                                        lhs = 4*S+2*sigma_R
                                        rhs = (2*b-8*root_r+5*U+5*sigma
                                               +2*(Q-f)+5*single_u
                                               +5*(outer-lower))
                                        assert lhs == rhs
                                        assert outer-G >= m-k+sigma+d
                                        count += 1
    return count


def parameter_recipe():
    # pi^2<16 and Delta_2>3/4. The two angular errors are <=.104Delta_2.
    assert F(48, 1000) < F(396, 1000)*F(3, 4)
    assert F(80+24, 1000) == F(104, 1000)


def main():
    triangles = two_step_pockets()
    tails = pocket_tail_counts()
    ledgers = train_bank_ledgers()
    parameter_recipe()
    print(f"PASS: {triangles} rational unit pockets, near-unit chords and positive vanishing residual")
    print(f"PASS: {tails} exact pocket node and terminal-mass tail ledgers")
    print(f"PASS: {ledgers} train banks, second-depletion cancellation and hull-budget implications")
    print("PASS: rational universal-cutoff error budget")
    print("SCOPE: finite geometry and scalar ledgers; no activation, optimality or asymptotic closure certificate")


if __name__ == "__main__":
    main()
