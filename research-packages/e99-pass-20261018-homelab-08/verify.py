#!/usr/bin/env python3
"""Exact geometric full-shore extension regression (all distances rational)."""

from fractions import Fraction as F
from itertools import combinations


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(p, r):
    return (p[0] + r[0], p[1] + r[1])


def sub(p, r):
    return (p[0] - r[0], p[1] - r[1])


def scale(k, p):
    return (k * p[0], k * p[1])


def norm2(p):
    """Squared Euclidean norm in the triangular basis e1,e2 at 60 degrees."""
    u, v = p
    return u * u + u * v + v * v


def cart_norm2(p):
    """Squared Euclidean norm for Cartesian coordinates used by the grid witness."""
    return p[0] * p[0] + p[1] * p[1]


def conflict(p, r):
    """Section-168 strict conflict: Euclidean distance strictly below one."""
    return norm2(sub(p, r)) < 1


def cross(p, r):
    return p[0] * r[1] - p[1] * r[0]


def on_segment(p, a, b):
    return (
        cross(sub(p, a), sub(b, a)) == 0
        and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
    )


def segments_intersect(first, second):
    """Closed segment intersection; an invertible basis change preserves it."""
    a, b = first
    c, d = second
    o1 = cross(sub(b, a), sub(c, a))
    o2 = cross(sub(b, a), sub(d, a))
    o3 = cross(sub(d, c), sub(a, c))
    o4 = cross(sub(d, c), sub(b, c))
    proper = o1 * o2 < 0 and o3 * o4 < 0
    touching = (
        (o1 == 0 and on_segment(c, a, b))
        or (o2 == 0 and on_segment(d, a, b))
        or (o3 == 0 and on_segment(a, c, d))
        or (o4 == 0 and on_segment(b, c, d))
    )
    return proper or touching


def is_saturating_matching(target_names, matching, targets, sources):
    left = [left_name for left_name, _ in matching]
    right = [right_name for _, right_name in matching]
    if len(left) != len(set(left)) or set(left) != set(target_names):
        return False
    if len(right) != len(set(right)):
        return False
    return all(
        conflict(targets[left_name], sources[right_name])
        for left_name, right_name in matching
    )


