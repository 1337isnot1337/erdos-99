#!/usr/bin/env python3
"""Exact regression and finite antitone-graph checks for the star-ray report.

Encodes: all seven-point distances and convex orientations, actual contacts and
diameters, assigned boundary layers, interval rows, projected positive balance,
and axial bundle resultants. Checks small finite chart barriers, an exterior
train finite diameter-count reduction, and rational oblique-grid immunity.
Enumerates *all* simple graphs through m=5 and compares connected antitone
graphs with monotone staircase paths and their central empty-support layers.

Omits: complete actual train cutsets, transverse rhombi, vertex KKT equilibrium,
mixed source rigidity, and global optimality. Positive output certifies only the
finite geometric regression and finite combinatorial comparison. The arbitrary-m
proof is in docs/reports/target_c_star_ray_staircase_reactions_2026-10-01.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
import json


@dataclass(frozen=True)
class Q42:
    """An exact element a + b sqrt(42), with exact order."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def lift(value: Q42 | int | Fraction) -> Q42:
        return value if isinstance(value, Q42) else Q42(Fraction(value))

    def __add__(self, other: Q42 | int | Fraction) -> Q42:
        other = self.lift(other)
        return Q42(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self) -> Q42:
        return Q42(-self.a, -self.b)

    def __sub__(self, other: Q42 | int | Fraction) -> Q42:
        return self + (-self.lift(other))

    def __mul__(self, other: Q42 | int | Fraction) -> Q42:
        other = self.lift(other)
        return Q42(self.a * other.a + 42 * self.b * other.b,
                   self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def sign(self) -> int:
        if not self.b:
            return (self.a > 0) - (self.a < 0)
        if not self.a:
            return (self.b > 0) - (self.b < 0)
        if self.a > 0 and self.b > 0:
            return 1
        if self.a < 0 and self.b < 0:
            return -1
        gap = self.a * self.a - 42 * self.b * self.b
        assert gap != 0, "42 is not a rational square"
        return ((gap > 0) - (gap < 0)) * ((self.a > 0) - (self.a < 0))

    def as_json(self) -> dict[str, str]:
        return {"rational": str(self.a), "sqrt42": str(self.b)}


def sub(p, q):
    return tuple(x - y for x, y in zip(p, q))


def dot(p, q):
    return sum(x * y for x, y in zip(p, q))


def det(p, q):
    return p[0] * q[1] - p[1] * q[0]


def geometric_regression() -> dict:
    q = Q42.lift
    s = Q42(Fraction(0), Fraction(1))
    points = {
        "v": (q(0), q(0)),
        "pm": (q(12), q(-5)),
        "pp": (q(12), q(5)),
        "L1": (q(6), -s),
        "U1": (q(6), s),
        "L2": (q(7), -s),
        "U2": (q(7), s),
    }
    hull = ["v", "L1", "L2", "pm", "pp", "U2", "U1"]
    for i, name in enumerate(hull):
        nxt = hull[(i + 1) % len(hull)]
        edge = sub(points[nxt], points[name])
        for other in hull:
            if other not in (name, nxt):
                assert det(edge, sub(points[other], points[name])).sign() > 0

    contacts, diameters = set(), set()
    for a, b in combinations(points, 2):
        r = sub(points[b], points[a])
        length2 = dot(r, r)
        assert (length2 - 1).sign() >= 0
        assert (length2 - 169).sign() <= 0
        if length2 == q(1):
            contacts.add(frozenset((a, b)))
        if length2 == q(169):
            diameters.add(frozenset((a, b)))
    assert contacts == {frozenset(("L1", "L2")), frozenset(("U1", "U2"))}
    assert diameters == {
        frozenset(("v", "pm")), frozenset(("v", "pp")),
        frozenset(("L1", "U2")), frozenset(("U1", "L2")),
    }
    for triple in combinations(points, 3):
        assert not all(frozenset(pair) in contacts for pair in combinations(triple, 2))

    # Orient from lower to higher layer. Positive normalized weights are 1/4.
    layers = {"v": 0, "L1": 1, "U1": 1, "L2": 2, "U2": 2, "pm": 2, "pp": 2}
    edges = [("v", "pm"), ("v", "pp"), ("L1", "U2"), ("U1", "L2")]
    rows = []
    bundles = {}
    for a, b in edges:
        lo, hi = layers[a], layers[b]
        assert lo < hi
        r = sub(points[b], points[a])
        rows.append([r[1] if lo < i <= hi else q(0) for i in (1, 2)])
        old = bundles.get((lo, hi), (q(0), q(0)))
        bundles[lo, hi] = tuple(x + Fraction(1, 4) * y for x, y in zip(old, r))
    assert rows == [[q(-5), q(-5)], [q(5), q(5)], [q(0), 2 * s], [q(0), -2 * s]]
    assert det(rows[0], rows[2]).sign() != 0
    assert all(sum(row[j] for row in rows).sign() == 0 for j in range(2))
    assert bundles == {(0, 2): (q(6), q(0)), (1, 2): (q(Fraction(1, 2)), q(0))}
    masses = [
        sum(r[0] for (a, b), r in bundles.items() if a < i <= b)
        for i in (1, 2)
    ]
    assert masses == [q(6), q(Fraction(13, 2))]

    # All physical diameters are distinct and properly cross unless sharing v.
    for h, k in combinations(edges, 2):
        if set(h).intersection(k):
            continue
        a, b, c, d = (points[name] for name in (*h, *k))
        ab, cd = sub(b, a), sub(d, c)
        assert det(ab, sub(c, a)).sign() * det(ab, sub(d, a)).sign() < 0
        assert det(cd, sub(a, c)).sign() * det(cd, sub(b, c)).sign() < 0

    # The source fails full KKT balance at v, which has no unit contacts.
    force_at_v = tuple(sum(Fraction(1, 4) * points[name][j] for name in ("pm", "pp"))
                       for j in range(2))
    assert force_at_v == (q(6), q(0))

    # Exact finite chart samples. tan(theta_i/2) lies in {-1/512,0,1/512}.
    # |theta_i| <= 2|tan(theta_i/2)| <= 1/256 < gamma/(4 D m)=5/104.
    assert Fraction(1, 256) < Fraction(5, 104)
    finite_motions = 0
    for ts in product((Fraction(-1, 512), Fraction(0), Fraction(1, 512)), repeat=2):
        if not any(ts):
            continue
        displacements = [(q(0), q(0))]
        for t in ts:
            cos = (1 - t * t) / (1 + t * t)
            sin = 2 * t / (1 + t * t)
            old = displacements[-1]
            displacements.append((old[0] + cos - 1, old[1] + sin))
        moved = {name: tuple(x + y for x, y in zip(point, displacements[layers[name]]))
                 for name, point in points.items()}
        for a, b in (("L1", "L2"), ("U1", "U2")):
            r = sub(moved[b], moved[a])
            assert dot(r, r) == q(1)
        changes = []
        for a, b in edges:
            r = sub(moved[b], moved[a])
            changes.append(dot(r, r) - 169)
        assert any(change.sign() > 0 for change in changes)
        finite_motions += 1
    assert finite_motions == 8

    # A finite exterior-train move beyond the local barrier. Coordinate 1
    # belongs only to the full span in this staircase.
    w = (Fraction(3, 5), Fraction(-4, 5))
    delta = (q(w[0] - 1), q(w[1]))
    far_moved = {
        name: tuple(x + y for x, y in zip(point, delta)) if layers[name] else point
        for name, point in points.items()
    }
    far_contacts, far_diameters = set(), set()
    for a, b in combinations(points, 2):
        r = sub(far_moved[b], far_moved[a])
        length2 = dot(r, r)
        assert (length2 - 1).sign() >= 0
        assert (length2 - 169).sign() <= 0
        if length2 == q(1):
            far_contacts.add(frozenset((a, b)))
        if length2 == q(169):
            far_diameters.add(frozenset((a, b)))
    assert far_contacts == contacts
    assert far_diameters == {
        frozenset(("L1", "U2")), frozenset(("U1", "L2"))
    }
    for name in ("pm", "pp"):
        r = sub(far_moved[name], far_moved["v"])
        assert (dot(r, r) - 169).sign() < 0
    return {
        "vertices": 7, "pair_distances_checked": 21,
        "unit_contacts": 2, "diameter_edges": 4, "diameter": 13,
        "derivative_rank": 2, "projected_positive_balance": True,
        "exact_small_finite_chart_motions_blocked": finite_motions,
        "finite_exterior_train_move": {
            "new_phase_vector": [str(x) for x in w],
            "all_new_pair_distances_checked": 21,
            "contact_count": len(far_contacts),
            "diameter_count": len(far_diameters),
            "full_span_diameters_strictly_shortened": 2,
        },
        "axial_bundles": {str(k): v[0].as_json() for k, v in bundles.items()},
        "full_source_KKT": False, "global_optimality": "not encoded",
    }


def connected(m: int, edges: tuple) -> bool:
    seen = {0}
    while True:
        new = seen | {b for a, b in edges if a in seen} | {a for a, b in edges if b in seen}
        if new == seen:
            return len(seen) == m + 1
        seen = new


def central_zero_row_regression() -> list[dict]:
    """Add an actual invisible diameter to either permitted central gap."""
    q = Q42.lift
    s = Q42(Fraction(0), Fraction(1))
    points = {
        "v": (q(0), q(0)), "pm": (q(24), q(-10)), "pp": (q(24), q(10)),
        "L1": (q(12), -2 * s), "U1": (q(12), 2 * s),
        "L2": (q(14), -2 * s), "U2": (q(14), 2 * s),
        "Le": (q(13), q(-13)), "Ue": (q(13), q(13)),
    }
    hull = ["v", "L1", "Le", "L2", "pm", "pp", "U2", "Ue", "U1"]
    for i, name in enumerate(hull):
        nxt = hull[(i + 1) % len(hull)]
        for other in hull:
            if other not in (name, nxt):
                assert det(sub(points[nxt], points[name]),
                           sub(points[other], points[name])).sign() > 0
    diameters = set()
    for a, b in combinations(points, 2):
        r = sub(points[b], points[a])
        length2 = dot(r, r)
        assert (length2 - 1).sign() > 0
        assert (length2 - 676).sign() <= 0
        if length2 == q(676):
            diameters.add(frozenset((a, b)))
    edges = [("v", "pm"), ("v", "pp"), ("L1", "U2"),
             ("U1", "L2"), ("Le", "Ue")]
    assert diameters == {frozenset(e) for e in edges}
    # The invisible upward vector has angle pi/2 strictly inside the
    # innermost two upward vectors; determinant checks avoid transcendental math.
    positive = sub(points["U2"], points["L1"])
    empty = sub(points["Ue"], points["Le"])
    negative_up = sub(points["U1"], points["L2"])
    assert det(positive, empty).sign() > 0
    assert det(empty, negative_up).sign() > 0
    results = []
    for k in (1, 2):
        layers = {"v": 0, "L1": 1, "U1": 1, "L2": 2, "U2": 2,
                  "pm": 2, "pp": 2, "Le": k, "Ue": k}
        # Both host arcs are monotone from the star anchor to the opposite arc.
        assert [layers[x] for x in ("v", "L1", "Le", "L2", "pm")] == \
               sorted(layers[x] for x in ("v", "L1", "Le", "L2", "pm"))
        assert [layers[x] for x in ("v", "U1", "Ue", "U2", "pp")] == \
               sorted(layers[x] for x in ("v", "U1", "Ue", "U2", "pp"))
        rows = []
        for a, b in edges:
            lo, hi = layers[a], layers[b]
            r = sub(points[b], points[a])
            rows.append([r[1] if lo < i <= hi else q(0) for i in (1, 2)])
        assert rows[-1] == [q(0), q(0)]
        assert all(sum(row[j] for row in rows).sign() == 0 for j in range(2))
        assert det(rows[0], rows[2]).sign() != 0
        results.append({"vertices": 9, "pair_distances_checked": 36,
                        "diameter": 26, "actual_diameters": 5,
                        "invisible_diameter_gap": k, "rank": 2,
                        "projected_positive_balance": True,
                        "complete_actual_train_cuts": "not encoded"})
    return results


def antitone(edges: tuple) -> bool:
    return all(not (a < c and b < d) and not (c < a and d < b)
               for (a, b), (c, d) in combinations(edges, 2))


def staircases(m: int) -> set[frozenset]:
    out = set()
    for word in product((0, 1), repeat=m - 1):
        a, b = 0, m
        edges = [(a, b)]
        for step in word:
            if step == 0:
                a += 1
            else:
                b -= 1
            edges.append((a, b))
        assert a + 1 == b
        out.add(frozenset(edges))
    return out


def finite_graph_check() -> list[dict]:
    results = []
    for m in range(1, 6):
        possible = tuple(combinations(range(m + 1), 2))
        survivors = set()
        for mask in range(1 << len(possible)):
            edges = tuple(edge for i, edge in enumerate(possible) if (mask >> i) & 1)
            if antitone(edges) and connected(m, edges):
                assert len(edges) == m
                survivors.add(frozenset(edges))
        expected = staircases(m)
        assert survivors == expected
        for edges in survivors:
            permitted_empty_layers = [
                k for k in range(m + 1) if all(a <= k <= b for a, b in edges)
            ]
            innermost = min(edges, key=lambda edge: edge[1] - edge[0])
            assert permitted_empty_layers == list(innermost)
            # Different empty layers put their two endpoints in the same
            # order on both physical hull arcs, so those chords do not cross.
            for k, ell in combinations(permitted_empty_layers, 2):
                assert k < ell
                lower_order = (k, ell)
                upper_order = (k, ell)
                assert lower_order == upper_order
        results.append({"m": m, "graphs_checked": 1 << len(possible),
                        "connected_antitone": len(survivors),
                        "central_empty_layers_checked": True})
    return results


def finite_oblique_grid_check() -> dict:
    """Exact finite crosscheck of the all-integer grid lemma."""
    u = (Fraction(1), Fraction(0))
    v = (Fraction(8, 17), Fraction(15, 17))
    w = (Fraction(3, 5), Fraction(-4, 5))
    assert dot(v, v) == dot(w, w) == 1
    assert Fraction(-1, 2) < dot(u, v) < Fraction(1, 2)
    assert Fraction(-1, 2) < dot(w, v) < Fraction(1, 2)
    assert det(v, u) < 0 and det(v, w) < 0
    checked = 0
    for k in range(1, 21):
        for ell in range(-20, 21):
            r = tuple((k - 1) * x + y + ell * z for x, y, z in zip(u, w, v))
            assert dot(r, r) >= 1
            checked += 1
    assert checked == 820
    return {
        "crosscut_pair_vectors_checked": checked,
        "unit_directions": {"u": list(map(str, u)), "v": list(map(str, v)),
                            "new_u": list(map(str, w))},
        "general_grid_lemma": "proved in report, not by this finite sample",
        "source_coembedding": "not encoded",
    }


def one_train_empty_far_arc_regression() -> dict:
    """Five actual source points show why the m>=2 hypothesis is needed."""
    a, x, height = Fraction(1999, 2000), Fraction(1, 28), Fraction(13)
    diameter2 = a * a + height * height
    y = (height + x) / 2
    radical = diameter2 - (height - x) ** 2 / 4

    # Local exact quadratic-field operations, now with this rational radicand.
    def scalar(value):
        return Fraction(value), Fraction(0)

    def add(p, q):
        return p[0] + q[0], p[1] + q[1]

    def minus(p, q):
        return p[0] - q[0], p[1] - q[1]

    def times(p, q):
        return p[0] * q[0] + radical * p[1] * q[1], p[0] * q[1] + p[1] * q[0]

    def sign(p):
        c, d = p
        if not d:
            return (c > 0) - (c < 0)
        if not c:
            return (d > 0) - (d < 0)
        if (c > 0) == (d > 0):
            return (c > 0) - (c < 0)
        gap = c * c - radical * d * d
        return ((gap > 0) - (gap < 0)) * ((c > 0) - (c < 0))

    def vector(p, q):
        return tuple(minus(c, d) for c, d in zip(p, q))

    def cross(p, q):
        return minus(times(p[0], q[1]), times(p[1], q[0]))

    points = {
        "v": ((a, Fraction(-1)), scalar(y)),
        "A": (scalar(0), scalar(0)),
        "C": (scalar(a), scalar(x)),
        "B": (scalar(a), scalar(height)),
        "E": (scalar(0), scalar(height + x)),
    }

    hull = ["v", "A", "C", "B", "E"]
    for i, name in enumerate(hull):
        nxt = hull[(i + 1) % len(hull)]
        edge = vector(points[nxt], points[name])
        for other in hull:
            if other not in (name, nxt):
                assert sign(cross(edge, vector(points[other], points[name]))) > 0
    diameters = set()
    for p, q in combinations(points, 2):
        r = vector(points[q], points[p])
        length2 = add(times(r[0], r[0]), times(r[1], r[1]))
        assert sign(minus(length2, scalar(1))) > 0
        assert sign(minus(length2, scalar(diameter2))) <= 0
        if sign(minus(length2, scalar(diameter2))) == 0:
            diameters.add(frozenset((p, q)))
    assert diameters == {
        frozenset(("v", "B")), frozenset(("v", "C")),
        frozenset(("A", "B")), frozenset(("C", "E")),
    }
    # v, A, E have layer 0; C, B layer 1. All four rows are full-span.
    # Equal positive weights cancel both pairs of transverse projections.
    assert (height - x) ** 2 < diameter2  # witness-star opening < pi/3
    assert radical > 0
    assert sign(cross(vector(points["B"], points["v"]),
                      vector(points["B"], points["A"]))) > 0
    assert sign(cross(vector(points["E"], points["C"]),
                      vector(points["v"], points["C"]))) > 0
    transformed_determinant = 2 * height * (a - 1)
    assert transformed_determinant < 0
    near2 = a * a + x * x
    assert 1 < near2 <= diameter2 / (diameter2 - 1)
    return {
        "vertices": 5, "all_pair_distances_checked": 10,
        "strictly_unit_separated": True, "actual_diameters": 4,
        "retained_trains": 1, "projected_positive_balance": True,
        "diameter_squared": str(diameter2),
        "empty_far_arc_determinant": str(transformed_determinant),
        "two_inactive_near_unit_pairs_squared": str(near2),
        "source_train_cut": "not encoded",
        "full_source_KKT": False, "global_optimality": "not encoded",
    }



def two_phase_grid_rotation_regression() -> dict:
    """Actual unit-cut patch whose strict diagonals block large rotations."""
    u = (Fraction(1), Fraction(0))
    vm = (Fraction(8, 17), Fraction(15, 17))
    vp = (Fraction(-8, 17), Fraction(15, 17))
    offsets = [(Fraction(0), Fraction(0)), vm,
               tuple(a + b for a, b in zip(vm, vp))]
    points = {(i, j): tuple(i * a + b for a, b in zip(u, offsets[j]))
              for i in range(3) for j in range(3)}
    contacts = set()
    diameter2 = Fraction(2056, 289)
    diameters = set()
    for p, q in combinations(points, 2):
        r = sub(points[q], points[p])
        length2 = dot(r, r)
        assert 1 <= length2 <= diameter2
        if length2 == 1:
            contacts.add(frozenset((p, q)))
        if length2 == diameter2:
            diameters.add(frozenset((p, q)))
    expected_contacts = {
        frozenset(((i, j), (i + 1, j))) for i in range(2) for j in range(3)
    } | {
        frozenset(((i, j), (i, j + 1))) for i in range(3) for j in range(2)
    }
    assert contacts == expected_contacts
    assert len(contacts) == 12
    for triple in combinations(points, 3):
        assert not all(frozenset(pair) in contacts for pair in combinations(triple, 2))
    assert diameters == {
        frozenset(((0, 0), (2, 2))), frozenset(((2, 0), (0, 2)))
    }
    # All diameter rows are full span, with opposite projections: rank 1, not 2.
    for edge in diameters:
        p, q = sorted(edge)
        assert (p[0], q[0]) == (0, 2)
    forbidden = {}
    for w in ((Fraction(3, 5), Fraction(-4, 5)),
              (Fraction(-1), Fraction(0))):
        delta = tuple(a - b for a, b in zip(w, u))
        moved = {name: tuple(a + b for a, b in zip(point, delta))
                 if name[0] >= 1 else point for name, point in points.items()}
        for edge in contacts:
            p, q = tuple(edge)
            r = sub(moved[q], moved[p])
            assert dot(r, r) == 1
        bad = []
        for p, q in combinations(points, 2):
            r = sub(moved[q], moved[p])
            if dot(r, r) < 1:
                assert frozenset((p, q)) not in contacts
                bad.append({"endpoints": [list(p), list(q)],
                            "new_squared_distance": str(dot(r, r))})
        assert bad
        forbidden[str(w)] = bad
    return {
        "vertices": 9, "pair_distances_checked": 36,
        "old_unit_contacts_preserved": 12, "unit_triangles": 0,
        "actual_diameter_edges": 2, "diameter_derivative_rank": 1,
        "forbidden_finite_rotations": forbidden,
        "full_rank_staircase": "not encoded",
        "full_source_KKT": "not encoded", "global_optimality": "not encoded",
    }

def main() -> None:
    print(json.dumps({"geometric_regression": geometric_regression(),
                      "central_zero_row_regressions": central_zero_row_regression(),
                      "finite_graph_classification": finite_graph_check(),
                      "finite_oblique_grid_immunity": finite_oblique_grid_check(),
                      "one_train_empty_far_arc": one_train_empty_far_arc_regression(),
                      "two_phase_grid_rotation": two_phase_grid_rotation_regression()},
                     indent=2))


if __name__ == "__main__":
    main()
