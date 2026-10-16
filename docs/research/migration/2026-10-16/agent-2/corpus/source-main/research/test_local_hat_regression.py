"""Tests for the local barycentric-hat overload regression."""

import unittest
from fractions import Fraction

from local_hat_regression import (
    alternating_ray_radius,
    central_hat_mass,
    is_triangle_free,
    pairwise_distance,
    pairwise_distance_squared,
)


class LocalHatRegressionTests(unittest.TestCase):
    def test_radius_is_in_the_strict_counterexample_interval(self) -> None:
        radius = alternating_ray_radius()
        self.assertGreater(radius * radius, Fraction(1, 3))
        self.assertLess(radius, Fraction(2, 3))

    def test_points_are_unit_separated_and_triangle_free(self) -> None:
        radius = alternating_ray_radius()
        self.assertGreater(pairwise_distance_squared(radius), 1)
        self.assertGreater(pairwise_distance(radius), 1.0)
        self.assertTrue(is_triangle_free(radius))

    def test_naive_central_hat_weights_overload_one_vertex(self) -> None:
        self.assertEqual(central_hat_mass(alternating_ray_radius()), Fraction(6, 5))
        self.assertGreater(central_hat_mass(alternating_ray_radius()), 1)


if __name__ == "__main__":
    unittest.main()
