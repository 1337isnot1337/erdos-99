#!/usr/bin/env python3
"""Exact finite certificates for five-distinct-bar flattening.

The report proves the source reduction and imports the stated standard
2-isogeny descent / torsion-injection theorems. This script checks the complete
1024-graph universe, modular obstructions, finite-field counts, and algebraic
identities. It does not certify an actual source or global optimality.
Requires SymPy; no floating-point arithmetic is used.
"""

from itertools import combinations, product

import sympy as sp


EXPECTED = {
    (12, 13, 15, 23, 24, 34, 35): ("A1", (2, 4)),
    (12, 14, 15, 23, 24, 34, 35): ("B1", (2, 3)),
    (12, 13, 14, 23, 25, 34, 35): ("A2", (2, 5)),
    (12, 14, 15, 23, 25, 34, 35): ("B2", (2, 3)),
    (12, 13, 14, 24, 25, 34, 35): ("C1", (2, 3)),
    (12, 13, 15, 24, 25, 34, 35): ("C2", (2, 3)),
}


def zero(expr):
    return sp.cancel(expr) == 0


def graph_cover():
    edges = list(combinations(range(1, 6), 2))
    survivors = set()
    for mask in range(1 << len(edges)):
        out = {i: set() for i in range(1, 6)}
        inc = {i: set() for i in range(1, 6)}
        for bit, (i, j) in enumerate(edges):
            if (mask >> bit) & 1:
                out[i].add(j)
                inc[j].add(i)
        if mask == 0:
            continue  # This is the desired B=0 case, not a nonzero obstruction.
        if any(len(out[i]) == 1 for i in out):
            continue
        if any(not inc[i] and 0 < len(out[i]) < 3 for i in out):
            continue
        if any(not out[i] and len(inc[i]) == 1 for i in out):
            continue
        if any(len(out[i] & out[j]) > 2 for i, j in edges):
            continue
        if any(j in out[i] and len(out[i] & out[j]) > 1 for i, j in edges):
            continue
        key = tuple(10*i+j for i in out for j in sorted(out[i]))
        survivors.add(key)
        assert key in EXPECTED, key

        # A two-term column with known nonzero coefficients makes the two
        # corresponding positive row weights rational multiples. A degree-two
        # row has nonzero diagonal by distinctness of the destination speeds.
        _, columns = EXPECTED[key]
        rational_links = []
        for column in columns:
            support = set(inc[column])
            if out[column]:
                assert len(out[column]) == 2
                support.add(column)
            assert len(support) == 2
            rational_links.append(support)
        reached = {1}
        for _ in range(3):
            for pair in rational_links:
                if pair & reached:
                    reached |= pair
        assert {1, 2, 3} <= reached

        tag, _ = EXPECTED[key]
        if tag.startswith("A"):
            assert {12, 13, 23} <= set(key)
        else:
            common = 4 if tag.endswith("1") else 5
            assert all(10*i+common in key for i in (1, 2, 3))
            assert ({12, 23} if tag.startswith("B") else {12, 13}) <= set(key)
    assert survivors == set(EXPECTED)
    print("PASS: all 1024 forward graphs; exactly six supports, each with a rational-weight witness")


def arithmetic_certificates():
    squares16 = {n*n % 16 for n in range(16)}
    for m, e in product(range(16), repeat=2):
        if m % 2 == 0 and e % 2 == 0:
            continue
        residue = (2*m**4 - 4*m*m*e*e + 8*e**4) % 16
        assert residue not in squares16
    print("PASS: E1 dual class 2 excluded for every primitive parity residue modulo 16")

    squares9 = {n*n % 9 for n in range(9)}
    for m, e in product(range(9), repeat=2):
        if m % 3 == 0 and e % 3 == 0:
            continue
        residue = (3*m**4 + 6*m*m*e*e - e**4) % 9
        assert residue not in squares9
    print("PASS: E2 class 3 excluded for every primitive 3-adic residue modulo 9")

    point_lists = {
        (2, -3): [(0, 0), (1, 0), (-3, 0), (-1, 2), (-1, -2), (3, 6), (3, -6)],
        (6, -3): [(0, 0), (1, 2), (1, -2), (-3, 6), (-3, -6)],
    }
    for (a, b), points in point_lists.items():
        discriminant = 16*b*b*(a*a-4*b)
        assert discriminant % 5 != 0
        count = 1 + sum((y*y-x**3-a*x*x-b*x) % 5 == 0 for x, y in product(range(5), repeat=2))
        assert count == len(points)+1
        assert len(set(points)) == len(points)
        assert all(y*y == x**3+a*x*x+b*x for x, y in points)
        print(f"PASS: (a,b)=({a},{b}), discriminant {discriminant}, #E(F5)={count}, {count} exhibited rational points")
    # Explicit image representatives for E0 and both dual curves.
    assert 3**2 == 3**3-3*3**2+3*3
    assert 2*(-3) == -6 and (-3)**2-4*3 == -3
    assert -2*2 == -4 and 2**2-4*(-3) == 16


def substitutions():
    a, b, t = sp.symbols("a b t", nonzero=True, real=True)
    c = -b-2*a*a/b
    x2 = (a*a+b*b)/(a*a)
    y2 = (a*a+c*c)/(a*a+b*b)
    assert zero((x2-1)*(y2-1)-4)
    c = 2*a*a/b
    y2 = (a*a+c*c)/(a*a)
    assert zero((x2-1)*(y2-1)-4)

    t3 = t
    t2 = -t3-2/t3
    t1 = -t2-2/t2
    r2 = (1+t1*t1)/(1+t2*t2)
    s2 = (1+t2*t2)/(1+t3*t3)
    assert zero(r2*(s2+1)**2-(s2*s2+6*s2-3))

    x = sp.symbols("x", real=True)
    X = x*x
    Y2 = x*x*((x*x+3)/(x*x-1))*(x*x-1)**2
    assert zero(Y2-X*(X-1)*(X+3))
    Y2 = x*x*(x**4+6*x*x-3)
    assert zero(Y2-(X**3+6*X*X-3*X))
    print("PASS: triangle, fork, and chain identities and both elliptic-curve substitutions")


def main():
    graph_cover()
    arithmetic_certificates()
    substitutions()
    print("All exact certificates passed; the report supplies the source reduction and standard descent premises.")


if __name__ == "__main__":
    main()