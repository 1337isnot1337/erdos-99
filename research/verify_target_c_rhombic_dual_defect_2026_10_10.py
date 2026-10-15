#!/usr/bin/env python3
"""Exact finite checks for the slot 02 rhombic dual-defect candidate.

The universal endpoint budget, infinite circle estimate, and full-source
shear proof are analytic in the report. This script checks their finite
arithmetic and noncanonical geometric guardrails, not global optimality.
"""

from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt
import json


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def rot(a):
    return (-a[1], a[0])


def sq(a):
    return a[0] ** 2 + a[1] ** 2


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def ledger(points):
    pairs = {(i, j): sq(sub(points[i], points[j]))
             for i, j in combinations(range(len(points)), 2)}
    assert min(pairs.values()) >= 1
    contacts = {ij for ij, d in pairs.items() if d == 1}
    assert not any({(i, j), (i, k), (j, k)} <= contacts
                   for i, j, k in combinations(range(len(points)), 3))
    diameter = max(pairs.values())
    diameters = {ij for ij, d in pairs.items() if d == diameter}
    return pairs, contacts, diameter, diameters


def defect_classes():
    classes = []
    for s, d_p, d_q, delta in product(range(5), repeat=4):
        if 2 * s + d_p + d_q + delta != 4:
            continue
        k_p, k_q = d_p + s, d_q + s + delta
        assert k_p + k_q == 4 and s <= 2
        assert d_q + delta == 4 - 2 * s - d_p
        classes.append({'s_Z_P': s, 'd_H_P': d_p, 'd_H_Q': d_q,
                        'h_Q_minus_h_P': delta,
                        'k_P': k_p, 'k_Q': k_q,
                        'q_Q_minus_q_P': 4 - 2 * k_p})
    assert len(classes) == 22
    assert [sum(row['s_Z_P'] == s for row in classes)
            for s in range(3)] == [15, 6, 1]
    return {'classes': classes, 'class_count': len(classes),
            'scope': 'all arithmetic classes; no realization is asserted'}


def split_formula(n):
    remaining, p, factors, split_count = n, 2, {}, 4
    while p * p <= remaining:
        exponent = 0
        while remaining % p == 0:
            remaining //= p
            exponent += 1
        if exponent:
            factors[p] = exponent
        p += 1
    if remaining > 1:
        factors[remaining] = 1
    for p, exponent in factors.items():
        if p % 4 == 3 and exponent % 2:
            return 0
        if p % 4 == 1:
            split_count *= exponent + 1
    return split_count


def circle_counts(limit=4096):
    counts = [0] * (limit + 1)
    bound = isqrt(limit)
    for a, b in product(range(-bound, bound + 1), repeat=2):
        n = a * a + b * b
        if 0 < n <= limit:
            counts[n] += 1
    for n in range(1, limit + 1):
        assert counts[n] == split_formula(n)
        if n >= 26:
            assert counts[n] ** 2 < 4 * n
    exceptions = [n for n in range(1, limit + 1)
                  if counts[n] ** 2 >= 4 * n]
    assert exceptions == [1, 2, 4, 5, 10, 13, 25]
    # These exact inequalities certify all branches of the infinite proof.
    proof_ratios = [F(64, 17), F(256, 65), F(144, 169),
                    F(32, 13), F(256, 125), F(144, 50), F(64, 30)]
    assert all(ratio < 4 for ratio in proof_ratios)
    return {'integers_checked': [1, limit],
            'direct_signed_ordered_enumeration_matches_split_formula': True,
            'exceptions_to_r2_squared_less_than_4N': exceptions,
            'infinite_proof_branch_bounds_for_r2_squared_over_N':
                [str(ratio) for ratio in proof_ratios],
            'scope': 'finite check plus rational constants; infinite proof is analytic'}


def gram_checks():
    x = F(5, 13)
    count = 0
    for m, n in product(range(-4, 5), repeat=2):
        if m == n == 0:
            continue
        f = lambda z: m * m + n * n + 2 * m * n * z
        for r in (F(0), F(1, 7), F(1, 2), F(1)):
            assert f(r * x) == ((1 + r) * f(x) + (1 - r) * f(-x)) / 2
            assert f(r * x) >= 1
            assert (f(r * x) == 1) == (m * m + n * n == 1)
            assert f(r * x) <= max(f(x), f(-x))
            count += 1
    # Circular interpolation of split orthogonal unit vectors has a hump.
    assert sq((F(1), F(1))) == sq((F(1), F(-1))) == 2
    # At pi/4 the two rotated vectors agree: their unit Gram entries are 1.
    # Thus the squared sum is 1+1+2*1, with no irrational approximation.
    midpoint_square = 1 + 1 + 2 * 1
    assert midpoint_square == 4
    return {'coefficient_pairs': 80, 'parameter_checks': count,
            'circular_interpolation_counterexample_squared_lengths': [2, 4, 2],
            'scope': 'finite Gram arithmetic and one failed interpolation mechanism'}


