#!/usr/bin/env python3
"""Independent exact checks for the PR #597 hostile audit.

Encodes nine/ten-point sources in Q(sqrt(42),sqrt(165)), every pair
distance, strict convexity, actual contact/diameter sets, nested layer maps,
projected positive circulation, interval rank, bundle resultants, and EVERY
choice of angular representatives. Tests both three-cell staircases and
two-cell coarsenings with multiple representatives in one bundle. The tenth
point makes the ray exit an actual parallel-diameter endpoint.

Also checks every directed simple cycle on at most eight gap vertices
against the necessary antitone endpoint-order relation. No cycle of length
at least three survives. This finite check is not the arbitrary-size proof.

The follow-up checks the exterior-train move against multiple full-span rows
and exact inactive blockers. Two five-point quadratic-field sources distinguish
an empty far arc from a singleton and distinguish aggregate contact-cut balance
from the edgewise contact-vector rule needed for finite contact preservation.

Omits actual global train cuts, a transverse O-O grid, mixed rigidity,
contact minimality and global optimality. Full-source KKT/contact-cut law
FAILURE is certified rather than omitted silently. A positive result proves
only these finite exact regressions and comparisons.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product
from math import isqrt
import json


@dataclass(frozen=True)
class Biquad:
    # Basis 1, sqrt(42), sqrt(165), sqrt(6930).
    c: tuple[Fraction, ...] = (Fraction(0),) * 4

    @staticmethod
    def lift(x):
        return x if isinstance(x, Biquad) else Biquad((Fraction(x),) + (Fraction(0),) * 3)

    def __add__(self, other):
        other = self.lift(other)
        return Biquad(tuple(a + b for a, b in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return Biquad(tuple(-a for a in self.c))

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __mul__(self, other):
        other = self.lift(other)
        out = [Fraction(0)] * 4
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                common = i & j
                factor = (42 if common & 1 else 1) * (165 if common & 2 else 1)
                out[i ^ j] += factor * a * b
        return Biquad(tuple(out))

    __rmul__ = __mul__

    def sign(self):
        if not any(self.c):
            return 0
        # All bounds are rational. isqrt verifies lower^2 <= N < upper^2.
        for power in range(1, 16):
            scale = 10 ** power
            lower = upper = self.c[0]
            for coefficient, radicand in zip(self.c[1:], (42, 165, 6930)):
                numerator = isqrt(radicand * scale * scale)
                lo = Fraction(numerator, scale)
                hi = Fraction(numerator + 1, scale)
                assert lo * lo <= radicand < hi * hi
                lower += coefficient * (lo if coefficient >= 0 else hi)
                upper += coefficient * (hi if coefficient >= 0 else lo)
            if lower > 0:
                return 1
            if upper < 0:
                return -1
        raise AssertionError(f"No sign certificate for {self.c}")

    def as_json(self):
        return dict(zip(("1", "sqrt42", "sqrt165", "sqrt6930"), map(str, self.c)))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def rational_rank(rows):
    rows = [[Fraction(x) for x in row] for row in rows]
    rank = 0
    for j in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        denominator = rows[rank][j]
        rows[rank] = [x / denominator for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank:
                factor = rows[i][j]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def geometric_check(parallel_exit, coarsen):
    q = Biquad.lift
    s = Biquad((Fraction(0), Fraction(1), Fraction(0), Fraction(0)))
    t = Biquad((Fraction(0), Fraction(0), Fraction(1), Fraction(0)))
    points = {
        "v": (q(0), q(0)), "pm": (q(12), q(-5)), "pp": (q(12), q(5)),
        "L1": (q(6), -s), "U1": (q(6), s),
        "L2": (q(7), -s), "U2": (q(7), s),
        "L3": (q(8), s - t), "U3": (q(8), t - s),
    }
    hull = ["v", "L1", "L2", "L3", "pm", "pp", "U3", "U2", "U1"]
    if parallel_exit:
        points["z"] = (q(13), q(0))
        hull.insert(5, "z")
    for a, b in zip(hull, hull[1:] + hull[:1]):
        for c in hull:
            if c not in (a, b):
                assert det(sub(points[b], points[a]), sub(points[c], points[a])).sign() > 0

    contacts, diameters = set(), set()
    for a, b in combinations(points, 2):
        length2 = dot(sub(points[b], points[a]), sub(points[b], points[a]))
        assert (length2 - 1).sign() >= 0
        assert (length2 - 169).sign() <= 0
        if (length2 - 1).sign() == 0:
            contacts.add(frozenset((a, b)))
        if (length2 - 169).sign() == 0:
            diameters.add(frozenset((a, b)))
    assert contacts == {frozenset(("L1", "L2")), frozenset(("U1", "U2"))}
    expected = {frozenset(e) for e in (("v", "pm"), ("v", "pp"),
                ("L1", "U2"), ("L2", "U1"), ("L1", "U3"), ("L3", "U1"))}
    if parallel_exit:
        expected.add(frozenset(("v", "z")))
    assert diameters == expected
    assert all(not all(frozenset(e) in contacts for e in combinations(triple, 2))
               for triple in combinations(points, 3))

    m = 2 if coarsen else 3
    levels = {"v": 0, "L1": 1, "U1": 1, "L2": 2, "U2": 2,
              "L3": m, "U3": m, "pm": m, "pp": m}
    if parallel_exit:
        levels["z"] = m
    lower_arc = ["v", "L1", "L2", "L3", "pm"] + (["z"] if parallel_exit else [])
    upper_arc = ["v", "U1", "U2", "U3", "pp"] + (["z"] if parallel_exit else [])
    assert all(levels[a] <= levels[b] for arc in (lower_arc, upper_arc)
               for a, b in zip(arc, arc[1:]))

    beta = Fraction(1, len(diameters))
    bundles, rows, indicator_rows = {}, [], []
    parallel_mass = q(0)
    for edge in sorted(diameters, key=lambda e: sorted(e)):
        a, b = sorted(edge, key=lambda name: levels[name])
        lo, hi = levels[a], levels[b]
        vector = sub(points[b], points[a])
        assert lo < hi
        if not vector[1].sign():
            assert set(edge) == {"v", "z"}
            parallel_mass += beta * vector[0]
            continue
        indicator = [int(lo < i <= hi) for i in range(1, m + 1)]
        indicator_rows.append(indicator)
        rows.append([vector[1] * x for x in indicator])
        bundle = bundles.setdefault((lo, hi), {"plus": [], "minus": [], "resultant": (q(0), q(0))})
        physical_up = vector if vector[1].sign() > 0 else tuple(-x for x in vector)
        bundle["plus" if vector[1].sign() > 0 else "minus"].append(physical_up)
        bundle["resultant"] = tuple(x + beta * y for x, y in zip(bundle["resultant"], vector))

    assert rational_rank(indicator_rows) == m
    assert all(sum(beta * row[i] for row in rows).sign() == 0 for i in range(m))
    cells = sorted(bundles, key=lambda e: (e[0], -e[1]))
    assert cells == ([(0, 2), (1, 2)] if coarsen else [(0, 3), (1, 3), (1, 2)])
    for bundle in bundles.values():
        assert bundle["resultant"][1].sign() == 0
        assert bundle["resultant"][0].sign() > 0
        assert all(det(a, b).sign() > 0 for a, b in product(bundle["plus"], bundle["minus"]))
    representative_choices = 0
    selections = [list(product(bundles[c]["plus"], bundles[c]["minus"])) for c in cells]
    for choices in product(*selections):
        representative_choices += 1
        for (a, b), (c, d) in zip(choices, choices[1:]):
            assert det(a, c).sign() > 0  # alpha_t < alpha_(t+1)
            assert det(d, b).sign() > 0  # gamma_(t+1) < gamma_t

    masses = [parallel_mass + sum(bundle["resultant"][0]
              for (a, b), bundle in bundles.items() if a < i <= b)
              for i in range(1, m + 1)]
    if coarsen:
        assert (masses[1] - masses[0]).sign() > 0
    else:
        assert (masses[1] - masses[0]).sign() > 0
        assert (masses[1] - masses[2]).sign() > 0
    contact_cut_counts = [sum(min(levels[x] for x in edge) < i <= max(levels[x] for x in edge)
                              for edge in contacts) for i in range(1, m + 1)]
    assert contact_cut_counts[0] == 0 and masses[0].sign() > 0
    assert all("v" not in edge for edge in contacts)
    # This failure holds for every positive weight on the two star bars:
    # both have positive axial component 12 at the contact-isolated vertex v.
    return {"vertices": len(points), "source_pairs": len(points) * (len(points) - 1) // 2,
            "m": m, "parallel_source_exit": parallel_exit, "unit_contacts": len(contacts),
            "actual_diameters": len(diameters), "rank": m, "projected_balance": True,
            "representative_choices_checked": representative_choices,
            "formal_cut_masses": [x.as_json() for x in masses],
            "actual_contact_cut_counts": contact_cut_counts,
            "full_source_KKT": False, "actual_contact_cut_law": False,
            "global_optimality": "not encoded"}


def simple_cycle_order_check():
    result = []
    for n in range(2, 9):
        inspected = surviving_two = surviving_long = 0
        for k in range(2, n + 1):
            for vertices in combinations(range(n), k):
                for tail in permutations(vertices[1:]):
                    cycle = (vertices[0],) + tail
                    edges = list(zip(cycle, cycle[1:] + cycle[:1]))
                    inspected += 1
                    if all((a - c) * (b - d) <= 0 for (a, b), (c, d) in combinations(edges, 2)):
                        if k == 2:
                            surviving_two += 1
                        else:
                            surviving_long += 1
        assert surviving_two == n * (n - 1) // 2
        assert surviving_long == 0
        result.append({"gap_vertices": n, "cycles_checked": inspected,
                       "two_cycles": surviving_two, "long_cycles": surviving_long})
    return result


@dataclass(frozen=True)
class Quadratic:
    radicand: Fraction
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def lift(self, other):
        if isinstance(other, Quadratic):
            assert other.radicand == self.radicand
            return other
        return Quadratic(self.radicand, Fraction(other))

    def __add__(self, other):
        other = self.lift(other)
        return Quadratic(self.radicand, self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Quadratic(self.radicand, -self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __mul__(self, other):
        other = self.lift(other)
        return Quadratic(self.radicand, self.a * other.a + self.radicand * self.b * other.b,
                         self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def sign(self):
        assert self.radicand > 0
        if not self.b:
            return (self.a > 0) - (self.a < 0)
        if not self.a:
            return (self.b > 0) - (self.b < 0)
        if (self.a > 0) == (self.b > 0):
            return (self.a > 0) - (self.a < 0)
        gap = self.a * self.a - self.radicand * self.b * self.b
        return ((gap > 0) - (gap < 0)) * ((self.a > 0) - (self.a < 0))


def multiple_full_span_far_move_check():
    q = Biquad.lift
    s = Biquad((Fraction(0), Fraction(1), Fraction(0), Fraction(0)))
    t = Biquad((Fraction(0), Fraction(0), Fraction(1), Fraction(0)))
    points = {
        "v": (q(0), q(0)), "pm": (q(12), q(-5)), "pp": (q(12), q(5)),
        "L1": (q(6), -s), "U1": (q(6), s),
        "L2": (q(7), -s), "U2": (q(7), s),
        "L3": (q(8), s - t), "U3": (q(8), t - s),
    }
    layers = {"v": 0, "L1": 0, "U1": 0, "L2": 1, "U2": 1,
              "L3": 2, "U3": 2, "pm": 2, "pp": 2}
    full = [("v", "pm"), ("v", "pp"), ("L1", "U3"), ("U1", "L3")]
    proper = [("L1", "U2"), ("U1", "L2")]
    contacts = {frozenset(e) for e in (("L1", "L2"), ("U1", "U2"))}
    actual_full = {frozenset(e) for e in full}
    actual_diameters = actual_full | {frozenset(e) for e in proper}
    for a, b in combinations(points, 2):
        old2 = dot(sub(points[b], points[a]), sub(points[b], points[a]))
        assert (old2 - 1).sign() >= 0 and (old2 - 169).sign() <= 0
        assert ((old2 - 1).sign() == 0) == (frozenset((a, b)) in contacts)
        assert ((old2 - 169).sign() == 0) == (frozenset((a, b)) in actual_diameters)
    rows = []
    for a, b in full + proper:
        r = sub(points[b], points[a])
        rows.append([r[1] if layers[a] < i <= layers[b] else q(0) for i in (1, 2)])
    assert all(sum(row[i] for row in rows).sign() == 0 for i in range(2))
    assert det(rows[0], rows[-1]).sign() != 0

    # Extrema (2,t) and (-2,t), not just the star directions (+/-12,5).
    assert det((q(1), t), (q(-1), t)).sign() > 0
    ignored_delta = (q(Fraction(-2, 5)), q(Fraction(-4, 5)))
    for a, b in full[:2]:
        r = tuple(x + y for x, y in zip(sub(points[b], points[a]), ignored_delta))
        assert (dot(r, r) - 169).sign() < 0
    r = tuple(x + y for x, y in zip(sub(points["L3"], points["U1"]), ignored_delta))
    assert (dot(r, r) - 169).sign() > 0

    # Exterior coordinate 2 affects every full-span row and no proper row.
    delta = (q(-2), q(0))  # w=-u, strict interior of the all-row far arc.
    moved = {name: tuple(x + y for x, y in zip(point, delta)) if layers[name] == 2 else point
             for name, point in points.items()}
    for a, b in full:
        r = sub(moved[b], moved[a])
        assert (dot(r, r) - 169).sign() < 0
    for a, b in proper:
        r = sub(moved[b], moved[a])
        assert (dot(r, r) - 169).sign() == 0
    violations = set()
    for a, b in combinations(points, 2):
        r = sub(moved[b], moved[a])
        new2 = dot(r, r)
        assert (new2 - 169).sign() <= 0
        if frozenset((a, b)) in contacts:
            assert (new2 - 1).sign() == 0
        if (new2 - 1).sign() < 0:
            violations.add(frozenset((a, b)))
            old = sub(points[b], points[a])
            assert (dot(old, old) - 1).sign() > 0
            assert (dot(old, old) - 9).sign() < 0  # 1<old distance<1+q, q=2.
    assert violations == {frozenset(e) for e in (("L1", "L3"), ("U1", "U3"))}
    return {"vertices": 9, "m": 2, "full_span_rows": 4, "proper_rows": 2,
            "all_row_phase": "pi", "old_contacts_preserved": True,
            "all_old_diameters_feasible": True, "inactive_unit_blockers": 2,
            "witness_only_phase_counterexample": ["3/5", "-4/5"],
            "actual_train_cut_and_global_optimality": "not encoded"}


def contact_rule_boundary_check(parameter):
    # Rational unit vector (a,x), and its reflection (a,-x).
    h = Fraction(13)
    a = (1 - parameter * parameter) / (1 + parameter * parameter)
    x = 2 * parameter / (1 + parameter * parameter)
    assert a * a + x * x == 1
    diameter2 = h * h + a * a
    y = (h + x) / 2
    radicand = diameter2 - (h - x) ** 2 / 4
    q = lambda value: Quadratic(radicand, Fraction(value))
    z = Quadratic(radicand, Fraction(0), Fraction(1))
    points = {"v": (q(a) - z, q(y)), "A": (q(0), q(0)),
              "C": (q(a), q(x)), "B": (q(a), q(h)), "E": (q(0), q(h + x))}
    hull = ["v", "A", "C", "B", "E"]
    for p, r in zip(hull, hull[1:] + hull[:1]):
        for other in hull:
            if other not in (p, r):
                assert det(sub(points[r], points[p]), sub(points[other], points[p])).sign() > 0
    contacts = {frozenset(e) for e in (("A", "C"), ("E", "B"))}
    edges = [("v", "B"), ("v", "C"), ("A", "B"), ("E", "C")]
    diameters = {frozenset(e) for e in edges}
    for p, r in combinations(points, 2):
        vector = sub(points[r], points[p])
        length2 = dot(vector, vector)
        assert (length2 - 1).sign() >= 0 and (length2 - diameter2).sign() <= 0
        assert ((length2 - 1).sign() == 0) == (frozenset((p, r)) in contacts)
        assert ((length2 - diameter2).sign() == 0) == (frozenset((p, r)) in diameters)
    assert (h - x) ** 2 < diameter2  # Common bracing-star opening < pi/3.
    beta = Fraction(1, 4)
    result = tuple(sum(beta * sub(points[r], points[p])[i] for p, r in edges) for i in (0, 1))
    assert result[1].sign() == 0 and result[0].sign() > 0
    alpha = (z + a) * (Fraction(1) / (4 * a))
    contact_result = tuple(alpha * (sub(points["C"], points["A"])[i]
                                   + sub(points["B"], points["E"])[i]) for i in (0, 1))
    assert all((contact_result[i] - result[i]).sign() == 0 for i in (0, 1))
    assert result[0].sign() > 0  # Aggregate positive contact-cut balance holds.
    transformed_det = 2 * h * (a - 1)
    levels = {"v": 0, "A": 0, "E": 0, "B": 1, "C": 1}
    if parameter:
        assert transformed_det < 0
        assert x != 0 and a != 1
        delta = (q(Fraction(-2, 5)), q(Fraction(-4, 5)))
        ac = tuple(v + d for v, d in zip(sub(points["C"], points["A"]), delta))
        assert (dot(ac, ac) - 1).sign() < 0  # Aggregate law does not preserve contacts.
        kind = "empty"
        singleton_endpoint = "not applicable"
    else:
        assert transformed_det == 0 and a == 1 and x == 0
        # The only nonzero phase is pi. Old contacts are genuinely u-directed.
        moved = {name: (point[0] - 2, point[1]) if levels[name] else point
                 for name, point in points.items()}
        new_contacts, new_diameters = set(), set()
        for p, r in combinations(points, 2):
            vector = sub(moved[r], moved[p])
            length2 = dot(vector, vector)
            assert (length2 - 1).sign() >= 0 and (length2 - diameter2).sign() <= 0
            if (length2 - 1).sign() == 0:
                new_contacts.add(frozenset((p, r)))
            if (length2 - diameter2).sign() == 0:
                new_diameters.add(frozenset((p, r)))
        assert new_contacts == contacts
        assert new_diameters == {frozenset(e) for e in (("A", "B"), ("E", "C"))}
        kind = "singleton"
        singleton_endpoint = "feasible; diameter count 4 -> 2"
    return {"vertices": 5, "source_pairs": 10, "rational_parameter": str(parameter),
            "contact_vector_a": str(a), "contact_vector_x": str(x),
            "diameter_squared": str(diameter2), "far_arc": kind,
            "transformed_determinant": str(transformed_det),
            "projected_balance_and_aggregate_contact_cut_law": True,
            "near_unit_pairs_are_already_unit": True,
            "edgewise_u_contact_rule": parameter == 0,
            "singleton_endpoint": singleton_endpoint,
            "full_source_KKT_and_global_optimality": "not encoded; v is contact-isolated"}


def main():
    print(json.dumps({"exact_geometric_checks": [geometric_check(p, c)
                      for p, c in product((False, True), repeat=2)],
                      "directed_cycle_order_check": simple_cycle_order_check(),
                      "multiple_full_span_far_move": multiple_full_span_far_move_check(),
                      "contact_rule_boundary_checks": [contact_rule_boundary_check(t)
                       for t in (Fraction(1, 100), Fraction(0))]}, indent=2))


if __name__ == "__main__":
    main()
