"""Replay the pinned candidate verifier and compare the saved exact output."""
import hashlib
import subprocess
import sys

CERTIFICATE = "research/target_c_large_array_boundary_attachment_certificate_2026_10_11.json"
VERIFIER = "research/verify_target_c_large_array_boundary_attachment_2026_10_11.py"
EXPECTED_SHA256 = "40cbdce45f7c718d6623c97fd31643b52850d2d550d080441dd2cb393596e49d"

with open(CERTIFICATE, "rb") as source:
    expected = hashlib.sha256(source.read()).hexdigest()
if expected != EXPECTED_SHA256:
    raise SystemExit("saved certificate hash differs from the pinned destination bytes")
run = subprocess.run([sys.executable, VERIFIER], check=True, capture_output=True, text=True)
actual = hashlib.sha256(run.stdout.encode("utf-8")).hexdigest()
if actual != expected:
    raise SystemExit("replayed exact verifier output differs from the saved certificate")
print("PASS: exact verifier output matches the saved finite certificate SHA-256")
