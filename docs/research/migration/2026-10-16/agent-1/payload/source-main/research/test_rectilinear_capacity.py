"""Tests for exact nonuniform rectilinear triangular-lattice capacity."""

import unittest
from fractions import Fraction

from rectilinear_capacity import (
    RectilinearPatch,
    homothetic_patch,
    point_to_cell_boundary_distance_squared,
    point_to_cell_distance_squared,
    short_diagonal_squared,
)


class RectilinearCapacityTests(unittest.TestCase):
    def test_one_direction_layer_gives_one_extra_row(self) -> None:
        patch = homothetic_patch(5, Fraction(1), Fraction(26, 20))
        self.assertEqual(patch.extra_layers_x, 0)
        self.assertEqual(patch.extra_layers_y, 1)
        self.assertEqual(patch.candidate_shape, (5, 6))
        self.assertEqual(patch.gain, 5)
        self.assertTrue(patch.candidate_fits)
        self.assertTrue(patch.candidate_is_unit_separated)

    def test_nonuniform_chain_uses_only_total_span(self) -> None:
        patch = RectilinearPatch.from_values(
            (0, Fraction(6, 5), Fraction(12, 5), Fraction(18, 5), Fraction(26, 5)),
            (0, Fraction(11, 10), Fraction(22, 10), Fraction(33, 10), Fraction(26, 5)),
        )
        self.assertEqual(patch.extra_layers_x, 1)
        self.assertEqual(patch.extra_layers_y, 1)
        self.assertEqual(patch.candidate_shape, (6, 6))
        self.assertEqual(patch.gain, 11)
        self.assertTrue(patch.candidate_fits)

    def test_homothetic_two_direction_formula(self) -> None:
        patch = homothetic_patch(10, Fraction(4, 3), Fraction(4, 3))
        self.assertEqual((patch.extra_layers_x, patch.extra_layers_y), (3, 3))
        self.assertEqual(patch.gain, 69)
        self.assertEqual(patch.candidate_size, 169)
        self.assertTrue(patch.candidate_fits)

    def test_subthreshold_spans_have_no_gain(self) -> None:
        patch = homothetic_patch(10, Fraction(21, 20), Fraction(21, 20))
        self.assertEqual((patch.extra_layers_x, patch.extra_layers_y), (0, 0))
        self.assertEqual(patch.gain, 0)
        self.assertTrue(patch.candidate_fits)

    def test_two_layer_buffer_is_not_yet_large_enough(self) -> None:
        patch = homothetic_patch(10, Fraction(10, 9), Fraction(10, 9))
        self.assertEqual((patch.extra_layers_x, patch.extra_layers_y), (1, 1))
        self.assertEqual(patch.boundary_safe_shape, (7, 7))
        self.assertEqual(patch.boundary_safe_candidate_size, 49)
        self.assertFalse(patch.boundary_safe_capacity)

    def test_four_layers_in_both_directions_exactly_clear_the_boundary_strip(self) -> None:
        patch = homothetic_patch(10, Fraction(13, 9), Fraction(13, 9))
        self.assertEqual((patch.extra_layers_x, patch.extra_layers_y), (4, 4))
        self.assertEqual(patch.boundary_safe_shape, (10, 10))
        self.assertEqual(patch.boundary_safe_candidate_size, patch.source_size)
        self.assertTrue(patch.boundary_safe_capacity)

    def test_one_sided_buffer_threshold_is_eleven_layers_at_side_ten(self) -> None:
        below = homothetic_patch(10, Fraction(1), Fraction(19, 9))
        above = homothetic_patch(10, Fraction(1), Fraction(20, 9))
        self.assertEqual(below.extra_layers_y, 10)
        self.assertEqual(above.extra_layers_y, 11)
        self.assertFalse(below.boundary_safe_capacity)
        self.assertTrue(above.boundary_safe_capacity)

    def test_many_layers_leave_a_protected_replacement_core(self) -> None:
        patch = homothetic_patch(10, Fraction(9, 5), Fraction(9, 5))
        self.assertEqual((patch.extra_layers_x, patch.extra_layers_y), (7, 7))
        self.assertEqual(patch.candidate_shape, (17, 17))
        self.assertEqual(patch.boundary_safe_shape, (13, 13))
        self.assertEqual(patch.boundary_safe_candidate_size, 169)
        self.assertTrue(patch.boundary_safe_capacity)
        self.assertTrue(patch.candidate_fits)

    def test_invalid_coordinate_gaps_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            RectilinearPatch.from_values((0, Fraction(9, 10)), (0, 1))

    def test_near_hexagonal_product_patch_strictly_covers_its_interior(self) -> None:
        patch = homothetic_patch(6, Fraction(6, 5), Fraction(6, 5))
        self.assertEqual(short_diagonal_squared(Fraction(6, 5), Fraction(6, 5)), Fraction(36, 25))
        self.assertTrue(patch.closed_unit_covering)
        self.assertTrue(patch.interior_unit_covering)

    def test_sqrt_three_gap_is_the_sharp_closed_covering_threshold(self) -> None:
        gap = Fraction(7, 5)
        patch = homothetic_patch(4, gap, gap)
        self.assertLess(short_diagonal_squared(gap, gap), 3)
        self.assertTrue(patch.interior_unit_covering)

        # The exact threshold is irrational, so use the rational pair (2, 1),
        # whose short diagonal has squared length three and whose cell contains
        # points at distance exactly one from all four corners.
        threshold = RectilinearPatch.from_values((0, 2, 4), (0, 1, 2))
        self.assertEqual(short_diagonal_squared(Fraction(2), Fraction(1)), 3)
        self.assertTrue(threshold.closed_unit_covering)
        self.assertFalse(threshold.interior_unit_covering)

    def test_large_equal_gaps_leave_an_interior_cavity(self) -> None:
        patch = homothetic_patch(3, Fraction(9, 5), Fraction(9, 5))
        self.assertGreater(short_diagonal_squared(Fraction(9, 5), Fraction(9, 5)), 3)
        self.assertFalse(patch.closed_unit_covering)
        self.assertFalse(patch.interior_unit_covering)

    def test_oblique_cell_projection_is_exact(self) -> None:
        self.assertEqual(
            point_to_cell_distance_squared(
                Fraction(3),
                Fraction(0),
                Fraction(0),
                Fraction(2),
                Fraction(0),
                Fraction(1),
            ),
            Fraction(3, 4),
        )
        self.assertEqual(
            point_to_cell_boundary_distance_squared(
                Fraction(1),
                Fraction(1, 2),
                Fraction(0),
                Fraction(2),
                Fraction(0),
                Fraction(1),
            ),
            Fraction(3, 16),
        )

    def test_bad_cell_mask_is_localized_to_large_gap_interfaces(self) -> None:
        patch = RectilinearPatch.from_values((0, 1, 3), (0, 1, 2))
        self.assertEqual(
            patch.cell_short_diagonal_squared,
            ((Fraction(1), Fraction(1)), (Fraction(3), Fraction(3))),
        )
        self.assertEqual(patch.bad_cell_indices, ((1, 0), (1, 1)))

    def test_all_good_patch_has_the_same_protected_core_as_boundary_buffer(self) -> None:
        patch = homothetic_patch(10, Fraction(13, 9), Fraction(13, 9))
        self.assertEqual(patch.bad_cell_indices, ())
        self.assertEqual(
            patch.cellwise_protected_candidate_size,
            patch.boundary_safe_candidate_size,
        )
        self.assertTrue(patch.cellwise_protected_capacity)

    def test_bad_cells_remove_nearby_candidate_sites(self) -> None:
        patch = RectilinearPatch.from_values(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11),
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
        )
        self.assertEqual(len(patch.bad_cell_indices), 9)
        self.assertLess(
            patch.cellwise_protected_candidate_size,
            patch.boundary_safe_candidate_size,
        )
        self.assertFalse(patch.cellwise_protected_capacity)

    def test_localized_bad_row_can_still_leave_full_replacement_capacity(self) -> None:
        patch = RectilinearPatch.from_values(
            (Fraction(9, 5) * index for index in range(15)),
            tuple(range(14)) + (Fraction(13) + Fraction(9, 5),),
        )
        self.assertEqual(patch.candidate_shape, (26, 15))
        self.assertEqual(len(patch.bad_cell_indices), 14)
        self.assertEqual(patch.cellwise_protected_candidate_size, 230)
        self.assertEqual(patch.source_size, 225)
        self.assertTrue(patch.candidate_fits)
        self.assertTrue(patch.cellwise_protected_capacity)


if __name__ == "__main__":
    unittest.main()
