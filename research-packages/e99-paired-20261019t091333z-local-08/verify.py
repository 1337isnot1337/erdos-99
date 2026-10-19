"""Hash-check the exact destination inputs and replay the frozen finite verifier."""
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "docs/reports/target_c_rigid_cycle_pinned_stress_and_arc_stars_slot02_2026-10-10.md":
        "a3c36980e3710fc84b318a90a987aaf98940a6384a7e6681cfc60d3b6e4be783",
    "research/verify_target_c_rigid_cycle_pinned_stress_2026_10_10.py":
        "c6e8793f9a06cd0d3c337c537ca04dc4d75173a92eb98c16329f2a374d212302",
    "research/target_c_rigid_cycle_pinned_stress_certificate_2026_10_10.json":
        "6d620fe5baa1a27fccdd34dffddb16cd33e984faeaa44d1cd58d18f5842b41cf",
    "research/verify_target_c_quarter_fold_face_obstructions_2026_10_10.py":
        "ced2ae1bb3ee3834f0a36d5869d25c7aedc0e447df2c8bb17013cf1d4a0a7d89",
    "research/verify_target_c_deep_face_transport_2026_10_10.py":
        "53cfc3d7ec915b5a5b903580f64b936473b5c86c1f223b8f0d23cef1a097cc7c",
}

# With no positive bar from T to W, the equilibrium and edge-length conditions
# are vacuous, while the free point can move and the unrelated pin stays fixed.
free_q, free_r = (0, 0), (1, 0)
pin_q = pin_r = (5, 0)
edges_q = edges_r = []
assert edges_q == edges_r and pin_q == pin_r and free_q != free_r

for relative, expected in EXPECTED.items():
    actual = sha256((ROOT / relative).read_bytes()).hexdigest()
    assert actual == expected, (relative, actual, expected)

sys.path.insert(0, str(ROOT / "research"))
captured = StringIO()
with redirect_stdout(captured):
    runpy.run_path(
        str(ROOT / "research/verify_target_c_rigid_cycle_pinned_stress_2026_10_10.py"),
        run_name="__main__",
    )
actual_output = captured.getvalue().encode()
certificate = (ROOT / "research/target_c_rigid_cycle_pinned_stress_certificate_2026_10_10.json").read_bytes()
assert actual_output == certificate, "destination verifier output differs from its saved certificate"

print(json.dumps({
    "destination_inputs": len(EXPECTED),
    "verifier_output_bytes": len(actual_output),
    "verifier_output_sha256": sha256(actual_output).hexdigest(),
    "saved_certificate_byte_match": True,
    "unattached_pin_wording_control": True,
}, sort_keys=True))
