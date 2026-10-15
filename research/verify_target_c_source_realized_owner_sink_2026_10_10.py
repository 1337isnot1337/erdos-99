#!/usr/bin/env python3
"""Exact full-source owner-sink regression; no canonical-source/globality claim.

Requires SymPy. Construction and certificates use rational arithmetic and certified
rational square-root intervals. Float arithmetic is not used in verification.
"""

import argparse
import json
import math
from fractions import Fraction
from functools import lru_cache
from itertools import pairwise

import sympy as S


class Source:
    def __init__(self, H=30):
        self.H = H
        self.pts = []
        self.owners = []
        self.names = []
        self.edges = set()
        self.strips = []
        tj = S.Rational(1, 100 * H * H)
        ti = 3 * tj
        self.a = [(1 - t * t) / (1 + t * t) for t in [ti, tj]]
        self.delta = [4 * t / (1 + t * t) for t in [ti, tj]]

    def point(self, p, owner=0, name=""):
        p = tuple(map(S.sympify, p))
        for k, q in enumerate(self.pts):
            if p == q:
                assert self.owners[k] == owner, (name, self.names[k])
                return k
        self.pts.append(p)
        self.owners.append(owner)
        self.names.append(name)
        return len(self.pts) - 1

    def edge(self, a, b):
        self.edges.add(tuple(sorted([a, b])))

    def path(self, ps, label):
        ids = [self.point(p, 0, label + str(k)) for k, p in enumerate(ps)]
        for a, b in pairwise(ids):
            self.edge(a, b)
        return ids

    def strip(self, p, owner, side, levels, label):
        a = self.a[owner - 1]
        d = self.delta[owner - 1]
        moving = []
        fixed = []
        for j in levels:
            moving.append(self.point((p[0], p[1] + j), owner, label + "m" + str(j)))
            fixed.append(
                self.point((p[0] + side * a, p[1] + d / 2 + j), 0, label + "f" + str(j))
            )
        for k in range(len(levels)):
            self.edge(moving[k], fixed[k])
            if k:
                self.edge(moving[k - 1], moving[k])
                self.edge(fixed[k - 1], fixed[k])
        self.strips.append((moving, fixed, label))
        return moving, fixed

    def cap(self, A, B, side, label):
        # Two unit sides joining endpoints with distance in (0,2).
        r = S.Matrix(B) - S.Matrix(A)
        l2 = r.dot(r)
        assert 1 < l2 < 4, (label, l2)
        h = S.sqrt(1 / l2 - S.Rational(1, 4))
        mid = (S.Matrix(A) + S.Matrix(B)) / 2 + side * h * S.Matrix([-r[1], r[0]])
        return self.path([A, tuple(mid), B], label)

    def straight_cap(self, A, B, side, label):
        # A and B have equal heights. Walk toward B, then cap residual in [1,2).
        r = S.Matrix(B) - S.Matrix(A)
        l2 = r.dot(r)
        n = math.isqrt(int(S.floor(l2))) - 1
        assert n >= 0 and (n + 1) ** 2 <= l2 < (n + 2) ** 2
        u = r / S.sqrt(r.dot(r))
        ps = [tuple(S.Matrix(A) + k * u) for k in range(n + 1)]
        self.path(ps, label + "straight")
        return self.cap(ps[-1], B, side, label + "cap")

    def rect(self, A, B, side, extent, label):
        # Horizontal arms of integer length extent and vertical column ending in cap.
        A = S.Matrix(A)
        B = S.Matrix(B)
        aa = A + S.Matrix([side * extent, 0])
        bb = B + S.Matrix([side * extent, 0])
        self.path(
            [tuple(A + S.Matrix([side * k, 0])) for k in range(extent + 1)],
            label + "armA",
        )
        self.path(
            [tuple(B + S.Matrix([side * k, 0])) for k in range(extent + 1)],
            label + "armB",
        )
        dy = bb[1] - aa[1]
        n = int(S.floor(dy)) - 1
        assert n >= 0
        ps = [tuple(aa + S.Matrix([0, k])) for k in range(n + 1)]
        self.path(ps, label + "vertical")
        # cap bends to outside of the rectangular path
        self.cap(ps[-1], tuple(bb), -side, label + "cap")

    def build(self):
        di, dj = self.delta
        Lm, Lf = self.strip((-5, 0), 1, 1, range(3), "L")
        Rm, Rf = self.strip((5, 0), 2, -1, range(3), "R")
        e1 = di - dj / 2
        e2 = dj / 2
        Am, Af = self.strip((0, 4), 1, -1, range(-2, 1), "A")
        Bm, Bf = self.strip((0, 5 + e1), 2, -1, range(3), "B")
        self.cap(self.pts[Af[-1]], self.pts[Bf[0]], 1, "AB")
        Cm, Cf = self.strip((0, 11), 2, 1, range(-2, 1), "C")
        Dm, Df = self.strip((0, 12 + e2), 1, 1, range(3), "D")
        self.cap(self.pts[Cf[-1]], self.pts[Df[0]], -1, "CD")
        d = 1 - dj * dj / 4
        Em, Ef = self.strip((0, 18), 1, -1, range(3), "E")
        Fm, Ff = self.strip((d, 18 + di - dj), 2, 1, range(3), "F")
        a = S.Matrix(self.pts[Ef[0]]) - S.Matrix([0, 1])
        b = S.Matrix(self.pts[Ff[0]]) - S.Matrix([0, 1])
        r = b - a
        l2 = r.dot(r)
        h = S.sqrt(1 / l2 - S.Rational(1, 16))
        step = r / 4 - h * S.Matrix([-r[1], r[0]])
        self.path(
            [
                self.pts[Ef[0]],
                tuple(a),
                tuple(a + step),
                tuple(a + 2 * step),
                tuple(b + step - r / 2),
                tuple(b),
                self.pts[Ff[0]],
            ],
            "EF",
        )
        self.straight_cap(self.pts[Lf[-1]], self.pts[Af[0]], -1, "LA")
        # R vertical six, then horizontal-left cap to lower C anchor
        rr = S.Matrix(self.pts[Rf[-1]])
        self.path([tuple(rr + S.Matrix([0, k])) for k in range(8)], "RCvert")
        self.straight_cap(tuple(rr + S.Matrix([0, 7])), self.pts[Cf[0]], 1, "RC")
        self.rect(self.pts[Bf[-1]], self.pts[Ef[-1]], -1, 2, "BE")
        self.rect(self.pts[Df[-1]], self.pts[Ff[-1]], 1, 3, "DF")
        ff = S.Matrix(self.pts[Ff[-1]])
        self.path([tuple(ff + S.Matrix([0, k])) for k in range(3)], "FQvert")
        ftop = ff + S.Matrix([0, 2])
        fl = ftop - S.Matrix([1, 0])
        self.path([tuple(ftop), tuple(fl)], "FQleft")
        self.cap(tuple(fl), (0, 22), 1, "FQcap")
        q = self.path([(0, k) for k in range(22, self.H + 1)], "Q")[-1]
        self.special = [(Am[-1], Bm[0]), (Cm[-1], Dm[0]), (Em[0], Fm[0])]
        self.diameter = [tuple(sorted([q, Lm[0]])), tuple(sorted([q, Rm[0]]))]
        return self


