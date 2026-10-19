"""Exact face-incidence and Euler checks for three finite rhombic complexes."""

from collections import Counter


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def edge(a, b):
    return tuple(sorted((a, b)))


def counts(cells, outside_labels=0):
    """Count an edge-to-edge parallelogram-lattice rhombus subcomplex."""
    cells = tuple(cells)
    if len(set(cells)) != len(cells):
        raise ValueError("duplicate face")

    incidence = Counter()
    vertices = set()
    for i, j in cells:
        cycle = ((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1))
        vertices.update(cycle)
        for p, q in zip(cycle, cycle[1:] + cycle[:1]):
            incidence[edge(p, q)] += 1

    if any(multiplicity not in (1, 2) for multiplicity in incidence.values()):
        raise ValueError("edge incidence is not one or two")

    parent = {v: v for v in vertices}

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for a, b in incidence:
        union(a, b)

    faces = len(cells)
    edge_count = len(incidence)
    boundary = sum(multiplicity == 1 for multiplicity in incidence.values())
    internal = sum(multiplicity == 2 for multiplicity in incidence.values())
    components = len({find(v) for v in vertices})
    euler = len(vertices) - edge_count + faces
    holes = components - euler
    if holes < 0:
        raise AssertionError("planar Euler characteristic produced a negative hole count")
    require(4 * faces == 2 * internal + boundary, "face-edge incidence identity failed")
    require(boundary % 2 == 0, "rhombic boundary edge count must be even")

    total_labels = len(vertices) + outside_labels
    correction = outside_labels + euler - 1
    require(len(vertices) == faces + boundary // 2 + euler, "V = R + B/2 + chi failed")
    require(
        total_labels == faces + boundary // 2 + euler + outside_labels,
        "n = R + B/2 + chi + t failed",
    )
    require(
        correction == outside_labels + components - holes - 1,
        "t + chi - 1 = t + k - h - 1 failed",
    )

    return {
        "R": faces,
        "B": boundary,
        "V": len(vertices),
        "M": edge_count,
        "chi": euler,
        "k": components,
        "h": holes,
        "t": outside_labels,
        "n": total_labels,
        "correction": correction,
        "rhs_bracket": boundary + 2 * correction,
    }


def rectangle(width, height, i0=0, j0=0):
    return {
        (i, j)
        for i in range(i0, i0 + width)
        for j in range(j0, j0 + height)
    }


def expect(name, cells, expected, outside_labels=0):
    actual = counts(cells, outside_labels)
    require(actual == expected, f"{name}: expected {expected}, got {actual}")
    print(f"{name}: {actual}")
    return actual


disk = expect(
    "2x2 disk",
    rectangle(2, 2),
    {"R": 4, "B": 8, "V": 9, "M": 12, "chi": 1, "k": 1, "h": 0,
     "t": 0, "n": 9, "correction": 0, "rhs_bracket": 8},
)

annulus_cells = rectangle(4, 4) - rectangle(2, 2, 1, 1)
annulus = expect(
    "4x4 rhombic patch minus central 2x2 hole",
    annulus_cells,
    {"R": 12, "B": 24, "V": 24, "M": 36, "chi": 0, "k": 1, "h": 1,
     "t": 0, "n": 24, "correction": -1, "rhs_bracket": 22},
)

two_components = expect(
    "two vertex-disjoint single rhombi",
    {(0, 0), (5, 0)},
    {"R": 2, "B": 8, "V": 8, "M": 8, "chi": 2, "k": 2, "h": 0,
     "t": 0, "n": 8, "correction": 1, "rhs_bracket": 10},
)

annulus_with_outside = expect(
    "same annulus with two outside source labels",
    annulus_cells,
    {"R": 12, "B": 24, "V": 24, "M": 36, "chi": 0, "k": 1, "h": 1,
     "t": 2, "n": 26, "correction": 1, "rhs_bracket": 26},
    outside_labels=2,
)

# Adversarial controls: disk topology gives the wrong vertex count for both
# the annulus and the disconnected union, so the -h and +k terms are active.
require(
    annulus["V"] != annulus["R"] + annulus["B"] // 2 + 1,
    "disk-only Euler correction unexpectedly passed the annulus control",
)
require(
    two_components["V"] != two_components["R"] + two_components["B"] // 2 + 1,
    "disk-only Euler correction unexpectedly passed the disconnected control",
)
require(annulus["correction"] == -1, "hole sign was lost")
require(two_components["correction"] == 1, "extra component sign was lost")
require(annulus_with_outside["correction"] == 1, "outside-label term was lost")
print("PASS: exact face incidence, Euler, hole/component signs, and outside-label term")
