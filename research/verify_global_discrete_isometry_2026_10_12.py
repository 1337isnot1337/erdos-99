#!/usr/bin/env python3
"""Exact full-source discrete-isometry tests; no global optimality oracle.

All distances and translation-offset cells use rational/real-algebraic
arithmetic. Successful assignments are independently checked on every pair.
See the associated report and research/README.md for the precise scope.
"""
from __future__ import annotations

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from functools import cmp_to_key
from itertools import combinations, product
import json

import sympy as S


def sign(x):
    x = S.simplify(x)
    if x == 0:
        return 0
    if x.is_positive is True:
        return 1
    if x.is_negative is True:
        return -1
    result = S.sign(x)
    if result in (S.Integer(-1), S.Integer(0), S.Integer(1)):
        return int(result)
    raise ArithmeticError(f"Undecided exact sign: {x}")


def distance2(p, q):
    return S.expand(sum((a - b) ** 2 for a, b in zip(p, q)))


def rational_points(rows):
    return [tuple(S.Rational(x) for x in row) for row in rows]


def diameter2(points):
    assert len(points) >= 2 and all(len(p) == 2 for p in points)
    values = [distance2(points[i], points[j])
              for i, j in combinations(range(len(points)), 2)]
    assert all(sign(x - 1) >= 0 for x in values)
    return max(values, key=cmp_to_key(lambda x, y: sign(x - y)))


def scc(graph):
    """Kosaraju, with iterative DFS to avoid source-size recursion limits."""
    reverse = [[] for _ in graph]
    for i, neighbours in enumerate(graph):
        for j in neighbours:
            reverse[j].append(i)
    seen, order = set(), []
    for start in range(len(graph)):
        if start in seen:
            continue
        seen.add(start)
        stack = [(start, iter(graph[start]))]
        while stack:
            v, neighbours = stack[-1]
            w = next(neighbours, None)
            if w is None:
                order.append(v)
                stack.pop()
            elif w not in seen:
                seen.add(w)
                stack.append((w, iter(graph[w])))
    components = [-1] * len(graph)
    number = 0
    for start in reversed(order):
        if components[start] >= 0:
            continue
        components[start] = number
        stack = [start]
        while stack:
            v = stack.pop()
            for w in reverse[v]:
                if components[w] < 0:
                    components[w] = number
                    stack.append(w)
        number += 1
    return components


def forbidden_graph(n, forbidden):
    graph = [[] for _ in range(2 * n)]
    for i, a, j, b in forbidden:
        graph[2 * i + a].append(2 * j + 1 - b)
        graph[2 * j + b].append(2 * i + 1 - a)
    return graph


def solve_binary(n, forbidden):
    comp = scc(forbidden_graph(n, forbidden))
    if any(comp[2 * i] == comp[2 * i + 1] for i in range(n)):
        return None
    state = [int(comp[2 * i] < comp[2 * i + 1]) for i in range(n)]
    assert all((state[i], state[j]) != (a, b)
               for i, a, j, b in forbidden)
    return state


def constraints(points, images, bound, strict=True):
    n = len(points)
    assert len(images) == n
    assert all(len(p) == 2 for p in [*points, *images])
    forbidden = []
    choices = (points, images)
    for i, j in combinations(range(n), 2):
        assert sign(distance2(points[i], points[j])
                    - distance2(images[i], images[j])) == 0
        for a, b in product(range(2), repeat=2):
            d = distance2(choices[a][i], choices[b][j])
            upper = sign(d - bound)
            if sign(d - 1) < 0 or upper > 0 or (strict and upper == 0):
                forbidden.append((i, a, j, b))
    return forbidden


def verify_endpoint(points, images, state, bound):
    assert len(points) == len(images) == len(state) >= 2
    assert all(type(bit) is int and bit in (0, 1) for bit in state)
    assert all(len(p) == 2 for p in [*points, *images])
    endpoint = [images[i] if bit else points[i]
                for i, bit in enumerate(state)]
    values = [distance2(endpoint[i], endpoint[j])
              for i, j in combinations(range(len(points)), 2)]
    assert all(sign(d - 1) >= 0 and sign(bound - d) > 0 for d in values)
    return max(values, key=cmp_to_key(lambda x, y: sign(x - y)))


def rational_between(lo, hi):
    denominator = 1
    while True:
        numerator = int(S.floor(lo * denominator)) + 1
        candidate = S.Rational(numerator, denominator)
        if sign(hi - candidate) > 0:
            return candidate
        denominator *= 2


