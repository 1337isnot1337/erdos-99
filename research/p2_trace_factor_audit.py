#!/usr/bin/env python3
"""Exact factor audit for the Target C P2 trace polynomials.

Tests

    H_m(X) = 2 T_m(X/2) + 16 X^2 - 48 X + 34

over Q for 3 <= m <= M.

This is the finite computational evidence recorded in
`docs/reports/target_c_cyclic_d2_p2_algebraic_degree_sieve_2026-09-10.md`.
The arithmetic is exact SymPy integer/rational polynomial arithmetic. A pass proves
only the displayed finite factorization range. It does not prove the eventual P2-I
irreducibility statement and it does not certify global packing optimality.

Reproduce with:

    python3 research/p2_trace_factor_audit.py
    python3 research/p2_trace_factor_audit.py --max-m 100
"""

from __future__ import annotations

import argparse

import sympy as sp


X = sp.Symbol("X")


def trace_poly(m: int) -> sp.Poly:
    """Return H_m exactly in ZZ[X], using the monic Chebyshev-trace recurrence."""
    s0 = sp.Poly(2, X, domain=sp.ZZ)
    if m == 0:
        s = s0
    else:
        s1 = sp.Poly(X, X, domain=sp.ZZ)
        if m == 1:
            s = s1
        else:
            a, b = s0, s1
            for _ in range(1, m):
                a, b = b, sp.Poly(X * b.as_expr() - a.as_expr(), X, domain=sp.ZZ)
            s = b
    return sp.Poly(s.as_expr() + 16 * X**2 - 48 * X + 34, X, domain=sp.ZZ)


def rational_factors(poly: sp.Poly) -> list[tuple[sp.Poly, int]]:
    """Return the exact irreducible factorization over Q/ZZ."""
    _, factors = sp.factor_list(poly.as_expr(), X)
    return [(sp.Poly(f, X, domain=sp.ZZ), exponent) for f, exponent in factors]


def has_expected_pattern(m: int, factors: list[tuple[sp.Poly, int]]) -> bool:
    """Check the P2-I pattern observed in the finite audit range."""
    if m % 6 == 3:
        if len(factors) != 2:
            return False
        linear = [f for f, e in factors if f.degree() == 1 and e == 1]
        large = [f for f, e in factors if f.degree() == m - 1 and e == 1]
        return (
            len(linear) == 1
            and linear[0].monic().as_expr() == X - 1
            and len(large) == 1
        )

    return (
        len(factors) == 1
        and factors[0][0].degree() == m
        and factors[0][1] == 1
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Exact Q-factorization audit for the Target C P2 trace polynomial."
    )
    parser.add_argument("--max-m", type=int, default=60)
    args = parser.parse_args()

    if args.max_m < 3:
        raise SystemExit("--max-m must be at least 3")

    for m in range(3, args.max_m + 1):
        poly = trace_poly(m)
        factors = rational_factors(poly)
        degrees = [factor.degree() for factor, _ in factors]
        ok = has_expected_pattern(m, factors)
        print(f"m={m:3d} degrees={degrees} expected={ok}")
        if not ok:
            print("Unexpected exact factorization:")
            for factor, exponent in factors:
                print(f"  exponent={exponent}: {factor.as_expr()}")
            raise SystemExit(1)

    print(
        "PASS: exact Q-factorization pattern verified for "
        f"3 <= m <= {args.max_m}."
    )


if __name__ == "__main__":
    main()
