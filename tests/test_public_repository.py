import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_repo
from triangular_lattice import enumerate_minimum


class PublicRepositoryTests(unittest.TestCase):
    def test_repository_metadata_and_local_links(self):
        self.assertEqual(check_repo.validate(), [])

    def test_lattice_baseline_matches_exact_replay(self):
        baseline = json.loads((ROOT / "research/triangular-lattice-baseline.json").read_text())
        replay = [enumerate_minimum(n) for n in range(2, 6)]
        self.assertEqual(replay, baseline)

    def test_lattice_distance_is_integer_and_symmetric(self):
        from triangular_lattice import distance_squared

        points = ((0, 0), (1, 0), (0, 1), (-1, 1), (2, -1))
        for p in points:
            for q in points:
                self.assertIsInstance(distance_squared(p, q), int)
                self.assertEqual(distance_squared(p, q), distance_squared(q, p))
                if p != q:
                    self.assertGreaterEqual(distance_squared(p, q), 1)


if __name__ == "__main__":
    unittest.main()
