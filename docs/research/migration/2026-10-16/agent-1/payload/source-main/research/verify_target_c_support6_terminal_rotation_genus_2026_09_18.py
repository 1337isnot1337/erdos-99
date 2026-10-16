#!/usr/bin/env python3
"""Exact terminal-rotation check for the support-six reciprocal H5 survivors.

This is a scoped global-embedding obstruction.  For each labelled H5 sign/order
survivor, the five force directions at each of the six non-ground vertices give a
cyclic order on a terminal pentagon.  Pair the two occurrences of every non-ground
relation side with opposite boundary orientation and leave the six ground-anchor
sides on the boundary.  The resulting rotation surface is computed by exact
integer disjoint-set arithmetic.

It proves only the following conditional statement: if the twelve residual trains
were direct shared sides of the six physical bounded faces, with no intervening
corridor/extra face/overlap, the resulting planar complex would have to have genus
zero.  Every H5 survivor instead has genus 2 or 3.  A complete stopped train can be
a corridor, so this is not a canonical C-II exclusion and no metric realization is
claimed.
"""

from collections import Counter
from contextlib import redirect_stdout
from importlib.util import module_from_spec, spec_from_file_location
from io import StringIO
from itertools import combinations, permutations


SPEC = spec_from_file_location(
    "h5_reduction",
    "research/verify_target_c_support6_reciprocal_h5_reduction_2026_09_18.py",
)
H5 = module_from_spec(SPEC)
with redirect_stdout(StringIO()):
    SPEC.loader.exec_module(H5)


def unpack(candidate, wall):
    if wall:
        _target, signs, missing, edge_signs = candidate
    else:
        signs, missing, edge_signs = candidate
    return signs, missing, edge_signs


def terminal_order(signs, missing, edge_signs, face):
    """Return the unique cyclic order forced by the regular 5-tournament."""
    neighbors = [
        j
        for j in H5.V
        if j != face and H5.edge(face, j) not in missing
    ]
    assert len(neighbors) == 5
    for order in permutations(neighbors):
        good = True
        for k in range(5):
            a = order[k]
            b = order[(k + 1) % 5]
            cross = (
                (1 if edge_signs[H5.edge(face, a)] else -1)
                * (1 if edge_signs[H5.edge(face, b)] else -1)
                * H5.chi(signs, face, a, b)
            )
            if cross <= 0:
                good = False
                break
        if good:
            return order
    raise AssertionError("regular force tournament has no cyclic realization")


class DSU:
    def __init__(self, items):
        self.parent = {x: x for x in items}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.parent[b] = a


def rotation_surface(candidate, wall, cut=frozenset()):
    signs, missing, edge_signs = unpack(candidate, wall)
    orders = {
        face: terminal_order(signs, missing, edge_signs, face)
        for face in range(1, 7)
    }

    corners = {(face, k) for face in range(1, 7) for k in range(5)}
    dsu = DSU(corners)
    occurrences = {}
    for face, order in orders.items():
        for k, neighbor in enumerate(order):
            edge = H5.edge(face, neighbor)
            if neighbor != 0:
                occurrences.setdefault(edge, []).append((face, k))

    # A relation edge occurs once at each endpoint.  Opposite side vectors glue
    # start-to-end and end-to-start, which is the orientation-preserving pairing.
    assert len(occurrences) == 12
    for edge, pair in occurrences.items():
        if edge in cut:
            continue
        assert len(pair) == 2, (edge, pair)
        (face_a, slot_a), (face_b, slot_b) = pair
        dsu.union((face_a, slot_a), (face_b, (slot_b + 1) % 5)
        )
        dsu.union((face_a, (slot_a + 1) % 5), (face_b, slot_b))

    vertex_classes = {dsu.find(corner) for corner in corners}
    # Twelve internal side classes plus six unpaired anchor side classes.
    V = len(vertex_classes)
    # A cut relation pair contributes two boundary edge classes instead of one.
    E = 12 + 6 + len(cut)
    F = 6
    chi = V - E + F

    # The six anchor sides form the boundary graph after internal gluing.
    boundary_adjacency = {}
    for face, order in orders.items():
        for slot, neighbor in enumerate(order):
            if neighbor != 0 and H5.edge(face, neighbor) not in cut:
                continue
            a = dsu.find((face, slot))
            b = dsu.find((face, (slot + 1) % 5))
            boundary_adjacency.setdefault(a, []).append(b)
            boundary_adjacency.setdefault(b, []).append(a)
    assert all(len(neighbors) == 2 for neighbors in boundary_adjacency.values())

    seen = set()
    boundary_components = 0
    for start in boundary_adjacency:
        if start in seen:
            continue
        boundary_components += 1
        stack = [start]
        seen.add(start)
        while stack:
            vertex = stack.pop()
            for neighbor in boundary_adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

    assert boundary_components >= 1
    numerator = 2 - boundary_components - chi
    assert numerator >= 0 and numerator % 2 == 0
    genus = numerator // 2
    return V, boundary_components, genus, orders


def minimum_relation_cuts(candidate, wall):
    """Minimum number of relation-side pairs left unglued to reach genus zero."""
    _signs, _missing, edge_signs = unpack(candidate, wall)
    relation_edges = sorted(edge for edge in edge_signs if 0 not in edge)
    for count in range(5):
        for cut in combinations(relation_edges, count):
            if rotation_surface(candidate, wall, frozenset(cut))[2] == 0:
                return count
    raise AssertionError("more than four relation cuts would be needed")


def main():
    uniform = H5.enumerate_uniform_extensions()
    _uniform_hull, uniform_survivors = H5.uniform_survivors(uniform)
    walls = H5.enumerate_simple_walls(uniform)
    _wall_hull, wall_survivors = H5.wall_survivors(uniform, walls)

    uniform_counts = Counter(
        rotation_surface(candidate, False)[:3] for candidate in uniform_survivors
    )
    wall_counts = Counter(
        rotation_surface(candidate, True)[:3] for candidate in wall_survivors
    )

    assert sum(uniform_counts.values()) == 48
    assert sum(wall_counts.values()) == 80
    assert all(genus >= 2 for _V, _b, genus in uniform_counts)
    assert all(genus >= 2 for _V, _b, genus in wall_counts)
    assert set(genus for _V, _b, genus in uniform_counts) == {2, 3}
    assert set(genus for _V, _b, genus in wall_counts) == {2, 3}

    uniform_cut_counts = Counter(
        minimum_relation_cuts(candidate, False) for candidate in uniform_survivors
    )
    wall_cut_counts = Counter(
        minimum_relation_cuts(candidate, True) for candidate in wall_survivors
    )
    assert uniform_cut_counts == Counter({3: 30, 4: 18})
    assert wall_cut_counts == Counter({3: 44, 4: 36})

    print("uniform_terminal_rotation_survivors", sum(uniform_counts.values()))
    print("uniform_surface_types", dict(sorted(uniform_counts.items())))
    print("wall_terminal_rotation_survivors", sum(wall_counts.values()))
    print("wall_surface_types", dict(sorted(wall_counts.items())))
    print("uniform_minimum_unglued_relation_pairs", dict(sorted(uniform_cut_counts.items())))
    print("wall_minimum_unglued_relation_pairs", dict(sorted(wall_cut_counts.items())))
    print("PASS: every noncollapsed H5 direct-side rotation has genus at least two")


if __name__ == "__main__":
    main()
