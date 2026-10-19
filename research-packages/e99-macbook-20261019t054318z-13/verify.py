"""Independent edge-incidence controls for the PR #125 audit.

The fixtures are finite subsets of the oblique unit-rhombus tiling. This checks
the integer identities and the exact coefficient reduction; the general result
is proved in README.md.
"""

from collections import defaultdict
from fractions import Fraction


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def edge(p, q):
    return tuple(sorted((p, q)))


def rectangle(width, height, i0=0, j0=0):
    return {
        (i, j)
        for i in range(i0, i0 + width)
        for j in range(j0, j0 + height)
    }


def counts(cells, outside_labels=0):
    incidences = defaultdict(int)
    vertices = set()
    adjacency = defaultdict(set)

    for i, j in cells:
        corners = ((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1))
        vertices.update(corners)
        for p, q in zip(corners, corners[1:] + corners[:1]):
            incidences[edge(p, q)] += 1
            adjacency[p].add(q)
            adjacency[q].add(p)

    if any(m not in (1, 2) for m in incidences.values()):
        raise AssertionError("a fixture has an edge with incidence outside {1, 2}")

    seen = set()
    components = 0
    for root in vertices:
        if root in seen:
            continue
        components += 1
        seen.add(root)
        stack = [root]
        while stack:
            p = stack.pop()
            for q in adjacency[p] - seen:
                seen.add(q)
                stack.append(q)

    faces = len(cells)
    edge_count = len(incidences)
    boundary = sum(m == 1 for m in incidences.values())
    internal = sum(m == 2 for m in incidences.values())
    vertex_count = len(vertices)
    chi = vertex_count - edge_count + faces
    holes = components - chi
    labels = vertex_count + outside_labels
    correction = outside_labels + chi - 1

    require(holes >= 0, "negative bounded-complement count")
    require(4 * faces == 2 * internal + boundary, "face incidence failed")
    require(edge_count == internal + boundary, "edge partition failed")
    require(boundary % 2 == 0, "boundary-edge count must be even")
    require(chi == components - holes, "planar Euler sign failed")
    require(
        vertex_count == faces + boundary // 2 + chi,
        "V = R + B/2 + chi failed",
    )
    require(
        labels == faces + boundary // 2 + chi + outside_labels,
        "source-count identity failed",
    )
    require(
        correction == outside_labels + components - holes - 1,
        "topology correction failed",
    )

    # With a0=sqrt(3)/2, the shell coefficient is
    # sqrt(3)*(B/4 + (t+chi-1)/2). The area budget after subtracting a0*R
    # is sqrt(3)*(n-1-R)/2. Compare the rational coefficients of sqrt(3).
    shell_coefficient = Fraction(boundary, 4) + Fraction(correction, 2)
    area_budget_coefficient = Fraction(labels - 1 - faces, 2)
    require(
        shell_coefficient == area_budget_coefficient,
        "shell and area-budget coefficients differ",
    )

    return {
        "R": faces,
        "B": boundary,
        "V": vertex_count,
        "M": edge_count,
        "chi": chi,
        "k": components,
        "h": holes,
        "t": outside_labels,
        "n": labels,
        "t+chi-1": correction,
        "sqrt3_rhs_coefficient": str(shell_coefficient),
    }


disk = counts(rectangle(2, 2))
annulus_cells = rectangle(4, 4) - rectangle(2, 2, 1, 1)
annulus = counts(annulus_cells)
two_components = counts({(0, 0), (5, 0)})
outside_labels = counts(annulus_cells, outside_labels=2)

require(disk == {
    "R": 4,
    "B": 8,
    "V": 9,
    "M": 12,
    "chi": 1,
    "k": 1,
    "h": 0,
    "t": 0,
    "n": 9,
    "t+chi-1": 0,
    "sqrt3_rhs_coefficient": "2",
}, "disk control differs")
require(annulus == {
    "R": 12,
    "B": 24,
    "V": 24,
    "M": 36,
    "chi": 0,
    "k": 1,
    "h": 1,
    "t": 0,
    "n": 24,
    "t+chi-1": -1,
    "sqrt3_rhs_coefficient": "11/2",
}, "annulus control differs")
require(two_components == {
    "R": 2,
    "B": 8,
    "V": 8,
    "M": 8,
    "chi": 2,
    "k": 2,
    "h": 0,
    "t": 0,
    "n": 8,
    "t+chi-1": 1,
    "sqrt3_rhs_coefficient": "5/2",
}, "disconnected control differs")
require(outside_labels["t+chi-1"] == 1, "outside-label correction differs")
require(outside_labels["n"] == 26, "outside-label source count differs")

# The disk-only substitution chi=1 gives the wrong count on both controls.
require(
    annulus["R"] + annulus["B"] // 2 + 1 == 25 != annulus["V"],
    "annulus must reject the disk-only chi=1 formula",
)
require(
    two_components["R"] + two_components["B"] // 2 + 1
    == 7
    != two_components["V"],
    "disconnected control must reject the disk-only chi=1 formula",
)
require(
    annulus["R"] + annulus["B"] // 2 + 1 + 1 == 26 != annulus["V"],
    "annulus must reject the wrong positive-hole sign",
)

for name, result in (
    ("2x2 disk", disk),
    ("4x4 patch minus central 2x2 hole", annulus),
    ("two vertex-disjoint rhombi", two_components),
    ("annulus plus two outside labels", outside_labels),
):
    print(f"{name}: {result}")
print("PASS: incidence, Euler signs, source count, and shell coefficient controls")
