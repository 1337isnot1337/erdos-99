#!/usr/bin/env python3
"""Exact checker for the three-rhombus two-grain L disk."""

from fractions import Fraction
from itertools import combinations, product
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def norm_squared(m, n):
    return Fraction(13 * m * m + 13 * n * n + 10 * m * n, 13)


def cell_vertices(cells):
    return {(i + di, j + dj)
            for i, j in cells
            for di, dj in ((0, 0), (1, 0), (0, 1), (1, 1))}


def cell_edges(cells):
    result = set()
    for i, j in cells:
        corners = ((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1))
        for index in range(4):
            edge = tuple(sorted((corners[index], corners[(index + 1) % 4])))
            result.add(edge)
    return result


def cell_edge_occurrences(cells):
    counts = {}
    for i, j in cells:
        corners = ((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1))
        for index in range(4):
            edge = tuple(sorted((corners[index], corners[(index + 1) % 4])))
            counts[edge] = counts.get(edge, 0) + 1
    return counts


def is_disk(cells):
    if not cells:
        return False
    todo = [next(iter(cells))]
    reached = {todo[0]}
    while todo:
        i, j = todo.pop()
        for candidate in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if candidate in cells and candidate not in reached:
                reached.add(candidate)
                todo.append(candidate)
    if reached != cells:
        return False
    vertices = cell_vertices(cells)
    edges = cell_edges(cells)
    return len(vertices) - len(edges) + len(cells) == 1


def grain_endpoints(row, column):
    return {("A", row), ("B", column)}


def count_minimal_patches():
    block = sorted(product(range(2), range(2)))
    disk_count = 0
    candidate_rows = []
    mask_count = 0
    for size in range(1, len(block) + 1):
        for chosen in combinations(block, size):
            mask_count += 1
            cells = set(chosen)
            if not is_disk(cells):
                continue
            disk_count += 1
            rows = {j for i, j in cells}
            columns = {i for i, j in cells}
            if len(rows) != 2 or len(columns) != 2:
                continue
            physical = {(j, i) for i, j in cells}
            for first, second in combinations(sorted(cells), 2):
                i1, j1 = first
                i2, j2 = second
                if i1 == i2 or j1 == j2:
                    continue
                if rows != {j1, j2} or columns != {i1, i2}:
                    continue
                crossing_slots = {(j1, i2), (j2, i1)}
                interface = crossing_slots & physical
                virtual = crossing_slots - physical
                if interface and virtual:
                    candidate_rows.append({
                        "cells": [list(cell) for cell in sorted(cells)],
                        "selected_grains": [list(first), list(second)],
                        "physical_cells": len(physical),
                        "interface_physical": len(interface),
                        "virtual_crossgrain": len(virtual),
                    })
    require(mask_count == 15, "2-by-2 cell-mask domain changed")
    require(disk_count == 13, "2-by-2 disk-mask enumeration changed")
    require(candidate_rows, "no embedded two-grain witness was found")
    minimum = min(row["physical_cells"] for row in candidate_rows)
    minima = [row for row in candidate_rows if row["physical_cells"] == minimum]
    require(minimum == 3, "smallest enumerated embedded witness is not 3 rhombi")
    require(all(row["interface_physical"] == 1
                and row["virtual_crossgrain"] == 1 for row in minima),
            "minimum patches do not have the claimed (I,V)=(1,1) ledger")
    return {
        "cell_masks": mask_count,
        "disk_masks": disk_count,
        "two_grain_candidates": len(candidate_rows),
        "minimum_physical_rhombi": minimum,
        "minimum_witnesses": minima,
    }


