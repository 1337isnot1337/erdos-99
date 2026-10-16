#!/usr/bin/env python3
"""Executable repair shim for the generic H7b law-of-sines certificate.

The original law-of-sines verifier imports the historical full-angle verifier directly.
That historical file has a one-site force-cycle dispatch bug and therefore raises before
the law-of-sines certificate payload is checked.  This shim redirects that dependency to
the already-committed repaired full-angle shim and otherwise executes the law-of-sines
verifier unchanged.
"""
from pathlib import Path

p = Path(__file__).with_name(
    "verify_target_c_support7_h7b_law_of_sines_2026_09_19.py"
)
src = p.read_text(encoding="utf-8")
old = "base = runpy.run_path(str(Path(__file__).with_name('verify_target_c_support7_h7b_full_angle_reduction_2026_09_19.py')))"
new = (
    "repair = runpy.run_path(str(Path(__file__).with_name('verify_target_c_support7_h7b_full_angle_reduction_repaired_2026_09_19.py')))\n"
    "base = repair['ns']"
)
assert src.count(old) == 1, "expected exactly one historical dependency dispatch"
assert src.count(new) == 0, "law-of-sines verifier already appears repaired"
patched = src.replace(old, new)
assert patched.count(old) == 0 and patched.count(new) == 1

ns = {"__name__": "__main__", "__file__": str(p)}
exec(compile(patched, str(p) + "[dependency-repair]", "exec"), ns)
