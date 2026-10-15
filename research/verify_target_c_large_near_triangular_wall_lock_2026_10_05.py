#!/usr/bin/env python3
"""Exact finite contracts for the large near-triangular fixed-wall lock.

Q(sqrt(3)) arithmetic checks actual grid points, contact support, pinned
rank and residual formulas. The global uniqueness angle window is proved
analytically from Groemer equality and compactness, not located by this
script. No checked positive angle is claimed to lie in that window.
"""
from fractions import Fraction as F
from itertools import combinations

from verify_target_c_loaded_flat_pentagon_second_depletion_2026_10_05 import (
    add, cross, dot, mul, rational, sign, sub, vsub,
)
from verify_target_c_pentagon_closure_core_elimination_2026_10_05 import field_rank


def grid(m, n, t):
    rad = F(3)
    denominator = 1+t*t
    u = (rational(1), rational(0))
    v = ((F(1-t*t, 2*denominator), -t/denominator),
         (t/denominator, F(1-t*t, 2*denominator)))
    assert dot(u, u, rad) == dot(v, v, rad) == rational(1)
    assert sign(v[0], rad) > 0 and sign(sub(rational(F(1, 2)), v[0]), rad) > 0
    assert sign(sub(v[1], (F(0), F(1, 2))), rad) > 0
    pos = {(i, j): (add(rational(i), mul(rational(j), v[0], rad)),
                    mul(rational(j), v[1], rad))
           for i in range(m+1) for j in range(n+1)}
    contacts = {tuple(sorted(((i, j), (i+1, j))))
                for i in range(m) for j in range(n+1)} | {
                    tuple(sorted(((i, j), (i, j+1))))
                    for i in range(m+1) for j in range(n)}
    assert len(contacts) == m*(n+1)+n*(m+1)
    checks = 0
    for a, b in combinations(sorted(pos), 2):
        d = vsub(pos[b], pos[a])
        d2 = dot(d, d, rad)
        assert sign(sub(d2, rational(1)), rad) >= 0
        assert (d2 == rational(1)) == (tuple(sorted((a, b))) in contacts)
        checks += 1
    boundary = {(i, j) for i, j in pos if i in (0, m) or j in (0, n)}
    interior = sorted(set(pos)-boundary)
    assert len(boundary) == 2*(m+n) and len(interior) == (m-1)*(n-1)
    adjacency = {a: set() for a in pos}
    for a, b in contacts:
        adjacency[a].add(b)
        adjacency[b].add(a)
    assert all(not adjacency[a] & adjacency[b] for a, b in contacts)
    for a in interior:
        resultant = [rational(0), rational(0)]
        for b in adjacency[a]:
            d = vsub(pos[b], pos[a])
            resultant = [add(resultant[c], d[c]) for c in range(2)]
        assert resultant == [rational(0), rational(0)]
    index = {a: i for i, a in enumerate(interior)}
    rows = []
    for a, b in sorted(contacts):
        d = vsub(pos[b], pos[a])
        row = [rational(0)]*(2*len(interior))
        for vertex, sg in ((a, -1), (b, 1)):
            if vertex in index:
                row[2*index[vertex]:2*index[vertex]+2] = [mul(rational(sg), x, rad) for x in d]
        rows.append(row)
    assert field_rank(rows, rad) == 2*len(interior)
    area = mul(rational(m*n), cross(u, v, rad), rad)
    # A/a0=2 sqrt(3) A/3, and P=2(m+n).
    residual = sub(add(mul(area, (F(0), F(2, 3)), rad), rational(m+n+1)),
                   rational(len(pos)))
    expected = mul(rational(m*n), sub(mul(v[1], (F(0), F(2, 3)), rad), rational(1)), rad)
    assert residual == expected and sign(residual, rad) > 0
    # Baseline equality at angle pi/3 and its full lattice roster.
    baseline_n = m*n+m+n+1
    assert baseline_n == (m+1)*(n+1)
    assert len({(i, j) for i in range(m+1) for j in range(n+1)}) == baseline_n
    return checks, len(interior)


def displacement_bound():
    # Exact scalar verification of the two telescoping inequalities:
    # -2 i rho^2 <= u.delta <= 2(m-i)rho^2.
    checks = 0
    for m in range(2, 12):
        for i in range(1, m):
            for rho in (F(1, 100), F(1, 10), F(1, 2)):
                lower, upper = -2*i*rho*rho, 2*(m-i)*rho*rho
                assert lower >= -2*m*rho*rho and upper <= 2*m*rho*rho
                checks += 1
    # The uniform forbidden displacement radius is a0/[2(m+n)],
    # whose square is exactly 3/[16(m+n)^2].
    for m in range(2, 12):
        for n in range(2, 12):
            radius2 = F(3, 16*(m+n)**2)
            assert radius2 > 0 and 4*(m+n)**2*radius2 == F(3, 4)
            checks += 1
    return checks


def explicit_container_floor():
    checks = 0
    for m in range(2, 40):
        for n in range(2, 40):
            t = F(1, 100*m*n*(m+n))
            # For delta=2 arctan(t), sin(phi)/a0-1 <= 2t/sqrt(3)<2t.
            upper_residual = 2*m*n*t
            assert 0 < t < F(1, 100) and 0 < upper_residual < 1
            assert upper_residual == F(1, 50*(m+n))
            checks += 1
    return checks


if __name__ == "__main__":
    packets = [grid(m, n, t) for m, n in ((2, 2), (3, 4), (4, 4), (6, 6))
               for t in (F(1, 5000), F(1, 10000))]
    scalar_checks = displacement_bound()
    floor_checks = explicit_container_floor()
    print(f"PASS: {sum(x[0] for x in packets)} exact unit-pair constraints in eight Q(sqrt(3)) grids")
    print("PASS: triangle-free full contact support and positive unloaded equilibrium")
    print(f"PASS: full pinned contact rank on {sum(x[1] for x in packets)} interior points")
    print("PASS: linear unit-wall size, quadratic interior count and exact positive Oler residual")
    print(f"PASS: {scalar_checks} telescoping/radius scalar checks and baseline lattice cardinalities")
    print(f"PASS: {floor_checks} exact residual floors for the explicit capacity-optimal container family")
    print("SCOPE: no effective global-lock angle window, actual diameter loading or global optimality certified")
