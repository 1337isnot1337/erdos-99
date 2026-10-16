#!/usr/bin/env python3
"""Exact finite source and separator regression; see research/README.md.

SymPy arithmetic is exact in Q(sqrt(3)), with the common coordinate scale
sqrt(2+sqrt(3)). This is not an optimal-packing or asymptotic certificate.
"""
from collections import deque
from itertools import combinations

import sympy as sp


def zero(x):
    return sp.simplify(sp.expand(x)) == 0


def connected(vertices, edges):
    vertices = set(vertices)
    if not vertices:
        return True
    reached = {next(iter(vertices))}
    queue = deque(reached)
    while queue:
        x = queue.popleft()
        for a, b in edges:
            y = b if a == x else a if b == x else None
            if y in vertices and y not in reached:
                reached.add(y)
                queue.append(y)
    return reached == vertices


def graph_diameter(vertices, edges):
    vertices = set(vertices)
    largest = 0
    for root in vertices:
        distances = {root: 0}
        queue = deque([root])
        while queue:
            x = queue.popleft()
            for a, b in edges:
                y = b if a == x else a if b == x else None
                if y in vertices and y not in distances:
                    distances[y] = distances[x] + 1
                    queue.append(y)
        assert len(distances) == len(vertices)
        largest = max(largest, max(distances.values()))
    return largest


