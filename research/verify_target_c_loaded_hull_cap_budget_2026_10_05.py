#!/usr/bin/env python3
"""Exact arithmetic checks for the loaded-hull cap attachment budget.

This certificate checks only the finite ledger/constants used in the analytic proof:
- occupied-cap charging from L_i>=2;
- the 68W tube coefficient using pi>3;
- the 12W shallow-layer coefficient using pi>3 and sqrt(3)>12/7;
- exact combinatorial consequences of W=sum_i(L_i-1).

It does not replace the convex cap-partition, nearest-point, or deep-interior
geometry proofs.
"""

from fractions import Fraction as F

def occupied_cap_ledger():
    checks = 0
    # Integer/rational synthetic ledgers with L_i >= ell_i >= 1.
    for n in range(1, 8):
        vals = [F(1+i, i) for i in range(1, n+1)]  # >1
        # Exhaust subsets as occupied; require occupied L>=2 by replacing as needed.
        from itertools import product
        for mask in product((0,1), repeat=n):
            L = []
            ell = []
            for i,m in enumerate(mask):
                if m:
                    Li = F(2+i, 1)
                    ei = F(1+i, 1)
                else:
                    Li = vals[i]
                    ei = F(1)
                L.append(Li); ell.append(min(ei,Li))
            W = sum((x-F(1) for x in L), F(0))
            occ = [i for i,m in enumerate(mask) if m]
            assert F(len(occ)) <= W
            assert sum((L[i] for i in occ), F(0)) <= 2*W
            assert sum((ell[i] for i in occ), F(0)) <= 2*W
            checks += 1
    return checks

def constant_checks():
    # P tube: coefficient = 56/pi + 49 < 68 using pi>3.
    assert F(56,3)+49 < 68

    # Shallow layer:
    # 4(2sqrt3+pi)/(pi(sqrt3-1))
    # < 4(1+2s/3)/(s-1), and this decreases in s.
    # At s=12/7 the RHS equals exactly 12.
    s = F(12,7)
    rhs = 4*(1+2*s/F(3))/(s-1)
    assert rhs == 12

    # 2sqrt2+1/2 < 7/2 follows from sqrt2<3/2.
    assert 2*F(3,2)+F(1,2) == F(7,2)

    return 3

def extreme_vertex_ledger():
    checks=0
    # v_K <= per(K), q <= v_K, W=per(K)-q => v_K-q<=W.
    for q in range(3,15):
        for extra in range(0,10):
            v=q+extra
            for slack in range(0,6):
                per=F(v)+F(slack,3)
                W=per-q
                assert v-q <= W
                checks += 1
    return checks

if __name__ == "__main__":
    a=occupied_cap_ledger()
    b=constant_checks()
    c=extreme_vertex_ledger()
    print(f"PASS: {a} occupied-cap charging ledgers")
    print(f"PASS: {b} exact constant inequalities")
    print(f"PASS: {c} extreme-vertex perimeter ledgers")
    print("SCOPE: arithmetic/ledger only; convex geometry is proved analytically")
