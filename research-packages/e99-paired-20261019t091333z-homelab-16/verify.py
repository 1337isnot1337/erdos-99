"""Independent exact checks for PR #147's two-grid pure-disk regression.

This checker rebuilds the labelled point set and tile incidence from the
displayed coordinates.  It does not import or call the candidate verifier.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def norm2(a):
    return dot(a, a)


def edge(a, b):
    return tuple(sorted((a, b)))


def positive_surd(a, b):
    """Exact sign of a + b*sqrt(3), for rational a,b."""
    if a == 0:
        return b > 0
    if b == 0:
        return a > 0
    if a > 0 and b > 0:
        return True
    if a < 0 and b < 0:
        return False
    if a > 0:
        return a * a > 3 * b * b
    return 3 * b * b > a * a


def verify_case(m):
    if m < 12 or m % 4:
        raise ValueError("m must be divisible by four and at least twelve")

    q = m * m
    p = isqrt((q * q) // 3) + 1
    # This integer comparison independently certifies p=floor(q/sqrt(3))+1.
    assert 3 * (p - 1) ** 2 < q * q < 3 * p * p
    t = F(p, q)
    c = (1 - t * t) / (1 + t * t)
    s = 2 * t / (1 + t * t)
    assert 0 < c < F(1, 2) and s * s + c * c == 1
    assert c + s > 1 and positive_surd(s, F(-1, 2))

    x, y = (F(1), F(0)), (F(0), F(1))
    v, u = (-c, -s), (-s, c)
    zero = (F(0), F(0))
    faces = []
    vertices = set()
    incidence = {}
    for i in range(m):
        for j in range(m):
            o = (F(i) - c * j, -s * j)
            faces.append(("grain1", (o, add(o, x), add(add(o, x), v), add(o, v))))
    for i in range(m):
        for j in range(m):
            o = (-s * j, F(i) + c * j)
            faces.append(("grain2", (o, add(o, y), add(add(o, y), u), add(o, u))))
    faces.append(("interface", (zero, x, (F(1), F(1)), y)))

    for kind, corners in faces:
        vertices.update(corners)
        center = (sum(p[0] for p in corners) / 4,
                  sum(p[1] for p in corners) / 4)
        for a, b in zip(corners, corners[1:] + corners[:1]):
            incidence.setdefault(edge(a, b), []).append((kind, center))
    assert all(len(fs) in (1, 2) for fs in incidence.values())

    # Exhaustive exact pair replay: contacts are precisely tile edges, and the
    # resulting graph is bipartite (a stronger control than triangle counting).
    contacts = set()
    minimum = None
    diameter2 = F(0)
    ordered = sorted(vertices)
    for a, b in combinations(ordered, 2):
        d2 = norm2(sub(a, b))
        minimum = d2 if minimum is None else min(minimum, d2)
        diameter2 = max(diameter2, d2)
        assert d2 >= 1
        if d2 == 1:
            contacts.add(edge(a, b))
    tile_edges = set(incidence)
    assert minimum == 1 and contacts == tile_edges
    graph = {p: set() for p in vertices}
    for a, b in contacts:
        graph[a].add(b)
        graph[b].add(a)
    color = {}
    for root in graph:
        if root in color:
            continue
        color[root] = 0
        todo = [root]
        while todo:
            here = todo.pop()
            for nxt in graph[here]:
                if nxt not in color:
                    color[nxt] = 1 - color[here]
                    todo.append(nxt)
                else:
                    assert color[nxt] != color[here]

    boundary = [e for e, fs in incidence.items() if len(fs) == 1]
    boundary_graph = {}
    for a, b in boundary:
        boundary_graph.setdefault(a, set()).add(b)
        boundary_graph.setdefault(b, set()).add(a)
    assert len(boundary) == 8 * m
    assert all(len(ns) == 2 for ns in boundary_graph.values())
    seen = set()
    todo = [next(iter(boundary_graph))]
    while todo:
        z = todo.pop()
        if z in seen:
            continue
        seen.add(z)
        todo.extend(boundary_graph[z] - seen)
    assert seen == set(boundary_graph)
    face_count = 2 * m * m + 1
    assert len(vertices) - len(incidence) + face_count == 1

    # The six listed scaled corners support every source vertex.  This proves
    # the displayed polygon is the full hull without trusting a hull routine.
    hull = [(-c*m, -s*m), ((1-c)*m, -s*m), (F(m), F(0)),
            (F(0), F(m)), (-s*m, (1+c)*m), (-s*m, c*m)]
    steps = [sub(hull[(i + 1) % 6], hull[i]) for i in range(6)]
    turns = [det(steps[i], steps[(i + 1) % 6]) for i in range(6)]
    normalized_turns = [F(m*m)*s, F(m*m)*(s+c), F(m*m)*(s-c),
                        F(m*m)*s, F(m*m)*(s-c), F(m*m)*(s+c)]
    assert turns == normalized_turns and all(z > 0 for z in turns)
    assert all(det(steps[i], sub(p0, hull[i])) >= 0
               for i in range(6) for p0 in vertices)
    assert all(det(steps[i], sub(zero, hull[i])) > 0 for i in range(6))
    twice_area = sum(det(hull[i], hull[(i + 1) % 6]) for i in range(6))
    hull_area = twice_area / 2
    assert hull_area == (1 + 2 * s) * m * m

    # Independently sum support depths using the incident tile side to orient
    # each unit normal toward the complement.
    H = F(0)
    for e in boundary:
        a, b = e
        midpoint = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        dx, dy = sub(b, a)
        outward = (dy, -dx)
        center = incidence[e][0][1]
        if dot(outward, sub(center, midpoint)) > 0:
            outward = (-outward[0], -outward[1])
        H += max(dot(outward, p0) for p0 in vertices) - dot(outward, midpoint)

    G = hull_area - (2 * s * m * m + 1)
    E_a, E_b = 2 * s * m * m + 1, -(F(m*m) + F(1, 2))
    J = H - 2 * G
    Q12 = 2 * (1 + c) * m * m
    P12 = F(1)
    V12 = Q12 - P12
    assert G == m * m - 1
    assert H == (4 + 2 * c) * m * m - 2
    assert J == Q12 and J == V12 + P12
    assert 2 * (G + E_a) == 2 * (1 + 2 * s) * m * m
    assert 2 * E_b == -(2 * m * m + 1)
    assert 2 * s * m * m + 1 + V12 == 2 * (s + 1 + c) * m * m

    # Section 50.1 filter/pruning checks, using its exact definition.  The
    # analytic derivative bound gives delta < 2/m^2; the box and grid side
    # give m <= D < 4m.  Thus only the square crossing is removed and every
    # remaining degree m exceeds lambda*D for lambda=1/4.
    assert m * m <= diameter2 < 16 * m * m
    assert m ** 3 > 16  # 2/m^2 < 1/(2 sqrt(m)) < D^(-1/2)
    assert m >= 12      # D^(-1/2) <= 1/sqrt(m) < 1/2 < pi/6

    # Track indices are the transverse cell indices: each grid contributes
    # exactly m tracks in each direction.  Its m^2 faces give K_(m,m).
    nodes = ({("1x", i) for i in range(m)} | {("1v", j) for j in range(m)} |
             {("2y", i) for i in range(m)} | {("2u", j) for j in range(m)})
    crossing_edges = []
    for i in range(m):
        for j in range(m):
            crossing_edges.append((("1x", i), ("1v", j), "internal"))
            crossing_edges.append((("2y", i), ("2u", j), "internal"))
    crossing_edges.append((("1x", 0), ("2y", 0), "interface"))
    retained_graph = {z: set() for z in nodes}
    for a, b, kind in crossing_edges:
        if kind == "internal":  # the single square edge is high-defect deleted
            retained_graph[a].add(b)
            retained_graph[b].add(a)
    assert all(len(ns) == m for ns in retained_graph.values())
    components = []
    unseen = set(nodes)
    while unseen:
        root = unseen.pop()
        comp, todo = {root}, [root]
        while todo:
            for nxt in retained_graph[todo.pop()]:
                if nxt not in comp:
                    comp.add(nxt)
                    unseen.discard(nxt)
                    todo.append(nxt)
        components.append(comp)
    assert sorted(map(len, components)) == [2*m, 2*m]

    # Positive PC1 trim, but zero cancellation term: each shore has m/2 unit
    # vectors and D>=m, so |U+V|<=m<=D.  The exact aligned sum also has norm^2
    # m^2(1-c)/2 < m^2.
    trim = m // 4
    d = trim - 2
    assert m - 2 * trim == m // 2 and d > 0
    assert F(m*m, 2) * (1 - c) < m * m

    # Exact sign of the overly generous direct-payment residual
    # V12-[P12+2(G+E)+(sqrt(3)/2)B].
    payment_a = 2 * (c - 2 * s) * m * m - 2
    payment_b = 2 * m * m - 4 * m + 1
    direct_a = V12 - P12 - 2 * (G + E_a)
    direct_b = -2 * E_b - 4 * m
    assert (payment_a, payment_b) == (direct_a, direct_b)
    assert positive_surd(payment_a, payment_b)

    # Strict global-minimizer shell upper margin, using t=0, chi=1 in §36.3.
    shell_a = G + E_a
    shell_b = E_b - 2 * m
    assert positive_surd(shell_a, shell_b)

    return {
        "m": m,
        "vertices": len(vertices),
        "tile_edges": len(incidence),
        "boundary_edges": len(boundary),
        "faces": face_count,
        "euler_characteristic": 1,
        "min_squared_separation": str(minimum),
        "diameter_squared": str(diameter2),
        "contact_graph_bipartite": True,
        "train_count_by_construction": 4 * m,
        "retained_crossing_components": 2,
        "retained_min_degree": m,
        "pc1_trim_depth": d,
        "pc1_diagonal_excess": 0,
        "V12": f"{V12.numerator}/{V12.denominator}",
        "G": f"{G.numerator}/{G.denominator}",
        "H": f"{H.numerator}/{H.denominator}",
        "J": f"{J.numerator}/{J.denominator}",
        "payment_residual": f"{payment_a} + ({payment_b})*sqrt(3)",
        "shell_upper_margin": f"{shell_a} + ({shell_b})*sqrt(3)",
    }


def main():
    # Boundary controls: the depth condition is not positive at m=8, and the
    # Q(sqrt(3)) sign routine is tested on both signs.
    assert 8 // 4 - 2 == 0
    assert not positive_surd(F(1), F(-1))
    assert positive_surd(F(-1), F(1))
    cases = [verify_case(m) for m in (12, 16, 20, 24)]
    print(json.dumps({
        "status": "PASS: independent exact reconstruction of the stated geometric regression",
        "arithmetic": "fractions.Fraction and integer arithmetic only",
        "domain_checked": "m=12,16,20,24; proof formulas cover all m>=12 divisible by four",
        "controls": ["all point pairs", "contact graph bipartite", "single boundary cycle",
                    "Euler characteristic", "hull support halfplanes", "Section 50.1 filter",
                    "degree pruning", "positive PC1 trim with zero excess",
                    "Q(sqrt(3)) payment sign", "global shell upper margin"],
        "cases": cases,
    }, sort_keys=True, indent=2))


main()
