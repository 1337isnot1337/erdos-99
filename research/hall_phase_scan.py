#!/usr/bin/env python3
"""Exact small-patch audit for the monomer--dimer Hall scaffold.

The scanner works on a rectangular patch of the unit triangular lattice. A
cell is either one elementary triangle (a monomer) or two edge-adjacent
elementary triangles (a dimer). A packing of cells may leave triangles
unused, but no elementary triangle may be used twice.

For every cell packing in the finite patch the script computes:

* the bipartite incidence matching rank and left Hall deficiency;
* the exact integer phase charge 4*p + 3*q - 12 at lattice vertices; and
* the cell-complex boundary/Euler formula
    |S|-|N(S)| = (m3-b)/2 - chi.

The optional degree cap is the necessary geometric condition that at most five
blocker points can lie in the open unit disk about one lattice vertex. It is
not sufficient for realization by unit-separated points; the output is an
incidence regression, not a geometric certificate.

The exhaustive state space grows quickly. The 2x3 patch is a convenient
regression; larger patches can be sampled with --max-leaves.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass


Vertex = tuple[int, int]
Triangle = tuple[Vertex, Vertex, Vertex]


@dataclass(frozen=True)
class Cell:
    """One monomer or dimer and its lattice-vertex set."""

    triangles: tuple[int, ...]
    vertices: frozenset[Vertex]
    kind: str


@dataclass
class ScanResult:
    leaves: int = 0
    valid_leaves: int = 0
    truncated: bool = False
    max_left_nullity: int = -1
    max_neighborhood_deficiency: int = -1
    witness: tuple[list[Cell], int, int] | None = None
    by_cells: Counter[int] | None = None


def rectangular_triangles(width: int, height: int) -> list[Triangle]:
    """Return both elementary triangles in each axial unit parallelogram."""

    triangles: list[Triangle] = []
    for i in range(width):
        for j in range(height):
            triangles.append(((i, j), (i + 1, j), (i, j + 1)))
            triangles.append(
                ((i + 1, j), (i, j + 1), (i + 1, j + 1))
            )
    return triangles


def elementary_edges(triangle: Triangle) -> tuple[tuple[Vertex, Vertex], ...]:
    """Return undirected lattice edges of one elementary triangle."""

    a, b, c = triangle
    return tuple(
        tuple(sorted((u, v))) for u, v in ((a, b), (a, c), (b, c))
    )


def build_cells(
    triangles: list[Triangle],
) -> tuple[list[Cell], list[list[int]], dict[tuple[int, int], Cell]]:
    """Build monomers, dimer lookup, and elementary-triangle adjacency."""

    triangle_sets = [frozenset(triangle) for triangle in triangles]
    monomers = [
        Cell((index,), vertices, "M")
        for index, vertices in enumerate(triangle_sets)
    ]
    adjacent: list[list[int]] = [[] for _ in triangles]
    dimers: dict[tuple[int, int], Cell] = {}
    for left in range(len(triangles)):
        for right in range(left + 1, len(triangles)):
            if len(triangle_sets[left] & triangle_sets[right]) == 2:
                adjacent[left].append(right)
                adjacent[right].append(left)
                dimers[(left, right)] = Cell(
                    (left, right),
                    triangle_sets[left] | triangle_sets[right],
                    "D",
                )
    return monomers, adjacent, dimers


def matching_rank(cells: list[Cell]) -> int:
    """Compute the exact incidence matching rank by Kuhn augmentations."""

    right_vertices = (
        sorted(set().union(*(cell.vertices for cell in cells)))
        if cells
        else []
    )
    right_index = {vertex: index for index, vertex in enumerate(right_vertices)}
    neighborhoods = [
        {right_index[vertex] for vertex in cell.vertices} for cell in cells
    ]
    matched: dict[int, int] = {}

    def augment(left: int, seen: set[int]) -> bool:
        for right in neighborhoods[left]:
            if right in seen:
                continue
            seen.add(right)
            if right not in matched or augment(matched[right], seen):
                matched[right] = left
                return True
        return False

    order = sorted(range(len(cells)), key=lambda index: len(neighborhoods[index]))
    return sum(augment(left, set()) for left in order)


def statistics_for_triangles(
    triangles: list[Triangle],
    cells: list[Cell],
) -> tuple[int, int, int, int, int, int, int, int]:
    """Compute matching, Euler, and phase-charge statistics."""

    m3 = sum(cell.kind == "M" for cell in cells)
    m4 = sum(cell.kind == "D" for cell in cells)
    vertices = set().union(*(cell.vertices for cell in cells)) if cells else set()
    edge_multiplicity: Counter[tuple[Vertex, Vertex]] = Counter()
    selected = [
        triangle_index for cell in cells for triangle_index in cell.triangles
    ]
    for triangle_index in selected:
        edge_multiplicity.update(elementary_edges(triangles[triangle_index]))
    edge_count = len(edge_multiplicity)
    boundary = sum(value == 1 for value in edge_multiplicity.values())
    face_count = len(selected)
    chi = len(vertices) - edge_count + face_count
    rank = matching_rank(cells)

    p = Counter()
    q = Counter()
    for cell in cells:
        target = p if cell.kind == "M" else q
        for vertex in cell.vertices:
            target[vertex] += 1
    charge = sum(4 * p[vertex] + 3 * q[vertex] - 12 for vertex in vertices)
    return (
        m3,
        m4,
        len(vertices),
        edge_count,
        boundary,
        chi,
        rank,
        charge,
    )


def format_cell(cell: Cell, triangles: list[Triangle]) -> str:
    """Use orientation and an anchor vertex for compact witness output."""

    anchor = min(triangles[cell.triangles[0]])
    return f"{cell.kind}{anchor}"


def degree_five_witness() -> tuple[list[Triangle], list[Cell]]:
    """Return a fixed 4x4 incidence pattern with positive left nullity.

    This is a regression showing that the local degree-five cap alone does not
    force Hall saturation. The pattern is deliberately not advertised as a
    geometric unit-separated configuration.
    """

    triangles = rectangular_triangles(4, 4)
    omitted = {0, 5, 9, 19, 21, 31}
    cells = [
        Cell((index,), frozenset(triangle), "M")
        for index, triangle in enumerate(triangles)
        if index not in omitted
    ]
    return triangles, cells


def scan(
    width: int,
    height: int,
    degree_cap: int,
    max_leaves: int | None,
) -> tuple[ScanResult, list[Triangle]]:
    triangles = rectangular_triangles(width, height)
    monomers, adjacent, dimers = build_cells(triangles)
    triangle_vertices = [frozenset(triangle) for triangle in triangles]
    lattice_vertices = sorted(set().union(*triangle_vertices))
    vertex_index = {vertex: index for index, vertex in enumerate(lattice_vertices)}
    monomer_masks = [
        sum(1 << vertex_index[vertex] for vertex in monomer.vertices)
        for monomer in monomers
    ]
    dimer_masks = {
        key: sum(1 << vertex_index[vertex] for vertex in cell.vertices)
        for key, cell in dimers.items()
    }
    result = ScanResult(by_cells=Counter())

    def visit(mask: int, selected: list[Cell], vertex_degrees: list[int]) -> None:
        if not mask:
            if max_leaves is not None and result.leaves >= max_leaves:
                result.truncated = True
                raise StopIteration
            result.leaves += 1
            if max(vertex_degrees, default=0) > degree_cap:
                return
            result.valid_leaves += 1
            (
                m3,
                _m4,
                vertex_count,
                _edge_count,
                boundary,
                chi,
                rank,
                charge,
            ) = statistics_for_triangles(triangles, selected)
            neighborhood_deficiency = len(selected) - vertex_count
            if m3 - boundary != 2 * (neighborhood_deficiency + chi):
                raise AssertionError("cell-complex Hall formula failed")
            if charge != 12 * neighborhood_deficiency:
                raise AssertionError("phase-charge Hall formula failed")
            left_nullity = len(selected) - rank
            result.by_cells[len(selected)] += 1
            result.max_neighborhood_deficiency = max(
                result.max_neighborhood_deficiency,
                neighborhood_deficiency,
            )
            if left_nullity > result.max_left_nullity:
                result.max_left_nullity = left_nullity
                result.witness = (selected[:], vertex_count, rank)
            return

        bit = mask & -mask
        triangle_index = bit.bit_length() - 1

        # Leave the first undecided triangle unused.
        visit(mask ^ bit, selected, vertex_degrees)

        # Use it as a monomer.
        monomer_mask = monomer_masks[triangle_index]
        next_degrees = [
            degree + ((monomer_mask >> index) & 1)
            for index, degree in enumerate(vertex_degrees)
        ]
        if max(next_degrees, default=0) <= degree_cap:
            visit(mask ^ bit, selected + [monomers[triangle_index]], next_degrees)

        # Pair it with an undecided edge-adjacent triangle.
        for other in adjacent[triangle_index]:
            other_bit = 1 << other
            if not (mask & other_bit):
                continue
            key = tuple(sorted((triangle_index, other)))
            dimer = dimers[key]
            dimer_mask = dimer_masks[key]
            next_degrees = [
                degree + ((dimer_mask >> index) & 1)
                for index, degree in enumerate(vertex_degrees)
            ]
            if max(next_degrees, default=0) <= degree_cap:
                visit(
                    mask ^ bit ^ other_bit,
                    selected + [dimer],
                    next_degrees,
                )

    try:
        visit((1 << len(triangles)) - 1, [], [0] * len(lattice_vertices))
    except StopIteration:
        pass
    return result, triangles


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--width", type=int, default=2)
    parser.add_argument("--height", type=int, default=3)
    parser.add_argument("--degree-cap", type=int, default=5)
    parser.add_argument(
        "--show-degree-five-witness",
        action="store_true",
        help="print the fixed 4x4 degree-five positive-nullity regression",
    )
    parser.add_argument(
        "--max-leaves",
        type=int,
        default=None,
        help="stop before visiting more than this many terminal states",
    )
    args = parser.parse_args()
    if args.width < 1 or args.height < 1:
        parser.error("width and height must be positive")

    if args.show_degree_five_witness:
        triangles, cells = degree_five_witness()
        (
            _m3,
            _m4,
            vertex_count,
            _edge_count,
            _boundary,
            _chi,
            rank,
            _charge,
        ) = statistics_for_triangles(triangles, cells)
        degrees = Counter(
            vertex
            for cell in cells
            for vertex in cell.vertices
        )
        print(
            "fixed_witness=4x4 triangles=32 cells=26 vertices="
            f"{vertex_count} rank={rank} left_nullity={len(cells) - rank} "
            f"max_vertex_incidence={max(degrees.values())}"
        )
        return

    result, triangles = scan(
        args.width,
        args.height,
        args.degree_cap,
        args.max_leaves,
    )
    status = "truncated" if result.truncated else "complete"
    print(
        f"patch={args.width}x{args.height} "
        f"triangles={len(triangles)} status={status}"
    )
    print(
        f"leaves={result.leaves} valid_degree_leaves={result.valid_leaves} "
        f"max_left_nullity={result.max_left_nullity} "
        f"max_neighborhood_deficiency={result.max_neighborhood_deficiency}"
    )
    print("cell_count_histogram=" + repr(sorted(result.by_cells.items())))
    if result.witness is not None:
        cells, vertex_count, rank = result.witness
        print(
            f"witness_cells={len(cells)} witness_vertices={vertex_count} "
            f"witness_rank={rank}"
        )
        print(
            "witness="
            + " ".join(format_cell(cell, triangles) for cell in cells)
        )


if __name__ == "__main__":
    main()
