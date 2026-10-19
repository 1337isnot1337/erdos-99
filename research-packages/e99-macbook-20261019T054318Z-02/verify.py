"""Exact rational checks for a scalable two-grain rhombic disk ledger."""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json


Point = tuple[F, F]
Vector = tuple[F, F]


def add(p: Point, q: Vector) -> Point:
    return p[0] + q[0], p[1] + q[1]


def scale(a: int | F, v: Vector) -> Vector:
    a = F(a)
    return a * v[0], a * v[1]


def dot(a: Vector, b: Vector) -> F:
    return a[0] * b[0] + a[1] * b[1]


def det(a: Vector, b: Vector) -> F:
    return a[0] * b[1] - a[1] * b[0]


def sqdist(a: Point, b: Point) -> F:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def positive_quadratic_surd(a: F, b: F) -> bool:
    """Decide exactly whether a+b*sqrt(3)>0 for rational a,b."""
    if a == 0:
        return b > 0
    if b == 0:
        return a > 0
    if a > 0 and b > 0:
        return True
    if a < 0 and b < 0:
        return False
    if a > 0:  # a - |b| sqrt(3)
        return a * a > 3 * b * b
    return 3 * b * b > a * a  # |b| sqrt(3) - |a|


def quadratic_surd_text(a: F, b: F) -> str:
    return f"{a} + ({b})*sqrt(3)"


def edge(a: Point, b: Point) -> tuple[Point, Point]:
    return tuple(sorted((a, b)))


class DSU:
    def __init__(self, items):
        self.parent = {item: item for item in items}

    def find(self, item):
        parent = self.parent[item]
        if parent != item:
            self.parent[item] = self.find(parent)
        return self.parent[item]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.parent[b] = a


