#!/usr/bin/env python3
"""Exact affine certificates excluding eight more fully convex support-seven H8 orbits.

Imports the exact support-seven H8 census, reconstructs force cycles from the convex
raw-ray order and edge signs, and checks eight sparse identities.  Every identity
forces a linear turn functional to equal the boundary value of a sum of strict,
already-proved pentagon turn inequalities.  Hence each corresponding orbit is empty.

Only standard-library integer/Fraction arithmetic is used.
"""

from fractions import Fraction
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_endpoint_reduction_2026_09_19.py"
spec = importlib.util.spec_from_file_location("support7_base", BASE)
base = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(base)


def edge(a, b):
    return tuple(sorted((a, b)))


def E(*pairs):
    return frozenset(edge(a, b) for a, b in pairs)


def raw_order(i, missing):
    return tuple(
        j
        for j in ((i + k) % 8 for k in range(1, 8))
        if edge(i, j) not in missing
    )


def force_cycle(i, missing, positive):
    raw = raw_order(i, missing)
    pos = tuple(j for j in raw if edge(i, j) in positive)
    neg = tuple(j for j in raw if edge(i, j) not in positive)
    return pos + neg


def edge_sign(positive, i, j):
    return 1 if edge(i, j) in positive else -1


def add_affine(a, b, scale=Fraction(1)):
    row = dict(a[0])
    for z, c in b[0].items():
        row[z] = row.get(z, Fraction(0)) + scale * c
        if row[z] == 0:
            del row[z]
    return row, a[1] + scale * b[1]


def scaled_row(row, scale):
    return {z: scale * c for z, c in row.items() if scale * c}


def var(i, k):
    return ({(i, k): Fraction(1)}, Fraction(0))


def pair(i, k):
    n = 7 if i == 0 else 5
    return add_affine(var(i, k), var(i, (k + 1) % n))


def force_arc(cycles, i, a, b):
    cyc = cycles[i]
    ia = cyc.index(a)
    ib = cyc.index(b)
    row = {}
    k = ia
    while k != ib:
        row[(i, k)] = row.get((i, k), Fraction(0)) + 1
        k = (k + 1) % len(cyc)
    return row


def raw_chi(i, a, b, missing):
    order = raw_order(i, missing)
    pa = order.index(a)
    pb = order.index(b)
    return 1 if pb > pa else -1


def raw_angle_affine(positive, cycles, missing, i, a, b):
    arc = force_arc(cycles, i, a, b)
    same = edge_sign(positive, i, a) == edge_sign(positive, i, b)
    chi = raw_chi(i, a, b, missing)
    if same and chi > 0:
        return arc, Fraction(0)
    if same and chi < 0:
        return scaled_row(arc, -1), Fraction(2)
    if (not same) and chi > 0:
        return arc, Fraction(-1)
    return scaled_row(arc, -1), Fraction(1)


def triangle_affine(positive, cycles, missing, a, b, c):
    assert all(edge(*e) not in missing for e in ((a, b), (a, c), (b, c)))
    out = ({}, Fraction(0))
    for i, j, k in ((a, b, c), (b, a, c), (c, a, b)):
        out = add_affine(
            out,
            raw_angle_affine(positive, cycles, missing, i, j, k),
        )
    return out


def face_affine(cycles, i):
    return (
        {(i, k): Fraction(1) for k in range(len(cycles[i]))},
        Fraction(0),
    )


def combine(terms, shift=0):
    out = ({}, Fraction(shift))
    for coefficient, affine in terms:
        out = add_affine(out, affine, Fraction(coefficient))
    return out


# Reproduce the 20 H8 reflection orbits left by the first support-seven reduction.
remaining = []
for typ, missing, H, solutions, smaller in base.canonical_orbits:
    if typ == "C7" and smaller == 2:
        continue
    patterns = {base.ground_minority(solution[1]) for solution in solutions}
    assert len(patterns) == 1
    minority = next(iter(patterns))
    reflected = frozenset(base.reflect_vertex(i) for i in minority)
    if minority in base.projection_bad or reflected in base.projection_bad:
        continue
    remaining.append((typ, missing, H, solutions[0][1], minority))
