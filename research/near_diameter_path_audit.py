"""Exact finite audits for the 2026-09-09 diameter-lens/path report.

Run: python3 research/near_diameter_path_audit.py

Tests: a rational, triangle-free, arbitrarily nearly straight three-contact
equilibrium star; the sharp 15-degree lens example in Q(sqrt(3)); full-KKT
straight chains with explicit better competitors; and the five chord-incidence
types in C53.T (integer convex-parabola representatives).
No numerical arithmetic or third-party packages are used.

The star encodes unit separation, an actual diameter path and positive LOCAL
equilibrium. It omits global KKT equilibrium and global optimality. The chord
audit encodes convex order and intersections, not a unit-contact realization.
The universal geometric and matrix proofs are in the adjacent research report;
finite checks alone do not prove them or solve Erdos #99.
"""

from fractions import Fraction as F
from itertools import combinations


def distance2(p, q):
    return sum((x - y) ** 2 for x, y in zip(p, q))


def rational_star(t):
    c, s = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
    assert c * c + s * s == 1 and 0 < s < F(1, 2)
    points = ((-c, -s), (F(0), F(0)), (c, -s), (F(0), F(1)))
    pairs = {(i, j): distance2(points[i], points[j])
             for i, j in combinations(range(4), 2)}
    assert min(pairs.values()) == 1
    assert {e for e, d in pairs.items() if d == 1} == {(0, 1), (1, 2), (1, 3)}
    assert max(pairs.values()) == 4 * c * c == pairs[0, 2]
    assert all(d < pairs[0, 2] for e, d in pairs.items() if e != (0, 2))
    # Three vectors FROM the center, with positive local stress 1,1,2s.
    assert tuple(points[0][j] + points[2][j] + 2 * s * points[3][j]
                 for j in range(2)) == (0, 0)
    # For t <= 1/10 the path half-angle is strictly below 15 degrees:
    # tan(theta)=s/c < 1/4 < 2-sqrt(3).
    assert s / c < F(1, 4)
    # A unit square is a certified strictly smaller 4-point competitor.
    assert pairs[0, 2] > 2
    return pairs


# Q(sqrt(3)), represented as (rational, rational).
def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def mul(x, y):
    return x[0] * y[0] + 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def qdistance2(p, q):
    ds = [add(x, neg(y)) for x, y in zip(p, q)]
    return add(mul(ds[0], ds[0]), mul(ds[1], ds[1]))


def sharp_lens():
    zero, one = (F(0), F(0)), (F(1), F(0))
    half = (F(1, 2), F(0))
    # Diameter normalized to 1. Scaling by sqrt(2+sqrt(3)) makes the two
    # path edges unit. Work entirely with squared distances, so no extra field.
    z, a = (zero, zero), (one, zero)
    p = (half, (F(1), F(-1, 2)))
    y = (half, (F(0), F(-1, 2)))
    ds = [qdistance2(v, w) for v, w in combinations((z, a, p, y), 2)]
    short = (F(2), F(-1))
    assert ds.count(one) == 4 and ds.count(short) == 2
    scale2 = (F(2), F(1))
    assert mul(short, scale2) == one
    # tan(theta)=h/(1/2)=2-sqrt(3).
    assert mul((F(2), F(0)), p[1]) == short


def straight_chain(k):
    """L5 endpoint-term equality, with a strict rational L-shaped competitor.

    Encodes a full equilibrium with positive weights on every actual contact
    and diameter pair. Omits contact minimality and global optimality; the
    explicit competitor certifies that global optimality fails.
    """
    points = [(j, 0) for j in range(k + 1)]
    pairs = {(i, j): distance2(points[i], points[j])
             for i, j in combinations(range(k + 1), 2)}
    contacts = {e for e, d in pairs.items() if d == 1}
    assert contacts == {(j, j + 1) for j in range(k)}
    assert {e for e, d in pairs.items() if d == k * k} == {(0, k)}
    # alpha=k on each unit contact; beta=1 on the only diameter.
    for i, p in enumerate(points):
        contact_force = tuple(sum(k * (p[c] - points[j][c])
                                  for j in range(k + 1)
                                  if (min(i, j), max(i, j)) in contacts)
                              for c in range(2))
        other = k if i == 0 else 0 if i == k else None
        diameter_force = (0, 0) if other is None else tuple(
            p[c] - points[other][c] for c in range(2))
        assert contact_force == diameter_force
    boundary_edges = {e for e in contacts if 0 in e or k in e}
    assert k * len(boundary_edges) == 2 * k
    assert k * len(contacts - boundary_edges) == k * k - 2 * k
    competitor = [(0, 0)] + [(1, j) for j in range(k)]
    ds = [distance2(p, q) for p, q in combinations(competitor, 2)]
    assert min(ds) == 1 and max(ds) == 1 + (k - 1) ** 2 < k * k