def main():
    # All coordinates in the local construction use e1=(1,0),
    # e2=(1/2,sqrt(3)/2).  Thus norm2 is exact and rational.
    x = (F(1, 3), F(1, 3))
    X = {"x": x}
    Y = {
        "y0": (F(0), F(0)),
        "y1": (F(1), F(0)),
        "y2": (F(0), F(1)),
    }
    local_sources = {
        "a1": (-F(2, 3), F(1, 2)),
        "a2": (-F(1, 3), F(4, 3)),
        "a3": (-F(1, 3), -F(2, 3)),
        "b": (F(1, 2), -F(1, 3)),
        "c": (F(5, 6), F(1, 2)),
    }

    # The six radius-6 vertices form a regular hexagon in the triangular basis.
    # Its inradius is 3*sqrt(3), so the closed unit disk about x lies inside it.
    directions = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
    hull_sources = {
        f"h{i}": add(x, scale(F(6), direction))
        for i, direction in enumerate(directions)
    }
    sources = dict(local_sources)
    sources.update(hull_sources)

    source_pairs = [norm2(sub(p, r)) for p, r in combinations(sources.values(), 2)]
    require(source_pairs and min(source_pairs) == F(13, 12), "unexpected minimum source distance")
    require(min(source_pairs) > 1, "source labels are not strictly unit-separated")

    # Every local label lies inside the inscribed disk of H: its squared distance
    # from x is below 27=(3*sqrt(3))^2.  The six hull vertices are included in A,
    # so conv(A) is exactly the stated regular hexagon H.
    local_radii2 = [norm2(sub(p, x)) for p in local_sources.values()]
    require(max(local_radii2) < 27, "a local source lies outside the hexagon")
    require(F(1) < 27, "the unit disk is not contained in H")

    # Enumerate the complete shifted-lattice shore inside int(K+B), where K={x}.
    # If norm2((u,v)-x)<1, completing the square gives
    # norm2>=3/4*(u-1/3)^2 and likewise for v, so -2..2 covers every candidate.
    lattice_inside = {
        (F(u), F(v))
        for u in range(-2, 3)
        for v in range(-2, 3)
        if norm2(sub((F(u), F(v)), x)) < 1
    }
    expected_Y = set(Y.values())
    require(lattice_inside == expected_Y, "enumeration did not recover the complete Y_in")
    require(
        all(norm2(sub(p, r)) >= 1 for p, r in combinations(Y.values(), 2)),
        "Y_in is not unit-separated",
    )

    # Full-shore matchings, each saturating its complete finite shore.
    matching_X = [("x", "a1")]
    matching_Y = [("y0", "a1"), ("y1", "b"), ("y2", "c")]
    require(
        is_saturating_matching(X, matching_X, X, sources),
        "the chosen full X matching is invalid",
    )
    require(
        is_saturating_matching(Y, matching_Y, Y, sources),
        "the chosen full Y_in matching is invalid",
    )
    selected_distances2 = {
        "x-a1": norm2(sub(X["x"], sources["a1"])),
        "x-a2": norm2(sub(X["x"], sources["a2"])),
        "y0-a1": norm2(sub(Y["y0"], sources["a1"])),
        "y1-b": norm2(sub(Y["y1"], sources["b"])),
        "y2-c": norm2(sub(Y["y2"], sources["c"])),
        "y0-a3": norm2(sub(Y["y0"], sources["a3"])),
    }
    require(
        selected_distances2
        == {
            "x-a1": F(31, 36),
            "x-a2": F(7, 9),
            "y0-a1": F(13, 36),
            "y1-b": F(19, 36),
            "y2-c": F(19, 36),
            "y0-a3": F(7, 9),
        },
        "fixture incidence arithmetic changed",
    )
    Y_segments = [(Y[left], sources[right]) for left, right in matching_Y]
    require(
        all(not segments_intersect(s, t) for s, t in combinations(Y_segments, 2)),
        "matched Y_in segments are not pairwise disjoint",
    )

    # Restrict the inherited full-shore matchings to C={x}, O={y0}.
    C = {"x"}
    O = {"y0"}
    inherited_X = [(left, right) for left, right in matching_X if left in C]
    inherited_Y = [(left, right) for left, right in matching_Y if left in O]
    image_X = {right for _, right in inherited_X}
    image_Y = {right for _, right in inherited_Y}
    inherited_overlap = len(image_X & image_Y)
    require(inherited_overlap == 1, "expected inherited source-image overlap one")

    # The restricted shores nevertheless admit disjoint source labels, so their
    # minimum achievable overlap is zero.  This is a geometric realization of
    # the extension mismatch, not a reproof of the abstract Hall formula.
    joint_witness = [("x", "a2"), ("y0", "a3")]
    require(
        is_saturating_matching(C, [joint_witness[0]], X, sources),
        "restricted X alternate assignment is invalid",
    )
    require(
        is_saturating_matching(O, [joint_witness[1]], Y, sources),
        "restricted Y alternate assignment is invalid",
    )
    require(joint_witness[0][1] != joint_witness[1][1], "joint witness reuses a source")
    alternate_full_X = [("x", "a2")]
    alternate_full_Y = [("y0", "a3"), ("y1", "b"), ("y2", "c")]
    require(
        is_saturating_matching(X, alternate_full_X, X, sources)
        and is_saturating_matching(Y, alternate_full_Y, Y, sources),
        "the coordinated alternative full-shore matchings are invalid",
    )
    require(
        {right for _, right in alternate_full_X}
        .isdisjoint({right for left, right in alternate_full_Y if left in O}),
        "the coordinated full-shore pair still overlaps on C and O",
    )
    require(norm2(sub(Y["y0"], Y["y1"])) == 1, "strict-boundary control changed")
    require(not conflict(Y["y0"], Y["y1"]), "distance-one points must not conflict")
    bad_matching = [("y0", "a1"), ("y1", "a1"), ("y2", "c")]
    require(
        not is_saturating_matching(Y, bad_matching, Y, sources),
        "duplicate-source matching control was not rejected",
    )

    # Source-capacity falsification uses the Cartesian grid about the origin.
    # H is centered at x, whose Cartesian coordinates are (1/2,sqrt(3)/6).
    # For every grid point g, |g| <= sqrt(8) < 3 and |x|^2 = 1/3 < 1.
    # Thus |g-x| < 4 < 3*sqrt(3), since 16 < 27: the grid lies in H.
    # Its 25 labels exceed |A|=11, excluding the zero-slack capacity endpoint.
    grid = [(F(i), F(j)) for i in range(-2, 3) for j in range(-2, 3)]
    grid_distances2 = [cart_norm2(sub(p, r)) for p, r in combinations(grid, 2)]
    grid_radii2 = [cart_norm2(point) for point in grid]
    require(len(sources) == 11, "unexpected source count")
    require(len(grid) == 25 and len(grid) > len(sources), "capacity witness count is invalid")
    require(min(grid_distances2) >= 1, "Cartesian capacity witness is not unit-separated")
    require(max(grid_radii2) == 8, "unexpected Cartesian grid radius")
    require(norm2(x) == F(1, 3), "unexpected displacement of the hexagon center")
    require(
        max(grid_radii2) < 9 and norm2(x) < 1 and F(16) < 27,
        "triangle-inequality bound does not place the Cartesian grid in H",
    )

    print("PASS: exact rational source, response, and complete lattice incidences")
    print("PASS: |A|=11; minimum source squared distance is 13/12; A is triangle-free")
    print("PASS: K+B subset H; complete Y_in has 3 lattice sites; both full shores saturate")
    print("PASS: chosen full-shore restrictions inherit overlap 1")
    print("PASS: the restricted shores admit a joint assignment with overlap 0")
    print("PASS: a coordinated pair of full-shore matchings also removes this restriction overlap")
    print("PASS: strict-distance boundary and duplicate-source controls")
    print("LIMIT: alpha_1(H) >= 25 > |A|=11; zero-slack capacity endpoint is not realized")


main()