def translation_cells(points, vector, bound):
    """Every nonnegative root and every intervening open interval, exactly."""
    assert all(x.is_Rational for p in points for x in p)
    assert all(x.is_Rational for x in vector)
    assert any(x != 0 for x in vector)
    t = S.Symbol("t", real=True)
    norm = sum(x * x for x in vector)
    roots = [S.Integer(0)]
    for i, j in combinations(range(len(points)), 2):
        d = distance2(points[i], points[j])
        projection = sum((points[i][k] - points[j][k]) * vector[k]
                         for k in range(2))
        for direction, threshold in product((-1, 1), (S.Integer(1), bound)):
            polynomial = norm * t * t + 2 * direction * projection * t + d - threshold
            for root in S.solve(polynomial, t):
                if root.is_real is True and sign(root) >= 0:
                    roots.append(root)
    roots.sort(key=cmp_to_key(lambda x, y: sign(x - y)))
    unique = []
    for root in roots:
        if not unique or sign(root - unique[-1]) != 0:
            unique.append(root)
    samples = []
    for i, root in enumerate(unique):
        samples.append(root)
        samples.append(rational_between(root, unique[i + 1])
                       if i + 1 < len(unique) else S.ceiling(root) + 1)
    return samples


def sweep(points, vector, brute=False):
    bound = diameter2(points)
    cells = translation_cells(points, vector, bound)
    witness = None
    for t in cells:
        images = [tuple(p[k] + t * vector[k] for k in range(2)) for p in points]
        forbidden = constraints(points, images, bound)
        state = solve_binary(len(points), forbidden)
        if brute:
            possible = next((bits for bits in product(range(2), repeat=len(points))
                             if all((bits[i], bits[j]) != (a, b)
                                    for i, a, j, b in forbidden)), None)
            assert (state is None) == (possible is None)
        if state is not None:
            new_d2 = verify_endpoint(points, images, state, bound)
            if witness is None:
                witness = {"offset": str(t), "state": state,
                           "diameter_squared": str(new_d2)}
    return {"cells": len(cells), "witness": witness}


def main():
    results = {}
    # One exact finite decision exhausts the continuous offset parameter.
    dumbbell = rational_points([(0, 0), (1, 0), (2, 0), (8, 1), (9, 1), (10, 1)])
    results["two_chains"] = sweep(dumbbell, (S.Integer(1), S.Integer(0)), brute=True)
    assert results["two_chains"]["witness"] is not None
    square = rational_points([(0, 0), (1, 0), (0, 1), (1, 1)])
    for vector in ((1, 0), (0, 1), (1, 1), (2, 1)):
        key = f"optimal_square_{vector}"
        results[key] = sweep(square, tuple(map(S.Integer, vector)), brute=True)
        assert results[key]["witness"] is None
    grid = rational_points([(x, y) for x in range(3) for y in range(3)])
    results["axis_grid"] = sweep(grid, (S.Integer(1), S.Integer(0)))
    assert results["axis_grid"]["witness"] is None
    # Shortening every old diameter does not certify the inactive upper pairs.
    points = rational_points([(0, 0), (10, 0), (9, 1), (1, 1), (1, 2)])
    images = [(x + S.Rational(21, 10), y) for x, y in points]
    state = [1, 0, 1, 0, 0]
    endpoint = [images[i] if bit else points[i] for i, bit in enumerate(state)]
    bound = diameter2(points)
    assert bound == 100
    assert sign(distance2(endpoint[0], endpoint[1]) - bound) < 0
    assert all(sign(distance2(endpoint[i], endpoint[j]) - 1) >= 0
               for i, j in combinations(range(len(points)), 2))
    assert sign(distance2(endpoint[2], endpoint[3]) - bound) > 0
    assert any((state[i], state[j]) == (a, b)
               for i, a, j, b in constraints(points, images, bound))
    results["inactive_isolate_upper_guard"] = "rejected exactly"
    # Explicit full-label validation, independent of successful solver output.
    for corrupted in ([0], [0, 0, 0, 0, 2]):
        try:
            verify_endpoint(points, images, corrupted, bound)
        except AssertionError:
            pass
        else:
            raise AssertionError("malformed full-source state accepted")
    results["full_label_state_guards"] = "truncated and nonbinary states rejected"
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