def pentagon_cut_audit():
    """Exact rejection of the fetched pentagon's mixed-cut ordering.

    Angles are rational multiples of pi. The regular-pentagon chord i->j
    has angle 1/2+(i+j)/5 for i<j. No trigonometric computation is required.
    """
    edges = ((0, 2), (0, 3), (1, 3))  # e, f, g
    base_angles = [F(1, 2) + F(i + j, 5) for i, j in edges]
    assert base_angles == [F(9, 10), F(11, 10), F(13, 10)]
    for cut, expected_order, expected_z in (
            (F(0), (1, 2, 0), (1, 0, -1)),
            (F(-1, 2), (0, 1, 2), (1, 1, 0))):
        data = []
        for label, ((i, j), angle) in enumerate(zip(edges, base_angles)):
            turns = (angle - cut) // 1
            oriented_angle = angle - turns
            sign = -1 if turns % 2 else 1
            z = sign * (int(j == 0) - int(i == 0))  # head minus tail
            assert cut < oriented_angle < cut + 1
            data.append((oriented_angle, label, z))
        data.sort()
        assert tuple(item[1] for item in data) == expected_order
        z = tuple(item[2] for item in data)
        assert z == expected_z
        x, y, w = z
        assert w * (x - y) <= 0 and x * (w - y) <= 0
    # The alleged counterexample uses the x-positive orientation but the
    # [0,pi) order. Its directions are not increasing in its chosen half-plane.
    wrong_angles = (F(1, 10), F(3, 10), F(-1, 10))
    assert wrong_angles != tuple(sorted(wrong_angles))


def intersects(e, f):
    if set(e) & set(f):
        return True
    i, j = e
    k, l = f
    return (i < k < j < l) or (k < i < l < j)


def chord_types():
    patterns, checks = set(), 0
    # Three edges have at most six distinct endpoints. Testing all triples in
    # each size includes all five abstract incidence types.
    for n in range(3, 7):
        edges = list(combinations(range(n), 2))
        for triple in combinations(edges, 3):
            if not all(intersects(e, f) for e, f in combinations(triple, 2)):
                continue
            # For p_i=(i,i^2), an edge's forward slope is i+j.
            ordered = sorted(triple, key=lambda e: sum(e))
            assert len({sum(e) for e in ordered}) == 3
            for cut in range(3):
                # Rotate the projective cut; wrapped edges reverse direction.
                oriented = [(e, 1) for e in ordered[cut:]] + [
                    (e, -1) for e in ordered[:cut]]
                for start in range(n):
                    for length in range(n + 1):
                        interval = {(start + j) % n for j in range(length)}
                        z = tuple(sign * (int(j in interval) - int(i in interval))
                                  for (i, j), sign in oriented)
                        x, y, w = z
                        assert w * (x - y) <= 0 and x * (w - y) <= 0, (n, triple, z)
                        patterns.add(z)
                        checks += 1
    assert len(patterns) == 19
    return checks, sorted(patterns)


def main():
    for denominator in (10, 20, 100, 1000, 1000000):
        rational_star(F(1, denominator))
    sharp_lens()
    for k in (2, 3, 5, 10, 25):
        straight_chain(k)
    pentagon_cut_audit()
    count, patterns = chord_types()
    print("PASS: five exact rational nearly-straight degree-three local stars")
    print("PASS: sharp 15-degree four-point lens example in Q(sqrt(3))")
    print("PASS: five full-KKT straight chains saturate L5's endpoint term;")
    print("      explicit unit-separated L-shaped competitors beat every one")
    print("PASS: pentagon's alleged C53 violation mixes two different cuts;")
    print("      both consistently ordered orientations satisfy C53.T exactly")
    print(f"PASS: {count} exact chord/interval checks; {len(patterns)} signed triples")
    print("No global-optimality claim; the rational stars are beaten by a unit square.")


if __name__ == "__main__":
    main()
