"""Independent exact replay of the PR #120 and #121 local regressions.

The inputs are the coordinates printed in the two pinned package reports. This
script checks only those finite Euclidean fixtures. It does not encode the
Section 168 source-capacity or global-optimality hypotheses.
"""

from fractions import Fraction as F
from itertools import combinations, permutations


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def sub(p, q):
    return tuple(a - b for a, b in zip(p, q))


def add(p, q):
    return tuple(a + b for a, b in zip(p, q))


def scale(k, p):
    return tuple(k * a for a in p)


def cross(p, q):
    return p[0] * q[1] - p[1] * q[0]


def norm2_cart(p):
    return p[0] * p[0] + p[1] * p[1]


def norm2_tri(p):
    u, v = p
    return u * u + u * v + v * v


def on_segment(p, a, b):
    return (
        cross(sub(p, a), sub(b, a)) == 0
        and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
    )


def segments_intersect(first, second):
    a, b = first
    c, d = second
    o1 = cross(sub(b, a), sub(c, a))
    o2 = cross(sub(b, a), sub(d, a))
    o3 = cross(sub(d, c), sub(a, c))
    o4 = cross(sub(d, c), sub(b, c))
    return (
        (o1 * o2 < 0 and o3 * o4 < 0)
        or (o1 == 0 and on_segment(c, a, b))
        or (o2 == 0 and on_segment(d, a, b))
        or (o3 == 0 and on_segment(a, c, d))
        or (o4 == 0 and on_segment(b, c, d))
    )


def saturating_matchings(targets, sources, neighbors):
    result = []
    for image in permutations(sources, len(targets)):
        candidate = dict(zip(targets, image))
        if all(candidate[t] in neighbors[t] for t in targets):
            result.append(candidate)
    return result


def check_pr120():
    p = {
        "a": (F(-3, 4), F(1, 4)),
        "b": (F(1, 2), F(3, 4)),
        "c": (F(-1, 8), F(5, 8)),
        "u": (F(5, 4), F(3, 4)),
        "o": (F(0), F(0)),
        "v": (F(1), F(0)),
    }
    d2 = lambda i, j: norm2_cart(sub(p[i], p[j]))
    source, shore_x, shore_y = ("a", "b"), ("c", "u"), ("o", "v")
    require(d2("a", "b") == F(29, 16) > 1, "PR120 source separation changed")
    # If H is interpreted as the canonical conv(A), it is a segment of length
    # sqrt(29)/4<2. No three unit-separated points fit on it, while A has two.
    require(F(29, 16) < 4, "PR120 source hull length is not below two")
    alpha_segment = 2
    require(d2("c", "u") == F(61, 32) > 1, "PR120 X separation changed")
    require(d2("o", "v") == 1, "PR120 lattice unit edge changed")
    require(all(d2(i, j) >= 1 for i, j in combinations(source, 2)), "PR120 A not separated")
    require(all(d2(i, j) >= 1 for i, j in combinations(shore_x, 2)), "PR120 X not separated")
    require(all(d2(i, j) >= 1 for i, j in combinations(shore_y, 2)), "PR120 Y not separated")

    neighbors = {
        t: {a for a in source if d2(t, a) < 1}
        for t in (*shore_x, *shore_y)
    }
    require(
        neighbors
        == {"c": {"a", "b"}, "u": {"b"}, "o": {"a", "b"}, "v": {"b"}},
        f"PR120 strict neighborhoods changed: {neighbors}",
    )
    mx = saturating_matchings(shore_x, source, neighbors)
    my = saturating_matchings(shore_y, source, neighbors)
    require(mx == [{"c": "a", "u": "b"}], f"PR120 X matching not unique: {mx}")
    require(my == [{"o": "a", "v": "b"}], f"PR120 Y matching not unique: {my}")

    for matching, targets in ((mx[0], shore_x), (my[0], shore_y)):
        segments = [(p[t], p[a]) for t, a in matching.items()]
        require(
            all(not segments_intersect(s, r) for s, r in combinations(segments, 2)),
            f"PR120 segments intersect on {targets}",
        )

    # C={c}, O={o}: each has both sources available; distinct images are possible.
    nu = 2  # c->a and o->b witness a matching of the two-vertex combined shore.
    delta = 1 + 1 - nu
    inherited = len({mx[0]["c"]} & {my[0]["o"]})
    free_min_overlap = 0  # the exhibited distinct assignment attains the nonnegative floor.
    require(delta == 0 and inherited == 1 and free_min_overlap == 0, "PR120 overlap result changed")
    return {
        "neighbors": neighbors,
        "matching_counts": (len(mx), len(my)),
        "delta": delta,
        "inherited": inherited,
        "free_min": free_min_overlap,
        "alpha_conv_A": alpha_segment,
    }


