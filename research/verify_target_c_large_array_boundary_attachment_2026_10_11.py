#!/usr/bin/env python3
"""Exact finite ingredients of the large-array source attachment candidate.

These rational/algebraic fixtures do not establish global optimality, the
ambient circumradius theorem, compactness, or a numerical asymptotic cutoff.
"""

from fractions import Fraction as F
from itertools import combinations, product
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as alg


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def scale(a, t):
    return a[0] * t, a[1] * t


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def norm(a):
    return dot(a, a)


def rot(a):
    return -a[1], a[0]


def circle(t):
    return (1 - t*t)/(1 + t*t), 2*t/(1 + t*t)


def encode(a):
    return [str(v) for v in a]


def lens_identities():
    radius = F(1, 2)
    fixtures = []
    point_checks = 0
    for parameter in (F(1, 5), F(1, 3), F(1, 2), F(2, 3)):
        cosine, sine = circle(parameter)
        height = 2 * radius * sine
        b = F(0), height
        extreme = radius * cosine
        intersections = [(extreme, -height/2), (-extreme, -height/2)]
        assert 0 < height < 2*radius and extreme > 0
        for p in intersections:
            assert norm(p) == radius**2 == norm(add(p, b))
            assert p[0]**2 == radius**2 - height**2/4
        samples = intersections + [(F(0), -height/2)]
        for i in range(-30, 31):
            p = scale(circle(F(i, 10)), radius)
            for w in (p, sub(p, b)):
                if norm(w) <= radius**2 and norm(add(w, b)) <= radius**2:
                    samples.append(w)
        for w in samples:
            x, y = w
            centered_y = y + height/2
            identity = x*x + centered_y**2 + height**2/4 + height*abs(centered_y)
            assert identity == max(norm(w), norm(add(w, b)))
            assert identity <= radius**2
            assert x*x <= extreme**2
            if x*x == extreme**2:
                assert w in intersections
            point_checks += 1
        fixtures.append({'circle_radius': str(radius),
                         'center_separation': str(height),
                         'perpendicular_extremes': [encode(p) for p in intersections],
                         'checked_lens_points': len(samples)})
    return {'fixtures': fixtures, 'exact_lens_point_identity_checks': point_checks,
            'scope': 'finite identities and extremal witnesses, not all continuous paths'}


def circle_chord_identity():
    radius = F(1, 2)
    points = [scale(circle(F(i, 10)), radius) for i in range(-10, 11)]
    identity_checks = 0
    tangent_checks = 0
    for p, q in combinations(points, 2):
        h = sub(q, p)
        assert h != (0, 0)
        assert 2*dot(p, h) + norm(h) == 0
        assert 2*dot(q, h) - norm(h) == 0
        identity_checks += 2
    for p in points:
        tangent = rot(p)
        assert dot(p, tangent) == 0 and norm(tangent) == radius**2
        assert det(tangent, scale(tangent, -1)) == 0
        tangent_checks += 1
    return {'oriented_chord_identities': identity_checks,
            'exact_tangent_identities': tangent_checks,
            'scope': 'the endpoint tangent limit is proved analytically in the report'}


