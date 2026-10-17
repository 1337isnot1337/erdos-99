#!/usr/bin/env python3
"""Exact affine certificate for the final uniform H5 surface signatures.

The verifier uses only the exact force cycles, edge signs, ground raw-ray order,
translation-surface corner pairing, and ordinary triangle angle sum.  All arithmetic
is integer coefficient arithmetic.  No floating point, coordinates, optimization,
or numerical tolerance is used.
"""

GROUND_FORCE = (1, 2, 3, 6, 5, 4)
RAW_GROUND = (1, 6, 5, 2, 3, 4)
MISSING = {tuple(sorted(e)) for e in ((1, 6), (2, 5), (3, 4))}

CASES = {
    1: {
        1: (0, 3, 5, 2, 4),
        2: (0, 1, 4, 6, 3),
        3: (0, 6, 2, 5, 1),
        4: (0, 5, 2, 6, 1),
        5: (0, 6, 1, 3, 4),
        6: (0, 3, 4, 2, 5),
    },
    2: {
        1: (0, 3, 5, 2, 4),
        2: (0, 1, 4, 6, 3),
        3: (0, 6, 2, 5, 1),
        4: (0, 6, 2, 5, 1),
        5: (0, 4, 1, 3, 6),
        6: (0, 3, 5, 2, 4),
    },
    3: {
        1: (0, 3, 4, 2, 5),
        2: (0, 1, 4, 6, 3),
        3: (0, 6, 2, 5, 1),
        4: (0, 1, 2, 6, 5),
        5: (0, 6, 4, 3, 1),
        6: (0, 3, 4, 2, 5),
    },
}

PSETS = {
    1: {(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 3), (3, 6), (4, 6)},
    2: {(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 3), (3, 6), (4, 5), (5, 6)},
    3: {(0, 1), (0, 2), (0, 3), (1, 2), (1, 5), (2, 3), (3, 6), (4, 5), (4, 6)},
}

EXPECTED_CLASSES = {
    1: [(16, 12, 4), (3, 2, 1), (3, 2, 1), (3, 3, 0), (11, 11, 0)],
    2: [(22, 16, 6), (3, 3, 0), (4, 4, 0), (3, 3, 0), (4, 4, 0)],
    3: [(19, 16, 3), (14, 12, 2), (3, 2, 1)],
}


def edge(a, b):
    return tuple(sorted((a, b)))


