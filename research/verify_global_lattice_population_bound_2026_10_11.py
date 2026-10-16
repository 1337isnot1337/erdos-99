#!/usr/bin/env python3
"""Finite exact checks for the uniform lattice-diameter population candidate.

The proof is analytic. These cases exercise the difference-body normalization,
boundary lattice multiplicities, cubic side penalty and noncircular hulls. No
finite example certifies global optimality or the missing crystallization step.
"""

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from fractions import Fraction as F
from math import gcd, isqrt

from verify_global_stress_density_regression_2026_10_11 import PI


SCALE = 10**40


def sqrt_bounds(value):
    assert value >= 0
    root = isqrt((value*SCALE*SCALE).__floor__())
    return F(root, SCALE), F(root+1, SCALE)


def integer_root(value, order):
    lo, hi = 0, 1 << ((value.bit_length()+order-1)//order)
    while lo+1 < hi:
        mid = (lo+hi)//2
        if mid**order <= value:
            lo = mid
        else:
            hi = mid
    return lo


def fifth_root_lower(value):
    root = integer_root((value*SCALE**5).__floor__(), 5)
    assert root**5 <= value*SCALE**5 < (root+1)**5
    return F(root, SCALE)


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def hull(points):
    points = sorted(set(points))
    chains = []
    for ordering in (points, list(reversed(points))):
        chain = []
        for p in ordering:
            while len(chain) >= 2 and cross(chain[-2], chain[-1], p) <= 0:
                chain.pop()
            chain.append(p)
        chains.append(chain[:-1])
    return chains[0]+chains[1]


def polygon_area(poly):
    return F(sum(p[0]*q[1]-p[1]*q[0]
                 for p, q in zip(poly, poly[1:]+poly[:1])), 2)


def edges(poly):
    return [(q[0]-p[0], q[1]-p[1])
            for p, q in zip(poly, poly[1:]+poly[:1])]


def squared(v, metric):
    u, w = v
    g11, g12, g22 = metric
    return g11*u*u+2*g12*u*w+g22*w*w


def primitive(edge):
    multiple = gcd(abs(edge[0]), abs(edge[1]))
    return (edge[0]//multiple, edge[1]//multiple), multiple


def check_shape(name, points, expected_population, metric):
    g11, g12, g22 = metric
    # These conditions prove the metric is unit-separated on the whole lattice:
    # q(u,v)>= (u^2+v^2)/2, with the norm-one integer vectors checked by g11,g22.
    assert g11 >= 1 and g22 >= 1
    assert (g11-F(1, 2))*(g22-F(1, 2)) >= g12*g12
    poly = hull(points)
    assert len(poly) >= 3
    area = polygon_area(poly)
    boundary = sum(primitive(e)[1] for e in edges(poly))
    population = area+F(boundary, 2)+1
    assert population.denominator == 1 and population == expected_population

    differences = {(p[0]-q[0], p[1]-q[1]) for p in poly for q in poly}
    diameter2 = max(squared(v, metric) for v in differences)
    difference_hull = hull(differences)
    # difference_hull is 2L, not L; both scale factors are explicit.
    assert polygon_area(difference_hull) >= 4*area
    assert all(squared(v, metric) <= diameter2 for v in difference_hull)
    difference_sides = {primitive(e)[0]: squared(e, metric)
                        for e in edges(difference_hull)}
    for e in edges(poly):
        direction, _ = primitive(e)
        assert difference_sides[direction] >= squared(e, metric)

    covolume = sqrt_bounds(g11*g22-g12*g12)
    deficit_lower = PI.lo*diameter2/4-area*covolume[1]
    assert deficit_lower > 0
    for e in edges(poly):
        length2 = squared(e, metric)
        # Exact positive squaring of ell^3 <= 48 D delta, using a lower
        # enclosure for delta. This is stronger than the desired finite check.
        assert length2**3 <= 48**2*diameter2*deficit_lower**2

    sqrt3 = sqrt_bounds(F(3))
    density_lower = PI.lo/(2*sqrt3[1])
    remainder_lower = fifth_root_lower(diameter2**2)
    assert population <= density_lower*diameter2+86*remainder_lower+1
    if diameter2 >= g11*g22-g12*g12:
        # Covolume-sensitive refinement, valid when D>=V. Use lower
        # bounds for both positive terms so the exact check is stronger.
        leading = PI.lo*diameter2/(4*covolume[1])
        remainder = fifth_root_lower(covolume[0]*diameter2**2)
        assert population <= leading+86*remainder+1
    print(f"{name}: source labels={population}, hull vertices={len(poly)}, "
          f"boundary lattice points={boundary}; all exact checks passed")
    return len(poly), int(population)


def check_periodic(name, metric, phases, radius):
    g11, g12, g22 = metric
    q = len(phases)
    assert q >= 1 and type(radius) is int and radius >= 1
    assert len(set(phases)) == q
    assert all(0 <= c < 1 for phase in phases for c in phase)
    assert g11 >= 1 and g22 >= 1
    assert (g11-F(1, 2))*(g22-F(1, 2)) >= g12*g12
    # Q(v)>=|v|^2/2. A lattice shift omitted below has one coordinate
    # of absolute value >=3; phase differences are strictly between -1
    # and 1, so its squared metric distance is strictly greater than 2.
    cross_checks = 0
    unit_degrees = [0]*q
    for i, phase in enumerate(phases):
        for j, other in enumerate(phases):
            for u in range(-2, 3):
                for v in range(-2, 3):
                    if i == j and u == v == 0:
                        continue
                    difference = (u+phase[0]-other[0], v+phase[1]-other[1])
                    distance2 = squared(difference, metric)
                    assert distance2 >= 1, ('full-period separation failure', i, j, u, v, distance2)
                    unit_degrees[i] += distance2 == 1
                    cross_checks += 1
    if name == "nonlattice two-site motif":
        assert unit_degrees == [1, 1]  # Infinite contact graph consists of dimers.
    volume2 = g11*g22-g12*g12
    assert volume2 >= F(3*q*q, 4)
    center = (F(1, 3), F(2, 5))
    bound = 2*radius+2
    all_points = []
    sides = 0
    for i, phase in enumerate(phases):
        indices = [(u, v) for u in range(-bound, bound+1)
                   for v in range(-bound, bound+1)
                   if squared((u+phase[0]-center[0], v+phase[1]-center[1]), metric)
                   <= radius**2]
        count_sides, count = check_shape(f"{name} coset {i+1}", indices,
                                        len(indices), metric)
        sides += count_sides
        assert count == len(indices)
        all_points.extend((u+phase[0], v+phase[1]) for u, v in indices)
    assert len(set(all_points)) == len(all_points)
    poly = hull(all_points)
    diameter2 = max(squared((p[0]-r[0], p[1]-r[1]), metric)
                    for p in poly for r in poly)
    assert diameter2 >= (16*q)**2
    sqrt3 = sqrt_bounds(F(3))
    lower_bound = (PI.lo*diameter2/(2*sqrt3[1])
                   +114*fifth_root_lower(q**6*diameter2**2)+q)
    assert len(all_points) <= lower_bound
    if volume2 > 16*q*q:
        assert len(all_points) < diameter2/2
    print(f"{name}: q={q}, labels={len(all_points)}, "
          f"full-period separation checks={cross_checks}; motif bound passed")
    return len(all_points), sides, cross_checks


def main():
    metrics = (
        ("square", (F(1), F(0), F(1))),
        ("triangular", (F(1), F(1, 2), F(1))),
        ("oblique", (F(1), F(3, 7), F(1))),
        ("rectangular", (F(1), F(0), F(9, 4))),
    )
    sides = labels = cases = 0
    for name, metric in metrics:
        for radius in (8, 16, 32):
            # An off-center disk crop tests phase without changing lattice coordinates.
            center = (F(1, 3), F(2, 5))
            bound = 2*radius+2
            points = [(i, j) for i in range(-bound, bound+1)
                      for j in range(-bound, bound+1)
                      if squared((i-center[0], j-center[1]), metric) <= radius**2]
            s, n = check_shape(f"{name} R={radius}", points, len(points), metric)
            sides += s
            labels += n
            cases += 1
        width, height = 97, 3
        poly = [(0, 0), (width, 0), (width, height), (0, height)]
        s, n = check_shape(f"{name} long rectangle", poly,
                           (width+1)*(height+1), metric)
        sides += s
        labels += n
        cases += 1
    print(f"PASS: {cases} exact crops/hulls, {sides} supporting-side checks, "
          f"{labels} lattice labels; Pick counts and difference-body factors verified.")
    # The first pattern has horizontal unit pairs, no unit triangles, and
    # nonuniform alternating horizontal gaps. The whole periodic packing,
    # rather than merely each coset, is certified separated above.
    periodic_cases = (
        ("nonlattice two-site motif",
         (F(53, 50), F(-7, 200), F(257, 80)),
         ((F(0), F(0)), (F(20, 41), F(20, 41))), 20),
        ("three-site triangular motif", (F(4), F(2), F(4)),
         ((F(0), F(0)), (F(1, 2), F(0)), (F(0), F(1, 2))), 28),
        ("four-site nonlattice motif", (F(9), F(0), F(9)),
         ((F(0), F(0)), (F(1, 3), F(0)), (F(0), F(1, 3)),
          (F(7, 15), F(7, 15))), 36),
        ("sparse four-site motif", (F(100), F(0), F(100)),
         ((F(0), F(0)), (F(1, 10), F(0)), (F(0), F(1, 10)),
          (F(7, 50), F(7, 50))), 36),
    )
    assert 4*86**5 < 114**5
    motif_labels = motif_sides = motif_checks = 0
    for args in periodic_cases:
        n, s, c = check_periodic(*args)
        motif_labels += n
        motif_sides += s
        motif_checks += c
    print(f"PASS: {len(periodic_cases)} full periodic patterns, {motif_labels} labels, "
          f"{motif_sides} coset-hull sides, {motif_checks} full-period separation checks.")
    # Two individually separated cosets need not have a separated full union.
    try:
        check_periodic('invalid close cosets', (F(4), F(0), F(4)),
                       ((F(0), F(0)), (F(1, 100), F(0))), 20)
    except AssertionError as exc:
        assert exc.args[0][0] == 'full-period separation failure'
    else:
        raise AssertionError('invalid cross-coset packing accepted')
    print('PASS: individually separated but cross-coset-invalid periodic union rejected')
    print("Scope: finite regression checks. The uniform O(D^(4/5)) theorem is "
          "proved analytically; the minimizer defect consequence remains "
          "conditional on the unreviewed linear reserve. No Level I certificate.")


if __name__ == "__main__":
    main()