assert len(remaining) == 20


# Each inequality descriptor contributes a strict row*x < bound.
# p_gt23 means -(x_ik+x_i,k+1) < -2/3, etc.
def strict_inequality(kind, i, k):
    if kind == "x_gt0":
        return combine([(-1, var(i, k))]), Fraction(0)
    if kind == "x_lt23":
        return var(i, k), Fraction(2, 3)
    if kind == "p_gt23":
        return combine([(-1, pair(i, k))]), Fraction(-2, 3)
    if kind == "p_lt1":
        return pair(i, k), Fraction(1)
    raise ValueError(kind)


CASES = [
    {
        "name": "A",
        "type": "C7",
        "missing": E((1, 2), (1, 6), (2, 7), (3, 4), (3, 5), (4, 6), (5, 7)),
        "positive": E((0, 2), (0, 3), (0, 5), (0, 6), (1, 4), (1, 7), (2, 3), (2, 5), (3, 6), (4, 7)),
        "ineq": [("p_gt23", 2, 0), ("p_gt23", 2, 2), ("p_gt23", 3, 0), ("p_lt1", 6, 1)],
        "eq": [(-1, "F", 3), (+1, "F", 6), (-1, "T", (2, 3, 6))],
        "shift": 0,
    },
    {
        "name": "B",
        "type": "C7",
        "missing": E((1, 3), (1, 6), (2, 3), (2, 7), (4, 5), (4, 6), (5, 7)),
        "positive": E((0, 2), (0, 3), (0, 5), (0, 6), (1, 4), (1, 7), (2, 5), (3, 4), (3, 6), (4, 7)),
        "ineq": [("x_lt23", 3, 4), ("p_gt23", 4, 0), ("p_lt1", 7, 1)],
        "eq": [(+1, "F", 3), (-1, "F", 4), (+1, "F", 7), (-1, "T", (3, 4, 7))],
        "shift": 0,
    },
    {
        "name": "C",
        "type": "C7",
        "missing": E((1, 3), (1, 7), (2, 4), (2, 7), (3, 5), (4, 6), (5, 6)),
        "positive": E((0, 2), (0, 3), (0, 5), (0, 7), (1, 4), (1, 6), (2, 5), (3, 6), (4, 7), (6, 7)),
        "ineq": [("p_lt1", 3, 3), ("p_gt23", 6, 0), ("x_lt23", 7, 2)],
        "eq": [(+1, "F", 0), (-1, "T", (0, 3, 6)), (+1, "T", (0, 3, 7)), (-1, "T", (0, 6, 7))],
        "shift": 0,
    },
    {
        "name": "D",
        "type": "C3+C4",
        "missing": E((1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)),
        "positive": E((0, 2), (0, 4), (0, 6), (1, 5), (1, 7), (2, 4), (2, 6), (3, 5), (3, 7), (5, 6)),
        "ineq": [("x_lt23", 3, 1), ("p_gt23", 4, 2), ("p_lt1", 7, 4)],
        "eq": [(+1, "F", 3), (-1, "F", 4), (+1, "F", 7), (-1, "T", (3, 4, 7))],
        "shift": 0,
    },
    {
        "name": "E",
        "type": "C3+C4",
        "missing": E((1, 2), (1, 3), (2, 3), (4, 6), (4, 7), (5, 6), (5, 7)),
        "positive": E((0, 2), (0, 4), (0, 6), (1, 5), (1, 7), (2, 4), (2, 6), (3, 5), (3, 7)),
        "ineq": [("x_gt0", 0, 4), ("p_gt23", 3, 2), ("p_gt23", 4, 2), ("p_gt23", 5, 2)],
        "eq": [(-1, "F", 4), (+1, "F", 5), (-1, "T", (0, 3, 5)), (-1, "T", (3, 4, 5))],
        "shift": 0,
    },
    {
        "name": "F",
        "type": "C3+C4",
        "missing": E((1, 2), (1, 7), (2, 7), (3, 4), (3, 5), (4, 6), (5, 6)),
        "positive": E((0, 2), (0, 3), (0, 5), (0, 7), (1, 4), (1, 6), (2, 3), (2, 5), (3, 6), (4, 7), (6, 7)),
        "ineq": [("x_gt0", 0, 0), ("p_gt23", 2, 0), ("p_gt23", 3, 0), ("p_gt23", 3, 1), ("p_gt23", 6, 0), ("x_lt23", 7, 2)],
        "eq": [(-1, "F", 2), (-1, "F", 6), (+1, "F", 7), (-1, "T", (0, 2, 3)), (-1, "T", (3, 6, 7))],
        "shift": 2,
    },
    {
        "name": "G",
        "type": "C3+C4",
        "missing": E((1, 3), (1, 7), (2, 3), (2, 7), (4, 5), (4, 6), (5, 6)),
        "positive": E((0, 2), (0, 3), (0, 5), (0, 7), (1, 4), (1, 6), (2, 5), (3, 4), (3, 6), (4, 7), (6, 7)),
        "ineq": [("p_lt1", 3, 4), ("p_gt23", 6, 0), ("x_lt23", 7, 2)],
        "eq": [(+1, "F", 3), (-1, "F", 6), (+1, "F", 7), (-1, "T", (3, 6, 7))],
        "shift": 0,
    },
    {
        "name": "H",
        "type": "C3+C4",
        "missing": E((1, 2), (1, 6), (2, 7), (3, 4), (3, 5), (4, 5), (6, 7)),
        "positive": E((0, 2), (0, 3), (0, 5), (0, 6), (1, 4), (1, 7), (2, 3), (2, 5), (3, 6), (4, 7), (5, 6)),
        "ineq": [("p_lt1", 2, 4), ("p_gt23", 5, 0), ("x_lt23", 6, 2)],
        "eq": [(-1, "F", 5), (-1, "T", (0, 2, 5)), (+1, "T", (0, 2, 6)), (-1, "T", (0, 5, 6))],
        "shift": 4,
    },
]