def add(a, b, scale=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + scale * v
        if out[k] == 0:
            del out[k]
    return out


def scaled(a, s):
    return {k: s * v for k, v in a.items() if s * v}


def variable(i, k):
    return {(i, k): 1}


def force_arc(face_cycles, i, a, b):
    """Normalized CCW force angle from neighbor a to neighbor b."""
    cyc = face_cycles[i]
    ia = cyc.index(a)
    ib = cyc.index(b)
    n = len(cyc)
    row = {}
    k = ia
    while k != ib:
        row = add(row, variable(i, k))
        k = (k + 1) % n
    return row


def edge_sign(case, i, j):
    return 1 if edge(i, j) in PSETS[case] else -1


def raw_chi(case, face_cycles, i, a, b):
    """Orientation sign of raw reciprocal rays ia,ib from exact order data."""
    if i == 0:
        pa = RAW_GROUND.index(a)
        pb = RAW_GROUND.index(b)
        return 1 if pb > pa else -1

    cyc = face_cycles[i]
    ia = cyc.index(a)
    ib = cyc.index(b)
    d = (ib - ia) % 5
    assert d in (1, 2, 3, 4)

    # The strict two-turn theorem makes the force cross tournament regular.
    force_chi = 1 if d in (1, 2) else -1
    return edge_sign(case, i, a) * edge_sign(case, i, b) * force_chi


def raw_angle_affine(case, face_cycles, i, a, b):
    """Return (row,const) for raw interior angle/pi at vertex i."""
    arc = force_arc(face_cycles, i, a, b)
    same = edge_sign(case, i, a) == edge_sign(case, i, b)
    chi = raw_chi(case, face_cycles, i, a, b)

    if same and chi > 0:
        return arc, 0
    if same and chi < 0:
        return scaled(arc, -1), 2
    if (not same) and chi > 0:
        return arc, -1
    return scaled(arc, -1), 1


def triangle_affine(case, face_cycles, a, b, c):
    row = {}
    const = 0
    for i, j, k in ((a, b, c), (b, a, c), (c, a, b)):
        r, q = raw_angle_affine(case, face_cycles, i, j, k)
        row = add(row, r)
        const += q
    return row, const


def face_affine(face_cycles, i):
    return {(i, k): 1 for k in range(len(face_cycles[i]))}, 0


class UF:
    def __init__(self, xs):
        self.p = {x: x for x in xs}

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.p[b] = a


def surface_classes(face_cycles):
    corners = [
        (f, k)
        for f, cyc in face_cycles.items()
        for k in range(len(cyc))
    ]
    uf = UF(corners)
    seen = set()

    for f, cyc in face_cycles.items():
        n = len(cyc)
        for k, g in enumerate(cyc):
            e = edge(f, g)
            if e in seen:
                continue
            seen.add(e)
            other = face_cycles[g]
            l = other.index(f)
            m = len(other)
            uf.union((f, k), (g, (l + 1) % m))
            uf.union((f, (k + 1) % n), (g, l))

    out = {}
    for c in corners:
        out.setdefault(uf.find(c), []).append(c)
    return list(out.values())


def class_gap_row(comp, face_cycles):
    # Corner k lies after exterior gap k-1 in the force cycle.
    row = {}
    for f, k in comp:
        gap = (k - 1) % len(face_cycles[f])
        row = add(row, variable(f, gap))
    return row


def combine_full_affine(terms, shift=0):
    row = {}
    const = shift
    for coeff, (r, q) in terms:
        row = add(row, r, coeff)
        const += coeff * q
    return row, const


# Each identity is written in terms of the full affine functionals F_i and T_ijk.
IDENTITIES = {
    1: {
        "class": 4,
        "terms": [
            (-1, "F0"),
            (-1, "T012"),
            (+1, "T015"),
            (-1, "T023"),
            (+1, "T035"),
            (-1, "T045"),
            (+1, "T046"),
            (-1, "T056"),
        ],
        "shift": 8,
        "gap_value": 5,
        "cone_order": 3,
    },
    2: {
        "class": 0,
        "terms": [
            (+1, "F1"), (+1, "F2"), (+1, "F3"),
            (+1, "F4"), (+1, "F5"), (+1, "F6"),
            (+1, "T012"), (-1, "T013"), (+1, "T023"),
            (-1, "T045"), (+1, "T046"), (-1, "T056"),
        ],
        "shift": -4,
        "gap_value": 8,
        "cone_order": 7,
    },
    3: {
        "class": 1,
        "terms": [
            (+1, "F0"), (+1, "F1"), (+1, "F5"),
            (+1, "T014"), (-1, "T023"), (-1, "T024"),
            (-1, "T026"), (+1, "T035"), (+1, "T046"),
        ],
        "shift": 0,
        "gap_value": 6,
        "cone_order": 4,
    },
}


for case in (1, 2, 3):
    face_cycles = {0: GROUND_FORCE, **CASES[case]}
    comps = surface_classes(face_cycles)

    summary = [
        (
            len(c),
            sum(f != 0 for f, _ in c),
            sum(f == 0 for f, _ in c),
        )
        for c in comps
    ]
    assert summary == EXPECTED_CLASSES[case], (case, summary)

    funcs = {f"F{i}": face_affine(face_cycles, i) for i in range(7)}
    for a in range(7):
        for b in range(a + 1, 7):
            for c in range(b + 1, 7):
                if any(
                    edge(*e) in MISSING
                    for e in ((a, b), (a, c), (b, c))
                ):
                    continue
                funcs[f"T{a}{b}{c}"] = triangle_affine(
                    case, face_cycles, a, b, c
                )

    spec = IDENTITIES[case]
    terms = [(coef, funcs[name]) for coef, name in spec["terms"]]
    rhs_row, rhs_const = combine_full_affine(terms, spec["shift"])
    target_row = class_gap_row(comps[spec["class"]], face_cycles)

    # This is the exact symbolic identity as an affine polynomial.
    assert rhs_row == target_row, (case, "coefficient mismatch")
    assert rhs_const == 0, (case, "constant mismatch", rhs_const)

    # Evaluate only the universal exact equalities F_i=2 and T_ijk=1.
    gap_value = spec["shift"]
    for coeff, name in spec["terms"]:
        gap_value += coeff * (2 if name.startswith("F") else 1)
    assert gap_value == spec["gap_value"]

    N = len(comps[spec["class"]])
    assert N - gap_value == 2 * spec["cone_order"]
    cone_order = (N - gap_value) // 2

    print(
        f"P{case}: N={N}, gap_sum/pi={gap_value}, "
        f"cone_order={cone_order}; exact affine identity PASS"
    )

print(
    "PASS: H5 triangle-angle identities force "
    "P1 H(4,2), P2 H(6), P3 H(5,3)."
)
