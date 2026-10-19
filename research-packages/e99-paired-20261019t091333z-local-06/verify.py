#!/usr/bin/env python3
"""Check frozen artifact hashes and the finite patch-exponent ledger only."""

from fractions import Fraction
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PINS = {
    "docs/audits/target_c_global_inverse_phase_face_tail_second_referee_2026-10-10.md":
        "9ed749f51f560af597875fc9fb7c2647395ce47a970583a9e3349df6f8e2bb38",
    "docs/audits/target_c_global_inverse_phase_face_tail_exclusion_independent_audit_2026-10-09.md":
        "158394e6106e12d46cb1a404e24cfabf3df629849b2956004c2bc0a1beabed78",
    "docs/audits/target_c_referee_run_ledger_2026-10-10.md":
        "a113dd7604cad043df72e0fe29cfc8487b808acc6ce0dd86ea1d9d09859f7e7e",
}

for relative, expected in PINS.items():
    actual = sha256((ROOT / relative).read_bytes()).hexdigest()
    assert actual == expected, f"pinned source hash mismatch: {relative}"

r_exp = Fraction(3, 4)
patch_count_exp = 1 - r_exp
local_cap_term_exp = (1 + r_exp) / 3
summed_local_cap_exp = patch_count_exp + local_cap_term_exp
constant_term_exp = patch_count_exp
assert summed_local_cap_exp == Fraction(5, 6)
assert constant_term_exp == Fraction(1, 4)
assert 1 - r_exp / 1 == Fraction(1, 4)  # C_M r / D term

print({
    "status": "pins-and-exponent-controls-passed",
    "pinned_artifacts": len(PINS),
    "summed_local_capacity_exponent": str(summed_local_cap_exp),
    "summed_constant_exponent": str(constant_term_exp),
    "mathematical_proof": False,
})
