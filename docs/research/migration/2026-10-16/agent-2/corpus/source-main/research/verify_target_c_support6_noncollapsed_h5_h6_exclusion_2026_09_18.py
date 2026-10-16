#!/usr/bin/env python3
"""Exact finite companion for the noncollapsed support-six exclusion.

The H5 step is the analytic cone/force-gap argument in the companion note. This
script reruns the exact H6 finite check and records the conservative counts. It
does not use floating point and does not certify the collapsed branch away.
"""

import contextlib
import importlib.util
import io
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "research" / "verify_target_c_support6_reciprocal_h6_exclusion_2026_09_18.py"
spec = importlib.util.spec_from_file_location("h6_exclusion", source)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(module)

# Reconstruct the exact finite counts rather than trusting printed output.
uniform = module.enumerate_uniform_extensions()
uniform_hull = [
    a for a in uniform
    if all(1 <= module.insertion_index(a, i) <= 4 for i in module.HULL)
]
uniform_survivors = [
    survivor
    for a in uniform
    for survivor in module.consistent_uniform_signings(a)
]
walls = module.simple_collinearity_walls(uniform)
wall_hull = walls
wall_survivors = [
    survivor
    for j, a, _b in walls
    for survivor in module.consistent_wall_signings(j, a)
]

assert len(uniform) == 26
assert len(uniform_hull) == 26
assert len(uniform_survivors) == 0
assert len(walls) == 14
assert len(wall_hull) == 0 or len(wall_survivors) == 0
assert len(wall_survivors) == 0

print("uniform_extensions", len(uniform))
print("uniform_insertion_types", len(uniform_hull))
print("uniform_sign_survivors", len(uniform_survivors))
print("simple_collinearity_walls", len(walls))
print("collinear_sign_survivors", len(wall_survivors))
print("PASS: noncollapsed H6 necessary sign/order branch is empty")
