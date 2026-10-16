"""Regression tests for strict coverage of scaffold cells by their blocker."""

import unittest
from fractions import Fraction

from cell_union_certificate import (
    cell_union_lattice_points,
    cell_union_lattice_sites,
    dimer_center_certificate,
    free_lattice_sinks,
    free_lattice_sites,
    free_sink_hall_lower_bound,
    lattice_points_in_convex_hull,
    monomer_centroid_certificate,
    strictly_covers_convex_cell,
)
from scaffold_cells import Cell, Triangle, plus_rectangle


class CellUnionCertificateTests(unittest.TestCase):
    def test_monomer_centroid_strictly_covers_its_cell(self) -> None:
        self.assertEqual(monomer_centroid_certificate(), Fraction(2, 3))

    def test_dimer_center_strictly_covers_its_cell(self) -> None:
        self.assertEqual(dimer_center_certificate(), Fraction(1, 4))

    def test_equality_is_not_promoted_to_strict_coverage(self) -> None:
        vertices = tuple(
            (Fraction(first), Fraction(second))
            for first, second in ((0, 0), (1, 0), (0, 1))
        )
        self.assertFalse(
            strictly_covers_convex_cell((Fraction(0), Fraction(0)), vertices)
        )

    def test_lattice_trace_of_cell_union_is_its_vertex_union(self) -> None:
        cells = (Cell.monomer(Triangle("+", 0, 0)),)
        self.assertEqual(
            cell_union_lattice_sites(cells),
            frozenset({(0, 0), (1, 0), (0, 1)}),
        )

    def test_free_lattice_sites_are_degree_zero_hall_witnesses(self) -> None:
        cells = plus_rectangle(3)
        ambient = {(i, j) for i in range(4) for j in range(4)}
        free = free_lattice_sites(cells, ambient)
        self.assertEqual(free, frozenset({(3, 3)}))
        self.assertEqual(free_sink_hall_lower_bound(cells, ambient), 1)

    def test_elementary_cells_have_only_their_declared_lattice_vertices(self) -> None:
        triangle = tuple(
            (Fraction(first), Fraction(second))
            for first, second in ((0, 0), (1, 0), (0, 1))
        )
        lozenge = tuple(
            (Fraction(first), Fraction(second))
            for first, second in ((0, 0), (1, 0), (0, 1), (1, 1))
        )
        self.assertEqual(set(lattice_points_in_convex_hull(triangle)), set(triangle))
        self.assertEqual(set(lattice_points_in_convex_hull(lozenge)), set(lozenge))

    def test_generic_cell_union_and_free_sinks_are_exact(self) -> None:
        triangle = tuple(
            (Fraction(first), Fraction(second))
            for first, second in ((0, 0), (1, 0), (0, 1))
        )
        lozenge = tuple(
            (Fraction(first), Fraction(second))
            for first, second in ((1, 1), (2, 1), (1, 2), (2, 2))
        )
        self.assertEqual(
            set(cell_union_lattice_points((triangle, lozenge))),
            {
                (Fraction(0), Fraction(0)),
                (Fraction(1), Fraction(0)),
                (Fraction(0), Fraction(1)),
                (Fraction(1), Fraction(1)),
                (Fraction(2), Fraction(1)),
                (Fraction(1), Fraction(2)),
                (Fraction(2), Fraction(2)),
            },
        )
        inner = (
            (Fraction(first), Fraction(second))
            for first in range(3)
            for second in range(3)
        )
        self.assertEqual(
            set(free_lattice_sinks(inner, (triangle, lozenge))),
            {(Fraction(0), Fraction(2)), (Fraction(2), Fraction(0))},
        )


if __name__ == "__main__":
    unittest.main()