def main():
    cells = {(0, 0), (1, 0), (0, 1)}
    vertices = cell_vertices(cells)
    tile_edges = cell_edges(cells)
    edge_occurrences = cell_edge_occurrences(cells)
    require(is_disk(cells), "the selected three-cell patch is not a disk")
    require(len(vertices) == 8, "unexpected vertex count")
    require(len(tile_edges) == 10, "unexpected tile-edge count")
    require(sum(count == 1 for count in edge_occurrences.values()) == 8,
            "the boundary does not have eight unit edges")
    require(sum(count == 2 for count in edge_occurrences.values()) == 2,
            "the two L-patch cells do not share the expected two edges")
    require(len(vertices) - len(tile_edges) + len(cells) == 1,
            "Euler characteristic is not that of a disk")

    pair_distances = {}
    for first, second in combinations(sorted(vertices), 2):
        delta = (second[0] - first[0], second[1] - first[1])
        pair_distances[(first, second)] = norm_squared(*delta)
    minimum_distance = min(pair_distances.values())
    require(minimum_distance == 1, "minimum point separation is not exactly 1")
    unit_edges = {edge for edge, distance in pair_distances.items() if distance == 1}
    require(unit_edges == tile_edges,
            "the point set has a unit contact outside or missing from the tiling")
    triangles = []
    for triple in combinations(sorted(vertices), 3):
        distances = [norm_squared(triple[j][0] - triple[i][0],
                                  triple[j][1] - triple[i][1])
                     for i, j in ((0, 1), (0, 2), (1, 2))]
        if all(distance == 1 for distance in distances):
            triangles.append(triple)
    require(not triangles, "the unit-contact graph contains a triangle")

    determinant = Fraction(12, 13)
    short_diagonal_squared = norm_squared(1, -1)
    long_diagonal_squared = norm_squared(1, 1)
    require(norm_squared(1, 0) == 1 and norm_squared(0, 1) == 1,
            "basis sides are not unit length")
    require(short_diagonal_squared == Fraction(16, 13)
            and long_diagonal_squared == Fraction(36, 13),
            "rhombus diagonal checks changed")

    physical = {(j, i) for i, j in cells}
    potential = set(product((0, 1), (0, 1)))
    virtual = potential - physical
    q1 = grain_endpoints(0, 1)
    q2 = grain_endpoints(1, 0)
    internal1 = {(0, 1)}
    internal2 = {(1, 0)}

    def is_interface(edge):
        row, column = edge
        endpoints = grain_endpoints(row, column)
        return endpoints <= q1 | q2 and (endpoints & q1) and (endpoints & q2)

    interface = {edge for edge in physical if is_interface(edge)}

    def is_inside(edge, grain):
        row, column = edge
        return grain_endpoints(row, column) <= grain

    def is_penetration(edge, grain):
        row, column = edge
        endpoints = grain_endpoints(row, column)
        return bool(endpoints & grain) and not endpoints <= grain

    x1 = {edge for edge in physical if is_penetration(edge, q1)}
    x2 = {edge for edge in physical if is_penetration(edge, q2)}
    crossgrain_slots = {edge for edge in potential if is_interface(edge)}
    virtual_crossgrain = crossgrain_slots - physical
    deleted = interface

    require(internal1 <= physical and internal2 <= physical,
            "one of the selected grain cells is not physical")
    require(internal1.isdisjoint(internal2), "internal grid edges overlap")
    require(physical == internal1 | internal2 | interface,
            "physical crossings do not partition into internal grids and interface")
    require(len(interface) == len(deleted) == 1,
            "the physical deleted interface count is not exactly one")
    require(x1 == x2 == interface, "penetration sets are not the shared edge")
    require(len(virtual) == len(virtual_crossgrain) == 1,
            "the missing cross-grain pair count is not exactly one")
    require(physical - deleted == internal1 | internal2,
            "deleting the interface does not leave exactly two grain components")

    r = len(physical)
    g = len(internal1) + len(internal2)
    i_count = len(interface)
    p1 = len(x1)
    p2 = len(x2)
    actual_interface_bound = g + max(i_count, p1, p2, p1 + p2 - i_count)
    upper_cap_bound = g + max(p1, p2, p1 + p2 - i_count)
    virtual_augmented_bound = g + i_count + len(virtual_crossgrain)
    require((r, g, i_count, p1, p2) == (3, 2, 1, 1, 1),
            "physical crossing ledger is not (R,G,I,p1,p2)=(3,2,1,1,1)")
    require(actual_interface_bound == upper_cap_bound == r,
            "the actual-interface or upper-cap formula is not saturated")
    require(virtual_augmented_bound == 4 and virtual_augmented_bound > r,
            "the virtual-mass nonpayment control did not reject the naive bound")

    total_determinant = len(potential) * determinant
    physical_area = len(physical) * determinant
    virtual_area = len(virtual) * determinant
    internal_area = g * determinant
    deleted_area = i_count * determinant
    require(total_determinant == Fraction(48, 13), "total determinant ledger changed")
    require(physical_area == Fraction(36, 13), "physical rhombus area changed")
    require(virtual_area == deleted_area == Fraction(12, 13),
            "virtual/deleted areas do not each equal 12/13")
    require(internal_area == Fraction(24, 13), "internal determinant area changed")
    require(internal_area + deleted_area + virtual_area == total_determinant,
            "determinant ledger does not balance")

    minimal = count_minimal_patches()
    print(json.dumps({
        "status": "PASS: exact finite embedded rhombic-disk regression",
        "arithmetic": "integers and fractions.Fraction only",
        "basis": {"u": [1, 0], "v": ["5/13", "12/13"]},
        "cells": [list(cell) for cell in sorted(cells)],
        "topology": {
            "vertices": len(vertices),
            "edges": len(tile_edges),
            "rhombi": len(cells),
            "euler_characteristic": len(vertices) - len(tile_edges) + len(cells),
            "boundary_unit_edges": sum(count == 1 for count in edge_occurrences.values()),
            "unit_contact_edges": len(unit_edges),
            "unit_contact_triangles": len(triangles),
        },
        "metric": {
            "minimum_squared_separation": str(minimum_distance),
            "unit_side_squared_length": "1",
            "short_diagonal_squared_length": str(short_diagonal_squared),
            "long_diagonal_squared_length": str(long_diagonal_squared),
            "acute_angle_cosine": "5/13",
            "determinant_per_unlike_train_pair": str(determinant),
        },
        "grain_ledger": {
            "Q1": ["A0", "B1"],
            "Q2": ["A1", "B0"],
            "physical_crossing_count_R": r,
            "internal_grid_count_G": g,
            "actual_physical_interface_I": i_count,
            "deleted_physical_interface_edges": len(deleted),
            "penetration_counts_X1_X2": [p1, p2],
            "virtual_crossgrain_pairs": len(virtual_crossgrain),
            "actual_interface_bound": actual_interface_bound,
            "upper_cap_bound_at_K_equal_I": upper_cap_bound,
            "bound_if_virtual_count_were_added": virtual_augmented_bound,
        },
        "area_ledger": {
            "internal": str(internal_area),
            "deleted_physical": str(deleted_area),
            "virtual": str(virtual_area),
            "physical_rhombus_area": str(physical_area),
            "total_train_pair_determinant": str(total_determinant),
        },
        "minimal_patch_enumeration": minimal,
        "limitations": [
            "finite two-direction lattice disk only",
            "one-crossing components fail asymptotic Section-50 minimum-degree and PC1 positive-depth hypotheses",
            "no source extraction, global-minimizer or shell-stability conclusion",
        ],
    }, sort_keys=True, indent=2))


main()
