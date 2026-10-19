#!/usr/bin/env python3
"""Independent exact checker for the pinned finite two-grain model."""

from fractions import Fraction
from itertools import combinations, product
import json


BOX = tuple(product(range(2), repeat=2))
L_PATCH = {(0, 0), (1, 0), (0, 1)}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def vertices(cells):
    return {
        (i + di, j + dj)
        for i, j in cells
        for di, dj in ((0, 0), (1, 0), (1, 1), (0, 1))
    }


def cell_boundary_edges(cells):
    result = set()
    for i, j in cells:
        corners = ((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1))
        for a, b in zip(corners, corners[1:] + corners[:1]):
            result.add(tuple(sorted((a, b))))
    return result


def edge_multiplicities(cells):
    counts = {}
    for i, j in cells:
        corners = ((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1))
        for a, b in zip(corners, corners[1:] + corners[:1]):
            edge = tuple(sorted((a, b)))
            counts[edge] = counts.get(edge, 0) + 1
    return counts


def is_cell_disk(cells):
    if not cells:
        return False
    start = next(iter(cells))
    seen = {start}
    queue = [start]
    while queue:
        i, j = queue.pop()
        for neighbor in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if neighbor in cells and neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    if seen != cells:
        return False
    boundary = edge_multiplicities(cells)
    boundary_edges = {edge for edge, multiplicity in boundary.items() if multiplicity == 1}
    boundary_vertices = {vertex for edge in boundary_edges for vertex in edge}
    boundary_graph = {vertex: set() for vertex in boundary_vertices}
    for a, b in boundary_edges:
        boundary_graph[a].add(b)
        boundary_graph[b].add(a)
    boundary_cycle = bool(boundary_graph) and all(
        len(neighbors) == 2 for neighbors in boundary_graph.values()
    )
    if boundary_cycle:
        root = next(iter(boundary_graph))
        reached_boundary = {root}
        pending = [root]
        while pending:
            vertex = pending.pop()
            for neighbor in boundary_graph[vertex] - reached_boundary:
                reached_boundary.add(neighbor)
                pending.append(neighbor)
        boundary_cycle = reached_boundary == set(boundary_graph)
    return (
        len(vertices(cells)) - len(cell_boundary_edges(cells)) + len(cells) == 1
        and boundary_cycle
    )


def physical_slots(cells):
    # The first coordinate labels the A train and the second labels B.
    return {(j, i) for i, j in cells}


def cross_slots(first, second):
    a, b = first
    c, d = second
    return {(a, d), (c, b)}


def enumerate_masks():
    rows = []
    for size in range(1, len(BOX) + 1):
        for choice in combinations(BOX, size):
            cells = set(choice)
            if not is_cell_disk(cells):
                continue
            physical = physical_slots(cells)
            for first, second in combinations(sorted(physical), 2):
                if first[0] == second[0] or first[1] == second[1]:
                    continue
                mixed = cross_slots(first, second)
                interface = physical & mixed
                missing = mixed - physical
                if interface and missing:
                    rows.append({
                        "cells": [list(cell) for cell in sorted(cells)],
                        "grains": [list(first), list(second)],
                        "physical_count": len(physical),
                        "physical_interface_count": len(interface),
                        "virtual_crossgrain_count": len(missing),
                    })
    return rows


def q(m, n):
    return Fraction(13 * m * m + 13 * n * n + 10 * m * n, 13)


