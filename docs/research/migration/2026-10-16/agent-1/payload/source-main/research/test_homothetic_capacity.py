"""Regression tests for the exact multi-layer homothetic capacity bound."""

import unittest
from fractions import Fraction

from homothetic_capacity import (
    candidate_diameter_squared,
    candidate_fits,
    candidate_size,
    extra_layers,
    original_size,
    strained_diameter_squared,
)


class HomotheticCapacityTests(unittest.TestCase):
    def test_threshold_exposes_one_complete_layer(self) -> None:
        side = 10
        strain = Fraction(1, side - 1)
        self.assertEqual(extra_layers(side, strain), 1)
        self.assertEqual(candidate_size(side, strain), 121)
        self.assertTrue(candidate_fits(side, strain))
        self.assertEqual(
            candidate_diameter_squared(side, strain),
            strained_diameter_squared(side, strain),
        )

    def test_subthreshold_strain_exposes_no_integer_layer(self) -> None:
        side = 10
        strain = Fraction(1, 20)
        self.assertEqual(extra_layers(side, strain), 0)
        self.assertEqual(candidate_size(side, strain), original_size(side))
        self.assertTrue(candidate_fits(side, strain))

    def test_multiple_layers_give_exact_quadratic_gain(self) -> None:
        side = 10
        strain = Fraction(1, 3)
        layers = extra_layers(side, strain)
        self.assertEqual(layers, 3)
        self.assertEqual(candidate_size(side, strain) - original_size(side), 69)
        self.assertTrue(candidate_fits(side, strain))

    def test_candidate_never_exceeds_strained_hull(self) -> None:
        for side in range(2, 30):
            for numerator in range(1, 16):
                strain = Fraction(numerator, 17)
                self.assertTrue(candidate_fits(side, strain))


if __name__ == "__main__":
    unittest.main()
