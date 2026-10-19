"""Exact relative-boundary accounting for a slit in an embedded rhombic annulus."""

from collections import Counter, defaultdict, deque


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def edge(a, b):
    return tuple(sorted((a, b)))


def cell_vertices(cell, side=None, slit_vertices=frozenset()):
    i, j = cell
    raw = ((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1))
    return tuple(
        (x, y, side if (x, y) in slit_vertices else "")
        for x, y in raw
    )


def boundary_components(boundary_edges):
    adjacency = defaultdict(set)
    for a, b in boundary_edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    require(
        all(len(neighbors) == 2 for neighbors in adjacency.values()),
        "boundary is not a disjoint union of cycles",
    )
    component_of = {}
    component = 0
    for start in adjacency:
        if start in component_of:
            continue
        component += 1
        component_of[start] = component
        queue = deque([start])
        while queue:
            here = queue.popleft()
            for nxt in adjacency[here]:
                if nxt not in component_of:
                    component_of[nxt] = component
                    queue.append(nxt)
    return component, component_of


def counts(cells, slit=None):
    """Count unit rhombi; `slit` is a simple proper path of internal edges."""
    cells = tuple(cells)
    require(len(set(cells)) == len(cells), "duplicate face")
    slit = tuple(slit or ())
    slit_vertices = frozenset(v for ab in slit for v in ab)
    if slit:
        require(
            all(slit[i][1] == slit[i + 1][0] for i in range(len(slit) - 1)),
            "slit edges are not consecutive",
        )
        path_vertices = (slit[0][0],) + tuple(b for _, b in slit)
        require(
            len(set(path_vertices)) == len(slit) + 1,
            "slit is not a simple path",
        )

    face_sides = {}
    incidence = Counter()
    vertices = set()
    for face in cells:
        i, _ = face
        side = "L" if i < 3 else "R"
        face_sides[face] = side
        cycle = cell_vertices(face, side, slit_vertices)
        vertices.update(cycle)
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            incidence[edge(a, b)] += 1

    require(
        all(multiplicity in (1, 2) for multiplicity in incidence.values()),
        "an edge has invalid face incidence",
    )
    boundary = {e for e, multiplicity in incidence.items() if multiplicity == 1}
    boundary_count, boundary_vertex_component = boundary_components(boundary)

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
    components = len({find(v) for v in vertices})
    face_count = len(cells)
    edge_count = len(incidence)
    chi = len(vertices) - edge_count + face_count
    holes = components - chi

    return {
        "V": len(vertices),
        "M": edge_count,
        "R": face_count,
        "B": len(boundary),
        "chi": chi,
        "components": components,
        "holes": holes,
        "boundary_components": boundary_count,
        "boundary_vertex_component": boundary_vertex_component,
        "edge_incidence": incidence,
    }