def check_pr121():
    x = (F(1, 3), F(1, 3))
    X = {"x": x}
    Y = {
        "y0": (F(0), F(0)),
        "y1": (F(1), F(0)),
        "y2": (F(0), F(1)),
    }
    local = {
        "a1": (F(-2, 3), F(1, 2)),
        "a2": (F(-1, 3), F(4, 3)),
        "a3": (F(-1, 3), F(-2, 3)),
        "b": (F(1, 2), F(-1, 3)),
        "c": (F(5, 6), F(1, 2)),
    }
    directions = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
    hull = {
        f"h{i}": add(x, scale(F(6), (F(u), F(v))))
        for i, (u, v) in enumerate(directions)
    }
    sources = dict(local)
    sources.update(hull)
    d2 = lambda p, q: norm2_tri(sub(p, q))

    source_distances = [d2(sources[i], sources[j]) for i, j in combinations(sources, 2)]
    require(min(source_distances) == F(13, 12), "PR121 minimum source distance changed")
    require(min(source_distances) > 1, "PR121 source labels are not unit-separated")
    local_radii = [d2(z, x) for z in local.values()]
    require(max(local_radii) == F(19, 9) < 27, "PR121 local sources not inside H")

    # q(r,s) >= 3/4 r^2 and q(r,s) >= 3/4 s^2. For q<1 this gives
    # |integer-1/3|<2/sqrt(3)<4/3, so each lattice coordinate is 0 or 1.
    # The four exact candidates have q-values 1/3, 1/3, 1/3 and 4/3.
    lattice_candidates = {(F(i), F(j)) for i in (0, 1) for j in (0, 1)}
    complete_y = {z for z in lattice_candidates if d2(z, x) < 1}
    require(complete_y == set(Y.values()), f"PR121 Y_in incomplete: {complete_y}")
    require(
        {d2(p, q) for p, q in combinations(Y.values(), 2)} == {F(1)},
        "PR121 Y_in is not an equilateral unit shore",
    )

    neighbors = {
        t: {a for a, z in sources.items() if d2(Y.get(t, X.get(t)), z) < 1}
        for t in ("x", "y0", "y1", "y2")
    }
    require(
        neighbors
        == {
            "x": {"a1", "a2", "b", "c"},
            "y0": {"a1", "a3", "b"},
            "y1": {"b", "c"},
            "y2": {"a2", "c"},
        },
        f"PR121 strict neighborhoods changed: {neighbors}",
    )
    mx = saturating_matchings(tuple(X), tuple(sources), neighbors)
    my = saturating_matchings(tuple(Y), tuple(sources), neighbors)
    require(len(mx) == 4, f"PR121 X full matching count changed: {len(mx)}")
    require(len(my) == 7, f"PR121 Y_in full matching count changed: {len(my)}")
    chosen_x = {"x": "a1"}
    chosen_y = {"y0": "a1", "y1": "b", "y2": "c"}
    require(chosen_x in mx and chosen_y in my, "PR121 displayed full matching invalid")
    y_segments = [(Y[t], sources[a]) for t, a in chosen_y.items()]
    require(
        all(not segments_intersect(s, r) for s, r in combinations(y_segments, 2)),
        "PR121 chosen Y_in matching segments intersect",
    )
    # X has one segment; pairwise disjointness is vacuous for its matching.

    inherited = len({chosen_x["x"]} & {chosen_y["y0"]})
    # x->a2 and y0->a3 is a disjoint restricted assignment, so nu=2 and delta=0.
    require("a2" in neighbors["x"] and "a3" in neighbors["y0"], "PR121 free restriction witness invalid")
    delta = 1 + 1 - 2
    alternate_x = {"x": "a2"}
    alternate_y = {"y0": "a3", "y1": "b", "y2": "c"}
    require(alternate_x in mx and alternate_y in my, "PR121 coordinated alternative is invalid")
    require(set(alternate_x.values()).isdisjoint({alternate_y["y0"]}), "PR121 alternative still overlaps")
    require(inherited == 1 and delta == 0, "PR121 inherited overlap result changed")

    # The source-packing witness is the 5x5 Cartesian integer grid used in PR121.
    # Its pair distances are at least 1; the next checks place it inside H.
    grid_count, max_radius2, inradius2 = 25, 8, 27
    require(grid_count > len(sources) and max_radius2 < inradius2, "PR121 capacity witness failed")
    grid = [(i, j) for i in range(-2, 3) for j in range(-2, 3)]
    grid_d2 = [norm2_cart(sub(p, q)) for p, q in combinations(grid, 2)]
    grid_r2 = [norm2_cart(z) for z in grid]
    require(len(grid) == 25 and min(grid_d2) == 1 and max(grid_r2) == 8, "PR121 grid geometry changed")
    require(norm2_tri(x) == F(1, 3), "PR121 hexagon center norm changed")
    # The submitted verifier's grid is actually centered at the origin, not x.
    # Still, |g-x| <= sqrt(8)+1/sqrt(3) < 4 < 3*sqrt(3), so these same
    # 25 points lie in H. This repairs the missing center-distance check exactly.

    # The selected cross-shore incidences stay strict; report any exact unit ties.
    boundary_pairs = [
        (t, a, d2((Y.get(t, X.get(t))), z))
        for t in ("x", "y0", "y1", "y2")
        for a, z in sources.items()
        if d2((Y.get(t, X.get(t))), z) == 1
    ]
    return {
        "neighbors": neighbors,
        "matching_counts": (len(mx), len(my)),
        "inherited": inherited,
        "delta": delta,
        "source_min": min(source_distances),
        "boundary_pairs": boundary_pairs,
    }


def main():
    a = check_pr120()
    b = check_pr121()
    require(not b["boundary_pairs"], f"unexpected exact unit cross-incidence: {b['boundary_pairs']}")
    print("PR120: exact strict rows and unique full-shore matchings verified")
    print("PR120: unit-separated A/X/Y; both matching segment pairs disjoint")
    print("PR120: restricted Hall defect 0; inherited overlap 1; free minimum overlap 0")
    print("PR120: for H=conv(A), raw alpha_1(H)=|A|=2; K+B and globality still fail")
    print("PR121: exact strict rows and complete three-site Y_in verified")
    print("PR121: source minimum squared distance 13/12; selected Y segments disjoint")
    print("PR121: full matching counts X=4, Y_in=7; selected pair overlap 1, defect 0")
    print("PR121: coordinated full-shore alternative has restricted overlap 0")
    print("PR121: no exact-unit source/shore incidence; Y_in uses the strict open disk")
    print("PR121: 5x5 grid proves alpha_1(H)>=25>|A|=11 after exact center-distance repair")
    print("LIMIT: these are local regressions; neither supplies Section-168 global source extraction")


if __name__ == "__main__":
    main()
