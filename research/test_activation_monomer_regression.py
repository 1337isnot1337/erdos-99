"""Regression tests for the exact activation/monomer construction."""

from __future__ import annotations

import unittest

from research.activation_monomer_regression import (
    activation_order,
    active_pairs,
    declared_monomer_vertices,
    distance2,
    final_patch,
    lattice_conflict_neighborhood,
    natural_scaffold_matching,
    points_at_step,
    unit_pairs,
)


class ActivationMonomerRegressionTests(unittest.TestCase):
    def test_every_state_is_unit_separated_with_fixed_diameter(self) -> None:
        for side in range(2, 10):
            order = activation_order(side)
            diameter2 = 64 * side * side
            for completed in range(len(order) + 1):
                points = points_at_step(side, completed)
                labels = sorted(points)
                distances = [
                    distance2(points[a], points[b])
                    for index, a in enumerate(labels)
                    for b in labels[index + 1 :]
                ]
                self.assertGreaterEqual(min(distances), 1)
                self.assertEqual(max(distances), diameter2)

    def test_each_move_preserves_old_pairs_and_creates_one_contact(self) -> None:
        for side in range(2, 10):
            order = activation_order(side)
            previous_points = points_at_step(side, 0)
            previous_active = active_pairs(previous_points, side)
            for completed, moved in enumerate(order, start=1):
                # The point about to move is strict in the current state.
                self.assertFalse(
                    any(moved in pair for pair in previous_active),
                    (side, completed, moved),
                )
                current_points = points_at_step(side, completed)
                current_active = active_pairs(current_points, side)
                self.assertTrue(previous_active <= current_active)
                new_pairs = current_active - previous_active
                self.assertEqual(len(new_pairs), 1)
                new_pair = next(iter(new_pairs))
                self.assertIn(moved, new_pair)
                self.assertEqual(
                    distance2(current_points[new_pair[0]], current_points[new_pair[1]]),
                    1,
                )
                previous_points = current_points
                previous_active = current_active

    def test_final_unit_graph_is_disjoint_row_paths(self) -> None:
        for side in range(2, 16):
            points = final_patch(side)
            expected = {
                tuple(sorted((("p", i, j), ("p", i + 1, j))))
                for j in range(side)
                for i in range(side - 1)
            }
            self.assertEqual(unit_pairs(points), frozenset(expected))
            self.assertEqual(len(expected), side * (side - 1))

    def test_every_patch_point_has_its_exact_monomer_neighborhood(self) -> None:
        for side in range(2, 20):
            points = final_patch(side)
            for j in range(side):
                for i in range(side):
                    self.assertEqual(
                        lattice_conflict_neighborhood(points[("p", i, j)]),
                        declared_monomer_vertices(i, j),
                    )

    def test_monomer_neighborhoods_persist_through_activation(self) -> None:
        for side in range(2, 9):
            for completed in range(len(activation_order(side)) + 1):
                points = points_at_step(side, completed)
                for j in range(side):
                    for i in range(side):
                        self.assertEqual(
                            lattice_conflict_neighborhood(points[("p", i, j)]),
                            declared_monomer_vertices(i, j),
                        )

    def test_natural_scaffold_matching_saturates_the_patch(self) -> None:
        for side in range(2, 20):
            points = final_patch(side)
            matching = natural_scaffold_matching(side)
            self.assertEqual(len(matching), side * side)
            self.assertEqual(len(set(matching.values())), side * side)
            for label, vertex in matching.items():
                self.assertIn(vertex, lattice_conflict_neighborhood(points[label]))


if __name__ == "__main__":
    unittest.main()
