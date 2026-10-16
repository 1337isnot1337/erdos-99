#!/usr/bin/env python3
"""Exact full-source certificates for the parallel-contact strict competitor."""

from fractions import Fraction as Q
from itertools import combinations

from verify_global_parallel_contact_density_2026_10_11 import R, fixtures


def abs_r(value):
    return -value if value.sign() < 0 else value


def source_data(points):
    pairs = {}
    for i, j in combinations(range(len(points)), 2):
        a, b = points[i][0] - points[j][0], points[i][1] - points[j][1]
        pairs[i, j] = (a, b, a * a + b * b)
    assert all(not value[2] < R(1) for value in pairs.values())
    return pairs


def certify(name, points):
    pairs = source_data(points)
    d2 = max(q for a, b, q in pairs.values())
    if not (d2 - R(1)).sign() > 0:
        raise ValueError("diameter must be greater than one")
    contacts = {pair for pair, (_, _, q) in pairs.items() if q == R(1)}
    diameters = {pair for pair, (_, _, q) in pairs.items() if q == d2}
    if any(pairs[pair][1].sign() != 0 for pair in contacts):
        raise ValueError("this certificate requires horizontal unit contacts")
    adj = [set() for _ in points]
    for i, j in contacts:
        adj[i].add(j)
        adj[j].add(i)
    signs = [None] * len(points)
    for start in range(len(points)):
        if signs[start] is not None:
            continue
        signs[start], stack = 1, [start]
        while stack:
            i = stack.pop()
            for j in adj[i]:
                if signs[j] is None:
                    signs[j] = -signs[i]
                    stack.append(j)
                assert signs[j] == -signs[i]
    k = 1
    while any((k * abs_r(pairs[pair][1]) - R(2)).sign() <= 0
              for pair in diameters if pairs[pair][1].sign() != 0):
        k += 1
    m = 1
    while (R(m * m) - d2).sign() < 0:
        m += 1
    e = (k + 2) * m + 2
    bound = 2 * m * e + e * e
    slacks = [q - R(1) for a, b, q in pairs.values() if q != R(1)]
    slacks += [d2 - q for a, b, q in pairs.values() if q != d2]
    delta = min(slacks) if slacks else R(1)
    assert delta.sign() > 0
    t = Q(1, 2)
    while not (t < Q(1, 2 * k)
               and ((R(1) - d2 * R(1 - t * t)).sign() < 0)
               and (delta - R(2 * bound * t)).sign() > 0):
        t /= 2
    endpoint = [(R(1 - 2 * t * t) * x, R(1 - k * t) * y + R(t * signs[i]))
                for i, (x, y) in enumerate(points)]
    new_pairs = source_data(endpoint)
    for pair, (a, b, q) in new_pairs.items():
        assert (q - R(1)).sign() > 0, (name, pair, "lower")
        assert (d2 - q).sign() > 0, (name, pair, "upper")
        if pair in contacts:
            assert q == R(1 + 4 * t**4)
    print(f"PASS {name}: labels={len(points)} pairs={len(pairs)} "
          f"contacts={len(contacts)} diameters={len(diameters)} K={k} t={t}")


def run():
    certify("chain", [(R(i), R()) for i in range(5)])
    rows = [(R(i), R(Q(3 * j, 2))) for i in range(4) for j in range(2)]
    certify("rows_and_isolate", rows + [(R(Q(9, 2)), R(3))])
    certify("stretched_square", [(R(x), R(Q(101, 100) * y))
                                 for x, y in [(0, 0), (1, 0), (1, 1), (0, 1)]])
    wheel = fixtures()[1][1]
    certify("stretched_wheel", [(x, R(Q(101, 100)) * y) for x, y in wheel])
    for name, points, expected in [
        ("diameter_one", [(R(), R()), (R(1), R())], "greater than one"),
        ("multiple_directions", wheel, "horizontal unit contacts"),
    ]:
        try:
            certify(name, points)
        except ValueError as error:
            assert expected in str(error)
            print(f"PASS rejected {name}: {error}")
        else:
            raise AssertionError(f"accepted invalid fixture {name}")
    print("PASS every full-source lower/upper pair; no Level I certificate")


if __name__ == "__main__":
    run()