PRECISION = 120


def interval_add(a, b):
    return a[0] + b[0], a[1] + b[1]


def interval_mul(a, b):
    z = [x * y for x in a for y in b]
    return min(z), max(z)


def interval_square(a):
    if a[0] <= 0 <= a[1]:
        return Fraction(0), max(a[0] * a[0], a[1] * a[1])
    return min(a[0] * a[0], a[1] * a[1]), max(a[0] * a[0], a[1] * a[1])


def sqrt_rational_bounds(x):
    assert x >= 0
    scale = 1 << PRECISION
    k = math.isqrt((x.numerator * scale * scale) // x.denominator)
    lo = Fraction(k, scale)
    assert lo * lo <= x
    if lo * lo == x:
        return lo, lo
    hi = Fraction(k + 1, scale)
    assert x < hi * hi
    return lo, hi


@lru_cache(None)
def enclosure(expr):
    if expr.is_Rational:
        q = Fraction(int(expr.p), int(expr.q))
        return q, q
    if expr.is_Add:
        out = (Fraction(0), Fraction(0))
        for x in expr.args:
            out = interval_add(out, enclosure(x))
        return out
    if expr.is_Mul:
        out = (Fraction(1), Fraction(1))
        for x in expr.args:
            out = interval_mul(out, enclosure(x))
        return out
    if expr.is_Pow:
        base, exponent = expr.args
        a = enclosure(base)
        if exponent == S.Rational(1, 2):
            return sqrt_rational_bounds(a[0])[0], sqrt_rational_bounds(a[1])[1]
        if exponent == -1:
            assert not a[0] <= 0 <= a[1]
            return Fraction(1, a[1]), Fraction(1, a[0])
        if exponent == -S.Rational(1, 2):
            b = enclosure(S.sqrt(base))
            assert b[0] > 0
            return Fraction(1, b[1]), Fraction(1, b[0])
        if exponent == 2:
            return interval_square(a)
    raise ValueError("unsupported expression: " + str(expr))


def squared_distance(a, b):
    return interval_add(
        interval_square((a[0][0] - b[0][1], a[0][1] - b[0][0])),
        interval_square((a[1][0] - b[1][1], a[1][1] - b[1][0])),
    )


def component_count(n, edges):
    adjacency = [set() for _ in range(n)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen = set(range(n))
    count = 0
    while unseen:
        count += 1
        stack = [unseen.pop()]
        while stack:
            for x in adjacency[stack.pop()]:
                if x in unseen:
                    unseen.remove(x)
                    stack.append(x)
    return count, adjacency


def verify(H, amplitude_repair=False, common_system=False):
    amplitude_repair = amplitude_repair or common_system
    assert H >= 30
    source = Source(H).build()
    n = len(source.pts)
    D2 = H * H + 25
    assert n == H + 79
    di, dj = source.delta
    assert di > 2 * dj > 0
    # di < D-sqrt(D^2-1) without approximating either square root.
    assert 2 * enclosure(S.sqrt(D2))[1] * Fraction(di) < 1
    assert di < Fraction(1, 1000)
    components, adj = component_count(n, source.edges)
    assert components == 1
    assert all(not (adj[a] & adj[b]) for a, b in source.edges)
    old_diameters = set(source.diameter)
    checks = 0
    bad_by_pair = {}
    common_bad_by_pair = {}
    min_strict = Fraction(1)
    upper_margin = Fraction(1)
    refined_endpoint = set(source.strips[0][0] + source.strips[1][0])
    endpoint_D2 = D2 - 2 * H * dj + dj * dj
    endpoint_diameter = source.diameter[1]
    amplitude_D2 = D2 - 4 * H * dj + 4 * dj * dj
    common_D2 = D2 - 4 * H * di + 4 * di * di
    released_contacts = {5: 0, 6: 0}
    for state in range(9 if common_system else 7 if amplitude_repair else 5):
        symbolic = []
        boxes = []
        for index, (p, owner) in enumerate(zip(source.pts, source.owners)):
            if state in (6, 7, 8):
                common_moved = bool(owner and (state == 6 or owner == state - 6))
                dy = 2 * di if common_moved else S.Integer(0)
            elif state == 5:
                dy = source.delta[owner - 1] * owner if owner else S.Integer(0)
            else:
                moved = (
                    index in refined_endpoint
                    if state == 4
                    else bool(owner and state & (1 << (owner - 1)))
                )
                dy = source.delta[owner - 1] if moved else S.Integer(0)
            q = (p[0], p[1] + dy)
            symbolic.append(q)
            boxes.append(tuple(enclosure(x) for x in q))
        for a in range(n):
            for b in range(a + 1, n):
                checks += 1
                pair = (a, b)
                bounds = squared_distance(boxes[a], boxes[b])
                if pair in source.edges:
                    qa, qb = symbolic[a], symbolic[b]
                    target = S.Integer(1)
                    if state >= 5 and source.owners[a] != source.owners[b]:
                        owner = source.owners[a] or source.owners[b]
                        assert not (source.owners[a] and source.owners[b])
                        shift = (
                            (
                                2 * di
                                if state == 6 or owner == state - 6
                                else S.Integer(0)
                            )
                            if state in (6, 7, 8)
                            else owner * source.delta[owner - 1]
                        )
                        target += shift * (shift - source.delta[owner - 1])
                        assert target >= 1
                        if target > 1 and state in released_contacts:
                            released_contacts[state] += 1
                    assert (
                        S.simplify((qa[0] - qb[0]) ** 2 + (qa[1] - qb[1]) ** 2 - target)
                        == 0
                    )
                elif bounds[1] < 1:
                    ledger = common_bad_by_pair if state in (7, 8) else bad_by_pair
                    ledger.setdefault(pair, []).append(state)
                else:
                    assert bounds[0] > 1, (
                        H,
                        state,
                        "uncertified lower",
                        source.names[a],
                        source.names[b],
                        bounds,
                    )
                    min_strict = min(min_strict, bounds[0] - 1)
                if pair in old_diameters:
                    mover = source.owners[a] or source.owners[b]
                    if state in (7, 8):
                        moved = mover == state - 6
                    elif state >= 5:
                        moved = True
                    elif state == 4:
                        moved = bool(set(pair) & refined_endpoint)
                    else:
                        moved = bool(state & (1 << (mover - 1)))
                    assert bounds[1] < D2 if moved else bounds == (D2, D2)
                else:
                    assert bounds[1] < D2, (
                        H,
                        state,
                        "upper",
                        source.names[a],
                        source.names[b],
                    )
                    upper_margin = min(upper_margin, D2 - bounds[1])
                if state == 4:
                    assert (
                        bounds == (endpoint_D2, endpoint_D2)
                        if pair == endpoint_diameter
                        else bounds[1] < endpoint_D2
                    )
                if state == 5:
                    assert (
                        bounds == (amplitude_D2, amplitude_D2)
                        if pair == endpoint_diameter
                        else bounds[1] < amplitude_D2
                    )
                if state == 6:
                    assert (
                        bounds == (common_D2, common_D2)
                        if pair in old_diameters
                        else bounds[1] < common_D2
                    )
    expected = {
        tuple(sorted(source.special[0])): [1],
        tuple(sorted(source.special[1])): [2],
    }
    Em, Fm = source.strips[6][0], source.strips[7][0]
    for a, b in zip(Em, Fm):
        expected[tuple(sorted([a, b]))] = [3]
    assert bad_by_pair == expected, (H, bad_by_pair, expected)
    # Exactly eight owner components; every train has two strict rhombi and
    # three cut contacts. Removing all 24 cut contacts gives nine core regions.
    cuts = set()
    for moving, fixed, label in source.strips:
        assert len(moving) == len(fixed) == 3
        cuts.update(tuple(sorted([a, b])) for a, b in zip(moving, fixed))
        for rows in [moving, fixed]:
            assert all(tuple(sorted([a, b])) in source.edges for a, b in pairwise(rows))
    count, _ = component_count(n, source.edges - cuts)
    assert count == 9
    # Neither singleton is lower-feasible; all-one fails three physical conflicts.
    assert {s for states in bad_by_pair.values() for s in states} == {1, 2, 3}
    # Exact full-source construction of a better packing, proving nonglobality.
    width = math.isqrt(n - 1) + 1
    assert width * width >= n and 2 * (width - 1) ** 2 < D2
    result = {
        "H": H,
        "vertices": n,
        "contacts": len(source.edges),
        "diameter_squared": D2,
        "actual_diameter_pairs": 2,
        "trains": 8,
        "refined_owner_components": 8,
        "full_pair_state_checks": checks,
        "refined_endpoint_diameter_squared": str(endpoint_D2),
        "refined_endpoint_strict_sub_D": True,
        "forbidden_lower_states": {
            source.names[a] + ":" + source.names[b]: v
            for (a, b), v in bad_by_pair.items()
        },
        "minimum_certified_positive_lower_margin": str(min_strict),
        "minimum_certified_inactive_upper_margin": str(upper_margin),
        "small_cloud_gamma_D_check": True,
        "triangle_free": True,
        "connected": True,
        "positive_KKT_claim": False,
        "global_minimizer": False,
    }
    if amplitude_repair:
        assert released_contacts == {5: 12, 6: 24}
        assert 4 * enclosure(S.sqrt(D2))[1] * Fraction(di) < 1
        result.update(
            {
                "amplitude_repair_diameter_squared": str(amplitude_D2),
                "amplitude_repair_contacts_removed": 12,
                "common_release_diameter_squared": str(common_D2),
                "common_release_contacts_removed": 24,
                "all_repair_noncontacts_strict": True,
                "common_release_cloud_below_gamma_D": True,
            }
        )
    if common_system:
        expected_common = {
            tuple(sorted(source.special[0])): [7],
            tuple(sorted(source.special[1])): [8],
        }
        assert common_bad_by_pair == expected_common
        # Actual full-pair witnesses give A=>B and B=>A; there is no unary.
        # Thus the maximal common-translation model is (A,B)=(1,1).
        result.update(
            {
                "common_implication_witnesses": {
                    source.names[a] + ":" + source.names[b]: [
                        "A=>B" if state == 7 else "B=>A" for state in states
                    ]
                    for (a, b), states in common_bad_by_pair.items()
                },
                "common_unary_blockers": 0,
                "common_maximal_feasible_model": [1, 1],
            }
        )
    return result


class SymbolicSource(Source):
    def __init__(self, H=30, parameter=None):
        super().__init__(H)
        parameter = t if parameter is None else parameter
        self.a = [(1 - z * z) / (1 + z * z) for z in [3 * parameter, parameter]]
        self.delta = [4 * z / (1 + z * z) for z in [3 * parameter, parameter]]

    def cap(self, A, B, side, label):
        r = S.Matrix(B) - S.Matrix(A)
        l2 = r.dot(r)
        h = S.sqrt(1 / l2 - S.Rational(1, 4))
        mid = (S.Matrix(A) + S.Matrix(B)) / 2 + side * h * S.Matrix([-r[1], r[0]])
        return self.path([A, tuple(mid), B], label)

    def straight_cap(self, A, B, side, label):
        v = S.Matrix([1 if label == "LA" else -1, 0])
        ps = [tuple(S.Matrix(A) + k * v) for k in range(3)]
        self.path(ps, label + "straight")
        return self.cap(ps[-1], B, side, label + "cap")

    def rect(self, A, B, side, extent, label):
        A = S.Matrix(A)
        B = S.Matrix(B)
        aa = A + S.Matrix([side * extent, 0])
        bb = B + S.Matrix([side * extent, 0])
        self.path(
            [tuple(A + S.Matrix([side * k, 0])) for k in range(extent + 1)],
            label + "armA",
        )
        self.path(
            [tuple(B + S.Matrix([side * k, 0])) for k in range(extent + 1)],
            label + "armB",
        )
        n = 11 if label == "BE" else 5
        ps = [tuple(aa + S.Matrix([0, k])) for k in range(n + 1)]
        self.path(ps, label + "vertical")
        self.cap(ps[-1], tuple(bb), -side, label + "cap")


def verify_symbolic_limit(amplitude_repair=False):
    global t
    t = S.Symbol("t", positive=True)
    source = SymbolicSource().build()
    n = len(source.pts)
    assert n == 109
    p0 = [tuple(S.simplify(x.subs(t, 0)) for x in p) for p in source.pts]
    boxes = [tuple(enclosure(x) for x in p) for p in p0]
    critical = []
    strict_limit_checks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) in source.edges:
                continue
            bounds = squared_distance(boxes[i], boxes[j])
            if bounds[0] > 1:
                strict_limit_checks += 1
                continue
            assert bounds[0] <= 1 <= bounds[1]
            assert S.simplify(sum((x - y) ** 2 for x, y in zip(p0[i], p0[j])) - 1) == 0
            critical.append((i, j))
    assert len(critical) == 11
    rows = []
    for i, j in critical:
        terms = []
        for state in range(4):
            p = S.Matrix(source.pts[i])
            q = S.Matrix(source.pts[j])
            for index, v in [(i, p), (j, q)]:
                owner = source.owners[index]
                if owner and state & (1 << (owner - 1)):
                    v[1] += source.delta[owner - 1]
            expr = S.cancel((p - q).dot(p - q) - 1)
            numerator, denominator = S.fraction(expr)
            assert S.simplify(denominator.subs(t, 0)) > 0
            poly = S.Poly(numerator, t)
            power = min(power[0] for power, coefficient in poly.terms())
            coefficient = S.simplify(
                poly.coeff_monomial(t**power) / denominator.subs(t, 0)
            )
            assert coefficient != 0
            terms.append([power, str(coefficient)])
        rows.append(
            {
                "pair": source.names[i] + ":" + source.names[j],
                "leading_lower_slack": terms,
            }
        )
        if amplitude_repair:
            extra_terms = []
            for common in [False, True]:
                p = S.Matrix(source.pts[i])
                q = S.Matrix(source.pts[j])
                for index, v in [(i, p), (j, q)]:
                    owner = source.owners[index]
                    if owner:
                        v[1] += (
                            2 * source.delta[0]
                            if common
                            else owner * source.delta[owner - 1]
                        )
                expr = S.cancel((p - q).dot(p - q) - 1)
                numerator, denominator = S.fraction(expr)
                denominator_at_zero = S.simplify(denominator.subs(t, 0))
                assert denominator_at_zero > 0
                poly = S.Poly(numerator, t)
                power = min(power[0] for power, _ in poly.terms())
                coefficient = S.simplify(
                    poly.coeff_monomial(t**power) / denominator_at_zero
                )
                assert coefficient > 0
                extra_terms.append([power, str(coefficient)])
            rows[-1]["amplitude_and_common_repair_leading_slacks"] = extra_terms
    # All eleven critical-pair leading signs agree with the exact fixtures.
    expected_bad = {
        source.names[i] + ":" + source.names[j]: v
        for (i, j), v in [
            (tuple(sorted(source.special[0])), [1]),
            (tuple(sorted(source.special[1])), [2]),
        ]
    }
    for i, j in zip(source.strips[6][0], source.strips[7][0]):
        expected_bad[source.names[i] + ":" + source.names[j]] = [3]
    for row in rows:
        assert [
            k
            for k, term in enumerate(row["leading_lower_slack"])
            if S.Rational(term[1]) < 0
        ] == expected_bad.get(row["pair"], [])
    # The limiting low cluster is contained in [-5,5] x [0,22]. For small t
    # it is in [-6,6] x [0,23]. Points below height 1 are bottom-strip points
    # with absolute x <= 5, so the report's uniform upper proof applies.
    assert all(enclosure(p[0])[0] >= -5 and enclosure(p[0])[1] <= 5 for p in p0)
    assert all(enclosure(p[1])[0] >= 0 and enclosure(p[1])[1] <= 30 for p in p0)
    for label, p in zip(source.names, p0):
        if p[1] > 22:
            assert p[0] == 0 and label.startswith("Q")
        if p[1] < 1:
            assert label in {"Lm0", "Lf0", "Rm0", "Rf0"} and abs(p[0]) <= 5
    return {
        "symbolic_limit_noncontact_pairs": n * (n - 1) // 2 - len(source.edges),
        "strict_limit_noncontact_pairs": strict_limit_checks,
        "critical_pairs": rows,
        "classification": "asymptotic family proof support",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--heights", nargs="+", type=int, default=[30, 31, 100])
    parser.add_argument("--symbolic-limit", action="store_true")
    parser.add_argument("--amplitude-repair", action="store_true")
    parser.add_argument("--common-implication-system", action="store_true")
    args = parser.parse_args()
    for H in args.heights:
        print(
            json.dumps(
                verify(H, args.amplitude_repair, args.common_implication_system),
                sort_keys=True,
            )
        )
    if args.symbolic_limit:
        print(
            json.dumps(
                verify_symbolic_limit(
                    args.amplitude_repair or args.common_implication_system
                ),
                sort_keys=True,
            )
        )