def regular_stars():
    us = [circle(t) for t in (F(-1, 8), F(-1, 16), F(0), F(1, 16), F(1, 8))]
    vs = [rot(circle(t)) for t in (F(-1, 10), F(-1, 20), F(0), F(1, 20), F(1, 10))]
    checks, zero_turns, nonzero_turns = 0, 0, 0
    for old, new, first_v, last_v in product(us, us, vs, vs):
        for u, v in product((old, new), (first_v, last_v)):
            assert norm(u) == norm(v) == 1
            assert abs(dot(u, v)) < F(1, 2)
            assert det(u, v) > 0 and 4*det(u, v)**2 > 3
        minus_old = scale(old, -1)
        minus_v = scale(last_v, -1)
        bottom = [new, first_v, minus_old]
        top = [new, minus_old, minus_v]
        bottom_spans = all(det(bottom[i], bottom[(i+1) % 3]) > 0 for i in range(3))
        top_spans = all(det(top[i], top[(i+1) % 3]) > 0 for i in range(3))
        turning = det(old, new)
        assert bottom_spans == (turning < 0)
        assert top_spans == (turning > 0)
        if turning:
            assert bottom_spans != top_spans
            nonzero_turns += 1
        else:
            assert old == new and add(old, minus_old) == (0, 0)
            assert not bottom_spans and not top_spans
            zero_turns += 1
        checks += 1
    assert (checks, nonzero_turns, zero_turns) == (625, 500, 125)
    return {'opposite_regular_star_fixtures': checks,
            'nonzero_turn_pairs_with_exactly_one_surrounding_star': nonzero_turns,
            'zero_turn_pairs_with_a_midpoint_exposure_obstruction': zero_turns,
            'scope': 'contact minimality supplies the loaded conclusion; not modeled'}


def array_monotonicity():
    us = [circle(t) for t in (F(-1, 8), F(0), F(1, 8))]
    vs = [rot(circle(t)) for t in (F(-1, 10), F(0), F(1, 10))]
    fixtures, pair_checks, determinant_checks = 0, 0, 0
    for choices in product(range(3), repeat=4):
        u = [us[i] for i in choices[:2]]
        v = [vs[i] for i in choices[2:]]
        xs, ys = [(F(0), F(0))], [(F(0), F(0))]
        for w in u:
            xs.append(add(xs[-1], w))
        for w in v:
            ys.append(add(ys[-1], w))
        labels = list(product(range(3), repeat=2))
        points = [add(xs[i], ys[j]) for i, j in labels]
        for i, j in combinations(range(9), 2):
            square = norm(sub(points[i], points[j]))
            expected_contact = sum(abs(labels[i][k] - labels[j][k]) for k in (0, 1)) == 1
            assert square == 1 if expected_contact else square > 1
            pair_checks += 1
        for i, j in combinations(range(3), 2):
            m = j - i
            d1 = det(sub(xs[j], xs[i]), ys[-1])
            d2 = det(xs[-1], sub(ys[j], ys[i]))
            for value in (d1, d2):
                assert value > 0 and 4*value**2 > 3*(2*m)**2
                determinant_checks += 1
        fixtures += 1
    return {'complete_actual_unit_array_fixtures': fixtures,
            'full_lower_pair_checks': pair_checks,
            'transverse_determinant_checks': determinant_checks,
            'scope': 'finite bent arrays; globality and circumradius roundness not modeled'}


def aspect_constant():
    root = alg.Q(F(0), F(1))
    sine = root * F(1, 2)
    kappa = 7 + 4*root
    assert ((1 - sine)*kappa - (1 + sine)) == alg.Q()
    assert (14 - kappa).sign() > 0
    assert (kappa - 1).sign() > 0
    return {'kappa': '7+4sqrt(3)',
            'exact_identity': '(1-sqrt(3)/2)*kappa=1+sqrt(3)/2',
            'integer_ceiling': 14,
            'canonical_aspect_ratio_scope': 'all actual diameter endpoints lie in the array'}


def main():
    certificate = {
        'classification': 'finite exact ingredient certificate for an unreviewed candidate',
        'report': 'docs/reports/target_c_large_array_boundary_attachment_slot02_2026-10-11.md',
        'lens': lens_identities(),
        'circle_tangency': circle_chord_identity(),
        'regular_opposite_stars': regular_stars(),
        'array_transverse_monotonicity': array_monotonicity(),
        'diameter_aspect_constant': aspect_constant(),
        'not_certified': ['global minimum diameter', 'source circumradius theorem',
                          'uniform compactness contradiction', 'numerical D_0 or epsilon_delta',
                          'complete-array extraction', 'full-source finite endpoint', 'Level I'],
    }
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
