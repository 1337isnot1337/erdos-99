"""Exact tests for the triangle-free near-hexagonal lattice regression."""

import unittest
from fractions import Fraction

from affine_lattice import AffineLattice


class AffineLatticeTests(unittest.TestCase):
    def test_minimum_distance_and_triangle_freeness(self) -> None:
        lattice = AffineLattice(Fraction(1, 100))
        for side in (2, 5, 20):
            summary = lattice.verify_patch(side)
            self.assertTrue(summary["minimum_distance_is_one"])
            self.assertEqual(summary["minimum_squared_distance"], 1)
            self.assertTrue(summary["unit_differences_are_horizontal"])
            self.assertTrue(summary["triangle_free"])

    def test_exact_diameter_formula(self) -> None:
        lattice = AffineLattice(Fraction(1, 10))
        side = 7
        scale = Fraction(11, 10)
        expected = Fraction((side - 1) ** 2) * (1 + scale + scale * scale)
        self.assertEqual(lattice.patch_squared_diameter(side), expected)
        self.assertEqual(lattice.verify_patch(side)["diameter_squared"], expected)

    def test_hexagonal_density_is_an_infimum_not_a_triangle_free_attainment(self) -> None:
        for denominator in (2, 10, 100, 1000):
            lattice = AffineLattice(Fraction(1, denominator))
            self.assertGreater(lattice.determinant_ratio_to_hexagonal, 1)
            self.assertLessEqual(
                lattice.determinant_ratio_to_hexagonal,
                Fraction(3, 2),
            )


if __name__ == "__main__":
    unittest.main()