def metric_certificate():
    pts = sorted(vertices(L_PATCH))
    pairs = list(combinations(pts, 2))
    d2 = {
        pair: q(pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
        for pair in pairs
    }
    boundary = cell_boundary_edges(L_PATCH)
    contacts = {pair for pair, value in d2.items() if value == 1}
    triangle_count = sum(
        all(d2[tuple(sorted(pair))] == 1 for pair in combinations(triple, 2))
        for triple in combinations(pts, 3)
    )
    multiplicities = edge_multiplicities(L_PATCH)
    u = (Fraction(1), Fraction(0))
    v = (Fraction(5, 13), Fraction(12, 13))
    cross_determinant = u[0] * v[1] - u[1] * v[0]
    same_direction_determinants = (
        u[0] * u[1] - u[1] * u[0],
        v[0] * v[1] - v[1] * v[0],
    )
    require(len(pts) == 8, "the L patch should have eight vertices")
    require(len(boundary) == 10, "the L patch should have ten tile edges")
    require(len(d2) == 28, "all 28 distinct point pairs must be checked")
    require(min(d2.values()) == 1, "the minimum squared separation is not one")
    require(max(d2.values()) == Fraction(85, 13), "the L patch diameter changed")
    require(contacts == boundary, "the unit-contact graph differs from tile edges")
    require(triangle_count == 0, "the unit-contact graph contains a triangle")
    require(sum(value == 1 for value in multiplicities.values()) == 8,
            "the boundary should have eight unit edges")
    require(sum(value == 2 for value in multiplicities.values()) == 2,
            "the L cells should share exactly two edges")
    require(q(1, -1) == Fraction(16, 13), "the short diagonal changed")
    require(q(1, 1) == Fraction(36, 13), "the long diagonal changed")
    require(cross_determinant == Fraction(12, 13), "the unlike-train determinant changed")
    require(same_direction_determinants == (0, 0),
            "same-direction train pairs must have zero determinant")
    return {
        "vertices": len(pts),
        "point_pairs_checked": len(d2),
        "minimum_squared_separation": "1",
        "diameter_squared": str(max(d2.values())),
        "unit_contacts": len(contacts),
        "tile_boundary_edges": len(boundary),
        "unit_contact_triangles": triangle_count,
        "shared_cell_edges": sum(value == 2 for value in multiplicities.values()),
        "boundary_unit_edges": sum(value == 1 for value in multiplicities.values()),
        "rhombus_area": "12/13",
        "unlike_direction_pair_determinant": str(cross_determinant),
        "same_direction_pair_determinants": [str(value) for value in same_direction_determinants],
        "short_diagonal_squared": str(q(1, -1)),
        "long_diagonal_squared": str(q(1, 1)),
    }


def grain_ledger():
    cells = L_PATCH
    physical = physical_slots(cells)
    potential = set(product(range(2), repeat=2))
    virtual = potential - physical
    q1 = frozenset((('A', 0), ('B', 1)))
    q2 = frozenset((('A', 1), ('B', 0)))
    require(q1.isdisjoint(q2), "the selected grain labels overlap")
    internal1 = {(0, 1)}
    internal2 = {(1, 0)}
    interface_slots = cross_slots((0, 1), (1, 0))
    interface = physical & interface_slots
    deleted = set(interface)
    virtual_crossgrain = virtual & interface_slots

    def penetration(grain):
        found = set()
        for row, column in physical:
            endpoints = frozenset((('A', row), ('B', column)))
            if endpoints & grain and not endpoints <= grain:
                found.add((row, column))
        return found

    x1, x2 = penetration(q1), penetration(q2)
    require(physical == internal1 | internal2 | interface,
            "physical crossings do not partition into grids and interface")
    require(internal1.isdisjoint(internal2), "internal crossing sets overlap")
    require(len(physical) == 3 and len(internal1 | internal2) == 2,
            "physical or internal crossing count changed")
    require(interface == {(0, 0)}, "the deleted physical interface changed")
    require(deleted == interface and len(deleted) == 1,
            "the deleted-edge set does not equal the actual physical interface")
    require(virtual == virtual_crossgrain == {(1, 1)},
            "the virtual cross-grain pair was misclassified")
    require(x1 == x2 == interface, "penetration sets do not share the interface")
    require(len(x1 | x2) == 1 and len(x1) + len(x2) == 2,
            "the overlap control does not expose double use")

    R, G, I = len(physical), len(internal1) + len(internal2), len(interface)
    p1, p2 = len(x1), len(x2)
    interface_rhs = G + max(I, p1, p2, p1 + p2 - I)
    cap_rhs = G + max(p1, p2, p1 + p2 - I)
    unsupported_virtual_augmented = G + I + len(virtual_crossgrain)
    require((R, G, I, p1, p2) == (3, 2, 1, 1, 1),
            "the physical crossing ledger changed")
    require(R == G + I, "physical crossings do not equal internal plus deleted")
    require(interface_rhs == cap_rhs == R, "the interface formula is not saturated")
    require(unsupported_virtual_augmented == 4 and unsupported_virtual_augmented > R,
            "the unpaid-virtual-mass control did not distinguish four from three")

    cell_area = Fraction(12, 13)
    internal_area = G * cell_area
    deleted_area = I * cell_area
    virtual_area = len(virtual_crossgrain) * cell_area
    physical_area = R * cell_area
    potential_area = len(potential) * cell_area
    require((internal_area, deleted_area, virtual_area, physical_area, potential_area) == (
        Fraction(24, 13), Fraction(12, 13), Fraction(12, 13),
        Fraction(36, 13), Fraction(48, 13)
    ), "the exact area ledger changed")
    require(internal_area + deleted_area == physical_area,
            "physical area does not equal internal plus deleted physical area")
    require(physical_area + virtual_area == potential_area,
            "the virtual determinant area is not separate from physical area")
    return {
        "physical_crossings_R": R,
        "internal_grid_crossings_G": G,
        "deleted_physical_interface_I": I,
        "deleted_physical_interface_edges": len(deleted),
        "penetration_counts": [p1, p2],
        "penetration_union_count": len(x1 | x2),
        "virtual_crossgrain_count": len(virtual_crossgrain),
        "actual_interface_rhs": interface_rhs,
        "upper_cap_rhs_at_K_equals_I": cap_rhs,
        "rhs_if_virtual_were_added_without_payment": unsupported_virtual_augmented,
        "areas": {
            "internal": str(internal_area),
            "deleted_physical": str(deleted_area),
            "virtual": str(virtual_area),
            "physical": str(physical_area),
            "complete_potential": str(potential_area),
        },
    }


def falsification_controls():
    broken_bridge = L_PATCH - {(0, 0)}
    require(not is_cell_disk(broken_bridge),
            "removing the L bridge should disconnect the physical disk")

    full_box = set(BOX)
    full_slots = physical_slots(full_box)
    possible = set(product(range(2), repeat=2))
    require(is_cell_disk(full_box), "the completed 2-by-2 box should remain a disk")
    require(possible - full_slots == set(),
            "filling the missing corner should remove all virtual slots")

    adjacent_domino = physical_slots({(0, 0), (1, 0)})
    pairs = list(combinations(sorted(adjacent_domino), 2))
    require(len(pairs) == 1 and (
        pairs[0][0][0] == pairs[0][1][0]
        or pairs[0][0][1] == pairs[0][1][1]
    ), "an adjacent two-cell patch should share a train and cannot be two disjoint grains")

    return {
        "removing_bridge_rejected_as_disk": True,
        "filling_missing_corner_removes_virtual_slot": True,
        "adjacent_two_cell_mask_shares_train": True,
    }


def main():
    masks = [set(choice) for size in range(1, len(BOX) + 1)
             for choice in combinations(BOX, size)]
    disk_masks = [mask for mask in masks if is_cell_disk(mask)]
    candidates = enumerate_masks()
    minimum = min(row["physical_count"] for row in candidates)
    minimizers = [row for row in candidates if row["physical_count"] == minimum]
    require(len(masks) == 15, "the bounded mask domain changed")
    require(len(disk_masks) == 13, "the disk-mask count changed")
    require(len(candidates) == 4, "the admissible two-grain mask count changed")
    require(minimum == 3, "the minimum physical cell count is not three")
    require(len(minimizers) == 4, "the number of minimum masks changed")
    require(all(row["physical_interface_count"] == 1
                and row["virtual_crossgrain_count"] == 1 for row in minimizers),
            "a minimum mask has the wrong physical/virtual ledger")
    require(all(len(row["cells"]) == 3 for row in minimizers),
            "a minimum witness does not have three physical cells")
    print(json.dumps({
        "status": "PASS: independent bounded finite-model audit",
        "arithmetic": "integer and Fraction only",
        "enumeration": {
            "nonempty_masks": len(masks),
            "edge_connected_euler_one_disk_masks": len(disk_masks),
            "admissible_two_grain_masks": len(candidates),
            "minimum_physical_rhombi": minimum,
            "minimum_witnesses": minimizers,
        },
        "metric": metric_certificate(),
        "grain_ledger": grain_ledger(),
        "falsification_controls": falsification_controls(),
        "scope_limit": "2-by-2 box only; no global source or canonical Target B inference",
    }, indent=2, sort_keys=True))


main()