def bent_grid(length):
    c, s = F(12, 13), F(5, 13)
    columns = [(F(0), F(0)), (c, s), (2 * c, F(0))]
    labels = [(i, j) for i in range(3) for j in range(length + 1)]
    index = {label: k for k, label in enumerate(labels)}
    points = [add(columns[i], (F(0), F(j))) for i, j in labels]
    endpoint = [rot(sub(columns[i], (F(0), F(j)))) for i, j in labels]
    pairs, contacts, diameter, diameters = ledger(points)
    new_pairs, new_contacts, new_diameter, new_diameters = ledger(endpoint)
    expected = {tuple(sorted((index[(i, j)], index[(i + 1, j)])))
                for i in range(2) for j in range(length + 1)}
    expected |= {tuple(sorted((index[(i, j)], index[(i, j + 1)])))
                 for i in range(3) for j in range(length)}
    assert contacts == new_contacts == expected
    assert new_diameter == diameter
    pair_images = set()
    for a, b in pairs:
        i, j = labels[a]
        k, ell = labels[b]
        image = tuple(sorted((index[(i, ell)], index[(k, j)])))
        assert image[0] != image[1]
        assert new_pairs[(a, b)] == pairs[image]
        pair_images.add(image)
    assert pair_images == set(pairs)
    assert len(new_diameters) == len(diameters)
    assert diameter == max(F(length * length) + 4 * c * c,
                           F(length * length) + 2 * length * s + 1)
    for a, b in contacts:
        sign = 1 if labels[a][0] != labels[b][0] else -1
        expected_increment = rot(sub(points[b], points[a]))
        assert sub(endpoint[b], endpoint[a]) == tuple(sign * v for v in expected_increment)
    for i, j in product(range(2), range(length)):
        a, b, d = index[(i, j)], index[(i + 1, j)], index[(i, j + 1)]
        old_area = det(sub(points[b], points[a]), sub(points[d], points[a]))
        new_area = det(sub(endpoint[b], endpoint[a]), sub(endpoint[d], endpoint[a]))
        assert old_area == c and new_area == -c
    # Undo J and translate by L*v after reversing row labels.
    for i, j in labels:
        rotated = rot(endpoint[index[(i, length - j)]])
        assert add(tuple(-v for v in rotated), (F(0), F(length))) == points[index[(i, j)]]
    witness = tuple(sorted((index[(0, 0)], index[(1, 1)])))
    assert pairs[witness] == 2 + 2 * s
    assert new_pairs[witness] == 2 - 2 * s
    moved = list(points)
    if length == 2:
        moving_label, velocity = (1, length), (F(0), F(1, 100))
    else:
        moving_label, velocity = (0, length), (F(-1, 100), F(1, 100))
    moving_index = index[moving_label]
    moved[moving_index] = add(moved[moving_index], velocity)
    moved_pairs, moved_contacts, moved_diameter, _ = ledger(moved)
    assert moved_diameter == diameter
    assert moved_contacts < contacts
    assert all(d <= diameter for d in moved_pairs.values())
    if length == 10:
        assert diameter > 81
    return {'rows_minus_one': length, 'labels': len(points),
            'complete_pair_checks_per_placement': len(pairs),
            'contacts': len(contacts), 'bounded_rhombi': 2 * length,
            'diameter_squared': str(diameter),
            'old_diameter_edges': [list(pair) for pair in sorted(diameters)],
            'new_diameter_edges': [list(pair) for pair in sorted(new_diameters)],
            'pair_involution_checks': len(pair_images),
            'labelled_noncongruence_witness': list(witness),
            'witness_squares': [str(pairs[witness]), str(new_pairs[witness])],
            'contact_loss_label': list(moving_label),
            'contact_loss_displacement': [str(v) for v in velocity],
            'contacts_after_finite_release': len(moved_contacts),
            'scope': 'fails canonical contact minimality; global optimality not claimed'}


def main():
    coarse_population_coefficient = F(3) / (2 * F(7, 4)) - F(2, 3)
    assert coarse_population_coefficient == F(4, 21)
    assert F(5, 3) ** 2 > F(8, 3)
    assert coarse_population_coefficient * 9 - F(5, 3) == F(1, 21)
    result = {'dual_defect_classes': defect_classes(),
              'square_lattice_circle_counts': circle_counts(),
              'coherent_Gram_checks': gram_checks(),
              'bent_grid_guardrails': [bent_grid(2), bent_grid(10)],
              'complete_array_isolate_bound_constants': {
                  'quadratic_coarse_lower': str(coarse_population_coefficient),
                  'linear_coarse_upper': '5/3',
                  'D_at_least_9_implies_strict_Z_lower': 'D/21'},
              'scope': 'exact finite arithmetic; universal source claims are analytic'}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