def main():
    # Coordinate squares map to rhombi by u=(1,0), v=(1/2,sqrt(3)/2):
    # u.u=v.v=1 and u.v=1/2. Remove the central 2x2 block from a 6x6 patch.
    annulus = tuple(
        (i, j)
        for i in range(6)
        for j in range(6)
        if not (2 <= i < 4 and 2 <= j < 4)
    )

    # Two internal unit edges join the outer and inner boundary cycles.
    slit = (((3, 0), (3, 1)), ((3, 1), (3, 2)))
    before = counts(annulus)
    after = counts(annulus, slit)
    ell = len(slit)

    require(before["R"] == 32, "annulus face count")
    require(
        (before["V"], before["M"], before["B"], before["chi"],
         before["components"], before["holes"], before["boundary_components"])
        == (48, 80, 32, 0, 1, 1, 2),
        "pre-cut annulus topology/counts",
    )
    require(
        (after["V"], after["M"], after["R"], after["B"], after["chi"],
         after["components"], after["holes"], after["boundary_components"])
        == (51, 82, 32, 36, 1, 1, 0, 1),
        "cut-open disk topology/counts",
    )
    require(after["R"] == before["R"], "cut must retain all rhombi")
    require(after["V"] - before["V"] == ell + 1, "slit vertex-copy count")
    require(after["M"] - before["M"] == ell, "slit edge-copy count")
    require(after["B"] - before["B"] == 2 * ell, "both slit banks enter relative B")
    require(after["chi"] - before["chi"] == 1, "one proper annular slit raises chi by one")

    # The path must be properly embedded: its ends lie on different old boundary cycles,
    # while every slit edge is an old two-face edge.
    c_before = before["boundary_vertex_component"]
    require(c_before[(3, 0, "")] != c_before[(3, 2, "")], "slit endpoints on distinct boundaries")
    for a, b in slit:
        old_edge = edge((a[0], a[1], ""), (b[0], b[1], ""))
        require(
            before["edge_incidence"][old_edge] == 2,
            "slit edge must be internal before cutting",
        )
        for side in ("L", "R"):
            bank = edge((a[0], a[1], side), (b[0], b[1], side))
            require(
                after["edge_incidence"][bank] == 1,
                "each bank of every slit edge is a relative boundary edge",
            )

    # Keep t fixed: it counts original source labels outside the original complex.
    # The same identity must hold with any such outside-label count.
    t = 0
    tau_before = t + before["chi"] - 1
    tau_after = t + after["chi"] - 1
    bracket_before = before["B"] + 2 * tau_before
    bracket_after = after["B"] + 2 * tau_after
    require((tau_before, tau_after) == (-1, 0), "annular hole correction is retained")
    require(bracket_before == 30 and bracket_after == 36, "relative shell brackets")
    formal_n_before = before["R"] + before["B"] // 2 + before["chi"] + t
    formal_n_after = after["R"] + after["B"] // 2 + after["chi"] + t
    require(formal_n_before == before["V"] + t, "pre-cut source-count identity")
    require(
        bracket_before == 2 * (formal_n_before - 1 - before["R"]),
        "pre-cut shell bracket equals 2*(n-1-R)",
    )
    require(
        bracket_after == 2 * (formal_n_after - 1 - after["R"]),
        "post-cut relative bracket equals 2*(formal n-1-R)",
    )
    require(
        formal_n_after - formal_n_before == ell + 1,
        "cut cell count includes duplicated vertices, not new source labels",
    )
    same_source_t = t - (ell + 1)
    require(same_source_t == -3, "fixture exposes the invalid outside-label adjustment")
    same_source_bracket = after["B"] + 2 * (
        same_source_t + after["chi"] - 1
    )
    require(
        same_source_bracket == bracket_before,
        "forcing the original formal n cancels the relative slit increment",
    )
    for outside_labels in (0, 2, 7):
        old = before["B"] + 2 * (outside_labels + before["chi"] - 1)
        new = after["B"] + 2 * (outside_labels + after["chi"] - 1)
        require(new - old == 2 * ell + 2, "outside-label term cancels in the delta")

    # The separate-interface and cut-boundary ledgers are alternatives. Combining
    # them double counts the two boundary banks; edge-only payment misses the +2.
    interface_occurrences = 2 * ell
    split_ledger = bracket_before + interface_occurrences + 2
    double_counted_ledger = bracket_after + interface_occurrences
    edge_only_ledger = bracket_before + interface_occurrences
    require(split_ledger == bracket_after, "single-charge gluing ledger")
    require(
        double_counted_ledger - bracket_after == interface_occurrences,
        "double-count control detects the full duplicated interface length",
    )
    require(
        bracket_after - edge_only_ledger == 2,
        "edge-only interface payment leaves one slit/Euler unit",
    )

    print("PASS: exact cut/gluing count on the embedded 6x6-minus-2x2 rhombic annulus")
    print(
        "before: "
        f"V={before['V']} M={before['M']} R={before['R']} B={before['B']} "
        f"chi={before['chi']} k={before['components']} h={before['holes']} "
        f"boundary_components={before['boundary_components']} tau={tau_before} "
        f"bracket={bracket_before}"
    )
    print(
        "after:  "
        f"V={after['V']} M={after['M']} R={after['R']} B={after['B']} "
        f"chi={after['chi']} k={after['components']} h={after['holes']} "
        f"boundary_components={after['boundary_components']} tau={tau_after} "
        f"bracket={bracket_after}"
    )
    print(
        f"slit: ell={ell}, delta_B={after['B']-before['B']}, "
        f"delta_chi={after['chi']-before['chi']}, "
        f"delta_bracket={bracket_after-bracket_before}=2*(ell+1)"
    )
    print(
        "controls: each deleted edge contributes its two boundary occurrences once; "
        "edge-only payment leaves +2; adding the interface again double counts it"
    )
    print(
        "source-count control: fixed t raises formal n by ell+1; forcing fixed n "
        f"would require t'={same_source_t}, which is not an outside-label count"
    )


main()
