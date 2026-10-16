#!/usr/bin/env python3
"""Exact full-source lift/rank and planar endpoint checks, not optimality checks.

--endpoint-json accepts rational source, target and t for the planar endpoint
(source+t*target)/sqrt(1+t*t). Every lower/upper pair is checked. Intermediate
path feasibility is deliberately not required. No Level I conclusion follows.
"""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")
import argparse
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
import sympy as sp


def rational(x):
    if isinstance(x, float):
        raise ValueError("Supply rational integers or strings, not floats")
    return F(x)


def points(rows):
    p = [tuple(map(rational, row)) for row in rows]
    if not p or any(len(row) != 2 for row in p):
        raise ValueError("Expected nonempty planar array")
    return p


def sq(x, y):
    return sum((a-b)**2 for a, b in zip(x, y))


def distances(p):
    return {(i, j): sq(p[i], p[j]) for i, j in combinations(range(len(p)), 2)}


def affine_rank(rows):
    return sp.Matrix([[sp.Rational(x-y) for x, y in zip(row, rows[0])]
                      for row in rows[1:]]).rank()


def lift_check(p, colour, t2):
    old = distances(p)
    assert len(p) == len(colour) and t2 > 0
    assert min(old.values()) >= 1 and max(old.values()) > 1
    assert all(colour[i] != colour[j] for (i, j), d in old.items() if d == 1)
    slack = [d-1 for (i, j), d in old.items() if colour[i] == colour[j]]
    assert not slack or t2 < min(slack)
    new = {e: (d+t2*(colour[e[0]] != colour[e[1]]))/(1+t2) for e, d in old.items()}
    assert min(new.values()) >= 1 and max(new.values()) < max(old.values())
    assert {e for e, d in old.items() if d == 1} == {e for e, d in new.items() if d == 1}
    assert all(new[e] < max(old.values()) for e, d in old.items() if d == max(old.values()))
    return {"labels": len(p), "pairs": len(old), "old_D2": str(max(old.values())),
            "lifted_D2": str(max(new.values()))}


def endpoint_check(p, v, t):
    if len(p) != len(v) or t <= 0:
        raise ValueError("One target per label and positive t required")
    old = distances(p)
    if not old or min(old.values()) < 1:
        raise ValueError("Source must be unit separated with at least two labels")
    numerator = [tuple(a+t*b for a, b in zip(x, z)) for x, z in zip(p, v)]
    new = {e: d/(1+t*t) for e, d in distances(numerator).items()}
    lower, diameter, old_diameter = min(new.values()), max(new.values()), max(old.values())
    return {"labels": len(p), "pairs_checked": len(old), "t": str(t),
            "minimum_squared_distance": str(lower), "source_D2": str(old_diameter),
            "endpoint_D2": str(diameter), "unit_separated": lower >= 1,
            "strict_diameter_improvement": diameter < old_diameter,
            "planar_strict_competitor": lower >= 1 and diameter < old_diameter,
            "source_global_optimality": "not checked"}


def verify():
    square = points([[0, 0], [1, 0], [1, 1], [0, 1]])
    rectangle = points([[0, 0], [1, 0], [1, "6/5"], [0, "6/5"]])
    triangle = points([[0, 0], [1, 0], [0, 1]])
    isolated = square+points([["1/2", 3]])
    for name, p, colour in [("square", square, [0, 1, 0, 1]),
                             ("rectangle", rectangle, [0, 1, 1, 0]),
                             ("right_triangle", triangle, [0, 1, 1]),
                             ("square_and_isolate", isolated, [0, 1, 0, 1, 2])]:
        print("PASS full-source lift", name, json.dumps(lift_check(p, colour, F(1, 100))))
    for p in (square, rectangle, triangle, isolated):
        n = len(p)
        pp = sp.Matrix([[sp.Rational(x) for x in row] for row in p])
        j = sp.eye(n)-sp.ones(n)/n
        g = j*pp*pp.T*j
        lam = sp.Rational(3, 5)
        new_g = lam*g+(1-lam)*j/2
        assert g.rank() == 2 and new_g.rank() == n-1
        for i, k in combinations(range(n), 2):
            assert new_g[i, i]+new_g[k, k]-2*new_g[i, k] == 1+lam*(sp.Rational(sq(p[i], p[k]))-1)
        print("PASS uniform Gram interpolation rank", n, "labels", new_g.rank())
    assert affine_rank([row+(F(c),) for row, c in zip(square, [0, 1, 0, 1])]) == 3
    assert affine_rank([row+(F(c),) for row, c in zip(rectangle, [0, 1, 1, 0])]) == 2
    print("PASS colour-lift ranks: square 3, affine-coloured rectangle 2")
    t2 = F(1, 100)
    rect_dist = [(rectangle[i][0]-rectangle[k][0])**2 +
                 (rectangle[i][1]-rectangle[k][1])**2/(1+t2)
                 for i, k in combinations(range(4), 2)]
    assert min(rect_dist) == 1 and max(rect_dist) < max(distances(rectangle).values())
    print("PASS actual planar flattening", str(max(rect_dist)))
    pair, target = points([[-2, 0], [2, 0]]), points([[3, 0], [-3, 0]])
    result = endpoint_check(pair, target, F(1))
    assert result["planar_strict_competitor"]
    middle = [tuple(a+F(2, 3)*b for a, b in zip(x, z)) for x, z in zip(pair, target)]
    assert sq(*middle) == 0
    print("PASS valid nonlocal endpoint despite intermediate collision", json.dumps(result))
    bad = endpoint_check(square, points([[0, 0]]*4), F(1))
    assert bad["strict_diameter_improvement"] and not bad["planar_strict_competitor"]
    print("PASS rejecting diameter-only contraction")
    print("PASS exact finite certificates; no global optimality or Level I conclusion")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--endpoint-json", type=Path)
    args = parser.parse_args()
    if args.endpoint_json:
        data = json.loads(args.endpoint_json.read_text())
        result = endpoint_check(points(data["source"]), points(data["target"]), rational(data["t"]))
        print(json.dumps(result, indent=2))
        return 0 if result["planar_strict_competitor"] else 1
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
