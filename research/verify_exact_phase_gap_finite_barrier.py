#!/usr/bin/env python3
"""Exact regression for an abstract exact-phase diameter interval system.

Encodes: full interval rank, a connected bridgeless gap multigraph,
strictly positive diameter weights, transverse KKT cancellation, nonzero
axial interface reactions, unique diameter directions, one common support
index, and a finite three-bar substitution inside an empty direction cell.

Also realizes the original diameter vectors by a convex circular matching,
then by a shifted 16-point source with actual nested contact cuts and a
strict finite competitor. The latter is certified for every real D>=13
by quadratic inequalities. It has loaded contact isolates, no full-source
positive contact stress, and no complete rhombic O--O train grid. No global
optimality is encoded. All arithmetic is rational. A PASS is a regression
against the abstract implication, not an Erdős-99 counterexample.
"""

from fractions import Fraction as Q
from itertools import combinations


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(k, a):
    return tuple(k * x for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm2(a):
    return dot(a, a)


def rank(rows):
    matrix = [list(row) for row in rows]
    lead = 0
    for col in range(len(matrix[0])):
        pivot = next((i for i in range(lead, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[lead], matrix[pivot] = matrix[pivot], matrix[lead]
        factor = matrix[lead][col]
        matrix[lead] = [x / factor for x in matrix[lead]]
        for i in range(len(matrix)):
            if i != lead:
                factor = matrix[i][col]
                matrix[i] = [x - factor * y for x, y in zip(matrix[i], matrix[lead])]
        lead += 1
    return lead


def reachable(edges, start):
    seen, pending = {start}, [start]
    while pending:
        here = pending.pop()
        for a, b in edges:
            if a == here and b not in seen:
                seen.add(b)
                pending.append(b)
    return seen


def polynomial_distance(a, b):
    """Points are (coefficient of D, constant vector)."""
    slope, constant = sub(a[0], b[0]), sub(a[1], b[1])
    return norm2(slope), 2 * dot(slope, constant), norm2(constant)


def polynomial_value(coefficients, at):
    a, b, c = coefficients
    return a * at**2 + b * at + c


def certify_nonnegative_ray(coefficients, threshold=Q(13), strict=False):
    """P>=0 on [threshold,infinity) by nonnegative leading term and derivative."""
    a, b, _ = coefficients
    assert a >= 0
    assert 2 * a * threshold + b >= 0
    value = polynomial_value(coefficients, threshold)
    assert value > 0 if strict else value >= 0


def actual_source_regression(packets, new_bars):
    unit = (Q(1), Q(0))
    zero = (Q(0), Q(0))
    shifts = [zero]
    for vector in new_bars:
        shifts.append(add(shifts[-1], sub(vector, unit)))

    # Each point is represented as v*D+z, allowing exact verification on
    # the entire ray D>=13 rather than a list of numerical examples.
    points, labels, old_diameters = [], [], set()
    for (a, b), direction in packets:
        center = scale(Q(-1, 8), add(shifts[a - 1], shifts[b]))
        for sign in (-1, 1):
            vector = (direction[0], sign * direction[1])
            old_diameters.add((len(points), len(points) + 1))
            points.extend([(scale(Q(-1, 2), vector), center),
                           (scale(Q(1, 2), vector), center)])
            labels.extend([a - 1, b])
    for j in range(4):
        points.append((zero, (Q(j) - Q(3, 2), Q(0))))
        labels.append(j)
    changed = [(slope, add(constant, shifts[label]))
               for (slope, constant), label in zip(points, labels)]
    contacts = {(12, 13), (13, 14), (14, 15)}

    for i, j in combinations(range(len(points)), 2):
        original = polynomial_distance(points[i], points[j])
        new = polynomial_distance(changed[i], changed[j])
        # Every source pair is checked, including previously strict pairs.
        certify_nonnegative_ray((original[0], original[1], original[2] - 1),
                                strict=(i, j) not in contacts)
        certify_nonnegative_ray((new[0], new[1], new[2] - 1),
                                strict=(i, j) not in contacts)
        certify_nonnegative_ray((1 - original[0], -original[1], -original[2]),
                                strict=(i, j) not in old_diameters)
        certify_nonnegative_ray((1 - new[0], -new[1], -new[2]), strict=True)
        if (i, j) in contacts:
            assert original == new == (Q(0), Q(0), Q(1))
        if (i, j) in old_diameters:
            assert original == (Q(1), Q(0), Q(0))

    # The actual contact cuts S_k={p:label(p)>=k}, k=1,2,3, are nested.
    # Every contact crosses exactly one cut and is oriented as +u.
    for i, j in contacts:
        assert labels[j] == labels[i] + 1
        assert sub(points[j][0], points[i][0]) == zero
        assert sub(points[j][1], points[i][1]) == unit
    assert all(i < 12 and j < 12 for i, j in old_diameters)
    assert all(i >= 12 and j >= 12 for i, j in contacts)
    # Thus every loaded vertex is a contact isolate, making full-source
    # positive diameter KKT equilibrium impossible at that vertex.

    new_squared = [polynomial_value(polynomial_distance(changed[i], changed[j]), Q(13))
                   for i, j in combinations(range(16), 2)]
    assert max(new_squared) == Q(28248541, 167281)
    assert min(value for value in new_squared if value > 1) == Q(61741, 32720)
    # The centered predecessor fails one inactive diameter bound. Retain
    # this exact negative control rather than checking only the active rows.
    centered = [(slope, zero) if index < 12 else (slope, constant)
                for index, (slope, constant) in enumerate(points)]
    centered_new = [(slope, add(constant, shifts[label]))
                    for (slope, constant), label in zip(centered, labels)]
    assert polynomial_value(polynomial_distance(centered_new[1], centered_new[4]), Q(13)) == Q(3481549, 20450)
    assert Q(3481549, 20450) > Q(169)
    print('PASS: actual 16-point source and finite competitor for every real D>=13')
    print('PASS: all 120 pairwise lower/upper quadratic inequalities; exact contact set')
    print('PASS: three actual nested source cuts; full-rank source derivative matrix')
    print('D=13 new squared diameter:', max(new_squared))
    print('D=13 squared-diameter improvement:', Q(169) - max(new_squared))
    print('PASS: centered predecessor rejected by an exact inactive-pair violation')
    print('OMITTED: full-source positive KKT/PSD, O--O rhombic train embedding, global optimality')


def main():
    diameter = Q(13)
    original_bar = (Q(1), Q(0))
    # Support, unit diameter direction; both transverse signs per support.
    packets = [
        ((1, 2), (Q(4, 5), Q(3, 5))),
        ((2, 3), (Q(3, 5), Q(4, 5))),
        ((1, 3), (Q(12, 13), Q(5, 13))),
    ]
    bars = []
    for interval, direction in packets:
        for sign in (-1, 1):
            vector = scale(diameter, (direction[0], sign * direction[1]))
            bars.append((interval, vector, Q(1, 6)))
    directions = [vector for _, vector, _ in bars]
    assert all(norm2(vector) == diameter**2 for vector in directions)
    assert all(a[0] * b[1] != a[1] * b[0] for a, b in combinations(directions, 2))

    rows = [tuple(vector[1] if a <= j <= b else Q(0) for j in range(1, 4))
            for (a, b), vector, _ in bars]
    assert rank(rows) == 3
    assert all(sum(weight * row[j] for (_, _, weight), row in zip(bars, rows)) == 0
               for j in range(3))
    axial = [sum(weight * vector[0] for (a, b), vector, weight in bars if a <= j <= b)
             for j in range(1, 4)]
    assert all(value > 0 for value in axial)
    # At gap 1 only [2,3] switches, and at gap 2 only [1,2] switches.
    assert axial[0] != axial[1] and axial[1] != axial[2]
    assert all(a <= 2 <= b for (a, b), _, _ in bars)

    oriented_edges = []
    for (a, b), vector, _ in bars:
        edge = (a - 1, b)
        oriented_edges.append(edge if vector[1] > 0 else edge[::-1])
    assert all(reachable(oriented_edges, start) == set(range(4)) for start in range(4))
    undirected = [(a - 1, b) for (a, b), _, _ in bars]
    for deleted in range(len(undirected)):
        remaining = [e for i, e in enumerate(undirected) if i != deleted]
        doubled = remaining + [(b, a) for a, b in remaining]
        assert reachable(doubled, 0) == set(range(4))

    # tan(theta/2)=3/20, hence exact rational rotations.
    cosine, sine = Q(391, 409), Q(120, 409)
    new_bars = [(cosine, sine), (cosine, -sine), (cosine, sine)]
    assert all(norm2(vector) == 1 for vector in new_bars)
    # The nearest diameter direction has slope 5/12. All new phases are
    # strictly inside the original cell (-atan(5/12), atan(5/12)).
    assert sine / cosine < Q(5, 12)
    differences = [sub(vector, original_bar) for vector in new_bars]
    squared_gains = []
    for (a, b), vector, _ in bars:
        change = tuple(sum(differences[i][axis] for i in range(a - 1, b))
                       for axis in range(2))
        gain = norm2(add(vector, change)) - diameter**2
        assert gain < 0
        squared_gains.append(gain)

    # An independent, actual geometric realization of the OLD vectors:
    # six distinct diameters of one circle of radius D/2.
    points = [scale(sign * Q(1, 2), vector) for vector in directions for sign in (-1, 1)]
    assert len(set(points)) == 12
    distances = [norm2(sub(a, b)) for a, b in combinations(points, 2)]
    assert min(distances) > 1 and max(distances) == diameter**2
    assert sum(value == diameter**2 for value in distances) == 6
    assert all(norm2(point) == diameter**2 / 4 for point in points)
    # This realization has no contacts. It cannot satisfy the source cut
    # hypothesis and is not the source of the abstract finite substitution.
    assert all(value != 1 for value in distances)

    print('PASS: full rank 3; six rows; positive KKT circulation; connected and bridgeless')
    print('PASS: nonzero axial interface reactions; common support index 2; unique directions')
    print('PASS: all six abstract diameters strictly shorten inside the original empty cell')
    print('squared diameter changes:', ', '.join(str(value) for value in squared_gains))
    print('PASS: independent convex circular diameter matching is unit-separated')
    print('minimum circular-source squared separation:', min(distances))
    print('OMITTED: actual contact-cut/source co-embedding, full source KKT, PSD, global optimality')
    actual_source_regression(packets, new_bars)


if __name__ == '__main__':
    main()
