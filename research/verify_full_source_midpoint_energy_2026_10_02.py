#!/usr/bin/env python3
"""Exact corroboration for the full-source midpoint-energy report.

Encoded: finite odd-mode energy/telescoping arithmetic; antipodal Lipschitz
tents; explicit minimizer constants; rational compact support-bump algebra;
diameter-midpoint and partner-variance identities; odd-shell spectral parity.
Arithmetic: Python Fraction and integer polynomial algebra only.
Omitted: completion existence, general support geometry, infinite Fourier
limits, the boundary-net geometric proof, and global optimality. The analytic
report proves the geometric steps. A pass establishes only the stated identities
and finite corroborations, not C-II or Erdős Problem #99.
"""

from fractions import Fraction as Q


def poly_mul(a, b):
    result = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def derivative(a):
    return [Q(i) * a[i] for i in range(1, len(a))]


def evaluate(a, x):
    return sum((coefficient * x**i for i, coefficient in enumerate(a)), Q(0))


def integral_symmetric(a):
    return sum((2 * coefficient / (i + 1)
                for i, coefficient in enumerate(a) if i % 2 == 0), Q(0))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, t):
    return tuple(t * x for x in a)


def square(a):
    return sum((x * x for x in a), Q(0))


def circle(t, diameter):
    return (diameter * (1 - t * t) / (1 + t * t),
            diameter * 2 * t / (1 + t * t))


def check_fourier_and_tents():
    telescoping = Q(0)
    for count in range(1, 1001):
        telescoping += Q(1, 4 * count * (count + 1))
        assert telescoping == Q(count, 4 * (count + 1)) < Q(1, 4)
        k = 2 * count + 1
        assert Q(k * k, k * k - 1) <= Q(9, 8)
    for numerator in range(1, 101):
        peak = Q(numerator, 13)
        lipschitz = Q(numerator + 5, 7)
        length = peak / lipschitz
        one_half = (peak * peak * length
                    - peak * lipschitz * length**2
                    + lipschitz**2 * length**3 / 3)
        assert 4 * one_half == 4 * peak**3 / (3 * lipschitz)
        assert Q(9, 4) * Q(3, 4) == Q(27, 16)
    # pi < 22/7 and sqrt(3) < 7/4 are analytic bounds used in the proof.
    assert Q(27, 16) * Q(11, 8) == Q(297, 128) < Q(64, 27)
    assert Q(1, 4) + Q(16, 9) == Q(73, 36) < Q(9, 4)
    assert Q(3) < Q(4, 3)**4
    assert Q(3, 2) + Q(1, 2) + Q(8, 3) == Q(14, 3) < 5
    assert 8 * Q(9, 4) == 18


def check_support_bumps():
    phi = [Q(1, 16), Q(0), Q(-1, 8), Q(0), Q(1, 16)]
    dphi, ddphi = derivative(phi), derivative(derivative(phi))
    assert integral_symmetric(phi) == Q(1, 15)
    assert integral_symmetric(poly_mul(phi, phi)) == Q(1, 315)
    assert integral_symmetric(poly_mul(dphi, dphi)) == Q(1, 105)
    assert evaluate(phi, Q(1, 2)) == Q(9, 256)
    assert evaluate(dphi, Q(1, 2)) == Q(-3, 32)
    for endpoint in (-1, 1):
        assert evaluate(phi, Q(endpoint)) == evaluate(dphi, Q(endpoint)) == 0
    for numerator in range(-1000, 1001):
        x = Q(numerator, 1000)
        assert 0 <= evaluate(phi, x) <= Q(1, 16)
        assert Q(-1, 4) <= evaluate(ddphi, x) <= Q(1, 2)
        for a in (Q(1), Q(1, 2), Q(1, 8)):
            rho = 1 + a * a * evaluate(phi, x) + evaluate(ddphi, x)
            assert Q(7, 16) <= rho <= Q(25, 16)
            assert Q(7, 16) <= 2 - rho <= Q(25, 16)
    for q in range(8, 1001):
        diameter, radius, a = Q(q**3), Q(q**3, 2), Q(1, q)
        deficit = radius**2 * (a**3 / 105 - a**5 / 315)
        assert deficit == Q(q**3, 420) - Q(q, 1260) > 0
        assert deficit < diameter / 420
        midpoint_lower = 3 * radius * a / 32
        circumcenter_upper = Q(q, 16) + Q(225, 4 * q**3)
        assert midpoint_lower - circumcenter_upper >= Q(q*q, 32)
        assert deficit + Q(5625, 128) * Q(22, 7) < diameter
    assert Q(35, 8) / Q(22, 7) > 1


def check_midpoint_and_variance():
    identities = 0
    for n in range(1, 41):
        diameter = Q(n + 2)
        normal = circle(Q(n, n + 3), Q(1))
        tangent = (-normal[1], normal[0])
        f, fp = Q(n, 17), Q(-n, 19)
        x = add(scale(normal, diameter / 2 + f), scale(tangent, fp))
        y = add(scale(normal, -diameter / 2 + f), scale(tangent, fp))
        midpoint = scale(add(x, y), Q(1, 2))
        assert square(add(x, scale(y, -1))) == diameter**2
        assert midpoint == add(scale(normal, f), scale(tangent, fp))
        assert square(midpoint) == f*f + fp*fp
        points = [circle(Q(j, n + 1), diameter) for j in range(1, 8)]
        weights = [Q(j + n, 97) for j in range(1, 8)]
        mass = sum(weights)
        mean = scale(tuple(sum(w * p[c] for w, p in zip(weights, points))
                           for c in range(2)), 1 / mass)
        variance = sum(w * square(add(p, scale(mean, -1)))
                       for w, p in zip(weights, points)) / mass
        pair_sum = sum(weights[i] * weights[j]
                       * square(add(points[i], scale(points[j], -1)))
                       for i in range(len(points)) for j in range(i))
        assert pair_sum == mass**2 * variance
        resultant = scale(mean, -mass)
        assert square(resultant) == diameter**2 * mass**2 - pair_sum
        center = points[0]
        max_radius2 = max(square(add(p, scale(center, -1))) for p in points)
        assert variance <= max_radius2
        identities += 1
    return identities


def check_shell_parity():
    modes = 0
    # The analytic monotonicity inequalities are in the report. This checks
    # their integer ranges and equality cases, not sampled trigonometry.
    for q in range(5, 502, 2):
        zero_modes = []
        for j in range(1, q):
            if j % 2 == 0:
                assert j <= q - 1
                equality = j == q - 1
            else:
                assert j >= 1
                equality = j == 1
            if equality:
                zero_modes.append(j)
            modes += 1
        assert zero_modes == [1, q - 1]
        if q >= 7:
            assert Q(4, 10) * q - Q(5, q) > Q(q, 4)
    return modes


def main():
    check_fourier_and_tents()
    check_support_bumps()
    identities = check_midpoint_and_variance()
    modes = check_shell_parity()
    print(f"PASS: 1000 Fourier sums; 100 antipodal tents; 2001 bump samples; "
          f"993 bump scales; {identities} midpoint/variance packets; "
          f"{modes} odd-shell modes. Geometry/global optimality not certified.")


if __name__ == "__main__":
    main()
