#!/usr/bin/env python3
"""Exact sharded closure of the sixth nullity-four order-2 (3,2,2,1) support class.

This wrapper reuses the exact shard-E enumeration engine. The new support has
the same verified global metadata and the same exact three-shard census. The
engine still recomputes the support orbit, touched blocks, admissible
singletons, generalized weights, relation rows, and rank increments from
TARGET before checking those expected values.
"""
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
PARENT = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_order2_shard_e_closure_2026_09_24.py"
spec = importlib.util.spec_from_file_location("eight_k5_p3_m4_3221_order2f_parent", PARENT)
V = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(V)

V.TARGET = (
    (1, 2, 3, 4),
    (1, 2, 3, 5),
    (1, 2, 4, 6),
    (3, 5, 6, 7),
)

if __name__ == "__main__":
    V.main()