remaining_keys = {(typ, missing, positive) for typ, missing, _, positive, _ in remaining}
excluded_keys = set()

for case in CASES:
    key = (case["type"], case["missing"], case["positive"])
    assert key in remaining_keys, (case["name"], "orbit not in 20-case input")
    assert key not in excluded_keys
    excluded_keys.add(key)

    cycles = {
        i: force_cycle(i, case["missing"], case["positive"])
        for i in range(8)
    }
    assert len(cycles[0]) == 7
    assert all(len(cycles[i]) == 5 for i in range(1, 8))

    # Sum the strict inequalities.  The actual geometry gives C(x) < B.
    C = ({}, Fraction(0))
    B = Fraction(0)
    for desc in case["ineq"]:
        affine, bound = strict_inequality(*desc)
        C = add_affine(C, affine)
        B += bound
    assert C[1] == 0

    # Build the exact affine identity C = shift + sum coeff * F/T.
    eq_terms = []
    value = Fraction(case["shift"])
    for coefficient, kind, data in case["eq"]:
        if kind == "F":
            affine = face_affine(cycles, data)
            value += coefficient * 2
        else:
            affine = triangle_affine(
                case["positive"], cycles, case["missing"], *data
            )
            value += coefficient * 1
        eq_terms.append((coefficient, affine))
    RHS = combine(eq_terms, case["shift"])

    assert C == RHS, (case["name"], "affine identity mismatch")
    assert value == B, (case["name"], "boundary value mismatch", value, B)
    print(
        f"{case['name']}: {case['type']} exact identity forces C={B}, "
        "but strict turn inequalities force C<B; EXCLUDED"
    )

assert len(excluded_keys) == 8
assert len(remaining_keys - excluded_keys) == 12
assert sum(typ == "C7" for typ, _, _ in remaining_keys - excluded_keys) == 9
assert sum(typ == "C3+C4" for typ, _, _ in remaining_keys - excluded_keys) == 3

print("PASS")
print("eight additional fully-convex H8 reflection orbits excluded exactly")
print("remaining H8 reflection orbits: 12 = 9 C7 + 3 C3+C4")
