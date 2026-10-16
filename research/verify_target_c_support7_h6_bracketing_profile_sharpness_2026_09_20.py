#!/usr/bin/env python3
"""Exact bracketing-profile census and sharpness witness for generic H6 geometry.

This certificate concerns only the convex-hexagon / two-interior-point geometry
used by the fixed-state domination bracketing bound.  It does not assert that
the rational witness satisfies the separate reciprocal force/closure equations.

It proves three finite facts without floating point:
  1. one generic interior target has at most 26 half-turn bracketing profiles;
  2. imposing those profile constraints does not lower the hull-hull support
     maximum 74 from the earlier independent-bracketing relaxation;
  3. a strict rational convex-hexagon geometry with two interior targets,
     no collinear triple, and 28 distinct segment lengths attains 74.  The two
     interior-root clauses add the unavoidable 8 hull-interior supports, so the
     bracketing-only 82 binary / 110 unary-plus-binary bounds are sharp.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product

HULL = tuple(range(6))
HULL_EDGES = tuple(frozenset((i, (i + 1) % 6)) for i in HULL)
OPTIONS = {
    r: tuple(edge for edge in HULL_EDGES if r not in edge)
    for r in HULL
}
assert all(len(v) == 4 for v in OPTIONS.values())


def complement_profile_ok(k):
    """Necessary half-turn consistency for one interior target.

    k[r] is the number of successive hull rays after r and before the ray
    antipodal to r.  For the pair (r, r+d), exactly one of the complementary
    directed angular arcs has length < pi.  In step-count form this is

        d <= k[r]  iff  6-d > k[r+d].
    """
    if len(k) != 6 or any(x not in (1, 2, 3, 4) for x in k):
        return False
    for r in HULL:
        for d in range(1, 6):
            s = (r + d) % 6
            if (d <= k[r]) != (6 - d > k[s]):
                return False
    return True


PROFILES = tuple(k for k in product(range(1, 5), repeat=6) if complement_profile_ok(k))
assert len(PROFILES) == 26
PROFILE_SET = set(PROFILES)


def profile_edges(k):
    """Convert half-turn counts to the six exit/bracketing hull edges."""
    assert complement_profile_ok(k)
    return {
        r: frozenset(((r + k[r]) % 6, (r + k[r] + 1) % 6))
        for r in HULL
    }


def aligned_hull_hull_pairs(r, s, edge6, edge7):
    """Count endpoint-literal pairs that fit one directed simple-cycle template."""
    assert r != s
    return sum(
        h != s and q != r and h != q
        for h in edge6
        for q in edge7
    )


def hull_hull_score(map6, map7):
    return sum(
        aligned_hull_hull_pairs(r, s, map6[r], map7[s])
        for r in HULL
        for s in HULL
        if r != s
    )


def independent_relaxation_maximum():
    """Reproduce the exact 74 upper bound over the old 4^12 relaxation."""
    maximum = -1
    for choices6 in product(range(4), repeat=6):
        map6 = {r: OPTIONS[r][choices6[r]] for r in HULL}
        total = 0
        for s in HULL:
            total += max(
                sum(
                    aligned_hull_hull_pairs(r, s, map6[r], edge7)
                    for r in HULL
                    if r != s
                )
                for edge7 in OPTIONS[s]
            )
        maximum = max(maximum, total)
    return maximum


INDEPENDENT_MAX = independent_relaxation_maximum()
assert INDEPENDENT_MAX == 74

PROFILE_SCORES = Counter(
    hull_hull_score(profile_edges(k6), profile_edges(k7))
    for k6 in PROFILES
    for k7 in PROFILES
)
PROFILE_MAX = max(PROFILE_SCORES)
assert PROFILE_MAX == 74
assert sum(PROFILE_SCORES.values()) == 26 ** 2
assert PROFILE_SCORES[74] == 6
assert max(score for score in PROFILE_SCORES if score < 74) == 69

EXTREME_BASE6 = (3, 2, 1, 1, 4, 4)
EXTREME_BASE7 = (1, 4, 4, 3, 2, 1)


def rotate_profile(k, shift):
    return tuple(k[(i - shift) % 6] for i in range(6))


extreme_pairs = {
    (k6, k7)
    for k6 in PROFILES
    for k7 in PROFILES
    if hull_hull_score(profile_edges(k6), profile_edges(k7)) == 74
}
expected_extreme_pairs = {
    (rotate_profile(EXTREME_BASE6, shift), rotate_profile(EXTREME_BASE7, shift))
    for shift in range(6)
}
assert extreme_pairs == expected_extreme_pairs


# A fully rational strict geometric witness.  Vertices 0,...,5 are the convex
# hull in counterclockwise order; 6 and 7 are strict interior targets.
POINTS = (
    (F(403, 200), F(1, 50)),
    (F(51, 50), F(99, 50)),
    (F(-41, 40), F(199, 100)),
    (F(-81, 40), F(-3, 200)),
    (F(-1), F(-401, 200)),
    (F(101, 100), F(-397, 200)),
    (F(-7, 4), F(-1, 4)),
    (F(21, 20), F(13, 20)),
)


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def cross2(a, b):
    return a[0] * b[1] - a[1] * b[0]


def orient(a, b, c):
    return cross2(sub(b, a), sub(c, a))


def dist2(a, b):
    d = sub(a, b)
    return d[0] * d[0] + d[1] * d[1]


# Strict convexity of the labelled hull and strict containment of both targets.
assert all(
    orient(POINTS[i], POINTS[(i + 1) % 6], POINTS[(i + 2) % 6]) > 0
    for i in HULL
)
for t in (6, 7):
    assert all(
        orient(POINTS[i], POINTS[(i + 1) % 6], POINTS[t]) > 0
        for i in HULL
    )

# Oriented-matroid genericity and strict segment-order genericity of the witness.
triple_dets = [
    orient(POINTS[i], POINTS[j], POINTS[k])
    for i, j, k in combinations(range(8), 3)
]
assert all(x != 0 for x in triple_dets)
segment_sq = [dist2(POINTS[i], POINTS[j]) for i, j in combinations(range(8), 2)]
assert len(segment_sq) == 28 == len(set(segment_sq))


def ray_exit(root, target):
    """Exact edge hit by the ray root -> target after it passes target.

    Solve R+s(T-R)=A+u(B-A).  Genericity gives one solution with s>1 and
    0<u<1; the corresponding hull edge is the bracketing edge.
    """
    R = POINTS[root]
    d = sub(POINTS[target], R)
    hits = []
    for i in HULL:
        j = (i + 1) % 6
        A = POINTS[i]
        e = sub(POINTS[j], A)
        den = cross2(d, e)
        if den == 0:
            continue
        ar = sub(A, R)
        s = cross2(ar, e) / den
        u = cross2(ar, d) / den
        if s > 1 and 0 < u < 1:
            hits.append((s, frozenset((i, j)), u))
    assert len(hits) == 1, (root, target, hits)
    return hits[0]


MAP6 = {r: ray_exit(r, 6)[1] for r in HULL}
MAP7 = {r: ray_exit(r, 7)[1] for r in HULL}

EXPECTED6 = {
    0: frozenset((3, 4)),
    1: frozenset((3, 4)),
    2: frozenset((3, 4)),
    3: frozenset((4, 5)),
    4: frozenset((2, 3)),
    5: frozenset((3, 4)),
}
EXPECTED7 = {
    0: frozenset((1, 2)),
    1: frozenset((0, 5)),
    2: frozenset((0, 1)),
    3: frozenset((0, 1)),
    4: frozenset((0, 1)),
    5: frozenset((0, 1)),
}
assert MAP6 == EXPECTED6
assert MAP7 == EXPECTED7


def infer_profile(edge_map):
    out = []
    for r in HULL:
        matches = [
            k for k in range(1, 5)
            if frozenset(((r + k) % 6, (r + k + 1) % 6)) == edge_map[r]
        ]
        assert len(matches) == 1
        out.append(matches[0])
    return tuple(out)


K6 = infer_profile(MAP6)
K7 = infer_profile(MAP7)
assert K6 in PROFILE_SET and K7 in PROFILE_SET

WITNESS_HULL_HULL = hull_hull_score(MAP6, MAP7)
assert WITNESS_HULL_HULL == 74 == INDEPENDENT_MAX == PROFILE_MAX

# The mutual-interior rays hit opposite boundary edges.  For root 6,target 7,
# each selected endpoint r of edge E_67 can pair with either endpoint of the
# state-specific (r,6) hull-root clause.  This gives 2*2=4 supports.  The
# symmetric root 7,target 6 clause gives another four.
E67 = ray_exit(6, 7)[1]
E76 = ray_exit(7, 6)[1]
assert E67 == frozenset((0, 1))
assert E76 == frozenset((3, 4))

HI_SUPPORTS = set()
for r in E67:
    for h in MAP6[r]:
        HI_SUPPORTS.add(("67", r, h))
for r in E76:
    for h in MAP7[r]:
        HI_SUPPORTS.add(("76", r, h))
assert len(HI_SUPPORTS) == 8

BINARY = WITNESS_HULL_HULL + len(HI_SUPPORTS)
UNARY = 14 * 2
assert BINARY == 82
assert UNARY + BINARY == 110

print("PASS: H6 bracketing-profile census and sharpness witness")
print("generic_single_target_profiles", len(PROFILES))
print("independent_relaxation_hull_hull_max", INDEPENDENT_MAX)
print("profile_restricted_hull_hull_max", PROFILE_MAX)
print("extreme_profile_pairs", len(extreme_pairs))
print("nonextreme_profile_hull_hull_max", max(score for score in PROFILE_SCORES if score < 74))
print("profile_score_histogram", dict(sorted(PROFILE_SCORES.items())))
print("witness_target6_profile", K6)
print("witness_target7_profile", K7)
print("witness_hull_hull_supports", WITNESS_HULL_HULL)
print("witness_interior_root_supports", len(HI_SUPPORTS))
print("witness_binary_supports", BINARY)
print("witness_unary_plus_binary_supports", UNARY + BINARY)
print("witness_noncollinear_triples", len(triple_dets))
print("witness_distinct_segment_lengths", len(set(segment_sq)))
print("min_abs_orientation", min(abs(x) for x in triple_dets))