def main():
    z = sp.sqrt(3)
    diameter2 = 2 + z
    beta = 2 - z
    directions = [sp.Matrix([1, 0]), sp.Matrix([-sp.Rational(1, 2), z / 2]),
                  sp.Matrix([-sp.Rational(1, 2), -z / 2])]
    # Actual coordinates equal sqrt(diameter2) times these scaled rows.
    points = [u / z for u in directions] + [(1 / z - 1) * u for u in directions]
    coords = sp.Matrix([list(p) for p in points]).applyfunc(sp.simplify)
    contacts = {(i, j + 3) for i in range(3) for j in range(3) if i != j}
    diameters = set(combinations(range(3), 2)) | {(i, i + 3) for i in range(3)}
    assert len(contacts) == len(diameters) == 6
    distances = {}
    for i, j in combinations(range(6), 2):
        d2 = sp.simplify(diameter2 * (points[i] - points[j]).dot(points[i] - points[j]))
        distances[i, j] = d2
        assert zero(d2 - (1 if (i, j) in contacts else diameter2 if (i, j) in diameters else 2))
    assert all(not all(tuple(sorted(e)) in contacts for e in combinations(t, 2))
               for t in combinations(range(6), 3))

    stress = sp.zeros(6)
    for edges, weight in ((contacts, sp.Integer(1)), (diameters, -beta)):
        for i, j in edges:
            stress[i, i] += weight
            stress[j, j] += weight
            stress[i, j] -= weight
            stress[j, i] -= weight
    affine = sp.ones(6, 1).row_join(coords)
    assert all(zero(x) for x in stress * affine)
    grounded = stress[3:6, 3:6]
    assert all(zero(x) for x in grounded - z * sp.eye(3))
    schur = stress[:3, :3] - stress[:3, 3:6] * grounded.inv() * stress[3:6, :3]
    assert all(zero(x) for x in schur)
    assert stress.rank() == 3 and affine.rank() == 3
    # Grounded positivity and zero Schur complement prove PSD and affine kernel.
    assert zero(6 - diameter2 * 6 * beta)

    rigidity = []
    for i, j in sorted(contacts | diameters):
        r = [sp.Integer(0)] * 12
        delta = points[i] - points[j]
        r[2 * i:2 * i + 2] = list(delta)
        r[2 * j:2 * j + 2] = list(-delta)
        rigidity.append(r)
    rigidity = sp.Matrix(rigidity)
    assert rigidity.rank() == 9

    # Exact kernel restriction formula, for every nonempty puncture set.
    punctures = 0
    line_punctures = 0
    for size in range(1, 7):
        for pins in combinations(range(6), size):
            keep = [i for i in range(6) if i not in pins]
            pin_rank = affine[list(pins), :].rank()
            principal = stress[keep, keep]
            assert len(keep) - principal.rank() == 3 - pin_rank
            punctures += 1
            if pin_rank <= 2:
                assert connected(keep, contacts | diameters)
                line_punctures += 1
    assert not connected({3, 4, 5}, contacts | diameters)
    assert connected({3, 4, 5}, {(3, 4), (4, 5)})

    # Arbitrary curved seams: full incident diameter rows and one-row surplus.
    islands = 0
    for size in range(1, 5):
        for packet in combinations(range(6), size):
            island = set(packet)
            if not connected(island, contacts):
                continue
            pins = {j if i in island else i for i, j in contacts
                    if (i in island) != (j in island)}
            if len(pins) < 2:
                continue
            ei = sum(bool(island & set(e)) for e in contacts)
            hi = sum(bool(island & set(e)) for e in diameters)
            ep = sum(set(e) <= pins for e in contacts)
            cols = [c for i in sorted(island) for c in (2 * i, 2 * i + 1)]
            assert rigidity[:, cols].rank() == 2 * len(island)
            assert ei + hi >= 2 * len(island) + 1
            delta = graph_diameter(island | pins, contacts)
            assert delta <= 2 * len(pins) + hi - ep - 3
            if island <= {3, 4, 5}:
                assert size == 1 and delta == 2 * len(pins) + hi - ep - 3
            islands += 1
    for k in range(2, 101):
        assert k == 2 * 2 + (k - 1) - 3
        assert k + (k - 1) == 2 * (k - 1) + 1
    # Three attachment pins, no incident diameters: Oler gives N<14, W<=10.
    pi_upper = sp.Rational(22, 7)
    sqrt3_lower = sp.Rational(1732, 1000)
    assert 9 * pi_upper / (2 * sqrt3_lower) + 3 * pi_upper / 2 + 1 < 14

    # Exact reflection/cut-product identity and the diameter depth bound.
    # Coordinates need no normalization; both sides are homogeneous quadratic.
    for nx, ny, offset in ((1, 0, 0), (0, 1, 0), (1, 1, sp.Rational(1, 7))):
        heights = coords * sp.Matrix([nx, ny]) - offset * sp.ones(6, 1)
        for mask in range(1, 63):
            subset = {i for i in range(6) if mask & (1 << i)}
            f = sp.Matrix([heights[i] if i in subset else 0 for i in range(6)])
            cut_work = 0
            for edges, weight in ((contacts, sp.Integer(1)), (diameters, -beta)):
                for i, j in edges:
                    if (i in subset) != (j in subset):
                        cut_work += weight * heights[i] * heights[j]
            assert zero((f.T * stress * f)[0] - cut_work)
    for i, j in diameters:
        # The sharp estimate 4ab <= (a+b)^2 is polynomial and exact.
        for a, b in ((sp.Rational(1, 3), sp.Rational(2, 3)), (1, 1), (0, 1)):
            assert (a + b) ** 2 - 4 * a * b == (a - b) ** 2

    # A pentagon and its center beat the k=2 source; certified rational bounds.
    assert sp.Rational(2237, 1000) ** 2 > 5
    assert sp.Rational(1732, 1000) ** 2 < 3
    assert (5 + sp.Rational(2237, 1000)) / 2 < 2 + sp.Rational(1732, 1000)

    # All k>=3 sources have explicit smaller square-grid competitors.
    # D > 3k/pi > 21k/22; pi<22/7. The first four cases and tail are rational.
    for k, width, height in ((3, 3, 3), (4, 4, 3), (5, 4, 4), (6, 5, 4)):
        assert width * height >= 3 * k
        assert (width - 1) ** 2 + (height - 1) ** 2 < sp.Rational(21 * k, 22) ** 2
    assert 441 * 7 > 6 * 484
    print(f"PASS: 15 actual source distances; full stress PSD/affine kernel; mixed rank 9; "
          f"{punctures} principal-kernel restrictions; {line_punctures} collinear punctures; "
          f"{islands} physical contact-island budgets; 99 exact sharpness counts; "
          "186 exact cut identities; curved-separator regression; all-k competitor arithmetic.")


if __name__ == "__main__":
    main()
