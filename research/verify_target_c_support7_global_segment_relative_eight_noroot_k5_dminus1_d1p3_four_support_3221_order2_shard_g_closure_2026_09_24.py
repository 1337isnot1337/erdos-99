#!/usr/bin/env python3
"""Exact seventh order-2 closure by audited specialization of the shard-E engine."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENGINE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order2_shard_e_closure_2026_09_24.py"
source = ENGINE.read_text()

replacements = (
    (
        """TARGET = (\n    (1, 2, 3, 4),\n    (1, 2, 3, 5),\n    (1, 2, 4, 6),\n    (3, 4, 5, 7),\n)""",
        """TARGET = (\n    (1, 2, 3, 4),\n    (1, 2, 3, 5),\n    (1, 2, 6, 7),\n    (1, 4, 5, 6),\n)""",
    ),
    ("EXPECTED_GLOBAL = (2, 177, 816_480, 14)", "EXPECTED_GLOBAL = (2, 168, 816_480, 15)"),
    (
        """EXPECTED_SHARDS = {\n    (0, 59): (12_272, 331_344, 257_478, 18_116, 70),\n    (59, 118): (12_272, 331_344, 256_917, 17_084, 70),\n    (118, 177): (12_272, 331_344, 271_507, 20_396, 70),\n}""",
        """EXPECTED_SHARDS = {\n    (0, 56): (12_992, 350_784, 266_148, 13_308, 36),\n    (56, 112): (12_992, 350_784, 270_816, 13_296, 36),\n    (112, 168): (12_992, 350_784, 272_064, 13_248, 34),\n}""",
    ),
    ("EXPECTED_TOTAL = (36_816, 994_032, 785_902, 55_596)", "EXPECTED_TOTAL = (38_976, 1_052_352, 809_028, 39_852)"),
    ("assert len(admissible) == 208", "assert len(admissible) == 232"),
    ("fifth order-2 class closure", "seventh order-2 class closure"),
)
for old, new in replacements:
    assert source.count(old) == 1, old
    source = source.replace(old, new)

namespace = {"__name__": "__main__", "__file__": str(__file__)}
exec(compile(source, str(ENGINE), "exec"), namespace)
