"""Replay the exact pinned finite controls and compare their saved certificate."""
from contextlib import redirect_stdout
import importlib
import io
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research"))
module = importlib.import_module("verify_target_c_deep_face_transport_2026_10_10")
replayed = io.StringIO()
with redirect_stdout(replayed):
    module.main()
expected = (ROOT / "research/target_c_deep_face_transport_certificate_2026_10_10.json").read_text(encoding="utf-8")
if replayed.getvalue() != expected:
    raise SystemExit("pinned finite replay differs from the saved certificate")
print("PASS: pinned exact finite controls reproduce the saved certificate byte-for-byte")