def hull(points: set[Point]) -> list[Point]:
    pts = sorted(points)

    def turn(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in pts:
        while len(lower) >= 2 and turn(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and turn(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def verify_one(m: int) -> dict:
    if m < 12 or m % 4:
        raise ValueError("m must be a multiple of four and at least twelve")

    # t is the first rational above 1/sqrt(3) on the denominator-m^2 grid.
    q = m * m
    p = isqrt((q * q) // 3) + 1
    t = F(p, q)
    c = (1 - t * t) / (1 + t * t)
    s = 2 * t / (1 + t * t)
    if not (0 < c < F(1, 2) and s * s + c * c == 1):
        raise AssertionError("the rational direction is not in the strict-angle range")

    x, y = (F(1), F(0)), (F(0), F(1))
    v, u = (-c, -s), (-s, c)
    origin = (F(0), F(0))

    # Each face is (type, origin, first side, second side).
    faces = []
    for i in range(m):
        for j in range(m):
            o = add(scale(i, x), scale(j, v))
            faces.append(("grain1", o, x, v))
    for i in range(m):
        for j in range(m):
            o = add(scale(i, y), scale(j, u))
            faces.append(("grain2", o, y, u))
    faces.append(("interface", origin, x, y))

    vertices: set[Point] = set()
    edge_faces: dict[tuple[Point, Point], list[Point]] = {}
    opposite_pairs = []
    face_track_specs = []
    for kind, o, a, b in faces:
        oa, ob = add(o, a), add(o, b)
        oab = add(oa, b)
        face_vertices = (o, oa, oab, ob)
        vertices.update(face_vertices)
        center = ((o[0] + oa[0] + oab[0] + ob[0]) / 4,
                  (o[1] + oa[1] + oab[1] + ob[1]) / 4)
        side_a = edge(o, oa), edge(ob, oab)
        side_b = edge(o, ob), edge(oa, oab)
        opposite_pairs.extend((side_a, side_b))
        face_track_specs.append((kind, side_a[0], side_b[0]))
        for e in (side_a[0], side_a[1], side_b[0], side_b[1]):
            edge_faces.setdefault(e, []).append(center)

    if any(len(incident) not in (1, 2) for incident in edge_faces.values()):
        raise AssertionError("the complex has a dangling or overfull edge")

    dsu = DSU(edge_faces)
    for a, b in opposite_pairs:
        dsu.union(a, b)

    # Check the point set: contacts are exactly the tile edges and are triangle-free.
    ordered = sorted(vertices)
    index = {point: i for i, point in enumerate(ordered)}
    tile_edges = {tuple(sorted((index[a], index[b]))) for a, b in edge_faces}
    contact_edges = set()
    minimum = None
    diameter2 = F(0)
    for i, j in combinations(range(len(ordered)), 2):
        d2 = sqdist(ordered[i], ordered[j])
        minimum = d2 if minimum is None or d2 < minimum else minimum
        diameter2 = max(diameter2, d2)
        if d2 < 1:
            raise AssertionError("two distinct source vertices are closer than one")
        if d2 == 1:
            contact_edges.add((i, j))
    if minimum != 1 or contact_edges != tile_edges:
        raise AssertionError("unit contacts differ from the rhombic cell edges")

    adjacency = [set() for _ in ordered]
    for a, b in contact_edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    triangles = 0
    for a, b in contact_edges:
        triangles += sum(1 for z in adjacency[a] & adjacency[b] if z > a and z > b)
    if triangles:
        raise AssertionError("the unit-contact graph contains a triangle")

    # Exact train tracks: opposite edges of every face are identified.
    roots_for_face = []
    track_directions = {}
    for e in edge_faces:
        root = dsu.find(e)
        a, b = e
        direction = (b[0] - a[0], b[1] - a[1])
        if root in track_directions:
            if det(track_directions[root], direction) != 0:
                raise AssertionError("one train class contains nonparallel edges")
        else:
            track_directions[root] = direction
    for kind, ea, eb in face_track_specs:
        ra, rb = dsu.find(ea), dsu.find(eb)
        if ra == rb:
            raise AssertionError("a rhombus train crosses itself")
        roots_for_face.append((kind, ra, rb))

    tracks = set(track_directions)
    graph = {track: set() for track in tracks}
    face_pairs = set()
    for kind, a, b in roots_for_face:
        pair = tuple(sorted((a, b)))
        if pair in face_pairs:
            raise AssertionError("one pair of train tracks crosses more than once")
        face_pairs.add(pair)
        if kind != "interface":
            graph[a].add(b)
            graph[b].add(a)

    components = []
    seen = set()
    for root in tracks:
        if root in seen:
            continue
        stack, component = [root], []
        seen.add(root)
        while stack:
            here = stack.pop()
            component.append(here)
            for neighbor in graph[here]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        components.append(component)
    if sorted(map(len, components)) != [2 * m, 2 * m]:
        raise AssertionError("Section-50 deletion did not leave two 2m-track components")
    if len(tracks) != 4 * m or any(len(graph[z]) != m for z in tracks):
        raise AssertionError("post-deletion degree or train count is wrong")
    by_kind = {kind: 0 for kind in ("grain1", "grain2", "interface")}
    for kind, _, _ in roots_for_face:
        by_kind[kind] += 1
    if by_kind != {"grain1": m * m, "grain2": m * m, "interface": 1}:
        raise AssertionError("physical crossing inventory changed")

    # Sum determinants over all unordered train pairs; physical faces and missing
    # pairs are kept separate, as required by the Section-26.4 identity.
    all_determinants = F(0)
    for a, b in combinations(tracks, 2):
        all_determinants += abs(det(track_directions[a], track_directions[b]))
    physical_determinants = F(0)
    for a, b in face_pairs:
        physical_determinants += abs(det(track_directions[a], track_directions[b]))
    virtual_determinants = all_determinants - physical_determinants
    cross_total = 2 * (1 + c) * m * m
    cross_virtual = cross_total - 1
    if all_determinants != 2 * m * m * (s + 1 + c):
        raise AssertionError("zonotope determinant sum does not match its formula")
    if physical_determinants != 2 * s * m * m + 1:
        raise AssertionError("physical rhombus determinant sum does not match its formula")
    if virtual_determinants != cross_virtual:
        raise AssertionError("virtual mass is not exactly the cross-component remainder")

    # Convexification area and the sum of exact support depths of boundary edges.
    h = hull(vertices)
    twice_area = sum(h[i][0] * h[(i + 1) % len(h)][1]
                     - h[i][1] * h[(i + 1) % len(h)][0] for i in range(len(h)))
    hull_area = twice_area / 2
    expected_hull_area = (1 + 2 * s) * m * m
    physical_area = 2 * s * m * m + 1
    convexification = hull_area - physical_area
    if len(h) != 6 or hull_area != expected_hull_area or convexification != m * m - 1:
        raise AssertionError("convex hull or convexification ledger changed")

    support_depth = F(0)
    boundary_count = 0
    for e, incident in edge_faces.items():
        if len(incident) != 1:
            continue
        boundary_count += 1
        a, b = e
        midpoint = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        dx, dy = b[0] - a[0], b[1] - a[1]
        normal = (dy, -dx)  # boundary edges have unit length
        center = incident[0]
        if dot(normal, (center[0] - midpoint[0], center[1] - midpoint[1])) > 0:
            normal = (-normal[0], -normal[1])
        support = max(dot(normal, p0) for p0 in vertices)
        support_depth += support - dot(normal, midpoint)
    expected_support_depth = (4 + 2 * c) * m * m - 2
    if boundary_count != 8 * m or support_depth != expected_support_depth:
        raise AssertionError("boundary length or support-depth sum changed")
    turning = support_depth - 2 * convexification
    if turning != cross_total:
        raise AssertionError("support turning does not equal the cross determinant sum")

    # Keep the triangular reference area and boundary allowance in Q(sqrt(3)),
    # then decide both the proposed payment inequality and shell-upper control
    # with exact rational sign comparisons.
    face_excess_a = 2 * s * m * m + 1
    face_excess_b = -(F(m * m) + F(1, 2))
    endpoint_a = 2 * (convexification + face_excess_a)
    endpoint_b = 2 * face_excess_b
    if (endpoint_a, endpoint_b) != (2 * (1 + 2 * s) * m * m, F(-(2 * m * m + 1))):
        raise AssertionError("shell endpoint does not equal 2(G+E)")
    payment_residual_a = cross_virtual - 1 - endpoint_a
    payment_residual_b = -endpoint_b - 4 * m
    if not positive_quadratic_surd(payment_residual_a, payment_residual_b):
        raise AssertionError("the displayed scalar payment counterexample failed")
    shell_margin_a = convexification + face_excess_a
    shell_margin_b = face_excess_b - 2 * m
    if not positive_quadratic_surd(shell_margin_a, shell_margin_b):
        raise AssertionError("the disk did not violate the global-minimizer shell upper bound")

    # Section 50.1 with eta=1/2 and lambda=1/4: D<4m makes every post-cut
    # degree m survive pruning. The m-by-m PC1 grids have d=m/4-2>0, while
    # |U+V|<=m<=D, so their PC1 excess is exactly zero.
    if not (m * m <= diameter2 < 16 * m * m):
        raise AssertionError("diameter bounds needed for the pruning check failed")
    trim = m // 4
    trim_depth = trim - 2
    if trim_depth <= 0:
        raise AssertionError("the PC1 trim depth is not positive")
    if m - 2 * trim != m // 2:
        raise AssertionError("trimmed shore size changed")

    return {
        "m": m,
        "rational_t": f"{t.numerator}/{t.denominator}",
        "cos_theta": f"{c.numerator}/{c.denominator}",
        "sin_theta": f"{s.numerator}/{s.denominator}",
        "vertex_count": len(vertices),
        "edge_count": len(edge_faces),
        "rhombi": len(faces),
        "boundary_edges": boundary_count,
        "euler_characteristic": len(vertices) - len(edge_faces) + len(faces),
        "diameter_squared": f"{diameter2.numerator}/{diameter2.denominator}",
        "train_count": len(tracks),
        "retained_component_sizes": sorted(map(len, components)),
        "minimum_degree_after_interface_deletion": min(map(len, graph.values())),
        "internal_crossings_per_component": m * m,
        "deleted_high_defect_interface_crossings": 1,
        "trim_depth_d": trim_depth,
        "trimmed_shore_size_per_family": m // 2,
        "pc1_diagonal_excess": 0,
        "physical_determinant_mass": f"{physical_determinants.numerator}/{physical_determinants.denominator}",
        "total_cross_component_determinant": f"{cross_total.numerator}/{cross_total.denominator}",
        "cross_component_virtual_determinant": f"{cross_virtual.numerator}/{cross_virtual.denominator}",
        "total_virtual_determinant_mass": f"{virtual_determinants.numerator}/{virtual_determinants.denominator}",
        "hull_area": f"{hull_area.numerator}/{hull_area.denominator}",
        "convexification_G": f"{convexification.numerator}/{convexification.denominator}",
        "support_depth_H": f"{support_depth.numerator}/{support_depth.denominator}",
        "support_turning_J": f"{turning.numerator}/{turning.denominator}",
        "face_area_excess_E": quadratic_surd_text(face_excess_a, face_excess_b),
        "scalar_payment_residual": quadratic_surd_text(payment_residual_a, payment_residual_b),
        "scalar_payment_rule_fails_exactly": True,
        "global_shell_upper_margin": quadratic_surd_text(shell_margin_a, shell_margin_b),
        "global_shell_upper_violated": True,
        "J_equals_total_cross_determinant": turning == cross_total,
        "J_equals_V_plus_deleted_interface_area": turning == cross_virtual + 1,
        "minimum_squared_separation": str(minimum),
        "unit_contact_edges": len(contact_edges),
        "unit_contact_triangles": triangles,
    }


def main() -> None:
    cases = [verify_one(m) for m in (12, 16, 20)]
    print(json.dumps({
        "status": "PASS: exact rational scalable two-grain disk ledger",
        "arithmetic": "fractions.Fraction and integer arithmetic; no floating-point geometry",
        "family": "two m-by-m strict-rhombic grids joined to one square interface",
        "parametric_identities": {
            "R": "2 m^2 + 1",
            "B": "8 m",
            "train_count": "4 m",
            "retained_components": "two copies of K_(m,m), after deleting one interface edge",
            "cross_determinant_total": "2 (1+c) m^2",
            "cross_virtual_determinant": "2 (1+c) m^2 - 1",
            "convexification_G": "m^2 - 1",
            "support_depth_H": "(4+2c) m^2 - 2",
            "support_turning_J": "2 (1+c) m^2",
            "pc1_depth": "m/4 - 2 > 0 for m>=12 divisible by four",
            "pc1_diameter_excess": "0",
        },
        "shell_ledger": {
            "face_excess_E": "2 m^2 (s-sqrt(3)/2) + 1-sqrt(3)/2",
            "exact_cancellation": "H-J=2G",
            "net_endpoint_quantity": "2E+H-J=2(G+E)=2(1+2s-sqrt(3))m^2-sqrt(3)",
            "virtual_minus_net_endpoint": "2(c-2s+sqrt(3))m^2+sqrt(3)-1 = m^2+O(1)",
            "lifecycle": "geometric regression only; not a global minimizer or endpoint obstruction",
        },
        "cases": cases,
    }, sort_keys=True, indent=2))


main()
