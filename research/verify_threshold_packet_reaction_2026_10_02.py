#!/usr/bin/env python3
"""Exact certificates for the threshold packet reaction report.

Encodes: all source-pair distances in two six-point families; source cardinality,
unit separation, actual diameter/contact graphs, and a paired transverse balance;
an algebraic convex-average identity and finite hull-side constants.
Arithmetic: Fraction and integer square roots; radicals have rational enclosing
intervals. No floating-point sign decision is used.
Omits: actual O--O trains, full positive KKT equilibrium/PSD, global optimality,
and the near-disk source population. It cannot prove Level I or realizability of
the complete conditional threshold stack. General geometric proofs are analytic.
"""

from fractions import Fraction as F
from itertools import combinations
from math import isqrt


def rational_root(value):
    num, den = isqrt(value.numerator), isqrt(value.denominator)
    if num * num == value.numerator and den * den == value.denominator:
        return F(num, den)
    return None


def root_interval(value, bits=160):
    exact = rational_root(value)
    if exact is not None:
        return exact, exact
    lo, hi = F(0), max(F(1), value)
    for _ in range(bits):
        mid = (lo + hi) / 2
        if mid * mid < value:
            lo = mid
        else:
            hi = mid
    assert lo * lo <= value <= hi * hi
    return lo, hi


def sign(expr, roots):
    """Sign of c + b sqrt(k2) + d sqrt(C2), using rational bounds."""
    c, b, d = expr
    coeffs = [b, d]
    for i, root in enumerate(roots):
        exact = rational_root(root)
        if exact is not None:
            c += coeffs[i] * exact
            coeffs[i] = F(0)
    if coeffs == [0, 0]:
        return (c > 0) - (c < 0)
    lo = hi = c
    for coeff, root in zip(coeffs, roots):
        lower, upper = root_interval(root)
        lo += coeff * (lower if coeff >= 0 else upper)
        hi += coeff * (upper if coeff >= 0 else lower)
    if lo > 0:
        return 1
    if hi < 0:
        return -1
    raise AssertionError(f"No certified sign: {expr}, interval {lo, hi}")


def squared_distance(point, other, k2, C2):
    # Each x coordinate is p+q*k; each y coordinate is r+s*C.
    p, q, r, s = (a - b for a, b in zip(point, other))
    return p*p + q*q*k2 + r*r + s*s*C2, 2*p*q, 2*r*s


def points(D, k2, C2, offset):
    return {
        "La": (F(0), -F(1, 2), F(0), -F(1, 2)),
        "Ub": (F(0), F(1, 2), F(0), F(1, 2)),
        "Ua": (F(0), -F(1, 2), offset, F(1, 2)),
        "Lb": (F(0), F(1, 2), offset, -F(1, 2)),
        "z": (-D/2, F(0), offset/2, F(0)),
        "w": (D/2, F(0), offset/2, F(0)),
    }


def edge(a, b):
    return frozenset((a, b))


def check_family(D, strict=False):
    D = F(D)
    if strict:
        k2 = 1 - 1/(8*D*D)
        C2 = D*D - k2
        offset = 1/(2*D) - 1/(8*D**3)
        expected_contacts = set()
        expected_diameters = {edge("La", "Ub"), edge("Ua", "Lb"), edge("z", "w")}
    else:
        k2 = 1 - 1/(4*D*D)
        C = D - 1/(2*D)
        C2 = C*C
        offset = 1/(2*D)
        expected_contacts = {edge("La", "Lb"), edge("Ua", "Ub")}
        expected_diameters = {
            edge("La", "Ub"), edge("Ua", "Lb"), edge("La", "Ua"), edge("z", "w")
        }
    assert k2+C2 == D*D
    cloud = points(D, k2, C2, offset)
    for lower, upper in (("La", "Lb"), ("Ua", "Ub")):
        # This hypothetical unit u-port is NOT added to the source. It is
        # excluded by its certified distance below one from the upper vertex.
        p, q, r, s = cloud[lower]
        proposed = (p+1, q, r, s)
        c, x, y = squared_distance(proposed, cloud[upper], k2, C2)
        assert sign((c-1, x, y), (k2, C2)) == -1
    contacts, diameters = set(), set()
    for a, b in combinations(cloud, 2):
        c, x, y = squared_distance(cloud[a], cloud[b], k2, C2)
        lower = sign((c-1, x, y), (k2, C2))
        upper = sign((c-D*D, x, y), (k2, C2))
        assert lower >= 0 and upper <= 0, (D, strict, a, b)
        if lower == 0:
            contacts.add(edge(a, b))
        if upper == 0:
            diameters.add(edge(a, b))
    assert contacts == expected_contacts, (D, contacts)
    assert diameters == expected_diameters, (D, diameters)
    assert not any(all(edge(a, b) in contacts for a, b in combinations(tri, 2))
                   for tri in combinations(cloud, 3))
    # Equal paired weights cancel transverse components; reaction/mass = k < 1.
    assert 0 < k2 < 1
    if strict:
        short_square = k2 + offset*offset
        assert 1 < short_square < 1 + 1/(4*D*D)
        assert sign((D-offset, F(0), -F(1)), (k2, C2)) == 1
        assert sign((1/D**3-D+offset, F(0), F(1)), (k2, C2)) == 1
    return 15


def check_convex_average():
    D = F(10)

    def direction(t):
        return D*(1-t*t)/(1+t*t), D*2*t/(1+t*t)

    pos = [direction(F(1, 2)), direction(F(1, 3))]
    neg = [direction(F(1, 4)), direction(F(1, 5))]
    fp, fn = [F(1), F(2)], [F(2), F(1)]
    W = sum(fp)
    beta = [f/q for f, (_, q) in zip(fp+fn, pos+neg)]
    mass = sum(beta)
    reaction = sum(b*d for b, (d, _) in zip(beta, pos+neg))
    sum_mu = sum_murho = F(0)
    for i, (dp, qp) in enumerate(pos):
        for j, (dn, qn) in enumerate(neg):
            mu = fp[i]*fn[j]/W * (1/qp+1/qn)
            rho = (qn*dp+qp*dn)/(qp+qn)
            sum_mu += mu
            sum_murho += mu*rho
    assert sum_mu == mass and sum_murho == reaction


def main():
    distances = 0
    for D in (3, 4, 5, 8, 16, 100):
        distances += check_family(D)
        distances += check_family(D, strict=True)
        # The discarded offset produces a source pair below unit distance.
        D = F(D)
        assert 1-1/(8*D*D)+(1/(4*D))**2 < 1
    check_convex_average()
    # FS.1 radius ratios and the explicit D>=512 hull-side constant.
    assert F(512)**2 > F(256)**2*3
    assert F(12, 7*512) < F(1, 256)
    assert F(1779, 2304) > F(3, 4)
    assert F(3, 4)**2 > F(1, 2)
    print(f"PASS: {distances} certified pair distances, 12 source graphs, "
          "24 forbidden-port distances, 6 rejected choices, "
          "exact packet-average identity, hull-side constants")


if __name__ == "__main__":
    main()
