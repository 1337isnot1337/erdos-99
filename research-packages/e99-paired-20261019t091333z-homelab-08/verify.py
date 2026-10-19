#!/usr/bin/env python3
"""Replay PR #948 finite controls against every pinned destination input."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = Path(__file__).resolve().parent
SOURCES = json.loads((PACKAGE / "SOURCES.json").read_text())
BASE = SOURCES["baseline_commit"]

for source in SOURCES["inputs"]:
    rel = source["path"]
    path = ROOT / rel
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != source["sha256"]:
        raise SystemExit(f"source hash mismatch: {rel}: {actual}")
    if source.get("commit") not in (None, BASE):
        raise SystemExit(f"unexpected source commit: {rel}")

cmd = [sys.executable, "research/verify_target_c_complete_array_diameter_forest_2026_10_11.py"]
run = subprocess.run(cmd, cwd=ROOT, check=True, capture_output=True, text=True)
actual = json.loads(run.stdout)
saved = json.loads((ROOT / "research/target_c_complete_array_diameter_forest_certificate_2026_10_11.json").read_text())
if actual != saved:
    raise SystemExit("replayed finite output differs from saved certificate")

paths = (actual["rational_path_bank_U"], actual["rational_path_bank_V"])
arrays = actual["complete_array_fixtures"]
guard = actual["additive_only_odd_cycle_guardrail"]
sharp = actual["sixty_degree_sharpness"]
if [x["valid_monotone_paths"] for x in paths] != [57, 57]:
    raise SystemExit("finite path control count mismatch")
if arrays["complete_bent_unit_array_fixtures"] != 81 or arrays["full_lower_upper_pair_checks"] != 2916:
    raise SystemExit("complete-array fixture count mismatch")
if guard["actual_odd_diameter_cycle"] != [0, 4, 8] or guard["unit_contacts"] != 0:
    raise SystemExit("additive-only odd-cycle guardrail mismatch")
if sharp["window_sum_degrees"] != 60 or sharp["scaled_all_pair_squares"] != "169":
    raise SystemExit("strict-window sharpness control mismatch")

print(json.dumps({
    "exact_destination_inputs": len(SOURCES["inputs"]),
    "source_hashes": "PASS",
    "source_verifier": "PASS (exit 0; replay JSON equals saved certificate)",
    "path_fixtures_per_bank": [57, 57],
    "complete_array_fixtures": arrays["complete_bent_unit_array_fixtures"],
    "complete_array_pair_checks": arrays["full_lower_upper_pair_checks"],
    "additive_only_odd_cycle_guardrail": "PASS",
    "sixty_degree_boundary_control": "PASS",
    "scope": "finite reproducibility only; universal analytic proof remains in README",
}, indent=2, sort_keys=True))
