#!/usr/bin/env python3
"""Exact geometric corroboration for the ball-hull lattice capacity report.

Encoded: finite unit-separated rational antipodal sources with actual diameter
partners; support margins; the diameter-midpoint containing disk; injection
under small chart error; exact lattice Gram algebra; thin-parabola and two-port
continuation regressions, including arbitrarily large actual diameter endpoints.

Omitted: global optimality, canonical positive stress, retained train extraction,
boundary chart concentration, Fourier oscillatory integrals and Poisson sums.
The analytic BH.1 proof is not certified by these finite checks. Arithmetic is
Fraction and SymPy exact algebra; no floating point predicate is used.

Run: python3 research/verify_target_c_ball_hull_lattice_2026_10_02.py
"""

from fractions import Fraction as F
from itertools import combinations
from math import lcm
from collections import Counter

import sympy as sp


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def scale(a, s):
    return (s * a[0], s * a[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def norm2(a):
    return dot(a, a)


def rational_circle(t):
    return ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


def main():
    pair_checks = support_checks = midpoint_checks = injection_checks = 0
    circle = {rational_circle(F(a, b)) for a, b in
              [(0, 1), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1)]}
    circle |= {scale(p, -1) for p in tuple(circle)}
    denominator = lcm(*(x.denominator for p in circle for x in p))
    for multiplier in (1, 2, 5):
        radius = F(multiplier * denominator)
        diameter = 2 * radius
        source = sorted(scale(p, radius) for p in circle)
        source_set = set(source)
        for p, q in combinations(source, 2):
            assert 1 <= norm2(sub(q, p)) <= diameter * diameter
            pair_checks += 1
        z, a = source[0], scale(source[0], -1)
        assert norm2(sub(z, a)) == diameter * diameter
        midpoint = scale(add(z, a), F(1, 2))
        shift = (F(1, 100) / diameter, F(1, 100) / diameter)
        epsilon = F(1, 20) / diameter
        assert norm2(shift) <= epsilon * epsilon
        rounded = {p: add(p, shift) for p in source}
        assert len(set(rounded.values())) == len(source)
        injection_checks += len(source)
        for p in source:
            partner = scale(p, -1)
            assert partner in source_set
            assert norm2(sub(p, partner)) == diameter * diameter
            normal = scale(sub(p, partner), 1 / diameter)
            assert norm2(normal) == 1
            assert norm2(sub(p, midpoint)) <= F(3, 4) * diameter * diameter
            midpoint_checks += 1
            for q in source:
                if p == q:
                    continue
                delta = sub(q, p)
                assert dot(normal, delta) <= -norm2(delta) / (2 * diameter)
                # Strong support remains strict after the encoded rounding.
                assert dot(normal, sub(rounded[q], rounded[p])) < 0
                support_checks += 1

    # The full-hull analogue is false. Middle thin-parabola points are not
    # diameter endpoints even though all points are close to one exact chart.
    parabola_checks = 0
    for count in range(2, 21):
        source = [(F(i), F(i * i, count**4))
                  for i in range(-count, count + 1)]
        diameter2 = F(4 * count * count)
        hits = []
        for i, j in combinations(range(len(source)), 2):
            length2 = norm2(sub(source[j], source[i]))
            assert 1 <= length2 <= diameter2
            if length2 == diameter2:
                hits.append((i, j))
            parabola_checks += 1
        assert hits == [(0, len(source) - 1)]
        slopes = [sub(source[i + 1], source[i])[1]
                  for i in range(len(source) - 1)]
        assert all(slopes[i] < slopes[i + 1] for i in range(len(slopes) - 1))
        assert all(y <= F(1, count * count) for _, y in source)

    # Exact conditioning identity for the entire allowed lattice family.
    c = sp.symbols("c", real=True)
    gram = sp.Matrix([[1, c], [c, 1]])
    assert gram.charpoly().all_coeffs() == [1, -2, 1 - c**2]
    assert sp.expand(gram.det() - (1 - c**2)) == 0

    # Full finite difference alphabet on c in [9/20,1/2]. Squared lengths
    # are affine in c, so endpoint checks classify the entire interval.
    allowed = {(1, 0), (0, 1), (1, -1), (1, 1), (2, -1), (1, -2),
               (2, 0), (0, 2), (2, -2)}
    allowed |= {(-i, -j) for i, j in tuple(allowed)}
    found = set()
    alphabet_checks = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i == j == 0 or i*i + j*j > 8:
                continue
            at_left = sp.Rational(i*i + j*j) + 2*i*j*sp.Rational(9, 20)
            at_right = sp.Rational(i*i + j*j + i*j)
            if min(at_left, at_right) <= 4:
                found.add((i, j))
            alphabet_checks += 1
    assert found == allowed
    # The extra vector is admissible only at the triangular endpoint.
    assert 8 - 8*sp.Rational(9, 20) > 4
    assert 8 - 8*sp.Rational(1, 2) == 4
    u0 = sp.Matrix([1, 0])
    v0 = sp.Matrix([sp.Rational(1, 2), sp.sqrt(3)/2])
    port_table = [((1, -1), [(1, 0), (0, -1)]),
                  ((2, -1), [(1, 0), (1, -1)]),
                  ((1, -2), [(0, -1), (1, -1)])]
    for (i, j), endpoints in port_table:
        w0 = i*u0 + j*v0
        for a, b in endpoints:
            point = a*u0 + b*v0
            assert sp.simplify(point.dot(point) - 1) == 0
            assert sp.simplify((point-w0).dot(point-w0) - 1) == 0
    # Rational squared bounds used to control the continuous derivative.
    assert sp.Rational(4, 3) < sp.Rational(36, 25)
    assert sp.Rational(5, 4) < sp.Rational(25, 16)
    assert sp.Rational(3, 2)*sp.Rational(12, 5) + 2*sp.Rational(5, 4)*4 < 14
    assert 14 + sp.Rational(6, 5) < 20

    # Three exact ports: every possible radius-one lattice triangle is tested
    # by a polynomial identity, not by cosine samples. This finite enumeration
    # supports the BH.5 factor table throughout the full continuous interval.
    vectors = [(i, j) for i in range(-2, 3) for j in range(-2, 3)
               if 0 < i*i+j*j <= 8]
    quadratic = lambda a: a[0]**2+a[1]**2+2*a[0]*a[1]*c
    factors = Counter()
    identities = triangle_checks = triangular_endpoint_checks = 0
    identity_centers = set()
    for a, b in combinations(vectors, 2):
        determinant = a[0]*b[1]-a[1]*b[0]
        if not determinant:
            continue
        difference = (a[0]-b[0], a[1]-b[1])
        if any(min(quadratic(z).subs(c, sp.Rational(9, 20)),
                   quadratic(z).subs(c, sp.Rational(1, 2))) > 4
               for z in (a, b, difference)):
            continue
        poly = sp.Poly(sp.expand(quadratic(a)*quadratic(b)*quadratic(difference)
                                - 4*(1-c*c)*determinant**2), c)
        basis_coefficients = sp.simplify(
            (sp.Matrix([a, b])*gram).inv()
            * sp.Matrix([quadratic(a)/2, quadratic(b)/2]))
        triangle_checks += 1
        if poly.is_zero:
            identities += 1
            center = tuple(basis_coefficients)
            assert center in {(-1, 0), (1, 0), (0, -1), (0, 1)}
            identity_centers.add(center)
        else:
            factors[sp.factor(poly.monic().as_expr())] += 1
        if poly.eval(sp.Rational(1, 2)) == 0:
            endpoint = basis_coefficients.subs(c, sp.Rational(1, 2))
            assert all(z.is_integer for z in endpoint)
            triangular_endpoint_checks += 1
    expected_factors = {
        (2*c-1)**2/4: 12,
        (c-1)**2: 6,
        (c-1)*(2*c-1)/2: 24,
        (c+1)*(2*c-1)*(8*c-7)/16: 6,
        (c+1)*(2*c-1)/2: 6,
        (c-1)*(2*c+1)/2: 6,
    }
    assert factors == Counter({sp.factor(k): v for k, v in expected_factors.items()})
    assert identities == 12 and triangle_checks == 72
    assert identity_centers == {(-1, 0), (1, 0), (0, -1), (0, 1)}

    # BH.6 leaf-location constants: universal conclusions have analytic proofs;
    # these rational checks cover the explicit large-D cutoff and contractions.
    leaf_constant_checks = 0
    for root_d in (256, 512, 1024, 4096, 65536):
        diameter = F(root_d*root_d)
        # 3^(1/4)<4/3 supplies a rational upper bound for eta.
        eta_upper = F(4, 3)*root_d
        epsilon1 = 32*(eta_upper+1)/diameter
        assert epsilon1 < F(1, 2)
        # sqrt(3)/2<7/8 implies the coarser ball inradius is positive.
        assert (1-F(7, 8))*diameter-1 > 0
        for d in (diameter-2, diameter-1, diameter):
            zeta = epsilon1/2
            assert (d-1+2*zeta)**2 >= (d-1)**2+2*d*zeta
            leaf_constant_checks += 1
        # The exact symbolic cancellation in the radial contraction.
        radius = (1-sp.sqrt(3)/2)*sp.Rational(diameter)-1
        assert sp.simplify((radius/(radius+sp.Rational(epsilon1)))
                           * sp.Rational(epsilon1)
                           - (sp.Rational(epsilon1)/(radius+sp.Rational(epsilon1)))
                           * radius) == 0
        # r_*>=D/8 follows from sqrt(3)/2 <= 7/8-1/D here.
        assert F(3, 4) <= (F(7, 8)-1/diameter)**2
        leaf_constant_checks += 1

    # One chart port leaves a fixed nonzero error even for a triangular chart.
    one_port = (F(3, 5), F(4, 5))
    assert norm2(one_port) == 1
    chart_units = [u0, -u0, v0, -v0, u0-v0, v0-u0]
    assert all(sp.Matrix(one_port) != z for z in chart_units)
    one_port_checks = 0
    for diameter in (3, 64, 512, 4096):
        source = [(F(0), F(0)), one_port, scale(one_port, 1-diameter)]
        assert norm2(sub(source[1], source[2])) == diameter*diameter
        assert norm2(source[2]) == (diameter-1)**2
        for a, b in combinations(source, 2):
            assert 1 <= norm2(sub(a, b)) <= diameter*diameter
            one_port_checks += 1

    # Two chart contacts do not force exact chart membership. The proof that
    # +/-u,+/-v are the only unit chart vectors is analytic in the report.
    algebraic_sources = algebraic_pair_checks = 0
    for cosine in (sp.Rational(3, 10), sp.Rational(1, 3), sp.Rational(2, 5),
                   sp.Rational(9, 20), sp.Rational(49, 100),
                   sp.Rational(499, 1000)):
        sine = sp.sqrt(1 - cosine**2)
        u, v = sp.Matrix([1, 0]), sp.Matrix([cosine, sine])
        w = 2 * u - v
        length2 = 5 - 4 * cosine
        jw = sp.Matrix([-w[1], w[0]])
        p = w / 2 + jw * sp.sqrt((4 - length2) / (4 * length2))
        n = jw / sp.sqrt(length2)
        height = sp.sqrt(1 - length2 / 4)
        assert sp.simplify(p.dot(p) - 1) == 0
        assert sp.simplify((p - w).dot(p - w) - 1) == 0
        assert sp.simplify(n.dot(n) - 1) == 0
        assert sp.simplify(p.dot(n) - height) == 0
        for chart_unit in (u, -u, v, -v):
            d2 = sp.simplify((chart_unit - w).dot(chart_unit - w))
            assert d2 != 1
        for diameter in (sp.Integer(64), sp.Integer(512), sp.Integer(4096)):
            y = p - diameter * n
            source = [sp.zeros(2, 1), w, p, y]
            expected = diameter**2 - 2 * diameter * height + 1
            assert sp.simplify(y.dot(y) - expected) == 0
            assert sp.simplify((y - w).dot(y - w) - expected) == 0
            # Exact squared comparisons avoid ordering general algebraic roots.
            assert 4 * diameter**2 * height**2 > 1  # expected < D^2
            assert diameter**2 > 4 * height**2      # expected > 1
            for i, j in combinations(range(4), 2):
                got = sp.simplify((source[j] - source[i]).dot(source[j] - source[i]))
                target = {(0, 1): length2, (0, 2): 1, (1, 2): 1,
                          (0, 3): expected, (1, 3): expected,
                          (2, 3): diameter**2}[(i, j)]
                assert sp.simplify(got - target) == 0
                algebraic_pair_checks += 1
            algebraic_sources += 1

    print(f"PASS: {pair_checks} rational source pairs; {support_checks} exact "
          f"support margins; {midpoint_checks} midpoint bounds; "
          f"{injection_checks} rounded representatives; {parabola_checks} "
          f"thin-parabola pairs; symbolic lattice conditioning; "
          f"{alphabet_checks} complete difference-alphabet checks; "
          f"{triangle_checks} three-port polynomials / {identities} identities / "
          f"{triangular_endpoint_checks} exact triangular centers; "
          f"{leaf_constant_checks} rational leaf-location bounds; "
          f"{one_port_checks} rational one-port pairs; "
          f"{algebraic_sources} algebraic two-port sources / "
          f"{algebraic_pair_checks} exact pair identities.")
    print("No Fourier, global-optimality, positive-stress, train, or atlas-"
          "concentration certificate is claimed.")


if __name__ == "__main__":
    main()
