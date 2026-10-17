"""Regression tests for the exact triangular-lattice scaffold audit."""

import unittest

from scaffold_cells import (
    Cell,
    Triangle,
    dimer_strip,
    dulmage_mendelsohn_core,
    full_set_deficiency,
    hall_witness,
    left_nullity,
    legal_cell_family,
    neighborhood,
    plus_rectangle,
    verify_identities,
)


class ScaffoldCellIdentityTests(unittest.TestCase):
    def test_plus_phase_is_legal_and_hall_neutral(self) -> None:
        for side in range(1, 9):
            cells = plus_rectangle(side)
            self.assertTrue(legal_cell_family(cells))
            summary = verify_identities(cells)
            self.assertTrue(summary["identities_agree"])
            self.assertEqual(summary["left_nullity"], 0)

    def test_dimer_strip_identity(self) -> None:
        for length in range(1, 12):
            cells = dimer_strip(length)
            summary = verify_identities(cells)
            self.assertTrue(summary["identities_agree"])
            self.assertEqual(summary["left_nullity"], 0)

    def test_overlapping_cells_are_rejected(self) -> None:
        first = Cell.monomer(Triangle("+", 0, 0))
        second = Cell.monomer(Triangle("+", 0, 0))
        self.assertFalse(legal_cell_family((first, second)))

    def test_one_cell_has_no_left_deficiency(self) -> None:
        cell = Cell.monomer(Triangle("+", 0, 0))
        self.assertEqual(full_set_deficiency((cell,)), -2)
        self.assertEqual(left_nullity((cell,)), 0)

    def test_hall_witness_can_hide_inside_negative_total_charge(self) -> None:
        # The first thirteen monomers form a compact deficient core.  The remote
        # monomer supplies three fresh lattice vertices, so the full selected
        # family has negative raw deficiency even though the core still has
        # positive transversal nullity.
        core_ids = (
            ("-", -1, -1),
            ("+", -1, 0),
            ("-", -1, 0),
            ("+", -1, 1),
            ("-", -1, 1),
            ("+", 0, -1),
            ("-", 0, -1),
            ("+", 0, 0),
            ("-", 0, 0),
            ("+", 0, 1),
            ("+", 1, -1),
            ("-", 1, -1),
            ("+", 1, 0),
        )
        core = tuple(
            Cell.monomer(Triangle(orientation, i, j))
            for orientation, i, j in core_ids
        )
        cells = core + (Cell.monomer(Triangle("+", 4, 4)),)

        self.assertTrue(legal_cell_family(cells))
        summary = verify_identities(cells)
        self.assertEqual(summary["full_deficiency"], -1)
        self.assertEqual(summary["left_nullity"], 1)

        witness = hall_witness(cells)
        witness_cells = tuple(cells[index] for index in witness["cells"])
        self.assertEqual(witness["deficiency"], 1)
        self.assertEqual(witness["vertices"], tuple(sorted(neighborhood(witness_cells))))

    def test_dm_core_is_empty_for_the_two_neutral_phases(self) -> None:
        for cells in (plus_rectangle(8), dimer_strip(11)):
            decomposition = dulmage_mendelsohn_core(cells)
            self.assertEqual(decomposition["deficiency"], 0)
            self.assertEqual(decomposition["cells"], ())
            self.assertEqual(decomposition["vertices"], ())
            self.assertEqual(decomposition["components"], ())

    def test_dm_core_removes_remote_low_charge_cells(self) -> None:
        core_ids = (
            ("-", -1, -1),
            ("+", -1, 0),
            ("-", -1, 0),
            ("+", -1, 1),
            ("-", -1, 1),
            ("+", 0, -1),
            ("-", 0, -1),
            ("+", 0, 0),
            ("-", 0, 0),
            ("+", 0, 1),
            ("+", 1, -1),
            ("-", 1, -1),
            ("+", 1, 0),
        )
        core = tuple(
            Cell.monomer(Triangle(orientation, i, j))
            for orientation, i, j in core_ids
        )
        cells = core + (Cell.monomer(Triangle("+", 4, 4)),)

        decomposition = dulmage_mendelsohn_core(cells)
        self.assertEqual(decomposition["deficiency"], 1)
        self.assertEqual(decomposition["cells"], tuple(range(13)))
        self.assertEqual(len(decomposition["components"]), 1)
        component = decomposition["components"][0]
        self.assertEqual(component["cells"], tuple(range(13)))
        self.assertEqual(component["deficiency"], 1)
        self.assertEqual(component["roots"], decomposition["roots"])

    def test_dm_component_deficiencies_add_for_disconnected_cores(self) -> None:
        core_ids = (
            ("-", -1, -1),
            ("+", -1, 0),
            ("-", -1, 0),
            ("+", -1, 1),
            ("-", -1, 1),
            ("+", 0, -1),
            ("-", 0, -1),
            ("+", 0, 0),
            ("-", 0, 0),
            ("+", 0, 1),
            ("+", 1, -1),
            ("-", 1, -1),
            ("+", 1, 0),
        )
        first = tuple(
            Cell.monomer(Triangle(orientation, i, j))
            for orientation, i, j in core_ids
        )
        second = tuple(
            Cell.monomer(Triangle(orientation, i + 20, j + 20))
            for orientation, i, j in core_ids
        )
        cells = first + second
        decomposition = dulmage_mendelsohn_core(cells)
        self.assertEqual(decomposition["deficiency"], 2)
        self.assertEqual(len(decomposition["components"]), 2)
        self.assertEqual(
            [component["deficiency"] for component in decomposition["components"]],
            [1, 1],
        )
        self.assertEqual(
            sum(component["deficiency"] for component in decomposition["components"]),
            decomposition["deficiency"],
        )


if __name__ == "__main__":
    unittest.main()
