#!/usr/bin/env python3
"""Exact regressions for weak-packet correction mass, not global optimality.

Encode: eight actual rational source points; every pair in [1,D]; every actual
diameter and positive normalized formal diameter weight; one A cut and a linear
number of repeated B cut equations; the global contact/diameter second-moment
identity with formal unit directions and contact coefficients at most D.
Omit: realization of those formal contacts/cuts at the eight points, vertex
equilibrium, actual O--O trains, canonical mixed rigidity/PSD, and global
optimality. A separate actual dense local grid supplies quadratic population
but keeps the diameter endpoints unloaded. The original contacts are certified
but are NOT the formal contacts. No positive output supplies those omissions.
All arithmetic is Fraction; general geometric claims have analytic proofs.
"""

from fractions import Fraction as F
from itertools import combinations
from math import ceil, isqrt


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def outer(x):
    return (x[0] ** 2, x[0] * x[1], x[1] ** 2)


def run(k, v):
    t = F(1, k)
    s0 = 2 * t / (1 + t * t)
    d = (1 - t * t) / (1 + t * t)
    D = 1 / (2 * s0)
    q = D * (1 - 2 * s0 * s0)
    a = D - q
    c, s = v
    assert c * c + s * s == 1 and c != 0 and s > 0
    sigma = 1 if c > 0 else -1
    assert d * d + q * q == D * D and d < 1
    assert d * d + a * a == 1
    pts = [
        (-d / 2, -q / 2), (d / 2, q / 2),
        (-d / 2, q / 2 + a), (d / 2, -q / 2 + a),
        (-D / 2, a / 2), (D / 2, a / 2),
        (-sigma * D * s / 2, a / 2 + sigma * D * c / 2),
        (sigma * D * s / 2, a / 2 - sigma * D * c / 2),
    ]
    diameters, contacts = set(), set()
    for i, j in combinations(range(8), 2):
        delta = sub(pts[j], pts[i])
        z = dot(delta, delta)
        assert 1 <= z <= D * D, (k, v, i, j, z)
        if z == D * D:
            diameters.add((i, j))
        if z == 1:
            contacts.add((i, j))
    assert diameters == {(0, 1), (2, 3), (0, 2), (4, 5), (6, 7)}
    assert contacts == {(0, 3), (1, 2)}

    # Small positive weights retain the third original diameter and reference.
    eta = 1 / (100 * D * D)
    M = (1 - eta * (2 + abs(c))) / (1 + abs(c) * q / D)
    bc = abs(c) * (M * q / D + eta)
    weights = {(0, 1): M / 2, (2, 3): M / 2,
               (0, 2): eta, (4, 5): eta, (6, 7): bc}
    assert all(x > 0 for x in weights.values())
    assert sum(weights.values()) == 1

    # Weak pair alone: axial reaction per mass d<1; export (0,Mq).
    assert M * q * abs(c) <= D * (1 - M)
    CB = (M * q + eta * D) * s
    B_load = (bc * sigma * D * s, M * q + eta * D - bc * sigma * D * c)
    assert B_load == (CB * c, CB * s)
    CA = M * d + eta * D
    assert 0 < CA <= D and 0 < CB <= D
    n = int(D // 100)
    assert n >= 1
    # Identical full support permits the same correction at all n cuts.
    for _ in range(n):
        assert B_load == (CB * c, CB * s)

    R = [F(0), F(0), F(0)]
    for edge, beta in weights.items():
        vec = sub(pts[edge[1]], pts[edge[0]])
        for j, val in enumerate(outer(vec)):
            R[j] += beta * val
    assert R[0] + R[2] == D * D
    # Formal A/B contact rows are included before the remaining moment is filled.
    T = [R[0] - CA - n * CB * c * c,
         R[1] - n * CB * c * s,
         R[2] - n * CB * s * s]
    assert T[0] > 0 and T[2] > 0 and T[0] * T[2] - T[1] ** 2 > 0
    z = T[1] / T[0]
    alpha1 = T[0] * (1 + z * z)
    alpha2 = T[2] - T[1] ** 2 / T[0]
    assert alpha1 > 0 and alpha2 > 0
    assert CA + n * CB + alpha1 + alpha2 == D * D
    # T=T00*(1,z)(1,z)^T+alpha2*(0,1)(0,1)^T. After normalizing
    # (1,z), its contact coefficient is alpha1. Split formal copies to cap alpha.
    copies1, copies2 = ceil(alpha1 / D), ceil(alpha2 / D)
    assert 0 < alpha1 / copies1 <= D and 0 < alpha2 / copies2 <= D
    reconstructed = [CA + n * CB * c * c + alpha1 / (1 + z * z),
                     n * CB * c * s + alpha1 * z / (1 + z * z),
                     n * CB * s * s + alpha1 * z * z / (1 + z * z) + alpha2]
    assert reconstructed == R

    # Exact angular-cost identity on arbitrary rational unit directions.
    def form(vec):
        x, y = vec
        return sigma * y * (-s * x + c * y)
    rhs = sum(beta * form(sub(pts[j], pts[i]))
              for (i, j), beta in weights.items())
    lhs = alpha1 * form((1, z)) / (1 + z * z) + alpha2 * abs(c)
    # A and B directions are zeros of the form.
    assert form((1, 0)) == form(v) == 0 and rhs == lhs
    return n, copies1 + copies2 + n + 1


def dense_source(k):
    """Co-embed an actual near-triangular grid, without claiming vertex KKT."""
    b0 = k * k
    a0 = isqrt(3 * b0 * b0)
    v = (F(a0 * a0 - b0 * b0, a0 * a0 + b0 * b0),
         F(2 * a0 * b0, a0 * a0 + b0 * b0))
    c, s = v
    assert 0 < c < F(1, 2) and c * c + s * s == 1
    run(k, v)  # Also validates the eight boundary points/formal stress system.
    t = F(1, k)
    s0 = 2 * t / (1 + t * t)
    D = 1 / (2 * s0)
    d = (1 - t * t) / (1 + t * t)
    q = D * (1 - 2 * s0 * s0)
    a = D - q
    failed_port = (c - d) ** 2 + (s - a) ** 2
    assert failed_port == 2 - 2 * (c * d + s * a) and failed_port < 1
    reflected_port = (d - c) ** 2 + (s - a) ** 2
    assert reflected_port == failed_port
    # Boundary coordinates are relative to o=(0,a/2).
    boundary = [(-d / 2, -D / 2), (d / 2, D / 2 - a),
                (-d / 2, D / 2), (d / 2, -D / 2 + a),
                (-D / 2, F(0)), (D / 2, F(0)),
                (-D * s / 2, D * c / 2),
                (D * s / 2, -D * c / 2)]
    for pt in boundary:
        norm2 = dot(pt, pt)
        assert (D / 2 - 1) ** 2 <= norm2 <= (D / 2 + 1) ** 2
    # Exact finite release. The two short boundary contacts move as rigid pairs;
    # reference/correction diameters contract along their own directions.
    lam = 1 / (100 * D)
    speeds = [(F(0), F(1)), (F(0), -F(1)), (F(0), -F(1)),
              (F(0), F(1)), (F(1), F(0)), (-F(1), F(0)),
              (s, -c), (-s, c)]
    moved = [tuple(x + lam * v0 for x, v0 in zip(pt, speed))
             for pt, speed in zip(boundary, speeds)]
    for i, j in combinations(range(8), 2):
        oldz = dot(sub(boundary[j], boundary[i]), sub(boundary[j], boundary[i]))
        if (i, j) not in {(0, 3), (1, 2)}:
            assert oldz >= 4
        z = dot(sub(moved[j], moved[i]), sub(moved[j], moved[i]))
        assert 1 <= z < D * D
        assert (z == 1) == ((i, j) in {(0, 3), (1, 2)})
    assert 2 - 2 * lam > 1  # Entire segment preserves all inactive lower bounds.
    for pt in moved:
        norm2 = dot(pt, pt)
        assert (D / 2 - 1 - lam) ** 2 <= norm2 <= (D / 2 + 1) ** 2
    R = D / 2 - 3
    assert R > 1
    bound = ceil(R / s)
    cn, cd = c.numerator, c.denominator
    rn, rd = R.numerator, R.denominator
    indices = set()
    for i in range(-bound, bound + 1):
        for j in range(-bound, bound + 1):
            if (cd * (i * i + j * j) + 2 * cn * i * j) * rd * rd <= rn * rn * cd:
                indices.add((i, j))
    assert (0, 0) in indices
    contacts = sum((i + 1, j) in indices for i, j in indices)
    contacts += sum((i, j + 1) in indices for i, j in indices)
    h = int(R // 4)
    assert all((i, j) in indices for i in range(-h, h + 1)
               for j in range(-h, h + 1))
    # The full lattice's shortest vectors are exactly +/-u,+/-v when 0<c<1/2.
    # Check the only potentially short finite candidates; the general proof is
    # a^2+b^2-ab>=1 for integer a,b>=1, as documented in the report.
    for i in range(-4, 5):
        for j in range(-4, 5):
            if i or j:
                z = F(i * i + j * j) + 2 * c * i * j
                assert z >= 1
                assert (z == 1) == (abs(i) + abs(j) == 1)
    # Triangle inequality, with the exact radius bounds above, certifies ALL
    # interior-boundary pairs as strictly between 1 and D, without quadratic scans.
    assert D / 2 - 1 - R == 2
    assert D / 2 - 1 - lam - R > 1
    assert D / 2 + 1 + R == D - 2 < D
    assert 2 * R < D
    return len(indices) + 8, contacts + 2, 2 * h


def main():
    cases = 0
    cuts = 0
    formal_contacts = 0
    for k in (401, 503, 701, 1001, 2001, 4001):
        for v in ((F(3, 5), F(4, 5)), (F(8, 17), F(15, 17)),
                  (F(5, 13), F(12, 13)), (-F(3, 5), F(4, 5)),
                  (-F(8, 17), F(15, 17)), (-F(5, 13), F(12, 13))):
            n, count = run(k, v)
            cases += 1
            cuts += n
            formal_contacts += count
    print(f"PASS: {cases} rational sources; {28 * cases} exact pair distances; "
          f"{cuts} repeated cut balances; {formal_contacts} bounded formal contacts")
    print("PASS: positive weights on every actual diameter; exact tensor and trace identities")
    for k in (401, 503, 701):
        size, contacts, shore = dense_source(k)
        print(f"PASS dense k={k}: {size} actual points, {contacts} actual contacts, "
              f"local complete {shore}x{shore} rhombus grid; boundary pairs are strict")
    print("PASS: six forbidden near-triangular unit ports in the dense cases")
    print("PASS: three finite strict diameter competitors preserve every actual contact")
    print("OMITTED: realization of formal contacts/cuts, vertex equilibrium, global optimality")


if __name__ == "__main__":
    main()
